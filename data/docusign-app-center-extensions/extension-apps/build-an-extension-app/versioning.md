---
title: Extension app versioning
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Versioning
scraped_at: '2026-06-18T19:51:49Z'
---

# Extension app versioning

When you [publish a new extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/), the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) displays version 1.0.0 as the first published version. That version is public and available for customers to discover and install from the [Docusign App Center](https://apps-d.docusign.com/app-center). If you [update the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) for a published extension app, Docusign creates a new version. To publish the new version to the App Center, you must first [submit it for review](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/#step-3-submit-your-extension-app-for-review-on-the-developer-console), and you can publish it after it's approved.

Extension app versioning works the same for both public extension apps and private extension apps.

## Major, minor, and patch versions

In the current release, only patch version updates are supported. Updates to a live extension app that result in a major or minor version change will not be allowed. Major and minor version updates will be supported in a future release.

Any extension app registration change that could cause authorization or API requests to fail is considered a major version update. For a major version update, the first part of the version string is updated. For example, if an extension app is currently at version 1.0.0, 1.1.0, or 1.2.0, a major update would cause the version to be incremented to 2.0.0.

When you introduce a new non-breaking feature to your extension app, the Developer Console increments the second part of the version string. For example, version 1.1.0 is a minor update for version 1.0.0.

Changes that are confined to extension app display information and metadata qualify for a patch version update. When you introduce a patch change to your app registration, the Developer Console increments the third part of the version string. For example, version 1.0.1 is a patch update for version 1.0.0.

### What qualifies as a patch version

When you submit an updated extension app registration for Docusign review, Docusign compares it to your published version. If the updated registration has no changes or the changes are limited to these properties, Docusign considers it a patch version update. You can update these properties [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-form/) or by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/).

| Form-based parameter | App manifest file property |
| --- | --- |
| App icon | `icon` |
| App name | `name` |
| Short description | `description.short` |
| Long description | `description.long` |
| Screenshots | `screenshots` |
| Terms of service URL | `termsOfServiceUrl` |
| Privacy policy URL | `privacyUrl` |
| Support URL | `supportUrl` |
| Signup URL | `signupUrl` |
| Published by | `publisher.name` |
| Support email | `publisher.email` |
| Support phone | `publisher.phone` |
| Publisher website | `publisher.website` |
| Changelog | `changelog` |
| Region | `publicationRegions` |
| Params URI | `params.uri` |

A change to [params.uri](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) qualifies as a patch version update only if there is no change to the API contract ([template](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) property) in the app manifest.

Changes to parameters not listed in the table will result in a major or minor version update. See [Update App Center listing](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/) or [Update extension and action settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings) for details about the form-based parameters in the list. See [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for details about the app manifest file properties in the list.

You can combine multiple changes in a single version. For example, you can change your extension app’s icon, name, and description, and all the changes can be included in a single patch version update.

### Version updates for back-end changes in API service

At times, you may need to make back-end changes to your API service code. These changes can include bug fixes, security patches, etc. You can make back-end changes without making app registration changes, and your extension app will remain at the same version in both the Developer Console and the App Center. However, when you make back-end changes, we recommend [updating the changelog](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-changelog) using a form or by editing the [changelog](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) in your app manifest. Then publish a new version to provide details about the changes in the App Center listing.

Back-end code changes may qualify as a patch version update, provided that the changes don't break the extension app. During the app review, Docusign will test the extension app using the credentials you provide to check for breaking changes.

## Extension app changelog

The changelog enables you to document updates to your extension app in a new version. When you [update the registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) for a published extension app, you must provide a value for the changelog. Include a description of changes or new features. When the new extension app version is published, customers will see this changelog in the App Center listing.

See [Update changelog](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-changelog) for details about the form-based update process. See [Use a manifest file to update a registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/) if you will edit the [changelog](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) property in the app manifest.

## Version updates in the Developer Console

In the Developer Console, the first version of any new extension app is automatically assigned version 1.0.0 when you [register it](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). When you [update a published extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/), Docusign automatically creates a new draft with an incremented version number. For example, when you save changes to an extension app whose published version is 1.0.0, Docusign creates a draft with version 1.0.1. If you subsequently make changes to that draft without submitting it for review, it remains at the same version. If an extension app fails Docusign review, you can update it to address the issues identified in the review, and it remains at the same version.

## How updates are applied on saving a new version

When you save a new version of a published extension app, the following occurs **in your account only**:

- In the Developer Console, the previous version is automatically uninstalled and replaced with the new version.
- The previous version's app listing is automatically replaced in the demo App Center.
- If the previous version was installed to your account in the demo App Center, it is automatically upgraded to the new version.

Saving a new version has no impact on:

- The app listing in the demo App Center for all other accounts
- The installed app version in the demo App Center for all other accounts
- The app listing and installed versions in the production App Center

See [Developer and production environments](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/#developer-and-production-environments) for details about the differences between the demo and production App Centers.

## How updates are applied on publishing a new patch version

To publish a new extension app version, you must submit it for Docusign review. After it has passed review and is approved, you can publish it to the App Center.

On publication of a new patch version:

- The new version number and updates to the metadata, such as the description, replace the previous version in the app listing that's visible to all accounts on the demo and production App Centers.
- The new version is available to install for all accounts on the demo and production App Centers.
- Any demo or production accounts that had the previous version installed are automatically upgraded to the new version. The upgrade is seamless for users and does not require any action on their part.
- The previous version is no longer available to install in the demo or production App Center.

## See a list of versions for an extension app

To see a list of all versions for an extension app:

1. Log in to the [Developer Console](https://devconsole.docusign.com).
2. On the **My Extension Apps** page, select an extension app.
3. In the left navigation, select **App Versions**.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='898' width='1727' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Extension Apps Versioning Page](https://images.ctfassets.net/aj9z008chlq0/6wYQF9cwvT0AIsg9n5cZQs/2bf96f3121d8e36b75e9431d282e94c6/ExtensionAppVersioningPage.png?w=1727&h=898&q=50&fm=png)

The page displays this information for each version:

|  |  |
| --- | --- |
| **Property** | **Description** |
| Status | See [Extension app status and distribution](https://developers.docusign.com/extension-apps/build-an-extension-app/status/) for a complete list of statuses and descriptions. |
| Type | Indicates whether the new version is a patch, minor, or major update to the extension app. See [Major, minor, and patch versions](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/#major-minor-and-patch-versions) for details. |
| Last Updated | The date when the extension app registration was last saved in the Developer Console. |
| Changelog | A description of the changes in the version as defined in the changelog. See [Update changelog](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-changelog) for details about providing this information via a form. See [Use a manifest file to update a registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/) for information about editing the [changelog](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) property in the app manifest file. |

The **Download Manifest** option in the kebab menu enables you to download a copy of that version's app manifest.

## Next steps

- Review the procedure to [update extension app registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/).
- Learn how to [publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) to the Docusign App Center.
- Read the App Center [publishing guidelines](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/guidelines/).

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
