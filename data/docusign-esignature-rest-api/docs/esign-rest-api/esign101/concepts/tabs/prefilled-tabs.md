---
title: Prefilled tabs
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/prefilled-tabs/
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
- Prefilled Tabs
scraped_at: '2026-06-18T21:09:58Z'
---

# Prefilled tabs

eSignature REST API 2.1 only
When you need to add tab data to one of your documents while sending your envelope, you can do that using prefilled tabs. A *prefilled tab* is a tab whose value is set by the sender and inserted to a document prior to sending its envelope to its recipients. These tabs are visible to all recipients during signing, but cannot be edited by them.

This enables you to:

- Prefill data in a document during sending without using read-only tabs.
- Edit the prefilled tab data via the `correct` option before recipients have acted on the document.
- Add data to a document during sending that is not associated with a specific recipient.

You can use the following tab types for prefilled tabs:

- Text
- Checkbox
- Radio
- Company
- Name

To define one or more prefilled tabs, enter your tab definition data in the new `prefillTabs` attribute alongside your other tab definition objects. **Note**: Prefilled tabs are available to all developer accounts for development and testing, but not all account plans provide access to prefilled tabs in the production environment. Make sure your plan includes this feature before developing against it.

For a full list of available Docusign eSignature tab types, see the [EnvelopeRecipientTabs Resource](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/) in the API Reference.

## Using prefilled tabs

You can add a prefilled tab to a document in the same way you would add any other tab, using the [EnvelopeDocumentTabs: create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/create/) API method or its SDK equivalent. Rather than define the prefilled tab JSON directly within the `tabs` object, they are added to a new child object, `prefillTabs`, which will contain the tab declarations.

There is no separate API or endpoint specifically for prefilled tabs. Prefilled tabs are standard tabs with values set before the envelope is sent. To prefill a tab, include the tab definition and set its value when creating the envelope or recipient. The following JSON shows how to define a prefilled `textTab` within the `tabs` object of your document:

```
"tabs":
{
  "prefillTabs":{
    "textTabs": [
      {
        "tabLabel": "Text 2db4770d-xxxx-xxxx-xxxx-cef65ebd1a6a",
        "conditionalParentLabel": null,
        "conditionalParentValue": null,
        "fontSize": "size9",
        "underline": false,
        "italic": false,
        "fontColor": "black",
        "bold": false,
        "font": "lucidaconsole",
        "required": true,
        "locked": false,
        "concealValueOnDocument": false,
        "name": "",
        "shared": false,
        "requireAll": false,
        "requireInitialOnSharedChange": false,
        "value": "",
        "validationPattern": "",
        "validationMessage": "",
        "disableAutoSize": false,
        "maxLength": 4000,
        "width": 84,
        "height": 22,
        "mergeFieldXml": "",
        "pageNumber": 1,
        "documentId": "1",
        "xPosition": 104,
        "yPosition": 94
      }
    ]
  }
}
```

To get a list of all tabs (including prefilled tabs) in the documents of an envelope, use the [EnvelopeDocuments:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/get/) API method or its SDK equivalent.

You can also add, update, or delete prefilled tabs data in your documents with the following API methods or their SDK equivalents:

- [EnvelopeDocumentTabs: get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/get/)
- [EnvelopeDocumentTabs: update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/update/)
- [EnvelopeDocumentTabs: create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/create/)
- [EnvelopeDocumentTabs: delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/delete/)
- [TemplateDocumentTabs: get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/get/)
- [TemplateDocumentTabs: update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/update/)
- [TemplateDocumentTabs: create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/create/)
- [TemplateDocumentTabs: delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/delete/)

## Using prefilled tabs with composite templates

When you create a composite template with one or more templates that include documents that have prefilled tabs, the following rules determine whether the prefilled tabs are retained in the composite template.

- If either the server template or inline template has prefilled tabs, but the other template does not, the tabs will be added to the envelope documents regardless of the sequence values of the templates.
- If both server template and inline template have defined different prefilled tabs, then all of the tabs from all templates will be added, regardless of the sequence value of the templates.
- If both the server template and inline template have the same prefilled tabs (prefilled tabs with the same `tabLabel` value) but have configured them with different properties, the prefilled tabs from the template with the lower sequence value will be used.

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
