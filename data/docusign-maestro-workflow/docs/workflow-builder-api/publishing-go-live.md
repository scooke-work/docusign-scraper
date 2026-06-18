---
title: Publishing and Go-Live
source_url: https://developers.docusign.com/docs/workflow-builder-api/publishing-go-live/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Workflow Builder API
- Workflow Builder API
- Publishing and Go-Live
scraped_at: '2026-06-18T17:59:18Z'
---

# Publishing and Go-Live

To use your Workflow Builder API integration app in production, you will need to:

- Publish any Workflow Builder workflows that the app invokes.
- Ensure that any [Extension apps](https://developers.docusign.com/extension-apps/) used in your Workflow Builder workflow steps are published.
- Promote your application’s integration key from your developer account to a production Docusign account by passing a Go-Live review, similar to the [Go-Live](https://developers.docusign.com/docs/esign-rest-api/go-live/) process for the eSignature REST API.

## Publishing workflows

Publishing a workflow makes it available for other users in your account to view and run, as well as making it usable by your apps in the production environment.

Before you can publish a workflow, it must first pass a short automated review, which ensures that it is configured correctly and that users have given appropriate consent for the workflow to run. You can start this review manually through the UI (see [Review and Publish a Workflow](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=iqm1698272226447.html)). 

If the prepublication check fails due to consent errors, open the URL provided in the `consentUrl` field and have the user provide consent, then make the API call again.

If the prepublication check passes, you can publish the workflow by calling the endpoint again and removing the `isPreRunCheck=true` parameter.

## Go-Live

Before you can begin the Go-Live process with an API integration that uses Workflow Builder API, you must have access to the Workflow Builder API for your account.

When you are ready to start Go-Live review for your application, follow the steps described on the [Go-Live](https://developers.docusign.com/docs/esign-rest-api/go-live/) overview page for the Docusign eSignature REST API. **Note:** If your application fails Go-Live review, you may be required to bring it into compliance with the [Rules and resource limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/) before you can Go-Live.

After the form is processed, your integration key will be copied into production, enabling your app to call the production API endpoints.

## API endpoints

The developer and production endpoints for most Docusign APIs use slightly different paths. This table lists the endpoint base paths for each Docusign API and environment so you know how to modify your code when you migrate from the developer environment to production.

|  |  |  |
| --- | --- | --- |
| **Environment** | **API Base URI** | **Web Site Login URL** |
| Developer | `https://api-d.docusign.com/v1/accounts/` | `https://account-d.docusign.com` |
| Production | `https://api.docusign.com/v1/accounts/`  ```  ``` | `https://account.docusign.com` |

 **Note:** To access production API endpoints, you will need to enable your integration key in the production environment. See [Go-Live](https://developers.docusign.com/platform/go-live/) for more information.

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
