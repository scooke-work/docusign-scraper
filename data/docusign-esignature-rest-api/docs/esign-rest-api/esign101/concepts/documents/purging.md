---
title: Purging documents
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/purging/
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
- Documents
- Documents
- Purging
scraped_at: '2026-06-18T21:09:58Z'
---

# Purging documents

By default, Docusign stores your envelopes and their documents indefinitely. Your data policies, however, may require you to purge (permanently delete) some of your documents, metadata, and personally identifiable information (PII) from completed envelopes. You can purge documents from any completed, declined, or voided envelope, either by using eSignature Admin in your developer account settings, or programmatically by calling the [Envelopes:update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/) API endpoint (or equivalent SDK method).

When you purge documents, you can choose between three levels of purging:

- **Documents only:** The documents are removed from the system, but all attachments and tabs that were associated with the documents are retained.
- **Documents and metadata:** Documents, attachments, and tabs are removed. Recipient information remains with the envelope.
- **Documents and metadata with recipient address redaction:** If GDPR compliance is enabled for your account, recipient addresses can also be redacted. For example, `accounts@example.com` would be redacted as `redacted_{{envelopeId}}@example.com`.

After you’ve chosen to purge documents from an envelope, they are immediately moved into a purge queue. In general, after 14 days in the queue, the documents (and metadata, if you so choose) in the envelope will be purged from Docusign systems (subject to limited exceptions, including such as during high-volume purge processing). As a default configuration in the sender’s account, senders and recipients with Docusign accounts receive two separate email notifications, generally 14 and seven days before the documents are purged, giving recipients the opportunity to save or download documents prior to such documents being purged.

**Note**: All sent, signed, and voided envelopes that belong to closed accounts that have no active memberships will be automatically purged two years from the date that the account was closed.

## Purge documents using eSignature Admin

To purge documents using the eSignature Admin UI, log in to your Docusign developer account and use the following steps.

1. Select **Admin** from the top nav.
2. In eSignature Admin, select **Document Retention** in the left nav.
3. Select **Targeted Purge**, define a filter to view your envelopes, and then select one or more envelopes that have documents to be purged.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='540' width='1283' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Purging documents from eSignature Admin](https://images.ctfassets.net/aj9z008chlq0/62uOSuE57UYCu8RxgziEZQ/8942026a25e5402c3d39dd101b6fbe03/document_purge.png?w=1283&h=540&q=50&fm=png)
4. When you’ve selected all the envelopes that contain the documents you want to purge, select **Add to purge queue.**
5. In the **Confirm Envelope Purge** dialog box, choose the level of purge to perform.
6. Select **Purge** to send the envelope’s documents to the purge queue. The documents and metadata will thereafter be purged from Docusign systems (subject to applicable purge queue period, as discussed above).

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='393' width='480' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Confirm envelope purge](https://images.ctfassets.net/aj9z008chlq0/5uQ23quiJpoerTCGYzsywz/5e9dff55fec0f6d3e002ff2ad96206d5/confirm_purge.png?w=480&h=393&q=50&fm=png)

## Purge documents using the API

You can also purge documents programmatically using the [Envelopes:update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/) method (or SDK equivalent).

To add an envelope’s documents to the purge queue, make a PUT call to the `/restapi/v2.1/accounts/<accountId>/envelopes/<envelopeId>` endpoint with a request body that specifies the `envelopeId` of the envelope containing the documents and a `purgeState` value that determines which purge level will be used. The possible `purgeState` values are:

- `documents_queued`: Only the documents will be purged.
- `documents_and_metadata_queued`: Documents and metadata will be purged.
- `documents_and_metadata_and_redact_queued`: Documents and metadata will be purged. Email addresses will be redacted.
- `documents_dequeued`: The envelope documents will be removed from the purge queue.

The following example shows the syntax for a sample call to purge documents using this endpoint on the developer environment.

```
PUT https://demo.docusign.net/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}
```

Body:

```
{
  "purgeState": "<your_purge_state_level>"
}
```

## Limitations

- If you choose to purge an envelope’s documents, all documents associated with that envelope will be purged. You cannot choose to purge or preserve individual documents from an envelope.
- Documents that are [authoritative copies](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/authoritative-copies/) cannot be purged.
- The user requesting the purge must have permission to purge documents and must be the sender or acting on behalf of the sender.
- If your account has a document retention policy, envelope documents are automatically placed in the purge queue, and notification emails are sent at the end of the retention period. Setting a document retention policy is the same as setting a schedule for purging documents.

## Next steps

- For example SDK code to purge documents, see [Common API Tasks: Purging envelopes from your Docusign account](https://www.docusign.com/blog/developers/common-api-tasks-purging-envelopes-your-docusign-account).
- For background information about document retention and purging, see [Document Retention and Targeted Envelope Purge](https://support.docusign.com/s/articles/Document-Retention-Envelope-Purge-What-you-should-know-before-using-these-features).
- For additional details about purging documents in eSignature Admin, see [Purging Envelopes](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=kcb1583277378645.html&_LANG=enus&language=en_US&rsc_301).

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
