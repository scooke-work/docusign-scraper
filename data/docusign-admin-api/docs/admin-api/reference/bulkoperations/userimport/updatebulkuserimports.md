---
title: ': updateBulkUserImports'
source_url: https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userimport/updatebulkuserimports/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:12:10Z'
---

[API Reference](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userimport/updatebulkuserimports/)[API Explorer](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userimport/updatebulkuserimports/?explorer=true)

[UserImport](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userimport/)

# : updateBulkUserImports

Bulk updates information for existing users.

Your CSV import file is made up of a header row with the column headers and a row of user or account data for each user you want to add to an account.

**Update limit:** You can update up to 2,000 users on an account and include up to 50 accounts per import. The maximum number of updated users per import is 8,000.

This method requires the following HTTP headers:

| Header | Value |
| --- | --- |
| Content-Type | `text/csv` |
| Content-Disposition | `filename=filename.csv` |

To ensure your CSV is properly formatted, use the
[Sample Bulk Update CSV file](https://admin.docusign.com/static-resources/organization-user-update-import.csv)
as a template. The following table describes the columns.

Note that the columns for bulk adding users and bulk update users are slightly different.
The update CSV file requires an `APIUserName` column, and does not have an `AutoActivate` column.

| Column | Required | Description |
| --- | --- | --- |
| AccountID | yes | The 32-character API account ID of the user's account in your organization. You can find this value in the API and Keys section of the Admin area of the account. |
| AccountName |  | The name of the user's account in your organization. The account name must match the account ID provided. |
| FirstName | yes | The user's first name. |
| LastName | yes | The user's last name. |
| UserEmail | yes | The user's complete email address. |
| PermissionSet | yes | The user's permission set. The PermissionSet value must match an existing permission set for the account. This value is not case sensitive. |
| UserTitle |  | The user's job title. |
| CompanyName |  | The user's company name. |
| Group |  | The user's assigned groups. The Group values must match existing Group names for the account. Additional Group columns can be added to the file to add users to more than one group. You do not need to add users to the Everyone group, since all new users are automatically added to that group. |
| AddressLine1 |  | The user's address, first line. |
| AddressLine2 |  | The user's address, second line. |
| City |  | The user's city name. |
| StateRegionProvince |  | The user's regional location. |
| PostalCode |  | The user's postal code. |
| Phone |  | The user's phone number. |
| Language |  | The user's display language for their Docusign account. Must be one of:  - Chinese Simplified: `zh_CN` - Chinese Traditional: `zh_TW` - Dutch: `nl` - English: `en` - French: `fr` - German: `de` - Italian: `it` - Japanese: `ja` - Korean: `ko` - Portuguese: `pt` - Portuguese Brazil: `pt_BR` - Russian: `ru` - Spanish: `es` |
| LoginPolicy |  | The user's login policy. Valid values include the following:  - Column left blank = The user is created with no policy assigned. - FedAuthRequired = The user must log in with an Identity Provider. - FedAuthBypass = The user may log in with an Identity Provider or their Docusign username and password.  For more information on login policies, see [Setting User Login Policy](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=zah1583359147774.html). |
| AutoActivate |  | For domain users, new users can be activated automatically for domain accounts using SSO by setting the value to **true.** The user is activated automatically once the import is complete. Memberships activated in this way do not receive an activation email. |

## Updating user email addresses

Changing a user's email address should be done carefully. The user's email address is used to log in to Docusign and receive documents to sign from others.
Once changed, existing documents that were sent or received:

- Will still appear in the user's documents list.
- Notifications about these documents will be sent to the new email address. If someone sends a new document to the old email address:
- Docusign will send a notification to the old address.
- It will not appear in the documents list of the account.

This change of email address will be applied to all of the user's account memberships.

[Required authentication scopes](https://developers.docusign.com/docs/admin-api/admin101/auth/): `user_write`.

## Request

#### HTTP Request

POST

```
/Management/v2/organizations/{organizationId}/imports/bulk_users/update
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| organizationId \* | string | The organization ID Guid |

\* Required

## SDK Method

### BulkOperations::updateBulkUserImports

## Request Body

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
