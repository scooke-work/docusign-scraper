"""Extractor for support.docusign.com (Salesforce Lightning Knowledge).

Article URLs look like:
    /s/document-item?language=en_US&bundleId=<B>&topicId=<T>.html&_LANG=enus

The article body is rendered by Lightning components; the visible text ends up in
a rich-text output container. We also harvest sibling-topic links *within the same
bundle* so crawl mode can walk a whole bundle without escaping into all of Support.
"""

from __future__ import annotations

from typing import List
from urllib.parse import parse_qs, urljoin, urlparse

from .base import Extractor, register


@register
class SupportExtractor(Extractor):
    host = "support.docusign.com"

    content_selectors = [
        "lightning-formatted-rich-text",
        ".slds-rich-text-editor__output",
        "[class*='document-item'] article",
        "article",
        "main",
    ]

    # Lightning wraps articles in lots of slds chrome; drop the obvious nav bits.
    strip_selectors = Extractor.strip_selectors + [
        "[class*='breadcrumbs']",
        "[class*='sidebar']",
        "[class*='toc']",
        "[class*='feedback']",
        "lightning-icon",
    ]

    def _bundle_id(self) -> str:
        return parse_qs(urlparse(self.url).query).get("bundleId", [""])[0]

    def _nav_links(self) -> List[str]:
        """Sibling document-item links sharing this page's bundleId."""
        bundle = self._bundle_id()
        if not bundle:
            return []
        links: List[str] = []
        for a in self.soup.select("a[href]"):
            href = urljoin(self.url, a.get("href", ""))
            parsed = urlparse(href)
            if parsed.netloc != self.host or "/s/document-item" not in parsed.path:
                continue
            qs = parse_qs(parsed.query)
            if qs.get("bundleId", [""])[0] == bundle:
                links.append(href)
        seen = set()
        out = []
        for link in links:
            if link not in seen:
                seen.add(link)
                out.append(link)
        return out
