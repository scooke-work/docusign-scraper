"""Tests for URL canonicalization and canonical cache keying (no browser)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scraper.config import Config  # noqa: E402
from scraper.fetcher import BrowserFetcher  # noqa: E402
from scraper.urls import canonical_url  # noqa: E402

BASE = "https://support.docusign.com/s/document-item"
VARIANTS = [
    f"{BASE}?language=en_US&bundleId=B&topicId=T.html&_LANG=enus",
    f"{BASE}?bundleId=B&topicId=T.html&_LANG=enus",
    f"{BASE}?topicId=T&bundleId=B",  # no .html, reversed order, no lang params
]


def test_support_variants_share_one_canonical():
    keys = {canonical_url(u) for u in VARIANTS}
    assert keys == {"support.docusign.com/document-item?B:T"}


def test_distinct_topics_differ():
    assert canonical_url(VARIANTS[0]) != canonical_url(f"{BASE}?bundleId=B&topicId=OTHER.html")


def test_dev_docs_normalize_fragment_and_trailing_slash():
    a = "https://developers.docusign.com/docs/agreement-manager-api/"
    b = "https://developers.docusign.com/docs/agreement-manager-api#section"
    assert canonical_url(a) == canonical_url(b) == "developers.docusign.com/docs/agreement-manager-api"


def test_cache_path_collapses_variants(tmp_path):
    cfg = Config(cache_dir=tmp_path)
    fetcher = BrowserFetcher(cfg)  # no browser launched; we only call _cache_path
    paths = {str(fetcher._cache_path(u)) for u in VARIANTS}
    assert len(paths) == 1, "all variants of one article must map to one cache file"
