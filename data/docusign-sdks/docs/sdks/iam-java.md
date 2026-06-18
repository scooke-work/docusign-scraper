---
title: IAM SDK - Java (beta)
source_url: https://developers.docusign.com/docs/sdks/iam-java/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- SDKs
- SDKs
- Java IAM SDK
scraped_at: '2026-06-18T21:43:09Z'
---

# IAM SDK - Java (beta)

The Docusign Intelligent Agreement Management (IAM) SDKs assist developers in using the Intelligent Agreement Management (IAM) APIs, simplifying common tasks.

This page offers high-level information about the Java SDK and its usage.

## APIs included in this SDK

The IAM SDKs include the following APIs:

- [Workflow Builder API](https://developers.docusign.com/docs/workflow-builder-api/): Trigger and manage Agreement Builder workflows from your own app.
- [Agreement Manager API](https://developers.docusign.com/docs/agreement-manager-api/): Connect AI-extracted data from agreements stored in Agreement Manager into your own app. into your own app.
- [Workspaces API](https://developers.docusign.com/docs/workspaces-api/): Create structured, secure, and scalable agreement workflows.
- [Connected Fields API](https://developers.docusign.com/docs/connected-fields-api/): Discover extension apps that your app can use to validate input as part of the eSignature process.

Additional APIs may be added later; check this page for updates.

## How to obtain the SDK

The easiest way to add the SDK to your Java project is by including the iam-sdk dependency using your preferred build tool.

### Adding the Java SDK to your project using Gradle

Add the following line to your `build.gradle` file inside the `dependencies` block:

```
implementation 'com.docusign:iam-sdk:1.0.0-beta.4'
```

To use a different version, simply update the version number in the string.

After saving your changes, run:

```
./gradlew build
```

This will download the SDK and its dependencies into your local Gradle cache and make them available to your project.

### Adding the Java SDK to your project using Maven

Add the following to your project's `pom.xml` files inside the `<dependencies>` section:

```
<dependency>
    <groupId>com.docusign</groupId>
    <artifactId>iam-sdk</artifactId>
    <version>1.0.0-beta.4</version>
</dependency>
```

To use a different version, adjust the `<version>` tag accordingly.
After updating your `pom.xml`, run the following command to install the dependencies:

```
mvn install
```

This will fetch the SDK and its dependencies into your local Maven repository.

## Getting started with the Java IAM SDK

The best way to learn how to use the Java IAM SDK is to explore the code examples provided by Docusign. You can find the Java code examples in the [code-examples-java](https://github.com/docusign/code-examples-java) public GitHub repository. These code examples can also be part of the ZIP file downloaded when you use the [Quickstart tool](https://developers.docusign.com/docs/esign-rest-api/quickstart/). This tool will also create all the necessary configuration data in your developer account so you’ll be ready to run it.

## Authentication support

Every API call must be [authenticated](https://developers.docusign.com/platform/auth/). The Java IAM SDK provides functionality to simplify the use of authentication for making IAM API calls.

### Obtaining an access token

Before you begin the authentication process, you must create and [configure your app](https://developers.docusign.com/platform/configure-app/). Specifically:

- Create your app and obtain your integration key (client ID).
- Generate a client secret for your app.
- Add your redirect URI to the list of allowed redirect URLs associated with your integration Key.

These settings are required to obtain an authorization code and exchange it for an access token in the steps below, which demonstrate the Confidential Authorization Code Grant flow. Other OAuth flows may require different configuration settings.

#### Step 1: Obtain an authorization code

To call the DocuSign IAM APIs, you must request the appropriate OAuth scopes. The SDK provides predefined constants for [common scope sets](https://github.com/docusign/docusign-iam-java-client/blob/1a4f28e395ff80be8cd0ec209bfe26db33554c6d/src/main/java/com/docusign/iam/sdk/models/components/AuthScope.java). For example, `AuthScope.getAllScopes()` includes all scopes used across the IAM SDK. You can use these helpers or supply your own array of scopes.
If this is the first time this application is requesting an authorization code from this user, the user will be asked to provide consent. Docusign will then redirect them to your specified redirect URI with an authorization code included as a query parameter named `code`.

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

import com.docusign.iam.sdk.models.components.

OAuthBasePath;

import com.docusign.iam.sdk.models.components.

OAuthResponseType;

import com.docusign.iam.sdk.models.components.

AuthScope;

import com.docusign.iam.sdk.utils.auth.

AuthorizationUrlBuilder;

// Create the authorization URL

String consentUrl = AuthorizationUrlBuilder.builder()

.basePath(OAuthBasePath.DEMO)

.responseType(OAuthResponseType.CODE)

.clientId(System.getenv("DOCUSIGN\_CLIENT\_ID"))

.redirectUri(System.getenv

("DOCUSIGN\_REDIRECT\_URI"))

.addScopes(AuthScope.getAllScopes())

.build();

// Direct the user to grant consent

#### Step 2: Exchange an authorization code for an access token

After you obtain the authorization code, you need to use it to get an access token. The SDK provides helper functions to simplify this process. The example below shows the Confidential Authorization Code Grant flow. You can find examples for other supported flows in the SDK repository, including:

- [Authorization Code (public)](https://github.com/docusign/docusign-iam-java-client/blob/main/docs/sdks/auth/README.md#gettokenfrompublicauthcode)
- [JWT Grant](https://github.com/docusign/docusign-iam-java-client/blob/main/docs/sdks/auth/README.md#gettokenfromjwtgrant)

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

import java.util.Scanner;

import com.docusign.iam.sdk.IamClient;

import com.docusign.iam.sdk.models.components.

ConfidentialAuthCodeGrantRequestBody;

import com.docusign.iam.sdk.models.operations.

GetTokenFromConfidentialAuthCodeResponse;

import com.docusign.iam.sdk.models.operations.

GetTokenFromConfidentialAuthCodeSecurity;

try {

// Prompt user for the authorization code

Scanner scanner = new Scanner(System.in);

System.out.print("Enter the authorization code

from the redirect URL: ");

String authCode = scanner.nextLine();

// Create an unauthenticated client to exchange

the auth code for a token

IamClient anonClient = IamClient.builder().build();

### Using an access token

Once you have obtained an access token, you can use it to make API calls this way:

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

import com.docusign.iam.sdk.IamClient;

// Initialize the SDK with your access token

IamClient sdk = IamClient.builder()

.accessToken(accessToken)

.build();

// Make API calls on behalf of the user

var userInfo = sdk.auth().getUserInfo().call();

System.out.println("User Info: " + userInfo);

## Open source repository

The source being used to build the Java IAM SDK is available publicly in the following repository on our public GitHub: [https://github.com/docusign/docusign-iam-java-client](https://github.com/docusign/docusign-iam-java-client/). You can use it to [build your own version of the SDK](https://github.com/docusign/docusign-iam-java-client?tab=readme-ov-file#how-to-build/).

## Compatibility

The Java IAM SDK requires JDK 11 or later.

## Code examples

You can find code examples showcasing how to use the IAM SDK with Maestro API, Connected Fields API, and Navigator API in the <https://github.com/docusign/code-examples-java> repo.

## Providing feedback about the SDK

To provide feedback on the SDK, please either submit an issue in the [GitHub repository](https://github.com/docusign/docusign-iam-java-client/) or send an email to [developers@docusign.com](mailto:developers@docusign.com).

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
