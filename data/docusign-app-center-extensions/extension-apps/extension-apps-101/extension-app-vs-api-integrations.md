---
title: How extension apps differ from API integrations
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/extension-app-vs-api-integrations/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Extension apps vs API integrations
scraped_at: '2026-06-18T19:51:48Z'
---

# How extension apps differ from API integrations

Extension apps and API integrations are types of applications that you can implement to meet your organization’s agreement process requirements.

An [extension app](https://developers.docusign.com/extension-apps/extension-apps-101/) incorporates external functionality into the Docusign agreement process. Each extension app performs one or more tasks, such as archiving a document or verifying customer data. It accomplishes a task by launching requests to an external service, such as Google, Salesforce, or Dropbox, or to your own API. To be used, an extension app must be incorporated into a Docusign [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) or [workflow](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/) at one or more [extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/#extension-points), such as an envelope field or workflow step. When a recipient completes the envelope field or workflow step, the extension app’s functionality is triggered.

An [API integration](https://developers.docusign.com/platform/build-integration/) is a self-contained application that incorporates Docusign features by making requests to [Docusign APIs](https://developers.docusign.com/docs/). API integrations can implement a complete, end-to-end agreement process that includes creating and sending documents, as well as any business logic that is applied before, during, or after document processing.

Here’s a summary of other differences.

| Area | Extension apps | API integrations |
| --- | --- | --- |
| API caller/callee relationship | The Docusign agreement is the caller, and the external API is the callee. An extension app defines the [connection and endpoint details](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/) that enable a Docusign agreement to call an external API. | The API integration is the caller, and the Docusign API is the callee. |
| Business logic | Business logic is implemented in an external platform. An extension app leverages this functionality by calling the external platform endpoints. | API integrations contain all the code required for business processes and calling Docusign APIs. |
| Development process | You register extension apps in the Docusign [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/) by [using a guided, form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/) or by [constructing a JSON app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/). | You create API integrations in your own development environment using your preferred development tools and programming languages. |
| Testing | You can [test extension apps](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) using the Developer Console’s built-in features that validate authorization and endpoint requests and responses. You can also create envelopes and workflows to test end-user functionality. | To test API integrations, you devise and execute a testing process in your development environment. |
| Deployment | Before you can use your extension app in production, you must submit it for [Docusign review](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/). After it has been approved, you can publish it for production use with the click of a button. | API integrations must pass a [go-live](https://developers.docusign.com/platform/go-live/) process on the Docusign developer environment in order to be promoted to production. You must perform additional configuration on the production environment after the integration is promoted. |
| Distribution | You can make extension apps available in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) after they pass a Docusign review. You can make them available to all users or only to users under specific Docusign accounts. | API integrations are typically available only to your organization or customers; you can choose your own distribution method. |

## Next steps

- Learn more about [Extension app concepts](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/).
- Get an overview of [Extension app use cases](https://developers.docusign.com/extension-apps/extension-apps-101/use-cases/).
- Find out how to [Build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).

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
