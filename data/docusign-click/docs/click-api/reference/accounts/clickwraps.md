---
title: ClickWraps Resource
source_url: https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Click API
- Click API
- API Reference
- API Reference
- Accounts
- Accounts
- Clickwraps
scraped_at: '2026-06-18T22:18:21Z'
---

# ClickWraps Resource

Methods for working with elastic templates and elastic signing agreements.

## Methods Supported

| Method | Description |
| --- | --- |
| [createBulkClickwrapAgreements](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createbulkclickwrapagreements/) | POST  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/bulk_agreements ```  Starts an export of clickwrap agreements for a specified date range. |
| [createClickwrap](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createclickwrap/) | POST  ```  /clickapi/v1/accounts/{accountId}/clickwraps ```  Creates an elastic template for an account. |
| [createClickwrapVersion](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createclickwrapversion/) | POST  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions ```  Creates a new elastic template version. |
| [createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/) | POST  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/agreements ```  Creates a unique URL for the agreement that you can embed in your application. |
| [deleteClickwrap](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/deleteclickwrap/) | DEL  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId} ```  Deletes an elastic template and all of its versions. |
| [deleteClickwraps](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/deleteclickwraps/) | DEL  ```  /clickapi/v1/accounts/{accountId}/clickwraps ```  Deletes elastic templates for an account. |
| [deleteClickwrapVersion](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/deleteclickwrapversion/) | DEL  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions/{versionId} ```  Deletes an elastic template version by version ID. |
| [deleteClickwrapVersions](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/deleteclickwrapversions/) | DEL  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions ```  Deletes the versions of an elastic template. |
| [getAgreement](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getagreement/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/agreements/{agreementId} ```  Gets a specific agreement for a specified elastic template. |
| [getAgreementDocument](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getagreementdocument/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions/{versionId}/documents/{orderOrDisclosure} ```  Downloads a document at an order within the agreement. |
| [getAgreementPdf](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getagreementpdf/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/agreements/{agreementId}/download ```  Gets the completed user agreement PDF. |
| [getClickwrap](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwrap/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId} ```  Gets a single elastic template object. |
| [getClickwrapAgreements](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwrapagreements/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/users ```  Get elastic signing agreements. |
| [getClickwraps](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwraps/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps ```  Gets all the elastic templates for a user. |
| [getClickwrapVersion](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwrapversion/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions/{versionId} ```  Gets a specific version of an elastic template by version ID. |
| [getClickwrapVersionAgreements](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwrapversionagreements/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions/{versionId}/users ```  Gets the agreement responses for an elastic template version by version ID. |
| [getClickwrapVersions](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwrapversions/) | GET  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions ```  Gets all the versions of an elastic template. |
| [getServiceInformation](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getserviceinformation/) | GET  ```  /clickapi/service_information ```  Gets the current version and other information about the Click API. |
| [updateClickwrap](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/updateclickwrap/) | PUT  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId} ```  Update properties of an elastic template. |
| [updateClickwrapVersion](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/updateclickwrapversion/) | PUT  ```  /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions/{versionId} ```  Update properties of an elastic template by its version ID. |

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
