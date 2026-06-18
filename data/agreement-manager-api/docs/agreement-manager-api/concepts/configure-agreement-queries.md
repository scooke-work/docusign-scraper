---
title: Configure agreement queries
source_url: https://developers.docusign.com/docs/agreement-manager-api/concepts/configure-agreement-queries/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Agreement Manager API
- Agreement Manager API
- Concepts
- Concepts
- Configure Agreement Queries
scraped_at: '2026-06-18T14:17:04Z'
---

# Configure agreement queries

When you get agreements using the [Agreements:getAgreementsList](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreementslist/) endpoint, you can apply [Open Data Protocol](https://www.odata.org/getting-started/basic-tutorial/) (OData) query model parameters to select and filter the results to return exactly the agreements you need. This query model currently supports basic filtering, as well as the following four query parameters:

- [$filter](https://developers.docusign.com/docs/agreement-manager-api/concepts/configure-agreement-queries/#filter-on-agreement-fields-using-filter)
- [$select](https://developers.docusign.com/docs/agreement-manager-api/concepts/configure-agreement-queries/#return-only-the-result-fields-that-you-need-by-using-select)

## Filter queries with basic syntax

The following bracketed operators are supported in basic queries that do not include any query parameters:

- `[gt]`: Greater than
- `[gte]` / `[ge]`: Greater than or equal to
- `[lt]`: Less than
- `[lte]` / `[le]`: Less than or equal to
- `[ne]` / `[eq]`: Not equal to

Basic queries support the following data types and operators:

| **Data Type** | **Type Supported Operators** |
| --- | --- |
| `string` | `=` |
| `number (integer, float, etc.)` | `=, gte, gt, lte, le` |
| `datetime` | `=, gte, gt, lte, le` |
| `duration (`[ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html)`)` | `=, gte, gt, lte, le` |

You can combine multiple filter conditions by including them as separate query parameters and linking them with ampersand (`&`) . 

Example query for multiple basic filter conditions:

`GET /agreements?status=COMPLETE&effective_date[gte]=2025-01-01`

Properties of complex types can be accessed using a forward slash notation (`/`). This is the same syntax as accessing resources in the URI. 

Example complex type property:

`companies(1)/address/street` **Note**: Filter parameters and operations are case insensitive.

### **List of filterable fields for each support resource type**

## Filter on agreement fields using $filter

The `$filter` query parameter enables you to perform more complex query filtering than basic syntax. You can use `$filter` to combine multiple conditions with and, or, in, contains, and group clauses with parentheses. Nested properties use `/` path syntax, such as `provisions/effective_date`.

Use cases include:

- AI agents with structured filters, which can translate user constraints into an OData `$filter` instead of pulling everything and filtering client-side.
- Renewal dashboards and reviews, such as filters for all active agreements expiring within a certain period of time. Common filters on fields such as `status`, `review_status`, `review_completed_at`, `metadata.created_at`, `provisions.effective_date`, `provisions.expiration_date`, or `provisions.execution_date`.
- Party-specific views for an agreement, such as showing all agreements where the specified party is a signer using a field like `parties/name_in_agreement`.

Example query syntax:`GET /employees?$filter=role eq 'Manager' or (role eq 'Developer' and department eq 'Engineering')`

## Return only the result fields that you need by using $select

The `$select` parameter enables you return only the values of exact fields that you care about for the objects in a result set. 

To use `$select`, you specify the relevant field names as values for the query parameter before executing your GET agreements API call. Using path syntax, you can project fields at any depth.

Example query:

`GET /agreements?$select=title,parties/name,provisions/term_length`

Implementing `$select` can help you reduce costs for interacting with agreements using Large Language Models (LLMs). Unnecessary data in API responses can increase the cost of running LLMs against your data. By using `$select` to only return the specific fields that you need, you can reduce payload size by 70-90% and keep your costs low by minimizing the data that the LLM processes. 

For example, an LLM answering a question about the names of parties in an agreement does not need data about the agreement’s value or renewal date, allowing you to query specifically for name fields and not process any unnecessary data.

## Use $search for keyword and partial-information searches

The $search query parameter enables you to perform searches using partial information, such as a probable keyword or a company name mentioned somewhere in an agreement document, rather than requiring exact terms or complicated queries.

$search is especially useful for [AI Agents](https://developers.docusign.com/platform/mcp-server/). It can be difficult to construct precise $filter queries based on natural language questions, sometimes leading to reduced accuracy or additional cost. $search more fully supports natural language queries and it is more flexible and simpler to use than $filter, but may only access data from designated supported searchable fields.  

$search can also be used as a broad keyword search to generate a result set, which you then filter using $filter and $select in later API calls.

The following example query returns agreements where searchable content matches the “market research” term, enabling natural discovery without requiring field-specific knowledge. In this case, every document with a field containing the term “market research” will be returned. $search queries are case-insensitive.

`GET /agreements?$search="market research"`

## Next steps

- See the [Agreements:getAgreementsList](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreementslist/) reference documentation.
- See the Agreement Manager [How-to guides](https://developers.docusign.com/docs/agreement-manager-api/how-to/).
- Learn about [Agreement Manager API use cases](https://developers.docusign.com/docs/agreement-manager-api/concepts/use-cases/).

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
