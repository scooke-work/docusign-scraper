# Docusign Docs & Support Scraper

Extracts the textual content of Docusign's developer documentation and support
sites into **clean, chunked Markdown + metadata** for LLM / RAG ingestion.

Both targets render content with JavaScript — the support site is a Salesforce
Lightning app that returns an empty loader shell to a plain HTTP request — so the
scraper drives a real headless **Chromium** (Playwright) and reads the DOM only
after the article has rendered.

## Install

Requires Python 3.9+. One command on a fresh machine:

```bash
make setup        # upgrades pip, installs the package + Chromium
```

Or manually:

```bash
pip install -e '.[dev,tokens]'    # omit extras for a lean runtime: pip install -e .
python -m playwright install chromium
```

This installs a `docusign-scraper` console command. Everywhere below you can use
either `docusign-scraper ...` or `python -m scraper ...` interchangeably.

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

### `data/` vs `output/`

- **`data/`** is **committed** to git — the canonical scraped corpus that travels
  with the repo, so a fresh clone has the dataset without re-scraping. Refresh it
  with `make scrape-support` / `make scrape-api` (these write into `data/<set>/`).
- **`output/`** is the **gitignored scratch** dir — the default `--out` target for
  ad-hoc runs. The HTML cache (`.cache/`) is gitignored too.

Currently committed under `data/`:
- `agreement-manager-api/` — 28 pages / 175 chunks (developer docs)
- `agreement-manager-support/` — 235 pages / 882 chunks (support docs)
- `docusign-ai-agents/` — 16 pages / 161 chunks (Docusign AI Agents: developer
  AI tooling, support AI bundle, and product/blog pages on Agent Studio, the MCP
  Server, and agentic workflows)
- `docusign-iris-ai-assistant/` — 29 pages / 146 chunks (Docusign Iris + AI
  Assistant: Iris platform pages, AI-Assisted Summaries/Q&A, multilingual AI, and
  the full AI-Assisted Review add-in support docs — install, playbooks, chat)
- `docusign-maestro-workflow/` — 119 pages / 451 chunks (Maestro, now branded
  Workflow Builder: the Workflow Builder API dev docs incl. full endpoint
  reference, the Workflow Builder support bundle, and product/blog pages)
- `docusign-connected-fields/` — 32 pages / 132 chunks (Connected Fields API +
  custom data verification: dev API/extension docs and the Data Verification
  support bundle — install, field types, email/phone/address, event review)
- `docusign-workspaces/` — 77 pages / 304 chunks (Workspaces collaborative hub:
  Workspaces API dev docs, support bundle, product page)
- `docusign-app-center-extensions/` — 152 pages / 837 chunks (App Center +
  Extension Apps: the full /extension-apps/ developer platform docs, the App
  Center support bundle, and product page)
- `docusign-web-forms/` — 103 pages / 345 chunks (Web Forms: Web Forms API dev
  docs and the Web Forms support bundle)
- `docusign-admin-api/` — 128 pages / 773 chunks (Admin API developer docs —
  complete: 101 guides, how-tos, and the full endpoint reference)
- `docusign-esignature-rest-api/` — 500 pages / 3,243 chunks (eSignature REST API
  developer docs. The 101 guides, how-tos, SDKs, and quickstart are complete; the
  endpoint reference is partial — capped at 500 pages, ~353 reference pages of a
  larger set. Re-run with a higher `--max-pages` to complete the reference.)

Promote an ad-hoc `output/<set>/` run into the committed corpus with
`python scripts/promote.py <set>` (rebuilds a consistent manifest + chunks).

## Using inside another repo (git submodule)

To consume this scraper + its `data/` corpus from a `cowork` (or any) project,
add it as a submodule rather than copying the folder (a plain copy nests a repo
inside a repo). From the parent repo:

```bash
git submodule add https://github.com/scooke-work/docusign-scraper.git docusign-scraper
git commit -m "Add docusign-scraper submodule"
```

On another machine, clone the parent with submodules included:

```bash
git clone --recurse-submodules <parent-repo-url>
# or, in an existing clone:
git submodule update --init --recursive
```

Pull updates later with `git submodule update --remote docusign-scraper`.

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
