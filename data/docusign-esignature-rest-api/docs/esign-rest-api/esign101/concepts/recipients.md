---
title: Recipients
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/
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
- Recipients
scraped_at: '2026-06-18T20:28:19Z'
---

# Recipients

A *recipient* object refers to a person who receives a Docusign [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/). Each envelope object must have one or more recipients, and each recipient may have one or more [Tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) (also known as *fields* or *tags*) defined for them. Each recipient is assigned a specific type, which defines their role in the signing process (see [EnvelopeRecipients](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/) for details on each type). Any of these recipients can be a *remote recipient* (who receives the envelope via email), or an *embedded recipient* (who views, approves, or signs the envelope’s documents directly through your app or website).

For examples of how to work with recipients using the API, see how to assign roles to a recipient and [How to request a signature by email](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-remote/).

The following diagram shows the structure of a recipient object, and how it relates to envelopes and documents.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='587' width='759' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Envelope structure graphic](https://images.ctfassets.net/aj9z008chlq0/6IQrFZIZVsWepUbWxtxsh0/83a2cfbd86b1a115588976ed953572ff/EnvelopeFlow.png?w=759&h=587&q=50&fm=png)

## Recipient types

Each recipient of a Docusign envelope is assigned a specific type that defines their responsibilities in the signing process. Each recipient type and the responsibilities associated with that type are described by the following table. The **Name in the UI** column contains the label used for the recipient type in the [eSignature web app](https://apps-d.docusign.com/send/documents/).

| Recipient type | Name in the UI | Description |
| --- | --- | --- |
| [Agents](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#agent-recipient) | Specify Recipients | An agent recipient can add name and email information for recipients that appear after the agent in the routing order. You can use this recipient type to designate an agent or manager to set your recipients when you do not know who the eventual signers will be. |
| [Carbon Copies](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#carbon-copy-recipient) | Receives a Copy | Carbon copy recipients get a copy of the envelope but don't need to sign, initial, date, or add information to any of the documents. This type of recipient can be used in any routing order. Carbon copy recipients receive their copy when the envelope reaches the recipient's order in the process flow and when the envelope is completed. |
| [Certified Deliveries](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#certified-delivery-recipient) | Needs to View | Certified delivery recipients must receive the completed documents for the envelope to be completed. However, they don't need to sign, initial, date, or add information to any of the documents. |
| [Editors](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#editor-recipient) | Allow to Edit | Editors have the same management and access rights for the envelope as the sender. They can make changes to the envelope as if they were using the Correct feature. This recipient can add name and email information, add or change the routing order, and set authentication options for the remaining recipients. Additionally, this recipient can edit signature/initial tabs and text tabs for the remaining recipients. The recipient must have a Docusign account to be an editor. |
| [In Person Signers](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#in-person-signer-recipient) | In Person Signer | An in person signer recipient is a Docusign user who is in the same physical location as the signer. |
| [Intermediaries](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#intermediary-recipient) | Update Recipients | An intermediary is a recipient who can, but is not required to, add name and email information for recipients at the same or subsequent level in the routing order, unless subsequent agents, editors, or intermediaries are added. You can use this recipient type to set up a recipient as a reviewer of your signer's information. They can specify details for role recipients and update information for named recipients. |
| [Notary recipients](https://developers.docusign.com/docs/notary-api/notary101/concepts/notary-recipients/) | Signs with Notary | Notaries are a specialized type of recipient that is new with the Notary API, enabling you to notarize documents remotely by having a notary public act as an in-person (online) witness to the electronic signing. |
| [Seals](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#seal-recipient) | Electronic Seal | Electronic seal recipients represent legal entities rather than individuals. [Electronic seals](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=xcm1643837555908&topicId=isl1578456577247.html&_LANG=enus) can be used by organizations and governments to show evidence of origin and integrity of documents. |
| [Signers](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#signer-recipient) | Needs to Sign | A signer is a recipient who must sign, initial, date, or add data to text tabs on the documents in the envelope. |
| [Witness](https://support.docusign.com/s/articles/DocuSign-eWitness?language=en_US&rsc_301) | Signs with Witness | A [Witness](https://support.docusign.com/s/articles/DocuSign-eWitness?language=en_US&rsc_301) is a recipient who must view and corroborate that a signer has provided their signature. |

For details on recipient objects and types, see [EnvelopeRecipients](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/).

Not all recipients are available to all account types. Review your account plan to determine which recipient types are available to you. All recipient types are available in the [developer environment](https://account-d.docusign.com/).

## Next steps

Read about important recipient features:

- [Recipient authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/)
- [Scheduled sending](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/scheduled-sending/)
- [Delayed routing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/delayed-routing/)
- [Pause and unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/pause-unpause-workflow/)
- [Specify conditional recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/conditional-recipients/)

Working with recipients? Learn how to:

- Retrieve and interpret [recipient status codes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/status-codes/)
- Handle [error codes](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/)
- Assign roles to a recipient and [How to request a signature by email](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-remote/)
- Add [Recipient authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/)
  - [How to require phone authentication for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/phone-auth/)
  - [How to require ID verification (IDV) for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/id-verification/)
  - [How to require knowledge-based authentication (KBA) for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/knowledge-based-authentication/)
  - [How to require access code authentication for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/require-access-code-recipient/)

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
