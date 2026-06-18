"""Offline tests for HTML->Markdown conversion, chunking, and extraction.

These run without a network or browser — they exercise the pure-Python pipeline
stages against small inline HTML fixtures.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scraper.extract import get_extractor  # noqa: E402
from scraper.models import Page, PageMetadata  # noqa: E402
from scraper.transform import chunk_page, html_to_markdown  # noqa: E402

SAMPLE_HTML = """
<html><head><title>Agreement Manager API overview | Docusign</title></head>
<body>
  <nav>site nav we should drop</nav>
  <main>
    <article>
      <h1>Agreement Manager API overview</h1>
      <p>The Agreement Manager API lets you manage agreements.</p>
      <h2>Authentication</h2>
      <p>Use OAuth to authenticate. See <a href="/docs/auth/">auth docs</a>.</p>
      <pre><code>GET /agreements</code></pre>
      <h2>Endpoints</h2>
      <p>There are several endpoints.</p>
    </article>
  </main>
  <footer>footer junk</footer>
</body></html>
"""


def _build_page(url: str, html: str) -> Page:
    page = get_extractor(url, html).extract()
    page.markdown = html_to_markdown(page.content_html)
    return page


def test_extract_strips_chrome_and_keeps_content():
    page = _build_page("https://developers.docusign.com/docs/agreement-manager-api/", SAMPLE_HTML)
    assert "site nav we should drop" not in page.markdown
    assert "footer junk" not in page.markdown
    assert "Agreement Manager API lets you manage agreements" in page.markdown
    assert page.metadata.title == "Agreement Manager API overview"
    assert page.metadata.site == "developers.docusign.com"


def test_markdown_has_headings_and_code():
    page = _build_page("https://developers.docusign.com/docs/agreement-manager-api/", SAMPLE_HTML)
    assert "# Agreement Manager API overview" in page.markdown
    assert "## Authentication" in page.markdown
    assert "GET /agreements" in page.markdown


def test_links_absolutized():
    page = _build_page("https://developers.docusign.com/docs/agreement-manager-api/", SAMPLE_HTML)
    assert "https://developers.docusign.com/docs/auth/" in page.markdown


def test_chunking_carries_heading_path():
    page = _build_page("https://developers.docusign.com/docs/agreement-manager-api/", SAMPLE_HTML)
    chunks = chunk_page(page, max_chars=4000, overlap_chars=100)
    assert chunks, "expected at least one chunk"
    auth = [c for c in chunks if "OAuth" in c.text]
    assert auth and "Authentication" in auth[0].heading_path[-1]
    assert all(c.token_estimate > 0 for c in chunks)


def test_empty_content_is_safe():
    page = Page(metadata=PageMetadata(source_url="x", site="x"), content_html="")
    page.markdown = html_to_markdown(page.content_html)
    assert page.markdown == ""
    assert chunk_page(page) == []
