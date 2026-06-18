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
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_fixed

from .config import Config

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
        digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:20]
        host = urlparse(url).netloc or "unknown"
        return self.config.cache_dir / host / f"{digest}.html"

    # -- fetching ----------------------------------------------------------
    def fetch(self, url: str) -> str:
        """Return rendered HTML for ``url`` (cache-first)."""
        cache_path = self._cache_path(url)
        if self.config.use_cache and cache_path.exists():
            return cache_path.read_text(encoding="utf-8")

        self._respect_rate_limit()
        html = self._render(url)

        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(html, encoding="utf-8")
        return html

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
    def _render(self, url: str) -> str:
        host = urlparse(url).netloc
        selector = CONTENT_READY_SELECTORS.get(host, DEFAULT_READY_SELECTOR)

        page = self._context.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded")
            # Let XHR/Lightning data settle, then wait for real content.
            try:
                page.wait_for_load_state("networkidle", timeout=self.config.selector_timeout_ms)
            except Exception:
                pass  # networkidle is best-effort; some Lightning pages never idle
            try:
                page.wait_for_selector(selector, timeout=self.config.selector_timeout_ms)
            except Exception:
                pass

            html = page.content()
            if any(marker in html for marker in SALESFORCE_ERROR_MARKERS) and (
                "slds-rich-text" not in html and "article" not in html.lower()
            ):
                raise TransientRenderError(f"Loader/error shell still present for {url}")
            return html
        finally:
            page.close()
