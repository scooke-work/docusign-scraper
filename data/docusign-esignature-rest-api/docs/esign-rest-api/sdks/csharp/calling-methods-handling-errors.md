---
title: Calling C# SDK methods and handling errors
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/csharp/calling-methods-handling-errors/
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
- Calling methods and handling errors
scraped_at: '2026-06-18T21:09:54Z'
---

# Calling C# SDK methods and handling errors

## Calling methods

Making API calls through the C# SDK requires calling defined methods in classes in the `DocuSign.eSign.Api` namespace. Each of these classes corresponds to a group of endpoints that are used for specific feature areas related to the Docusign eSignature REST API.

Each specific REST endpoint typically has four or more different C# SDK methods that can be used to call it. As an example, here are four methods that call the endpoint `"/v2.1/accounts/{accountId}/brands/{brandId}"``:`

```
    accountsApi.UpdateBrand(accountId, brandId, brand);
    accountsApi.UpdateBrandAsync(accountId, brandId, brand);
    accountsApi.UpdateBrandWithHttpInfo(accountId, brandId, brand);
    accountsApi.UpdateBrandAsyncWithHttpInfo(accountId, brandId, brand);
```

The differences between these four methods are the information they return and whether they make the call on the calling thread or in a separate background thread. It’s important to note that each of the four methods above call the same API endpoint.

The first method, [UpdateBrand](https://github.com/docusign/docusign-esign-csharp-client/blob/5174c1f6d4b03e0f5e8f50cd79ddd6acde834fd1/sdk/src/DocuSign.eSign/Api/AccountsApi.cs#L14607), which is considered the most simple approach, makes the API call from the same calling thread synchronously, blocking it until the call is complete. It will only return the `Brand` object that represents the JSON object that is being sent back from the API.

The second method, [UpdateBrandAsync](https://github.com/docusign/docusign-esign-csharp-client/blob/5174c1f6d4b03e0f5e8f50cd79ddd6acde834fd1/sdk/src/DocuSign.eSign/Api/AccountsApi.cs#L14708), uses the C# concurrency library and returns a generic [System.Threading.Tasks.Task<Brand>](https://docs.microsoft.com/en-us/dotnet/api/system.threading.tasks.task-1?view=net-5.0) object. This object represents a parallel C# task that can be run independently of the main thread and can signal the main thread when it completes. At that point, the object of type `Brand` will be ready to be consumed by the main thread. This approach is recommended when the API call is made from a UI, and the UI is blocked until the API call is complete. It enables the developer to make API calls in parallel and continue the main UI thread to improve the user experience.

The third ([UpdateBrandWithHttpInfo](https://github.com/docusign/docusign-esign-csharp-client/blob/5174c1f6d4b03e0f5e8f50cd79ddd6acde834fd1/sdk/src/DocuSign.eSign/Api/AccountsApi.cs#L14621)) and fourth ([UpdateBrandAsyncWithHttpInfo](https://github.com/docusign/docusign-esign-csharp-client/blob/5174c1f6d4b03e0f5e8f50cd79ddd6acde834fd1/sdk/src/DocuSign.eSign/Api/AccountsApi.cs#L14723)) methods are variants on the first and second methods that return additional information. These methods return the generic `ApiResponse<Brand>` class, which provides both the data from the body of the HTTP response (the JSON) as a generic object (in this case, `Brand`) as well as the status code and the collection called `Headers` that includes all the HTTP headers in the response. These are useful to get additional information from the API—for example, information about API request limits—that lives in the HTTP headers of the response.

## Handling errors

Error handling is an important part of developing your software. Your code should handle both expected and unexpected errors.

The C# SDK provides an [ApiException](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiException.cs) class that is used for common scenarios where exceptions are thrown. It’s a best practice to catch this exception in your code and inspect the `ErrorCode` and `ErrorMessage` objects to provide useful information to understand the cause of the error.

Common scenarios where the SDK throws an `ApiException` are:

- Invalid or expired access token.
- HTTP response status code 400 and above. These represent various [error messages](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/) that are identified by the HTTP layer. Such errors include not authorized (403) errors, which occur due to issues with authentication.
- Issues in deserialization of the response JSON. If the JSON sent back by the API cannot be properly deserialized into the C# objects that the SDK is expecting, an `ApiException` is thrown, and the "bad" JSON is returned in the `ErrorMessage` property of the exception.
- JWT issues with either the private RSA key pair or `userId`. Since the [RequestJWTUserToken](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Client/ApiClient.cs#L997) method for obtaining an OAuth token using JWT is included in the SDK, an `ApiException` is thrown if the RSA key or `userId` are missing or malformed.

[Troubleshooting for common errors](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/) has detailed information about causes and resolutions for specific errors.

### Obtaining the trace token for solving problems via Support

Every API response includes a GUID that can be used to trace it on the back end by Docusign [Support](https://support.docusign.com/). This GUID is called the *trace token*. The trace token enables Support staff to find the internal logs in the system related to the API request/response and to get additional information about it. This information may not be directly available to developers with or without the SDK.

The trace token is part of the HTTP response header. To obtain the trace token, you will first call the `WithHttpInfo` variant of the method to retain the header of the HTTP response.

```
    ApiResponse response = accountsApi.UpdateBrandWithHttpInfo(accountId, brandId, brand);
    string traceToken = response.Headers["X-Docusign-TraceToken"];
```

**Note:** Some API calls do not return an error, but instead provide error information inside the body of the HTTP response. In this case, you will need to have your code check the data returned from the API to make sure the call was successful.

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
