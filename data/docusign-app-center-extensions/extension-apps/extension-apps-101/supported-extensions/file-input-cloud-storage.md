---
title: File input cloud storage extension overview
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- File Input Cloud Storage
scraped_at: '2026-06-18T19:51:49Z'
---

# File input cloud storage extension overview

The file input cloud storage extension imports agreements from a cloud storage service to [Docusign Agreement Manager](https://www.docusign.com/products/platform/agreement-manager), a smart repository that uses AI analysis to transform flat, unstructured documents into structured data points.

After files have been imported into Agreement manager, your organization can:

- Use robust [search features](https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=qzl1712244340883.html) to easily locate agreements
- Manage [agreement obligations](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=csm1727128259486.html), such as payments, renewal notices, and termination notices
- Gain valuable insights into agreement data with [dashboards and reports](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=jyq1749000353004.html)
- Track schedules for agreement [renewals and terminations](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=hjg1712251035061.html)
- Implement a [Agreement Manager API](https://developers.docusign.com/docs/agreement-manager-api/) integration to programmatically retrieve agreement data for additional processing on your system

For example, a municipal government can implement a file input from cloud storage solution to store documents such as contracts, funding applications, and meeting minutes. After the files have been uploaded to Agreement Manager and processed by AI, municipal workers can finalize agreements faster, easily fulfill document requests from elected officials and constituents, and track and act on upcoming contract renewals.

## When to use a file input extension instead of other import options

Agreement Manager offers several [standard file import methods](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=rrs1712255668350.html) that enable users to select files stored in these locations:

- A user's local machine or an accessible drive
- Cloud storage platforms, including Google Drive, Dropbox, Box, OneDrive, and SharePoint
- Email attachments

To complement these standard import methods, you can use the file input cloud storage extension to implement a customized import process. This option can be used if the Docusign [App Center](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=twl1726764423921.html) does not offer an app that integrates with your cloud storage platform. A custom solution also enables your organization to implement code within your own application to meet specific business requirements. For example, you can impose custom restrictions on files that can be imported into Agreement Manager. You can also log imports to address reporting or compliance requirements. In addition, you can trigger notifications or other downstream processing after imports. Finally, a custom file import solution can be implemented as a [private extension app](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/), which enables you to control which Docusign accounts can install and use the app.

This extension cannot be included in the same extension app manifest or form-based app registration alongside the file input system of record extension.

## Use a file input cloud storage extension in Agreement Manager

After a file input from cloud storage extension app has been [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to a Docusign account, it can be invoked to upload files into Agreement Manager. Expand the sections below to see how the extension functions during Agreement Manager [agreement upload](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=rrs1712255668350.html). See [File input cloud storage actions and capability](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/#file-input-cloud-storage-actions-and-capability) for details about the functionality.

## File input cloud storage actions and capability

A file input cloud storage extension implements the [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capability](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) listed below. Both actions and capabilities send requests to an external API service. Actions are required and provide the core functionality for an extension. Capabilities are optional and offer additional features to enhance the core functionality.

| Action or capability | Executed when | Description |
| --- | --- | --- |
| [Get File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file) action | A user selects one or more files to upload on the Agreement Manager **Select Files** window and submits the request. | **Required.** Uploads files from the cloud storage system to Agreement Manager. This action is invoked once for each file. |
| [List Drives](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-drives) capability | A user selects a [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/) on the Agreement Manager **Select Files** window. | **Optional.** Gets a list of cloud storage drives. This enables the user to select a drive that contains files to be uploaded. This capability is appropriate for cloud storage systems that have drives or similar structures that contain folders and files. |
| [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-directory-contents) action | A user does either of the following:  - Selects a drive on the Agreement Manager **Select Files** window and then selects **Next** - Selects a folder on the **Select Files** window | **Required**. Gets a list of the folders and files in the selected cloud storage drive (or similar container type) or directory. The list is displayed on the **Select Files** window so that the user can either select files to upload or select another folder to drill down into the cloud storage structure. |
| [Search](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#search) action | A user enters a search string on the Agreement Manager **Select Files** window. | **Required.** Returns a list of cloud storage folders and files whose names match the search string. |

## Requests that enable users to locate files for upload

This flow shows how the file input cloud storage extension’s actions and capability are invoked to enable users to locate files for upload.

This flow describes the sequence of calls to the external system when an extension app implements the optional **List Drives** capability. An extension app can be implemented without this capability. See [External system logic to return cloud storage content lists](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/#external-system-logic-to-return-cloud-storage-content-lists) for details.

**List Drives capability:** When a user starts the process to locate files for upload, Docusign sends a **List Drives** request to the external system to retrieve a list of drives or similar structures that contain folders and files. The **Select Files** window displays the list in a dropdown.

**List Directory Contents action:** The user’s selection of a drive causes Docusign to launch a **List Directory Contents** request. The **Select Files** window displays the folder and file names returned in the response. To drill down further in the directory structure, the user can select subfolders. A **List Directory Contents** request is launched with each new selection of a subfolder. The user can then choose files for upload. 

**Search action:** At any point during the process of locating files, the user can enter a search string, which triggers a **Search** request to the external system. The **Select Files** window displays the matching files and folders that the external system returns in the response. The user can then select files for upload.

For details about the request and response contents, see the [extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/).

![](data:image/svg+xml;charset=utf-8,%3Csvg height='2193' width='1288' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Locate files for upload](https://images.ctfassets.net/aj9z008chlq0/60EzDO5rKuAbV6GbFUptFw/92fb5a7a06d98f64d9078231d5b52e5b/LocateFilesFlow.png?w=1288&h=2193&q=50&fm=png)

## Requests in the file upload process

This example flow shows a sequence of requests and responses between Docusign and the external system when a **Get File** action is initiated to upload a file from cloud storage to Agreement Manager. For details about the request and response contents, as well as error handling, see the [extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/).

If a user selects multiple files for upload in Agreement Manager, the sequence described here is repeated for each file.

1. Docusign sends a **Get File** request to the external service. The request includes the ID of the file that a Agreement Manager user selected for upload.
2. The external service responds to the **Get File** request.
3. The external service sends Docusign the file contents.
4. Docusign sends a response to indicate whether it processed the uploaded file successfully.
5. The external service sends a callback request to Docusign to report whether the upload succeeded or failed.
6. Docusign sends a response to the callback request.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1734' width='1288' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![File upload flow](https://images.ctfassets.net/aj9z008chlq0/1QoGzrbL9LPIz5BPdX27l8/b299a8ceb733cf8a6e37e6f391cf93af/FileUploadFlow.png?w=1288&h=1734&q=50&fm=png)

## Plan a file input from cloud storage implementation

These sections describe options that should be considered when planning a file input from cloud storage implementation:

- [External system logic to return cloud storage content lists](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/#external-system-logic-to-return-cloud-storage-content-lists)
- [External system logic to upload files](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/#external-system-logic-to-upload-files)

### External system logic to return cloud storage content lists

Your implementation choices determine which cloud storage locations and files Agreement Manager users can select when locating files for import. See the next sections for considerations.

#### Determine whether users can select a drive or similar container

The file input cloud storage extension has an optional **List Drives** capability. If you want Agreement Manager users to choose from a list of drives or similar containers on the Agreement Manager **Select Files** window, your extension app should implement this capability. If you do not implement it, the external system must determine the drive or similar container whose files and folders are returned when Docusign sends a **List Directory Contents** request.

#### Restrict access to files and folders if appropriate

When Docusign sends a **List Directory Contents** request, the external system can determine which folders and files it returns for display on the Agreement Manager **Select Files** window. To comply with your organization's security or privacy requirements, your extension app can omit certain folders and files from its response to a **List Directory Contents** request.

#### Adhere to file upload limitations

In response to a **List Directory Contents** or **Search** request, the external service should only return files that meet the restrictions listed below. Docusign will return an error response to an upload request for a file that does not meet these restrictions.

| File attribute | Restriction | Notes |
| --- | --- | --- |
| Size | 25 MB maximum |  |
| File type | Must be one of the following:   - .doc, .docx - .htm, .html - .jpg, .jpeg - .pdf - .png - .ppt, .ppsx, .pptx - .tif, .tiff - .wpd - .xls, .xlsb, .xlsx | These are the currently supported file types.  This list may change. The external service should always check the list of supported MIME types included in [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-directory-contents) and [Search](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#search) requests, and only return files of those types. |
| Name | Can be up to 254 characters long |  |

### External system logic to upload files

When a Agreement Manager user selects files for upload, Docusign sends a separate **Get File** request for each file that a user selects for upload. As a result, the external service can receive multiple **Get File** requests in a short time. The service should implement logic to queue and process them. See [Get File sequence of requests and responses](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file-sequence-of-requests-and-responses) for details about the sequence of calls required to process each **Get File** request from Docusign.

## Next steps

- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- See [File input cloud storage extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/) for details about the action and capability requests and responses.
- Learn more about [private extension apps](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/), which are available only to specified Docusign accounts.

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
