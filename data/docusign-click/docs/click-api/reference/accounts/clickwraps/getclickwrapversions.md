---
title: ': getClickwrapVersions'
source_url: https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwrapversions/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T22:18:21Z'
---

[API Reference](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwrapversions/)[API Explorer](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/getclickwrapversions/?explorer=true)

[ClickWraps](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/)

# : getClickwrapVersions

Gets all the versions of an elastic template for an account.

[Required authentication scopes](https://developers.docusign.com/docs/click-api/click101/auth/): `click.manage`.

This example shows three versions:
two major versions (1.0 and 2.0), and one minor version (2.1).

```
{
  "accountId": ""624e3e00-xxxx-xxxx-xxxx-43918c520dab",
  "clickwrapId": ""b4cb1e3a-xxxx-xxxx-xxxx-3b3c21b853ea",
  "clickwrapName": "The name of this",
  "versions": [
    {
      "versionId": ""0df7af2d-xxxx-xxxx-xxxx-c2b960b73fef",
      "versionNumber": "2.1",
      "status": "active",
      "createdTime": "2023-02-24T01:45:21.0138703Z",
      "lastModified": "2023-02-24T01:45:25.8540652Z",
      "lastModifiedBy": ""7c430bdb-xxxx-xxxx-xxxx-538c11111ff7",
      "requireReacceptance": false,
      "ownerUserId": ""7c430bdb-xxxx-xxxx-xxxx-538c11111ff7",
      "dataFields": []
    },
    {
      "versionId": ""4976a2f5-xxxx-xxxx-xxxx-dc1fd3b97c15",
      "versionNumber": "2.0",
      "status": "inactive",
      "createdTime": "2023-02-24T01:36:07.6852505Z",
      "lastModified": "2023-02-24T01:45:25.8853154Z",
      "lastModifiedBy": ""7c430bdb-xxxx-xxxx-xxxx-538c11111ff7",
      "requireReacceptance": true,
      "ownerUserId": ""7c430bdb-xxxx-xxxx-xxxx-538c11111ff7",
      "dataFields": []
    },
    {
      "versionId": ""987e83d7-xxxx-xxxx-xxxx-5348c4f89dca",
      "versionNumber": "1.0",
      "status": "inactive",
      "createdTime": "2023-02-24T01:17:59.806101Z",
      "lastModified": "2023-02-24T01:36:11.1843708Z",
      "lastModifiedBy": ""7c430bdb-xxxx-xxxx-xxxx-538c11111ff7",
      "requireReacceptance": true,
      "ownerUserId": ""7c430bdb-xxxx-xxxx-xxxx-538c11111ff7",
      "dataFields": []
    }
  ],
  "page": 0,
  "pageSize": 40,
  "minimumPagesRemaining": 0
}
```

## Request

#### HTTP Request

GET

```
/clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/versions
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| clickwrapId \* | string | The GUID of the elastic template. |

\* Required

## SDK Method

### Accounts::getClickwrapVersions

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
