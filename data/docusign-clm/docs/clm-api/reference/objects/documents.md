---
title: Documents Resource
source_url: https://developers.docusign.com/docs/clm-api/reference/objects/documents/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- API Reference
- API Reference
- Objects
- Objects
- Documents
scraped_at: '2026-06-18T21:49:00Z'
---

# Documents Resource

Documents resource

Developing with the CLM API is only available
for CLM customers with a production account.
To purchase a plan to gain access to the CLM API,
contact [Docusign Sales](https://www.docusign.com/contact-sales).

## Methods Supported

| Method | Description |
| --- | --- |
| [Delete](https://developers.docusign.com/docs/clm-api/reference/objects/documents/delete/) | DEL  ```  /v2/{accountId}/documents/{id} ```  Move a document to the trash folder. |
| [DeleteLock](https://developers.docusign.com/docs/clm-api/reference/objects/documents/deletelock/) | DEL  ```  /v2/{accountId}/documents/{id}/lock ```  Release a lock on a document |
| [Get](https://developers.docusign.com/docs/clm-api/reference/objects/documents/get/) | GET  ```  /v2/{accountId}/documents/{id} ```  Get a document by ID |
| [GetByPath](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getbypath/) | GET  ```  /v2/{accountId}/documents ```  Get a document by path |
| [GetCustomData](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getcustomdata/) | GET  ```  /v2/{accountId}/documents/{id}/customdata ```  Query a CSV document by ID |
| [GetDocumentProcessTrackingActivities](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getdocumentprocesstrackingactivities/) | GET  ```  /v2/{accountId}/documents/{id}/documentprocesstrackingactivities ```  Get the workflow user steps containing a document |
| [GetDocumentReminders](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getdocumentreminders/) | GET  ```  /v2/{accountId}/documents/{id}/documentreminders ```  Get the document reminders for a document |
| [GetDocumentWorkItems](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getdocumentworkitems/) | GET  ```  /v2/{accountId}/documents/{id}/workitems ```  Get workitems associated with the document |
| [GetExternalReviewFromDocument](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getexternalreviewfromdocument/) | GET  ```  /v2/{accountId}/documents/{id}/reviews ```  Gets the external review associated with the document |
| [GetHistoryItems](https://developers.docusign.com/docs/clm-api/reference/objects/documents/gethistoryitems/) | GET  ```  /v2/{accountId}/documents/{id}/historyItems ```  Get the history of a document |
| [GetLock](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getlock/) | GET  ```  /v2/{accountId}/documents/{id}/lock ```  Get the lock status of a document |
| [GetRelatedDocuments](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getrelateddocuments/) | GET  ```  /v2/{accountId}/documents/{id}/relateddocuments ```  Get related documents |
| [GetShareLinks](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getsharelinks/) | GET  ```  /v2/{accountId}/documents/{id}/sharelinks ```  Get the share links of a document |
| [GetVersions](https://developers.docusign.com/docs/clm-api/reference/objects/documents/getversions/) | GET  ```  /v2/{accountId}/documents/{id}/versions ```  Get the versions of a document |
| [Patch](https://developers.docusign.com/docs/clm-api/reference/objects/documents/patch/) | PATCH  ```  /v2/{accountId}/documents/{id} ```  Update a document |
| [PatchLock](https://developers.docusign.com/docs/clm-api/reference/objects/documents/patchlock/) | PATCH  ```  /v2/{accountId}/documents/{id}/lock ```  Update a lock on a document |
| [PostLock](https://developers.docusign.com/docs/clm-api/reference/objects/documents/postlock/) | POST  ```  /v2/{accountId}/documents/{id}/lock ```  Create a lock on a document |
| [PublishDocument](https://developers.docusign.com/docs/clm-api/reference/objects/documents/publishdocument/) | POST  ```  /v2/{accountId}/documents/{id}/publish ```  Publishes document by ID. Returns document information. |
| [Put](https://developers.docusign.com/docs/clm-api/reference/objects/documents/put/) | PUT  ```  /v2/{accountId}/documents/{id} ```  Update a document |
| [PutLock](https://developers.docusign.com/docs/clm-api/reference/objects/documents/putlock/) | PUT  ```  /v2/{accountId}/documents/{id}/lock ```  Update a lock on a document |

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
