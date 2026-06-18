---
title: Design Standards Requirements
source_url: https://developers.docusign.com/docs/tsp-api/tsp101/design-standards-requirements/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- Tsp101
- Tsp101
- Design Standards Requirements
scraped_at: '2026-06-18T22:15:24Z'
---

# Design Standards Requirements

This topic describes the requirements and standards for each TSP iframe element.

## General requirements on modals

If you selected the modal display, the TSP iframe opens inside a Docusign-hosted responsive modal in the context of the signing experience. 

Modals have a close button, a top and bottom padding of 40 pixels and a left and right padding of 48 pixels. Their size adjusts to the height and width of the web browser. If the iframe content exceeds the modal’s height, users must scroll the page vertically to access the content that is not visible. Also, check that the iframe content fits the modal’s width. If not, users have to horizontally scroll the page to access the whole content. The height of the modal expands vertically to fit the content until it comes within 80 px of the top and bottom of the page. Modals have a maximum width of 800 pixels.

The Docusign teams recommend setting the background color of the modals to white.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='322' width='512' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image showing general requirements for modals in TSP](https://images.ctfassets.net/aj9z008chlq0/738gok3dWSSXguLqqJmRJB/8399ccfa6e7db40f4279f61fcc0244fd/tspGeneralModal.png?w=512&h=322&q=50&fm=png)

## General requirements on overlays

If you selected the overlay display, the TSP iframe opens inside a Docusign-hosted responsive overlay in the context of the signing experience. 

Overlays have a close button, a top padding of 64 pixels and a left and right padding of 80 pixels. The Docusign teams recommend setting the background color of the modals to white.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='322' width='512' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image showing general requirements for overlays in TSP](https://images.ctfassets.net/aj9z008chlq0/1muFazVWOg5Qb2Oy68VBIm/81527ed2f60d6d9d583fdcee32249bee/tspGeneralOverlay.png?w=512&h=322&q=50&fm=png)

## General requirements on tabs

If you choose the tab display, the content of the iframe opens in a new browser’s tab. If selecting this display, TSPs must ensure seamless navigation for the signer. They also must provide clear navigation buttons that allow the signer to easily transition back to the original workflow from the opened tab.

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
