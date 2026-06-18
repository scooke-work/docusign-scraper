---
title: Forms Category
source_url: https://developers.docusign.com/docs/rooms-api/reference/forms/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- API Reference
- API Reference
- Forms
scraped_at: '2026-06-18T22:33:03Z'
---

# Forms Category

## Form groups

With the appropriate permissions, form administrators at your company can create form groups, or curated set of forms gathered from the association **form libraries** to which Docusign provides access. Form groups enable agents to know which forms to add to rooms based on the type of transaction they are working on. When creating groups, administrators can make certain forms required, ensuring compliance. If you don't create groups, agents will have to choose forms they need from a list of association forms.

## Permissions

To manage forms, you must have the `canManageFormGroups` permission, which enables you to access the **Forms** tab in **Admin.** For all other roles, assign permissions based on how these users will be working with forms. If no form permissions are enabled for these roles, users cannot add forms to rooms.

Form administrators must have the `canManageFormGroups` permission assigned to their user role. This gives them access to the **Forms** tab in **Admin.** However, you should also consider the user's access level. For example, if the user has access to specific offices, they can only administer form groups for those offices.

[ExternalFormFillSessions](https://developers.docusign.com/docs/rooms-api/reference/forms/externalformfillsessions/)

Description

This resource provides a method that returns a URL for a new external form fill session, based on the `roomId` and `formId` that you specify in the `formFillSessionForCreate` request body.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [CreateExternalFormFillSession](https://developers.docusign.com/docs/rooms-api/reference/forms/externalformfillsessions/createexternalformfillsession/) |  |  |

[FormDetails](https://developers.docusign.com/docs/rooms-api/reference/forms/formdetails/)

Description

This resource contains details about a form, such as the date it was created and last updated, the number of pages, the form owner, and other information.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [GetFormDetails](https://developers.docusign.com/docs/rooms-api/reference/forms/formdetails/getformdetails/) |  |  |

[FormGroups](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/)

Description

The `FormGroups` resource enables you to create and manage custom groups of association forms.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [AssignFormGroupForm](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/assignformgroupform/) | [CreateFormGroup](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/createformgroup/) | [DeleteFormGroup](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/deleteformgroup/) |
| [GetFormGroup](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/getformgroup/) | [GetFormGroupForms](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/getformgroupforms/) | [GetFormGroups](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/getformgroups/) |
| [GrantOfficeAccessToFormGroup](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/grantofficeaccesstoformgroup/) | [RemoveFormGroupForm](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/removeformgroupform/) | [RenameFormGroup](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/renameformgroup/) |
| [RevokeOfficeAccessFromFormGroup](https://developers.docusign.com/docs/rooms-api/reference/forms/formgroups/revokeofficeaccessfromformgroup/) |  |  |

[FormLibraries](https://developers.docusign.com/docs/rooms-api/reference/forms/formlibraries/)

Description

The `FormLibraries` resource enables you to access standard real estate industry association forms and add them to rooms.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [GetFormLibraries](https://developers.docusign.com/docs/rooms-api/reference/forms/formlibraries/getformlibraries/) | [GetFormLibraryForms](https://developers.docusign.com/docs/rooms-api/reference/forms/formlibraries/getformlibraryforms/) |  |

[FormProviders](https://developers.docusign.com/docs/rooms-api/reference/forms/formproviders/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [GetFormProviderAssociations](https://developers.docusign.com/docs/rooms-api/reference/forms/formproviders/getformproviderassociations/) |  |  |

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
