---
title: ': list'
source_url: https://developers.docusign.com/docs/esign-rest-api/v2/reference/templates/templates/list/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:10:56Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/v2/reference/templates/templates/list/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/v2/reference/templates/templates/list/?explorer=true)

[Templates](https://developers.docusign.com/docs/esign-rest-api/v2/reference/templates/templates/)

# : list

Retrieves the list of templates for the specified account. The request can be limited to a specific folder.

## Request

#### HTTP Request

GET

```
/restapi/v2/accounts/{accountId}/templates
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account id GUID. |

| Query Parameters |  |  |
| --- | --- | --- |
| count | string | The number of records to return. |
| folder | string | The query value can be a folder name or folder ID. The response will only return templates in the specified folder. |
| folder\_ids | string | A comma-separated list of folder ID GUIDs. |
| from\_date | string | Start of the search date range. Only returns templates created on or after this date/time. If no value is specified, there is no limit on the earliest date created. |
| include | string | A comma separated list of additional template attributes to include in the response. Valid values are: recipients, folders, documents, custom\_fields, and notifications. |
| modified\_from\_date | string |  |
| modified\_to\_date | string |  |
| order | string | Sets the direction order used to sort the list. Valid values are:   - `asc` = ascending sort order (a to z) - `desc` = descending sort order (z to a) |
| order\_by | string | Sets the file attribute used to sort the list. Valid values are:   - `name`: template name - `modified`: The date and time the template was last modified. - `used`: The date and time the template was last used. |
| search\_text | string | The search text used to search the names of templates. |
| shared\_by\_me | string | If true, the response only includes templates shared by the user. If false, the response only returns template not shared by the user. If not specified, the response is not affected. |
| start\_position | string | The starting index for the first template shown in the response. This must be greater than or equal to 0 (zero). |
| to\_date | string | End of the search date range. Only returns templates created up to this date/time. If no value is provided, this defaults to the current date. |
| used\_from\_date | string | Start of the search date range. Only returns templates used or edited on or after this date/time. If no value is specified, there is no limit on the earliest date used. |
| used\_to\_date | string | End of the search date range. Only returns templates used or edited up to this date/time. If no value is provided, this defaults to the current date. |
| user\_filter | string | Sets if the templates shown in the response Valid values are: -owned\_by\_me: only shows templates the user owns. -shared\_with\_me: only shows templates that are shared with the user. -all: shows all templates owned or shared with the user. |
| user\_id | string | The id of the user. |

\* Required

## SDK Method

### Templates::ListTemplates

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
