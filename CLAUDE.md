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
- **docs/ reference files** (`ai-extraction-fields.html` + `.md`) are standalone (no deps, light/dark). Keep every enum/value claim **grounded**, and explicitly flag anything unverified rather than guessing.
- **Don't** scrape eSignature SOAP (legacy — intentionally excluded; command in README) or expand multi-language code-example tabs (the `LANGUAGE_TAB_LABELS` guard in `fetcher.py`).

## Gotchas (most are session-earned, not visible in code)
- **Docusign renames products; live slugs redirect.** Navigator API → **Agreement Manager API**; Maestro API → **Workflow Builder API** (even the product page redirects). The scraper now records the **final URL** (`FetchResult.final_url`); crawl discovery derives its path-prefix bound from the post-redirect URL.
- **`searchDocusignDocs` (the Docusign MCP) is STALE** (indexed ~2025-10) — it still returns old `navigator-api` content. Don't trust it for current slugs/values; verify against the live site.
- **support.docusign.com is Salesforce Lightning** (empty JS shell to a plain fetch → must render). The same article has many URL variants (bundleId/topicId order, `.html`, `_LANG`); `canonical_url` (in `scraper/urls.py`) dedups them and keys the cache.
- **Crawls hit `--max-pages` caps silently.** After a crawl, check whether the per-host page count equals the cap; if so it's truncated — re-run with a higher cap (warm cache makes already-fetched pages instant). Happened with eSignature reference, App Center, CLM, Rooms.
- **Lazy-loaded UI on dev docs**: agreement-type category tabs only render the active tab → `_reveal_tabs` clicks through ARIA tabs; API reference schemas hide behind `aria-expanded` accordions → `_expand_disclosures`. **Still not handled**: `role="combobox"` schema-variant selectors (e.g. `getAgreement` per-agreement-type response templates) — deepest per-variant provision trees aren't captured.
- **`promote.py` overwrites `data/<set>/` from `output/<set>/`.** Running it against a *partial* output dir destroys the full dataset. For a single-page refresh, rebuild `data/<set>/` **in place** from its own `.md` files (see the inline scripts used in git history), don't promote from a 1-page output.
- **gh account drifts to `iamdocu`; pushes need `scooke-work`.** This clone has a local gh credential helper so `git push` works; if it 403s, `gh auth switch --user scooke-work`.
- **Shell**: `grep -c` exits non-zero when count is 0 and breaks `&&` chains (bit me on a commit). Live scrapes need `dangerouslyDisableSandbox: true`; long crawls run in background.

## Current state & next steps
- **Scraper is complete & hardened**; corpus = ~20 datasets under `data/` covering the full dev API surface (minus SOAP), AI products (Agents, Iris/AI Assistant), the IAM platform, core support, and the **Salesforce-integration stack** (IAM for Sales, Gen for Salesforce, eSignature/DAL for Salesforce, Agreement Prep). See README for the list and known-partial notes (CLM support = representative sample).
- **Salesforce / "Gen for SFDC <> IAM for Sales" use cases**: a user shared a relaunch plan (`~/Downloads/Recommendation on Gen for Salesforce <> IAM for Sales Relaunch.docx`) for an SC build guide (NDA, General Legal, 3rd-Party Paper, Quotes/SOW, CPQ). The 5 doc gaps it exposed are now **scraped** (the 4 `docusign-*-salesforce` / `iam-for-sales` / `agreement-prep` datasets). Next action if asked: **draft the SC step-by-step guide**, grounded in these new datasets + maestro-workflow + agreement-desk. APrep's WTA-vs-ATB autoplace template syntax is the one detail to confirm lives in `docusign-agreement-prep`.
- **Recent focus = reference docs in `docs/`**: `ai-extraction-fields.html` + `.md` document the Agreement Manager AI **extraction fields** and **obligations** — field types, the ⚡ auto-calculated fields, per-type fields, and full enum values. Obligation enum values (Status: Active/Fulfilled/Unfulfilled/Dependent; Frequency: One Time/Recurring; ISO-4217 currency) are **UI-only** — captured from user-provided screenshots, not in any public doc/API. There is **no obligations API** (Agreement Manager API exposes only `getAgreement`/`getAgreementsList`).
- **Loose ends / possible next actions**:
  - The **contract-hierarchy** concept visual was rendered inline (SVG) but **not saved to a file** — save to `docs/` if wanted.
  - Fill the remaining doc gaps only with grounded sources: `Discounts` obligation field type (undocumented), and the combobox-gated per-variant provision schemas.
  - If asked for more coverage: SOAP API, fuller CLM support, or non-Docusign sites (explicitly out of scope unless the user reopens it).
