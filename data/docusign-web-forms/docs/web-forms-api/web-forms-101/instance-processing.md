---
title: Web form instance processing
source_url: https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Web Forms API 101
- Web Forms API 101
- Web form instance processing
scraped_at: '2026-06-18T19:46:29Z'
---

# Web form instance processing

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

Web Forms API requests enable you to create and manage [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances). These sections walk you through the processing of web form instances generated from two types of [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations): template-based and standalone. See [Web Forms concepts](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/) for details about the differences between the two configuration types.

## Instance processing: Template-based web form configuration

The next two sections illustrate how an end user, your application, and the Docusign platform interact during the processing of a web form instance generated from a template-based web form configuration.

### Embedded web form instances

For this flow, the web form instance is embedded in your application, or your application redirects users to the Docusign platform to fill out the form instance.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='573' width='1002' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Instance creation from a template-based configuration via the Web Forms API](https://images.ctfassets.net/aj9z008chlq0/7FpXvS2ATxCfWP4hr49JrP/37b648441e6d51fe638519ed2f27dc48/ProcessFlowEmbedded.png?w=1002&h=573&q=50&fm=png)

1. A user takes an action in your application, such as clicking a button, to start filling out a form.
2. Your application launches an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call to create a web form instance for the user to fill out. The request specifies the [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) from which to create the instance by referencing the configuration ID.
3. The response includes a secure, unique URL for the web form instance. See [Web form instance URLs](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) for details.
4. Your application renders the web form instance URL. It can do this by using the Docusign JS client SDK to embed the instance in your application, or by redirecting to the instance URL. See [Render embedded web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/) for details about these options.
5. The user populates the web form instance fields and submits the instance to Docusign, which generates an [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) for the user to sign. Envelope creation and its display or delivery to the user occur automatically on web form instance submission, without requiring additional API requests from your application to create or deliver the envelope.

   The envelope includes values that the user entered on the form instance, if the form fields are [connected to template fields](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=vlb1680643208628.html) in the web form configuration.

   The envelope delivery method depends on a setting in the web form configuration:
   - [Embedded signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/): If the **Initiate signing session from email** setting on the web form configuration [signature page](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) is not enabled, the envelope signing session is displayed in the web browser after the user submits the form.
   - [Remote signing](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-template-remote/): If the **Initiate signing session from email** setting is enabled, the user receives an email that includes a link to the envelope signing session.

   If the web form configuration includes additional recipients who fill out the web form instance, they will receive an [envelope email](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=pah1578456451991.html) with a link. On selecting the link, they will be routed to the envelope with the web form instance embedded in it. After filling out the web form instance, they will be presented with the envelope. For additional recipients who are not required to fill out the web form instance, the emailed link will take them directly to the envelope.
6. Depending on the method your application used to render the form instance URL in step 4, Docusign issues one of these responses when the web form submitter signs and completes the envelope in an embedded signing session:
   1. If your application used the Docusign JS client SDK to render the form instance, Docusign returns a JavaScript `sessionEnd` [event](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) of type `signingResult` to your application when the web form submitter completes the envelope.
   2. If your application redirected the user to the form instance URL and the web form configuration is set to use embedded signing, Docusign sends the user to the [returnUrl](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_returnurl) specified in the `Instances:createInstance` API request or equivalent SDK method call. See [Redirect users after form submission](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/) for details.

      For a remote signing session, a `sessionEnd` event of type `remoteSigningInitiated` is triggered when the envelope is generated. The user is not routed to another URL upon envelope completion unless the web form template is associated with a brand that specifies a [post-signing destination](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=tad1583277330037.html). See [Form and envelope events](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) and [Form submission after a redirect to the Docusign platform](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/#form-submission-after-a-redirect-to-the-docusign-platform) for more information.

## Remote web form instances

For this flow, users access web form instances via an [envelope email](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=pah1578456451991.html).

When created from a multiple-recipient [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations), a remote web form instance and its associated envelope can be filled out by multiple users. Each recipient who fills out the form instance sees a distinct view with form fields specific to that user. All recipients are presented with the same envelope. The web form configuration specifies which users fill out both the form instance and envelope, and which users fill out the envelope only. The configuration also defines the order in which the recipients fill out the form instance and/or envelope. See [Build a Multiple-Recipient Web Form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=inc1745950777430.html)﻿ for instructions to set up multiple recipients.

In the example illustrated here, the web form configuration specifies two recipients who complete their tasks sequentially. The example configuration also requires that both recipients populate the web form instance, as well as the envelope.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='789' width='1002' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Remote web form instance process flow](https://images.ctfassets.net/aj9z008chlq0/4YNrm1mliMNKX8VJM2DeSn/a0ce0dcf94a23340c39f2397ba10cb54/ProcessFlowRemote.png?w=1002&h=789&q=50&fm=png)

1. Your application launches an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call to create a web form instance. The request specifies the web form configuration from which to create the instance by referencing the configuration ID.

   At the same time, Docusign generates an envelope based on the configuration's [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates).
2. The first user in the routing order receives an envelope email.
3. The link in the email routes the user to the Docusign platform, which displays an envelope with an embedded web form instance. The user fills out the form fields associated with that user's view of the web form instance. The user submits the web form instance.

   The eSignature envelope is displayed for the user to sign. Envelope display occurs automatically on web form instance submission.

   The envelope includes values that the user entered on the form instance, if the form fields are [connected to template fields](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=vlb1680643208628.html) in the web form configuration. The user signs and completes the envelope.
4. If a [brand](https://developers.docusign.com/docs/web-forms-api/plan-integration/apply-custom-branding/) is applied to the web form template or instance and the brand specifies a post-signing URL, the user is routed to that URL. Otherwise, the user remains on the Docusign platform.
5. The second user in the routing order receives an envelope email.
6. The link routes the user to the Docusign platform, which displays an envelope with an embedded web form instance. The user fills out the form fields associated with that user's view of the web form instance. The user submits the web form instance.

   The eSignature envelope is displayed, and the user signs and completes it.
7. If a brand is applied to the web form template or instance and the brand specifies a post-signing URL, the user is routed to that URL. Otherwise, the user remains on the Docusign platform.

## Instance processing: Standalone web form configurations

This diagram illustrates how an end user, your application, and the Docusign platform interact during the processing of a web form instance generated from a standalone web form configuration.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='573' width='1002' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Instance creation via the Web Forms API from a standalone configuration](https://images.ctfassets.net/aj9z008chlq0/3eWedF4S4huVO021U4kg62/f0b867e24424441c8e70a8b4800c1cb2/ProcessFlowStandalone.png?w=1002&h=573&q=50&fm=png)

1. A user takes an action in your application, such as clicking a button, to start filling out a form.
2. Your application launches an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call to create a web form instance for the user to fill out. The request specifies the [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) from which to create the instance by referencing the configuration ID.
3. The response includes a secure, unique URL for the web form instance. See [Web form instance URLs](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) for details.
4. Your application renders the web form instance URL. It can do this by using the Docusign JS client SDK to embed the instance in your application, or by redirecting to the instance URL. See [Render embedded web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/) for details about these options.
5. The user populates the web form instance fields and submits the instance to Docusign.
6. Depending on the method your application used to render the form instance URL in step 4, Docusign issues one of these responses:
   1. If your application used the Docusign JS client SDK to render the form instance, Docusign returns a JavaScript `sessionEnd` [event](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) of type `formConfirmation` to your application when the user submits the web form instance.
   2. If your application redirected the user to the form instance URL, Docusign displays the [thank you page](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=vgq1683244272836.html) defined in the web form configuration.

## Next steps

- See [Plan a Web Forms API integration](https://developers.docusign.com/docs/web-forms-api/plan-integration/) for an overview of the implementation details that you should consider before starting work on your application.
- See the [how-to guides](https://developers.docusign.com/docs/web-forms-api/how-to/) for detailed walkthroughs and code examples.

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
