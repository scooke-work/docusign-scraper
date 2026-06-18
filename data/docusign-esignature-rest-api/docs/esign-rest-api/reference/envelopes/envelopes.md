---
title: Envelopes Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Envelopes
- Envelopes
- Envelopes
scraped_at: '2026-06-18T21:10:03Z'
---

# Envelopes Resource

The Envelope resource provides methods that allow you to manipulate and monitor envelopes.

Once you have authenticated the user you can use the Envelopes: createEnvelope method to create an envelope. You can call the EnvelopeDocuments: update or EnvelopeDocuments: updateList method to add additional documents.

Setting the `status` property on the envelope to `sent` allows you to send it or `created` to save it as a draft.

You can receive envelope event notifications by setting the `eventNotification` properties. When the envelope or recipient status changes to one of the specified status codes, a notification is sent to a URL that you specify.

If you have an envelope that you have previously saved, you can modify the subject and message, send it, void it, or place it in the purge queue using the Envelope: update method.

In addition to receiving notifications you can monitor the status of the envelopes using the following methods:

- Envelope: getEnvelope - To get the status of a envelope.
- Envelope: listStatus - To get the envelope status for a set of envelopes.
- Envelope: listStatusChanges - To get status changes information for one or more envelopes.

If you need to delete a page from a document in an envelope, use the Envelope: deleteDocumentPage method.

The resource also includes a number of methods that allow you to retrieve and set the initials and signature for certain types of recipients on the document.

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/envelopes ```  Creates an envelope. |
| [deleteDocumentPage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/deletedocumentpage/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages/{pageNumber} ```  Deletes a page from a document in an envelope. |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId} ```  Gets the status of a single envelope. |
| [getNotificationSettings](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getnotificationsettings/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/notification ```  Gets envelope notification information. |
| [getPageImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getpageimage/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages/{pageNumber}/page_image ```  Gets a page image from an envelope for display. |
| [getPageImages](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getpageimages/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages ```  Returns document page images based on input. |
| [getRecipientInitialsImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getrecipientinitialsimage/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/initials_image ```  Gets the initials image for a user. |
| [getRecipientSignature](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getrecipientsignature/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/signature ```  Gets signature information for a signer or sign-in-person recipient. |
| [getRecipientSignatureImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getrecipientsignatureimage/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/signature_image ```  Retrieve signature image information for a signer/sign-in-person recipient. |
| [listAuditEvents](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/listauditevents/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/audit_events ```  Gets the envelope audit events for an envelope. |
| [listStatus](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatus/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/status ```  Gets envelope statuses for a set of envelopes. |
| [listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes ```  Search for specific sets of envelopes by using search filters. |
| [rotateDocumentPage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/rotatedocumentpage/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages/{pageNumber}/page_image ```  Rotates page image from an envelope for display. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId} ```  Send, void, or modify a draft envelope. Purge documents from a completed envelope. |
| [updateNotificationSettings](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/updatenotificationsettings/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/notification ```  Sets envelope notifications for an existing envelope. |
| [updateRecipientInitialsImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/updaterecipientinitialsimage/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/initials_image ```  Sets the initials image for an accountless signer. |
| [updateRecipientSignatureImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/updaterecipientsignatureimage/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/signature_image ```  Sets the signature image for an accountless signer. |

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
