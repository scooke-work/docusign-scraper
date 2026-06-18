---
title: Specify conditional recipients
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/conditional-recipients/
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
- Recipients
- Conditional Recipients
scraped_at: '2026-06-18T21:09:59Z'
---

# Specify conditional recipients

eSignature REST API 2.1 only
You can customize a signature workflow to have a different set of recipients sign a document only if specific conditions are met. This feature, called *conditional recipients*, is one of a suite of eSignature platform features collectively known as *Advanced Recipient Routing* (ARR).

## Why specify conditional recipients?

By default, signature workflows are predetermined; you define specific recipients who sign documents in a set order determined by the envelope definition. However, some business processes require that different groups of people sign a document depending on different conditions. For these scenarios, the conditional recipients feature enables you to embed conditional logic and control the signature workflow directly within an envelope or template. This helps you avoid having to create multiple templates to handle different signing conditions and manage conditional logic in an integration.

- **Alternate signers:** You can set the entity who signs a document based on a condition. For example, with purchase order approvals, you might specify one signer for amounts up to a given figure, and another signer for amounts above that figure.
- **Adding signers:** You can require additional signatures if a condition is met. With a sales contract, for example, you might specify different discount levels at which additional signers can be required. One example would be that a manager has to sign up to a 20% discount, a VP for a 40% discount, and a CFO for a 60% discount.
- **Choosing signers:** You can conditionally choose among sets of signers. In a university, for instance, a student's application for admission or tuition assistance might go through the dean's office, but then to whichever one of the several dozen academic departments matches the student's major.

Using conditional recipients, each of these scenarios can be handled with a single template.

## How conditional recipients work

The eSignature REST API provides an object named `workflow` that defines a workflow and specifies conditional recipients for an envelope. The `workflow` object can also be used to [pause and unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/pause-unpause-workflow/).The following diagram shows the structure of the `workflow` object:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='713' width='471' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![diagram of the workflow object structure](https://images.ctfassets.net/aj9z008chlq0/3kmQykhnimfOahqHnu0DqT/bdb948e8678ebc0fe1a8809317ffe2da/Conditialrecip_workflow.png?w=471&h=713&q=50&fm=png)

1. The `workflow` object contains `workflowSteps`, an array of objects that define each step in the workflow.
2. Each object in the `workflowSteps` array contains a `recipientRouting` property, which in turn contains a `rules` object.
3. Each rules object contains a `conditionalRecipients` array. Each entry in this array represents a rule that can define a set of recipients and the conditions under which they will be used for your envelope by setting:
   - An array of conditions that define when the conditional recipients will be used, including the step(s) in the workflow where the condition applies
   - An array of recipients that will be used for the envelope if all of the defined conditions are met

See [How to use conditional recipients](https://developers.docusign.com/docs/esign-rest-api/how-to/use-conditional-recipients/) for details on how to use set and use conditional recipients in a workflow.

## Next steps

For details and full example code that demonstrates how to specify conditional recipients, see:

- [How to use conditional recipients](https://developers.docusign.com/docs/esign-rest-api/how-to/use-conditional-recipients/)

For more features of Advanced Recipient Routing, see:

- [Scheduled sending](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/scheduled-sending/)
- [How to schedule an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/schedule-an-envelope/)
- [Delayed routing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/delayed-routing/)
- [How to send an envelope with delayed routing](https://developers.docusign.com/docs/esign-rest-api/how-to/send-envelope-with-delayed-routing/)
- [Pause and unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/pause-unpause-workflow/)
- [How to pause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/pause-workflow/)
- [How to unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/unpause-workflow/)

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
