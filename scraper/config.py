"""Runtime configuration for the scraper.

A single ``Config`` dataclass is threaded through the fetcher, crawler and
output writer so behaviour (rate limiting, timeouts, cache location, output
directory) is set once at the CLI boundary.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# A realistic, honest User-Agent. We identify as a scraper rather than
# impersonating a person — the goal is authorized/internal collection.
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 "
    "DocusignDocsScraper/0.1 (+internal research use)"
)


@dataclass
class Config:
    """All tunable knobs for a scrape run."""

    out_dir: Path = field(default_factory=lambda: Path("output"))
    cache_dir: Path = field(default_factory=lambda: Path(".cache"))

    # Politeness
    rate_seconds: float = 1.0  # min delay between navigations
    concurrency: int = 1  # parallel pages (kept low to be polite)
    user_agent: str = DEFAULT_USER_AGENT

    # Timing (milliseconds, Playwright convention)
    nav_timeout_ms: int = 45_000
    selector_timeout_ms: int = 20_000  # max wait for the content selector to appear
    # Short, best-effort "settle" wait after content appears. Kept low because
    # Salesforce Lightning pages often never reach networkidle — waiting the full
    # selector timeout on every page was the dominant per-page cost.
    idle_timeout_ms: int = 2_500

    # Behaviour
    use_cache: bool = True
    headless: bool = True

    # Crawl bounds
    max_pages: int = 50

    # Output format: "md", "jsonl", or "both"
    output_format: str = "both"

    # Accumulate into an existing output dir instead of overwriting it.
    append: bool = False

    # Chunking
    chunk_max_chars: int = 4_000
    chunk_overlap_chars: int = 200

    def __post_init__(self) -> None:
        self.out_dir = Path(self.out_dir)
        self.cache_dir = Path(self.cache_dir)
