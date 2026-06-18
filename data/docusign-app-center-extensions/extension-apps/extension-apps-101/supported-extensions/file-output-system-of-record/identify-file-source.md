---
title: Identify the file source (beta)
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-file-source/
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
- Identify File Source
scraped_at: '2026-06-18T19:51:51Z'
---

# Identify the file source (beta)

The file output system of record extension supports two sources for files to export: a **Send Documents for Signature** workflow step, or any envelope sent from the account that meets certain conditions. See the next sections for details.

## Send Documents for Signature workflow step

During workflow configuration, a process builder can select a [Send Documents for Signature step](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uww1698167288211.html) as the source for files that will be exported in a **File Output** step. The **Send Documents for Signature** step setup defines the content and delivery method for [eSignature envelopes](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=ghu1578456429097.html).

During workflow instance execution, the **Send Documents for Signature** step generates an envelope, which the customer completes and signs. The **File Output** step exports the envelope's documents to the system of record.

Use this option if the file export requirements are specific to the [eSignature template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=dqj1578456412286.html&rsc_301) and agreement process defined in the workflow. This option supports exporting all the files associated with an envelope as a single PDF. For a choice of export formats, or if the export requirements apply more broadly to envelopes sent from the account instead of from a specific workflow, the option described in the next section may be a better choice.

See [File output system of record test: Workflow step creates envelopes](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-system-of-record-workflow-step-creates-envelopes/) for details about workflow setup.

## Envelopes sent from the account

During workflow configuration, a process builder can set the workflow [start method](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=ztb1727892686033.html) to **From an Event**. This start method triggers a workflow instance for any envelope sent from the account if the envelope meets certain conditions. For example, the process builder can specify that workflow instances start on completion of envelopes created from a specific template. When this option is used, the process builder also configures the **File Output** step to use the instance-triggering envelopes as the source of files to write to the system of record.

At runtime, an envelope event that meets the workflow start requirements triggers the execution of a workflow instance. The **File Output** step exports the envelope's documents to the system of record.

Use this option if file export is broadly applicable to envelopes being sent from the account, possibly via multiple mechanisms (for example, envelopes sent manually from the eSignature web application and envelopes sent programmatically via an eSignature API integration). In addition, this option supports exporting envelope files individually, as a ZIP file containing the individual envelope files, or as a single PDF that includes the contents of all the files. The process builder can select one of these options during **File Output** step configuration.

See [File output system of record test: An event triggers the workflow](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-system-of-record-event-triggers-workflow/) for details about workflow setup.

## Next steps

- Learn more about [setting up workflows](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/workflow-configuration/) that include file output to system of record.
- See how the file output system of record [extensions and actions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/extensions-and-actions/) function during workflow configuration and execution.
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
