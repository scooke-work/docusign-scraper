---
title: Standards-based signatures
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/standards-based-signatures/
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
- Standards Based Signatures
scraped_at: '2026-06-18T20:28:08Z'
---

# Standards-based signatures

Docusign enables document signers to use [electronic](https://www.docusign.com/products/electronic-signature) or [digital](https://www.docusign.com/how-it-works/electronic-signature/digital-signature) signatures of the following types within a single envelope by using standards-based signatures (SBS):

- Electronic signatures
- [Advanced Electric Signature (AES)](https://en.wikipedia.org/wiki/Advanced_electronic_signature) using certificates from Docusign or from your organization
- [Qualified Electronic Signature (QES)](https://en.wikipedia.org/wiki/Qualified_electronic_signature) from government-certified Qualified Trust Service Providers (QTSPs)

## Add a digital signature in your envelope

To use a digital signature in your envelope:

1. Determine the signature providers that your signers will use from the [signature provider options](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/standards-based-signatures/#signature-provider-options) list. See [Use Digital Certificate-Based Signatures for More Secure Agreements](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=xww1594245808169&topicId=hxl1594246065723.html&_LANG=enus) for a list of additional TSPs that are available.
2. Include a value for the `recipientSignatureProviders` parameter for at least one signer defined in your [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) method call. This parameter specifies the digital signature provider(s) available for the recipient to use, and any options associated with the provider(s).

   The definition of the `recipientSignatureProviders` object is:

| Name/Type | Description |
| --- | --- |
| `recipientSignatureProviders` `[recipientSignatureProvider]` | Each `recipientSignatureProvider` object in the array defines one signature provider that the recipient may choose to use, along with its options.  The definitions of the signature provider component objects are available in the API Reference:  - [recipientSignatureProvider](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/create/#definitions_recipientsignatureprovider) - [recipientSignatureProviderOptions](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/create/#definitions_recipientsignatureprovideroptions) |

The associated example shows two EU AES recipients. One uses SMS authentication, the other uses a one-time password (OTP) for authentication.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

{

"signers": [

{

"routingOrder": 1,

"name": "Sue Collins",

"email": "sue@example.com",

"deliveryMethod": "email",

"recipientId": "1",

"recipientSignatureProviders": [

{

"signatureProviderName":

"UniversalSignaturePen\_OpenTrust

\_Hash\_TSP",

"signatureProviderOptions": {

"oneTimePassword": "

{YOUR\_PASSWORD}"

}

}

]

},

## AES signatures

Advanced electronic signatures require signers to use digital certificates to verify their identity. When a signer receives the envelope to sign, the sender can specify if they would like for the signer to sign using an AES certificate from Docusign or by using a certificate owned by the signer, such as a [smart card](https://en.wikipedia.org/wiki/Smart_card). The signer will receive the envelope and sign as normal while having the certificate applied in the sender’s desired form.

## QES signatures

QES signatures use a government-authorized entity known as a [Qualified Trust Service Provider](https://support.docusign.com/s/document-item?language=en_US&bundleId=xww1594245808169&topicId=def1594657272301.html&_LANG=enus) (QTSP) to:

- verify the identity of the signer, either face-to-face or through a video chat, with a valid identification document
- validate the identity of the signer at the time of signature through signer-held or cloud-based certificates

### Provisioning QES Signatures for your account

To enable QES Signatures for your developer account, contact [Docusign Support](https://support.docusign.com/s/contactSupport). To enable it for your production account, contact [Sales](https://www.docusign.com/contact-sales).

### Send an envelope with a QES

To create an envelope that includes a qualified electronic signature, you must provide the following additional values in your envelope definition:

- `recipientSignatureProviders`: The parent object required to define the electronic signature parameters.
- `signatureProviderName`: The name of the electronic signature provider for the signer to use. For details, see the [signature provider options](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/standards-based-signatures/#signature-provider-options) or list the types available on your account by using the [AccountSignatureProviders:list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountsignatureproviders/list/) method.

The associated example JSON envelope definition demonstrates the data required for adding a QES. It uses [IDNow](https://www.idnow.io/products/idnow-videoident/), an identity verification service that uses the signer’s webcam and microphone to verify their identity. If you would like to use this code along with one of the Docusign SDKs, you can use our [JSON to SDK tool](https://jsontosdk.dshackathon.com/) to transform the call into C#, Java, Node.js, PHP, Python, Ruby, or VB.NET.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

{

"emailSubject": "Please sign the attached

document",

"status": "sent",

"documents": [

{

"documentId": "1",

"name": "TestDocument.docx",

"fileExtension": "docx",

"documentBase64": "documentBase64String"

}

],

"recipients": {

"signers": [

{

"email": "email@email.com",

"name": "Tester: X-MANUALTEST",

"recipientId": "1",

"recipientSignatureProviders": [

{

### IDV for EU Qualified Electronic Signatures

You can also use EU Qualified Electronic Signature with [ID verification](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/#idv) (IDV) to verify the identity of an envelope recipient, instead of or in addition to other types of IDV. This method of generating qualified electronic signatures uses IDV to verify the recipient’s identity and complies with the European [eIDAS](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation) (electronic Identification, Authentication and Trust Services) regulation.

This eIDAS regulation requires an equivalent of face-to-face identity verification for signers to issue qualified signatures; Docusign uses a certified remote identification provider to comply with these requirements. The provider offers a self-serve identification process, meaning signers can complete the process without interacting with a live agent. A back-office agent will review the transaction afterward, typically within 3–5 minutes. See [Verification of Government-Issued IDs for European Qualified Signatures](https://support.docusign.com/s/document-item?bundleId=ced1643229641057&topicId=vke1672930715877.html) for details.

To use EU QES for IDV:

- Your plan needs to support IDV For QES.
- You must have an admin account to register an account and create a custom Connect event.

Docusign provides a default EU QES for IDV configuration by default, or you can create your own in eSignature Admin by opening the [Identity Verification](https://apps-d.docusign.com/admin/identity-verification) page, selecting **Add Verification** at the upper right of the screen, then choosing **Docusign ID Verification for EU Qualified** and checking your desired verification options. See [Add Identity Verification for EU Qualified Electronic Signatures](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=pyx1678128186236.html&_LANG=enus) for details.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='276' width='512' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image of the eSignature admin Identity Verification page UI showing the configurable options for a IDV for EU Qualified workflow.](https://images.ctfassets.net/aj9z008chlq0/78WyVtPXHmkNob6C5gMyRW/848006ab5124be1ee17c9b70e381d8ca/IDV.png?w=512&h=276&q=50&fm=png)

When creating your envelope, you can use IDV for EU QES by specifying a `workflowId` value for one of your defined EU QES for IDV workflows. You can find the `workflowId` for a workflow by opening the [Identity Verification](https://apps-d.docusign.com/admin/identity-verification) page, scrolling to find your IDV for EU QES workflow in the list, then selecting **Edit**, or by calling the [IdentityVerifications:list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/identityverifications/list/) API endpoint. The Configuration ID for API integrations is the `workflowId` that you can use to implement the workflow for your envelopes. 

A default IDV for EU QES workflow is provided with the feature. You can use this workflow as an example implementation and the basis for creating your own IDV for EU QES workflows. The ID of this default workflow is `5eedeb39-c6a2-48d9-b789-b5459c2ff9bb`.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='287' width='512' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image of the configurable options for an IDV for QES custom workflow.](https://images.ctfassets.net/aj9z008chlq0/IYaq5waU4OdnGDxFC9KIi/bbf382867031b68918f4d89e9c244959/EditIDVforQESCustom.png?w=512&h=287&q=50&fm=png)

After the envelope and recipient view have been created, the IDV for EU QES workflow begins. The recipient performs ID checks, including ID capture, facial recognition, and liveness tests. When the recipient finishes all of their challenges, Docusign sends an `identity-verification-pending` Connect message. At this point the signer must wait until the final review is completed.

When the ID is verified, Docusign sends an `identity-verification-completed` Connect message indicating that validation is completed. If the verification was successful, then your app can create the recipient view and show agreement documents or, if unsuccessful, retry.

1

2

3

4

5

6

7

8

9

10

11

12

13

#!/usr/bin/env node

// DocuSign API Request Builder example. Generated:

Thu, 29 Feb 2024 15:25:49 GMT

// DocuSign Ⓒ 2024. MIT License -- https://

opensource.org/licenses/MIT

'use strict';

const fse = require('fs-extra')

, path = require('path')

, docusign = require('docusign-esign')

, baseUri = 'https://demo.docusign.net/' //

demo base url

// Note: the accessToken is for testing and

is temporary. It is only good for 8 hours

from the time you

// authenticated with API Request Builder. In

production, use an OAuth flow to obtain

access tokens.

, accessToken = '{YOUR\_ACCOUNT\_ID}'

, accountId = '{YOUR\_ACCOUNT\_ID}'

, documentDirectory = '.'; // The directory

## Testing digital signatures

Standards-based signatures are not included with default developer accounts. To test with standards-based signatures, ask your Docusign technical contact, or Docusign Customer Service, to add the SBS feature to your account. To test with a TSP, you will also need a test account from them. Discuss your needs with your Docusign Account Manager.
> **Note:** By design, digital signatures created in your developer account will verify with warnings that the signer's identity cannot be trusted. Digital signatures created on Docusign production systems will not have this issue. See the [Standards-based signatures](https://support.docusign.com/s/articles/Standards-Based-Signature-The-Digital-ID-used-to-Certify-Ubiquitize-Sign-this-document-in-Demo) support page for details.

## Listing an account's signature providers

You can list your account's enabled signature providers using the [AccountSignatureProviders:list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountsignatureproviders/list/) method. Using this method is optional; you can also hardcode signature provider names.

## Signature provider options

### Electronic signature

Electronic signatures do not use digital certificates. These are the default type of signatures from Docusign.

- **API signatureProviderName:** `UniversalSignaturePen_ImageOnly`
- **Required options:** none

### Email signature

Docusign-generated generic, "on-the-fly" digital signatures that include a certificate.

- **API signatureProviderName:** `ds_email`
- **Required options:** none

### **Email signature for FAA compliant customers**

A version of the standard **ds\_email** signature provider that is compliant with FAA regulations. Use this variant instead of **ds\_email** if your digitally signed documents must be FAA compliant.

You can contact [Developer support](https://developers.docusign.com/support/) to enable **ds\_email\_shield** for your account, if required for your business.

- **API signatureProviderName:** ds\_email\_shield
- **Required options:** none

### EU Advanced signature

Docusign-generated, eIDAS AES compliant signatures. See the [Standards-based signatures](https://support.docusign.com/s/articles/Standards-Based-Signature-The-Digital-ID-used-to-Certify-Ubiquitize-Sign-this-document-in-Demo) support page for details.

- **API signatureProviderName:** `UniversalSignaturePen_OpenTrust_Hash_TSP`
- **Required options:** SMS or one-time password

> **Note:** If you are using Docusign EU Advanced signatures and embedded signing, in the event the recipient fails the Access Code or SMS OTP when the digital signature is applied, you are redirected to the ReturnURL with the query parameter `?event=access_code_failed.`

- **Limitation:** The recipient [name](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/) must not contain the following characters: ^ : \ @ + < >

### ICP-Brasil

ICP-Brasil is the official Brazilian public key infrastructure. It provides digital certificates for virtual identification of Brazilian citizens. Find more information at  [Brazil's National Institute for Information Technology website](https://www.gov.br/iti/pt-br).

- **API signatureProviderName:** `UniversalSignaturePen_ICP_SmartCard_TSP`
- **Required options:** none

### IDnow

EU Qualified electronic signatures from [IDNow](https://www.idnow.io/products/idnow-videoident/). IDnow is a leading European online video-identification service based in Germany.

- **API signatureProviderName:** `docusign_eu_qualified_idnow_tsp`
- **Required options:** none

### itAgile

Qualified electronic signatures using [itAgile](http://www.itagile.it/docusign/) EU Qualified Certificates.

- **API signatureProviderName:** `UniversalSignaturePen_ItAgile_TSP`
- **Required options:** none

### US PIV Card

The US Federal government specifies [Personal Identity Verification](https://csrc.nist.gov/projects/piv) (PIV) smart card requirements for Federal employees and contractors. This provider enables PIV card holders to digitally sign documents.

- **API production signatureProviderName:** `UniversalSignaturePen_PIV_SmartCard_TSP`
- **API test signatureProviderName:** `UniversalSignaturePen_PIV_Test_TSP`
- **Required options:** none

## Next steps

- [Docusign eSignature types](https://www.docusign.com/blog/developers/docusign-esignature-types)

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
