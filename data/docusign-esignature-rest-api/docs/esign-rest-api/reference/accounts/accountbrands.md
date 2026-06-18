---
title: AccountBrands Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Accounts
- Accounts
- Accountbrands
scraped_at: '2026-06-18T20:28:20Z'
---

# AccountBrands Resource

The AcccountBrands resource provides methods that enable you to create and manage [brands](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/branding/) for an account.

Branding enables you to add the look and feel of your organization's brand to the sending, signing, and email processes, making it easier for recipients to identify envelopes coming from your organization.

The Docusign Account Custom Branding feature enables you to set the colors, logo, and text that recipients see at the account level. The settings associated with a brand are applied to all of the envelopes that use the brand. You can create multiple brand profiles for different corporate brands or internal departments.

**Note:** To use this resource, branding for either signing or sending must be enabled for the account (either `canSelfBrandSend`, `canSelfBrandSign`, or both of these account settings must be set to **true**).

### Next steps

- See [how to create a brand via the API](https://developers.docusign.com/docs/esign-rest-api/how-to/create-brand/).
- Learn [how to apply a brand to an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/apply-brand-to-envelope/).

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/brands ```  Creates one or more brand profiles for an account. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/delete/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId} ```  Deletes a brand. |
| [deleteList](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/deletelist/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/brands ```  Deletes one or more brand profiles. |
| [deleteLogo](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/deletelogo/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId}/logos/{logoType} ```  Deletes a brand logo. |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/get/) | GET  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId} ```  Gets information about a brand. |
| [getExportFile](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/getexportfile/) | GET  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId}/file ```  Exports a brand. |
| [getLogo](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/getlogo/) | GET  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId}/logos/{logoType} ```  Gets a brand logo. |
| [getResource](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/getresource/) | GET  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId}/resources/{resourceContentType} ```  Returns a branding resource file. |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/list/) | GET  ```  /restapi/v2.1/accounts/{accountId}/brands ```  Gets a list of brands. |
| [listResources](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/listresources/) | GET  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId}/resources ```  Returns metadata about the branding resources for an account. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId} ```  Updates an existing brand. |
| [updateLogo](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/updatelogo/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId}/logos/{logoType} ```  Updates a brand logo. |
| [updateResource](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/updateresource/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/brands/{brandId}/resources/{resourceContentType} ```  Updates a branding resource file. |

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
