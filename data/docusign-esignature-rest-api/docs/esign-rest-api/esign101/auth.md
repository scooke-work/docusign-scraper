---
title: Authentication
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Authentication
scraped_at: '2026-06-18T20:28:07Z'
---

# Authentication

Before your application can make calls to the Docusign eSignature API, it must authenticate and obtain an access token. This access token, which proves your app’s identity and authorization, must be submitted alongside each request to the Docusign eSignature API.

You can use any Docusign-supported OAuth2 authentication workflow to obtain an access token and make calls to the eSignature API: [Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/), [Public Authorization Code Grant](https://developers.docusign.com/platform/auth/public-authcode-get-token/), [JSON Web Token (JWT) Grant](https://developers.docusign.com/platform/auth/jwt/), or [Implicit Grant](https://developers.docusign.com/platform/auth/implicit/). Service Integrations may use the Confidential/Public Authorization Code or JSON Web Token grants, while mobile apps may use the Public Authorization Code or Implicit Grants. See [Platform Authentication](https://developers.docusign.com/platform/auth/) for an overview of these grants and how to choose which grant to use for your app.

## Required scopes

To make calls to the eSignature API, you must request the signature [scope](https://developers.docusign.com/platform/auth/#authentication-scopes) during the authentication process.

- Using the Confidential or Public Authorization Code Grants, you request the signature scope when you make the the authentication code request
- Using the JWT grant, you request the signature scope in the body of the JWT token
- Using the Implicit grant, you request the signature scope when you make the access token request

For a walkthrough of how to get an access token using each flow, see [How to get an access token with Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/), [How to get an access token using Public Authorization Code Grant](https://developers.docusign.com/platform/auth/public-authcode-get-token/), [How to get an access token with JWT Grant](https://developers.docusign.com/platform/auth/jwt-get-token/), and [How to get an access token with Implicit Grant](https://developers.docusign.com/platform/auth/implicit-get-token/).

## Next steps

- See [Authentication](https://developers.docusign.com/platform/auth/) in the Platform 101 documentation for an overview of each OAuth grant and how to choose which grant to use for your app.
- Learn about how to implement each authentication flow by viewing and downloading code examples:
  - [Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/)
  - [Public Authorization Code Grant](https://developers.docusign.com/platform/auth/public-authcode-get-token/)
  - [JSON Web Token (JWT) Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/)
  - [Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/)

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
