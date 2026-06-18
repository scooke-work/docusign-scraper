---
title: Delete personal data for your users
source_url: https://developers.docusign.com/docs/admin-api/admin101/concepts/delete-personal-data/
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
- Delete Personal Data
scraped_at: '2026-06-18T20:12:06Z'
---

# Delete personal data for your users

When a user leaves your organization or account, you can delete their personal identifiable information (PII) such as email address, home address, and name using the management API. The API provides two endpoints for deleting personal data:

- `POST https://api.docusign.net/management/v2/data_redaction/organizations/{organizationId}/user`
  Used by [organization admins](https://developers.docusign.com/docs/admin-api/admin101/concepts/delete-personal-data/#delete-personal-data-as-an-organization-administrator) to delete a user’s personal data from the specified list of their organization’s accounts and its domains.
- `POST https://api.docusign.net/management/v2/data_redaction/accounts/{accountId}/user`
  Used by [eSignature account admins](https://developers.docusign.com/docs/admin-api/admin101/concepts/delete-personal-data/#delete-personal-data-as-a-eSignature-account-administrator) to delete personal data for members of their accounts.

See [How to delete user data from one or more accounts as an organization admin](https://developers.docusign.com/docs/admin-api/how-to/org-admin-delete-user-data/) and [How to delete user data from an account as an account admin](https://developers.docusign.com/docs/admin-api/how-to/account-admin-delete-user-data/) for a code example demonstrating how to delete data from a closed user account membership.

You can only delete the personal data from your user accounts beginning 24 hours after the date and time when their membership was closed. **Note**: You must request the `user_data_redact` [scope](https://developers.docusign.com/platform/auth/reference/scopes/) during [Authenticate](https://developers.docusign.com/platform/auth/) to call either endpoint.

## Delete personal data as an organization administrator

To delete personal data from a user as an organization admin:

- You must be an organization admin (or delegated admin) with permission to manage the given account or manage domain users for the user’s email domain.
- The user account membership whose data will be deleted must have been closed for at least 24 hours.
- You must have requested the `user_data_redact` [scope](https://developers.docusign.com/platform/auth/reference/scopes/) during [Authenticate](https://developers.docusign.com/platform/auth/) .

You must also provide the following parameters to the POST `https://api.docusign.net/management/v2/data_redaction/organizations/{organizationId}/user` endpoint:

- **The user ID of the user whose PII will be removed**
  You can find this information in the organization admin UI by selecting **Users**, then **Status** and selecting the default **Status** filter and choosing **Closed**. On the chosen user’s row, select **View**. The User ID will be displayed under the user’s name in the resulting user details screen.

  ![](data:image/svg+xml;charset=utf-8,%3Csvg height='540' width='1294' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

  ![Image of the org admin UI showing where to find a user's ID](https://images.ctfassets.net/aj9z008chlq0/eRNIpjYqEB9qpQpgBXcZo/8e7c2e9613644b57df7d96b3797f6e88/UserID.png?w=1294&h=540&q=50&fm=png)
- **A set of account IDs within which the user has membership**
  You can get the set of accounts that a user has membership in by calling the  [MultiProductUserManagement:getUserDSProfile](https://developers.docusign.com/docs/admin-api/reference/usermanagement/multiproductusermanagement/getuserdsprofile/) endpoint. The user’s data will be deleted from the specified accounts.
- **Your organization ID**
  You can find this ID by selecting **Features** in the left nav, then the **Organization Details** tab.

The associated example API call shows the syntax for calling this endpoint to remove the personal data of a user from one account.

See [DataDeletion: redactIndividualUserData](https://developers.docusign.com/docs/admin-api/reference/usermanagement/datadeletion/redactindividualuserdata/) for details on this endpoint, or [How to delete user data from one or more accounts as an organization admin](https://developers.docusign.com/docs/admin-api/how-to/org-admin-delete-user-data/) for a code example demonstrating how to use it in a workflow.

1

2

3

4

5

6

7

8

9

curl --request POST 'https://api-d.docusign.net/

management/v2/data\_redaction/organizations/

9d407bcb-xxxx-xxxx-xxxx-d49be542fb08/user' \

--header 'Authorization: Bearer ey...37Q' \

--header 'Content-Type: application/json' \

--data-raw '{

"user\_id": "c26eb3fc-xxxx-xxxx-xxxx-cbcc72608d4c",

"memberships": [

{"account\_id":

"d201c20c-xxxx-xxxx-xxxx-e7a37c97513d"}

]

}'

## Delete personal data as a eSignature account administrator

To delete personal data from a user as an eSignature account admin:

- You must be an account admin (or delegated admin) with permission to manage the given account.
- The user account membership whose data will be deleted must have been closed for at least 24 hours.
- You must have requested the `user_data_redact` [scope](https://developers.docusign.com/platform/auth/reference/scopes/) during [Authenticate](https://developers.docusign.com/platform/auth/).

You must also provide the following parameters to the POST `https://api.docusign.net/management/v2/data_redaction/accounts/{accountId}/user` endpoint:

- **The user ID of the user whose PII will be removed**
  You can find this information in the [eSignature Admin](https://admindemo.docusign.com/) UI by selecting [Users](https://admindemo.docusign.com/users), then the default **Status** filter and choosing **Closed**. On the chosen user’s row, select **Actions** and **View**. The User ID will be displayed under the user’s name in the resulting user details screen.

  ![](data:image/svg+xml;charset=utf-8,%3Csvg height='924' width='1778' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

  ![Image of the eSignature Admin UI showing a user's profile ID](https://images.ctfassets.net/aj9z008chlq0/3nK3giKK1GifFBA1FQ9GvL/2a93949e5a786780a20fa968c7a40521/UserProfile.png?w=1778&h=924&q=50&fm=png)
- **Your account ID**
  You can find this ID (also called the API account ID) on the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page.

The associated example API call shows the syntax for calling this endpoint to remove the personal data of a user from one account.

See [DataDeletion: redactIndividualMembershipData](https://developers.docusign.com/docs/admin-api/reference/usermanagement/datadeletion/redactindividualmembershipdata/) for details on this endpoint, or [How to delete user data from an account as an account admin](https://developers.docusign.com/docs/admin-api/how-to/account-admin-delete-user-data/) for a code example demonstrating how to use it in a workflow.

1

2

3

4

5

6

curl --request POST 'https://api-d.docusign.net/

management/v2/data\_redaction/accounts/

d201c20c-xxxx-xxxx-xxxx-e7a37c97513d/user' \

--header 'Authorization: Bearer eyJ...37Q' \

--header 'Content-Type: application/json' \

--data-raw '{

"user\_id": "c26eb3fc-xxxx-xxxx-xxxx-cbcc72608d4c"

}'

## Next steps

- See [How to delete user data from one or more accounts as an organization admin](https://developers.docusign.com/docs/admin-api/how-to/org-admin-delete-user-data/) and [How to delete user data from an account as an account admin](https://developers.docusign.com/docs/admin-api/how-to/account-admin-delete-user-data/) for a code example demonstrating how to delete data from a closed user account membership.
- See [DataDeletion: redactIndividualUserData](https://developers.docusign.com/docs/admin-api/reference/usermanagement/datadeletion/redactindividualuserdata/) or [DataDeletion: redactIndividualMembershipData](https://developers.docusign.com/docs/admin-api/reference/usermanagement/datadeletion/redactindividualmembershipdata/) for an API reference on both user data removal endpoints.
- See [Admin API data model](https://developers.docusign.com/docs/admin-api/admin101/concepts/data-model/) for details, diagramming, and exact definitions for important Admin API terms, including organizations, users, accounts, and domains.
- See [Docusign Admin concepts](https://developers.docusign.com/docs/admin-api/admin101/concepts/) for an overview of Docusign admin and its functionality.

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
