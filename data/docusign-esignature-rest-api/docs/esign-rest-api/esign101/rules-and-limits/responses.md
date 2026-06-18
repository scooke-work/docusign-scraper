---
title: Handling API responses
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/responses/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Rules and resource limits
- Rules and resource limits
- Responses
scraped_at: '2026-06-18T21:09:48Z'
---

# Handling API responses

Responses are usually JSON or XML-formatted objects. In some cases, such as when requesting a document, the response is data.

## Response status

Successful API responses are in the 200 range. The body of the response has the result.

| Status | Description |
| --- | --- |
| 200 | Successful |
| 201 | Created.   **Example:** An envelope has been successfully created. |
| 204 | No Content response. |
| 400 | Bad Request.   **Example**: The request is missing information or not legal XML or JSON. |
| 401 | Unauthorized. **Example:** Your integration key is incorrect. |
| 403 | Forbidden.   **Example:** user lacks permission to complete this action. |
| 408 | Request timeout. |
| 415 | Unsupported media type.   **Example:** Your request may be in XML, but you did not specify Content-Type: application/xml in the request header. |
| 429 | Too many requests. |
| 444 | No response. Indicated dropped connection by server. |

Error results have a response body that describes the error:

```
{
  "errorCode": "PARTNER_AUTHENTICATION_FAILED",
  "message": "The specified integrator key was not found or is disabled. An integrator key was not specified."
}
```

## Response headers

In addition to the standard response headers, API responses include the following headers.

| Header | Description |
| --- | --- |
| X-BurstLimit-Limit | The maximum number of API requests you can make in a 30-second burst. |
| X-BurstLimit-Remaining | The number of API requests left before you reach the burst limit. |
| X-RateLimit-Limit | The maximum number of API requests you can make. |
| X-RateLimit-Remaining | The number of API requests left before you reach the limit. |
| X-RateLimit-Reset | The time, in Unix Epoch terms, when the rate limit will be reset. |
| Content-Type | The format of the response. Usually one of application/json, application/xml, or application/pdf. |
| Content-Disposition | Present only if the body is an attachment. Specifies the attachment’s file name. |

## Response body

API responses use the following conventions:

- All response fields are in camelCase: `userName`, `envelopeId`.
- All values that represent constants or enumerations, except for errors, are given in lowercase: `status: 'created'`.
- Error constants are in uppercase.
- Fields with `uri` in their name are relative to the base URL.
- Fields with `url` in their name are fully qualified URLs.
- All times are in [UTC](https://www.timeanddate.com/worldclock/timezone/utc).

By default, responses are formatted as JSON. Otherwise, results are rendered according to the `Content-Type` header in the request. For example, if you request a document from an envelope, the response body contains the data of a PDF file, and the content type is `application/pdf`.

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
