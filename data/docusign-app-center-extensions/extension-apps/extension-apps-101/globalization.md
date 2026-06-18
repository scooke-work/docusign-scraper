---
title: Globalization
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/globalization/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Globalization
scraped_at: '2026-06-18T19:51:50Z'
---

# Globalization

You have the option of making your extension app available for production use in specific regions.

If you limit your extension app's availability by region, [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) users can install your extension app only if their account is based in a Docusign data center that corresponds to one of the allowed regions.

This table lists the supported regions and the Docusign data centers that each region includes.

| Region | Data centers |
| --- | --- |
| Australia | AU |
| Canada | CA |
| European Union | EU |
| Japan | JP1 |
| United States | NA1, NA2, NA3, and NA4 |

For example, if you limit your extension app to the United States region, Docusign users can install your extension app for production use if their account is based in the NA1, NA2, N3, or NA4 data center.

**Note:** Additional globalization features, such as the ability to localize extension app metadata for specific languages, will be available in future releases.

## Behaviors and limitations

Regional availability for extension apps is subject to these behaviors and limitations:

- Region restrictions apply only in the production App Center. In the demo App Center, published extension apps are available to all users, regardless of region.
- In the production App Center, users who have not logged in will see listings only for extension apps that are available to the US region. After logging in, users will see listings for apps that are available to their region.

## Implement regional availability for an extension app

You define supported regions when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/).

If you will register the extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), see [Update distribution details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-distribution-details) for instructions on defining the regions.

If you will register the extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), set the value of `publicationRegions` to an array of regions in which your app should be available. See [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for the list of valid values and an example.

If you omit `publicationRegions` when creating a new app manifest, a default value of `US` will be used. If you omit `publicationRegions` when updating an app manifest for a published extension app, the value from the published version will be used. If `publicationRegions` is set to an empty array, the [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/) will return a validation error.

When [updating extension app registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) for a published extension app, you can add regions, but you cannot remove them. Removing regions from a published extension app is not recommended and not supported in the Developer Console. If absolutely necessary, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. Requests will be handled on a case-by-case basis.

You may need to configure your firewall to allow requests from IP addresses associated with the selected regions. See [Firewall configuration](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/network-configuration/#firewall-configuration) for details.

## Next steps

- Get an overview of the differences between [public and private extension apps](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/).
- Find out how to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- Learn about [extension app statuses](https://developers.docusign.com/extension-apps/build-an-extension-app/status/).
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
