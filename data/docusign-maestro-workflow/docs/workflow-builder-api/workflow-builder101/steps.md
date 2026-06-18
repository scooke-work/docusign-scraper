---
title: Steps
source_url: https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/steps/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Workflow Builder API
- Workflow Builder API
- Workflow Builder101
- Workflow Builder101
- Steps
scraped_at: '2026-06-18T17:59:19Z'
---

# Steps

Steps are the individual tasks executed in [Workflows](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/). Steps invoke functionality from Docusign modules such as eSignature and web forms or [Extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/) to call third-party platforms that an admin has authorized for your account, such as archiving a file to a cloud storage site or verifying bank account data.

The available step types depend on the applications and extensions authorized for your account. For beta, the following step types are supported:

- **Collect Data with Web Forms**. Used to collect data from your workflow participants and save that data to [Variables](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/variables/). You can then use the values of these variables to prefill document fields, help verify identity, and populate other data points.
- **Set Up Invite**. Used to send email workflow invitations to your participants.
- **Verify Someone's Identity.** Used to validate that a participant is who they claim to be. All Identity Verification options configured by your account administrator are supported as options for this step.
- **Collect Data from an ID**. Used to verify a participant’s ID and extract fields from it, such as the participant name or verification provider, that will be used in future workflow steps.
- **Send Documents for Signature**. Used to present documents from one of your account’s templates to your participants for signature. You can prefill the template document fields with data gathered in any previous step, such as a web form or identity verification.

  You can set the first signer to use either direct ([embedded](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/)) or remote signing. All subsequent signers must use email notifications to access their signing sessions.
- **Add a Branching Rule**. Branching rules enable you to split your workflow into one of two different paths, depending on the result of an if/else step.
- **Show a Confirmation Screen**. Used to display messages (preset or customized) to specific workflow participants. Typically used to notify participants that their tasks in the workflow are complete.
- **Set up Invite**. Used to invite new participants to your workflow.
- **Send an Email**. Used to automate sending email, typically to notify someone about the status of the workflow or agreement.
- **Extension steps**. Any extensions from your account’s installed extension apps may be configured as steps in your workflow. For example, you might use an extension to verify a participant's bank account information, write data to your CRM, or archive files to cloud storage using extensions. See [Extension apps overview](https://developers.docusign.com/extension-apps/) for more information.

## Next steps

- [Participants](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/participants/)
- [Branching rules](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/branching-rules/)
- [Workflows](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/)
- [Variables](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/variables/)
- [Install extension apps for Workflow Builder](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=bgb1697668738892.html)

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
