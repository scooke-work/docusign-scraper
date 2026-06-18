---
title: Python SDK setup and configuration
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/python/setup-and-configuration/
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
- Setup and configuration
scraped_at: '2026-06-18T20:28:16Z'
---

# Python SDK setup and configuration

Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run eSignature REST API code examples.

## Adding the SDK to your project

The Python eSignature SDK is provided as a
[PyPI module](https://pypi.org/project/docusign-esign/) named docusign-esign. By default, you will always get the latest stable version of the SDK. Prerelease versions (either release candidate (RC) or beta) can also be downloaded, as we’ll show later.

There are two ways to add the package to your project: via the command line or by downloading the SDK from GitHub.

### Adding the SDK to your project using the command line

1. In your command console, input:
   `pip install docusign-esign`

### Downloading the SDK from the GitHub repository

The SDK is provided as an open-source library for cases where you would like to make additional changes that are not provided out of the box. You can download the SDK from GitHub using the instructions below:

1. Go to the
   [Python SDK GitHub repository](https://github.com/docusign/docusign-python-client).
2. Select the green
   **Code** button. From here, you can clone the repo, open it in GitHub Desktop, or download it as a ZIP, which you can install to a path of your choice.
3. Locate your Python installation. This folder is usually labeled in a format of Python{VersionNumber}.

   Examples:

   - Unix/Linux: /usr/lib/python3.8
   - Mac: /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7
   - Windows: C:\Users\{username}\AppData\Local\Programs\Python\Python37
4. Inside your Python folder you will find a site-packages folder. Make sure that your newly downloaded Python SDK is inside that site-packages folder.
5. Add the path to your Python folder as an environment variable. You can skip this step if you have already set up the appropriate PYTHONPATH variable.

## Including the SDK library

Once you have installed the PyPI module, you need to find the public classes that are needed to complete various eSignature tasks. To do that, you will use import statements to add any classes that you need to your code. The three most commonly required namespaces that you will be importing from are
`docusign_esign`,
`docusign_esign.models`, and
`docusign_esign.client`.

### [docusign\_esign.apis](https://github.com/docusign/docusign-python-client/tree/master/docusign_esign/apis) module

This Python SDK module contains endpoint categories. Each class under this module corresponds to one of the categories listed in the left menu of the
[Docusign eSignature REST API reference](https://developers.docusign.com/docs/esign-rest-api/reference/). You will need to use this namespace to make calls to SDK methods that initiate REST API calls to the Docusign eSignature REST API.

An
[API category](https://developers.docusign.com/docs/esign-rest-api/reference/) contains all of the methods for each API resource in that category. For example, the Python SDK EnvelopesApi class includes the
[create\_envelope](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/apis/envelopes_api.py#L1313) method. This method corresponds to the API Envelopes resource
[create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) method.

The SDK’s method names roughly correspond to the API Resource:method names.

The API reference page for each endpoint lists the corresponding SDK method associated with that endpoint. To find the Python SDK method that corresponds to an API Resource:method page, use the API reference page’s
**SDK Method** box. The Python method name will be the “snake\_case” version of the API SDK Method name. For example, the API SDK Method
`Envelopes::createEnvelope` is the Python SDK method
`create_envelope`.

### [docusign\_esign.models](https://github.com/docusign/docusign-python-client/tree/master/docusign_esign/models) module

This module contains the objects used for sending and receiving data from the eSignature API endpoints. By using these classes instead of generic JSON objects, Python developers can develop with the Docusign eSignature API much more easily and quickly than by using JSON directly.

There is a one-to-one correspondence between the objects described in the API reference and the classes in the docusign\_esign.models module. The API object names use camelCase (the first letter is lowercase) while the corresponding SDK models use PascalCase (the first letter is uppercase). For example, the API object
[paymentgatewayaccount](https://developers.docusign.com/docs/esign-rest-api/reference/payments/paymentgatewayaccounts/list/#response200_paymentgatewayaccount) corresponds to the Python object
[PaymentGatewayAccount](https://github.com/docusign/docusign-esign-python-client/blob/master/docusign_esign/models/payment_gateway_account.py).

**Note:** The API object name is often not the same as the corresponding model in the Python SDK.

Object attribute names in the API also use camelCase. The corresponding properties of the Python SDK classes are in “snake\_case.”

Some API endpoints also use HTTP query parameters. Within the API, the query parameters use "snake\_case." For example, the
[Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) API method includes an optional query parameter
**change\_routing\_order**. Within the SDK, the API’s query parameters are added as an optional
`**kwargs` parameter after the request object.

**Example:** The
[EnvelopesApi.create\_envelope](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/apis/envelopes_api.py#L1313) function takes three parameters:
`self`,
`account_id`, and
`**kwargs`.

When calling the function, you might need to pass an EnvelopeDefinition object as one of the arguments. To do this, you would create an EnvelopeDefinition object named
`new_envelope` and pass it as
`envelope_definition=new_envelope`.

### [docusign\_esign.client](https://github.com/docusign/docusign-python-client/tree/master/docusign_esign/client) module

This namespace contains the classes needed to manage the overall API experience. These include the classes needed to instantiate a client element to make API calls and the classes used for authentication and exception handling. You will need to include this namespace to be able to use the Docusign eSignature API correctly.

### Using the SDK

To make eSignature REST API calls with the SDK, you need:

- A current access token
- The base path for the API call
- For most API calls, you’ll also need the relevant
  `account_id`. Note that it is common for a user to be a member of multiple accounts.

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
