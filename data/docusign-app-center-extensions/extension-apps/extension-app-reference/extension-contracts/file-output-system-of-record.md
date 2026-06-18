---
title: File output system of record extension contract reference (beta)
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- Extension Contracts
- Extension Contracts
- File Output System Of Record
scraped_at: '2026-06-18T19:51:52Z'
---

# File output system of record extension contract reference (beta)

This extension can be invoked from a step in a [workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html) to write files to a system of record. The source for the files to write can be either of the following:

- A workflow [Send Documents for Signature step](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uww1698167288211.html), which enables users to complete and sign [eSignature envelopes](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=ghu1578456429097.html).
- Any envelope sent from the Docusign account that meets certain conditions.

See [Identify the file source](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-file-source/) for details.

A workflow that uses the file output system of record extension may also invoke a [data IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/). The data IO extension enables workflow process builders to define a query that returns the ID of the record to which a file will be written. If a data IO extension is not used, workflow process builders must select a workflow variable instead. The runtime value of this workflow variable can be used to identify the record to which a file will be written. See [Identify destination records](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/) for more information.

## Extension app registration

You can include the file output system of record extension and, optionally, the data IO extension when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). If you register the extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-form/), select the **File Output System of Record** extension and, if needed, the **Data IO** extension in the form-based UI, as shown here:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='659' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Form-based extension selection](https://images.ctfassets.net/aj9z008chlq0/2NXr8RmjPTNWLSYkqn2GH1/4555a482a9d9e71ad9394713ec0ee953/FormBasedSelectExtensionwithDataIOsmall.png?w=600&h=659&q=50&fm=png)

During the form-based extension app registration process, if you select a [file IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), its required actions are automatically added to the app. You can then configure the actions' endpoint URIs and other properties on the [Integration Details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/) page. The extension's optional capabilities can be added or removed only by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). After you've added capabilities via the manifest file, you can edit them on the Integration Details page. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action and capability properties in the app manifest file.

If you register the extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), the `extensions` object must include the file output system of record extension and, if needed, the data IO extension. Set the `extensions.template` values in your app manifest as follows:

- `FileIO.Version1.FileOutputSystemOfRecord` for the file output system of record extension
- `DataIO.Version6.DataInputOutput` (optional) for the data IO extension

The actions that your app manifest includes depend on whether the app uses the data IO extension. This extension enables process builders to define a query that returns the ID of the record to which files will be written. See the next sections for details.

When registering an extension app, you cannot include both a [file output system of record extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/) and a [file output cloud storage extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/) in the same app. If you need to use both types of output in workflows, register a separate app for each extension.

## Required actions

A file output to system of record app requires you to implement a set of actions to support the functionality. This set of actions differs depending on whether you are implementing the file output system of record extension by itself, or implementing file output alongside data IO. See the next sections for details.

### Required actions: File output system of record extension only

For this option, the app registration must include both the **Write File** action and the **Get Type Names** capability. Below is a list of their identifiers as they appear in the form-based app registration UI and the app manifest. See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for this scenario.

| Form-based UI name | App manifest actions.template value | App manifest actions.name value | App manifest extensions.capabilities value | Required |
| --- | --- | --- | --- | --- |
| Write File | `FileIO.Version1.WriteFile` | `write-file` | N/A | Yes |
| Get Type Names | `DataIO.Version6.GetTypeNames` | `get-type-names` | `DataIO.Version6.GetTypeNames` | Yes |

Both the action and the capability are defined in the app manifest fileʼs `actions` object. This definition includes a template value, a name, and the endpoint URL. The action and capability must also be referenced from the `extensions` object as follows:

- For both the action and capability, include the `actions.name` value from the `actions` object in the `extensions.actionReferences` array.
- Include a reference to the capability in the `extensions.capabilities` array. Use the value from the **App manifest extensions.capabilities value** column in the table above.

For example, the manifest file action definitions for the **Write File** action and the **Get Type Names** capability look like this:

```
"actions": [
  {
    "name": "get-type-names",
    "description": "Returns system of record objects",
    "template": "DataIO.Version6.GetTypeNames",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/dataio/getTypeNames"
    }
  },
  {
    "name": "write-file",
    "description": "Writes files to a system of record",
    "template": "FileIO.Version1.WriteFile",
    "connectionsReference": "authentication",
    "params": {
	    "uri": "https://fontara.com/api/writefile"
    }
  }
]
```

The `extensions` object includes the `actions.name` values for both the **Write File** action and the **Get Type Names** capability in the `actionReferences` array. In addition, the **Get Type Names** capability is included in the `capabilities` array:

```
"extensions": [
  {
    "name": "File Output to Fontara Data Source",
    "description": "Write a file to the system of record",
    "template": "FileIO.Version1.FileOutputSystemOfRecord",
    "actionReferences": [
    	"write-file",
    	"get-type-names"
    ],
    "capabilities": ["DataIO.Version6.GetTypeNames"]
  }
]
```

### Required actions: File output system of record extension with data IO extension

For this option, the app registration must include the **Write File**, **Get Type Names**, **Get Type Definitions**, and **Search Records** actions. Below is a list of the actions' identifiers as they appear in the form-based app registration UI and the app manifest. See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for this scenario.

| Form-based UI name | App manifest actions.template value | App manifest actions.name value | Required |
| --- | --- | --- | --- |
| Write File | `FileIO.Version1.WriteFile` | `write-file` | Yes |
| Get Type Names | `DataIO.Version6.GetTypeNames` | Any name can be used.  **Note:** If **Get Type Names** is included as a capability for the file output system of record extension, the `actions.name` must be `get-type-names`. See [Required actions: File output extension only](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#required-actions-file-output-system-of-record-extension-only) for details. | Yes |
| Get Type Definitions | `DataIO.Version6.GetTypeDefinitions` | Any name can be used. | Yes |
| Search Records | `DataIO.Version6.SearchRecords` | Any name can be used. | Yes |

Each action is defined in the app manifest fileʼs `actions` object. This definition includes a template value, a name, and the endpoint URL. Each action must also be referenced from the `extensions` object. To reference it, include the `actions.name` value from the `actions` object in the `extensions.actionReferences` array.

For example, the manifest file action definitions look like this:

```
"actions": [
  {
    "name": "search-records",
    "description": "Searches the system of record",
    "template": "DataIO.Version6.SearchRecords",
    "connectionsReference": "authentication",
    "params": {
	  "uri": "https://fontara.com/api/dataio/searchRecords"
    }
  },
  {
    "name": "get-type-names",
    "description": "Retrieves a list of objects from the system of record",
    "template": "DataIO.Version6.GetTypeNames",
    "connectionsReference": "authentication",
    "params": {
	  "uri": "https://fontara.com/api/dataio/getTypeNames"
    }
  },
  {
    "name": "get-type-definitions",
    "description": "Retrieves object property definitions from the system of record",
    "template": "DataIO.Version6.GetTypeDefinitions",
    "connectionsReference": "authentication",
    "params": {
	  "uri": "https://fontara.com/api/dataio/getTypeDefinitions"
    }
  },
  {
    "name": "write-file",
    "description": "Writes a file to the system of record",
    "template": "FileIO.Version1.WriteFile",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/writefile"
    }
  }
]
```

The `extensions` object includes both the file output system of record extension and the data IO extension, with the `actions.name` values for each extension's actions in the corresponding `actionReferences` array:

```
"extensions": [
  {
    "name": "Data IO",
    "description": "Reads from the system of record",
    "template": "DataIO.Version6.DataInputOutput",
    "actionReferences": [
	  "search-records",
	  "get-type-names",
	  "get-type-definitions"
    ]
  },
  {
    "name": "File output system of record",
    "description": "Writes a file to the system of record",
    "template": "FileIO.Version1.FileOutputSystemOfRecord",
    "actionReferences": [
      "write-file"
    ],
    "capabilities": []
    }
]
```

## Action contracts

These sections provide details about the requests and responses sent between Docusign and the external service for each action and capability:

- [Write File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#write-file)
- [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#get-type-names)

**Note:** For details about the data IO action contracts, see [Data IO extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/).

## Write File (FileIO.Version1.WriteFile)

This required action writes one or more documents to a system of record. It can be triggered from a Workflow Builder workflow.

**Write File** is the label that appears when you register an extension app [using a guided, form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/).

If you register your extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), make sure that you:

1. Include a definition for the action in the `actions` object. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for details about the required properties. The action definition must include these values, which are specific to this action:
   - `name: write-file`
   - `template: FileIO.Version1.WriteFile`
2. Include the value from the `actions.name` property in the `extensions.actionReferences` array.  See [Extension schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) for details.

See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for file output to system of record.

### HTTP method

This action initiates a POST request to the external API service.

### Request

Request with hardcoded file name:

```
{
  "files": [
    {
      "basename": "EFTAuthorization.pdf",
      "path": "",
      "pathTemplateValues": [],
      "parentId": "111222333",
      "contents": "JVBERi...VFT0YK"
    }
  ],
  "rootId": "FinancialAccount"
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `files` | `Object[]` | Required | An array of files to write to the system of record.  If a workflow is configured to send files generated from a **Send Documents for Signature** step, the `files` array contains a single element.  The `files` array can contain multiple elements if both of the following are true:   - The workflow that generates the request is configured to [start new instances](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html) based on an envelope event. - When configuring the **File Output** step, the workflow process builder selected the option to store envelope documents individually.   A `file` object contains a single `parentId`, whose value identifies  the record to which to write the file or files. To support storing documents individually, the external data source must be able to accommodate writing multiple files to the same record. If the data source does not support this, you should notify process builders that they should not select the option to store documents individually. |
| `files.basename` | `String` | Required | The file name, including the extension.  Docusign populates this value based on the file name that a process builder defines while configuring a Workflow Builder workflow **File Output** step. The naming convention can use workflow variables, such as an envelope ID, and hardcoded values. See [File names that include workflow variables](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#file-names-that-include-workflow-variables) for details.  If the `files` array contains multiple elements, each file's `basename` will follow the file naming convention specified, with a hyphen and number appended to the name. For example, if the process builder specified that the file name should use an envelope ID workflow variable, the `basename` values for each of three files would look like this:   - `{{Envelope Id}}-1.pdf` - `{{Envelope Id}}-2.pdf` - `{{Envelope Id}}-3.pdf` |
| `files.path` | `String` | Required | Not used. This property is included in requests triggered from Workflow Builder workflows, but it has an empty value. |
| `files.pathTemplateValues` | `String[]` | Optional | If the workflow was configured with a file naming convention that includes variables, the elements in this array consist of the workflow-instance–specific variable values. The external system must extract the variable values in this array and use them to construct the file name. See [File names that include workflow variables](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-output-system-of-record/#file-names-that-include-workflow-variables) for details. |
| `files.parentId` | `String` | Required | A value that can be used to identify the record to which the file is to be written. The external service must implement logic to select a record based on this value.  Depending on how the workflow has been configured, `parentId` can be populated with:   - A workflow variable value derived from the workflow start method or a previous workflow step - A data source record ID returned by **Read from** step in the workflow - Another type of data source record value returned by a **Read from** step   See [Identify destination records](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/) for details. |
| `files.contents` | `String` | Required | The file contents, converted to a Base64 string. |
| `rootId` | `String` | Required | The system of record object to which the file is to be written. |

Docusign passes values in the **Write File** request that specify the object (in the `rootId` property) and record (in the `parentId` property) to which a file is to be written. The external service must implement logic to determine the property to which to write the file contents.

#### Hardcoded file names

A workflow process builder can hardcode file names when defining a **File Output** step, as shown here:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='549' width='520' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Hardcoded file name](https://images.ctfassets.net/aj9z008chlq0/4TXQ5fbYKTfBJ8BUnJ84FA/5498e550b0f12e9707a626232c314fb3/MaestroConfigHardcodedFileName_small.png?w=520&h=549&q=50&fm=png)

If the file name is hardcoded, the same name will be used for every file that is written to the system of record when workflow instances are executed. The hardcoded name will be populated in the **Write File** requestʼs `files.basename` property. If a workflow process builder has selected the option to store files individually, a hyphen and number will be appended to the name of each file included in the same **Write File** request.

#### File names that include workflow variables

Instead of hardcoding file names, a process builder can use workflow variables to construct names that will be unique for each workflow instance. The variable values will be set during instance execution.

**Note:** Because hardcoded values will result in the same file names being used for every workflow instance, Docusign recommends using variables in the names.

If a workflow is configured to start from an event and to store files individually, a process builder can select the **Document Name** variable. At run time, this value will be populated with the file name from the eSignature envelope.

Shown here is an example in which a process builder has constructed a file naming convention that consists of a combination of hardcoded values and variable names. The variable names appear in square brackets in the **File path**.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='622' width='620' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![File name with variables](https://images.ctfassets.net/aj9z008chlq0/4SK8SjmeQ30gIdX3dhlQ8S/ae3de8a1bbe728233cbe13086670cb71/MaestroConfigVariableFileName_small.png?w=620&h=622&q=50&fm=png)

If a file output step specifies a file name containing variables, the **Write File** request body will include a `files.pathTemplateValues` array that lists the workflow-instance–specific variable values. When it receives the **Write File** request, the external system must use values from the `files.basename` property and the `files.pathTemplateValues` array to construct the file name as follows:

- Parse the `files.basename` value in the request to determine which variables must be replaced with values. Each variable is listed in double curly braces. For example, `{{Envelope ID}}` refers to an envelope ID variable.
- For each variable in `files.basename`, replace the string in double curly braces with the corresponding instance-specific value from the `pathTemplateValues` array. The order of the `pathTemplateValues` elements matches the order of the `files.basename` variables.

Below is an example **Write File** request based on the file naming convention shown in the screenshot:

```
{
  "files": [
    {
      "basename": "Envelope ID {{Envelope ID}}Instance start time {{Start Date and Time}}.pdf",
      "path": "",
      "pathTemplateValues": [
        "a7ac1092-xxxx-xxxx-xxxx-7d4f31cb017d",
        "2025-12-01T19:12:27.560Z"
      ],
      "parentId": "1",
      "contents": "JVBERi...VFT0YK"
    }
  ],
  "rootId": "Contact"
}
```

The external system would complete these steps to derive the file name:

1. Replace `{{Envelope ID}}` with `a7ac1092-xxxx-xxxx-xxxx-7d4f31cb017d`
2. Replace `{{Start Date and Time}}` with `2025-12-01T19:12:27.560Z`

**Note:** The external system should remove or replace prohibited characters in the file name.

The file name to use for the file sent in the request would be:

`Envelope ID a7ac1092-xxxx-xxxx-xxxx-7d4f31cb017dInstance start time 2025-12-01T19_12_27.560Z.pdf`

In this example, the prohibited colon character in the start date/time has been replaced with an underscore.

### Response

```
{
  message: "File successfully saved"
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `message` | `String` | Required | Information describing the result of the file write operation. This message is displayed with the test result when a Developer Console [extension test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) is run. It is not displayed to end users during workflow instance execution. |

## Get Type Names (DataIO.Version6.GetTypeNames)

This optional [capability](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) can be implemented for a file output system of record extension. It retrieves the names of the data objects (or database table names) in your system of record.

If this capability is implemented, the object names that it returns will be displayed in the Workflow Builder **File Output** step configuration screen. This enables a workflow process builder to select the object to which files will be written. If this capability is not implemented, the destination object for file output can be determined by a **Read from** step in the workflow that precedes the **File Output** step. See [Identify destination records](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/identify-destination-records/) for details about the two options.

**Get Type Names** is the label for this capability that appears when you register an extension app using a form. If you register your extension app using an app manifest file, the `actions.template` property value for this action is `DataIO.Version6.GetTypeNames`. The file output system of record extension uses the data IO extension’s **Get Type Names** action contract because the contract details are identical.

### HTTP method

This action initiates a POST request to the external API service.

### Request

```
{}
```

Docusign sends an empty request body to the external API service. No data is specified because the external system returns any objects that are available as the file output destination.

### Response

```
{
  "typeNames": [
    {
      "typeName": "Address",
      "label": "Address"
    },
    {
      "typeName": "Contact",
      "label": "Contact"
    },
    {
      "typeName": "FinancialAccount",
      "label": "Financial Account"
    }
  ]
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `typeNames` | `Object[]` | Required | A list of objects in the external system that support file output. |
| `typeNames[].typeName` | `String` | Required | The name of the object. This appears in the Workflow Builder **File Output** step configuration panel's list of objects. A workflow process builder selects the destination object for the **Write File** action from this list. |
| `typeNames[].label` | `String` | Required | This value is not displayed in Workflow Builder. |
| `typeNames[].description` | `String` | Optional | This value is not displayed in Workflow Builder. |

## Error handling

The external system should return a 200 response code to Docusign if a request succeeded. Any other response code indicates that the request was not successfully executed. Developers are responsible for providing a code and message for each error.

## Next steps

- Get an [overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/) of the file output system of record extension and how it can be used.
- Explore the options for [testing](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) a file output system of record extension.
- Find out about other [supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/).

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
