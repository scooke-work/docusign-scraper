---
title: Connected fields extension overview
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- Connected Fields
scraped_at: '2026-06-18T19:51:49Z'
---

# Connected fields extension overview

The connected fields extension enables you to perform real-time custom data verification of values entered in eSignature [envelopes](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=gso1578456465211.html). Unlike the data verification [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), which verify specific types of values (such as bank account numbers and addresses), the connected fields extension can verify any data against your organization’s system of record.

For example, you can use a connected fields extension to verify user-supplied values in an eSignature envelope to authorize a transfer in a financial account. Each envelope value can be mapped to a property in your system of record. When a user completes the required envelope fields, Docusign sends your system a verification request that includes the values. Your system can apply its verification logic and return the result in its response to Docusign, which then displays the result to the user.

In the response, your system also supplies custom messages that provide users with specific guidance about the information they must enter. In addition, your system can return autofill values for the envelope based on known information about a user.

In the current release, Docusign will display field labels and messages in the signing UI in the language in which the external system provides them. In a future release, translation to other languages will be supported.

Because connected fields extensions verify organization-specific data, they are useful for [private extension apps](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/). Private extension apps can be developed and published for use by specific accounts or within your organization. This contrasts with public extension apps, which are available for all Docusign customers to view and install.

## Connected fields in Docusign envelopes

After a connected fields extension app has been [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to a Docusign account, the fields it implements are available for custom data verification in envelopes created in the account. Expand the sections below to see how connected fields function during envelope preparation and signing.

## Create envelopes with connected fields programmatically

To create envelopes that include connected fields programmatically, use these API requests:

- Connected Fields API [TabInfo:GetConnectedFieldsTabGroups](https://developers.docusign.com/docs/connected-fields-api/reference/connectedfields/tabinfo/getconnectedfieldstabgroups/) request: Retrieves information about the connected fields extension apps installed and connected to your account, and the required connected fields associated with each extension app.
- eSignature REST API [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) request: Creates envelopes that can include connected fields from the extension apps installed to your account

See [Connected fields concepts](https://developers.docusign.com/docs/connected-fields-api/concepts/) for an overview of the API, and see [How to send an envelope with extension app data verification fields](https://developers.docusign.com/docs/connected-fields-api/send-envelope-with-data-verification-fields/) for example code and a detailed walkthrough.

## Verification results

To retrieve verification results programmatically, you can use [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/) and implement a listener to receive the `extension-executed` event. This event is supported only with the [JSON SIM event model](https://developers.docusign.com/platform/webhooks/connect/json-sim-event-model/). See [JSON SIM event reference](https://developers.docusign.com/platform/webhooks/connect/json-sim-event-model/#json-sim-event-reference) for the event structure.

Verification results are also included in the [envelope history](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=dpr1578456338693.html), shown in this figure, and the [certificate of completion](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=gpa1578456339545.html).

![](data:image/svg+xml;charset=utf-8,%3Csvg height='788' width='1740' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Envelope history showing connected fields verification results](https://images.ctfassets.net/aj9z008chlq0/1sqPUrGC9CqGZgfxDDZX0E/cebbae7026b9f53b85e9d3e0080c59a6/EnvelopeHistory.png?w=1740&h=788&q=50&fm=png)

## Connected fields actions

A connected fields extension implements these [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/):

| Action | Executed when | Description |
| --- | --- | --- |
| [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names) | The extension app establishes or refreshes a connection. This can be triggered by:   - Running a [connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) from the Developer Console Testing module - Creating or refreshing a connection in the App Center. See [Manage Docusign App Connections](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=xyw1716318604389.html)﻿ for details. | Gets the names of the types that are used by your system of record.  In the [extension app manifest](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/), this action is identified as `DataIO.Version6.GetTypeNames`.  The connected fields extension uses the data IO extension’s **Get Type Names** action contract because the contract details are identical. |
| [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) | The extension app establishes or refreshes a connection. This action is executed directly after **Get Type Names**. | Gets a set of type definitions from your system of record and returns their equivalents in the [Concerto](https://concerto.accordproject.org/docs/intro/) data model format.  Docusign uses the Concerto data model to map the data from your system of record. If your system of record does not already use the Concerto data model, you must implement transform logic that defines how your records map to Concerto data types before they can be read. This transform logic should be implemented within your **Get Type Definitions** action, and is called whenever the action is executed. See [Data model](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/) for details on the structure.  In the extension app manifest, this action is identified as `DataIO.Version6.GetTypeDefinitions`.  The connected fields extension uses the data IO extension’s **Get Type Definitions** action contract because the contract details are identical. |
| [Verify](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#verify) | A recipient of a Docusign envelope populates all required connected fields, and when a user modifies a value in any required connected field. | Sends user-populated connected field values from an envelope to the external system for verification.  The external system applies verification logic to the values and returns a response to Docusign indicating whether verification passed or failed. The response must include success or failure messages that are displayed in the signing UI. The response can also provide suggested values to be autofilled in the fields.  In the extension app manifest, this action is identified as `ConnectedFields.Version1.Verify`. |

## Get Type Names and Get Type Definitions flow

When your connected fields extension app is [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to a Docusign account, or when a connection is [refreshed](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=qkv1716320270335.html) in the Docusign App Center, the extension app will automatically get the types and type definitions of the objects that your system of record is configured to expose:

1. Docusign calls [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names) to get the set of types that your system of record exposes. The types are returned as a JSON object that includes the name, label, and an optional description for each type.
2. Docusign calls [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions), inputting the types returned by **Get Type Names**. This returns the definitions of each type that your system of record exposes for Docusign.

After the Docusign platform receives the type definitions, it will display the corresponding connected fields in the eSignature [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html) for users in your account. This enables template and envelope preparers to include the connected fields in documents that will be sent to your customers.

**Important**: Docusign models data input and output definitions using a flexible schema in [Concerto](https://concerto.accordproject.org/docs/intro/). If your system of record does not already use the Concerto data model, you must implement logic to convert your type definitions into Concerto format as part of your response to the **Get Type Definitions** call.

See [Data model](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/) for recommendations on mapping types or [Concerto specification](https://concerto.accordproject.org/docs/category/specification) for details on specific types, syntax, and examples.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1736' width='1288' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Get Type Names and Definitions diagram](https://images.ctfassets.net/aj9z008chlq0/27P7XUE5ogJ2r15wvbPDOo/b33d5ef3766b92b26f850363c595347b/GetTypeNamesDefinitionsDiagram.png?w=1288&h=1736&q=50&fm=png)

## Verify flow

The [Verify](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#verify) action is executed when a user completes all required connected fields in a Docusign envelope or updates a required connected field value:

1. The **Verify** request is sent to the system of record. The request body is a JSON object that includes key-value pairs representing property names and user-populated values from the envelope, as well as a type name and a unique key that the external system can use to identify duplicate requests.
2. The external system applies any required business logic to verify the user-populated values.
3. The external system sends a response to Docusign indicating the verification result, suggested values if appropriate, and a message for the user.
4. Docusign displays the verification result, accompanying message, and any suggested values used to autofill fields in the envelope signing view.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1630' width='1163' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Connected fields Verify action diagram](https://images.ctfassets.net/aj9z008chlq0/5B2hQKSGvmEyMudCHZQlgJ/f11337a2658977f3f5a20e9a245a6fb7/VerifyDiagram.png?w=1163&h=1630&q=50&fm=png)

## Plan a connected fields extension implementation

When planning the implementation of a connected fields extension, you’ll need to consider the following:

- [eSignature envelope field mapping to data source properties](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#esignature-envelope-field-mapping-to-data-source-properties)
- [External system logic to return data model with verification markers](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#external-system-logic-to-return-data-model-with-verification-decorators)
- [External system logic to process verification requests](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#external-system-logic-to-process-verification-requests)

### eSignature envelope field mapping to data source properties

Identify eSignature envelope fields whose values are to be verified, and determine which external data source properties they can be verified against. For the example case described in [Connected fields in Docusign envelopes](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#connected-fields-in-docusign-envelopes), the mapping might be:

| eSignature document field | External data source property |
| --- | --- |
| Account Number | `account_num` |
| Source Fund | `source_fund` |
| Destination Fund | `destination_fund` |
| Amount to Transfer | `balance` |
| Transfer Date | `transferDate` |
| Send Destination Fund Prospectus | `prospectus` |
| Type of Account | `typeOfAccount` |
| Owner Email | `email` |
| Account Owner Name | `ownername` |

When planning the mapping of external data source properties to Docusign envelope fields, keep in mind that each data type returned in a [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) response will be automatically rendered as one of the supported envelope field types. See [Transform logic](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#transform-logic) for details.

### External system logic to return data model with verification decorators

Your external system must be able to return the information Docusign needs to determine which values can be sent to your system for verification. The two requests that Docusign will send to retrieve this information are:

- [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names): Retrieves a list of objects in the data source.
- [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions): Retrieves definitions of the properties in the data source. This response must include decorators that mark objects as verifiable and indicate which properties are required for verification.

See the [connected fields extension contract](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/) for details about the request formats and the expected response formats. See [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) for guidance about transforming requests and responses to the correct format.

### External system logic to process verification requests

Your system must implement logic to verify user-entered envelope values according to your business requirements. For example, if Docusign sends an account owner name, account number, source fund for a transfer, destination fund, and transfer amount, your system might evaluate whether:

1. The account owner name matches the owner on record for the supplied account number.
2. The account has a position in the source fund supplied.
3. The source fund balance is greater than or equal to the transfer amount.
4. All of your organization’s other requirements for the transfer have been met.

For details about the format of the verification request that Docusign sends and the required format for the response, see the [Verify](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#verify) action contract. See [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) for guidance about transforming requests and responses to the correct format.

## Next steps

- See [Connected fields extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/) for details about the action requests and responses.
- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- Learn more about [private extension apps](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/), which are available only to specified Docusign accounts.

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
