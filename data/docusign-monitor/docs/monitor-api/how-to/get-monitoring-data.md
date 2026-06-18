---
title: How to get monitoring data
source_url: https://developers.docusign.com/docs/monitor-api/how-to/get-monitoring-data/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Monitor API
- Monitor API
- How-to guides
- How-to guides
- Get monitoring data
scraped_at: '2026-06-18T21:15:04Z'
---

# How to get monitoring data

This topic demonstrates how to get and display all of your organization’s monitoring data.

Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).

## Prerequisites

Running the code in this how-to requires this data:

| Prerequisite | Description |
| --- | --- |
| Admin access | To call the Docusign Monitor endpoint, you must impersonate a user with administrator access to your organization.  This means that you must have obtained your access token using [JWT Grant](https://developers.docusign.com/platform/auth/jwt-get-token/) and have requested the impersonation [scope](https://developers.docusign.com/platform/auth/reference/scopes/).  **Note:** The impersonated administrator may not be an admin of more than one organization. Admins of two or more organizations who call the Monitor API endpoint will receive responses with the 403 Forbidden [error code](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/). |
| Your organization must have access to Docusign Monitor | Your organization must have access to Docusign Monitor to call the endpoint.  The Monitor API is available for developer (demo) accounts for testing and development, but for apps in the production environment, it is a separate SKU that requires Enterprise Pro. For more information about how to enable the Monitor API for your account, contact Docusign Support. |

## Step 1. Obtain your OAuth token

To make the API calls shown in this how-to, you need a valid OAuth access token.

Because Docusign Monitor requires that you impersonate a user with admin access to your organization, you must have obtained your access token using [JWT Grant](https://developers.docusign.com/platform/auth/jwt-get-token/) and have requested the impersonation [scope](https://developers.docusign.com/platform/auth/reference/scopes/). For details, see [Docusign Monitor Authentication](https://developers.docusign.com/docs/monitor-api/monitor101/auth/).

![](data:image/svg+xml;charset=utf-8,%3Csvg height='122' width='200' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![JWTOnly.png](https://images.ctfassets.net/aj9z008chlq0/5ZF1FDuFYhdvBB8C45oADv/851ab2a181cdf8d22ee9f45599cac126/JWTOnly.png?w=293&h=179&q=50&fm=png)

## Step 2. Construct your API headers

After you have a valid OAuth access token, you are ready to construct the API headers that you will pass to the API call. Construct your headers like this, but make sure to substitute your valid OAuth access token for {ACCESS\_TOKEN}.

1

2

3

declare -a Headers=('--header' "Authorization:

Bearer ${ACCESS\_TOKEN}"

'--header' "Accept: application/json"

'--header' "Content-Type: application/json")

## Step 3. Get monitoring data

Make a GET request to the [DataSet:getStream](https://developers.docusign.com/docs/monitor-api/reference/monitor/dataset/getstream/) endpoint to get your monitoring data. Because your organization may have large amounts of data, you can use the `limit` query parameter to specify the maximum number of records each call will return (2,000 in the example shown here) and a `cursor` value to continue the query from where the previous one left off.

In this example, we return and display chunks of monitoring data, record the returned cursor value, and use that value to begin the next query until all data has been returned.

View the source code for this how-to on GitHub: [Bash](https://github.com/docusign/code-examples-bash/blob/master/examples/Monitor/eg001GetMonitoringData.sh), [C#](https://github.com/docusign/code-examples-csharp/blob/master/launcher-csharp/Monitor/Examples/GetMonitoringDataFunc.cs), [Java](https://github.com/docusign/code-examples-java/blob/master/src/main/java/com/docusign/controller/monitor/services/GetMonitoringDataService.java), [Node.js](https://github.com/docusign/code-examples-node/blob/master/lib/monitor/examples/getMonitoringData.js), [PHP](https://github.com/docusign/code-examples-php/blob/master/src/Services/Examples/Monitor/GetMonitoringDataService.php), [PowerShell](https://github.com/docusign/code-examples-powershell/blob/master/examples/Monitor/eg001GetMonitoringData.ps1), [Python](https://github.com/docusign/code-examples-python/blob/master/app/monitor/examples/eg001_get_monitoring_data.py), or [Ruby](https://github.com/docusign/code-examples-ruby/blob/master/app/services/monitor_api/eg001_get_monitoring_dataset_service.rb).

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

if date -v -10d &>/dev/null; then

# Mac

cursorDate=$(date -v -1y '+%Y-%m-%d')

else

# Not a Mac

cursorDate=$(date --date='-1 year' '+%Y-%m-%d')

fi

complete=false

cursorValue="${cursorDate}T00:00:00Z"

iterations=0

while [ $complete == false ]; do

((iterations=iterations+1))

# Create a temporary file to store the response

response=$(mktemp /tmp/response-bs.XXXXXX)

Status=$(curl -w '%{http\_code}' -i --request GET

"https://lens-d.docusign.net/api/v2.0/datasets/

monitor/stream?cursor=${cursorValue}&limit=2000" \

"${Headers[@]}" \

## Expected response

If your API call is successful, you should see a JSON response similar to this.

The sample response shows only the results of the final three query loops; the first loops (and the body of the data returned) are omitted due to lack of space. You can see the structure of the returned JSON in [Tracking data and handling alerts](https://developers.docusign.com/docs/monitor-api/monitor101/tracking-data-handling-alerts/).

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

<Responses for the first 3 loops are displayed here.

Only the final loops are

displayed in this example response>

Increment:

3

Response:

HTTP/1.1 200 OK

Transfer-Encoding: chunked

Content-Type: application/json; charset=utf-8

Server: Kestrel

Strict-Transport-Security: max-age=5184000;

includeSubDomains; preload

api-supported-versions: 2.0

X-DocuSign-TraceToken:

a778d0c4-xxxx-xxxx-xxxx-c676ed038c22

X-DocuSign-Node: SE4DFE181

Date: Thu, 29 Oct 2020 20:29:13 GMT

Strict-Transport-Security: max-age=15768000

{"endCursor":"aa\_637395998467230467\_63739599784434397

0\_195","data":[{EVENT/ALERT DATA HERE}]}

## Next steps

- Run this code example from our [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/) or launcher projects: [Bash](https://github.com/docusign/code-examples-bash), [C#](https://github.com/docusign/code-examples-csharp), [Java](https://github.com/docusign/code-examples-java), [Node.js](https://github.com/docusign/code-examples-node), [PHP](https://github.com/docusign/code-examples-php), [PowerShell](https://github.com/docusign/code-examples-powershell), [Python](https://github.com/docusign/code-examples-python), or [Ruby](https://github.com/docusign/code-examples-ruby).
- Learn the context of getting [tracking data](https://developers.docusign.com/docs/monitor-api/monitor101/tracking-data-handling-alerts/).
- Find out more about [Docusign Monitor Authentication](https://developers.docusign.com/docs/monitor-api/monitor101/auth/).
- See [Best practices for handling alerts](https://developers.docusign.com/docs/monitor-api/monitor101/best-practices-handling-alerts/).
- See [Go-Live](https://developers.docusign.com/docs/monitor-api/go-live/) to see the Monitor API endpoint base path for the production environment.

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
