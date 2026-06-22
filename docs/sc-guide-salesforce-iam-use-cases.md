# SC Build Guide — Docusign for Salesforce IAM Use Cases

A solutions-consultant walkthrough for building/demoing the **Gen for Salesforce ↔
IAM for Sales** use cases from the relaunch plan. Each recipe is grounded in the
scraped corpus (`data/docusign-iam-for-sales`, `-gen-for-salesforce`,
`-esignature-for-salesforce`, `-agreement-prep`, `-agreement-desk`,
`-maestro-workflow`). Page titles below map 1:1 to support articles in those sets.

> **Status:** v1 draft. Recipes follow the relaunch plan; validate exact clicks
> against the cited corpus pages and your org. Items the plan marks **(Roadmap)**
> or **P0/P1** are called out inline.

---

## 1. The five use cases (and how they're built)

| # | Use case | DocGen source | Prep / redline | Send | Phasing |
|---|----------|---------------|----------------|------|---------|
| 1 | **NDA** | APrep template (IAM-native) | Agreement Desk | Maestro/eSign | IAM (Q2→Q4) |
| 2 | **General Legal Requests** | 3P-DocGen / 1P (APrep) | Agreement Desk | IAM + EfS | 3P-DocGen+IAM+EfS → IAM |
| 3 | **3rd-Party Paper Contracts** | external (uploaded) | Agreement Desk (Web Form intake) | DAL/eSign | 3P-DocGen+IAM+EfS |
| 4 | **Basic Quotes / SOW / Sales Orders** | **Gen for Salesforce** | Agreement Desk | DAL/eSign (+ SF Flow) | Gen+IAM+EfS → IAM |
| 5 | **Salesforce CPQ Quotes** | **Gen for Salesforce** (CPQ data) | Agreement Desk | DAL/eSign | Gen+IAM+EfS → IAM |

**Product stack** (all included in the IAM for Sales license): eSignature,
Workflow Builder (Maestro), Agreement Prep (APrep), Agreement Desk (ADesk),
Agreement Manager, and the Docusign-for-Salesforce connector.

**APrep editor choice — WTA vs. ATB** (`Choosing Between Document Editors`):
- **WTA = Word Template Assistant** — Microsoft Word add-in; advanced syntax,
  rich native Word controls. **Use when the customer needs precise font,
  background, and page-layout formatting** (the plan's default recommendation).
- **ATB = Agreement Template Builder** — streamlined editor *inside* Docusign;
  upload a `.docx`, add sender/signer fields and conditional rules. Faster, simpler.

---

## 2. One-time setup (do this first)

Grounded in `data/docusign-iam-for-sales` and `-esignature-for-salesforce`.

1. **Install the packages in Salesforce**
   - `Install Docusign Apps Launcher in Your Salesforce Organization` (DAL — bundles
     eSignature, Gen, Apex Toolkit, CLM).
   - `Install the IAM for Salesforce Application (Salesforce Instructions)` (or via
     `Docusign App Center Instructions`).
2. **Connect & configure Workflow Builder for Salesforce**
   - `Getting Started with Workflow Builder for Salesforce`
   - `Configure Workflow Builder for Salesforce Fields and Settings`
   - `Access Required to Start Docusign Workflows from Salesforce`
3. **Stand up Agreement Desk for Salesforce**
   - `Step 1: Create an Agreement Desk for Salesforce External Object`
   - `Step 2: Create an Agreement Desk for Salesforce Report`
   - `Agreement Desk for Salesforce User Access`
4. **Add the Lightning components to your page layouts**
   - `Add the Docusign IAM Launcher Component to a Salesforce Layout`
   - `Add the Docusign Agreement Requests Component to a Salesforce Layout`
   - `Add the Docusign Completed Agreements Component to a Salesforce Layout`
   - `Add the Envelope Status Component to a Salesforce Layout`
   - `Adding Docusign Workflow Actions to Salesforce Layouts`

---

## 3. Building blocks — the Maestro Salesforce steps

These are the reusable Maestro steps the recipes compose. Each has a dedicated
corpus page (`Configure a … Step`).

| Step (plan name) | Maestro step / corpus page | Purpose |
|---|---|---|
| Data Read | **Read from Salesforce** | Pull Opportunity/record data into the workflow |
| Use File from Salesforce | **Use Salesforce Files** | Grab the latest file (e.g. Gen output) off the record |
| Create / Get Document from a Request | **Agreement Desk Workflow** step | Create an ADesk request; later retrieve its finalized doc |
| Store Files to Salesforce | **Store Files in Salesforce** | Save finalized agreement back to the SF record |
| Write to Salesforce | **Writeback to Salesforce** | Update fields (e.g. Opportunity Status) |
| Send Documents for Signature | **Send Documents for Signature** (+ `Add Salesforce Merge Fields…`) | Send the envelope |

**Triggers** (how a workflow starts):
- `Build a Workflow to Be Triggered By a Start with Docusign Action` (user clicks
  *Start with Docusign* on a record)
- `Build a Workflow to Be Triggered By Agreement Desk Requests` (request status
  changes drive downstream workflows)
- `Build a Docusign Workflow to Be Started By a Salesforce Flow` +
  `Configure a Start Docusign Workflow Step in Salesforce Flow` (headless / automation)

**Step configuration notes** (verified from the corpus):
- *Prereq for every SF step:* install the **Salesforce app from Docusign App
  Center** and start from a base workflow (`Installing Extension Applications for
  Workflow Builder`).
- **Read from Salesforce** — as admin, **map workflow fields ↔ Salesforce fields**;
  recipients then see imported record data on the envelope.
- **Use Salesforce Files** — provide the **record ID**; Docusign pulls files from
  the record's **Notes & Attachments**. Upload mode: **All Files**, **File Name
  Contains**, or **Latest Document Only** (use *Latest Document Only* for the Gen
  output in UC4/UC5).
- **Agreement Desk step** — *+ Add a step → Agreement Desk → Create a Request*,
  then pick the **Request type** (the type wired to your intake Web Form).
- **Writeback to Salesforce** — map **workflow fields ↔ Salesforce fields**; this
  one step can **update fields** (e.g. Opportunity Status), **save documents to the
  record**, and **create new records** — i.e. it covers the plan's "Store Files to
  Salesforce" + "Write to Salesforce" + "Update Opty Status."

---

## 4. Use-case recipes

> All recipes assume the Opportunity status begins at **"Proposal/Price Quote."**

### UC1 — NDA (IAM-native, APrep template)

Pattern: `[ADesk Request] → [APrep – WTA] → [Maestro (Automated) or ADesk (Manual) / Send for Signature]`
**Recommended template: WTA** (precise formatting). Demo customers: *Seismic (MSA), Firework.*

- **Prereq:** build the NDA document-generation template in **APrep/WTA**
  (`Create a Document Generation Template with the Agreement Template Builder` /
  `Docusign Template Assistant for Word`; add sender fields; `Autoplacing Suggested
  Fields` for signature placement).
- **Workflow 1 — Request Submission** (trigger: Start with Docusign action / API call)
  1. **Read from Salesforce** (Opportunity data)
  2. **Agreement Desk step → Create a Request**
- **Workflow 2 — Generate Document using APrep** (trigger: ADesk Request Status = `New`; start when `Submitted`)
  1. **Preparing Document** using the *WTA* document template
- **Workflow 3 — Redlining Completed** (trigger/start: ADesk Request Status = `Ready for Signature`)
  1. **Agreement Desk step → Get Document from a Request** *(Roadmap: choose the
     APrep-generated doc)*
  2. **Send Documents for Signature**

### UC2 — General Legal Requests

Same skeleton as UC1, but DocGen may be **3P-DocGen or 1P (APrep)** depending on
phase (`3P-DocGen/1P + IAM + EfS` → fully `IAM` by Q4). Reuse the UC1 workflows;
swap the template/source as needed. Use **ADesk** for intake + redline.

### UC3 — 3rd-Party Paper Contracts (uploaded paper)

Pattern: `[3P-PAPER] → [ADesk Request] → [DAL/eSign (Manual) / Send for Signature]`
Send via **either** IAM for Sales *Send for Signature* **or** DAL/eSign.
Demo customers: *HydroCorp, ARK Data Center, AGI Net.*

- **Key intake step:** in the **ADesk Web Form**, include the **Attachment
  component** in the Intake form (the Attachment component is a Web Forms feature —
  see `docusign-web-forms`; wire it to the request via the ADesk **Request Type**,
  `docusign-agreement-desk` → `Create a New Request Type`). Users upload the
  third-party paper from their local repository during request submission.
- **Workflow 1 — Request Submission**
  1. **Read from Salesforce**
  2. **Agreement Desk step → Create a Request** (Web Form requires the uploaded 3P doc)
- **Workflow 2A — Redlining Completed** (start: Request Status = `Ready for Signature`)
  1. **Get Document from a Request** *(Roadmap: Get all Documents)*
  2. **Store Files in Salesforce**
  3. **Writeback to Salesforce** → set Opportunity Status = `Negotiation / Review`
     *(final status TBD with the deal team)*
  4. Send via DAL/eSign (manual) or the IAM send step.

### UC4 — Basic Quotes / SOW / Sales Orders (Gen for Salesforce)

Pattern (P0 manual): `[3P DocGen = Gen for SFDC] → [ADesk Request] → [DAL/eSign in SF — MANUAL]`
Pattern (P1 automation): `… → [DAL/eSign in SF — AUTOMATION / headless]`
Demo customer: *Seismic (SOW).*
**Gen for Salesforce is the DocGen engine; ADesk handles redline/approval; DAL/eSign sends.**

- **Prereq:** Gen for Salesforce generates the quote/SOW doc and saves it to the
  record (`docusign-gen-for-salesforce` → `Generate Agreements` / template setup).
- **Workflow 1 — Request Submission**
  1. **Read from Salesforce**
  2. **Use Salesforce Files** — *Latest Document Only* (the Gen-generated doc on the record)
  3. **Agreement Desk step → Create a Request**, Documents: **Include all documents**
     (runtime grabs the latest file from the CRM record and adds it to the ADesk request)
- **Workflow 2 — Redlining Completed** (start: Request Status = `Ready for Signature`)
  1. **Get Document from a Request** *(Roadmap: Get all Documents)*
  2. **Store Files in Salesforce**
  3. **Writeback to Salesforce** → Opportunity Status = `Negotiation / Review`
- **Workflow 3 — Salesforce Flow → Send for Signature** *(automation path only; the
  manual send path skips this)*
  - Triggered by Status = `Negotiation / Review`; SF Flow Action **Send for Signature**
    using the *Latest File from the Opportunity record*
    (`Build a Docusign Workflow to Be Started By a Salesforce Flow`).

### UC5 — Salesforce CPQ Quotes

Same as UC4 (`Gen + IAM + EfS`), with **Salesforce CPQ** as the data/quote source feeding
Gen for Salesforce. Build the Gen template against CPQ quote line data, then reuse the
UC4 workflows (Read → Use Salesforce Files → ADesk → redline → Store/Writeback → send).

---

## 5. Phasing (from the relaunch plan)

| Use Case | Q2 (May) | Q3 | Q4 |
|---|---|---|---|
| NDA | IAM | IAM | IAM |
| General Legal Requests | 3P-DocGen/1P + IAM + EfS | 3P-DocGen/1P + IAM + EfS | IAM |
| 3rd-Party Paper Contracts | 3P-DocGen + IAM + EfS | 3P-DocGen + IAM + EfS | — |
| Basic Quotes/SOW & Sales Orders | Gen + IAM + EfS | Gen + IAM + EfS | IAM |
| Salesforce CPQ Quotes | Gen + IAM + EfS | Gen + IAM + EfS | IAM |

---

## 6. Open items to confirm before a customer build

- **Final Opportunity statuses** for write-back (plan flags "Negotiation / Review
  (or other status — to be discussed)").
- **Roadmap-gated steps**: "Get all Documents," "choose the APrep-generated doc,"
  and the auto-include-latest-file behavior are marked Roadmap in the plan — verify
  GA status before committing to a demo.
- **Send path per use case**: manual (P0) vs. headless Salesforce Flow (P1).

## 7. Reference map (corpus)

- Setup & SF steps → `data/docusign-iam-for-sales/`
- DocGen engine → `data/docusign-gen-for-salesforce/`
- Send / DAL / SF Flow → `data/docusign-esignature-for-salesforce/`
- Template authoring (WTA/ATB, syntax, autoplace) → `data/docusign-agreement-prep/`
- Request intake / Web Form attachment / redline → `data/docusign-agreement-desk/`
- Workflow engine fundamentals → `data/docusign-maestro-workflow/`
