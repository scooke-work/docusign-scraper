"""Offline tests for redirect-aware crawl discovery (no browser/network)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import scraper.discover as discover  # noqa: E402
from scraper.config import Config  # noqa: E402
from scraper.fetcher import FetchResult  # noqa: E402

AM = "https://developers.docusign.com/docs/agreement-manager-api/"
CHILD = AM + "concepts/"
OTHER = "https://developers.docusign.com/docs/esign-rest-api/"
NAV = "https://developers.docusign.com/docs/navigator-api/"

_NAV_HTML = f'<main><a href="{CHILD}">c</a><a href="{OTHER}">o</a></main>'


def _pages():
    return {
        NAV: FetchResult(_NAV_HTML, AM),       # seed redirects to AM
        AM: FetchResult(_NAV_HTML, AM),
        CHILD: FetchResult("<main>leaf</main>", CHILD),
    }


def test_seed_redirect_is_canonicalized_and_bounded(monkeypatch):
    monkeypatch.setattr(discover, "_try_sitemap", lambda *a, **k: [])  # force BFS path
    pages = _pages()
    fake_fetch = lambda u: pages.get(u, FetchResult("<main></main>", u))

    urls = discover.discover_urls(NAV, Config(max_pages=10), fake_fetch)

    # Followed the redirect: output uses the final URL, never the requested one.
    assert AM in urls
    assert all("navigator-api" not in u for u in urls)
    # Bounded to the section it actually landed on (not other API families).
    assert CHILD in urls
    assert OTHER not in urls


def test_two_urls_redirecting_to_same_page_dedup(monkeypatch):
    monkeypatch.setattr(discover, "_try_sitemap", lambda *a, **k: [])
    # Both the seed and a discovered link resolve to AM -> AM appears once.
    pages = {
        NAV: FetchResult(f'<main><a href="{AM}">self</a></main>', AM),
        AM: FetchResult(f'<main><a href="{AM}">self</a></main>', AM),
    }
    fake_fetch = lambda u: pages.get(u, FetchResult("<main></main>", u))
    urls = discover.discover_urls(NAV, Config(max_pages=10), fake_fetch)
    assert urls.count(AM) == 1
