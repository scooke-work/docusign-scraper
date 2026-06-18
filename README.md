# Docusign Docs & Support Scraper

Extracts the textual content of Docusign's developer documentation and support
sites into **clean, chunked Markdown + metadata** for LLM / RAG ingestion.

Both targets render content with JavaScript — the support site is a Salesforce
Lightning app that returns an empty loader shell to a plain HTTP request — so the
scraper drives a real headless **Chromium** (Playwright) and reads the DOM only
after the article has rendered.

## Install

```bash
pip install -r requirements.txt
playwright install chromium
```

## Usage

Single page:

```bash
python -m scraper url "https://developers.docusign.com/docs/agreement-manager-api/"
python -m scraper url "https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=dpj1702944516878.html&_LANG=enus"
```

Crawl a whole doc section / support bundle:

```bash
python -m scraper crawl "https://developers.docusign.com/docs/agreement-manager-api/" --max-pages 25
```

### Options

| Flag | Default | Meaning |
|------|---------|---------|
| `--out DIR` | `output` | Output directory |
| `--format md\|jsonl\|both` | `both` | What to write |
| `--rate SECONDS` | `1.0` | Min delay between page loads |
| `--no-cache` | off | Ignore the on-disk HTML cache |
| `--append` | off | Accumulate into an existing `--out` dir (merge manifest, dedup chunks by URL) |
| `--max-pages N` | `50` | (crawl) page cap |
| `--chunk-size N` | `4000` | Max chars per RAG chunk |
| `--no-headless` | off | Show the browser window (debugging) |

## Output

```
output/
  developers.docusign.com mirrored as docs/...     # one .md per page
  support/<bundleId>/<topicId>.md
  chunks.jsonl     # {id, page_url, title, heading_path, text, token_estimate}
  manifest.json    # every page, status, output path
```

Each `.md` has YAML frontmatter (`title`, `source_url`, `site`, `breadcrumb`,
`scraped_at`) followed by the article in Markdown.

## Architecture

```
scraper/
  cli.py        # argparse entrypoint
  pipeline.py   # fetch -> extract -> transform -> write orchestration
  fetcher.py    # Playwright Chromium, render + cache + Salesforce retry
  discover.py   # crawl URL discovery (sitemap + in-page nav BFS)
  extract/      # per-host content extractors (developers / support)
  transform.py  # HTML -> Markdown + heading-aware chunking
  output.py     # .md frontmatter, chunks.jsonl, manifest.json
  config.py, models.py
```

Site extractors are isolated behind a host registry, so a markup change on the
Salesforce support site (whose CSS class names are unstable) only touches
`extract/support.py`. The offline test suite (`pytest`) exercises extraction,
Markdown conversion and chunking against inline fixtures — no network needed.

## Notes / etiquette

Intended for authorized internal / research use. The scraper rate-limits by
default, sends an honest User-Agent, and caches raw HTML so re-runs don't re-hit
the network. Respect Docusign's Terms of Service and `robots.txt`.
