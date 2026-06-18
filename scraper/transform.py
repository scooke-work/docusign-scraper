"""HTML -> Markdown conversion and heading-based chunking for RAG."""

from __future__ import annotations

import re
from typing import List

from bs4 import BeautifulSoup
from markdownify import markdownify as md

from .models import Chunk, Page


def html_to_markdown(content_html: str) -> str:
    """Convert cleaned content HTML to normalized Markdown."""
    if not content_html.strip():
        return ""
    text = md(
        content_html,
        heading_style="ATX",
        code_language="",
        bullets="-",
        strip=["span"],
    )
    return _normalize_whitespace(text)


def _normalize_whitespace(text: str) -> str:
    # Collapse 3+ blank lines to a single blank line; trim trailing spaces.
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def estimate_tokens(text: str) -> int:
    """Token estimate. Uses tiktoken when available, else ~4 chars/token."""
    try:
        import tiktoken

        enc = tiktoken.get_encoding("cl100k_base")
        return len(enc.encode(text))
    except Exception:
        return max(1, len(text) // 4)


def chunk_page(page: Page, max_chars: int = 4000, overlap_chars: int = 200) -> List[Chunk]:
    """Split a page's Markdown into heading-aware, size-bounded chunks.

    Each chunk records the heading path (H1>H2>H3 trail) it falls under so the
    embedding/retrieval layer keeps document structure as context.
    """
    sections = _split_by_headings(page.markdown)
    chunks: List[Chunk] = []
    base_id = re.sub(r"\W+", "-", page.metadata.source_url)[-60:].strip("-")

    idx = 0
    for heading_path, body in sections:
        for piece in _split_oversize(body, max_chars, overlap_chars):
            if not piece.strip():
                continue
            chunks.append(
                Chunk(
                    id=f"{base_id}#{idx}",
                    page_url=page.metadata.source_url,
                    title=page.metadata.title,
                    heading_path=heading_path,
                    text=piece.strip(),
                    token_estimate=estimate_tokens(piece),
                )
            )
            idx += 1
    return chunks


def _split_by_headings(markdown: str):
    """Yield (heading_path, body_markdown) keeping the H1>H2>H3 trail."""
    lines = markdown.splitlines()
    path: List[str] = []
    buf: List[str] = []
    sections = []

    def flush():
        if buf:
            sections.append((list(path), "\n".join(buf).strip()))

    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush()
            buf = []
            level = len(m.group(1))
            title = m.group(2).strip()
            path = path[: level - 1]
            while len(path) < level - 1:
                path.append("")
            path = path[: level - 1] + [title]
        else:
            buf.append(line)
    flush()

    if not sections:  # no headings at all
        sections = [([], markdown.strip())]
    return sections


def _split_oversize(text: str, max_chars: int, overlap: int) -> List[str]:
    """Break a section body that exceeds max_chars on paragraph boundaries."""
    if len(text) <= max_chars:
        return [text]
    paras = text.split("\n\n")
    out: List[str] = []
    cur = ""
    for para in paras:
        if cur and len(cur) + len(para) + 2 > max_chars:
            out.append(cur)
            tail = cur[-overlap:] if overlap else ""
            cur = (tail + "\n\n" + para).strip()
        else:
            cur = (cur + "\n\n" + para).strip() if cur else para
    if cur:
        out.append(cur)
    return out
