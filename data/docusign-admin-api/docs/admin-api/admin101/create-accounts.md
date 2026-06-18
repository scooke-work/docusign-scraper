---
title: Create new eSignature accounts
source_url: https://developers.docusign.com/docs/admin-api/admin101/create-accounts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- API 101
- API 101
- Create Accounts
scraped_at: '2026-06-18T20:12:03Z'
---

# Create new eSignature accounts

This feature is only available in the production environment. To request to enable account creation and account cloning in your developer account, contact [Docusign Support](https://support.docusign.com/s/contactSupport) and include your demo organization ID, which you can obtain from the **Organization** section of the [Account Profile](https://admindemo.docusign.com/authenticate?goTo=accountProfile) page.

New [eSignature accounts](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=moe1583277322917.html) can be created in your [organization](https://developers.docusign.com/docs/admin-api/admin101/concepts/data-model/) through the Docusign Admin API or through [Docusign Admin](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=ptx1683672714427.html). You must be an [organization administrator](https://developers.docusign.com/docs/admin-api/admin101/concepts/org-admins/) to perform these actions. See [Considerations Before Creating New Accounts﻿](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=aza1683656783269.html) for information about when it's appropriate to create an account rather than using an existing account.

## Defining the new account

When you create a new account with the API, you specify the following features of the account in your API request body.

- Subscription ID: The ID of the subscription under which the new account will be created.
- Plan ID: The ID of the eSignature [account plan](https://www.docusign.com/plans-and-pricing/) that defines general account features.
- Modules: Any add-ons that provide enhanced functionality, such as [SMS and WhatsApp delivery](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/sms-delivery/) and [CFR Part 11](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/cfr-part-11-accounts/).
- Account name: The name of the new account.
- Country code: This determines the data residency of the new account. In the production environment this value can be set to the two-character [ISO 3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) for the country of the target account.
- Admin: Information about the new account admin including name and email address.

The request body should look like this:

```
{
    "subscriptionDetails": {
        "id": "'${SUBSCRIPTION_ID}'",
		"planId": "'${PLAN_ID}'",
		"modules": []
    },
    "targetAccount": {
        "name": "'${ACCOUNT_NAME}'",
        "countryCode": "US",
        "admin": {
            "email": "'${EMAIL_ADDRESS}'",
            "firstName": "'${FIRST_NAME}'",
            "lastName": "'${LAST_NAME}'",
            "locale": "en"
        }
    }
}
```

## API endpoints and required scopes for account cloning

The [AccountCreation Resource](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/) includes four endpoints related to account creation. This section describes each endpoint and lists the scope that you must supply during [authentication](https://developers.docusign.com/docs/admin-api/admin101/auth/) in order to use the endpoint.

All account cloning requests require an organization ID. You can obtain your organization ID via a request to the [Organization:getOrganizations](https://developers.docusign.com/docs/admin-api/reference/organization/organization/getorganizations/) endpoint or by copying it from the **Organization** section of the [account profile](https://admindemo.docusign.com/authenticate?goTo=accountProfile) page.

The Admin API [SDKs](https://developers.docusign.com/docs/admin-api/sdks/) include the equivalent SDK methods for the account creation endpoints in six programming languages. See [How to create an account](https://developers.docusign.com/docs/admin-api/how-to/create-account/) for code examples that show how to implement account creation using SDK methods.

| Endpoint | Description | Required scope |
| --- | --- | --- |
| [AccountCreation : CreateAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/createassetgroupaccount/) | Creates a new Docusign account using the plan and modules specified in the request body. | `organization_sub_account_write` |
| [AccountCreation: GetOrganizationPlanItems](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/getorganizationplanitems/) | Get information about plan items within an organization. | `organization_sub_account_read` |
| [AccountCreation: GetSubAccountCreateProcessByAssetGroupWorkId](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/getsubaccountcreateprocessbyassetgroupworkid/) | Get a single account creation process. | `organization_sub_account_read` |
| [AccountCreation: GetSubAccountCreateProcessesByOrgId](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/getsubaccountcreateprocessesbyorgid/) | Get all ongoing account creation processes for an Organization. | `organization_sub_account_read` |

## Account creation request processing

If an [AccountCreation : CreateAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/createassetgroupaccount/) request succeeds, the response looks like this:

```
{
  "AssetGroupWork": {
    "AssetGroupWorkId": "81bffa7c-xxxx-xxxx-beaxxxx4-9ebd34820ea3",
    "AssetGroupId": "73018b16-xxxx-xxxx-xxxx-1e51982162fd",
    "AssetGroupWorkType": "AccountAssetCreate",
    "Status": "Pending",
    "TargetAccountId": "00000000-0000-0000-0000-000000000000",
    "CreateSubAccountDetails": {
      "SubscriptionDetails": {
        "SubscriptionId": "795b8b77-xxxx-xxxx-xxxx-a57827759219",
        "PlanId": "22a84d6c-xxxx-xxxx-xxxx-1232cc3e1a5b",
        "Modules": []
      },
      "Name": "Account Name",
      "CountryCode": "US",
      "Region": "NA",
      "Site": "Demo",
      "AdminUser": {
        "EmailAddress": "example@example.com",
        "FirstName": "First",
        "LastName": "Last",
        "Locale": "en"
      },
      "BillingProfileType": 0
    },
    "Attempts": 0,
    "Message": "Awaiting Asset Group Work Job",
    "NewAssetGroupSubscriptionId": "00000000-0000-0000-0000-000000000000",
    "CreatedBy": "8cb9aa3f-xxxx-xxxx-xxxx-f6ce2e16dad1",
    "CreatedByType": 1,
    "CreatedDate": "2024-08-07T21:17:05.8912009Z",
    "UpdatedBy": "8cb9aa3f-xxxx-xxxx-xxxx-f6ce2e16dad1",
    "UpdatedByType": 1,
    "UpdatedDate": "2024-08-07T21:17:05.8912009Z"
  },
  "Message": "",
  "Success": true
}
```

The `Pending` status indicates that the account creation process will begin shortly. The response contains a placeholder value for `TargetAccountId` because the account ID won't be available until the process has finished successfully, which can take up to 10 minutes. Keep in mind that after a successful response to an `AccountCreation: CreateAssetGroupAccount` request, it's still possible for the process to fail.

## Troubleshoot account creation errors

This section describes issues that can cause an account cloning process to fail. The errors may appear in the response to the [AccountCreation : CreateAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/createassetgroupaccount/) request.

| Error code | Error message | Description |
| --- | --- | --- |
| `account_creation_active_create_limit_reached` | The maximum number of accounts being created has been reached. | The maximum number of accounts that can be created at once has been reached. Currently you can only create one account at a time. |
| `account_creation_entitlement_disabled` | Organization does not have the required entitlement enabled. | Account creation is not enabled in this organization. |
| `account_creation_inactive_subscription` | Subscription provided is not active. | The account subscription for the new account is not currently active. |
| `account_creation_incompatible_asset_group_id` | Asset Group ID provided does not belong to this organization. | The asset group ID provided does not belong to the organization. |
| `account_creation_invalid_asset_requested` | Requested asset(s) does not belong to subscription. | The plan ID from the request body does not belong to the subscription. |
| `account_creation_invalid_inputs` | Target account details must be provided. | One or more of the values of [SubAccountCreateRequest.targetAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/createassetgroupaccount/#schema__subaccountcreaterequest_targetaccount) is missing. |
| `account_creation_region_cannot_be_determined_from_country` | The region cannot be determined based on the country code | An invalid value was provided for [targetAccount.countryCode](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/createassetgroupaccount/#schema__subaccountcreaterequest_targetaccount_countrycode), and [targetAccount.region](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/createassetgroupaccount/#schema__subaccountcreaterequest_targetaccount_region) was not supplied. Valid `targetAccount.countryCode` values are the two-letter [ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). |
| `account_creation_site_cannot_be_determined` | Site cannot be determined. | An invalid value was provided for [targetAccount.region](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/createassetgroupaccount/#schema__subaccountcreaterequest_targetaccount_region). Valid values correspond to these Docusign data center regions: `NA`, `EU`, `AU`, and `CA`. **Note:** In the developer environment, only `NA` can be used for this value. |
| `account_creation_subscription_id` | Incorrect Subscription ID provided. | Invalid subscription id provided. |
| `account_creation_subscription_info` | Required subscription details must be provided. | The request body does not include the subscription ID or plan ID. |

## Next steps

For more information about account creation, see:

- [How to create an account](https://developers.docusign.com/docs/admin-api/how-to/create-account/)
- [AccountCreation Resource](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcreation/) in the API reference
- [Clone eSignature accounts](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/)

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
