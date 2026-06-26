# Docusign AI Extraction Fields & Obligations

A reference for the **Agreement Manager (Iris)** AI extraction fields and agreement
**obligations** — field types, enum values, and which fields are automatically set.
Legend: `⚡` = automatically set / calculated.

Type vocabulary: **date · duration · number · currency · enum · boolean · text**
(API data types: `string · number · datetime · duration · enum · boolean`).

---

## Part 1 — AI Extraction Fields

### Automatically set (derived from other fields)

| Field | Type | How it's set |
|-------|------|--------------|
| ⚡ **Status** | enum | Calculated from **Effective Date**, **Expiration Date** & **Renewal Type**. Auto-calc is on by default; setting it manually stops the calculation. |
| ⚡ **Notice date** (`renewal_notice_date`) | date | = **Expiration Date** − **Notice period**. |

### Top-level insights

| Field | Type |
|-------|------|
| `type` | enum (49 values) |
| `category` | enum |
| `parties` | object[] |
| ⚡ `status` | enum |
| `languages` | string[] |

### Provisions (field-level extractions)

| Group | Field | Type |
|-------|-------|------|
| **Dates & term** | `effective_date` | date |
| | `expiration_date` | date |
| | `execution_date` | date |
| | `term_length` | duration |
| **Value** | `total_agreement_value` | number |
| | `total_agreement_value_currency_code` | currency |
| | `annual_agreement_value` | number |
| | `annual_agreement_value_currency_code` | currency |
| **Renewal** | `renewal_type` | enum |
| | `renewal_notice_period` | duration |
| | ⚡ `renewal_notice_date` | date |
| | `auto_renewal_term_length` | duration |
| | `renewal_extension_period` | duration |
| | `renewal_process_owner` | text |
| | `renewal_additional_info` | text |
| **Liability cap** | `liability_cap_fixed_amount` | number |
| | `liability_cap_currency_code` | currency |
| | `liability_cap_multiplier` | number |
| | `liability_cap_duration` | duration |
| **Payment & pricing** | `payment_terms_due_date` | enum |
| | `can_charge_late_payment_fees` | boolean |
| | `late_payment_fee_percent` | number |
| | `price_cap_percent_increase` | number |
| **Assignment** | `assignment_type` | enum |
| | `assignment_change_of_control` | enum |
| | `assignment_termination_rights` | enum |
| **Termination** | `termination_period_for_cause` | duration |
| | `termination_period_for_convenience` | duration |
| **Governing** | `governing_law` | text |
| | `jurisdiction` | text |

### Document Details panel — fields by category (UI rendering)

How the Agreement preview **Details pane** — titled **"Review & edit details"**
(AI‑Assisted) — groups the standard fields for display. **Agreement Type** sits at
the top, above the category groups; the remaining fields render under five category
headers in this order. Each category shows a review‑progress counter — **General**
lists **13** fields (confirmed live: *"Reviewed 0/13"*), matching the table below.
`⚡` = auto‑set.

> Verified against the corpus: the category set (General · Termination · Renewal ·
> Payment · Legal and Compliance · Other) matches the Fields Manager *Category*
> classification, and all display names are corroborated **except** the two marked
> `†` below — *Original File Name* and the three *Assignment (…)* sub‑fields — which
> reflect live‑UI granularity (the scraped docs show a single *Assignment* and only
> *File Name*). *Other* / *Human Resources* carry no standard fields (they're for
> custom fields), so they don't appear here.

**▸ Agreement Type** → `type` · enum (49 values)

| Category | Field (UI) | Maps to | Type |
|----------|-----------|---------|------|
| **General** | Status | ⚡ `status` | enum |
| | Title | (agreement title) | text |
| | Parties | `parties` | object[] |
| | Line of Business | `line_of_business` | enum |
| | Total Contract Value | `total_agreement_value` (+ currency) | number |
| | Annual Contract Value | `annual_agreement_value` (+ currency) | number |
| | Execution Date | `execution_date` | date |
| | Effective Date | `effective_date` | date |
| | Expiration Date | `expiration_date` | date |
| | Initial Term Length | `term_length` | duration |
| | Original File Name `†` | (source file metadata) | text |
| | File Name | (file metadata) | text |
| | Languages | `languages` | string[] |
| **Termination** | Termination for Cause – Notice Period | `termination_period_for_cause` | duration |
| | Termination for Convenience – Notice Period | `termination_period_for_convenience` | duration |
| **Renewal** | Renewal Type | `renewal_type` | enum |
| | Renewal Notice Period | `renewal_notice_period` | duration |
| | Renewal Notice Date | ⚡ `renewal_notice_date` | date |
| | Renewal Term | `auto_renewal_term_length` | duration |
| | Extension Period | `renewal_extension_period` | duration |
| | Renewal Owner | `renewal_process_owner` | text |
| | Additional Info | `renewal_additional_info` | text |
| **Payment** | Payment Terms | `payment_terms_due_date` | enum |
| | Late Fees Apply | `can_charge_late_payment_fees` | boolean |
| | Late Fee % | `late_payment_fee_percent` | number |
| | Price Cap Increase % | `price_cap_percent_increase` | number |
| | Liability Cap Amount | `liability_cap_fixed_amount` (+ currency) | number |
| | Liability Cap Multiplier | `liability_cap_multiplier` | number |
| | Liability Cap Duration | `liability_cap_duration` | duration |
| **Legal and Compliance** | Assignment (General) `†` | `assignment_type` | enum |
| | Assignment (Change of Control) `†` | `assignment_change_of_control` | enum |
| | Assignment (Termination Rights) `†` | `assignment_termination_rights` | enum |
| | Governing Law | `governing_law` | text |
| | Jurisdiction | `jurisdiction` | text |

`†` live‑UI granularity not in the scraped docs (see note above). Which of these
fields actually appear for a given agreement depends on its type — see
[Fields available by agreement type](#fields-available-by-agreement-type).

### Enum values

**`category`** (agreement‑type classification) — `BusinessServices` · `HumanResources` · `Miscellaneous`

**Line of Business** (`line_of_business`, dropdown — verified live UI) — **Human Resources** *(Employee data appears)* · **Sales** *(You are the seller)* · **Procurement** *(You are the buyer)* · **Unspecified**

**`status`** (agreement) — UI: `Active` / `Inactive` · API: `PENDING` / `COMPLETE` / `INACTIVE`

**`renewal_type`** — Auto-Renew · Evergreen · Fixed Term · Renewal Option · Unspecified · Other

**`assignment_type`** — No, or consent required · Yes · Yes, with conditions · Other

**`assignment_change_of_control`** — No, or consent required · Yes, notice required · Yes, restrictions apply · Yes, with conditions · Other

**`assignment_termination_rights`** — Yes · Other

**`payment_terms_due_date`** — Under 7 days · 7 days · 15 days · 30 days · 45 days · 60 days · 90 days · >90 days · On Receipt · Other

**Type-specific enum fields** (surface for certain agreement types):
- **NDA Type** — Mutual · One Way
- **Employment Type** — Fixed Term · Full Time · Intern · Part Time
- **Party Role** — Buyer · Seller
- **Late Fees Apply** — Yes · No

> **Notes:** `Other` is the universal catch-all returned when the AI cannot locate
> the value. The API returns equivalent `UPPER_SNAKE_CASE` codes (Auto-Renew →
> `AUTO_RENEW`, Yes, with conditions → `YES_WITH_CONDITIONS`, 30 days →
> `THIRTY_DAYS`; `SILENT` appears for unspecified). Value sets are English (U.S.)
> and vary slightly by language.
>
> **Custom field types:** When you **create a custom field** (Fields Manager →
> *Add a field*), the Field type choices are **Text · Number · Date · Dropdown ·
> Currency** (verified from the live UI — the published support docs are stale and
> list only the first four). The same set are the standard-field type indicators
> shown in the Fields Manager. **Category** choices: General · Termination ·
> Renewal · Payment · Legal and Compliance · Other. `custom_provisions` hold the
> resulting user-defined terms.

### `type` enum — 49 standard agreement types (by category)

**Business Services (26):** Certificate of Insurance · Consulting Agreement · Credit Card Agreement · Engagement Letter · Franchise Agreement · Investment Account Agreement · Joint Venture Agreement · Letter of Intent · Loan agreement · Marketing agreement · Master Service Agreement · Memorandum of Understanding · Non-disclosure Agreement · Order Form · Partnership Agreement · Proposal agreement · Purchase Agreement · Purchase Order · Quote agreement · Service Level Agreement · Services Agreement · Statement of Work · Stock Purchase Agreement · Subscription agreement · Supply / Distribution agreement · Wealth Management Agreement

**Miscellaneous (20):** Addendum agreement · Amendment agreement · Appendix agreement · Attachment agreement · Change Order agreement · Event agreement · Exhibit agreement · Fee agreement · Intellectual Property Assignment Agreement · Lease agreement · License agreement · Miscellaneous agreement · Privacy and Security agreement · Publishing Agreement · Release / Waiver agreement · Renewal agreement · Retainer agreement · Supplemental Document · Termination agreement · Terms and Conditions agreement

**Human Resources (3):** Contractor Agreement · Employment Separation Agreement · Offer Letter

*(Plus organization-defined custom agreement types.)*

### Fields available by agreement type

Every type includes the **universal fields**: Title · Parties · Execution Date · Effective Date · Expiration Date · Status · Line of Business. The table below shows which *additional* standard fields each type surfaces (✓ = present). **Non-agreement** types (Application, Certificate, Invoice, etc.) are included at the bottom.

> Verified against Docusign's *Standard Fields for Agreement and Non-Agreement Types* support article. Addendum/Amendment notably omit **Governing Law**; Employment Separation has only **Termination for Convenience**; Terms and Conditions has no **Total Contract Value**.

| Agreement type | TCV | ACV | Term | Renew | Pay | LateFee | PriceCap% | LoLCap | Assign | GovLaw | Juris | TrmCause | TrmConv | Extra |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:| --- |
| Master Service Agreement / Statement of Work | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Non-Disclosure Agreement | ✓ | · | ✓ | ✓ | · | · | · | · | ✓ | ✓ | ✓ | ✓ | ✓ | NDA Type, Confidentiality Duration |
| Change Order | ✓ | · | · | · | ✓ | · | · | · | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Addendum / Amendment | ✓ | · | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ |  |
| Lease / License / Services Agreement / Supply/Distribution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Purchase Order | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · |  |
| Engagement Letter | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Fee | ✓ | · | · | · | ✓ | · | · | · | ✓ | · | ✓ | ✓ | ✓ |  |
| Letter of Intent | ✓ | · | · | · | ✓ | · | · | · | · | · | ✓ | ✓ | ✓ |  |
| Memorandum of Understanding | ✓ | · | · | · | ✓ | · | · | · | · | ✓ | ✓ | ✓ | ✓ |  |
| Order Form | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Proposal / Quote | ✓ | · | · | · | ✓ | · | · | · | ✓ | · | ✓ | ✓ | ✓ |  |
| Retainer | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Service Level Agreement | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Terms and Conditions | · | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Appendix / Attachment / Exhibit | ✓ | · | ✓ | · | · | · | · | · | · | · | · | · | · |  |
| Supplemental Document | ✓ | · | ✓ | · | · | · | · | · | ✓ | ✓ | ✓ | · | · |  |
| Contractor Agreement / Consulting Agreement | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Franchise Agreement / Purchase Agreement | ✓ | · | ✓ | ✓ | ✓ | · | · | · | · | ✓ | ✓ | ✓ | ✓ |  |
| Partnership Agreement | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Joint Venture Agreement | ✓ | · | ✓ | ✓ | ✓ | · | · | · | · | ✓ | ✓ | ✓ | ✓ |  |
| Offer Letter | ✓ | · | · | · | ✓ | · | · | · | · | ✓ | ✓ | ✓ | ✓ |  |
| Intellectual Property Assignment Agreement / Publishing Agreement / Investment Account Agreement / Wealth Management Agreement / Credit Card Agreement | ✓ | · | ✓ | · | ✓ | · | · | · | · | ✓ | ✓ | ✓ | ✓ |  |
| Employment Separation Agreement | ✓ | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ |  |
| Certificate of Insurance | · | · | ✓ | · | · | · | · | · | ✓ | · | ✓ | ✓ | ✓ |  |
| Event / Marketing | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Loan / Miscellaneous / Subscription | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Privacy and Security | ✓ | · | ✓ | ✓ | · | · | · | · | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Release/Waiver | · | · | ✓ | · | · | · | · | · | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Renewal | · | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | · | ✓ | · | · |  |
| Stock Purchase Agreement | ✓ | · | ✓ | ✓ | · | · | · | · | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| Termination | · | · | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| **Non-agreement:** Application / Certificate / Form / Handbook / Notice / Plan / Policy / Report / Summary | · | · | · | · | · | · | · | · | · | · | · | · | · | universal fields only |
| **Non-agreement:** Invoice | ✓ | · | · | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | · |  |

**Non-agreement types** — *Application / Certificate / Form / Handbook / Notice / Plan / Policy / Report / Summary*: universal fields only. **Invoice**: universal + Total Contract Value, Renewal, Payment Terms, Late Payment Fee, Price Cap %.

> Source: *Standard Fields for Agreement and Non-Agreement Types* (Agreement Manager support). NDA is the only type with extra fields (NDA Type, Confidentiality Duration). Note: Amendment/Addendum omit Governing Law; lightweight types (NDA, LOI, MOU, Fee, Proposal/Quote, Offer Letter) omit the financial cluster (ACV, Late Payment Fee, Price Cap %, LoL Cap).

---

## Part 2 — Agreement Obligations

The fields on an obligation record. Obligations are **auto-surfaced by AI**
(payment, renewal, termination) during processing — **English (U.S.) only** — or
created manually.

### Automatically set / AI-driven

| | Detail |
|---|---|
| ⚡ **Notice date** | = **Expiration Date** − **Notice period**. Present on **renewal & termination** obligations; all other types use a directly-entered **Due date**. |
| ⚡ **AI auto-surfacing** | AI surfaces **Payment**, **Renewal** & **Termination** obligations and their fields during processing. All other types are **created manually**. |

### Obligation fields

| Field | Type | Notes |
|-------|------|-------|
| **Obligation Name** | text | required |
| **Type** | enum | |
| **Status** | enum | |
| **Owner** | text | assignee (name/email) |
| **Obligated Party** | text | the contractual party |
| **Due Date** | date | non-renewal/termination types |
| **Notice Period** | duration | renewal & termination only |
| ⚡ **Notice Date** | date | renewal & termination only |
| **Payment Value** | number + currency | payment only |
| **Frequency** | enum | payment only |
| **Discounts** | text | AI-extracted attribute (see note) |
| **Repercussions** | text | |
| **Description** | text | |

### Fields by obligation type

| Obligation type | Type-specific fields |
|-----------------|----------------------|
| **Payment** (One-Time / Deposit) | Payment Value · Due Date · Frequency · Discounts |
| **Renewal** (Renewal Notice) | Notice Period · ⚡ Notice Date |
| **Termination** (Cause / Convenience Notice) | Notice Period · ⚡ Notice Date |
| **All other types** | Due Date |

*Common to every type:* Obligation Name · Type · Status · Owner · Repercussions · Description

### Enum values

**Type — 15 standard (+ custom):** Compliance · Confidentiality · Data Breach · Escalation · Indemnification · Insurance · Limitation of Liability · Miscellaneous · Notification · Payment · Renewal · Service Level Agreements · Subcontracting · Termination · Warranties *(verified from live UI; the support doc lists "Renewal notification" / "Warranty")*
*(plus organization-defined custom types; AI auto-surfaces only Payment, Renewal & Termination).*

**Status** — `Active` · `Fulfilled` · `Unfulfilled` · `Dependent`

**Frequency** (payment obligations) — `One Time` · `Recurring`

**Payment value currency** — ISO 4217 currency codes (USD, EUR, GBP, AED, AFN, ALL, AMD, ANG, AOA, ARS, …)

> **✓ Verified from the live UI** (Edit Obligation screen). The Status, Frequency,
> and currency values above are **not** published in Docusign's help docs or API —
> captured from the product UI.
>
> **No obligations API:** the Agreement Manager API exposes only `getAgreement` /
> `getAgreementsList` — obligations are a UI/product feature with no API endpoint.
>
> **Discounts** appears as an AI-extracted attribute but is not a field in the Edit
> Obligation form; its type is undocumented.

---

### Sources

- Agreement Manager API schema & reference; openapi-navigator schema definitions
- Agreement Manager support: Fields Manager, Update Agreement Status, Extracted
  Agreement Insights & Definitions, Obligation Management, Manually Create an
  Obligation, Custom Obligation Types
- Obligation enum values verified from the live Edit Obligation UI
