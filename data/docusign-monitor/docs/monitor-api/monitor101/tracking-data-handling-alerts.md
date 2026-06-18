---
title: Tracking data and handling alerts
source_url: https://developers.docusign.com/docs/monitor-api/monitor101/tracking-data-handling-alerts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Monitor API
- Monitor API
- API 101
- API 101
- Tracking Data Handling Alerts
scraped_at: '2026-06-18T21:15:04Z'
---

# Tracking data and handling alerts

You can get activity tracking information for your organization by calling the Docusign Monitor API [DataSet:getStream](https://developers.docusign.com/docs/monitor-api/reference/monitor/dataset/getstream/) endpoint. This endpoint enables you to download your organization’s data in segments specified by a cursor (a bookmark value returned by a previous `DataSet:getStream` operation). You can use the resulting dataset to integrate the Monitor API with your existing SIEM software tools and apps.

- In the development (demo) environment, the endpoint is:
  `https://lens-d.docusign.net/api/v2.0/datasets/monitor/stream?cursor={{cursorValue}}&limit={{queryLimit}}`

- In the production environment, the endpoint is:
  `https://lens.docusign.net/api/v2.0/datasets/monitor/stream?cursor={{cursorValue}}&limit={{queryLimit}}`

## Using cursor values

When you call the [DataSet:getStream](https://developers.docusign.com/docs/monitor-api/reference/monitor/dataset/getstream/) endpoint, you can supply two parameters, `cursor` and `limit`, that determine the subset of the monitoring data that will be returned in the response JSON.

**Note:** To call the Monitor API endpoint, you must have obtained an access token using JWT authentication. See [Authentication](https://developers.docusign.com/docs/monitor-api/monitor101/auth/) for details.

| Name | Description |
| --- | --- |
| `cursor` | A `string` query parameter that specifies the place in your monitoring data from which the request will begin gathering records. Your app can use `cursor` to keep its place while iterating through monitoring records in a way similar to how you might use a bookmark to keep your place while reading chapters of a book. Whenever you successfully call the Monitor API endpoint, the response will include an `endCursor` value which you can use to create the `cursor` for your next request, enabling you to chunk your downloads as you examine large numbers of event and alert records.  Calls that do not specify a `cursor` will begin retrieving records starting seven days ago.  If data is needed beginning at a certain point in time, `cursor` can be specified as an ISO DateTime string value (such as 2022-01-01T00:00:00Z) instead of a cursor query string. In this case, data will be retrieved beginning from that DateTime. The earliest data available in the system is from 2021-01-01.  Docusign does not return all available data in response to a single request. Your integration should iterate through the dataset using a series of API calls, with each one requesting data starting from the `cursor` value and the subsequent request starting from the `endCursor` in the response.  **Note:** If a request returns no data, your integration should continue iterating using `cursor` and `endCursor` until data is returned. To avoid throttling, do not make requests more frequently than once per minute.  Not required. Defaults to 0. |
| `limit` | An `Int32` query parameter that specifies the maximum number of records (up to 2000) to be returned in the response. Not required. Defaults to 1000.  This parameter enforces a maximum number of records returned but does not guarantee a minimum number of records. |

After a successful call, a set of JSON event and alert records is returned, including an `endCursor` metadata property.

| Name | Description |
| --- | --- |
| `endCursor` | A `string` value that specifies the place at which the monitoring data in the current response ended.   Use the value of `endCursor` to begin your next query from this spot in your records. |

1

2

3

4

5

6

7

8

declare -a Headers=('--header' "Authorization:

Bearer {ACCESS\_TOKEN}" \

'--header' "Accept: application/

json" \

'--header' "Content-Type:

application/json")

curl --request GET

https://lens-d.docusign.net/api/v2.0/datasets/

monitor/stream?limit=1 \

"${Headers[@]}" \

## Next steps

- Review the event and alert objects in the [API reference](https://developers.docusign.com/docs/monitor-api/reference/)
- See [best practices for handling alerts](https://developers.docusign.com/docs/monitor-api/monitor101/best-practices-handling-alerts/)
- See [how to get monitoring data](https://developers.docusign.com/docs/monitor-api/how-to/get-monitoring-data/)

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
