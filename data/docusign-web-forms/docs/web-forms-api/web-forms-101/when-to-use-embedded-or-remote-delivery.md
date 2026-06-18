---
title: When to use embedded or remote web form instance delivery
source_url: https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Web Forms API 101
- Web Forms API 101
- When to use embedded or remote delivery
scraped_at: '2026-06-18T19:46:29Z'
---

# When to use embedded or remote web form instance delivery

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

You can request more information from a recipient before they open and sign an envelope agreement using Web Forms. There are two options for presenting your recipients with your web form instances: embedded and remote.

## Learn about embedded web form instance delivery

You can have your recipients view and sign web form instances within your app using *embedded web form instance delivery*. In embedded delivery, you create instances of your activated web form configurations for your recipients by embedding the web form instance URL in your app. Each recipient will get one web form instance which, for eSignature-based flows, will generate one envelope.

Embedded template-based web form delivery follows these steps:

1. Ensure that you have a web form configuration created from an existing eSignature template. The Web Forms builder extracts [document](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), [tab](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/), and [recipient](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/) information from the eSignature template to serve as the framework for your web form configuration, which you can edit as needed. This template can include multiple recipients.
2. Call the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API endpoint, using your web form configuration ID as the call’s form ID. You can find your web form’s configuration ID by calling the [Configurations:listForms](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/listforms/) endpoint and finding the form entry in that call’s response.
3. The generated web form instance will include an instance URL, which you can open in your app. This displays the web form, and the recipient is prompted to enter information for the web form fields assigned to them.
4. After they finish entering their information in their web form, the recipient is presented with their envelope, which is prefilled with their web form instance information. They are then prompted to fill in any envelope tabs assigned to them and/or sign the agreement.

If there are multiple recipients, only the primary recipient is presented with the web form instance in an embedded view. Additional recipients access the web form instance via an envelope email.

See [Web form instance processing](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/) for details and flow diagrams.

## When to use embedded web form instance delivery

Embedded web form instance delivery has two main advantages:

- Because you are embedding the web form instance into your app, your user is already logged in and authenticated. This offers the highest level of security.
- Embedding the form instance directly in your app provides a seamless experience where your users can view and sign forms immediately.

Use embedded web form instance delivery when your users need to complete and sign forms instantly, directly within your digital environment, or when you need to support high-volume, public, or in-person workflows without relying on email distribution.

### Example use cases

- **Self-service workflows**
  - **Account registration:** New users can fill out and sign onboarding forms immediately after creating an account, without waiting for an email.
  - **Service requests:** Customers can submit signed service requests or support forms directly from your portal.
- **Walk-in or in-person scenarios**
  - **In-branch or in-office signing:** Banks, clinics, or government offices can have clients complete forms on tablets or kiosks during their visit.
  - **Event check-in:** Attendees can sign waivers or registration forms on-site at events or conferences.
- **Immediate action required**
  - **Time-sensitive agreements:** Users can complete forms instantly (e.g., urgent consent forms, last-minute registrations) without email delays.
  - **Real-time transactions:** E-commerce or financial platforms can capture signatures as part of the checkout or transaction process.

Embedded web form instance delivery also supports standalone web form configurations, which do not have a template and do not generate an envelope. These forms are used purely for data collection.

## Learn about remote web form instance delivery

You can send web form instances directly to one or more recipients via email using *remote web form instance delivery*. These recipients each fill out their own view of a web form instance, and the information from those form instances is used to prefill and personalize an eSignature envelope that each recipient will then complete. 

You can use this feature to send web form instances to your recipients through the UI or by making a call to the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API endpoint. Remote web form instance delivery follows these steps:

1. Ensure that you have a web form configuration created from an existing eSignature template. The Web Forms builder extracts [document](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), [tab](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/), and [recipient](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/) information from the eSignature template to serve as the framework for your web form configuration, which you can edit as needed. This configuration can include multiple recipients. Older versions of a web form configuration may not support remote delivery; in these cases, recreate the form.
2. Call the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API endpoint, using your web form configuration ID as the call’s form ID. To indicate that you are using remote web form delivery, you must also include the following body fields:
   - `"sendOption": "now"`
   - A `recipients` object or a `formValues` object containing required values for each recipient. See [Required user values for remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/#required-user-values-for-remote-web-form-instances) for details.
   You can find your web form’s configuration ID by calling the [Configurations:listForms](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/listforms/) endpoint and finding the form entry in that call’s response. Any recipients whose information is not provided in the request body will have their assigned tabs removed from the generated web form instance and envelope.

   See [How to create and send a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-send-instance/) for a detailed walkthrough.
3. In routing order, each recipient receives an email containing a link to an envelope. This envelope will include an embedded web form instance if your web form configuration specifies that they must fill out fields for that web form instance. If they select the link, their browser opens the web form instance and they are prompted to enter information for the form fields assigned to them. Users who are  [not required to fill out the web form instance](https://developers.docusign.com/docs/web-forms-api/plan-integration/identify-instance-users/) will be routed directly to the envelope.
4. After they finish entering their information in the web form instance, the recipient is presented with the envelope, which is prefilled with web form instance information. They are then prompted to fill in any envelope tabs assigned to them and/or sign the agreement.

See [Deliver remote web form instances to users](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/) for details on how to generate remote web form instances, or [Web form instance processing](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/) for more information on the flow and diagrams.

### Restrictions for using remote web form instance delivery

- Standalone web form configurations are not supported.
- Attachment fields are not supported.
- Older form configurations may not be compatible with the new remote sending functionality. To check for compatibility, you should look at the `allowSending` flag under `formProperties` (which requires a [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) API call).

## When to use remote web form instance delivery

Use remote web form instance delivery for flows that do not require an embedded experience. This enables you to rely on Docusign to handle the user flow from end-to-end.

### Example use cases

- **Mass onboarding**
  - **Employee onboarding:** HR departments can send onboarding forms (e.g., tax forms, direct deposit, policy acknowledgments) to new hires.
  - **Vendor/supplier onboarding:** Procurement teams can distribute registration or compliance forms to vendors.
- **Customer agreements and consents**
  - **Service agreements:** Companies can send updated terms of service or consent forms to customers who need to review and sign.
  - **Policy updates:** When privacy policies or terms change, organizations can request acknowledgment from affected users.
- **Compliance and regulatory requirements**
  - **Annual compliance certifications:** Financial institutions or healthcare providers can send compliance attestation forms to employees or clients.
  - **Audit documentation:** Collect required documentation from multiple parties for regulatory audits.

## Next steps

- Learn more about [Web Forms concepts](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/).
- Review the steps to [Deliver remote web form instances to users](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/).
- Get the details about [Web form instance processing](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/).

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
