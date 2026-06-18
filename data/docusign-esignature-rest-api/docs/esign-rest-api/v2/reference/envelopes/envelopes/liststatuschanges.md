---
title: ': listStatusChanges'
source_url: https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/liststatuschanges/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:10:49Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/liststatuschanges/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/liststatuschanges/?explorer=true)

[Envelopes](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/)

# : listStatusChanges

Retrieves a list of envelopes that match your request.
A large set of optional filters let you filter
by date,
by envelope ID,
or by status codes.

Your request must include one or more of the following parameters:

- `from_date`
- `envelope_ids`
- `transaction_ids`

Getting envelope status using `transaction_ids` is useful
for offline signing situations where it can be used
determine if an envelope was created or not. It can be used
for the cases where a network connection was lost, before
the envelope status could be returned.

To avoid unnecessary database queries, the DocuSign
signature platform first checks requests to ensure that the
filter set supplied does not result in a zero-size response
before querying the database.

For example, for a request with a `from_to_status` of
`delivered` and a current `status` of `created,sent`,
DocuSign will always return an empty list.
This is because the request translates to: find the
envelopes that were delivered between the `from_date` and
`to_date` dates that have a current status of `created` or
`sent`. Since an envelope that has been delivered can
never have a status of `created` or `sent`, a zero-size
response would be generated.
In this case, DocuSign does not query the database
and returns an empty list immediately.

The following table shows the valid current envelope
statuses (`status` parameter) for the different status
qualifiers (`from_to_status` parameter) in the request. If
the status and status qualifiers in the API request do not
contain any of the values shown in the Valid Current
Statuses column, then an empty list is returned.

Client applications should check that the statuses (`status`
parameter) they are requesting make sense for a given
`from_to_status` parameter value.

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

## Extraneous results

In some cases, a request for a specific envelope status will
include envelopes with additional statuses. For example, in
a request with a `from_date` of 2017-01-01, a `to_date` of
2017-01-07 and the status qualifier (`from_to_status`) set
to `delivered`, the response set might contain envelopes
that were created during that time period, but not delivered
during the time period. As a workaround, check the envelope
status values in the result set as needed.

## Request

#### HTTP Request

GET

```
/restapi/v2/accounts/{accountId}/envelopes
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account id GUID. |

| Query Parameters |  |  |
| --- | --- | --- |
| ac\_status | string | Specifies the Authoritative Copy Status for the envelopes. The possible values are: Unknown, Original, Transferred, AuthoritativeCopy, AuthoritativeCopyExportPending, AuthoritativeCopyExported, DepositPending, Deposited, DepositedEO, or DepositFailed. |
| block | string | Reserved for DocuSign. |
| count | string | Optional. Number of items to return. Currently there is no implicit maximum limit of the number of items that can be returned. |
| custom\_field | string | Optional. Specifies a envelope custom field name and value searched for in the envelopes. Format: `custom_envelope_field_name=desired_value`  Example: If you have an envelope custom field named "Region" and you want to search for all envelopes where the value is "West" you would use set this parameter to `Region=West`. |
| email | string | Limit results to envelopes sent by the account user with this email address.  `user_name` must be given as well, and both `email` and `user_name` must refer to an existing account user. |
| envelope\_ids | string | Comma separated list of `envelopeId` values. |
| from\_date | string | Specifies the date and time to start looking for status changes. This parameter is required unless `envelopeIds` or `transactionIds` are set.  Although you can use any date format supported by the .NET system library's [`DateTime.Parse()`](https://msdn.microsoft.com/en-us/library/system.datetime.parse(v=vs.110).aspx#StringToParse) function, DocuSign recommends using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format dates with an explicit time zone offset If you do not provide a time zone offset, the method uses the server's time zone.  For example, the following dates and times refer to the same instant:   - `2017-05-02T01:44Z` - `2017-05-01T21:44-04:00` - `2017-05-01T18:44-07:00` |
| from\_to\_status | string | This is the status type checked for in the `from_date`/`to_date` period. If `changed` is specified, then envelopes that changed status during the period are found. If for example, `created` is specified, then envelopes created during the period are found. Default is `changed`.  Possible values are: Voided, Changed, Created, Deleted, Sent, Delivered, Signed, Completed, Declined, TimedOut and Processing. |
| start\_position | string | This value is supported and currently has no implicit maximum items. |
| status | string | A comma-separated list of current envelope statuses to included in the response. Possible values are:   - completed - created - declined - deleted - delivered - processing - sent - signed - timedout - voided   The `any` value is equivalent to any status. |
| to\_date | string | Specifies the date and time to stop looking for status changes. The default is the current date and time.  Although you can use any date format supported by the .NET system library's [`DateTime.Parse()`](https://msdn.microsoft.com/en-us/library/system.datetime.parse(v=vs.110).aspx#StringToParse) function, DocuSign recommends using [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format dates with an explicit time zone offset If you do not provide a time zone offset, the method uses the server's time zone.  For example, the following dates and times refer to the same instant:   - `2017-05-02T01:44Z` - `2017-05-01T21:44-04:00` - `2017-05-01T18:44-07:00` |
| transaction\_ids | string | If included in the query string, this is a comma separated list of envelope `transactionId`s.  If included in the `request_body`, this is a list of envelope `transactionId`s. Note: `transactionId`s are only valid in the DocuSign system for seven days. |
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
