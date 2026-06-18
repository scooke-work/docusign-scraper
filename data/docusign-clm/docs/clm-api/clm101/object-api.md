---
title: Object API
source_url: https://developers.docusign.com/docs/clm-api/clm101/object-api/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- API 101
- API 101
- Object Api
scraped_at: '2026-06-18T21:48:55Z'
---

# Object API

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

The CLM Object API exposes create, read, update, and delete (CRUD) actions for items that are commonly used in the Docusign CLM web application. JSON is the supported format for requests and responses.

## HTTP methods

The following HTTP methods are exposed in the API, though not all methods are exposed for all objects:

- **GET**: Retrieves the standard JSON representation of an object. You can request additional data about the object or its child objects by using the `expand` query string parameter.
- **POST**: Creates a new object in Docusign CLM.
- **DELETE**: Deletes an object from Docusign CLM. You can also use this method for a logical delete, such as aborting a running workflow.
- **PATCH**: Makes a partial update to an object.
- **PUT**: Fully replaces the representation of an object. This method is used sparingly in the API. In most cases, a PUT call will also make a partial update.

See the [API reference](https://developers.docusign.com/docs/clm-api/reference/) for a list of objects and the methods you can use with them.

### Methods for member objects

The CLM API only exposes read-only methods for members (or users). See the [API reference](https://developers.docusign.com/docs/clm-api/reference/) for details. Operations for managing members are available through the [Docusign Admin API](https://developers.docusign.com/docs/admin-api/).

### Methods for group objects

The [CLM API](https://developers.docusign.com/docs/clm-api/reference/) exposes the following methods for groups:

- Read-only endpoints for getting information about groups. You manage groups through the [Docusign Admin](https://www.docusign.com/products/admin) application.
- A separate set of endpoints for performing CRUD operations on mailing lists.

## Navigating the API

Each object in the API has a unique URI that is specified by its `Href` property. When an object contains child objects, the API returns the URIs for those child objects, rather than the full child objects themselves. You can then retrieve a child object by making a GET request to its URI. This approach enhances API performance.

For example, the following document object contains core properties, as well as properties that contain references to child objects. Note that the full folder object is not returned in the `ParentFolder` property. Instead, this property contains an `Href` property specifying the unique URI to the folder.

You can retrieve the parent folder of this document by making a GET request to the URI in this `ParentFolder.Href` property. This approach enables dynamic discovery, enables you to navigate the API via the `Href` properties, and removes the need to perform client-side string manipulation to create URIs for child resources.

**Example document object**

```
{

  "Name": "Company ABC Contract.pdf",

  "CreatedDate": "2015-04-21T15:54:28.653Z",

  "CreatedBy": "example@springcm.com",

  "UpdatedDate": "2015-05-03T17:59:35.41Z",

  "UpdatedBy": "example@springcm.com",

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

  "Href": "https://apiqana11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14"

}
```

In some instances, a URI may be a template containing placeholders for which you must provide values. In these instances, the API will create the URI using the URI Template standard as documented by [RFC 6570](https://tools.ietf.org/html/rfc6570). The following example shows the URI to which you can POST a document to upload it to Docusign CLM. Note that you must append the name of the document to the query string where the placeholder appears when you make the POST request.

**Example URI template**

```
https://apiuploadna11.springcm.com/v2/folders/7506bd38-xxxx-xxxx-xxxx-001cc448da6a/documents{?name}
```

### Retrieving parent and child objects in one request

There might be times when you want to retrieve the full child objects of a parent object in your request. This approach can increase performance because only a single request is made to the server to retrieve the objects the application needs.

To do this, specify that you want to expand the parent folder by adding `expand=parentfolder` to the query string when you make a GET request for the document. The response will include the full folder object, as shown in the following example.

**Example document object with the parent folder expanded**

```
{

  "Name": "Company ABC Contract.pdf",

  "CreatedDate": "2015-04-21T15:54:28.653Z",

  "CreatedBy": "example@springcm.com",

  "UpdatedDate": "2015-05-03T17:59:35.41Z",

  "UpdatedBy": "example@springcm.com",

  "Description": "",

  "ParentFolder": {

    "Name": "Admin",

    "CreatedDate": "2010-02-24T05:34:21.893Z",

    "CreatedBy": "example@springcm.com",

    "UpdatedDate": "2010-02-24T05:34:25.487Z",

    "UpdatedBy": "example@springcm.com",

    "Description": "",

    "ParentFolder": {

      "Href": "https://apina11.springcm.com/v2/folders/1a5eaa38-xxxx-xxxx-xxxx-001cc448da6a"

    },

    "BrowseDocumentsUrl": "https://na11.springcm.com/atlas/Link/Folder/6410/7506bd38-xxxx-xxxx-xxxx-001cc448da6a",

    "AccessLevel": {

      "See": true,

      "Read": true,

      "Write": true,

      "Move": true,

      "Create": true,

      "SetAccess": true

    },

    "Documents": {

      "Href": "https://apina11.springcm.com/v2/folders/7506bd38-xxxx-xxxx-xxxx-001cc448da6a/documents"

    },

    "Folders": {

      "Href": "https://apina11.springcm.com/v2/folders/7506bd38-xxxx-xxxx-xxxx-001cc448da6a/folders"

    },

    "ShareLinks": {

      "Href": "https://apina11.springcm.com/v2/folders/7506bd38-xxxx-xxx-xxxx-001cc448da6a/sharelinks"

    },

    "CreateDocumentHref": "https://apiuploadna11.springcm.com/v2/folders/7506bd38-4e91-df11-9372-001cc448da6a/documents{?name}",

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

}
```

You can expand multiple child objects in a single GET request. For example, if you want to return both the parent folder and the history item collection for a document, you can specify those properties in a comma-separated list in the `expand` parameter:

`expand=parentfolder,historyitems`

Note that expansion only goes one level deep, and therefore generally applies only to the parent object. You must request a child object directly to expand its child objects.

See the method-level documentation for the full list of expandable properties for each object.

### More about child objects

Child objects can only be addressed in the context of their parent objects. For example, document history items always belong to a parent document and must always be retrieved or expanded in the scope of the parent document. The API does not expose methods for querying, filtering, and sorting history items across multiple documents in a single call.

## API collections: Pagination, filtering and sorting

A property of an object will often contain a collection of child or related objects. An API collection always contains the same types of objects and has a common set of properties:

- `Items` (array): An array of API objects.
- `Href` (string): The URI for the current collection. You can use this URI to retrieve the collection at any time.
- `Offset` (integer): The number of elements in the collection to skip when retrieving the collection. The default offset is zero.
- `Limit` (integer): The maximum number of elements retrieved per request. The default limit is 20, and the maximum limit is 100.
- `First` (string): The URI of the first page of the collection.
- `Previous` (string): The URI of the previous page of the collection.
- `Next` (string): The URI of the next page of the collection.
- `Last` (string): The URI of the last page of the collection.
- `Total` (integer): The total number of elements in the collection.

### Pagination

When there are more items in the collection than the specified `Limit`, your application can page through the collection, retrieving the objects in chunks by specifying the `limit` and/or `offset` in the query string when it requests the collection. You can also navigate through the collection by creating the URIs for the **first**, **previous**, **next**, and **last** pages in the collection. To do this, append the appropriate `limit` and `offset` to the URI, then make a GET request to the URI.

### Filtering and sorting

In addition to navigation, API collections support filtering and sorting via query string parameters.

#### Filtering

To use a filter, you specify name-value pairs in the `filter` query parameter.

Filters return partial matches by default. (To get an exact match, in the `pageSortParams` parameter, set `FilterExact` to `true`.) For example, to see all of the users that viewed a document, you can filter on the **Preview Mode** action when requesting the history item collection for a document. Because filters do partial actions by default, you can specify:

`filter=action=preview`

**Note**: The equals sign is not URL-encoded when specifying the name-value pairs.

To use multiple filters, pass in a comma-separated set of filter values to the `filter` parameter. For example, to find out how many times the user with the email address **bob@springcm.com** previewed a particular document, you could further refine the filter:

```
filter=action=preview,useremail=bob@springcm.com
```

#### Sorting

You can also sort API collections by using these parameters:

- `sortproperty`: Specifies the collection property on which you want to sort the collection.
- `sortdirection`: Specifies the order in which to sort the collection. The possible values are `asc` (ascending) and `desc` (descending).

For example, to sort the history item collection by created date in descending order (with the most recently created one first), you would add the following to the query string when you make the GET request to the history item collection URI:

```
sortproperty=createddate&sortdirection=desc
```

You can only use certain API object properties to filter and sort collections. The **Object Model** section in the [API reference](https://developers.docusign.com/docs/clm-api/reference/) for an object method specifies which properties are filterable and sortable for an object.

**Example API collection of history items**

```
{

  "Items": [

    {

      "UserEmail": "example@springcm.com",

      "Action": "Document Added",

      "User": {

        "Href": "https://apina11.springcm.com/v2/users/77126573-xxxx-xxxx-xxxx-001cc448da6a"

      },

      "CreatedDate": "2015-04-21T15:54:28.847Z"

    },

    {

      "UserEmail": "bob@springcm.com",

      "Action": "Preview Mode",

      "User": {

        "Href": "https://apina11.springcm.com/v2/users/77126573-xxxx-xxxx-xxxx-001cc448da6a"

      },

      "CreatedDate": "2015-04-21T15:54:31.23Z"

    },

    {

      "UserEmail": "example@springcm.com",

      "Action": "Download Document Native",

      "MoreInfo": "SpringCM Expense Report (Developer)",

      "User": {

        "Href": "https://apina11.springcm.com/v2/users/77126573-xxxx-xxxx-xxxx-001cc448da6a"

      },

      "CreatedDate": "2015-04-25T18:45:40.35Z"

    },

    {

      "UserEmail": "bob@springcm.com",

      "Action": "Download Document PDF",

      "MoreInfo": "SpringCM Expense Report (Developer)",

      "User": {

        "Href": "https://apina11.springcm.com/v2/users/77126573-xxxx-xxxx-xxxx-001cc448da6a"

      },

      "CreatedDate": "2015-04-25T18:47:02.813Z"

    },

    {

      "UserEmail": "example@springcm.com",

      "Action": "File Name Changed",

      "MoreInfo": "File name changed from: 'Company ABC Contract.pdf'",

      "User": {

        "Href": "https://apina11.springcm.com/v2/users/77126573-xxxx-xxxx-xxxx-001cc448da6a"

      },

      "CreatedDate": "2015-05-03T17:59:23.323Z"

    }

  ],

  "Href": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/historyitems",

  "Offset": 0,

  "Limit": 20,

  "First": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/historyitems",

  "Last": "https://apina11.springcm.com/v2/documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/historyitems",

  "Total": 5

}
```

Note that specifying `limit`, `offset`, `filter`, and `sort` parameters is only effective when working with the collection URI directly. When a collection is expanded on a parent object instead of accessed by its URI directly, the standard `limit` and `offset` are used and no filtering or sorting can be specified.

## Next steps

See the [API reference](https://developers.docusign.com/docs/clm-api/reference/) for a list of objects and the methods you can use with them.

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
