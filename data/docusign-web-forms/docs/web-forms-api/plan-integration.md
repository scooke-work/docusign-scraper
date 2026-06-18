---
title: Plan a Web Forms API integration
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
scraped_at: '2026-06-18T19:46:29Z'
---

# Plan a Web Forms API integration

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

Before you begin work on an application that creates and manages [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances), consider how the application will implement Web Forms API features and processes. See the table below for a list.

**Note:** The table indicates whether items are applicable to embedded and remote web form instance delivery. See [When to use embedded or remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/) for an overview of the differences in delivery methods.

| Feature or process | Applicable to embedded delivery | Applicable to remote delivery |
| --- | --- | --- |
| [Authentication](https://developers.docusign.com/docs/web-forms-api/plan-integration/#authenticate) | Yes | Yes |
| [Identifying the web form configuration](https://developers.docusign.com/docs/web-forms-api/plan-integration/#identify-the-web-form-configuration) from which to create web form instances | Yes | Yes |
| [Identifying users](https://developers.docusign.com/docs/web-forms-api/plan-integration/#identify-users) who fill out web form instances | Yes | Yes |
| [Customizing the appearance and behavior](https://developers.docusign.com/docs/web-forms-api/plan-integration/#customize-instance-and-envelope-appearance-and-behavior) of web form instances and envelope | Yes | Yes |
| [Prefilling web form instance fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/#determine-which-form-field-values-will-be-prefilled) | Yes | Yes |
| [Constructing web form instance URLs](https://developers.docusign.com/docs/web-forms-api/plan-integration/#construct-web-form-instance-urls) | Yes | No |
| [Handling expiration](https://developers.docusign.com/docs/web-forms-api/plan-integration/#handle-instance-token-and-web-form-instance-expiration) of instance tokens and web form instances | Yes | No |
| [Rendering web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/#determine-how-your-application-renders-web-form-instances) using a URL with an instance token | Yes | No |
| [Delivering web form instances via email](https://developers.docusign.com/docs/web-forms-api/plan-integration/#deliver-web-form-instances-via-email) | No | Yes |
| [Tracking the status](https://developers.docusign.com/docs/web-forms-api/plan-integration/#track-the-status-of-web-form-instances-and-envelopes) of web form instances and envelopes | Yes | Yes |
| [Retrieving form data after submission](https://developers.docusign.com/docs/web-forms-api/plan-integration/#retrieve-form-data-after-submission) | Yes | Yes |
| [Redirecting users after form submission](https://developers.docusign.com/docs/web-forms-api/plan-integration/#define-the-web-page-to-display-after-form-submission) | Yes | Yes |

## Authenticate

Before making any Web Forms API requests, your application must obtain an access token via one of the supported OAuth 2.0 grant types: Authorization Code Grant, Implicit Grant, or JSON Web Token (JWT) Grant.

See [Authentication](https://developers.docusign.com/docs/web-forms-api/plan-integration/authentication/) for details.

## Identify the web form configuration

When creating web form instances for users to fill out, your application must supply the ID of the [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) from which the instances are to be created. The web form configuration defines the form structure and the form data that will be available to your application. If the web form configuration is [template-based](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/#instance-processing-template-based-web-form-configurations), each web form instance has an associated [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) for the user to review and sign after form instance submission. For [standalone](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/#instance-processing-standalone-web-form-configurations) web form configurations, envelopes are not generated. The web form configuration must be [created](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=euk1665093155272.html) and [activated](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=iri1669070601520.html) before your application can create instances from it.

See [Retrieve web form configuration details](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/) for an overview of the web form configuration properties that your application can obtain via Web Forms API requests.

## Identify users

Before creating a Web Forms API integration, consider which value from your backend system the integration will use to uniquely identify users who fill out web form instances. Your application can also use this value to retrieve data from your system of record and prefill form fields with known information about users, as well as write data back to the system of record.

See [Identify web form instance users](https://developers.docusign.com/docs/web-forms-api/plan-integration/identify-instance-users/) for details.

## Customize instance and envelope appearance and behavior

Your Web Forms API integration can use the branding feature to customize the appearance and behavior of web form instances and their associated envelopes. You can create a brand in your Docusign account, define visual elements such as a logo and colors, and set behavior such as a URL to which users are routed after completing an envelope. Once you have defined a brand, you can apply it at the web form configuration level or the web form instance level.

See [Apply custom branding](https://developers.docusign.com/docs/web-forms-api/plan-integration/apply-custom-branding/) for details.

## Determine which form field values will be prefilled

The request to create a web form instance enables you to supply values that will be populated in the form fields when the web form instance loads in a user's web browser. For instances created from [template-based](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/#instance-processing-template-based-web-form-configurations) web form configurations, you can also prefill [envelope custom fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#envelope-custom-fields) that can be used for classification and reporting. You'll need to determine which form field values to prefill and implement logic for setting their values. Prefilling form field values is optional.

See [Prefill web form instance fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) for more information.

## Construct web form instance URLs

**Note:** This process is not applicable to [remote web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/).

If your API integration displays web form instances by embedding them in your web application or redirecting users to the Docusign platform, it must obtain the components of each instance's secure, unique URL and combine them in the required format.

See [Web form instance URLs](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) for details.

## Handle instance token and web form instance expiration

**Note:** This process is not applicable to [remote web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/).

When your application creates a web form instance for a user to fill out, it defines an expiration period in hours. After the expiration, users will no longer be able to submit the web form instance, and any attempt to render the instance URL will result in an error. Web form instances are also subject to a five-minute expiration for the [web form instance URL](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) instance token component, which makes the URL unique and secure. New instance tokens can be issued until a web form instance expires.

Your application should set a web form instance expiration that is appropriate for business and security needs, as well as implement instance token refresh logic to ensure that user access to a web form instance is maintained.

See [Handle expirations and timeouts](https://developers.docusign.com/docs/web-forms-api/plan-integration/expirations-timeouts/) for more information about implementing this logic in your application.

## Determine how your application renders web form instances

**Note:** This process is not applicable to [remote web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/).

Your application can render web form instance URLs using the Docusign JS client SDK, which embeds form instances seamlessly into your website, or by redirecting users' browsers to the Docusign platform for the display of form instances.

See [Render embedded web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/) for more information about these options.

## Deliver web form instances via email

**Note:** This process is not applicable to [embedded web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/) or instances displayed by redirecting users to the Docusign platform.

Instead of embedding web form instances or redirecting users to them, your application can trigger the sending of an [envelope email](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=pah1578456451991.html) with a link. The link routes a user to a web form instance that is embedded in an envelope. The user fills out the form instance and is then presented with an envelope to sign.

See [Deliver remote web form instances to users](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/) for details.

## Track the status of web form instances and envelopes

After your application has created web form instances, it can monitor their status. For form instances created from [template-based web form configurations](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/), your application can also track the status of the envelope that is associated with a web form instance. Monitoring the status of web form instances and envelopes enables your application to trigger additional processing as needed.

See [Track web form instance and envelope status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/) for details about the status information that is available to your application.

## Retrieve form data after submission

Your application can retrieve values that a user submits in a web form instance and write them to your system of record.

See [Retrieve submitted web form instance values](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/) for details about how your application can obtain these values.

## Define the web page to display after form submission

After a user fills out a web form instance and submits it, your application should display an appropriate page to indicate that the user information has been received successfully.

See [Redirect users after form submission](https://developers.docusign.com/docs/web-forms-api/plan-integration/redirect-users-form-submission/) for details about how your application can define a page to display.

## Next steps

- See [Get started with the Web Forms API](https://developers.docusign.com/docs/web-forms-api/get-started/) for a list of requirements for making Web Forms API calls.
- See [Go-Live](https://developers.docusign.com/docs/web-forms-api/go-live/) for information about the process to move a Web Forms API integration from the developer environment to production.

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
