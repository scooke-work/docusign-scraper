---
title: Workspaces API concepts
source_url: https://developers.docusign.com/docs/workspaces-api/workspaces101/concepts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Workspaces API
- Workspaces API
- API 101
- API 101
- Concepts
scraped_at: '2026-06-18T19:36:44Z'
---

# Workspaces API concepts

The following sections describe the objects and key terms used by Docusign Workspaces API.

### Workspaces

Docusign Workspaces is a single, digital place to bring people, agreements, and information together. 

It simplifies customer experience by providing end users with a consolidated view of all forms, documents, and tasks related to a particular agreement process. A workspace provides a central place to track and manage every detail, task, and agreement document. Workspaces enable you to streamline complex agreements that include multiple parties, documents, and stages.

### Envelopes

An *envelope* is a container for a Docusign agreement. An [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) object contains:

- One or more documents that will be sent for electronic signature
- Information about the sender
- Information about the recipients, including authentication requirements and the areas where they need to provide input
- The content of the email notification that recipients receive
- Status information that tracks delivery and signature progress

Envelopes are used to secure agreements in a workspace just as they are used generally through the eSignature API.

To use envelopes within a workspace, for the initial release of Workspaces API, you must create envelopes in a workspace using a [Workspaces API call](https://developers.docusign.com/docs/workspaces-api/reference/workspaces/workspaces/createworkspaceenvelope/), then modify the envelope using the eSignature REST API. Full import functionality is planned to be added in a future release. See [How to send an envelope with recipient info](https://developers.docusign.com/docs/workspaces-api/how-to/send-envelope-with-recipient-information/) for a detailed walkthrough. **Note**: SMS, WhatsApp, and fax delivery are not available for envelopes you send from Workspaces.

### Users

*Users* are individuals who are invited to collaborate together in a workspace for an agreement. Users must be assigned a role as either a **manage** or **participate** user.

### Roles and permission levels

A *role* defines a set of permissions that are applied to users in a workspace. Roles are defined as either **internal** or **external**: internal users are users on the same account as the person who created the workspace. All other users are external. Users can have one of two permission levels:

- **Manage users:** Manage users can view all documents in the workspace, view completed envelopes, add and share documents, and invite other collaborators. The **Manage permission can only be assigned to internal users**. To have this role, users must be on the same account as the person who created the workspace.
- **Participate users:** Participate users can view and complete agreement steps assigned to them. All external users must be assigned this permission level, but you can also optionally assign it to internal users as well.

Within these permission level categories, you can assign users a specific role:

- **Workspaces owner**: The creator of the workspace.
- **Internal invitee**: An individual invited to the workspace who is a member of the same Docusign account as the Workspaces owner.
- **External invitee**: An individual invited to the workspace who is not a member of the same Docusign account as the Workspaces owner.
- **Internal or external non-invitee**: Individual who is not invited to a workspace but is associated with the tasks or documents within the workspace. For example, an individual that is assigned an upload request.

See [Actions Permitted By Permission Level and Role﻿](https://support.docusign.com/s/document-item?language=en_US&bundleId=bmb1723842049882&topicId=oiu1731179949375.html) for details and a full matrix of which actions are permitted for each role.

You can update a user’s role by calling the [WorkspaceUsers: updateWorkspaceUser](https://developers.docusign.com/docs/workspaces-api/reference/workspaces/workspaceusers/updateworkspaceuser/) API endpoint.

### Documents

A *document* contains the content for a recipient to review or sign. Docusign supports documents in a variety of file formats, including PDF, Word, and HTML. A document object also contains metadata such as the file extension, file name, and document ID. 

Documents in the context of Workspaces API behave just like documents do for eSignature. Users with the appropriate permissions can add documents to a room and share them with other users.

## Next steps

- See [How to add a document to workspace](https://developers.docusign.com/docs/workspaces-api/how-to/add-a-document/) using the API.
- Learn about [Workspaces API concepts](https://developers.docusign.com/docs/workspaces-api/workspaces101/concepts/) and terms.
- Learn about [Workspaces API rules and resource limits](https://developers.docusign.com/docs/workspaces-api/rules-and-resource-limits/)

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
