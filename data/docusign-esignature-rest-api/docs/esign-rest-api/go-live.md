---
title: Go-Live
source_url: https://developers.docusign.com/docs/esign-rest-api/go-live/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- Go-Live
scraped_at: '2026-06-18T21:09:47Z'
---

# Go-Live

When you are ready to launch your app in a production environment, you will need to promote your [integration key](https://developers.docusign.com/platform/configure-app/#integration-key) from your developer account to a production Docusign account. This will enable:

- Sending of legally binding eSignature requests.
- Any user on any production Docusign account to access your app.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='510' width='800' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![The Go-Live process](https://images.ctfassets.net/aj9z008chlq0/6A1OeRsnEHNLrBS3iQ9hl2/44326dfe37806d267fe0f5cd0bf95472/Environments-go-live.jpg?w=800&h=510&fl=progressive&q=50&fm=jpg)

## Promoting your app

To promote your app, you must:

1. Choose a classification for your app. Your app’s classification is determined by its business model. Choose the option that aligns with your role and the type of app that you are building. Your choice of **integration classification** at Go-Live also affects how envelopes are billed on your production account. Each classification uses a different billing model for envelope sends. To understand the specific pricing for each send type, review your Docusign production plan details or contact your Docusign representative.

   The options and their associated requirements are listed below:

   |  |  |
   | --- | --- |
   | **Use case** | **Classification to choose** |
   | Your integration will be directly used by your employees or your customers’ employees. | Private custom integration |
   | You want to use a Docusign partner integration for your business need, and that integration requires you to provide your own integration key (IK). | Third-party integration key |
   | You’re building a public integration for multiple Docusign customers, who will access it using their own Docusign accounts. They will authorize your integration to connect with their account directly.  As they use your integration, you’ll earn referral revenue from Docusign based on their usage. **Note**: You’ll need to join the Docusign Partner Program to launch a public integration. | Public integration |
   | You’re embedding one or more Docusign features into your own product and offering them as a service to your customers.   Your customers won’t need their own Docusign accounts to access this. Instead, they’ll use the features through your Docusign account, which you own and control. **Note**: To use this model, you’ll need to be an ISV Embed partner, which requires a special license. | Embedded integration |
2. Request a **Go-Live review** in eSignature Admin.
3. To qualify for and pass the Go-Live review, your app must meet all the requirements for going live for its classification. See [Go-Live review](https://developers.docusign.com/docs/esign-rest-api/go-live/#review) for details.
4. After passing this review, you will receive an email notification and the key’s status changes to **Live**, indicating the key is enabled in the production environment. The key will also be displayed in the production Docusign account into which it has been promoted. If your app fails the review, its status changes to **Declined**.
5. When your app is promoted into the production environment, its integration key is duplicated into the production environment rather than moved. The integration key's configuration parameters such as secrets and redirect URIs are not also duplicated; you must add them in the production environment to match the settings for your app in the developer environment.

## Go-Live review

To pass the Go-Live review for the eSignature REST API, you must have:

- [OAuth 2.0 authentication](https://developers.docusign.com/platform/auth/) configured for your app.
- A paid production account that will serve as the management account for the app in the production environment. ISV partners can apply for a free IK management account via the partner program.
- Administrator access to the production account.

If you’re encountering problems passing the Go-Live review, see [Go-Live troubleshooting](https://developers.docusign.com/platform/go-live/troubleshooting/).

## API endpoints

The developer and production endpoints for most Docusign APIs use slightly different paths. This table lists the endpoint base paths for each Docusign environment so you know how to modify your code when you migrate from the developer environment to production.

| Environment | API base URI | Web site login URL |
| --- | --- | --- |
| Developer | `https://demo.docusign.net/restapi/v2.1/` | https://account-d.docusign.com |
| Production | `https://{server}.docusign.net/restapi/v2.1/` | https://account.docusign.com |

For information on the CLM API endpoints, see CLM [API 101](https://developers.docusign.com/docs/clm-api/clm101/). **Note:** {server} is the data center location of your production account (for example, **CA**, **NA2**, or **EU**). You can obtain your production data center location from:

- The `base_uri` in the response of a call to the [/oauth/userinfo](https://developers.docusign.com/platform/auth/reference/user-info/). If you obtain the `base_uri` in this way, you should do it once when the user authenticates for the first time and cache the response.
- The **Account Base URI** section of the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page.

For a full list of sites, see [Site certificates](https://support.docusign.com/s/document-item?bundleId=khf1655309726546&topicId=kkh1657307586557.html&_LANG=enus). To access production API endpoints, you'll need to enable your integration key in the production environment.

## Next steps

- For a list of issues that can prevent an app from passing a Go-Live review, see [Go-Live troubleshooting](https://developers.docusign.com/platform/go-live/troubleshooting/).
- For a list of configuration changes required for the production environment, see [After Go-Live](https://developers.docusign.com/platform/go-live/after-go-live/).

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
