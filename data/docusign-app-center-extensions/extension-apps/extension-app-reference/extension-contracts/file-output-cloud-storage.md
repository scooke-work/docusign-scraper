---
title: File output cloud storage extension contract reference
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- Extension Contracts
- Extension Contracts
- File Output Cloud Storage
scraped_at: '2026-06-18T19:51:52Z'
---

# File output cloud storage extension contract reference

The file output cloud storage extension writes documents generated from a Workflow Builder workflow [Send Documents for Signature step](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uww1698167288211.html) to a cloud storage platform.

You can include this extension when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). If you register the extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), select the **File Output Cloud Storage** extension in the form-based UI, as shown in this figure:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='293' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Selecting the file output cloud storage extension when registering an extension app](https://images.ctfassets.net/aj9z008chlq0/6zf7koYzyjAgIGyTTqjwXv/0d2bc6265873757d84716ca7f919e0fb/DevConsoleFormBasedExtensionSelection.png?w=600&h=293&q=50&fm=png)

During the form-based extension app registration process, if you select a [file IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), its required actions are automatically added to the app. You can then configure the actions' endpoint URIs and other properties on the [Integration Details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/) page. The extension's optional capabilities can be added or removed only by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). After you've added capabilities via the manifest file, you can edit them on the Integration Details page. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action and capability properties in the app manifest file.

If you register the extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), set the `extensions.template` value in your app manifest to `FileIO.Version1.FileOutputCloudStorage`.

This extension has one required action and two optional capabilities. Below is a list of their identifiers as they appear in the form-based app registration UI and the app manifest. See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for file output to cloud storage.

| Form-based UI name | App manifest actions.template value | App manifest actions.name value | App manifest extensions.capabilities value | Required |
| --- | --- | --- | --- | --- |
| Write File | `FileIO.Version1.WriteFile` | `write-file` | N/A | Yes |
| List Directory Contents | `FileIO.Version1.ListDirectoryContents` | `list-directory-contents` | `FileIO.Version1.ListDirectoryContents` | No |
| List Drives | `FileIO.Version1.ListDrives` | `list-drives` | `FileIO.Version1.ListDrives` | No |

Both the action and the capabilities are defined in the app manifest fileʼs `actions` object. This definition includes a `template` value, a `name`, and the endpoint URL. The action and capabilities must also be referenced from the `extensions` object as follows:

- For both the action and capabilities, include the `actions.name` value from the `actions` object in the `extensions.actionReferences` array.
- Include a reference to each capability in the `extensions.capabilities` array. Use the value from the **App manifest extensions.capabilities value** column in the table above.

For example, the manifest file action definitions for the **Write File** action and the **List Drives** capability look like this:

```
"actions": [
  {
    "name": "write-file",
    "description": "Writes a file to a cloud storage system",
    "template": "FileIO.Version1.WriteFile",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/writefile"
    }
  },
  {
    "name": "list-drives",
    "description": "Retrieves a list of drives on a cloud storage system",
    "template": "FileIO.Version1.ListDrives",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/listdrives"
    }
]
```

The `extensions` object includes the `actions.name` values for both the **Write File** action and the **List Drives** capability in the `actionReferences` array. In addition, the **List Drives** capability is included in the `capabilities` array:

```
"extensions": [
  {
    "name": "My File Output Cloud Storage Extension",
    "description": "Writes files to a cloud storage system",
    "template": "FileIO.Version1.FileOutputCloudStorage",
    "capabilities": ["FileIO.Version1.ListDrives"],
    "actionReferences": [
      "write-file",
      "list-drives"
    ]
  }
]
```

For details about what the actions and capabilities do when invoked, see [File output cloud storage actions and capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/#file-output-cloud-storage-actions-and-capabilities).

When registering an extension app, you cannot include both a [file output system of record extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/) and a [file output cloud storage extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/) in the same app. If you need to use both types of output in workflows, register a separate app for each extension.

## Action contracts

## Error handling

The external system should return a 200 response code to Docusign if a request succeeded. Any other response code indicates that the request was not successfully executed.

This applies to all actions and capabilities. Developers are responsible for providing a code and message for each error.

## Next steps

- Get an [overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/) of the file output cloud storage extension and how it can be used.
- Explore the options for [testing](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) a file output cloud storage extension.
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
