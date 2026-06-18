---
title: IAM SDK - C# (beta)
source_url: https://developers.docusign.com/docs/sdks/iam-c-sharp/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- SDKs
- SDKs
- C# IAM SDK
scraped_at: '2026-06-18T21:43:09Z'
---

# IAM SDK - C# (beta)

The Docusign Intelligent Agreement Management (IAM) SDKs assist developers in using the Intelligent Agreement Management (IAM) APIs, simplifying common tasks.

This page offers high-level information about the C# SDK and its usage.

## APIs included in this SDK

The IAM SDKs include the following APIs:

- [Workflow Builder API](https://developers.docusign.com/docs/workflow-builder-api/): Trigger and manage Agreement Builder workflows from your own app.
- [Agreement Manager API](https://developers.docusign.com/docs/agreement-manager-api/): Connect AI-extracted data from agreements stored in Agreement Manager into your own app. into your own app.
- [Workspaces API](https://developers.docusign.com/docs/workspaces-api/): Create structured, secure, and scalable agreement workflows.
- [Connected Fields API](https://developers.docusign.com/docs/connected-fields-api/): Discover extension apps that your app can use to validate input as part of the eSignature process.

Additional APIs may be added later; check this page for updates.

## How to obtain the SDK

The easiest way to add the SDK to your project is by adding the [Docusign.IAM.SDK](https://www.nuget.org/packages/Docusign.IAM.SDK/) Nuget package to your project in Visual Studio.

### Adding the SDK to your project using the Visual Studio UI

1. Open Visual Studio and load the solution you wish to use.
2. Open the **Solution Explorer** window and right-click the desired project in the solution.
3. Select **Manage NuGet Packages…** (shown below).

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='497.00000000000006' width='359' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![C# IAM SDK VS menu showing nuget packages option](https://images.ctfassets.net/aj9z008chlq0/7oZgN7ueN3SojtxNrrKAYI/183043d5d6a2b400c94ff11a31d375cd/image__178_.png?w=359&h=497&q=50&fm=png)
4. In the **NuGet Package Manager** window, select the **Browse** tab on the left.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='173' width='512' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![C# IAM SDK searching for Nuget packages](https://images.ctfassets.net/aj9z008chlq0/2PZ4DoqUEpHYQHJ4mRMf8Z/c18bf994aee5a8d1d8748cece36e4c96/C-IAMSDK2.png?w=512&h=173&q=50&fm=png)
5. In the **Search** textbox, enter "Docusign.IAM" to find the IAM SDK. Make sure the **Include prerelease** checkbox is selected.
6. **Docusign.IAM.SDK** by Docusign (publisher) should be displayed first in the search results. Select it.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='202' width='512' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![C# IAM SDK VS found Nuget package to add](https://images.ctfassets.net/aj9z008chlq0/3vpucTpXiXpVtL9FTaCooS/e9987c642b406f4a608f00c67e1bef03/C-IAMSDK3.png?w=512&h=202&q=50&fm=png)
7. Select **Install** to install the latest version of the package.
8. Acknowledge the license agreement by selecting **I Accept** on the **License Acceptance** screen.

You have now successfully downloaded, configured, and installed the Docusign IAM SDK for your project. To confirm the package is available in your project, you can go back to the **Solution Explorer** window and expand the **Dependencies > Packages** section of the project. You should see **Docusign.IAM.SDK** (version number) listed.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='333' width='327' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![VS Explorer showing added C# IAM SDK](https://images.ctfassets.net/aj9z008chlq0/ApJbJvNwrmMJkT2E2pI8T/d2f0f1745e6aad4e024f33724e59005b/C-IAMSDK4.png?w=327&h=333&q=50&fm=png)

**Note:** If you expand the **Docusign.IAM.SDK** package, you will see the additional dependencies that are automatically installed by the NuGet package manager.

### Adding the C# SDK to your project using the command line

1. Open the NuGet Package Manager command line from the Visual Studio menu bar by selecting **Tools > NuGet Package Manager > Package Manager Console**.
2. From the **Package Manager Console**, run the following command:

   `dotnet add package Docusign.IAM.SDK`

   The command above will automatically install the latest stable version. If desired, you can specify a specific version by using the -Version switch. For example, this command installs version 1.0.0 of the Docusign C# IAM package:

   `dotnet add package Docusign.IAM.SDK --version 1.0.0`

## Getting started with the C# IAM SDK

The best way to learn how to use the C# IAM SDK is to explore the code examples provided by Docusign. You can find the C# code examples in the [code-examples-csharp](https://github.com/docusign/code-examples-csharp) public github repository.
These code examples can also be part of the ZIP file downloaded when you use the [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/). This tool will also create all the necessary configuration data in your developer account so you’ll be ready to run it.

## Authentication support

Every API call must be [authenticated](https://developers.docusign.com/platform/auth/). The C# IAM SDK provides functionality to simplify the use of authentication for making IAM API calls.

### Obtaining an access token

Before you begin the authentication process, you must create and [configure your app](https://developers.docusign.com/platform/configure-app/). Specifically:

- Create your app and obtain your integration key (client ID).
- Generate a client secret for your app.
- Add your redirect URI to the list of allowed redirect URLs associated with your integration Key.

These settings are required to obtain an authorization code and exchange it for an access token in the steps below, which demonstrate the Confidential Authorization Code Grant flow. Other OAuth flows may require different configuration settings.

#### Step 1: Obtain authorization code

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

// before using this code, make sure your .env has

“DOCUSIGN\_CLIENT\_ID” which is your IK (GUID)that you

created as well as the “DOCUSIGN\_REDIRECT\_URI” which is

the URI to redirect the browser after authentication.

using System;

using Docusign.IAM.SDK;

using Docusign.IAM.SDK.Models.Components;

using Docusign.IAM.SDK.Utils.Auth;

// Create the authorization URL

String consentUrl = AuthorizationUrlBuilder.Create()

.WithBasePath(OAuthBasePath.Demo)

.WithResponseType(AuthorizationUrlResponseType.Code)

.WithClientId(Environment.GetEnvironmentVariable

("DOCUSIGN\_CLIENT\_ID"))

.WithRedirectUri(Environment.GetEnvironmentVariable

("DOCUSIGN\_REDIRECT\_URI"))

.Build();

#### Step 2: Exchange Authorization Code for Access Token

After you obtain the authorization code, you need to use it to get an access token. The SDK provides helper functions to simplify this process.

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

// before using this code, make sure your .env has

“DOCUSIGN\_CLIENT\_ID” which is your IK (GUID)that you

created as well as the “DOCUSIGN\_CLIENT\_SECRET” which you

can create together with the IK.

using Docusign.IAM.SDK;

using Docusign.IAM.SDK.Models.Components;

using Docusign.IAM.SDK.Models.Requests;

using Docusign.IAM.SDK.Models.Errors;

using System;

using System.Threading.Tasks;

try

{

// Create an unauthenticated client to exchange the auth

code for a token

var anonClient = IamClient.Builder().Build();

// Prepare the request with the auth code

var request = new ConfidentialAuthCodeGrantRequestBody()

{

Code = authCode,

};

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

using Docusign.IAM.SDK;

// Initialize the SDK with your access token

var sdk = IamClient

.Builder()

.WithAccessToken("<YOUR\_ACCESS\_TOKEN\_HERE>")

.Build();

// Make API call to get the basePath as well as account

information for the user

var res = await sdk.Auth.GetUserInfoAsync();

## Open source repository

The source being used to build the C# IAM SDK is available publicly in the following repository on our public GitHub: <https://github.com/docusign/docusign-iam-csharp-client> You can use it to build your own version of the SDK.

## Compatibility

The C# IAM SDK requires .NET version 8.0 or above.

## Code examples

You can find code examples showcasing how to use the IAM SDK with Agreement Builder API, Connected Fields API, and Agreement Manager API in the <https://github.com/docusign/code-examples-csharp> repo.

## Providing feedback about the SDK

To provide feedback on the SDK, please either submit an issue in the [GitHub repository](https://github.com/docusign/docusign-iam-csharp-client) or send an email to [developers@docusign.com](mailto:developers@docusign.com).

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
