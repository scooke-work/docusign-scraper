---
title: ': getAgreementsList'
source_url: https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreementslist/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Agreement Manager API
- Agreement Manager API
- API Reference
- API Reference
- Agreementmanager
- Agreementmanager
- Agreements
- Agreements
- Getagreementslist
scraped_at: '2026-06-18T14:17:04Z'
---

[Agreements](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/)

# : getAgreementsList

This operation retrieves a list of all agreements available in the system. It provides a high-level overview of each agreement, including its unique identifier (`id`), title, type, status, and involved parties. The list also includes important metadata, such as the agreement's creation and modification timestamps, and information on the agreement's source system (e.g., eSign, CLM).

Each agreement entry includes essential details that allow users to quickly assess the agreements and determine which ones are relevant for their needs. For example, the agreement's status can help users understand whether an agreement is still active, pending, or completed.

The response also includes provisions that outline the key legal, financial, and lifecycle conditions, along with custom user-defined fields, providing a comprehensive understanding of each agreement.

### Use Cases:

- **Retrieving a list of agreements for integration into external systems**: Export or sync agreement data into other platforms (e.g., CRM, ERP systems) to align business processes across different tools.
- **Providing data for RAG (Retrieval-Augmented Generation) applications or Copilots**: The list of agreements can be a valuable data source for AI/LLM-based applications that answer user queries about agreements.
  It allows Copilots to understand what agreements exist and offer insights based on their details.
- **Filtering agreements by type or status**: Determine which agreements are active, pending, or completed, and gather a summary of key provisions across multiple agreements.
- **Auditing or reporting**: Generate a report on agreements based on type, status, or date created, helping with compliance tracking and internal reviews.
- **Metadata tracking**: Track when agreements were created, modified, and by whom, ensuring proper governance and version control.

### Key Features:

- **Comprehensive Agreement Overview**: Provides high-level visibility into all agreements, with essential details for each one, including status, type, and involved parties.
- **Metadata and Provisions**: Returns important metadata and provisions (legal, financial, and custom) for each agreement, helping users understand their obligations and contract terms.
- **Source System Information**: Captures details about where the agreement originated (e.g., eSign, CLM), making it easier to integrate and track agreements across different business systems.
- **Data for AI Applications**: The operation is designed to support LLM-powered apps, making it ideal for use in RAG-based applications and Copilots that query agreements for decision-making or information purposes.

HTTP Request

GET

```
/v1/accounts/{accountId}/agreements
```

Base URL : Demo

```
https://api-d.docusign.com
```

## Request

Query Parameters

limit

---

PageLimit

Use example values

10

The maximum number of items that can be returned in a single page.

format: int32

minimum: 1

ctoken

---

ContinuationToken

Use example values

abc123

An opaque token that helps retrieve the a page of data.

$search

---

string

Use example values

/agreements?$search=Acme

OData full-text search expression. Performs a case-insensitive search across agreement text fields including title, type, parties, and provisions.

The search term is matched as a substring against searchable fields. Enclose multi-word terms in double quotes for exact phrase matching.

Examples:

- `$search=Acme` — matches agreements mentioning "Acme" in any searchable field
- `$search="Non-Disclosure Agreement"` — exact phrase match
- `$search=renewal` — matches agreements with "renewal" in title, type, or provisions

**Note**: `$search` can be combined with `$filter` for more targeted results (e.g., `$search=Acme&$filter=status eq 'COMPLETE'`).

maxLength: 500

$filter

---

string

Use example values

parties/name\_in\_agreement eq 'HEALTHEON CORPORATION'

OData filter expression for complex queries. Supports:

- Comparison operators: `eq`, `ne`, `gt`, `ge`, `lt`, `le`
- Logical operators: `and`, `or`
- In operator: `in` (e.g., `type in ('Msa','Sow')`)

**Note**: Use forward slash `/` to navigate nested properties (e.g., `provisions/effective_date`), not dot notation.

Examples:

- `status eq 'COMPLETE' and provisions/effective_date ge 2025-01-01`
- `parties/name_in_agreement eq 'Acme Corp' or parties/name_in_agreement eq 'Beta Ltd'`
- `provisions/renewal_type in ('EVERGREEN','AUTO_RENEW')`

maxLength: 2000

sort

---

string

Field to sort the agreements by.

direction

---

string

Direction of sorting (ascending or descending).

enum: ascdesc

id

---

string

List of agreement IDs to filter by (comma-separated), use operators (=, [in]) with an UUID format.

document\_id

---

string

List of document IDs to filter by (comma-separated), use operators (=, [in]) with an UUID format.

status

---

string

Status of the agreement.

review\_status

---

string

Review status of the agreement Supported values include:

- COMPLETE
- PENDING

review\_completed\_at

---

string

Extraction review completed at date. Use operators (`=`, `gte`, `gt`, `lte`, `le`, `ne`) with an ISO 8601 DateTime string (e.g., `YYYY-MM-DD`).

format: DateTime

parties.name\_in\_agreement

---

string

Filter by party display name in the agreement.

metadata.created\_at

---

string

Filter by creation date (also available via `created_at` key). Use operators (`=`, `gte`, `gt`, `lte`, `le`, `ne`) with an ISO 8601 DateTime string (e.g., `YYYY-MM-DD`).

format: DateTime

title

---

string

Title of the agreement.

related\_agreement\_documents.parent\_agreement\_document\_id

---

string

Filter by parent agreement document ID (also available via `parent_agreement_document_id` key). with an UUID format.

languages

---

string

List of BCP-47 language tags (comma-separated). Use operators (`=`) with a string format.

provisions.effective\_date

---

string

Filter by effective date range (also available via `effective_date` key). Use operators (`=`, `gte`, `gt`, `lte`, `le`, `ne`) with an ISO 8601 DateTime string (e.g., `YYYY-MM-DD`).

format: DateTime

provisions.expiration\_date

---

string

Filter by expiration date (also available via `expiration_date` key). Use operators (`=`, `gte`, `gt`, `lte`, `le`, `ne`) with an ISO 8601 DateTime string (e.g., `YYYY-MM-DD`).

format: DateTime

provisions.execution\_date

---

string

Filter by execution date (also available via `execution_date` key). Use operators (`=`, `gte`, `gt`, `lte`, `le`, `ne`) with an ISO 8601 DateTime string (e.g., `YYYY-MM-DD`).

format: DateTime

provisions.term\_length

---

string

duration of the agreement (also available via `term_length` key). Use operators (`=`, `gte`, `gt`, `lte`, `le`, `ne`) with an ISO 8601 Duration string (e.g., `P1Y`).

source\_name

---

string

Source name of the agreement.

source\_id

---

string

Source id of the agreement.

include\_linked\_data

---

boolean

Include linked data from external systems that correlate with agreements.

## Response

###### Request Example

1

2

3

curl --location "https://

api-d.docusign.com/

v1/accounts/

{accountId}/

agreements"

--header "Authorization:

Bearer {accessToken}"

--header "Content-Type:

application/json"

Was this result helpful?

###### Response Example

JSON

Click Try It! to start a request and see the response here!

Or choose an example:

Was this result helpful?

[![Footer: Platform 101: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/1B2IgSQD94ohLe7UVvJ5AU/ef33d80a2fbfcf734362995ffd43a438/footer-icon-1.svg)

Platform 101

Get up to speed on our concepts and platform](https://developers.docusign.com/platform/build-integration/)[Learn More](https://developers.docusign.com/platform/build-integration/)[![Footer: Stack Overflow: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/4gZwid50MSnlXqHMTZLCdV/4cc92d22086124f2f622c781cb554844/footer-icon-2.svg)

Docusign Community

Get answers from our API experts and community](https://community.docusign.com/developer-59)[Learn More](https://community.docusign.com/developer-59)[![Footer: GitHub: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/208FBzUKngjwdVfL0wAgd7/f6ff4fd8071196e37c5cac5f4f12c38c/footer-icon-3.svg)

GitHub

Find our SDKs and other source code](https://github.com/docusign)[Learn More](https://github.com/docusign)[![Footer: Partner Directory: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/2YWAk0yl09YARzBDgoq6dN/48d159475098419d1da9b3fcf14a4791/footer-icon-4.svg)

Partner Directory

See the full directory of Docusign partners](https://partners.docusign.com/s/partnerfinder)[Learn More](https://partners.docusign.com/s/partnerfinder)

[![Docusign.com](https://developers.docusign.com/img/docusign-logo.svg)](https://docusign.com)

[![X](https://images.ctfassets.net/aj9z008chlq0/jUnMYaPzapgZma42YHdEv/375916f63ce5f10c79da650018f8cb0c/x-logo.png)](https://x.com/DocusignDevs)[![youtube](https://images.ctfassets.net/aj9z008chlq0/pYBeoyZ3yAWrQ7yx2MV6U/c3e2679fb091dd6f6dbf9b250bd5ed9a/social-icon-youtube.png)](https://www.youtube.com/@DocusignDevs)[![linkedin](https://images.ctfassets.net/aj9z008chlq0/5dZh3hbAdZ97DYDNdhijTA/19230fd1c70b76dea1eef8834779e2cd/social-icon-linkedin.png)](https://www.linkedin.com/showcase/docusigndevs/)

APIs- [eSignature API](https://developers.docusign.com/docs/esign-rest-api/)
- [Web Forms API](https://developers.docusign.com/docs/web-forms-api/)
- [Workflow Builder API](https://developers.docusign.com/docs/workflow-builder-api/)
- [Agreement Manager API](https://developers.docusign.com/docs/agreement-manager-api/)
- [Docusign Admin API](https://developers.docusign.com/docs/admin-api/)
- [View all](https://developers.docusign.com/docs/)

Featured Content- [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/)
- [Sample Apps](https://developers.docusign.com/sample-apps/)
- [Authentication](https://developers.docusign.com/platform/auth/)
- [Webhooks](https://developers.docusign.com/platform/webhooks/)
- [Go-Live](https://developers.docusign.com/platform/go-live/)
- [SDKs](https://developers.docusign.com/docs/sdks/)

Help- [Support](https://developers.docusign.com/support/)
- [FAQs](https://support.docusign.com/s/articles/DocuSign-Developer-Support-FAQs)

More- [Partner With Us](https://developers.docusign.com/partner/)
- [Docusign University](https://developers.docusign.com/training/)
- [Trust Center](https://www.docusign.com/trust)
- [Trust Portal](https://www.docusign.com/trust-portal)
- [ISV integration guides](https://developers.docusign.com/partner/isv-integration-guides/)

[![X](https://images.ctfassets.net/aj9z008chlq0/jUnMYaPzapgZma42YHdEv/375916f63ce5f10c79da650018f8cb0c/x-logo.png)](https://x.com/DocusignDevs)[![youtube](https://images.ctfassets.net/aj9z008chlq0/pYBeoyZ3yAWrQ7yx2MV6U/c3e2679fb091dd6f6dbf9b250bd5ed9a/social-icon-youtube.png)](https://www.youtube.com/@DocusignDevs)[![linkedin](https://images.ctfassets.net/aj9z008chlq0/5dZh3hbAdZ97DYDNdhijTA/19230fd1c70b76dea1eef8834779e2cd/social-icon-linkedin.png)](https://www.linkedin.com/showcase/docusigndevs/)

© 2024 Docusign, Inc.

[Docusign.com](https://docusign.com)

[Terms of Use](https://www.docusign.com/company/terms-and-conditions/developers)

[Privacy Notice](https://www.docusign.com/company/privacy-policy)

[Notice to California Residents](https://www.docusign.com/privacy#8)

[Intellectual Property](https://www.docusign.com/IP)

![ccpa-opt-out](https://developers.docusign.com/img/svg/ccpa-opt-out.svg)
