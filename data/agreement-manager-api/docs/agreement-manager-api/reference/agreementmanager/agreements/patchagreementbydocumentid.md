---
title: ': patchAgreementByDocumentId'
source_url: https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/patchagreementbydocumentid/
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
- Patchagreementbydocumentid
scraped_at: '2026-06-18T14:17:05Z'
---

[Agreements](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/)

# : patchAgreementByDocumentId

This operation updates a specific agreement by first locating it using its associated `document_id`.
This is useful when the client knows the document storage identifier but not the agreement ID.

The operation accepts a `document_id` query parameter to uniquely identify the agreement, then applies the partial updates specified in the request body.
The system will search for an agreement containing the specified document ID, and if found, apply the requested modifications.
The operation returns a `204 No Content` response on success.

This endpoint provides an alternative way to update agreements when the agreement ID is not readily available, making it convenient for systems that primarily work with document references rather than agreement identifiers.

### Use Cases:

- **Updating agreements referenced by document storage ID**: When integration points provide document IDs but not agreement IDs, this endpoint allows direct updates without a prior lookup.
- **Batch updating via external document references**: Systems that track agreements through external document management systems can update agreements using their document storage identifiers.
- **Cross-system synchronization**: Update agreements based on document references from external systems (e.g., content management systems, document repositories) without maintaining agreement ID mappings.
- **Document-centric workflows**: In document-first business processes, update agreements using the document reference that users are familiar with.

### Key Features:

- **Document ID Based Lookup**: Locate agreements by their associated document storage identifier rather than requiring the agreement ID upfront.
- **Automatic Resolution**: The system automatically finds the agreement associated with the provided document ID.
- **Partial Updates**: Modify only the fields you need; other agreement data remains unchanged.

HTTP Request

PATCH

```
/v1/accounts/{accountId}/agreements
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

Query Parameters

document\_id

---

string

The unique document storage identifier associated with the agreement to be updated. This ID is used to locate the agreement.

Request Body

Agreement

---

Agreement

\*required

The Agreement component represents a comprehensive overview of a contractual document, detailing its unique identifiers, key properties, parties involved,
and specific provisions. It includes general information such as the title, type, status, and important dates like effective and expiration dates.
The component also incorporates various provisions—legal, financial, lifecycle, and custom—along with metadata, external references, and related documents
to offer a full representation of the structure and context of an agreement.

required: id

## Response

###### Request Example

1

2

3

4

5

6

curl --location "https://

api-d.docusign.com/v1/

accounts/{accountId}/

agreements"

--header "Authorization:

Bearer {accessToken}"

--header "Content-Type:

application/json"

--data-raw '{

"body": {}

}'

Was this result helpful?

###### Response Example

JSON

Click Try It! to start a request and see the response here!

Or choose an example:

No response examples available

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
