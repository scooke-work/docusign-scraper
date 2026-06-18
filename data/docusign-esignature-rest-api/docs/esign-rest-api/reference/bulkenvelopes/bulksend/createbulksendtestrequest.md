---
title: ': createBulkSendTestRequest'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendtestrequest/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:31Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendtestrequest/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendtestrequest/?explorer=true)

[BulkSend](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/)

# : createBulkSendTestRequest

This method tests a bulk send list for compatibility with the envelope or template that you want to send. For example, a template that has three roles is not compatible with a bulk send list that has only two recipients. For this reason, you might want to test compatibility first.

A successful test result returns `true` for the `canBeSent` property. An unsuccessful test returns a JSON response that contains information about the errors that occurred.

If the test is successful, you can then send the envelope or template by using the [BulkSend::createBulkSendRequest](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendrequest/) method.

## Envelope Compatibility Checks

This section describes the envelope compatibility checks that the system performs.

**Top-Level Issues**

- Envelopes must be in a sendable state.
- The bulk send list must contain at least one copy (instance of an envelope), and no more than the maximum number of copies allowed for the account.
- The envelope must not be null and must be visible to the current user.
- The account cannot have more queued envelopes than the maximum number configured for the account.
- The bulk send list must exist.

**Recipients**

- The envelope must have recipients.
- If you are using an envelope, all of the recipients defined in the bulk send list must have corresponding recipient IDs in the envelope definition. If you are using a template, you must either match the recipient IDs or role IDs.
- The envelope cannot contain a bulk recipient (an artifact of the legacy version of Docusign bulk send
  functionality).

**Recipient Tabs**

- Every `recipient ID, tab label` pair in the bulk send list must correspond to a tab in the envelope.

**Custom Fields**

- Each envelope-level custom field in the bulk send list must correspond to the name of a `customField` in the
  envelope definition. You do not have to match the recipient-level custom fields.

## Request

#### HTTP Request

POST

```
/restapi/v2.1/accounts/{accountId}/bulk_send_lists/{bulkSendListId}/test
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| bulkSendListId \* | string | The GUID of the bulk send list. This property is created after you post a new bulk send list. |

\* Required

## SDK Method

### BulkEnvelopes::createBulkSendTestRequest

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
