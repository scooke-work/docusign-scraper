---
title: Task API
source_url: https://developers.docusign.com/docs/clm-api/clm101/task-api/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- API 101
- API 101
- Task Api
scraped_at: '2026-06-18T21:48:55Z'
---

# Task API

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

The CLM Task API exposes Docusign CLM services as tasks that can be executed and monitored programmatically. It offers methods for generating documents, manipulating documents, advanced search, and other long-running document operations. JSON is the supported format for requests and responses.

Task API operations are based on a task object. However, the properties associated with the task object vary depending on the operation you are invoking. In general, you only need to include a subset of task properties to invoke a Task API method. See the [API reference](https://developers.docusign.com/docs/clm-api/reference/) for details.

## Using the Task API

Tasks are asynchronous, and are invoked and monitored in the following way:

1. To initiate a task operation, a POST request is made to a task endpoint. The request passes in a task object containing the subset of properties that the specific endpoint requires.
2. All POST requests to initiate a task will return a result object. The structure of the result object varies based on the task being invoked, but all result objects have some commonalities:
   1. An `Href` property that contains a URI that uniquely identifies the task invocation. You can make a GET request to this URI to check the status of the task and retrieve the results. For a longer-running task, you can periodically poll GET requests to this URI to check the current status and get the results of the task.
   2. A `Status` property that indicates the state or result of the operation. Statuses for most tasks include: `Processing`, `Success`, and `Failure`. Some tasks may also have specialized statuses. See the API reference for more information.
   3. Result properties that vary based on the task.
3. Some tasks allow you to cancel the operation. To cancel a task operation, make a DELETE request to the task URI.

**Note:** Although the Docusign CLM Advanced Workflow engine is a long-running series of tasks, it is not exposed via the Task API. The engine’s workflows, work items, and queues are considered objects and are exposed in the [Object API](https://developers.docusign.com/docs/clm-api/clm101/object-api/).

## Document search tasks

**Example search request for "Contract" in the document name**

Headers: `Accept: 'application/json'`

URI: `https://apina11.springcm.com/v2/documentsearchtasks`

Method: POST

JSON:

```
{
  "Title":"Contract"
}
```

**Example search response for "Contract" in the document name**

```
{
  "Status": "Success",
  "Result": {
    "Items": [
      {
        "Name": "Company ABC Contract.pdf",
        "CreatedDate": "2015-04-21T15:54:28.653Z",
        "CreatedBy": "klitwin@springcm.com",
        "UpdatedDate": "2015-05-03T17:59:35.41Z",
        "UpdatedBy": "klitwin@springcm.com",
        "Description": "",
        "ParentFolder": {
          "Href": "https://apina11.springcm.com/v2/folders/7506bd38-xxxx-xxxx-xxxx-001cc448da6a"
        },
        "HistoryItems": {
          "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/historyitems"
        },
        "AccessLevel": {
          "See": true,
          "Read": true,
          "Write": true,
          "Move": true,
          "Create": true,
          "SetAccess": true
        },
        "PageCount": 1,
        "Lock": {
          "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/lock"
        },
        "PreviewUrl": "https://na11.springcm.com/atlas/documents/preview.aspx?aid=6410&lduid=e0db92b0-xxxx-xxxx-xxxx-3863bb335c14",
        "Versions": {
          "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/versions"
        },
        "ShareLinks": {
          "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/sharelinks"
        },
        "DocumentProcessTrackingActivities": {
          "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/documentprocesstrackingactivities"
        },
        "DocumentReminders": {
          "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/documentreminders"
        },
        "DownloadDocumentHref": "https://apidownloadna11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14",
        "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14"
      },
      {
        "Name": "Company XYZ Contract.pdf",
        "CreatedDate": "2010-12-07T15:47:27.23Z",
        "CreatedBy": "example@springcm.com",
        "UpdatedDate": "2010-12-07T15:47:27.23Z",
        "UpdatedBy": "example@springcm.com",
        "Description": "",
        "ParentFolder": {
          "Href": "https://apina11.springcm.com/v2/folders/aea58e35-xxxx-xxxx-xxxx-001cc448e3c7"
        },
        "HistoryItems": {
          "Href": "https://apina11.springcm.com/v2/documents/c512034a-xxxx-xxxx-xxxx-001cc448e3c7/historyitems"
        },
        "AccessLevel": {
          "See": true,
          "Read": true,
          "Write": true,
          "Move": true,
          "Create": true,
          "SetAccess": true
        },
        "PageCount": 3,
        "Lock": {
          "Href": "https://apina11.springcm.com/v2/documents/c512034a-xxxx-xxxx-xxx-001cc448e3c7/lock"
        },
        "PreviewUrl": "https://na11.springcm.com/atlas/documents/preview.aspx?aid=6410&lduid=c512034a-xxxx-xxxx-xxxx-001cc448e3c7",
        "Versions": {
          "Href": "https://apina11.springcm.com/v2/documents/c512034a-xxxx-xxxx-xxxx-001cc448e3c7/versions"
        },
        "ShareLinks": {
          "Href": "https://apina11.springcm.com/v2/documents/c512034a-xxxx-xxxx-xxxx-001cc448e3c7/sharelinks"
        },
        "DocumentProcessTrackingActivities": {
          "Href": "https://apina11.springcm.com/v2/documents/c512034a-xxxx-xxxx-xxxx-001cc448e3c7/documentprocesstrackingactivities"
        },
        "DocumentReminders": {
          "Href": "https://apina11.springcm.com/v2/documents/c512034a-xxxx-xxxx-xxxx-001cc448e3c7/documentreminders"
        },
        "DownloadDocumentHref": "https://apidownloadna11.springcm.com/v2/documents/c512034a-xxxx-xxxx-xxxx-001cc448e3c7",
        "Href": "https://apina11.springcm.com/v2/documents/c512034a-xxxx-xxxx-xxxx-001cc448e3c7"
      }
    ],
    "Href": "https://apina11.springcm.com/v2/documentsearchtasks/1fe928eb-xxxx-xxxx-xxxx-fe2e229c77a6/Result",
    "Offset": 0,
    "Limit": 20,
    "First": "https://apina11.springcm.com/v2/documentsearchtasks/1fe928eb-xxxx-xxxx-xxxx-fe2e229c77a6/Result",
    "Last": "https://apina11.springcm.com/v2/documentsearchtasks/1fe928eb-xxxx-xxxx-xxxx-fe2e229c77a6/Result",
    "Total": 2
  },
  "Href": "https://apina11.springcm.com/v2/documentsearchtasks/1fe928eb-xxxx-xxxx-xxxx-fe2e229c77a6"
}
```

## Copy document tasks

**Example request for Initiate Copy**

Headers: `Accept: 'application/json'`

URI: `https://apina11.springcm.com/v2/copytasks`

Method: POST

JSON:

```
{
  "DocumentsToCopy": [
    {
      "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14"
    }
  ],
  "DestinationFolder": {
    "Href": "https://apina11.springcm.com/v2/folders/16caaf38-xxxx-xxxx-xxxx-001cc448da6a"
  }
}
```

**Example response for Initiate Copy**

```
{
  "Status": "Processing",
  "Href": "https://apina11.springcm.com/v2/copytasks/95a91709-4a73-xxxx-xxxx-11e18fd81b19"
}
```

**Example request for Check Status**

Headers: `Accept: 'application/json'`

URI: `https://apina11.springcm.com/v2/copytasks/95a91709-xxxx-xxxx-xxxx-11e18fd81b19`

Method: GET

**Example response for Check Status**

```
{
  "DocumentResults": [
    {
      "Href": "https://apina11.springcm.com/v2/documents/b11b6fc3-xxxx-xxxx-xxxx-3863bb335c14"
    }
  ],
  "FolderResults": [],
  "FailedDocuments": [],
  "FailedFolders": [],
  "Status": "Success",
  "Href": "https://apina11.springcm.com/v2/copytasks/95a91709-xxxx-xxxx-xxxx-11e18fd81b19"
}
```

## Document generation tasks

Many task operations create a new document. For these tasks, you can handle the resulting document in one of the following ways:

- To save the document in CLM, specify a `DestinationFolder` in your request object.
- Alternatively, some tasks allow you to create a temporary file that you can download, without saving it in CLM. To do this, omit the `DestinationFolder`. To determine which tasks allow you to create this temporary file, see the [API reference](https://developers.docusign.com/docs/clm-api/reference/).

The following examples of document generation tasks demonstrate the first option, in which you specify a `DestinationFolder` to save the resulting document in CLM.

**Merging PDFs: Example request to Initiate Merge**

Headers: `Accept: 'application/json'`

URI: `https://apina11.springcm.com/v2/documentmergetasks`

Method: POST

JSON:

```
{
  "DocumentsToMerge": [
    {
      "Href": "https://apiqana11.springcm.com/v2/documents/ac0de547-xxxx-xxxx-xxxx-3863bb335c14"
    },
    {
      "Href": "https://apiqana11.springcm.com/v2/documents/b11b6fc3-xxxx-xxxx-xxxx-3863bb335c14"
    }
  ],
  "DeleteOriginals": true,
  "DestinationFolder": {
    "Href": "https://apiqana11.springcm.com/v2/folders/16caaf38-xxxx-xxxx-xxxx-001cc448da6a"
  },
  "DestinationDocumentName": "Final Contract.pdf"
}
```

**Merging PDFs: Example response to Initiate Merge request**

```
{
"Status": "Processing",
"Href": "https://apina11.springcm.com/v2/documentmergetasks/e4b9ddcf-xxxx-xxxx-xxxx-687fa2c2f6f1"
}
```

**Merge Document Tasks - Check Status - Sample Request**

Headers: `Accept: 'application/json'`

URI: `https://apina11.springcm.com/v2/documentmergetasks/e4b9ddcf-xxxx-xxxx-xxxx-687fa2c2f6f1`

Method: GET

**Merge Document Tasks - Check Status - Sample Response**

```
{
  "ResultDocument": {
    "Name": "Final Contract.pdf",
    "CreatedDate": "2015-05-03T23:00:34.003Z",
    "CreatedBy": "klitwin@springcm.com",
    "UpdatedDate": "2015-05-03T23:00:34.003Z",
    "UpdatedBy": "klitwin@springcm.com",
    "Description": "",
    "ParentFolder": {
      "Href": "https://apina11.springcm.com/v2/folders/16caaf38-xxxx-xxxx-xxxx-001cc448da6a"
    },
    "HistoryItems": {
      "Href": "https://apina11.springcm.com/v2/documents/88ffac33-xxxx-xxxx-xxxx-3863bb335c14/historyitems"
    },
    "AccessLevel": {
      "See": true,
      "Read": true,
      "Write": true,
      "Move": true,
      "Create": true,
      "SetAccess": true
    },
    "PageCount": 2,
    "Lock": {
      "Href": "https://apina11.springcm.com/v2/documents/88ffac33-xxxx-xxxx-xxxx-3863bb335c14/lock"
    },
    "PreviewUrl": "https://na11.springcm.com/atlas/documents/preview.aspx?aid=6410&lduid=88ffac33-xxxx-xxxx-xxxx-3863bb335c14",
    "Versions": {
      "Href": "https://apina11.springcm.com/v2/documents/88ffac33-xxxx-xxxx-xxxx-3863bb335c14/versions"
    },
    "ShareLinks": {
      "Href": "https://apina11.springcm.com/v2/documents/88ffac33-xxxx-xxxx-xxxx-3863bb335c14/sharelinks"
    },
    "DocumentProcessTrackingActivities": {
      "Href": "https://apina11.springcm.com/v2/documents/88ffac33-xxxx-xxxx-xxxx-3863bb335c14/documentprocesstrackingactivities"
    },
    "DocumentReminders": {
      "Href": "https://apina11.springcm.com/v2/documents/88ffac33-xxxx-xxxx-xxxx-3863bb335c14/documentreminders"
    },
    "DownloadDocumentHref": "https://apidownloadna11.springcm.com/v2/documents/88ffac33-xxxx-xxxx-xxxx-3863bb335c14",
    "Href": "https://apina11.springcm.com/v2/documents/88ffac33-xxxx-xxxx-xxxx-3863bb335c14"
  },
  "Status": "Success",
  "Href": "https://apina11.springcm.com/v2/documentmergetasks/e4b9ddcf-xxxx-xxxx-xxxx-687fa2c2f6f1"
}
```

## Next steps

See the [API reference](https://developers.docusign.com/docs/clm-api/reference/) for a list of tasks and the methods you can use with them.

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
