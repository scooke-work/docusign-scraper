---
title: Troubleshooting manifest errors
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/troubleshooting-manifest-errors/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- App Manifest Reference
- App Manifest Reference
- Troubleshooting Manifest Errors
scraped_at: '2026-06-18T19:51:51Z'
---

# Troubleshooting manifest errors

This section describes common errors when validating a manifest for your extension app. 

If you encounter other errors, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance.

| **Error message** | **Fix** |
| --- | --- |
| App name must be unique within a Publisher | Each extension app needs a unique name. Change the `name` property or (if appropriate) delete the existing app with the same name. |
| Authorization URL cannot be a Docusign endpoint | The `customConfig.authorizationUrl` cannot include "docusign" in its domain. For example, `www.docusign.example.com` is not allowed, but `www.example.com/docusign` is allowed. |
| Authorization URL must contain an allowed TLD: com, net, org, app | The `customConfig.authorizationUrl` must be one of the following domain types:  - .com - .net - .org - .app |
| Cannot remove publication regions | When you update a published extension app's manifest to a new draft version, you cannot remove values from the `publicationRegions` array. Removing regions from a published extension app is not recommended and not supported in the Developer Console. If absolutely necessary, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. Requests will be handled on a case-by-case basis. |
| Capability name must be unique within the extension | Check the `extensions.capabilities` array and remove any duplicate values. |
| Connections must contain no more than 1 element | Your app cannot have more than one connection. To call multiple API platforms, you need to create multiple extension apps. |
| Expected one of: ['capability1', 'capability2'] | Check the `extensions.capabilities` array and make sure that all elements reference capabilities defined in the `actions` object and that they are supported for the extension. See the [extension contract](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) for details about the supported capabilities for each extension. |
| Expected referenced action templates required by capability: [capability name] to match: [`actions.template` value] | Check the `extensions.capabilities` array and confirm that each capability name listed has a corresponding action defined in the `actions` object with the correct `actions.template` value, which is listed in the error message. See the [extension contract](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) for details about the required `actions.template` value for each capability. |
| Expected referenced action templates to match | Each extension (defined by the `template` property in the `extension` object) corresponds to a set of actions. This error indicates that one or more of the actions listed in the `actionReferences` object do not match the extension. You can access details about the supported actions for each extension from the [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) page. |
| File Input Cloud Storage only supports `client_credentials` `grantType` | For a file input cloud storage extension app, set the `connections.params.grantType` property to `client_credentials`. In the current release, the default grant type of `authorization_code` is not supported with file input from cloud storage. |
| For app versions greater than 1.0, this property cannot be modified | Once your extension app is live, you cannot modify the value of the `distribution` property from `PUBLIC` to `PRIVATE` or vice versa. You can only modify this value for apps before they are published. |
| Invalid action `contractType` | The [Get File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file) action definition for a file input cloud storage extension must include a `contractType` property set to `action-with-callback`. `contractType` can be omitted from the action definition for all other actions. |
| Invalid action name | Check the [actions.name](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) values for any file IO actions and make sure that the required action names are used. The names are listed in the [extension contract](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/). |
| Invalid publication regions: [list of invalid values] | Remove invalid values from the `publicationRegions` array. See the `publicationRegions` description in the [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for a list of supported regions. After you've published your extension app, production App Center users will be able to use your app only if their Docusign account is based in a supported region. |
| Missing capability defined by action: ''[`actions.template`]" | Make sure that all capabilities defined in the `actions` object are referenced in the `extensions.capabilities` array. |
| Must refer to a defined action | Correct any values in the `extensions.actionReferences` list that do not match an `actions.name` value defined in the `actions` property. |
| Must refer to a defined connection | The `actions.connectionsReference` property value must match the `connections.name` value. |
| `publicationRegions` should not be empty | The `publicationRegions` property must be set to an array consisting of at least one element. See the `publicationRegions` description in the [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for a list of supported regions. You can also omit this property, and the default value of `US` will be applied. |
| template must match ${TEMPLATE\_REGEX} regular expression | For both extensions and actions, the `template` property must match values predefined by Docusign. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) and [Extension schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) for the specific values. |

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
