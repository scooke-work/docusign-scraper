# docs/ — Docusign reference set

Curated, human-readable references distilled from the scraped corpus under
[`../data/`](../data). Each is grounded in the support/developer docs (and, where
noted, verified against the live UI from screenshots). Start here.

## Products & platform
- **[iam-products.html](iam-products.html)** — visual **product map** (open in a
  browser): a layered diagram of the editions, the applications grouped by
  agreement lifecycle (Create → Sign → Manage → Automate), platform services, and
  the Iris engine underneath.
- **[iam-coverage-matrix.html](iam-coverage-matrix.html)** — **edition × application
  coverage matrix**: which apps each edition (Core / CX / Sales / HR) bundles, with
  a confidence legend (included vs. base-platform vs. not-documented).
- **[product-embedding.md](product-embedding.md)** — **product-in-product
  embedding**: which products surface another product inside their UI (Workflow
  Builder steps, Agreement Manager panes, eSignature signing, Salesforce DAL,
  Word add-ins, App Center, MCP/Copilot), grouped by host with a quick matrix.
- **[iam-products.md](iam-products.md)** — Docusign IAM product summary: the
  editions (IAM Core / Sales / CX / HR) and every application (Agreement Manager,
  Agreement Desk, Agreement Prep, Workflow Builder, eSignature, Web Forms,
  Connected Fields, Workspaces, ID Verification, App Center, Admin, Monitor, AI
  Agents) plus the Iris engine — each with a deeper summary.

## Agreement Manager — AI extraction & obligations
- **[ai-extraction-fields.html](ai-extraction-fields.html)** — visual reference
  (open in a browser): extraction field types, enum values, the auto-calculated
  fields, the 49 agreement types, the per-type field matrix, and the obligations
  model. *(Verified field/enum values incl. live-UI corrections.)*
- **[ai-extraction-fields.md](ai-extraction-fields.md)** — the same content in
  Markdown (tables/lists).
- **[contract-hierarchy.html](contract-hierarchy.html)** — visual of the
  Agreement Hierarchies concept (primary agreement + related documents).
- **[agreement-manager-ui-screens.md](agreement-manager-ui-screens.md)** — the UI
  screen inventory (pages, panes, dashboards, managers, dialogs) named in the
  Agreement Manager docs.
- **[iris-chat-entry-points.md](iris-chat-entry-points.md)** /
  **[.html](iris-chat-entry-points.html)** — where the Iris‑powered chat / Q&A
  surfaces can be initiated (Agreement Desk request record · document preview ·
  Word add‑in; eSignature "Ask a question"; agent/MCP/Copilot), with a visual.

## Salesforce / IAM-for-Sales build guide
- **[sc-guide-salesforce-iam-use-cases.md](sc-guide-salesforce-iam-use-cases.md)** —
  SC walkthrough for the Gen-for-Salesforce ↔ IAM-for-Sales use cases (NDA,
  General Legal, 3rd-Party Paper, Quotes/SOW, CPQ): setup, the Maestro Salesforce
  step building blocks, the WTA-vs-ATB editor decision, and per-use-case recipes.

---

**Caveats.** These reflect the docs as scraped (a point in time). Docusign renames
and repackages products, and the live UI can lead the published docs — items
verified from live screenshots are flagged inline. The data behind these docs
lives in `../data/<dataset>/` (Markdown + `chunks.jsonl` + `manifest.json`); see
the top-level [`../README.md`](../README.md) for the scraper and dataset list, and
[`../CLAUDE.md`](../CLAUDE.md) for maintenance notes and known gaps.
