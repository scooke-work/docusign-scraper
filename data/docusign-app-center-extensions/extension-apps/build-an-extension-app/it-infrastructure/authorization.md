---
title: Authorization
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- IT Infrastructure
- IT Infrastructure
- Authorization
scraped_at: '2026-06-18T19:51:50Z'
---

# Authorization

To make calls to another platform or [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/), your extension app must be authorized with that platform using [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749). To obtain authorization, your extension app must provide its credentials to the platform and obtain an [access token](https://www.oauth.com/oauth2-servers/access-tokens/), which it includes in all requests to that platform or proxy.

## Supported authorization grants

Docusign supports two methods for authentication: [Authorization Code Grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) or [Client Credentials Grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4). For public extension apps that connect Docusign with external systems, use Authorization Code Grant. For private extension apps that connect Docusign with internal systems, you can use either Authorization Code Grant or Client Credentials Grant. Client Credentials Grant is only supported for clients in the United States.

Your extension app will provide different sets of values for each Grant, and the authentication logic will be implemented on your platform. You will need to specify which type will be used before creating your extension app, then define the required values within your extension app manifest.

Note that the type of authentication that your extension app uses, as identified by the `grantType` property in its manifest, cannot be changed after it is initially set during extension app creation.

See [Authorization Code Grant](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/#authorization-code-grant) or [Client Credentials Grant](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/#client-credentials-grant) for details.

### Authorization Code Grant

In Authorization Code Grant (ACG) authentication, the user exchanges an authorization for an access token by calling an authorization URL with a set of required parameters. Authorization Code Grant flows can only be used by apps that can secure a client secret.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1067' width='1043' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A diagram showing the flow steps for Authorization Code Grant.](https://images.ctfassets.net/aj9z008chlq0/755ztKmQ9UoZ3EPFMVGIqH/8f887e90242832183b71a5cd27bc049e/Extension_app_auth_code_grant.png?w=1043&h=1067&q=50&fm=png)

The Authorization Code Grant flow consists of these steps:

1. The Docusign platform directs a user to an authorization endpoint for the external service.
2. The user logs in with their external service credentials and provides consent for the extension app to send requests on their behalf. The external service, which manages the consent process, returns an authorization code to the Docusign platform.
3. The Docusign platform provides the authorization code in a request to a token issuance URL for the external service, and the external service’s response contains an access token.

All subsequent API requests from the extension app include the access token in the request.

If your extension app will call an external service that supports authorization, then your extension app can obtain authorization directly from the external service. Another option is to use an identity provider for authorization.

To configure an extension app that uses the Authorization Code Grant flow:

- When creating your extension app through the form-based experience, select your distribution type. If you select **Private**, choose **OAuth 2.0 – Authorization Code**.

  ![](data:image/svg+xml;charset=utf-8,%3Csvg height='500.99999999999994' width='705' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

  ![An image of the Docusign UI showing the prompt to choose an authorization grant type for your extension app.](https://images.ctfassets.net/aj9z008chlq0/2z18ut8MA2dUR4RDcXIdlP/3504a2ae882b3bb847e352467a7bda81/chooseOAuth.png?w=705&h=501&q=50&fm=png)

  Or, if you are creating an extension by uploading a manifest, set the `grantType` property to  `authorization_code`.

  If you select **Public** for your distribution type, your extension app will use Authorization Code Grant by default.
- In your extension app manifest, provide values for your `clientId`, `clientSecret`, `authorizationUrl`, and `authorizationParams` elements.
  - `clientId` should contain a value that uniquely identifies the app in your platform.
  - `clientSecret` should contain a secret known only to your secure app and your platform.
  - `authorizationUrl` should contain the URL where your extension app can exchange an authorization code for an access token.
  - `authorizationParams` should contain all the values that your platform requires to authenticate your extension app.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

"connections": [

{

"id":

"fa25ea6e-xxxx-xxxx-xxxx-9d98f0fb92b2",

"name": "authentication",

"description": "Secure connection to

Sample Extension App",

"type": "oauth2",

"params": {

"provider": "CUSTOM",

"clientId": "[omitted]",

"clientSecret": "[omitted]",

"scopes": [],

"grantType": "authorization\_code",

"customConfig": {

"authorizationMethod": "header",

"authorizationParams": {

"prompt": "consent",

"access\_type": "offline"

},

### Client Credentials Grant

Client Credentials Grant is an OAuth 2.0 flow where your [private](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/) extension app exchanges its client ID and client secret credentials for an access token. It is typically used by automated processes because it does not require user interaction or consent. Apps using Client Credentials Grant are meant to be shared between multiple admins within the same org, and this grant flow cannot be used by public extension apps. It is currently only available to customers in the United States.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='818' width='717' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A flow diagram showing each step for the extension app Client Credentials Grant.](https://images.ctfassets.net/aj9z008chlq0/rGOExjDLhPD1QnEsGaQpe/61192aecc018b2f21343e46ad8dc3e12/Extension_app_client_credentials.png?w=717&h=818&q=50&fm=png)

The Client Credentials Grant flow consists of these steps:

1. The extension app provides its client ID and secret to the authorization server and requests an access token from the token endpoint.
2. The authorization server authenticates the client and, if valid, returns an access token.

To configure an extension app that uses the Client Credentials Grant flow:

- When creating your extension app through the form-based experience, select your distribution type. Select **Private**, then choose **OAuth 2.0 – Client Credentials**.

  Or, if you are creating an extension by uploading a manifest, set the `grantType` property to  `client_credentials`.
- In your extension app manifest, provide values for your `clientId` and `clientSecret` elements.
  - `clientId` should contain a value that uniquely identifies the app in your platform.
  - `clientSecret` should contain a secret known only to your secure app and your platform.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

"connections": [

{

"name": "authentication",

"description": "Secure connection to Sample

Extension App",

"type": "oauth2",

"params": {

"provider": "CUSTOM",

"scopes": [],

"grantType": "client\_credentials",

"clientId": "[omitted]",

"clientSecret": "[omitted]",

"customConfig": {

"tokenUrl": "https://www.samplecompany.com/

api/oauth/token",

"authorizationMethod": "header",

"scopeSeparator": " ",

"requiredScopes": []

## Access token expiration

Access tokens obtained via the Authorization Code Grant are typically short-lived. Extension apps attempt to automatically refresh expiring tokens as many times as possible by obtaining longer-lived refresh tokens. Tokens must be refreshed for the extension app to remain authorized to send requests to the external service.

The extension app's ability to obtain refresh tokens depends on whether the external service supports them, and whether it provides expiration information for access and refresh tokens. If the external service does not provide this support, the extension app will not be able to refresh tokens automatically, and the authorized user will have to re-authorize upon token expiration.

The automatic refresh can fail in these situations:

- Changes occur in the authorized user's account with the external service. Account changes that can prevent token refresh include updates to the account password or permissions, the account becoming disabled, or the user revoking consent.
- The refresh process violates external service restrictions. For example, the platform may prohibit the refresh of a token that hasn't been used for a length of time, may limit the number of refresh tokens per account, may have a limit on session length, or may consider continuous automated refresh to be a violation of their terms of service.

If an extension app is unable to refresh an expired access token, the extension app's API requests will fail. If you suspect that this has occurred, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance.

See [Refresh tokens](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/#refresh-tokens) for configuration information.

## Authorization setup

You define authorization details when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/).

If you will register the extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), see [Update connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) for instructions on defining authorization details.

If you will register the extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), you define authorization details in the [connection object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) in the [extension app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/).

Regardless of which registration method you use, Docusign uses the values you provide to obtain authorization from the external service to which your extension app makes calls, or from the identity provider if you use one for authorization.

To populate the values, you'll need to consult the authorization documentation for the external API that your extension app calls. If you are using an identity provider, consult its documentation for authorization requirements. You may also need to configure options in the identity provider settings.

When consulting the external API authorization documentation or identity provider documentation, be sure to check for any requirements in the areas listed below.

### OAuth 2.0 grant type

Extension apps support Authorization Code Grant. Make sure that the external API or identity provider documentation that you're consulting is for this authorization type. If you are using an identity provider, you may need to select Authorization Code Grant in the identity provider settings.

### Scopes

Consult the external API documentation or identity provider documentation to determine whether any scopes are required for authorization. When you register an extension app, include the scopes:

- In the [connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) if you register the app using a form.
- In the extension app manifest [scopes](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/#connection-parameters-schema) property if you register the app using an app manifest file.

  Also check the API documentation to determine which scopes are required for the endpoints your extension app will call, and include them as well when you register the extension app.

### Refresh tokens

Make sure you supply any properties in the [connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) or in the app manifest file [connection object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) that the external service or identity provider requires to support refresh tokens. This may include a value that you must provide in the scopes setting. If you are using an identity provider, you may also need to enable refresh tokens in the identity provider settings. The external API or identity provider documentation may refer to the option for refresh tokens as *offline access*.

### Communication type

If the external API or identity provider requires the selection of a communication type, use [machine-to-machine (M2M)](https://www.techtarget.com/iotagenda/definition/machine-to-machine-M2M).

### Redirect URIs

A redirect URI (also referred to as a *callback URI*) appears as a query parameter in the authorization endpoint that Docusign generates from the authorization URL supplied in the [connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) or the extension app manifest file [authorizationUrl](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/#connection-custom-configuration-schema) property. Docusign automatically populates the correct redirect URI in the authorization endpoint and uses the redirect URI to persist the user's access token and refresh token, which is required for the connection to work. The redirect URI is hosted on the Docusign platform. You do not need to create your own redirect URI.

The external API or identity provider may require redirect URIs to be configured. If so, supply the appropriate redirect URI listed below for the environment you're using.

| Environment | Region | Redirect URI |
| --- | --- | --- |
| Developer | All | https://demo.services.docusign.net/act-gateway/v1.0/oauth/callback |
| Production | AU | https://au.services.docusign.net/act-gateway/v1.0/oauth/callback |
| Production | CA | https://ca.services.docusign.net/act-gateway/v1.0/oauth/callback |
| Production | EU | https://eu.services.docusign.net/act-gateway/v1.0/oauth/callback |
| Production | US | https://us.services.docusign.net/act-gateway/v1.0/oauth/callback |

Additional regional production redirect URIs will be available in future releases.

## Requirements for OAuth 2.0 implementation

Docusign requires that your authorization service:

1. Receives, stores, and sends back the `state` parameter. This parameter is used by Docusign and is sent when Docusign attempts to obtain authorization. Your service must store the value being passed and send it back again to Docusign with the token.
2. Sends both the `code` and `state` parameters as URL parameters when making the call to the callback URL.

## Next steps

- [Update connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) has details about configuring authorization settings when registering an extension app using a form.
- [Use a manifest file to register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/) provides a walkthrough of registering an extension app using an app manifest file and includes sample authorization parameters.
- [Connection schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) has details about the [extension app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/) properties that enable you to configure authorization parameters.
- [Run a connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) explains how to test your extension app's authorization process.

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
