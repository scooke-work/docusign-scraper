---
title: Formatting API requests
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/requests/
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
- Requests
scraped_at: '2026-06-18T20:28:08Z'
---

# Formatting API requests

When making a request to the eSignature API, you must include the following set of data:

- **The****`base_uri`****for your account**, which is used to build the full path of the API call. To find your base URI, you can call the [UserInfo endpoint](https://developers.docusign.com/platform/auth/reference/user-info/) or look in your [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page.
  - For integrations in the developer environment, the base URI is `https://demo.docusign.net/`
  - For integrations in production, the base URI is in the form `https://{server}.docusign.net/`
- **Your API account ID**, which is also used to build the full path of the API call. You can find your API account ID on the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page.
- **An access token**, which is obtained via [Authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/) and attached as a request header for the call.

To build the base path of your call, include your `base_uri` and API account ID in the following format (using `/restapi/v2.1/accounts/` as an example endpoint):

`{base_uri} + "/restapi/v2.1/accounts/" + {api_account_id}`

Always use HTTPS to send eSignature API requests in both the developer and production environments.

## Request headers

Every API request must have an authentication header.

| Authentication method | Required header |
| --- | --- |
| OAuth2 | `Authorization: Bearer <OAuth2 token>` |

The default request body format is JSON. If the request body is in XML, you must supply a `Content-Type` header.

| Format | Request header |
| --- | --- |
| JSON | `Content-Type: application/json` |
| XML | `Content-Type: application/xml` |

## Request parameters

A request can take path parameters or query parameters. Path parameters are always required. Query parameters are usually optional.

The **Parameters** section of the [API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/) for each method shows you which parameters are path parameters and which are query parameters.

## Request body

Request bodies are usually used in `POST` requests to send information to the platform. The request body can be formatted as JSON or XML. If you don’t specify a format in a `Content-Type` header, the default is JSON.

If the request body does not match the `Content-Type` header, you will get a 400 or 415 response status code.

## Timing requests

You can add an `X-DocuSign-TimeTrack` header to your request to track how long it took to complete. If you use this header, the API response header will include an `X-DocuSign-TimeTrack` property with two semicolon-separated values showing the start and end times of the request, such as:

`REST0_Start,2016-10-20T21:58:00.7388927Z;REST0_End,2016-10-20T21:58:03.0514225Z`

If you provide a value for `X-DocuSign-TimeTrack` in the request, it will appear before the time values in the response header.

`MyApp 2.0 (gdef6cd);REST0_Start,2016-10-20T21:58:00.7388927Z;REST0_End,2016-10-20T21:58:03.0514225Z`

## Multipart form requests (binary transfer)

Some API methods, such as [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/), require you to provide source content for your documents. You can provide source content by:

- Base64-encoding the document and inserting the encoded bytes in the appropriate field. In the [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) method, this is the `documentBase64` field.
- Using multipart form requests, also known as *binary transfer*.

Binary transfer is 33% more efficient than base64 encoding and is recommended for all documents that are larger than 15 MB. To perform binary transfer, you must:

- Wrap each part of the document (which is formatted as bytes) in two hyphens and a value identifying the boundary separator (which should be unique in your document).
- Define a `Content-Disposition: form data` header for each part of the document.

See [How to attach documents via binary transfer](https://developers.docusign.com/docs/esign-rest-api/how-to/send-binary/) for a full example.

## Base64 encoding

The base64 content type encoding is supported for documents and images by setting the `Content-Transfer-Encoding` header to `base64`.

For `PUT` and `POST` requests, this setting indicates that the document or image bytes are encoded as base64, and the platform should decode the stream.

For `GET` requests, this setting indicates that the document or image bytes requested are to be encoded as base64 by Docusign before sending them in the response. This header is set in the response if the conversion was performed.

## Best practices for uploading documents

When uploading documents to your envelope, use the following guidelines for the best efficiency. For documents:

- Smaller than 25 MB, include them as a base64 encoded string in the envelope definition.
- Larger than 25 MB but smaller than 32 MB, use [binary transfer](https://developers.docusign.com/docs/esign-rest-api/how-to/send-binary/).
- Larger than 32MB, use [chunked uploads](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/).

Ensure that your documents are 52 MB or smaller. Documents that are 50 MB larger can cause delays for envelope operations.

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
