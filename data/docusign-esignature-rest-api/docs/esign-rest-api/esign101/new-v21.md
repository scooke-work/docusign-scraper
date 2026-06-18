---
title: What's New in eSignature API v2.1
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/new-v21/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- New V21
scraped_at: '2026-06-18T20:28:08Z'
---

# What's New in eSignature API v2.1

Version 2.1 of the Docusign eSignature API includes usability updates, new features, and better tools for handling large workloads and bulk operations. It is an incremental but substantial update to the existing v2.0 eSignature API.

## Improved usability

Improving usability is a major goal of the v2.1 API. Many API responses now return more useful and standardized sets of data, and you are now able to customize what data is returned by many requests, based on your needs. New URL parameters such as `include={data}`, `exclude={data}`, and `include_metadata` help you minimize the number of API calls that you need to make to get all the information you need (and less information that you don’t).

Many properties throughout the API now have a corresponding *Metadata* properties that indicate whether the property has additional options, or if it is editable. Where possible, parameters have been standardized to string format, and objects that used comma-separated string formats (such as some properties within Tab, Envelope, and Template objects) have been converted to string array format to make development smoother and easier.

## Envelope search

Version 2.1 of the Docusign eSignature API introduces new filters and capabilities for envelope search that enable you to search precisely and flexibly for specific sets of envelopes and tailor search functionality to use our API to build UI functionality for your applications. You can now filter your search results by providing parameters that specify attributes (such as text, a common folder, or a common user involved in the signing process) that all returned envelopes must have.

You can also include or exclude additional metadata from the returned envelope data, including:

- The recipients, PowerForms and/or folders associated with the returned envelopes.
- Data on purged or deleted information associated with the returned envelopes.

Search results may also be ordered in ascending or descending order by any envelope property.

See [Searching for Envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/search/) for details.

## Bulk sending envelopes

The ability to bulk send envelopes (or to send copies of an envelope to a list of recipients) has been extensively updated in version 2.1 of the API. You can now customize the envelope to be sent to multiple recipients (per copy), use custom fields (tabs), perform validation checks to ensure that your list of recipients is valid, and use the full range of Docusign capabilities that apply to non-bulk sending such as authentication, embedded signing, and customized messages.

These updates are summarized in the following table:

| **Bulk Send in the v2.0 API** | **Bulk Send in the v2.1 API** |
| --- | --- |
| Can use envelopes | Can use envelopes and templates |
| Single recipient per envelope | Multiple recipients per envelope |
| Only recipient name and email can be customized | Each recipient in each envelope can be individually customized just as you would in a normal envelope send operation, including capabilities such as:     - [Identity Authentication Methods](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/) such as access code, SMS authentication, and IDV - Embedded signing - Customized tab values - Customized email messages |
| No validation | Optional pre-send validation check |
| Custom fields are not supported | Custom fields are supported |

See [Bulk Sending Envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/bulk-send/) for details.

## Managing and sharing templates

Templates are now organized within folders, which group similar templates together and allow you to share groups of templates with other users, rather than sharing them one-at-a-time.

You can share your templates (either a single template or a folder containing one or more templates) with:

- An account, specified by `accountId`
- A user, specified by `userId`
- A group, specified by `groupName`

**Note:** If you choose to share a template folder with one or more users, accounts, or groups, any new templates you later add to that folder will also be automatically shared.

See [Sharing templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/sharing/) for details.

## CC recipient commenting

Carbon Copy (CC) Recipients may now make and respond to comments in the documents belonging to the envelopes that they are sent. A new object, [Comment](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/comments/), has been added to contain their comment data.

Each comment may be up to 500 characters. See [Comment](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/comments/) for details.

## Witness recipient identity authentication

A new type of recipient Identity Authentication, witness authentication, has been added. This method of authentication requires that you create a recipient with the new witness type, who must be viewing each document as it is signed.

To use witness authentication:

1. Create at least one recipient in your envelope and assign the new `witness` type to it.
2. Set the envelope to use the `witness` type of recipient authentication.
3. During the signing workflow, each recipient that is assigned the `witness` type must view the documents in the envelope after they are signed.

Typically, a witness will be in the same room as the signer but this guidance is not enforced by Docusign.

## API object model updates

Many properties throughout the API now have a corresponding *Metadata* properties that indicate whether the property has additional options, or if it is editable. For example, the `name` property may have a `nameMetadata` property that indicates whether the name is editable.

The Document, Envelope, Tab, Recipient, User, and Template API endpoints have been updated to improve usability and support new capabilities, as outlined by the following table:

| **Object** | **Updates in API v2.1** |
| --- | --- |
| Documents, Templates, and Envelopes | **New endpoint query parameters:**   - `include_metadata`: Enables you to include sets of metadata in the response when getting documents. When this parameter is **true**, responses will include metadata fields. Note that you cannot include metadata for template responses. - `shared_user_id`: Enables you to impersonate a shared inbox user to retrieve their view of a list of documents. - `documents_by_userid`: Enables you to order documents by their user IDs when getting a list of documents. For example, if a user is included in two different routing orders with different visibilities, using this parameter returns all of the documents from both routing orders. - `recipient_id`: Enables an envelope sender to retrieve documents as though they were one of the recipients. The `documents_by_userid` parameter must be **false** to retrieve documents in this way.   **New capabilities:**   - Document endpoints that add documents to get documents from an envelope may now be passed an Envelope object, rather than just an ID. - Encoded unicode characters in document file names are now supported when adding or updating a document, if a Content-Disposition header is included. - Calls that retrieve document data now return a new Pages object (which contain Ids, sequence numbers, height, width, and DPI information for each page in the document) rather than a count of the total number of pages. - All comma-separated value properties have been changed to string arrays. |
| Recipients | **New endpoint query parameters:**    - `include_metadata`: Enables you to include sets of metadata in the response when getting documents. When this parameter is **true**, responses will include object metadata fields. Note that you cannot include metadata for template responses. - `Include_tab_count`: For operations to get recipient data, enables you to specify that the response will also include data on the total number of tabs assigned to the recipient.   **New capabilities:**    - CC recipient types have a new tabs property that holds their Comments. These objects contain the data for each comment left by the CC recipient. - In-person (embedded) signers may now have their name set in two properties, `signerFirstName` and `signerLastName`. - Notary hosts may now be set as a signing group. - Operations to get recipient data now also return a `RecipientType` property denoting the types of each recipient. - Docusign now tracks how many times each recipient has been through a signing completion for that envelope with a new property, `completedCount`. If the value of this property is more than 0 for a signing group, only the user who previously completed signing may sign again. - A new type of recipient authentication, `witness`, has been added. This type of recipient authentication requires that a specified recipient (who must have the `witness` type) must be view the signed documents before it can be completed. |
| Tabs | **New endpoint query parameters**:   - `include_metadata`: Enables you to include sets of metadata in the response when getting tabs. When this parameter is **true**, responses will include object metadata fields.   **New capabilities:**   - New metadata properties have been created to contain metadata for many existing tab properties that indicate whether the sender can edit that property. - A new tab type, [PolyLineOverlay](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/get/#polyLineOverlayTabs), is now available. This tab type enables users to strike out text on a document. |
| User | **New capabilities:**    - The `userSettingsInformation` object has been expanded to contain additional user setting information related to PowerForm access, permissions, time zone/locale, commenting, and metadata. |

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
