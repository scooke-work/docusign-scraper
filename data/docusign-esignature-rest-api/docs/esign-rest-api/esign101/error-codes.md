---
title: Error codes
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Error codes
scraped_at: '2026-06-18T21:09:48Z'
---

# Error codes

The Docusign REST APIs return either 200 (OK) or 201 (Created) when an API request successfully runs to completion. It may also return 204 (No Content) to that the requested action was completed successfully, but the server does not need to return any data or a new resource in the response body.
 Status codes in the 400-500 range indicate failures. For APIs that process a single item, this overall status code determines success or failure. There are special considerations for `PUT` and `POST` calls that process multiple items. See [Error response handling for API requests that support multiple items](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/#error-response-handling-for-api-requests-that-support-multiple-items) for more information on error response handling. If an API request is not successful, the HTTP response code returned is generally one of the following:

| Error code | Message | Description |
| --- | --- | --- |
| 400 | Bad Request | A portion of the request was not valid or could not be processed in the current context. |
| 401 | Unauthorized | The authentication or authorization required for the API request did not pass. |
| 403 | Forbidden | This resource is not allowed for the caller |
| 404 | Not Found | The resource does not exist. This might occur on `GET` or `DELETE` requests. |
| 408 | Request Timeout | It took too long to get a response |
| 415 | Unsupported Media Type | The data type of some data in the request is not supported. For example: your request may be in XML, but you did not specify `Content-Type: application/xml` in the request header. |
| 429 | Too Many Requests | API limit was reached |
| 444 | The API request is forbidden. Request blocked due to excess usage | The request was blocked by Docusign's traffic management system. |

The following error codes occur with much less frequency:

| Error code | Message | Description |
| --- | --- | --- |
| 405 | Method Not Allowed | The HTTP method (`GET`, `PUT`, `POST`, or `DELETE`) is not valid for the given resource URI. |
| 500 | Internal Server Error | An internal server-side error has occurred. |

In most cases, the response body contains a more detailed `errorDetails` structure when an error occurs. However, depending on the error, the server might return HTML in place of the `errorDetails` structure, or nothing in the case of certain error types.

## General error response handling

The general flow for response handling is:

```
if (statusCode == 200 || statusCode == 201) {
  // successful call - but do special processing for multi-item PUT & POST requests
} else if (statusCode == 404) {
  // call was processed but the resource being accessed was not found
  // envelope doesn’t exist, user doesn’t exist, etc. There may not be any more details in the errorDetails response.
} else // other errors
{
  var errorDetails = Json.Decode(response.body);
  if (errorDetails != null) {
    // process errorDetails.errorCode - See table of error codes
    if (errorDetails.message != null) {
      // use errorDetails.message to get more information in textual form.
    }
  }
}
```

## Error response handling for API requests that support multiple items

The [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/) supports many calls that operate on multiple items, such as adding one or more users to an account or adding one or more documents to a draft envelope. This decreases the number of HTTP requests required to perform some common operations. For API requests that support multiple items, the overall HTTP response code will be 200 (OK) or 201 (Created) if the API request has run to completion, which means all items in the request structure were processed. This response code is returned even if there were failures for individual items in the array.

The response body contains information about each item processed, and the structure for each item contains an `errorDetails` element if that item was not successfully processed.

You are responsible for checking for the `errorDetails` element for each item in the array to perform proper error handling. The general response processing logic for these types of APIs is:

```
if (statusCode == 200 || statusCode == 201) {
  // check for errors with each item processed.
  var itemsArray = Json.Decode(response.body);
  foreach(var item in itemsArray) {
    if (item.errorDetails != null) {
      // an error occurred during processing - handle it
      string errorCode = item.errorDetails.errorCode;
      string errorMessage = item.errorDetails.message;
      // perform error handling based on errorCode
    } else {
      // item processing was successful
    }
  }
} else {
  // statusCode indicated overall error with the request.
}
```

## Next steps

- See [Troubleshooting for common errors](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/) for causes and resolutions for specific errors.
- Learn more about [Envelope status codes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/status-codes/).
- Get an overview of [Recipient status codes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/status-codes/).

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
