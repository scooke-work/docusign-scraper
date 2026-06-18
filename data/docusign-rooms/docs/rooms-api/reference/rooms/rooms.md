---
title: Rooms Resource
source_url: https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- API Reference
- API Reference
- Rooms
- Rooms
- Rooms
scraped_at: '2026-06-18T22:33:04Z'
---

# Rooms Resource

A room can hold documents, envelopes, a list of tasks comprising a workflow, and other related information. You can invite others to this space and assign them permissions on a per-room basis.

## Methods Supported

| Method | Description |
| --- | --- |
| [AddDocumentToRoom](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/adddocumenttoroom/) | POST  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/documents ```  Adds a document to a room. |
| [AddDocumentToRoomViaFileUpload](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/adddocumenttoroomviafileupload/) | POST  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/documents/contents ```  Uploads the contents of a file as a document to a room. |
| [AddFormToRoom](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/addformtoroom/) | POST  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/forms ```  Adds a form to a room. |
| [CreateRoom](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/createroom/) | POST  ```  /restapi/v2/accounts/{accountId}/rooms ```  Creates a room. |
| [CreateRoomEnvelope](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/createroomenvelope/) | POST  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/envelopes ```  Creates an envelope with the given documents. |
| [DeleteRoom](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/deleteroom/) | DEL  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId} ```  Deletes a room. |
| [GetAssignableRoles](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/getassignableroles/) | GET  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/assignable_roles ```  Gets assignable room-level roles in v6. |
| [GetDocuments](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/getdocuments/) | GET  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/documents ```  Gets a list of documents in a room. |
| [GetRoom](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/getroom/) | GET  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId} ```  Gets a room. |
| [GetRoomFieldData](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/getroomfielddata/) | GET  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/field_data ```  Gets a room's field data. |
| [GetRoomFieldSet](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/getroomfieldset/) | GET  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/field_set ```  Gets the field set for a room. |
| [GetRooms](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/getrooms/) | GET  ```  /restapi/v2/accounts/{accountId}/rooms ```  Returns a list of rooms. |
| [GetRoomUsers](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/getroomusers/) | GET  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/users ```  Gets a room's users. |
| [InviteUser](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/inviteuser/) | POST  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/users ```  Invites a user to a room. |
| [PutRoomUser](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/putroomuser/) | PUT  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/users/{userId} ```  Updates a room user. |
| [RestoreRoomUserAccess](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/restoreroomuseraccess/) | POST  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/users/{userId}/restore_access ```  Restores the specified user's access to the room. |
| [RevokeRoomUserAccess](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/revokeroomuseraccess/) | POST  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/users/{userId}/revoke_access ```  Revokes the specified user's access to the room. |
| [UpdatePicture](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/updatepicture/) | PUT  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/picture ```  Updates the picture for a room. |
| [UpdateRoomFieldData](https://developers.docusign.com/docs/rooms-api/reference/rooms/rooms/updateroomfielddata/) | PUT  ```  /restapi/v2/accounts/{accountId}/rooms/{roomId}/field_data ```  Updates a room's field data. |

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
