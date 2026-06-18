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


def test_support_url_variants_render_once(monkeypatch):
    monkeypatch.setattr(discover, "_try_sitemap", lambda *a, **k: [])
    base = "https://support.docusign.com/s/document-item"
    seed = f"{base}?language=en_US&bundleId=B&topicId=T1.html&_LANG=enus"
    # The seed page links to T2 in two equivalent variants + T1 (itself) variant.
    t2_a = f"{base}?bundleId=B&topicId=T2.html&_LANG=enus"
    t2_b = f"{base}?topicId=T2&bundleId=B"  # no .html, different order
    t1_self = f"{base}?bundleId=B&topicId=T1"
    page_html = f'<article><a href="{t2_a}">a</a><a href="{t2_b}">b</a><a href="{t1_self}">self</a></article>'

    calls = []

    def fake_fetch(u):
        calls.append(u)
        return FetchResult(page_html if "T1" in u else "<article>t2</article>", u)

    urls = discover.discover_urls(seed, Config(max_pages=50), fake_fetch)

    # Exactly two distinct topics fetched (T1 seed + T2 once), not three+ variants.
    assert len(calls) == 2
    assert len(urls) == 2


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
