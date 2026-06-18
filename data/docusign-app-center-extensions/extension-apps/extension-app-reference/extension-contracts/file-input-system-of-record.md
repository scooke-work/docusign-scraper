---
title: File input system of record extension contract reference (beta)
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-system-of-record/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- Extension Contracts
- Extension Contracts
- File Input System Of Record
scraped_at: '2026-06-18T19:51:52Z'
---

# File input system of record extension contract reference (beta)

This extension can be invoked from a step in a [Maestro workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html) to retrieve files from a system of record. The files to import can be identified using workflow data, such as values captured earlier in the workflow or returned from other extension steps. See [File input system of record extension overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-system-of-record/) for details about how the extension is invoked in Workflow Builder and other behaviors and restrictions.

The file input system of record extension defines a structured interface between Docusign and the external service provider:

- Docusign initiates a request for files using context data populated by the workflow users.
- The external system identifies the relevant records and returns the corresponding file metadata.
- Docusign retrieves each document through a secure, managed pipeline for ingestion.

You can include this extension when you register an extension app. If you register the extension app using a form, select the **File Input System of Record** extension in the form-based UI, as shown in this figure:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='414' width='763' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![form based UI extension selecton](https://images.ctfassets.net/aj9z008chlq0/6G5kIrkbGSfR2bZteb3yjr/44f5927520bcbc877afb2acd624544fa/form.png?w=763&h=414&q=50&fm=png)

During the form-based extension app registration process, if you select a [file IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), its required actions are automatically added to the app. You can then configure the actions' endpoint URIs and other properties on the [Integration Details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/) page. The extension's optional capabilities can be added or removed only by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). After you've added capabilities via the manifest file, you can edit them on the Integration Details page. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action and capability properties in the app manifest file.

If you register the extension app using an app manifest file, make sure that you:

- Set the `extensions.template` value in your app manifest to `FileIO.Version1.GetFiles`.
- Include a definition for the required action in the `actions` object, using these values:
  - `name: get-files`
  - `template: FileIO.Version1.GetFiles`
- Include the value from the `actions.name` property in the `extensions.actionReferences` array.

See [Update extension and action settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings) for information about defining actions using the form-based registration process. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action properties in the app manifest file.

When registering an extension app, you cannot include both a [file output system of record extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/) and a [file output cloud storage extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/) in the same app. If you need to use both types of output in workflows, register a separate app for each extension.

## Action contracts

## Error handling

The external system should return a 200 response code to Docusign if a request succeeded. Any other response code indicates that the request was not successfully executed. Developers are responsible for providing an error code and message for each error.

## Next steps

- Get an [overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-system-of-record/) of the file input system of record extension and how to use it.
- Explore how to [Use extensions in workflows](https://developers.docusign.com/extension-apps/workflows/).
- Find out about other [supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/).

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
