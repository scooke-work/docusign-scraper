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
import re
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

# Tab labels that mark a multi-language code-example tab group. These are
# intentionally NOT expanded for now (see _reveal_tabs / README "Not included"):
# we keep only the default-language sample rather than every language variant.
LANGUAGE_TAB_LABELS = {
    "curl", "c#", "csharp", "java", "node", "node.js", "nodejs", "javascript",
    "js", "ts", "typescript", "php", "python", "ruby", "go", "golang", "vb",
    "vb.net", ".net", "kotlin", "swift", "objective-c", "c++", "powershell",
    "postman", "http", "shell", "bash", "json", "xml",
}


def is_language_tab_group(labels) -> bool:
    """True if a tab group's labels look like a multi-language code-example
    selector (cURL/C#/Java/…). Such groups are intentionally not expanded — we
    keep only the default-language sample. See README "Not included (by choice)".
    """
    norm = [re.sub(r"[^a-z0-9.+#-]", "", (l or "").lower()) for l in labels]
    nonempty = [x for x in norm if x]
    if len(nonempty) < 2:
        return False
    return sum(1 for x in nonempty if x in LANGUAGE_TAB_LABELS) >= max(2, len(nonempty) // 2)


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
            self._expand_disclosures(page, host)

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
        the others. We process each tablist independently: skip multi-language
        code-example groups (see ``LANGUAGE_TAB_LABELS`` — scoped out for now, we
        keep only the default-language sample), and for content tablists click
        every tab, harvest its panel, and replace the live panels with the union.
        Best-effort, bounded, no-op on pages without tabs, scoped to the dev docs.
        """
        if host != "developers.docusign.com":
            return
        try:
            n_lists = page.eval_on_selector_all("[role='tablist']", "els => els.length")
        except Exception:
            n_lists = 0
        for li in range(n_lists):
            try:
                self._reveal_one_tablist(page, li)
            except Exception:
                continue

    def _reveal_one_tablist(self, page, li: int) -> None:
        lists = page.query_selector_all("[role='tablist']")
        if li >= len(lists):
            return
        tabs = lists[li].query_selector_all("[role='tab']")
        if len(tabs) < 2:
            return
        labels = [(t.inner_text() or "").strip() for t in tabs]
        # Skip multi-language code-example tab groups (intentionally out of scope).
        if is_language_tab_group(labels):
            return

        harvested, panel_ids = [], []
        for i in range(min(len(tabs), 20)):
            lists = page.query_selector_all("[role='tablist']")
            if li >= len(lists):
                break
            tabs = lists[li].query_selector_all("[role='tab']")
            if i >= len(tabs):
                break
            try:
                tabs[i].click(timeout=2000)
            except Exception:
                continue
            page.wait_for_timeout(250)
            info = page.evaluate(
                """(tabEl) => {
                    const id = tabEl.getAttribute('aria-controls');
                    const p = id ? document.getElementById(id)
                                 : document.querySelector("[role='tabpanel']");
                    return p ? {id: p.id || '', html: p.outerHTML} : null;
                }""",
                tabs[i],
            )
            if info and info.get("html"):
                harvested.append(info["html"])
                if info.get("id"):
                    panel_ids.append(info["id"])

        if harvested:
            page.evaluate(
                """(args) => {
                    const {htmls, ids} = args;
                    let anchor = null;
                    for (const id of ids) { const p = document.getElementById(id); if (p) { anchor = p; break; } }
                    if (!anchor) anchor = document.querySelector("[role='tabpanel']");
                    const host = anchor && anchor.parentElement ? anchor.parentElement : document.body;
                    ids.forEach(id => { const p = document.getElementById(id); if (p) p.remove(); });
                    const c = document.createElement('div');
                    c.setAttribute('data-scraper-tabs', '1');
                    c.innerHTML = htmls.join('\\n');
                    host.appendChild(c);
                }""",
                {"htmls": harvested, "ids": panel_ids},
            )

    def _expand_disclosures(self, page, host: str) -> None:
        """Expand collapsed ARIA disclosures (accordions) within the content.

        API reference pages render their schema/property trees behind disclosure
        buttons (``aria-expanded='false'``); a single snapshot misses every
        collapsed field. We click them open in rounds, since expanding one node
        reveals further collapsed children, until none remain or a bound is hit.
        Language-labeled disclosures (code samples) are skipped, consistent with
        the multi-language exclusion. Best-effort, bounded, no-op when there are
        no collapsed disclosures, scoped to the developer docs.
        """
        if host != "developers.docusign.com":
            return
        for _ in range(12):  # nested schema reveals more collapsed nodes each round
            try:
                handles = page.query_selector_all("main [aria-expanded='false']")
            except Exception:
                return
            if not handles:
                return
            clicked = 0
            for h in handles[:400]:
                try:
                    first_line = ((h.inner_text() or "").strip().split("\n", 1)[0])
                    norm = re.sub(r"[^a-z0-9.+#-]", "", first_line.lower())
                    if norm in LANGUAGE_TAB_LABELS:  # skip code-sample disclosures
                        continue
                    h.click(timeout=1500)
                    clicked += 1
                except Exception:
                    continue
            page.wait_for_timeout(250)
            if clicked == 0:
                return
