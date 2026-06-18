---
title: PowerForms Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Powerforms
- Powerforms
- Powerforms
scraped_at: '2026-06-18T21:10:27Z'
---

# PowerForms Resource

PowerForms enable you to create self-service documents for signature. A PowerForm is an envelope initiated from a URL that you make available for signers to complete. You can either add a PowerForm to your website or email the URL to recipients. Docusign saves the data that recipients enter so you can easily integrate it with your other applications.

For more information, see [Using PowerForms](https://support.docusign.com/s/document-item?bundleId=jbx1643062255110&topicId=eke1578456649038.html).

**Note:** PowerForms are available only for Docusign Enterprise accounts.

### Errors

PowerForm methods return the following 404 errors:

- `PowerForms_Recipient_Denied_Documents`: The recipient is denied access to the documents.
- `PowerForms_DigitalCerts_Shared_Tabs_Not_Allowed`: Shared tags are not allowed because a digital certificate is required
  for a signer.
- `PowerForms_DigitalCerts_Free_Form_Tabs_Not_Allowed`: Signers that are required to use a digital certificate must have at
  least one required, non-conditional signature or initials tab.
- `PowerForms_DigitalCerts_Multiple_Recipients_Routing_Order`: Signers that are required to use a digital certificate must be the
  only recipient in a routing order. Edit the routing order or remove the digital certificate requirement.
- `PowerForms_DigitalCerts_Markup_Not_Allowed`: Document markup is not allowed because a digital certificate is
  required for a signer.
- `PowerForms_Incomplete_Recipient`: The recipient's username, email, or role is not set.
- `PowerForms_PowerFormId_Required`: A `powerFormId` is required.
- `PowerForms_PowerFormId_Mismatch`: A `powerFormId` mismatch has occurred.

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/powerforms ```  Creates a new PowerForm |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/delete/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/powerforms/{powerFormId} ```  Deletes a PowerForm. |
| [deleteList](https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/deletelist/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/powerforms ```  Deletes one or more PowerForms. |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/get/) | GET  ```  /restapi/v2.1/accounts/{accountId}/powerforms/{powerFormId} ```  Returns a single PowerForm. |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/list/) | GET  ```  /restapi/v2.1/accounts/{accountId}/powerforms ```  Returns a list of PowerForms. |
| [listSenders](https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/listsenders/) | GET  ```  /restapi/v2.1/accounts/{accountId}/powerforms/senders ```  Gets PowerForm senders. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/powerforms/{powerFormId} ```  Updates an existing PowerForm. |

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
