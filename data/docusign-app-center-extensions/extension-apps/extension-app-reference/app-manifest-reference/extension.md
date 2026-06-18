---
title: Extension schema
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- App Manifest Reference
- App Manifest Reference
- Extension
scraped_at: '2026-06-18T19:51:51Z'
---

# Extension schema

The `extension` object defines the basic data of your app. It includes the extension (defined by the `template` property) and references to the `action` objects for that extension. The `action` references are included as follows:

- Required actions and optional actions, known as [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/), must be included in the `actionReferences` array.
- Capabilities must also be included in the `capabilities` array.

| **Property** | **Type** | **Required?** | **Description** |
| --- | --- | --- | --- |
| `name` | `String` | Yes | The name of the extension. For file output cloud storage and file output system of record extensions, the name will appear on the Workflow Builder workflow step selection and step configuration screens. |
| `description` | `String` | Yes | The description of the extension.  For a file IO extension or a data IO extension, the description will appear on the Workflow Builder workflow step selection screen. |
| `template` | `String` | Yes | Defines the contract of your extension. Valid values:  - `ConnectedFields.Version1.ConnectedFields` - `DataIO.Version6.DataInputOutput` - `FileIO.Version1.FileInputCloudStorage` - `FileIO.Version1.FileOutputCloudStorage` - `FileIO.Version1.FileOutputSystemOfRecord` - `FileIO.Version1.FileOutputTabularFormat` - `Verify.Version1.BankAccountOwner` - `Verify.Version3.BankAccount` - `Verify.Version1.BusinessEntity` - `Verify.Version1.Email` - `Verify.Version1.PhoneNumber` - `Verify.Version1.PostalAddress` - `Verify.Version2.SocialSecurityNumber` - `FileIO.Version1.FileOutputTabularFormat` - `FileIO.Version1.FileInputSystemOfRecord` |
| `capabilities` | `String[]` | No | A list of capabilities that are implemented for the extension. Capabilities are defined in `action` objects and represent optional functionality for an extension. See the [extension contract](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) for details about how to reference a capability in this array.  For extensions that have no capabilities, or if you choose not to implement any capabilities for the extension, omit this property from the manifest. |
| `actionReferences` | `String[]` | Yes | A list of actions and capabilities that will be implemented for the extension.   The names in the `actionReferences` object must match the names of actions defined in the `actions` object of your extension app manifest.  This array cannot be empty. |

An `extension` object looks like this.

```
"extensions": [
  {
    "name": "My File Output Cloud Storage Extension",
    "description": "Writes files to cloud storage",
    "template": "FileIO.Version1.FileOutputCloudStorage",
    "actionReferences": [
      "list-directory-contents",
      "list-drives",
      "write-file"
    ],
    "capabilities": [
      "FileIO.Version1.ListDirectoryContents",
      "FileIO.Version1.ListDrives"
    ]
  }
]
```

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
