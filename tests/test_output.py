"""Offline tests for title selection and append/merge output behavior."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scraper.extract import get_extractor  # noqa: E402
from scraper.models import Chunk, Page, PageMetadata  # noqa: E402
from scraper.output import OutputWriter  # noqa: E402

# A Lightning-style page: a site-chrome <h1> precedes the real article <h1>.
SUPPORT_HTML = """
<html><head><title>Docusign Agreement Manager</title></head>
<body>
  <header><h1>Docusign Agreement Manager</h1></header>
  <main>
    <lightning-formatted-rich-text>
      <h1>Agreement Manager<span> for </span>Administrators</h1>
      <p>Read about how administrators interact with Agreement Manager.</p>
    </lightning-formatted-rich-text>
  </main>
</body></html>
"""

SUPPORT_URL = (
    "https://support.docusign.com/s/document-item"
    "?bundleId=pqz1702943441912&topicId=dpj1702944516878.html&_LANG=enus"
)


def test_title_prefers_content_container_heading():
    page = get_extractor(SUPPORT_URL, SUPPORT_HTML).extract()
    # Must pick the article heading, not the site-chrome one.
    assert page.metadata.title == "Agreement Manager for Administrators"


def _page(url: str, title: str) -> Page:
    return Page(metadata=PageMetadata(source_url=url, site="x", title=title), content_html="", markdown="body")


def _chunk(url: str, text: str) -> Chunk:
    return Chunk(id=url + "#0", page_url=url, title="t", heading_path=[], text=text)


def test_default_mode_overwrites(tmp_path):
    with OutputWriter(tmp_path, "both") as w:
        w.write_page(_page("u/a", "A"), [_chunk("u/a", "first")])
    with OutputWriter(tmp_path, "both") as w:  # fresh session overwrites
        w.write_page(_page("u/b", "B"), [_chunk("u/b", "second")])
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    urls = [p["source_url"] for p in manifest["pages"]]
    assert urls == ["u/b"]
    lines = (tmp_path / "chunks.jsonl").read_text().strip().splitlines()
    assert len(lines) == 1 and "second" in lines[0]


def test_append_merges_distinct_urls(tmp_path):
    with OutputWriter(tmp_path, "both") as w:
        w.write_page(_page("u/a", "A"), [_chunk("u/a", "first")])
    with OutputWriter(tmp_path, "both", append=True) as w:
        w.write_page(_page("u/b", "B"), [_chunk("u/b", "second")])
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    urls = sorted(p["source_url"] for p in manifest["pages"])
    assert urls == ["u/a", "u/b"]
    lines = (tmp_path / "chunks.jsonl").read_text().strip().splitlines()
    assert len(lines) == 2


def test_append_dedups_rescraped_url(tmp_path):
    with OutputWriter(tmp_path, "both") as w:
        w.write_page(_page("u/a", "A"), [_chunk("u/a", "old")])
    # Re-scrape same URL in append mode -> replace, not duplicate.
    with OutputWriter(tmp_path, "both", append=True) as w:
        w.write_page(_page("u/a", "A"), [_chunk("u/a", "new")])
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    assert [p["source_url"] for p in manifest["pages"]] == ["u/a"]
    lines = (tmp_path / "chunks.jsonl").read_text().strip().splitlines()
    assert len(lines) == 1 and "new" in lines[0] and "old" not in lines[0]
