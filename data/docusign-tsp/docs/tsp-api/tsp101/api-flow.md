---
title: TSP API Flow
source_url: https://developers.docusign.com/docs/tsp-api/tsp101/api-flow/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- Tsp101
- Tsp101
- Api Flow
scraped_at: '2026-06-18T22:15:24Z'
---

# TSP API Flow

The following example describes the entire signing process with the TSP API—all the way from envelope creation to document signing:

1. The sender adds documents to an envelope, sets the envelope recipients, and selects the signature type associated with the TSP.

   ![Recipient configuration](https://developers.docusign.com/img/tsp/tsp_api_flow_recipconfig.png?v=20260610.1 "Recipient configuration")
2. The envelope recipient (the signer) receives an email notification and selects \*\*REVIEW DOCUMENT\*\* for reviewing and signing documents.

   ![Review document](https://developers.docusign.com/img/tsp/tsp_api_flow_revdoc.png?v=20260610.1 "Review document")
3. In Docusign, the signer selects SIGN and CONTINUE to request signatures.
4. Docusign generates an iframe with a URL that redirects to the signature provider. The URL also contains a code that the TSP can use for
   [authentication](https://developers.docusign.com/docs/tsp-api/tsp101/tsp-authentication/) purposes.

   ![Authentication](https://developers.docusign.com/img/tsp/tsp_api_flow_auth.png?v=20260610.1 "Authentication")
5. In response to the authentication process, the TSP gets an access token that they must use in every request to authenticate in Docusign (see also
   [Authentication](https://developers.docusign.com/docs/tsp-api/tsp101/tsp-authentication/)).
6. The signature provider requests Docusign for the signer’s information (
   [GET User Info](https://developers.docusign.com/docs/tsp-api/reference/get-tsp-user-information/)). In response, Docusign sends the signer’s name, email, language, and other available information.
7. The signature provider prompts the user to authenticate on the page displayed in the iframe. If the authentication is successful, the signature process starts. If it fails, the signature provider notifies Docusign using the
   [POST Update Transaction](https://developers.docusign.com/docs/tsp-api/reference/update-transaction/) endpoint.
8. The signature provider requests Docusign to sign for the first document. The
   [POST Sign Hash Session Information](https://developers.docusign.com/docs/tsp-api/reference/sign-hash-session-information/) request returns an array of either hashed or base64 documents to the TSP.
9. The Trust Service Provider signs all the supplied documents and encapsulates each document using a CMS. Trust Service Providers can build CMSs on their own or let Docusign build one by using the following endpoints:
   1. `POST SignedAttributes` allows TSPs to provide Docusign with all the information (user certificate, documents hashes, PAdES format) required to build the CMS's signed attributes. Docusign creates the signed attributes and returns them as a base 64 encoded string to the TSP.
   2. `POST cms` provides Docusign with all the information required to build the final CMS. Expected information includes the signed attributes, the signatures and timestamp tokens. Docusign creates a proper CMS and returns it to the TSP.
10. Once all signatures are complete, the TSP returns the Base64-encoded CMSs to Docusign using the
    [POST Complete Sign Hash Session Information](https://developers.docusign.com/docs/tsp-api/reference/complete-sign-hash-session-information/) request. Docusign returns a response to the TSP that indicates the number of remaining signatures (if any).

    ![TSP API flow](https://developers.docusign.com/img/tsp/tsp_api_diagram.png?v=20260610.1 "TSP API flow")

At any time during the signature process, the TSP can use the [POST Update Transaction](https://developers.docusign.com/docs/tsp-api/reference/update-transaction/) request to push messages to the log file. Such messages can be of great help to troubleshoot signatures.

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
