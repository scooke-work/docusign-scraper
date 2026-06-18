---
title: Java SDK authentication
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/java/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- Java
- Java
- Authentication
scraped_at: '2026-06-18T20:28:15Z'
---

# Java SDK authentication

Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run eSignature REST API code examples.

## Obtaining an access token

The goal of [authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/) is to obtain an access token. An access token is needed for every API call to Docusign. Access tokens last from one to eight hours, depending on the grant type used to obtain the access token.

## Determining your OAuth flow

Please review the [Platform Authentication 101](https://developers.docusign.com/platform/auth/) documentation on the Developer Center to determine which OAuth flow to use.

## Authorization Code Grant with Java

Because the OAuth Authorization Code Grant flow is centered on interactions between the user and the identity server via the browser, the SDK is not used.

### Configuration information required to proceed with Authorization Code Grant

- **Integration key** (client ID): This can be obtained in your developer account by accessing the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. See the [Administration Guide](https://support.docusign.com/guides/ndse-admin-guide-api-and-keys) for more information.
- **Client secret**: This is for the integration key you obtained above. It is also created in the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. The client secret can only be copied the first time it is displayed; it will not be visible later. Make sure to retain it for your records. If you forget your client secret, you can generate a new one to use.
- **Redirect/Callback URI**: This is the URI to which the end user will be redirected when your application uses the Authorization Code Grant flow. That URI must exactly match one of the redirect URIs you define for your integration key in the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. You can add multiple redirect URIs for a single integration key.

Authorization Code Grant requires a web interface because users must utilize the Docusign Identity Provider (IdP) to authenticate with their Docusign account. In this section we’ll cover the recommended practices for using Authorization Code Grant with Java applications. Other Java web technologies may require a different technique to complete the Authorization Code Grant flow and are beyond the scope of this guide.

### Using Authorization Code Grant with [Spring Boot](https://spring.io/quickstart) web applications

1. Add a config override method in your WebSecurityConfig.file

   ```
       @Override
       protected void configure(HttpSecurity http) throws Exception {
           http.apply(authCodeGrantFilter());
       }
   ```
2. Add the following `OAuth2ClientAuthenticationProcessingFilter` method to enable Docusign Authorization Code Grant flow to work with your application (you can find a full working example in our [GitHub repository](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/WebSecurityConfig.java#L100)):

   ```
       private OAuth2ClientAuthenticationProcessingFilter authCodeGrantFilter() {
       OAuth2SsoProperties authCodeGrantSso = authCodeGrantSso();
       AuthorizationCodeResourceDetails authCodeGrantClient = authCodeGrantClient();

       authCodeGrantClient.setScope("signature");

       ResourceServerProperties userInfoResource = userInfoResource();
       OAuth2ClientAuthenticationProcessingFilter filter =
           new OAuth2ClientAuthenticationProcessingFilter(authCodeGrantSso.getLoginPath());
       OAuth2RestTemplate restTemplate = new OAuth2RestTemplate(authCodeGrantClient, oAuth2ClientContext);
       filter.setRestTemplate(restTemplate);
       ResourceServerTokenServices tokenServices = new UserInfoTokenServices(userInfoResource.getUserInfoUri(),
           authCodeGrantClient.getClientId());
       filter.setTokenServices(tokenServices);
       return filter;
   }
   ```
3. Drop in a method to retrieve and redirect the resulting OAuth Login to the code grant IdP server:

   ```
       private String getLoginPath(AuthType authTypeSelected) {
           OAuthProperties oAuth2SsoProperties = authCodeGrantSso;
           return oAuth2SsoProperties.getLoginPath();
       }
   ```

   This `getLoginPath` method above can be used from any controller to start the Authorization Code Grant process to obtain an access token.

## JSON Web Tokens (JWT) with Java

Every [Java SDK](https://developers.docusign.com/docs/esign-rest-api/sdks/java/) (eSignature as well as others) includes two JWT Grant methods:

[RequestJWTUserToken](https://github.com/docusign/docusign-java-client/blob/master/src/main/java/com/docusign/esign/client/ApiClient.java#L826): This method uses the JWT Grant flow to request a token that will represent a specific user. This JWT Grant flow is used for all eSignature REST API methods and for most other Docusign API methods as well.

[RequestJWTApplicationToken](https://github.com/docusign/docusign-esign-java-client/blob/master/src/main/java/com/docusign/esign/client/ApiClient.java#L899): This method uses the JWT Grant flow to request a token that will represent the application itself (not a user). This JWT Grant flow is useful for specific Docusign partners who are part of special Docusign programs allowing them to manage accounts using the [Docusign Admin API](https://developers.docusign.com/docs/admin-api/).

### Configuration information required to proceed with JWT

- **Base path:** To use either JWT Grant method, you need to use an SDK `ApiClient` object. To create an `ApiClient` object, you need to provide a `basePath` attribute. Since the application’s correct base path is not yet known, use placeholder values to indicate which system should be queried:

- `https://demo.docusign.net/restapi # development`
- `https://www.docusign.net/restapi # production`

You can find the above URLs in the following two public constants:

```` ```
    ApiClient.PRODUCTION_REST_BASEPATH
    ApiClient.DEMO_REST_BASEPATH
``` ````

**Note:** This placeholder base path is used only for the `ApiClient RequestJWTUserToken`, `RequestJWTApplicationToken`, and `GetUserInfo` methods. Once you make these calls, you should be able to get the correct base path and use it to make all other API calls.

- **Integration key (client ID):** This can be obtained in your developer account from the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. See the [Administration Guide](https://support.docusign.com/guides/ndse-admin-guide-api-and-keys) for more information.
- **RSA private key:** This is for the integration key you obtained above and can also be created in the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page. You only need the private key, and it can only be copied once if you use the administration tool to create it. Make sure to retain it for your records.
- **Impersonated User ID:** This is a GUID identifying the Docusign user that you will be impersonating with the access token. Your own **User ID** can be found at the top of the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page.

  User IDs for other members of your account can be looked up on the [Users](https://admindemo.docusign.com/authenticate?goTo=users) page. Locate the user in the list; then use the **Actions > Edit** command to open the user’s **Profile** page. The user’s user ID is shown on the page as the **User ID** value.

  User IDs can also be looked up programmatically by using the [Users: list](https://developers.docusign.com/docs/esign-rest-api/reference/users/users/list/) method. It requires administrative permissions.

  This parameter is not used for the `RequestJWTApplicationToken` method.
- **Scopes:** These represent the OAuth scopes (permissions) that are being requested. For eSignature REST API methods, use the `signature` scope. The `impersonation` scope is implied by the JWT Grant operation and does not need to be included. If the access token will be used for other Docusign APIs, additional scopes may be required; see each API’s [authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/) requirements.
- **Parameter formats and additional parameters** are documented in the [Java SDK Reference](https://javadoc.io/doc/com.docusign/docusign-esign-java/latest/index.html).

User IDs for everyone in your account are available on the account administrator's [Users](https://admindemo.docusign.com/authenticate?goTo=users) page.

[JWT Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/) enables developers to obtain OAuth access tokens without requiring users to log in, given that they have already [provided consent](https://www.docusign.com/blog/developers/oauth-jwt-granting-consent) for the application to impersonate them when making API calls.

To use JWT from the Java SDK, simply make the following call (you can find this code in [GitHub](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/core/security/jwt/JWTAuthenticationMethod.java)):

```
public class JWTAuthenticationMethod {

    public static final String CONSENT_REQUIRED = "consent_required";

    private static final long TOKEN_EXPIRATION_IN_SECONDS = 3600;

    public static final String REQUEST_CONSENT_LINK = "https://%s/oauth/auth?prompt=login&response_type=code&scope=%s&client_id=%s&redirect_uri=%s";

    public static final String CONSENT_REDIRECT_URL = "http://localhost:8080/login/oauth2/code/jwt";

    public RedirectView loginUsingJWT(
            DSConfiguration configuration,
            Session session,
            String redirectURL) {
        List<String> scopes = new ArrayList<>();
        for(var scope : ApiType.values()){
            scopes.addAll(Arrays.asList(scope.getScopes()));
        }

        try {
            ApiClient apiClient = new ApiClient(configuration.getBasePath());
            byte[] privateKeyBytes = Files.readAllBytes(Paths.get(configuration.getPrivateKeyPath()));

            OAuth.OAuthToken oAuthToken = apiClient.requestJWTUserToken(
                    configuration.getUserId(),
                    configuration.getImpersonatedUserId(),
                    scopes,
                    privateKeyBytes,
                    TOKEN_EXPIRATION_IN_SECONDS);
            String accessToken = oAuthToken.getAccessToken();
            OAuth.UserInfo userInfo = apiClient.getUserInfo(accessToken);
            String accountId = userInfo.getAccounts().size() > 0 ?
                    userInfo.getAccounts().get(0).getAccountId()
                    : "";

            setSpringSecurityAuthentication(scopes, oAuthToken, userInfo, accountId, session);
        }
        catch (ApiException | IOException exp)
        {
            if (exp.getMessage().contains(CONSENT_REQUIRED))
            {
                String consent_scopes = String.join("%20", scopes) + "%20impersonation";

                var consent_url = String.format(
                    REQUEST_CONSENT_LINK,
                    configuration.getBaseURL(),
                    consent_scopes,
                    configuration.getUserId(),
                    CONSENT_REDIRECT_URL);

                System.err.println("\nC O N S E N T   R E Q U I R E D" +
                    "\nAsk the user who will be impersonated to run the following URL: " +
                    "\n" + consent_url +
                    "\n\nIt will ask the user to login and to approve access by your application." +
                    "\nAlternatively, an Administrator can use Organization Administration to" +
                    "\npre-approve one or more users.");

                configuration.setIsConsentRedirectActivated(true);

                return new RedirectView(consent_url);
            }
        }

        return new RedirectView(redirectURL);
    }

    private void setSpringSecurityAuthentication(
            List<String> scopes,
            OAuth.OAuthToken oAuthToken,
            OAuth.UserInfo userInfo,
            String accountId,
            Session session) {
        JWTOAuth2User principal = new JWTOAuth2User();
        principal.setAuthorities(scopes);
        principal.setCreated(userInfo.getCreated());
        principal.setName(userInfo.getName());
        principal.setGivenName(userInfo.getGivenName());
        principal.setFamilyName(userInfo.getFamilyName());
        principal.setSub(userInfo.getSub());
        principal.setEmail(userInfo.getEmail());
        principal.setAccounts(userInfo.getAccounts());
        principal.setAccessToken(oAuthToken);

        session.setTokenExpirationTime(System.currentTimeMillis() + oAuthToken.getExpiresIn() * 1000L);

        OAuth2AuthenticationToken token = new OAuth2AuthenticationToken(principal, principal.getAuthorities(), accountId);
        SecurityContextHolder.getContext().setAuthentication(token);
    }
}
```

Best practices for managing access tokens:

- Do cache the access token until it expires or is about to expire.
- Do not create a new access token for each API call.
- Recommended: Check the expiration time of the access token before you use it. If it is expired or about to expire (within 10 minutes), then obtain a new authorization token before making the API call. (If using a refresh token, check that it hasn’t expired as well.)

## Obtaining user information

Once authenticated, you need information about the access token’s user. That information is required to make future API calls. Moreover, it’s possible that the user is a member of more than one Docusign account. In this scenario, you can obtain all of the accounts associated with this user to enable them to pick which Docusign account they wish to use with your integration.

The recommended practice (frequently used by Docusign apps) is to use the user’s default account and let them change to use a different account.

The recommended practice from the partner group is to include the `accountId` as a configuration value since the API application may require specific account settings. In this case, the app should check that the user has access to the configured `accountId`.

The Java code to retrieve the [user information](https://developers.docusign.com/platform/auth/reference/user-info/) object in the developer account is:

```
    apiClient = new ApiClient();
    UserInfo userInfo = apiClient.getUserInfo(oAuthToken.getAccessToken());
```

The [getUserInfo](https://github.com/docusign/docusign-java-client/blob/master/src/main/java/com/docusign/esign/client/ApiClient.java#L664) function returns a [UserInfo](https://github.com/docusign/docusign-java-client/blob/master/src/main/java/com/docusign/esign/client/auth/OAuth.java#L708) object that has various pieces of information related to the user. The [accounts](https://github.com/docusign/docusign-java-client/blob/master/src/main/java/com/docusign/esign/client/auth/OAuth.java#L717)property is a list of [Account](https://github.com/docusign/docusign-java-client/blob/master/src/main/java/com/docusign/esign/client/auth/OAuth.java#L536) objects that provide the collection of Docusign accounts and their information. You can use the `isDefault` property of the `Account` object to check if this is the user’s default account. The [UserInfo](https://github.com/docusign/docusign-java-client/blob/master/src/main/java/com/docusign/esign/client/auth/OAuth.java#L708) object also includes the `name` and `email` properties related to the logged-in user.

The `Account` object also includes the `baseUri` property. The `baseUri` property forms the first term of the URL you must use to make API calls on behalf of the user's account. Since each Docusign account is associated with a specific Docusign data center, the `baseUri` property includes the data center's designation, such as na2.docusign.net or eu.docusign.net, like so: https://na2.docusign.net. The `baseUri` property's value is concatenated with the string "/restapi" to form the base path, which represents the root of the URL for all endpoints in the eSignature REST API, for example: https://na2.docusign.net/restapi.

When you instantiate the `ApiClient` object, which is used to make API calls, you pass the value of the base path in its constructor (see below). If you reuse an `ApiClient` object, use its `setBasePath` method to ensure the correct base path is set.

## Instantiating and configuring the ApiClient for making API calls

The `ApiClient` class represents the base object used as a starting point for all eSignature API calls. You will have to instantiate this object in your code before you can proceed to make API calls.

The basic flow of instantiating the `ApiClient` looks like this:

```
    ApiClient apiClient = new ApiClient(basePath);
    apiClient.addDefaultHeader("Authorization", "Bearer " + accessToken);
    EnvelopesApi envelopesApi = new EnvelopesApi(apiClient);
```

Let’s break down these three lines of code to understand them better.

### Instantiating the ApiClient object

```
    ApiClient apiClient = new ApiClient(basePath);
```

This line is used to instantiate a new `ApiClient` object. This object is used to make eSignature API calls to Docusign.

### Setting the base path

The only required parameter for the `ApiClient` object is a `basePath`. The `basePath` tells the SDK the first part of the URL to use when making API calls. The latter part of the URL is determined in each API call by the specific classes and methods you choose to use.

The base path for the developer (demo) environment is https://demo.docusign.net/restapi. The base path for the production environment depends on the specific data center where your account is provisioned.

The base path for the eSignature REST API consists of the name of the data center (demo, na2, na3, eu1, ca, au etc.) and then .docusign.net/restapi.

### Setting the HTTP header with authentication token

```
    apiClient.addDefaultHeader("Authorization", "Bearer " + accessToken);
```

This line is used to provide the authentication information required to make API calls. You first need to obtain a valid access token for authentication. You can find out how to obtain a token from the how-to topics for [Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/confidential-authcode-get-token/), [Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/), and [JWT Grant](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/).

`defaultHeader` is a `Map` that is used to provide additional HTTP headers for API requests. You can add additional headers to be used with API calls that use the `ApiClient` object. The "`Authorization"` header is used to provide the authentication information for the request. The token is added after the word "`Bearer"`, provided in the `accessToken` variable. This only needs to be done once for all API calls that will be utilizing the same `ApiClient` object; however, the token is only valid for up to eight hours. You will need to obtain a new one and update this header when the token expires.

### Instantiating the required object for the specific set of API calls

```
    EnvelopesApi envelopesApi = new EnvelopesApi(apiClient);
```

This is an example of how to use the `ApiClient` object. It is used as a parameter on the constructors of all the API classes under the `com.docusign.esign` namespace. By instantiating the `EnvelopesApi` class to use the preconfigured `ApiClient`, you are ready to make API calls.

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
