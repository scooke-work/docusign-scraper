---
title: File output cloud storage extension workflow test
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Test
- Test
- Functional Tests
- Functional Tests
- File Output Cloud Storage Workflow
scraped_at: '2026-06-18T19:51:52Z'
---

# File output cloud storage extension workflow test

This procedure explains how to set up and execute a [functional test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) that invokes a [file output cloud storage extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/) from a [workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html). For this test, you configure and run a workflow that displays a document for signature and writes the signed document to a cloud storage system.

The high-level steps to create and run this test are:

- [Step 1. Identify or create an eSignature template](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#step-1-identify-or-create-an-esignature-template)
- [Step 2. Create and publish the workflow](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#step-2-create-and-publish-the-workflow)
- [Step 3. Execute a workflow instance](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#step-3-execute-a-workflow-instance)

This is one of many possible approaches to setting up a workflow. For additional options, see the [workflow user documentation](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html).

Make sure that you’ve completed all the requirements listed for functional tests in [Test prerequisites](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-prerequisites).

## Step 1. Identify or create an eSignature template

Before you create the workflow, make sure that you have an eSignature [template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=dqj1578456412286.html&rsc_301) in your account that you can use in a signing step in the workflow. The document to be signed in that step will be derived from the template. You can [use an existing eSignature template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=epp1578456404448.html) in your account, or [create a new template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html).

When selecting or creating a template:

- For a simpler workflow setup, the template should have a single recipient instead of multiple recipients.
- The recipient type must be **Needs to Sign**.
- Do not hard-code a recipient name or email in the template.
- Make sure that the template document includes, at minimum, a Signature tab.

See [Template Requirements](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=xnw1709852160602.html) for additional information about templates to be used with a workflow signing step.

## Step 2. Create and publish the workflow

To create a workflow that tests a file output cloud storage extension:

1. Log in to the [Workflow Designer](https://apps-d.docusign.com/send/workflows/).
2. Follow the steps in [Create a Basic Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uhm1697826856678.html)﻿ to create and save a workflow. When creating a workflow, select **Blank Workflow**. Your workflow should include:
   - The workflow [start method](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=ztb1727892686033.html) **From within Workflow Builder**.
   - A participant who will sign a document that will be written to cloud storage. See [Workflow participant](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#workflow-participant) for configuration guidelines.
   - A step that defines an eSignature template containing a document to be signed. See [Prepare eSignature Template step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#prepare-esignature-template-step)﻿ for configuration guidelines.
   - A step that displays a document for signature. See [Send Documents for Signature step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#send-documents-for-signature-step) for configuration guidelines.
   - A step that invokes your extension app to write the signed document to cloud storage. See [File output cloud storage extension step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#file-output-cloud-storage-extension-step) for configuration guidelines.
   - A step that displays a message confirming that all workflow steps are complete. See [Show a Confirmation Screen step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#show-a-confirmation-screen-step) for configuration guidelines.

     When youʼve finished configuring the start method, workflow participant, and the steps, the workflow should appear as shown.
3. Complete the steps in [Review and Publish a Workflow](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=iqm1698272226447.html)﻿. Then you can [execute instances of the workflow](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#step-3-execute-a-workflow-instance) to test your extension app.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1598' width='1139' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Workflow steps](https://images.ctfassets.net/aj9z008chlq0/2olW7V56jKIJdtVigFDZ76/2aef40cfbb9b710fe80ae497e8f22507/WorkflowSteps_orig.png?w=1139&h=1598&q=50&fm=png)

### Workflow participant

Although a workflow can have multiple participants, you only need a single participant for a workflow that invokes a file output cloud storage extension. [Define Workflow Participants](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=ypt1698264964168.html) has information about configuring a participant. The participant role name that you enter will be displayed on configuration screens for workflow steps that require selection of a participant.

### Prepare eSignature Template step

The first step in your workflow should be a **Prepare eSignature Template** step . A procedure for adding this type of step appears in [Configure a Prepare eSignature Template step﻿](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=tskd83cc960-fb4b-4534-9573-1041591501e2.html).

When you add this step, configure the settings as follows:

| Setting | Value |
| --- | --- |
| Select a template | Select the eSignature template that you created for the workflow test, or an existing template that you've identified for use with the test.  See [Step 1. Identify or create an eSignature template](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#step-1-identify-or-create-an-esignature-template) for more information. |
| Map template fields to workflow fields | Optional. This enables you to populate fields on the document with values from the workflow, so that you don't have to enter values during the signing process when you execute the test. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='842' width='795' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Prepare eSignature Template step](https://images.ctfassets.net/aj9z008chlq0/3mE9Z1BDga27ANaCkUuiID/32b22ff710a4e8ee1d8cbb9737890c25/PrepareeSignatureTemplate.png?w=795&h=842&q=50&fm=png)

### Send Documents for Signature step

The next step in your workflow should be a **Send Documents for Signature** step, which generates an eSignature envelope for the workflow participant to sign. A procedure for adding this type of step appears in [Configure a Send Documents for Signature Step﻿](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uww1698167288211.html).

When you add this step, configure the settings as follows:

| Setting | Value |
| --- | --- |
| What documents would you like to send? | Select the template associated with the **Prepare eSignature Template** step. |
| Choose direct or remote signing | Select **Use a direct signing session**. |
| Confirm recipient details | The role name associated with the recipient from your eSignature template is displayed here.  Select the participant role name you entered when you configured the [workflow participant](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#workflow-participant)**.** Supply a name and email address for the recipient, either by hard-coding values or selecting workflow variables. With a direct signing session, Docusign does not send an email to the supplied address when executing workflow instances. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1140' width='790' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Get Signatures step](https://images.ctfassets.net/aj9z008chlq0/4OO8xN9VmRazO1V9Y5YiCO/aecacd3772951738451863cda6198ec4/SendDocumentsforSignature.png?w=790&h=1140&q=50&fm=png)

### File output cloud storage extension step

This step will invoke your extension app.

To add this step, display the **Apps** tab on the **Add New Step** panel and select the extension thatʼs defined in your extension app registration. The **Add New Step** panel displays the values from the [extensions.name](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) and [extensions.description](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) properties in the app manifest.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='380' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![File output step selection](https://images.ctfassets.net/aj9z008chlq0/5EKLln7shfVNw96sjt914o/3074ed75366ec7dd32250b2457f6b100/AddStepExtensionApp_small.png?w=600&h=380&q=50&fm=png)

**Note:** The step for your extension will not appear in the **Connected Apps** list if the extension app is not [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to your account.

When you configure this step, these capabilities will be invoked if they are implemented in the extension app [registration](https://developers.docusign.com/extension-apps/build-an-extension-app/register/):

- [List Drives](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#list-drives): Enables the step configuration page to retrieve a list of drives (or similar structures that contain folders and files) on the cloud storage system. If the app registration does not include this capability, the UI will not display the drive selection control.
- [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#list-directory-contents): Enables the step configuration page to retrieve a list of folders from the selected drive (or similar container type) or directory. If the app registration does not include this capability, the UI will not display folder selection controls.

When you [execute an instance](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#step-3-execute-a-workflow-instance) of the workflow, this step invokes the [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#write-file) action defined in the extension app registration.

When you add this step, configure the settings as follows:

| Setting | Value |
| --- | --- |
| What are you storing? | **Files to archive:** Select **Send Documents for Signature.Combined Envelope File**This instructs the workflow to store the signed document from the **Send Documents for Signature** step. |
| Where are you storing it? | **Select connection**: Select the default connection.  **Select drive:** This setting appears only if the extension app registration includes the **List Drives** capability. Select the destination drive (or similar container type) on the cloud storage system.  **Add Folder:** This setting appears only if the extension app registration includes the **List Directory Contents** capability. Select **Add Folder** to display a folder list. After selecting a folder, you can select **Add Subfolder** one or more times to drill down further in the directory structure.  Instead of selecting an existing folder, you can select **New Folder** and then define a naming convention for a folder to be created at workflow instance run time. The naming convention can include hardcoded text, [workflow variables](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#workflow-variables), or a combination of the two. |
| What will you call it? | Define a naming convention for the file. The naming convention can include hardcoded text, [workflow variables](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#workflow-variables), or a combination of the two. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='937' width='830' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![File output cloud storage step](https://images.ctfassets.net/aj9z008chlq0/1uBfjaBOZzEllYpzhacC3U/aacb3dbb35da3b512d8664d0192cccbb/WriteFileStep_orig.png?w=830&h=937&q=50&fm=png)

#### Workflow variables

When defining the naming convention for files to be written or folders to be created on the cloud storage system, you can include workflow variables in the name. Variables will be populated with values at workflow instance run time. This enables you to define a naming convention that results in a unique name for each agreement to be stored.

The types of variables available for selection include:

- **Workflow step variables.** For example, variables associated with the **Send Documents for Signature** step include the unique ID of the eSignature envelope and values from the envelope fields.
- **Workflow participant variables**. These are values associated with the customer who completes the steps in a workflow instance. They include the participant name and email address.
- **Workflow instance variables.** These are values associated with the workflow instance, such as the instance ID and the start date and time.

Docusign recommends testing with both hardcoded file and folders names, as well as file and folder names that include one or more variables, because the external API service must handle both cases. See the [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#write-file) action contract for details.

### Show a Confirmation Screen step

The last step in your workflow should be a **Show a Confirmation Screen** step, which displays a message to indicate that the workflow is complete. A procedure for adding this type of step appears in [Configure a Show a Confirmation Screen Step﻿](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=rpc1698682081448.html).

When you add this step, configure the settings as follows:

| Setting | Value |
| --- | --- |
| Participant | Select the role name you entered when you configured the [workflow participant](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/#workflow-participant). |
| Message type | End of participantʼs tasks |
| Message title | Keep the default value |
| Message body | Keep the default value |

## Step 3. Execute a workflow instance

After you've published your test workflow, you can execute an instance of it, run through the steps as a customer would, and make sure that the file is written to the cloud storage system successfully. You can [monitor the progress](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=vcp1698707326210.html) of the workflow instance as it executes.

To execute a workflow instance:

1. Follow the steps in the **From Within Workflow Builder** section of [How to Start a Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html) to execute a workflow instance.

   The document to be signed is displayed in your browser.
2. Complete the signing process.

   The file output step is executed and the confirmation page is displayed.
3. Check the cloud storage location to which the external service stores files and confirm that the file output step succeeded.

If your extension is not invoked successfully, run the Developer Console [connection and extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) for the extension app to get detailed error messages and troubleshoot.

## Next steps

- Find out more about [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/).
- Review the [File output cloud storage extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/).
- Learn how to run [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/).

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
