---
title: Identify destination records (beta)
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/
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
- Identify Destination Records
scraped_at: '2026-06-18T19:51:51Z'
---

# Identify destination records (beta)

The file output system of record extension supports two options for identifying the record that a file will be written to: a workflow variable value or a record ID returned from a **Read from** workflow step. See the next sections for details.

## Use a workflow variable value

During workflow [File Output step](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/#workflow-step-that-exports-files) configuration, the process builder can select a workflow variable to use as the record identifier. The variable can represent a value that:

- Is passed to the workflow from an API integration that triggered the workflow
- Identifies the customer, such as their name or email address
- The customer enters during a previous workflow step, such as a [Send Documents for Signature step](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uww1698167288211.html)

The process builder also selects the object in the system of record that the file will be written to.

At runtime, when a workflow instance reaches the **File Output** step, Docusign sends a [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) request to the external system. The request includes the object the process builder selected and the variable value as the record identifier.

For additional details about configuration and runtime execution, see [Extensions and actions: Record identifier is a workflow variable](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/#extensions-and-actions-record-identifier-is-a-workflow-variable).

This option for selecting a record identifier is easier for workflow process builders to configure. However, it requires that the external system use a single workflow variable value, along with an object name, to uniquely identify a record to write files to. If this is not feasible, you can instead identify a record using a **Read from** workflow step, as described in the next section.

## Use an ID returned by a Read from workflow step

During workflow configuration, a process builder can include a **Read from** step that defines a search query to the external system. The query identifies the record to write a file to and returns the record ID. When the process builder configures the **File Output** step, they select the ID returned by the **Read from** step as the record identifier. 

At workflow instance runtime, the **Read from** step execution sends a query to the external system, which returns the ID of the record to write the file to. Docusign includes this ID in the request it sends to the external system when the **File Output** step is executed.

For additional details about configuration and runtime execution, see [Extensions and actions: Record ID is from a Data read step](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/#extensions-and-actions-record-id-is-from-a-data-read-step).

Use this option if you need more than a single workflow variable value to identify the record to write a file to. For example, if a customer name, email address, and account number are all required to uniquely identify a destination record, a process builder can configure a **Read from** step that launches a query that uses all three values. You may also prefer this option if other steps in a workflow, such as a [Collect Data with Web Forms step](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=gua1698120920620.html), require values to be retrieved from the record in the external data source. In this case, you can configure the **Read from** step so that it returns multiple values from the data source record, in addition to the ID of the record that the files are to be written to.

## Impact on implementation

The choice of how to identify records to write to determines which [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/) and [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) your app must implement, so it should be made early in your development planning process. The required extensions and actions for each option are listed below.

| Record identifier | Required extension(s) | Required actions | Notes |
| --- | --- | --- | --- |
| A workflow variable value | [File output system of record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/) | File output:   - [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#get-type-names) capability - [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) action | The inclusion of the **Get Type Names** capability causes the **File Output** step configuration panel to display a dropdown for selecting the external system object. |
| A record ID returned by a **Read from** step | [Data IO](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/) and [File output system of record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/) | Data IO:   - [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-names) action - [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) action - [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records) action   File output:   - [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) action | The inclusion of the data IO extension makes the **Read from** step available in the workflow. |

For additional information, see:

- [Workflow configuration for file output scenarios](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/workflow-configuration/) for details about workflow setup.
- [Extensions and actions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/) to learn about the required extension app components.

## Next steps

- See the choices available to select as the [file source](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-file-source/).
- Learn more about [setting up workflows](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/workflow-configuration/) that include file output to system of record.
- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).

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
