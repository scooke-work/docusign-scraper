---
title: Embedded signing
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embedded-signing/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Embedding
- Embedding
- Embedded Signing
scraped_at: '2026-06-18T20:28:20Z'
---

# Embedded signing

As an app developer, you can direct users to complete Docusign transactions in either of two ways:

- Remotely, via an email, SMS, or WhatsApp notification that prompts signers to view or sign their documents through the Docusign eSignature web app.
- Directly within your application using embedded signing.

*Embedded signing* (also called the *envelope recipient view*) enables users to view and sign documents directly through your app or website by embedding a Docusign signing session into your application. This is a smoother, more productive flow for signers, compared to leaving your application to receive the signing link via email, SMS, or WhatsApp. Embedded signing should be considered for any web application that generates agreements to be signed and the application is used by the signers themselves. 

To use embedded signing, your app must:

- Authenticate the envelope recipients (the signing session can include additional signer authentication)
- Generate signing URLs
- Present the signing request in the app UI

Building a partner integration? See guidance and best practices for [Envelope signing](https://developers.docusign.com/partner/isv-connector-implementation/#step-4-envelope-signing) as an ISV partner.

Docusign offers multiple options for embedding the signing experience in your application. Each has its own benefits and cautions:

1. **Classic signing session.** [Try it](https://docusign.github.io/app-examples/embedded-signing/#mode=classic-tab)**.** This signing session works with the most [authentication options](https://support.docusign.com/s/articles/What-kinds-of-Recipient-Authentication-are-available) including [Access code](https://developers.docusign.com/docs/esign-rest-api/how-to/require-access-code-recipient/), [KBA](https://developers.docusign.com/docs/esign-rest-api/how-to/knowledge-based-authentication/), and [ID verification](https://developers.docusign.com/docs/esign-rest-api/how-to/id-verification/). This signing session can be used with desktop and mobile browsers.

   You can use iframes, but they are not supported with all types of authentication options or [SBS pen types](https://support.docusign.com/s/articles/Electronic-and-Digital-Signatures). Only full-screen iframes are supported for signers on mobile devices.

   This signing session redirects back to your application when the signer has finished.
2. **Focused view signing session.** [Try it](https://docusign.github.io/app-examples/embedded-signing/#mode=focusedView-tab). Focused view is a technique for embedding an efficient signing session into your application. It includes several benefits:

   - It uses a minimalist UX wrapper that shows only the agreement document and a floating button that takes signers directly to their assigned tabs.
   - You can customize the colors and position of the primary UX button
   - For signers with mobile devices, focused view signing sessions can be used with a small amount of [GUI chrome](https://www.nngroup.com/articles/browser-and-gui-chrome/) from your application.

     ![](data:image/svg+xml;charset=utf-8,%3Csvg height='572' width='901' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

     ![An image comparing the UI impact of standard embedded signing with focused view.](https://images.ctfassets.net/aj9z008chlq0/01gJo2i5nk1ZtLApTJEQ8S/5bae067136411feb9e7f6f9c1c6c24c9/focusViewComparison.jpg?w=901&h=572&fl=progressive&q=50&fm=jpg)

   **Easier integrations**: The [Docusign JS](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/docusign-js-embedded-reference/#introduction) library is used for focused view and the next two views below. Instead of redirecting the browser when the signing session completes, the library raises [DOM events](https://en.wikipedia.org/wiki/DOM_event). This enables a more convenient and productive integration experience. 

   This type of signing session only works within an iframe. The Docusign JS JavaScript library builds the iframe for you in the browser’s DOM.

   **Note:** This type of signing session does not yet support payment tabs, ID verification, nor some types of [standards-based signatures](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/standards-based-signatures/#signature-provider-options) (SBS) pen providers.
3. **Focused view / Click to Agree.** [Try it](https://docusign.github.io/app-examples/embedded-signing/#mode=click2agree-tab)**.** The Click to Agree mode presents a Clickwrap-style agreementto your web app user. [Clickwrap agreements](https://www.docusign.com/blog/what-is-a-clickwrap-agreement) implement a type of electronic signature with a quick, easy-to-use agreement process. To determine which type of eSignature is right for your transaction type, consult with your company’s legal counsel.

   To use Click to Agree mode, do not use any tabs in your envelope’s regular documents, then use the focused view mode of Docusign JS. Focused View/Click to Agree requires the account to have [Document Visibility](https://support.docusign.com/s/document-item?language=en_US&bundleId=gbo1643332197980&topicId=tmi1578456411160.html&_LANG=enus) off.

   Like focused view, Click to Agree can be used with your application’s GUI chrome. You should use no chrome, or only very minimal chrome, if your application is accessed using mobile browsers.

   Also like focused view, Click to Agree uses Docusign JS for easy integrations and uses DOM events to update the calling application.
4. **Classic view with Docusign JS**. [Try it](https://docusign.github.io/app-examples/embedded-signing/#mode=dsjsDefault-tab). The Classic signing session can be combined with the benefits of Docusign JS. This mode offers all the options of classic view. When used with mobile browsers, your application must not provide any GUI chrome.
5. **Mobile applications.** The Docusign [iOS](https://developers.docusign.com/docs/mobile-sdks/ios-sdk/) and [Android](https://developers.docusign.com/docs/mobile-sdks/android-sdk/) SDKs can be used to embed signing sessions within mobile native applications.
6. **Mobile webview integration.** [Webview](https://en.wikipedia.org/wiki/WebView) integration is also supported. Any of the first four options can be used with webviews. You’ll need to enable JavaScript and DOM storage. Configure the webview to enable URLs to be opened within the webview itself.

The embedded signing workflow is usually performed in three steps:

1. **Send an envelope with an embedded recipient.**
   To designate a recipient as embedded, you must set a value (unique within the envelope, but otherwise arbitrary) for their clientUserId property alongside your other recipient properties, such as name and email. The clientUserId is a sender-defined value that identifies the embedded recipient and allows a signing URL to be generated for them.

   A server template recipient can be updated to include a clientUserId when the envelope is sent by using the [Composite templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/composite/) pattern.
2. **Generate the recipient signing URL.**
   To generate the recipient signing URL, call the [EnvelopeViews:createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) method using the same identifying recipient information, including the clientUserId that was sent with the envelope.

   You can only generate recipient signing links for envelopes that are in sent status. **Note:** Because signing links expire after 300 seconds (five minutes) and are one-time use only, you will need to generate a new signing URL each time the recipient wants to access the envelope.
3. **Open the signing session**. For the classic signing session, either redirect the user’s browser to the recipient signing URL or open it within an iframe.

   To use the focused view, focused view/Click to Agree, or classic view with Docusign JS, initialize [Docusign JS](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/docusign-js-embedded-reference/#introduction) and pass the signing URL as a parameter.

For more information on focused view, see [How to request a signature using focused view](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-focused-view/) for a detailed walkthrough of an example focus view implementation or [How to request a signature through your app](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded/) for a code example demonstrating the standard embedded signing flow.

## Next steps

For details on each step and full code examples that demonstrate how to request signatures using embedded signing, see:

- [Embed the Sender and Correct views](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embed-sender-correct-views/)
- [How to request a signature using focused view](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-focused-view/)
- [How to request a signature through your app](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded/) (embedded signing)
- [How to request a signature using a composite template](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-composite-template-embedded/) (embedded signing)
- [How to request a signature through your app (embedded signing) with a CFR Part 11 account](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded-cfrpart11/)
- [How to send an envelope via your app](https://developers.docusign.com/docs/esign-rest-api/how-to/embedded-sending/) (embedded sending)

For a demo of embedded signing and a walkthrough of the sequence of API calls that implement it, see the [Embedded Signing](https://myapicalls.sampleapps.docusign.com/scenario/2) scenario in the MyAPICalls sample app.

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
