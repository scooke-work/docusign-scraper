---
title: Searching for envelopes
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/search/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Envelopes
- Envelopes
- Search
scraped_at: '2026-06-18T21:09:56Z'
---

# Searching for envelopes

Expanded by eSignature REST API 2.1

You can search precisely and flexibly for specific sets of envelopes by setting search filters and using the [Envelopes:listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/) endpoint or the `listStatusChanges` [SDK](https://developers.docusign.com/docs/esign-rest-api/sdks/) method.

You can retrieve envelopes using their specific ID or search by using any combination of the following filters:

**Important:** `to_date` and `from_date` are required parameters and must be included in every envelope search operation. They can be combined with any other search parameters or used alone for a date-range search.

| Filter | Search parameters | Description |
| --- | --- | --- |
| Parent folder | `folder_ids, folder_types, intersecting_folder_ids` | Inclusion by association with a specific folder (multiple folders can be specified by comma-separated list) or by folder type.  The `folder_ids` parameter allows you to specify any combination of IDs and folder types. Valid types are:  - `awaiting_my_signature` - `completed` - `draft` - `drafts` - `expiring_soon` - `inbox` - `out_for_signature` - `recyclebin` - `sentitems` - `waiting_for_others`  The `folder_types` parameter allows you to specify a subset of commonly used folder types:  - `inbox` - `sentitems` - `draft` - `templates` - `normal`  The `intersecting_folder_ids` parameter enables you to search for envelopes that are within two folders simultaneously. For example, an envelope might be in the `awaiting_my_signature` and `inbox` folders at once; this parameter lets you filter results to return only these envelopes, rather than all envelopes in both folders. You can specify any folder type, just as with `folder_ids`. |
| Contains text | `search_text` | Text strings that must be present in the email subject, email address, user name, email body, and/or the custom fields of returned envelopes. |
| Parent PowerForm | `power_form_ids` | Inclusion by association with a specific PowerForm ID or a comma-separated list of PowerForm IDs. |
| Current user | `user_filter` | Includes envelopes where the current user is the recipient, the sender, or is exclusively a recipient and not also the sender.  Possible values are:  - `sender` - `recipient` - `recipient_only` |
| User ID | `user_id` | Inclusion by association with the ID of a user in your account. All envelopes where the specified user is a recipient or sender will be included in the search. |
| Date range when the envelope status was changed | `from_date, to_date` | A range of dates within which the status of the returned envelopes was changed. |

You can also include or exclude additional metadata, including:

- Recipients, PowerForms and/or folders associated with the returned envelopes.
- Data on purged or deleted information associated with the returned envelopes.

Search results may also be ordered in ascending or descending order by any envelope property.

For details on these query parameters, see [Envelopes:listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/).

## Excluding result data

You can specifically exclude categories of data from being returned using an `exclude` request parameter and specifying recipients, PowerForms, or folders.

## Searching for envelopes in a specific folder

You can filter your envelope search to search only in specific folders by specifying a `folder_ids` request parameter and providing a comma-separated list of folder GUIDs (to search within only those folders) and/or a list of the following valid folder categories:

- `awaiting_my_signature`
- `completed`
- `draft`
- `drafts`
- `expiring_soon`
- `inbox`
- `out_for_signature`
- `recyclebin`
- `sentitems`
- `waiting_for_others`

## Searching for envelopes in a folder type

You can filter your envelope search to search only in folders of a specified type by providing a `folder_types` request parameter and providing a comma-separated list of the following valid folder categories:

- `normal`
- `inbox`
- `draft`
- `sentitems`
- `templates`

## Searching for specific text

You can search for envelopes that contain specific text strings using a `search_text` request parameter and specifying a string that all returned envelope text must contain. The envelope’s email subject, recipient user names, email addresses, and custom fields are all searched for the strings.

## Searching for envelopes associated with specific users

You can search for envelopes that are associated with a specific user ID (who may be a recipient or a sender) using the `user_id` request parameter and specifying the ID of a user within your account. All envelopes where that user is a recipient or sender will be searched.

## Next steps

- See [How to list envelope status changes](https://developers.docusign.com/docs/esign-rest-api/how-to/list-envelope-status-changes/) for a code example demonstrating how search for envelopes.
- See the MyAPICalls sample app scenario [Envelope Search with Resend](https://myapicalls.sampleapps.docusign.com/scenario/10), which walks you through a sequence of API calls that search for envelopes and resend an envelope returned in the results.

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
