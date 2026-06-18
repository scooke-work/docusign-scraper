"""Extractor for developers.docusign.com (React-rendered docs)."""

from __future__ import annotations

from typing import List
from urllib.parse import urljoin, urlparse

from ..models import Page  # noqa: F401  (kept for typing clarity)
from .base import Extractor, register


@register
class DevelopersExtractor(Extractor):
    host = "developers.docusign.com"

    # The docs body lives in a main/article region; class names are hashed by
    # the build so we lean on semantic elements first.
    content_selectors = [
        "main article",
        "main [class*='markdown']",
        "main",
        "article",
    ]

    # Documentation sections on this host. Not every dev doc lives under /docs/
    # (e.g. the extension-apps platform docs). The crawl's path-prefix bound keeps
    # a run scoped to the seed's own section, so listing several here is safe.
    DOC_PREFIXES = ("/docs/", "/extension-apps/", "/platform/", "/iam-toolkit/")

    def _nav_links(self) -> List[str]:
        """Same-host links within known documentation sections."""
        links: List[str] = []
        for a in self.soup.select("a[href]"):
            href = urljoin(self.url, a.get("href", ""))
            parsed = urlparse(href)
            if parsed.netloc == self.host and parsed.path.startswith(self.DOC_PREFIXES):
                links.append(href.split("#")[0])
        # de-dup, preserve order
        seen = set()
        out = []
        for link in links:
            if link not in seen:
                seen.add(link)
                out.append(link)
        return out
