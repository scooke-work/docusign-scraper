---
title: Configure an Agreement Desk Workflow Step
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=map8c30aa94-7e9f-4950-92fc-dd22c6d9f835&topicId=tsk8ded1bbd-661a-412a-adfb-583a052df64c.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-22T19:15:48Z'
---

# Configure an Agreement Desk Workflow Step

Important: This feature is only available to IAM for
Sales customers. Contact [Docusign support](https://support.docusign.com/s/?language=en_US&_gl=1*74elk4*_gcl_au*MTY5ODQyMjA2MC4xNzY5NjM1OTA1LjE5ODM3MTQzNjguMTc2OTYzNjIwNC4xNzY5NjM2MjA0) or [Docusign
sales](https://www.docusign.com/contact-sales) for more information.

Before you begin
:   - Purchase a Docusign Intelligent Agreement
      Management (IAM) plan.
    - Required: Installation of the Salesforce app
      from Docusign App Center. Review the [Installing Extension
      Applications for Workflow Builder](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=bgb1697668738892.html&_LANG=enus) topic for more
      information.
    - Required: [Workflows Create
      permissions](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=gbb1696973048215.html&_LANG=enus) or be an account
      administrator.

Workflow Builder is a workflow builder that you can use to automate agreement actions from
your Docusign account.

Agreement Desk is a centralized workspace designed to simplify and accelerate the
pre-signature phase of the agreement lifecycle. It provides a single location for
all requests related to your agreements.

You can use Agreement Desk steps in Workflow Builder workflows by adding a Create a
Request step.

Use this procedure to configure a Create a Request step:

1. Build a Workflow to Be Triggered By Agreement Desk Requests.
2. Add an Agreement Desk step:
   1. Select + Add a step from the workflow builder
      canvas.

      The Add New Step panel displays.
   2. Agreement Desk: Select Create a
      Request.

      The Create a Request panel displays.
   3. Step Name: Keep or change the name.
3. Select a request type:
   1. Which request type would you like to use?:
      Choose a request type from the dropdown menu.
   2. How would you like to fill out the request
      form?: Select an option:

      - Automatic: Form fields will be
        auto-mapped from the documents within the request.
      - Manual Entry: Form fields will be filled
        out manually.
   3. Select Next.

   The Request title section displays.
4. Request title:
   1. Select the plus + to add variables. You can add
      up to five variables. You can also enter text. The text and variables
      combine to create unique workflow request titles.
   2. Select Next.

   The Documents section displays.
5. Documents:
   1. Choose which documents you would like to include within the
      request:

      - Include all documents
      - Manually select documents to include:
        Select Add Document >  Select Document and choose a document from the dropdown
        menu.
      - Do not include any documents
   2. Select Next.
6. Field mapping: Docusign auto-maps fields from your
   documents. Review the mappings and complete any required fields that are
   missing.
   1. For each variable, enter text manually or choose a variable from the
      dropdown menu.
   2. Select Finish.
7. Select Apply.

You have completed the process. You have configured a Create a Request
step in your workflow. Your workflow can use Agreement Desk requests.
