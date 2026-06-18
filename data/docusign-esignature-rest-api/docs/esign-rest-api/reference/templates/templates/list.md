---
title: ': list'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/list/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:10:01Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/list/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/list/?explorer=true)

[Templates](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/)

# : list

Retrieves the list of templates for the specified account. The request can be limited to a specific folder.

### Related topics

- [How to create a template](https://developers.docusign.com/docs/esign-rest-api/how-to/create-template/)

## Request

#### HTTP Request

GET

```
/restapi/v2.1/accounts/{accountId}/templates
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |

| Query Parameters |  |  |
| --- | --- | --- |
| count | string | The maximum number of results to return.  Use `start_position` to specify the number of results to skip.  **Note:** If the `count` parameter is not used, `listTemplates` has a default limit of 2,000 templates. If the account has more than 2,000 templates, `listTemplates` will return the first 2,000 templates. To retrieve more than 2,000 templates, repeat the API call, specifying `start_position` and `count` to control the number of templates retrieved. |
| created\_from\_date | string | Lists templates created on or after this date. |
| created\_to\_date | string | Lists templates modified before this date. |
| folder\_ids | string | A comma-separated list of folder ID GUIDs. |
| folder\_types | string | The type of folder to return templates for. Possible values are:   - `templates`: Templates in the **My Templates** folder.   Templates in the **Shared Templates** and **All Template** folders (if the request ID from and Admin) are excluded. - `templates_root`: Templates in the root level of the **My Templates** folder, but not in an actual folder. Note that the **My Templates** folder is not a real folder. - `recylebin`: Templates that have been deleted. |
| from\_date | string | Start of the search date range. Only returns templates created on or after this date/time. If no value is specified, there is no limit on the earliest date created. |
| include | string | A comma-separated list of additional template attributes to include in the response. Valid values are:   - `powerforms`: Includes details about the PowerForms associated with the templates. - `documents`: Includes information about template documents. - `folders`: Includes information about the folder that holds the template. - `favorite_template_status`: Includes the template `favoritedByMe` property. **Note:** You can mark a template as a favorite only in eSignature v2.1. - `advanced_templates`: Includes information about advanced templates. - `recipients`: Includes information about template recipients. - `custom_fields`: Includes information about template custom fields. - `notifications`: Includes information about the notification settings for templates. |
| is\_deleted\_template\_only | string | When **true,** retrieves templates that have been permanently deleted. The default is **false.**  **Note:** After you delete a template, you can see it in the `Deleted` bin in the UI for 24 hours. After 24 hours, the template is permanently deleted. |
| is\_download | string | When **true,** downloads the templates listed in `template_ids` as a collection of JSON definitions in a single zip file.  The `Content-Disposition` header is set in the response. The value of the header provides the filename of the file.  The default is **false.**  **Note:** This parameter only works when you specify a list of templates in the `template_ids` parameter. |
| link\_configuration\_id | string |  |
| modified\_from\_date | string | Lists templates modified on or after this date. |
| modified\_to\_date | string | Lists templates modified before this date. |
| order | string | Specifies the sort order of the search results. Valid values are:   - `asc`: Ascending (A to Z) - `desc`: Descending (Z to A) |
| order\_by | string | Specifies how the search results are listed. Valid values are:   - `name`: template name - `modified`: date/time template was last modified - `used`: date/time the template was last used. |
| search\_fields | string | A comma-separated list of additional template properties to search.   - `sender`: Include sender name and email in the search. - `recipients`: Include recipient names and emails in the search. - `envelope`: Not used in template searches. |
| search\_text | string | The text to use to search the names of templates.  Limit: 48 characters. |
| shared\_by\_me | string | When **true,** the response only includes templates shared by the user. When **false,** the response only returns template not shared by the user. If not specified, templates are returned whether or not they have been shared by the user. |
| start\_position | string | The zero-based index of the result from which to start returning results.  Use with `count` to limit the number of results.  The default value is `0`. |
| template\_ids | string | A comma-separated list of template IDs to download. This value is valid only when `is_download` is **true.** |
| to\_date | string | The end of a search date range in UTC DateTime format. When you use this parameter, only templates created up to this date and time are returned.  **Note:** If this property is null, the value defaults to the current date. |
| used\_from\_date | string | Start of the search date range. Only returns templates used or edited on or after this date/time. If no value is specified, there is no limit on the earliest date used. |
| used\_to\_date | string | End of the search date range. Only returns templates used or edited up to this date/time. If no value is provided, this defaults to the current date. |
| user\_filter | string | Filters the templates in the response. Valid values are:   - `owned_by_me`: Results include only templates owned by the user. - `shared_with_me`: Results include only templates shared with the user. - `all`: Results include all templates owned or shared with the user. |
| user\_id | string | The ID of the user. |

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
