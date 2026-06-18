"""Core data structures passed between pipeline stages."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class PageMetadata:
    """Metadata captured about a single source page."""

    source_url: str
    site: str  # e.g. "developers.docusign.com"
    title: str = ""
    breadcrumb: List[str] = field(default_factory=list)
    scraped_at: str = ""  # ISO-8601 UTC, stamped at write time


@dataclass
class Page:
    """A fully extracted page: clean content HTML + markdown + metadata."""

    metadata: PageMetadata
    content_html: str  # cleaned main-content HTML (chrome stripped)
    markdown: str = ""
    nav_links: List[str] = field(default_factory=list)  # discovered for crawling


@dataclass
class Chunk:
    """A RAG-sized slice of a page, tagged with its heading path."""

    id: str
    page_url: str
    title: str
    heading_path: List[str]
    text: str
    token_estimate: int = 0
