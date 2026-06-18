---
title: Extension app status and distribution
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/status/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Status
scraped_at: '2026-06-18T19:51:49Z'
---

# Extension app status and distribution

The [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/) displays two types of status for each extension app:

- [Status](https://developers.docusign.com/extension-apps/build-an-extension-app/status/#status): Indicates the current stage of an extension app in the development, review, and publishing process.
- [Distribution](https://developers.docusign.com/extension-apps/build-an-extension-app/status/#distribution): Indicates whether the published version of an extension app is available to all [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) users or only to users in accounts that you specify.

By default, published extension apps are available only to US customers on the production App Center. You can specify availability in additional regions. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for details.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='779' width='1397' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![My Apps page](https://images.ctfassets.net/aj9z008chlq0/7fV1NdPWwXPgKTff3xnZou/2f21a312e2e52d26ab9f5bce54fcd324/MyApps.png?w=1397&h=779&q=50&fm=png)

## Display the status and distribution for extension apps

You can see status and distribution information in these Developer Console locations:

- My Extension Apps page: Lists all extension apps in your account, including the status for each extension app's latest [version](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) and the distribution. The My Apps page is displayed when you log in to the [Developer Console](https://devconsole.docusign.com).
- Header in the extension app detail pages: Selecting an extension app on the My Extension Apps page displays a menu of detail pages where you can perform various tasks. Each detail page header includes the latest version number, the status of that version, and the distribution type.
- [App Versions](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/#see-a-list-of-versions-for-an-extension-app) page: An extension app detail page that lists all versions of an extension app, including their statuses and changelog details.

## Status

Each [version](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) of an extension app has a status. An extension app can have multiple versions in different statuses.

For an extension app that has multiple versions, only one version can be in any of these statuses at a time: **Draft**, **In Review**, **Approved**, or **Rejected**. You cannot create a new draft version while any other version is in **Draft**, **In Review**, **Approved**, or **Rejected** status.

Extension app statuses are described below.

| Status | Description | Prohibited actions | Notes |
| --- | --- | --- | --- |
| **Draft** | The extension app version is being [registered](https://developers.docusign.com/extension-apps/build-an-extension-app/register/) and [tested](https://developers.docusign.com/extension-apps/build-an-extension-app/test/). | [Publishing](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) | Extension app versions in this status can be used for testing in envelopes and workflows in your developer account. They cannot be used in production, and members of other accounts cannot view or install them.  After you have finished development and testing, you can start the process to [publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) to the Docusign App Center.  You can delete an extension app version only if it's in **Draft** status. |
| **In Review** | The extension app version has been [submitted](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) for Docusign review to obtain approval to publish it to the App Center. | [Updating](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) [Publishing](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) [Deleting](https://developers.docusign.com/extension-apps/build-an-extension-app/delete/) | An extension app version that's been submitted for review remains in this status until Docusign approves or rejects it.  To update or delete a version that's in this status, you must first [cancel the publishing process](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) so that the version reverts to **Draft** status. After updating it, you must resubmit it for review if you want to publish it to the App Center. |
| **Approved** | Docusign has completed review of the extension app version and [approved](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) it for distribution in the App Center. | [Updating](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) [Deleting](https://developers.docusign.com/extension-apps/build-an-extension-app/delete/) | An extension app version that's been approved remains in this status until you publish it or cancel publication.  To update or delete a version that's in this status, you must first [cancel the publishing process](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) so that the version reverts to **Draft** status. After updating it, you must resubmit it for review if you want to publish it to the App Center. |
| **Rejected** | The extension app version failed Docusign review. | [Updating](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) [Publishing](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) [Deleting](https://developers.docusign.com/extension-apps/build-an-extension-app/delete/) | To update or delete a version that's in this status, you must first [cancel the publishing process](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) so that the version reverts to **Draft** status. After updating it, you must resubmit it for review if you want to publish it to the App Center. |
| **Live** | The extension app version has been [published](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) to the App Center. | [Deleting](https://developers.docusign.com/extension-apps/build-an-extension-app/delete/) [Publishing](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) | **Live** extension app versions can be viewed and installed on the production App Center. Availability may be restricted by the distribution type or region. See [Distribution](https://developers.docusign.com/extension-apps/build-an-extension-app/status/#distribution) for details.  If you [update the registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) for a **Live** extension app, Docusign creates a new version in **Draft** status. You can submit the new version for review and publish it after it has passed. The new version becomes **Live** on publication, and the previous **Live** version's status changes to **Discontinued**. See [Extension app versioning](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) for details.  For an extension app that has multiple versions, only one version can be **Live**.  You cannot delete an extension app version that's in **Live** status. If you want to remove a live extension app from the App Center without replacing it with a new version, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. |
| **Discontinued** | This previously **Live** version of an extension app has been replaced with a new version. | [Updating](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) [Publishing](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) [Deleting](https://developers.docusign.com/extension-apps/build-an-extension-app/delete/) | When a newer version of an extension app passes Docusign review and you publish it, the previous **Live** version's status changes to **Discontinued**.  When a version's status becomes **Discontinued**:   - It is no longer listed on the Docusign App Center and cannot be installed. - Any accounts that had the **Discontinued** version installed are automatically upgraded to the new **Live** version.   **Discontinued** versions appear only on the [App Versions](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/#see-a-list-of-versions-for-an-extension-app) page. |

## Distribution

An extension app has only one distribution type, regardless of the number of [versions](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/). You define the distribution type when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/).

The distribution types are:

- **Public:** After the extension app has been published and is in **Live** status, it can be used in production by any App Center user whose account is based in an allowed region for the app. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for more information.
- **Private:** The **Live** extension app version is available in production only to users in accounts that you specify. See [Choosing private distribution instead of public](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/) for details about how private and public extension apps differ.

This table summarizes how an extension app's distribution type and status determine the app's availability to users on the demo and production [App Centers](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

| Distribution | Status | Available on demo App Center to | Available on production App Center to |
| --- | --- | --- | --- |
| **Public** | **Draft** or other pre-publication status | Users under your developer account | Not available |
| **Public** | **Live** | Users under all accounts | Any user whose Docusign account is based in one of the allowed regions for the extension app. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for details. |
| **Private** | **Draft** or other pre-publication status | Users under your developer account | Not available |
| **Private** | **Live** | Users under your developer account | Any user under the accounts that you share the extension app with during publication. In the current release, private extension apps can be shared only with accounts based in the US.  **Note:** Before users can view and install your extension app, their account administrator must approve it. See [Choosing private distribution instead of public](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/) for details. |

## Next steps

- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- See how Docusign applies [versions](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) to extension apps.
- Learn more about the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).
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
