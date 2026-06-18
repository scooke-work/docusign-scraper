---
title: EnvelopeRecipientTabs Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- V2
- V2
- API Reference
- API Reference
- Envelopes
- Envelopes
- Enveloperecipienttabs
scraped_at: '2026-06-18T21:10:48Z'
---

# EnvelopeRecipientTabs Resource

The EnvelopeRecipientTabs resource provides methods that let you
add,
update,
and delete tabs
from an envelope.
Tabs are associated with a specific recipient
in an envelope
and are only used by the recipient types
In Person Signers and Signers.

**On this page**

- [Tab Types](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/#tab-types)
- [Sign Here Tab Alignment](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/#sign-here-tab-alignment)
- [View Tab](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/#view-tab)
- [Requesting Payments](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/#requesting-payments)
- [Using Custom Tabs in Envelopes and Templates](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/#using-custom-tabs-in-envelopes-and-templates)
- [Anchoring Tabs](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/#anchoring-tabs)
- [Automatically Populating Tabs](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/#automatically-populating-tabs)

## Tab Types

Some tabs enable values to be entered by the signer. Those tabs' values can be preset either through the web browser or via the API. Other tab types use information that is already recognized by the DocuSign platform. These tabs cannot have their value updated on a per-tab basis by the API or via the browser. In some cases, the info might be settable using a different technique. For example, the Full name tab uses the signer's name, which is set elsewhere in the request.

Here is the list of tabs and whether you can or cannot set their values in the tab definition:

| Tab Type | Description |
| --- | --- |
| Approve ([`approve`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/approve)) | Allows the recipient to approve documents without placing a signature or initials on the document. If the recipient clicks the tab during the signing process, the recipient is considered to have signed the document. No information is shown on the document of the approval, but it is recorded as a signature in the envelope history. This value **can't** be set. |
| Checkbox ([`checkbox`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/checkbox)) | Allows the recipient to select a yes/no (on/off) option. This value can be set. |
| Company ([`company`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/company)) | Displays the recipient's company name. This value **can't** be set. |
| Date Signed ([`dateSigned`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/dateSigned)) | Displays the date that the recipient signed the document. This value **can't** be set. |
| Date ([`date`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/date)) | Allows the recipient to enter a date. Date tabs are one-line fields that allow date information to be entered in any format. The tooltip for this tab recommends entering the date as MM/DD/YYYY, but this is not enforced. The format entered by the signer is retained. If you need a particular date format enforced, DocuSign recommends using a Text tab with a validation pattern and a validation message to enforce the format. This value can be set. |
| Decline ([`decline`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/decline)) | Allows the recipient the option of declining an envelope. If the recipient clicks the tab during the signing process, the envelope is voided. This value **can't** be set. |
| Email Address ([`emailAddress`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/emailAddress)) | Displays the recipient's email as entered in the recipient information. This value **can't** be set. |
| Email ([`email`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/email)) | Allows the recipient to enter an email address. This is a one-line field that checks that a valid email address is entered. It uses the same parameters as a Text tab, with the validation message and pattern set for email information.  When getting information that includes this tab type, the original value of the tab when the associated envelope was sent is included in the response. This value be set. |
| Envelope ID ([`envelopeId`][envelopeId]) | Displays the envelope ID. Recipients cannot enter or change the information in this tab. This value **can't** be set. |
| First Name ([`firstName`][firstName]) | Displays the recipient's first name. This tab takes the recipient's name as entered in the recipient information, splits it into sections based on spaces and uses the first section as the first name. This value **can't** be set. |
| Formula Tab ([`formulaTab`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/formulaTab)) | The value of a formula tab is calculated from the values of other number or date tabs in the document. When the recipient completes the underlying fields, the formula tab calculates and displays the result. This value can be set.The `formula` property of the tab contains the references to the underlying tabs. See [Calculated Fields](https://support.docusign.com/en/guides/ndse-user-guide-calculated-fields) in the DocuSign Support Center to learn more about formulas. If a formula tab contains a `paymentDetails` property, the tab is considered a payment item. See [Requesting Payments Along with Signatures](https://support.docusign.com/en/guides/requesting-payments-along-with-signatures) in the DocuSign Support Center to learn more about payments. |
| Full Name ([`fullName`][fullName]) | Displays the recipient's full name. This value **can't** be set. |
| Initial Here ([`initialHere`][initialHere]) | Allows the recipient to initial the document. May be optional. This value **can't** be set. |
| Last Name ([`lastName`][lastName]) | Displays the recipient's last name. This tab takes the recipient's name as entered in the recipient information, splits it into sections based on spaces and uses the last section as the last name. This value **can't** be set. |
| List ([`list`][list]) | This tab offers a list of options to choose from. The `listItems` property is used to specify the selectable options. This value can be set, |
| Notarize ([`notarize`][notarize]) | Place this tab on a page to alert Notary recipients that they must take action. Only one notarize tab can appear on a page. This value can be set. |
| Note ([`note`][note]) | Displays additional information, in the form of a note, for the recipient. This value can be set. |
| Number ([`number`][number]) | Allows the recipient to enter numbers and decimal (.) points. This value can be set. |
| Radio Group ([`radioGroup`][radioGroup]) | This group tab is used to place radio buttons on a document. The `radios` property is used to add and place the radio buttons associated with the group. Only one radio button can be selected in a group. This value can be set. |
| Sign Here ([`signHere`][signHere]) | Allows the recipient to sign a document. May be optional. This value **can't** be set.  **Note**: `signHere` tabs can also be used to add a visual representation for an electronic seal in a document. |
| Signer Attachment ([`signerAttachment`][signerAttachment]) | Allows the recipient to attach supporting documents to an envelope. This value **can't** be set. |
| SSN ([`ssn`][ssn]) | A one-line field that allows the recipient to enter a Social Security Number. The SSN can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for SSN information. This value can be set. |
| Text ([`text`][text]) | Allows the recipient to enter any type of text. This value can be set. |
| Title ([`title`][title]) | Displays the recipient's title. This value **can't** be set. |
| View ([`view`][view]) | The View tab is used with the Approve tab to handle supplemental documents. This value can be set. |
| Zip ([`zip`][zip]) | Allows the recipient to enter a ZIP code. The ZIP code can be five digits or nine digits in the ZIP+4 format. The zip code can be typed with or without dashes. It uses the same parameters as a Text tab, with the validation message and pattern set for ZIP code information. This value can be set. |

[envelopeId]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/envelopeId>
[firstName]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/firstName>
[formulaTab](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/formulaTab): <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/formulaTab>
[fullName]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/fullName>
[initialHere]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/initialHere>
[lastName]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/lastName>
[list]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/list>
[notarize]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/notarize>
[note]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/note>
[number]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/number>
[radioGroup]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/radioGroup>
[signerAttachment]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/signerAttachment>
[signHere]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/signHere>
[ssn]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/ssn>
[text]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/text>
[title]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/title>
[view]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/view>
[zip]: <https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/zip>

## Sign Here Tab Alignment

When you provide an x- and y-coordinate for the
sign here tab,
the tab appears 21 points *lower*
than the value you provide for the y-coordinate.
To align the tab as expected,
subtract 21 from the expected y-value.

![Sign Here Tab Alignment](https://developers.docusign.com/img/signherealign.png?v=20260610.1)

## View Tab

The View tab is used on supplemental documents.
To learn more about using the View tab with
supplemental documents, see
[Using Supplemental Documents](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/Envelopes/create/#using-supplemental-documents)
in the [Sending Documents](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/Envelopes/create/#sending-envelopes) section of
the [Envelope: create](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/create/) method.

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| documentId | Yes | String | The document ID number that the tab is placed on. This must refer to an existing Document's ID attribute. |
| pageNumber | Yes | String | Must be set to 1. |
| recipientId | Yes | String | The recipient associated with the tab. Must refer to an existing recipient's ID attribute. |
| required | No | Boolean | If **true**, the recipient is required to select the supplemental document View button during signing. |
| tabLabel | No | String | The label used for the tab. If an empty string is provided for this, an empty sting is used. If no value is provided, the tab type is used as the value. Maximum of 500 characters. |
| templateLocked | No | Boolean | Optional. Used only when working with template tabs. If **true**, the attributes of the tab cannot be changed by the sender. |
| templateRequired | No | Boolean | Optional. Used only when working with template tabs. If **true**, the tab cannot be removed by the sender. |
| xPosition | Yes | String | Required, but can be 0. |
| yPosition | Yes | String | Required, but can be 0. |

## Requesting Payments

The Payments feature of the DocuSign eSignature REST API
lets you collect payments
along with signatures and other information.

To send a request for payment
and collect payments,
you need a payment gateway account,
which is the destination for the payments.
Create a payment account
with a supported payment gateway,
and then connect the payment gateway account
to your DocuSign account.
To learn how to connect a payment gateway account
to your DocuSign account
see [Managing Payment Gateways](https://support.docusign.com/en/guides/managing-payment-gateways)
in the DocuSign Support Center.
You must connect and manage payment gateway accounts manually
through the DocuSign Admin console
and through your chosen payment gateway.
There is no public API
for connecting payment gateway accounts
to DocuSign accounts
or for managing payment gateway accounts.

Currently
[Stripe](https://stripe.com/),
[Braintree](https://www.braintreepayments.com/), and
[Authorize.net](https://www.authorize.net/)
are the supported payment gateways.

### How Payments Work

To make a request for payment,
use a [`formulaTab`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/formulaTab)
that has a
[`paymentDetails`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/paymentDetails) object.
This object includes
a list of [`paymentLineItem`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/paymentLineItem) objects.
Each line item refers to a [`number`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/number) tab
that contains the value of the each item.
The purpose of the line items
is to transmit them to the payment gateway
as metadata, so that you can use the information
in the payment processor.

**Note**: If the fileExtension parameter is not added in an API call, only base64 converted pdf files will be accepted.
Any attempt to send a non pdf file without using fileExtension results in an error.

This is an example request for two books.
Each book is specified in the `number` tabs
labeled "Hamlet" and "Tempest".
The books are referenced as line items
by their tab labels
within the `paymentDetails` object
of a `formula` tab.
The formula of the `formula` tab
add the values of the same two `number` tabs.

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

Use the
[EnvelopeRecipients: list](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipients/list/) method
to check the status of a payment.
When the payment is successful,
the `status` property of
the [`paymentDetails`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Envelopes/EnvelopeRecipientTabs/create/#/definitions/paymentDetails) object
is `payment_complete`.

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
            "yPosition": "134",
          },
          {
            "value": "10.00",
            "tabLabel": "Tempest",
            "documentId": "1",
            "recipientId": "1",
            "pageNumber": "1",
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
            "pageNumber": "1",
          }
        ]
      },
      "creationReason": "sender",
      "email": "vreader@example.com",
      "name": "Voracious Reader",
      "recipientId": "1",
      "requireIdLookup": "false",
      "status": "completed",
    }
  ],
  . . .
}
```

### Some Things to Keep in Mind About Payments

- An envelope is not completed until all payments are completed.
- If a DocuSign account Administrator
  deletes a payment gateway account connection
  DocuSign cancels all in-process envelopes
  that reference the deleted payment gateway account.
- If the sender voids an envelope,
  all payment authorizations are canceled.
- If a required recipient refuses to sign,
  all authorized payments are canceled.
- If a required recipient's payment fails authorization,
  DocuSign attempts to recover
  by sending the recipient
  notification about the failed payment authorization.
  The recipient has the opportunity
  to correct the payment method information.
- Each recipient's payment is authorized separately.
  Accounts are charged and payment made
  after all required tabs are completed,
  and all payments in an envelope for all recipients are authorized.
- Refunds are not supported.
  Conduct refunds or payment changes
  with the payment gateway separately from DocuSign.
- At this time, DocuSign does not charge a per-transaction fee.

## Using Custom Tabs in Envelopes and Templates

Custom Tabs can be added to envelopes and templates
by setting the `customTabId` property
when creating an envelope or template recipient
or when adding a new tab for an existing recipient.
The custom tab must be added as the correct tab type.
For example if the custom tab type is text, it cannot be used as a number tab.

When the `customTabId` property is set,
the new tab inherits all the custom tab properties.
Required information that is not included in the custom tab,
such as document ID and page ID, must be included when adding the tab.
If the custom tab does not have anchor settings, the X and Y positions must be included.

After the tab is created,
it is treated as any other tab for updating or deleting.

## Anchoring Tabs

The tab anchoring option
allows you to send documents for signature
that do not have a fixed layout or format.
In these documents you might not know
the absolute location of the tabs
when you design your API client application because the tabs must move with text.
As an alternative to sending X and Y coordinates for tabs,
the DocuSign Service can derive an anchor location for the tab
by correlating anchor information to data within the document.

When the DocuSign Service receives a request that contains tabs
with anchor information,
it searches the document for instances of the `anchorString` property.
When found,
it places a tab of the specified type for the designated recipient.
Tab positions are established by setting offsets for the tab.

When you apply tabs to the document,
DocuSign does not remove or replace the text in the `anchorString` property. You can hide codified anchors by using the same font color as the background of the document. So the anchor can be used by DocuSign processes and it will not be visible on the document.

To use an anchoring option:

1. Identify the location in the document by text string. You can use a pre-existing text string or add a new one.
   For best performance DocuSign recommends using single word anchor strings when possible, especially when there are a large number of pages in the envelope.
   For example, you might want to add a Sign Here tab to the "Borrower's Signature" lines in a document, but that phrase might occur in places in the document where you don't want to tab to appear. In this case, you could add the text "BorrowerSignHere" in white font color (so that isn't visible in the document) to all the places you want Sign Here tabs to appear and use "BorrowerSignHere" as the anchor string.
2. Reference the anchor through the `anchorString` property of the tab.
3. Determine the offset from the anchor string location to where the tab should be placed.

Setting a positive value in the `anchorXOffset` property moves the tab right on the page and positive values in the `anchorYoffset` prove moves the tab down the page. The `anchorUnits` property specifies the units used for the offsets.
For Sign Here and Initial Here tabs the bottom-left of the anchor string is equivalent to position (0,0), and the bottom-left of the tab graphic is placed relative to that.
For all other tabs the bottom-left of the anchor string is equivalent to position (0,0), and the top-left of the tab graphic is placed relative to that.
DocuSign does not currently provide tools to derive the offset values. Determination of the proper offset will likely require some trial-and-error.

### Rules for working with anchor tags

When anchor tabs are used, all documents in the envelope are searched for the `anchorString` property.

- You set the text of the anchor string in the `anchorString` property. DocuSign tabs are created for each instance of the `anchorString` property within the document, so special care must be taken to establish unique anchor strings that do not result in unintentional tabs.
- You cannot use the same anchored tab for different recipients for the same document.
- The DocuSign system cannot search for text that is embedded in an image when checking for anchor strings.
- X or Y offsets supplied for a tab apply to all instances of the tab in the document. To use different offsets at different locations in the document for the same recipient, create multiple, unique anchor tabs.
- If the Y offset value of an anchor string would force a tab outside of the page boundaries, the tag is placed at the page boundary. If the X offset value places a tab outside of the page boundaries, the error message `Invalid_User_Offset` is sent. The error message includes the X offset that resulted in the error.
- The system does not support an anchor string embedded in the form of a PDF X-object in the document.
- The system does not re-flow the text that surrounds the anchor tabs. It is the responsibility of the document author to provide sufficient white space to contain the potential width of the ultimate tab value.

### Tips and Tricks

The following are tips for effective use of anchor tags:

- In order to avoid unintentional conflicts between text contained in an `anchorString` property and the text that naturally exists in documents, establish a codified syntax for the anchor string text that is unlikely to appear elsewhere in a document.
- Develop an extensible and consistent syntax that can be used across multiple document types.
- Especially for documents that have variable numbers of tabs or signers, author the source document to include hidden anchor tabs for all potential signers/permutations. Then, control the tabs that are actually placed by including/excluding the anchor tabs in the request. This approach allows a single document to be used for all use cases instead of maintaining separate documents for each scenario.

## Automatically Populating Tabs

If you want similar tab types
to automatically populate with the same data,
you must follow these guidelines:

- Each `tabLabel` entry must have the characters
  `\\*` in front of the label.
  If you omit the `\\*` prefix,
  only the first occurrence of the tab is populated.

  When automatically populating tabs,
  the `tabLabel` must not contain any spaces.
  In the JSON example below,
  the Text tabs properties `StudentLastName` and `StudentFirstName`
  will be auto-populated as specified ("Doe" and "John")
  each place they appear throughout the envelope.

  ```
  "tabs": {
    "textTabs": [
    {
      "tabLabel": "\\*StudentLastName",
      "value": "Doe"
    },
    {
      "tabLabel": "\\*StudentFirstName",
      "value": "John"
    }]
  }
  ```
- Each occurrence of the tab must have identical properties.

  For example, suppose there are two Text tabs in a document,
  each with `tabLabel` set to `Name`.
  If one tab has the `bold` property set to **true**,
  and the other has the `bold` property set to **false**,
  only the first one will be populated.
  In order to automatically populate both occurrences
  of the `Name` Text tabs,
  the `bold` property must be set to the same value for both tabs.

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/create/) | POST  ```  /restapi/v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs ```  Adds tabs for a recipient. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/delete/) | DEL  ```  /restapi/v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs ```  Deletes the tabs associated with a recipient. |
| [list](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/list/) | GET  ```  /restapi/v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs ```  Gets the tabs information for a signer or sign-in-person recipient in an envelope. |
| [update](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/enveloperecipienttabs/update/) | PUT  ```  /restapi/v2/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs ```  Updates the tabs for a recipient. |

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
