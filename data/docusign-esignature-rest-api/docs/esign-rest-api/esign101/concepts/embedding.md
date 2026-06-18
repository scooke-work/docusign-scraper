---
title: Embedding Docusign eSignature into your app
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/
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
scraped_at: '2026-06-18T20:28:19Z'
---

# Embedding Docusign eSignature into your app

An eSignature agreement flow includes multiple user experience options (UXs) designed for different use cases. For most user experiences, you have two options for integrating the experience into your app:

- **Use the API:** Your app can provide its own user experience and call the eSignature API to implement your app’s e-signature functionality. For example, you can add a **Send for Signature** button to your app. Your software would then call the eSignature API to create and send an envelope by combining a template with your app’s current document and signer’s information. You should always investigate this option when you’re designing your app.
  - Uses your own app’s user experience, and so typically provides a smoother experience for your users.
  - Is often easy to provide and implement.
- **Embed the Docusign user experience:** You can embed parts of the Docusign eSignature signing experience into your application. In other cases, your app can redirect to Docusign and, afterwards, Docusign will redirect the user’s browser back to your application.
  - Uses your app’s user experience to initiate the signing process and enable your users to send or sign documents directly within your app.
  - Avoids the need to switch contexts to email.

## Embedding options for eSignature

### Preparing and sending the envelope

This step is often the easiest to implement using your own user experience and the eSignature API. Gather the information for the signers and other recipients, your templates, documents, and other information for the envelope, then send the envelope using the API.  **Tagging documents**

When creating the envelope, your documents should be *tagged* with text that Docusign can use as identifiers to place the **Sign Here**, **Text**, **Payment**, and other types of [Tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) (also known as fields) with which the recipients interact. This recommended type of tab placement is known as [Auto-place (anchor tagging)](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/auto-place/). [Fixed positioning](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/fixed/) placement for tabs is also supported.

One advantage of using templates to create your envelope is that, if a template definition can be used to tag the documents, the documents will not need to be tagged for each envelope.

If the documents for an individual envelope need to be manually tagged, you can embed the **Sender View** into your application. For more information, see [Embed the Sender and Correct views](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embed-sender-correct-views/).

### Correcting the envelope

You can correct an envelope by making changes to it after it has been sent. When you design your process flow, correcting an envelope should never be a standard part of your process. Envelopes should only be corrected as part of an exception process. Envelopes cannot be corrected after they’ve reached the completed state.

Sometimes, however, you may need to change an envelope’s recipients, documents, tabs, or other data after the envelope has already been sent and possibly signed by some recipients. For these cases, you can correct envelopes programmatically using the API, or you can [Embed the Sender and Correct views](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embed-sender-correct-views/).

### Signing

There are two types of recipient signers:

- **Remote Signers**. These signers are notified by email, SMS, or WhatsApp to open the Docusign web app and sign. This is the default mode.
- **Embedded Signers**. These signers use your application and the **Embedded Recipient View** to sign from within your application. This is the recommended choice when the signer is already using your application via a browser or mobile app. See [Embedded signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embedded-signing/) for an example.

Note that the API cannot be used to sign a document. It must be signed directly by recipients.

## Template editing

Depending on your application’s use cases, you can use the [TemplateViews : createEdit](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templateviews/createedit/) to enable your application’s users to update templates from within your application.

## Next steps

For details on each step and full example code that demonstrates how to request signatures using embedded signing, see:

- [Embed the Sender and Correct views](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embed-sender-correct-views/)
- [Embedded signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embedded-signing/)
- [How to request a signature using focused view](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-focused-view/)
- [How to request a signature through your app](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded/) (embedded signing)
- [How to request a signature using a composite template](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-composite-template-embedded/) (embedded signing)
- [How to request a signature through your app (embedded signing) with a CFR Part 11 account](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded-cfrpart11/)
- [How to send an envelope via your app](https://developers.docusign.com/docs/esign-rest-api/how-to/embedded-sending/) (embedded sending)
- [How to embed a workflow in your web application](https://developers.docusign.com/docs/maestro-api/maestro101/embed-workflow/)

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
