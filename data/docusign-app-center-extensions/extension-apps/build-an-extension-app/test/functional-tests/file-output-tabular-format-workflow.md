---
title: File output tabular format extension workflow test
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/
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
- File Output Tabular Format Workflow
scraped_at: '2026-06-18T19:51:53Z'
---

# File output tabular format extension workflow test

This procedure explains how to set up and execute a [functional test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) that invokes a [File output tabular format](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-tabular-format/) extension from a [workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html). For this test, you configure and run a workflow that collects user data from a web form and writes the form values to an existing spreadsheet stored in a cloud storage system.

The high-level steps to create and run this test are:

- [Step 1. Identify or create a web form configuration](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#step-1-identify-or-create-a-web-form-configuration)
- [Step 2. Create and publish the workflow](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#step-2-create-and-publish-the-workflow)
- [Step 3. Execute a workflow instance](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#step-3-execute-a-workflow-instance)

This is just one of many possible approaches to setting up a workflow. For additional options, see the [workflow user documentation](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html).

Make sure that you’ve completed all the requirements listed for functional tests in [Test prerequisites](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-prerequisites).

## Step 1. Identify or create a web form configuration

Before you create a workflow, make sure that you have a stand-alone [web form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=brp1660583998599.html) in your account that can be used in a web form step in the workflow. This form collects data in the workflow, which is then exported to a spreadsheet.

## Step 2. Create and publish the workflow

To create a workflow that tests a file output tabular format extension:

1. Log in to the [Workflow Designer](https://apps-d.docusign.com/send/workflows/).
2. Follow the steps in [Create a Basic Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uhm1697826856678.html) to create and save a workflow. When prompted, select the option to start from a blank canvas instead of a template. Your workflow should include:
   - The workflow [start method](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=ztb1727892686033.html): **From within Workflow Builder**.
   - A participant: The participant fills out the web form with values that will be written to a spreadsheet. See [Workflow participant](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#workflow-participant) for configuration guidelines.
   - A web form step: This step displays a web form to collect the participant’s data. See [Web form step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#web-form-step) for configuration guidelines.
   - A step that invokes your extension app: This step writes the values entered in the web form to a spreadsheet. See [File output tabular format extension step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#file-output-tabular-format-extension-step) for configuration guidelines.
   - A confirmation step: This step displays a message confirming that all workflow steps are complete. See [Show a Confirmation Screen step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#show-a-confirmation-screen-step) for configuration guidelines.
3. Complete the steps in [Review and Publish a Workflow](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=iqm1698272226447.html). Then you can [execute instances of the workflow](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#step-3-execute-a-workflow-instance) to test your extension app.

### Workflow participant

Although a workflow can have multiple participants, you only need a single participant for a workflow that invokes a file output tabular format extension. See [Define Workflow Participants](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=ypt1698264964168.html) for details on configuring a participant. The participant role name you enter will be displayed on configuration screens for workflow steps that require selection of a participant.

### Web form step

The first step in your workflow should be a **Collect Data with Web Forms** step. This step collects participant information in a form. See [Configure a Collect Data with Web Forms Step](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=gua1698120920620.html) for more information on how to add this type of step.

When you add this step, configure the settings as follows:

| Setting | Value |
| --- | --- |
| Which form would you like to use? | Select the web form that you created for the workflow test, or an existing web form that you've identified for use with the test.  See [Step 1. Identify or create a web form configuration](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#step-1-identify-or-create-a-web-form-configuration) for more information. |
| Who will participate in this step? | Select the workflow participant that you defined for this test. |
| Map data fields | Optional. This enables you to populate fields in the web form with values from the workflow. For this test, this isn’t necessary. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1274' width='1148' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of a web form step configuration in a Maestro workflow](https://images.ctfassets.net/aj9z008chlq0/4ZcdkSWCCrbqz1qoUAlaXe/308c7b0219be09bf5b42b0502c59fff0/TabularWorkflowTestWebFormStep.png?w=1148&h=1274&q=50&fm=png)

### File output tabular format extension step

This step will invoke your extension app.

To add this step, select the extension thatʼs defined in your extension app registration. The **Add New Step** panel's **Apps** tab displays the values from the [extensions.name](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) and [extensions.description](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) properties in the app manifest.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='734' width='1148' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the menu when adding a file output tabular format step to a workflow](https://images.ctfassets.net/aj9z008chlq0/6fbOH79iVCeTaoKG2icsrp/ee861531547d2c128564043fbba27dd3/TabularWorkflowTestAddStep.png?w=1148&h=734&q=50&fm=png)

**Note:** The step for your extension will not appear on the **Apps** tab if the extension app is not [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to your account.

When you configure this step, the following capabilities will be invoked if they are implemented in the extension app [registration](https://developers.docusign.com/extension-apps/build-an-extension-app/register/):

- [List Drives](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/#list-drives): Enables the step configuration page to retrieve a list of drives (or similar structures that contain files) on the cloud storage system. If the app registration does not include this capability, the UI will not display the drive selection control.
- [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-cloud-storage/#list-directory-contents): Enables the step configuration page to retrieve a list of folders and tabular files from the selected drive (or similar container type) or directory. If the app registration does not include this capability, the UI will not display file selection controls.
- [List Headers](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/#list-headers): Enables the step configuration page to check the column headers in the destination sheet against the selected variables and ensure that there will be no data corruption.

When you [execute an instance](https://docs.google.com/document/d/1FNfkIJqtI6M61AWvYrwuB43g0tiTipaFxWtBFPHXMS8/edit?tab=t.0#heading=h.w84lmgkmqc7o) of the workflow, this step invokes the Export to Destination action defined in the extension app registration.

When you add this step, configure the settings as follows:

| **Setting** | **Value** |
| --- | --- |
| Choose where you'd like the file to be stored | **Select connection**: Select the default connection.  **Select drive:**This setting appears only if the extension app registration includes the **List Drive** capability. Select the destination drive (or similar container type) on the cloud storage system.**Select file**: This setting appears only if the extension app registration includes the **List Directory Contents** capability. Choose the file where the values will be written. |
| What variables should we export? | Select **Add variables** to choose the variables from the workflow that you want to export. The variables will be checked against the number of columns returned from the **List Headers** action to prevent data corruption. If the number of variables selected exceeds the number of columns, the excess variables' values will be written to new columns in the spreadsheet. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1741.9999999999998' width='1150' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the file output tabular format step configuration](https://images.ctfassets.net/aj9z008chlq0/1XiDYO96q7TKEsDeeAFjSb/15619a739cb86dc5ab7a8fd304c5299b/TabularWorkflowTestTabularStep.png?w=1150&h=1742&q=50&fm=png)

### Show a confirmation screen step

The last step in your workflow should be a **Show a Confirmation Screen** step, which displays a message to indicate that the workflow is complete. A procedure for adding this type of step appears in [Configure a Show a Confirmation Screen Step﻿](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=rpc1698682081448.html&_gl=1*12hqdx0*_gcl_au*MTIyNDAzOTI2Mi4xNzUwNjk3MTM1LjEyMzYzMjA5MjMuMTc1NTU0OTQwOS4xNzU1NTQ5NTUz).

When you add this step, configure the settings as follows:

| **Setting** | **Value** |
| --- | --- |
| Participant who will see messages | Select the role name you entered when you configured the [Workflow participant](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/#workflow-participant). |
| Message type | End of participant's tasks |
| Message title | Keep the default value |
| Message body | Keep the default value |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1740' width='1150' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the configuration screen for a confirmation screen step](https://images.ctfassets.net/aj9z008chlq0/2GsjxVDjhYM6oNnlyi7XX7/2e2112791fc498d94c97d6d00209e86d/TabularWorkflowConfirmationStep.png?w=1150&h=1740&q=50&fm=png)

## Step 3. Execute a workflow instance

After you publish your test workflow, you can execute a workflow instance, follow the steps as a customer would, and verify that the correct spreadsheet is successfully updated with the values of the expected variables. You can [monitor the progress](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=vcp1698707326210.html) of the workflow instance as it executes.

To execute a workflow instance:

1. Follow the steps in the **From Within Workflow Builder** section of [How to Start a Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html) to execute a workflow instance.

   The web form is displayed in your browser.
2. Fill out and submit the web form.

   The file output step is executed and the confirmation page is displayed.
3. Check the cloud storage file to which the external service writes data and confirm that the file output step succeeded.

If your extension is not invoked successfully, run the Developer Console [connection and extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) for the extension app to get detailed error messages and troubleshoot.

## Next steps

- Find out more about [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/).
- Review the [File output tabular format extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-tabular-format/).
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
