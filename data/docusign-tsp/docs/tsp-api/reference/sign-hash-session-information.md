---
title: TSP Sign Hash Session Information
source_url: https://developers.docusign.com/docs/tsp-api/reference/sign-hash-session-information/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- API Reference
- API Reference
- Sign Hash Session Information
scraped_at: '2026-06-18T22:15:24Z'
---

# TSP Sign Hash Session Information

`POST /restapi/{apiVersion}/signature/signhashsessioninfo`

This method provides signing session information for a Trust Service Provider (TSP). This method is used by TSPs to sign documents hashes.

## Request Header Parameters

The following header parameters apply to the TSP API and the CMS API calls.

| Name | Type | Description |
| --- | --- | --- |
| Authentication | String | Required. See [Authentication](https://developers.docusign.com/docs/tsp-api/tsp101/tsp-authentication/) |
| Content-Type | String | Required. Specifies the type of data returned in the request body. This parameter must be set to `application/json`. |
| X-Docusign-CorrelationToken | GUID | Optional. ID used for telemetry. Docusign recommends that you set up a correlation token for all the TSP API and CMS API calls. |

## Request Body Parameters

This table provides descriptions of the information in the request body.

| Name | Description |
| --- | --- |
| certificate | Optional. Base 64 string representing the x509 certificate used to sign. |
| SignatureManifestation | Optional. Specifies an image file and size for representing the signature.  Note: this parameter is only supported by version 2.1 of the eSignature REST API. It also requires additional configuration at the account level. Please, contact your account administrator to enable this feature. |
| signatureImage | Optional. Base 64 string representing the image associated with the signature. |
| width | Optional. Image width in points. If you set a width value, you must also specify a height. |
| height | Optional. Image height in points. If you set a height value, you must also specify a width. |

## Response Information

If successful, this returns signHashSessionInfoResponse. The table below provides descriptions of the information in the response.

| Name | Description |
| --- | --- |
| redirectionUrl | String holding the URL the user is redirected to after signing completion. |
| remainingSignatureRequests | String holding the number of signature requests remaining, for documents that require multiple signatures. |
| documents | An array of documents |
| documents.documentId | String identifier for the document that must be returned in subsequent requests. |
| documents.name | The string name of the document being signed. |
| documents.data | String holding the hash stream or ASN1Set SignedAttributes to be signed. |
| documents.remainingSignatures | String holding the number of remaining signatures that need to be applied to this document. |

1

2

3

4

5

6

7

8

{

"certificate": "base 64 string",

"SignatureManifestation": {

"signatureImage": "base64 string",

"width": "integer",

"height": "integer"

}

}

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
