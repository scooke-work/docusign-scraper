---
title: ChunkedUploads Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Envelopes
- Envelopes
- Chunkeduploads
scraped_at: '2026-06-18T20:28:22Z'
---

# ChunkedUploads Resource

A chunked upload is a temporary file that you upload in parts and stage at Docusign, then refer to as the content for other API calls. For example, you might use it for document content when assembling an envelope or template.

A chunked upload is linked to the Docusign account member who initiated the API call. This user is the only user who is able to reference the chunked upload.

A ChunkedUpload is intended to be an area for briefly staging data for use with other Docusign API calls. The ChunkedUpload API endpoints do not provide an action to download the ChunkedUpload's content.

The typical flow for using a chunked upload involves the following steps:

1. Initiate the chunked upload with content representing part 0.
2. Add more parts to the chunked upload until you have transmitted the entirety of the content.
3. Commit the chunked upload, preparing it for use with other API calls.
4. Assemble a Docusign envelope with a document that includes a reference to the chunked upload as the content.
5. Continue with envelope-related processes.

**Note:** You must fully upload and use a chunked upload within 20 minutes of initializing it.

After the chunked upload has been correctly referenced within another API call, it becomes unavailable for any further use and is promptly removed from the system.

Chunked uploads have the following limits, which are configured per Docusign environment, account, or integrator:

- The maximum number of all of a member's unexpired, unconsumed ChunkedUploads. The default value is 64.
- The maximum total size of all of a member's unexpired, unconsumed ChunkedUploads. The default value is 1 GB.
- The amount of time that a chunked upload is active after you initialize it. The default value is 20 minutes.

## Methods Supported

| Method | Description |
| --- | --- |
| [commit](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/commit/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/chunked_uploads/{chunkedUploadId} ```  Commit a chunked upload. |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/chunked_uploads ```  Initiate a new chunked upload. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/delete/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/chunked_uploads/{chunkedUploadId} ```  Deletes a chunked upload. |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/get/) | GET  ```  /restapi/v2.1/accounts/{accountId}/chunked_uploads/{chunkedUploadId} ```  Retrieves metadata about a chunked upload. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/chunked_uploads/{chunkedUploadId}/{chunkedUploadPartSeq} ```  Add a chunk to an existing chunked upload. |

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
