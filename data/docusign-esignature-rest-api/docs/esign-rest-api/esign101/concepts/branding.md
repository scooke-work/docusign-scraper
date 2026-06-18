---
title: Branding
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/branding/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Branding
scraped_at: '2026-06-18T20:28:08Z'
---

# Branding

Expanded by eSignature REST API 2.1

You can customize the look and feel of the emails and envelopes that you send out for signature using the *branding* feature. Branding enables you to add visual elements, such logos and colors, to:

- Customize your app's signing experience
- Customize your app's sending experience
- Enforce brand consistency across your account

You can create multiple brands in your Docusign account to represent different corporate brands or internal departments (custom groups). You can also manage brand access for users in your account.

You can configure branding on the [Brands](https://admindemo.docusign.com/authenticate?goTo=brands) page of eSignature Admin or through the eSignature REST API [AccountBrands Resource](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/).

A brand is identified by its ID, which is a [GUID](http://guid.one/). You can reference this ID in API calls that update or retrieve information about a brand. To obtain a brand's ID, you can do either of the following:

- Send an [AccountBrands:list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/list/) request to retrieve details about all brands in your account.
- Locate the brand on the eSignature Admin [Brands](https://admindemo.docusign.com/authenticate?goTo=brands) page and select **Edit**. The brand detail page displays the brand ID.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='485' width='400' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![The eSignature Admin Brands page contains the brand ID](https://images.ctfassets.net/aj9z008chlq0/6IUs2cHLu3S8gIzkB7UZBv/500c610aefe55967a6084125ddad1a14/BrandID.png?w=400&h=485&q=50&fm=png)

## What you can set in a brand

Branding enables you to add your organization's visual identity to your integration's eSignature sending and signing views. This helps maintain a consistent user experience for your organization. **For the signing view, you can:**

- Set the colors of the UI
- Set a custom logo
- Set a new redirect URL for all branded envelopes
- Add your own set of header and footer links
- Set a default language and specify additional languages available to signers
- Update a resource file that controls text in emails and in the signing view

**For the sending view, you can:**

- Set the colors of the UI
- Set a custom logo
- Set footer links

**For brand management, you can:**

- Set your brand as the default used for all envelopes created by your account. You can also manually specify which brand to use each time you create a new envelope.
- Assign brands to one or more [Groups](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=pik1583277475390&topicId=cuv1583277363488.html&_LANG=enus) defined for your account. Only users who belong to a group that has been assigned a brand may use it, unless it is set as the default brand. See [Assign Brands to Groups](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=pik1583277475390&topicId=iby1583277366335.html&_LANG=enus) for details.

For more information on setting up brands, see [From the Trenches: Apply your brand to your Docusign emails](https://www.docusign.com/blog/developers/the-trenches-apply-your-brand-to-your-docusign-emails/) or try the [Government Sample App](https://government.sampleapps.docusign.com).

## Next steps

Working with brands? See code examples on:

- [How to create a brand](https://developers.docusign.com/docs/esign-rest-api/how-to/create-brand/)
- [How to apply a brand to an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/apply-brand-to-envelope/)
- [How to apply a brand and template to an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/apply-brand-and-template-to-envelope/)

See [AccountBrands Resource](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accountbrands/) for details about API requests related to brands.

See [Brands](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=lfr1583277366660.html) in the eSignature Admin Guide for details on working with brands using the UI.

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
