---
title: How to add users via bulk import
source_url: https://developers.docusign.com/docs/admin-api/how-to/add-users-bulk-import/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- How-to guides
- How-to guides
- Add Users Bulk Import
scraped_at: '2026-06-18T20:12:04Z'
---

# How to add users via bulk import

This topic demonstrates how to bulk import users and add user data from an example CSV (comma-separated value) file into a Docusign Admin organization.

Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).

## Required data

Running the code in this how-to requires this data:

| Data element | Description |
| --- | --- |
| {ACCOUNT\_ID} | A [GUID](http://guid.one/) value that identifies the account to which the user will be added.  To determine your account IDs, open your [Organization](https://apps-d.docusign.com/admin/organization/) home page in Docusign Admin, then select the **Accounts** tile. The **Account ID** values for each account in your organization will be shown on the resulting page. |
| Admin access | The caller must be at least one of the following:  - A full organization administrator - A delegated organization administrator  See [Organization Administrators](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=rrf1583359212854&topicId=god1583359152535.html&_LANG=enus) for details on Docusign Admin roles. |
| {ORGANIZATION\_ID} | A [GUID](http://guid.one/) value that identifies the the organization that contains the account to which the user will be added. Copy the value from the **Organization ID** field in the **Organization** section of the [Account Profile](https://admindemo.docusign.com/authenticate?goTo=accountProfile) page. |
| User data | A CSV file containing the user data to add, typically generated through a [bulk export](https://developers.docusign.com/docs/admin-api/how-to/bulk-export-users/) operation. The user data contained in this CSV will be imported into your organization. |

## Step 1. Obtain your OAuth token

To make the API calls shown in this how-to, you need a valid OAuth access token. Docusign supports access tokens for three different recommended OAuth grant types: Public Authorization Code Grant, Confidential Authorization Code Grant, and JSON Web Token (JWT) Grant. Choose the OAuth grant type appropriate for your scenario.

Docusign Admin OAuth access tokens are the same ones used for our [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/), although you must request one or more Docusign Admin scopes to call the Docusign Admin API. The endpoint calls made in this how-to require that you request the Docusign Admin-specific `user_write` scope when obtaining your access token.

See [Docusign Admin Authentication](https://developers.docusign.com/docs/admin-api/admin101/auth/) for details and the full list of Docusign Admin scopes.

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

## Step 3. Create the bulk import request

To import the user data from a CSV file, call [UserImport:addBulkUserImport](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userimport/addbulkuserimport/) to create a new bulk import add users request. When complete, the users whose data is contained in this CSV file will be added to the specified account in your organization.

Rather than specifying a file to use for the request, the CSV data is defined within the request body, as demonstrated in this how-to.

**Note:** When adding user data, the `AccountId`, `UserName`, `FirstName`, `LastName`, `UserEmail`, and `PermissionSet` fields are required. For updating user data, `APIUsername` is required to identify the user, rather than `UserName`/`FirstName`/`LastName`, and `PermissionSet` is not required.

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

request\_data=$(mktemp /tmp/request-oa.XXXXXX)

printf \

'AccountID,UserName,UserEmail,PermissionSet

\"'${API\_ACCOUNT\_ID}'\",FirstLast1,

exampleuser1@example.com,DS Viewer,

\"'${API\_ACCOUNT\_ID}'\",FirstLast2,

exampleuser2@example.com,DS Viewer

' >>$request\_data

# Create a temporary file to store the response

response=$(mktemp /tmp/response-oa.XXXXXX)

curl --request POST ${base\_path}/v2/organizations/$

{ORGANIZATION\_ID}/imports/bulk\_users/add \

"${Headers[@]}" \

--data-binary @${request\_data} \

--output ${response}

echo ''

## Expected response

You should see a JSON response similar to this.

The important parts of the **Sample response** are highlighted in the table below.

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

{

id: "cd400bc0-xxxx-xxxx-xxxx-c79a7c93416f",

type: "add\_users",

requestor: {

name: "Susan Signer",

id: "c316f86c-xxxx-xxxx-xxxx-6b39358381d2",

type: "user",

email: "test@email.com"

},

created: "2022-12-14T19:25:41.660Z",

last\_modified: "2022-12-14T19:25:41.660Z",

status: "queued",

has\_csv\_results: false

}

| **Property** | **Description** |
| --- | --- |
| `id` | Identifies the request. You can use this value in a call to [UserImport:getBulkUserImportRequest](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userimport/getbulkuserimportrequest/) to return the status, details, and metadata for the bulk import data, as shown in Step 4. |
| `status` | The status of the request. This value will be `queued`, after creation.  Possible values are:   - `unknown`: Unknown status - `queued`: Ready to be created - `in_process`: The export is being created - `completed`: The export was created - `failed`: The export could not be created |

If you receive a **401 - Unauthorized** response, your access token is not valid for the endpoint. If you receive this error:

- Make sure that your access token has `user_read` and `user_write` scopes.
- Make sure that the calling user has admin rights.

Creating and provisioning the bulk import list can take some time, especially for large organizations spread out over several regions. You can check the status of your bulk import request by calling [UserImport:getBulkUserImportRequest](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userimport/getbulkuserimportrequest/) as demonstrated in Step 4.

## Step 4. Check the request status

It can take some time for the response to a bulk user import request to be fully created, depending on the number of users that it contains and the regions it encompasses. You can call [UserImport:getBulkUserImportRequest](https://developers.docusign.com/docs/admin-api/reference/bulkoperations/userimport/getbulkuserimportrequest/) to check the status of your pending request and, if complete, obtain a URL that you can call to download the CSV file containing the data to verify that the updates were made.

**Important:** Be sure to set the `importId` value in the path with the import ID of the bulk user export request that you retrieved in the previous step.

View the source code for this how-to on GitHub: [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg004AddUsersViaBulkImport.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/ImportUser.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/services/BulkImportUserDataService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/importUser.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/BulkImportUserDataService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg004AddUsersViaBulkImport.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg004_add_users_via_bulk_import.py), or [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg004_import_user_service.rb).

1

2

3

curl --request GET ${base\_path}/v2/organizations/$

{ORGANIZATION\_ID}/imports/bulk\_users/${importId} \

"${Headers[@]}" \

--output ${response}

## Expected response

You should see a JSON response similar to this.

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

19

20

{

id: "cd400bc0-xxxx-xxxx-xxxx-c79a7c93416f",

type: "add\_users",

requestor: {

name: "Susan Signer",

id: "c316f86c-xxxx-xxxx-xxxx-6b39358381d2",

type: "user",

email: "test@email.com"

},

created: "2022-12-14T19:25:41.660Z",

last\_modified: "2022-12-14T19:27:02.169Z",

status: "completed",

user\_count: 2,

processed\_user\_count: 2,

added\_user\_count: 0,

updated\_user\_count: 2,

closed\_user\_count: 0,

no\_action\_required\_user\_count: 0,

error\_count: 0,

warning\_count: 0,

## Next steps

- Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).
- Learn [How to create a new active eSignature user](https://developers.docusign.com/docs/admin-api/how-to/create-active-user/) for details on how to create a new active organization user.
- See [How to bulk export user data](https://developers.docusign.com/docs/admin-api/how-to/bulk-export-users/) for details on how to use bulk export to create or update large numbers of user accounts within an organization or to verify your account users and their permissions.
- See [Docusign Admin concepts](https://developers.docusign.com/docs/admin-api/admin101/concepts/) for more information on Docusign Admin capabilities and features.
- See [Go-Live](https://developers.docusign.com/docs/admin-api/go-live/) to find the base path for Docusign Admin API calls in the production environment.

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
