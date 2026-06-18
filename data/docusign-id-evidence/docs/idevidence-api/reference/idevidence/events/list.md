---
title: ': list'
source_url: https://developers.docusign.com/docs/idevidence-api/reference/idevidence/events/list/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:43:33Z'
---

[API Reference](https://developers.docusign.com/docs/idevidence-api/reference/idevidence/events/list/)[API Explorer](https://developers.docusign.com/docs/idevidence-api/reference/idevidence/events/list/?explorer=true)

[Events](https://developers.docusign.com/docs/idevidence-api/reference/idevidence/events/)

# : list

Returns a list of events for a specific recipient. You can filter the results by specifying additional criteria.
**Note**: This method supersedes the older `GET /api/v1.0/events/{entityType}/{entityId}` request. If you're still using the old `GET` request, we highly recommend you switch to this method.

### Related topics

- [How to retrieve ID Evidence events](https://developers.docusign.com/docs/idevidence-api/how-to/retrieve-idevidence-events/)
- [How to retrieve ID Evidence media](https://developers.docusign.com/docs/idevidence-api/how-to/retrieve-idevidence-media/)

## Request

#### HTTP Request

GET

```
/restapi/api/v1.0/events/{entityType}/{entityId}.{format}
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| entityType \* | string | The type of the entity (for example room, user or envelope). ID Evidence only supports the `person` (recipient) entity type. Optional. |
| entityId \* | string | The id of the Docusign entity. Optional. |
| format \* | string | The format of the content in the response. ID Evidence supports the following format and extensions:   - JSON (json) - PDF (pdf)   Note: if you choose the PDF format, ID Evidence applies a digital signature to the file to guarantee the origin and integrity of data. |
| version \* | string | The requested API version |

| Query Parameters |  |  |
| --- | --- | --- |
| actor\_id | string | *This parameter is not used with ID Evidence.* |
| from\_date | string | Retrieves all the events created from the specified date. This date is inclusive. If empty, then all the events created up until the *to\_date* value are returned. |
| to\_date | string | Retrieves all the events created until the specified date. This date is inclusive. If empty, then all the events created from the from\_date are returned. |
| include\_media | boolean | Indicates whether you want to include the media in the response. The media depends on the event returned by the ID Evidence API. For example, ID Evidence can return the capture of the ID uploaded for verification. Note that including the media in the response may carry a large amount of data. If set to *false*, then the request returns a link that you can use later with the Get Media request to retrieve the media file. |
| page\_index | integer | The index position of the currently displayed page. |
| page\_size | integer | The number of records to display on a page. |

\* Required

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
