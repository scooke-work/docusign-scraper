---
title: Action schema
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- App Manifest Reference
- App Manifest Reference
- Action
scraped_at: '2026-06-18T19:51:51Z'
---

# Action schema

The `action` object describes a call to an external service.

An `action` object may define a required call for an extension or an optional call. Optional calls are known as [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/).

Each action must conform to a contract defined by Docusign. This contract is specified by the `template` property.

| **Property** | **Type** | **Required?** | **Description** |
| --- | --- | --- | --- |
| `name` | `String` | Yes | The name of the action or capability.  For file IO extensions, valid values are:  - `get-file` - `get-files` - `get-type-names` - `list-directory-contents` - `list-drives` - `list-headers` - `export-to-destination` - `search` - `write-file`  For other extensions, any value can be used. Note that the `get-file` value is only used for actions that have Agreement Manager as the extension point. |
| `description` | `String` | Yes | The description of the action. |
| `template` | `String` | Yes | Defines the contract of the action. This determines the shape of the request that Docusign will send to the external platform called by this action.   Valid values:  - `ConnectedFields.Version1.Verify` - `DataIO.Version6.CreateRecord` - `DataIO.Version6.GetTypeDefinitions` - `DataIO.Version6.GetTypeNames` - `DataIO.Version6.PatchRecord` - `DataIO.Version6.SearchRecords` - `FileIO.Version1.GetFile` - `FileIO.Version1.GetFiles` - `FileIO.Version1.ListDirectoryContents` - `FileIO.Version1.ListDrives` - `FileIO.Version1.Search` - `FileIO.Version1.WriteFile` - `FileIO.Version1.ListHeaders` - `FileIO.Version1.ExportToDestination` - `Suggest.Version1.PostalAddress` - `Typeahead.Version1.PostalAddress` - `Verify.Version1.BankAccountOwner` - `Verify.Version3.BankAccount` - `Verify.Version1.BusinessEntity` - `Verify.Version1.Email` - `Verify.Version1.PhoneNumber` - `Verify.Version1.PostalAddress` - `Verify.Version2.SocialSecurityNumber` |
| `contractType` | `String` | Depends on the action | Valid values:   - `action`: The default value. The external system does not send a callback request to Docusign after performing an asynchronous operation. - `action-with-callback`: The external system sends Docusign a callback request to report the outcome of an asynchronous operation.   **Note:** The only action that currently supports this property is the file input cloud storage extension's [Get File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file) action. This property is required for the **Get File** action, and it must be set to `action-with-callback`. |
| `connectionsReference` | `String` | Yes | The name of the connection defined in your manifest. |
| `params` | `Object` | Yes | An object containing the data required to call the external platform. |
| `params.uri` | `String` | Yes | The URI of the external platform called by the action. |

An `action` object looks like this.

```
{
  "name": "Verify Action",
  "description": "Sends envelope values for verification by an external service",
  "template": "ConnectedFields.Version1.Verify",
  "connectionsReference": "authentication",
  "params": {
    "uri": "https://fontara.com/api/connectedfields/verify"
}
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
