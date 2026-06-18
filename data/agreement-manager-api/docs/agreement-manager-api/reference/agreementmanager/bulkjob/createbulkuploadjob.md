---
title: ': createBulkUploadJob'
source_url: https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/bulkjob/createbulkuploadjob/
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
- Bulkjob
- Bulkjob
- Createbulkuploadjob
scraped_at: '2026-06-18T14:17:05Z'
---

[BulkJob](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/bulkjob/)

# : createBulkUploadJob

Create a new job, give presigned URLs back, the client will upload to Azure Blob Store directly.

**Important Upload Workflow**:

1. Call this endpoint to create a job and receive upload URLs
2. For each document in the response's `_embedded.documents` array, extract the `upload_document` URL from `_actions`
3. Upload your document file to each URL using an HTTP PUT request with the document content as binary data
4. After all documents are uploaded, call the `/actions/complete` endpoint to finalize the job
5. Use the GET endpoint to monitor job progress

**Example response structure**:

```
{
  "_embedded": {
    "documents": [
      {
        "id": "8c566d26-e7fb-4b7e-870c-1d0fb8df9084",
        "sequence": 1,
        "_actions": {
          "upload_document": "https://docupstoragewestwu3dsto.blob.core.windows.net/..."
        }
      }
    ]
  }
}
```

**Azure Blob Storage Upload Instructions**:

Use the pre-signed URL from step 2 to upload your document directly to Azure Blob Storage:

```
PUT [pre-signed URL from _actions.upload_document]

Headers:

- x_ms_blob-type: BlockBlob (Required)
- x_ms_meta-filename: YourDocumentName.pdf (Recommended)
- Content-Type: application/pdf (Required)
- x_ms_meta-metadata: <stringified JSON metadata> (Optional)

Body: [Your document binary data]
```

**Important Notes**:

- The `upload_document` URLs are pre-signed Azure Blob Storage URLs with time-limited validity (8 hours)
- No Auth header is needed
- The `x_ms_meta-filename` header should contain your original document filename
- The `x_ms_blob-type` must be set to `BlockBlob`
- Setting the `Content-Type` header is recommended to match your document type
- If `Content-Type` is not specified, Azure defaults to `application/octet-stream`
- The `x_ms_meta-metadata` header is optional and allows you to attach metadata to the newly created agreement at upload time. See **Applying Metadata to Agreements** below for details

**Applying Metadata to Agreements**:

You may include metadata alongside the document bytes during upload. This metadata will be directly applied to the
newly created agreement. To do this, include the `x_ms_meta-metadata` header on the PUT operation with a stringified
JSON value.

The JSON schema for this header follows the same structure as the standard Agreement PATCH request body.

**Example metadata JSON**:

```
{
  "provisions": {
    "jurisdiction": "California",
    "payment_terms_due_date": "OTHER"
  },
  "custom_provisions": {
    "c_ClientId": "value"
  },
  "linked_data": [
    {
      "application_name": "Salesforce",
      "object_name": "Account",
      "record_id": "579386BF-C8EA-4673-AE0E-E2F922B09DC5"
    },
    {
      "application_name": "Dynamics",
      "object_name": "Account",
      "record_id": "514CEAFB-1AC7-43FF-9E88-24CB15150963"
    }
  ]
}
```

**Stringified header value**:

The JSON must be stringified before being set as the header value. For example, the above JSON would become:

```
x_ms_meta-metadata: "{\"provisions\":{\"jurisdiction\":\"California\",\"payment_terms_due_date\":\"OTHER\"},\"custom_provisions\":{\"c_ClientId\":\"value\"},\"linked_data\":[{\"application_name\":\"Salesforce\",\"object_name\":\"Account\",\"record_id\":\"579386BF-C8EA-4673-AE0E-E2F922B09DC5\"},{\"application_name\":\"Dynamics\",\"object_name\":\"Account\",\"record_id\":\"514CEAFB-1AC7-43FF-9E88-24CB15150963\"}]}"
```

**Metadata Notes**:

- The `x_ms_meta-metadata` header is entirely optional. If omitted, the agreement is created with AI-extracted values only
- The JSON must be stringified (serialized to a single string) before being placed in the header value
- The metadata payload follows the same schema as the Agreement PATCH endpoint request body
- Values provided via metadata will be applied to the agreement after creation, overriding any AI-extracted values for the same fields

**Firewall & Network Configuration**:

If your organization uses firewalls or network restrictions, you may need to whitelist the following Azure Blob Storage domains
to ensure successful document uploads. The upload URLs returned by this API will use one of these domains based on your
account's geographic region:

**Primary Storage Endpoints**:

- `https://docupstorageaustauepsto.blob.core.windows.net/`
- `https://docupstoragecanacacpsto.blob.core.windows.net/`
- `https://docupstoragecentcuspsto.blob.core.windows.net/`
- `https://docupstorageeasteu2psto.blob.core.windows.net/`
- `https://docupstorageeasteusdsto.blob.core.windows.net/` (Demo)
- `https://docupstoragejapajpepsto.blob.core.windows.net/`
- `https://docupstoragenortneupsto.blob.core.windows.net/`
- `https://docupstoragewestweupsto.blob.core.windows.net/`
- `https://docupstoragewestwu3dsto.blob.core.windows.net/` (Demo)

**Secondary Storage Endpoints** (for redundancy/failover):

- `https://docupstorageaustauepsto-secondary.blob.core.windows.net/`
- `https://docupstoragecanacacpsto-secondary.blob.core.windows.net/`
- `https://docupstoragecentcuspsto-secondary.blob.core.windows.net/`
- `https://docupstorageeasteu2psto-secondary.blob.core.windows.net/`
- `https://docupstorageeasteusdsto-secondary.blob.core.windows.net/` (Demo)
- `https://docupstoragejapajpepsto-secondary.blob.core.windows.net/`
- `https://docupstoragenortneupsto-secondary.blob.core.windows.net/`
- `https://docupstoragewestweupsto-secondary.blob.core.windows.net/`
- `https://docupstoragewestwu3dsto-secondary.blob.core.windows.net/` (Demo)

**Note**: You may whitelist all domains listed above, or contact your DocuSign administrator to determine which specific
region(s) your account uses to minimize the whitelist scope.

**Supported File Formats & Content Types**:

The table below shows common file formats and their recommended Content-Type headers.
**Note**: For the most up-to-date list of supported formats, headers, and constraints, always refer to the
`_action_templates` object in the API response, which provides dynamic configuration including:

- `allowed_formats`: Current list of supported file extensions
- `headers`: Required HTTP headers with examples
- `constraints`: Maximum file size and other limits
- `success_status_code`: Expected response code for successful uploads

| Format | Extension | Content-Type |
| --- | --- | --- |
| PDF | .pdf | `application/pdf` |
| Word Document (2007+) | .docx | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| Word Document (Legacy) | .doc | `application/msword` |
| PowerPoint Presentation (2007+) | .pptx | `application/vnd.openxmlformats-officedocument.presentationml.presentation` |
| PowerPoint Presentation (Legacy) | .ppt | `application/vnd.ms-powerpoint` |
| PowerPoint Slideshow | .ppsx | `application/vnd.openxmlformats-officedocument.presentationml.slideshow` |
| Excel Workbook (2007+) | .xlsx | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| Excel Workbook (Legacy) | .xls | `application/vnd.ms-excel` |
| Excel Binary Workbook | .xlsb | `application/vnd.ms-excel.sheet.binary.macroenabled.12` |
| Rich Text Format | .rtf | `text/rtf` |
| WordPerfect Document | .wpd | `application/vnd.wordperfect` |
| HTML | .html, .htm | `text/html` |
| JPEG Image | .jpg, .jpeg | `image/jpeg` |
| PNG Image | .png | `image/png` |
| TIFF Image | .tif, .tiff | `image/tiff` |

**Example Upload Requests**:

PDF Document (with optional metadata):

```
PUT https://storage.blob.core.windows.net/container/doc-id?signature=...
Content-Type: application/pdf
x_ms_blob-type: BlockBlob
x_ms_meta-filename: contract.pdf
x_ms_meta-metadata: "{\"provisions\":{\"jurisdiction\":\"California\"},\"custom_provisions\":{\"c_ClientId\":\"value\"}}"

[Binary PDF data]
```

Word Document:

```
PUT https://storage.blob.core.windows.net/container/doc-id?signature=...
Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
x_ms_blob-type: BlockBlob
x_ms_meta-filename: agreement.docx

[Binary DOCX data]
```

Image:

```
PUT https://storage.blob.core.windows.net/container/doc-id?signature=...
Content-Type: image/jpeg
x_ms_blob-type: BlockBlob
x_ms_meta-filename: signed-page.jpg

[Binary JPEG data]
```

HTTP Request

POST

```
/v1/accounts/{accountId}/upload/jobs
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

Request Body

CreateBulkJob

---

CreateBulkJob

\*required

required: expected\_number\_of\_docs

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

upload/jobs"

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
