---
title: ': createHasAgreed'
source_url: https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T22:18:21Z'
---

[API Reference](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/)[API Explorer](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/?explorer=true)

[ClickWraps](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/)

# : createHasAgreed

Creates a unique URL for the elastic signing agreement
that you can embed in your application. The URL expires after one hour.

[Required authentication scopes](https://developers.docusign.com/docs/click-api/click101/auth/): `click.manage` and `click.send`.

The request must include at least the
`clientUserId`. This is a value that you
generate to identify the unique recipient
of the agreement.

If you are using a [dynamic content](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields/#add-dynamic-content-to-your-elastic-template) document,
you can supply the values in the `documentData`
property of the request, like this:

```
{
  "clientUserId": "cl-bc7f-48a9",
  "documentData": {
    "fullName": "T. J. Fanning",
    "email": "tj@example.com",
    "company": "Fanning Industries",
    "title": "Cat wrangler",
    "date": "2022-10-13T05:17:14-07:00"
  }
}
```

A response looks like this.
The `agreementUrl` is unique to the user identified by the `clientUserId`.
Your user can open the URL to approve the agreement.
The `documentData` property appears only if you provided it in the request.

```
{
  "accountId": "624e3e00-xxxx-xxxx-xxxx-43918c520dab",
  "clickwrapId": "0e64e4a7-xxxx-xxxx-xxxx-ce5a93b162af",
  "clientUserId": "tcl-bc7f-48a9j",
  "agreementId": "1f346c7d-xxxx-xxxx-xxxx-a5c968666785",
  "documents": [ . . .],
  "consumerDisclosureEnabled": true,
  "agreementUrl": "https://demo.docusign.net/clickapi/v1/redeem?agreementToken=AcTZT8g ... cxEqrUsA1lQ8DPPy05dE0",
  "createdOn": "2022-10-20T16:27:25.1287685Z",
  "status": "created",
  "versionId": "5957716d-xxxx-xxxx-xxxx-e1594f00ff12",
  "versionNumber": 1,
  "settings": {
    "displayName": "Agree with me",
    "hasDeclineButton": true,
    . . .
    "statementAlignment": "bottom"
  },
  "documentData": {
    "fullName": "T. J. Fanning",
    "email": "tj@example.com",
    "company": "Fanning Industries",
    "title": "Cat wrangler",
    "date": "2022-10-13T05:17:14-07:00"
  }
}
```

A successful response always includes
the following response. The response code
is different, depending on whether
the user has agreed:

| Response code | Meaning | Notes |
| --- | --- | --- |
| 200 | User has agreed. | The `agreementUrl` property does not appear in the response body. |
| 201 | User has not yet agreed. |  |

### Related topics

- [Add dynamic content to your elastic template](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields/#add-dynamic-content-to-your-elastic-template)
- [How to embed an elastic template](https://developers.docusign.com/docs/click-api/how-to/embed-elastic-templates/)

## Request

#### HTTP Request

POST

```
/clickapi/v1/accounts/{accountId}/clickwraps/{clickwrapId}/agreements
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| clickwrapId \* | string | The GUID of the elastic template. |

\* Required

## SDK Method

### Accounts::createHasAgreed

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
