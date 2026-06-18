---
title: Retrieve submitted web form instance values
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Retrieve submitted web form instance values
scraped_at: '2026-06-18T19:46:29Z'
---

# Retrieve submitted web form instance values

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

After a user has filled out a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) and submitted it, your application can retrieve the form field values and write them to a backend system. See these topics for details:

- [Options to detect that a web form instance has been submitted](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/#options-to-detect-that-a-web-form-instance-has-been-submitted)
- [Request that retrieves web form instance values](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/#request-that-retrieves-web-form-instance-values)
- [Retrieve attachments that users upload](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/#retrieve-attachments-that-users-upload)
- [Form instance property that identifies users](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/#form-instance-property-that-identifies-users)

## Options to detect that a web form instance has been submitted

Your application can detect that a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) has been submitted in two ways:

- If your application uses the [Docusign JS](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls) client SDK to render the web form instance, it can implement a listener for events that are triggered on form instance submission. See [Form and envelope events](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) for details. [How to create and embed a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-embed-web-form-instance/) has listener sample code. Docusign JS only applies to embedded web form instances.
- Responses to the [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) and [Instances:listInstances](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/listinstances/) API requests and equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method calls include a `status` property whose value will be `SUBMITTED` after a user has submitted a web form instance. The `submittedDateTime` in the `Instances:listInstances` and `Instances:getInstance` response indicates the submission date and time. See [Form instance property that identifies users](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/#form-instance-property-that-identifies-users) for an example response.

## Request that retrieves web form instance values

Your application can retrieve a list of the form field names and values at the time of [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) submission via an [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) API request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call. The submitted field values appear in the `formValues` object in the response. For example:

```
"formValues": {
  "name": "Sally Signer",
  "email": "sally.signer@email.com",
  "phone_num": {
    "countryCode": "55",
    "nationalNumber": "1133301000"
  },
  "birth_date": "1980-12-10",
  "salary": 121000,
  "marital_status": "single",
  "education": "advanced",
  "alerts": [
    "Funds_withdrawn",
    "Account_info_changed"
  ]
},
```

For form fields whose values are saved as [envelope custom fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#envelope-custom-fields), the values at the time of form instance submission are included in the `Instances:getInstance` response's `formValues` object. You can also retrieve the envelope custom field values via the eSignature API [EnvelopeCustomFields:list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopecustomfields/list/) request or an equivalent [SDK](https://developers.docusign.com/docs/esign-rest-api/sdks/) method call.

## Retrieve attachments that users upload

A [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) can include [attachment fields](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=oyz1722621351928.html) that enable users to upload files when filling out [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances). The uploaded files are appended as documents to the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) that Docusign generates on web form instance submission.

Attachment fields are supported with template-based web form configurations but not with standalone web form configurations or remote web form instances. See [Web form configuration type](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) for details.

To retrieve files uploaded in attachment fields, use these API requests or equivalent SDK method calls:

1. [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) or [Instances:listInstances](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/listinstances/): Returns the envelope ID in the `envelopes` array.

   **Note:** The requests in the next two steps are [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/) requests.
2. [EnvelopeDocuments:list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/list/): Returns a list of all documents in the envelope, including the files uploaded in attachment fields. In the response, you can identify files uploaded in attachment fields by the format of the `name` property, which will look like this:
   `"name": "__identification__certificate.pdf",`

   The first component of the value, which is enclosed in double underscores, is the attachment field's **API reference name** as displayed in the [Properties panel](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=wor1676501633875.html) of the Web Forms builder. This value also appears as the `componentName` in the [form field definition](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#form-field-definitions) in the [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) response. After the second pair of underscores, the name of the file that the user uploaded appears with a .pdf extension. All uploaded files are converted to PDF format.

   The `EnvelopeDocuments:list` response includes a document ID for each document associated with an envelope.
3. [EnvelopeDocuments:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/get/): Downloads documents associated with an envelope. You can either retrieve a specific document by referencing the `documentId` returned in the `EnvelopeDocuments:list` response, or retrieve all documents in the envelope.

## Form instance property that identifies users

When you create a new [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) by making an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call, you supply a [clientUserId](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_clientuserid) that is a unique identifier for the user who will fill out the form instance. After form instance submission, you can use the `clientUserId` to identify the customer record in your backend system that your application will update with data collected from the form instance. The `clientUserId` appears in the responses to the [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) and [Instances:listInstances](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/listinstances/) requests and equivalent SDK method calls. See [Identify web form instance users](https://developers.docusign.com/docs/web-forms-api/plan-integration/identify-instance-users/) for more information.

For remote web form recipients, a `clientUserId` is not required to identify the recipient. However, it can still be useful for tracking the primary recipient associated with the web form instance. Recipients are identified by their `roleName`, which ensures the correct participant is mapped to each role in the web form. 

To locate web form instances created for a specific user, use a `client_user_id` query parameter with the `Instances:listInstances` request. For example:

`https:// apps-d.docusign.com/api/webforms/v1.1/accounts/{accountId}/forms/{formId}/instances?client_user_id=1234-xxxx-xxxx-efda`

If the response includes multiple form instances with the same `clientUserId` in a `SUBMITTED` status, check the `instanceMetadata.lastModifiedDateTime` to identify the most recent form instance submission. Below is a sample portion of an `Instances:listInstances` response with two form instances submitted by the same user.

```
{
  "id": "9fb1a4c1-xxxx-xxxx-xxxx-97b816652150",
  "clientUserId": "1234-xxxx-xxxx-efda",
  "formId": "9e5dbf14-xxxx-xxxx-xxxx-6163f2b5401a",
  "accountId": "4b65f24e-xxxx-xxxx-xxxx-3fb0f92931d4",
  "tags": [
    "tag1",
    "tag2"
  ],
  "status": "SUBMITTED",
  "instanceMetadata": {
    "expirationDateTime": "2024-05-17T15:20:12.535Z",
    "createdDateTime": "2023-12-19T15:20:12.535Z",
    "createdBy": {
      "userId": "a2af44c8-xxxx-xxxx-xxxx-6edb18a3168b",
      "userName": "xxxx"
    },
  "lastModifiedDateTime": "2023-12-19T15:20:57.446Z"
  },
  "envelopes": [
    {
        "id": "df4b9a5f-xxxx-xxxx-xxxx-2e73a296a903"
    }
  ]
},
{
  "id": "48ed96ea-xxxx-xxxx-xxxx-d2747a67c6ee",
  "clientUserId": "1234-xxxx-xxxx-efda",
  "formId": "9e5dbf14-xxxx-xxxx-xxxx-6163f2b5401a",
  "accountId": "4b65f24e-xxxx-xxxx-xxxx-3fb0f92931d4",
  "tags": [
    "tag3",
    "tag4"
  ],
  "status": "SUBMITTED",
  "instanceMetadata": {
    "expirationDateTime": "2024-01-14T06:24:15.269Z",
    "createdDateTime": "2024-01-11T18:24:15.269Z",
    "createdBy": {
      "userId": "a2af44c8-xxxx-xxxx-xxxx-6edb18a3168b",
      "userName": "xxxx"
    },
  "lastModifiedDateTime": "2024-01-11T18:25:43.615Z"
  },
  "envelopes": [
    {
        "id": "ceb7fca9-xxxx-xxxx-xxxx-76cc37c8ca98"
    }
  ]
},
```

Once you've identified a user's most recently submitted web form instance, include its `id` in an `Instances:getInstance` request to retrieve the form field values from that form instance submission.

The previous example also includes sample values for the [tags](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_tags) object, which you can populate in an `Instances:createInstance` request to associate metadata with a web form instance to help your application identify it.

## Next steps

- See [Prefill web form instance fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) for information about populating a web form instance with known information about users.
- Read about your options to [redirect users after form submission](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/).

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
