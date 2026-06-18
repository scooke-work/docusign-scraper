---
title: Using forms in a room
source_url: https://developers.docusign.com/docs/rooms-api/rooms101/forms/using-forms-in-a-room/
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
- Using forms in a room
scraped_at: '2026-06-18T22:33:02Z'
---

# Using forms in a room

Forms are standard preset documents imported to your company’s Rooms account for easy reuse. These documents, typically association forms or other documents required for legal compliance in real estate transactions, can be compiled into form groups by forms administrators (users in your account who have been granted permission to manage forms). A form group should contain all of the forms required for a specific type of transaction in a specific area.

When a room is created, a user, typically an agent, can add forms to the room from a form library or a form group depending on their permissions and company setup.

Docusign Forms is partnered with and automatically supports forms from many real estate associations, and you can contact the Account Manager to add your own custom forms. Your agents can add their National Realtor Database System (NRDS) ID, either when prompted or manually via the **Rooms Settings** menu, to unlock additional supported forms.

See [how to add forms to a room](https://developers.docusign.com/docs/rooms-api/how-to/add-form-to-room/) for a full code example demonstrating how to add a form to a room.

**Note:** Forms is a Rooms for Real Estate feature. There is no comparable feature in Rooms for Mortgage.

## Data propagation between forms

Data between all forms in a room is shared. When you update a field in one form, such as the seller’s name, all other forms that contain that field will also be updated. The room’s **Details** tab will also be updated with this data, reducing data entry and ensuring consistency across multiple forms.

## Embedded form fill

You can integrate forms from a room into your app, enabling your users to fill out those forms using your own app’s UI and workflow via the embedded form fill feature.

To embed a form to fill out in your app, you need the ID of the room containing the form and the ID of the form to be filled out.

**Note:** Embedded form fill is only available in v2 of the Rooms API.

## Next steps

- See [how to add forms to a room](https://developers.docusign.com/docs/rooms-api/how-to/add-form-to-room/) for a full code example demonstrating how to add a form to a room.
- See [Managing forms](https://developers.docusign.com/docs/rooms-api/rooms101/forms/managing-forms-rooms/) for details on managing forms for your rooms.
- For code examples demonstrating how to work with form groups, see [How to create a form group](https://developers.docusign.com/docs/rooms-api/how-to/create-form-group/), [How to assign a form to a form group](https://developers.docusign.com/docs/rooms-api/how-to/assign-form-group/), and [How to grant office access to a form group](https://developers.docusign.com/docs/rooms-api/how-to/access-form-group/).

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
