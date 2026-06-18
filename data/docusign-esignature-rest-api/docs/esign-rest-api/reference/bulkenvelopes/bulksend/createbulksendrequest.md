---
title: ': createBulkSendRequest'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendrequest/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:31Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendrequest/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendrequest/?explorer=true)

[BulkSend](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/)

# : createBulkSendRequest

This method queues envelopes for bulk sending to multiple recipients. It requires an existing bulk send list (created using the [BulkSend::createBulkSendList](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendlist/) method) and an envelope or `templateID`.

Consider using the [BulkSend::createBulkSendTestRequest](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendtestrequest/) method to test your bulk send list against the envelope or template that you want to send first. To learn about the complete bulk send flow, see the [Bulk Send overview](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/).

If the envelopes were successfully queued for asynchronous processing, the response contains a `batchId` that you can use to get the status of the batch. If a failure occurs, the API returns an error message.

**Note:** The entire batch either queues successfully or fails. Partial success does not occur.

### Related topics

- [How to bulk send envelopes](https://developers.docusign.com/docs/esign-rest-api/how-to/bulk-send-envelopes/)

### Errors

This method returns the following errors:

| Error code | Description |
| --- | --- |
| BULK\_SEND\_ENVELOPE\_NOT\_IN\_SENDABLE\_STATE | Envelope {0} is not in a sendable state. The envelope is not complete. Make sure it has a sendable status, such as `created`. |
| BULK\_SEND\_ENVELOPE\_LIST\_CONTAINS\_NO\_COPIES | Cannot send an envelope with a bulk sending list which contains no copies. The list you're trying to bulk send is empty. Make sure the bulk sending list you're using contains recipients. |
| BULK\_SEND\_ENVELOPE\_LIST\_CONTAINS\_TOO\_MANY\_COPIES | Bulk sending list contains more than {0} copies. The list you're trying to bulk send will cause your account to exceed the 1,000-copy limit imposed for all accounts. Try sending two or more separate lists. |
| BULK\_SEND\_ENVELOPE\_CANNOT\_BE\_NULL | Cannot send a bulk list without an envelope. Specify the envelope ID or template ID for the envelope you want to bulk send. |
| BULK\_SEND\_BLOB\_STORE\_ERROR | Could not save copy of bulk sending list. An error writing to the database occurred. Try again. If the error persists, contact Docusign Support. |
| BULK\_SEND\_ACCOUNT\_HAS\_TOO\_MANY\_QUEUED\_ENVELOPES | Cannot send this bulk sending list because doing so would exceed the maximum of {maxCopies} in-flight envelopes. This account currently has {unprocessedEnvelopes} envelopes waiting to be processed. Please try again later, or contact Docusign Support to request a higher tier." |
| BULK\_SEND\_ENVELOPE\_NOT\_FOUND | Envelope {envelopeOrTemplateId} does not exist or you do not have permission to access it. The envelopeId or templateId specified could not be found. Specify a valid value. |
| BULK\_SEND\_LIST\_NOT\_FOUND | Bulk Sending list {listId} does not exist or you do not have permission to access it. The mailingListId specified could not be found. Specify a valid value. |
| BULK\_SEND\_ENVELOPE\_HAS\_NO\_RECIPIENTS | Bulk sending copy contains recipients, but the specified envelope does not. The recipients on the envelope and the bulk send list do not match. Make sure the envelope and list are compatible for sending. |
| BULK\_SEND\_RECIPIENT\_ID\_DOES\_NOT\_EXIST\_IN\_ENVELOPE | Recipient {0} does not exist in the envelope. Add the missing recipient to the envelope. |
| BULK\_SEND\_RECIPIENT\_ID\_DOES\_NOT\_MATCH | Recipient ID {envelopeMember.ID} does not match. Make sure the recipient information in the list and the envelope match up. |
| BULK\_SEND\_ENVELOPE\_HAS\_BULK\_RECIPIENT | Recipient {0} is a bulk recipient. This is not supported. No legacy 'bulk recipient' allowed. In v2.1 of the eSignature API, you must use a bulk send list instead of a bulk recipient. See the API documentation for details. |
| BULK\_SEND\_RECIPIENT\_ROLE\_DOES\_NOT\_MATCH | Recipient Role {envelopeMember.RoleName} does not match. Make sure the recipient information in the list and the envelope is compatible. |
| BULK\_SEND\_DUPLICATE\_RECIPIENT\_DETECTED | Duplicate recipients ({0}) not allowed, unless recipients have unique routing order specified on envelope. |
| BULK\_SEND\_ENVELOPE\_HAS\_NO\_TABS | Bulk sending copy contains tabs, but the specified envelope does not. List and envelope tabs cannot be coalesced. Make sure they are compatible for sending. |
| BULK\_SEND\_TAB\_LABEL\_DOES\_NOT\_EXIST\_IN\_ENVELOPE | Tab with label {0} does not exist in envelope. Add the tab label to the envelope, remove the label from the list, or make sure you're specifying the correct list and envelope. |
| BULK\_SEND\_TAB\_DOES\_NOT\_MATCH | Tab {0} does not match {0} in envelope. A tab exists on the list that does not match or is missing on the envelope. Make sure the tabs on the list and the envelope match. |
| BULK\_SEND\_ENVELOPE\_HAS\_NO\_ENVELOPE\_CUSTOM\_FIELDS | Bulk sending copy contains custom fields, but the specified envelope does not. There are custom fields on the list that the envelope does not have. Make sure that any custom fields on the list and the envelope match. |
| BULK\_SEND\_ENVELOPE\_CUSTOM\_FIELD\_DOES\_NOT\_EXIST\_IN\_ENVELOPE | Custom field {0} does not exist in the envelope. Either add the custom field on the list to the envelope, remove the custom field from the list, or make sure you're specifying the correct list and envelope. |
| BULK\_SEND\_ENVELOPE\_CUSTOM\_FIELD\_NAME\_DOES\_NOT\_MATCH | Custom field names must match. {0} and {1} do not match. The custom field names on the list and the envelope do not match. Use identical names for both. |

## Request

#### HTTP Request

POST

```
/restapi/v2.1/accounts/{accountId}/bulk_send_lists/{bulkSendListId}/send
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| bulkSendListId \* | string | The GUID of the bulk send list. This property is created after you post a new bulk send list. |

\* Required

## SDK Method

### BulkEnvelopes::createBulkSendRequest

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
