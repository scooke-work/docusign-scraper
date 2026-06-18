---
title: Authoritative copies
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/authoritative-copies/
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
- Authoritative Copies
scraped_at: '2026-06-18T20:28:19Z'
---

# Authoritative copies

An *authoritative copy* is the single, distinct, absolute original version of a document that is unique, identifiable, and unalterable without detection. You can specify whether all of the documents in an envelope are authoritative copies or just specific documents.

Whether a document is considered an authoritative copy depends on the values of three properties in the envelope and `document` objects.

|  |  |
| --- | --- |
| PROPERTY | DESCRIPTION |
| Envelope `authoritativeCopy` | Enables or disables the feature. If this value is **false**, no documents are authoritative copies. |
| Envelope `authoritativeCopyDefault` | The default value of the document's `authoritativeCopy` property if it is not set. |
| Document `authoritativeCopy` | As long as the envelope's `authoritativeCopy` property is **true,** specifies whether the document is an authoritative copy. |

Note that, to make every document in an envelope authoritative, it is enough to make the envelope's `authoritativeCopyDefault` property **true**, leaving the other properties unset. Conversely, to make no documents authoritative, it is enough to set the envelope's `authoritativeCopyDefault` property to **false**.

After an agreement, authoritative copies are watermarked, then should be *vaulted* and stored in an external system. The following diagram and table describes how these settings affect whether a document is an authoritative copy and subsequently vaulted.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='540' width='960' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Diagram showing when a document is classified as authoritative copy, in relation to your envelope and document properties.](https://images.ctfassets.net/aj9z008chlq0/7duV4sfR7Zxblz879a37oP/e115d83ad417058182649410d69e8735/authoritativeCopy.png?w=960&h=540&q=50&fm=png)

|  |  |  |  |
| --- | --- | --- | --- |
| **ENVELOPE AUTHORITATIVECOPY** | **ENVELOPE AUTHORITATIVECOPYDEFAULT** | **DOCUMENT AUTHORITATIVECOPY** | **DOCUMENT IS AN AUTHORITATIVE COPY** |
| false | any | any | No document in the envelope is authoritative |
| true | false | false | No |
| true | false | true | Yes |
| true | true | false | No |
| true | true | true | Yes |
| true | true | null | Yes |
| true | false | null | No |
| true | null | null | Yes, every document in the envelope is authoritative |

In the table above, **null** means that no value was set; **any** means that the value can be **null**, **true**, or **false**.Authoritative copies can be purged once they have been exported.

See[Working with authoritative copies using Docusign APIs](https://www.docusign.com/blog/developers/the-trenches-working-authoritative-copies-using-docusign-apis) for examples on how to construct envelopes flagged for authoritative copy, check its status, update it, frequently asked questions, and more.

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
