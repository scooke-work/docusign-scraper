---
title: How to retrieve the user's Docusign profile using an email address
source_url: https://developers.docusign.com/docs/admin-api/how-to/retrieve-docusign-profile-using-email/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Docusign Admin API
- Docusign Admin API
- How-to guides
- How-to guides
- Retrieve Docusign Profile Using Email
scraped_at: '2026-06-18T20:12:05Z'
---

# How to retrieve the user's Docusign profile using an email address

This topic demonstrates how to obtain the user’s Docusign profile information across all Docusign accounts by specifying the user’s email address.

**Important:** This endpoint can only be used by organizations that have purchased Docusign plans for both CLM and eSignature.

**Note:** If you only know the user’s **User ID** and do not know their email address, see [How to retrieve the user's Docusign profile using a User ID](https://developers.docusign.com/docs/admin-api/how-to/retrieve-docusign-profile-using-userid/)

Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).

## Required data

Running the code in this how-to requires this data:

| Data element | Description |
| --- | --- |
| {BASE\_PATH} | A string value that forms the root of the URL required to make API calls. The base path value in the example code is set to target the developer environment at   https://<domain>/management  Where <domain> is api-d.docusign.net for the developer environment and api.docusign.net for production. |
| {EMAIL\_ADDRESS} | An email address for a user in the given organization. |
| {ORGANIZATION\_ID} | A [GUID](http://guid.one/) value that identifies the the organization that contains the account to which the user will be added. Copy the value from the **Organization ID** field in the **Organization** section of the [Account Profile](https://admindemo.docusign.com/authenticate?goTo=accountProfile) page. |

## Step 1. Obtain your OAuth token

To make the API call shown in this how-to, you need a valid OAuth access token. Docusign supports access tokens for three different recommended OAuth grant types: Public Authorization Code Grant, Confidential Authorization Code Grant, and JSON Web Token (JWT) Grant. Choose the OAuth grant type appropriate for your scenario. See [Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/#confidential-authorization-code-grant) for guidance on your options to get an Confidential Authorization Code Grant OAuth token.

Docusign Admin OAuth access tokens are the same ones used for our [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/esign101/auth/), although you must request one or more [Docusign Admin scopes](https://developers.docusign.com/docs/admin-api/admin101/auth/) to call the Docusign Admin API. The endpoint call made in this how-to requires that you request the Docusign Admin-specific `user_write` scope when obtaining your access token.

See [Docusign Admin Authentication](https://developers.docusign.com/docs/admin-api/admin101/auth/) for details and the full list of Docusign Admin scopes.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='384' width='565' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Three icons that represent the three methods a user can use to obtain an OAuth token: JSON Web Token (JWT), Public Authorization Code Grant (ACG), and Confidential Authorization Code grant](https://images.ctfassets.net/aj9z008chlq0/6wHxmI9WeaVLfXApVnBMN/e8974bf495b34ce2d78a4925bace1bd8/authOptions.png?w=565&h=384&q=50&fm=png)

## Step 2. Construct your API headers

After you have a valid OAuth access token, you are ready to construct the API headers that you will pass to the API call. Construct your headers like this, but make sure to substitute your valid OAuth access token for {ACCESS\_TOKEN}.

1

2

3

declare -a Headers=('--header' "Authorization:

Bearer ${ACCESS\_TOKEN}" \

'--header' "Accept: application/json" \

'--header' "Content-Type: application/json")

## Step 3. Call the Admin API

Now that you have constructed your request body, make a GET request to the Admin API. Here’s how you make the call, but make sure to substitute your Organization ID for {ORGANIZATION\_ID}.

View the source code for this how-to on GitHub:
[Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Admin/eg006RetrieveDocuSignProfileByEmailAddress.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Admin/Examples/RetrieveDocuSignProfileByEmailAddress.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/admin/examples/A006RetrieveDocuSignProfileByEmailAddress.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/admin/examples/getUserProfileByEmail.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Admin/RetrieveDocuSignProfileByEmailAddress.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Admin/eg006GetUserProfileByEmail.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/admin/examples/eg006_get_user_profile_by_email.py), or [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/admin_api/eg006_get_user_profile_by_email_service.rb).

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

# Calculate date parameter to get users modified in

the last 10 days

if date -v -10d &>/dev/null; then

# Mac

# modified\_since=`date -v -10d '

+%Y-%m-%dT%H:%M:%S%z'`

modified\_since=$(date -v -10d '+%Y-%m-%d')

else

# Not a Mac

# modified\_since=`date --date='-10 days' '

+%Y-%m-%dT%H:%M:%S%z'`

modified\_since=$(date --date='-10 days' '

+%Y-%m-%d')

fi

response=$(mktemp /tmp/response-admin.XXXXXX)

# Call the Admin API

curl --request GET ${base\_path}/v2.1/organizations/$

{ORGANIZATION\_ID}/users/dsprofile?email=$

## Expected response

If you run this code example from our Quickstart or launcher projects, you should see a JSON response similar to this for each user.

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

{

"users": [

{

"id": "c316f86c-xxxx-xxxx-xxxx-6b39358381d2",

"site\_id": 1,

"site\_name": "Demo",

"user\_name": "Susan Signer",

"first\_name": "Susan",

"last\_name": "Signer",

"user\_status": "active",

"default\_account\_id":

"b71dbd28-xxxx-xxxx-xxxx-8d99842a7982",

"default\_account\_name": "Acme",

"language\_culture": "en",

"is\_organization\_admin": true,

"created\_on": "2020-09-30T21:39:06.527",

"memberships": [

{

"email": "test@example.com",

"account\_id":

## Next steps

- Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).
- See [How to retrieve the user's Docusign profile using a User ID](https://developers.docusign.com/docs/admin-api/how-to/retrieve-docusign-profile-using-userid/).
- Learn [How to create a new active user for CLM and eSignature](https://developers.docusign.com/docs/admin-api/how-to/create-active-clm-esign-user/).
- See how to [Go-Live](https://developers.docusign.com/docs/admin-api/go-live/) with a completed app and find the base path for API calls in the production environment..

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
