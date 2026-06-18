---
title: Authentication
source_url: https://developers.docusign.com/docs/admin-api/admin101/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- API 101
- API 101
- Authentication
scraped_at: '2026-06-18T20:12:04Z'
---

# Authentication

All calls to the Docusign Admin API are authenticated using an access token that your app obtains using one of the standard OAuth 2.0 grants supported by Docusign[:](https://developers.docusign.com/platform/auth/jwt/jwt-get-token/)

- [Public Authorization Code Grant](https://developers.docusign.com/platform/auth/public-authcode-get-token/)
- [Confidential Auth Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/)
- [Implicit Grant](https://developers.docusign.com/platform/auth/implicit-get-token/)
- [JWT Grant](https://developers.docusign.com/platform/auth/jwt-get-token/)

**Note:** See [Choose an OAuth type](https://developers.docusign.com/platform/auth/choose/) for details on when to use each authentication type.When using the Admin API, you must request a special set of Docusign Admin scopes in addition to your other Docusign eSignature [Authentication scopes](https://developers.docusign.com/platform/auth/reference/scopes/).The list of Docusign Admin scopes that you can request and the types of operations that require them are listed below:

|  |  |
| --- | --- |
| Scope | Description |
| `organization_read` | Gets lists of organizations and organization data |
| `group_read` | Gets lists of groups associated with an account |
| `permission_read` | Gets lists of permission profiles associated with an account |
| `user_read` | Reads user data |
| `user_write` | Updates, creates, or deletes users |
| `account_read` | Gets account data |
| `account_write` | Updates, creates, or deletes account data |
| `domain_read` | Gets data on reserved domains for the organization |
| `identity_provider_read` | Gets data on identity providers for an organization |
| `user_data_redact` | Deletes personal data for closed user accounts |
| `asset_group_account_read` | Gets a list of organization accounts that indicates which accounts are [eligible to be cloned](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#source-accounts-must-be-compliant) |
| `asset_group_account_clone_write` | Initiates an [account cloning process](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#cloning-request-processing) |
| `asset_group_account_clone_read` | Gets status and results for an[account cloning process](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#cloning-request-processing) |
| `connect_org_config_read_api` | Reads data for an Organization-Level Connect configuration |
| `connect_org_config_write_api` | Writes data for an Organization-Level Connect configuration |
| `connect_org_oauth_read_api` | Reads data for your Organization-Level Connect configuration OAuth settings |
| `connect_org_oauth_write_api` | Writes data for your Organization-Level Connect configuration OAuth settings |
| `connect_org_hmac_read_api` | Reads a list of the HMAC keys for your organization |
| `connect_org_hmac_write_api` | Creates new HMAC keys for your organization |

**Important:** If the required Docusign Admin scopes were not explicitly requested, calls to the Docusign Admin API will fail.

## Application access tokens

When obtaining an access token using the [JWT Grant](https://developers.docusign.com/platform/auth/jwt/), you can choose to create either a user-access token that impersonates an account user or an access token that represents an application, called an application-access token.

Application-access tokens can be used only for Docusign Admin API endpoints. They cannot be used with the eSignature or other Docusign APIs.

Application-access tokens are an alternative to using the JWT Grant to impersonate a user with account admin or organization privileges.

## Next steps

- See [How to send an envelope with extension app data verification fields](https://developers.docusign.com/docs/connected-fields-api/send-envelope-with-data-verification-fields/) for a detailed walkthrough of how to send an envelope and validate the values of its connected fields.
- Learn how to get an access token with any authentication flow by viewing these guides:
  - [Authenticate with Public Authorization Code Grant](https://developers.docusign.com/platform/auth/public-authcode-get-token/)
  - [Authenticate with the Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/)
  - [Authenticate with the Implicit Grant](https://developers.docusign.com/platform/auth/implicit-get-token/)
  - [Authenticate with the JWT Grant](https://developers.docusign.com/platform/auth/jwt-get-token/)

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
