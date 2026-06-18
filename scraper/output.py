"""Write extracted pages to disk: Markdown, chunks JSONL, and a manifest."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List
from urllib.parse import parse_qs, urlparse

import yaml

from .models import Chunk, Page


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _safe_slug(url: str) -> str:
    """Build a filesystem-safe relative path mirroring the URL."""
    p = urlparse(url)
    parts = [seg for seg in p.path.split("/") if seg]
    # Salesforce articles carry their identity in the query string, not path.
    if "document-item" in p.path:
        qs = parse_qs(p.query)
        bundle = qs.get("bundleId", ["bundle"])[0]
        topic = qs.get("topicId", ["topic"])[0].replace(".html", "")
        parts = ["support", bundle, topic]
    if not parts:
        parts = ["index"]
    slug = "/".join(re.sub(r"[^A-Za-z0-9._-]", "_", s) for s in parts)
    if not slug.endswith(".md"):
        slug += ".md"
    return slug


class OutputWriter:
    def __init__(self, out_dir: Path, output_format: str = "both", append: bool = False):
        self.out_dir = Path(out_dir)
        self.output_format = output_format
        self.append = append
        self.manifest: List[Dict] = []
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self._writes_jsonl = output_format in ("jsonl", "both")
        # Default mode streams chunks straight to disk (memory-light for large
        # crawls). Append mode buffers per-page so re-scraping a URL replaces its
        # old chunks instead of duplicating them, then rewrites on close.
        self._chunks_fh = None
        self._chunk_store: Dict[str, List[Dict]] = {}
        if append:
            self._load_existing()
        elif self._writes_jsonl:
            self._chunks_fh = (self.out_dir / "chunks.jsonl").open("w", encoding="utf-8")

    def _load_existing(self) -> None:
        """Seed manifest + chunk store from a prior run for append/merge."""
        manifest_path = self.out_dir / "manifest.json"
        if manifest_path.exists():
            try:
                self.manifest = json.loads(manifest_path.read_text(encoding="utf-8")).get("pages", [])
            except (ValueError, OSError):
                self.manifest = []
        chunks_path = self.out_dir / "chunks.jsonl"
        if self._writes_jsonl and chunks_path.exists():
            for line in chunks_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                self._chunk_store.setdefault(rec.get("page_url", ""), []).append(rec)

    def write_page(self, page: Page, chunks: List[Chunk]) -> Dict:
        page.metadata.scraped_at = _now_iso()
        record = {
            "source_url": page.metadata.source_url,
            "site": page.metadata.site,
            "title": page.metadata.title,
            "breadcrumb": page.metadata.breadcrumb,
            "scraped_at": page.metadata.scraped_at,
            "chunks": len(chunks),
            "has_content": bool(page.markdown.strip()),
        }

        if self.output_format in ("md", "both"):
            rel = _safe_slug(page.metadata.source_url)
            md_path = self.out_dir / rel
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(self._render_markdown(page), encoding="utf-8")
            record["markdown_path"] = str(md_path.relative_to(self.out_dir))

        if self._writes_jsonl:
            chunk_dicts = [_chunk_dict(c) for c in chunks]
            if self.append:
                # Replace any prior chunks for this URL (dedup on re-scrape).
                self._chunk_store[page.metadata.source_url] = chunk_dicts
            elif self._chunks_fh is not None:
                for cd in chunk_dicts:
                    self._chunks_fh.write(json.dumps(cd, ensure_ascii=False) + "\n")

        self._upsert_manifest(record)
        return record

    def _upsert_manifest(self, record: Dict) -> None:
        """Append the record, or replace an existing one with the same URL."""
        for i, existing in enumerate(self.manifest):
            if existing.get("source_url") == record["source_url"]:
                self.manifest[i] = record
                return
        self.manifest.append(record)

    def _render_markdown(self, page: Page) -> str:
        front = {
            "title": page.metadata.title,
            "source_url": page.metadata.source_url,
            "site": page.metadata.site,
            "breadcrumb": page.metadata.breadcrumb,
            "scraped_at": page.metadata.scraped_at,
        }
        fm = yaml.safe_dump(front, sort_keys=False, allow_unicode=True).strip()
        return f"---\n{fm}\n---\n\n{page.markdown}"

    def close(self) -> None:
        if self._chunks_fh is not None:
            self._chunks_fh.close()
        elif self.append and self._writes_jsonl:
            with (self.out_dir / "chunks.jsonl").open("w", encoding="utf-8") as fh:
                for recs in self._chunk_store.values():
                    for rec in recs:
                        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        (self.out_dir / "manifest.json").write_text(
            json.dumps({"generated_at": _now_iso(), "pages": self.manifest}, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def __enter__(self) -> "OutputWriter":
        return self

    def __exit__(self, *exc) -> None:
        self.close()


def _chunk_dict(c: Chunk) -> Dict:
    return {
        "id": c.id,
        "page_url": c.page_url,
        "title": c.title,
        "heading_path": c.heading_path,
        "text": c.text,
        "token_estimate": c.token_estimate,
    }
