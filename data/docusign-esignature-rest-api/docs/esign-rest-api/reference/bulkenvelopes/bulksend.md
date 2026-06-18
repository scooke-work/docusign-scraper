---
title: BulkSend Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Bulkenvelopes
- Bulkenvelopes
- Bulksend
scraped_at: '2026-06-18T21:10:10Z'
---

# BulkSend Resource

You can use bulk send lists send documents to a large number of recipients on a
recurring basis. You can use a bulk send list to send up to 1,000 copies at a time.

After you create a bulk send list, it persists and can be reused and edited any number of times.

You can customize individual copies of the envelope. For example, you can customize the email notification and
language and add personalized notes.

### Requirements and limitations

- Bulk send must be enabled for your account. To enable this feature, contact your Account Manager or Business Development representative.
- You can include up to 1,000 bulk recipients in each request.
- When you send an envelope with bulk recipients, envelopes are added to a bulk recipient queue and sent in a metered fashion.
  An account can have a total of 2,000 total envelopes in the queue at a time.
  If you reach this limit, you will get an error message. Wait and resend the envelope at a later time.
  If you hit queue limits often, contact your Account Manager to see about modifying the queue limits for your account.

### Related topics

- [Bulk sending envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/bulk-send/) concept guide
- [How to bulk send envelopes](https://developers.docusign.com/docs/esign-rest-api/how-to/bulk-send-envelopes/)

## Methods Supported

| Method | Description |
| --- | --- |
| [createBulkSendList](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendlist/) | POST  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_lists ```  Creates a bulk send list. |
| [createBulkSendRequest](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendrequest/) | POST  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_lists/{bulkSendListId}/send ```  Creates a bulk send request. |
| [createBulkSendTestRequest](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendtestrequest/) | POST  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_lists/{bulkSendListId}/test ```  Creates a bulk send test. |
| [deleteBulkSendList](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/deletebulksendlist/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_lists/{bulkSendListId} ```  Deletes a bulk send list. |
| [getBulkSendBatchEnvelopes](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/getbulksendbatchenvelopes/) | GET  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_batch/{bulkSendBatchId}/envelopes ```  Gets envelopes from a specific bulk send batch. |
| [getBulkSendBatches](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/getbulksendbatches/) | GET  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_batch ```  Returns a list of bulk send batch summaries. |
| [getBulkSendBatchStatus](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/getbulksendbatchstatus/) | GET  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_batch/{bulkSendBatchId} ```  Gets the status of a specific bulk send batch. |
| [getBulkSendList](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/getbulksendlist/) | GET  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_lists/{bulkSendListId} ```  Gets a specific bulk send list. |
| [getBulkSendLists](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/getbulksendlists/) | GET  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_lists ```  Gets bulk send lists. |
| [updateBulkSendBatchAction](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/updatebulksendbatchaction/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_batch/{bulkSendBatchId}/{bulkAction} ```  Applies a bulk action to all envelopes from a specified bulk send. |
| [updateBulkSendBatchStatus](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/updatebulksendbatchstatus/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_batch/{bulkSendBatchId} ```  Updates the name of a bulk send batch. |
| [updateBulkSendList](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/updatebulksendlist/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/bulk_send_lists/{bulkSendListId} ```  Updates a bulk send list. |

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
