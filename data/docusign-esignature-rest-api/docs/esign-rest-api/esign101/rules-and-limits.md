---
title: eSignature API rules and resource limits
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Rules and resource limits
scraped_at: '2026-06-18T20:28:08Z'
---

# eSignature API rules and resource limits

The eSignature API has a set of rules and resource limits that help ensure the security of the Docusign platform and your [integration](https://developers.docusign.com/docs/esign-rest-api/). These rules and limits also help you build your integration in a way that is efficient and scalable.

The API rules and resource limits listed in this topic exist alongside the rules and limits that apply at the [platform level](https://developers.docusign.com/platform/resource-limits/) to all Docusign APIs.

This topic includes:

- [Request limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#request-limits)
- [Document upload and download limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#document-upload-and-download-limits)
- [File size limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#file-size-limits)
- [HTTP request limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#http-request-limits)
- [Polling rate limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#polling-rate-limits)
- [Anchor tab request limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#anchor-tab-request-limits)
- [Envelope custom field limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#envelope-custom-field-limits)
- [Account limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#account-limits)
- [Envelope recipient limit](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#envelope-recipient-limit)
- [Get templates request limit](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#get-templates-request-limit)
- [Best practices](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/#best-practices)

## Request limits

In addition to the standard request limits applied at the [platform level](https://developers.docusign.com/platform/resource-limits/), the Docusign eSignature API implements several API request limits designed to protect the performance of your integrations.

- Accounts have a maximum number of requests per hour. The total number of requests from all integrations associated with an account cannot exceed this limit. This value can be found in the response header of any request using the `X-RateLimit-Limit` response header. Hourly API usage is refreshed on the hour (e.g., 1:00 pm - 2:00 pm). You can [update this limit](https://developers.docusign.com/tools/api-usage-center/limit-management/) through the API Usage Center if your account meets certain prerequisites.
- Accounts are restricted in the number of GET or PUT requests they can make per envelope, per hour. This includes the envelope and all objects that the envelope contains, such as documents.
  - If your account makes too many GET requests for an envelope in an hour period, you may receive an `Hourly_Envelope_Polling_Limit_Exceeded` error.
  - If your account makes too many GET requests for an envelope in a 30-second burst period, you may receive a `Burst_Envelope_Polling_Limit_Exceeded` error.
  - If your account makes too many PUT requests for an envelope in an hour period, you may receive an `Hourly_APIInvocation_Envelope_Limit_Exceeded` error.
  - If your account makes too many PUT requests for an envelope in a 30-second burst period, you may receive a `Burst_APIInvocation_Envelope_Limit_Exceeded` error.

    To avoid exceeding these limits and encountering errors, try to use five API calls or fewer when creating or updating the envelope. This includes envelope creation, sending, and any updates. As a best practice, use [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/) to track your envelopes rather than manually making GET calls to poll for their status. If Connect is not available in your infrastructure, limit polling and reduce the rate at which you poll over time.
- Individual apps have an additional limit for calls to get envelope status. Apps are limited to one GET status request per unique envelope per 15 minutes. If you exceed this limit, the request will not fail, but it will be flagged as a violation of rate limits, which can cause your app to fail review for [Go-Live](https://developers.docusign.com/docs/esign-rest-api/go-live/). To avoid exceeding this limit, design your app to poll at 20-minute intervals rather than 15 or, rather than polling for envelope status, your integration can subscribe to [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/) to get status updates for the envelope.

For example, the following transactions violate API rules due to the repeated GET requests to the first document and second recipient:

```
[12:00:00] POST /accounts/12345/envelopes
[12:01:00] GET /accounts/12345/envelopes/AAA/documents/1
[12:02:00] GET /accounts/12345/envelopes/AAA/recipients/2
[12:03:00] POST /accounts/12345/envelopes
[12:04:00] GET /accounts/12345/envelopes/AAA/documents/1 *
[12:05:00] GET /accounts/12345/envelopes/AAA/recipients/2 *
```

However, the following set of requests comply with API rules and limits and would not be flagged by the platform:

```
[12:00:00] POST /accounts/12345/envelopes
[12:01:00] GET /accounts/12345/envelopes/AAA
[12:16:00] GET /accounts/12345/envelopes/AAA
[12:17:00] GET /accounts/12345/envelopes/AAA/documents/1
[12:32:00] GET /accounts/12345/envelopes/AAA/documents/1
[12:40:00] PUT /accounts/12345/envelopes/AAA/recipients/1
[12:41:00] PUT /accounts/12345/envelopes/AAA/recipients/1
```

If you exceed the API rate limit, you will receive the error: "The maximum number of hourly API invocations has been exceeded."

### Burst limit

To protect against possible attacks on the platform, a shorter 30-second burst limit of 200 calls in the developer environment (or 500 calls, in the production environment) is also implemented at the account level to prevent applications from making large numbers of calls in very short periods of time.

## Document upload and download limits

To prevent degradation of service caused by long-running and inoperable document uploads or downloads, Docusign enforces limits on concurrent upload or download requests. These limits apply to in-progress requests for the same document. Requests are not subject to these limits if they upload or download documents that are not referenced in other concurrent requests.

Integration developers should take steps to prevent document upload and download requests for the same document from being sent to Docusign too frequently and exceeding the limits.

### API endpoints subject to upload limits

Requests to these eSignature REST API endpoints are subject to the document upload limits:

- [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/)
- [EnvelopeDocuments:update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/update/)
- [EnvelopeDocuments:updateList](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/updatelist/)
- [Templates:create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/create/)
- [TemplateDocuments:update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/update/)
- [TemplateDocuments:updateList](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/updatelist/)

### Upload limit details

For document upload limits, documents are identified using the document bytes. Any in-progress upload requests with identical document bytes are subject to the limits, even if the requests are not associated with the same account or integration.

The limits for uploads of the same document are:

- A maximum of 70 in-progress uploads of the same document that started within the last hour.
- A maximum of 70 in-progress uploads of the same document that started within the last six hours.

Requests to different endpoints that reference the same document can cause an upload limit to be exceeded. For example, 40 `EnvelopeDocuments:update` requests and 40 `EnvelopeDocuments:updateList` requests in the same hour will exceed the limit if they all reference the same document.

Limits are enforced as follows:

- Any document upload requests that exceed either the one-hour or six-hour maximum will be blocked and never executed.
- If either limit is exceeded and requests have been blocked, the counter for that limit's upload requests will reset to zero on completion of any in-progress request that began processing before the limit was exceeded. At that point, new upload requests for the document will be permitted, up to the limits.
- Because limits are enforced per document, an upload request for multiple documents may have one blocked due to exceeding a limit, while the others referenced in the request are successfully uploaded. In this case, the request will return a 200 OK status code. The response body will indicate which documents were successfully uploaded and which ones were blocked.

### Error response for upload limit violation

If a request fails because it exceeded an upload limit, Docusign returns this error response:

```
{
  "errorCode":"UNSPECIFIED_ERROR",
  "message":"PDF validation failed"
}
```

### Upload limit example case

In the example case illustrated below, all upload requests are for the same document, as identified by the document bytes.

| Time | Upload requests received | Upload requests finished | 1-hour counter total | 6-hour counter total | Result |
| --- | --- | --- | --- | --- | --- |
| 12:00 | 70 | 0 | 70 | 70 | Within limits. All requests are processing. |
| 12:45 | 10 | 0 | 80 | 80 | One-hour and six-hour limits of 70 exceeded. The 10 new requests are blocked and will never be executed. The previous 70 requests continue processing. |
| 1:00 | 0 | 1 | 0 | 0 | Because one request finished, both the counters are reset. The remaining 69 requests continue processing. |
| 3:00 | 40 | 0 | 40 | 40 | Within limits. The 40 new requests are processing along with the previous 69, for a total of 109. |
| 5:00 | 40 | 0 | 40 | 80 | Six-hour limit of 70 exceeded. The one-hour counter only has 40 because the previous batch was received more than an hour ago. Because the six-hour counter has exceeded the limit of 70, only the first 30 new requests are processed. The last 10 are blocked. The total now processing is 139. |

### API endpoints subject to download limits

Requests to these eSignature REST API endpoints are subject to the document download limits:

- [EnvelopeDocuments:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/get/)
- [TemplateDocuments:get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/get/)

### Download limit details

The limits for downloads of the same document are:

- For requests that specify the `combined` option, which retrieves all of an envelope's or template's documents in a single PDF file:
  - A maximum of three in-progress downloads of the same document that started within the last hour
  - A maximum of five in-progress downloads of the same document that started within the last six hours
- For all other download types (see the table below for a list of types):
  - A maximum of 10 in-progress downloads of the same document that started within the last hour
  - A maximum of 20 in-progress downloads of the same document that started within the last six hours

Any in-progress download requests for the same document are subject to the limits, even if the requests are not associated with the same account or integration.

To maintain the counters for downloads of the same document, Docusign uses the following criteria:

| Download request type | Downloads are considered to be for the same document if the API request has |
| --- | --- |
| Individual document | The same envelope ID and document ID or the same template ID and document ID |
| ZIP archive that contains all of an envelope's PDF documents and the certificate of completion | The same envelope ID and the `archive` option specified |
| Envelope certificate of completion | The same envelope ID and the `certificate` option specified |
| A PDF portfolio containing all of an envelope's documents | The same envelope ID and the `portfolio` option specified |
| All of an envelope's or template's documents in a single PDF file | The same envelope ID and the `combined` option specified or the same template ID and the `combined` option specified |

Limits are enforced as follows:

- Any document download requests that exceed either the one-hour or six-hour maximum will be blocked and never executed.
- If either limit is exceeded and requests have been blocked, the counter for that limit's download requests resets to zero on completion of any in-progress request that began processing before the limit was exceeded. At that point, new download requests for the document will be permitted, up to the limits.

### Error response for download limit violation

If a request fails because it exceeded a download limit, Docusign returns this error response:

```
{
  "errorCode":"API_REQUEST_IS_THROTTLED",
  "message":"GetDocument call blocked"
}
```

### Download limit example case 1

In the example case illustrated below, all download requests are for the same individual document, as identified by the envelope ID in combination with the document ID.

| Time | Download requests received | Download requests finished | 1-hour counter total | 6-hour counter total | Result |
| --- | --- | --- | --- | --- | --- |
| 12:00 | 10 | 0 | 10 | 10 | Within limits. All requests are processing. |
| 12:45 | 1 | 0 | 11 | 11 | One-hour limit of 10 exceeded. The new request is blocked and will never be executed. The previous 10 requests continue processing. |
| 1:00 | 0 | 1 | 0 | 0 | Because one request finished, both counters reset. The remaining nine requests continue processing. |
| 2:00 | 10 | 0 | 10 | 10 | Within limits. The 10 new requests are processing along with the previous nine, for a total of 19. |
| 3:01 | 10 | 0 | 10 | 20 | Within limits. The one-hour counter only has 10 because the previous batch was received more than an hour ago. The 10 new requests are processing along with the previous 19, for a total of 29. |
| 4:02 | 10 | 0 | 10 | 30 | Six-hour limit of 20 exceeded. The 10 new requests are blocked. The total now processing remains at 29. |

### Download limit example case 2

In the example case illustrated below, all download requests are for the same envelope ID.

| Time | Download type | Number of requests received | Downloads finished | 1-hour counter total | 6-hour counter total | Result |
| --- | --- | --- | --- | --- | --- | --- |
| 12:00 | Individual document with ID 1 | 10 | 0 | 10 | 10 | Within limits. All requests are processing. |
| 12:00 | Archive | 10 | 0 | 10 | 10 | Within limits.  All requests are processing. Although this batch and the previous batch are for the same envelope, they are considered different documents due to the download type, and are tracked in separate counters. |
| 12:00 | Combined | 3 | 0 | 3 | 3 | Within limits. Tracked in separate counters from the previous two batches due to the download type. |
| 12:15 | Archive | 1 | 0 | 11 | 11 | One-hour limit of 10 exceeded for archive type downloads for the envelope. The new request is blocked and will never be executed. The individual and combined downloads continue processing, along with the 10 previous archive downloads. |
| 12:30 | Archive | 0 | 1 | 0 | 0 | Because one archive download request finished, both archive counters are reset. The remaining nine archive requests continue processing. |
| 12:30 | Individual document with ID 2 | 10 | 0 | 10 | 10 | Within limits. Although there is already a batch of 10 individual document downloads in progress, they are for a different document ID and are tracked in separate counters. |
| 2:00 | Combined | 2 | 0 | 2 | 5 | Within limits. The one-hour counter only has two because the previous batch of combined requests was received more than an hour ago. The two new requests are processing along with the previous three, for a total of five. |
| 3:00 | Combined | 1 | 0 | 1 | 6 | Six-hour limit exceeded. The new combined download request is blocked. The total of combined downloads processing remains at five. |

## File size limits

Docusign has the following limitations on files used in envelopes and attachments:

- There is a limit of 50 MB per upload to an envelope when using the UI, or 32 MB per upload when using the API. You can use [chunked uploads](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/) to upload documents in pieces of up to 52 MB.
- The total envelope size, including all the documents, cannot exceed 200 MB.
- There is a file size limit of 5 MB when attaching completed documents to emails sent by Docusign to recipients when an envelope is completed. If the completed documents are larger than 5 MB, the email provides a link to the documents on the Docusign system.
- For signer-uploaded attachments (files uploaded through the console), Docusign supports file sizes up to 25 MB for an envelope.
- When bulk sending envelopes, the size of the envelope to be bulk-sent cannot exceed 75 MB.

Depending on the recipient’s internet connection, attaching large files or a large number of files might affect signing performance.

## HTTP request limits

The maximum request size for an incoming HTTP request is between 35 and 36 MB (35651584 bytes). Note that request length is different from document limits such as `MaxPageCount`.

## Polling rate limits

For any specific envelope, polling status requests are limited to once every 15 minutes. To avoid violating the API rules, design your app to poll at 20-minute intervals, rather than 15.

To avoid excessive polling, you can specify a span of time to poll in each [Envelopes:listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/) or equivalent `listStatusChanges` SDK method call. To ensure that you don’t miss any changes, we recommend that you request overlapping times in your polls or subscribe to [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/) to get status updates for the envelope.

## Anchor tab request limits

Docusign has the following limitations on the number of [anchor tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/auto-place/) and anchor tab strings:

- The maximum number of anchor tab instances that can be present in an envelope is 3,000. The number of anchor tabs on each document (in the request body or server templates) included in the envelope counts toward this limit. Any calls that attempt to add anchor tabs that would bring the total number of anchor tabs above 3,000 will fail.
- The maximum number of anchor tab strings that can be used in an API call (including multi-request calls) is 3,000. The number of anchor tab strings for each document (in the request body or server templates) included in the call counts toward this limit. If you exceed this limit, the API call will fail.

## Envelope custom field limits

Your account can define a maximum of 500 envelope custom fields. The maximum length of an envelope custom field name or value is 100 characters.

## Account limits

The maximum number of integration keys, Connect configurations, and signing groups that can be created for an account are:

- 100 integration keys
- 20 Connect configurations
- 50 signing groups

## Envelope recipient limit

Each envelope can have a maximum of 100 recipients.

## Get templates request limit

A [Templates:list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/list/) request is limited to returning a maximum of 2,000 templates. If more than 2,000 templates are found, only the first 2,000 are returned.

## Best practices

- **Checking API limits:** In every API response, Docusign includes headers that tell you (1) what your current API calls/hour limit is, and (2) how much of that limit is remaining for the current hour. Docusign recommends that your application read the headers and, when the limit is reached for the hour, pause all activity until the next hour. We also recommend that you log, monitor, and build alerts to notify you when the API calls/hour is getting close to the limit. By default, each account has 3,000 API calls/hour as its limit. You can [update this limit](https://developers.docusign.com/tools/api-usage-center/limit-management/) through the API Usage Center if your account meets certain prerequisites. See [API resource limits](https://developers.docusign.com/platform/resource-limits/) for details about response headers that contain limit information.
- **Gradually scaling your service:** Scaling up is always a slow discovery of bottlenecks and addressing them one by one. We recommend starting slowly and ramping up over time.

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
