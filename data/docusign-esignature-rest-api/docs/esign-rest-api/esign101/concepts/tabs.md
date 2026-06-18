---
title: Tabs
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/
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
scraped_at: '2026-06-18T21:09:57Z'
---

# Tabs

*Tabs* (also called tags or fields) are places in a [document](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) where a [recipient](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/) must provide input (typically a signature) or where a calculated value (derived from a formula) is displayed. Tabs are typically assigned to individual recipients to provide input; after the recipients have entered data for all of their tabs in all of the documents of an [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/), the signing process is complete.

For examples of how to work with tabs using the API, see how to [Add tabs to a template using fixed positioning](https://developers.docusign.com/docs/esign-rest-api/how-to/create-template/) or [Add tabs to a document using AutoPlace anchor tabs](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-composite-template-embedded/), [Set envelope tab values directly using the API](https://developers.docusign.com/docs/esign-rest-api/how-to/set-envelope-tab-values/), or [Set template tab values directly from the API](https://developers.docusign.com/docs/esign-rest-api/how-to/set-template-tab-values/).

Each tab is defined by a**type**, a set of parameters that determine what kind of input it requires (for example, a **Sign Here** tab requires a signature, while a **Text** tab prompts the user to input text), and where it is placed on a document. [See the full list of tab types](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/#tab-types).

Tabs are positioned within a document in one of three ways:

- [Fixed](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/fixed/) (or *absolute*) positioning
- [AutoPlace](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/auto-place/) (or *anchor-tag*) positioning
- [PDF form field transformation](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/pdf-transform/)

> **Note:** You can also use the Docusign website to manually position recipient tabs and save those locations and settings in a [template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/) for repeated use. Additionally, you can use the [Embedded signature and elastic signing with eSignature (Embedded Signing)](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/) workflow to load the tagging view of an envelope at run time.

If you do not add any tabs to an envelope, you create a free-form signing experience. In free-form signing, recipients can freely add and place any tabs they wish on the documents. The only requirement for free-form signers is that they place at least one tab in the envelope.

Your recipients can navigate from tab to tab either by scrolling through your document, or you can set a tab order that automatically moves recipients from one tab to another as they complete their assignments.

You can set this tab order by adding a value for the `tabOrder` property of your tab definitions in the API; all tabs must be assigned a `tabOrder` or the default ordering will be used. Tabs on a page are navigated to in ascending order, starting with the lowest number and moving to the highest. If two or more tabs have the same `tabOrder` value, the normal auto-navigation setting behavior for the envelope is used. If no `tabOrder` is set, tabs will be ordered top to bottom, then left to right, based on the top left corner pixel position of each tab.

**Note**: The tab order feature is not enabled for all accounts by default. To enable the tab order feature for your account, contact customer support.

## Next steps

Read about important tab features:

- [See the full list of tab types](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/#tab-types)
- [Auto-place (anchor tagging)](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/auto-place/)
- [Fixed positioning](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/fixed/)
- [PDF form field transformation](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/pdf-transform/)
- [Data replication](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/data-replication/)
- [Number fields](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/number-fields/)
- [Calculated fields](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/calculated-fields/)
- [Conditional fields](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/conditional-fields/)
- [Custom tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/custom-tabs/)
- [Requesting payment with tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/payment/)
- [Pre-filled tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/prefilled-tabs/)

Working with tabs? Learn how to:

- [Add tabs to a document using AutoPlace anchor tabs](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-composite-template-embedded/)
- [Add tabs to a template using fixed positioning](https://developers.docusign.com/docs/esign-rest-api/how-to/create-template/)
- [Set envelope tab values directly using the API](https://developers.docusign.com/docs/esign-rest-api/how-to/set-envelope-tab-values/)
- [Set template tab values directly from the API](https://developers.docusign.com/docs/esign-rest-api/how-to/set-template-tab-values/)

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
