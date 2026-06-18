---
title: Authentication
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/authentication/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Authentication
scraped_at: '2026-06-18T19:46:29Z'
---

# Authentication

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

Before your application can make calls to the Web Forms API, it must authenticate and obtain an access token. You must submit this access token, which proves your application’s identity and authorization, with each request.

You can use these supported OAuth2 authentication workflows to obtain an access token and make calls to the Web Forms API:

- [Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/): For the highest level of security, Docusign recommends using this authentication method when possible.
- [Implicit Grant](https://developers.docusign.com/platform/auth/implicit/): This authentication method can be used with public clients, as defined in [RFC 6749 section 2.1](https://datatracker.ietf.org/doc/html/rfc6749#section-2.1). Implicit Grant must be used for applications that are not able to store sensitive data on a secure server.
- [JSON Web Token (JWT) Grant](https://developers.docusign.com/platform/auth/jwt/): With this authentication method, the access token impersonates a user, also known as an *account member*. Use JWT Grant for heavily automated applications that call the Docusign platform without direct user interaction.

See the [platform authentication overview](https://developers.docusign.com/platform/auth/) for a description of these grants and how to choose between them.

## Required scopes

When you request an access token for your OAuth2 scenario, you must request Web Forms API [scopes](https://developers.docusign.com/platform/auth/reference/scopes/) during the authentication process.

The eSignature REST API `signature` scope is required for Web Forms API requests, in addition to Web Forms API scopes. For JWT Grant, the `impersonation` scope is also required.

The Web Forms API supports these scopes:

| Scope | Description | Required for these requests |
| --- | --- | --- |
| `webforms_read` | Allows an application to retrieve information about [web form configurations](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) defined in an account. | [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) [Configurations:listForms](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/listforms/) |
| `webforms_instance_read` | Allows an application to retrieve information about [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances). | [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) [Instances:listInstances](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/listinstances/) |
| `webforms_instance_write` | Allows an application to create web form instances and refresh [instance tokens](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#instance-token-expiration). | [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) [Instances:refreshToken](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/refreshtoken/) |
| `signature` | Used for operations on the Docusign eSignature API. | Required for requests to all Web Forms API endpoints. |

The scopes request is included in these authentication flow components:

- **Authorization Code Grant:** The authorization code request
- **Implicit Grant:** The access token request
- **JWT Grant:** The body of the JWT token

See [Authentication examples](https://developers.docusign.com/docs/web-forms-api/plan-integration/authentication/#authentication-examples) for details.

## Authentication examples

### Authorization Code Grant

#### Request URL

`https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20webforms_read%20webforms_instance_read%20webforms_instance_write&client_id=7c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&redirect_uri=http://example.com/callback/`

### Implicit Grant

#### Request URL

`https://account-d.docusign.com/oauth/auth?response_type=token&scope=signature%20webforms_read%20webforms_instance_read%20webforms_instance_write&client_id=7c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&redirect_uri=http://example.com/callback/`

### JSON Web Token (JWT) Grant

#### Request URL

`https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation%20webforms_read%20webforms_instance_read%20webforms_instance_write&client_id=7c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f&redirect_uri=http://example.com/callback/`

#### JSON request body

```
{
  "iss": "5c2b8d7e-xxxx-xxxx-xxxx-cda8a50dd73f",
  "sub": "464f7988-xxxx-xxxx-xxxx-781ee556ab7a",
  "iat": 1705602811,
  "exp": 1705606811,
  "aud": "account-d.docusign.com",
  "scope": "signature impersonation webforms_read webforms_instance_read webforms_instance_write"
}
```

## Next steps

- See [Authenticate](https://developers.docusign.com/platform/auth/) in the Platform 101 documentation for an overview of each OAuth grant and how to choose which grant to use.
- Learn about how to implement each authentication flow by viewing these guides:
  - [Authorization Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/)
  - [Implicit Grant](https://developers.docusign.com/platform/auth/implicit-get-token/)
  - [JWT Grant](https://developers.docusign.com/platform/auth/jwt-get-token/)

    For the Web Forms API, you do not need to complete the step **Get your user's base URI** in these guides. See [Production data center autorouting](https://developers.docusign.com/docs/web-forms-api/web-forms-101/endpoint-base-path/#production-data-center-autorouting) for more information.

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
