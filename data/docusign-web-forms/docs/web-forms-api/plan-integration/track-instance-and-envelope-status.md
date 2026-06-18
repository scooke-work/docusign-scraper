---
title: Track web form instance and envelope status
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Track web form instance and envelope status
scraped_at: '2026-06-18T19:46:29Z'
---

# Track web form instance and envelope status

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

When your application makes an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call to create a new [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances), the response includes a unique web form instance ID in the `id` property. The ID is a GUID. You can use this instance ID to:

- Track [web form instance status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/#web-form-instance-status)
- Retrieve the ID of the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) that is associated with the web form instance, in order to track [envelope status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/#envelope-status). Envelopes are not generated for instances created from standalone configurations. See [Web form configuration type](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) for more information about the two types.

## Web form instance status

A [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) includes an overall [status](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema_200_webforminstance_webforminstance_status/) property that reflects the current state of the form as a whole.

Valid values for `status` are:

- `INITIATED`: The web form instance has been created but the user has not submitted it yet.
- `INPROGRESS`: The user selected the [Finish Later](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=uwd1725382029336.html) button after partially filling out a web form instance. The form field values have been saved so that the user can resume filling out the form at another time.
- `SUBMITTED`: The user has filled out and submitted the web form instance.
- `EXPIRED`: The [instanceMetadata.expirationDateTime](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema_200_webforminstance_webforminstance_instancemetadata_expirationdatetime) for the web form instance has passed without a submission, and the web form instance is no longer accessible. This status is not applicable to remote web form instances. See [Web form instance expiration](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#web-form-instance-expiration) for more information.
- `FAILED`: Instance processing failed.

## Recipient status for web form instances

In addition to the overall status of a web form instance, web form instances also include an [instanceRecipientStatus](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema_200_webforminstance_webforminstance_recipients_instancerecipientstatus/) property. This property indicates the user’s progress towards completing their view of the web form instance.

Valid values of `instanceRecipientStatus` are:

- `INITIATED`: The web form instance has been created for the user.
- `INPROGRESS`: The user has opened the web form but has not submitted it yet. This status includes cases where the user has saved their progress to complete the web form later.
- `SUBMITTED`: The user has completed and submitted their view of the web form instance.

You can retrieve both the overall web form instance status and the recipient-specific status through the response to an [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) request, which returns information for a specific instance; an [Instances:listInstances](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/listinstances/) request, which returns information for all instances created from a web form configuration; or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method calls.

## Envelope status

Envelopes are generated for web form instances created from template-based web form configurations only. See [Web form configuration type](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) for more information.

The ID of the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) associated with a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) appears in the `envelopes` array in the response to the [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) and [Instances:listInstances](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/listinstances/) requests and equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method calls. For remote web form instances, the envelope is generated when the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request is processed. For embedded web form instances, the envelope is generated when the first user submits the web form instance. See [When to use embedded or remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/) for details.

Below is an `Instances:getInstance` response with an `envelopes` array:

```
{
  "id": "48ed96ea-xxxx-xxxx-xxxx-d2747a67c6ee",
  "clientUserId": "1234-xxxx-xxxx-efda",
  "formId": "9e5dbf14-xxxx-xxxx-xxxx-6163f2b5401a",
  "accountId": "4b65f24e-xxxx-xxxx-xxxx-3fb0f92931d4",
  "tags": [],
  "status": "SUBMITTED",
  "instanceMetadata": {
    "expirationDateTime": "2025-08-20T06:24:15.269Z",
    "createdDateTime": "2025-08-20T18:24:15.269Z",
    "createdBy": {
      "userId": "a2af44c8-xxxx-xxxx-xxxx-6edb18a3168b",
      "userName": "xxxx"
    },
  "instanceSource": "API_REMOTE",
  "lastModifiedDateTime": "2025-08-20T18:25:43.615Z",
  "lastModifiedBy": {
       "userId": "a2af44c8-xxxx-xxxx-xxxx-6edb18a3168b",
       "userName": "xxxx"
    }
  },
  "webFormRecipients": [
    {
       "recipientViewId": "41f3109b-xxxx-xxxx-xxxx-eac994ad0988",
        "instanceRecipientStatus": "INITIATED",
        "roleName": "signer"
    }
  ],
  "envelopes": [
    {
        "id": "ceb7fca9-xxxx-xxxx-xxxx-76cc37c8ca98",
        "createdDateTime": "2025-08-20T15:57:03.653Z"
     }
  ]
}
```

You have several options for tracking envelope status:

- If your application uses the [Docusign JS](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls) client SDK, your application receives JavaScript [events](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) triggered by envelope activity. These events only reflect envelope activity for the web form instance submitter. To track envelopes for additional recipients, use one of the options listed below. Note that this option only applies to [embedded web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/).
- Use a [Docusign Connect](https://developers.docusign.com/platform/webhooks/connect/) listener to subscribe to receive envelope updates. When envelope status changes, Docusign Connect will send the listener an event.
- Use the eSignature [Envelopes:listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/) request or an equivalent SDK method call. See [How to list envelope status changes](https://developers.docusign.com/docs/esign-rest-api/how-to/list-envelope-status-changes/) for a walkthrough and code examples.

## Next steps

- See [Retrieve submitted web form instance values](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/) for information about obtaining user-entered values to write to your system of record.
- [Learn about remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/#learn-about-remote-web-form-instance-delivery).
- See [Redirect users after form submission](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/) for an overview of options for routing a user to a web page after the user submits a web form instance.

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
