---
title: Trust Service Provider Concepts
source_url: https://developers.docusign.com/docs/tsp-api/tsp101/concepts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- Tsp101
- Tsp101
- Concepts
scraped_at: '2026-06-18T22:15:24Z'
---

# Trust Service Provider Concepts

[Envelope](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#envelope)

[Long term validation](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#longtermvalidation)

[Sender](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#sender)

[Signature type](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#sigtype)

[Signer](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#signer)

[Trust Service Provider (TSP)](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#tsp)

[Trust Service Provider API (TSP API)](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#tspapi)

[Cryptographic message syntax (CMS)](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#cms)

[Redirection URL](https://developers.docusign.com/docs/tsp-api/tsp101/concepts/#rurl)

## Envelope

An envelope is equivalent to a transaction and includes the following items:

- documents
- signers
- tags (signature placeholder on the documents)

The TSP API allows you to perform signatures for each recipient of an envelope provided at least one document contains one signature tag or one initials tag.

![Envelopes contain documents, signers, and tags](https://developers.docusign.com/img/tsp/tsp101_concepts_fig1.png?v=20260610.1 "Envelopes contain documents, signers, and tags")

## Long-term validation

Long–term validation (LTV) is a format that provides all the information required to verify that a signature was valid at the time it was issued. LTV relies on several profiles delivering distinct security levels. The TSP API supports the LT and LTA levels. For more information, see [Long term validation of PDF signatures](https://developers.docusign.com/docs/tsp-api/tsp101/long-term-signature-validation/).

## Sender

Senders assign signers to envelopes. They select the envelopes' documents, document signers, and signature types for each signer.

## Signature type

When creating an envelope, senders select the type of signature each recipient can apply to documents. Every TSP belongs to a signature type.

## Signer

Senders assign documents to signers. Usually, signers receive an email from senders to review and sign documents. They do not need to be registered Docusign users.

## Trust Service Provider (TSP)

A TSP is a third-party signature provider that stores the identity of its users and issues digital signatures under their identity.

## Trust Service Provider API (TSP API)

The TSP API is a set of REST API methods that Trust Service Providers can use to sign documents managed in a Docusign workflow.

## Cryptographic message syntax (CMS)

CMS is an encryption standard based on the PKCS #7 syntax. The TSP encapsulates each signed document in a CMS and sends them back to Docusign. The TSP partners who are not familiar with building a CMS can use the [CMS service API](https://developers.docusign.com/docs/tsp-api/tsp101/cms-service-api/) to generate a CMS.

## Redirection URL

A Redirection URL is an HTTP address that Docusign displays in an iframe after a signer requests the signature of a document. Usually, it redirects to the TSP login page. Once the signer logs in, the TSP starts the signature process.

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
