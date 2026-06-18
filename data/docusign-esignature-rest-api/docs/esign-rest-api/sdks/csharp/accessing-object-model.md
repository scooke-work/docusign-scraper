---
title: Accessing the C# SDK object model
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/csharp/accessing-object-model/
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
- Accessing the object model
scraped_at: '2026-06-18T20:28:15Z'
---

# Accessing the C# SDK object model

Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run eSignature REST API code examples.

## Instantiating the models

When making a specific eSignature REST API call using the C# SDK, you usually have to include a specific class used for the data sent or returned as part of that API request. The C# classes used to pass data to and from API endpoints are called
*models*, and all use standard C# properties to get and set values. We will use the
`Brand` object as an example. The
[Brand](https://github.com/docusign/docusign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Model/Brand.cs) class can be found in our open-source GitHub repository. Each data member of the class is decorated by a
`DataMember` attribute and includes the standard triple-slash (XML documentation) descriptive comments that the Visual Studio IntelliSense feature uses to help developers when accessing public libraries.

```
    /// </summary>
    /// The name of the brand.
    /// </summary>
    /// <value>The name of the brand.</value>
    [DataMember(Name="brandName",EmitDefaultValue=false)]
    public string BrandName { get; set; }
```

`BrandName` is an example of a string that is part of the
`Brand` class that has both a public getter and a public setter. To set the
`BrandName` property of a
`Brand` object, use this code:

```
    brand.BrandName = "My Brand";
```

To get the value of the
`BrandName` property, you can simply use the string that it returns:

```
    Console.WriteLine ("The brand name is " + brand.BrandName);
```

Most C# SDK models also provide a constructor that enables developers to initialize many of the object’s properties at the same time that it is created. Instead of using the getter and setter methods, you could set property values in the constructor code when you create the object. For example, you could instantiate a new
`Brand` object and set some of its properties at the same time:

```
    Brand brand = new Brand
    {
        BrandName = "My Brand",
        DefaultBrandLanguage = "en",
        Colors = myBrandColors
    };
```

## Making API calls

To construct an API call, you need to include both the model and the
`accountId` of the account making the API call, each time you make a request. That information is not part of the
`DocuSignClient` object, but is required by the SDK to be able to generate the URL for the specific endpoint.

To create a new brand, for instance, you would instantiate a
`Brand` object and populate it with initial values as shown above, then add the
`accountId` to call the API:

```
    var results = accountsApi.UpdateBrand(accountId, brandId, brand);
```

## Naming conventions

The C# SDK uses the
[Conventions for Reusable .NET Libraries](https://docs.microsoft.com/en-us/dotnet/standard/design-guidelines/capitalization-conventions). All public classes and methods use PascalCase and all parameters use camelCase.

- The categories in the API Reference are all called
  `Apis` in the C# SDK and can be found in the
  `DocuSign.eSign.Api` namespace. As an example,
  [AccountsApi](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Api/AccountsApi.cs) would be the class you use to make API calls for endpoints in the
  [Accounts Category](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/) in the API Reference.
- The resources within each category in the API Reference do not have direct counterparts in the C# SDK. Instead, each API method in each resource corresponds to a C# public method within the class corresponding to the top-level category. The method name is always PascalCase and is a combination of the verb and the proper noun that is being worked upon. For example, for the
  [AccountBrands:update](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/update/) API method, the C# method name within the
  `AccountsApi` class is
  [UpdateBrand](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Api/AccountsApi.cs#L1488).
- The parameters for each API method are based on the API Reference. Every API call has to specify the
  `accountId` as its first parameter, required to determine which account is making the API request. The remaining parameters are defined per API call in the documentation and may include optional parameters. Parameter names are always written in camelCase.
- The request and response objects (if they exist; some methods have one or the other) are all defined as objects in the
  `DocuSign.eSign.Model` namespace as public classes. These classes are a deserialized version of the JSON that is sent by the REST API. For example, the
  [UpdateBrand](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Api/AccountsApi.cs#L1488) method returns an object called
  [Brand](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Model/Brand.cs), which represents the response of the API call.

  Models do not include any methods; they only include properties that have getters and setters. For any array returned by the JSON, the model would include a
  `List<T>` with elements corresponding to that information where
  `T` can be another model or a simple type (typically a string). All models also implement two interfaces:
  `IEquatable<T>` and
  `IValidatableObject` to support comparison as well as cleanup of unused objects.

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
