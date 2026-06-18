---
title: ': create'
source_url: https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/create/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:10:48Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/create/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/create/?explorer=true)

[Envelopes](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/)

# : create

Creates and sends an envelope or creates a draft envelope.
Envelopes are fundamental resources in the DocuSign platform.

With this method you can:

- Create and send an envelope
  with [documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), [recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/), and [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/).
- Create and send an envelope from a template.
- Create and send an envelope from
  a combination of documents and templates.
- Create a draft envelope.

When you use this method
to create and send an envelope
in a single request,
the following parameters in the request body (an [`envelopeDefinition`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/envelopes/envelopes/create/#definition__envelopedefinition)) are required:

| Parameter | Description |
| --- | --- |
| `status` | Set to `sent` to send the envelope to recipients. Set to `created` (or don't set at all) to save the envelope as a draft. |
| `emailSubject` | The subject of the email used to send the envelope. |
| `documents` | The [documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) to be signed. |
| `recipients` | The email addresses of the envelope [recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/). |

There are many ways to use envelopes.
You can create and send an envelope
with a single API request,
or you can use several API requests
to create, populate, and send envelopes.

| See | To learn about |
| --- | --- |
| [Envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) | Envelopes, [adding documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/), [tracking](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/), [locking](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/), [deleting](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/), [templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) |
| [Documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) | Documents, [attachments](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), [supplemental documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), [authoritative copies](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), [purging](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) |
| [Recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/) | Recipients, [recipient types](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/), [recipient status](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/) |
| [Tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) | Tabs, [tab types](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/), [anchoring tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/auto-place/), [auto-populating tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/), [custom tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/custom-tabs/), [payments](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/payment/) |

**Note**: When you create an envelope by using a [composite template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/composite/), you should specify the envelope custom fields in the inline template. Any custom fields that you specify at the root level are ignored.

## Request

#### HTTP Request

POST

```
/restapi/v2/accounts/{accountId}/envelopes
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account id GUID. |

| Query Parameters |  |  |
| --- | --- | --- |
| cdse\_mode | string | Reserved for DocuSign. |
| change\_routing\_order | string | When true, users can define the routing order of recipients while sending documents for signature. |
| completed\_documents\_only | string | Reserved for DocuSign. |
| merge\_roles\_on\_draft | string | When set to **true**, template roles will be merged, and empty recipients will be removed. This parameter applies when you create a draft envelope with multiple templates. (To create a draft envelope, the `status` field is set to `created`.) Note: DocuSign recommends that this parameter should be set to **true** whenever you create a draft envelope with multiple templates. |
| tab\_label\_exact\_matches | string | Reserved for DocuSign. |

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
