---
title: Connected fields extension contract reference
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- Extension Contracts
- Extension Contracts
- Connected Fields
scraped_at: '2026-06-18T19:51:51Z'
---

# Connected fields extension contract reference

The connected fields extension enables you to verify user-entered values in eSignature [envelopes](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=gso1578456465211.html) against a system of record. The verification result and message from the external system, as well as suggested autofill values, are displayed in the signing UI.

You can include this extension when you [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). If you register the extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), select the **Connected Fields** extension in the form-based UI, as shown in this figure:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='535' width='645' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Registering a connected fields extension app](https://images.ctfassets.net/aj9z008chlq0/jvdUNWvK8d7JgeNTzpdFC/6e393167747af47bd23ff0280b21a2c2/FormBasedRegistration_ConnectedFields.png?w=645&h=535&q=50&fm=png)

If you register the extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/), set the `extensions.template` value in your app manifest to `ConnectedFields.Version1.ConnectedFields`.

This extension has three actions. The action names you specify when you register an extension app depend on whether you register the app using a form or using an app manifest file. The app manifest file values listed here appear in the `actions.template` property.

| Form-based action name | App manifest file value |
| --- | --- |
| Get Type Names | `DataIO.Version6.GetTypeNames` |
| Get Type Definitions | `DataIO.Version6.GetTypeDefinitions` |
| Verify | `ConnectedFields.Version1.Verify` |

For details about what each action does and when it is invoked, see [Connected fields actions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/#connected-fields-actions). The connected fields extension uses the data IO extension’s **Get Type Names** and **Get Type Definitions** action contracts because the contract details are identical.

You provide the details required for action execution when you register an extension app. See [Update extension and action settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings) for information about defining actions using the form-based registration process. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action properties in the app manifest file.

## Action contracts

## Error handling

If a connected fields action results in an error that prevents the request from being processed, the external system should return an HTTP error code 400, 404, or 500 along with a message describing the error.

Do not return one of these errors if the verification logic was executed and identified one or more user-entered values as invalid. In that case, return a [Verify](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#verify) response with the `verified` property set to `false`, and supply appropriate values for the `verifyResponseMessage` and `verifyFailureReason` properties.

Example error responses:

```
HttpErrorCode: 404
{
   code: NOT_FOUND
   message: Type Address does not exist in the system.
}
```

```
HttpErrorCode: 400
{
   code: BAD_REQUEST
   message: Missing required property account_num.
}
```

```
HttpErrorCode: 500
{
   code: INTERNAL_SERVER_ERROR
   message: Unknown error when trying to verify values.
}
```

This error structure applies to all actions. Developers are responsible for providing a code and message for each error.

### Retry logic

If Docusign receives a 500 Internal Server Error in response to an action request, it implements retries as follows:

- Docusign resends the request up to three times.
- For a [Verify](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#verify) request retry, the `idempotencyKey` is the same as in the original request, so that the external system can identify it as a resubmitted request.
- After the third retry fails, Docusign considers the request to have failed.
- If Docusign does not receive a response to a request within 15 seconds, up to three retries are launched before the request is considered a failure.

## Next steps

- Get an [overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/) of the connected fields extension and how it can be used.
- Find out more about the [data model](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/).
- Explore the options for [testing](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) a connected fields extension app.

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
