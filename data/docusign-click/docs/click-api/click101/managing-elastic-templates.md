---
title: Managing elastic templates
source_url: https://developers.docusign.com/docs/click-api/click101/managing-elastic-templates/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Click API
- Click API
- API 101
- API 101
- Managing Elastic Templates
scraped_at: '2026-06-18T22:18:19Z'
---

# Managing elastic templates

You can use the Click API to manage the different versions of your elastic templates, get a list of elastic templates, retrieve lists of users who have consented to your agreements, and more.

## Creating elastic templates

You can create an elastic template with the Click API, or you can generate one in the UI. For a detailed walkthrough of the process, see [How to create an elastic template](https://developers.docusign.com/docs/click-api/how-to/create-elastic-templates/).

## Activating elastic templates

New elastic templates are inactive by default. After you create a new elastic templates, you must activate it before you can use it. To learn how, see [How to activate an elastic template](https://developers.docusign.com/docs/click-api/how-to/activate-elastic-template/).

## Testing elastic templates

You can preview how an active elastic template appears and functions when embedded in a website by using the Docusign Elastic Template Tester. The elastic template must be active before you can test it. For details, see [How to test an elastic template](https://developers.docusign.com/docs/click-api/how-to/test-elastic-template/).

## Share elastic templates

Any users within your organization’s account can choose to share the elastic templates they have created. 

To share an elastic template, open the **Elastic Templates** tab on the **Templates** page. Find the row of the elastic template you want to share, then choose the drop-down icon to the right of the **Copy Code** button. In the drop down menu, choose **Share**, then choose **Share** again in the confirmation window.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='268' width='118' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Elastic template copy code dropdown image](https://images.ctfassets.net/aj9z008chlq0/2kbWW72Xfb83nXPhcBTduN/ae40f721d8efe2b28a0bfe74dd20e6b3/Screenshot_2025-01-02_at_2.19.06_PM.png?w=118&h=268&q=50&fm=png)

When an elastic template is shared, it becomes visible to the other users on your account in their **Shared with me** folder, under **Elastic Templates** on the left nav.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='248' width='205' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image of UI for sharing an elastic template](https://images.ctfassets.net/aj9z008chlq0/1RY5XcZipAfNgWB8ValiWo/5cf4424169488c337b19caacdaf96f0b/templatesShared.png?w=205&h=248&q=50&fm=png)

Other users can open, edit, and save their updates to your shared elastic template as **drafts**.

## Draft elastic templates

A *draft elastic template* is a set of updates to an existing elastic template that acts as a separate branch of the main elastic template from which it was created. A draft elastic template is created whenever you make and save updates to a elastic template without subsequently activating them.

The elastic template’s owner can choose to activate the draft at any time, merging it as a new version of the main elastic template. 

Only one draft version of each elastic template can exist at once; if another user opens the current draft and makes a new set of edits before saving, the previous draft will be overwritten.

When you create an elastic template without activating it using an API or SDK method, a successful response will contain a GUID `draftVersionId`. To activate a draft using the API, you must provide the value of this draft version ID as the `clickwrapId` parameter for the [ClickWraps:updateClickwrapVersion](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/updateclickwrapversion/) method call.

## Embedding agreements using elastic templates

After you have [created](https://developers.docusign.com/docs/click-api/how-to/create-elastic-templates/) and [activated](https://developers.docusign.com/docs/click-api/how-to/activate-elastic-template/) your elastic template, you can use it by:

- **Embedding an agreement directly into your website or application**.
  Once your elastic template looks and behaves the way you expect, you can embed an instance of it in your own website or app. You can obtain the JavaScript code you need to embed your elastic signing agreement in one of the following ways:
  1. Copying the embed code that's generated after you successfully test your elastic template by following the steps in [How to test an elastic template](https://developers.docusign.com/docs/click-api/how-to/test-elastic-template/).
  2. Writing a short piece of JavaScript code from scratch by following the steps in [How to embed an elastic signing agreement](https://developers.docusign.com/docs/click-api/how-to/embed-elastic-templates/).
  3. Copying the JavaScript code from the UI by logging in to your [developer environment](https://account-d.docusign.com/) or [production environment](https://apps.docusign.com/send/home) account, going to **Templates -> Elastic Templates**, and selecting **COPY CODE** from the drop-down list next to the elastic template.
  See [To get the code for an elastic template](https://support.docusign.com/s/document-item?bundleId=igo1666647424726&topicId=xmw1600983388178.html&_LANG=enus) in the Click API user guide for details on getting the code, and [How to embed an elastic signing agreement](https://developers.docusign.com/docs/click-api/how-to/embed-elastic-templates/) for details on how to embed the elastic template instance within your website or application.
- **Generating an agreement URL through the API.**You can create a specific agreement URL that contains the client user ID and document data to be agreed on by the signer using the [ClickWraps:createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/) endpoint. You can create the agreement URL through the API for use with either of the above methods, either by embedding with `agreementUrl` instead of `environment`, `accountId`, and `clickwrapId`, or by sending this URL directly to the user to sign.

> **Note:** For compatibility with previous versions of the Click API, elastic templates use clickwrap endpoints.

## Download the certificate of completion

A certificate of completion is a record that is created after each Docusign eSignature and elastic signing agreement. It provides a permanent record of each sender, signer, approver, and recipient.

When using the Click API, you can download this certificate after an agreement is completed by using the [ClickWraps:getAgreementPdf](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getagreementpdf/) endpoint and appending the query parameter `include_coc=true`.

For example:

```
GET /clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/agreements/{agreementId}?include_coc=true
```

You can get the agreement ID by:

- Looking at the body of the `onAgreed` [event callback](https://developers.docusign.com/docs/click-api/click101/callbacks/):

  ```
  docuSignClick.Clickwrap.render({ //... onAgreed: (agreementData) => { // agreementData.agreementId } }, '#host-element');
  ```
- Making a POST request to the [ClickWraps:createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/) endpoint, providing the `clientUserId` of the agreeing user as the value of the `accountId` parameter.

## Next steps

- See the [How-to guides](https://developers.docusign.com/docs/click-api/how-to/) for code examples for common elastic signing scenarios.
- See the MyAPICalls sample app [Create and Activate an Elastic Template](https://myapicalls.sampleapps.docusign.com/scenario/3) scenario, which walks you through a sequence of API calls that define an elastic template and then activate it.

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
