---
title: ': getAgreement'
source_url: https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreement/
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
- Getagreement
scraped_at: '2026-06-18T14:17:04Z'
---

[Agreements](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/)

# : getAgreement

This operation retrieves detailed information about a specific agreement, identified by its unique `id`. The response provides a comprehensive view of the agreement, including its title, type, status, summary, and the full list of involved parties.

In addition to general details, the operation returns provisions that define the agreement's legal, financial, lifecycle, and custom conditions. It also provides key metadata, such as creation and modification timestamps, related agreements, and user-defined or custom attributes, which help represent the structure and context of the agreement.

The operation is essential for retrieving the full context of an agreement, enabling users to understand the contract's scope, key provisions, and the legal or financial obligations that have been agreed upon.

### Use Cases:

- **Integrating agreement data into external systems**: Sync detailed agreement information, such as legal and financial provisions, into external systems like ERP, CRM, or contract management tools to streamline workflows.
- **Providing detailed data for RAG (Retrieval-Augmented Generation) applications or Copilots**: Retrieve detailed agreement data for use in LLM-based applications that answer specific user queries about their agreements, such as the status of a contract, its provisions, or involved parties.
- **Retrieving the complete details of a specific agreement**: Use the full details of the agreement, including legal and financial provisions, for auditing, compliance, or review purposes.
- **Accessing agreement provisions for verification**: Verify compliance with specific legal or financial terms of the agreement, ensuring that all parties are following the agreed-upon conditions.
- **Tracking agreement changes and history**: Fetch metadata and related agreements to understand the evolution of an agreement, including modifications, associated agreements, and additional context provided by custom fields.
- **Reviewing user-defined or custom attributes**: Examine custom fields or attributes to get more context about the agreement, particularly where the business has defined custom provisions or attributes.

### Key Features:

- **Detailed Agreement Overview**: Provides a comprehensive view of a specific agreement, including its title, type, status, summary, and more.
- **Provisions for Legal, Financial, and Lifecycle Conditions**: Includes the full set of provisions that define the terms and conditions of the agreement, making it ideal for compliance and auditing purposes.
- **Metadata and History**: Tracks the agreement’s history through metadata such as creation and modification dates and user-defined fields.
- **Data Source for AI Applications**: Enables LLM-based applications to access granular agreement data, providing AI/ML-based solutions (such as Copilots) with the necessary context to answer detailed queries about an agreement.
- **Involved Parties and Related Agreements**: Lists all parties involved and related agreements, allowing users to see all associated legal documents and relationships between agreements.

HTTP Request

GET

```
/v1/accounts/{accountId}/agreements/{agreementId}
```

Base URL : Demo

```
https://api-d.docusign.com
```

## Request

Path Parameters

accountId

---

UUID

\*required

pattern: ^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$

agreementId

---

AgreementId

\*required

pattern: ^[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?$

Query Parameters

include\_linked\_data

---

boolean

Include linked data from external systems that correlate with this agreement.

## Response

###### Request Example

1

2

3

curl --location "https://

api-d.docusign.com/

v1/accounts/

{accountId}/

agreements/

{agreementId}"

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
