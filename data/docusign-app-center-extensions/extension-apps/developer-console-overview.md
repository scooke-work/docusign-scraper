---
title: Developer Console overview
source_url: https://developers.docusign.com/extension-apps/developer-console-overview/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Developer Console Overview
scraped_at: '2026-06-18T19:51:48Z'
---

# Developer Console overview

The [Developer Console](https://devconsole.docusign.com) is the single place where you can both create and manage [API integrations](https://developers.docusign.com/extension-apps/developer-console-overview/#the-developer-console-for-api-integrations) and register and publish [extension apps](https://developers.docusign.com/extension-apps/developer-console-overview/#the-developer-console-for-extension-apps).

## The Developer Console for extension apps

The [Developer Console](https://devconsole.docusign.com) is a tool that enables developers to perform these tasks for extension apps:

- [Register](https://developers.docusign.com/extension-apps/developer-console-overview/#register-extension-apps)
- [Test](https://developers.docusign.com/extension-apps/developer-console-overview/#test-extension-apps)
- [Manage](https://developers.docusign.com/extension-apps/developer-console-overview/#manage-extension-apps)
- [Publish](https://developers.docusign.com/extension-apps/developer-console-overview/#publish-extension-apps)

To use the Developer Console, you must log in with a free Docusign [developer account](https://www.docusign.com/developers/sandbox). All users under your account who have admin permissions can use the Developer Console.

### Register extension apps

When you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/), you provide Docusign with the extension app name and description, publisher information, and details required to launch requests to the external API that provides extension functionality.

The Developer Console offers a guided web interface for providing all the details needed to register your extension app. You also have the option of manually populating extension app details in a JSON app manifest file and uploading or pasting the file in the Developer Console app manifest editor.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1714' width='900' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Register an extension app](https://images.ctfassets.net/aj9z008chlq0/3LeRmGqGsktAs3GoJdDqJI/8c3f7cf35e104b2247b5fc8d7bc080e3/Screenshot_2025-06-26_at_1.16.54â__PM.png?w=900&h=1714&q=50&fm=png)

### Test extension apps

A built-in [test feature](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) enables you to verify that Docusign can obtain [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) from the external API service or identity provider, connect to endpoints, send requests, and process the responses. You can also verify that the extension app functions correctly when used in an envelope or workflow.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1540' width='2108' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Developer Console: Test an extension app](https://images.ctfassets.net/aj9z008chlq0/4zdlyahvTCLSE5ZcQfFOMC/e25ddb2ca788f18cb33977ef3bbdbe56/Screenshot_2025-06-26_at_1.38.37â__PM.png?w=2108&h=1540&q=50&fm=png)

### Manage extension apps

After you have registered an extension app, you can [update the registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) or [delete it](https://developers.docusign.com/extension-apps/build-an-extension-app/delete/).

![](data:image/svg+xml;charset=utf-8,%3Csvg height='779' width='1397' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Developer Console: Extension app information](https://images.ctfassets.net/aj9z008chlq0/190xnuur9CLn5XGujkOB0N/2b333c2d1db244c8e48adcaae99bcd11/MyApps.png?w=1397&h=779&q=50&fm=png)

### Publish extension apps

Before you can use your extension app in production or make it publicly available in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/), it must pass a Docusign review. When you’ve finished developing and testing your extension app, you can [submit it for review](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) from the Developer Console.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1209' width='2044' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Publish an extension app](https://images.ctfassets.net/aj9z008chlq0/1d6zTvtoq4ZCZHbwnyBfBA/be7a35dd097edc72cdcb9594ce421f15/PublishApp.png?w=2044&h=1209&q=50&fm=png)

After an extension app has passed Docusign review, you can publish it to the App Center so that users can install it and use it in production envelopes and workflows.

## The Developer Console for API integrations

The Developer Console is the single location where you can manage [integration keys](https://developers.docusign.com/platform/configure-app/#integration-key) (IKs) across both the demo and production environments. Now, you can promote your app to production through the click of a button and you no longer need to switch between multiple accounts or follow the legacy [Go-Live](https://developers.docusign.com/platform/go-live/) process.

In the [Developer Console](https://devconsole.docusign.com/), developers can perform these tasks for API integrations:

- [Create an integration key (IK)](https://developers.docusign.com/platform/create-ik-developer-console/)
- [Give developers granular permissions over specific IKs](https://developers.docusign.com/platform/create-ik-developer-console/#share-specific-IKs-with-developers)
- [Monitor your integration](https://developers.docusign.com/platform/monitor-your-integration/)
- [View API logs at the integration key level](https://developers.docusign.com/platform/monitor-your-integration/integration-dashboard/)

## Next steps

- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- Learn about the process to [test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).
- Find out how to [publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/).
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
