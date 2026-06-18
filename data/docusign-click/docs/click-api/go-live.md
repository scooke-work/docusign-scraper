---
title: Go-Live
source_url: https://developers.docusign.com/docs/click-api/go-live/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Click API
- Click API
- Go-Live
scraped_at: '2026-06-18T22:18:20Z'
---

# Go-Live

Before you can begin the Go-Live process, you must have a paid production Docusign account with a plan that includes elastic signing.To start Go-Live review for your application:

1. Open a [Docusign Support case](https://support.docusign.com/CSP_DSClogin?startURL=%2Fen%2FcaseOverview%3Fdfl%3D1) to create a request.
2. In the **Choose Case Subject** screen, select **APIs and & Developement**, then **Docusign APIs**.
3. Select the **Add Case Details** button.
4. In the **Add New Case** screen, enter “Click API Go-Live**”** in the **Case Subject** field, then enter your integration's data and a brief description.
5. Select **Submit Case**.

**Note:** If your application fails Go-Live review, you may be required to bring it into compliance with the [Rules and resource limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/) before you can Go-Live.

After the form is processed (which takes up to three business days), your integration key will be copied into production, enabling your app to call the production API endpoints.

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
