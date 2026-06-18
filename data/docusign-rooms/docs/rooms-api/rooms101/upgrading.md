---
title: Upgrading from Docusign Rooms API v1.0 to v2.0
source_url: https://developers.docusign.com/docs/rooms-api/rooms101/upgrading/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Rooms API
- Rooms API
- API 101
- API 101
- Upgrading
scraped_at: '2026-06-18T22:33:01Z'
---

# Upgrading from Docusign Rooms API v1.0 to v2.0

The release of Docusign Rooms API 2.0 brings a host of new features to enhance and expand your Docusign integration.
**Important:** The Docusign Developer Center only contains documentation for the latest version of the Rooms API (v2.0). The information on this page pertains to you only if you created your Docusign Rooms integration prior to September 16, 2019.

## Why upgrade to Rooms API v2.0?

There are several benefits to upgrading your existing integrations from Rooms API v1.0 to v2.0 but please note that incompatible changes in v2.0 will require you to update your code.

- All new features and functionality will be made available only in Rooms API v2.0.
- The following Rooms API v1.0 endpoints do not support Version 6 of the Rooms platform:
- POST /v1/rooms
- POST /v1/members
- PUT /v1/members/{userId}
- GET /v1/meta/roles

## What is the difference between Rooms API v1.0 and v2.0?

Here’s an overview of the differences between Docusign Rooms API versions:

- **Tip**: Some endpoints, such as user endpoints, clearly state which version of the Rooms platform they support.
- The API Account ID is required in the URL in Rooms API v2.0. As a reminder, the API Account ID is a GUID that you can find in your eSignature account. From the top menu, select **Admin**, then select **Apps and Keys**.
- v1.0 **Meta** endpoints are under the **Global Resources** category in Rooms API v2.0.
- v1.0 **Members** endpoints are under the **Users** category in Rooms API v2.0.
- In Rooms API v2.0, **Roles** is a separate category, and is not included in the **Global Resources** category. In Version 6 of Rooms, Roles are configurable per account. As a result, we created a new category with endpoints that enable you to manage roles, including but not limited to getting a list of roles, getting the details about a specific role, and creating and deleting roles.
- Room details are handled differently in v2.0 to support the advanced configurability of Version 6. There is a new `fieldSet` object that contains a preconfigured list of fields that appear on a room's **Details** tab. Each fieldset is identified by a `fieldSetId`. A fieldset helps you make sense of the field data that you can include when creating a room, updating a room, or pulling data from a room.

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
