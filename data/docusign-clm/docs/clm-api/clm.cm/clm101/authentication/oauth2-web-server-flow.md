---
title: 'Authentication: OAuth2.0 web server flow'
source_url: https://developers.docusign.com/docs/clm-api/clm.cm/clm101/authentication/oauth2-web-server-flow/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- CLM.CM
- CLM.CM
- API 101
- API 101
- Authentication
- Authentication
- Oauth2 Web Server Flow
scraped_at: '2026-06-18T21:49:14Z'
---

# Authentication: OAuth2.0 web server flow

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

Docusign CLM supports the [OAuth 2.0](http://tools.ietf.org/html/rfc6749) web server flow.

## OAuth 2.0 Overview

In this authentication scheme, the application invokes Docusign CLM OAuth by redirecting the user to the **authorization endpoint**, passing their **client id** on the query string. It is up to the calling application to decide when to redirect the user. Common scenarios include presenting the user with an "authorization" button or automatically redirecting the user when the application detects that it does not have a refresh token stored for the end user.

The OAuth 2.0 process flows as follows:

- The app detects that an authorization token is needed and redirects the user to the authorization endpoint.
- Since the authorization endpoint is a secure page in Docusign CLM, standard Docusign CLM authentication is invoked, which will either be the Docusign CLM login page or SAML SSO.
- After the user authenticates, they are presented with the OAuth authorization page. In the case that the user has multiple Docusign CLM accounts, they are prompted for which one they would like to use with the application.
- After the user authorizes the application the browser is redirected to the **redirection endpoint (callback url)** that is associated with the **client id** that is was passed to the **authorization endpoint**. The **redirection endpoint** is an endpoint configured in the application that is programmed to receive a one time use authorization code that is passed on the query string.
- The authorization code represents the user/account that was authorized for use with the application and is posted to the **token endpoint** to exchange it for a **refresh token** and **access token** that can then used with the REST API.

## OAuth 2.0 Configuration Steps

The following steps describe how to configure Docusign CLM OAuth:

1. The client application redirects the user’s browser to the Docusign CLM authorization endpoint, passing the applications client id on the querystring. The authorization endpoints are as follows:

   **Production Authorization Endpoint**

   ```
   https://login.springcm.com/oauth/authorize?client_id=[your client id]
   ```

   **UAT Authorization Endpoint**

   ```
   https://loginuat.springcm.com/oauth/authorize?client_id=[your client id]
   ```
2. Since the authorization endpoint is a secure page, the user is prompted for their Docusign CLM credentials.
3. After being authenticated, the user is presented with the authorization page for the application. If the user is a member of more than one Docusign CLM account, they will be presented with a drop down list where they must choose which account they are authorizing access to for use with the application. The screen will look similar to the following:

   ![Docusign CLM authorization page with drop-down menu for choosing your account](https://developers.docusign.com/img/clm-api/oauth.png?v=2023061320)
4. When the user authorizes access to their account, the browser is redirected to the redirect endpoint that is associated with the client id and will pass an authorization code on the query string.

   **Callback URL Format**

   ```
   https://[redirection endpoint registered for a client id]?code=[one time use authorization code]
   ```
5. The authorization code passed on the query string is a one time use token and has an expiration of 1 minute. It can be exchanged for an access token and refresh token in the context of the authorizing user by making a post to the token endpoint. In addition to the authorization code, the client id that was used in Step 1 must also be passed along with its corresponding client secret and grant type of "authorization\_code". The token endpoint and sample request/response JSON is shown below:

   **Production Token Endpoint**

   ```
   https://auth.springcm.com/api/v201606/token
   ```

   **UAT Token Endpoint**

   ```
   https://authuat.springcm.com/api/v201606/token
   ```

   **Exchanging an authorization code for refresh and access tokens - Sample Request**

   ```
   headers: Accept: 'application/json', Content-Type: application/json
   uri: https://auth.springcm.com/api/v201606/token
   method: POST
   {
     "code": [authorization code from the query string],
     "grant_type":"authorization_code",
     "client_id": [client id passed to the authorization endpoint],
     "client_secret": [client secret pair for the client id]
   }
   ```

   **Exchanging an authorization code for refresh and access tokens - Sample Response**

   ```
   {
     "access_token": [access token that can be used immediately],
     "token_type":"bearer",
     "expires_in": [number of seconds before the access token expires],
     "refresh_token": [refresh token for the user],
     "api_base_url": [base url for the object api]
   }
   ```
6. The access token can now be used to access the API. It must be passed in the Authorization header for all calls to the Object, Task and Content API. When passing it must be prefixed with “bearer” as shown below:Authorization: bearer [your access token]
7. Access tokens are short lived and are currently valid for one hour. The expiration date time for the token is returned in the authorization call. Refresh tokens are long lived and currently expire after 3 months of non-use. The refresh token can be used to retrieve a new access token for the authorizing user without prompting them for credentials. The same client Id and client secret used to retrieve the refresh token must be posted along with the refresh token itself to retrieve a new access token. The access token service endpoint and sample JSON for retrieving a new access token from a refresh token are shown below. Note that these are also passed back in the response in Step 5 :

   **Exchanging a refresh token for an access token - Sample Request**

   ```
   headers: Accept: 'application/json', Content-Type: application/json
   uri: https://auth.springcm.com/api/v201606/token
   method: POST
   json:
   {
     "refresh_token": [refresh token for the user],
     "grant_type":"refresh_token",
     "client_id": [client id passed to the authorization endpoint],
     "client_secret": [client secret pair for the client id]
   }
   ```

   **Exchanging a refresh token for an access token - Sample Response**

   ```
   {
     "access_token": [access token that can be used immediately],
     "token_type":"bearer",
     "expires_in": [number of seconds before the access token expires],
     "api_base_url": [base url for the object api]
   }
   ```

   > **Note:** Best practice is to code for access token expiration by either tracking the token expiration time or trapping a 401 error response and requesting a fresh token.

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
