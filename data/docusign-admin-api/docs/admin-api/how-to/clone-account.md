---
title: How to clone an account
source_url: https://developers.docusign.com/docs/admin-api/how-to/clone-account/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- How-to guides
- How-to guides
- Clone Account
scraped_at: '2026-06-18T20:12:05Z'
---

# How to clone an account

This topic demonstrates how to create a new Docusign eSignature account in your organization by cloning an existing account.

**Note:** Cloning copies some features of the source account to the target account, but not others; see [Clone eSignature accounts](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/) for details.

Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).

## Required data

Running the code in this how-to requires this data:

| Data element | Description |
| --- | --- |
| {ACCOUNT\_NAME} | The name of the new account. |
| Admin access | The caller must be a full organization administrator. See [Organization Administrators](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=rrf1583359212854&topicId=god1583359152535.html&_LANG=enus) for details on Docusign Admin roles. |
| {BASE\_PATH} | A string value that forms the root of the URL required to make API calls. The base path value in the example code is set to target the developer environment at   https://<domain>/management  Where <domain> is api-d.docusign.net for the developer environment and api.docusign.net for production. |
| countryCode | The two-character [ISO 3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) of the country where the target account will reside. |
| {EMAIL\_ADDRESS} | The email address of the administrator for the target account. |
| {FIRST\_NAME} | The first name of the administrator for the target account. |
| {LAST\_NAME} | The last name of the administrator for the target account. |
| {ORGANIZATION\_ID} | A [GUID](http://guid.one/) value that identifies the organization to which the account will be added. Copy the value from the **Organization ID** field in the **Organization** section of the [Account Profile](https://admindemo.docusign.com/authenticate?goTo=accountProfile) page. |

## Step 1. Obtain your OAuth token

To make the API call(s) shown in this how-to, you need a valid OAuth access token. Docusign supports access tokens for three different OAuth grant types: Authorization Code Grant, Implicit Grant, and JSON Web Token (JWT) Grant. Choose the OAuth grant type appropriate for your scenario.

Docusign Admin OAuth access tokens are the same ones used for our [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/), although you must request one or more [Docusign Admin scopes](https://developers.docusign.com/docs/admin-api/admin101/auth/) to call the Docusign Admin API. The endpoint calls made in this how-to require that you request the following Docusign Admin-specific scopes when obtaining your access token: `asset_group_account_read`, `asset_group_account_clone_write`, and `asset_group_account_clone_read`.

See [Docusign Admin Authentication](https://developers.docusign.com/docs/admin-api/admin101/auth/) for the full list of Docusign Admin scopes.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='384' width='565' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Three icons that represent the three methods a user can use to obtain an OAuth token: JSON Web Token (JWT), Public Authorization Code Grant (ACG), and Confidential Authorization Code grant](https://images.ctfassets.net/aj9z008chlq0/6wHxmI9WeaVLfXApVnBMN/e8974bf495b34ce2d78a4925bace1bd8/authOptions.png?w=565&h=384&q=50&fm=png)

## Step 2. Construct your API headers

After you have a valid OAuth access token, you are ready to construct the API headers that you will pass to the API call. Construct your headers like this, but make sure to substitute your valid OAuth access token for `{ACCESS_TOKEN}`.

1

2

3

declare -a Headers=('--header' "Authorization:

Bearer ${ACCESS\_TOKEN}"

'--header' "Accept: application/json"

'--header' "Content-Type: application/json")

## Step 3. Get the list of eligible accounts

First, determine the accounts in your organization that are eligible to be cloned. To get a list of accounts in an organization that are [in compliance](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/#source-accounts-must-be-compliant), call the [AccountCloning:getAssetGroupAccounts](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/getassetgroupaccounts/) endpoint. Be sure to substitute your organization ID for `{ORGANIZATION_ID}`.

1

2

3

Status=$(curl --request GET ${base\_path}/v1/

organizations/${ORGANIZATION\_ID}/assetGroups/

accounts?compliant=true \

"${Headers[@]}" \

--output ${response})

## Step 4. Construct the request body

Next, construct the request body for the API call that will clone the account. Replace `{SOURCE_ACCOUNT_ID}` with the ID of one of the compliant accounts that was identified in the previous step. This is the ID of the account that will be cloned. Inside the targetAccount object, replace `{ACCOUNT_NAME}`, `{FIRST_NAME}`, `{LAST_NAME}`, and `{EMAIL}` with the name and email address of the administrator for the new account. This administrator should already exist as an admin user in your organization.

The `countryCode` parameter is used to determine the data residency for the new account. In the developer environment there is only one region available, and the value should be set to `"US"`. In the production environment this value can be set to the two-character [ISO 3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) for the country of the target account.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

# The country code value is set to "US" for the

developer environment

# In production, set the value to the code for the

country of the target account

printf \

'{

"sourceAccount": {

"id": "'${SOURCE\_ACCOUNT\_ID}'"

},

"targetAccount": {

"name": "'${ACCOUNT\_NAME}'",

"admin": {

"firstName": "'${FIRST\_NAME}'",

"lastName": "'${LAST\_NAME}'",

"email": "'${EMAIL}'"

},

"countryCode": "US"

}

}

' >>$request\_data

## Step 5. Call the Docusign Admin API to clone the account

Now that you have constructed your API headers and request body, make a POST request to the [AccountCloning:cloneAssetGroupAccount](https://developers.docusign.com/docs/admin-api/reference/accountprovisioning/accountcloning/cloneassetgroupaccount/) method and include the request body to clone the account. Here’s how you make the call, but make sure to substitute your organization ID for `{ORGANIZATION_ID}`. This will clone the source account into a new Docusign eSignature account.

View the source code for this how-to on GitHub: [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg012CloneAccount.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/CloneAccount.cs),[Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/CloneAccountService.java) ,[Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/cloneAccount.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/CloneAccountService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg012CloneAccount.ps1) ,[Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg012_clone_account.py).[Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg012_clone_account_service.rb) .

1

2

3

4

Status=$(curl --request POST ${base\_path}/v1/

organizations/${ORGANIZATION\_ID}/assetGroups/

accountClone \

"${Headers[@]}" \

--data-binary @${request\_data} \

--output ${response})

## Expected response

If you run this code example from our Quickstart or launcher projects, you should see a JSON response similar to the code shown.

Depending on the organization settings, the admin of the new account will receive an email with a link to activate the new account, or the account will automatically be activated. If the account does need to be activated, the status in the JSON response will be “Pending” until the account is activated.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

{

"sourceAccount": {

"id": "ed3efc40-xxxx-xxxx-xxxx-17b8f1caab2b"

},

"targetAccount": {

"id": "00000000-xxxx-xxxx-xxxx-000000000000",

"name": "Target Account",

"region": "NA",

"site": "Demo",

"admin": {

"email": "example@example.com",

"firstName": "Donna",

"lastName": "Developer"

}

},

"assetGroupWorkId":

"56cf1cf2-xxxx-xxxx-xxxx-00758573acdf",

"assetGroupId":

"ef233c93-xxxx-xxxx-xxxx-5e53e7a3c56b",

"assetGroupWorkType": "AccountAssetClone",

## Next steps

- Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).
- Learn more about [cloning eSignature accounts](https://developers.docusign.com/docs/admin-api/admin101/clone-accounts/).
- Learn [How to create a new active eSignature user](https://developers.docusign.com/docs/admin-api/how-to/create-active-user/).
- See how to [Go-Live](https://developers.docusign.com/docs/admin-api/go-live/) with a completed app and find the base path for API calls in the production environment.

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
