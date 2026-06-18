---
title: ': createBulkSendList'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendlist/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:31Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendlist/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendlist/?explorer=true)

[BulkSend](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/)

# : createBulkSendList

This method creates a bulk send list that you can use to send an envelope to up to 1,000 recipients at once.

### Related topics

- [How to bulk send envelopes](https://developers.docusign.com/docs/esign-rest-api/how-to/bulk-send-envelopes/)

### Errors

| Error code | Description |
| --- | --- |
| BULK\_SEND\_MAX\_COPIES\_EXCEEDED | A bulk sending list cannot specify more than XXX copies in the mailing list. Call the settings API endpoint to find the maximum number of copies in a batch allowed for your account. In almost all cases, the default limit is 1000. |
| BULK\_SEND\_RECIPIENT\_IDS\_MUST\_BE\_UNIQUE | No two recipientIds can be same within a bulkCopy. Same restriction as a regular envelope applies. Specify unique recipient IDs for each recipient within a bulkCopy (model for envelope in mailing list). |
| BULK\_SEND\_RECIPIENT\_ID\_REQUIRED | If no RoleName is present, recipientID is required in mailing list's bulkCopy. Add a roleName (that coalesces with template/envelope) or a recipientID. |
| BULK\_SEND\_RECIPIENT\_NAME\_REQUIRED | Recipient {0} has no name. Specify a name for the recipient. |
| BULK\_SEND\_EMAIL\_ADDRESS\_REQUIRED\_FOR\_EMAIL\_RECIPIENT | Recipient {0} is an email recipient with no email address. Specify an email for the email recipient. |
| BULK\_SEND\_FAX\_NUMBER\_REQUIRED\_FOR\_FAX\_RECIPIENT | Recipient {0} is a fax recipient with no fax number. Specify a fax number for the fax recipient. |
| BULK\_SEND\_FAX\_NUMBER\_NOT\_VALID | Recipient {0} specifies fax number {1}, which is not valid. Specify a valid fax number for the fax recipient. |
| BULK\_SEND\_EMAIL\_ADDRESS\_NOT\_VALID | Recipient {0} specifies email address {1}, which is not a valid email address. Specify a valid email address for the recipient. |
| BULK\_SEND\_PHONE\_NUMBER\_REQURED\_FOR\_SMS\_AUTH | Recipient {0} specifies SMS auth, but no number was provided. Specify a phone number for the SMS auth recipient. |
| BULK\_SEND\_PHONE\_NUMBER\_INVALID\_FOR\_SMS\_AUTH | Recipient {0} specifies phone number {1} for SMS auth, which is not valid. Specify a valid phone number for the SMS auth recipient. |
| BULK\_SEND\_ROLE\_NAMES\_MUST\_BE\_UNIQUE | Recipient role names cannot be duplicated; role {duplicateRecipientRole} appears multiple times. Use unique roleNames for recipients. |
| BULK\_SEND\_CANNOT\_USE\_BOTH\_ROLE\_AND\_ID\_ON\_SAME\_RECIPIENT | Recipients cannot have both ID and Role; {0} has both. Specify a roleName or recipientId, but not both for the same recipient. |
| BULK\_SEND\_CANNOT\_USE\_BOTH\_ROLE\_AND\_ID\_IN\_SAME\_LIST | Cannot use both recipient role and ID in the same list. Specify a roleName or recipientId, but not both in the same list. |
| BULK\_SEND\_INVALID\_ID\_CHECK\_CONFIGURATION | Recipient {0} specified SMS authentication, but no SMS auth settings were provided. Provide an SMS auth setting (proper ID configuration) if SMS auth is specified. |
| BULK\_SEND\_INVALID\_SBS\_INPUT\_CONFIGURATION | Recipient {0} has more than one signature provider specified. Or signingProviderName is not specified. Or Signature provider : {0} is either unknown or not an available pen for this account. One or more SBS configuration is missing or invalid. The error details provide specifics. |
| BULK\_SEND\_TAB\_LABELS\_MUST\_BE\_UNIQUE | Tab label {0} is duplicated. Needs to be unique. Use a unique tab label. |
| BULK\_SEND\_TAB\_LABEL\_REQUIRED | Tab label is required. Specify a tab label. |
| BULK\_SEND\_TAB\_VALUE\_REQUIRED | Tab Label value is required. Specify a value for the tab label. |
| BULK\_SEND\_ENVELOPE\_CUSTOM\_FIELD\_NAME\_MUST\_BE\_UNIQUE | Custom fields must have distinct names. The field {0} appears more than once in a copy. Use unique names for custom fields. |
| BULK\_SEND\_ENVELOPE\_CUSTOM\_FIELD\_NAME\_REQUIRED | All custom fields must have names. Specify a name for the custom field. |
| BULK\_SEND\_ENVELOPE\_CUSTOM\_FIELD\_VALUE\_REQUIRED | Custom field {0} has no value. A custom field can have an empty value, but it cannot have a null value. Specify a value for the custom field. |

## Request

#### HTTP Request

POST

```
/restapi/v2.1/accounts/{accountId}/bulk_send_lists
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The ID of the account. |

\* Required

## SDK Method

### BulkEnvelopes::createBulkSendList

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
