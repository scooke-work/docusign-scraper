---
title: Create a Workflow from an eSignature Template
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=tsk3aff5ded-8b1a-47e2-89a4-a6bca6c990be.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T18:04:35Z'
---

# Create a Workflow from an eSignature Template

Learn how to generate a fully configured workflow directly from an existing eSignature template to quickly automate your signing process.

This topic explains how to create Workflow Builder workflows directly from your existing eSignature templates. This feature helps you easily turn simple document signing into automated, complex workflows.

As a process builder, you can start a workflow from various eSignature locations: from the main action menus of the Templates, Home, and Agreements pages, or from the Workflow Builder Workflows view. For more information on required permissions to complete this task, see [Workflow Builder Roles and Permission Requirements](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=gbb1696973048215.html&_LANG=enus "Read about the different roles involved with creating and using workflows with Docusign Workflow Builder. Each role requires specific user permissions.").

When you create a workflow from an eSignature template, the system automatically configures key elements of your new workflow. You can use any eSignature template that meets the Workflow Builder template requirements. To review these requirements, see the help topic [Template Requirements](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=xnw1709852160602.html&_LANG=enus "Important information for process builders to consider before starting to develop workflows that include a Prepare eSignature Template step. When you prepare a template to use in a Send Documents for Signature step, there are several requirements and limitations that must be respected to configure the step successfully."). The workflow you create will have the following structure:

- The workflow's start method will be set to Manually in Docusign.
- Recipients from the eSignature template are automatically added to the workflow's list of participants.
- The workflow will include three main process steps: a Collect Data with Web Forms, Prepare eSignature Template, and Send Documents for Signature.
- A web form is automatically created to collect recipient information for the Prepare and Send steps.

1. In your Docusign account do one of the following:
   1. From the Templates page, locate the template you want to use, select the more actions menu, and choose Add Automation with Workflow Builder .
   2. From the Home page, select Start >  Workflows  > Create New Workflow > Start with eSignature template. Select the template you want to use and follow the prompts.
   3. From the Workflows view on the Agreements page, select Create Workflow > Start with eSignature template. Select the template you want to use and follow the prompts.

   The Preparing your workflow... message displays while your new workflow is created.
2. You can now publish the workflow as is, or continue to add more workflow steps to meet your process needs as described in the article [Create a Basic Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uhm1697826856678.html&_LANG=enus "Learn the basics of how to create an agreement workflow. Process creators and account administrators can create workflows to automate the agreement process.").

   ![Screenshot of a workflow created from a template.](https://docusign-be-prod.zoominsoftware.io/api/bundle/yff1696971835267/page/images/wf-from-template.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE4MDU2OTQsInNoZWFmIjoieWZmMTY5Njk3MTgzNTI2NyJ9.4tdkLeqjMHOweJWK31AK7BvSJltdF7ogAfE4aUH9-mQ&_LANG=enus "Screenshot of a workflow created from a template.")
