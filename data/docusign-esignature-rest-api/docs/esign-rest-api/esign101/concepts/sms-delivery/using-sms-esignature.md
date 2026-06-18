---
title: Using SMS and WhatsApp delivery with the eSignature REST API
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/sms-delivery/using-sms-esignature/
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
- SMS delivery
- Using SMS delivery with the eSignature REST API
scraped_at: '2026-06-18T20:28:20Z'
---

# Using SMS and WhatsApp delivery with the eSignature REST API

eSignature REST API 2.1 only

To send an envelope with [SMS and WhatsApp delivery](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/sms-delivery/) enabled for one or more recipients, you can call [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) and pass in data for a new attribute, `secondaryDeliveryMethod`, to the `additionalNotifications` properties of your `signer`, `carbonCopy`, or `certifiedDelivery` recipients, specifying the phone number for each recipient. The required values and object hierarchy for this are shown below:

| Object | Description |
| --- | --- |
| `signers, carbonCopy`, or `certifiedDelivery` | Recipient types that support SMS and WhatsApp delivery are `signer`, `carbonCopy`, or `certifiedDelivery`. |
| `additionalNotifications` | Attribute of the recipient that contains an array of `recipientAdditionalNotification` objects.  The `recipientAdditionalNotification` object has an optional attribute, `secondaryDeliveryMethod`, where you can define the SMS or WhatsApp delivery details for the recipient. |
| `secondaryDeliveryMethod` | Contains the SMS or WhatsApp delivery details for the recipient. Has the following two attributes:    - `phoneNumber`: A `recipientPhoneNumber` object that holds the SMS or WhatsApp delivery phone number. - `secondaryDeliveryMethod`: A string that indicates the delivery method. The supported values are `SMS` and `WhatsApp`. |

For a walkthrough of how to request a signature using SMS or WhatsApp delivery, see [How to request a signature by SMS or WhatsApp delivery](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-sms-whatsapp/).

## JSON example request bodies

The following example JSON shows the structure of the SMS delivery attributes within a `signers` object when the envelope is to be delivered by SMS only:

```
"signers": [
  {
    "name": "Signer Name",
    "recipientId": "1",
    "deliveryMethod": "SMS",
    "phoneNumber": {
      "countryCode": "1",
      "number": "2125551212"
    },
    "tabs": …
```

This example shows how to use WhatsApp delivery in addition to email delivery:

```
"signers": [
  {
    "recipientId": "1",
    "name": "Signer Name",
    "email": "signer@fontara.com", 
    "deliveryMethod": "Email",
    "additionalNotifications":
	[
        {
          "secondaryDeliveryMethod": "WhatsApp",
          "phoneNumber": {
            "countryCode": "1",
            "number": "2125551212"
          }
        }
      ]
    "tabs": ...
```

 **Note:** To use SMS or WhatsApp delivery in the UI, follow the steps documented in the [Multi-Channel Delivery for Notifications: SMS and WhatsApp](https://support.docusign.com/s/document-item?bundleId=gav1643676262430&topicId=kwk1607393003979.html) support guide.

## API usage notes

- Only eSignature REST API v2.1 is supported.
- The `countryCode` attribute is the numeric country code for the phone number.
- Use country code “1” for the US, Canada, and the other countries in the [North American Numbering Plan](https://en.wikipedia.org/wiki/North_American_Numbering_Plan) (NANP).
- Do not include a plus symbol (+) before the numeric country code.
- The `number` attribute can include a leading zero for countries outside of the NANP. Do not include a leading one or zero for the US or other countries in the NANP.
- Use only the characters 0-9 in the `number` attribute. Since users may include spaces, dashes or other characters when they input the number, remove any additional characters before sending the number in an API call.
- The `additionalNotifications` attribute is set to an array. The array must have exactly one element.
- [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/) only supports receiving SMS notification details in JSON format, rather than in XML.

## SDK support

The current [eSignature REST API v2.1 SDKs](https://developers.docusign.com/docs/esign-rest-api/sdks/) for C#, Node.js, Java, PHP, Python, and Ruby include support for the `recipientAdditionalNotification` and `recipientPhoneNumber` objects that enable SMS and WhatsApp delivery.

## Troubleshooting errors

- **"errorCode" : "OPTED\_OUT\_PHONE\_NUMBER\_FOR\_RECIPIENT"**
  This [error code](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/) indicates that the recipient has opted out of Docusign SMS or WhatsApp messages and is unable to receive your SMS or WhatsApp notification.
  - The recipient would need to opt back in before you can send an envelope to them using SMS or WhatsApp delivery. The [Multi-Channel Delivery for Notifications: SMS and WhatsApp](https://support.docusign.com/s/document-item?bundleId=gav1643676262430&topicId=kwk1607393003979.html) guide provides instructions for opting back in to Docusign SMS or WhatsApp messages, which you can share with your signers if they need assistance.
  - You can change the **Delivery** selection to **Email** only rather than have the recipient opt in for SMS or WhatsApp delivery.
- **Other errors**
  Other errors will occur if:
  - The recipient type is not `signer`, `carbonCopy`, or `certifiedDelivery` (Needs to Sign, Needs to View, or Receives a Copy).
  - The recipient is a signing group. Signing groups do not support SMS or WhatsApp delivery.
  - The envelope already has 10 or more SMS or WhatsApp delivery recipients. Ten is the maximum number of SMS and WhatsApp delivery recipients allowed per envelope.

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
