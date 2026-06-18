---
title: Extensions and actions (beta)
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- File Output System Of Record
- File Output System Of Record
- Extensions And Actions
scraped_at: '2026-06-18T19:51:51Z'
---

# Extensions and actions (beta)

[Extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/) are the components that determine the type of functionality that an extension app implements. Each extension supports one or more [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/). Both actions and capabilities send requests to an external API service. Actions are required and provide the core functionality for an extension. Capabilities are optional and offer additional features to enhance the core functionality. You specify the extensions, actions, and capabilities to include in an extension app when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/).

For file output to system of record, the method your extension app uses for [identifying a destination record](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/) determines the extensions, actions, and capabilities that should be included in the app. See these sections for details:

- [Extensions and actions: Record identifier is a workflow variable](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/#extensions-and-actions-record-identifier-is-a-workflow-variable)
- [Extensions and actions: Record ID is from a Data read step](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/#extensions-and-actions-record-id-is-from-a-data-read-step)

## Extensions and actions: Record identifier is a workflow variable

If a [workflow variable value](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/#use-a-workflow-variable-value) will identify the record to write files to, the file output system of record extension must implement the **Write File** action and the **Get Type Names** capability. Below are descriptions of how they function.

| Extension | Action or capability | Executed when | Description |
| --- | --- | --- | --- |
| File output system of record | [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#get-type-names) capability | A workflow process builder configures a **File Output** step and selects a workflow variable whose value will be sent in the **Write File** request. | Gets the names of objects in your system of record. The names are displayed on the **File Output** step configuration panel to enable the process builder to select the object to write files to. |
| File output system of record | [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) action | A running workflow instance reaches a **File Output** step. | Writes a completed agreement file or files to the system of record.  To enable the external system to identify the destination for the files, the request includes:   - The runtime value of a workflow variable that the process builder selected - The object that the workflow process builder selected |

These sections explain the flow for action and capability execution:

- [Get Type Names flow](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/#get-type-names-flow)
- [Write File flow](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/#write-file-flow)

### Get Type Names flow

When a workflow process builder configures a **File Output** step, a [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#get-type-names) call retrieves a list of objects that your system of record exposes.

Docusign displays the list of objects in a dropdown on the **File Output** step configuration panel. This enables the process builder to select an object to write files to. The object name is included in the **Write File** request during workflow instance execution.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='2040' width='2447' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Get Type Names flow](https://images.ctfassets.net/aj9z008chlq0/5jEC7Omq0eSri16cxjvU1z/97ac6104f29ef3f5304b9482866a18dd/GetTypeNamesFlow.png?w=2447&h=2040&q=50&fm=png)

### Write File flow

As a customer completes the steps in a running workflow instance, Docusign calls [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) to write the envelope file or files to the system of record. The request includes the file contents, the destination object, and a value that can be used to identify the destination record.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1991.0000000000002' width='2448' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Write File flow](https://images.ctfassets.net/aj9z008chlq0/6aKOMArMmbXrAemd2uXXBI/5c77dd7b548e5917bfcc5fe8520058fe/WriteFileFlow.png?w=2448&h=1991&q=50&fm=png)

## Extensions and actions: Record ID is from a Data read step

If a [record ID](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/#use-an-id-returned-by-a-read-from-workflow-step) returned from a workflow **Data read** step will identify the record to write files to, the extension app requires two extensions:

- [Data IO](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/): This extension retrieves data model details from the external system of record and searches for a record to which a file or files will be written. The extension must include these actions:
  - **Get Type Names**
  - **Get Type Definitions**
  - **Search Records**
- [File output system of record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/): This extension writes envelope files to the system of record. The extension must include this action:
  - **Write File**

Below are descriptions of the actions.

| Extension | Action | Executed when | Description |
| --- | --- | --- | --- |
| Data IO | [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-names) | The extension app establishes or refreshes a [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/). This can be triggered by:   - Running a [connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) from the Developer Console Testing module - Creating or refreshing a connection in the App Center. See [Manage Docusign App Connections](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=xyw1716318604389.html)﻿ for details. | Gets the names of the objects that are used by your system of record. |
| Data IO | [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) | The extension app establishes or refreshes a connection. This action is executed directly after **Get Type Names**. | Gets a set of object definitions from your system of record and returns their equivalents in the [Concerto](https://concerto.accordproject.org/docs/intro/) data model format.  Docusign uses the Concerto data model to map the data from your system of record. If your system of record does not already use the Concerto data model, you must implement transform logic that defines how your records map to Concerto data types before they can be read. This transform logic should be implemented within your **Get Type Definitions** action, and is called whenever the action is executed. See [Data model](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/) for details on the structure. |
| Data IO | [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records) | A running workflow instance reaches a **Read from** step. | Sends the external system a query to retrieve the ID of the record to which the envelope file or files should be written. |
| File output system of record | [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) | A running workflow instance reaches a **File Output** step. | Writes a completed agreement file or files to the system of record.  To enable the external system to identify the destination for the files, the request includes:   - The record ID returned from the **Search Records** request - The object associated with that record ID |

These sections explain the flow for action execution:

- [Get Type Names and Get Type Definitions flow](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/#get-type-names-and-get-type-definitions-flow)
- [Search Records and Write File flow](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/#search-records-and-write-file-flow)

### Get Type Names and Get Type Definitions flow

When your extension app is [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to a Docusign account, or when a connection is [refreshed](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=qkv1716320270335.html) in the Docusign App Center, the extension app will automatically get the types and type definitions of the objects that your system of record is configured to expose:

1. Docusign calls [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-names) to get the set of objects that your system of record exposes.
2. Docusign calls [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions), inputting the objects returned by **Get Type Names**. This returns the definitions of each object that your system of record exposes for Docusign.

After Docusign has retrieved the object definitions, it displays them on the workflow **Read from** step configuration panel. This enables workflow process builders to set up parameters that will be used at workflow instance run time to identify the object and record that envelope files are written to.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='3140' width='2365' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Get Type Names and Definitions flow](https://images.ctfassets.net/aj9z008chlq0/548dlFNttiTPtlRDq2Ee9o/38f7ff7586d272d4001e5fcccb567977/GetTypeNamesDefinitionsFlow.png?w=2365&h=3140&q=50&fm=png)

### Search Records and Write File flow

This action flow is executed as a customer completes the steps in a running workflow instance.

1. Docusign calls [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records) to get the ID of a record in the external data source to which envelope files are to be written.
2. Docusign calls [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) to write the file to the record identified in the response to the **Search Records** request.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='3427' width='2367' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Search Records Write File flow](https://images.ctfassets.net/aj9z008chlq0/6yygEQ3g3zmg7qCv1WUg5r/e7139d2ac5f9a23e8c9a522c2c43e119/SearchRecordsWriteFileFlow.png?w=2367&h=3427&q=50&fm=png)

## Next steps

- Review options to consider when you [plan a file output to system of record implementation](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/plan-implementation/).
- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- See [File output system of record extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/) for details about the action and capability requests and responses.

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
