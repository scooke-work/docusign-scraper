---
title: Embed a workflow in your web application
source_url: https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/embed-workflow/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Workflow Builder API
- Workflow Builder API
- Workflow Builder101
- Workflow Builder101
- Embed Workflow
scraped_at: '2026-06-18T17:59:18Z'
---

# Embed a workflow in your web application

When your Workflow Builder API integration starts a workflow instance by making a [Workflows: triggerWorkflow](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/triggerworkflow/) request, the response includes an `instance_url`. This is the URL of the web page where a user completes the workflow steps. Your integration has two options for displaying the `instance_url`:

- **Redirect the user's browser to the workflow instance URL:** The user is routed from your web application to the Docusign platform. When the user completes the workflow, they remain at the Docusign platform instead of returning to your web application.

  For sample code that demonstrates this option, see [How to trigger a Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/) and the [Workflows Sample App](https://workflows.sampleapps.docusign.com/).
- **Embed the workflow instance URL in an iframe:** The workflow is displayed within your web application, and your web application's user interface is visible as users complete the workflow. This contributes to a more seamless user experience. When a user finishes the workflow, their browser window still displays your web application, which can route the user to other pages in your application as needed.

## Embedded workflow instance recommendations and restrictions

### Workflow start methods

For Workflow Builder API integrations that embed workflow instances, the supported [workflow start methods](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=ztb1727892686033.html) are **From a Link** and **From an API call**.

### Workflow starting variable values

If your integration's [Workflows: triggerWorkflow](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/triggerworkflow/) request will include [starting variable](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/variables/) values passed in the `trigger_inputs` object, Docusign recommends that the workflow start method be set to **From an API cal**l instead of **From a Link**. For sample code that includes starting variable values, see [How to trigger a Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/).

### Workflow step types

These restrictions related to [workflow step types](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=afu1730332596907.html) apply to embedded workflow instances:

- All workflow step types are supported with integrations that embed workflow instances, except for **Collect Data from an ID**.
- For **Verify Someone's Identity** steps, only the **Phone Authentication** verification method is supported with embedded workflow instances.
- If a workflow does not include any steps that users complete in a UI, Docusign does not recommend embedding workflow instances in your web application. An example of a workflow with no UI steps is one that only sends an email to users.
- For workflows that include a **Send Documents for Signature** step, [focused view](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embedded-signing/#focused-view) display of the agreement to be signed is not supported.

## Embed a workflow instance URL

To embed the `instance_url` returned in a [Workflows: triggerWorkflow](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/triggerworkflow/) response, include the URL in an iframe, for example:

```
<div className={styles.formContainer}>
  <iframe src={triggerUrl} width="800" height="600">
  </iframe>
</div>
```

## Next steps

- See the [API reference](https://developers.docusign.com/docs/workflow-builder-api/reference/) for details about Workflow Builder API endpoints.
- Learn more about [workflow steps](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/steps/).
- Review the options to [monitor workflow instances](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/monitor-workflow/) that your integration has triggered.

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
