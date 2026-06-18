---
title: Envelope status codes
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/status-codes/
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
- Status codes
scraped_at: '2026-06-18T20:28:18Z'
---

# Envelope status codes

An envelope’s [status code](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/status-codes/#envelope-status-code-descriptions) indicates where it is in its workflow. This enables you to monitor which envelopes have been completed and which ones are outstanding. In addition, your integration can initiate custom processing based on changes in envelope status.

## Retrieving envelope status

As a best practice for retrieving envelope status, use [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/) and a listener to subscribe to receive updates. When an envelope status changes, Docusign Connect will send your listener a message letting you know and enabling your integration to respond immediately.

You can also retrieve envelope status by making a request to one of these endpoints or a corresponding SDK method:

- [Envelopes:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/): returns the status of a single envelope
- [Envelopes:listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/): returns statuses for all envelopes that match filters you specify

## Envelope status code descriptions

The table below provides descriptions of the envelope status codes.

| Envelope status | Description |
| --- | --- |
| `completed` | The envelope has been completed by all the recipients. |
| `correct` | The envelope has been opened by the sender for correction. The signing process is stopped for envelopes with this status. |
| `created` | The envelope is in a draft state and has not been sent for signing. |
| `declined` | The envelope has been declined for signing by one of the recipients. |
| `deleted` | This is a legacy status and is no longer used. |
| `delivered` | All recipients have viewed the document(s) in an envelope through the Docusign signing website. This does not indicate an email delivery of the documents in an envelope. |
| `sent` | An email notification with a link to the envelope has been sent to at least one recipient. The envelope remains in this state until all recipients have viewed it at a minimum. |
| `signed` | The envelope has been signed by all the recipients. This is a temporary state during processing, after which the envelope is automatically moved to `completed` status. |
| `template` | The envelope is a template. |
| `timedout` | This is a legacy status and is no longer used. |
| `voided` | The envelope has been voided by the sender or has expired. The void reason indicates whether the envelope was manually voided or expired. |

## Next steps

For more information about retrieving envelope status, see:

- [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/)
- [How to get envelope information](https://developers.docusign.com/docs/esign-rest-api/how-to/get-envelope-information/)
- [How to list envelope status changes](https://developers.docusign.com/docs/esign-rest-api/how-to/list-envelope-status-changes/)

For information about errors, see:

- [Error codes](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/) for information about interpreting and handling errors.
- [Troubleshooting for common errors](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/) for detailed information about causes and resolutions for specific errors.

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
