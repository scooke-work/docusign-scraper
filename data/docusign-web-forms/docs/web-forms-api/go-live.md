---
title: Go-Live
source_url: https://developers.docusign.com/docs/web-forms-api/go-live/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Go-Live
scraped_at: '2026-06-18T19:46:30Z'
---

# Go-Live

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

When you are ready to launch your Web Forms API application in production, you will need to promote your application’s integration key from your developer account to a production Docusign account by passing a Go-Live review, similar to the [Go-Live](https://developers.docusign.com/docs/esign-rest-api/go-live/) process for the eSignature REST API.

Before you can begin the Go-Live process, you must have a paid production Docusign account with a plan that includes the Web Forms API.

To start a Go-Live review for your application:

1. Open a [Docusign Support case](https://support.docusign.com/CSP_DSClogin?startURL=%2Fen%2FcaseOverview%3Fdfl%3D1) to create a request.
2. Select **Continue** under eSignature.
3. On the **My Cases** screen, select **New Case**.
4. Select **APIs & Development**, then **Docusign APIs**.
5. Select **Add Case Details**.
6. On the **Add New Case** screen, enter “Web Forms API Go-Live**”** in the **Case Subject** field, then enter your integration's data and a brief description.
7. Select **Submit Case**.

After the form is processed (which takes up to three business days), your integration key will be copied into production and will be able to call production API endpoints.

## Migrate components to production after Go-Live

Production account settings and data are separate from developer account settings and data. When you promote a Web Forms API integration to production, you must migrate any components that the integration depends on to production. This includes:

- Web form configurations. To migrate a web form configuration, download it from the developer environment and upload it to production. See [Transfer a Web Forms Configuration File](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=xbb1680567836531.html)﻿ for details.
- Account users. See [User Management](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=ixb1583277365937.html) and related topics for user creation options.

Make sure that your production account has the same [account settings](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=nfw1583277366851.html) and options enabled that your application used in your developer account.

## Next steps

- See [Endpoint base path](https://developers.docusign.com/docs/web-forms-api/web-forms-101/endpoint-base-path/) for information about the production base URI.
- See the Docusign [Go-Live](https://developers.docusign.com/platform/go-live/) page for additional details about the process.

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
