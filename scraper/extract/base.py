"""Extractor interface and host-based dispatch.

Each Docusign property gets its own ``Extractor`` subclass that knows how to
locate the main content, strip chrome, and pull metadata (title, breadcrumb) out
of the rendered DOM. Keeping them isolated means a Salesforce markup change only
touches one file.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Type
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, Tag

from ..models import Page, PageMetadata


class Extractor:
    """Base class. Subclasses set ``host`` and override the hooks below."""

    host: str = ""
    # Selectors tried in order to find the main content container.
    content_selectors: List[str] = ["main", "article"]
    # Elements removed from the content container before conversion.
    strip_selectors: List[str] = [
        "nav", "header", "footer", "script", "style", "noscript",
        "[role='navigation']", "[class*='cookie']", "[class*='banner']",
        "[class*='breadcrumb']", "button", "svg",
    ]

    def __init__(self, url: str, html: str):
        self.url = url
        self.html = html
        self.soup = BeautifulSoup(html, "lxml")

    # -- public API --------------------------------------------------------
    def extract(self) -> Page:
        container = self._find_content()
        meta = PageMetadata(
            source_url=self.url,
            site=urlparse(self.url).netloc,
            title=self._title(container),
            breadcrumb=self._breadcrumb(),
        )
        nav_links = self._nav_links()
        if container is not None:
            self._clean(container)
            self._absolutize_links(container)
            content_html = str(container)
        else:
            content_html = ""
        return Page(metadata=meta, content_html=content_html, nav_links=nav_links)

    # -- hooks (override as needed) ---------------------------------------
    def _find_content(self) -> Optional[Tag]:
        for sel in self.content_selectors:
            node = self.soup.select_one(sel)
            if node and node.get_text(strip=True):
                return node
        return None

    def _title(self, container: Optional[Tag] = None) -> str:
        # Prefer a heading *inside* the article body — on Lightning/Salesforce
        # pages a site-chrome <h1> precedes the real article heading in the DOM.
        if container is not None:
            for sel in ("h1", "h2"):
                node = container.select_one(sel)
                if node and node.get_text(strip=True):
                    return self._clean_text(node)
        for sel in ("h1", "title"):
            node = self.soup.select_one(sel)
            if node and node.get_text(strip=True):
                return self._clean_text(node)
        return ""

    @staticmethod
    def _clean_text(node: Tag) -> str:
        # Join nested inline elements with a space, then collapse runs, so
        # "Manager<span>for</span>" renders "Manager for", not "Managerfor".
        return " ".join(node.get_text(" ", strip=True).split())

    def _breadcrumb(self) -> List[str]:
        crumbs: List[str] = []
        node = self.soup.select_one("[class*='breadcrumb'], nav[aria-label*='readcrumb']")
        if node:
            crumbs = [a.get_text(strip=True) for a in node.select("a, li") if a.get_text(strip=True)]
        return crumbs

    def _nav_links(self) -> List[str]:
        """Same-host links useful for crawl discovery. Overridden per site."""
        return []

    # -- shared helpers ----------------------------------------------------
    def _clean(self, container: Tag) -> None:
        for sel in self.strip_selectors:
            for node in container.select(sel):
                node.decompose()

    def _absolutize_links(self, container: Tag) -> None:
        for a in container.select("a[href]"):
            a["href"] = urljoin(self.url, a["href"])
        for img in container.select("img[src]"):
            img["src"] = urljoin(self.url, img["src"])


# -- registry -------------------------------------------------------------
_REGISTRY: Dict[str, Type[Extractor]] = {}


def register(cls: Type[Extractor]) -> Type[Extractor]:
    _REGISTRY[cls.host] = cls
    return cls


def get_extractor(url: str, html: str) -> Extractor:
    """Return the host-specific extractor, or the generic base as fallback."""
    host = urlparse(url).netloc
    cls = _REGISTRY.get(host, Extractor)
    return cls(url, html)
