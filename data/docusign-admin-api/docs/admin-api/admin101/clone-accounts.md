---
title: Clone eSignature accounts
source_url: https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- API 101
- API 101
- Clone Accounts
scraped_at: '2026-06-18T20:12:04Z'
---

# Clone eSignature accounts

*Account cloning* enables you to create an [eSignature account](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=moe1583277322917.html) in your [organization](https://developers.docusign.com/docs/admin-api/admin101/concepts/data-model/) by copying features of an existing account, referred to as a *source account*, to a new account, referred to as a *target account*. This can be useful for quickly provisioning accounts that your organization uses to differentiate business operations based on region, department, integration features, or other requirements. See [Considerations Before Creating New Accounts﻿](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=aza1683656783269.html) for information about when it's appropriate to create an account rather than using an existing account.

You can clone accounts via [API requests](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#api-endpoints-and-required-scopes-for-account-cloning) or by using [Docusign Admin](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=ydm1682347143672.html).

This feature is only available in the production environment. To request to enable account creation and account cloning in your developer account, contact [Docusign Support](https://support.docusign.com/s/contactSupport) and include your demo organization ID, which you can obtain from the **Organization** section of the [Account Profile](https://admindemo.docusign.com/authenticate?goTo=accountProfile) page.

## Features that are copied when cloning an account

When you clone an account, these features of the target account will be identical to those of the source account:

- The eSignature [account plan](https://www.docusign.com/plans-and-pricing/): This defines general account features.
- Modules: These include add-ons that provide enhanced functionality, such as [SMS and WhatsApp delivery](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/sms-delivery/) and [CFR Part 11](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/cfr-part-11-accounts/).
- [Settings](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=wzt1583359174550.html): These determine account behavior in areas such as envelope sending, signing, and security.

These items are not copied to the target account:

- [Users](https://developers.docusign.com/docs/admin-api/admin101/concepts/data-model/)
- [Groups](https://developers.docusign.com/docs/admin-api/admin101/concepts/groups/)
- [Signing groups](https://support.docusign.com/s/document-item?bundleId=gav1643676262430&topicId=zgn1578456447934.html&_LANG=enus&language=en_US&rsc_301)
- [Permission profiles](https://developers.docusign.com/docs/admin-api/admin101/concepts/permission-profiles/)
- [Integrations](https://developers.docusign.com/platform/configure-app/) listed on the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page
- [Templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/)
- [Elastic templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/elastic-templates/)
- [Brands](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/branding/)
- [Connect configurations](https://developers.docusign.com/platform/webhooks/connect/create-configuration-trigger-event/)

## Account cloning behaviors and restrictions

These sections describe account cloning behaviors and restrictions:

- [Cloning occurs within an organization](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#cloning-occurs-within-an-organization)
- [Source accounts must be compliant](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#source-accounts-must-be-compliant)
- [All source account settings are copied](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#all-source-account-settings-are-copied)
- [Up to five processes can be active per source account](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#one-cloning-process-can-be-active-per-source-account)
- [Do not modify source account while cloning is in progress](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#do-not-modify-source-account-while-cloning-is-in-progress)
- [Target account administrator must be an organization admin](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#target-account-administrator-must-be-an-organization-admin)
- [Target account properties determine data residency](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#target-account-properties-determine-data-residency)

### Cloning occurs within an organization

Account cloning occurs within the context of an organization. Because of this, cloning is subject to the following restrictions:

- The user who initiates an account cloning API request must be an [organization administrator](https://developers.docusign.com/docs/admin-api/admin101/concepts/org-admins/) of the organization whose ID is specified in the request.
- The source account must be under the organization whose ID is specified in the API request. You cannot clone accounts that are not associated with an organization.
- By default, the target account will be in the same organization as the source account. If you do not want the target account to be in that organization, after the cloning process has finished, you can [unlink the account](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=qlu1583359176306.html) and [link it to a different organization](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=mtc1583359175678.html).

### Source accounts must be compliant

In order for a source account to be cloned, it must meet Docusign compliance criteria. Docusign evaluates account compliance by checking the asset group to which the account belongs. An *asset group* consists of all the plan items covered by the account subscription with Docusign. If an account has plan items enabled that are not included in its asset group, the account is considered noncompliant, and it cannot be cloned.

Before attempting to clone a source account, you can check whether it's compliant by making an [AccountCloning:getAssetGroupAccounts](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccounts/) request. It returns a list of your organization's accounts, with a `compliant` property that indicates whether each account is compliant.

If a source account is not compliant, you have two options:

- Clone a different account. Every organization has at least one compliant account.
- Contact [Docusign Support](https://support.docusign.com/s/contactSupport) to explore options for bringing the account into compliance.

### All source account settings are copied

The cloning process copies all source account settings to the target account. If you want to change target account settings, you can do so after the target account has been [activated](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#target-account-activation).

### Up to five processes can be active per source account

You can run up to five cloning processes per source account at any given time, allowing you to create up to five target accounts concurrently.

To create more than one target account from the same source account, launch a separate [AccountCloning:cloneAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/) request for each target account.

For details on tracking progress and status, see the [Cloning request processing](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#cloning-request-processing) documentation.

### Do not modify source account while cloning is in progress

To avoid unexpected results for a target account, Docusign recommends that you do not modify settings for a source account while a clone of that account is in progress. [Cloning request processing](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#cloning-request-processing) has information about how you can determine when a cloning process has finished.

### Target account administrator must be an organization admin

An account cloning API request includes a [targetAccount.admin](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_admin) object that defines an account administrator for the target account. The administrator specified in the [AccountCloning:cloneAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/) request must already exist as a user in your organization with [organization admin permissions](https://developers.docusign.com/docs/admin-api/admin101/concepts/org-admins/). If you want to [define additional administrators](https://admindemo.docusign.com/authenticate?goTo=users) for the target account, you can do so after the account has been [activated](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#target-account-activation).

### Target account properties determine data residency

An account cloning API request includes properties that define [data residency](https://www.docusign.com/privacy/data-residency) for the target account. You have the option of specifying a country code ([targetAccount.countryCode](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_countrycode) property) or a region ([targetAccount.region](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_region) property) in the [AccountCloning:cloneAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/) request. Docusign recommends supplying a country code, and the target account will be mapped automatically to a data center. Valid country code values are the two-letter [ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).

If the source account and the target account have the same country code or region, the target account will be assigned the same Docusign data center as the source account. Otherwise, the target account will be assigned to the default data center for the country or region specified in the request to clone the account.

In the developer environment, the region NA (North America) will be used for all new target accounts, regardless of the region or country code specified in the request to clone an account.

## API endpoints and required scopes for account cloning

The [AccountCloning Resource](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/) includes four endpoints related to the cloning process. This section describes each endpoint and lists the scope that you must supply during [authentication](https://developers.docusign.com/docs/admin-api/admin101/auth/) in order to use the endpoint.

All account cloning requests require an organization ID. You can obtain your organization ID via a request to the [Organization:getOrganizations](https://developers.docusign.com/docs/admin-api/reference/organization/organization/getorganizations/) endpoint or by copying it from the **Organization** section of the [Account Profile](https://admindemo.docusign.com/authenticate?goTo=accountProfile) page.

The Admin API [SDKs](https://developers.docusign.com/docs/admin-api/sdks/) include the equivalent SDK methods for the account cloning endpoints in six programming languages. See [How to clone an account](https://developers.docusign.com/docs/admin-api/how-to/clone-account/) for code examples that show how to implement account cloning using SDK methods.

| **Endpoint** | **Description** | **Required scope** |
| --- | --- | --- |
| [AccountCloning:getAssetGroupAccounts](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccounts/) | Returns a list of accounts in an organization and indicates which are [in compliance](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#source-accounts-must-be-compliant) and therefore eligible to be cloned. | `asset_group_account_read` |
| [AccountCloning:cloneAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/) | Initiates an account cloning process and supplies the source account and target account details in the request. | `asset_group_account_clone_write` |
| [AccountCloning:getAssetGroupAccountClone](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclone/) | Returns information about a cloning process, including the status, whether it succeeded or failed, the target account ID after successful completion, and an error message in the event of a failure. | `asset_group_account_clone_read` |
| [AccountCloning:getAssetGroupAccountClonesByOrgId](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclonesbyorgid/) | Returns a list of all cloning processes for the organization, including their statuses, the outcome (success or failure), the target account ID after successful completion, and an error message in the event of a failure. | `asset_group_account_clone_read` |

## Cloning request processing

If an [AccountCloning:cloneAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/) request succeeds, the response looks like this:

```
{
  "sourceAccount": {
    "id": "dac17ad7-xxxx-xxxx-xxxx-873f3b4cb7e2"
  },
  "targetAccount": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "TestClone",
    "region": "NA",
    "site": "Demo",
    "admin": {
      "email": "test@email.com",
      "firstName": "TestFirst",
      "lastName": "TestLast"
    }
  },
  "assetGroupWorkId": "c9da77ee-xxxx-xxxx-xxxx-347704226e15",
  "assetGroupId": "ef233c93-xxxx-xxxx-xxxx-5e53e7a3c56b",
  "assetGroupWorkType": "AccountAssetClone",
  "status": "Pending",
  "attempts": 0,
  "createdDate": "2023-08-09T13:46:20.268974Z",
  "message": "Awaiting Asset Group Work Job"
}
```

The `Pending` status indicates that the cloning process will begin shortly. The response contains a placeholder value for `targetAccount.id`, because the account ID won't be available until the cloning process has finished successfully, which can take up to 10 minutes. Keep in mind that after a success response to an `AccountCloning:cloneAssetGroupAccount` request, it's still possible for the cloning process to fail.

You can monitor the cloning process status and retrieve the target account ID by using the [AccountCloning:getAssetGroupAccountClone](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclone/) call. You identify the cloning process by populating `assetGroupWorkId` in this request with the value returned in the response to the `AccountCloning:cloneAssetGroupAccount` request. You can also use the [AccountCloning:getAssetGroupAccountClonesByOrgId](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclonesbyorgid/) call, which returns information about all cloning processes for an organization. A `Processing` status indicates that cloning is in progress. Upon successful completion, the status will be `Completed`, and the `targetAccount.id` property will contain the ID of the new account.

If a cloning process fails, the `AccountCloning:getAssetGroupAccountClone` and `AccountCloning:getAssetGroupAccountClonesByOrgId` requests return a `PendingError` status, and the `cloneProcessingFailureDetails` property provides an [error code and message](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#troubleshoot-account-cloning-errors). Docusign will retry a failed cloning process 10 times. The `attempts` property in the responses to the two `GET` requests tracks the number of retries attempted. If a retry succeeds, the `GET` requests return a `Completed` status. If none of the 10 retries succeeds, the `GET` requests return a `PermanentFailure` status, and the `cloneProcessingFailureDetails` object contains the error code and message for the last retry.

## Target account activation

Upon successful completion of a cloning process, account activation for the target account's administrator occurs as follows, depending on the organization's [Signup Settings](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=hyk1668217995409.html):

- If the organization is configured to activate memberships automatically, no action is needed from the target account administrator to activate their membership in the target account.
- If automatic activation is not enabled, the target account's administrator will receive an email with the subject line **Account Activation**. The administrator must click the **Activate** link in the email to complete the process of assuming the administrator role for the target account.

After automatic or manual account activation, the target account administrator will see the account in the list displayed when they [switch between accounts](https://support.docusign.com/s/document-item?bundleId=jux1643235969954&topicId=gmc1578456462118.html) in the eSignature web application.

## Close unneeded target accounts

If you have accounts in your organization created via the cloning process that you no longer need, you can file a Support ticket to request that they be closed. See [Close an account](https://developers.docusign.com/platform/account/#close-an-account)  for details.

## Troubleshoot account cloning errors

This section describes issues that can cause an account cloning process to fail. The errors may appear in the response to any of these requests:

- [AccountCloning:cloneAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/)
- [AccountCloning:getAssetGroupAccountClone](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclone/)
- [AccountCloning:getAssetGroupAccountClonesByOrgId](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclonesbyorgid/)

### Source account errors

The request to clone an account includes a [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) property, which identifies the account to clone. These errors can occur as a result of issues with the source account:

| **Error code** | **Error message** | **Description** |
| --- | --- | --- |
| `clone_account_not_compliant` | `The source clone account is not compliant.` | The account specified in [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) cannot be cloned because it includes features not covered under the account subscription. See [Source accounts must be compliant](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#source-accounts-must-be-compliant) for more information. |
| `invalid_account` | `The source account does not exist.` | The value of [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) is not the ID of an account in the system. |
| `invalid_account` | `The source account is not in the organization of the asset group.` | The account specified in [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) is not in the organization whose ID appears in the request header. You can only initiate cloning requests for accounts in the organization in the request header. |
| `invalid_asset_group_account` | `The source account does not belong to any asset group.` | The account specified in [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) has not been associated with an asset group and therefore cannot be cloned. If you have confirmed that this account is in your organization, contact [Docusign Support](https://support.docusign.com/s/contactSupport) for assistance with associating the account with an asset group. See [Source accounts must be compliant](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#source-accounts-must-be-compliant) for more information. |
| `invalid_asset_group_work` | `The max number of active clones for this Source Account has been reached (1).` | The account specified in [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) is also the source account for another cloning process that's in progress. An account cannot serve as the source for more than one concurrent cloning process. Use the [AccountCloning:getAssetGroupAccountClone](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclone/) request or the [AccountCloning:getAssetGroupAccountClonesByOrgId](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclonesbyorgid/) request to verify that the previous cloning process for the source account has finished before attempting to use the account as the source for a new cloning request. |
| `invalid_asset_group_work` | `The source clone account has unfulfilled assets.` | The account specified in [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) is in the process of being created as a target account via the cloning process, and the process has not finished. You cannot use a target account as the source account for a new cloning request until that account's cloning process has finished successfully. Use the [AccountCloning:getAssetGroupAccountClone](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclone/) request or the [AccountCloning:getAssetGroupAccountClonesByOrgId](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccountclonesbyorgid/) request to verify that the cloning process has finished successfully before attempting to use the target account as the source account for a cloning request. |
| `invalid_request_parameter_value` | `Error converting value \"[value]\" to type 'System.Guid'. Path 'sourceAccount.id', line [line number], position [position number].` | The value of [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) in the request is an empty string or is not a valid GUID. |
| `invalid_request_parameter_value` | `Required property 'id' not found in JSON. Path 'sourceAccount', line [line number], position [position number].` | [sourceAccount.id](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount_id) is missing from the request. |
| `invalid_request_parameter_value` | `The sourceAccount field is required.` | [sourceAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_sourceaccount) is missing from the request. |

### Target account errors

The request to clone an account includes a [targetAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount) object that defines properties associated with the target account. These errors can occur as a result of issues with this definition:

| **Error code** | **Error message** | **Description** |
| --- | --- | --- |
| `clone_account_invalid_country` | `The country code should have exactly two characters. The provided country code has [length] characters.` | The value provided for [targetAccount.countryCode](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_countrycode), was not two characters long, and [targetAccount.region](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_region) was not supplied. Valid `targetAccount.countryCode` values are the two-letter [ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). |
| `clone_account_invalid_country` | `The region cannot be determined based on the country code [countryCode].` | An invalid value was provided for [targetAccount.countryCode](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_countrycode), and [targetAccount.region](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_region) was not supplied. Valid `targetAccount.countryCode` values are the two-letter [ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes). |
| `invalid_account_admin_user` | `A valid admin user email is required.` | [targetAccount.admin.email](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_admin_email) contains a value that is not a valid email address. |
| `invalid_account_name` | `Account name must be provided.` | [targetAccount.name](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_name)is missing from the request or contains an empty string. |
| `invalid_account_name` | `The account name entered is [length] characters, the maximum is 100 characters.` | [targetAccount.name](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_name) exceeded the maximum length of 100 characters. |
| `invalid_email_address` | `Admin email must be provided.` | [targetAccount.admin.email](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_admin_email)is missing from the request or contains an empty string. |
| `invalid_region` | `Region or country code must be provided.` | Both [targetAccount.region](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_region) and [targetAccount.countryCode](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_countrycode) are missing or contain an empty string. At least one of these values must be supplied. |
| `invalid_site` | `This site cannot be determined.` | An invalid value was provided for [targetAccount.region](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_region). Valid values correspond to these Docusign data center regions: `NA`, `EU`, `AU`, and `CA`.  **Note:** In the developer environment, only `NA` can be used for this value. |
| `invalid_user_name` | `Admin first name must be provided.` | [targetAccount.admin.firstName](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_admin_firstname) is missing from the request or contains an empty string. |
| `invalid_user_name` | `Admin last name must be provided.` | [targetAccount.admin.lastName](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/#schema__assetgroupaccountclone_targetaccount_admin_lastname) is missing from the request or contains an empty string. |

## Next steps

For more information about account cloning, see:

- [How to clone an account](https://developers.docusign.com/docs/admin-api/how-to/clone-account/)
- [AccountCloning Resource](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/) in the API reference
- [Clone an Existing Account﻿](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=ydm1682347143672.html) in the Docusign Admin Guide

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
