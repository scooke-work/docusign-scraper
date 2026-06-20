"""Playwright-based page fetcher.

Both target sites render their content with JavaScript (the Salesforce-backed
support site returns a bare loader shell to a plain HTTP request), so we drive a
real Chromium instance and read ``page.content()`` only after the site-specific
content selector becomes visible.

The fetcher also provides:
  * an on-disk raw-HTML cache so re-runs and extractor tweaks don't re-hit the
    network;
  * polite rate limiting between navigations;
  * a bounded retry for the transient Salesforce "Sorry to interrupt / CSS Error"
    overlay.
"""

from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_fixed

from .config import Config
from .urls import canonical_url

# Per-host CSS selector that signals "real content has rendered". Used as the
# wait condition before snapshotting the DOM. Kept here (not in extractors) so
# the fetcher can wait without importing extractor logic.
CONTENT_READY_SELECTORS = {
    "developers.docusign.com": "main, article, [class*='content']",
    "support.docusign.com": "article, .slds-rich-text-editor__output, "
    "lightning-formatted-rich-text, [class*='article']",
}
DEFAULT_READY_SELECTOR = "main, article"

# Text that indicates the Salesforce Lightning shell failed to load its styles
# and is showing the interstitial instead of the article.
SALESFORCE_ERROR_MARKERS = ("Sorry to interrupt", "CSS Error")


class TransientRenderError(RuntimeError):
    """Raised when a page rendered into a known error/loader state."""


@dataclass
class FetchResult:
    """Rendered HTML plus the URL the browser actually landed on.

    ``final_url`` differs from the requested URL when the site redirects (e.g.
    ``/docs/navigator-api/`` -> ``/docs/agreement-manager-api/``). Callers should
    use ``final_url`` as the canonical identity for output and dedup so content
    is never mislabeled with the pre-redirect URL.
    """

    html: str
    final_url: str


class BrowserFetcher:
    """Context manager that owns a single Chromium browser + context."""

    def __init__(self, config: Config):
        self.config = config
        self._pw = None
        self._browser = None
        self._context = None
        self._last_nav = 0.0

    # -- lifecycle ---------------------------------------------------------
    def __enter__(self) -> "BrowserFetcher":
        from playwright.sync_api import sync_playwright

        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(headless=self.config.headless)
        self._context = self._browser.new_context(
            user_agent=self.config.user_agent,
            viewport={"width": 1280, "height": 1600},
        )
        self._context.set_default_navigation_timeout(self.config.nav_timeout_ms)
        return self

    def __exit__(self, *exc) -> None:
        for closer in (self._context, self._browser):
            try:
                if closer:
                    closer.close()
            except Exception:
                pass
        if self._pw:
            self._pw.stop()

    # -- caching -----------------------------------------------------------
    def _cache_path(self, url: str) -> Path:
        # Key on the canonical identity so all URL variants of one article
        # (and a redirect's source/target) share a single cache entry.
        digest = hashlib.sha256(canonical_url(url).encode("utf-8")).hexdigest()[:20]
        host = urlparse(url).netloc or "unknown"
        return self.config.cache_dir / host / f"{digest}.html"

    def _write_cache(self, cache_path: Path, html: str, final_url: str) -> None:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(html, encoding="utf-8")
        cache_path.with_suffix(".url").write_text(final_url, encoding="utf-8")

    # -- fetching ----------------------------------------------------------
    def fetch(self, url: str) -> FetchResult:
        """Return rendered HTML + final (post-redirect) URL for ``url``.

        Cache-first: the resolved ``final_url`` is persisted in a ``.url`` sidecar
        next to the cached HTML so redirects survive cache hits. Pre-sidecar
        caches fall back to the requested URL.
        """
        cache_path = self._cache_path(url)
        meta_path = cache_path.with_suffix(".url")
        if self.config.use_cache and cache_path.exists():
            final_url = meta_path.read_text(encoding="utf-8").strip() if meta_path.exists() else url
            return FetchResult(cache_path.read_text(encoding="utf-8"), final_url or url)

        self._respect_rate_limit()
        html, final_url = self._render(url)

        self._write_cache(cache_path, html, final_url)
        # Write-through under the redirect target's key too, so a later request
        # for the final URL is an instant hit (e.g. navigator-api -> agreement-manager-api).
        final_cache = self._cache_path(final_url)
        if final_cache != cache_path:
            self._write_cache(final_cache, html, final_url)
        return FetchResult(html, final_url)

    def _respect_rate_limit(self) -> None:
        elapsed = time.monotonic() - self._last_nav
        wait = self.config.rate_seconds - elapsed
        if wait > 0:
            time.sleep(wait)
        self._last_nav = time.monotonic()

    @retry(
        retry=retry_if_exception_type(TransientRenderError),
        stop=stop_after_attempt(3),
        wait=wait_fixed(2),
        reraise=True,
    )
    def _render(self, url: str) -> tuple[str, str]:
        host = urlparse(url).netloc
        selector = CONTENT_READY_SELECTORS.get(host, DEFAULT_READY_SELECTOR)

        page = self._context.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded")
            # Wait for real content FIRST — this resolves the moment the article
            # renders, instead of blocking on networkidle (which Lightning pages
            # frequently never reach, wasting the full timeout on every page).
            try:
                page.wait_for_selector(selector, timeout=self.config.selector_timeout_ms)
            except Exception:
                pass
            # Then a short, best-effort settle for any trailing XHR.
            try:
                page.wait_for_load_state("networkidle", timeout=self.config.idle_timeout_ms)
            except Exception:
                pass

            self._reveal_tabs(page, host)

            html = page.content()
            final_url = page.url or url
            if any(marker in html for marker in SALESFORCE_ERROR_MARKERS) and (
                "slds-rich-text" not in html and "article" not in html.lower()
            ):
                raise TransientRenderError(f"Loader/error shell still present for {url}")
            return html, final_url
        finally:
            page.close()

    def _reveal_tabs(self, page, host: str) -> None:
        """Click through ARIA tab widgets so lazy-loaded panels are captured.

        React tab components (e.g. the Agreement Manager "agreement types by
        category" tabs) render only the active panel, so a single snapshot misses
        the others. We click each tab, harvest its panel HTML, then replace the
        live panels with the union so one snapshot contains every tab's content.
        Best-effort, bounded, and a no-op on pages without tabs. Scoped to the
        developer docs, where this pattern occurs and clicking is side-effect-free.
        """
        if host != "developers.docusign.com":
            return
        try:
            tab_count = page.eval_on_selector_all("[role='tab']", "els => els.length")
        except Exception:
            tab_count = 0
        if not tab_count or tab_count < 2:
            return

        harvested = []
        for i in range(min(tab_count, 20)):
            try:
                tabs = page.query_selector_all("[role='tab']")
                if i >= len(tabs):
                    break
                tabs[i].click(timeout=2000)
                page.wait_for_timeout(300)
                panel_html = page.eval_on_selector_all(
                    "[role='tabpanel']", "els => els.map(e => e.outerHTML).join('')"
                )
                if panel_html:
                    harvested.append(panel_html)
            except Exception:
                continue

        if harvested:
            try:
                page.evaluate(
                    """(htmls) => {
                        const anchor = document.querySelector("[role='tabpanel']");
                        const host = anchor && anchor.parentElement
                            ? anchor.parentElement
                            : (document.querySelector('main') || document.body);
                        document.querySelectorAll("[role='tabpanel']").forEach(p => p.remove());
                        const c = document.createElement('div');
                        c.setAttribute('data-scraper-tabs', '1');
                        c.innerHTML = htmls.join('\\n');
                        host.appendChild(c);
                    }""",
                    harvested,
                )
            except Exception:
                pass
