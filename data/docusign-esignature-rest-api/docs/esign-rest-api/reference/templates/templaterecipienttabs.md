---
title: TemplateRecipientTabs Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Templates
- Templates
- Templaterecipienttabs
scraped_at: '2026-06-18T21:10:31Z'
---

# TemplateRecipientTabs Resource

The TemplateRecipientTabs resource provides methods that let you add, update, and delete tabs from an envelope. Tabs are associated with a specific recipient in an envelope and are only used by the recipient types In Person Signers and Signers.

## Tab Types

Docusign supports a wide range of tab types for input and display of specific types of information. See [EnvelopeRecipientTabs Resource](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/) for the complete list.

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
the Docusign Service can derive an anchor location for the tab
by correlating anchor information to data within the document.

When the Docusign Service receives a request that contains tabs
with anchor information,
it searches the document for instances of the `anchorString` property.
When found,
it places a tab of the specified type for the designated recipient.
Tab positions are established by setting offsets for the tab.

When you apply tabs to the document,
Docusign does not remove or replace the text in the `anchorString` property. You can hide codified anchors by using the same font color as the background of the document. So the anchor can be used by Docusign processes and it will not be visible on the document.

To use an anchoring option:

1. Identify the location in the document by text string. You can use a pre-existing text string or add a new one.
   For best performance Docusign recommends using single word anchor strings when possible, especially when there are a large number of pages in the envelope.
   For example, you might want to add a Sign Here tab to the "Borrower's Signature" lines in a document, but that phrase might occur in places in the document where you don't want to tab to appear. In this case, you could add the text "BorrowerSignHere" in white font color (so that isn't visible in the document) to all the places you want Sign Here tabs to appear and use "BorrowerSignHere" as the anchor string.
2. Reference the anchor through the `anchorString` property of the tab.
3. Determine the offset from the anchor string location to where the tab should be placed.

Setting a positive value in the `anchorXOffset` property moves the tab right on the page and positive values in the `anchorYoffset` prove moves the tab down the page. The `anchorUnits` property specifies the units used for the offsets.
For Sign Here and Initial Here tabs the bottom-left of the anchor string is equivalent to position (0,0), and the bottom-left of the tab graphic is placed relative to that.
For all other tabs the bottom-left of the anchor string is equivalent to position (0,0), and the top-left of the tab graphic is placed relative to that.
Docusign does not currently provide tools to derive the offset values. Determination of the proper offset will likely require some trial-and-error.

### Rules for working with anchor tags

When anchor tabs are used, all documents in the envelope are searched for the `anchorString` property.

- You set the text of the anchor string in the `anchorString` property. Docusign tabs are created for each instance of the `anchorString` property within the document, so special care must be taken to establish unique anchor strings that do not result in unintentional tabs.
- You cannot use the same anchored tab for different recipients for the same document.
- The Docusign system cannot search for text that is embedded in an image when checking for anchor strings.
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
- Note that `\\*` matches *anything*. If you were to add
  another tab with the `tabLabel` set to `\\*Name` to the
  example above, it would end up matching the other two
  labels as well. This pattern is not a regex expression, and Docusign uses it as a wildcard to populate identical values in tabs.
- Each occurrence of the tab must have identical properties.

  For example, suppose there are two Text tabs in a document,
  each with `tabLabel` set to `Name`.
  If one tab has the `bold` property set to **true,**
  and the other has the `bold` property set to **false,**
  only the first one will be populated.
  In order to automatically populate both occurrences
  of the `Name` Text tabs,
  the `bold` property must be set to the same value for both tabs.

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs ```  Adds tabs for a recipient. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/delete/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs ```  Deletes the tabs associated with a recipient in a template. |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/list/) | GET  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs ```  Gets the tabs information for a signer or sign-in-person recipient in a template. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs ```  Updates the tabs for a recipient. |

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
