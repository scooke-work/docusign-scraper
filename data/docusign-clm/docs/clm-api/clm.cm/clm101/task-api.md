---
title: Task API
source_url: https://developers.docusign.com/docs/clm-api/clm.cm/clm101/task-api/
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
- Task Api
scraped_at: '2026-06-18T21:48:56Z'
---

# Task API

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

As the name implies the [Task API](https://apidocsna11.springcm.com/apidocs#taskapi) exposes Docusign CLM services as tasks that can be executed and monitored programmatically. The Task API includes methods for document generation, document manipulation, advanced search and other long running document operations.

## Using the Task API

Tasks are asynchronous and are invoked and monitored in the following way:

1. A POST request is made passing a Task object to the corresponding Task endpoint to initiate a task operation. There is a specific task object that corresponds to each task operation endpoint and the properties of the task objects will vary significantly depending on the operation being invoked. Generally, only a subset of the properties of a Task are required to invoke the operation.
2. A result object is returned for any Task initiation POST request. The result objects will vary based on the Task being invoked, however result objects have some commonalities:
   1. An **Href** property that contains a URI that will uniquely identify the task invocation. A GET request can be made to this URI to get the status of the task operation and retrieve the results. For a longer running task, GETs to this URI can be periodically polled to get the current status and results of the task operation.
   2. The **Status** parameter that indicates the state or result of the operation. Statuses for most tasks include: Processing, Success, and Failure. Some tasks may have specialized statuses, see the [Task API](https://apidocsna11.springcm.com/apidocs#taskapi) documentation for more information.
   3. Result properties that will vary based on the task.
3. Some tasks will allow the operation to be canceled. This is done via a DELETE request to the task URI.

> **Note:** Although Docusign CLM’s Advanced Workflow engine is a long running series of tasks, it is not exposed via the Task API. The engine’s workflows, work items, and queues are considered objects and are exposed in the Object API as opposed to the Task API.

## Document search tasks

The examples to the right show an example request and response for an operation to find documents whose name contains "Contract".

1

2

3

4

5

6

7

headers: Accept: 'application/json'

uri: https://apina11.springcm.com/v201411/

documentsearchtasks

method: POST

json:

{

"Title":"Contract"

}

## Copy document tasks

The examples to the right show sample requests and responses for initiating and checking the status of a copy document operation.

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

headers: Accept: 'application/json'

uri: https://apina11.springcm.com/v201411/copytasks

method: POST

json:

{

"DocumentsToCopy": [

{

"Href": "https://apina11.springcm.com/v201411/

documents/e0db92b0-xxxx-xxxx-xxxx-3863bb335c14"

}

],

"DestinationFolder": {

"Href": "https://apina11.springcm.com/v201411/

folders/16caaf38-xxxx-xxxx-xxxx-001cc448da6a"

}

}

## Document generation tasks

Many of the task operations will result in a new document being created. For these tasks, there are two options for how the resulting document is handled.

The examples to the right show sample requests and responses for initiating and checking the status of a merge document operation.

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

headers: Accept: 'application/json'

uri: https://apina11.springcm.com/v201411/

documentmergetasks

method: POST

json:

{

"DocumentsToMerge": [

{

"Href": "https://apiqana11.springcm.com/

v201411/documents/

ac0de547-xxxx-xxxx-xxxx-3863bb335c14"

},

{

"Href": "https://apiqana11.springcm.com/

v201411/documents/

b11b6fc3-xxxx-xxxx-xxxx-3863bb335c14"

}

],

"DeleteOriginals": true,

"DestinationFolder": {

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
