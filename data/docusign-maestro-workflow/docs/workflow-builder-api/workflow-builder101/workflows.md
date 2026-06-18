---
title: Workflows
source_url: https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Workflow Builder API
- Workflow Builder API
- Workflow Builder101
- Workflow Builder101
- Workflows
scraped_at: '2026-06-18T17:59:19Z'
---

# Workflows

A Workflow Builder workflow is an object that represents your end-to-end agreement workflow, including all pre and post-signing [Steps](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/steps/). You can add and order steps as necessary for your workflow and add conditional logic to create branches within that workflow. 

Workflows are made up of a sequence of [step](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/steps/) objects. Each step object contains the information and logic necessary for a single operation within your workflow, such as:

- Getting participant data via web forms to populate variables used by subsequent steps
- Requesting a signature
- Saving information to a database or archiving it to the cloud

See [Steps](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/steps/) for details.

When you’ve finished creating your workflow, you can [publish](https://developers.docusign.com/docs/workflow-builder-api/publishing-go-live/) it to make it available for other users in your account to view and run, as well as making it usable by your apps in the production environment. See [Publishing and Go-Live](https://developers.docusign.com/docs/workflow-builder-api/publishing-go-live/) for details.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1453' width='828' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Screenshot of an example workflow](https://images.ctfassets.net/aj9z008chlq0/4i8Ta6MXTaD4YeDjVzUAiY/c974cb37f35bfe9a90ad667348ee574f/WorkflowAllShort.png?w=828&h=1453&q=50&fm=png)

## Running workflows

You can configure how your workflow is triggered by setting a start method. Each Start method surfaces shortcuts such as a link button that helps you configure and use your workflow more easily, or prompts you to define variables that must be populated before the workflow can be started via API. The start method that you select determines how a workflow can be triggered. Each method corresponds to a specific HTTP trigger type. For example, workflows configured to start **From an API** **call** use the `POST` method and can only be triggered through the Workflow Builder API. Workflows set to start **From a link** use the `GET` method and can only be started when someone opens the published trigger URL in a browser. Because of these differences, changing a workflow’s start method affects which trigger methods will continue to work.

The following start methods are currently supported in Workflow Builder:

| **Start method** | **Trigger type** | **Description** |
| --- | --- | --- |
| **From a link** | `GET` | Starts a workflow when a user clicks a browser link. |
| **From within Workflow Builder** | `POST` | Initiated manually from within the Workflow Builder application. |
| **From an event** | `GET` | Triggered automatically by a system or event. |
| **From a CLM workflow** | `POST` | Initiated from a CLM workflow. |
| **From an API call** | `POST` | Supports both **Human** and **Automated Process** triggers. Required for API-triggered workflows. |

**Note:** Only workflows configured with the **From an API call** start method can be triggered using the `POST` endpoint. Attempting to start a workflow with any other method will return an error.

You can trigger and run a workflow from the Workflow Builder workflow designer UI or by opening a trigger URL:

- **Using the trigger URL as a link:** The trigger URL leads to an unauthenticated endpoint that can be used by non-developers. You can open the published workflow’s unique trigger URL in your browser, embed it in a website, or provide it to your participants to enable them to run the workflow themselves.

  When this URL is accessed, a new instance of the workflow will be executed. You can get the URL:
  - In the [Workflow Designer](https://apps-d.docusign.com/send/workflows/) by finding the row with the workflow you want to run that is configured to be started via link, then selecting the link icon to copy the URL. You can then embed the link in a page or email that you share with a user. This is typically used by self-service workflows, allowing participants to initiate workflows whenever they need to.
  - By making a POST call to the [Workflows: triggerWorkflow](https://developers.docusign.com/docs/workflow-builder-api/reference/workflowbuilder/workflows/triggerworkflow/) Workflow Builder API endpoint. The trigger URL value will be returned in the call response.  See [How to trigger a Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/) for a full walkthrough.

Or from within Docusign:

- **Using the Workflow Builder UI** by a user within your organization by selecting the **Run Workflow** button next to the listed workflow. This enables the person who starts the workflow to specify the identities of the workflow participants, such as their names and emails before inviting them. This option is designed to be triggered from within Docusign, rather than externally
- **Using a CLM workflow**. This option lets you trigger your Workflow Builder workflow from within a CLM workflow, enabling you to use CLM options such as WhatsApp delivery or SMS delivery alongside Workflow Builder in a single automated process. This option is designed to be triggered from within Docusign, rather than externally.

See [Workflow start methods](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=ztb1727892686033.html) for details on each option.

After a workflow is triggered, a new *instance* of that workflow will be created. A workflow instance is created for a specific set of participants and holds the data for their agreement process. You can monitor the progress of any instances of a particular workflow using [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/). See [Monitor a workflow](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/monitor-workflow/) for details.

The following example workflow definition shows the structure of a basic rental agreement workflow. It includes steps to collect information using web forms, send a notification, request a signature, and show confirmation screens.

## Next steps

- [Workflow versioning and drafts](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/versioning/)
- [Steps](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/steps/)
- [Branching rules](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/branching-rules/)
- [Monitor a workflow](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/monitor-workflow/)
- [Workflow start methods](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=ztb1727892686033.html)

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
