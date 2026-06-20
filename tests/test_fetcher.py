"""Offline tests for fetcher helpers that don't need a browser."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scraper.fetcher import is_language_tab_group  # noqa: E402


def test_language_tab_groups_are_detected():
    # Multi-language code-example selectors → skipped (not expanded).
    assert is_language_tab_group(["cURL", "C#", "Java", "Node.js", "PHP", "Python", "Ruby"])
    assert is_language_tab_group(["Python", "JavaScript"])
    assert is_language_tab_group(["C#", "VB.NET", ".NET"])


def test_content_tab_groups_are_kept():
    # Content category tabs → expanded so all panels are captured.
    assert not is_language_tab_group(["BusinessServices", "Miscellaneous", "HumanResources"])
    assert not is_language_tab_group(["Schema", "Definitions", "Examples"])
    assert not is_language_tab_group(["Overview", "Pricing"])


def test_edge_cases():
    assert not is_language_tab_group([])           # nothing to do
    assert not is_language_tab_group(["Python"])   # single tab — not a selector
    assert not is_language_tab_group(["", "  "])   # empty labels
