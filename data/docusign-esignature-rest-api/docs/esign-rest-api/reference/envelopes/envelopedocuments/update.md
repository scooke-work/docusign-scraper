---
title: ': update'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/update/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:21Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/update/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/update/?explorer=true)

[EnvelopeDocuments](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/)

# : update

Adds or replaces a document in an existing draft or in-process envelope.
An in-process envelope is one that has been sent but not yet completed or voided.

**Note:** When adding or modifying documents for an in-process envelope,
Docusign recommends
[locking the envelope](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopelocks/create/)
prior to making any changes.

To add a new document, set the `documentId` path parameter to a new document ID.

To replace a document, set the `documentId` path parameter to the document ID of the existing document.
The tabs of the original document will be applied to the new document.
For example, a request in cURL looks like this:

```
$ curl --location --request PUT 'https://demo.docusign.net/restapi/v2.1/accounts/0cdb3ff3-xxxx-xxxx-xxxx-e43af011006d/envelopes/ea4cc25b-xxxx-xxxx-xxxx-a67a0a2a4f6c/documents/1' \
    --header 'Authorization: Bearer eyJ...bqg' \
    --header 'Content-Disposition: filename="newDocument"' \
    --header 'Content-Type: application/pdf' \
    --data-binary '@/location/of/document.pdf'
```

If HTML document files contain `<img>` elements with the `src` attribute set to a path or URL, those images will not be displayed. Images in HTML files must be encoded in Base64 format, like this:
`<img src="data:image/gif;base64,R0lGODlh...IQAAOw==" alt="Base64 encoded image" width="150" height="150"/>`

### Related topics

- [eSignature API rules and resource limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/)
- [How-to guides for working with envelopes](https://developers.docusign.com/docs/esign-rest-api/how-to/#working-with-documents)

## Request

#### HTTP Request

PUT

```
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| documentId \* | string | The unique ID of the document within the envelope.  Unlike other IDs in the eSignature API, you specify the `documentId` yourself. Typically the first document has the ID `1`, the second document `2`, and so on, but you can use any numbering scheme that fits within a 32-bit signed integer (1 through 2147483647).  Tab objects have a `documentId` property that specifies the document on which to place the tab. |
| envelopeId \* | string | The envelope's GUID.  Example: `93be49ab-xxxx-xxxx-xxxx-f752070d71ec` |

\* Required

## SDK Method

### Envelopes::updateDocument

## Request Body

## Responses

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
