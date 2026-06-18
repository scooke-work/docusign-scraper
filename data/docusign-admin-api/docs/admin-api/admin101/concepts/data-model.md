---
title: Admin API data model
source_url: https://developers.docusign.com/docs/admin-api/admin101/concepts/data-model/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- API 101
- API 101
- Concepts
- Concepts
- Data Model
scraped_at: '2026-06-18T20:12:05Z'
---

# Admin API data model

An organization is divided into accounts, domains, and users, as outlined by this animated diagram:

![Organization example diagram](https://developers.docusign.com/img/admin-user-animated.gif?v=2023050417)

- An **organization** contains accounts, domains, and the users within those accounts and domains. An organization administrator can perform operations to add, update, or close any users within any of the organization’s accounts or reserved domains from one place, rather than performing these operations for each account individually.
  - You can manage account settings, domain settings, and users within accounts through the organization to which they belong.
  - Organizations may reserve domains.
  - Organizations may be linked with one or more accounts.
- **Accounts** contain users and envelopes, and have specific settings, templates, brands, billing, and usage. An organization can export settings for any of its accounts, enabling easy auditing, troubleshooting, and sharing setting changes to any other account in the organization.
  - Accounts are linked to an organization.
  - You can perform operations to add/update/close account users, and change account settings within your organization.
  - An account can only have one organization.
- **Domains** are organization-specific reserved internet domains, such as @exampledomain.com. You can define policy settings for users of each reserved domain within your organization, export lists of domain users for audit purposes, and manage domain users.
  - Domains may be claimed by an organization.
  - When a domain is claimed by an organization, all users within that domain are added to the organization, even if they have trial or free accounts.
  - You can set domain controls for all users of the domain.
  - You can export information about your organization’s users that are associated with your reserved domains.
- **Users** represent individual Docusign users in your organization. Users may be present in one or more accounts and may be associated with a reserved domain.
  - Users must be members of at least one account within an organization.
  - Users may be part of a domain reserved to the organization.
  - If a user is a member of multiple accounts, their information is present in each account.
  - If a user is part of a reserved domain, then they are a user within the organization.
  - You can query, add, update, or close users through their associated account or domain.

## Next steps

- See the [How-to guides overview](https://developers.docusign.com/docs/admin-api/how-to/) for a list of guides that demonstrate how common Docusign Admin scenarios work.
- See the MyAPICalls sample app [Add a User](https://myapicalls.sampleapps.docusign.com/scenario/7) scenario, which walks you through a sequence of API calls that retrieve organization, group, and permission profile information, and use it to create a user.

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
