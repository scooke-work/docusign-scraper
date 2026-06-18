---
title: Docusign Admin API concepts
source_url: https://developers.docusign.com/docs/admin-api/admin101/concepts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- API 101
- API 101
- Concepts
scraped_at: '2026-06-18T20:12:05Z'
---

# Docusign Admin API concepts

For administrators of complex Docusign accounts, including organizations with multiple domains and accounts, Docusign Administration centralizes the management of Docusign users, accounts, and single sign-on (SSO). It allows you to protect and manage corporate assets with the security of SSO, domain-level controls, and the administration of all corporate users from a single user interface. This includes being able to search for a user across all your accounts and domains, then manage that user's permissions centrally. Docusign Admin provides both a UI interface and an API that you can leverage to manage organization users and accounts.

- **Without Docusign Admin**, a company with multiple Docusign accounts must manage their users on a per-account basis. This can force companies to apply configuration changes and user updates multiple times, one time for each account, causing more work, higher risk of errors, and inconsistent organization or implementation of account structure.
- **Using Docusign Admin**, each account is part of an *Organization*, which enables you to manage all the organization’s accounts and users from one place. You can use bulk operations to apply configuration changes and user updates to many users with one operation.

For developers working with the Docusign APIs, implementing the Docusign Admin API has the following advantages over working with individual accounts without Docusign Admin:

- It provides endpoints for automating actions and performing bulk operations on larger numbers of users across multiple accounts.
- It provides endpoints to export and import user- and account-specific lists, enabling you to quickly obtain the information you need about your organization and make necessary changes with a single operation.
- Unlike the account model, organization administrators do not need to be members or administrators of an account to manage its users. This helps reduce the scope of access by separating user management from account management.
- Because Docusign Admin endpoints are gated by a special scope that you obtain through OAuth authentication, you can customize the permissions for a Docusign Admin account by requesting only the set of scopes needed for their work. See  [Authenticating with the Docusign Admin API](https://developers.docusign.com/docs/admin-api/admin101/auth/)  for details.

## Docusign Admin API Functionality

The Docusign Admin API is focused on automation and performing operations in bulk, but it supports several key scenarios including:

- **Bulk actions:** You can use bulk actions to manage settings for multiple users and/or accounts within an organization simultaneously.
- **Centralized user management:** You can manage user access and permissions for any account from one place, rather than needing to manage them in each account separately.
- **Auto activate membership:** When adding a user of a domain reserved by your organization, the Docusign Admin API enables you to activate that user automatically in an account.
- **View domain users:** The Docusign Admin API enables you to get data on each user within your organization that is associated with a reserved domain, regardless of their account.
- **Change user email addresses:** You can leverage the Docusign Admin API to update user email addresses within your organization.

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
