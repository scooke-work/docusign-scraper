---
title: Go-Live
source_url: https://developers.docusign.com/docs/rooms-api/go-live/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- Go-Live
scraped_at: '2026-06-18T22:33:02Z'
---

# Go-Live

Before you can begin the Go-Live process, you must have a paid Docusign account with a plan that includes a Rooms API product, such as:

- Enterprise Offerings
- [Enhanced Real Estate Brokerage Plans](https://www.docusign.com/products-and-pricing/real-estate-editions)
- [Rooms for Mortgage](https://www.docusign.com/products/rooms-for-mortgage?_gl=1*6lyh4a*_ga*NjU1MTM1MTQxLjE2NTk2NTI2NjU.*_ga_1TZ7S9D6BQ*MTY1OTczMTc0MS42LjEuMTY1OTczNTA4My42MA..&_ga=2.18371579.39987545.1659652665-655135141.1659652665)

To begin the Go-Live process for your application:

1. Open a [Support Case](https://support.docusign.com/CSP_DSClogin), choose **Continue** in the **eSignature Rooms CLM** column, then **APIs & Development**, and finally **Docusign APIs**. Include the words **Rooms Go-Live** in the your **Case Subject** and provide the following information:
   - The name and email of a Production Admin user, who can be any member of the account with full administrative permissions
   - Your production API Account ID
   - Your developer API Account ID
   - The integration key of the application in the developer environment to be pushed into production
2. Docusign will perform a review on the developer transactions recorded between the specified dates. Once they're confirmed, you will receive a Go-Live form to sign. Sign the form to submit it to Docusign for processing.

   **Note:** If your application fails Go-Live review, you may be required to bring it into compliance with the [Rules and resource limits](https://developers.docusign.com/docs/rooms-api/rooms101/rules-and-limits/) before you can Go-Live.

## API endpoints

The developer and production endpoints for most Docusign APIs use slightly different paths. This table lists the endpoint base paths for each Docusign environment so you know how to modify your code when you migrate from the developer environment to production.

| **Environment** | **API Base URI** | **Website Login URL** |
| --- | --- | --- |
| Developer | `https://demo.rooms.docusign.com/restapi/v2/` | https://demo.room.docusign.com |
| Production | `https://rooms.docusign.com/restapi/v2/` | https://rooms.docusign.com |

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
