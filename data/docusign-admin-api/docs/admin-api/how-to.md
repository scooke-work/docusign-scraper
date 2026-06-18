---
title: How-to guides overview
source_url: https://developers.docusign.com/docs/admin-api/how-to/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- How-to guides
scraped_at: '2026-06-18T20:12:04Z'
---

# How-to guides overview

The how-to guides in this section demonstrate how common [Docusign Admin](https://developers.docusign.com/docs/admin-api/admin101/) scenarios work and how you can implement them into your own apps.

**Note**: Although the authentication process to obtain an access token is the same for both eSignature REST and other Docusign APIs, you must request a different set of scopes during that process to call other Docusign API endpoints. See  [Authenticating with the Docusign Admin API](https://developers.docusign.com/docs/admin-api/admin101/auth/)  for details.

All API how-to guides assume you are developing with a Docusign developer account. A developer account is not specific to the [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/). If you have a developer account that you are using with our eSignature REST API, it will also work with other [Docusign APIs](https://developers.docusign.com/docs/). If you need to create a free developer account, select **Developer Account** from the menu at the top-right of the page, then **Create Account** or use the button below.

[Create account](https://www.docusign.com/developers/sandbox)

Each Admin API how-to guide is listed below:

|  |  |
| --- | --- |
| **How-to guide** | **Code example source** |
| [How to create a new active eSignature user](https://developers.docusign.com/docs/admin-api/how-to/create-active-user/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg001CreateNewUserWithActiveStatus.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/CreateUser.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/examples/A001AddActiveUser.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/createUser.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/CreateNewUserService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg001CreateNewUserWithActiveStatus.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg001_create_a_new_user.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg001_create_user_service.rb) |
| [How to create a new active user for CLM and eSignature](https://developers.docusign.com/docs/admin-api/how-to/create-active-clm-esign-user/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg002CreateActiveCLMESignUser.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/CreateCLMESignUser.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/CreateActiveCLMESignUserService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/createCLMESignUser.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/CreateActiveCLMESignUserService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg002CreateActiveCLMEsignUser.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg002_create_active_clm_esign_user.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg002_create_active_clm_esign_user_service.rb) |
| [How to bulk export user data](https://developers.docusign.com/docs/admin-api/how-to/bulk-export-users/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg003BulkExportUserData.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/BulkExportUserData.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/BulkExportUserDataService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/bulkExportUserData.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/BulkExportUserDataService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg003BulkExportUserData.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg003_bulk_export_user_data.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg003_bulk_export_user_data_service.rb) |
| [How to add users via bulk import](https://developers.docusign.com/docs/admin-api/how-to/add-users-bulk-import/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg004AddUsersViaBulkImport.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/ImportUser.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/BulkImportUserDataService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/importUser.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/BulkImportUserDataService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg004AddUsersViaBulkImport.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg004_add_users_via_bulk_import.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg004_import_user_service.rb) |
| [How to audit users](https://developers.docusign.com/docs/admin-api/how-to/audit-users/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg005AuditUsers.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/AuditUsers.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/AuditUsersService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/auditUsers.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/AuditUsersService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg005AuditUsers.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg005_audit_users.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg005_audit_users_service.rb) |
| [How to retrieve the user's Docusign profile using an email address](https://developers.docusign.com/docs/admin-api/how-to/retrieve-docusign-profile-using-email/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg006RetrieveDocuSignProfileByEmailAddress.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/RetrieveDocuSignProfileByEmailAddress.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/examples/A006RetrieveDocuSignProfileByEmailAddress.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/getUserProfileByEmail.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/RetrieveDocuSignProfileByEmailAddress.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg006GetUserProfileByEmail.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg006_get_user_profile_by_email.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg006_get_user_profile_by_email_service.rb) |
| [How to retrieve the user's Docusign profile using a User ID](https://developers.docusign.com/docs/admin-api/how-to/retrieve-docusign-profile-using-userid/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg007RetrieveDocuSignProfileByUserId.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/RetrieveDocuSignProfileByUserId.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/examples/A007RetrieveDocuSignProfileByUserID.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/getUserProfileByUserId.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/RetrieveDocuSignProfileByUserId.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg007GetUserProfileByUserId.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg007_get_user_profile_by_user_id.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg007_get_user_profile_by_user_id_service.rb) |
| [How to update user product permission profiles using an email address](https://developers.docusign.com/docs/admin-api/how-to/update-user-product-permission-profiles-using-email/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg008UpdateUserProductPermissionProfile.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/UpdateUserProductPermissionProfileByEmail.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/UpdateUserProductPermissionProfileByEmail.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/updateUserProductPermissionProfile.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/UpdateUserProductPermissionProfileByEmailService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg008UpdateUserProductPermissionProfile.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg008_update_user_product_permission_profile.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg008_update_user_product_permission_profile_service.rb) |
| [How to delete user product permission profiles using an email address](https://developers.docusign.com/docs/admin-api/how-to/delete-user-product-permission-profiles-using-email/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg009DeleteUserProductPermissionProfile.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/DeleteUserProductPermissionProfileById.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/DeleteUserProductPermissionProfileById.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/deleteUserProductPermissionProfile.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/DeleteUserProductPermissionProfileByIdService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg009DeleteUserProductPermissionProfile.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg009_delete_user_product_permission_profile.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg009_delete_user_product_permission_profile_service.rb) |
| [How to delete user data from an account as an account admin](https://developers.docusign.com/docs/admin-api/how-to/account-admin-delete-user-data/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg011DeleteUserDataFromAccount.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/DeleteUserDataFromAccount.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/examples/A011DeleteUserDataFromAccount.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/deleteUserDataFromAccount.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/DeleteUserDataFromAccountService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg011DeleteUserDataFromAccount.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg011_delete_user_data_from_account.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg011_delete_user_data_from_account_service.rb) |
| [How to delete user data from one or more accounts as an organization admin](https://developers.docusign.com/docs/admin-api/how-to/org-admin-delete-user-data/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg010DeleteUserDataFromOrganization.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/DeleteUserDataFromOrganization.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/examples/A010DeleteUserDataFromOrganization.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/deleteUserDataFromOrganization.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/DeleteUserDataFromOrganizationService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg010DeleteUserDataFromOrganization.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg010_delete_user_data_from_organization.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg010_delete_user_data_from_organization_service.rb) |
| [How to clone an account](https://developers.docusign.com/docs/admin-api/how-to/clone-account/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg012CloneAccount.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/CloneAccount.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/CloneAccountService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/cloneAccount.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/CloneAccountService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg012CloneAccount.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg012_clone_account.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg012_clone_account_service.rb) |
| [How to create an account](https://developers.docusign.com/docs/admin-api/how-to/create-account/) | [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg013CreateAccount.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/CreateAccount.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/CreateAccountService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/createAccount.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/CreateAccountService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg013CreateAccount.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg013_create_account.py), [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg013_create_account_service.rb) |

## Next steps

- See [Go-Live](https://developers.docusign.com/docs/admin-api/go-live/) to find the base path for Docusign Admin API calls in the production environment.
- Learn [How to create a new active eSignature user](https://developers.docusign.com/docs/admin-api/how-to/create-active-user/) for details on how to create a new active organization user.
- See [How to bulk export user data](https://developers.docusign.com/docs/admin-api/how-to/bulk-export-users/) for details on how to use bulk export to create or update large numbers of user accounts within an organization or to verify your account users and their permissions.
- Learn [How to add users via bulk import](https://developers.docusign.com/docs/admin-api/how-to/add-users-bulk-import/) to see how to use bulk import operations to create and update large numbers of users across all accounts in your organization simultaneously.

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
