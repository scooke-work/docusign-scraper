---
title: File input cloud storage extension contract reference
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- Extension Contracts
- Extension Contracts
- File Input Cloud Storage
scraped_at: '2026-06-18T19:51:52Z'
---

# File input cloud storage extension contract reference

The file input cloud storage extension imports documents from a cloud storage system to [Docusign Agreement Manager](https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=adf1702945446135.html). Agreement Manager is a platform service that uses AI to analyze, classify, and extract structured data from agreements. See [File input cloud storage extension overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/) for details about how the extension is invoked in Agreement Manager, the supported file types, and other behaviors and restrictions.

You can include this extension when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). If you register the extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), select the **File Input Cloud Storage** extension in the form-based UI, as shown in this figure:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='328' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Form-based app creation](https://images.ctfassets.net/aj9z008chlq0/3yqjUkaebQ8s2CdYMT4j1N/31bba8248695fd6d0c14cc64c9323a7c/FormBasedExtensionSelection.png?w=600&h=328&q=50&fm=png)

During the form-based extension app registration process, if you select a [file IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), its required actions are automatically added to the app. You can then configure the actions' endpoint URIs and other properties on the [Integration Details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/) page. The extension's optional capabilities can be added or removed only by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). After you've added capabilities via the manifest file, you can edit them on the Integration Details page. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action and capability properties in the app manifest file.

If you register the extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), set the `extensions.template` value in your app manifest to `FileIO.Version1.FileInputCloudStorage`.

This extension has three required actions and one optional capability. Below is a list of their identifiers as they appear in the form-based app registration UI and the app manifest. See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for file input from cloud storage.

| Form-based UI name | App manifest actions.template value | App manifest actions.name value | App manifest extensions.capabilities value | Required |
| --- | --- | --- | --- | --- |
| Get File | `FileIO.Version1.GetFile` | `get-file` | N/A | Yes |
| Search | `FileIO.Version1.Search` | `search` | N/A | Yes |
| List Directory Contents | `FileIO.Version1.ListDirectoryContents` | `list-directory-contents` | N/A | Yes |
| List Drives | `FileIO.Version1.ListDrives` | `list-drives` | `FileIO.Version1.ListDrives` | No |

Both the actions and the capability are defined in the app manifest fileʼs `actions` object. This definition includes a `template` value, a `name`, and the endpoint URL. The actions and capability must also be referenced from the `extensions` object as follows:

- For both the actions and capability, include the `actions.name` value from the `actions` object in the `extensions.actionReferences` array.
- Include a reference to the capability in the `extensions.capabilities` array. Use the value from the **App manifest extensions.capabilities value** column in the table above.

For example, the manifest file action definitions for the required actions and the optional **List Drives** capability look like this:

```
"actions": [
  {
    "name": "get-file",
    "description": "Uploads files from cloud storage",
    "template": "FileIO.Version1.GetFile",
    "contractType": "action-with-callback",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/getfile"
    }
  },
  {
    "name": "list-directory-contents",
    "description": "Lists files and folders in a cloud storage directory",
    "template": "FileIO.Version1.ListDirectoryContents",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/listdirectorycontents"
    }
  },
  {
    "name": "search",
    "description": "Searches for files and folders on the cloud storage system",
    "template": "FileIO.Version1.Search",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/search"
    }
  },
  {
    "name": "list-drives",
    "description": "List drives on the cloud storage system",
    "template": "FileIO.Version1.ListDrives",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/listdrives"
    }
]
```

The `extensions` objectʼs `actionReferences` array includes the `actions.name` values for the **Get File**, **List Directory Contents**, and **Search** actions and the **List Drives** capability. In addition, the **List Drives** capability is included in the `capabilities` array:

```
"extensions": [
  {
    "name": "My File Input Cloud Storage Extension",
    "description": "Imports files from cloud storage",
    "template": "FileIO.Version1.FileInputCloudStorage",
    "capabilities": ["FileIO.Version1.ListDrives"],
    "actionReferences": [
      "get-file",
      "list-directory-contents",
      "search",
      "list-drives"
    ]
  }
]
```

For details about what the actions and capability do when invoked, see [File input cloud storage actions and capability](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/#file-input-cloud-storage-actions-and-capability).

These sections provide details about the requests and responses sent between Docusign and the external service for each action and capability:

- [Get File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file)
- [List Drives](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-drives)
- [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-directory-contents)
- [Search](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#search)

## Get File (FileIO.Version1.GetFile)

This required action imports a file into Docusign Agreement Manager. If a user selects multiple files for import, Docusign executes a separate **Get File** action for each file.

**Get File** is the label that appears when you register an extension app [using a guided, form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/).

If you register your extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), make sure that you:

1. Include a definition for the action in the `actions` object. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for details about the required properties. The action definition must include these values, which are specific to this action:
   - `name: get-file`
   - `template: FileIO.Version1.GetFile`
   - `contractType: action-with-callback`
2. Include the value from the `actions.name` property in the `extensions.actionReferences` array.  See [Extension schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) for details.

See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for file input from cloud storage.

### Get File sequence of requests and responses

Below is the sequence of requests and responses between Docusign and the external service for a **Get File** action. Details about each one appear in the next sections.

1. [Get File request to the external service](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file-request-to-the-external-service)
2. [Get File synchronous response to Docusign](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file-synchronous-response-to-docusign)
3. [Upload request to Docusign](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#upload-request-to-docusign)
4. [Upload response to the external service](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#upload-response-to-the-external-service)
5. [Callback request to Docusign](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#callback-request-to-docusign)
6. [Callback response to the external service](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#callback-response-to-the-external-service)

### Get File request to the external service

Docusign sends this POST request when a user selects a file for upload in Agreement Manager.

#### Get File request header

The request includes an `x-docusign-session` header that is Base64-encoded. The external service must decode this header to extract these values for use in subsequent processing:

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `sessionToken` | `String` | Required | A token that is unique to the **Get File** request and contains encoded claims. This value must be provided in the `Authorization` header of the [upload](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#upload-request-to-docusign) and [callback](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#callback-request-to-docusign) requests to Docusign. |
| `expiresAt` | `DateTime` | Required | The date and time at which the `sessionToken` expires. This value is:   - Eight hours after the request time - In ISO 8601 UTC format   For example:   ``` 2025-10-07T03:17:42.879Z ```  If Docusign receives an [upload](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#upload-request-to-docusign) or [callback](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#callback-request-to-docusign) request with an expired `sessionToken`, a **401 Unauthorized** HTTP error code is returned. |
| `filesApiUrl` | `String` | Required | The Docusign URL to which the external system should send the file [upload](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#upload-request-to-docusign) request. |
| `callbackUrl` | `String` | Required | The Docusign URL to which the external system should send the [callback](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#callback-request-to-docusign) request. |

#### Get File request body

The **Get File** request body includes a `fileId`, which is the ID of the file to upload to Agreement Manager. Docusign uses the file ID that the external system supplied in its response to a [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-directory-contents) or [Search](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#search) request that preceded the **Get File** request.

```
{
  "fileId": "12345"
}
```

### Get File synchronous response to Docusign

On receiving a **Get File** request, the external service should return a synchronous response with an empty response body. The synchronous response has no dependency on the file import being initiated or succeeding.

A success response from the external service should use a **202 Accepted** HTTP status code. If the external service cannot fulfill the **Get File** request from Docusign, it should return an appropriate HTTP error code, such as **401 Unauthorized** or **404 Not Found**.

On completion of the **Get File** request and a **202 Accepted** response, Agreement Manager creates an upload job for the file. The job status is **Transferring**. See [Job Monitoring for Agreement Uploads and Processing](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=ahg1742251814403.html)﻿ for details.

### Upload request to Docusign

This POST request to Docusign includes the contents of the file being uploaded. The file contents must be sent as a stream of raw bytes.

The request must use these values that have been extracted from the `x-docusign-session` header of the **Get File** request that Docusign sent to the external service:

- The URL to which the request should be sent.
- A session token in the request's `Authorization` header in this format:
  `Bearer: [sessionToken]`

See [Get File request header](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file-request-header) for details.

**Note:** The request does not require a `Content-Type` header. The type of file that Docusign expects in the request is encoded in the `sessionToken`. Docusign sets the expected file type based on the file that a user selected for upload in Agreement Manager.

After Docusign successfully processes an upload request, the Agreement Manager [upload job](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=ahg1742251814403.html) remains in **Transferring** status.

### Upload response to the external service

If Docusign successfully processes the upload request, it returns a **201 Created** HTTP status code with an `id` in the response body. The `id` is a GUID value that identifies the file on the Docusign system. This identifier will be different from the file ID that Docusign sent in the initial **Get File** request to the external service.

```
{
  "id": "ba7bf300-xxxx-xxxx-xxxx-563ce67f7053"
}
```

If the uploaded file exceeds the 25 MB [size limit](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/#adhere-to-file-upload-limitations), Docusign returns a **413 Content Too Large** error. After Docusign sends this or any other error response to an upload request, additional upload requests for the same **Get File** action will not succeed. The external service must report the failure in the callback request. See the next section for details.

### Callback request to Docusign

When the external system receives a response to the file upload request, it must send a POST callback request to notify Docusign whether the upload request succeeded or failed.

The request must use these values that have been extracted from the `x-docusign-session` header of the **Get File** request that Docusign sent to the external service:

- The URL to which the request should be sent.
- A session token in the request's `Authorization` header in this format:
  `Bearer: [sessionToken]`

See [Get File request header](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file-request-header) for details.

If the upload response from Docusign had a **201 Created** HTTP status code, the external system should report success in the callback request, as shown below. For a response with an HTTP error status code, such as **400 Bad Request**, the external system should report failure in the callback request.

```
{
  "status": "EXECUTION_STATUS_SUCCEEDED",
  "output": {
    "data": {
      "documentId": "ba7bf300-xxxx-xxxx-xxxx-563ce67f7053"
    }
  }
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `status` | `String` | Required | A status to indicate whether the upload request succeeded. Valid values:   - `EXECUTION_STATUS_SUCCEEDED`: Docusign returned a **201 Created** response to the upload request. - `EXECUTION_STATUS_FAILED`: Docusign returned any response other than **201 Created** for the upload request. |
| `output.data.documentId` | `String` | Required | The `id` that Docusign returned to the external service in the response to the upload request. |

After Docusign processes a callback request for a successful upload, the Agreement Manager [upload job](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=ahg1742251814403.html) status changes from **Transferring** to **Uploading**, and then to **Upload to Agreement Manager complete**. At this point, the file appears in the Agreement Manager [Agreement List Table](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=yjz1702945473104.html). Next, Agreement Manager uses AI to process the file and extract agreement data. See [Processing Agreements](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=rvw1736364838500.html) for details. For a failed upload, the Agreement Manager upload job status changes to **Failed** after the callback request is processed.

### Callback response to the external service

After Docusign processes the callback request, it returns a response with an `id` in the response body. This ID represents the file upload execution on the Docusign platform. This value is informational only. The external system is not required to use this ID for any processing.

```
{
  "id": "0fa98196-xxxx-xxxx-xxxx-9ae046c0c87b"
}
```

## List Drives (FileIO.Version1.ListDrives)

This optional [capability](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) can be implemented for a file input cloud storage extension. It returns the drives available in the cloud storage system. If this capability is implemented, a Agreement Manager user can select from a list of drives before browsing folders, searching, and selecting files to upload.

**Note:** If the cloud storage system does not have the concept of drives and instead organizes folders and files under a different container type, this capability can retrieve a list of those containers instead. They will appear in Agreement Manager's **Select Drive** list.

**List Drives** is the label that appears when you register an extension app [using a guided, form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/).

If you register your extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), make sure that you:

1. Include a definition for the capability in the `actions` object. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for details about the required properties. The action definition must include these values, which are specific to this capability:
   - `name: list-drives`
   - `template: FileIO.Version1.ListDrives`
2. Include the value from the `actions.name` property in the `extensions.actionReferences` array.
3. Include the value from the `actions.template` property in the `extensions.capabilities` array.

See [Extension schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) for details about the `actionReferences` and `capabilities` arrays. See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for file input from cloud storage.

### HTTP method

This capability initiates a POST request to the external API service.

### List Drives request body

```
{
  "containerType": "drive",
  "parentId": ""
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `containerType` | `String` | Required | Valid value:  ``` drive ```  **Note:** If the cloud storage system does not have the concept of drives and instead organizes folders and files under a different container type, the request will still have a value of `drive` for this property. |
| `parentId` | `String` | Optional | Docusign includes this property in requests but does not populate it with a value. |

### List Drives response body

```
{
  "containerType": "drive",
  "data": [
    {
      "containerId": "324235",
      "containerName": "Drive 1"
    },
    {
      "containerId": "546876",
      "containerName": "Drive 2"
    }
  ]
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `containerType` | `String` | Required | Valid value:  ``` drive ```  **Note:** If the cloud storage system does not have the concept of drives and instead organizes folders and files under a different container type, the response must still have a value of `drive` for this property. |
| `data` | `Object[]` | Required | An array of drives or similar structures that contain folders and files. |
| `data.containerId` | `String` | Required | A unique ID for the drive or other container type.  A `containerId` returned in this response will be included in a subsequent **List Directory Contents** request as follows:   1. A user selects from a list of drives (or other containers) on Navigator's **Select Files** window. 2. Docusign launches a **List Directory Contents** request to the external system that includes the `containerId` of the container selected in step 1 so that the external system can retrieve a list of folders and files from the selected container. |
| `data.containerName` | `String` | Required | The name of the drive or other container type. Agreement Manager displays `containerName` values in a list on the **Select Files** window. |

## List Directory Contents (FileIO.Version1.ListDirectoryContents)

This action is required for a file input cloud storage extension. It returns a list of folders and files in a drive or directory on the cloud storage system so that Agreement Manager can display them. This enables users to drill down into the cloud storage structure to locate files to upload. Each time a user selects a directory, Agreement Manager sends a **List Directory Contents** request to get the contents of the currently selected directory.

**List Directory Contents** is the label that appears when you register an extension app [using a guided, form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/).

If you register your extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), make sure that you:

1. Include a definition for the action in the `actions` object. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for details about the required properties. The action definition must include these values, which are specific to this action:
   - `name: list-directory-contents`
   - `template: FileIO.Version1.ListDirectoryContents`
2. Include the value from the `actions.name` property in the `extensions.actionReferences` array.

See [Extension schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) for details about the `actionReferences` and `capabilities` arrays. See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for file input from cloud storage.

### HTTP method

This action initiates a POST request to the external API service.

### List Directory Contents request body

```
{
  "filterOptions": {
    "allowedMimeTypes": [
      "application/pdf",
      "application/msword",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.
         document",
      "application/vnd.ms-powerpoint",
      "application/vnd.openxmlformats-officedocument.presentationml.
        slideshow",
      "application/vnd.openxmlformats-officedocument.presentationml.
        presentation",
      "application/rtf",
      "application/wordperfect",
      "application/vnd.ms-excel",
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
      "text/html",
      "image/jpeg",
      "image/png",
      "image/tiff"
    ],
    "maxFileSizeInBytes": 104857600
  },
  "limit": 100,
  "parentId": "324235"
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `filterOptions.allowedMimeTypes` | `String[]` | Required | A list of MIME types that Docusign supports for upload into Agreement Manager.  The external service should only return files of the supported types in response to a **List Directory Contents** request. |
| `filterOptions.maxFileSizeInBytes` | `Number` | Required | Not used.  **Note:** Docusign supports a file size of up to 25 MB, regardless of the number populated in this property. The external service should only return files that meet the 25 MB size restriction in response to a **List Directory Contents** request. |
| `limit` | `Number` | Required | Docusign includes this property in requests, but it is not used. |
| `parentId` | `String` | Required | One of the following:   - If the extension app implements **List Drives** and a user has selected a drive (or similar container type) and then selects a directory, this value will be the ID of the selected container. Container IDs are returned in the response to the **List Drives** request. - If the extension app does not implement **List Drives** and a user selects a top-level directory, this value will be `root`. - If the user selects a directory that is not at the top level, this value will be the ID of the parent folder. |

### List Directory Contents response body

```
{
  "parentId":"953831"
  "data":[
    {
      "type":"file",
      "name":"Addendum.pdf",
      "id": "84753",
      "parentId": "953831",
      "mimeType": "application/pdf",
      "lastModifiedDate": "2025-10-13T21:25:12.212Z"
    },
    {
      "type":"folder",
      "name":"Master Service Agreements",
      "id":"479012",
      "parentId": "953831"
    }
  ]
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `parentId` | `String` | Required | The external service should return the same `parentId` value that was supplied in the **List Directory Contents** request. |
| `data` | `Object[]` | Required | An array of files and folders in the drive (or similar container type) or directory specified in the request's `parentId` property.  **Note:** Only files within the 25 MB size limit should be returned. |
| `data.type` | `String` | Required | Valid values:   - `folder` - `file` |
| `data.name` | `String` | Required | The file or folder name. Agreement Manager displays the `name` value on the **Select Files** window.  Names can be up to 254 characters long. |
| `data.id` | `String` | Required | The file or folder ID.  If a Agreement Manager user selects a folder to drill down in the cloud storage structure, the `id` of the selected folder will be passed as the `parentId` in the next **List Directory Contents** request.  If a Agreement Manager user selects a file for upload, the `id` of the selected file will be sent to the external service in the [Get File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file) request. |
| `data.parentId` | `String` | Required | The ID of the folder in which the file or folder is located. For a top-level folder, use the drive ID or `root` if the extension app does not implement **List Drives**. This value should be the same as the `parentId` value that was supplied in the **List Directory Contents** request. |
| `data.mimeType` | `String` | Required for files only | For a file, populate the MIME type. It must be one of the supported MIME types provided in the [List Directory Contents request body](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-directory-contents-request-body). Agreement Manager displays the file type on the **Select Files** window.  For a folder, omit this property. |
| `data.lastModifiedDate` | `String` | Required for files only | For a file, populate the date-time when the file was last modified in this ISO 8601 UTC format:   ``` YYYY-MM-DDTHH:mm:ss.SSSZ ```  For example:   ``` 2025-10-13T00:00:00.000Z ```  Navigator displays the last modified date on the **Select Files** window.  For a folder, omit this property. |

## Search (FileIO.Version1.Search)

This action is required for a file input cloud storage extension. It returns a list of cloud storage folders and files whose names match a search string that a Agreement Manager user has entered.

Docusign passes the search string to the external service exactly as entered in the Agreement Manager search field. The external service can implement handling for wildcard characters in search strings, or any other search logic as appropriate.

The search request from Docusign does not specify the ID of a drive or directory to search. The response should return all matching folders and files that are eligible to be selected as an upload source, regardless of their location on the cloud storage system.

**Search** is the label that appears when you register an extension app [using a guided, form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/).

If you register your extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), make sure that you:

1. Include a definition for the action in the `actions` object. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for details about the required properties. The action definition must include these values, which are specific to this action:
   - `name: search`
   - `template: FileIO.Version1.Search`
2. Include the value from the `actions.name` property in the `extensions.actionReferences` array.

See [Extension schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) for details about the `actionReferences` and `capabilities` arrays. See [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for a complete sample app manifest for file input from cloud storage.

### HTTP method

This action initiates a POST request to the external API service.

### Search request body

```
{
  "searchQuery": "payment",
  "filterOptions": {
    "allowedMimeTypes": [
      "application/pdf",
      "application/msword",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.
         document",
      "application/vnd.ms-powerpoint",
      "application/vnd.openxmlformats-officedocument.presentationml.
        slideshow",
      "application/vnd.openxmlformats-officedocument.presentationml.
        presentation",
      "application/rtf",
      "application/wordperfect",
      "application/vnd.ms-excel",
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
      "text/html",
      "image/jpeg",
      "image/png",
      "image/tiff"
    ],
    "maxFileSizeInBytes": 104857600
  }
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `searchQuery` | `String` | Required | The search string that a user entered in Agreement Manager. |
| `filterOptions.allowedMimeTypes` | `String[]` | Required | A list of MIME types that Docusign supports for upload into Agreement Manager.  The external service should only return files of the supported types in response to a **Search** request. |
| `filterOptions.maxFileSizeInBytes` | `Number` | Required | Not used.  **Note:** Docusign supports a file size of up to 25 MB, regardless of the number populated in this property. The external service should only return files that meet the 25 MB size restriction in response to a **Search** request. |

### Search response body

```
{
  "results": [
    {
      "type": "folder",
      "name": "Payments",
      "id": "479012",
      "parentId": "48939"
    },
    {
      "type": "file",
      "name": "PaymentSchedule.xlsx",
      "id": "23573",
      "parentId": "93170",
      "mimeType":"application/vnd.openxmlformats-officedocument.
        spreadsheetml.sheet",
      "lastModifiedDate": "2025-10-13T21:51:20.267Z"
    },
    {
      "type": "file",
      "name": "PaymentReceipt.png",
      "id": "36756",
      "parentId": "73783",
      "mimeType": "image/png",
      "lastModifiedDate": "2025-10-13T21:51:20.267Z"
    }
  ]
}
```

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `results` | `Object[]` | Required | An array of files and folders on the cloud storage system whose names match the search string in the request.  **Note:** Only files within the 25 MB size limit should be returned. |
| `results.type` | `String` | Required | Valid values:   - `folder` - `file` |
| `results.name` | `String` | Required | The file or folder name. Agreement Manager displays the `name` value on the **Select Files** window.  Names can be up to 254 characters long. |
| `results.id` | `String` | Required | The file or folder ID.  If a Agreement Manager user selects a folder to drill down in the cloud storage structure, the `id` of the selected folder will be passed as the `parentId` in the next **List Directory Contents** request.  If a Agreement Manager user selects a file for upload, the `id` of the selected file will be sent to the external service in the [Get File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file) request. |
| `results.parentId` | `String` | Required | The ID of the folder in which the file or folder is located. For a top-level folder, use the drive ID or `root` if the extension app does not implement **List Drives**. |
| `results.mimeType` | `String` | Required for files only | For a file, populate the MIME type. It must be one of the supported MIME types provided in the [Search request body](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#search-request-body). Agreement Manager displays the file type on the **Select Files** window.  For a folder, omit this property. |
| `results.lastModifiedDate` | `String` | Required for files only | For a file, populate the date-time when the file was last modified in this ISO 8601 UTC format:   ``` YYYY-MM-DDTHH:mm:ss.SSSZ ```  For example:   ``` 2025-10-13T00:00:00.000Z ```  Navigator displays the last modified date on the **Select Files** window.  For a folder, omit this property. |

## Error handling

In general, the external system should return a 200 response code to Docusign if a request succeeded. For a [success response](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file-synchronous-response-to-docusign) to an initial **Get File** request, a 202 response code should be used. Any other response code indicates that the request was not successfully executed.

This applies to all actions and capabilities. Developers are responsible for providing a code and message for each error.

## Next steps

- Get an [overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/) of the file input cloud storage extension and how it can be used.
- Explore the options for [testing](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) a file input cloud storage extension.
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
