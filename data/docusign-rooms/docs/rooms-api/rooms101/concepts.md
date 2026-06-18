---
title: Rooms concepts
source_url: https://developers.docusign.com/docs/rooms-api/rooms101/concepts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- API 101
- API 101
- Concepts
scraped_at: '2026-06-18T22:33:01Z'
---

# Rooms concepts

The Docusign Rooms API is based around these objects:

- [Companies](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#companies): A company may contain regions and offices, and be associated with rooms, roles, and users. Docusign sets up your company in Rooms as part of the account activation process. Similar to eSignature, the first user on the account automatically has the Default Admin role for the company's Rooms account. This user's role can be changed at a later time.
- [Roles](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#roles): Roles define user permissions. When users are invited to join the company, they are assigned a role. Roles can be added, edited, and deleted by a user who has permission to do so.
- [Users](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#users): Individuals who are associated with your company or with a specific room.
- [Rooms](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#rooms): A room is a digital workspace that holds all of the documents, users, data, and other information associated with a transaction.
- [Transaction sides](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#transaction-sides): In Rooms for Real Estate, this is the part your company plays in the transaction, such as **buy** or **sell**.
- [Fieldsets](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#fieldsets): Preconfigured sets of data fields that appear on a room’s **Details** tab.
- [Documents](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#documents): A document in Rooms is similar to a document in eSignature. Rooms can hold documents that room users or other parties must sign.
- [Forms](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#forms): Common forms from relevant industry associations that Docusign makes available through integrated form libraries, or your own custom forms.
- [Room templates](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#room-templates): Creating a room from a room template enables users with the correct permissions to standardize rooms for common transactions. Room templates can be made available to the whole company or specific regions or offices.
- [Room task lists](https://developers.docusign.com/docs/rooms-api/rooms101/concepts/#room-task-lists): Importing a standardized task list into a new room enables users with the correct permissions to assign common tasks and make sure they’re completed before a transaction is closed out. Users with the correct permissions can create task list templates to standardize tasks, and make them available to the whole company or specific regions or offices.

## Companies

Docusign sets up your *company* in Rooms for you and assigns a Default Admin. That user can then add other admins, regions, offices, roles, and users who will use Rooms.

## Roles

A *role* defines a set of permissions. Roles are either internal or external. You assign external roles to people from outside your company when you invite them into a room. You can configure custom roles with permissions that make sense for your company.

Docusign also offers preconfigured roles. For example, real estate companies can use the Default Admin, Agent, and Transaction Coordinator roles. You can use them as they are, customize them, or create your own roles from scratch.

People inside your company can have different roles based on the rooms to which they are added. Each person has a default company role, but you can assign them lower or external room roles as necessary. Regardless of the person's default company role, what they can do in a room is entirely controlled by their role in that particular room.

An admin user must configure roles for your company by using either the [Roles:CreateRole](https://developers.docusign.com/docs/rooms-api/reference/roles/roles/createrole/) method or the UI before you can add users. To learn more about working with roles and the types of roles you can configure, see the [Roles category](https://developers.docusign.com/docs/rooms-api/reference/roles/) in the API reference and the [permissions reference](https://developers.docusign.com/docs/rooms-api/reference/roles/roles/createrole/#schema__roleforcreate_permissions).

## Users

*Users* are individuals who are invited to your company, or to a room. There are two types of users:

- **Company users:** Your organization’s internal staff. Company users can be added to specific regions and offices.
- **Room users:** Users who have been invited to a specific room, as well as the creator of the room. They can either be external or internal users. For example, you might invite an external real estate agent or buyer to a room.

## Rooms

A *room* is a secure workspace in the Docusign Agreement Cloud that's associated with a specific transaction. Rooms enable you to streamline complex agreements that include multiple parties, documents, and stages. To learn more about working with rooms, see:

- [How to create a room with data](https://developers.docusign.com/docs/rooms-api/how-to/create-room-with-data/)
- [How to create a room with a template](https://developers.docusign.com/docs/rooms-api/how-to/create-room-with-template/)
- [How to export data from a room](https://developers.docusign.com/docs/rooms-api/how-to/export-room-data/)
- [How to add forms to a room](https://developers.docusign.com/docs/rooms-api/how-to/add-form-to-room/)
- [How to get a room with filters](https://developers.docusign.com/docs/rooms-api/how-to/get-room-with-filters/)

## Transaction sides

A *transaction side* indicates a side of a real estate transaction, such as buy, sell, refinance, or both buy and sell. You need to specify a transaction side when you create a new room in Rooms for Real Estate.

## Fieldsets

A *fieldset* is a preconfigured set of fields that display on a room’s **Details** tab, such as **Contact Name** and **Phone**. You can even populate values for the fields at the time that you create a new room. You specify the fields and corresponding values in the `fieldData` object when you create the room. For more information, see [How to create a room with data](https://developers.docusign.com/docs/rooms-api/how-to/create-room-with-data/).

## Documents

Documents in Rooms are similar to documents in eSignature. Users with the appropriate permissions can add documents to a room. You can share documents with others in the room. Sharing is explicit, except in the case of certain permissions, such as when the **Automatically share documents in the room with other users from the same office** permission is set.

## Forms

If your organization uses Docusign forms, you can add standard association forms to a room. Docusign Rooms provides access to forms from industry associations, such as the Mainstreet Organization of Realtors, via integrated form libraries. These libraries enable you to add these forms to your rooms directly by using the Rooms API. For example, if you have the appropriate permissions, you can use the [Rooms:AddFormToRoom](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/addformtoroom/) method to add the form **Short Sale Supplement to Marketing Agreement.pdf** to a new room or room template for short sale transactions.

With the appropriate permissions, form administrators at your company can create form groups, or curated sets of forms gathered from the association form libraries to which Docusign provides access. Form groups enable agents to know which forms to add to rooms based on the type of transaction they are working on. When creating groups, administrators can make certain forms required to ensure compliance.

To learn more about working with forms, see:

- [Forms](https://developers.docusign.com/docs/rooms-api/rooms101/forms/)
- [Using forms in a room](https://developers.docusign.com/docs/rooms-api/rooms101/forms/using-forms-in-a-room/)
- [Managing forms](https://developers.docusign.com/docs/rooms-api/rooms101/forms/managing-forms-rooms/)
- [How to add forms to a room](https://developers.docusign.com/docs/rooms-api/how-to/add-form-to-room/)
- The [Forms category](https://developers.docusign.com/docs/rooms-api/reference/forms/) in the API reference

## Room templates

A *room template* holds room information and tasks for room participants. By specifying a template when you create a room, you can automatically import this data. You create room templates in the UI. To learn more, see [How to create a room with a template](https://developers.docusign.com/docs/rooms-api/how-to/create-room-with-template/).

## Room task lists

A *room task list* holds a checklist of steps for a common transaction type. By specifying a task list when you create a room, you standardize the tasks that must be completed for the transaction. The assignees must check the items off the list before a room can be closed.

## Next steps

- See the [How-to guides](https://developers.docusign.com/docs/rooms-api/how-to/) for code examples for common Rooms API scenarios.
- See the MyAPICalls sample app [Create a Room](https://myapicalls.sampleapps.docusign.com/scenario/8) scenario, which walks you through a sequence of API calls that define a role and then define a room associated with that role.

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
