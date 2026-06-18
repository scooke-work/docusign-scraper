---
title: ': get'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/get/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:10:01Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/get/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/get/?explorer=true)

[EnvelopeDocuments](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/)

# : get

Retrieves a single document or all documents from an envelope.

To retrieve a single document, provide the ID of the document in the `documentId` path parameter.
Alternatively, by setting the `documentId` parameter to special keyword values,
you can retrieve all the documents (as a combined PDF, portfolio PDF, or ZIP archive)
or just the certificate of completion. See the `documentId` description for how to retrieve each format.

The response body of this method
is a file. If you request multiple documents,
the result is a ZIP archive
that contains all of the documents.

In all other cases, the response is a PDF
file or PDF portfolio.

You can get the file name and document ID from the response's `Content-Disposition` header:

```
Content-Disposition: file; filename="NDA.pdf"; documentid="1
```

By default, the response is the PDF file
as a byte stream.
For example a request/response in `curl` looks like this:

```
$ curl --request GET 'https://demo.docusign.net/restapi/v2/accounts/0cdb3ff3-xxxx-xxxx-xxxx-e43af011006d/envelopes/ea4cc25b-xxxx-xxxx-xxxx-a67a0a2a4f6c/documents/1/' \
       --header 'Authorization: Bearer eyJ...bqg'

HTTP/1.1 200 OK
Content-Length: 167539
Content-Type: application/pdf
. . .
Content-Disposition: file; filename="Lorem_Ipsum.pdf"; documentid="1"
Date: Tue, 23 Aug 2022 01:13:15 GMT

%PDF-1.4
%˚¸˝˛
6 0 obj
<</Length 14>>stream
. . .
```

By using the `Content-Transfer-Encoding`
header in the request, you can obtain the PDF file
encoded in base64. The same `curl` request with
the base64 header would look like this:

```
$ curl --request GET 'https://demo.docusign.net/restapi/v2/accounts/0cdb3ff3-xxxx-xxxx-xxxx-e43af011006d/envelopes/ea4cc25b-xxxx-xxxx-xxxx-a67a0a2a4f6c/documents/1/' \
       --header 'Authorization: Bearer eyJ...bqg' \
       --header 'Content-Transfer-Encoding: base64'

HTTP/1.1 200 OK
Content-Length: 223384
Content-Type: application/pdf
. . .
Content-Disposition: file; filename="Lorem_Ipsum.pdf"; documentid="1"
Content-Transfer-Encoding: base64
Date: Tue, 23 Aug 2022 01:12:30 GMT

JVBERi0xLjQKJfv8/f4KNiAwIG9iago8PC9MZW. . .==
```

(In an actual `curl` request you would use the `--output` switch to
save the byte stream into a file.)

### Related topics

- [How to download envelope documents](https://developers.docusign.com/docs/esign-rest-api/how-to/download-envelope-documents/)
- [eSignature API rules and resource limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/)

## Request

#### HTTP Request

GET

```
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| documentId \* | string | The ID of the document to retrieve. Alternatively, you can use one of the following special keywords:   - `combined`: Retrieves all of the documents as a single PDF file.   When the query parameter `certificate` is **true,** the certificate of completion is included in the PDF file.   When the query parameter `certificate` is **false,** the certificate of completion is not included in the PDF file. - `archive`: Retrieves a ZIP archive that contains all of the PDF documents and the certificate of completion. - `certificate`: Retrieves only the certificate of completion as a PDF file. - `portfolio`: Retrieves the envelope documents as a [PDF portfolio](https://helpx.adobe.com/acrobat/using/overview-pdf-portfolios.html). |
| envelopeId \* | string | The envelope's GUID.  Example: `93be49ab-xxxx-xxxx-xxxx-f752070d71ec` |

| Query Parameters |  |  |
| --- | --- | --- |
| certificate | string | Used only when the `documentId` parameter is the special keyword `combined`.  When **true,** the certificate of completion is included in the combined PDF file. When **false,** (the default) the certificate of completion is not included in the combined PDF file. |
| documents\_by\_userid | string | When **true,** allows recipients to get documents by their user id. For example, if a user is included in two different routing orders with different visibilities, using this parameter returns all of the documents from both routing orders. |
| encoding | string | Reserved for Docusign. |
| encrypt | string | When **true,** the PDF bytes returned in the response are encrypted for all the key managers configured on your Docusign account. You can decrypt the documents by using the Key Manager DecryptDocument API method. For more information about Key Manager, see the Docusign Security Appliance Installation Guide that your organization received from Docusign. |
| language | string | Specifies the language for the Certificate of Completion in the response. The supported languages are: Chinese Simplified (zh\_CN), Chinese Traditional (zh\_TW), Dutch (nl), English US (en), French (fr), German (de), Italian (it), Japanese (ja), Korean (ko), Portuguese (pt), Portuguese (Brazil) (pt\_BR), Russian (ru), Spanish (es). |
| recipient\_id | string | Allows the sender to retrieve the documents as one of the recipients that they control. The `documents_by_userid` parameter must be set to **false** for this functionality to work. |
| shared\_user\_id | string | The ID of a shared user that you want to impersonate in order to retrieve their view of the list of documents. This parameter is used in the context of a shared inbox (i.e., when you share envelopes from one user to another through the Docusign Admin console). |
| show\_changes | string | When **true,** any changed fields for the returned PDF are highlighted in yellow and optional signatures or initials outlined in red. The account must have the **Highlight Data Changes** feature enabled. |
| watermark | string | When **true,** the account has the watermark feature enabled, and the envelope is not complete, then the watermark for the account is added to the PDF documents. This option can remove the watermark. |

\* Required

## SDK Method

### Envelopes::getDocument

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
