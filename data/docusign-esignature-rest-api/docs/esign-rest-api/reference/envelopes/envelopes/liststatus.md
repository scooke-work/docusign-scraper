---
title: ': listStatus'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatus/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:10:01Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatus/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatus/?explorer=true)

[Envelopes](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/)

# : listStatus

Retrieves envelope statuses for a set of envelopes. `Envelopes: listStatus` has both a `GET` and a `PUT` implementation:

- `PUT /restapi/v2.1/accounts/{accountId}/envelopes/status` is passed a set of envelope IDs in the request body. This version of the method returns a smaller subset of envelope information.
- `GET /restapi/v2.1/accounts/{accountId}/envelopes/status` is passed a list of envelope IDs in a query string.

To search for envelopes using a broad range of filters, use
[Envelopes: listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/)
instead of this method.

You must specify exactly one of the following query parameters:

| Parameter | Description |
| --- | --- |
| `from_date` | a valid UTC DateTime: `2016-01-01` |
| `envelope_ids` | - For the `GET` implementation of this method, include the envelope IDs in a comma-separated list. - For the `PUT` version of this method, you should use the `request_body` value for this parameter and include the list of envelope IDs in the request body. |
| `transaction_ids` | A comma-separated list of transaction IDs or the special value `request_body` |

When you use the special value `request_body`, the request body looks like this:

```
{
  "envelopeIds": [
    "44c5ad6c-xxxx-xxxx-xxxx-ebda5e2dfe15",
    "8e26040d-xxxx-xxxx-xxxx-1e29b924d237",
    "c8b40a2d-xxxx-xxxx-xxxx-4fe56fe10f95"
  ]
}
```

Omitting the request body altogether causes the endpoint to return an error.
The request body must be at least `{}`.

### Related topics

- [Searching for envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/search/)
- [How to list envelope status changes](https://developers.docusign.com/docs/esign-rest-api/how-to/list-envelope-status-changes/)

## Request

#### HTTP Request

PUT

```
/restapi/v2.1/accounts/{accountId}/envelopes/status
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |

| Query Parameters |  |  |
| --- | --- | --- |
| ac\_status | string | Specifies the Authoritative Copy Status for the envelopes. Valid values:   - `Unknown` - `Original` - `Transferred` - `AuthoritativeCopy` - `AuthoritativeCopyExportPending` - `AuthoritativeCopyExported` - `DepositPending` - `Deposited` - `DepositedEO` - `DepositFailed` |
| block | string | When **true,** removes any results that match one of the provided `transaction_ids`. |
| count | string | The maximum number of results to return.  Use `start_position` to specify the number of results to skip. |
| email | string | The email address of the sender. |
| envelope\_ids | string | The envelope IDs to include in the results.  The value of this property can be:   - For the `GET` implementation of this method, use a comma-separated list of envelope IDs. - For the `PUT` implementation of this method, use the `request_body` value, and include the envelope IDs in the request body. |
| from\_date | string | The date/time setting that specifies when the request begins checking for status changes for envelopes in the account. This is required unless parameters `envelope_ids` and/or `transaction_Ids` are provided.  **Note:** This parameter must be set to a valid `DateTime`, or `envelope_ids` and/or `transaction_ids` must be specified. |
| from\_to\_status | string | The envelope status that you are checking for. Possible values are:   - `Changed` (default) - `Completed` - `Created` - `Declined` - `Deleted` - `Delivered` - `Processing` - `Sent` - `Signed` - `TimedOut` - `Voided`   For example, if you specify `Changed`, this method returns a list of envelopes that changed status during the `from_date` to `to_date` time period. |
| start\_position | string | The zero-based index of the result from which to start returning results.  Use with `count` to limit the number of results.  The default value is `0`. |
| status | string | A comma-separated list of envelope status to search for. Possible values are:   - `completed` - `created` - `declined` - `deleted` - `delivered` - `processing` - `sent` - `signed` - `template` - `voided` |
| to\_date | string | Optional date/time setting that specifies the last date/time or envelope status changes in the result set.  The default value is the time that you call the method. |
| transaction\_ids | string | The transaction IDs to include in the results. Note that transaction IDs are valid for seven days.  The value of this property can be:   - A list of comma-separated transaction IDs - The special value `request_body`. In this case, this method uses the transaction IDs in the request body. |
| user\_name | string | Limits results to envelopes sent by the account user with this user name.  `email` must be given as well, and both `email` and `user_name` must refer to an existing account user. |

\* Required

## SDK Method

### Envelopes::listStatus

## Request Body

## Responses

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
