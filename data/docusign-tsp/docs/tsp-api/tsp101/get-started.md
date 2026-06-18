---
title: Getting started with your TSP integration
source_url: https://developers.docusign.com/docs/tsp-api/tsp101/get-started/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- Tsp101
- Tsp101
- Get started with the Web Forms API
scraped_at: '2026-06-18T22:15:24Z'
---

# Getting started with your TSP integration

Proceed as follows to start your TSP integration:

1. Submit your integration project. To join the TSP Partner Program, you must first submit the details of your integration project to
   [TSPprogram@docusign.com](mailto:tspprogram@docusign.com) . If the TSP Partner Program team approves your project, you can proceed with the integration.
2. Create your developer account. A developer account enables you to develop your integration in an internal demo environment. For more information on how to create your developer account, see
   [Build a Docusign integration](https://developers.docusign.com/platform/build-integration/) .
3. Configure your integration.Configuring your integration requires that you create and set up a Docusign application. See
   **Configure your integration** below for more information on how to configure your application.
4. Send configuration information to your Docusign representative.You must provide your Docusign representative with proper configuration information to finalize the integration. For more information, see
   **Send configuration information to your Docusign representative** below.

## Configure your integration

1. Create your integration key See
   [Integration key](https://developers.docusign.com/platform/configure-app#integration)
2. Create your secret key See
   [Secret key](https://developers.docusign.com/platform/configure-app#secret)
3. Create a redirect URL The redirect URL targets the iframe of the TSP (see also
   [API Flow](https://developers.docusign.com/docs/tsp-api/tsp101/api-flow/)). Docusign recommends that you create both a development and production redirect URL. To simplify the integration in your development environment, use a localhost server (for example, https://localhost:8080/docusign). For more information on how to create redirect URLs, see
   [Redirect URI](https://developers.docusign.com/platform/configure-app#redirect).
4. Add the redirect URL to the integration key
   [Edit your integration key](https://support.docusign.com/guides/ndse-admin-guide-api-and-keys)
   and add the redirect URL in the
   **Redirect URIs** section.
5. Create an RSA key pair See
   [RSA key pair](https://developers.docusign.com/platform/configure-app#keypair)
6. Create a User ID See
   [User ID](https://developers.docusign.com/platform/configure-app#userid)
7. Create an API account ID See
   [API account ID](https://developers.docusign.com/platform/configure-app#apiaccountid)
8. Select an authentication method See
   [Authentication method](https://developers.docusign.com/platform/configure-app#authmethod)
9. Set privacy policy link See
   [Privacy policy](https://developers.docusign.com/platform/configure-app#privacylink)
10. Set a terms of use linkSee
    [Terms of use](https://developers.docusign.com/platform/configure-app#termslink)

## Send configuration information to your Docusign representative

Your Docusign representative needs the following data to set up the signature type associated with your TSP:

- Developer account ID
- Integration Key ID
- Redirect URL

### Developer account ID

To get your developer account ID, see
[Where do I find my Docusign account number?](https://support.docusign.com/articles/Where-do-I-find-my-Docusign-account-number)

### Integration Key ID

Proceed as follows to get your integration key ID:

1. Log in to your developer account.
2. Select the **Settings** tab.
3. Select the **Apps and Keys** menu.
4. Locate your application and copy the ID in the **Integration Key** column.

### Redirect URL

Proceed as follows to get your redirect URL:

1. Log in to your developer account.
2. Select the
   **Settings** tab.
3. Select the
   **Apps and Keys** menu.
4. Locate your application and select
   **Actions > Edit**.
5. In the
   **Additional settings** section, copy the redirect URLs.

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
