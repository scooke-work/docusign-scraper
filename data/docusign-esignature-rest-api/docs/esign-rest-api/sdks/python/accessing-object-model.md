---
title: Accessing the Python SDK object model
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/python/accessing-object-model/
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
- Accessing the object model
scraped_at: '2026-06-18T21:09:55Z'
---

# Accessing the Python SDK object model

Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run eSignature REST API code examples.

## Instantiating the models

When making a specific eSignature REST API call using the Python SDK, you usually have to import a specific class used for the data sent or returned as part of that API request. The Python classes used to pass data to and from API endpoints are called models. We will use the
`Brand` object as an example. The
[Brand class](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/models/brand.py) can be found in our open-source GitHub repository.

Each class in the Python SDK defines its properties using the
`@property` decorator.
`brand_name` is an example of a property of the
`Brand` class. To set the
`brand_name` property of a
`Brand` object, use this code:

```
    brand.brand_name = "my brand"
```

To get the value of the
`brand_name` property, you can simply use the string that it returns like this:

```
    print("The brand name is" + brand.brand_name)
```

Most Python models also provide a constructor that enables developers to initialize many of the object’s properties at the same time that it is created. For example, you can instantiate a new
`Brand` object and set some of its properties at the same time, like this:

```
    brand = Brand(
        brand_name="My Brand",
        default_brand_language="en",
        colors=myBrandColors
    )
```

## Making API calls

To construct an API call, you need to include both the model and the
`account_id` of the account making the API call each time you make a request. That information is not part of the
`ApiClient` object, but is required by the SDK to be able to generate the URL for the specific endpoint.

For example, to create a new brand, you would instantiate a
`Brand` object and populate it with initial values as shown above, then use it along with the
`account_id` to call the API, as shown below.

```
    response = account_api.create_brand(account_id=account_id, brand=brand)
```

## Naming conventions

The Python SDK uses the naming conventions in the
[Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). All class names use PascalCase while methods and properties of those classes use snake\_case.

- The categories in the API reference are
  `apis` in the Python SDK and can be found in the
  [docusign\_esign.apis](https://github.com/docusign/docusign-python-client/tree/master/docusign_esign/apis) namespace. As an example, the
  [AccountsApi](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/apis/accounts_api.py#L27) class would be the class you use to make API calls for endpoints in the
  [Accounts Category](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/) in the API Reference.
- The resources within each category in the API Reference do not have direct counterparts in the Python SDK. Instead, each API method in each resource corresponds to a Python method within the class corresponding to the top-level category. The method name is always snake\_case and is a combination of the verb and the object that is being worked on. For example, for the
  [AccountBrands: update](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/update/) API method, the Python method within the
  `AccountsApi` class is named
  [update\_brand](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/apis/accounts_api.py#L6278).
- The parameters for each API method are based on the API reference. Every API call has to specify the
  `account_id` as its first parameter, required to determine which account is making the API request. The remaining parameters are defined per API call in the documentation and may include optional parameters. Parameter names are always written in snake\_case.
- The request and response objects (if they exist; some methods have one or the other) are all defined as objects in the
  [docusign\_esign.models](https://github.com/docusign/docusign-python-client/tree/master/docusign_esign/models) namespace as public classes. These classes are a deserialized version of the JSON that is sent by the REST API. For example, the
  [update\_brand](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/apis/accounts_api.py#L6278) method returns an object called
  [Brand](https://github.com/docusign/docusign-python-client/blob/master/docusign_esign/models/brand.py), which represents the response of the API call. Models do not include any methods; they only include properties (all written in snake\_case) that have getters and setters. For any array returned by the JSON, the model would include a dictionary called
  `attribute_map` with elements corresponding to that information.

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
