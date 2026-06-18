---
title: ': listStatusChanges'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:22Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/?explorer=true)

[Envelopes](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/)

# : listStatusChanges

This method lets you [search for envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/search/) in your accounts. A large set of filters let you narrow the scope of your search by date, by envelope ID, or by status codes. Your request must include one or more of the following parameters:

- `from_date`
- `envelope_ids`
- `transaction_ids`

### Restrictions

**Number of envelopes**

The number of envelopes returned is limited to 1,000 per call. To retrieve the next or previous set of envelopes, use the `nextUri` and `previousUri` parameters returned in the original call's response.

**Date range**

If no `from_date` query parameter is specified, envelopes from more than two years ago will not be returned. To fetch older envelopes, set the specific date range using the `from_date` and `to_date` parameters.

**Zero-size response check**

To avoid unnecessary database queries, the Docusign signature platform first checks requests to ensure that the filter set supplied does not result in a zero-size response before querying the database.

**Cross-site envelopes in production**

When using this endpoint in production, you cannot retrieve documents across different sites (NA2, EU1, CA, etc.). You can only obtain documents sent from the same site (URL).
If your account has envelopes on multiple production sites and you want to download their documents, you must make separate API calls to each site (URL) to retrieve the documents from all envelopes.

### Envelope statuses

This table shows the valid current envelope statuses (`status` parameter) for the different status qualifiers (`from_to_status` parameter) in the request. If the status and status qualifiers in the API request do not contain any of the values shown in the Valid Current Statuses column, then an empty list is returned.

Client applications should check that the statuses (`status` parameter) they are requesting make sense for a given `from_to_status` parameter value.

| Status Qualifier | Effective Status Qualifier | Valid Current Statuses |
| --- | --- | --- |
| any (changed) | StatusChanged | any, created, sent, delivered, signed, completed, declined, voided, deleted |
| created | Created | any, created, sent, delivered, signed, completed, declined, voided, deleted |
| sent | Sent | any, sent, delivered, signed, completed, declined, voided, deleted |
| delivered | StatusChanged | any, delivered, signed, completed, declined, voided, deleted |
| signed | StatusChanged | any, signed, completed, declined, voided, deleted |
| completed | Completed | any, completed, declined, voided, deleted |
| declined | StatusChanged | any, declined, voided, deleted |
| timedout always return zero results | StatusChanged | any, voided, deleted |
| voided | Voided | any, voided, deleted |
| deleted | StatusChanged | any, deleted |

### Extraneous results

In some cases, a request for a specific envelope status will
include envelopes with additional statuses. For example, in
a request with a `from_date` of 2017-01-01, a `to_date` of
2017-01-07 and the status qualifier (`from_to_status`) set
to `delivered`, the response set might contain envelopes
that were created during that time period, but not delivered
during the time period. As a workaround, check the envelope
status values in the result set as needed.

### Related topics

- [Searching for envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/search/)
- [How to list envelope status changes](https://developers.docusign.com/docs/esign-rest-api/how-to/list-envelope-status-changes/)

## Request

#### HTTP Request

GET

```
/restapi/v2.1/accounts/{accountId}/envelopes
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |

| Query Parameters |  |  |
| --- | --- | --- |
| ac\_status | string | Specifies the authoritative copy status for the envelopes. Valid values:   - `Unknown` - `Original` - `Transferred` - `AuthoritativeCopy` - `AuthoritativeCopyExportPending` - `AuthoritativeCopyExported` - `DepositPending` - `Deposited` - `DepositedEO` - `DepositFailed` |
| block | string | Reserved for Docusign. |
| cdse\_mode | string | Reserved for Docusign. |
| continuation\_token | string | Reserved for Docusign. |
| count | string | The maximum number of results to return.  The maximum value is 1000. To get the next or previous set of envelopes, use `nextUri` or `previousUri` from the response. |
| custom\_field | string | Optional. Specifies an envelope custom field name and value searched for in the envelopes. Format: `custom_envelope_field_name=desired_value`  Example: If you have an envelope custom field named "Region" and you want to search for all envelopes where the value is "West" you would use set this parameter to `Region=West`. |
| email | string | Limit results to envelopes sent by the account user with this email address.  `user_name` must be given as well, and both `email` and `user_name` must refer to an existing account user. |
| envelope\_ids | string | Comma separated list of `envelopeId` values. |
| exclude | string | Excludes information from the response. Enter as a comma-separated list (e.g., `folders,powerforms`).  Valid values:   - `recipients` - `powerforms` - `folders` |
| folder\_ids | string | Returns the envelopes from specific folders. Enter as a comma-separated list of either valid folder GUIDs or the following values:   - `awaiting_my_signature` - `completed` - `draft` - `drafts` - `expiring_soon` - `inbox` - `out_for_signature` - `recyclebin` - `sentitems` - `waiting_for_others` |
| folder\_types | string | Returns the envelopes from folders of a specific type. Enter as a comma-separated list of the following values:   - `normal` - `inbox` - `sentitems` - `draft` - `templates` |
| from\_date | string | Specifies the date and time to start looking for status changes. This parameter is required unless `envelopeIds` or `transactionIds` are set.  Although you can use any date format supported by the .NET system library's [`DateTime.Parse()`](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.parse?redirectedfrom=MSDN&view=net-5.0#overloads) function, Docusign recommends using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format dates with an explicit time zone offset. If you do not provide a time zone offset, the method uses the server's time zone.  For example, the following dates and times refer to the same instant:   - `2017-05-02T01:44Z` - `2017-05-01T21:44-04:00` - `2017-05-01T18:44-07:00`   If this property is not included, envelopes from the last two years will be returned. |
| from\_to\_status | string | This is the status type checked for in the `from_date`/`to_date` period. For example, if `Created` is specified, then envelopes created during the period are found. If `Changed` is specified, then envelopes that changed status during the period are returned. The default value is `Changed`.  Valid values:   - `Changed` - `Voided` - `Created` - `Deleted` - `Sent` - `Delivered` - `Signed` - `Completed` - `Declined` - `TimedOut` - `Processing` |
| include | string | Specifies additional information to return about the envelopes. Use a comma-separated list, such as `folders, recipients` to specify information. Valid values are:   - `custom_fields`: The custom fields associated with the envelope. - `documents`: The documents associated with the envelope. See the Restrictions section above for more information. - `attachments`: The attachments associated with the envelope. - `extensions`: Information about the email settings associated with the envelope. - `folders`: The folders where the envelope exists. - `recipients`: The recipients associated with the envelope. - `payment_tabs`: The payment tabs associated with the envelope. |
| include\_purge\_information | string | When **true,** information about envelopes that have been deleted is included in the response. |
| intersecting\_folder\_ids | string | A comma-separated list of folders from which you want to get envelopes. Valid values:   - `normal` - `inbox` - `sentitems` - `draft` - `templates` |
| last\_queried\_date | string | Returns envelopes that were modified prior to the specified date and time.  Example: `2020-05-09T21:56:12.2500000Z` |
| order | string | Returns envelopes in either ascending (`asc`) or descending (`desc`) order. |
| order\_by | string | Sorts results according to a specific property. Valid values:   - `last_modified` - `action_required` - `created` - `completed` - `envelope_name` - `expire` - `sent` - `signer_list` - `status` - `subject` - `user_name` - `status_changed` - `last_modified` |
| powerformids | string | A comma-separated list of `PowerFormId` values. |
| query\_budget | string | The time in seconds that the query should run before returning data. |
| requester\_date\_format | string |  |
| search\_mode | string |  |
| search\_text | string | Free text search criteria that you can use to filter the list of envelopes that is returned. |
| start\_position | string | The zero-based index of the result from which to start returning results.  Use with `count` to limit the number of results.  The default value is `0`. |
| status | string | A comma-separated list of current envelope statuses to be included in the response. Valid values:   - `completed` - `created` - `declined` - `deleted` - `delivered` - `processing` - `sent` - `signed` - `timedout` - `voided`   The `any` value is equivalent to any status. |
| to\_date | string | Specifies the date and time to stop looking for status changes. The default is the current date and time.  Although you can use any date format supported by the .NET system library's [`DateTime.Parse()`](https://docs.microsoft.com/en-us/dotnet/api/system.datetime.parse?redirectedfrom=MSDN&view=net-5.0#overloads) function, Docusign recommends using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format dates with an explicit time zone offset If you do not provide a time zone offset, the method uses the server's time zone.  For example, the following dates and times refer to the same instant:   - `2017-05-02T01:44Z` - `2017-05-01T21:44-04:00` - `2017-05-01T18:44-07:00` |
| transaction\_ids | string | A comma-separated list of envelope transaction IDs.  Getting envelope status by transaction IDs is useful for offline signing situations to determine if an envelope was created or not. It can be used for the cases where a network connection was lost before the envelope status could be returned.  **Note:** Transaction IDs are only valid in the Docusign system for seven days. |
| user\_filter | string | Returns envelopes where the current user is the recipient, the sender, or the recipient only. (For example, `user_filter=sender`.) Valid values are:   - `sender` - `recipient` - `recipient_only` |
| user\_id | string | The ID of the user who created the envelopes to be retrieved. Note that an account can have multiple users, and any user with account access can retrieve envelopes by user\_id from the account. |
| user\_name | string | Limit results to envelopes sent by the account user with this user name.  `email` must be given as well, and both `email` and `user_name` must refer to an existing account user. |

\* Required

## SDK Method

### Envelopes::listStatusChanges

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
