---
title: Elastic signing concepts
source_url: https://developers.docusign.com/docs/click-api/click101/concepts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Click API
- Click API
- API 101
- API 101
- Concepts
scraped_at: '2026-06-18T22:18:19Z'
---

# Elastic signing concepts

This page describes the basic concepts used in elastic signing.

## Elastic templates

The Click API is built around a core object called an *elastic template*. An elastic template is an iframe that displays your terms to your customers for them to review and accept. You can display an elastic template as a modal (a window positioned over your page), or inline as part of your page.

An elastic template may record agreements from multiple users. Each time a new user accepts the elastic template, that user agreement is stored with the elastic template object.

## Elastic template versions

Docusign automatically versions your elastic templates. The first elastic template you create becomes version 1 (**V1.0**). Updating an elastic template automatically creates a new version (**V2.0**, and so on). You can configure your elastic template settings to prompt users to agree to the updated terms the next time they log in.

The version number for each elastic template displays in the **Version** column on your dashboard in the UI, as shown in the following image:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='410' width='1093' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![The My Elastic Templates page displays the version number of each of your elastic templates.](https://images.ctfassets.net/aj9z008chlq0/24WfOHKlqAhpXuEHWXOjba/39a5a61399c1de62d8fcad8edb372423/Clickwrap_versions_image.png?w=1093&h=410&q=50&fm=png)

An elastic template can have any number of versions. When you edit an elastic template, you can choose to edit an existing [draft](https://developers.docusign.com/docs/click-api/click101/managing-elastic-templates/#draft-elastic-templates) of that template or, if your chosen template does not already have a draft, one will be created for you automatically. If you save your changes without activating, the draft will be saved and your changes will persist to the next time you choose to edit the elastic template. Only the most recent version of the elastic template can be active.

## Client ID

When you create an agreement from elastic template, you specify a `clientUserId` that uniquely identifies the agreement's user. This value can be any identifier that your own system uses to track individual users. Examples include employee IDs, email addresses, and surrogate key values. The Click API uses this identifier in combination with other information to determine whether a user has already accepted the agreement, and also to report on user responses.

## Next steps

- [Click API 101](https://developers.docusign.com/docs/click-api/click101/)
- [Rules and resource limits](https://developers.docusign.com/docs/click-api/click101/rules-and-limits/)

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
