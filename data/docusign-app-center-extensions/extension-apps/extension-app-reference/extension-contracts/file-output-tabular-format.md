---
title: File output tabular format extension contract reference
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- Extension Contracts
- Extension Contracts
- File Output Tabular Format
scraped_at: '2026-06-18T19:51:52Z'
---

# File output tabular format extension contract reference

The file output tabular format extension exports data from a Workflow Builder workflow to an existing tabular format file stored in a cloud provider like Google Drive or Sharepoint.

You can include this extension when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). If you register the extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), select the **File Output Tabular Format** extension in the form-based UI, as shown in this figure:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='371' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Selecting the file output tabular format when registering an extension app](https://images.ctfassets.net/aj9z008chlq0/6WQfuNFJd0FKzkPobUqaCW/1470927d5951e30376e91b94a48e2f57/fileIOTabularFormat.png?w=600&h=371&q=50&fm=png)

In the current release, users can export data only to an existing spreadsheet. Creating a new spreadsheet from within the extension is not yet supported.

If you register the extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/)[,](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/) set the `extensions.template` value in your app manifest to `FileIO.Version1.FileOutputTabularFormat`.

This extension has two required actions and two optional capabilities. Below is a list of their identifiers as they appear in the form-based app registration UI and the app manifest. See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for file output to tabular format.

| Form-based UI name | App manifest actions.template value | App manifest actions.name value | App manifest extensions.capabilities value | Required |
| --- | --- | --- | --- | --- |
| Export To Destination | `FileIO.Version1.ExportToDestination` | `export-to-destination` | N/A | Yes |
| List Headers | `FileIO.Version1.ListHeaders` | `list-headers` | N/A | Yes |
| List Directory Contents | `FileIO.Version1.ListDirectoryContents` | `list-directory-contents` | `FileIO.Version1.ListDirectoryContents` | No |
| List Drives | `FileIO.Version1.ListDrives` | `list-drives` | `FileIO.Version1.ListDrives` | No |

During the form-based extension app registration process, if you select a [file IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), its required actions are automatically added to the app. You can then configure the actions' endpoint URIs and other properties on the [Integration Details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/) page. The extension's optional capabilities can be added or removed only by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). After you've added capabilities via the manifest file, you can edit them on the Integration Details page. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action and capability properties in the app manifest file.

## Action contracts

## Error handling

The external system should return a 200 response code to Docusign if a request succeeded. Any other response code indicates that the request was not successfully executed.

This applies to all actions and capabilities. Developers are responsible for providing a code and message for each error.

## Next steps

- Get an [overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-tabular-format/) of the file output tabular format extension and how it can be used.
- Explore different options for [testing](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) your extension.
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
