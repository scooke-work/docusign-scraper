---
title: IAM SDK - TypeScript (beta)
source_url: https://developers.docusign.com/docs/sdks/iam-typescript/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- SDKs
- SDKs
- TypeScript IAM SDK
scraped_at: '2026-06-18T21:43:09Z'
---

# IAM SDK - TypeScript (beta)

The Docusign Intelligent Agreement Management (IAM) SDKs assist developers in using the Intelligent Agreement Management (IAM) APIs, simplifying common tasks.

This page offers high-level information about the TypeScript SDK and its usage.

## APIs included in this SDK

The IAM SDKs include the following APIs:

- [Workflow Builder API](https://developers.docusign.com/docs/workflow-builder-api/): Trigger and manage Agreement Builder workflows from your own app.
- [Agreement Manager API](https://developers.docusign.com/docs/agreement-manager-api/): Connect AI-extracted data from agreements stored in Agreement Manager into your own app. into your own app.
- [Workspaces API](https://developers.docusign.com/docs/workspaces-api/): Create structured, secure, and scalable agreement workflows.
- [Connected Fields API](https://developers.docusign.com/docs/connected-fields-api/): Discover extension apps that your app can use to validate input as part of the eSignature process.

Additional APIs may be added later; check this page for updates.

## How to obtain the SDK

The easiest way to add the SDK to your project is by installing the [@docusign/iam-sdk](https://www.npmjs.com/package/@docusign/iam-sdk) package using your preferred package manager.

### Adding the TypeScript SDK to your project using the command line

Run the following command to install the SDK and add it to your project dependencies:

```
npm install @docusign/iam-sdk
```

```

```

To install a specific version, append the version number to the package name:

```
npm install @docusign/iam-sdk@1.0.0-beta.3
```

```

```

This will automatically update your `package.json` file and download the SDK and its dependencies into your `node_modules` directory.

### Adding the TypeScript SDK to your project using your project’s package.json file

Alternatively, you can manually add the dependency by editing your `package.json` file:

```
"dependencies": {
  "@docusign/iam-sdk": "1.0.0-beta.3"
}
```

Then run your package manager’s install command:

```
npm install
```

## Getting started with the TypeScript IAM SDK

The best way to learn how to use the TypeScript IAM SDK is to explore the code examples provided by Docusign. You can find the TypeScript code examples in the [code-examples-node](https://github.com/docusign/code-examples-node) public GitHub repository. These code examples can also be part of the ZIP file downloaded when you use the [Quickstart tool](https://developers.docusign.com/docs/esign-rest-api/quickstart/). This tool will also create all the necessary configuration data in your developer account so you’ll be ready to run it.

## Authentication support

Every API call must be [authenticated](https://developers.docusign.com/platform/auth/). The TypeScript IAM SDK provides functionality to simplify the use of authentication for making IAM API calls.

### Obtaining an access token

Before you begin the authentication process, you must create and [configure your app](https://developers.docusign.com/platform/configure-app/). Specifically:

- Create your app and obtain your integration key (client ID).
- Generate a client secret for your app.
- Add your redirect URI to the list of allowed redirect URLs associated with your integration Key.

These settings are required to obtain an authorization code and exchange it for an access token in the steps below, which demonstrate the Confidential Authorization Code Grant flow. Other OAuth flows may require different configuration settings.

#### Step 1: Obtain an authorization code

To call the DocuSign IAM APIs, you must request the appropriate OAuth scopes. The SDK provides predefined constants for [common scope sets](https://github.com/docusign/docusign-iam-typescript-client/blob/28254cd50d38d6df1cd037f86ccc78a46c7f67ee/src/security/scopes.ts/). For example, `AuthUtils.DOCUSIGN_IAM_OAUTH_SCOPES` includes all scopes used across the IAM SDK. You can use these helpers or supply your own array of scopes.

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

import { AuthUtils, IamClient } from '@docusign/

iam-sdk';

// Details configured from the Docusign developer

console.

const clientId = process.env.

AUTH\_CODE\_CONFIDENTIAL\_CLIENT\_ID!;

const secretKey = process.env.

AUTH\_CODE\_CONFIDENTIAL\_SECRET\_KEY!;

const redirectUri = process.env.

DOCUSIGN\_REDIRECT\_URI!;

const authorizationUrl = AuthUtils.

createAuthorizationUrl({

type: "code",

clientId,

redirectUri,

scopes: AuthUtils.DOCUSIGN\_IAM\_OAUTH\_SCOPES,

});

// Prompt the user to visit the authorization URL.

They'll need to grab

// the code from the `code` query parameter

#### Step 2: Exchange an authorization code for an access token

After you obtain the authorization code, you need to use it to get an access token. The SDK provides helper functions to simplify this process. This example shows the Confidential Authorization Code Grant flow. You can find examples for other supported flows in the SDK repository, including:

- [Authorization Code (public)](https://github.com/docusign/docusign-iam-typescript-client/blob/28254cd50d38d6df1cd037f86ccc78a46c7f67ee/auth-examples/auth-code-public.ts/)
- [Implicit Grant](https://github.com/docusign/docusign-iam-typescript-client/blob/28254cd50d38d6df1cd037f86ccc78a46c7f67ee/auth-examples/implicit-grant.ts)
- [JWT Grant](https://github.com/docusign/docusign-iam-typescript-client/blob/28254cd50d38d6df1cd037f86ccc78a46c7f67ee/auth-examples/jwt-grant.ts/)

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

// Get token information using the authorization code

const { accessToken, refreshToken, expiresIn } =

await new IamClient().auth

.getTokenFromConfidentialAuthCode({ clientId,

secretKey }, { code })

.catch((error) => {

if (error instanceof OAuthErrorResponse) {

throw new Error(

`Failed to get auth session. Error: ${error.

error}, Description: ${error.

errorDescription}`,

);

}

throw error;

});

console.log(

`Auth Session:\n${JSON.stringify({ accessToken,

refreshToken, expiresIn }, null, 2)}\n`,

);

### Using an access token

Once you have obtained an access token, you can use it to make API calls this way:

1

2

3

4

const authenticatedClient = new IamClient({

accessToken: accessToken,

});

const result = await authenticatedClient.auth.

getUserInfo();

## Open source repository

The source being used to build the TypeScript IAM SDK is available publicly in the following repository on our public GitHub:  [https://github.com/docusign/docusign-iam-typescript-client](https://developers.docusign.com/docs/sdks/iam-typescript/ https:/github.com/docusign/docusign-iam-typescript-client/). You can use it to build your own version of the SDK.

## Compatibility

The TypeScript IAM SDK requires Node.js version 18 or above. See [RUNTIMES.md](https://github.com/docusign/docusign-iam-typescript-client/blob/main/RUNTIMES.md) for more information.

**Note**: Node v18 is deprecated and may be unsupported in future SDK releases. Use Node v20 or later when possible.

## Code examples

You can find code examples showcasing how to use the IAM SDK with Agreement Builder API, Connected Fields API, and Agreement Manager API in the <https://github.com/docusign/code-examples-node> repo.

## Providing feedback about the SDK

To provide feedback on the SDK, please either submit an issue in the [GitHub repository](https://developers.docusign.com/docs/sdks/iam-typescript/ https:/github.com/docusign/docusign-iam-typescript-client/) or send an email to [developers@docusign.com](mailto:developers@docusign.com).

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
