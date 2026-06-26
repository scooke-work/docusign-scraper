# CLAUDE.md — working notes for this repo

Agent-facing context for picking this up fresh. User-facing docs (architecture,
install, dataset inventory, options) live in **[README.md](README.md)** — don't
duplicate them here; this file is the stuff that isn't obvious from the code.

## What this is (1 line)
Python + Playwright scraper that turns Docusign docs (developers.docusign.com,
support.docusign.com, and www/community pages) into RAG-ready Markdown + chunks.
Code in `scraper/`, scraped corpus committed under `data/`. **Scope: Docusign only**
(decided this session — keep the tuned extractors/discovery focused).

## Workflow & conventions
- **Run from the venv**: `make setup` (upgrades pip → editable install → `playwright install chromium`), `make test`. Invoke as `python -m scraper ...` or `docusign-scraper ...`.
- **Scrape → promote → commit pipeline**: scrape into `output/<set>/` (scratch, gitignored) → `python scripts/promote.py <set>` rebuilds a consistent `data/<set>/` (manifest + chunks, drops empties) → commit `data/<set>/`. README's dataset list is the source of truth for what's captured.
- **Tests are offline**: pytest with no network/browser. When logic lives inside browser interaction, extract a **pure helper** and unit-test that (e.g. `is_language_tab_group`, `canonical_url`). 20 tests currently; keep them browser-free.
- **Commits**: one per dataset/feature, then push. End messages with the `Co-Authored-By: Claude Opus 4.8` trailer. Working tree is kept clean/pushed.
- **Politeness**: cache-first, rate-limited, honest User-Agent. Respect robots/ToS.
- **docs/ reference set** is a curated knowledge base with an index ([docs/README.md](docs/README.md)): `iam-products.md`, `ai-extraction-fields.html`+`.md` (fields/enums/obligations/per-type matrix), `contract-hierarchy.html`, `agreement-manager-ui-screens.md`, `sc-guide-salesforce-iam-use-cases.md`. Standalone HTML (no deps, light/dark). Keep every enum/value claim **grounded**; flag unverified or screenshot-sourced items explicitly rather than guessing.
- **Don't** scrape eSignature SOAP (legacy — intentionally excluded; command in README) or expand multi-language code-example tabs (the `LANGUAGE_TAB_LABELS` guard in `fetcher.py`).

## Gotchas (most are session-earned, not visible in code)
- **Docusign renames products; live slugs redirect.** Navigator API → **Agreement Manager API**; Maestro API → **Workflow Builder API** (even the product page redirects). The scraper now records the **final URL** (`FetchResult.final_url`); crawl discovery derives its path-prefix bound from the post-redirect URL.
- **`searchDocusignDocs` (the Docusign MCP) is STALE** (indexed ~2025-10) — it still returns old `navigator-api` content. Don't trust it for current slugs/values; verify against the live site.
- **Scraped support docs lag the live UI** — several claims were corrected from user screenshots: custom field types now include **Currency** (docs list only Text/Number/Date/Dropdown); obligation **Type** uses *Renewal* / *Warranties* (docs say *Renewal notification* / *Warranty*); custom-field **Category** showed 6 in the UI (no *Human Resources*). Treat doc-derived enum/field lists as point-in-time; the genuinely UI-only values (obligation **Status** Active/Fulfilled/Unfulfilled/Dependent, **Frequency** One Time/Recurring) exist in no public doc/API and must come from screenshots.
- **support.docusign.com is Salesforce Lightning** (empty JS shell to a plain fetch → must render). The same article has many URL variants (bundleId/topicId order, `.html`, `_LANG`); `canonical_url` (in `scraper/urls.py`) dedups them and keys the cache.
- **Crawls hit `--max-pages` caps silently.** After a crawl, check whether the per-host page count equals the cap; if so it's truncated — re-run with a higher cap (warm cache makes already-fetched pages instant). Happened with eSignature reference, App Center, CLM, Rooms.
- **Lazy-loaded UI on dev docs**: agreement-type category tabs only render the active tab → `_reveal_tabs` clicks through ARIA tabs; API reference schemas hide behind `aria-expanded` accordions → `_expand_disclosures`. **Still not handled**: `role="combobox"` schema-variant selectors (e.g. `getAgreement` per-agreement-type response templates) — deepest per-variant provision trees aren't captured.
- **`promote.py` overwrites `data/<set>/` from `output/<set>/`.** Running it against a *partial* output dir destroys the full dataset. For a single-page refresh, rebuild `data/<set>/` **in place** from its own `.md` files (see the inline scripts used in git history), don't promote from a 1-page output.
- **gh account drifts to `iamdocu`; pushes need `scooke-work`.** This clone has a local gh credential helper so `git push` works; if it 403s, `gh auth switch --user scooke-work`.
- **Shell**: `grep -c` exits non-zero when count is 0 and breaks `&&` chains (bit me on a commit). Live scrapes need `dangerouslyDisableSandbox: true`; long crawls run in background.

## Current state & next steps
- **Scraper is complete & hardened**; corpus = ~24 datasets under `data/` covering the full dev API surface (minus SOAP), AI products (Agents, Iris/AI Assistant), the IAM platform, core support, and the **Salesforce-integration stack** (IAM for Sales, Gen for Salesforce, eSignature/DAL for Salesforce, Agreement Prep). See README for the list and known-partial notes (CLM support = representative sample).
- **SC guide is DRAFTED** ([docs/sc-guide-salesforce-iam-use-cases.md](docs/sc-guide-salesforce-iam-use-cases.md)) for the "Gen for SFDC <> IAM for Sales" relaunch plan (`~/Downloads/Recommendation on Gen for Salesforce <> IAM for Sales Relaunch.docx`): use cases NDA / General Legal / 3rd-Party Paper / Quotes-SOW / CPQ, with one-time setup, the Maestro Salesforce step building blocks, per-use-case recipes, and a corpus reference map. **WTA = Word Template Assistant** (Word add-in, precise formatting), **ATB = Agreement Template Builder** (in-app) — confirmed in `docusign-agreement-prep`. The relaunch `.docx` extracts cleanly by stripping XML tags (no python-docx).
- **Reference docs (`docs/`) are built out** with an index: IAM products, AI extraction fields + obligations (+ per-type field matrix from "Standard Fields for Agreement and Non-Agreement Types"), the contract-hierarchy visual (now **saved** as `contract-hierarchy.html`), and the UI screen inventory. There is **no obligations API** (Agreement Manager API exposes only `getAgreement`/`getAgreementsList`).
- **Recommended next action**: deepen the SC guide — expand the flagship **UC4 (Gen → Agreement Desk → DAL/eSign)** into click-by-click steps for a demo-ready walkthrough.
- **Loose ends / open gaps**:
  - **Scraper enhancement**: drive the `role="combobox"` schema-variant selector on the `getAgreement` reference to capture the deepest per-agreement-type provision trees (the one dev-side gap; not screenshot-fixable).
  - **Screenshot-dependent** (UI-only, user must supply): obligation **Status** tooltip definitions, where **Discounts** appears on an obligation, confirm custom-field **Category** has no Human Resources.
  - If asked for more coverage: SOAP API, fuller CLM support, or non-Docusign sites (explicitly out of scope unless the user reopens it).
