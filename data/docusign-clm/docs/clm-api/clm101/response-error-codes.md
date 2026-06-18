---
title: Response and Error Codes
source_url: https://developers.docusign.com/docs/clm-api/clm101/response-error-codes/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- API 101
- API 101
- Response Error Codes
scraped_at: '2026-06-18T21:48:55Z'
---

# Response and Error Codes

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

Docusign CLM uses standard HTTP response codes and error objects to communicate the results of Docusign CLM API calls. Note that there are subsets of codes that only apply to certain operations, such as authentication or file downloads.

## Success response codes

The CLM API returns these response codes for successful requests:

**200 - OK**: Success response.

**201 - Object Created**: The POST request to create an object via the Object API was successful.

**202 - Request Accepted for Asynchronous Processing**: This is the standard response for a POST request to the Task API. The response object contains an `Href` property indicating the URL to which you can make a GET request to find the status of the task.

**204 - No Content**: The server has completed its work, but there is nothing to return to the user. This code is returned in response to delete requests that eliminate the object from the system. Note that soft deletes such as deleting a document or folder only move the object to the trash, and therefore return a 200 response code instead of a 204 response code.

## Download-only response codes

These response codes only apply when downloading documents through the [Content API](https://developers.docusign.com/docs/clm-api/clm101/content-api/):

**205 - Partial Content**: The download was incomplete.

**406 - Not Acceptable**: The accept header for the request is not supported.

**416 - Requested Range Not Satisfiable**: The byte range in the request is invalid.

## Authorization and security response codes

The API returns these authorization and security response codes:

**401 - Unauthorized**: There is an invalid or missing authentication token in the request. This is also the standard response for an invalid authentication request.

**403 - Forbidden**: The user is not authorized to perform the operation. The server understood the operation request, but the user does not have rights in Docusign CLM to perform this operation. If the user does not have permissions to see the object or the object does not exist, a 404 response code is returned.

**429 – Rate Limit Exceeded**: The API rate limit has been exceeded. See  [API Rules and Resource Limits](https://developers.docusign.com/docs/clm-api/clm101/rules-and-limits/) for more information.

## Error response codes

The following error codes are returned:

**400 - Bad Request**: The client has sent a request object that the server could not parse. This error is often caused by malformed JSON in the request.

**404 - Not Found**: Returned when the requested object does not exist. This is also returned when the object exists in Docusign CLM, but the user does not have access to it based on their security profile. When this occurs, the error message is "Object does not exist or the user does not have access rights".

**422 - Unprocessable entity**: Returned for validation errors where the Docusign CLM application will not accept the request, such as using an invalid character in a document name. See [Validation errors](https://developers.docusign.com/docs/clm-api/clm101/response-error-codes/#validation-errors) for more information.

**500 - Internal Server Error**: An unexpected server error occurred. This response code generally indicates a system error that must be addressed by Docusign. If the error persists, contact Docusign Support.

### Error response object

When an error response code is returned, the response body contains the REST API error object:

```
{
  "Error": {
    "HttpStatusCode": 401,
    "UserMessage": "Access Denied",
    "DeveloperMessage": "Access Denied",
    "ErrorCode": 103,
    "ReferenceId": "b797912a-xxxx-xxxx-xxxx-6febc4e07875"
  }

}
```

The error object contains the following properties:

- `HttpStatusCode`: The HTTP response status code.
- `UserMessage`: A user-friendly message that you can display to the end user in UI-based applications. In some cases, this value is the same as the `developerMessage`.
- `DeveloperMessage`: Technical error information that developers can use for debugging.
- `ErrorCode`: The Docusign CLM error code for the error message.
- `ReferenceId`: A Docusign CLM internal code for the error instance. Refer to this value when communicating with Docusign CLM support about the error.

### Validation error response object

Responses to validation errors include an array of validation error objects. For example, this response is returned when you try to create a folder with a name that contains invalid characters:

```
{
  "Error": {
    "HttpStatusCode": 422,
    "UserMessage": "Validation Error",
    "DeveloperMessage": "See the list of validation errors",
    "ErrorCode": 101,
    "ReferenceId": "430df1ca-xxxx-xxxx-xxxx-89fd73642d25"
  },
  "ValidationErrors": [
    {
      "PropertyName": "Name",
      "UserMessage": "Names cannot contain the following characters: \ / : * ? " &lt; > |",
      "DeveloperMessage": "Names cannot contain the following characters: \ / : * ? " &lt; > |",
      "ErrorCode": 1001
    }
  ]
}
```

The validation error object contains the following properties:

- `PropertyName`: The property in the request that did not pass validation.
- `UserMessage`: A user-friendly message that you can display to the end user in UI-based applications. In some cases, this value is the same as the developer message.
- `DeveloperMessage`: Technical error information that developers can use for debugging.
- `ErrorCode`: The Docusign CLM error code for the error message.

## Docusign CLM error codes

Docusign CLM returns the following application error codes, along with a `UserMessage` and `DeveloperMessage` that you can use to investigate and resolve issues:

**100** - General Error

**101** - Validation Error

**103** - AccessDenied

**104** - Not Found

**105** - Failed To Save

**106** - Conflict

**107** - Invalid Folder Filter

**108** - Invalid System Folder

**109** - Folder Not Found

**110** - Invalid Sort Property

**111** - Search Criteria Missing

**112** - Too Many Items Requested

**113** - Parent Folder Required

**114** - Cannot Parse Uid From Uri

**115** - Cannot ParseId From Uri

**116** - File Data Required

**117** - Document Not Found

**118** - Manager Not Found

**119** - Document Not Yet Available

**120** - Uploads Not Allowed

**121** - Downloads Not Allowed

**122** - Can Not Update Lock On Version

**123** - Can Not Update Version

**124** - Invalid Page

**125** - Not Supported

**126** - Workflow Not Found

**127** - Share Link Folder Or Document Missing

**128** - Can Not View Lock On Version

**129** - MultiPart File Without Name

**130** - File Too Big

**131** - Aborted Completed Workflow

**132** - Signaled Completed Workflow

**133** - Invalid Filter Property

**134** - Required Property Missing

**135** - Missing Search Task

**136** - Missing Change Security Task

**137** - Security Object Required

**138** - Invalid Workflow Signal

**139** - Missing Document Process Tracking Task

**140** - Folder Required

**141** - Document Required

**142** - Scope Required

**143** - Invalid Group Type

**144** - Signature Task Not Found

**145** - Content Disposition With Filename Required

**146** - Unauthorized

**147** - Only One Document Allowed For External Review

**148** - New External Review Is Not Enabled

**149** - External Review Is Not Enabled

## Validation errors

Validation errors occur when the request is syntactically correct, but the rules configured in the Docusign CLM application do not allow the request to be completed. The API returns several validation error codes that you can display to the end user:

**1001** - Invalid Name

**1002** - Attribute Validation Failed

**1003** - Invalid Selection

**1004** - Invalid Parameters Or Access Denied

**1005** - Attribute Group Does Not Exist

**1006** - Attribute Field Does Not Exist

**1007** - Invalid Role

**1008** - Change Security Allowed Properties

**1009** - Invalid Access Type

**1010** - Invalid Email

**1011** - Invalid Document Href

**1012** - Document Is Checked Out

**1013** - At Least One Document Required For External Review

**1014** - Check Out Permission Denied

**1015** - Date Must Be In The Future

**1016** - Invalid Sender

**1017** - NotOutForExternalReview

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
