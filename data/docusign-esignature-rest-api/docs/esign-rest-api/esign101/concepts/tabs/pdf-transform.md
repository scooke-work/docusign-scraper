---
title: PDF form field transformation
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/pdf-transform/
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
- Pdf Transform
scraped_at: '2026-06-18T20:28:18Z'
---

# PDF form field transformation

*PDF form field transformation* enables you to transform PDF form fields automatically into Docusign tabs, carrying over all of their existing values. The locations of the created tabs will match the locations of the fields from which they were generated.

To transform PDF form fields into Docusign tabs, you need to set the `transformPdfFields` property on the documents whose fields you want to transform.

PDF fields are converted to Docusign tab types based on the Adobe name of the original field, as shown in the table below:

| Original PDF field | Converted Docusign tab |
| --- | --- |
| Adobe name contains DocusignSignHere or eSignSignHere | Sign here (`signhere`) |
| Adobe name contains DocusignSignHereOptional or eSignSignHereOptional | Optional Sign here (`signhere`)   **Note:** To transform an Optional Sign Here field, you must include an `"optional":"true"` value in the tab definition, as shown in [this example](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/pdf-transform/#codeExample). |
| Adobe name contains DocusignInitialHere or eSignInitialHere | Initial here (`initialHere`) |
| Adobe name contains DocusignInitialHereOptional or eSignInitialHereOptional | Optional Initial Here (`initialHere`)   **Note:** To transform an Optional Initial Here field, you must include an `"optional":"true"` value in the tab definition, as shown in [this example](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/pdf-transform/#codeExample). |
| Adobe name contains DocusignEnvelopeID or eSignEnvelopeID | Envelope ID (`envelopeId`) |
| Adobe name contains DocusignCompany or eSignCompany | Company (`company`) |
| Adobe name contains DocusignDateSigned or eSignDateSigned | Date signed (`dateSigned`) |
| Adobe name contains DocusignTitle or eSignTitle | Title (`title`) |
| Adobe name contains DocusignFullNameor eSignFullName | Full name (`fullName`) |
| Adobe name contains DocusignLastName or eSignLastName | LastName |
| Adobe name contains DocusignFirstName or eSignFirstName | FirstName |
| Adobe name contains DocusignEmailAddress or eSignEmailAddress | EmailAddress |
| Adobe name contains DocusignNumber or eSignNumber | Number |
| Adobe name contains DocusignDate or eSignDate | Date |
| Adobe name contains DocusignSSN or eSignSSN | SSN |
| Adobe name contains DocusignZIP5 or eSignZIP5 | ZIP5 |
| Adobe name contains DocusignZIP5DASH4 or eSignZIP5DASH4 | ZIP5DASH4 |
| Adobe name contains DocusignNote or eSignNote | Note |
| Adobe name contains DocusignList or eSignList | List |
| Adobe name contains DocusignCheckbox or eSignCheckbox | Checkbox |
| Adobe name contains DocusignRadio or eSignRadio | Radio |
| Adobe name contains DocusignApprove or eSignApprove | Approve |
| Adobe name contains DocusignDecline or eSignDecline | Decline |
| Adobe name contains DocusignView or eSignView | View |
| Adobe name contains DocusignSignerAttachment or eSignSignerAttachment | Required Signer attachment (signerAttachment) |
| Other PDF field names | Any other name will default to a Docusign data (`text`) field |
| Adobe name contains DocusignSignerAttachmentOptional or eSignSignerAttachmentOptional | Optional Signer attachment (`signerAttachment`)  **Note:** To transform an optional signer attachment field, you must include an `"optional":"true"` value in the tab definition, as shown in [this example](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/pdf-transform/#codeExample). |

Docusign will not transform PDF form fields that have the text `DocusignIgnoreTransform` or `eSignIgnoreTransform` as part of the name of the PDF form field.

When you convert PDF form fields to Docusign tabs, each tab in the document will be assigned to a single recipient specified by the `assignTabsToRecipientId` document property (or defaulting to 1). Because the tabs are created dynamically, they cannot be mapped individually to specific signers.

**Important**: The names of the PDF fields must match the (case-sensitive) `tabLabel` values of the Docusign tabs to which you wish to transfer their values. For example, to convert a PDF form field to a Docusign List tab, the name of the form field must include
`eSignList` or `DocusignList`.

If the PDF field names match the Docusign `tabLabel`, you can set the `transformPdfFields` property to true for a given document in the documents array like this:

> ```
> {
>   "status": "sent",
>   "emailSubject": "PDF Transform Example 2",
>   "recipients": {
>     "signers": [
>       {
>         "email": "sally@email.com",
>         "name": "Sally Dough",
>         "recipientId": "1",
>         "tabs": {
>           "initialHereTabs": [
>             {
>               "tabLabel": "DocusignInitialHere1"
>             },
>             {
>               "tabLabel": "DocusignInitialHereOptional1",
>               "optional": "true"
>             }
>           ]
>         }
>       }
>     ]
>   },
>   "documents": [
>     {
>       "documentId": "1",
>       "name": "contract.pdf",
>       "transformPdfFields": true,
>       "assignTabsToRecipientId": "1"
>     }
>   ]
> }
> ```

## Field properties cheat sheet

The following table shows how field properties are assigned between PDF forms and Docusign tabs (fields).

|  |  |  |  |
| --- | --- | --- | --- |
| **Adobe** | **CDSE/NDSE** | **REST API** | **SOAP API** |
| Name | Label | tabLabel | TabLabel |
| Tooltip | Tool Tip | name | Name |
| Read Only | Locked/Read Only | locked | CustomTabLocked |
| Required | Required | required | CustomTabRequired |
| Default Value | Initial Value | value | Value |
| Max Length | Max # of chars | maxLength | MaxLength |

## Next steps

- [Tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/)
- [Fixed](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/fixed/) positioning
- [AutoPlace](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/auto-place/) positioning

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
