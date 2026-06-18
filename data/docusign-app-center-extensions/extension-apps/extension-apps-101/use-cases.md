---
title: Extension app use cases
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/use-cases/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Use cases
scraped_at: '2026-06-18T19:51:48Z'
---

# Extension app use cases

You can use extension apps to simplify tasks during document preparation, signing, and post-signing. Some examples of extension app use cases include:

- Verifying bank account information in a financial agreement
- Address verification
- Recording data to your system of record
- Reading data from your proprietary system

![](data:image/svg+xml;charset=utf-8,%3Csvg height='342.99999999999994' width='688' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image showing an example flow where an extension app is used to verify data](https://images.ctfassets.net/aj9z008chlq0/70YBgwFFEZ2mGvErIcfpe1/771b419a79ccf47b5477cb3ab49bac42/Group_5.png?w=688&h=343&q=50&fm=png)

## Example data verification use case

1. A developer [builds](https://developers.docusign.com/extension-apps/build-an-extension-app/) a data verification extension app.
2. The developer submits their extension app for review with Docusign.
3. The developer [publishes](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) their extension app to the Docusign App Center, either as a **public** or [private](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/) extension app.
4. If it was built as a public extension app, a customer admin, looking for an app that can improve their organization’s processes, **finds the app and installs it**. If the app is private, only the owners of the accounts selected by the extension app developer can find and install it.
5. The extension app’s [Connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/) is configured to connect to the external platform that performs the data verification (for example, a bank account or email address verification service).
6. A customer process builder uses the [Workflow Builder API](https://developers.docusign.com/docs/workflow-builder-api/) or [Workflow Designer](https://apps-d.docusign.com/send/workflows/) to **create a workflow**. This workflow includes:
   1. A document that includes data verification fields that are connected to a data verification extension app
   2. An envelope signing step
7. Whenever that customer’s users sign that envelope as part of the Workflow Builder workflow, the **extension app will be executed** during the signing process. The extension app will validate the user’s entered information, such as a bank account number or email address, through the external platform. If the verification is successful, the signing continues. If not, the user is prompted to update the information.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='877' width='1381' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image showing an example data verification extension being created, published, and used.](https://images.ctfassets.net/aj9z008chlq0/4Wa9oAaJZSO6EV84BKIkbL/cd0a0cb41b14176c2bc5d135183f6eb4/Frame_1__2_.png?w=1381&h=877&q=50&fm=png)

## Next steps

- Learn more about [How extension apps work](https://developers.docusign.com/extension-apps/extension-apps-101/how-extension-apps-work/).
- See an [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/).
- Learn more about how to [Build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).

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
