---
title: ': create'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:20Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/?explorer=true)

[Envelopes](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/)

# : create

Creates and sends an envelope or creates a draft envelope.
Envelopes are fundamental resources in the Docusign platform.

With this method you can:

- Create and send an envelope
  with [documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), [recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/), and [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/).
- [Create and send an envelope from a template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/).
- [Create and send an envelope from
  a combination of documents and templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/composite/).
- Create a draft envelope.

When you use this method
to create and send an envelope
in a single request,
the following parameters in the request body (an [`envelopeDefinition`](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/#schema__envelopedefinition) object) are required:

| Parameter | Description |
| --- | --- |
| `status` | Set to `sent` to send the envelope to recipients. Set to `created` (or don't set at all) to save the envelope as a draft. |
| `emailSubject` | The subject of the email used to send the envelope. |
| `documents` | The [documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) to be signed. |
| `recipients` | The email addresses of the envelope [recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/). |

When you create an envelope by using a
[composite template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/composite/),
you should specify the envelope custom fields in the inline template.
Any custom fields that you specify at the root level are ignored.

If the envelope has a workflow definition
and the `workflowStatus` is `paused`,
the envelope will not be sent immediately,
even if the envelope's `status` is `sent`.

### Related topics

[Envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) and [template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/)
objects along with [documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/),
[recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/), and [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/)
are the five object models at the core of the eSignature API.
The [eSignature concepts guide](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/)
describes how the five object models work together.

The following how-to articles contain
practical examples that show you how to
to
configure this method's
[`envelopeDefinition`](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/#schema__envelopedefinition) request body
to perform common tasks.

Requesting a signature

- [How to request a signature by email](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-remote/)
- [How to request a signature through your app](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded/)
- [How to request a signature by email using a template](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-template-remote/)
- [How to request a signature using a composite template](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-composite-template-embedded/)
- [How to request a signature by SMS or WhatsApp delivery](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-sms-whatsapp/)
- [How to send a request for payment](https://developers.docusign.com/docs/esign-rest-api/how-to/request-a-payment/)
- [How to send an envelope to an In Person Signer](https://developers.docusign.com/docs/esign-rest-api/how-to/send-envelope-to-in-person-signer/)
- [How to request a signature by email using CORS](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-browser-cors/)
- [How to request a signature through your CORS-enabled browser app](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-cors-app-embedded/)
- [How to request a signature through your app (embedded signing) with a CFR Part 11 account](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded-cfrpart11/)

Working with envelopes and templates

- [How to get envelope information](https://developers.docusign.com/docs/esign-rest-api/how-to/get-envelope-information/)
- [How to list envelope recipients](https://developers.docusign.com/docs/esign-rest-api/how-to/get-envelope-recipients/)
- [How to list envelope status changes](https://developers.docusign.com/docs/esign-rest-api/how-to/list-envelope-status-changes/)
- [How to create a template](https://developers.docusign.com/docs/esign-rest-api/how-to/create-template/)
- [How to send an envelope via your app](https://developers.docusign.com/docs/esign-rest-api/how-to/embedded-sending/)
- [How to bulk send envelopes](https://developers.docusign.com/docs/esign-rest-api/how-to/bulk-send-envelopes/)

Working with advanced recipient routing

- [How to pause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/pause-workflow/)
- [How to unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/unpause-workflow/)
- [How to use conditional recipients](https://developers.docusign.com/docs/esign-rest-api/how-to/use-conditional-recipients/)
- [How to schedule an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/schedule-an-envelope/)
- [How to send an envelope with delayed routing](https://developers.docusign.com/docs/esign-rest-api/how-to/send-envelope-with-delayed-routing/)

Working with documents

- [How to list envelope documents](https://developers.docusign.com/docs/esign-rest-api/how-to/list-envelope-documents/)
- [How to download envelope documents](https://developers.docusign.com/docs/esign-rest-api/how-to/download-envelope-documents/)
- [How to attach documents via binary transfer](https://developers.docusign.com/docs/esign-rest-api/how-to/send-binary/)
- [How to create a signable HTML document](https://developers.docusign.com/docs/esign-rest-api/how-to/creating-signable-html/)
- [How to convert a PDF file into a signable HTML document](https://developers.docusign.com/docs/esign-rest-api/how-to/converting-pdf/)
- [How to set document visibility for envelope recipients](https://developers.docusign.com/docs/esign-rest-api/how-to/set-document-visibility/)
- [How to request a signature by email with document generation](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-document-generation/)

Working with tabs

- [How to get envelope tab values](https://developers.docusign.com/docs/esign-rest-api/how-to/get-envelope-tab-values/)
- [How to get envelope custom tab values](https://developers.docusign.com/docs/esign-rest-api/how-to/get-envelope-custom-tab-values/)
- [How to set envelope tab values](https://developers.docusign.com/docs/esign-rest-api/how-to/set-envelope-tab-values/)
- [How to set tab values in a template](https://developers.docusign.com/docs/esign-rest-api/how-to/set-template-tab-values/)

Working with brands

- [How to create a brand](https://developers.docusign.com/docs/esign-rest-api/how-to/create-brand/)
- [How to apply a brand to an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/apply-brand-to-envelope/)
- [How to apply a brand and template to an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/apply-brand-and-template-to-envelope/)

Working with permissions

- [How to create a permission profile](https://developers.docusign.com/docs/esign-rest-api/how-to/permission-profile-creating/)
- [How to update individual permission settings](https://developers.docusign.com/docs/esign-rest-api/how-to/permission-profile-updating/)
- [How to set a permission profile](https://developers.docusign.com/docs/esign-rest-api/how-to/permission-profile-setting/)
- [How to delete a permission profile](https://developers.docusign.com/docs/esign-rest-api/how-to/permission-profile-deleting/)

Implementing multi-factor recipient (signer) authentication

- [How to require ID verification (IDV) for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/id-verification/)
- [How to require knowledge-based authentication (KBA) for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/knowledge-based-authentication/)
- [How to require phone authentication for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/phone-auth/)
- [How to require access code authentication for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/require-access-code-recipient/)

API service limits

- [eSignature API rules and resource limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/)

## Request

#### HTTP Request

POST

```
/restapi/v2.1/accounts/{accountId}/envelopes
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |

| Query Parameters |  |  |
| --- | --- | --- |
| cdse\_mode | string | Reserved for Docusign. |
| change\_routing\_order | string | When true, users can define the routing order of recipients while sending documents for signature. |
| completed\_documents\_only | string | Reserved for Docusign. |
| merge\_roles\_on\_draft | string | When **true,** template roles will be merged, and empty recipients will be removed. This parameter applies when you create a draft envelope with multiple templates. (To create a draft envelope, the `status` field is set to `created`.)  **Note:** Docusign recommends that this parameter should be set to **true** whenever you create a draft envelope with multiple templates. |

\* Required

## SDK Method

### Envelopes::createEnvelope

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
