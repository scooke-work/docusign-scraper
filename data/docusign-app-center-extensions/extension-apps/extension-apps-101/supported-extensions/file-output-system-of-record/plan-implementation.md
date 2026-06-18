---
title: Plan an implementation (beta)
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/plan-implementation/
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
- Plan Implementation
scraped_at: '2026-06-18T19:51:52Z'
---

# Plan an implementation (beta)

These sections describe options that should be considered when planning a file output to system of record implementation:

- [External system logic to process Write File requests](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/plan-implementation/#external-system-logic-to-process-write-file-requests)
- [Mechanisms for starting workflow instances](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/plan-implementation/#mechanisms-for-starting-workflow-instances)
- [File output system of record restrictions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/plan-implementation/#file-output-system-of-record-restrictions)

## External system logic to process Write File requests

Docusign sends [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) requests during workflow instance execution to write one or more files to the system of record. The format of the request can vary depending on how a process builder has configured the workflow. See [Workflow configuration for file output scenarios](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/workflow-configuration/) for more information.

The simplest scenario for a **Write File** request is one that includes a single file and specifies:

- The file contents as a Base64 string in `contents`
- The data source object name in `rootId`
- A value that the external system uses to identify the destination record in `parentID`
- A file name in `basename`

For example:

```
{
  "files": [
    {
      "basename": "EFTAuthorization.pdf",
      "path": "",
      "pathTemplateValues": [
      ],
      "parentId": "1227",
      "contents": "JVBERi...VFT0YK"
    }
  ],
  "rootId": "FinancialAccount"
}
```

**Note:** The request does not identify the data source property to which files should be written, so the external system logic must handle this.

For details about the **Write File** request and response formats, see the [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file) action contract. See [Use an API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) for guidance about transforming requests and responses to the required format.

Depending on how the workflow has been configured, the **Write File** request may have one or more variations in its values. These scenarios are described in the next sections.

### Options for record identifier

Depending on how a process builder configures a **File Output** step, the value that a **Write File** request includes in the `parentId` can be any of the following:

- A workflow variable value derived from the workflow start method or a previous workflow step
- A data source record ID returned by a **Read from** step in the workflow
- Another type of data source record value returned by a **Read from** step

The external system logic to identify a record to write to should handle these possibilities. See [Identify destination records](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/) for more information.

### Request includes multiple files

If a workflow is configured to start from an event, the **File Output** step configuration panel gives process builders the option to store envelope files individually. This can result in a **Write File** request that includes multiple files, and the external system logic should handle this. If the data source does not support writing multiple files to the same record, process builders should not select the option to store files individually. See [Envelopes sent from the account](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-file-source/#envelopes-sent-from-the-account) for more information.

### File names contain variables

File names in **Write File** requests can include variables whose values are populated during workflow instance execution. The external system must implement logic to construct the file names from the variable values in requests. See [File names that include workflow variables](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#file-names-that-include-workflow-variables) for more information.

## Mechanisms for starting workflow instances

Docusign supports multiple options for starting workflow instances that write files to a system of record. To review the options for starting workflow instances manually, see [How to Start a Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html).

To start workflow instances programmatically, you can implement a Docusign Workflow Builder API integration that includes the [Workflows: triggerWorkflow](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/triggerworkflow/) request. See [Workflow Builder API 101 overview](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/) for an introduction to the API, and see [How to trigger a Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/) for example code and a detailed walkthrough.

## File output system of record restrictions

These restrictions apply when implementing file output to a system of record:

- When you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/), you cannot include both a file output system of record extension and a [file output cloud storage extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/) in the same app. If you need to use both types of output in workflows, register a separate app for each extension.
- The maximum supported total size for the files in a **Write File** request is 25 MB.
- If files from multiple envelopes are to be written to the system of record, the workflow process builder must define a separate file output step for each envelope.

## Next steps

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
