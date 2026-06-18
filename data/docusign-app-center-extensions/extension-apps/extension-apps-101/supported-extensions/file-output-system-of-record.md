---
title: File output system of record extension overview (beta)
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- File Output System Of Record
scraped_at: '2026-06-18T19:51:51Z'
---

# File output system of record extension overview (beta)

The file output system of record extension exports documents to a system of record in real time as customers complete them. For example, the extension can be invoked from a [workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html) that sets up electronic funds transfer (EFT) for investment accounts. After customers sign EFT authorization forms, the extension sends a request to the system of record to write the files to the specified object and record.

Docusign offers extension apps that integrate with HubSpot, Microsoft Dynamics 365, and Salesforce. If you want to store files to these services, visit the [Docusign App Center](https://apps.docusign.com/app-center) for details.

## Workflow step that exports files

After a file output to system of record extension app has been [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to a Docusign account, workflows in the account can write files to a system of record. To use this feature, a workflow must include a **File Output** step that invokes the extension.

**File Output** and other workflow steps have two phases of operation:

1. **Workflow configuration:** A workflow process builder in your or your customer's organization creates a workflow. During this one-time setup, the process builder adds workflow steps and defines properties that determine each step's runtime behavior. For example, when a process builder defines a **File Output** step, they select the file source, the destination object, a value that identifies the record to write the file to, and a file naming convention.
2. **Workflow instance execution:** A workflow instance is a runtime execution of a workflow's steps for a specific customer. Each instance includes customer-specific workflow variable values that can be used in the steps. For example, when workflow instance execution reaches a **File Output** step, a customer's account number can be sent as a record identifier in the request to write the file to the system of record. The request also includes the object that the process builder selected during workflow configuration.

Additional workflow steps or configuration may be required along with the **File Output** step. This depends on how your implementation identifies the destination record for the write operation and how the workflow obtains files to write. These topics explain the options:

- [Identify destination records](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/)
- [Identify the file source](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-file-source/)

The next section provides an example of how the file output system of record extension functions during workflow configuration and instance execution.

## Use a file output system of record extension in a workflow

In the example described here, a process builder defines a workflow that enables a customer to authorize EFT for a financial account.

Expand the sections below to see how a file output system of record extension functions during workflow configuration and execution. See [Extensions and actions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/) for details about the functionality.

## Next steps

- Review the options for [identifying a destination record](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/) to which a file will be written.
- See the choices available to select as the [file source](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-file-source/).
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
