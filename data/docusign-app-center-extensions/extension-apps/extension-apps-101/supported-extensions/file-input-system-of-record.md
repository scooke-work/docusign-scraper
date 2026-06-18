---
title: File input system of record extension overview (beta)
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-system-of-record/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- File Input System Of Record
scraped_at: '2026-06-18T19:51:49Z'
---

# File input system of record extension overview (beta)

The file input system of record [extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) imports documents from an external system of record into a [Maestro workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html). Instead of requiring users to manually search for documents that they need to include in an envelope, this extension enables workflows to dynamically retrieve files such as contracts, supporting documents, or templates from external systems like CRMs, document management systems, or internal databases. The workflow defines which files are needed, and the external system determines how to locate them. This separation allows workflows to remain flexible while delegating retrieval logic to the system of record.

For example, the extension can be invoked from a workflow that processes loan applications. When an applicant completes their application package, the workflow is triggered; the extension sends a request to the system of record to locate all of the applicant’s supporting documents, apply any required business logic (such as selecting the current versions), and return the documents to Docusign. The workflow then continues using those files in a **Send Documents for Signature** step.

## Use a file input system of record extension in a workflow

After a file input system of record extension app has been [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to a Docusign account, you can invoke it as a step in your workflows. In the example described here, a process builder defines a workflow that adds an applicant's supporting documents to an eSignature envelope. The workflow steps include:

- An applicant confirms that they have completed a loan application in a web form and submits it.
- The extension imports the applicant’s supporting documents into an eSignature [envelope](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=gso1578456465211.html&_gl=1*1u0i9kq*_gcl_au*MTA1Mzc0MjYzOS4xNzcwMjM4NDE5LjIxMTU4NTUwNDIuMTc3MTg2OTk1Ny4xNzcxODY5OTcw).
- The loan officer receives the eSignature envelope containing all the client’s supporting documents and the loan application in a single package for review.

Expand the sections below to see how a file input system of record extension functions during workflow [configuration](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=tco1697826811758.html) and [execution](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=zbf1698707257742.html) .

## Get Files action

A file input system of record extension app implements the **Get Files** action, which is executed when a Workflow Builder workflow reaches a file input system of record step. At this point, Docusign sends a request to the external system to retrieve documents from the system of record.

The external system locates the relevant files based on criteria set by the user or process builder, and returns them to Docusign. The retrieved files are then made available for use in downstream workflow steps, such as a **Prepare eSignature template** step or a **Send Documents for Signature** step.

In the extension app manifest, this action is identified as `FileIO.Version1.GetFiles`.

## Restrictions

These restrictions apply when implementing the file input system of record extension:

- When you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/), you cannot include both a file input system of record extension and a [file input cloud storage extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/) in the same app. If you need to use both input types in workflows, register a separate app for each extension.
- The maximum supported file size for import from a system of record is 10 MB or 100 MB per request. The workflow process builder must ensure that the documents imported from the system of record are within this limit.

## Mechanisms for starting workflow instances

Docusign supports multiple options for starting workflow instances that import files from a system of record. A workflow instance is a runtime execution of workflow steps that enables a customer to complete tasks such as filling out a form and signing an agreement.

To review the options for manually starting workflow instances, see [How to Start a Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html).

To start workflow instances programmatically, you can implement a Docusign Workflow Builder API integration that includes the [Workflows: triggerWorkflow](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/triggerworkflow/) request. See [Workflow Builder API 101 overview](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/) for an introduction to the API, and see [How to trigger a Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/) for example code and a detailed walkthrough.

## Next steps

- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- See [File input system of record extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-system-of-record/) for details about the action requests and responses.
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
