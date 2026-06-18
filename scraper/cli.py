"""Command-line entrypoint.

Usage:
    python -m scraper url   <URL>        [options]
    python -m scraper crawl <SEED_URL>   [options]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .config import Config
from .pipeline import scrape_crawl, scrape_url


def _add_common(p: argparse.ArgumentParser) -> None:
    p.add_argument("--out", default="output", help="Output directory (default: output)")
    p.add_argument(
        "--format",
        dest="output_format",
        choices=["md", "jsonl", "both"],
        default="both",
        help="Output format (default: both)",
    )
    p.add_argument("--rate", type=float, default=1.0, help="Min seconds between page loads")
    p.add_argument("--no-cache", action="store_true", help="Ignore the on-disk HTML cache")
    p.add_argument(
        "--append",
        action="store_true",
        help="Accumulate into an existing --out dir (merge manifest, dedup chunks by URL)",
    )
    p.add_argument("--cache-dir", default=".cache", help="Raw HTML cache directory")
    p.add_argument("--no-headless", action="store_true", help="Show the browser window")
    p.add_argument("--chunk-size", type=int, default=4000, help="Max chars per chunk")


def _config_from_args(args: argparse.Namespace) -> Config:
    return Config(
        out_dir=Path(args.out),
        cache_dir=Path(args.cache_dir),
        rate_seconds=args.rate,
        use_cache=not args.no_cache,
        headless=not args.no_headless,
        output_format=args.output_format,
        append=args.append,
        chunk_max_chars=args.chunk_size,
        max_pages=getattr(args, "max_pages", 50),
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="scraper", description="Docusign docs/support scraper")
    sub = parser.add_subparsers(dest="command", required=True)

    p_url = sub.add_parser("url", help="Scrape a single URL")
    p_url.add_argument("target", help="The page URL to scrape")
    _add_common(p_url)

    p_crawl = sub.add_parser("crawl", help="Crawl a doc section / support bundle")
    p_crawl.add_argument("target", help="Seed URL")
    p_crawl.add_argument("--max-pages", type=int, default=50, help="Max pages to scrape")
    _add_common(p_crawl)

    args = parser.parse_args(argv)
    config = _config_from_args(args)

    if args.command == "url":
        record = scrape_url(args.target, config)
        ok = record.get("has_content")
        print(f"{'[ok]' if ok else '[empty]'} {args.target} "
              f"-> {record.get('markdown_path', '(no md)')} ({record.get('chunks', 0)} chunks)")
        return 0 if ok else 2

    if args.command == "crawl":
        records = scrape_crawl(args.target, config)
        ok = sum(1 for r in records if r.get("has_content"))
        print(f"Crawled {len(records)} pages from {args.target}; {ok} with content.")
        print(f"Output in {config.out_dir}/ (manifest.json, chunks.jsonl)")
        return 0 if ok else 2

    return 1


if __name__ == "__main__":
    sys.exit(main())
