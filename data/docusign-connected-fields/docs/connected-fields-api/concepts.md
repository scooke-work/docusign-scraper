---
title: Connected Fields API concepts
source_url: https://developers.docusign.com/docs/connected-fields-api/concepts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Connected Fields API
- Connected Fields API
- Concepts
scraped_at: '2026-06-18T18:25:43Z'
---

# Connected Fields API concepts

The Connected Fields API enables you to perform real-time programmatic custom data verification for values in your eSignature envelopes. The API provides an endpoint, [TabInfo:GetConnectedFieldsTabGroups](https://developers.docusign.com/docs/connected-fields-api/reference/connectedfields/tabinfo/getconnectedfieldstabgroups/), which returns the full definitions of your *connected fields*: every field type whose data can be verified using one of your account’s [Extension apps](https://developers.docusign.com/extension-apps/). 

Your app can call this endpoint to get the types of data that can be verified, then map these connected fields to your envelope fields (also known as [Tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/)) before you send it. When your recipient enters data in these fields, the extension apps associated with the connected field will verify that data in real time and display a response.

For example, you can verify user-supplied values in an eSignature envelope to authorize a transfer in a financial account. Each envelope value can be mapped to a property in your system of record. When a user completes the required envelope fields, Docusign sends your system a verification request that includes the values. Your system can apply its verification logic and return the result in its response to Docusign, which then displays the result to the user.

To verify custom data programmatically with the Connected Fields API, you must first create a [Connected fields](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/) or **data verification** extension app. If your account has neither extension, the [TabInfo:GetConnectedFieldsTabGroups](https://developers.docusign.com/docs/connected-fields-api/reference/connectedfields/tabinfo/getconnectedfieldstabgroups/) method will not return any data types.

For connected fields extension apps, you must:

- Implement the data verification rules that your system will enforce on the *connected fields* (the field types that can be verified by one or more of the extensions defined for your account)
- Define mappings for your data types to Docusign data types
- Install and connect a connected fields or data verification extension
- Create the messages that will be shown for success or when error conditions are found.

See [Transform logic](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#transform-logic) for details on how to map your data types to the [Concerto](https://concerto.accordproject.org/docs/intro/) format that Docusign uses. See [External system logic to return data model with verification markers](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#external-system-logic-to-return-data-model-with-verification-decorators) and [External system logic to process verification requests](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#external-system-logic-to-process-verification-requests) for guidance on setting up your system to work with a connected fields extension app.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1415' width='1405' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A diagram showing the execution flow for a Connected Fields API data verification flow.](https://images.ctfassets.net/aj9z008chlq0/1SQ9H6BllP43Yl0NmwPtdd/7a8ac869afc2e8e0e50bff22dce4de0a/Connected_Fields_API_diagram__1_.png?w=1405&h=1415&q=50&fm=png)

To verify supported generic fields, you must install and connect a data verification extension app. See [Install Docusign Apps for Data Verification](https://support.docusign.com/s/document-item?language=en_US&bundleId=qki1698158012210&topicId=pyp1698158616536.html) for details.

Once your connected fields or data verification extension app and your external system logic are implemented, send connected field data to be verified programmatically using the following steps:

### 1. Call the Connected Fields API endpoint

Call the Connected Fields API endpoint, [TabInfo:GetConnectedFieldsTabGroups](https://developers.docusign.com/docs/connected-fields-api/reference/connectedfields/tabinfo/getconnectedfieldstabgroups/). This method returns the full models of all of your connected fields (the data structures used by your system of record and mapped in your connected fields extension app).

Note that, unlike the Connected Fields UI, the Connected Fields API endpoint returns only fields that are either mandatory or have the **IsRequiredForVerifyingType** [decorators](https://concerto.accordproject.org/docs/design/specification/model-decorators)**.**

### 2. Extract the data from the response

Extract the data from this response needed to create corresponding fields (also called [Tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/)) in your envelope. This code shows example properties returned for both generic fields (used by data verification extensions) and custom fields (used by connected fields extensions).

1

2

3

4

5

6

7

8

9

10

11

12

13

14

{

"appId": "ae832a12-xxxx-xxxx-xxxx-aa85f5d64159",

"tabs": [

{

"extensionData": {

"extensionGroupId":

"2018f518-xxxx-xxxx-xxxx-fa039570f643",

"actionInputKey": "accountNumber",

"publisherName": "John Doe",

"applicationName": "File Archive and

Verification",

"actionContract": "Contracts.Actions.

Verify.Version1.BankAccountOwner",

"extensionName": "My Bank Account Owner

Verification Extension",

"actionName": "My Bank Account Owner

Verification Action",

"extensionContract": "Contracts.Extensions.

Verify.Version1.BankAccountOwner",

"extensionPolicy": "None",

### 3. Create the envelope definition

Create the envelope definition. When defining your fields, provide this type and extension app data in a tab’s `extensionData` property to mark it as a connected field whose values will be verified.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

{

"emailSubject": "Please sign this document",

"documents": [

{

"documentBase64": "' > "$request\_data"

cat $doc1\_base64 >> $request\_data

printf '",

"name": "Lorem Ipsum",

"fileExtension": "pdf",

"documentId": "1"

}

],

"status": "sent",

"recipients": {

"signers": [

{

"email": "'"${SIGNER\_EMAIL}"'",

"name": "'"${SIGNER\_NAME}"'",

"recipientId": "1",

"routingOrder": "1",

### 4. Verify data

When the recipient enters data into a tab marked as a connected field, that data will be sent to an external system for verification (or to your system of record, for custom field verification). For custom field verifications, these values will be evaluated against the verification rules that you have defined for that data type, and the success or failure message that you have defined for its category will be shown.

See [How to send an envelope with extension app data verification fields](https://developers.docusign.com/docs/connected-fields-api/send-envelope-with-data-verification-fields/) for a detailed walkthrough on how to programmatically send an envelope that verifies custom data, or [Connected fields in Docusign envelopes](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#connected-fields-in-docusign-envelopes) for an overview of the process to manually send an envelope using the eSignature user interface.  **Note**: Connected fields are not currently supported in Docusign Maestro.

The following sections describe the objects and key terms used by the Connected Fields API.

### Connected fields

A connected field is a field whose type is mapped to a corresponding object type in your system of record. The values for this type can be verified by data verification or connected fields extensions defined in your account. You can verify the inputs to your connected fields by creating a connected fields extension app and defining the verification logic on your system of record (for custom data models) or using a data verification extension app (for supported standard data models).

### Connected fields extension app

A connected fields extension app is required to verify custom field values. See [Connected fields](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/) for details.

### Custom data verification

Custom data verification is a feature, provided by the Connected Fields API, that enables you to implement verification logic for custom fields, rather than only for fields that map directly to data verification extensions, such as [Bank account verification](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/bank-account-verification/).

### Data verification extension app

A data verification extension app is required to verify supported generic field values. See [Supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) for details and a list of supported types.

## Next steps

- See [How to send an envelope with extension app data verification fields](https://developers.docusign.com/docs/connected-fields-api/send-envelope-with-data-verification-fields/) for a detailed walkthrough of how to send an envelope and validate the values of its connected fields.
- Learn about [Extension apps](https://developers.docusign.com/extension-apps/) and the [Connected fields](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/) extension.
- See [Transform logic](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#transform-logic) for details on how to map your data types to the [Concerto](https://concerto.accordproject.org/docs/intro/) format that Docusign uses.
- See [External system logic to return data model with verification markers](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#external-system-logic-to-return-data-model-with-verification-decorators) and [External system logic to process verification requests](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#external-system-logic-to-process-verification-requests) for guidance on setting up your system to work with a connected fields extension app.

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
