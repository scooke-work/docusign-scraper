---
title: Managing forms
source_url: https://developers.docusign.com/docs/rooms-api/rooms101/forms/managing-forms-rooms/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- API 101
- API 101
- Forms
- Forms
- Managing forms
scraped_at: '2026-06-18T22:33:02Z'
---

# Managing forms

*Forms* are standard preset documents imported to your company’s Rooms account for easy reuse.

**Note:** Forms is a Rooms for Real Estate feature. There is no comparable feature in Rooms for Mortgage.

## Managing forms access

Forms access policies and Forms Groups are created and managed by forms administrators. A user must have the **rooms\_forms** permission assigned to their user to become a forms administrator; this gives them access to the **FORMS** tab in the Rooms admin panel.

**Note:** Form access is office-specific. If a member has access only to specific offices, they can only administer form groups for those offices. During the process of setting up the Forms feature, you can set a different permission, "Manage form libraries," that enables you to make individual libraries visible to specific offices.

## Form groups

Expanded by Rooms API v2

The *Form groups* feature enables you to connect any number of your forms into a group that you can share to specific roles and offices. This is useful to:

- Help your agents easily find and choose the forms they need to work with, rather than having to look through large libraries to find them. Form groups only contain the forms from your libraries that you choose.
- Create groups of forms used in specific tasks that your agents perform frequently. You can share your form groups with specific offices to ensure that your agents they have exactly what they need for their work.
- Share forms from multiple libraries to agents without sharing the full contents of each library. You (or any users who you authorize to manage the form group) can take any form from any libraries that you can access and add it to a form group.

To work with form groups in v2 of the Rooms API, you need to add the `manage form groups` scope to your [OAuth request](https://developers.docusign.com/docs/rooms-api/rooms101/auth/) in addition to the existing Rooms API scopes.

See [How to create a form group](https://developers.docusign.com/docs/rooms-api/how-to/create-form-group/) for an example of how to define a new form group using the API.

## Next steps

- See [How to add forms to a room](https://developers.docusign.com/docs/rooms-api/how-to/add-form-to-room/) for a full code example demonstrating how to add a form to a room.
- See [Using forms in a room](https://developers.docusign.com/docs/rooms-api/rooms101/forms/using-forms-in-a-room/) for details on how forms work within a room.
- For more code examples demonstrating how to work with form groups, see [How to create a form group](https://developers.docusign.com/docs/rooms-api/how-to/create-form-group/), [How to assign a form to a form group](https://developers.docusign.com/docs/rooms-api/how-to/assign-form-group/), and [How to grant office access to a form group](https://developers.docusign.com/docs/rooms-api/how-to/access-form-group/).

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
