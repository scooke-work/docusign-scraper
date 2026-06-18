---
title: Upgrading from API v2.0 to v2.1
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/upgrading-v21/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Upgrading V21
scraped_at: '2026-06-18T20:28:08Z'
---

# Upgrading from API v2.0 to v2.1

The release of version 2.1 of the Docusign eSignature REST API brings a host of new features and usability improvements. For an overview, see [What's new in eSignature API v2.1](https://developers.docusign.com/docs/esign-rest-api/esign101/new-v21/). Check the [API reference](https://developers.docusign.com/docs/esign-rest-api/reference/) for details. Upgrading your existing integrations from v2.0 to v2.1 of the eSignature REST API gives you the opportunity to take advantage of these new capabilities, but changes in v2.1 may require you to update your code.

Changes appear in the following areas:

- The syntax of API calls and SDK methods
- The available parameters and their associated data types
- The structure or data types of the request or response objects

One example of a change that may require code updates is the improved standardization of return parameters. For example, v2.0 of the API returns some parameters as comma-separated strings, as shown in the following examples:

```
"envelopeEvents": ["Completed,Declined,Delivered,Sent,Voided"],
"recipientEvents": ["Completed,Declined,Delivered,Sent,AuthenticationFailed,AutoResponded"],
```

In v2.1, these parameters are separated into arrays of strings:

```
"envelopeEvents": ["Completed", "Declined", "Delivered", "Sent", "Voided"],
"recipientEvents": ["Completed", "Declined", "Delivered", "Sent", "AuthenticationFailed", "AutoResponded"],
```

This change improves usability because you no longer have to parse a long string to extract a single value, but it will break integrations that expect to parse such a string.

## Tab alignment

The placement of the **signHere** and **initialHere** tabs have changed for v2.1.

In v2 of the eSignature API, when you used fixed positioning for the **signHere** tab, the tab appeared 21 pixels *lower* on the final PDF document than the value you provided for the y-coordinate. To align the tab as expected, you had to subtract 21 pixels from the expected y-value (+0, -21) to make it appear where you expected during the signing view.

For the **initialHere** tab, you had to subtract 16 pixels from the expected y-value (+0, -16) to make it appear where you expected.

We have corrected these tab placement issues in v2.1 so that placement is much more accurate. However, as a result, when you migrate from v2 to v2.1 of the eSignature API, you will need to update your fixed tab coordinates by adding +21 back to the y-coordinate for the **signHere** tab and +16 back to the **initialHere** tab, since you will no longer need to account for the erroneous v2 downshifts for these tab types.

This image demonstrates the v2.0 (+0, -21) shift for **signHere** tab positioning in the signing view:

![v2.0 signHere tab positioning in the signing view](https://developers.docusign.com/img/fixed-tab-issue/signHerefixed-tab-shift-migration-annotated.png?v=2023080415)

This image demonstrates the v2.0 (+0, -16) shift for **initialHere** tab positioning in the signing view:

![v2.0 initalHere tab positioning in the signing view](https://developers.docusign.com/img/fixed-tab-issue/initialHere-fixed-tab-shift-migration-annotated.png?v=2023080415)

## Updating your code: Direct API calls vs. using an SDK

The changes to the eSignature REST API for version 2.1 will impact your integration differently depending on whether you called REST API endpoints directly or used one of the Docusign eSignature SDKs.

- [REST API](https://developers.docusign.com/docs/esign-rest-api/esign101/upgrading-v21/#rest-api)
- [SDKs](https://developers.docusign.com/docs/esign-rest-api/esign101/upgrading-v21/#sdks)

### Direct API calls

Integrations built by using direct calls to the REST API may break on endpoints that are affected by changes in v2.1. See the list of changes that may cause breaks below.

Use the following steps to upgrade your integration to v2.1:

- Test your integration to determine whether it is failing, and if so, on which API calls.
- Check the [API reference](https://developers.docusign.com/docs/esign-rest-api/reference/) to find out how to make the calls you need to the API v2.1 endpoints.
- Update your code to account for the API changes, recompile the code, and retest.> **Note:** With direct API integrations, calls to endpoints not affected by the v2.1 changes do not need to be updated. You can make calls to both API v2.0 and API v2.1 endpoints in the same integration.

**Endpoints that contain changes in Docusign eSignature REST API 2.1:**

| Category | Method Name | HTTP Method | Path |
| --- | --- | --- | --- |
| Accounts | `getAccountInformation` | GET | /{vx}/accounts/{accountId} |
| Accounts | `listBrands` | GET | /{vx}/accounts/{accountId}/brands |
| Accounts | `listSettings` | GET | /{vx}/accounts/{accountId}/settings |
| Accounts | `updateSettings` | PUT | /{vx}/accounts/{accountId}/settings |
| Accounts | `listSharedAccess` | GET | /{vx}/accounts/{accountId}/shared\_access |
| Accounts | `updateSharedAccess` | PUT | /{vx}/accounts/{accountId}/shared\_access |
| Billing | `getPlan` | GET | /{vx}/accounts/{accountId}/billing\_plan |
| Connect | `getConfiguration` | GET | /{vx}/accounts/{accountId}/connect/{connectId} |
| Connect | `listConfigurations` | GET | /{vx}/accounts/{accountId}/connect |
| Connect | `createConfiguration` | POST | /{vx}/accounts/{accountId}/connect |
| CustomTabs | `list` | GET | /{vx}/accounts/{accountId}/tab\_definitions |
| Envelopes | `deleteDocuments` | DEL | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/documents |
| Envelopes | `getDocument` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId} |
| Envelopes | `listDocuments` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/documents |
| Envelopes | `updateDocument` | PUT | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId} |
| Envelopes | `updateDocuments` | PUT | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/documents |
| Envelopes | `getEnvelope` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId} |
| Envelopes | `listStatusChanges` | GET | /{vx}/accounts/{accountId}/envelopes |
| Envelopes | `createEnvelope` | POST | /{vx}/accounts/{accountId}/envelopes |
| Envelopes | `update` | PUT | /{vx}/accounts/{accountId}/envelopes/{envelopeId} |
| Envelopes | `listStatus` | PUT | /{vx}/accounts/{accountId}/envelopes/status |
| Envelopes | `deleteLock` | DEL | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/lock |
| Envelopes | `getLock` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/lock |
| Envelopes | `createLock` | POST | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/lock |
| Envelopes | `deleteRecipient` | DEL | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId} |
| Envelopes | `deleteRecipients` | DEL | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients |
| Envelopes | `deleteTabs` | DEL | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs |
| Envelopes | `listRecipients` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients |
| Envelopes | `getRecipientSignature` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/signature |
| Envelopes | `listTabs` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs |
| Envelopes | `createRecipient` | POST | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients |
| Envelopes | `createTabs` | POST | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs |
| Envelopes | `updateRecipients` | PUT | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients |
| Envelopes | `updateTabs` | PUT | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/tabs |
| Envelopes | `getDocumentTabs` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/tabs |
| Envelopes | `getPageTabs` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/pages/{pageNumber}/tabs |
| Envelopes | `listTemplatesForDocument` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/documents/{documentId}/templates |
| Envelopes | `listTemplates` | GET | /{vx}/accounts/{accountId}/envelopes/{envelopeId}/templates |
| Folders | `listItems` | GET | /{vx}/accounts/{accountId}/folders/{folderId} |
| Folders | `list` | GET | /{vx}/accounts/{accountId}/folders |
| Folders | `moveEnvelopes` | PUT | /{vx}/accounts/{accountId}/folders/{folderId} |
| Folders | `search` | GET | /{vx}/accounts/{accountId}/search\_folders/{searchFolderId} |
| Groups | `deleteGroupUsers` | DEL | /{vx}/accounts/{accountId}/groups/{groupId}/users |
| Groups | `listGroups` | GET | /{vx}/accounts/{accountId}/groups |
| Groups | `listGroupUsers` | GET | /{vx}/accounts/{accountId}/groups/{groupId}/users |
| Groups | `createGroups` | POST | /{vx}/accounts/{accountId}/groups |
| Groups | `updateGroupUsers` | PUT | /{vx}/accounts/{accountId}/groups/{groupId}/users |
| Templates | `listDocuments` | GET | /{vx}/accounts/{accountId}/templates/{templateId}/documents |
| Templates | `getPageImages` | GET | /{vx}/accounts/{accountId}/templates/{templateId}/documents/{documentId}/pages |
| Templates | `deleteTabs` | DEL | /{vx}/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs |
| Templates | `listRecipients` | GET | /{vx}/accounts/{accountId}/templates/{templateId}/recipients |
| Templates | `listTabs` | GET | /{vx}/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs |
| Templates | `createTabs` | POST | /{vx}/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs |
| Templates | `updateRecipients` | PUT | /{vx}/accounts/{accountId}/templates/{templateId}/recipients |
| Templates | `updateTabs` | PUT | /{vx}/accounts/{accountId}/templates/{templateId}/recipients/{recipientId}/tabs |
| Templates | `getDocumentTabs` | GET | /{vx}/accounts/{accountId}/templates/{templateId}/documents/{documentId}/tabs |
| Templates |  | GET | /{vx}/accounts/{accountId}/templates/{templateId} |
| Templates | `ListTemplates` | GET | /{vx}/accounts/{accountId}/templates |
| Templates | `createTemplate` | POST | /{vx}/accounts/{accountId}/templates |
| Templates | `update` | PUT | /{vx}/accounts/{accountId}/templates/{templateId} |
| Users | `getInformation` | GET | /{vx}/accounts/{accountId}/users/{userId} |
| Users | `updateUser` | PUT | /{vx}/accounts/{accountId}/users/{userId} |
| Users | `getProfile` | GET | /{vx}/accounts/{accountId}/users/{userId}/profile |
| Users | `updateProfile` | PUT | /{vx}/accounts/{accountId}/users/{userId}/profile |
| Users |  | DEL | /{vx}/accounts/{accountId}/users |
| Users | `list` | GET | /{vx}/accounts/{accountId}/users |
| Users | `create` | POST | /{vx}/accounts/{accountId}/users |
| Users | `getSettings` | GET | /{vx}/accounts/{accountId}/users/{userId}/settings |
| Users | `updateSettings` | PUT | /{vx}/accounts/{accountId}/users/{userId}/settings |

### Using an SDK

We have also released new versions of our SDKs for the eSignature REST API v2.1. To upgrade your integration to API v2.1, you will need to adopt the latest version of your SDK.

Use the following steps to upgrade your integration to v2.1:

1. Upgrade to the latest version of the SDK using the package manager for your programming environment.
2. Recompile your integration using the new SDK version to see if any errors are generated.
3. Update your code to account for the changes, recompile the code, and retest.

**SDK version numbers:**

| Language | Latest version number for API 2.0 | Starting version number for API 2.1 |
| --- | --- | --- |
| C# | 3.3.0 | 4.0.0 |
| Node.js | 4.6.0 | 5.0.0 |
| Java | 2.14.0 | 3.0.0 |
| PHP | 4.2.0 | 5.0.0 |
| Python | 2.3.0 | 3.0.0 |
| Ruby | 2.3.0 | 3.0.0 |

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
