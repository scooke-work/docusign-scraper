---
title: File output tabular format extension overview
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-tabular-format/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- File Output Tabular Format
scraped_at: '2026-06-18T19:51:50Z'
---

# File output tabular format extension overview

The file output tabular format extension exports data from [steps in an agreement process](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=afu1730332596907.html) to tabular format files stored in cloud storage systems. Supported file types are Excel sheets, Google sheets, and CSV files.

## Use a file output tabular format extension in a workflow

After a file output to tabular format extension app has been [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to a Docusign account, a workflow process builder can include a step that invokes the extension. In the example described here, a process builder defines a workflow that verifies an employee’s right to work in compliance with the [United Kingdom’s Right to Work laws](https://www.docusign.com/en-gb/blog/digitalise-your-right-to-work-process-with-digital-identity-checks). The workflow steps include:

1. An employee supplies their information including a Share Code in a web form and submits it.
2. The employee completes identity verification.
3. The extension writes the values entered by the employee and the result of their identity verification to a spreadsheet for compliance.

Expand the sections below to see how a file output tabular format extension functions during workflow [configuration](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=tco1697826811758.html) and [execution](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=zbf1698707257742.html). See [File output tabular format actions and capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-tabular-format/#file-output-tabular-format-actions-and-capabilities) for details about the functionality.

## File output tabular format actions and capabilities

A file output tabular format extension implements the [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) listed below. Both actions and capabilities send requests to an external API service. Actions are required and provide the core functionality for an extension. Capabilities are optional and offer additional features to enhance the core functionality.

| **Action or capability** | **Executed when** | **Description** |
| --- | --- | --- |
| [Export to Destination](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/#export-to-destination) action | A running workflow instance reaches a file output step that exports values of workflow variables to a spreadsheet. | **Required.** Exports values of workflow variables to a spreadsheet. If the file output tabular format extension implements **List Drives**, the values are written to a file in the drive (or similar container type) that the process builder selected during workflow configuration. If the extension implements **List Directory Contents**, the values are written to the file that the process builder selected. |
| [List Headers](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/#list-headers) action | While configuring a file output to tabular format workflow step, a process builder selects variables whose values are to be exported. | **Required.** To ensure no data corruption, a request is sent to check that the number of columns in the destination sheet is greater than or equal to the number of variables being exported. If this check is not successful, the process builder will not be able to complete the step configuration. |
| [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/#list-directory-contents) capability | While configuring a file output to tabular format workflow step, after selecting a drive, a process builder selects a [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/). | **Optional.** Gets a list of the folders and tabular format files in the selected drive (or similar container type) or directory on the cloud storage system. This enables the process builder to select a destination file from a list of existing files. |
| [List Drives](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/#list-drives) capability | While configuring a file output to tabular format workflow step, a process builder selects a [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/). If only one connection is available, this request is sent when the step configuration page loads. | **Optional.** Gets a list of drives on the cloud storage system. This enables the process builder to select a destination drive. This capability is appropriate for cloud storage systems that have drives or similar structures that contain folders and files. |

## Workflow configuration requests to the external system

This flow shows how the file output tabular format extension’s [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and optional [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) can be invoked during configuration of a Maestro workflow. The process builder is able to select a drive and file destination where the workflow variable values will be written.

This flow describes the sequence of calls to the external system when an extension app implements the optional **List Drives** and **List Directory Contents** capabilities. An extension app that exports values to tabular format can be implemented without these capabilities. See [External system logic to return file destination options](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-tabular-format/#extension-implementation-details) for details.

**List Drives capability:** When a process builder configures a file output step, Docusign sends a **List Drives** request to the external system to retrieve a list of drives or similar structures that contain folders and files. The file output step configuration page displays the list in a dropdown.

**List Directory Contents capability:** When a drive has been selected, the system launches a **List Directory Contents** request. The page displays the file names from the response in a list. The process builder selects the destination file to which the values will be exported.

**List Headers action:** After the process builder selects the variables to be written to the destination file, the system sends a **List Headers** request to compare the columns in the destination file to the number of variables being exported. This prevents data corruption in the destination file.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1280' width='656' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A diagram of the file output tabular format extension workflow configuration requests](https://images.ctfassets.net/aj9z008chlq0/1tdIAKn2Xy9IwwSamago0v/42d2ad320da754f876be939c45a0e3e4/TabularFormatWorkflowConfiguration.png?w=656&h=1280&q=50&fm=png)

## Workflow instance runtime requests to the external system

This flow shows how the file output tabular format extension is invoked during the execution of a workflow instance.

**Export to Destination action**: When a running workflow instance reaches a file output to tabular format step, Docusign sends an **Export to Destination** request to the external system. The request includes a Base64-encoded string representing the drive and file information, an array of strings representing the column header names, and a two-dimensional array of strings representing the data being written to the file.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='826' width='844' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A diagram of the requests in a file output tabular format extension at runtime](https://images.ctfassets.net/aj9z008chlq0/1TvBI00rOF6vk9DtUKaVFz/1da45f0a4a89a5b0ff5f118602574c87/TabularFormatWorkflowRuntimeRequests.png?w=844&h=826&q=50&fm=png)

## Plan a file output to tabular format implementation

These sections describe options that should be considered when planning a file output to tabular format implementation:

- [Extension implementation details](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-tabular-format/#extension-implementation-details)
- [Workflow configuration options and restrictions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-tabular-format/#workflow-configuration-options-and-restrictions)
- [Mechanisms for starting workflow instances](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-tabular-format/#mechanisms-for-starting-workflow-instances)

### Extension implementation details

Your implementation choices for the file output tabular format extension determine the details of how values are exported to files stored in cloud storage. See the next two sections for guidance.

#### External system logic to return file destination options

The file output tabular format extension supports capabilities that enable workflow process builders to select the file where the workflow variable values will be written. Below are the available options and the capabilities that enable each option.

| **To enable the process builder to** | **Implement this capability** |
| --- | --- |
| Select a drive or similar structure that contains folders and files. | **List Drives** |
| Select an existing file at any level in the directory structure. | **List Directory Contents** |
| Select a drive or similar structure, and select an existing file in that drive. | **List Drives** and **List Directory Contents** |

If the extension enables the process builder to select a drive (or similar container type), Docusign sends the configured container and/or file path with **Export to Destination** requests at workflow instance runtime.

If the app does not implement capabilities to allow process builders to select a file destination, **Export to Destination** requests will include a file name only. The external system must implement logic to select a storage location. If the cloud storage system has a structure similar to Google Drive, Docusign recommends implementing both the **List Drives** and **List Directory Contents** capabilities.

See the file output tabular format extension contract for details about the request formats and the expected response formats. See [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) for guidance on transforming requests and responses to the correct format.

#### External system logic to process Export to Destination requests

Docusign includes the workflow variables’ values, the file headers, and, optionally, a drive (or similar container type) and/or a file name in **Export to Destination** requests.

Some considerations for the external system logic to process these requests include:

- If the extension does not implement capabilities that enable a workflow process builder to specify a storage location, how will the external system select a location when it receives a request to write data to a file?

For details about the **Export to Destination** request and response formats, see the Export to Destination action contract. See [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) for guidance on transforming requests and responses to the required format.

### Workflow configuration options and restrictions

Workflow Builder workflows are highly customizable and offer many possibilities for constructing the [steps in an agreement process](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=afu1730332596907.html). To export values to a tabular format, a workflow must be configured with a **File output step**, which invokes the file output tabular format extension. This step is available to workflows in any Docusign account that has the extension app [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html).

These restrictions apply when configuring a workflow to write data to tabular format files:

- The maximum number of variable values that can be exported to a tabular format from a workflow is 1,000.
- If values should be exported to multiple different files, the process builder must define a separate file output to tabular format step for each file.
- Not all variable types can be exported from a workflow. Checkboxes and radio groups are not supported in the current release.
- Values will be written to columns in the tabular format file from left to right in the order in which they are configured in the file output tabular format step. Process builders should ensure that the order in which they configure the variables matches the order of any existing columns in the destination file.
- For a file that has existing column headers, if the number of variables selected for export exceeds the number of column headers in the file, additional variable values will be written to new columns with generic headers like **Column 1**.

### Mechanisms for starting workflow instances

Docusign supports multiple options for starting workflow instances that export variable values to tabular format files. A workflow instance is a runtime execution of workflow steps that enables a customer to complete tasks such as filling out a form and signing an agreement.

To start workflow instances manually, see [How to Start a Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html).

To start workflow instances programmatically, you can implement a Docusign Workflow Builder API integration that includes the [Workflows: triggerWorkflow](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/triggerworkflow/) request. See [Workflow Builder API 101 overview](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/) for an introduction to the API, and [How to trigger a Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/) for example code and a detailed walkthrough.

## Next steps

- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- See [File output tabular format extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/) for details about the action and capability requests and responses.
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
