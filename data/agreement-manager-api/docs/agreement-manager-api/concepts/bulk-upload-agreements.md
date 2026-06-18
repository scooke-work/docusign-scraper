---
title: Bulk upload agreements
source_url: https://developers.docusign.com/docs/agreement-manager-api/concepts/bulk-upload-agreements/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Agreement Manager API
- Agreement Manager API
- Concepts
- Concepts
- Bulk Upload Agreements
scraped_at: '2026-06-18T14:17:04Z'
---

# Bulk upload agreements

Bulk Upload enables developers to programmatically upload many agreements into the Agreement manager at the same time, triggering AI extraction where applicable on your uploaded documents or applying your supplied metadata directly. 

Agreement manager bulk upload works by generating upload URLs as part of a bulk job and passing them back to your app. Your app then uploads one document to each upload URL and, when all of your documents are uploaded, calls an endpoint to signal completion. This removes the overhead of proxying large files and enables you to easily and painlessly mass-onboard legacy documents, such as old contracts from disparate systems, split between different file formats and organization systems.

## Bulk upload use cases

**Bulk upload enables you to migrate large numbers of legacy agreements into one place for management.** Bulk upload legacy contracts from disparate systems such as your on-premises storage, SharePoint, Google Drive, or Dropbox into the Agreement Management platform. 

You can use AI extraction to order and apply metadata to these documents, or upload documents alongside structured metadata such as custom field values, record IDs, or tags, to skip AI extraction overhead and maintain data fidelity.

For example, a bank with contracts going back years or decades, in many different formats, from many different regions, wants to standardize their documents and manage them from one place. Bulk upload is the mechanism by which the masses of these documents can be added to Agreement Manager for ingestion, sorting, and categorization.

## How bulk upload works

You can create bulk upload jobs for documents using the following steps:

**1. Create a bulk upload job**

Call the `POST /v1/accounts/{accountId}/upload/jobs` endpoint to create a job, providing a name, language, and the number of docs to be uploaded.

The response includes a job ID and pre-signed blob storage URLs for each document, which are valid for 8 hours. 

The `document_uploader_write` and `document_uploader_read` scopes are required for performing bulk upload tasks with the API. The `adm_store_unified_repo_read` is also required for tasks that involve reading agreement records.

1

curl --location \ 'https://api-d.docusign.com/v1/

accounts/08b4799a-xxxx-xxxx-xxxx-b5b4b8a97604/upload/

jobs' \ --header 'Authorization: Bearer eyJ…1UA ' \

--header 'Content-Type: application/json' \

--data-raw '{ "job\_name": "Q4 Contract Migration",

"expected\_number\_of\_docs": 3, "language": "en-US",

"agreement\_set\_ids": [ "-8c-dVtBzjSe7nh\_zAf9L" ] }'

**2. Upload documents to pre-signed URLs** For each document URL in the `_embedded.documents` array, make an HTTP PUT request providing the binary file content. The required headers for these calls are:

- `x-ms-blob-type`: `BlockBlob`: Required.
- `x-ms-meta-filename: YourDocumentName.pdf`: Recommended. Defaults to your document ID if omitted.
- `Content-Type`: The appropriate MIME type for your file. Required.

Documents can be uploaded in parallel, with your own retry logic, and integrated into existing file processing pipelines. 

You can also add a metadata header alongside each document to be uploaded. When metadata is provided, the platform skips the AI extraction step for that document since the metadata already exists. This metadata must be provided in JSON format via the API (CSV-based metadata is a UI-only feature). 

Supported file formats for bulk upload documents are:

- .pdf
- .docx
- .doc
- .pptx
- .txt
- .html
- .htm
- .rtf
- .jpg or .jpeg
- .png
- .tiff or .tif
- .eml
- .zip

For the authoritative list of supported formats, size limits, and headers, always refer to the `allowed_formats` and headers in the `_action_templates` section of the `createBulkUploadJob` response.

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

{

"provisions":{

"jurisdiction":"California"

},

"custom\_provisions":{

"c\_ClientId":{

"value":"12345"

}

}

}

**3. Mark the job complete**Once all of the documents have been uploaded, make a POST `/v1/accounts/{accountId}/upload/jobs/{jobId}/actions/complete` call to mark the job complete, triggering ingestion of the documents and AI extraction.

1

curl --location \ 'https://api-d.docusign.com/v1/

accounts/08b4799a-xxxx-xxxx-xxxx-b5b4b8a97604/upload/

jobs/c5f018e6-xxxx-xxxx-xxxx-539c6f505a95/actions/

complete' \ --request POST \ --header

'Authorization: Bearer eyJ…1UA' \ --header

'Content-Type: application/json'

## Bulk upload rules and rate limits

| **Constraint** | **Description** |
| --- | --- |
| Maximum documents per job | 10,000 documents. For uploads exceeding 10,000 documents, you must use multiple bulk upload jobs. |
| Maximum file size | 500 MB per file. |
| AI extraction file size limit | 190 MB (up to 300 pages). |
| Pre-signed URL validity | 8 hours. |
| Bulk upload job lifespan | A job will expire after 3 days. |

## Next steps

- Learn how to [Unlock Your Historical Agreements: Agreement Manager API Bulk Ingestion Made Simple](https://www.docusign.com/blog/developers/navigator-api-bulk-ingestion-made-simple)
- See the Agreement Manager [Bulk Jobs API reference](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/#bulkjob)

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
