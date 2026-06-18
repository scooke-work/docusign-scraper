---
title: ': createCorrect'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createcorrect/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:44Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createcorrect/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createcorrect/?explorer=true)

[EnvelopeViews](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/)

# : createCorrect

Returns a URL that enables you to embed the envelope sender view of the Docusign UI. You can customize the appearance of the view via the settings request attribute. You can embed the view in an iframe.

**API request update**

The request object for this API method was updated in June 2024. The new API request format is described below. Existing applications must update to the new version; it solves a security issue with the old version. The deprecation schedule has been announced in the [Docusign Core Release Notes](https://support.docusign.com/s/document-item?language=en_US&bundleId=adp1720620778794_24-2-02-00-demo&topicId=wcz1616195757589.html&_LANG=enus). While backwards compatibility will be provided for a while for existing applications, all applications must be updated to be secure. See below for migration information.

**Best practices**

The returned URL expires after 10 minutes. Therefore, request the URL immediately before you redirect your user to it.

Due to screen space issues, do not use an iframe for embedded operations on mobile devices. For mobile applications, use a [WebView](https://developer.android.com/reference/android/webkit/WebView) (Android) or [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) (iOS).

## Customizing the user experience

By default, the view includes two pages: the **Prepare** and **Tagger** pages. The settings object is used to control the user experience. For example, to limit the user to the **Tagger** page, and not allow the user to change the recipient information:

- `"startingScreen": "Tagger"`
- `"showBackButton": "false"`
- `"showEditRecipients": "false"`

Use the [Embedded Views Test Too](https://docusign.github.io/app-examples/embedded-views-v2/) to try the different UX controls. Some UI settings attributes are not yet implemented.

### The envelope must be in the correct state for the Embedded View

To use the Correct View, the envelope **must** be in the `sent` or `delivered` state. Otherwise, a 400 error will be returned with an error message in the response body:

```
{
    "errorCode": "ENVELOPE_INVALID_STATUS",
    "message": "Invalid envelope status. Correct view cannot be created for an envelope in a Created state."
}
```

### Modifying the envelope after redirection

If you set `"sendButtonAction": "redirect"` or `"backButtonAction": "redirect"`, and your app will modify the envelope before or after the view completes, you must lock the envelope before the API call and provide the lock as the lockToken attribute in the API request object.

Delete the lock token after the browser has been redirected to your application.

### Closing the view's iframe

If you choose to embed the view in your application via an iframe, Docusign recommends this software pattern to close the iframe after the view has completed:

- (One time) create a standalone return page that you will use as the `returnUrl` target for the view. The view will redirect the iframe to this URL when it has completed. Here's an [example return page](https://github.com/docusign/docusign.github.io/blob/master/jsfiddleDsResponse.html). In this page, use JavaScript and the [postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) method to send a message to your application with the results of the view.
- In your application, use `window.addEventListener("message", function_name)` to register a listener for incoming messages.
- To show the view, use this API method, then set the iframe to load the URL from the API response.
- In your application, receive the completion message, validate it, and then close the iframe.

### Information security

This view only has write access to the specific envelope referenced in the API call. It also has read access to templates and other secondary information that a user can access to modify the envelope. The read access corresponds to the access rights of the user associated with the access token used for the API call.

> **Recommendations:**
>
> - Use the access token of a service user who can access the templates appropriate for your use case.
> - Do not use the access token of a user with administrator privileges.

## Migrating to the current version of the request object

This section only applies to existing applications that use the older version of the request object.

Migrating from the old API request object to the new version will take under a day of developer time.

**Step 1.** Does your application set the `returnUrl` attribute?

Yes: continue with step 2.

No: In this case, your users first update the envelope, and then the Docusign eSignature home screen is shown. To accomplish this UI pattern with the new API request format:

- Set the `returnUrl` to a new endpoint for your application. You can use query parameters or session data to manage state. Remember to authenticate the incoming requests.
- When the new endpoint is called, use the [EnvelopeViews:createConsole](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createconsole/) API call to obtain and then display the Docusign eSignature home page to your application's user.

**Step 2.** Does your application modify the default UI of the view?

No: continue with step 3.

Yes: With the new API request object, UI controls for the view are now set when you make the API call via the `settings` attribute.

- Note the UI settings your application is currently modifying by adding and updating query parameters on the URL *returned* by the API method.
- Using the reference documentation below, create a settings object that accomplishes your UI goals. You can use the [Embedded Views Test tool](https://docusign.github.io/app-examples/embedded-views-v2/) to check your UI settings. Note that the `settings` object includes multiple objects and subobjects for various UI settings.
- **Delete the code** in your application that modifies and adds query parameters to the URL returned by the API. With the new API format, your application will not make any changes to the returned URL. Exception: If you set the view's locale specifically, that is still accomplished by appending the `locale` query parameter.

**Step 3.** Is the envelope always in the right state before you call the Embedded View?

If your software may try to create the Embedded View when the envelope is not in the right state (see above), then you must add additional checks and logic to prevent this.

**Step 4.** Check that these API attributes are set:

- `"viewAccess" = "envelope"`
- The `returnUrl` is set

**Step 5.** All done! Test your application.

## Request

#### HTTP Request

POST

```
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/correct
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| envelopeId \* | string | The envelope's GUID.  Example: `93be49ab-xxxx-xxxx-xxxx-f752070d71ec` |

\* Required

## SDK Method

### Envelopes::createCorrectView

## Request Body

## Responses

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
