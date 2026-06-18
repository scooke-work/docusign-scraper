---
title: Object API
source_url: https://developers.docusign.com/docs/clm-api/clm.cm/clm101/object-api/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- CLM.CM
- CLM.CM
- API 101
- API 101
- Object Api
scraped_at: '2026-06-18T21:48:56Z'
---

# Object API

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

The Object API exposes create, read, update, and delete actions for items that are commonly worked with in the Docusign CLM user interface. The objects are exposed using [RESTful](http://en.wikipedia.org/wiki/Representational_state_transfer) conventions and JSON is the supported Request/Response format.

The following operations HTTP methods are exposed in the API, though not all methods are exposed for all objects:

**GET** – Retrieve the standard data JSON representation of the current object. Additional data about the object or its child objects may be requested by using the **expand** query string parameter.
**POST** – Create a new item in Docusign CLM.
**DELETE** – Delete an item from Docusign CLM. This may include a logical delete, such as aborting a running workflow.
**PATCH** – Used to make partial updates to an object.
**PUT** – Used to fully replace the representation of an object. This is used sparingly in the API. In most cases, a call to PUT will also make a partial update.

See the [method level documentation](https://apidocsna11.springcm.com/apidocs#objectapi) for the list of objects and the methods that can be used with them.

## Navigating the API

All objects in the API are referenced by a unique URI and is specified by its **href** property. Objects can contain references to other objects which can be retrieved by calling a GET on that property. In the example below, the document object contains core properties as well as properties that contain references to a number of child objects. For example, looking at the property called **ParentFolder**, the full folder objects is not returned, it only contains the unique URI to the folder via its **href** property. This is done for performance reasons, as often the full set of child objects of a parent object are not always needed, but can be retrieved by the calling application when required. In this case, the parent folder of this document can be retrieved by make a **GET** request to the document’s **ParentFolder.href** property. In this way, the API enables dynamic discovery and can be navigated via the **href** properties and negates the need to do client side string manipulation to create URIs for child resources.

In some instances, a URI may be a template for a resource and need additional information by the calling application. In these instances, the API will create the URI using the URI Template standard as documented by RFC 6570 (link). The example below shows the URI to which a document can be POST’d to upload it to Docusign CLM. It shows that that name of the document must be appended to the query string when making the post.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

{

"Name": "Company ABC Contract.pdf",

"CreatedDate": "2015-04-21T15:54:28.653Z",

"CreatedBy": "klitwin@springcm.com",

"UpdatedDate": "2015-05-03T17:59:35.41Z",

"UpdatedBy": "klitwin@springcm.com",

"Description": "",

"ParentFolder":

{

"Href": "https://apina11.springcm.com/

v201411/folders/

7506bd38-xxxx-xxxx-xxxx-001cc448da6a"

},

"HistoryItems":

{

"Href": "https://apina11.springcm.com/

v201411/documents/

e0db92b0-xxxx-xxxx-xxxx-3863bb335c14/

historyitems"

},

## Sample URI template

```
https://apiuploadna11.springcm.com/v201411/
    folders/7506bd38-xxxx-xxxx-xxxx-001cc448da6a/documents{?name}
```

There are occasions where it may be desirable to retrieve the child objects of a parent object in a single request. This can actually increase performance as only a single request is made to the server to retrieve the objects needed by the application. Building on the previous example, assuming the application knows that it needs both the document and the parent folder objects, the parent folder property can be requested to be expanded when retrieving the document object. This is done by adding **expand=parentfolder** to the query string when making a GET request for the document. Instead of just the URI to the parent folder being returned, the full folder object will be returned as shown in the example JSON to the right.

Multiple child objects may be expanded on a single GET request. For example, if we wanted both the parent folder and history item collection returned for the document, the properties can be specified in a comma separated list to the **expand** parameter: **expand=parentfolder,historyitems.**

Note that expansion only goes one level deep, so generally only applies to the parent object. A child object must be directly requested to expand its child objects, etc.

See the [method level documentation](https://apidocsna11.springcm.com/apidocs) for the full list of expandable properties for each object.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

{

"Name": "Company ABC Contract.pdf",

"CreatedDate": "2015-04-21T15:54:28.

653Z",

"CreatedBy": "klitwin@springcm.com",

"UpdatedDate": "2015-05-03T17:59:35.

41Z",

"UpdatedBy": "klitwin@springcm.com",

"Description": "",

"ParentFolder": {

"Name": "Admin",

"CreatedDate": "2010-02-24T05:34:21.

893Z",

"CreatedBy": "klitwin@springcm.com",

"UpdatedDate": "2010-02-24T05:34:25.

487Z",

"UpdatedBy": "klitwin@springcm.com",

"Description": "",

"ParentFolder": {

"Href": "https://apina11.springcm.

## API Collections – Pagination, filtering, and sorting

Often a property of an object will contain a collection of child or related objects. An API Collection will always contain the same type of object and will have a common set of properties:

- **Items** – An array of API objects.
- **Href (string):** URI of the current collection. Can be used to retrieve the collection at any time.
- **Offset (integer):** The number of elements in the collection to skip when retrieving the collection. The default offset is zero.
- **Limit (integer):** The maximum number of elements retrieved per request. Default limit is 20. Maximum limit is 100
- **First (string):** URI of the first page of the collection.
- **Previous (string):** URI of the previous page of the collection.
- **Next (string):** URI of the next page of the collection.
- **Last (string):** URI of the last page of the collection.
- **Total (integer):** Total number of elements in the collection.

When there are more items in the collection than the specified limit, the application can page through the collection, retrieving the objects in chunks by specifying the **limit** and/or **offset** on the query string when the collection is requested. The **first, previous, next,** and **last** properties are added as a convenience by appending the appropriate **limit** and **offset** to the URI and a GET request can be done to this URIs specified by these properties to navigate the collection.

In addition to navigation, API collections support filtering and sorting via query string parameters. Filters are specified by specifying name value pairs to the **filter** parameter on the query string. Filters will do partial matches by default (double check this). For example, if wanted to see all of the users that had viewed a document, we could filter on the **Preview Mode** action when requesting the history item collection for a document. Since filters do partial actions by default we can specify **filter=action=preview** (note that the equals sign is not URL encoded when specifying the name value pairs). Multiple filters may be used by passing in a comma separated set of filters to the **filter\*\*** parameter. Building on this example, if we wanted to know how many times the user with email address **bob@springcm.com** previewed a particular document, we could further refine the filter: **filter=action=preview,useremail=bob@springcm.com.**

API Collections also support sorting via two parameters: **sortproperty** and **sortdirection.** The **sortproperty** parameter simply takes the collection property that should sorted on. The **sortdirection** will specify either **asc** or **desc** to specify if the collection should be sorted ascending or descending. For example, if we wanted to sort the history item collection by created date in descending order (most recent first), we would add the following to the query string when making a GET request to the history item collection URI: **sortproperty=createddate&sortdirection=desc.**

Only certain API object properties can be filtered and sorted upon. The **Object Model** section in the Object API documentation specified which properties are filterable and sortable for a given object.

Note that specifying limit, offset, filter, and sort parameters is only effective when working with the collection URI directly. When a collection is expanded on a parent object instead of accessed by its URI directly, the standard limit and offset will be used and no filtering or sorting can be specified.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

{

"Items": [

{

"UserEmail": "klitwin@springcm.com",

"Action": "Document Added",

"User": {

"Href": "https://apina11.springcm.com/

v201411/users/

77126573-xxxx-xxxx-xxxx-001cc448da6a"

},

"CreatedDate": "2015-04-21T15:54:28.847Z"

},

{

"UserEmail": "bob@springcm.com",

"Action": "Preview Mode",

"User": {

"Href": "https://apina11.springcm.com/

v201411/users/

77126573-xxxx-xxxx-xxxx-001cc448da6a"

},

## Child objects

Some API objects can only be addressed in the context of their parent objects. For example, document history items always belong to a parent document and must always be retrieved or expanded in the scope of the parent document. The API does not expose methods for querying, filtering and sorting history items across multiple documents in a single call.

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
