---
title: Apply custom branding
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/apply-custom-branding/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Apply custom branding
scraped_at: '2026-06-18T19:46:29Z'
---

# Apply custom branding

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

Web Forms support the use of [branding](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/branding/) for [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) and their associated [envelopes](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes). Branding enables you to modify the logos and colors displayed in form instances and envelopes. It also enables you to customize envelope behavior. For example, you can set the URL to which users are routed after completing an envelope. Any brand defined in your Docusign account can be applied at the [web form configuration level](https://developers.docusign.com/docs/web-forms-api/plan-integration/apply-custom-branding/#apply-a-brand-to-a-web-form-configuration) or the [web form instance level](https://developers.docusign.com/docs/web-forms-api/plan-integration/apply-custom-branding/#apply-a-brand-when-creating-a-web-form-instance). See the Docusign account administration [Brands](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=lfr1583277366660.html) guide for details about how to define brands.

## Visual customizations

If a brand is applied, web form instances and envelopes display visual customizations in various locations. Expand each section below for an example.

## Advanced brand configuration options

If a brand includes advanced configuration options, such as destination URLs to which users are routed after signing an envelope, those settings will be applied to the web form instance flow. See [Advanced Configuration for Signing Brands﻿](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=cno1583277333030.html) for details about these settings.

## Apply a brand to a web form configuration

When you apply a brand to a web form configuration, it will be used for all web form instances created from the configuration, unless the brand is overridden when [creating a web form instance](https://developers.docusign.com/docs/web-forms-api/plan-integration/apply-custom-branding/#apply-a-brand-when-creating-a-web-form-instance). The options to apply a brand to a configuration are:

- [Create a web form configuration](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=euk1665093155272.html) from an eSignature template that has a brand selected. See [Set Advanced Options for an Envelope or Template](https://support.docusign.com/s/document-item?bundleId=gbo1643332197980&topicId=pbj1578456352875.html)﻿ for details about selecting a brand for a template. When this option is used, the brand is applied to both web form instances and envelopes. This option is available only for template-based web form configurations.
- Edit the web form configurationʼs [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates) in the Web Forms builder and select **Advanced Options** to select a brand. See [The Signature Page﻿](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) for details about how to access a web form template. Selecting a brand in a web form template affects envelopes only, not web form instances. This option is available only for template-based web form configurations.
- [Edit a web form configuration](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=zqg1667509078130.html) and select **Branding** on the Preview tab (shown below) to select a brand. Selecting a brand in the web form configuration affects web form instances, but not envelopes. A brand can be applied in this manner to both standalone and template-based web form configurations.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='805' width='1600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Web form configuration branding setting](https://images.ctfassets.net/aj9z008chlq0/7r7EBmvC83xmarQEw8IsKz/19fc727ab60df2cb76cd2247de61c985/WebFormConfigBrandingButton.png?w=1600&h=805&q=50&fm=png)

## Apply a brand when creating a web form instance

To apply a brand during web form instance creation, include a `brandId` property in the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call. A brand selected via this method applies to both web form instances and envelopes. A brand specified in the `Instances:createInstance` request overrides any brand applied at the web form configuration level. 

**Note:** Applying a brand via an API request is not supported for web form instances created from [standalone](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/#instance-processing-standalone-web-form-configurations) web form configurations.

To obtain a brandʼs ID, you can do either of the following:

- Send an eSignature API [AccountBrands:list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/list/) request to retrieve details about all brands in your account.
- Locate the brand on the eSignature Admin [Brands](https://admindemo.docusign.com/authenticate?goTo=brands) page and select **Edit**. The brand detail page displays the brand ID.

Below is an example request with a `brandId`.

```
{
  "sendOption": "now",
  "brandId": "75f4513d-xxxx-xxxx-xxxx-0c988eeb463c",
  "formValues": {
    "salary": 121800.55,
    "birth_date": "1980-12-18",
    "marital_status": "single",
    "education": "advanced",
    "alerts": ["Funds_withdrawn","Account_info_changed"]
  },
  "expirationOffset": 720,
  "recipients": [
    {
      "roleName": "signer1",
      "name": "Sally Signer",
      "email": "sally.signer@email.com"
    },
    {
      "roleName": "signer2",
      "name": "Steven Signer",
      "email": "steven.signer@email.com"
    }
  ]
}
```

## Next steps

- See [Web Forms concepts](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/) for more information about web form configurations, instances, and related components.
- See [When to use embedded or remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/) for an overview of the differences between delivery methods.

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
