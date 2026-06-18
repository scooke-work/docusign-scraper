---
title: Choosing private distribution instead of public
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Choosing Private Distribution
scraped_at: '2026-06-18T19:51:49Z'
---

# Choosing private distribution instead of public

Docusign provides the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) as a central location for all extension apps. This is where customers can discover a variety of extension apps to solve their business problems. As a developer, you have a choice. You can make your extension app public and available for all customers in the App Center, or you can make it available as a private extension app to a select group of customers only.

## Why build private extension apps?

Private extension apps are meant for customers who have specific business needs that can be met by building an extension app. However, they may be using proprietary or internal systems, there may not be a way for other customers to connect to their systems, or there may be other limitations imposed on their business. For all these reasons, they may not want to share their app with all Docusign customers. These private extension apps may be built directly by the customers who need the functionality, or they can be built by [Docusign Partners](https://developers.docusign.com/partner/) who are contracted by the customer to create and maintain extension apps on their behalf. 

In all of these cases, the developer does not wish to make the extension app available for all Docusign customers, but instead wants to limit the distribution to a select group of customers using a predefined list of Docusign production accounts.

## Example use cases for private extension apps

Some common scenarios include:

- **Internal data verification:** Verify signer information against internal CRM and ERP systems in real time during the agreement signing process. For more information, see [Connected fields extension overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/).
- **Custom form autofill:** Automatically populate agreement fields using data stored in internal CRMs, HR systems, or financial platforms. For more information, see [Connected fields extension overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/).
- **Secure data input and output:** Retrieve data from a system of record, display it to end users in a form, and write user-entered form values back to the system of record. For more information, see [Data IO extension overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/).

## Differences between public and private extension apps

### Defining distribution type

You select public or private distribution when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/).

If you will register the extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), see [Update distribution details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-distribution-details) for instructions on defining the distribution type. If you will register the extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), set the `distribution` property in the [app manifest](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) to `PUBLIC` or `PRIVATE`.

### Publishing and sharing with customers

To publish a public extension app, you need to be a Docusign partner. If you’re not yet a Docusign partner, Docusign will work with you for partner program onboarding when you submit your app for review. See [Join now](https://partners.docusign.com/s/join-now) for details on how to join the Docusign partner program.

The [publishing process](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) for new private extensions apps is very similar to the publishing process for public extensions apps, but private extension apps require an extra step after they are live to share them with one or more production accounts. To do so, the developer provides a list of up to 20 production accounts with whom they wish to share the new private extension app. The administrators for these production accounts receive a notification in the Docusign App Center about a new private extension app that is available for them, and then have to approve the new private extension app before any user in their account can install and use it. For public extension apps, however, no additional steps are required after publishing; public apps are automatically shared with all Docusign customers when published.

### Approval process

The [guidelines for approving extension apps](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/guidelines/) are less stringent for private extension apps compared to public extension apps.

## Private extension apps limitations

### Publishing requires Docusign approval

While private extension apps are not visible publicly for all customers, Docusign still needs to approve private extension apps before they can be published. The publishing process still requires the developer to ensure their app adheres to many of the same requirements that apply to public extension apps.

### Account owner (administrator) approval

An administrator of the production account must first approve a private extension app before it can be used by any member of the account.

### Modifying the distribution of extension apps

The distribution type cannot be modified once the extension app is in the **Live** state. You can only modify it if the app has never been live and is in **Draft**, **Approved**, or **Rejected** state. See [Update an extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) for details about the options for modifying the distribution.

### Sharing with other developer accounts

Your extension app is automatically available for you in your own developer account. You can share private extension apps (once published) with additional production accounts, but you cannot share them with additional developer accounts.

## Next steps

- Learn more about the [extension app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/).
- Find out how to [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/).
- Review the process to [publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/).
- View a [dashboard](https://developers.docusign.com/extension-apps/build-an-extension-app/monitor-usage/) that displays extension app usage data.

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
