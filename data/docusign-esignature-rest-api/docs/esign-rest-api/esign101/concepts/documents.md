---
title: Envelope and Template Documents
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Documents
scraped_at: '2026-06-18T21:09:58Z'
---

# Envelope and Template Documents

A *document* is an object that contains a digital document file and a set of metadata describing that document file. A document file contains content to be reviewed or signed by one or more [recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/). Documents are always defined as part of the `documents` property in an [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) or a [template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/), and are always securely encrypted while stored in the system.

For examples of how to work with documents using the API, see [How to add a document to an envelope and request a signature by email](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-remote/).

Document files can be supplied through client devices, cloud storage systems, or additional document sources. Docusign accepts almost all document types, including PDF, DOCX, RTF, TXT, and PNG, and you can store multiple documents in a single envelope.

When you add a document file to an envelope, the Docusign platform converts it to PDF and stores it as base64-encoded ASCII.

## Supported document file types

You can use the following types of files as documents in an envelope. File types are ordered by category below for organizational purposes, but are accepted and output by the API in the same way, regardless of category.

| Document category | File type |
| --- | --- |
| Document | .doc, .docm, .docx, .dot, .dotm, .dotx, .htm, .html, .msg, .pdf, .rtf, .txt, .wpd, .xps |
| Image | .bmp, .gif, .jpg, .jpeg, .png, .tif, .tiff |
| Presentation | .pot, .potx, .pps, .ppt, .pptm, .pptx |
| Spreadsheet | .csv, .xls, .xlsm, .xlsx |

If HTML document files contain `<img>` elements with the `src` attribute set to a path or URL, those images will not be displayed. Images in HTML files must be encoded in Base64 format, as shown in the example below:

```
<img src="data:image/gif;base64,R0lGODlhDwAPAKECAAAAzMzM/////
wAAACwAAAAADwAPAAACIISPeQHsrZ5ModrLlN48CXF8m2iQ3YmmKqVlRtW4ML
wWACH+H09wdGltaXplZCBieSBVbGVhZCBTbWFydFNhdmVyIQAAOw=="
alt="Base64 encoded image" width="150" height="150"/>
```

## Attaching documents to an envelope

There are two ways to attach documents to envelopes:

- Converting the documents to base64 and attaching them to a single object
- Using multipart form data to send the documents directly, without converting them into base64

The second technique, also known as *binary transfer,* is 33% more efficient than base64 encoding and is recommended for all documents that are larger than 15MB. See [How to attach documents via binary transfer](https://developers.docusign.com/docs/esign-rest-api/how-to/send-binary/) for a walkthrough of using binary transfer to add documents to an envelope before sending it for signing via email (remote signing).
> **Note:** Binary transfer is not yet supported by any of the Docusign SDKs. It can only be performed via direct API calls.

## Downloading completed documents and tag data

For client applications that are not using Connect to receive events from Docusign, Docusign recommends usingand [getDocuments](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/get/) calls. When using `getEnvelope`, if you need additional data such as recipient or tab data, you can combine it into a single call using the URL parameter `"Include="`. See the documentation for a full list of items that can be fetched in a single call. When fetching documents, we recommend that you get documents as a ZIP file (using the Archive endpoint `/envelopes/{envelopeId}/documents/archive`), as this is the quickest and most efficient call. Clients should not get document and recipient data one at a time in a recursive loop.

## Next steps

Read about important document features:

- [Document generation](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/)
- [Purging documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/purging/)
- [Authoritative copies](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/authoritative-copies/)
- [Attachments](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/attachments/)
- [Supplemental documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/supplemental/)

Working with documents? Learn:

- [How to add a document to an envelope and request a signature by email](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-remote/)
- [How to request a signature by email with document generation](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-document-generation/)
- [How to attach documents via binary transfer](https://developers.docusign.com/docs/esign-rest-api/how-to/send-binary/)
- [How to download envelope documents](https://developers.docusign.com/docs/esign-rest-api/how-to/download-envelope-documents/)
- How to work with the [EnvelopeDocuments](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/) resource

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
