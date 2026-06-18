"""Crawl-mode URL discovery.

Two strategies, chosen by host:

* **developers.docusign.com** — try the site ``sitemap.xml`` first (fast, complete),
  filtered to the seed's path prefix; otherwise fall back to a breadth-first walk
  over left-nav links extracted from each rendered page.
* **support.docusign.com** — no useful sitemap for Lightning articles, so we walk
  sibling ``document-item`` links that share the seed's ``bundleId`` (handled by
  the support extractor's ``nav_links``).

Both paths are bounded by ``max_pages`` and stay on the seed host.
"""

from __future__ import annotations

import re
from collections import deque
from typing import Callable, List, Set
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from .config import Config
from .extract import get_extractor


def _path_prefix(url: str) -> str:
    """Directory-ish prefix of a URL path, used to bound dev-docs crawls."""
    p = urlparse(url)
    path = p.path
    if not path.endswith("/"):
        path = path.rsplit("/", 1)[0] + "/"
    return path


def _try_sitemap(seed_url: str, config: Config) -> List[str]:
    p = urlparse(seed_url)
    sitemap_url = f"{p.scheme}://{p.netloc}/sitemap.xml"
    prefix = _path_prefix(seed_url)
    try:
        req = Request(sitemap_url, headers={"User-Agent": config.user_agent})
        with urlopen(req, timeout=15) as resp:
            xml = resp.read().decode("utf-8", "replace")
    except Exception:
        return []
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    out = []
    for loc in locs:
        pp = urlparse(loc)
        if pp.netloc == p.netloc and pp.path.startswith(prefix):
            out.append(loc.split("#")[0])
    return out


def discover_urls(seed_url: str, config: Config, fetch: Callable[[str], str]) -> List[str]:
    """Return an ordered, de-duplicated list of URLs to scrape (incl. the seed).

    ``fetch`` renders a URL to HTML (typically ``BrowserFetcher.fetch``); it is
    injected so discovery reuses the same browser, cache and rate limiting.
    """
    host = urlparse(seed_url).netloc

    # Fast path: dev docs sitemap.
    if host == "developers.docusign.com":
        sm = _try_sitemap(seed_url, config)
        if sm:
            ordered = [seed_url] + [u for u in sm if u != seed_url]
            return ordered[: config.max_pages]

    # General path: BFS over rendered-page nav links, bounded by host + prefix.
    prefix = _path_prefix(seed_url) if host == "developers.docusign.com" else None
    seen: Set[str] = set()
    ordered: List[str] = []
    queue: deque[str] = deque([seed_url])

    while queue and len(ordered) < config.max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        ordered.append(url)
        try:
            html = fetch(url)
        except Exception:
            continue
        for link in get_extractor(url, html).extract().nav_links:
            lp = urlparse(link)
            if lp.netloc != host:
                continue
            if prefix and not lp.path.startswith(prefix):
                continue
            if link not in seen:
                queue.append(link)
    return ordered[: config.max_pages]
