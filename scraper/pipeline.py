"""Orchestration: fetch -> extract -> transform -> write, for one or many URLs."""

from __future__ import annotations

from typing import List

from .config import Config
from .discover import discover_urls
from .extract import get_extractor
from .fetcher import BrowserFetcher
from .output import OutputWriter
from .transform import chunk_page, html_to_markdown


def _process_url(url: str, html: str, config: Config, writer: OutputWriter) -> dict:
    page = get_extractor(url, html).extract()
    page.markdown = html_to_markdown(page.content_html)
    chunks = chunk_page(page, config.chunk_max_chars, config.chunk_overlap_chars)
    return writer.write_page(page, chunks)


def scrape_url(url: str, config: Config) -> dict:
    """Scrape a single URL. Returns its manifest record."""
    with BrowserFetcher(config) as fetcher, OutputWriter(
        config.out_dir, config.output_format, config.append
    ) as writer:
        res = fetcher.fetch(url)
        record = _process_url(res.final_url, res.html, config, writer)
    return record


def scrape_crawl(seed_url: str, config: Config) -> List[dict]:
    """Discover and scrape a section/bundle starting from ``seed_url``."""
    with BrowserFetcher(config) as fetcher, OutputWriter(
        config.out_dir, config.output_format, config.append
    ) as writer:
        urls = discover_urls(seed_url, config, fetcher.fetch)
        records = []
        seen_final = set()
        for url in urls:
            try:
                res = fetcher.fetch(url)
            except Exception as exc:  # noqa: BLE001 - record and continue
                records.append({"source_url": url, "error": str(exc), "has_content": False})
                continue
            if res.final_url in seen_final:  # two requests redirected to same page
                continue
            seen_final.add(res.final_url)
            records.append(_process_url(res.final_url, res.html, config, writer))
    return records
