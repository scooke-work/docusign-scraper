---
title: ': getUsers'
source_url: https://developers.docusign.com/docs/admin-api/reference/usermanagement/users/getusers/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:12:09Z'
---

[API Reference](https://developers.docusign.com/docs/admin-api/reference/usermanagement/users/getusers/)[API Explorer](https://developers.docusign.com/docs/admin-api/reference/usermanagement/users/getusers/?explorer=true)

[Users](https://developers.docusign.com/docs/admin-api/reference/usermanagement/users/)

# : getUsers

Returns information about the users in an organization.

You must include at least one of the following query parameters in the request:

- `account_id`: The ID of an account associated with the organization.
- `organization_reserved_domain_id`: The ID of one of the organization's reserved domains.
- `email`: An email address associated with the users that you want to return.

[Required authentication scopes](https://developers.docusign.com/docs/admin-api/admin101/auth/): `user_read`.

## Request

#### HTTP Request

GET

```
/Management/v2/organizations/{organizationId}/users
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| organizationId \* | string | The organization ID Guid |

| Query Parameters |  |  |
| --- | --- | --- |
| start | integer | Index of first item to include in the response. The default value is 0. |
| take | integer | Page size of the response. The default value is 20. |
| end | integer | Index of the last item to include in the response. Ignored if `take` parameter is specified. |
| email | string | Email address of the desired user. At least one of `email`, `account_id` or `organization_reserved_domain_id` must be specified. |
| email\_user\_name\_like | string | Selects users by pattern matching on the user's email address |
| status | string | Status. |
| membership\_status | string | The user's membership status. One of:   - `activation_required` - `activation_sent` - `active` - `closed` - `disabled` |
| account\_id | string | Select users that are members of the specified account. At least one of `email`, `account_id` or `organization_reserved_domain_id` must be specified. |
| organization\_reserved\_domain\_id | string | Select users that are in the specified domain. At least one of `email`, `account_id` or `organization_reserved_domain_id` must be specified. |
| last\_modified\_since | string | Select users whose data have been modified since the date specified. `account_id` or `organization_reserved_domain_id` must be specified. |
| include\_ds\_groups | boolean | Select users with groups the users belong to; The organization must have entitlement `AllowMultiApplication` enabled. |
| include\_license | boolean | When true: additional details about the user's license will be included in the response; account\_id must be specified and the account must have an IAM plan with licenses. |

\* Required

## SDK Method

### UserManagement::getUsers

## Responses

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
