---
title: SMS and WhatsApp delivery
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/sms-delivery/
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
- SMS delivery
scraped_at: '2026-06-18T21:09:59Z'
---

# SMS and WhatsApp delivery

eSignature REST API 2.1 only

You can send signing requests and agreement notifications directly to a recipient’s mobile device. This feature enables you to send [envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) via SMS or WhatsApp, either by these methods alone or along with email. A phone number is required for every signer, carbon copy recipient, or certified delivery recipient when creating an envelope. Each notification contains direct, clickable links to the document delivered to the recipient.You can also use the API to update your existing recipients. If you have recipients who have been previously set for email delivery via their template roles, you can set them to use SMS or WhatsApp delivery instead when you send your envelope.

SMS and WhatsApp delivery are available to all customers globally, and notification messages can be sent to any phone numbers other than those from [countries sanctioned under US laws](https://home.treasury.gov/policy-issues/financial-sanctions/sanctions-programs-and-country-information).

## When to use SMS or WhatsApp delivery

One of the fastest ways to connect with other people across the world is through their mobile devices. SMS and WhatsApp delivery helps you guide recipients through the signing process directly via their mobile devices, and is recommended to use in remote email eSignature scenarios where:

- Increasing transaction speed is important
- You need to reach consumers anywhere in the world
- Your recipients may not have access to or want to use email

## Enable SMS or WhatsApp for your account

To enable SMS or WhatsApp delivery in your developer account, open a support case with [Docusign Support](https://support.docusign.com/s/contactSupport) if you have a production account. If you don't have one, visit the [Docusign Support](https://support.docusign.com/s/contactSupport) page, select **Docusign API Integration Support** under **More Support Options**, and submit details using the form.

For production accounts, SMS or WhatsApp delivery is available as a separate add-on to [Standard](https://www.docusign.com/products-and-pricing) or higher Docusign eSignature direct plans. Contact [Docusign Sales](https://www.docusign.com/contact-sales) to inquire about availability for your account.

For partners, SMS and WhatsApp delivery are freely available in the developer (demo) environment to customers that are part of the EAP program. For production environments, you can request a limited free trial before accruing charges. Please reach out to your account team for more information.

## Use SMS or WhatsApp delivery

You can deliver envelope notifications via SMS or WhatsApp using the UI or the API:

- In the UI, the option to send via SMS or WhatsApp appears in the **Delivery** control for each recipient you define. See [Send an Envelope with SMS or WhatsApp Delivery﻿](https://support.docusign.com/s/document-item?rsc_301=&bundleId=gav1643676262430&topicId=krj1607396924116.html) for details.
- Using the API, when creating your envelope definition, you need to include a phone number and a secondary delivery method of SMS or WhatsApp in the signer definition `additionalNotifications` fields. See [How to request a signature by SMS or WhatsApp delivery](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-sms-whatsapp/) for details and full code examples.

## Best practices

### Optimize for mobile devices

When you use SMS or WhatsApp delivery, your envelope will probably be signed using a mobile device. Test your envelope and template formats with mobile devices and use envelope options to provide the best signing experience for your signers. For example, turn on [responsive signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/responsive/) and investigate using [smart sections](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=gbo1643332197980&topicId=qlx1578456478178.html&_LANG=enus).

### SMS-only or WhatsApp-only delivery

You should use SMS-only or WhatsApp-only delivery (without email) when:

- Your end users don’t have an email address.
- A transaction should happen synchronously with the end user and email is not readily available.

For example, SMS-only delivery and WhatsApp-only delivery are ideal for situations where customers must fill out forms when bringing their own devices or for walking them through signing an agreement while on a phone call.

## Next steps

- See [SMS and WhatsApp delivery notes and limitations](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/sms-delivery/sms-delivery-limitations/) for information that can be important for your integration.
- See [How to request a signature by SMS or WhatsApp delivery](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-sms-whatsapp/) for code examples for delivering an envelope to each recipient via a single method.
- See [How to request a signature by multiple delivery methods](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-multiple-delivery-methods/) for code examples for delivering an envelope to each recipient via multiple methods.
- See [Send an Envelope with SMS or WhatsApp Delivery﻿](https://support.docusign.com/s/document-item?rsc_301=&bundleId=gav1643676262430&topicId=krj1607396924116.html) for details on how to send an envelope with SMS delivery in the UI.

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
