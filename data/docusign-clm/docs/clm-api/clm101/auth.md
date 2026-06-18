---
title: Authentication Overview
source_url: https://developers.docusign.com/docs/clm-api/clm101/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- API 101
- API 101
- Authentication
scraped_at: '2026-06-18T21:48:55Z'
---

# Authentication Overview

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

Before your application can make calls to the CLM API, it must authenticate and obtain an access token. This access token proves your app’s identity and authorization. You must submit the token with each request.

You can use any Docusign-supported OAuth2 authentication workflow to obtain an access token and make calls to the CLM API: [Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/#confidential-authorization-code-grant), [Public Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/#public-authorization-code-grant), [Implicit Grant](https://developers.docusign.com/platform/auth/implicit/), or [JSON Web Token (JWT) Grant](https://developers.docusign.com/platform/auth/jwt/). Service integrations may use Confidential Authorization Code Grant or JWT Grant, while mobile apps may use Public Authorization Code Grant or Implicit Grant.

**Note**: Salesforce clients authenticate by using JWT Grant. For details, see [Salesforce Client Authentication](https://developers.docusign.com/docs/clm-api/clm101/salesforce-clients/).

For an overview of these grant types and to determine the best grant type to use for your app, see [Authentication](https://developers.docusign.com/platform/auth/) in the Platform 101 documentation.

## **Prerequisites**

Before you can use the Docusign CLM API, you need:

1. A [Docusign eSignature developer account](https://go.docusign.com/o/sandbox/) and a Docusign CLM account.
2. An [integration key](https://developers.docusign.com/platform/configure-app/#integration-key) that identifies your app.
3. A defined redirect URI for your integration key. This is the URL to which Docusign will redirect the user's browser after authentication is complete.
4. You must also have configured your app correctly for the OAuth type you want to use. For details, see the instructions for the grant type you want to use under [Next steps](https://developers.docusign.com/docs/clm-api/clm101/auth/#next_steps).

## Required scopes

One of the differences between authenticating with the CLM API and the eSignature API is that, when you request an access token for your OAuth2 scenario, you must request a special CLM API [scope](https://developers.docusign.com/platform/auth#scopes) during the authentication process. You can combine CLM scopes with eSignature API scopes.

You can choose from the following CLM scopes:

|  |  |
| --- | --- |
| **Scope** | **Description** |
| `spring_read` | Allows read access to all objects, including downloading documents. |
| `spring_write` | Allows write access to all objects, including uploading documents. |
| `content` | Allows read and write access only to document content. This scope grants you access to download and upload documents, but does not grant access to other resources. If you are already requesting the `spring_read` and `spring_write` scopes, you don't need to also request the content scope. |

**Note**: The `impersonation` scope is also required when using the JWT flow.

Only request the scopes you need for your application.

- Using Authorization Code Grant, you request scopes when you make the authorization code request.
- Using Implicit Grant, you request scopes when you make the access token request.
- Using JWT Grant, you request scopes in the body of the JWT token.

## Authentication examples

The following examples show how to authenticate by using each grant type.

### Authorization Code Grant

Request URL:

```
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20spring_read%20spring_write&client_id=5c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&redirect_uri=http://localhost/
```

### Implicit Grant

Request URL:

```
https://account-d.docusign.com/oauth/auth?response_type=token&scope=spring_read%20spring_write%20signature&client_id=5c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&redirect_uri=http://localhost/
```

### JSON Web Token (JWT) Grant

Request URL:

```
https://account-d.docusign.com/oauth/auth?response_type=code&scope=impersonation%20content&client_id=5c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&redirect_uri=http://localhost/
```

JSON request body:

```
{
  "iss": "6c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f", "iat": 1541785491,
  "exp": 1561785491,
  "aud": "account-d.docusign.com",
  "scope": "signature content"
}
```

## Next steps

- See [Platform Authentication](https://developers.docusign.com/platform/auth/) for an overview of each OAuth grant flow and how to choose which grant to use for your app.
- Learn how to implement each authentication flow by viewing these guides:
  - [Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/confidential-authcode-get-token/)
  - [Public Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/public-authcode-get-token/)
  - [Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/)
  - [JSON Web Token (JWT) Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/)
- To learn about JWT Grant authentication for Salesforce integrations, see [Salesforce Client Authentication](https://developers.docusign.com/docs/clm-api/clm101/salesforce-clients/).

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
