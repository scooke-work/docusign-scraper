---
title: EnvelopeWorkflowDefinition Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/
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
- Envelopeworkflowdefinition
scraped_at: '2026-06-18T21:10:23Z'
---

# EnvelopeWorkflowDefinition Resource

Describes the workflow for an envelope or template. These methods enable you to use the [scheduled sending](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/scheduled-sending/) and [delayed routing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/delayed-routing/) features.

### Related topics

- [How to schedule an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/schedule-an-envelope/)
- [How to send an envelope with delayed routing](https://developers.docusign.com/docs/esign-rest-api/how-to/send-envelope-with-delayed-routing/)

## Methods Supported

| Method | Description |
| --- | --- |
| [createEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/createenvelopeworkflowstepdefinition/) | POST  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/steps ```  Adds a new step to an envelope's workflow. |
| [createTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/createtemplateworkflowstepdefinition/) | POST  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/steps ```  Adds a new step to a template's workflow. |
| [deleteEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopedelayedroutingdefinition/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/steps/{workflowStepId}/delayedRouting ```  Deletes the delayed routing rules for the specified envelope workflow step. |
| [deleteEnvelopeScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopescheduledsendingdefinition/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/scheduledSending ```  Deletes the scheduled sending rules for the envelope's workflow. |
| [deleteEnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopeworkflowdefinition/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow ```  Delete the workflow definition for an envelope. |
| [deleteEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopeworkflowstepdefinition/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/steps/{workflowStepId} ```  Deletes a workflow step from an envelope's workflow definition. |
| [deleteTemplateDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplatedelayedroutingdefinition/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/steps/{workflowStepId}/delayedRouting ```  Deletes the delayed routing rules for the specified template workflow step. |
| [deleteTemplateScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplatescheduledsendingdefinition/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/scheduledSending ```  Deletes the scheduled sending rules for the template's workflow. |
| [deleteTemplateWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplateworkflowdefinition/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow ```  Delete the workflow definition for a template. |
| [deleteTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplateworkflowstepdefinition/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/steps/{workflowStepId} ```  Deletes a workflow step from an template's workflow definition. |
| [getEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopedelayedroutingdefinition/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/steps/{workflowStepId}/delayedRouting ```  Returns the delayed routing rules for an envelope's workflow step definition. |
| [getEnvelopeScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopescheduledsendingdefinition/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/scheduledSending ```  Returns the scheduled sending rules for an envelope's workflow definition. |
| [getEnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopeworkflowdefinition/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow ```  Returns the workflow definition for an envelope. |
| [getEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopeworkflowstepdefinition/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/steps/{workflowStepId} ```  Returns a specified workflow step for a specified template. |
| [getTemplateDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/gettemplatedelayedroutingdefinition/) | GET  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/steps/{workflowStepId}/delayedRouting ```  Returns the delayed routing rules for a template's workflow step definition. |
| [getTemplateScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/gettemplatescheduledsendingdefinition/) | GET  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/scheduledSending ```  Returns the scheduled sending rules for a template's workflow definition. |
| [getTemplateWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/gettemplateworkflowdefinition/) | GET  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow ```  Returns the workflow definition for a template. |
| [getTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/gettemplateworkflowstepdefinition/) | GET  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/steps/{workflowStepId} ```  Returns a specified workflow step for a specified envelope. |
| [updateEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopedelayedroutingdefinition/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/steps/{workflowStepId}/delayedRouting ```  Updates the delayed routing rules for an envelope's workflow step definition. |
| [updateEnvelopeScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopescheduledsendingdefinition/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/scheduledSending ```  Updates the scheduled sending rules for an envelope's workflow. |
| [updateEnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopeworkflowdefinition/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow ```  Updates the workflow definition for an envelope. |
| [updateEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopeworkflowstepdefinition/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/workflow/steps/{workflowStepId} ```  Updates the specified workflow step for an envelope. |
| [updateTemplateDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updatetemplatedelayedroutingdefinition/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/steps/{workflowStepId}/delayedRouting ```  Updates the delayed routing rules for a template's workflow step. |
| [updateTemplateScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updatetemplatescheduledsendingdefinition/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/scheduledSending ```  Updates the scheduled sending rules for a template's workflow definition. |
| [updateTemplateWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updatetemplateworkflowdefinition/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow ```  Updates the workflow definition for a template. |
| [updateTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updatetemplateworkflowstepdefinition/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/workflow/steps/{workflowStepId} ```  Updates a specified workflow step for a template. |

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
