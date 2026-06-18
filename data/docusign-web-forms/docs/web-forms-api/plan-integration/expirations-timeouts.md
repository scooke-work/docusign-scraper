---
title: Handle expirations and timeouts
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Handle expirations and timeouts
scraped_at: '2026-06-18T19:46:29Z'
---

# Handle expirations and timeouts

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

**Note:** This topic applies only to web form instances that are embedded in a web application or displayed via a redirect to the Docusign platform. The information does not apply to remote web form instances. See [When to use embedded or remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/) for information about the delivery methods.

Your application logic should handle several different types of expiration and timeout related to [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances):

- [Instance token expiration](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#instance-token-expiration)
- [Web form instance expiration](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#web-form-instance-expiration)
- [Web form inactivity timeout](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#web-form-inactivity-timeout)
- [Host website inactivity timeout](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#host-website-inactivity-timeout)

## Instance token expiration

When your application creates a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) via an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call, the response includes an instance token, which is the component of a [web form instance URL](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) that makes the URL unique and secure. The instance token expires after five minutes. You cannot change this expiration period. If your application tries to load a web form instance URL that includes an expired instance token, Docusign displays this message in the browser:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='141' width='250' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Unable to load form message](https://images.ctfassets.net/aj9z008chlq0/5HUhfgIJdgvL3rdMnVtvKp/544dc975f9df59cc76124a5b53a4460e/InstanceTokenExpiredMessage.png?w=250&h=141&q=50&fm=png)

To avoid the display of this message to a user, your application should check whether the instance token has expired before attempting to display the web form instance URL. The response to the `Instances:createInstance` request includes the instance token expiration time in the [tokenExpirationDateTime](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema_200_webforminstance_webforminstance_tokenexpirationdatetime) property, as shown below:

```
{
  "id": "4b26198f-xxxx-xxxx-xxxx-50ce0cf8924a",
  "formUrl": "https://apps-d.docusign.com/webforms/us/333fdc52xxxxxxxxxxxxxxxx24c6cc03",
  "instanceToken": "U2FsdGVkX18…PzkH8v7eFQ==",
  "tokenExpirationDateTime": "2023-11-22T15:00:20.852Z",
  "clientUserId": "1234-xxxx-xxxx-efgh",
  "formId": "9e5dbf14-xxxx-xxxx-xxxx-6163f2b5401a",
  "accountId": "4b65f24e-xxxx-xxxx-xxxx-3fb0f92931d4",
  "tags": [],
  "status": "INITIATED",
  "instanceMetadata": {
    "expirationDateTime": "2024-04-20T14:55:20.852Z",
    "createdDateTime": "2023-11-22T14:55:20.852Z",
    "createdBy": {
      "userId": "a2af44c8-xxxx-xxxx-xxxx-6edb18a3168b",
      "userName": "xxxxxxxx"
    },
    "lastModifiedDateTime": "2023-11-22T14:55:20.852Z"
  }
}
```

If the instance token has expired, your application can obtain a new one by making an [Instances:refreshToken](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/refreshtoken/) request or equivalent SDK method call. The refresh request must include the web form instance ID returned in the `id` property in the response to the `Instances:createInstance` request. The instance token obtained via the refresh request also has a five-minute expiration, and the new expiration time appears in the `tokenExpirationDateTime` property in the response. You can continue to refresh instance tokens for an instance until the [web form instance expires](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#web-form-instance-expiration).

You do not need to supply any request body values in the [Instances:refreshToken](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/refreshtoken/) request.

### Refresh token after form submission to render the envelope

After a user has submitted a web form instance (the [instance status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/#web-form-instance-status) is `SUBMITTED`), your application may need to refresh the instance token to render the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) that was generated on form submission. The [instance URL](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) that displayed the web form instance will display the envelope after form submission if the instance token is still valid and the web form instance has not expired. This applies only if the web form instance was generated from a template-based web form configuration; instances generated from standalone web form configurations do not trigger the creation of an envelope. See [Web form configuration type](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) for more information about the two types.

## Web form instance expiration

When your application creates a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) via an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call, it can set a web form instance expiration period in the [expirationOffset](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_expirationoffset) property. This value represents the number of hours until the web form instance expires. If an `expirationOffset` value is not supplied, Docusign uses a default value of 720 hours (30 days). The maximum allowed `expirationOffset` is 23976 (999 days).

Docusign uses the `expirationOffset` to calculate a web form instance expiration date and time, which appear in the [instanceMetadata.expirationDateTime](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema_200_webforminstance_webforminstance_instancemetadata_expirationdatetime) property in the response to the `Instances:createInstance` request. You can also obtain the instance expiration time by making an [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) or [Instances:listInstances](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/listinstances/) request or equivalent SDK method call.

### How expiration affects web form instances and envelopes

After a web form instance has expired, a user can no longer access or submit the instance. In addition, for instances created from [template-based web form configurations](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/), the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) that is generated on web form instance submission will no longer be accessible using the [web form instance URL](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/).

If your application attempts to render a web form instance URL after the instance has expired, the web form instance UI displays the message **Unable to load form**. To prevent this, your application should make sure that the `instanceMetadata.expirationDateTime` has not elapsed before attempting to render an instance URL.

If your application displays a web form instance for a user before the `instanceMetadata.expirationDateTime`, but the user submits the web form instance after the expiration time, the submission will fail, and the instance UI will display a **Form not submitted** message.

To render a web form instance for a user after the instance has expired, your application must create a new web form instance via an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call.

### Web form instance status change at expiration time

The [status](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/#schema_200_webforminstance_webforminstance_status) of an unsubmitted web form instance changes to `EXPIRED` when the `instanceMetadata.expirationDateTime` arrives. If a user has already submitted the web form instance when the expiration time arrives, the web form instance status remains `SUBMITTED` and does not change to `EXPIRED`.

### Relationship between web form instance expiration and token expiration

The relationship between the web form instance expiration and the [instance token expiration](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#instance-token-expiration) is as follows:

- Instance tokens expire five minutes after they are generated. If a user attempts to access a web form instance URL containing an expired token, Docusign displays an error.
- Your application can issue [Instances:refreshToken](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/refreshtoken/) API requests or equivalent SDK method calls to obtain a new token for the web form instance until the instance expires. After that, refresh requests for the instance will result in an error response, and your application must create a new web form instance for the user.

## Web form inactivity timeout

If your web application loads a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) in a user's browser and the user doesn't type or click in the form for 20 minutes, the form instance UI will time out. If your application uses the [Docusign JS](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls) client SDK, it will receive a `sessionEnd` [event](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) of type `sessionTimeout` when an inactivity timeout occurs. Any data that a user entered in the web form instance prior to the timeout will be lost.

To reload the web form instance after an inactivity timeout, your application must obtain a new instance token by making an [Instances:refreshToken](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/refreshtoken/) request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call and supplying the instance ID in the request, since the [instance token expiration](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#instance-token-expiration) will have elapsed. It should then use the new token to create a [web form instance URL](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) and load it.

## Host website inactivity timeout

If your web application embeds [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) in a host website, user activity in the iframe that displays the web form instance may not be detected by the host website. This may cause the host website to time the user session out for inactivity.

To avoid this, your application can use the [Docusign JS](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls) client SDK to embed the web form instance and create a listener to monitor for the `userActivity` JavaScript [event](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events). This event is triggered when a user clicks or types in the web form instance iframe.

If the host website times a user session out before the user submits the web form instance, the iframe will close and any data that the user entered in the form will be lost. Your application can reload the form instance for the user after the user logs in to the host website again, but the application may need to refresh the instance token via an [Instances:refreshToken](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/refreshtoken/) API request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call first if the [instance token expiration](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#instance-token-expiration) has elapsed.

## Next steps

- See the options for [rendering embedded web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/).
- Learn about [web form instance and envelope status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/).

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
