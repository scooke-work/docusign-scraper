---
title: Ruby SDK authentication
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/ruby/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- Ruby
- Ruby
- Authentication
scraped_at: '2026-06-18T21:09:55Z'
---

# Ruby SDK authentication

## Obtaining an access token

The goal of
[authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/) is to obtain an access token. An access token is needed for every API call to Docusign. Access tokens last from one to eight hours, depending on the grant type used to obtain the access token.

## Determining your OAuth flow

Please review the
[Platform Authentication 101](https://developers.docusign.com/platform/auth/) documentation on the Developer Center to determine which OAuth flow to use.

## Authorization Code Grant with Ruby

Because the OAuth Authorization Code Grant flow is centered on interactions between the user and the identity server via the browser, the SDK is not used.

### Configuration information required to proceed with Authorization Code Grant

- **Integration key** (client ID): This can be obtained in your developer account by accessing the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. See the
  [Administration Guide](https://support.docusign.com/guides/ndse-admin-guide-api-and-keys) for more information.
- **Client secret**: This is for the integration key you obtained above. It is also created in the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. The client secret can only be copied the first time it is displayed; it will not be visible later. Make sure to retain it for your records. If you forget your client secret, you can generate a new one to use.
- **Redirect/Callback URI**: This is the URI to which the end user will be redirected when your application uses the Authorization Code Grant flow. That URI must exactly match one of the redirect URIs you define for your integration key in the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. You can add multiple redirect URIs for a single integration key.

Authorization Code Grant requires a web interface because users must utilize the Docusign Identity Provider (IdP) to authenticate with their Docusign account. In this section, we’ll cover the recommended practices for using Authorization Code Grant in your Ruby on Rails web application. Other Ruby web technologies may require a different technique to complete the Authorization Code Grant flow and are beyond the scope of this guide.

### Using Authorization Code Grant with Rails web applications and [OmniAuth](https://github.com/omniauth/omniauth/blob/master/README.md)

1. In a file named
   [docusign.rb](https://github.com/docusign/code-examples-ruby/blob/master/lib/docusign.rb), create an
   [OmniAuth strategy](https://github.com/omniauth/omniauth/blob/master/README.md#an-introduction) for authenticating with Docusign with the following code:

   ```
   require 'omniauth-oauth2'

   module OmniAuth
     module Strategies
       class Docusign < OmniAuth::Strategies::OAuth2
         option :name, 'docusign'

         uid { raw_info['sub'] }

         info do
           {
             name: raw_info['name'],
             email: raw_info['email'],
             first_name: raw_info['given_name'],
             last_name: raw_info['family_name']
           }
         end

         extra do
           {
             sub: raw_info['sub'],
             account_id: @account['account_id'],
             account_name: @account['account_name'],
             base_uri: @account['base_uri']
           }
         end

         private

         def raw_info
           return @raw_info if @raw_info

           @raw_info = access_token.get(options.client_options.user_info_url.to_s).parsed || {}
           fetch_account(@raw_info['accounts']) if @raw_info.present?
           @raw_info
         end

         def fetch_account(items)
           if options.target_account_id
             @account = items.find { |item| item['account_id'] == options.target_account_id }
           else
             @account = items.find { |item| item['is_default'] }
           end

           if @account.blank?
             raise %'Could not find account information for the user in the "accounts" of raw_info: #{@raw_info}'
           end
         end
       end
     end
   end
   ```
2. Create a file called
   [config/initializers/omniauth.rb](https://github.com/docusign/code-examples-ruby/blob/main/config/initializers/omniauth.rb) and add the following code to enable Docusign Authorization Code Grant to work with your application:

   ```
   require 'docusign'

   OmniAuth.config.logger = Rails.logger
   OmniAuth.config.allowed_request_methods = [:post, :get]

   config = Rails.application.config
   config.middleware.use OmniAuth::Builder do
     provider :docusign, config.integration_key, config.integration_secret, setup: lambda { |env|
       strategy = env['omniauth.strategy']
       strategy.options[:client_options].site = config.app_url
       strategy.options[:prompt] = 'login'
       strategy.options[:oauth_base_uri] = config.authorization_server
       strategy.options[:target_account_id] = config.target_account_id
       strategy.options[:client_options].authorize_url = "#{strategy.options[:oauth_base_uri]}/oauth/auth"
       strategy.options[:client_options].user_info_url = "#{strategy.options[:oauth_base_uri]}/oauth/userinfo"
       strategy.options[:client_options].token_url = "#{strategy.options[:oauth_base_uri]}/oauth/token"
       strategy.options[:authorize_params].prompt = strategy.options.prompt
     }
   end
   ```
3. Add the following redirect route to existing routes in
   [config/routes.rb](https://github.com/docusign/code-examples-ruby/blob/master/config/routes.rb#L173):

   ```
   # Handle OmniAuth OAuth2 login callback result that includes the AuthHash
   get '/auth/:provider/callback', to: 'session#create'
   ```
4. Edit
   `create` action in your
   [SessionController](https://github.com/docusign/code-examples-ruby/blob/main/app/controllers/session_controller.rb):

   ```
   class SessionController < ApplicationController
     def create
       Rails.logger.debug "\n==> Docusign callback Authentication response:\n#{auth_hash.to_yaml}\n"
       Rails.logger.info "==> Login: New token for admin user which will expire at: #{Time.at(auth_hash.credentials['expires_at'])}"
       redirect_to redirect_url
     end
   ```

   ```
     # returns hash with key structure of:
     # provider
     # uid
     # info: [name, email, first_name, last_name]
     # credentials: [token, refresh_token, expires_at, expires]
     # extra: [sub, account_id, account_name, base_uri]
     def auth_hash
       @auth_hash ||= request.env['omniauth.auth']
     end
   end
   ```

## JSON Web Tokens (JWT) with Ruby

Every Ruby SDK (eSignature as well as others) includes two JWT Grant methods:

`request_jwt_user_token`: This method uses the JWT Grant flow to request a token that will represent a specific user. This JWT Grant flow is used for all eSignature REST API methods and for most other Docusign API methods as well.

`request_jwt_application_token`: This method uses the JWT Grant flow to request a token that will represent the application itself (not a user). This JWT Grant flow is useful for specific Docusign partners who are part of special Docusign programs allowing them to manage accounts using the
[Docusign Admin API](https://developers.docusign.com/docs/admin-api/).

### Configuration information required to proceed with JWT

- **Integration key (client ID)**: This can be obtained in your developer account from the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. See the
  [Administration Guide](https://support.docusign.com/guides/ndse-admin-guide-api-and-keys) for more information.
- **RSA private key**: This is for the integration key you obtained above and can also be created in the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. You only need the private key, and it can only be copied once, if you use the administration tool to create it. Make sure to retain it for your records.
- **Base path**: To use either JWT Grant method, you need to use an SDK
  `ApiClient` object. To create an
  `ApiClient` object, you need to provide a
  `base_path` attribute. Since the application’s correct base path is not yet known, use placeholder values to indicate which system should be queried:

  - `https://demo.docusign.net/restapi # development`
  - `https://www.docusign.net/restapi # production`

  **Note:** This placeholder base path is used only for the
  `ApiClient`
  `request_jwt_user_token`,
  `request_jwt_application_token`, and
  `get_user_info` methods. Once you make these calls, you should be able to get the correct base path and use it to make all other API calls.
- **Impersonated User ID** : This is a GUID identifying the Docusign user that you will be impersonating with the access token. Your own
  **User ID** can be found at the top of the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page.

  User IDs for other members of your account can be looked up via the
  [Users](https://admindemo.docusign.com/authenticate?goTo=users) page. Locate the user in the list; then use the
  **Actions > Edit** command to open the user’s
  **Profile** page. The user’s user ID is shown on the page as the
  **User ID** value.

  User IDs can also be looked up programmatically by using the
  `Users: list` method. It requires administrative permissions.

  This parameter is not used for the
  `request_jwt_application_token` method.
- **Scopes**: These represent the OAuth scopes (permissions) that are being requested. For eSignature REST API methods, use the
  `signature` scope. The
  `impersonation` scope is implied by the JWT Grant operation and does not need to be included. If the access token will be used for other Docusign APIs, additional scopes may be required; see each API’s
  [authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/) requirements.
- **Parameter formats and additional parameters** are documented in the
  [Ruby SDK](https://docusign.github.io/docusign-esign-ruby-client/).

User IDs for everyone in your account are available on the account administrator’s
[Users](https://admindemo.docusign.com/authenticate?goTo=users) page.

[JWT Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/) enables developers to obtain OAuth access tokens without requiring users to log in, given that they have already
[provided consent](https://www.docusign.com/blog/developers/oauth-jwt-granting-consent) for the application to impersonate them when making API calls.

To use JWT from the Ruby SDK, make the following call (you can find this code in
[GitHub](https://github.com/docusign/code-examples-ruby/blob/master/app/services/jwt_auth/jwt_creator.rb#L57)):

```
    token = api_client.request_jwt_user_token(Rails.configuration.jwt_integration_key, Rails.configuration.impersonated_user_guid, rsa_pk, expires_in=3600, "signature impersonation")
```

Best practices for managing access tokens:

- Do cache the access token until it expires or is about to expire.
- Do not create a new access token for each API call.
- Recommended: Check the expiration time of the access token before you use it. If it has expired or is about to expire (within 10 minutes), then obtain a new authorization token before making the API call. (If using a refresh token, check that it hasn’t expired as well.)

## Obtaining user information

Once authenticated, you need information about the access token’s user. That information is required to make future API calls. Moreover, it’s possible that the user is a member of more than one Docusign account. In this scenario, you can obtain all of the accounts associated with this user to enable them to pick which Docusign account they wish to use with your integration.

The recommended practice (frequently used by Docusign apps) is to use the user’s default account and let them change to use a different account.

The recommended practice from the partner group is to include the
`account_id` as a configuration value since the API application may require specific account settings. In this case, the app should check that the user has access to the configured
`account_id`.

The Ruby code to retrieve the
[user information](https://developers.docusign.com/platform/auth/reference/user-info/) from the developer account is:

```
    user_info_response = api_client.get_user_info(token.access_token)
```

The
[get\_user\_info](https://github.com/docusign/docusign-ruby-client/blob/master/lib/docusign_esign/client/api_client.rb#L538) function returns a
[UserInfo](https://github.com/docusign/docusign-ruby-client/blob/master/lib/docusign_esign/client/auth/oauth.rb#L818) object that has various pieces of information related to the user. The
[accounts](https://github.com/docusign/docusign-ruby-client/blob/master/lib/docusign_esign/client/auth/oauth.rb#L863) property is a list of
[Account](https://github.com/docusign/docusign-ruby-client/blob/master/lib/docusign_esign/client/auth/oauth.rb#L23) objects that provides the collection of Docusign accounts and their information. You can use the
`is_default` property of the
`Account` object to check if this is the user’s default account. The
`UserInfo` object also includes
`name` and
`email` properties related to the logged-in user.

The
`Account` object also includes the
`base_uri` property. The
`base_uri` property forms the first term of the URL you must use to make API calls on behalf of the user’s account. Since each Docusign account is associated with a specific Docusign data center, the
`base_uri` property includes the data center’s designation, such as na2.docusign.net or eu.docusign.net, like so: https://na2.docusign.net. The
`base_uri` property’s value is concatenated with the string “/restapi” to form the base path, which represents the root of the URL for all endpoints in the eSignature REST API, for example: https://na2.docusign.net/restapi.

When you instantiate the
`ApiClient` object, which is used to make API calls, you pass the value of the base path in its constructor (see below). If you reuse an
`ApiClient` object, use its
`set_base_path` method to ensure the correct base path is set.

## Instantiating and configuring the ApiClient for making API calls

The
`ApiClient` class represents the base object used as a starting point for all eSignature API calls. You will have to instantiate this object in your code before you can proceed to make API calls.

The basic flow of instantiating an
`ApiClient` looks like this:

```
    configuration = Docusign_eSign::Configuration.new
    configuration.host = base_path
    api_client = Docusign_eSign::ApiClient.new configuration
    api_client.default_headers['Authorization'] = "Bearer #{access_token}"
    envelopes_api = Docusign_eSign::EnvelopesApi.new api_client
```

Let’s break down these five lines of code to understand them better.

### Instantiating a Configuration object

```
    configuration = Docusign_eSign::Configuration.new
```

The
`Configuration` object holds settings to be used in the API client and is used to instantiate a new
`ApiClient` object.

### Setting the base path

```
    configuration.host = base_path
```

This
`base_path` parameter tells the SDK the first part of the URL to use when making API calls. The latter part of the URL is determined in each API call by the specific classes and methods you choose to use.

The base path for the developer (demo) environment is https://demo.docusign.net. The base path for the production environment depends on the specific data center where your account is provisioned.

The base path for the eSignature REST API consists of the name of the data center (demo, na2, na3, eu1, ca, au etc.) and then .docusign.net.

### Instantiating the ApiClient object

```
    api_client = Docusign_eSign::ApiClient.new configuration
```

This line is used to instantiate a new
`ApiClient` object using the above configuration. This object is used to make eSignature API calls to Docusign.

### Setting the HTTP header with an authentication token

```
    api_client.default_headers['Authorization'] = "Bearer #{args[:access_token]}"
```

This line is used to provide the authentication information required to make API calls. You first need to obtain a valid access token for authentication. You can find out how to obtain a token from the how-to topics for
[Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/confidential-authcode-get-token/),
[Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/), and
[JWT Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/).

The
[set\_default\_header](https://github.com/docusign/docusign-esign-ruby-client/blob/master/lib/docusign_esign/client/api_client.rb#L584) method sets the
`default_headers` attribute of the
`ApiClient` class. The
`default_headers` attribute is a hash that is used to provide additional HTTP headers for API requests. You can add additional headers to be used with API calls that use the
`ApiClient` object. The
`"Authorization"` header is used to provide the authentication information for the request. The token is added after the word
`"Bearer"`, provided in the
`access_token` variable. This only needs to be done once for all API calls that will be utilizing the same
`ApiClient` object; however, the token is only valid for eight hours. You will need to obtain a new one and update this header when the token expires.

### Instantiating the required object for the specific set of API calls

```
    envelopes_api = Docusign_eSign::EnvelopesApi.new api_client
```

This is an example of how to use the
`ApiClient` object. It is used as a parameter on the constructors of all the API classes. By instantiating the
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
