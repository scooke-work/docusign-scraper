---
title: Migrating from the SOAP API to the CLM API
source_url: https://developers.docusign.com/docs/clm-api/clm.cm/clm101/migrating-soap-to-rest/
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
- Migrating Soap To Rest
scraped_at: '2026-06-18T21:48:56Z'
---

# Migrating from the SOAP API to the CLM API

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

If you are already using the SpringCM SOAP API, this page will help you map your existing code if you choose to transition to the CLM API. The following table shows the equivalent REST API calls for a given SOAP call. The CLM API also includes additional functionality that is not exposed in the SOAP API.SOAP API calls not listed here are either deprecated or scheduled to be upgraded in a future release.

| SOAP API | REST API |
| --- | --- |
| AccountGetCurrent | GET /{apiversion}/accounts/current See also: [Get the account of the current user](https://apidocsna11.springcm.com/apidocs#!/Accounts/Accounts_Get) |
| Authenticate | See the [REST API Authentication](https://developers.docusign.com/docs/clm-api/clm.cm/clm101/authentication/) section |
| AuthenticateNonDefault | See the [REST API Authentication](https://developers.docusign.com/docs/clm-api/clm.cm/clm101/authentication/) section |
| AuthenticateSSO | See [Salesforce Client Flow Authentication](https://developers.docusign.com/docs/clm-api/clm.cm/clm101/authentication/salesforce-client-flow/) section |
| BPMAbortWorkflow | DELETE /{apiversion}/workflows/{instanceId} See also: [Stop a workflow instance](https://apidocsna11.springcm.com/apidocs#!/Workflows/Workflows_Delete) |
| BPMInitiateWorkflow | POST /{apiversion}/workflows See also: [Start a workflow instance](https://apidocsna11.springcm.com/apidocs#!/Workflows/Workflows_Post)  Pass the data to start the workflow in the Params property |
| BPMInitiateWorkflowWithDocuments | POST /{apiversion}/workflows See also: [Start a workflow instance](https://apidocsna11.springcm.com/apidocs#!/Workflows/Workflows_Post)  Pass the data to start the workflow in the WorkflowDocuments collection property |
| BPMSignalWorkflow | POST /{apiversion}/workflows/{instanceId}/signal See also: [Signal a workflow](https://apidocsna11.springcm.com/apidocs#!/Workflows/Workflows_PostSignal) |
| BPMWorkflowInstanceInformation | GET /{apiversion}/workflows/{instanceId} See also: [Get a workflow instance](https://apidocsna11.springcm.com/apidocs#!/Workflows/Workflows_Get) |
| ContactFind | GET /{apiversion}/contacts Filterable on Email, First Name, Last Name, Company  See also: [Get the contacts of the current account](https://apidocsna11.springcm.com/apidocs#!/Contacts/Contacts_GetAllContacts) |
| Copy | POST /{apiversion}/copytasks See also: [CopyTasks](https://apidocsna11.springcm.com/apidocs#!/CopyTasks) |
| Delete  DeleteBaseObjects | Use the DELETE method on the specific object HREF. Will vary for object type:  [Contacts](https://apidocsna11.springcm.com/apidocs#!/Contacts/Contacts_Delete) – DELETE /{apiversion}/contacts/{id}  [Documents](https://apidocsna11.springcm.com/apidocs#!/Documents/Documents_DeleteDocument) – DELETE /{apiversion}/documents/{id}  [Folders](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_Delete) – DELETE /{apiversion}/folders/{id}  [Groups](https://apidocsna11.springcm.com/apidocs#!/Groups/Groups_Delete) – DELETE /{apiversion}/groups/{id}  [Users](https://apidocsna11.springcm.com/apidocs#!/Users/Users_Delete) – DELETE /{apiversion}/users/{id} |
| DocumentCheckin  DocumentCheckout  DocumentCheckoutCancel | Working with checkins and checkouts without versioning the content is done with the “lock” object. Document objects will always have one and only one “lock” object that manages the document checkin/checkout. See the [Content API](https://developers.docusign.com/docs/clm-api/clm.cm/clm101/content-api/) documentation for details on working with the lock object as well as the [Document](https://apidocsna11.springcm.com/apidocs#!/Documents) object method level documentation |
| DocumentCreateBeginWithFolder  DocumentCreateCancel  DocumentCreateCheckin  DocumentCreateCommit  DocumentCreateFilesBegin  DocumentCreateFilesCommit  DocumentCreateUploadChunk | See the [Content API](https://developers.docusign.com/docs/clm-api/clm.cm/clm101/content-api/) documentation for information on uploading new documents. |
| DocumentDownload  DocumentDownloadPreviewImage  DocumentGetExtractedText  DocumentHash | See the [Content API](https://developers.docusign.com/docs/clm-api/clm.cm/clm101/content-api/) documentation for information on downloading documents in various supported formats. |
| DocumentGetById | GET /{apiversion}/documents/{id} See also: [Get a document by ID](https://apidocsna11.springcm.com/apidocs#!/Documents/Documents_Get) |
| DocumentGetPath | GET /{apiversion}/documents?path={path to document} See also: [Get a document by path](https://apidocsna11.springcm.com/apidocs#!/Documents/Documents_GetByPath) |
| DocumentHistoryGetById | GET /{apiversion}/documents/{id}?expand=historyitems  GET /{apiversion}/documents/{id}/historyitems See also: [Get the history of a document](https://apidocsna11.springcm.com/apidocs#!/Documents/Documents_GetHistoryItems) |
| DocumentMerge  DocumentMergeCheck  DocumentMergeDownload | POST /{apiversion}/documentmergetasks See also: [DocumentMergeTasks](https://apidocsna11.springcm.com/apidocs#!/DocumentMergeTasks) |
| DocumentPagedSearch  DocumentSearch | POST /{apiversion}/documentsearchtasks See also: [DocumentSearchTasks](https://apidocsna11.springcm.com/apidocs#!/DocumentSearchTasks) |
| DocumentPublish | POST /{apiversion}/sharelinks DocumentPublish is deprecated. The [Sharelinks](https://apidocsna11.springcm.com/apidocs#!/ShareLinks) object should be used instead. |
| DocumentSave | PUT /{apiversion}/documents/{id}  PATCH /{apiversion}/documents/{id} See also: [PUT - Update a document](https://apidocsna11.springcm.com/apidocs#!/Documents/Documents_Put), [PATCH - Update a document](https://apidocsna11.springcm.com/apidocs#!/Documents/Documents_Patch) |
| DocumentSendForSignature  DocumentSendForSignatureCancel  DocumentSendForSignatureStatus | POST /{apiversion}/signaturetasks See also: [SignatureTasks](https://apidocsna11.springcm.com/apidocs#!/SignatureTasks) |
| DocumentSplit | POST /{apiversion}/splitdocumenttasks See also: [SplitDocumentTasks](https://apidocsna11.springcm.com/apidocs#!/SplitDocumentTasks) |
| DocumentXMLMerge  DocumentXMLMergeStatus | POST /{apiversion}/documentxmlmergetasks See also: [DocumentXmlMergeTasks](https://apidocsna11.springcm.com/apidocs#!/DocumentXmlMergeTasks) |
| FindOrCreateEOSFolder | POST /{apiversion}/folders Must supply the EOSInfo object as child on the posted Folder object  The REST API also supports a method to find an EOS Folder that will not create the folder if it is not found:  GET /{apiversion}/folders?eosObjectType={EOS object type}&eosObjectId={EOS Object Id} See also: [Create a folder](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_Post), [Get a folder by EOS object id and type](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_GetByEos) |
| FolderArchive  FolderArchiveDownload  FolderArchiveGetStatus | POST /{apiversion}/folderarchivetasks See also: [FolderArchiveTasks](https://apidocsna11.springcm.com/apidocs#!/FolderArchiveTasks) |
| FolderCreate | POST /{apiversion}/folders See also: [Create a folder](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_Post) |
| FolderGetById | GET /{apiversion}/folders/{id} See also: [Get a folder by ID](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_Get) |
| FolderGetContents SystemFolderGetContents | GET /{apiversion}/folders/{id}?expand=documents,folders  GET /{apiversion}/folders/{id}/documents  GET /{apiversion}/folders/{id}/folders See also: [Get the documents in a folder](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_GetDocuments), [Get the folders in a folder](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_GetChildFolders) |
| FolderGetPath | GET /{apiversion}/folders/{id}?expand=path See also: [Get a folder by path or system folder](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_GetByPathOrSystemFolder) |
| FolderPagedSearch  FolderSearch | /POST /{apiversion/foldersearchtasks See also: [FolderSearchTasks](https://apidocsna11.springcm.com/apidocs#!/FolderSearchTasks) |
| FolderSave | PUT /{apiversion}/folders/{id}  PATCH /{apiversion}/folders/{id} See also: [PUT - Update a folder](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_Put), [PATCH - Update a folder](https://apidocsna11.springcm.com/apidocs#!/Folders/Folders_Patch) |
| GetDocumentRevisions | GET /{apiversion}/documents/{id}?expand=versions  GET /{apiversion}/documents/{id}/versions See also: [Get the versions of a document](https://apidocsna11.springcm.com/apidocs#!/Documents/Documents_GetVersions) |
| GetMetadataFields | GET /{apiversion}/attributegroups/{id} See also: [Get an attribute group](https://apidocsna11.springcm.com/apidocs#!/AttributeGroups/AttributeGroups_Get) |
| GetMetadataGroups | GET /{apiversion}/accounts/current/attributegroups See also: [Get the attribute groups of the current account](https://apidocsna11.springcm.com/apidocs#!/Accounts/Accounts_GetAttributeGroups) |
| GetRecentlyAccessedDocuments | GET /{apiversion}/users/current/recentdocuments See also: [Get the recently accessed documents for the current user](https://apidocsna11.springcm.com/apidocs#!/Users/Users_GetRecentDocumentsCurrent) |
| GroupFind | GET /{apiversion}/groups Filterable on Name, GroupType  See also: [Get the groups in the current account](https://apidocsna11.springcm.com/apidocs#!/Groups/Groups_GetAllGroups) |
| GroupGetByContact | GET /{apiversion}/users/current?expand=groups  GET /{apiversion}/users/current/groups See also: [Get the groups of the current user](https://apidocsna11.springcm.com/apidocs#!/Users/Users_GetGroupsCurrent) |
| ImportSalesforceAttachments  ImportSalesforceAttachmentsStatus | POST /{apiversion}/salesforceattachmentimportasks See also: [SalesforceAttachmentImportTasks](https://apidocsna11.springcm.com/apidocs#!/SalesforceAttachmentImportTasks) |
| Load | There is no generic load in the REST API. Use GET requests to an object endpoint to load an object. |
| Move | There is no specific move task in the REST API. To move a document or folder in the REST API, change the parent folder on the object and PUT/PATCH the document or folder. |
| ParsePath | No exact match in the REST API, but the same functionality can be obtained by first trying the document endpoint as a path, if it’s not found, try the path at the folder endpoint. |
| Save | There is no bulk save in the REST API. PUT/PATCH to a specific object endpoint to save an object. |
| SetPermission | POST /{apiversion}/changesecuritytasks See also: [ChangeSecurityTasks](https://apidocsna11.springcm.com/apidocs#!/ChangeSecurityTasks) |
| UserGetByAccountId | GET /{apiversion}/users See also: [Get the users in the current account](https://apidocsna11.springcm.com/apidocs#!/Users/Users_GetUsers) |

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
