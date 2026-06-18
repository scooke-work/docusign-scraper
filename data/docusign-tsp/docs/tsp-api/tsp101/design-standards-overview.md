---
title: Design Standards Overview
source_url: https://developers.docusign.com/docs/tsp-api/tsp101/design-standards-overview/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- Tsp101
- Tsp101
- Design Standards Overview
scraped_at: '2026-06-18T22:15:24Z'
---

# Design Standards Overview

To improve the quality of the integration between Trust Service Providers (TSPs) and Docusign, follow these standards for creating a more consistent, clear and delightful experience for signers.

## TSP signature flow

**Step 1. Invitation to Sign**

The signer gets an invitation to sign through an email, a web page or from the sender during in-person signing. **Step 2. Access Authentication (Optional)**

The signer authenticates to access the document. **Step 3. Review Document**

The signer reviews and completes the document in the Docusign signing experience. **Step 4. TSP Integration**All TSP partner content opens in an iframe within a Docusign-hosted modal or overlay. The TSP iframe opens when the signer is about to sign documents in the Docusign signing experience. The signer completes identity verification or uses the digital certificate to sign the document. **Step 5. Document Completed**

The document is completed after the signer signs with the digital signature.

## TSP integration options

The TSP’s iframe opens inside a Docusign-hosted page as the signer follows the signature workflow. The TSP API provides several options for opening the TSP’s iframe:

- **Modal**
- **Overlay**
- **New tab**

### **Modal**

The content of the iframe opens in a modal that displays over the last active page. Modals are web-responsive. This means they adapt and display content across various devices and screen sizes. However, modals also have a maximum height. Beyond that limit, users must vertically scroll the modal to access the content that is not visible. For that reason, the Docusign teams recommend using modals for pages with minimal content. For example, you can use modals to display login pages.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='756' width='1201' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image of a TSP modal](https://images.ctfassets.net/aj9z008chlq0/6pN5WexcGbhuYyalzozInO/21eb6bd16085cf1e06de2b9a9b93e030/tspModal.png?w=1201&h=756&q=50&fm=png)

### **Overlay**

The content of the iframe opens in an overlay that displays on top of the last active page. Overlays are responsive like modals but cover the entire page. You can use them to display pages with substantial content.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='322' width='512' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image of TSP overlay](https://images.ctfassets.net/aj9z008chlq0/mLOy1fWeZDX3HyiiKeo8v/0b0b5cb41a35bb3cb67d5a837bd45605/tspOverlay.png?w=512&h=322&q=50&fm=png)

### **New tab**

The content of the iframe opens in a new browser’s tab. Choose this option if you want to have full control of the display.

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
