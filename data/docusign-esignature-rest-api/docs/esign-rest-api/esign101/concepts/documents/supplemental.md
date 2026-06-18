---
title: Supplemental documents
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/supplemental/
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
- Documents
- Documents
- Supplemental
scraped_at: '2026-06-18T21:09:58Z'
---

## Supplemental documents

*Supplemental documents* are supporting materials, such as disclosures or informational documents, that recipients can view and acknowledge but do not need to sign.

You can identify a document as supplemental by checking its `display` property. If the `display` property has a value of `modal`, the document is considered supplemental.

Supplemental documents use the following properties in the `document` object:

| **Property** | **Description** |
| --- | --- |
| `includeInDownload` | Determines whether the supplemental document is included in the combined document download. |
| `display` | Specifies how the supplemental document is displayed to the recipient.  The possible values are:  - `modal` The document appears in a modal window as a supplement action strip. Recipients can view, download, or print it. This is the recommended value for supplemental documents. - `inline` The document is displayed in the normal signing window. This value is typically not used for supplemental documents but is the default for all other documents. |
| `signerMustAcknowledge` | Indicates whether the signer must acknowledge the supplemental document if they do not have Approve and View tabs. |

If a signer does not have **Approve** and **View** tabs, the value of the `signerMustAcknowledge` property determines the required interaction with the supplemental document:

| `signerMustAcknowledge` | **Signer Action** |
| --- | --- |
| `no_interaction` | No action is required. |
| `view` | The signer must view the document. |
| `accept` | The signer must accept the document. |
| `view_accept` | The signer must view and accept the document. |
| `view_read_accept` | The signer must view, read, and accept the document. |

If the signer has **Approve** and **View** tabs, the platform disregards the `signerMustAcknowledge` property and instead uses the values of these tabs to determine signer requirements:

| **Approve Tab is present** | **View Tab's requiredRead Property** | **View Tab's required Property** | **Signer Action** |
| --- | --- | --- | --- |
| No | `false` (default) | `false` (default) | No requirements. |
| No | `false` | `true` | The signer must view the document. |
| No | `true` | -- | The signer must view and read the document. |
| Yes | `false` | `false` | The signer must view and accept the document. |
| Yes | `false` | `true` | The signer must view and accept the document. |
| Yes | `true` | -- | The signer must view, read, and accept the document. |

> **Note:** The `requiredRead` property of a Viewtab takes precedence over its `required` property. If `requiredRead` is set to `true`, the platform assumes `required` is also true.

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
