---
title: Bulk sending envelopes
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/bulk-send/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Envelopes
- Envelopes
- Bulk Send
scraped_at: '2026-06-18T21:09:56Z'
---

# Bulk sending envelopes

You can use bulk sending to send an envelope to a list of recipients, each of whom will receive a copy of the chosen envelope to read or sign. When compared to creating and sending individual envelopes to each recipient, bulk sending saves time by enabling you to use a single call to send out many envelopes to a customized list of recipients.Each bulk send operation is performed in these general steps:

1. **Create envelopes:** Create one or more envelopes to be bulk sent. Envelopes used for bulk send are identical to normal envelopes, but you can set desired values of the following envelope properties programmatically in the bulk send list, rather than when you create the envelope:
   - Recipients
     - All tabs assigned to the recipients
     - Recipient authentication requirements (such as phone, fax, or SMS)
     - Email subject
   - Email description text
   - Envelope custom fields
     > **Note:** Although these properties will typically be set in the bulk send list, you must still add placeholder values for all required envelope fields in this step, including the envelope custom fields.
2. **Create bulk send list:** Use the [POST /v2.1/accounts/{accountId}/bulk\_send\_lists](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendlist/) endpoint (or equivalent `createBulkSendList` SDK method) to create a JSON block that holds information about the recipients, email description, and custom fields for each bulk copy of the envelope to be sent.
3. **Validate envelopes:** Validate the bulk send list, providing the list ID and specifying the ID of the envelope to use in the request body. See [Bulk send list validation](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/bulk-send/#validation) for details on how logical consistency is enforced.
4. Bulk send envelopes: Send the bulk send list by calling the [POST /v2.1/accounts/{accountId}/bulk\_send\_lists/{listId}/send](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendrequest/) API endpoint (or equivalent `createBulkSendRequest` SDK method.

## Bulk send list validation

Each time you create a new bulk send list, the following rules are enforced to perform logical consistency. The list must comply with all of the rules below, or the bulk send will fail.These rules are also enforced when you call the [POST /v2.1/accounts/{accountId}/bulk\_send\_lists/{listId}/test](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendtestrequest/)endpoint endpoint (or the equivalent `createBulkSendTestRequest` SDK method), which should be done before sending the envelope (to determine that it is still valid if it was changed after creation) to make sure that the operation is successful:

- Recipients
  - Recipient IDs within each copy must be unique
  - Recipient IDs must be provided for each recipient
  - Email recipients must have email addresses
  - Fax numbers are required for fax recipients
  - Fax numbers must be valid phone numbers
  - Phone authentication numbers must be valid phone numbers
  - Email addresses must be valid
  - SMS authentication requires valid phone numbers
- Recipient Tabs
  - Tab labels must be unique within each recipient
  - Tab labels are required for each tab
  - Tab values are required for each tab
  - Every recipient ID/tab label pair in the bulk send list must correspond to a tab defined in the envelope
- Custom Fields
  - Envelope Custom Field names must be unique within each copy
  - Envelope Custom Fields must have names
  - Each Envelope Custom Field name in the bulk send list must match a Custom Field name in the envelope

## Bulk sending limits

When bulk sending envelopes, the size of the envelope to be bulk-sent cannot exceed 75 MB.

## Next steps

To see a code example demonstrating how to implement bulk send, see [How to bulk send envelopes](https://developers.docusign.com/docs/esign-rest-api/how-to/bulk-send-envelopes/).

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
