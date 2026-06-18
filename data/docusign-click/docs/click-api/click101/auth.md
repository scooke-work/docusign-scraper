---
title: Authentication
source_url: https://developers.docusign.com/docs/click-api/click101/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Click API
- Click API
- API 101
- API 101
- Authentication
scraped_at: '2026-06-18T22:18:19Z'
---

# Authentication

Before your application can make calls to the Click API, it must authenticate and obtain an access token. You must submit this access token, which proves your app’s identity and authorization, with each request.

You can use any supported [OAuth2 authentication workflows](https://developers.docusign.com/platform/auth/choose/) to obtain an access token and make calls to the Click API. Service integrations may use Authorization Code Grant or JSON Web Token (JWT) Grant, while mobile apps may use Implicit Grant. See [Platform Authentication](https://developers.docusign.com/platform/auth/) for an overview of these grants and how to choose which grant to use for your app.

## Required scopes

The only difference between authenticating with the Click API and the eSignature API is that when you request an access token for your OAuth2 scenario, you must request a special Click API [scope](https://developers.docusign.com/platform/auth/reference/scopes/) during the authentication process. You can combine some Click API scopes with eSignature scopes.

You can choose from the following Click API scopes:

| **Scope** | **Description** |
| --- | --- |
| click.manage | Enables most elastic template operations, including creating and updating elastic templates; getting a list of elastic templates; creating user agreements; getting a list of users; and retrieving responses. |
| click.send | Enables checking to see if a user has agreed to a elastic template, as well as retrieving an agreement or PDF file for an agreement. No other operations. This scope provides access to a subset of the functions available under the `manage` scope. The only function available under the `send` scope that is not also available under the `manage` scope is [ClickWraps:createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/).  **Note:** Although the scope is named `send`, elastic templates are not sent to recipients. Instead, they are embedded in a web page or app. |

- Using Authorization Code Grant, you request scopes when you make the authorization code request.
- Using Implicit Grant, you request scopes when you make the access token request.
- Using JWT Grant, you request scopes in the body of the JWT token.

## Authentication examples

The following examples show how to authenticate by using each grant type.

### Authorization Code Grant

**Request URL:**`https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20click.manage%20click.send&client_id=7c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&state=a39fh23hnf23&redirect_uri=http://example.com/callback`

### Implicit Grant

**Request URL:**`https://account-d.docusign.com/oauth/auth?response_type=token&scope=signature%20click.manage%20click.send&client_id=7c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&state=a39fh23hnf23&redirect_uri=http://example.com/callback/`

### JSON Web Token (JWT) Grant

**Request URL:**`https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20click.manage%20click.send&client_id=7c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&state=a39fh23hnf23&redirect_uri=http://example.com/callback`

```

```

**JSON request body**:

```
{
  "iss": "5c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f",
  "sub": "464f7988-xxxx-xxxx-xxxx-781ee556ab7a",
  "iat": 1523900289,
  "exp": 1523903289,
  "aud": "account-d.docusign.com",
  "scope": "signature click.manage click.send"
}
```

## Next steps:

- See [authentication](https://developers.docusign.com/platform/auth/) in the Platform 101 documentation for an overview of each OAuth grant and how to choose which grant to use for your app.
- Learn about how to implement each authentication flow by viewing these guides:
  - [Authorization Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/)
  - [Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/)
  - [JSON Web Token (JWT) Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/)

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
