---
title: Fixed positioning
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/fixed/
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
- Fixed
scraped_at: '2026-06-18T21:09:57Z'
---

# Fixed positioning

*Fixed positioning* (also known as absolute positioning) places a tab at a fixed location using the `xPosition` and `yPosition` tab properties, measured in units of points. A point is 1/72nd inch (or 3.527 points per millimeter). This method works well for static documents or documents that don't change much over time.

In most cases, the upper left corner of the tab will be placed at a position a number of points equal to `xPosition` from the left side of the document and a number of points equal to `yPosition` from the top of the document.

For example, if you want to place a signature tab in a specific location that does not change based on the position of related text, you can use the code below. It places the tab 100 points to the right of the document’s left edge and 200 points below the document’s top edge. :

```
"tabs": {
  "signHereTabs": [
    {
      "xPosition": "100",
      "yPosition": "200",
      "name": "signHere",
      "documentId": "1",
      "pageNumber": "1"
    }
  ]
}
```

**Note:** [How to set tab values in a template](https://developers.docusign.com/docs/esign-rest-api/how-to/set-template-tab-values/) provides a walkthrough and sample code for fixed positioning.

## Calculating tab position

1. Decide where you want to put the tab on your page. The x and y coordinates you choose for the tab specify where the upper left point of the tab will be placed. This will be considered Point A. Any decimal measurements will be rounded to the nearest 72nd of an inch.
2. Calculate the `xPosition` and `yPosition` of Point A. To calculate your `xPosition` and `yPosition`, you should:
   1. Determine how many inches from the left side of the page Point A is. We will call this number *DistanceX*.

      The `xPosition` for Point A will be:

      xPosition (points) = 72 (DPI) \* DistanceX (inches)

      Alternatively, for millimeters: xPosition (points) = DistanceX (millimeters) / 3.527 (millimeters per dot)
   2. Determine how many inches from the top of the page Point A is. We will call this number *DistanceY*.

      The `yPosition` for Point A will be:

      yPosition (points) = 72 (DPI) \* DistanceY (inches)

      Alternatively, for millimeters: yPosition (points) = DistanceY (millimeters) / 3.527 (millimeters per dot)

      Round the `xPosition` and `yPosition` values to the nearest whole integer.

      ![](data:image/svg+xml;charset=utf-8,%3Csvg height='410' width='549' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

      ![co-ordinates origin](https://images.ctfassets.net/aj9z008chlq0/1YRhyICiDe7Mr3fS42YDfc/8515845ec9155ccd2db25ca33aa7ec04/CoordinatesOrigin.png?w=549&h=410&q=50&fm=png)
   3. Determine the offset that you want for your tab. Due to requirements for supporting legacy functionality and to avoid breaking any existing integrations, some tabs can have different behavior when placed with fixed positioning. See each tab's individual documentation in the [API reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/#tab-types) for details.

      Once you've found the offset you want, apply it to your tab's `xPosition` and `yPosition` values. These values must be integers.
3. Now that you have calculated the `xPosition` and `yPosition` of the point where you need to add your tab, you can add it to the document via an API call or using one of the eSignature SDKs. For details, see one of the [code examples](https://developers.docusign.com/docs/esign-rest-api/how-to/) that demonstrate adding tabs to a document, such as [How to request a signature by email](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-remote/).

   **Note:** In v2.1 of the eSignature API, you cannot specify a negative `xPosition` or `yPosition` or an exception will be generated.
4. After adding the tab to your document, verify that the tab was placed in the correct spot on the final completed PDF. To view the tab in its document, send the envelope to yourself, sign or complete it (if applicable), and then view the completed envelope in your inbox.

   **Note:** The completed document holds the absolute position of all added tabs. Any other representation of the document in a web or mobile UI is an approximation of how the tabs will appear within the completed document.

   On the **Envelope Summary** page, on the right side above **Signing Order**, you will be able to download the relevant document as a PDF. The tab you placed will be saved directly into the page.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='389' width='619' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![envelope summary](https://images.ctfassets.net/aj9z008chlq0/GQVtq9epqM0JfAduQyRlC/80288d7736a855994c85ccf329089336/EnvelopeSummary.png?w=619&h=389&q=50&fm=png)

## Next steps

See [How to set tab values in a template](https://developers.docusign.com/docs/esign-rest-api/how-to/set-template-tab-values/) for an example of how to add tabs to a document via fixed positioning.

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
