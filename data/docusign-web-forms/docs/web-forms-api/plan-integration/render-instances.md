---
title: Render embedded web form instances
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Render embedded web form instances
scraped_at: '2026-06-18T19:46:29Z'
---

# Render embedded web form instances

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

**Note:** This topic applies only to web form instances that are embedded in a web application or displayed via a redirect to the Docusign platform. The information does not apply to remote web form instances. See [When to use embedded or remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/) for information about the delivery methods.

Your application has two options for rendering [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances):

- [Use the Docusign JS client SDK library](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls) to embed web form instances in the web application.
- [Redirect users' browsers](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#redirect-to-web-form-instance-urls) to web form instance URLs.

Regardless of which option you choose, your application must use the Web Forms API [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request or an equivalent server-side [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call to create web form instances before rendering them.

## Use Docusign JS to render web form instance URLs

Docusign JS is a JavaScript client SDK that enables you to embed [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) in your web application. Docusign JS creates an iframe in which the web form instance is displayed and loads the web form instance URL that your application passes to it. You can access the Docusign JS libraries here:

- Developer environment: <https://js-d.docusign.com/bundle.js>
- Production: <https://js.docusign.com/bundle.js>

Docusign JS features include:

- A unified experience for users that makes the web form instance appear as if it's hosted on your website
- A focused view display of the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) that Docusign generates after a user submits a web form instance, if the instance was created from a [template-based](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/#instance-processing-template-based-web-form-configurations) web form configuration. Focused view eliminates some of the Docusign signing UI components, further contributing to a seamless user experience. Focused view is not available if the web form configuration [Initiate signing session from email](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) setting is enabled.
- Display customization options that can be set using the [webFormOptions object](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#webformoptions-object)
- The ability to apply any CSS style property to the iframe, such as width, height, and border size
- [Form and envelope events](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) that your application can use to trigger actions

Although it is possible to create your own iframe and embed the web form instance URL in it, Docusign recommends using Docusign JS instead. Without it, your application will not be able to take advantage of its display customization options or focused view.

### webFormOptions object

The Docusign JS `webFormOptions` object enables you to customize the web form instance display in your web application and define other settings. The properties of `webFormOptions` are listed below. See [How to create and embed a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-embed-web-form-instance/) for sample code that includes a `webFormOptions` object.

| Property | Type | Default value | Description |
| --- | --- | --- | --- |
| `autoResizeHeight` | boolean | `true` | If `true`, the iframe height is adjusted automatically to display the entire form. If `false`, the iframe height is fixed based on the values supplied in the iframe style properties, and a vertical scrollbar appears if the form height exceeds the iframe height. |
| `dismissWidgetOnSessionEnd` | boolean | `true` | If `true`, the iframe is automatically deleted when a `sessionEnd` event is triggered. See [Form and envelope events](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#form-and-envelope-events) for a list of `sessionEnd` event types. If `false`, the iframe is not deleted automatically and remains open until your web application deletes it. |
| `hideProgressBar` | boolean | `false` | If `true`, a progress bar is not displayed at the top of the web form instance. The screenshot on [Web Forms API 101](https://developers.docusign.com/docs/web-forms-api/web-forms-101/) shows the progress bar. If `false`, the progress bar is displayed. |
| `hideWelcomePage` | boolean | `false` | If `true,` the web form configuration [welcome page](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=nhh1674600364930.html) is not displayed. If `false`, the welcome page is displayed. |
| `instanceToken` | string |  | An identifier that is appended to a [web form instance URL](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) to make it unique and secure. This value is returned by the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or an equivalent server-side [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call. |
| `prefillValues` | a set of key/value strings |  | An optional list of form fields and values with which to prefill them.  In each key/value pair, the key is the `componentName` from the [form field definition](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#form-field-definitions). For dropdowns, radio buttons, and checkboxes, the values your application supplies must be allowed for the field. See [Identify permitted values for dropdowns, radio buttons, and checkboxes](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#identify-permitted-values-for-dropdowns-radio-buttons-and-checkboxes) for more information.  Below is a sample `prefillValues` definition that prefills the set of form fields shown in the example [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request in [Supply prefill values in the request to create a web form instance](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/#supply-prefill-values-in-the-request-to-create-a-web-form-instance):    ``` prefillValues: {   name: 'Sally Signer',   email: 'sally.signer@email.com',   ['phone_num.countryCode']: '55',   ['phone_num.nationalNumber']: '1133301000',   salary: '121800.55',   birth_date: '1980-12-18',   marital_status: 'single',   education: 'advanced',   alerts: 'Funds_withdrawn,Account_info_changed' }, ```   If form field values are supplied in the Docusign JS `prefillValues` property, they override prefill values supplied in the `Instances:createInstance` request or an equivalent server-side [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call. See [Prefill values override web form configuration defaults](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/#prefill-values-override-web-form-configuration-defaults) for details. |
| `showFinishLater` | boolean | `false` | If `true`, the web form instance UI includes a [Finish Later](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=uwd1725382029336.html) button that enables users to save a partially filled out form instance. Selecting **Finish Later** causes Docusign to save the form instance with any user-populated values. To enable a user to finish filling out the form, your application can render the form instance URL after [refreshing the instance token](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#instance-token-expiration), and Docusign will automatically populate the saved form values. If `false`, users will not have the option to save a partially filled out form instance and complete it later. |
| `useFocusedViewForSigning` | boolean | `true` | If `true`, the envelope that is generated on submission of a web form instance is presented in a focused view, which includes only the agreement to be signed and a navigation button. If `false`, the standard signing UI is displayed. |

### Form and envelope events

Docusign JS enables you to set up listeners that can receive these events. See [How to create and embed a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-embed-web-form-instance/) for sample code that includes listeners.

| Event | Type | Triggered when |
| --- | --- | --- |
| `ready` |  | Your web application loads a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances). |
| `userActivity` |  | A user types or clicks inside the iframe that displays a web form instance.  By default, the host website in which the iframe is embedded cannot detect user actions in the iframe. This may cause the host website to time the user session out for inactivity while the user is filling out the web form instance. By monitoring this event, your application can detect user activity in the web form instance and avoid timing out the user session. See [Host website inactivity timeout](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#host-website-inactivity-timeout) for additional information. |
| `submitted` |  | A user successfully submits a completed web form instance to Docusign. |
| `signingReady` |  | The envelope signing view is loaded in a user's browser after the user submits a web form instance.  This event is triggered only if both of the following are true:  - The web form instance was generated from a [template-based](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) web form configuration. - The web form configuration's [Initiate signing session from email](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) setting is not enabled.   This event is triggered only for the user who submits the web form instance. See [Envelope status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/#envelope-status) for options for tracking the status for additional envelope recipients. |
| `sessionEnd` | `finishLater` | A web form instance submitter selects the [Finish Later](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=uwd1725382029336.html) button after partially filling out a web form instance.  When a user selects **Finish Later**, the form field values are saved so that the user can resume filling out the form at another time. |
| `sessionEnd` | `signingResult` | A web form instance submitter completes or ends an envelope signing process. This event type can be triggered even if the submitter has not signed the envelope. See the section **The event status parameter** on the [EnvelopeViews:createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) page for a list of completion statuses that can trigger this event.  This event is triggered only if both of the following are true:  - The web form instance was generated from a [template-based](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) web form configuration. - The web form configuration's [Initiate signing session from email](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) setting is not enabled.   This event is triggered only for the web form instance submitter. See [Envelope status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/#envelope-status) for options for tracking the status for additional envelope recipients. |
| `sessionEnd` | `remoteSigningInitiated` | A user submits a web form instance, and an envelope is generated for email delivery to the user.  This event is triggered only if both of the following are true:  - The web form instance was generated from a [template-based](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) web form configuration. - The web form configuration's [Initiate signing session from email](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) setting is enabled.   This event is triggered only for the web form instance submitter. See [Envelope status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/#envelope-status) for options for tracking the status for additional envelope recipients. |
| `sessionEnd` | `formConfirmation` | A user submits a web form instance that was generated from a [standalone](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) web form configuration. This event is not triggered for web form instances generated from [template-based](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) web form configurations. |
| `sessionEnd` | `sessionTimeout` | Due to 20 minutes of user inactivity, a form instance session expires. See [Web form inactivity timeout](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#web-form-inactivity-timeout) for details. |

## Redirect to web form instance URLs

For this option, your application constructs [web form instance URLs](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) and redirects users' browsers to them. Users will see that they are being routed from your website to the Docusign platform, which displays the web form instances. See [Form submission after a redirect to the Docusign platform](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/#form-submission-after-a-redirect-to-the-docusign-platform) for a description of what happens after a user submits a web form instance.

## Next steps

- Learn more about [web form instance expiration](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/#web-form-instance-expiration).
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
