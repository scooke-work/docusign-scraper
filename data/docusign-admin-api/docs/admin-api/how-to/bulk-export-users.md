---
title: How to bulk export user data
source_url: https://developers.docusign.com/docs/admin-api/how-to/bulk-export-users/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- How-to guides
- How-to guides
- Bulk Export Users
scraped_at: '2026-06-18T20:12:04Z'
---

# How to bulk export user data

This topic demonstrates how to bulk export user accounts within an organization into a CSV (comma separated value) file.

Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).

## Required data

Running the code in this how-to requires this data:

| Data element | Description |
| --- | --- |
| {ACCOUNT\_ID} | A [GUID](http://guid.one/) value that identifies the account to which the user will be added.  To determine your account IDs, open your [Organization](https://apps-d.docusign.com/admin/organization/) home page in Docusign Admin, then select the **Accounts** tile. The **Account ID** values for each account in your organization will be shown on the resulting page. |
| Admin access | The caller must be at least one of the following:  - A full organization administrator - A delegated organization administrator  See [Organization Administrators](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=rrf1583359212854&topicId=god1583359152535.html&_LANG=enus) for details on Docusign Admin roles. |
| {BASE\_PATH} | A string value that forms the root of the URL required to make API calls. The base path value in the example code is set to target the developer environment at   https://<domain>/management  Where <domain> is api-d.docusign.net for the developer environment and api.docusign.net for production. |
| {ORGANIZATION\_ID} | A [GUID](http://guid.one/) value that identifies the the organization that contains the account to which the user will be added. Copy the value from the **Organization ID** field in the **Organization** section of the [Account Profile](https://admindemo.docusign.com/authenticate?goTo=accountProfile) page. |

## Step 1. Obtain your OAuth token

To make the API calls shown in this how-to, you need a valid OAuth access token. Docusign supports access tokens for three different recommended OAuth grant types: Public Authorization Code Grant, Confidential Authorization Code Grant, and JSON Web Token (JWT) Grant. Choose the OAuth grant type appropriate for your scenario.

Docusign Admin OAuth access tokens are the same ones used for our [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/), although you must request one or more Docusign Admin scopes to call the Docusign Admin API. The endpoint calls made in this how-to require that you request the Docusign Admin-specific `user_write` scope when obtaining your access token.

See [Docusign Admin Authentication](https://developers.docusign.com/docs/admin-api/admin101/auth/) for details and the full list of Docusign Admin scopes.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='384' width='565' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Three icons that represent the three methods a user can use to obtain an OAuth token: JSON Web Token (JWT), Public Authorization Code Grant (ACG), and Confidential Authorization Code grant](https://images.ctfassets.net/aj9z008chlq0/6wHxmI9WeaVLfXApVnBMN/e8974bf495b34ce2d78a4925bace1bd8/authOptions.png?w=565&h=384&q=50&fm=png)

## Step 2. Construct your API headers

After you have a valid OAuth access token, you are ready to construct the API headers that you will pass to the API call. Construct your headers like this, but make sure to substitute your valid OAuth access token for {ACCESS\_TOKEN}.

1

2

3

declare -a Headers=('--header' "Authorization:

Bearer ${ACCESS\_TOKEN}"

'--header' "Accept: application/json"

'--header' "Content-Type: application/json")

## Step 3. Create the bulk export request

Next, begin the process of creating the bulk export list by calling the [createUserListExport](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userexport/createuserlistexport/) endpoint. You can retrieve the resulting CSV data in a future step.

Creating and provisioning the bulk export list can take some time, especially for large organizations spread out over several regions. You can check the status of your bulk export request by calling the [getUserListExport](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userexport/getuserlistexport/) endpoint, as demonstrated in the next step.

You can filter the users that will be added to the generated bulk export user list using the type parameter of the request body, which specifies the category of users within your organization that will be added to the generated list of user data. Possible values are:

- `organization_external_memberships_export`: Returns a list of users with email addresses that are part of your organization’s domain(s), but with memberships in accounts that are not part of your organization.
- `organization_memberships_export`: Returns a list of all users with memberships in your organization’s accounts.
- `organization_domain_users_export`: Returns a list of all users within your organization’s domain(s).

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

retryCount=0

downloadUrl=''

while [ $retryCount -le 5 ]; do

echo ''

echo 'Retrieving Bulk Action Status...'

echo ''

curl --request GET ${base\_path}/v2/organizations/

${ORGANIZATION\_ID}/exports/user\_list/$

{requestId} \

"${Headers[@]}" \

--output ${response}

echo ''

echo "Response:"

echo ''

cat $response

echo ''

#Check the status of the Bulk Action

status=$(cat $response | grep status | sed 's/.

## Expected response

After a successful request, you will receive a response similar to this.

The important parts of the response are highlighted below:

| Property | Description |
| --- | --- |
| `id` | Identifies the request. You can use this value to check the status of the export request again, if its status is not yet `completed`. |
| `status` | The status of the request. If the bulk export data is still being created, this value will be `queued` or `in_progress`. When the bulk export data is ready, this value will be `completed`.Possible values are:  - `unknown:` Unknown status. - `queued:` Ready to be created. - `in_process:` The export is being created. - `completed:` The export was created. - `failed:` The export could not be created. |
| `metadata_url` | The endpoint URL that you can call to check the request status and, if it is completed, get a download link for the export data. |

If you receive a **401 - Unauthorized** response, your access token is not valid for the endpoint. If you receive this error:

- Make sure that your access token has the `user_read` scope.
- Make sure that the calling user has admin rights.

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

{

"id": "f7638356-xxxx-xxxx-xxxx-4935e87d88c1",

"type": "organization\_memberships\_export",

"requestor": {

"name": "1007 a",

"id": "9cb13e29-xxxx-xxxx-xxxx-6baeba17505c",

"type": "user",

"email": "1007a@example.com"

},

"created": "2021-10-07T22:16:16.4923965Z",

"last\_modified": "2021-10-07T22:16:16.4923965Z",

"status": "queued",

"metadata\_url": "https://api-d.docusign.net/

management/v2/organizations/

e1b55b52-xxxx-xxxx-xxxx-8a7ff52dd8e0/exports/

user\_list/f7638356-xxxx-xxxx-xxxx-4935e87d88c1",

"percent\_completed": 0,

"number\_rows": 0,

"size\_bytes": 0

}

## Step 4. Check the request status

It can take some time for a bulk user export request to be fully created, depending on the number of users that it contains and the regions it encompasses. You can call the [getUserListExport](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userexport/getuserlistexport/) endpoint to check the status of your pending request and, if complete, obtain a URL that you can call to download the CSV file containing the export data.

**Important**: Be sure to replace the `requestId` value in the request with the ID of the bulk user export request that you created in the previous step.

1

2

3

curl --request GET ${base\_path}/v2/organizations/$

{ORGANIZATION\_ID}/exports/user\_list/${requestId} \

"${Headers[@]}" \

--output ${response}

## Expected response

This call will return a response similar to this.

The important parts of the response are highlighted below:

| Property | Description |
| --- | --- |
| `id` | Identifies the request. You can use this value to check the status of the export request again, if its status is not yet `completed`. |
| `status` | The status of the request. If the bulk export data is still being created, this value will be `queued` or `in_progress`. When the bulk export data is ready, this value will be `completed`.Possible values are:  - `unknown:` Unknown status. - `queued:` Ready to be created. - `in_process:` The export is being created. - `completed:` The export was created. - `failed:` The export could not be created. |
| `success` | Indicates whether the export was successful. If false, the export failed and the data cannot be downloaded. |
| `percent_completed` | Indicates how close to completion the export request is. |
| `results.id` | The ID of the generated user list data. |
| `results.url` | The URL that you can call to download the exported list of user data, as demonstrated in the next step. |

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

{

"id": "f7638356-xxxx-xxxx-xxxx-4935e87d88c1",

"type": "organization\_memberships\_export",

"requestor": {

"name": "1007 a",

"id": "9cb13e29-xxxx-xxxx-xxxx-6baeba17505c",

"type": "user",

"email": "1007a@example.com"

},

"created": "2021-10-07T22:16:16.4923965Z",

"last\_modified": "2021-10-07T22:16:37.4462418Z",

"completed": "2021-10-07T22:16:37.4462418Z",

"expires": "2022-01-05T22:16:32.1492867Z",

"status": "completed",

"metadata\_url": "https://api-d.docusign.net/

management/v2/organizations/

e1b55b52-xxxx-xxxx-xxxx-8a7ff52dd8e0/exports/

user\_list/f7638356-xxxx-xxxx-xxxx-4935e87d88c1",

"percent\_completed": 100,

"number\_rows": 182,

## Step 5. Download the exported user data

After the export is complete and you’ve obtained the URL to retrieve the bulk export data, you can download a CSV file of that data.

The `results.url` value returned by the status request made in the previous step will contain the full path for the URL where you can download the CSV data, but you can also create the request manually by calling the [getUserListExport](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userexport/getuserlistexport/) endpoint, as demonstrated in this example.

1

2

3

curl --request GET "${downloadUrl}" \

"${Headers[@]}" \

--output ${response2}

## Expected response

**Important:** Make sure to replace the `resultId` placeholder with the `results.id` value you obtained in the previous step (or copy and paste the `results.url` value to completely replace the URL).

This API call will return a CSV file containing the list of user data, similar to this.

After downloading the CSV file, you can make edits to the list and either reimport it to update your user data or import it to a new account or organization. See [How to add users via bulk import](https://developers.docusign.com/docs/admin-api/how-to/add-users-bulk-import/) for details.

View the source code for this how-to on GitHub: [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg003BulkExportUserData.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/BulkExportUserData.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/BulkExportUserDataService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/bulkExportUserData.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/BulkExportUserDataService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg003BulkExportUserData.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg003_bulk_export_user_data.py), or [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg003_bulk_export_user_data_service.rb)

1

"SiteID","AccountID","AccountName","APIUserName",

"FullName","FirstName","LastName","UserEmail",

"UserStatus","AddedDate","MembershipStatus",

"eSignPermissionProfile","CompanyName","JobTitle",

"AddressLine1","AdressLine2","City",

"StateRegionProvince","PostalCode","Country","Phone",

"Groups","EnableCLM","CLMPermissionProfile",

"IdentityProviderInfo","eSignPermissionProfileID",

## Next steps

- Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).
- See [How to create a new active eSignature user](https://developers.docusign.com/docs/admin-api/how-to/create-active-user/)
- Learn [How to add users via bulk import](https://developers.docusign.com/docs/admin-api/how-to/add-users-bulk-import/)
- See [Docusign Admin concepts](https://developers.docusign.com/docs/admin-api/admin101/concepts/) for more information on Docusign Admin capabilities and features.
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
