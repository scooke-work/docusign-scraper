---
title: File output cloud storage extension overview
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- File Output Cloud Storage
scraped_at: '2026-06-18T19:51:49Z'
---

# File output cloud storage extension overview

The file output cloud storage extension exports completed agreements to a cloud storage service. Agreements are written to cloud storage in real time as customers complete tasks in a [workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html). For example, a workflow for adding an account beneficiary can automatically store the beneficiary document after a customer has signed it.

Docusign offers extension apps that integrate with Google Drive, Dropbox, Box, OneDrive, and SharePoint. If you want to store files to these services, visit the [Docusign App Center](https://apps.docusign.com/app-center) for details.

## Use a file output cloud storage extension in a workflow

After a file output to cloud storage extension app has been [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to a Docusign account, a workflow process builder can include a step that invokes the extension. In the example described here, a process builder defines a workflow that adds a beneficiary to a financial account. The workflow steps include:

1. A customer supplies beneficiary information in a web form and submits it.
2. The customer completes an eSignature [envelope](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=gso1578456465211.html) to confirm the beneficiary update.
3. The extension writes the completed envelope to the cloud storage system.

Expand the sections below to see how a file output cloud storage extension functions during workflow [configuration](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=tco1697826811758.html) and [execution](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=zbf1698707257742.html). See [File output cloud storage actions and capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/#file-output-cloud-storage-actions-and-capabilities) for details about the functionality.

## File output cloud storage actions and capabilities

A file output cloud storage extension implements the [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) listed below. Both actions and capabilities send requests to an external API service. Actions are required and provide the core functionality for an extension. Capabilities are optional and offer additional features to enhance the core functionality.

|  |  |  |
| --- | --- | --- |
| **Action or capability** | **Executed when** | **Description** |
| [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#write-file) action | A running workflow instance reaches a file output step that stores a completed agreement in a cloud storage system. | **Required.** Writes a completed agreement file to the cloud storage system. If the file output cloud storage extension implements **List Drives**, the file is written to the drive (or similar container type) that the process builder selected during workflow configuration. If the extension implements **List Directory Contents**, the file is written to the folder that the process builder selected. |
| [List Drives](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#list-drives) capability | While configuring a file output to cloud storage workflow step, a process builder selects a [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/). If only one connection is available, this request is sent when the step configuration page loads. | **Optional.** Gets a list of drives on the cloud storage system. This enables the process builder to select a destination drive. This capability is appropriate for cloud storage systems that have drives or similar structures that contain folders and files. |
| [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#list-directory-contents) capability | While configuring a file output to cloud storage step, a process builder selects **Add Folder** or **Add Subfolder** to display a list of folders. | **Optional.** Gets a list of the folders in the selected drive (or similar container type) or directory on the cloud storage system. This enables the process builder to select a destination folder from a list of existing folders or to specify a naming convention for a new folder. |

## Workflow configuration requests to the external system

This flow shows how the file output cloud storage extension’s optional [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) can be invoked during configuration of a Maestro workflow. These capabilities enable a process builder to configure a file destination in the cloud storage system.

This flow describes the sequence of calls to the external system when an extension app implements the optional **List Drives** and **List Directory Contents** capabilities. An extension app that writes to cloud storage can be implemented without these capabilities. See [External system logic to return file output destination options](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/#external-system-logic-to-return-file-destination-options) for details.

**List Drives capability:** When a process builder configures a file output step, Docusign sends a **List Drives** request to the external system to retrieve a list of drives or similar structures that contain folders and files. The file output step configuration page displays the list in a dropdown.

**List Directory Contents capability:** The process builder’s selection of the **Add Folder** button on the step configuration page causes Docusign to launch a **List Directory Contents** request. The page displays the folder names from the response in a dropdown. The process builder selects the destination folder for files that will be written to cloud storage. To drill down further in the directory structure, the process builder can select **Add Subfolder** one or more times, and a **List Directory Contents** request is launched each time.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1736' width='1288' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Workflow configuration requests](https://images.ctfassets.net/aj9z008chlq0/6RluH6ybPIVEkConnjT2Mc/91238b646ab62e245de210cb9bea81d2/WorkflowConfigurationRequests.png?w=1288&h=1736&q=50&fm=png)

## Workflow instance runtime requests to the external system

This flow shows how the file output cloud storage extension is invoked during the execution of a workflow instance.

**Write File action:** When a running workflow instance reaches a file output to cloud storage step, Docusign sends a **Write File** request to the external system. The request includes a Base64-encoded string representing the file contents, as well as naming details for the file and the location where it should be stored. The external system responds with a message indicating the result.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1118' width='1288' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Example workflow instance runtime flow](https://images.ctfassets.net/aj9z008chlq0/1265Dc6uQcgjSyYjNSC24n/d0b72ce52e54fb4fa2640cbf2f955eeb/WorkflowInstanceRequest.png?w=1288&h=1118&q=50&fm=png)

## Plan a file output to cloud storage implementation

These sections describe options that should be considered when planning a file output to cloud storage implementation:

- [Extension implementation details](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/#extension-implementation-details)
- [Configuration options and restrictions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/#configuration-options-and-restrictions)
- [Mechanisms for starting workflow instances](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/#mechanisms-for-starting-workflow-instances)

### Extension implementation details

Your implementation choices for the file output cloud storage extension determine the details of how files are written to cloud storage. See the next two sections for guidance.

#### External system logic to return file destination options

The file output cloud storage extension supports [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) that enable workflow process builders to select the location where completed agreements will be archived. Below are the available options and the capabilities that enable each option.

|  |  |
| --- | --- |
| **To enable the process builder to** | **Implement this capability** |
| Select a drive or similar structure that contains folders and files | **List Drives** |
| Select an existing folder at any level in the directory structure, specify the creation of a new folder, and define a naming convention for new folders | **List Directory Contents** |
| Select a drive or similar structure, select an existing folder at any level in the directory structure, specify the creation of a new folder, and define a naming convention for new folders | **List Drives** and **List Directory Contents** |

If the extension enables the process builder to select a drive (or similar container type) and/or a folder, at workflow instance runtime, Docusign sends the configured container and/or folder path with **Write File** requests.

If the app does not implement capabilities to allow process builders to select a file destination, **Write File** requests will include a file naming convention only. The external system must implement logic to select a storage location. If the cloud storage system has a structure similar to Google Drive, Docusign recommends implementing both the **List Drives** and **List Directory Contents** capabilities.

See the [file output cloud storage extension contract](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/) for details about the request formats and the expected response formats. See [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) for guidance about transforming requests and responses to the correct format.

#### External system logic to process Write File requests

Docusign includes the file contents, a file naming convention, and, optionally, a drive (or similar container type) and/or a folder in **Write File** requests.

Some considerations for the external system logic to process these requests include:

- If the extension does not implement capabilities that allow a workflow process builder to specify a storage location, how will the external system select a location when it receives a request to write a file?
- Both the file and folder name in the request can include variables whose values are populated during workflow instance execution. The external system must implement logic to construct the folder and/or file names from the variable values in requests. See [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#write-file) for details.
- Will the external system allow an existing file to be overwritten, if the file name in the request already exists in the specified directory? If not, will it write the file with a different name or return an error?

For details about the **Write File** request and response formats, see the [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#write-file) action contract. See [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) for guidance about transforming requests and responses to the required format.

### Configuration options and restrictions

Workflow Builder workflows are highly customizable and offer many possibilities for constructing the [steps in an agreement process](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=afu1730332596907.html). To write files to cloud storage, a workflow must be configured with these steps at minimum:

- **Send Documents for Signature** **step.** This is a step in which a customer completes an eSignature [envelope](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=gso1578456465211.html). Detailed requirements and the process to define this type of step appear in [Configure a Send Documents for Signature Step﻿](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uww1698167288211.html).
- **File output step.** This step invokes the file output cloud storage extension. This step will be available to workflows in any Docusign account that has the extension app [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html).

You can add other types of steps as needed based on business requirements. For a walkthrough of the process to define a simple workflow that invokes a file output cloud storage extension, see [File output cloud storage extension workflow test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/).

These restrictions apply when implementing file output to cloud storage:

- When you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/), you cannot include both a file output cloud storage extension and a [file output system of record extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/) in the same app. If you need to use both types of output in workflows, register a separate app for each extension.
- Only envelopes generated from a workflow **Send Documents for Signature** step can be written to cloud storage.
- The maximum supported size for a file to be written to cloud storage is 10 MB. The workflow process builder must ensure that the template selected in the **Send Documents for Signature** step is within this limit.
- If multiple envelopes are to be written to cloud storage, the process builder must define a separate file output to cloud storage step for each envelope.

### Mechanisms for starting workflow instances

Docusign supports multiple options for starting workflow instances that write files to cloud storage. A workflow instance is a runtime execution of workflow steps that enables a customer to complete tasks such as filling out a form and signing an agreement.

To review the options for starting workflow instances manually, see [How to Start a Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html).

To start workflow instances programmatically, you can implement a Docusign Workflow Builder API integration that includes the [Workflows: triggerWorkflow](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/triggerworkflow/) request. See [Workflow Builder API 101 overview](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/) for an introduction to the API, and see [How to trigger a Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/) for example code and a detailed walkthrough.

## Next steps

- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- See [File output cloud storage extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/) for details about the action and capability requests and responses.
- Learn how to programmatically [trigger workflows](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/) that write files to cloud storage.

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
