---
title: Requesting payment with tabs
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/payment/
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
- Tabs
- Tabs
- Payment
scraped_at: '2026-06-18T21:09:58Z'
---

# Requesting payment with tabs

You can collect payments along with signatures and other information by using the [Docusign Payments](https://www.docusign.com/products/payments) feature. For example, if you manage rental properties, you could use Payments to collect the first and last month’s rent at the same time as the tenant signs the lease.

Docusign Payments uses industry-leading payment processors that are configured to be payment gateways. Therefore, to send a request for payment, you need a payment gateway account with one of our approved payment processors before you can begin. Docusign supports [Stripe](https://stripe.com/), [Braintree](https://www.paypal.com/us/braintree), and [Authorize.net](https://www.authorize.net/). Each of these processors have developer accounts that you can create and test with your Docusign developer account for free.

Configuring a payment gateway can only be done by logging into your Docusign account. To learn how to connect a payment gateway account to your Docusign account, see [Managing Payment Gateways](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=juu1573854950452&topicId=knc1573854895499.html&) in the Docusign Support Center.

## Requesting payment

After you configure your payment gateway, you can initiate a payment request using the eSignature API by creating a [formula tab](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/calculated-fields/) within the tabs section of your envelope JSON with a `paymentDetails` property. This property should include a list of `paymentLineItem` objects, each of which refers to a number tab that contains the value of each item to be purchased. The purpose of these line items is to transmit the total purchase amount to the payment gateway as metadata, enabling your payment to be processed.

For example, if you were creating a payment request for two books, the cost of which is specified in the number tabs with `tabLabel` values of `Hamlet` and `Tempest`, you could use a formula tab to aggregate the cost of both books. The following example demonstrates the envelope JSON for requesting a payment for the books, which are referenced as line items by their `tabLabel` values within the `paymentDetails` object of a `formulaTab`.

```
{
  "documents": [
    {
      "documentBase64": "<base64-encoded PDF document>",
      "documentId": "1",
      "fileExtension": "pdf",
      "name": "payment.pdf"
    }
  ],
  "emailSubject": "Order Some Books",
  "recipients": {
    "signers": [
      {
        "email": "vreader@example.com",
        "name": "Voracious Reader",
        "recipientId": "1",
        "routingOrder": "1",
        "tabs": {
          . . .
          "numberTabs": [
            {
              "value": "10.00",
              "width": 78,
              "required": "true",
              "locked": "true",
              "tabLabel": "Hamlet",
              "documentId": "1",
              "pageNumber": "1",
              "xPosition": "323",
              "yPosition": "134"
            },
            {
              "value": "10.00",
              "width": 78,
              "required": "true",
              "locked": "true",
              "tabLabel": "Tempest",
              "documentId": "1",
              "pageNumber": "1",
              "xPosition": "323",
              "yPosition": "154"
            }
          ],
          "formulaTabs": [
            {
              "required": "true",
              "formula": "([Hamlet] + [Tempest]) * 100",
              "roundDecimalPlaces": "2",
              "paymentDetails": {
                "currencyCode": "USD",
                "lineItems": [
                  {
                    "name": "Hamlet",
                    "description": "The Danish Play",
                    "itemCode": "SHAK1",
                    "amountReference": "Hamlet"
                  },
                  {
                    "name": "Othello",
                    "description": "The one with Caliban in it",
                    "itemCode": "SHAK2",
                    "amountReference": "Tempest"
                  }
                ],
                "gatewayAccountId": "e76668b4-xxxx-xxxx-xxxx-a208d659e490"
              },
              "tabLabel": "Payment1",
              "documentId": "1",
              "pageNumber": "1",
              "xPosition": 300,
              "yPosition": 200
            }
          ]
        }
      }
    ]
  },
  "status": "sent"
}
```

## Checking the status of a payment

You can use the [EnvelopeRecipients:list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/list/) endpoint or equivalent `listRecipients` SDK method to check the status of a payment. When the payment is successful, the `status` property of the `paymentDetails` object is `payment_complete`, as shown in the example JSON response below.

```
{
  "signers": [
    {
      "tabs": {
        . . .
        "numberTabs": [
          {
            "value": "10.00",
            "tabLabel": "Hamlet",
            "documentId": "1",
            "recipientId": "1",
            "pageNumber": "1",
            "xPosition": "323",
            "yPosition": "134"
          },
          {
            "value": "10.00",
            "tabLabel": "Tempest",
            "documentId": "1",
            "recipientId": "1",
            "pageNumber": "1"
          }
        ],
        "formulaTabs": [
          {
            "formula": "([Hamlet] + [Tempest]) * 100",
            "roundDecimalPlaces": "2",
            "paymentDetails": {
              "status": "payment_complete",
              "currencyCode": "USD",
              "lineItems": [
                {
                  "name": "Hamlet",
                  "description": "The Danish Play",
                  "itemCode": "SHAK1",
                  "amountReference": "Hamlet"
                },
                {
                  "name": "Tempest",
                  "description": "The one with Caliban in it",
                  "itemCode": "SHAK2",
                  "amountReference": "Tempest"
                }
              ],
              "gatewayAccountId": "e76668b4-xxxx-xxxx-xxxx-a208d659e490"
            },
            "value": "20",
            "required": "true",
            "locked": "false",
            "tabLabel": "Payment1",
            "documentId": "1",
            "recipientId": "1",
            "pageNumber": "1"
          }
        ]
      },
      "creationReason": "sender",
      "email": "vreader@example.com",
      "name": "Voracious Reader",
      "recipientId": "1",
      "requireIdLookup": "false",
      "status": "completed"
    }
  ],
  . . .
}
```

## Payment notes

- An envelope is not completed until all payments are completed.
- If a Docusign account administrator deletes a payment gateway account connection, Docusign will cancel all in-process envelopes that reference the deleted payment gateway account.
- If the sender voids an envelope, all payment authorizations are canceled.
- If a required recipient refuses to sign, all authorized payments are canceled.
- If a required recipient's payment fails authorization, Docusign attempts to recover by sending the recipient a notification about the failed payment authorization. The recipient then has the opportunity to correct the payment method information.
- Each recipient's payment is authorized separately. Accounts are charged and payment made after all required tabs are completed, and all payments in an envelope for all recipients are authorized.
- Refunds are not supported. Request refunds or payment changes with the payment processor directly.

## Next steps

See [How to send a request for payment](https://developers.docusign.com/docs/esign-rest-api/how-to/request-a-payment/) for a full code example demonstrating the process of sending a payment request.

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
