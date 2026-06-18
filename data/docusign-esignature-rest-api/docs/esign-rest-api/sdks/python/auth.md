---
title: Python SDK authentication
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/python/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- Python
- Python
- Authentication
scraped_at: '2026-06-18T20:28:16Z'
---

# Python SDK authentication

Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run eSignature REST API code examples.

## Obtaining an access token

The goal of [authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/) is to obtain an access token. An access token is needed for every API call to Docusign. Access tokens last from one to eight hours, depending on the grant type used to obtain the access token.

## Determining your OAuth flow

Please review the [Platform Authentication 101](https://developers.docusign.com/platform/auth/) documentation on Dev Center to determine which OAuth flow to use.

## Authorization Code Grant with Python

Because the OAuth Authorization Code Grant flow is centered on interactions between the user and the identity server via the browser, the SDK is not used.

### Configuration information required to proceed with Authorization Code Grant

- **Integration key** (client ID): This can be obtained in your developer account by accessing the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. See the
  [Administration Guide](https://support.docusign.com/guides/ndse-admin-guide-api-and-keys) for more information.
- **Client secret**: This is for the integration key you obtained above. It is also created in the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. The client secret can only be copied the first time it is displayed; it will not be visible later. Make sure to retain it for your records.
- **Redirect/Callback URI**: This is the URI to which the end user will be redirected when your application uses the Authorization Code Grant flow. That URI must exactly match one of the redirect URIs you define for your integration key in the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. You can add multiple redirect URIs for a single integration key.

Authorization Code Grant requires a web interface because users must use the Docusign Identity Provider (IdP) to authenticate with their Docusign account. In this section we’ll cover the recommended practices for using Authorization Code Grant with Flask applications. Other Python web technologies may require a different technique to complete the Authorization Code Grant flow and are beyond the scope of this guide.

### Using Authorization Code Grant with Flask applications

In your Flask application you can create an OAuth object and register your remote application on it using the
[remote\_app()](https://pythonhosted.org/Flask-OAuth/#flask_oauth.OAuth.remote_app) method as shown below. Using the
`authorized_response()` Flask method on your remote app will give you a response containing your access token. You can find a full working example in our
[GitHub repository](https://github.com/docusign/code-examples-python).

```
    oauth = OAuth(app)
    cls.ds_app = oauth.remote_app(
        "docusign",
        consumer_key=DS_CONFIG["ds_client_id"],
        consumer_secret=DS_CONFIG["ds_client_secret"],
        access_token_url=DS_CONFIG["authorization_server"] + "/oauth/token",
        authorize_url=DS_CONFIG["authorization_server"] + "/oauth/auth",
        request_token_params=request_token_params,
        base_url=None,
        request_token_url=None,
        access_token_method="POST"
    )
```

## JSON Web Tokens (JWT) with Python

Every Python SDK (eSignature as well as others) includes two JWT Grant methods:

- **request\_jwt\_user\_token**: This method uses the JWT Grant flow to request a token that will represent a specific user. This JWT Grant flow is used for all eSignature REST API methods and for most other Docusign API methods as well.
- **request\_jwt\_application\_token**: This method uses the JWT Grant flow to request a token that will represent the application itself (not a user). This JWT Grant flow is useful for specific Docusign partners who are part of special Docusign programs allowing them to manage accounts using the
  [Docusign Admin API](https://developers.docusign.com/docs/admin-api/).

### Configuration information required to proceed with JWT

- **Integration key (client ID)**: This can be obtained in your developer account from the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. See the
  [Administration Guide](https://support.docusign.com/guides/ndse-admin-guide-api-and-keys) for more information.
- **RSA private key**: This is for the integration key you obtained above and can also be created in the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. You only need the private key, and it can only be copied once if you use the administration tool to create it. Make sure to retain it for your records.
- **Base path**: To use either JWT Grant method, you need to use an SDK ApiClient object. To create an ApiClient object, you need to provide a
  `basePath` attribute. Since the application’s correct base path is not yet known, use placeholder values to indicate which system should be queried:

  - `https://demo.docusign.net/restapi#development`
  - `https://www.docusign.net/restapi#production`

  **Note:** This placeholder
  **BASE\_PATH** is used only for the
  `ApiClient request_jwt_user_token, request_jwt_application_token`, and
  `get_user_info` methods. Once you make these calls, you should be able to get the correct
  **BASE\_PATH** and use it to make all other API calls.
- **Impersonated User ID** : This is a GUID uniquely identifying the Docusign user that you will be impersonating with the access token. Your own
  **User ID** can be found at the top of the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page.

  User IDs for other members of your account can be looked up on the
  [Users](https://admindemo.docusign.com/authenticate?goTo=users) page. Locate the user in the list; then use the
  **Action > Edit** command to open the user’s
  **Profile** page. The user’s user ID is shown on the page as the
  **User ID** value.

  User IDs can also be looked up programmatically by using the
  [Users: list](https://developers.docusign.com/docs/esign-rest-api/reference/users/users/list/) method. It requires administrative permissions.

  This parameter is not used for the
  `request_jwt_application_token` method.
- **Scopes**: These represent the OAuth scopes (permissions) that are being requested. For eSignature REST API methods, use the
  `signature` scope. The
  `impersonation` scope is implied by the JWT Grant operation and does not need to be included. If the access token will be used for other Docusign APIs, additional scopes may be required; see each API’s
  [authentication requirements](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/).
- **Parameter formats and additional parameters** are documented in the
  [Python SDK](https://docusign.github.io/docusign-esign-python-client/).

User IDs for everyone in your account are available on the account administrator’s
[Users](https://admindemo.docusign.com/authenticate?goTo=users) page.

[JWT Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/) enables developers to obtain OAuth access tokens without requiring users to log in, given that they have already
[provided consent](https://www.docusign.com/blog/developers/oauth-jwt-granting-consent) for the application to impersonate them when making API calls.

To use JWT from the Python SDK, simply make the following call (you can find this code in
[GitHub](https://github.com/docusign/code-examples-python/blob/master/app/docusign/ds_client.py#L92)):

```
    cls.ds_app = api_client.request_jwt_user_token(
        client_id=DS_JWT[“ds_client_id”],
        user_id=DS_JWT[“ds_impersonated_user_id”],
        oauth_host_name=DS_JWT[“authorization_server”],
        private_key_bytes=private_key,
        expires_in=3600,
        scopes=[“signature”, “impersonation”]
    )
```

Now you can save the access token as shown in the following code:

```
access_token = cls.ds_app.access_token
```

Best practices for managing access tokens:

- Do cache the access token until it expires or is about to expire.
- Do not create a new access token for each API call.
- Recommended: Check the expiration time of the access token before you use it. If it is expired or about to expire (within 10 minutes), then obtain a new authorization token before making the API call. (If using a refresh token, check that it hasn’t expired as well.)

## Obtaining user information

Once authenticated, you need information about the access token’s user. That information is required to make future API calls. Moreover, it’s possible that the user is a member of more than one Docusign account. In this scenario, you can obtain all of the accounts associated with this user to enable them to pick which Docusign account they wish to use with your integration.

The recommended practice (frequently used by Docusign apps) is to use the user’s default account and let them change to use a different account.

Recommended practice is to include the
`account_id` as a configuration value, since the API application may require specific account settings. In this case, the app should check that the user has access to the configured
`account_id`.

The Python code to retrieve the
[user information](https://developers.docusign.com/platform/auth/reference/user-info/) from the developer account is:

```
    api_client = ApiClient()
    user_info = api_client.get_user_info(access_token)
```

The
[get\_user\_info](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/client/api_client.py#L749) function returns an
[OAuthUserInfo](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/client/auth/oauth.py#L42) object that has various pieces of information related to the user. The
[accounts](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/client/auth/oauth.py#L50) property is a list of
[Account](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/client/auth/oauth.py#L187)) objects that provides the collection of Docusign accounts and their information. You can use the
`is_default` property of the
`Account` object to check if this is the user’s default account. The
`OAuthUserInfo` object also includes
`name` and
`email` properties related to the logged-in user.

The
`Account` object also includes the
`base_uri` property. The
`base_uri` property forms the first term of the URL you must use to make API calls on behalf of the user’s account. Since each Docusign account is associated with a specific Docusign data center, the
`base_uri` property includes the data center’s designation, such as na2.docusign.net or eu.docusign.net, like so: https://na2.docusign.net. The base\_uri property’s value is concatenated with the string “/restapi” to form the base path, which represents the root of the URL for all endpoints in the eSignature REST API, for example: https://na2.docusign.net/restapi.

When you instantiate the
`ApiClient` object, which is used to make API calls, you pass the value of the base path in its constructor (see below). If you reuse an
`ApiClient` object, use its
`set_base_path` method to ensure the correct base path is set.

## Instantiating and configuring the ApiClient for making API calls

The `ApiClient` class represents the base object used as a starting point for all eSignature API calls. You will have to instantiate this object in your code before you can proceed to make API calls.

The basic flow of instantiating an ApiClient looks like this:

```
    api_client = ApiClient()
    api_client.host = base_path
    api_client.set_default_header(header_name=”Authorization”, header_value=f”Bearer {access_token}”)
    envelopes_api = EnvelopesApi(api_client)
```

Let’s break down these four lines of code to understand them better.

### Instantiating the ApiClient object

```
    api_client = ApiClient()
```

This line is used to instantiate a new
`ApiClient` object. This object is used to make eSignature API calls to Docusign.

### Setting the base path

```
    api_client.host = base_path
```

This line sets the
`ApiClient` object’s host parameter to the base path which tells the SDK the first part of the URL to use when making API calls. The latter part of the URL is determined in each API call by the specific classes and methods you choose to use.

The base path for the developer (demo) environment is https://demo.docusign.net/restapi. The base path for the production environment depends on the specific data center where your account is provisioned.

The base path for the eSignature REST API consists of the name of the data center (demo, na2, na3, eu1, ca, au, etc.) and then .docusign.net/restapi.

### Setting the HTTP header with authentication token

```
api_client.set_default_header(header_name="Authorization", header_value=f"Bearer {access_token}")
```

This line is used to provide the authentication information required to make API calls. You first need to obtain a valid access token for authentication. You can find how to obtain a token from the how-to topics for
[Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/confidential-authcode-get-token/),
[Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/), and
[JWT Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/).

The
`set_default_header` method sets the
`default_headers` attribute of the
`ApiClient` class. The
`default_headers` attribute is a dictionary that is used to provide additional HTTP headers for API requests. You can add additional headers to be used with API calls that use the
`ApiClient` object. The
`"Authorization"` header is used to provide the authentication information for the request. The token is added after the word
`"Bearer"`, provided in the
`accessToken` variable. This only needs to be done once for all API calls that will be utilizing the same
`ApiClient` object; however, the token is only valid for eight hours. You will need to obtain a new one and update this header when the token expires.

### Instantiating the required object for the specific set of API calls

```
    envelopes_api = EnvelopesApi(api_client)
```

This is an example of how to use the
`ApiClient` object. It is used as a parameter on the constructors of all the API classes under the docusign\_esign namespace. By instantiating the
`EnvelopesApi` class to use the preconfigured
`ApiClient`, you are ready to make API calls.

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
