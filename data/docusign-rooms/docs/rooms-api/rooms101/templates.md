---
title: Using room templates and task lists
source_url: https://developers.docusign.com/docs/rooms-api/rooms101/templates/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- API 101
- API 101
- Templates
scraped_at: '2026-06-18T22:33:01Z'
---

# Using room templates and task lists

You can save time and simplify your company’s processes by using a *room template* and one or more *task lists* when you create a new room. For example, if your company has a common set of steps and requirements for each mortgage loan transaction, you could create a room template containing that common task list data and use it to pre-populate each new mortgage loan room. This would ensure that every time someone creates a mortgage loan transaction room, it would also include all of the required tasks.
Templates are created for one side of a transaction (if in [Rooms for Real Estate](https://www.docusign.com/products/rooms-for-real-estate?_gl=1*av7kpr*_gcl_au*MTk3ODAwMTU2NC4xNzY2MTc1ODQ3/)), are locked to a region/office, and may contain one or more task lists. The tasks defined in a task list hold the bulk of template data and can include:

- Due dates
- Required assignee actions and permissions associated with the task
- Descriptions of the documents associated with the task
- The roles which have actions associated with the task
- Reminders, and when they will be delivered

  **Note:** A single task list may be part of multiple templates, so long as they are set to the same region/office.

## Create a room from a template

Before creating a room from a template, you should first:

1. **Add a Task list**. Task lists contain one or more tasks that room members can complete. See [Create Task List Templates to Group Common Transaction Activities﻿](https://support.docusign.com/s/document-item?language=en_US&bundleId=clr1643042075783&topicId=lkn1572968392044.html&*LANG=enus&_gl=1*sy1ig8*_gcl_au*MTI0OTM5NDAwMi4xNzU4NzUwNzU4LjUyODkwODgzLjE3NjYwODM2MTMuMTc2NjA4MzYxMw..*FPAU*MTI0OTM5NDAwMi4xNzU4NzUwNzU4) for details on how to create a task list.
2. **Define a room template**, which contains your task list. See [Create Room Templates to Auto-Populate New Rooms With Task Lists](https://support.docusign.com/s/document-item?language=en_US&bundleId=hyt1643056100211&topicId=bir1572968393341.html&_LANG=enus&_gl=1*u4uc6o*_gcl_au*MTI0OTM5NDAwMi4xNzU4NzUwNzU4LjUyODkwODgzLjE3NjYwODM2MTMuMTc2NjA4MzYxMw..*FPAU*MTI0OTM5NDAwMi4xNzU4NzUwNzU4) for details on how to create a room template.

Once you have a template, you can use it to create a new room with the Rooms UI or the [Rooms:CreateRoom](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/createroom/) method. See [Create Room Templates to Auto-Populate New Rooms With Task List](https://support.docusign.com/s/document-item?language=en_US&_gl=1*2dduy3*_gcl_au*MTI0OTM5NDAwMi4xNzU4NzUwNzU4LjUyODkwODgzLjE3NjYwODM2MTMuMTc2NjA4MzYxMw..*FPAU*MTI0OTM5NDAwMi4xNzU4NzUwNzU4&bundleId=clr1643042075783&topicId=bir1572968393341.html&_LANG=enus) for details on how to create a room with a template using the UI.

To create a room from your template with the API [Rooms:CreateRoom](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/createroom/) method, you must provide the ID of the template to be used in the body of the request.
> **Note:** To find your API Account ID, log in to [eSignature Admin](https://admindemo.docusign.com/) and select **Apps and Keys** in the **Integrations** section of the left nav bar to open the **API and Integration Key Information** page. Your API Account ID is shown in the **My Account Information** section.

The following example API call demonstrates how to create a room from a previously defined template:
> **Note:** You can get the IDs of your templates by using the [RoomTemplates:GetRoomTemplates](https://developers.docusign.com/docs/rooms-api/reference/roomtemplates/roomtemplates/getroomtemplates/) method, which will return data about all of the room templates you can access.

These examples require the following data:

| Requirement | Description |
| --- | --- |
| {ACCESS\_TOKEN} | An access token with the Docusign `dtr.rooms.write` scope. See [Authentication](https://developers.docusign.com/docs/rooms-api/rooms101/auth/) for details on obtaining an access token. |
| `roleId` | The ID of the role assigned to the room owner. You can get the list of roles for your account using the [Roles:GetRoles](https://developers.docusign.com/docs/rooms-api/reference/roles/roles/getroles/) method. |
| `templateId` | The ID of a template belonging to your account. You can get the list of templates defined for your account using the [RoomTemplates:GetRoomTemplates](https://developers.docusign.com/docs/rooms-api/reference/roomtemplates/roomtemplates/getroomtemplates/) method. |
| `officeId` | The ID of an office belonging to your account. You can get the list of offices for your account using the [Offices:GetOffices](https://developers.docusign.com/docs/rooms-api/reference/offices/offices/getoffices/) method. |

See [how to create a Room with a template](https://developers.docusign.com/docs/rooms-api/how-to/create-room-with-template/) for a more detailed, in-depth code example demonstrating how to create a new room using a template in a variety of languages.

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

17

$headers = New-Object

"System.Collections.Generic.Dictionary[[String],

[String]]"

$headers.add("Authorization","Bearer {ACCESS\_TOKEN}")

$headers.add("Accept", "application/json")

$headers.add("Content-Type", "application/json")

$body = @"

{

"name": "Example Property 2818 SW Alaska St",

"roleId": 292949,

"templateId": 1140,

"transactionSideId": "listbuy",

"officeId": 11570

}

"@

$uri = "https://demo.rooms.docusign.com/restapi/v2/

accounts/{ACCOUNT\_ID}/rooms"

$result = Invoke-WebRequest -headers $headers -Uri

$uri -Method POST -Body $body

$result.Content

## Next steps

- [Create Task List Templates to Group Common Transaction Activities](https://support.docusign.com/s/document-item?language=en_US&bundleId=clr1643042075783&topicId=lkn1572968392044.html&*LANG=enus&_gl=1*1940b4v*_gcl_au*MTI0OTM5NDAwMi4xNzU4NzUwNzU4LjUyODkwODgzLjE3NjYwODM2MTMuMTc2NjA4MzYxMw..*FPAU*MTI0OTM5NDAwMi4xNzU4NzUwNzU4)
- [Create Room Templates to Auto-Populate New Rooms With Task Lists](https://support.docusign.com/s/document-item?language=en_US&bundleId=hyt1643056100211&topicId=bir1572968393341.html&_LANG=enus&_gl=1*u4uc6o*_gcl_au*MTI0OTM5NDAwMi4xNzU4NzUwNzU4LjUyODkwODgzLjE3NjYwODM2MTMuMTc2NjA4MzYxMw..*FPAU*MTI0OTM5NDAwMi4xNzU4NzUwNzU4)
- [Create Room Templates to Auto-Populate New Rooms With Task List](https://support.docusign.com/s/document-item?language=en_US&_gl=1*2dduy3*_gcl_au*MTI0OTM5NDAwMi4xNzU4NzUwNzU4LjUyODkwODgzLjE3NjYwODM2MTMuMTc2NjA4MzYxMw..*FPAU*MTI0OTM5NDAwMi4xNzU4NzUwNzU4&bundleId=clr1643042075783&topicId=bir1572968393341.html&_LANG=enus)
- [How to create a room with a template](https://developers.docusign.com/docs/rooms-api/how-to/create-room-with-template/)

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
