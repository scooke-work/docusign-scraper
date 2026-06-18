---
title: Pause and unpause a signature workflow
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/pause-unpause-workflow/
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
- Pause Unpause Workflow
scraped_at: '2026-06-18T21:09:59Z'
---

# Pause and unpause a signature workflow

eSignature REST API 2.1 only

The Docusign eSignature API lets you customize a signature workflow by pausing and unpausing the signing process. This is one of a suite of eSignature platform features collectively known as *Advanced Recipient Routing* (ARR).

## Why pause and unpause a signature workflow?

Many companies have internal business rules for processes that require signatures. For example, some industries must enforce very prescriptive rules about when certain individuals can sign. Such rules can not only make these processes complex, but also deter businesses from implementing automated signature workflows. The pausing and unpausing features of the eSignature API enable developers to accommodate business rules that affect the timing of signatures in a workflow, thereby making these complex processes amenable to automation.

Among the many use cases for pausing and unpausing a workflow are:

- Scheduling the sending of envelopes to some subset of recipients at a specific time
- Enforcing a wait period before a signer can sign
- Conducting part of a signature workflow outside of Docusign and verifying the external process is complete before continuing the signature workflow
- Using [conditional recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/conditional-recipients/), another feature of advanced recipient routing (which requires pausing and unpausing the workflow)

## How pausing and unpausing works

The eSignature REST API provides an object named `workflow` that contains the properties of an envelope that enable you to pause or unpause it.

When you create an envelope or [template](https://developers.docusign.com/docs/esign-rest-api/how-to/create-template/) using the eSignature REST API, you can include the `workflow` object in the envelope definition's JSON structure to make the envelope's signature workflow pause at the step you designate.

When the envelope is sent, the properties of the `workflow` object will trigger a pause when the condition is met such as, for example, before a second signer is prompted to sign. While the envelope is paused, its envelope cannot be signed, and no notifications are delivered for it. Pausing the signature workflow enables a developer to have their integration carry on actions both outside and inside Docusign to fulfill their business process's requirements before continuing the workflow.

The `workflowStatus` property is used to unpause the envelope and thereby restart a signature workflow. To do so, make another call to the eSignature REST API and set the `workflowStatus` property to `in_progress` in the JSON request body.

See [How to pause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/pause-workflow/) and [How to unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/unpause-workflow/) for detailed walkthroughs of how to pause and unpause your workflows.

## Determine whether an envelope is paused

Connect messages do not include an envelope's `workflowStatus` indicating whether it is paused or not, but your app can call the [EnvelopeWorkflowDefinition:getEnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopeworkflowdefinition/) endpoint (or equivalent SDK method) to manually check. You can also use your recipient statuses to determine whether the envelope should be paused or unpaused.

The following example `EnvelopeWorkflowDefinition:getEnvelopeWorkflowDefinition` response message shows a sample response indicating that your envelope is paused.

```
{
  "workflowStatus": "paused",
  "currentWorkflowStepId": "71d8e564-xxxx-xxxx-xxxx-43c709920db6",
  "workflowSteps": [
    {
      "action": "pause_before",
      "triggerOnItem": "routing_order",
      "itemId": "2",
      "workflowStepId": "71d8e564-xxxx-xxxx-xxxx-43c709920db6",
      "status": "in_progress",
      "triggeredDate": "2022-01-17T18:29:31.3632611Z"
    }
  ]
}
```

**Note:** Do not call the `EnvelopeWorkflowDefinition:getEnvelopeWorkflowDefinition` method to poll for your envelope's pause status more than once per every 15 minutes. Making excess calls to check an envelope's pause status will violate Docusign polling rules and can increase your risk of being locked out for exceeding [API call limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/).

## Next steps

For details and full example code that demonstrates how to pause and unpause a signature workflow, see:

- [How to pause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/pause-workflow/)
- [How to unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/unpause-workflow/)

For more features of Advanced Recipient Routing, see:

- [Scheduled sending](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/scheduled-sending/)
- [How to schedule an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/schedule-an-envelope/)
- [Delayed routing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/delayed-routing/)
- [How to send an envelope with delayed routing](https://developers.docusign.com/docs/esign-rest-api/how-to/send-envelope-with-delayed-routing/)
- [Specify conditional recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/conditional-recipients/)
- [How to use conditional recipients](https://developers.docusign.com/docs/esign-rest-api/how-to/use-conditional-recipients/)

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
