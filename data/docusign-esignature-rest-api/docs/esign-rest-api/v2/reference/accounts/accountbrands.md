---
title: AccountBrands Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/
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
- Accounts
- Accounts
- Accountbrands
scraped_at: '2026-06-18T21:10:36Z'
---

# AccountBrands Resource

The AcccountBrands resource provides methods that allow you to create and delete the account brand associated with an account.

Branding allows you to add the look and feel of your organization's
brand to the sending, signing, and email process making it easier for users to identify envelopes coming from your organization.

The DocuSign Account Custom Branding feature lets you set the colors, logo, and text for your account. You can create any number of brand profiles with different settings to reflect each of your corporate brands or different internal divisions or departments.

When you create or change a branding profile, it applies to everyone using that profile and affects all envelopes sent with that profile.

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/create/) | POST  ```  /restapi/v2/accounts/{accountId}/brands ```  Creates one or more brand profile files for the account. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/delete/) | DEL  ```  /restapi/v2/accounts/{accountId}/brands/{brandId} ```  Removes a brand. |
| [deleteList](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/deletelist/) | DEL  ```  /restapi/v2/accounts/{accountId}/brands ```  Deletes one or more brand profiles. |
| [deleteLogo](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/deletelogo/) | DEL  ```  /restapi/v2/accounts/{accountId}/brands/{brandId}/logos/{logoType} ```  Delete one branding logo. |
| [get](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/get/) | GET  ```  /restapi/v2/accounts/{accountId}/brands/{brandId} ```  Get information for a specific brand. |
| [getExportFile](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/getexportfile/) | GET  ```  /restapi/v2/accounts/{accountId}/brands/{brandId}/file ```  Export a specific brand. |
| [getLogo](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/getlogo/) | GET  ```  /restapi/v2/accounts/{accountId}/brands/{brandId}/logos/{logoType} ```  Obtains the specified image for a brand. |
| [getResource](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/getresource/) | GET  ```  /restapi/v2/accounts/{accountId}/brands/{brandId}/resources/{resourceContentType} ```  Returns the specified branding resource file. |
| [list](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/list/) | GET  ```  /restapi/v2/accounts/{accountId}/brands ```  Gets a list of brand profiles. |
| [listResources](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/listresources/) | GET  ```  /restapi/v2/accounts/{accountId}/brands/{brandId}/resources ```  Returns the specified account's list of branding resources (metadata). |
| [update](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/update/) | PUT  ```  /restapi/v2/accounts/{accountId}/brands/{brandId} ```  Updates an existing brand. |
| [updateLogo](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/updatelogo/) | PUT  ```  /restapi/v2/accounts/{accountId}/brands/{brandId}/logos/{logoType} ```  Put one branding logo. |
| [updateResource](https://developers.docusign.com/docs/esign-rest-api/v2/reference/accounts/accountbrands/updateresource/) | PUT  ```  /restapi/v2/accounts/{accountId}/brands/{brandId}/resources/{resourceContentType} ```  Uploads a branding resource file. |

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
