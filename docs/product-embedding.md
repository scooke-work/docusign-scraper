# Docusign product-in-product embedding

Which Docusign products **surface or embed another product inside their own UI** —
i.e. where you see/operate product B from within product A. Grouped by **host**
(the UI you're in) → **embedded** (what shows up there) → **how**.

> Grounded in the scraped corpus. Mechanisms: **step** (Workflow Builder),
> **pane/view** (Agreement Manager), **extension app** (App Center), **add‑in**
> (Microsoft Word), **package** (Salesforce / DAL). Items inferred from product
> framing rather than an explicit screen are flagged *(inferred)*.

---

## A. Host = another Docusign app

### Workflow Builder *(Maestro)* — embeds products as **steps**
The richest host: each step runs another product inside the workflow canvas.
- **Web Forms** — *Collect Data with Web Forms* step
- **eSignature** — *Get Signatures* / *Send Documents for Signature* step (uses your account templates)
- **ID Verification** — *Verify Someone's Identity* (IDV) step
- **Data Verification / Connected Fields** — verification within send steps *(inferred)*
- **Agreement Desk** — *Agreement Desk* step (*Create a Request*)
- **Salesforce** — *Read from / Write back to / Use Salesforce Files* steps (embeds CRM data)

### eSignature *(envelope / signing experience)* — embeds into the signing UI
- **Connected Fields / extension apps** — data‑verification fields shown **during signing**; results land in Envelope History & the Certificate of Completion
- **ID Verification** — identity/Liveness check gates access to the envelope
- **Web Forms** — a form feeds and generates the envelope
- **Signing AI (Iris)** — "Ask a question" Q&A on the open document *(see [iris-chat-entry-points.md](iris-chat-entry-points.md))*

### Agreement Manager — embeds via **panes / views**
- **eSignature** — completed envelopes ingest into **Completed Documents** (Envelope ID column, *Envelopes* view)
- **CLM** — read‑only **CLM Attributes** pane on the Agreement preview page (CLM customers, IAM Enterprise)
- **Iris** — AI suggestions / extraction surfaced inline on the preview

### Agreement Desk — embeds into the request workspace
- **AI‑Assisted Review (Iris)** — document **preview + Chat/playbooks** inside the request
- **eSignature** — send the request's documents for signature *(inferred)*
- **Web Forms** — intake form that opens a request

### App Center — the **delivery mechanism**
- Surfaces installed **extension apps** (connected fields, cloud‑storage/file input, data sources) **inside host products** — eSignature, Workflow Builder, Agreement Desk. App Center is *how* B gets into A's UI.

### IAM platform / Docusign Home — the **shell**
- Top‑level launcher that displays the entitled apps (and App Center apps) as tiles/nav.

---

## B. Host = a third‑party product *(Docusign embedded elsewhere)*

### Salesforce — via the **Docusign Apps Launcher (DAL)** package
DAL packages multiple Docusign products into the Salesforce UI:
- **eSignature** (send/sign from records)
- **Gen for Salesforce** (document generation on the record)
- **CLM** (CLM for Salesforce)
- **Negotiate** / **Apex Toolkit** *(part of the DAL bundle)*

### Microsoft Word — via **add‑ins**
- **AI‑Assisted Review (Agreement Desk / Iris)** — chat, summaries, playbook markup inside Word
- **Agreement Prep — Word Template Assistant (WTA)** — template authoring inside Word

### AI clients / low‑code — via **connector / MCP** *(early access / Beta)*
- **Microsoft Copilot Studio** — build/run a Docusign **agent**; chat from the Test pane
- **MCP Server** — Docusign tools exposed to **Claude · Gemini · ChatGPT**
- **HubSpot, Microsoft Dynamics** — IAM‑for‑Sales CRM‑native surfaces *(inferred from "CRM‑native"; not detailed in corpus)*

---

## Quick matrix (host → what it can display)

| Host UI | Embedded Docusign products |
|---|---|
| **Workflow Builder** | Web Forms · eSignature · ID Verification · Data Verification · Agreement Desk · Salesforce data |
| **eSignature signing** | Connected Fields/extension apps · ID Verification · Web Forms · Signing AI (Iris) |
| **Agreement Manager** | eSignature (envelopes) · CLM (attributes) · Iris |
| **Agreement Desk** | AI‑Assisted Review (Iris) · eSignature · Web Forms |
| **App Center (into hosts)** | extension apps → eSignature, Workflow Builder, Agreement Desk |
| **Salesforce (DAL)** | eSignature · Gen · CLM · Negotiate · Apex Toolkit |
| **Microsoft Word** | AI‑Assisted Review (Iris) · Agreement Prep WTA |
| **Copilot Studio / MCP clients** | Iris agents · Docusign tools (Claude/Gemini/ChatGPT) |

*Caveats:* reflects documented integrations at scrape time. *(inferred)* items follow
from product positioning but aren't tied to a specific screen in the corpus —
confirm against the live UI. See [iam-products.md](iam-products.md) for the products
themselves and [iam-products.html](iam-products.html) for the platform map.
