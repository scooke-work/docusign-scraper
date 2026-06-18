---
title: Conditional fields
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/conditional-fields/
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
- Conditional Fields
scraped_at: '2026-06-18T21:09:58Z'
---

# Conditional fields

You can reveal specific tabs (also known as fields) to signers when specified conditions are met by making them *conditional fields*. For example, you can reveal conditional fields for a user to input data after they select a checkbox, or require a user to provide additional data after entering text in a text field.

Dependent conditional fields (revealed when user input has been provided to the parent) can be of any tab type. Which types you are allowed to use for Parent conditional fields differ between the UI and the API. In the UI, you can use only the following tab types to trigger revealing conditional fields:

- Checkbox
- Radio button
- Dropdown
- Text

In the API, you can use any field type as a Parent field if you set its `optional` property to `true`. For example, the following `initialHereTab` definition could be used as a conditional parent, because the `optional` property is set to `true`:

```
"initialHereTabs": [
    {
        "optional" : "true",
        "tabLabel": "exampleParent",
        "xPosition": "300",
        "yPosition": "300",
        "pageNumber": "1",
        "documentId": "1"
    }
]
```

## Configuring parent (trigger) tabs

To set the tab to be used as the trigger for a conditional field, you configure properties on the conditional field itself. When you create a conditional field, you specify a `conditionalParentLabel` tab property and a `conditionalParentValue` property.

- `conditionalParentLabel` is the trigger tab whose state can reveal the conditional field
- `conditionalParentValue` is the value of the trigger tab needed to reveal the conditional field

If the conditional field is a **Checkbox** tab or button from a **Radio Group** tab, use `on` as the value to show that the parent tab is active.

### Radio Groups as conditional parents

To reference a **Radio Group** as a conditional parent, the value of the `conditionalParentLabel` property should match the `groupName` property of the radio group tab and the `conditionalParentValue` property value should match the corresponding radio button's `value` property.

### Text tabs as conditional parents

Text tabs can be set as conditional parents to reveal conditional fields either when a specific string is input, or when any text is input.

- For a specific string, enter the specific required value in `conditionalParentValue`
- For any text input, set `conditionalParentValue` to `##ANY##`

## Example conditional field definition

The following example uses conditional fields to reveal a Sign Here tab after a Checkbox tab is selected:

```
{
    "status": "sent",
    "emailSubject": "Conditional Tabs Example",
    "documents": [{
        "documentId": "1",
        "name": "contract.pdf",
        "documentBase64": "base64 encoded string..."
    }],
    "recipients": {
        "signers": [{
            "email": "smason@email.com",
            "name": "Sara Mason",
            "recipientId": "1",
            "tabs": {
                "checkboxTabs": [{
                    "tabLabel": "sampleCheckbox",
                    ...
                }],
                "signHereTabs": [{
                    "conditionalParentLabel": "sampleCheckbox",
                    "conditionalParentValue": "on",
                    "xPosition": "80",
                    "yPosition": "40",
                    "documentId": "1",
                    "pageNumber": "1"
                }]
            }
        }]
    }
}
```

## Next steps

- [How do I set a conditional field based on the response to one or more radio button groups?](https://support.docusign.com/s/articles/How-to-set-a-conditional-field-based-on-the-response-to-one-or-more-radio-button-groups)
- [Conditional fields](https://support.docusign.com/s/document-item?bundleId=gbo1643332197980&topicId=hew1578456460132.html)
- [Common API Tasks: Using conditional tabs](https://www.docusign.com/blog/developers/common-api-tasks-using-conditional-tabs)

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
