---
title: What's inside an extension app registration
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/inside-an-extension-app/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Inside An Extension App
scraped_at: '2026-06-18T19:51:48Z'
---

# What's inside an extension app registration

There are two ways to register an extension app in the [Docusign Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/): by using the form-based experience in the UI, or by uploading a JSON [app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/) file that describes the extension app, its connections, its actions, and its optional capabilities. The Developer Console enables you to manage the entire lifecycle of  your extension apps, including registering, testing, publishing, monitoring, and updating.

See [Use a form to register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/) and [Use a manifest file to register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/) for details on each way to register an extension app. See an [Example JSON manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) or view the [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for a full list of supported elements.

The following diagram sequence illustrates how you might create each piece of an extension app, step by step.

1. Register an **extension app** through the Developer Console and choose the extensions your app will implement. In the form-based experience, you choose the type in the UI. In the app manifest, you define this in the **template** property.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='372' width='656' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image showing the first step of creating an extension app registration](https://images.ctfassets.net/aj9z008chlq0/67dPPMeRM3vxZkBWnHm8Ni/6a809bd6f5384450daef94abbf74a027/what-s_inside_-_step_1.png?w=656&h=372&q=50&fm=png)

2. Each extension has a contract that defines its required supported types. You can add these actions and capabilities in the form-based experience UI or in the **actionReferences** object of your app manifest.

**Note:** If you register your app using an app manifest, make sure that the action names in the **actionReferences** object match the names in the **actions** objects.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='573' width='891' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image showing the structure of an extension app registration with an extension and three actions.](https://images.ctfassets.net/aj9z008chlq0/7DoaHTMNFRP31FWDEcpqmu/46e2ca3cfea500818944451b11921987/what-s_inside_-_step_2.png?w=891&h=573&q=50&fm=png)

3. Each **action** and **capability** defines an API call to an **external service**.  This **Connection** tells your app how to connect to and obtain authorization from the external service. You can configure this using the UI in the form-based experience, or add a **Connection** object in the app manifest.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='833.9999999999999' width='912' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image showing the structure of an extension app registration, highlighting the connection and external service](https://images.ctfassets.net/aj9z008chlq0/1W0qIep1gUEHKpkH16675q/c9c8f7970f42ebe7d387314959d83b8d/what-s_inside_-_step_3.png?w=912&h=834&q=50&fm=png)

4. Your app also needs to include some **metadata**, like your app's name and publisher information.

Here’s an example of the components of an extension app registration with one extension and one action to verify a phone number.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='841' width='831' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image showing an example app registration structure](https://images.ctfassets.net/aj9z008chlq0/2azR2jeyHx2ZUqLnuZQtTl/7684231a040023dd3f49dba763d99459/what-s_inside_-_step_4.png?w=831&h=841&q=50&fm=png)

An extension app will connect to a single external platform. The extension app’s registration defines:

- **A** [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/), which defines the authorization data Docusign needs to communicate with the external platform.
- **Any number of** [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/).  Each extension supports a type of external functionality, such as data verification or connected fields. Extensions must adhere to the contracts of required actions based on their type (the value of the extension’s `template`property).
- **Any number of** [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/), which are triggered to do units of work for your extensions. When triggered, each action and capability will call an external platform API endpoint to perform a function. Actions and capabilities must also adhere to input and output contracts based on their type (the value of their `template`property). Actions are required for an extension; capabilities are optional.
- **A set of metadata** that describes the extension app and publisher. This metadata is referenced when the extension app is published in the [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

See [Extension app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/) for details.

## Next steps

- See [Use a form to register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/) and [Use a manifest file to register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/) for details on how to register an extension app through the UI or via uploading a JSON manifest file.
- Learn more about [supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/).
- See [extension app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/) details and an example.
- Get specifications in the [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/).

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
