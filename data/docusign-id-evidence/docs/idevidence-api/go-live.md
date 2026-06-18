---
title: Go-Live
source_url: https://developers.docusign.com/docs/idevidence-api/go-live/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- ID Evidence API
- ID Evidence API
- Go-Live
scraped_at: '2026-06-18T21:43:33Z'
---

# Go-Live

When you are ready to launch your ID Evidence API app in production, you will need to promote your application’s integration key from your developer account to a production Docusign account by passing a Go-Live review, similar to the [Go-Live](https://developers.docusign.com/docs/esign-rest-api/go-live/) process for the eSignature API.

Before you can begin the Go-Live process, you must have a paid production Docusign account with a plan that includes ID Evidence.

When you are ready to start the Go-Live review for your application, follow the steps described on the [Go-Live](https://developers.docusign.com/docs/esign-rest-api/go-live/) overview page for Docusign eSignature.

**Note:** If your application fails Go-Live review, you may be required to bring it into compliance with the [API rules and resource limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/) before you can Go-Live.

After the form is processed (which takes up to three business days), your integration key will be copied into production, enabling your app to call the production ID Evidence API endpoints.

## API endpoints

The developer environment and production endpoints for most Docusign APIs use slightly different paths. For the ID Evidence API:

| Environment | ID Evidence API base URL |
| --- | --- |
| Developer | https://proof-d.docusign.net/api/ |
| Production | https://proof.docusign.net/api/ |

**Note:** {server} is the data center location of your production account (for example, **CA**, **NA2**, or **EU**). You can obtain your production data center location from:

- The `base_uri` in the response of a call to [/oauth/userinfo](https://developers.docusign.com/platform/auth/reference/user-info/). If you obtain the `base_uri` in this way, you should do it once when the user authenticates for the first time and cache the response.
- The **Account Base URI** section of the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page

For a full list of sites, see [Site certificates](https://support.docusign.com/s/document-item?bundleId=khf1655309726546&topicId=kkh1657307586557.html&_LANG=enus). To access production API endpoints, you'll need to enable your integration key in the production environment. See [Go-Live](https://developers.docusign.com/platform/go-live/) for more information.

## Next steps

Learn more about the Go-Live process and what you need to do after you pass Go-Live with these resources:

- [Go-Live troubleshooting](https://developers.docusign.com/platform/go-live/troubleshooting/)
- [After Go-Live](https://developers.docusign.com/platform/go-live/after-go-live/)

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
