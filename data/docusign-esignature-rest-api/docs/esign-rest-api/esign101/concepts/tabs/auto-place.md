---
title: Auto-Place (Anchor Tagging) Tabs
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/auto-place/
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
- Auto Place
scraped_at: '2026-06-18T21:09:57Z'
---

# Auto-Place (Anchor Tagging) Tabs

*Anchor tagging* enables you to place tabs at every location where a specified text string, also known as an *anchor*, is found in a document. When tabs are added with anchor tagging, Docusign searches the document for instances of an `anchorString` property that you provide. For each found instance, it places a tab of the specified type for the designated recipient. Tab positions in relation to the string instances can be set by providing *x* and *y* offsets. These properties are part of the [tabs](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/) object.

Anchor tagging is especially useful for documents that do not have a fixed layout or format. In these documents, you might not know the absolute location of the tabs because they must move with text.

For example, you might have a document that contains the text **Please Sign Here**. If you want to place a signature tab by each instance where this string is found in the document or, better yet, place a signature tab one inch to the right of the string to make sure the signature does not overwrite it, you could use the following tab definition:

```
"tabs": {
    "signHereTabs": [{
        "anchorString": "Please Sign Here",
        "anchorXOffset": "1",
        "anchorYOffset": "0",
        "anchorIgnoreIfNotPresent": "false",
        "anchorUnits": "inches"
    }]
}
```

Because you set the `anchorString` property to the value **Please Sign Here**, a **Sign Here** tab will be placed wherever that string is found in the document, and because `anchorXOffset` is set to `1` and `anchorUnits` is set to `inches`, the signature tabs will be placed one inch to the right of each location. Note that with `anchorIgnoreIfNotPresent` set to **false**, an error will be returned if the text **Please Sign Here** is not found anywhere in the document.

**Note:** When you add anchor tabs as part of a composite template and your account has set `document` **Data Population Scope** (meaning your anchor tabs are only applied to chosen documents, rather than all documents in an envelope), your composite template is limited to containing one server and one inline template. Note that the Data Population Scope settings can only be updated by DocuSign support.

## Setting tab offsets from anchor strings

By default, an anchor tab is placed starting at the first character of its anchor string. You can customize this placement by:

- Setting values for the tab’s `anchorXOffset` and `anchorYOffset` properties (offsets default to pixels, but you can also choose to use inches, mms, or cms by setting the anchorUnits property)
- Setting a value of right or left for the `anchorHorizontalAlignment` property, which controls whether the offset is at the left or right edge of the anchor string

## Anchor strings with custom tabs

You can also use AutoPlace to place Docusign custom tabs in the same way as any other tab. Just as for predefined tabs, to set a custom tab to use AutoPlace, specify an anchor string in your custom tab definition that matches the anchor string in your document where the tab(s) will be placed.

1. Set the `anchorString` property in the tab to the value of the anchor string in your document.
2. Ensure that the document contains an instance of the anchor string in each location where you want to place your tab.
3. Send the envelope as normal.

## Best practices

One common approach to anchor tagging is to use special strings that don’t appear anywhere else in the document as the `anchorString` property for anchor tagging, and then setting the color of these strings to match the document background, making them invisible to recipients. This enables you to easily attach tabs to many places in your documents without disrupting the signing experience for your recipients.

For example, the string **\s1\** could be used to indicate where signature tabs for the first recipient should be placed, and **\i2\** could be used to indicate where initial tabs for the second recipient go. By setting their font color to the same color as the background, you can hide these strings so that the recipients will only see the tabs at those locations, eliminating the need to set an offset.

## Next steps

The following examples, all of which are available in 8 programming languages, demonstrate how to add tabs to a document via anchor tagging.

- [How to request a signature using a composite template](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-composite-template-embedded/)
- [How to set envelope tab values](https://developers.docusign.com/docs/esign-rest-api/how-to/set-envelope-tab-values/)
- [How to request a signature by email](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-remote/)
- [How to request a signature through your app](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded/)

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
