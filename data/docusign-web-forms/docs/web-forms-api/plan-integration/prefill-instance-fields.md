---
title: Prefill web form instance fields
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Prefill web form instance fields
scraped_at: '2026-06-18T19:46:29Z'
---

# Prefill web form instance fields

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

The Web Forms API enables you to prefill [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) fields with customer data from your system of record. Any known information about a customer, such as a name, account information, and contact information, can be loaded in the user's browser with the web form instance. See these topics for details:

- [Obtain information about fields that can be prefilled](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/#obtain-information-about-fields-that-can-be-prefilled)
- [Supply prefill values in the request to create a web form instance](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/#supply-prefill-values-in-the-request-to-create-a-web-form-instance)
- [Prefill values override web form configuration defaults](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/#prefill-values-override-web-form-configuration-defaults)
- [Prefill values for embedded web form instances with Docusign JS](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/#prefill-values-for-embedded-web-form-instances-with-docusign-js)

Prefilling fields is optional for web form instances that are embedded in a web application or displayed via a redirect to the Docusign platform. For remote web form instances that users access via an envelope email, some values must be supplied when creating instances. See [Required user values for remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/#required-user-values-for-remote-web-form-instances) and [Additional prefill requirements for remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/#additional-prefill-requirements-for-remote-web-form-instances) for details.

## Obtain information about fields that can be prefilled

Before creating a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) with prefilled values, your application can use a [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call to obtain information about fields in a [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) that can be prefilled, including the field names and types. Your application must reference the field names to [supply prefill values when creating form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/#supply-prefill-values-in-the-request-to-create-a-web-form-instance). See [Form field definitions](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#form-field-definitions) for details about the field information that is available.

## Supply prefill values in the request to create a web form instance

To prefill data in an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call that creates a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances), your application includes form field names and prefill values in the request's [formValues](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_formvalues) object.

Below is a sample `Instances:createInstance` request body that includes a `formValues` object. In each name/value pair in the `formValues` object, the name is the `componentName` from the [form field definition](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#form-field-definitions). This value also appears as the **API reference name** in the Web Forms builder [Properties panel](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=wor1676501633875.html).

```
{
  "clientUserId": "1234-xxxx-xxxx-efda",
    "formValues": {
      "name": "Sally Signer",
      "email": "sally.signer@email.com",
      "phone_num": {
        "countryCode": "55",
        "nationalNumber": "1133301000"
      },
      "salary": 121800.55,
      "birth_date": "1980-12-18",
      "marital_status": "single",
      "education": "advanced",
      "alerts": ["Funds_withdrawn","Account_info_changed"]
    },
  "expirationOffset": 720,
  "returnUrl": "https://developers.docusign.com"
}
```

To prefill a form field whose value will be saved as an [envelope custom field](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#envelope-custom-fields), include the field's `componentName` and a prefill value in the `formValues` object, just as you would with any other form field. For [remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/), any required envelope custom fields must be prefilled.

See the [how-to guides](https://developers.docusign.com/docs/web-forms-api/how-to/) for code examples that show how to prefill values.

Below is a list of form field types (identified by the `componentType` that appears in the [form field definition](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#form-field-definitions) in a [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) response), a description of the value to supply in the `formValues` object, and an example of a prefill value. To learn how to obtain the allowed values for fields in which users make a selection, see [Identify permitted values for dropdowns, radio buttons, and checkboxes](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#identify-permitted-values-for-dropdowns-radio-buttons-and-checkboxes).

| `componentType` | Prefill value | Example |
| --- | --- | --- |
| `TextBox` | Text | `"name": "Sally Signer"` |
| `Number` | A number. Use a period as the decimal separator in the request, even if the web form configuration specifies a comma as the [decimal separator](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=zxq1673475126383.html) for the display format. | `"salary": 121800.55` |
| `Email` | An email address. The Web Forms API does not check whether the value is a valid email address. If an invalid email address is supplied in a request, the web form instance UI displays the message `Input must be a valid email address` below the field. | `"email": "sally.signer@email.com"` |
| `PhoneNumber` | A phone number defined by two properties:  - `countryCode`: The one-, two-, or three-digit dialing code for the country. If this value is omitted, the web form instance UI displays the default country code defined in the web form configuration. - `nationalNumber`: The phone number's area code and local number. The maximum length is 15 characters. Special characters such as spaces and hyphens can be included in prefill values. When a web form instance is submitted, special characters are removed from the `nationalNumber`, and only the digits are included in responses to requests that return submitted form values.  Phone number fields are supported in standalone web form configurations, but not in template-based configurations. See [Web form configuration type](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) for more information about the two types. | ``` "phone_num": {   "countryCode": "55",   "nationalNumber": "1133301000" } ``` |
| `Date` | A date in the format `yyyy-mm-dd`. Use this format in the request even if a different [date display format](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=hsg1673483253591.html) is selected in the web form configuration. | `"birth_date": "1980-12-18"` |
| `Select` | One of the permitted values for the dropdown as defined in the web form configuration. Case-sensitive. | `"marital_status": "single"` |
| `RadioButtonGroup` | One of the permitted values for the radio button group as defined in the web form configuration. Case-sensitive. | `"education": "advanced"` |
| `CheckboxGroup` | A string array containing one or more permitted values for the checkbox group as defined in the web form configuration. Case-sensitive. | `"alerts": ["Funds_withdrawn","Account_info_changed"]` |

 **Note:** Prefill values are not supported for `FileInput` (attachment) fields.

## Prefill values override web form configuration defaults

A prefill value supplied in an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call overrides any default value defined in the [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations). If your application does not prefill a value for a form field, the web form configuration default value, if one exists, will be displayed when the [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) loads. Users can change default or prefilled form values before submitting a form instance, unless a field is defined in the web form configuration as read-only.

## Prefill values for embedded web form instances with Docusign JS

As an alternative to prefilling values in an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or equivalent SDK method call, you can prefill them using the [Docusign JS](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls) client SDK `prefillValues` property. Prefill values supplied through Docusign JS override those in an `Instances:createInstance` request, unless the prefill value is for a read-only field.

For read-only form fields, prefill values are applied as follows:

- If supplied in an `Instances:createInstance` request, prefill values can be used to populate read-only fields.
- If supplied with Docusign JS, prefill values cannot be used to populate read-only fields.

If you are using both the Web Forms API and Docusign JS, Docusign recommends prefilling via the `Instances:createInstance` request rather than Docusign JS because:

- Prefilling through the API stores the form values on the Docusign platform. If you prefill using Docusign JS, form values are not stored on the Docusign platform until the user submits the form instance.
- Passing user information through API requests is more secure than passing it through a client SDK.

You should only prefill with Docusign JS if you are not using the Web Forms API to create web form instances.

## Next steps

- See the [how-to guides](https://developers.docusign.com/docs/web-forms-api/how-to/) for code examples that include prefill values.
- See [Retrieve submitted web form instance values](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/) for information about obtaining user-entered values to write to your system of record.

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
