---
title: C# SDK authentication
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/csharp/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- Csharp
- Csharp
- Authentication
scraped_at: '2026-06-18T21:09:54Z'
---

# C# SDK authentication

## Obtaining an access token

The goal of [authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/) is to obtain an access token. An access token is needed for every API call to Docusign. Access tokens last from one to eight hours, depending on the grant type used to obtain the access token.

## Determining your OAuth flow

Please review the [Platform Authentication 101](https://developers.docusign.com/platform/auth/) documentation on the Developer Center to determine which OAuth flow to use.

## Authorization Code Grant with C#

Because the
[OAuth Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/) flow is centered on interactions between the user and the identity server via the browser, the SDK is not used.

### Configuration information required to proceed with Authorization Code Grant

- **Integration key** (client ID): This can be obtained in your developer account by accessing the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. See the
  [Docusign eSignature Admin Guide](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=pmp1583277397015.html) for more information.
- **Client secret**: This is for the integration key you obtained above. It is also created on the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. The client secret can only be copied the first time it is displayed; it will not be visible later. Make sure to retain it for your records. If you forget your client secret, you can generate a new one to use.
- **Redirect/Callback URI**: This is the URI to which the end user will be redirected when your application uses the Authorization Code Grant flow. That URI must exactly match one of the redirect URIs you defined for your integration key on the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. You can add multiple redirect URIs for a single integration key.

Authorization Code Grant requires a web interface because users must use the Docusign Identity Provider (IdP) to authenticate with their Docusign account. In this section, we’ll cover two common C# web project scenarios and the recommended practices for using Authorization Code Grant with each of them. Other C# web technologies may require a different technique to complete the Authorization Code Grant flow and are beyond the scope of this guide.

### Using Authorization Code Grant with your ASP.NET Core web application

1. When using an ASP.NET Core web application, you can add the following code to your startup.cs file in the
   `ConfigureServices()` method to enable Docusign Authorization Code Grant flow to work with your application. You can find a full working example in our
   [GitHub repository](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Startup.cs#L90).

   ```
       .AddOAuth("Docusign", options =>
       {
           options.ClientId = Configuration["Docusign:ClientId"];
           options.ClientSecret = Configuration["Docusign:ClientSecret"];
           options.CallbackPath = new PathString("/ds/callback");
           options.AuthorizationEndpoint = "https://account-d.docusign.com/oauth/auth";
           options.TokenEndpoint = "https://account-d.docusign.com/oauth/token";
           options.UserInformationEndpoint = "https://account-d.docusign.com/oauth/userinfo";
       }
   ```
2. Add a controller with a method that looks like this:

   ```
       public IActionResult Login(string authType = "CodeGrant", string returnUrl = "/")
       {
           if (authType == "CodeGrant")
           {
               return Challenge(new AuthenticationProperties() { RedirectUri = returnUrl });
           }
       }
   ```

This
`Login()` method can be used from any controller to start the Authorization Code Grant process and obtain an access token.

### Using Authorization Code Grant with your ASP.NET MVC .NET Framework application

When using an ASP.NET MVC .NET Framework application (not .NET Core), we highly recommend that you use the Open Web Interface (OWIN) package provided by Microsoft to complete the OAuth process.

1. Add the [Microsoft.OWIN NuGet](https://www.nuget.org/packages/Microsoft.Owin/) to your project to use its functionality.
2. You then have to add a file called DSOwinStartup.cs and include a public method called `ConfigureAuth()`. You can find the
   [full code in GitHub](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Common/AuthCodeGrant.cs#L39):

   ```
       public void ConfigureAuth(IAppBuilder app)
       {
           app.UseCookieAuthentication(new CookieAuthenticationOptions());
           app.UseExternalSignInCookie(DefaultAuthenticationTypes.ExternalCookie);
           app.Use(typeof(DocusignAuthenticationMiddleware), app, new DocusignAuthenticationOptions
           {
               ClientId = ConfigurationManager.AppSettings["IntegrationKey"],
               ClientSecret = ConfigurationManager.AppSettings["SecretKey"],
               AuthorizationEndpoint = "https://account-d.docusign.com/oauth/auth",
               TokenEndpoint = "https://account-d.docusign.com/oauth/token",
               UserInformationEndpoint = "https://account-d.docusign.com/oauth/userinfo",
               AppUrl = ConfigurationManager.AppSettings["AppUrl"],
               CallbackPath = new PathString("/ds/Callback")
           });
       }
   ```
3. In DSOwinStartup.cs, add the following line above the namespace declaration:

   ```
       [assembly: Microsoft.Owin.OwinStartupAttribute(typeof(.DocuSign.eSignature.DSOwinStartup))]

   ```

You will need to use ASP.NET MVC filters to enable your controller to obtain the access token. You can use the [GitHub code](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Common/AuthCodeGrant.cs) used by the [Docusign Visual Studio Extension](https://marketplace.visualstudio.com/items?itemName=Docusign.DocusignVSExtension) as an example.

## JSON Web Tokens (JWT) with C#

Every C# SDK (eSignature as well as others) includes two JWT Grant methods:

- [RequestJWTUserToken](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L997): This method uses the JWT Grant flow to request a token that will represent a specific user. This JWT Grant flow is used for all eSignature REST API methods and for most other Docusign API methods as well.
- [RequestJWTApplicationToken](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L1108): This method uses the JWT Grant flow to request a token that will represent the application itself (not a user). This JWT Grant flow is useful for specific Docusign partners who are part of special Docusign programs allowing them to manage accounts using the
  [Docusign Admin API](https://developers.docusign.com/docs/admin-api/).

### Configuration information required to proceed with JWT

- **Integration key (client ID)**: This can be obtained in your developer account from the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. See the
  [Docusign eSignature Admin Guide](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=pmp1583277397015.html) for more information.
- **RSA private key**: This is for the integration key you obtained above and can also be created on the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. You only need the private key, and it can only be copied once. Make sure to retain it for your records. Different formats can be used for the private key.
- **Base path**: To use either JWT Grant method, you need to use an SDK
  `DocuSignClient` object. To create an
  `DocuSignClient` object, you need to provide a base path. Since the application’s correct base path is not yet known, use placeholder values to indicate which system should be queried:

  - `https://demo.docusign.net/restapi # development`
  - `https://www.docusign.net/restapi # production`

  You can find the above URLs in the following
  [two public constants](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L41):

  ```
      DocuSignClient.Production_REST_BasePath
      DocuSignClient.Demo_REST_BasePath
  ```

  **Note:** This placeholder base path is used only for the
  `DocuSignClient`
  [RequestJWTUserToken](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L997),
  [RequestJWTApplicationToken](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L1108), and
  [GetUserInfo](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L883) methods. Once you make these calls, you should be able to get the correct base path and use it to make all other API calls.
- **Impersonated User ID (UserID)**: This is a GUID identifying the Docusign user that you will be impersonating with the access token. Your own
  **User ID** and can be found at the top of the
  [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page.

  User IDs for other members of your account can be looked up via the
  [Users](https://admindemo.docusign.com/authenticate?goTo=users) page. Locate the user in the list; then use the
  **Action > Edit** button to open the user’s
  **Profile** page. The user’s user ID is shown on the page as the
  **User ID** value.

  User IDs can also be looked up programmatically by using the
  [Users:list](https://developers.docusign.com/docs/esign-rest-api/reference/users/users/list/) method. It requires administrative permissions.

  This parameter is not used for the
  [RequestJWTApplicationToken](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L1105) method.
- **Scopes**: These represent the OAuth scopes (permissions) that are being requested. For eSignature REST API methods, use the `signature` scope. The `impersonation` scope is implied by the JWT Grant operation and does not need to be included. If the access token will be used for other Docusign APIs, additional scopes may be required; see each API’s [authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/) requirements.
- **Parameter formats and additional parameters** are documented in the [C# SDK](https://docusign.github.io/docusign-esign-csharp-client/).

User IDs for everyone in your account are available on the account administrator’s [Users](https://admindemo.docusign.com/authenticate?goTo=users) page.

[JWT Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/) enables developers to obtain OAuth access tokens without requiring users to log in, given that they have already [provided consent](https://www.docusign.com/blog/developers/oauth-jwt-granting-consent) for the application to impersonate them when making API calls.

To use JWT from the C# SDK, you simply have to make the following call (you can find this code in [GitHub](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Common/RequestItemsService.cs)):

```
    // We don’t yet know our base path, so indicate which Docusign
    // identity server (demo or production) should be used by
    // setting basePath to a placeholder value for use with the
    // RequestJWTUserToken and GetUserInfo methods
    var devPlaceholder = "https://demo.docusign.net/restapi" // dev
    var prodPlaceholder = "https://www.docusign.net/restapi" // production
    var _apiClient = new ApiClient(devPlaceholder);
    authToken = _apiClient.RequestJWTUserToken(
    _configuration["DocusignJWT:ClientId"],
    _configuration["DocusignJWT:ImpersonatedUserId"],
    "account-d.docusign.com",
    DSHelper.ReadFileContent(DSHelper.PrepareFullPrivateKeyFilePath(this._configuration["DocusignJWT:PrivateKeyFile"])), 1, "impersonation signature");
```

Best practices for managing access tokens:

- Do cache the access token until it expires or is about to expire.
- Do not create a new access token for each API call.
- Recommended: Check the expiration time of the access token before you use it. If it is expired or about to expire (within 10 minutes), then obtain a new authorization token before making the API call. If using a refresh token, check that it hasn’t expired as well.

## Obtaining user information

Once authenticated, you need information about the access token’s user. That information is required to make future API calls. Moreover, it’s possible that the user is a member of more than one Docusign account. In this scenario, you can obtain all accounts associated with this user to enable them to pick which Docusign account they wish to use with the integration.

The recommended practice (frequently used by Docusign apps) is to use the user’s default account and let them change to use a different account.

Recommended practice from the partner group is to include the `accountId` as a configuration value since the API application may require specific account settings. In this case, the app should check that the user has access to the configured `accountId`.

The C# code to retrieve the [user information](https://developers.docusign.com/platform/auth/reference/user-info/) object in the developer account is:

```
    UserInfo userInfo = DocuSignClient.GetUserInfo(accessToken);
```

The [GetUserInfo](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L883) function returns a [UserInfo](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/Auth/OAuth.cs#L59) object has various pieces of information related to the user. The [List<Account> Accounts](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/Auth/OAuth.cs#L464) object provides the collection of Docusign accounts and their information. You can use the `IsDefault` property of the `Account` object to check if this is the user’s default account. The `UserInfo` object also includes the `Name` and `Email` properties related to the logged-in user.

The `Account` object also includes the `BaseUri` property. The `BaseUri` property forms the first term of the URL you must use to make API calls on behalf of the user's account. Since each Docusign account is associated with a specific Docusign data center, the `BaseUri` property includes the data center's designation, such as na2.docusign.net or eu.docusign.net, e.g., https://na2.docusign.net. The `BaseUri` property's value is concatenated with the string "/restapi" to form the base path, which represents the root of the URL for all endpoints in the eSignature REST API, e.g., https://na2.docusign.net/restapi.

When you instantiate the `DocuSignClient` object, which is used to make API calls, you pass the value of the base path in its constructor (see below). If you reuse an `DocuSignClient` object, use its [SetBasePath](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L757) method to ensure the correct base path is set.

## Instantiating and configuring the DocuSignClient for making API calls

The `DocuSignClient` class represents the base object used as a starting point for all eSignature API calls. You will have to instantiate this object in your code before you can proceed to make API calls.

If you are using the Docusign eSignature REST C# SDK version 5.0.0 or above, the basic flow of instantiating the DocuSignClient looks like this:

```
    var DocuSignClient = new DocuSignClient(basePath);
    DocuSignClient.Configuration.DefaultHeader.Add("Authorization", "Bearer " + accessToken);
    var envelopesApi = new EnvelopesApi(DocuSignClient);
```

Let’s break down these three lines of code to understand them better.

### Instantiating the DocuSignClient object

```
    var DocuSignClient = new DocuSignClient(basePath);
```

This line is used to instantiate a new `DocuSignClient` object. This object is used to make eSignature API calls to Docusign.

The only required parameter for the constructor is a `basePath`. The `basePath` parameter tells the SDK the first part of the URL to use when making API calls. The latter part of the URL is determined in each API call by the specific classes and methods you choose to use.

The base path for the developer (demo) environment is https://demo.docusign.net/restapi. The base path for the production environment depends on the specific data center where your account is provisioned.

The base path for the eSignature REST API consists of the name of the data center (demo, na2, na3, eu1, ca, au etc.) and then .docusign.net/restapi.

### Setting the HTTP header with an authentication token

```
    DocuSignClient.Configuration.DefaultHeader.Add("Authorization", "Bearer " + accessToken);
```

This line is used to provide the authentication information required to make API calls. You first need to obtain a valid access token for authentication. You can find out how to obtain a token from the how-to topics for [Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/confidential-authcode-get-token/),
[Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/), and [JWT Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/).

The `Configuration` object is a [singleton](https://en.wikipedia.org/wiki/Singleton_pattern) that is instantiated when the `DocuSignClient` object is created. You do not need to create a new object.

`DefaultHeader` is a collection (a dictionary) that is used to provide additional HTTP headers for API requests. You can add additional headers with API calls that use the `DocuSignClient` object. The `"Authorization"` header is used to provide the authentication information for the request. The token is added after the word `"Bearer"`, provided in the `accessToken` variable. This only needs to be done once for all API calls that will be utilizing the same `DocuSignClient` object; however, the token is only valid for eight hours. You will need to obtain a new one and update this header when the token expires.

### Instantiating the required object for the specific set of API calls

```
    var envelopesApi = new EnvelopesApi(DocuSignClient);
```

This is an example of how to use the `DocuSignClient` object. It is used as a parameter on the constructors of all the API classes under the `DocuSign.eSign.Api` namespace. By instantiating the `EnvelopesApi` class to use the preconfigured `DocuSignClient`, you are ready to make API calls.

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
