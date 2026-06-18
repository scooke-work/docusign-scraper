---
title: ': getUserProfiles'
source_url: https://developers.docusign.com/docs/admin-api/reference/usermanagement/esignusermanagement/getuserprofiles/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:12:06Z'
---

[API Reference](https://developers.docusign.com/docs/admin-api/reference/usermanagement/esignusermanagement/getuserprofiles/)[API Explorer](https://developers.docusign.com/docs/admin-api/reference/usermanagement/esignusermanagement/getuserprofiles/?explorer=true)

[eSignUserManagement](https://developers.docusign.com/docs/admin-api/reference/usermanagement/esignusermanagement/)

# : getUserProfiles

Returns historical information about users with a specific email address.
**Note:** The `email` query parameter is *required*.

To get a list of users in an organization,
use [Users: getUsers](https://developers.docusign.com/docs/admin-api/reference/usermanagement/users/getusers/)
instead.

For example, the following request gets information about
accounts that use `max@example.net` as an email address:

```
GET /Management/v2/organizations/96e994fa-xxxx-xxxx-xxxx-c5fe9d1ccd10/users/profile?email=max@example.net

{
  "users": [
    {
      "id": "6b67a1ee-xxxx-xxxx-xxxx-385763624163",
      "site_id": 1,
      "site_name": "Monadnock",
      "user_name": "Max Example",
      "first_name": "Max",
      "last_name": "Example",
      "user_status": "active",
      "default_account_id": "f636f297-xxxx-xxxx-xxxx-8e7a14715950",
      "default_account_name": "BizCo",
      "is_organization_admin": false,
      "created_on": "2019-04-01T22:11:56.457",
      "memberships": [
        {
          "email": "max@example.net",
          "account_id": "624e3e00-xxxx-xxxx-xxxx-43918c520dab",
          "external_account_id": "17xxxxx1",
          "account_name": "LoanCo",
          "is_external_account": false,
          "status": "active",
          "permission_profile": { },
          "created_on": "2019-04-01T22:11:56.457",
          "groups": [ ],
          "is_admin": false
        },
        {
          "email": "max@example.net",
          "account_id": "f636f297-xxxx-xxxx-xxxx-8e7a14715950",
          "external_account_id": "25xxxxx0",
          "account_name": "BizCo",
          "is_external_account": true,
          "status": "active",
          "permission_profile": { },
          "created_on": "2021-07-07T15:10:51.96",
          "groups": [ ],
          "is_admin": false
        },
        {
          "email": "max@example.net",
          "account_id": "6aed3a52-xxxx-xxxx-xxxx-e89988167cfd",
          "external_account_id": "11xxxxx1",
          "account_name": "SleepCo",
          "is_external_account": true,
          "status": "closed",
          "permission_profile": { },
          "created_on": "2021-07-11T12:40:44.26",
          "groups": [],
          "is_admin": true,
          "closed_on": "2021-07-13T08:40:51.8"
        }
      ],
      "identities": [],
      "device_verification_enabled": false
    }
  ]
}
```

The response includes up to the first 20 users modified in the last 10 days.

[Required authentication scopes](https://developers.docusign.com/docs/admin-api/admin101/auth/): `user_read`.

### Related topics

- [How to Audit Users](https://developers.docusign.com/docs/admin-api/how-to/audit-users/)

## Request

#### HTTP Request

GET

```
/Management/v2/organizations/{organizationId}/users/profile
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| organizationId \* | string | The organization ID Guid |

| Query Parameters |  |  |
| --- | --- | --- |
| email | string | The email address associated with the users you want to retrieve.  **Note:** This property is required. |
| include\_license | boolean | When true: additional details about the user's license will be included in the response. The account must have an IAM plan with licenses. |

\* Required

## SDK Method

### UserManagement::getUserProfiles

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
