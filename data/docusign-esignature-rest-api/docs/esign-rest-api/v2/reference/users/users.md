---
title: Users Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- V2
- V2
- API Reference
- API Reference
- Users
- Users
- Users
scraped_at: '2026-06-18T21:10:58Z'
---

# Users Resource

The Users resource provides methods that allow you to manage users for an account. The "title" field in the Users object – used in the Users:create, delete, deleteProfile Image, get, getProfileImage, getSettings, list, update, updateList, updateProfileImage, updateSettings calls is not used. Instead, the user's job title may be retrieved and set using the UserProfiles: get and update methods. See [UserProfiles](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/userprofiles/) for more information.

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/create/) | POST  ```  /restapi/v2/accounts/{accountId}/users ```  Adds news user to the specified account. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/delete/) | DEL  ```  /restapi/v2/accounts/{accountId}/users ```  Removes users account privileges. |
| [deleteProfileImage](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/deleteprofileimage/) | DEL  ```  /restapi/v2/accounts/{accountId}/users/{userId}/profile/image ```  Deletes the user profile image for the specified user. |
| [get](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/get/) | GET  ```  /restapi/v2/accounts/{accountId}/users/{userId} ```  Gets the user information for a specified user. |
| [getProfileImage](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/getprofileimage/) | GET  ```  /restapi/v2/accounts/{accountId}/users/{userId}/profile/image ```  Retrieves the user profile image for the specified user. |
| [getSettings](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/getsettings/) | GET  ```  /restapi/v2/accounts/{accountId}/users/{userId}/settings ```  Gets the user account settings for a specified user. |
| [list](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/list/) | GET  ```  /restapi/v2/accounts/{accountId}/users ```  Retrieves the list of users for the specified account. |
| [update](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/update/) | PUT  ```  /restapi/v2/accounts/{accountId}/users/{userId} ```  Updates the specified user information. |
| [updateList](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/updatelist/) | PUT  ```  /restapi/v2/accounts/{accountId}/users ```  Change one or more user in the specified account. |
| [updateProfileImage](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/updateprofileimage/) | PUT  ```  /restapi/v2/accounts/{accountId}/users/{userId}/profile/image ```  Updates the user profile image for a specified user. |
| [updateSettings](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/updatesettings/) | PUT  ```  /restapi/v2/accounts/{accountId}/users/{userId}/settings ```  Updates the user account settings for a specified user. |

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
