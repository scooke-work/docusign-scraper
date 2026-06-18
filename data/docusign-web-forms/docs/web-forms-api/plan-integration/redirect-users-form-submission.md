---
title: Redirect users after form submission
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Redirect users after form submission
scraped_at: '2026-06-18T19:46:29Z'
---

# Redirect users after form submission

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

After a user submits a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances), your application should direct their browser to an appropriate page to inform the user that their information was successfully submitted.

The mechanism for doing so depends on which of these options your application uses to [render or deliver web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/):

- [Docusign JS](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/#form-submission-when-rendering-with-docusign-js)
- [Redirection to the Docusign platform](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/#form-submission-after-a-redirect-to-the-docusign-platform)
- [Remote delivery](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/#redirects-for-remote-web-form-instances)

## Form submission when rendering with Docusign JS

If your application uses the [Docusign JS](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls) client SDK to render [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) in an embedded iframe, you should implement listeners to detect [events](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) that indicate when a form submitter has finished their tasks. When the relevant event is triggered, your application can route the user to another page in your web application. See [Form and envelope events](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) for details about the events your application should use to trigger a redirect.

## Form submission after a redirect to the Docusign platform

If your web application redirects users' browsers to the Docusign platform for the display of [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances), page display options after form submission depend on the [type of web form configuration](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) that is used to generate web form instances. See the next sections for details.

**Instances generated from template-based configurations with embedded signing**
In this scenario, web form instances are generated from a [template-based](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/#instance-processing-template-based-web-form-configurations) web form configuration, and the configuration's [Initiate signing session from email](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) setting is not enabled. This means that the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) generated on web form instance submission is displayed in an *embedded signing* view within your web application. To redirect users' browsers after envelope completion, your application can supply a [returnUrl](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_returnurl) in the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call that creates a web form instance. If you do not supply a `returnUrl`, the web form configuration [thank you page](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=vgq1683244272836.html) is displayed after users complete envelopes.

**Instances generated from template-based configurations with remote signing**In this scenario, web form instances are generated from a [template-based](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/#instance-processing-template-based-web-form-configurations) web form configuration, and the configuration's [Initiate signing session from email](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) setting is enabled. After submitting a web form instance, a user accesses the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) on the Docusign platform via an emailed link (a process known as *remote signing*).The user is not routed elsewhere after signing, unless the [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates) is associated with a brand that specifies a post-signing destination. See [Destination URLs for Post-Signing Navigation﻿](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=tad1583277330037.html)﻿ for more information.

**Instances generated from standalone configurations**For web form instances generated from [standalone](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/#instance-processing-standalone-web-form-configurations) web form configurations, form instance submission does not generate an envelope. After form submission, Docusign displays the [thank you page](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=vgq1683244272836.html) defined in the web form configuration. In the current release, there is no option to redirect users to another URL.

## Redirects for remote web form instances

Redirects after submission for [remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/) are supported through the [branding](https://developers.docusign.com/docs/web-forms-api/plan-integration/apply-custom-branding/)feature. A redirect works only if the [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates) or instance is associated with a brand, and that brand has a post-signing URL configured. A brand associated with a web form template will be applied by default to all web form instances created from that template. A brand supplied in an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request overrides a brand associated with a web form template. Without a brand that includes a post-signing URL, a remote web form instance will redirect to a static, Docusign-branded page.

To configure a post-signing URL in a brand:

1. In your Docusign account, select **Admin**, then from the left nav, choose **Brands**.
2. Create a new brand; or select the brand you want to apply and choose **Edit** from the brand’s kebab menu; then, under **Advanced Configuration,** choose **Destination URLs.**
3. In the **Signing Completed** field, add the destination URL to which you want users routed after they complete the remote web form instance and envelope.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='600' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Destination URL](https://images.ctfassets.net/aj9z008chlq0/500mBlH89iJSWYrYoAPfqN/176a66fd9845964c87ce43d4dbf8184e/DestinationURL.png?w=1592&h=1554&q=50&fm=png)

When the brand is applied to a web form template or instance, the **Signing Completed** URL from the brand’s configuration determines the redirect destination. See [Apply custom branding](https://developers.docusign.com/docs/web-forms-api/plan-integration/apply-custom-branding/) for more information about how to associate a web form template or instance with a brand.

## Next steps

- See [Web form instance processing](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/) for an overview of the interaction between a user, a Web Forms API integration, and the Docusign platform.
- Review the process to [deliver remote web form instances via email](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/).
- See the options for [rendering embedded web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/).

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
