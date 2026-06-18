#!/usr/bin/env python3
"""Promote a scraped set from output/ (scratch) into data/ (committed corpus).

Rebuilds manifest.json + chunks.jsonl from the .md files so all three reconcile,
drops empty pages (e.g. dead-link 404s), and dedups by output path. This is the
canonical way to turn an ad-hoc crawl into a committed dataset.

Usage:
    python scripts/promote.py <set-name> [<set-name> ...]
    # e.g. python scripts/promote.py docusign-iris-ai-assistant
"""

from __future__ import annotations

import glob
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone

import yaml

# Make the scraper package importable when run from the repo root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.models import Page, PageMetadata  # noqa: E402
from scraper.output import _chunk_dict  # noqa: E402
from scraper.transform import chunk_page  # noqa: E402

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n\n?(.*)$", re.S)


def promote(name: str, src_root: str = "output", dst_root: str = "data") -> None:
    src = os.path.join(src_root, name)
    dst = os.path.join(dst_root, name)
    if not os.path.isdir(src):
        raise SystemExit(f"no such scraped set: {src}")
    if os.path.exists(dst):
        shutil.rmtree(dst)

    manifest, chunk_lines, seen = [], [], set()
    for f in sorted(glob.glob(src + "/**/*.md", recursive=True)):
        txt = open(f, encoding="utf-8").read()
        m = _FRONTMATTER.match(txt)
        if not m:
            continue
        front = yaml.safe_load(m.group(1)) or {}
        body = m.group(2)
        if not body.strip():
            continue  # drop empties / 404 shells
        rel = os.path.relpath(f, src)
        if rel in seen:
            continue
        seen.add(rel)

        out = os.path.join(dst, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        shutil.copyfile(f, out)

        meta = PageMetadata(
            source_url=front.get("source_url", ""), site=front.get("site", ""),
            title=front.get("title", ""), breadcrumb=front.get("breadcrumb") or [],
            scraped_at=front.get("scraped_at", ""),
        )
        chunks = chunk_page(Page(metadata=meta, content_html="", markdown=body), 4000, 200)
        chunk_lines += [json.dumps(_chunk_dict(c), ensure_ascii=False) for c in chunks]
        manifest.append({
            "source_url": meta.source_url, "site": meta.site, "title": meta.title,
            "breadcrumb": meta.breadcrumb, "scraped_at": meta.scraped_at,
            "chunks": len(chunks), "has_content": True, "markdown_path": rel,
        })

    with open(os.path.join(dst, "chunks.jsonl"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(chunk_lines) + "\n")
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(os.path.join(dst, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump({"generated_at": stamp, "source": "docusign-scraper", "pages": manifest},
                  fh, indent=2, ensure_ascii=False)
    print(f"{dst}: {len(manifest)} pages, {len(chunk_lines)} chunks")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for name in sys.argv[1:]:
        promote(name)
