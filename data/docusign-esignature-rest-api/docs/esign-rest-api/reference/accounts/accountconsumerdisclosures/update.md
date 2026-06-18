---
title: ': update'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountconsumerdisclosures/update/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:10:04Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountconsumerdisclosures/update/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountconsumerdisclosures/update/?explorer=true)

[AccountConsumerDisclosures](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountconsumerdisclosures/)

# : update

Account administrators can use this method to perform the following tasks:

- Customize values in the default disclosure.
- Switch to a custom disclosure that uses your own text and HTML formatting.
- Change values in your existing consumer disclosure.

To specify the signer language version of the disclosure that you are updating, use the optional `langCode` query parameter.

**Note:** Only account administrators can use this method. Each time you change the disclosure content, all unsigned recipients of outstanding documents will be required to accept a new version.

## Updating the default disclosure

When you update the default disclosure, you can edit all properties except for the following ones:

- `accountEsignId`: This property is read-only.
- `custom`: The default value is **false.** Editing this property causes the default disclosure to switch to a custom disclosure.
- `esignAgreement`: This property is read-only.
- `esignText`: You cannot edit this property when `custom` is set to **false.** The API returns a 200 OK HTTP response, but does not update the `esignText`.
- Metadata properties: These properties are read-only.

**Note:** The text of the default disclosure is always in English.

## Switching to a custom disclosure

To switch to a custom disclosure, set the `custom` property to **true** and customize the value for the `eSignText` property.

You can also edit all of the other properties except for the following ones:

- `accountEsignId`: This property is read-only.
- `esignAgreement`: This property is read-only.
- Metadata properties: These properties are read-only.

**Note:** When you use a custom disclosure, you can create versions of it in different signer languages and se the `langCode` parameter to specify the signer language version that you are updating.

**Important:** When you switch from a default to a custom disclosure, note the following information:

- You will not be able to return to using the default disclosure.
- Only the disclosure for the currently selected signer language is saved. Docusign will not automatically translate your custom disclosure. You must create a disclosure for each language that your signers use.

## Updating a custom disclosure

When you update a custom disclosure, you can update all of the properties except for the following ones:

- `accountEsignId`: This property is read-only.
- `esignAgreement`: This property is read-only.
- Metadata properties: These properties are read-only.

**Important:** Only the disclosure for the currently selected signer language is saved. Docusign will not automatically translate your custom disclosure. You must create a disclosure for each language that your signers use.

## Request

#### HTTP Request

PUT

```
/restapi/v2.1/accounts/{accountId}/consumer_disclosure/{langCode}
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| langCode \* | string | The code for the signer language version of the disclosure that you want to update. The following languages are supported:   - Arabic (`ar`) - Bulgarian (`bg`) - Czech (`cs`) - Chinese Simplified (`zh_CN`) - Chinese Traditional (`zh_TW`) - Croatian (`hr`) - Danish (`da`) - Dutch (`nl`) - English US (`en`) - English UK (`en_GB`) - Estonian (`et`) - Farsi (`fa`) - Finnish (`fi`) - French (`fr`) - French Canadian (`fr_CA`) - German (`de`) - Greek (`el`) - Hebrew (`he`) - Hindi (`hi`) - Hungarian (`hu`) - Bahasa Indonesian (`id`) - Italian (`it`) - Japanese (`ja`) - Korean (`ko`) - Latvian (`lv`) - Lithuanian (`lt`) - Bahasa Melayu (`ms`) - Norwegian (`no`) - Polish (`pl`) - Portuguese (`pt`) - Portuguese Brazil (`pt_BR`) - Romanian (`ro`) - Russian (`ru`) - Serbian (`sr`) - Slovak (`sk`) - Slovenian (`sl`) - Spanish (`es`) - Spanish Latin America (`es_MX`) - Swedish (`sv`) - Thai (`th`) - Turkish (`tr`) - Ukrainian (`uk`) - Vietnamese (`vi`)   Additionally, you can automatically detect the browser language being used by the viewer and display the disclosure in that language by setting the value to `browser`. |

| Query Parameters |  |  |
| --- | --- | --- |
| include\_metadata | string | (Optional) When true, the response includes metadata indicating which properties are editable. |

\* Required

## SDK Method

### Accounts::updateConsumerDisclosure

## Request Body

## Responses

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
