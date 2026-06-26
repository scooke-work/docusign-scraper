# Docusign IAM — Product Summary

**Intelligent Agreement Management (IAM)** is Docusign's AI-powered platform for the
full agreement lifecycle (create → sign → manage → act). It's *a suite of
applications* powered by the **Docusign Iris** AI engine, sold as **editions**
(what you buy) made up of **applications/services** (what's inside).

> Source: IAM platform / IAM-for-Sales / per-product support docs in the corpus.
> These are the *documented* apps; Docusign repackages editions periodically, and
> two products were renamed (Navigator → Agreement Manager, Maestro → Workflow
> Builder). Early-access / extension items are flagged inline.

---

## Editions (packaged solutions)

### IAM Core
The general, build-your-own offering for teams that want to assemble their own
package. Comes in three plan levels — **Standard, Professional, Enterprise** —
with escalating feature allowances. Foundation for the role-specific editions.

### IAM for Sales
Streamlines sales contracting so sellers can create optimal deals more
independently, close faster, and extract more value over time. **CRM-native**
(Salesforce, HubSpot, Microsoft Dynamics). Bundles **Workflow Builder, App Center,
Admin, Agreement Manager, Data Verification, Monitor (extension), Gen for
Salesforce**, plus the **Docusign-for-Salesforce connector** (and eSignature,
Agreement Prep, Agreement Desk). Typical flow: generate quote/SOW → route intake/
approval in Agreement Desk → send via eSignature/DAL → analyze in Agreement Manager.

### IAM for CX (Customer Experience)
Simplifies and automates the agreement process for product managers and improves
the experience for their **end customers** — e.g. customer onboarding, service
agreements, renewals with verification and self-service signing.

### IAM for HR
Brings the employee-agreement process together — offer letters, onboarding,
policy acknowledgements — with **mobile I-9 verification** and **HCM integrations**.
*(Announced at Momentum '26; U.S. early access.)*

---

## Applications & platform services

### Docusign Agreement Manager  *(formerly Navigator)*
The **AI agreement repository** — store, manage, and analyze agreements from one
place. The Iris engine extracts structured data (agreement **type**/category,
**parties**, **provisions**, **obligations**) from uploaded or eSignature-completed
documents. Key surfaces: the **Completed Documents** list, the **Agreement preview**
page (AI-suggested values + data review), **Insights** dashboards (Overview,
Renewals, Obligations), **obligation management** (auto-surfaced payment/renewal/
termination + manual), **agreement hierarchies**, and the shared **Fields /
Agreement Types Managers** for custom types and fields. Roles: Administrators,
Contract Managers/Analyzers, Contract Viewers/End Users. **API:** Agreement Manager
API (`getAgreement` / `getAgreementsList`). See
[`ai-extraction-fields.md`](ai-extraction-fields.md) for the full field/obligation model.

### Docusign Agreement Desk
The **pre-signature workspace** — a single place for request intake, review,
negotiation, and approvals before an agreement is sent. Configurable **Request
Types** and **statuses**, owners, and an intake **Web Form** (with an Attachment
component for third-party paper). Includes the **AI-Assisted Review** add-in for
Microsoft Word, which checks contracts against **playbooks** and suggests markups,
plus an in-app chat. Drives downstream automation via Workflow Builder (Create a
Request / Get Document from a Request steps).

### Docusign Agreement Prep (Agreement Preparation)
The **"create" stage** — everything between deciding an agreement is needed and
sending it. **Document generation**: merge customer/product/pricing data into a
Word template to produce finished agreements, with **dynamic tables**, **conditional
rules** (show/hide content), and **sender/signer fields**. Two editors: **ATB
(Agreement Template Builder)** — streamlined, in-Docusign — and **WTA (Word Template
Assistant)** — a Word add-in with advanced syntax and precise formatting control.
Also: the **Template Assistant**, **Autoplacing Suggested Fields**, and third-party
data sources. Shares the unified **Fields Manager** with Agreement Manager.

### Docusign Workflow Builder  *(formerly Maestro)*
**No-code agreement workflow automation** — chain steps that extend beyond
eSignature without writing code. Step library includes triggers, **Web Forms**,
**eSignature**, **Data Verification**, **ID Verification**, **Agreement Desk**
requests, file store/export, branching/conditional logic, participants, and
variables — plus **Salesforce steps** (Read from / Writeback to / Use Salesforce
Files) and Salesforce-Flow triggers. Extensible through App Center apps. **API:**
Workflow Builder API.

### Docusign eSignature
The **core electronic-signature** product. Envelopes, **templates**, recipients and
routing, and a rich **tab/field** model (Sign Here, Initial, Date Signed, Text,
Number, Checkbox, Radio, Dropdown, **Formula/calculated** fields, etc.), including
conditional and data-replicated fields. Available across IAM editions. **APIs:**
eSignature REST (and legacy SOAP); deep Salesforce integration via DAL.

### Docusign Web Forms
**Online forms** based on an eSignature template (or standalone for data-only
collection) that recipients complete to provide data; a template-based form then
**generates an envelope**. Components include text, number, checkbox, radio,
dropdown, date, and **attachment**; supports conditional logic, prefill, and
embedded or remote delivery. **API:** Web Forms API.

### Data Verification (Connected Fields)
**Real-time verification** of signer-provided data during signing, via extension
apps that check values against a system of record. Supported field types: **email,
phone number, postal address** (with address auto-suggestion). Verification events
are reviewable in **Envelope History** and the **Certificate of Completion**. **API:**
Connected Fields API.

### Docusign Workspaces
A **collaborative agreement hub** that centralizes an agreement's documents, tasks,
and people in one space (newly global). Surfaces agreements for real-estate/mortgage
and general collaborative flows. **API:** Workspaces API.

### Docusign ID Verification (Identify)
**Identity verification** for signers — government ID, eID, and **Liveness** checks —
embedded into signing/workflow steps to confirm a signer is who they claim before
they access an envelope.

### Docusign App Center
The **marketplace of installable extension apps** that add functionality to
agreement processes (connected fields, cloud-storage/file input, data sources,
etc.). Admins install/auto-install and govern apps; the **Apps Launcher (DAL)**
packages Docusign apps (eSignature, Gen, CLM, Apex Toolkit) for Salesforce.

### Docusign Admin
**Centralized account administration** — users and permission profiles, branding,
security, and account settings — improving system-wide visibility and admin
efficiency across IAM apps.

### Docusign Monitor
**Activity and security tracking** — near-real-time monitoring of eSignature web/
mobile/API activity to detect threats; alerts, event export, and **Splunk**
integration. *(Available as an extension.)* **API:** Monitor API.

### AI Agents / Agent Studio
The **agentic layer** — ready-to-deploy agents (intake & triage, smart redlining,
relationship intelligence) and **Agent Studio** for building/governing custom agents
in natural language, grounded in agreement history and playbooks. Connects to
external AI tools via the **Docusign MCP Server**. *(U.S. early access.)*

---

## The AI engine

### Docusign Iris
The **agreement-tuned AI engine** behind the platform — trained to *identify,
classify, and extract* contract-specific concepts (not just summarize). Powers
Agreement Manager extraction, AI-Assisted Summaries & Q&A in eSignature,
AI-Assisted Review, and the AI Agents — with multilingual support. Not a standalone
app; it's the intelligence under the others.

### Gen for Salesforce  *(connector / IAM for Sales)*
**Document generation inside Salesforce** — merge CRM, product, and pricing data to
generate sales documents (quotes, SOWs) on the record, feeding the Agreement Desk /
eSignature flow. Bundled with IAM for Sales.
