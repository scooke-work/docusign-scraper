---
title: TSP Complete Sign Hash Session Information
source_url: https://developers.docusign.com/docs/tsp-api/reference/complete-sign-hash-session-information/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- API Reference
- API Reference
- Complete Sign Hash Session Information
scraped_at: '2026-06-18T22:15:24Z'
---

# TSP Complete Sign Hash Session Information

`POST /restapi/{apiVersion}/signature/completesignhash`

This method provides completed signing session information from the TSP. It builds the resulting signed PDF.

## Request Header Parameters

The following header parameters apply to the TSP API and the CMS API calls.

| Name | Type | Description |
| --- | --- | --- |
| Authentication | String | Required. See [Authentication](https://developers.docusign.com/docs/tsp-api/tsp101/tsp-authentication/) |
| Content-Type | String | Required. Specifies the type of data returned in the request body. This parameter must be set to `application/json`. |
| X-Docusign-CorrelationToken | GUID | Optional. ID used for telemetry. Docusign recommends that you set up a correlation token for all the TSP API and CMS API calls. |

## Request Body Parameters

This table provides descriptions of the information in the request.

| Name | Description |
| --- | --- |
| documentUpdateInfos | Required |
| documentUpdateInfos.data | Required.  The base 64 encoded value of the Cryptographic Message Syntax (CMS). |
| documentUpdateInfos.documentId | Required.  String document identifier for the given document.  **Note**: when using `completesignhash` to create timestamping data, the identifier must correspond to the value of `documentID` returned by the response to the previous `completesignhash` request. For more information, see [Long term validation of PDF signatures](https://developers.docusign.com/docs/tsp-api/tsp101/long-term-signature-validation/). |
| documentUpdateInfos.documentSecurityStore | Optional.  Embeds the validation information.  PAdES B-LTA and PAdES B-LT formats require this parameter. |
| documentUpdateInfos.documentSecurityStore.certificates | Optional.  An array of the base64 certificates builds the chain of trust from the user certificate up to the AATL (Adobe Approved Trust List) trusted root.  PAdES B-LTA and PAdES B-LT formats require this parameter. |
| documentUpdateInfos.documentSecurityStore.crls | Optional.  An array of the base64 CRLs (Certificate Revocation List) containing the revocation information on the certificate chain.  PAdES B-LTA and PAdES B-LT formats require that the signature embeds the revocation status of the certificate chain either through CRLs or OCSP servers.  **Important**: the size of the CRLs can impact the size of the resulting PDF. Consider using OCSPs instead. |
| documentUpdateInfos.documentSecurityStore.ocsps | Optional.  An array of the base64 encoded OCSPs (Online Certificate Status Protocol) that provide revocation information on the certificate chain.  PAdES B-LTA and PAdES B-LT formats require that the signature embeds the revocation status of the certificate chain either through CRLs or OCSP servers. |
| documentUpdateInfos.name | Optional.  String containing the suggested document name. |
| documentUpdateInfos.returnFormat | Required.  A string indicating the requested return format. The only allowed return format is "CMS". |
| documentUpdateInfos.timeStampField | Optional.  PAdES B-LTA format requires that you set this parameter to an empty value in the request that creates the last signature. This configuration triggers the creation of a timestamp that is sent back to Docusign and added to the PDF. For more information, see [Long term validation of PDF signatures](https://developers.docusign.com/docs/tsp-api/tsp101/long-term-signature-validation/). |
| transactionId | Optional.  A string holding the TSP transaction ID. This parameter allows you to correlate information between Docusign and the TSP. |

## Response Information

If successful, this returns completeSignResponse. The table below provides descriptions of the information in the response.

| Name | Description |
| --- | --- |
| redirectionUrl | The URL that is redirecting the user after signing completion. |
| remainingSignatureRequests | A string representing the number of signature requests remaining for documents that require multiple signatures |
| documents | An array of documents if more signatures are required |
| documents.name | A string representing the name of the document being signed. |
| documents.documentId | A string representing the identifier for the document that must be returned in subsequent requests |
| documents.data | A Base 64 String representing the hash stream or ASN1Set SignedAttributes to be signed. |
| documents.remainingSignatures | A string representing the number of remaining signatures to apply to the document. |

1

2

3

4

5

6

7

8

9

10

11

12

13

{

"documentUpdateInfos": [{

"documentId": "string",

"data": "base 64 string",

"returnFormat": "string",

"documentSecurityStore": {

"certificates": "array of base64 encoded

certificates",

"ocsps": "array of base64 encoded OCSPs",

},

"timestampField": "the empty string if a

timestamp signature is required, null

otherwise"

}],

"transactionId": "string"

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
