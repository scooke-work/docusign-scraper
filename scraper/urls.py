"""URL canonicalization shared across discovery and caching.

A single article is reachable under several URL strings during a crawl — the
nav-link variant, the seed form, and the post-render ``final_url`` — which differ
in query-param order, the ``.html`` suffix, and ``language``/``_LANG`` params.
``canonical_url`` collapses those variants to one stable identity so:

  * crawl discovery queues each article once (no duplicate renders), and
  * the fetch cache stores each article once (variants share a cache entry).
"""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse


def canonical_url(url: str) -> str:
    """Return a stable identity for ``url``, collapsing equivalent variants.

    Support article URLs key on ``bundleId`` + ``topicId``; all other URLs key on
    host + path (fragment dropped, trailing slash normalized).
    """
    p = urlparse(url)
    if "/s/document-item" in p.path:
        qs = parse_qs(p.query)
        bundle = qs.get("bundleId", [""])[0]
        topic = qs.get("topicId", [""])[0].replace(".html", "")
        return f"{p.netloc}/document-item?{bundle}:{topic}"
    return f"{p.netloc}{p.path.rstrip('/')}"
