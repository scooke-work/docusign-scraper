---
title: Node.js SDK setup and configuration
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/node/setup-and-configuration/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- Node
- Node
- Setup and configuration
scraped_at: '2026-06-18T21:09:54Z'
---

# Node.js SDK setup and configuration

Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run eSignature REST API code examples.

## Adding the SDK to your project

The Node.js eSignature SDK is provided as a package named [docusign-esign](https://www.npmjs.com/package/docusign-esign/). By default, you will always get the latest stable version of the SDK. Prerelease versions (either release candidate (rc) or beta) can also be downloaded as shown below.

There are three ways to add the package to your project: via your preferred console, your project’s package.json file, or by downloading the SDK from GitHub.

### Adding the Node.js SDK to your project using your console

In your console, navigate to your project directory, then run: `npm i -s docusign-esign`

To specify a version using your console, you can use the @ syntax: `npm i -s docusign-esign@5.8.1`

### Adding the Node.js SDK to your project using your project’s package.json file

1. In your application's package.json file, add: `"docusign-esign"`
2. Open your console, navigate to your project directory, then run: `"npm install"`

If desired, you can specify a version. For example, adding the following to your project’s package.json file installs version 5.8.1 of the Docusign Node.js eSignature SDK: `"docusign-esign": "5.8.1"`

### Downloading the Node.js SDK from the GitHub repository

This open-source SDK is available for download in cases where you would like to make changes to the SDK. You can download the SDK from GitHub using the instructions below:

1. Download or clone the SDK from the [docusign-esign-node-client](https://github.com/docusign/docusign-esign-node-client) repository.
2. In the console, navigate to the docusign-esign-node-client directory, then run: `npm install`

You can also select a different version to download from the [docusign-esign-node-client](https://github.com/docusign/docusign-esign-node-client) repository's [release history](https://github.com/docusign/docusign-esign-node-client/releases/).

## Including the SDK library

Once you have installed the docusign-esign package, you will need to find the public modules that are required to complete various eSignature tasks.

When using the Node.js package, you must add the following `require` statement in your Node.js code:  `const docusign = require('docusign-esign')`

## Docusign eSignature API modules

These [Node.js SDK modules](https://github.com/docusign/docusign-esign-node-client/tree/master/src/api) contain endpoint categories. Each of these modules corresponds to one of the categories listed in the left menu of the [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/) reference. You will need these modules to make calls to the SDK functions that initiate REST API calls to the Docusign eSignature REST API.

Hereafter in the SDK documentation, the term “API object” will refer to [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/) reference objects.

An [API category](https://developers.docusign.com/docs/esign-rest-api/reference/) contains all methods for each API resource in that category. For example, the Node.js SDK [EnvelopesApi](https://github.com/docusign/docusign-esign-node-client/blob/master/src/api/EnvelopesApi.js) module includes the [Envelopes:create](https://github.com/docusign/docusign-esign-node-client/blob/master/src/api/EnvelopesApi.js#L1079) function. This function corresponds to the [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) method of the API [Envelopes](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/) resource.

The Node.js SDK function names roughly correspond to the API Resource:method names.

The API Resource:method page for each endpoint lists the API SDK Method in the **SDK Method** box. The Node.js function name will be the camelCase version of the API SDK Method name. For example, the API SDK Method `Envelopes::createEnvelope`, listed toward the bottom of the [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) page, is the Node.js SDK function [createEnvelope](https://github.com/docusign/docusign-esign-node-client/blob/master/src/api/EnvelopesApi.js#L1079).

Some API endpoints also use HTTP query parameters. Within the API, such query parameters use snake\_case. For example, the [Envelopes:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/) API method includes an optional query parameter, `advanced_update`. Within the SDK, the API’s query parameters are added as an elective `optsOrCallback` parameter after the request object.

**Example:** The [getEnvelope](https://github.com/docusign/docusign-esign-node-client/blob/master/src/api/EnvelopesApi.js#L4550) function signature is: `this.getEnvelope = function(accountId, envelopeId, optsOrCallback, callback)`The [queryParams](https://github.com/docusign/docusign-esign-node-client/blob/master/src/api/EnvelopesApi.js#L4581) variable is used to set the API method’s query parameters.

```
    var queryParams = {
        'advanced_update': optsOrCallback['advancedUpdate'],
        'include': optsOrCallback['include']
    };
```

The Node.js SDK query parameters in snake\_case correspond to the API endpoint’s query parameters.

## Docusign eSignature Models

These [models](https://github.com/docusign/docusign-esign-node-client/tree/master/src/model) contain the objects used for sending and receiving data from the eSignature API endpoints. By using these models instead of generic JSON objects, Node.js developers can develop with the Docusign eSignature API more easily and quickly than by using JSON directly.

There’s a one-to-one correspondence between the objects described in the [API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/) and the Node.js Docusign eSignature Models. The API object names use flatcase (all lowercase without spaces) while the corresponding SDK models use PascalCase (the first letter is uppercase). For example, the API object [paymentgatewayaccount](https://developers.docusign.com/docs/esign-rest-api/reference/payments/paymentgatewayaccounts/list/#response200_paymentgatewayaccount) corresponds to the Node.js model [PaymentGatewayAccount](https://github.com/docusign/docusign-esign-node-client/blob/master/src/model/PaymentGatewayAccount.js).

The API object name is often not the same as the corresponding model in the Node.js SDK.

Object attribute names in the API also use camelCase. The corresponding properties of the Node.js SDK are also in camelCase.

## Docusign eSignature Client, OAuth, and Error functions

These [functions](https://github.com/docusign/docusign-esign-node-client/tree/master/src/) are needed to manage the overall API experience. The Client, OAuth, and Error functions, respectively, handle instantiating a client element to make API calls, authentication, and exception handling. You will need these functions to be able to use the Docusign eSignature API correctly.

## Using the SDK

To make eSignature REST API calls with the SDK, you need:

- A current `accessToken`.
- The `basePath` for the API call.
- For most API calls, you’ll also need the relevant `accountId`. Note that it is common for a user to be a member of multiple accounts.

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
