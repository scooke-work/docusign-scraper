---
title: Authentication
source_url: https://developers.docusign.com/docs/rooms-api/rooms101/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- API 101
- API 101
- Authentication
scraped_at: '2026-06-18T22:33:01Z'
---

# Authentication

Before your application can make calls to the Rooms API, it must authenticate and obtain an access token. You must submit this access token, which proves your app’s identity and authorization, with each request.

You can use any supported OAuth2 authentication workflows to obtain an access token and make calls to the Rooms API: [Authorization Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/), [Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/), or [JSON Web Token (JWT) Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/). Service integrations may use Authorization Code Grant or JWT grant, while mobile apps may use Implicit Grant. See [platform authentication](https://developers.docusign.com/platform/auth/) for an overview of these grants and how to choose which grant to use for your app.

## Prerequisites

Before you can use the Docusign Rooms API, you need the following:

1. A Docusign eSignature developer account and a Docusign Rooms account.
   - [Create an eSignature developer account](https://www.docusign.com/developers/sandbox?postActivateUrl=https://developers.docusign.com/&_gl=1*1d3gman*_gcl_au*ODczOTUxNTUwLjE3MjcyOTgwNDc.).
   - [Create a Rooms developer account](https://developers.docusign.com/docs/rooms-api/rooms101/create-account/).
2. An [integration key](https://developers.docusign.com/platform/configure-app/#integration-key) that identifies your app.
3. A defined [redirect URI](https://developers.docusign.com/platform/configure-app/#redirect-uri) for your integration key. This is the URL the user's internet browser will be sent to the redirect URI after authentication is complete.
4. You must also have configured your app correctly for the OAuth type you want to use. For details, see [configure your app](https://developers.docusign.com/platform/configure-app/).

## Required scopes

The only difference between authenticating with the Rooms API and the eSignature API is that when you request an access token for your OAuth2 scenario, you must request a special Rooms API [scope](https://developers.docusign.com/platform/auth/reference/scopes/) during the authentication process. You can combine Rooms scopes with eSignature API scopes.

You can choose from the following Rooms scopes:

| **Scope** | **Description** |
| --- | --- |
| `dtr.rooms.read` | Read rooms data. |
| `dtr.rooms.write` | Update the data of a room. |
| `dtr.documents.read` | Read documents from Docusign Rooms. |
| `dtr.documents.write` | Write documents to Docusign Rooms. |
| `dtr.profile.read` | Read profile data for accounts or signers associated with your company. |
| `dtr.profile.write` | Write profile data to accounts or signers associated with your company. |
| `dtr.company.read` | Read information from all rooms and profiles associated with your company. |
| `dtr.company.write` | Write information to all rooms and profiles associated with your company. |
| `room_forms` | Use endpoints related to the forms feature. |
| `signature` | The eSignature API `signature` scope is required to call the [GetESignPermissionProfiles](https://developers.docusign.com/docs/rooms-api/reference/esignpermissionprofiles/esignpermissionprofiles/getesignpermissionprofiles/) method. |

- Using Authorization Code Grant, you request scopes when you make the authorization code request.
- Using Implicit Grant, you request scopes when you make the access token request.
- Using JWT Grant, you request scopes in the body of the JWT token.

## Next steps:

- See [authentication](https://developers.docusign.com/platform/auth/) in the Platform 101 documentation for an overview of each OAuth grant and how to choose which grant to use for your app.
- Learn how to implement each authentication flow by viewing these guides:
  - How to [obtain an access token with Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/).
  - How to [obtain an access token with Implicit Grant](https://developers.docusign.com/platform/auth/implicit-get-token/).
  - How to [obtain an access token with JWT Grant](https://developers.docusign.com/platform/auth/jwt-get-token/).

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
