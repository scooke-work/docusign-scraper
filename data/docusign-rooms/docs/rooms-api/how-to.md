---
title: How-to guides overview
source_url: https://developers.docusign.com/docs/rooms-api/how-to/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- How-to guides
scraped_at: '2026-06-18T22:33:01Z'
---

# How-to guides overview

The how-to guides in this section demonstrate how common [Docusign Rooms](https://developers.docusign.com/docs/rooms-api/rooms101/) scenarios work and how you can implement them in your own apps.

**Note**: Although the authentication process to obtain an access token is the same for both eSignature REST and other Docusign APIs, you must request a different set of scopes during that process to call other Docusign API endpoints. See [Rooms API authentication](https://developers.docusign.com/docs/rooms-api/rooms101/auth/) for details.

All API how-to guides assume you are developing with a Docusign developer account. A developer account is not specific to the [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/). If you have a developer account that you are using with our eSignature REST API, it will also work with other [Docusign APIs](https://developers.docusign.com/docs/). If you need to create a free developer account, select **Developer Account** from the menu at the top-right of the page, then **Create Account** or use the button below.

[Create account](https://www.docusign.com/developers/sandbox)

After you obtain your developer account, you will need to contact [Docusign Support](https://support.docusign.com/s/contactSupport) to enable Docusign Rooms for your developer account. Once enabled, you will need to link the Docusign eSignature account to your newly created Docusign Rooms account by logging into it from your Docusign developer account. At that point, you will be ready to use Docusign Rooms and its API. For complete instructions on setting up your accounts, see [Create a Rooms developer account](https://developers.docusign.com/docs/rooms-api/rooms101/create-account/).

Each Rooms API how-to guide is listed below:

| **How-to guide** | **Code example source** |
| --- | --- |
| [How to create a room with data](https://developers.docusign.com/docs/rooms-api/how-to/create-room-with-data/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg001CreateRoomWithDataController.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/CreateRoomWithData.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/examples/R001ControllerCreateRoom.java), [Node](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/createRoomWithData.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/CreateRoomsWithDataService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg001CreateRoomWithDataController.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg001_create_room_with_data.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/room_api/eg001_create_room_with_data_service.rb) |
| [How to create a room with a template](https://developers.docusign.com/docs/rooms-api/how-to/create-room-with-template/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg002CreateRoomWithTemplateController.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/CreateRoomFromTemplate.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/services/CreateRoomWithTemplateService.java), [Node](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/createRoomFromTemplate.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/CreateRoomWithTemplatesService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg002CreateRoomWithTemplateController.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg002_create_room_with_template.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/room_api/eg002_create_room_with_template_service.rb) |
| [How to export data from a room](https://developers.docusign.com/docs/rooms-api/how-to/export-room-data/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg003ExportDataFromRoomController.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/ExportDataFromRoom.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/examples/R003ControllerExportingDataFromRoom.java), [Node](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/exportDataFromRoom.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/ExportDataFromRoomService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg003ExportDataFromRoomController.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg003_export_data_from_room.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/room_api/eg003_export_data_from_room_service.rb) |
| [How to add forms to a room](https://developers.docusign.com/docs/rooms-api/how-to/add-form-to-room/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg004AddFormsToRoomController.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/AddingFormToRoom.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/examples/R004ControllerAddingFormsToRoom.java), [Node](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/addingFormToRoom.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/AddFormsToRoomService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg004AddFormsToRoomController.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg004_add_forms_to_room.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/main/app/services/room_api/eg004_add_forms_to_room_service.rb) |
| [How to get a room with filters](https://developers.docusign.com/docs/rooms-api/how-to/get-room-with-filters/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg005GetRoomsWithFiltersController.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/GetRoomsWithFilters.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/examples/R005ControllerGetRoomsWithFilters.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/getRoomsWithFilters.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/GetRoomsWithFiltersService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg005GetRoomsWithFiltersController.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg005_get_rooms_with_filters.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/room_api/eg005_get_rooms_with_filters_service.rb) |
| [How to create an external form fillable session](https://developers.docusign.com/docs/rooms-api/how-to/external-form-fill/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg006CreateAnExternalFormFillSessionController.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/CreateExternalFormFillSession.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/examples/R006ControllerCreateExternalFormFillSession.java), [Node](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/createExternalFormFillSession.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/CreateExternalFormFillSessionService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg006CreateAnExternalFormFillSessionController.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg006_create_external_form_fill_session.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/room_api/eg006_create_an_external_form_fill_session_service.rb) |
| [How to create a form group](https://developers.docusign.com/docs/rooms-api/how-to/create-form-group/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg007CreateFormGroup.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/CreateFormGroups.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/examples/R007ControllerCreateFormGroup.java), [Node](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/createFormGroup.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/CreateFormGroupService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg007CreateFormGroup.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg007_create_form_group.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/main/app/services/room_api/eg007_create_form_group_service.rb) |
| [How to grant office access to a form group](https://developers.docusign.com/docs/rooms-api/how-to/access-form-group/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg008AccessFormGroup.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/GrantOfficeAccessToFormGroup.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/examples/R008ControllerGrantOfficeAccessToFormGroup.java), [Node](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/grantOfficeAccessToFormGroup.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/GrantOfficeAccessToFormGroupService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg008AccessFormGroup.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg008_grant_office_access_to_form_group.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/main/app/services/room_api/eg008_grant_office_access_to_form_group_service.rb) |
| [How to assign a form to a form group](https://developers.docusign.com/docs/rooms-api/how-to/assign-form-group/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Rooms/eg009AssignFormGroup.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Rooms/Examples/AssignFormToFormGroups.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/rooms/examples/R009ControllerAssignFormToFormGroup.java), [Node](https://github.com/docusign/code-examples-node/blob/master/lib/rooms/examples/assignFormToFormGroup.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Rooms/AssignFormToFormGroupService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Rooms/eg009AssignFormGroup.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/rooms/examples/eg009_assign_form_to_form_group.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/main/app/services/room_api/eg009_assign_form_to_form_group_service.rb) |

## Next steps

- See [Go-Live](https://developers.docusign.com/docs/rooms-api/go-live/) to find the base path for API calls in the production environment.
- Learn about [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) and how you can use it to quickly set up and run API code examples.

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
