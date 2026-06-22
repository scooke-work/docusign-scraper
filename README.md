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
- `docusign-esignature-rest-api/` — 1,058 pages / 6,268 chunks (eSignature REST
  API developer docs — complete: 101 guides, how-tos, SDKs, quickstart, and the
  full endpoint reference incl. the v2 reference)
- `docusign-monitor/` — 75 pages / 188 chunks (Monitor activity/security
  tracking: Monitor API dev docs, the Monitor support bundle, and product page)
- `docusign-clm/` — 452 pages / 1,664 chunks (Contract Lifecycle Management. The
  CLM API dev docs are complete (241 pages); the support side is a representative
  sample (210 pages from the Introduction and Administration bundles, each capped)
  — CLM's full support docs are very large. Plus the product page.)
- `docusign-sdks/` — 5 pages / 54 chunks (the developer SDKs overview docs)
- `docusign-id-evidence/` — 13 pages / 69 chunks (ID Evidence API developer docs
  — retrieving proof of completed ID Verification)
- `docusign-tsp/` — 18 pages / 89 chunks (TSP API developer docs — Trust Service
  Provider program: concepts, get-started, API flow, and endpoint reference)
- `docusign-iam-for-sales/` — 158 pages / 377 chunks (IAM for Sales on Salesforce:
  install/setup, the embedded experience, and the Maestro-with-Salesforce steps)
- `docusign-gen-for-salesforce/` — 250 pages / 467 chunks (Docusign Gen for
  Salesforce document generation — user + admin guides)
- `docusign-esignature-for-salesforce/` — 480 pages / 884 chunks (eSignature for
  Salesforce admin + user guides, plus the Docusign Apps Launcher / DAL admin guide)
- `docusign-agreement-prep/` — 46 pages / 104 chunks (Agreement Preparation — the
  "create" stage: document editors, template builder, sender/signer fields)
- `docusign-click/` — 45 pages / 288 chunks (Click API developer docs — clickwrap
  for high-volume low-risk acceptance — plus the product page)
- `docusign-rooms/` — 296 pages / 1,086 chunks (Rooms for Real Estate/Mortgage:
  the Rooms API dev docs (complete, 161 pages), the Rooms support bundle, product)
- `docusign-agreement-desk/` — 84 pages / 141 chunks (Agreement Desk support — the
  IAM pre-signature intake/review/approval workspace: user guide + admin bundles)
- `docusign-iam-platform/` — 6 pages / 48 chunks (IAM platform overview only —
  the umbrella "what is IAM" pages incl. IAM Core / CX / Sales, plus the product
  page. Intentionally small: IAM's depth lives in the per-product datasets above.)
- `docusign-esignature-support/` — 174 pages / 281 chunks (eSignature end-user
  guides: sending/"Welcome to Docusign", the signer experience, and templates)
- `docusign-account-admin/` — 326 pages / 428 chunks (Account Administration —
  users, permissions, security, branding, and account settings; complete)

Promote an ad-hoc `output/<set>/` run into the committed corpus with
`python scripts/promote.py <set>` (rebuilds a consistent manifest + chunks).

A standalone visual reference of the Agreement Manager AI extraction fields
(types, enum values, and which fields are auto-calculated) lives at
[`docs/ai-extraction-fields.html`](docs/ai-extraction-fields.html) — open it in a browser.

### Not included (by choice)

- **eSignature SOAP API** (`/docs/esign-soap-api/`) — intentionally skipped. The
  SOAP API is legacy; the eSignature REST API (`docusign-esignature-rest-api/`) is
  the current, fully-captured interface. Add it later with
  `docusign-scraper crawl "https://developers.docusign.com/docs/esign-soap-api/" --out output/docusign-esign-soap-api --max-pages 600`
  then `python scripts/promote.py docusign-esign-soap-api` if it's ever needed.
- **CLM support docs** are a representative sample, not exhaustive — see the
  `docusign-clm/` entry above.
- **Combobox-selected schema variants** — the fetcher expands ARIA tab panels and
  collapsed accordions/disclosures (`aria-expanded`) on developer-doc pages, so
  reference-page schemas are captured. It does **not** drive `role="combobox"`
  selectors that swap the displayed schema among many variants (e.g. the
  per-agreement-type response template on the Agreement Manager `getAgreement`
  reference). Those nested per-variant property trees aren't expanded.
- **Multi-language code examples** — the fetcher reveals lazy-loaded tab panels
  (so content tabs like the agreement-type categories are fully captured), but it
  intentionally does **not** expand multi-language code-example tab groups
  (cURL / C# / Java / Node.js / PHP / Python / Ruby …). Only the default-language
  sample is kept, to avoid N near-duplicate copies of every example bloating the
  corpus. Controlled by `LANGUAGE_TAB_LABELS` / `is_language_tab_group()` in
  `scraper/fetcher.py`; remove or narrow that guard to capture all languages.

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
