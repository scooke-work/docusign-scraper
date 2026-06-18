---
title: Data IO extension workflow test
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/
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
- Data IO workflow
scraped_at: '2026-06-18T19:51:52Z'
---

# Data IO extension workflow test

These procedures explain how to set up and execute a [functional test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) that invokes a data IO extension from a [Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/). For this test, you run a workflow that reads data from your external system, populates [web form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=brp1660583998599.html) fields with the retrieved values, and writes values from the web form to the external system.

**Note:** You can configure a data IO extension so that it reads from an external system, but does not write to it. See [Data IO extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/) for details. When setting up a workflow, you can omit the data read step or data write step if you only want to test one of these operations.

The high-level steps to create and run this test are:

- [Step 1. Identify or create a web form](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#step-1-identify-or-create-a-web-form)
- [Step 2. Create and publish the workflow](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#step-2-create-and-publish-the-workflow)
- [Step 3. Execute a workflow instance](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#step-3-execute-a-workflow-instance)

This is one of many possible approaches to setting up a workflow. For additional options, see the [workflow user documentation](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html).

Make sure that you’ve completed all the requirements listed for functional tests in [Test prerequisites](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-prerequisites).

**Walkthrough playlist:** You can also see a video overview of the data IO extension workflow test using the [Data IO Reference Implementation](https://github.com/docusign/extension-app-data-io-reference-implementation) below:

## Step 1. Identify or create a web form

Before you create the workflow, make sure that your developer account has a web form that you can use in a data collection step in the workflow. You can [use an existing web form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=tpj1664990031635.html) in your account, or [create a new web form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=euk1665093155272.html).

When selecting or creating a web form:

- The web form must be standalone. Web forms that are derived from eSignature templates cannot be used in workflows. [Web Form Requirements and Data-Mapping Information﻿](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=oha1716325069710.html) explains how to create a standalone web form.
- The web form should contain fields that correspond to fields in your external system. This enables you to test your extension by populating web form fields with values retrieved from the external system and/or writing web form field values to the external system.
- Each web form field has a **Field name** property, which appears on the [Properties panel](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=wor1676501633875.html) in the Web Forms builder. Field names are also listed on Workflow Builder screens that map web form fields to external system fields. Make note of the field names in the Web Forms builder so that you can easily identify web form fields when configuring workflow steps in Workflow Builder.

## Step 2. Create and publish the workflow

To create a workflow that tests a data IO extension:

1. Log in to the [Workflow Designer](https://apps-d.docusign.com/send/workflows/).
2. Follow the steps in [Create a Basic Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uhm1697826856678.html)﻿ to create and save a workflow. When creating a workflow, select **Blank Workflow**. Your workflow should include:
   - The workflow start method **From within Maestro**.
   - A participant who fills out the web form. See [Workflow participant](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#workflow-participant) for configuration guidelines.
   - Optional: A step that invokes your extension to read external system data so that the values can be populated in the web form. See [Data read step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#data-read-step) for configuration guidelines. If you want to test writing data but not reading data, omit this step.
   - A step that displays a web form. See [Collect Data with Web Forms step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#collect-data-with-web-forms-step) for configuration guidelines.
   - Optional: A step that invokes your extension to write data collected in the web form to the external system. See [Data write step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#data-write-step) for configuration guidelines. If you want to test reading data but not writing data, omit this step.
   - A step that displays a message confirming that all workflow steps are complete. See [Show a Confirmation Screen step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#show-a-confirmation-screen-step) for configuration guidelines.

     When you’ve finished configuring the start method, the workflow participant, and the steps for a test of both reading and writing data, the workflow should appear as shown. If you want to test reading data only or writing data only, do not include the unneeded step in the workflow.
3. Complete the steps in [Review and Publish a Workflow](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=iqm1698272226447.html)﻿. Then you can [execute instances of the workflow](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#step-3-execute-a-workflow-instance) to test your extension app.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='930' width='475' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Workflow steps data IO](https://images.ctfassets.net/aj9z008chlq0/1CLIYzknrVVJnmpBtQYe4L/f4f373dbd9df51234068c1bdd4f651cb/WorkflowSteps.png?w=475&h=930&q=50&fm=png)

### Workflow participant

Although a workflow can have multiple participants, you only need one for a workflow that invokes a data IO extension. [Create a Basic Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uhm1697826856678.html) has information about configuring a participant. The participant role name that you enter will be displayed on configuration screens for workflow steps that require selection of a participant.

### Data read step

**Note:** If you do not want to test reading data from an external data source, omit this step from the workflow.

This step will invoke your data IO extension to search for records in the external system and read values from them. This step tests the [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records) action.

When you add this step, you select the data read function for your extension. The workflow step dropdown displays **Read from** followed by the **App name** you selected when you registered the extension app via the [form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), or the value from the [name](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) property in the app manifest if you registered the extension app by [uploading an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/).

![](data:image/svg+xml;charset=utf-8,%3Csvg height='167' width='325' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Workflow read step selector](https://images.ctfassets.net/aj9z008chlq0/Bja7l0Ha9kGuEfmHXaluo/b099064b3f4b00f827872ba8453defad/StepSelectorReadStep.png?w=325&h=167&q=50&fm=png)

The **Read from** step for your extension will not appear in the dropdown if:

- The extension app is not [installed and connected to your account](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html).
- The [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-names) and [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) actions, which are executed when the connection is established, did not succeed. If you suspect that this is the case, run the Developer Console [connection and extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) to troubleshoot.

Configure the settings for this step as follows:

| **Setting** | **Value** |
| --- | --- |
| Where will you read from? | **Connection**: Select the default connection  **[extension app name] object:** Select the object type in the external system to read data from. The objects listed are those the Maestro service retrieved when it executed the [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-names) action. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='460' width='824' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Where will you read from](https://images.ctfassets.net/aj9z008chlq0/4QShvPhbfGOyO5yBebBLA1/b3be1dea3b888885b2b34b7855a99919/ReadStep_WhereWillYouReadFrom.png?w=824&h=460&q=50&fm=png)

|  |  |
| --- | --- |
| Which fields would you like to read? | Select **Add or Remove Fields** to choose the fields whose values the Maestro service should retrieve.   The **Add or Remove Fields** page lists all fields in the selected source object that were returned by the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) action. In addition, the page lists any objects related to the source object that were included in the data model information returned to Docusign. You can select a related object, and then select fields in that object to read. Embedded objects are also listed, and their fields can be selected as well.   Select fields that you can map to fields in the web form that you’ll use in the [Collect Data with Web Forms step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#collect-data-with-web-forms-step). You’ll configure that step to populate web form fields with values retrieved from the external system. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='641' width='1377' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Which fields would you like to read](https://images.ctfassets.net/aj9z008chlq0/2dI8YNgikU5aDpOkdj7D81/bb50f68e55178d88c2eb224d86631baf/ReadStep_AddOrRemoveFields.png?w=1377&h=641&q=50&fm=png)

|  |  |
| --- | --- |
| Which record are you reading from? | Add rules that the Maestro service will use to identify records to read data from.  When defining a rule, you select a data source field, an operator, and a workflow field to compare to the data source field. For the data source field, you can select any field that was configured in the **Which fields would you like to read** setting. This includes fields from related and embedded objects, which are listed in the **[app name] field** list by object name followed by **(reference)**. To select a field from a related or embedded object, you first select the object name and then select a field from the object.  For testing purposes, select **Manual entry** under **Workflow field**, and then hard-code a value.  To define additional rules, select the **AND** or **OR** button.  **Note:** When the workflow is executed, the read step will fail if no record in the data source meets the criteria. Maestro uses only the first five records in the response in subsequent workflow processing.  You can use the preview feature to see which records the search will return. See [Configure a Read from Salesforce Step﻿](https://support.docusign.com/s/document-item?bundleId=qwr1706590641805&topicId=idr1713985144297.html) for details about previewing query results. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='920' width='831' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Which record are you reading from](https://images.ctfassets.net/aj9z008chlq0/7hrD7TtXyTGERBdD418CuA/09b209aefbd4a923af27616fbe3c00f1/ReadStep_WhichRecordAreYouReadingFrom.png?w=831&h=920&q=50&fm=png)

### Collect Data with Web Forms step

A **Collect Data with Web Forms** step displays a web form consisting of fields in which a participant can supply values. A procedure for adding this type of step appears in [Configure a Collect Data with Web Forms Step](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=gua1698120920620.html)﻿﻿.

Configure the settings for this step as follows:

| **Setting** | **Value** |
| --- | --- |
| Which form would you like to use? | Select the web form that you created for the workflow test, or an existing web form that you can use.  Only standalone web forms are available for selection. See [Step 1. Identify or create a web form](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#step-1-identify-or-create-a-web-form) for more information. |
| Who will participate in this step? | Select the role name you entered when you configured the [workflow participant](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#workflow-participant). |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='852' width='834' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Web form step configuration](https://images.ctfassets.net/aj9z008chlq0/2a4ErN7Rk6fgimsgec7lUn/bbf55406039a267800f25d0f45744c71/WebFormStep_FormAndParticipant.png?w=834&h=852&q=50&fm=png)

|  |  |
| --- | --- |
| Map data fields | **Note:** If your workflow does not include a data read step, do not map data fields.  This section maps web form fields to fields in the external system. The form fields will be populated with values retrieved from the external system via the data read step when you execute the workflow.  The configuration screen lists all web form fields. You are not required to map every form field to a field in the external system.  To map a form field:  1. Select the dropdown below the form field name. 2. Scroll to the **Workflow Steps** list. 3. Select the data read step. 4. Select the external system field whose value should be displayed in the web form field.   **Note:** The only external system fields available to select are those you configured in the **Which fields would you like to read?** section of the [data read step](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#data-read-step). |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1247' width='832' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Web form step map data fields](https://images.ctfassets.net/aj9z008chlq0/2BVtT3yTYVFKTd0nnqmcDw/94884531eaf7b6d21431b4d74fe09353/WebFormStep_MapDataFields.png?w=832&h=1247&q=50&fm=png)

### Data write step

**Note:** If you do not want to test writing data to an external data source, omit this step from the workflow.

This step invokes your data IO extension to write values from the web form to the external system. This step tests the [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records), [Patch Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-patch-record), and [Create Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-create-record) actions.

When you add this step, you select the data write function for your extension. The workflow step dropdown displays **Writeback to** followed by the **App name** you selected when you registered the extension app via the [form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), or the value from the [name](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) property in the app manifest if you registered the extension app by [uploading an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/).

![](data:image/svg+xml;charset=utf-8,%3Csvg height='163' width='325' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Step selector data write step](https://images.ctfassets.net/aj9z008chlq0/4B6HgGdDI3eiPoA72iULoJ/75f62ee1a1968e1ca4a5cb7ca70166ee/StepSelectorWriteStep.png?w=325&h=163&q=50&fm=png)

The **Writeback to** step for your extension will not appear in the dropdown if:

- The extension app is not [installed and connected to your account](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html).
- The [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-names) and [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) actions, which are executed when the connection is established, did not succeed. If you suspect that this is the case, run the Developer Console [connection and extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) to troubleshoot.

- The extension app implements data read but not data write.

Configure the settings for this step as follows:

| **Setting** | **Value** |
| --- | --- |
| Where will you write to? | **Connection**: Select the default connection.  **[extension app name] object:** Select the object in the external system to write data to. The objects listed are those the Maestro service retrieved when it executed the [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-names) action.   **Write settings:** Select one of the following:  - **Update or create:** Attempts to identify a record to update based on criteria you supply. If no existing record meets the criteria, Maestro creates a new record. Executes the [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records) action. Then, if a matching record is found, executes [Patch Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-patch-record); otherwise, executes [Create Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-create-record). - **Update:** Updates a record based on criteria you supply. If no existing record meets the criteria, the write operation fails. Executes the **Search Records** action and then **Patch Record** if a matching record is found. - **Create:** Creates a new record. Executes the **Create Record** action. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='719.0000000000001' width='829' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Where will you write to](https://images.ctfassets.net/aj9z008chlq0/23nI05KyhqrQtPTKuV5NVu/84881bba8390f0279f048111de151439/WritebackStep_WhereWillYouWriteTo.png?w=829&h=719&q=50&fm=png)

|  |  |
| --- | --- |
| Which fields are you writing to? | The **Fields** list contains the external system fields that this step will write to. By default, the list contains only fields that are marked as required and not read-only in the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) response.  To update additional fields, select **Add or remove fields**. You can select fields and save the selections. The added fields appear in the **Fields** list. You can write only to one object. You cannot select fields from related or embedded objects.  Map each external system field in the **Fields** list to a web form field:  1. Select the dropdown below the field name. 2. Scroll down to the **Collect Data with Web Forms** section. 3. Select the web form field whose value should be written to this field in the external system.   For some web form fields, you can select one of several value types. See [Web form field value types](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#web-form-field-value-types) for details. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='996' width='827' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Which fields are you writing to](https://images.ctfassets.net/aj9z008chlq0/331LKuHazTsNJDB92qBB5V/356fc7c79550b9ed72f5a28e3058ba00/WritebackStep_WhichFieldsAreYouWritingTo.png?w=827&h=996&q=50&fm=png)

|  |  |
| --- | --- |
| Which record are you writing to? | This setting appears only if **Write settings** is set to **Update** or **Update or create**.  Add rules that the Maestro service will use to identify a record to write to. When defining a rule, you select a data source field, an operator, and a workflow field to compare to the data source field. For the data source field, you can select any field that was configured in the **Which fields would you like to read** setting. This includes fields from related and embedded objects, which are listed in the **[app name] field** list by object name followed by **(reference)**. To select a field from a related or embedded object, you first select the object name and then select a field from the object.  For the **Workflow field**, you can select a field from the read step or the web form, or you can select **Manual entry**, and then hard-code a value.  To define additional rules, select the **AND** or **OR** button.  If the rules defined here result in the retrieval of more than one matching record, the workflow instance execution fails with the error `Found multiple records for the given search query`. |

![](data:image/svg+xml;charset=utf-8,%3Csvg height='846' width='842' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Which record are you writing to](https://images.ctfassets.net/aj9z008chlq0/7zMvEjZB8rKvL7c4notr7D/7254d4216d5da704105de5ac80ca3baa/WritebackStep_WhichRecordAreYouWritingTo.png?w=842&h=846&q=50&fm=png)

### Show a Confirmation Screen step

The last step in your workflow should be a **Show a Confirmation Screen** step, which displays a message to indicate that the workflow is complete. A procedure for adding this type of step appears in [Configure a Show a Confirmation Screen Step﻿](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=rpc1698682081448.html).

When you add this step, configure the settings as follows:

| **Setting** | **Value** |
| --- | --- |
| Participant who will see messages | Select the role name you entered when you configured the [workflow participant](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/#workflow-participant). |
| Message type | End of participant’s tasks |
| Message title | Keep the default value |
| Message body | Keep the default value |

### Web form field value types

When working with web form fields in Workflow Builder, you can select different value types for some fields. For fields that support multiple value types, the step configuration screen’s web form field list includes a row for each value type. In the sample screen shown here, the **Last Review** web form field has these value types available to select: **Normalized**, **User Value**, and **Format**.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='397' width='510' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Web form field value types](https://images.ctfassets.net/aj9z008chlq0/7JVGICl2sN9benn71tMKAG/09db89da6f416b75d6c8fbb798602d10/WebFormValueTypes.png?w=510&h=397&q=50&fm=png)

Below is a list of value types available for each web form field type.

| **Value type** | **Applicable web form field types** | **Value used in the operation when you select this type** |
| --- | --- | --- |
|  | Text | The value entered in the web form field is always used, so text field listings do not include a value type. |
| User Value | Number Date | The value entered in the web form field, including any separators. |
| Normalized | Number Date | For a date field, the date in UTC format. For a number field, the number with a period as a decimal separator. |
| Format | Number Date | The format of the date or number field as defined in the web form. For a date field, this will be a format like `MM/DD/YYYY`. For a number field, possible values are `periodSeparatedNumber` (decimal separator is a period) and `commaSeparatedNumber` (decimal separator is a comma). |
| Selected Value | Dropdown Radio buttons | The **API value** of the selected dropdown item or radio button, as defined in the web form. See [Add or Edit Field Properties on a Web Form﻿](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=fzu1672965301647.html) for details. |
| Selected Label | Dropdown Radio buttons | The **Option text** of the selected dropdown item or radio button, as defined in the web form. See [Add or Edit Field Properties on a Web Form﻿](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=fzu1672965301647.html)﻿ for details. |
| [checkbox option text] | Checkbox | `true` if the checkbox is selected in the web form, otherwise `false`. The checkbox **Option text** is defined in the web form. See [Add or Edit Properties for a Web Forms Checkbox Field](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=rws1673560056362.html)﻿ for details. |

## Step 3. Execute a workflow instance

Once you’ve [published your workflow](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=iqm1698272226447.html), you can execute an instance of it to run through the steps as an end user would and make sure that the data read and write operations succeed.

1. Follow the steps in the **From Within Workflow Builder** section of [How to Start a Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html) to execute a workflow instance.
2. If the workflow includes a data read step, confirm that the web form loads with values retrieved from the external system.
3. Fill out and submit the web form.
4. Confirm the submitted form values.
5. The confirmation page is displayed.
6. If the workflow includes a data write step, check the external system to confirm that web form values were successfully written to it.

If your extension is not invoked successfully, run the Developer Console [connection and extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) for the extension app to get detailed error messages and troubleshoot.

## Next steps

- Find out more about [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/).
- See reference information for the [data IO extension](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/).
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
