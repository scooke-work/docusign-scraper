---
title: Authentication
source_url: https://developers.docusign.com/docs/tsp-api/tsp101/tsp-authentication/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- Tsp101
- Tsp101
- Tsp Authentication
scraped_at: '2026-06-18T22:15:24Z'
---

# Authentication

Before your application can make calls to the TSP API, it must authenticate and obtain an access token. This access token proves your app’s identity and authorization. You must submit it with each request to the TSP API. If you're
[delegating the creation of the CMS](https://developers.docusign.com/docs/tsp-api/tsp101/cms-service-api/) to Docusign, you must provide the same access token you submitted to get the signing information.

TSP authentication uses an extension of the Docusign OAuth framework. This framework requires that you register your TSP as an OAuth client with Docusign.

## Prerequisites

Before you can use the TSP API, you need the following:

1. A Docusign eSignature
   [developer account](https://developers.docusign.com/platform/build-integration/).
2. An
   [integration key](https://developers.docusign.com/platform/configure-app#integration) that identifies your application.
3. A
   [redirect URI](https://developers.docusign.com/platform/configure-app#redirect) associated with your integration key. The redirect URI points to a web application managed by the TSP. All signers must log in to this page to authenticate and proceed with the signature process. TSPs can use a localhost address during the development phase then an HTTPS once the integration is live.

Once TSPs get their integration key and redirect URI, they can request the Docusign account server for an access token they will use to authenticate in every call to the TSP API.

## Authentication in the signature process

Once a TSP registers as an OAuth client with Docusign, it authenticates in the signature process as follows:

1. In a Docusign document, a signer selects SIGN and CONTINUE to request signatures from the TSP (see [Getting Started](https://developers.docusign.com/docs/tsp-api/tsp101/get-started/) for more information on this step).
2. The Docusign account server sends the following information to the TSP:
   - the redirect URI of the TSP (see also **Prerequisites** above)
   - a standard OAuth authorization code:

     ```
     HTTP/1.1 302 Found
             Location: https://client.example.org/cb?
             code=SplxlOBeZQQYbYS6WxSbIA
     ```

     **Code sample 1**: authentication information sent to the TSP

     **Note:** the OAuth authorization code expires after 2 minutes.
3. The TSP uses the OAuth authorization code from step 2 to request the creation of a token to access DocuSIgn (see also **Access token request** below).
4. Docusign returns an access token to the TSP.
5. The TSP can now use the access token to call the next TSP API endpoint in the signing flow (see also [Geting Started](https://developers.docusign.com/docs/tsp-api/tsp101/get-started/). This token is only valid for this transaction. All subsequent requests require a new access token.

## Access token request

The [POST /oauth/token](https://developers.docusign.com/platform/auth/reference/obtain-access-token/) endpoint contains all the claims needed to complete every request authentication step.

```
POST oauth/token HTTP/1.1
Host: account-d.docusign.com
Content-Type: application/x-www-form-urlencoded
Authorization: Basic Y2xpZW50SWQ6Y2xpZW50U2VjcmV0
```

```
grant_type=authorization_code
    &code=SplxlOBeZQQYbYS6WxSbIA
    &redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb
```

The Authorization header follows the OAuth 2.0 Basic authentication schema described in [Section 2.3.1 of the OAuth 2.0 RFC](https://tools.ietf.org/html/rfc6749#section-2.3). It concatenates the client ID, a semicolon, and the client secret. Docusign provides the client ID and client secret when TSPs [configure their applications](https://developers.docusign.com/platform/configure-app/).

In the above example, the value of the client ID is “clientId” and the value of the client secret is “clientSecret”. Optionally, you can pass this information as the `client_id` and `client_secret` POST parameters.

## Access token response

The response to the access token request contains the following parameters:

- `access_token`: The access token used by the TSP to authenticate with the Docusign APIs.
- `expires_in`: The lifetime of the access token.
- `token_type`: The Bearer, describing the usage of the access token.
- `user_api`: The base URI used for subsequent requests to the TSP REST APIs. `HTTP/1.1 200 OK
  Content-Type: application/json
  Cache-Control: no-store
  Pragma: no-cache{
  "access_token": "(access token example removed for document brevity)",
  "expires_in": 28800,
  "token_type": "Bearer",
  "user_api": "https://{server}.docusign.net"
  }`

TSPs must use the returned token in all subsequent requests to authenticate to Docusign. They must also ensure they use the returned base URI in their calls to the TSP API. Note that if you're calling the CMS API, you must use the dedicated [base URL](https://developers.docusign.com/docs/tsp-api/tsp101/cms-service-api/).

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
