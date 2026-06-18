---
title: Content API
source_url: https://developers.docusign.com/docs/clm-api/clm.cm/clm101/content-api/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- CLM.CM
- CLM.CM
- API 101
- API 101
- Content Api
scraped_at: '2026-06-18T21:48:56Z'
---

# Content API

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

The Content API’s purpose is to allow upload, download, and versioning of documents in Docusign CLM.

The URL’s for Content API operations are generally discovered as properties of the Object API’s Document and Folder objects. For performance reasons, the Content API uses different base URLs than the Object and Task API. See [Base URLs](https://developers.docusign.com/docs/clm-api/clm.cm/clm101/overview/) for more information.

## Document download

The URI for downloading a document via the REST API is in general the same path as getting document object via the Object API, however the base URL is different for the Object and Content API. As a convenience, the Document object contains a **DownloadDocumentHref** property. A GET to this URI will retrieve the document content stream in its native format. For certain document types Docusign CLM will create copies of the document in different formats. To download the document in a format other than the native content type, specify the desired content type via the ACCEPT header. The following document types are supported:

- **Native** – Not sending an ACCEPT header or specifying an accept header of **native** will download the document in the original format it was uploaded. This is supported for all documents in Docusign CLM.
- **PDF** – This is supported for native PDFs, Word, Excel, PowerPoint, and text files (check this). Specify the content type of **application/pdf** to download the PDF rendition of the document. Note that the creation of the PDF document is an asynchronous operation in Docusign CLM. A newly uploaded or created document can be downloaded immediately in its native format, however the PDF rendition will not be available for download until a short time after upload/creation. The **PageCount** property of a document will be populated as part of PDF creation. Generally, if the **PageCount** property of the document object is greater than zero, the PDF rendition of the document can be requested. If a PDF rendition is not available for a document, a **404** response will be returned.
- **Text** – Docusign CLM will execute OCR (Optical Character Recognition) for PDFs, most image types, and Office documents (check this) as part of full text indexing the documents for search. Docusign CLM stores the OCR’d text and makes it available for download via the Content API. To download the OCR’d text, specify **text/plain** in the ACCEPT header. If no text is available for a given document, a **404** response is returned. OCR text extraction for a document is an asynchronous process in Docusign CLM, so it will not available for a short time after newly creating or uploading a document in Docusign CLM.
- **Image** – For any document that has a PDF rendition in Docusign CLM, a PNG image of a given page at a given zoom level can be requested. To request the **png** download of a document specify **image/png** in the ACCEPT header. If a specific page or zoom is not requested, page 1 of the document at the default zoom (generally 100%) set for the account will be returned. To ask for a specific page, the **page** query string parameter may be appended set to the specific page to be download. If a zoom level other than the default zoom is needed, the **zoom** query string parameter may be appended to the URI. Valid values for **zoom** are **thumbnail**, **50, 75, 100, 125, 150,** and **200**. Unlike PDFs and OCR text, png images are generated on the fly when requested via the API and then cached for an indefinite period of time. If the image is available from the cache at the time of the request, it will be returned immediately. If it is not, it will be queued for creation and a response similar to the one shown below will be returned. Docusign CLM does not support a strict SLA for png creation time, however it is generally available within a few seconds and developers using this request method should code retry logic accordingly.

### Error object when a document preview image is not yet available

The example to the right shows a sample error object returned when a document preview image is not available.

1

2

3

4

5

6

7

8

9

{

"Error": {

"HttpStatusCode": 404,

"UserMessage": "Document Not Yet Available",

"DeveloperMessage": "Document Not Yet Available",

"ErrorCode": 119,

"ReferenceId":

"77e94e25-xxxx-xxxx-xxxx-d297ff6730ac"

}

}

### Document download - native document hashes

When downloading most documents, Docusign CLM will add a custom **X-SpringCM-Content-SHA256** header to the header collection. As the name implies, this will be a base64 encoded SHA256 hash of the native content that can be used to verify the download. Hashes of content other than the native file are not supported at this time.

In some cases, it maybe be desirable to retrieve the SHA256 hash generated by Docusign CLM on the server side without downloading the entire document. To enable this, a HEAD request may be made to the download URL to only retrieve the download headers without asking the server to send the full document body in the response.

## Document upload – new document creation

There are 2 items that are required when uploading a new document to Docusign CLM, the target parent folder for the document and the document’s name. The URI template for uploading a document to a particular folder is specified on the object API folder object in the **CreateDocumentHref** property. For general reference the URI will be as follows:

### Document Upload Format

`https://apiupload[datacenter].springcm.com/[api version]/folders/[folder identifier]/documents{?name}`

The {?name} is the RFC 6570 (link) nomenclature to specify that a **name** parameter must be added to the query string to indicate the target name of the document being uploaded. This is only required if a document is being streamed to the upload endpoint.

One or more documents may also be uploaded via the **multipart/form-data** content type. In this case, the native document names will be used and names are not appended to the query string.

If a file is successfully uploaded, the server will return a **201** **Created** response and the document object of the uploaded file. In the case where multiple documents are successfully uploaded in a multi-part form, an array of document objects will be returned.

## Document upload – versioning a document

The **Lock** object is a child object of a document and is used to manage document check in, check out, and versioning. The lock object is also used to monitor when a document is sent out for electronic signature, as this is a special type of document check out. The document lock object can have the following properties:

- **IsLocked** (boolean): If the document is locked.
- **LockDate** (string): When the document was locked. Null if the document is not locked.
- **Type** (string): Type of document lock. Possibilities: not checked out, checked out, out for signature
- **Comment** (string): Comment provided by the user when the document was locked.
- **LockOwner** (User): The owner of the lock. Null if not locked.
- **CheckInHref** (string): If the document is checked out, this is the URI where it can be checked in.
- **SignatureHref** (string): If the lock due to a pending signature(s), this is the URI for checking signature status.
- **Href** (string): Uri where the object can be retrieved.

The lock object for a document is retrieved either by a GET request to the URI specified in the documents **Lock.Href** or by adding **expand=lock** to the query string when requesting the document object. A lock object on a document that is not checked out will be similar to the following:

### Sample Lock object

The document can be versioned by making a POST request to the **CheckInHref** of the lock object of the document. Note that is this is the same URI as the document object itself but has substituted the API upload base URL for the Object API base URL.

In the case where a document must be checked out by a user so that no one else may upload a document until the current user is finished with it, an empty POST request may be made to the URI specified in the **Lock.Href** property. To cancel the checkout a DELETE request may be made to the same URI. To check the document back in a PUT or PATCH request can be made to the same URI.

1

2

3

4

5

6

7

{

"Lock": {

"IsLocked": false,

"Type": "NotCheckedOut",

"CheckInHref": "https://apiuploadna11.springcm.

com/v201411/documents/

133d190e-xxxx-xxxx-xxxx-3863bb335c14"

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
