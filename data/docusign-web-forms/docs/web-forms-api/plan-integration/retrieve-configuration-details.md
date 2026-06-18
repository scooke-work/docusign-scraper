---
title: Retrieve web form configuration details
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Retrieve web form configuration details
scraped_at: '2026-06-18T19:46:29Z'
---

# Retrieve web form configuration details

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

When creating [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances), your application must supply the ID of the [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) from which the instances are to be created. The web form configuration determines which form fields will be available to your application for [prefilling](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) and [retrieving user-entered data](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/). Your application should also check web form configuration [status](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-status) and [version](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-version) information before attempting to create a web form instance to ensure that the instance can be created successfully.

These Web Forms API endpoints return information about web form configurations in your account:

- [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/): Returns details about a specific web form configuration, including the form type, components, status, and version.
- [Configurations:listForms](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/listforms/): Returns information about all web form configurations in your account, including form types, names, IDs, and statuses.

For details about the web form configuration information available with these requests, see:

- [Web form configuration ID](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-id)
- [Web form configuration support for remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-support-for-remote-web-form-instances)
- [Web form configuration type](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type)
- [Web form configuration structure](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-structure)
- [Web form configuration status](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-status)
- [Web form configuration version](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-version)

## Web form configuration ID

Each web form configuration is identified by a unique ID, which is a GUID. This ID is required in API requests that create and manage web form instances.

You can retrieve a list of all web form configuration IDs in your account via a Web Forms API [Configurations:listForms](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/listforms/) request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call. You can also use this request to search for a web form configuration by name. See Step 3 of [How to create and embed a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-embed-web-form-instance/) for an example.

To obtain a web form configuration's ID from the [Web Forms builder](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=gpc1660591510274.html):

1. Log in to the [eSignature web application](https://account-d.docusign.com/).
2. Select **Templates** from the top navigation.
3. In the left navigation under **Web Forms**, select **My Web Forms** or **All Web Forms**.
4. Locate the web form configuration in the list.
5. Do one of the following:
   - Select **Download Configuration** from the kebab menu in that row to download a JSON file containing form information, including the `id` property.
   - Select the **Open** button to open the web form configuration. The ID appears in the URL.

## Web form configuration type

A web form configuration's type determines whether an eSignature [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) is generated after a user completes and submits a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) created from the configuration.

Responses to the [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) request, the [Configurations:listForms](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/listforms/) request, and equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method calls include a `type` property that indicates the configuration type. Possible values are:

- `hasEsignTemplate`: The web form configuration is template-based. The configuration's [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates) determines the format of an eSignature envelope that is created for each user to review and sign after filling out a web form instance.
- `standalone`: The web form configuration is standalone. This configuration type is not associated with a web form template, and a web form instance submission does not generate an envelope. This configuration type is also not eligible for [remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/).

In addition to the generation of eSignature envelopes, template-based web form configurations provide the following features that are not supported with standalone configurations:

- Routing the envelope that is generated on web form instance submission to additional recipients for review. See ﻿[Review and Update Recipient Information﻿](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bro1678386015232.html) for details about configuring envelope recipients.
- [Envelope custom fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#envelope-custom-fields), which can be used for envelope classification and reporting
- [Attachment fields](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=oyz1722621351928.html), which enable web form instance submitters to upload files
- [Records of recipient authentication](https://developers.docusign.com/docs/web-forms-api/plan-integration/identify-instance-users/#create-a-record-of-recipient-authentication), which provide an audit trail for envelope recipient authentication
- Ability to deliver the web form instance as remote (delivered as a link via email). For more information, see [When to use embedded or remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/).

## Web form configuration support for remote web form instances

The [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) and [Configurations:listForms](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/listforms/) responses include an `allowSending` property. When `true`, the web form configuration can be used to create [remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/), which users access via a link in an [envelope email](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=pah1578456451991.html). If the response includes an `allowSending` property set to `false` or does not include the `allowSending` property, the web form configuration cannot be used to create remote web form instances.

A web form configuration does not allow the creation of remote web form instances if any of the following is true:

- The web form configuration is [standalone](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type). To use the web form configuration with remote web form instances, [recreate it](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=euk1665093155272.html) in the Web Forms builder as a template-based configuration.
- The web form configuration has an attachment field. Attachment fields are not supported in remote web form instances. To use the web form configuration with remote web form instances, [edit the web form configuration](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=zqg1667509078130.html) and remove the attachment field.
- The web form configuration was created with an older Web Forms release. To use the web form configuration with remote web form instances, [recreate it](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=euk1665093155272.html) in the Web Forms builder.

## Web form configuration structure

The [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call returns details about a web form configuration's structure in the [formContent.components](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/#schema_200_webform_webform_formcontent_components) object. These details include:

- The pages that make up a web form configuration and their content
- Information about the form fields, including their names, types, default values, and permitted values for dropdowns, radio buttons, and checkboxes. You'll need this information if your application [prefills](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) form fields, and to [retrieve user-entered form values](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/).
- Recipient information, including the [primary recipient](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bro1678386015232.html) who fills out the web form instance and any additional recipients for the [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) that will be generated if the web form configuration is [template-based](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type)

### Form field definitions

The [formContent.components](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/#schema_200_webform_webform_formcontent_components) object in a [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) response includes a form field definition for each field defined in the web form configuration.

An example form field definition for a text field is shown here.

```
"TextBox_7oknP_C2": {
  "componentKey": "TextBox_7oknP_C2",
  "componentType": "TextBox",
  "componentName": "name",
  "label": "Name",
  "description": "",
  "multiLine": false,
  "placeholder": "",
  "required": true,
  "maxLength": 4000,
  "defaultValue": "New account holder"
},
```

Properties in form field definitions include:

- `componentKey`: A unique identifier for the field. The `componentKey` is referenced in other sections of `formContent.components`. For example, the sections that define the contents of each web form page use the `componentKey` to map form fields to pages.
- `componentName`: This name is referenced in API requests and SDK method calls when [prefilling](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) and [retrieving](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/) form field values. This value is defined in the **API reference name** in the Web Forms builder [Properties panel](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=wor1676501633875.html).
- `componentType`: The type of form field.

Supported `componentTypes` are:

| `componentType` | Form field type |
| --- | --- |
| `TextBox` | Text field |
| `Number` | Number field |
| `Email` | Email field |
| `PhoneNumber` | Phone number field. Supported in [standalone web form configurations](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/) only. |
| `Date` | Date field |
| `Select` | Dropdown |
| `RadioButtonGroup` | Radio buttons |
| `CheckboxGroup` | Checkboxes |
| `FileInput` | Attachment field. Supported in [template-based web form configurations](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/)  with embedded delivery only; not supported for [remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/). |

See [Add or Edit Field Properties on a Web Form﻿](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=fzu1672965301647.html) for descriptions of the different types of form fields.

### Identify permitted values for dropdowns, radio buttons, and checkboxes

For the field types `Select` (dropdown), `RadioButtonGroup`, and `CheckboxGroup`, the values that your application [prefills](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) must be permitted values for that component as defined in the web form configuration. If an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call supplies a prefill value that is not among the permitted values for a component, Docusign returns an error.

The form field definitions for `Select`, `RadioButtonGroup`, and `CheckboxGroup` fields include the permitted values. Here is an example `CheckboxGroup` form field definition from a [formContent.components](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/#schema_200_webform_webform_formcontent_components) object in a [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) response. The `value` properties in the `options` array contain the values that an application can prefill for the checkbox group. These values are case-sensitive.

```
"CheckboxGroup_WP_RWoJO": {
  "componentKey": "CheckboxGroup_WP_RWoJO",
  "componentType": "CheckboxGroup",
  "componentName": "alerts",
  "label": "Alert me when any of the following occurs:",
  "options": [
    {
      "optionKey": "EjN9ohno",
      "value": "Account_login",
      "label": "Account login",
      "selected": false,
      "description": ""
    },
    {
      "optionKey": "ZG8Xjs3_",
      "value": "Funds_withdrawn",
      "label": "Funds withdrawn",
      "selected": false,
      "description": ""
    },
    {
      "optionKey": "sYZOE3ji",
      "value": "Funds_deposited",
      "label": "Funds deposited",
      "selected": false,
      "description": ""
    },
    {
      "optionKey": "k_XDytml",
      "value": "Account_info_changed",
      "label": "Account info changed",
      "selected": false,
      "description": ""
    }
],
```

Another option for obtaining form field names and permitted values is to [open the web form configuration](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=tpj1664990031635.html) in the Web Forms builder and display the [Properties panel](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=wor1676501633875.html) for the form fields.

The form field name appears on the Properties panel in the **API reference name** setting. Below is an example definition in the Web Forms builder for a set of checkboxes. The **API reference name** `alerts` is the form field name that an application would use to reference this checkbox group when supplying prefill values or retrieving the user-submitted value.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='889' width='411' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Properties panel for checkbox](https://images.ctfassets.net/aj9z008chlq0/3QlWDIX4NX2HV1kCHOICie/26432cbaa5e5ddfe3529b424b8e5e0f3/CheckboxDefinition.png?w=411&h=889&q=50&fm=png)

To see the allowed values for a form field, select the pencil icon next to **Checkbox options**. The **API value** column on the Checkbox options window lists the prefill values that an application can use. The Properties panel displays similar lists of permitted values for dropdowns and radio buttons.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='339' width='632' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Checkbox options](https://images.ctfassets.net/aj9z008chlq0/3Ocdh1E7y0pch72X8Fe8pW/8608293e9bbb761e6faf7d12258da812/CheckboxOptions.png?w=632&h=339&q=50&fm=png)

### Envelope custom fields

A web form configuration can include form fields whose values are saved as [envelope custom fields](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=qor1583277385137.html). Envelope custom fields can be used for classification and [reporting](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=cuj1583277384946.html) on envelopes generated after users submit web form instances.

**Note:** Envelope custom fields are supported with template-based web form configurations, but not with standalone web form configurations. See [Web form configuration type](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) for details.

For form fields that are saved as envelope custom fields, your integration can:

- [Supply a prefill value](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) for the field in the request's [formValues](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/#supply-user-values-in-the-formValues-object) object when creating the web form instance. If the field is required, your integration must supply a prefill value when creating a remote web form instance.
- [Retrieve the field value](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/) after form instance submission

Envelope custom fields may or may not be visible to users on web form instances. The next section explains how to identify both types of envelope custom fields.

#### Identify envelope custom fields

On form pages in a web form configuration, most form field types can be designated as envelope custom fields by enabling the **Save as envelope custom field** option on the [Properties panel](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=wor1676501633875.html), as shown here:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='825' width='396' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Save as envelope custom field setting in Web Forms builder](https://images.ctfassets.net/aj9z008chlq0/5LawnrJTqaWdbeMEgYakus/135af934d6ba7b80ed265dfd6c76335d/SaveAsEnvCustomFieldEnabled.png?w=396&h=825&q=50&fm=png)

**Note:** The **Save as envelope custom field** option is not available for checkboxes and attachment fields.

The response to a [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call includes a `useEnvelopeCustomField` property set to `true` for any form field that has **Save as envelope custom field** enabled. This example `Select` field definition from the [formContent.components](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/#schema_200_webform_webform_formcontent_components) section of a `Configurations:getForm` response includes a value of `true` for `useEnvelopeCustomField`.

```
"Select_uewVECYK": {
  "label": "Account type",
  "options": [
    {
      "optionKey": "AqVoIDkN",
      "label": "Checking",
      "value": "checking"
    },
    {
      "optionKey": "Ijcq3blw",
      "value": "savings",
      "label": "Savings",
      "selected": false
    }
  ],
  "required": false,
  "componentKey": "Select_uewVECYK",
  "componentType": "Select",
  "componentName": "account_type",
  "useEnvelopeCustomField": true
},
```

Instead of appearing on a form page in the web form configuration, an envelope custom field can be included on the configuration's [Pre-fill data page](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=leh1723234738023.html). Pre-fill data page fields are not visible to users in web form instances, but your integration can prefill these fields and retrieve their values after form instance submission.

If an envelope custom field is included on the Pre-fill data page and therefore will not be visible to users, the field is referenced in the section of the `formContent.components` object that defines the Pre-fill data page. The Pre-fill data page definition has a `componentType` of `Step` and a `stepMode` of `prefill`.

For example, if the `Select` field whose definition is shown above is not visible to users, its `componentKey` appears in `children` array in the Pre-fill data page definition, as shown here:

```
"Step_swvX58gq": {
  "componentKey": "Step_swvX58gq",
  "componentType": "Step",
  "componentName": "Step_swvX58gq",
  "stepMode": "prefill",
  "text": "Pre-fill data",
  "children": [
    "Select_uewVECYK"
  ]
},
```

### Form field definitions for active web form configurations

When calling [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method to obtain form field information for a web form configuration, include the query parameter `state` with a value of `active`. This returns [form field definitions](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#form-field-definitions) for the active web form configuration. If `state` is set to `draft`, the response may reflect form field additions, deletions, or modifications in a draft web form configuration version. Until the draft version is activated, the field updates will not appear in web form instances that are displayed to users. See [Web form configuration version](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-version) for more information.

The [formContent.components](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/#schema_200_webform_webform_formcontent_components) object in a `Configurations:getForm` response includes a `publishedComponentNames` section that lists form field `componentNames` and `componentTypes`. However, `publishedComponentNames` lists all form fields that have ever appeared in an active version of a web form configuration, including fields that have been deleted. Deleted fields are listed in `publishedComponentNames` even if the `Configurations:getForm` request includes the query parameter `state=active`. To determine which form fields exist in the current active web form configuration version, check the form field definitions in the response to a `Configurations:getForm` request. Unlike `publishedComponentNames`, the form field definitions include only fields that exist in the active web form configuration, provided that you include the query parameter `state=active` with the request.

## Web form configuration status

A web form configuration has several properties that indicate the status. Your application code should check these statuses before attempting to create a web form instance, to ensure that the configuration is in a state that will allow form instances to be created successfully.

The responses to the [Configurations:listForms](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/listforms/) request and the [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) request, and equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method calls, include these properties.

- `isPublished`: `true` for an [activated](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=iri1669070601520.html) web form configuration or `false` for a configuration that has never been activated. After a web form configuration has been activated for the first time, this property will always contain `true`. If you attempt to create a web form instance from a configuration when this value is `false`, Docusign returns an error.
- `isEnabled`: `true` for a web form configuration that is currently activated or `false` for a configuration that has never been activated, or has been [deactivated](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=hmt1669070749005.html). If you attempt to create a web form instance from a configuration when this value is `false`, Docusign returns an error.
- `hasDraftChange`: `true` for a web form configuration that has been edited since the last time the configuration was activated, or `false` if no changes to the configuration have been made since it was last activated. Any changes to the configuration since it was last activated will not appear in web form instances that are created from the configuration.
- `formState`: `draft` if the web form configuration has never been activated. `active` if the configuration has been activated and has not been changed since it was last activated. 

  If the configuration has been changed since it was last activated, the `formState` value depends on the request:
  - `draft`: returned in response to a `Configurations:getForm` request with query parameter `state=draft`. `draft` is also returned in response to a `Configurations:listForms` request.
  - `active`: returned in response to a `Configurations:getForm` request with query parameter `state=active`.

See [Web form configuration version](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-version) for a description of configuration state and versioning details that appear in responses to `Configurations:getForm` and `Configurations:listForms` requests.

This table lists combinations of web form configuration status values and indicates whether a web form instance can be successfully created from a configuration that has these values.

| isPublished | isEnabled | hasDraftChanges | Description of this combination of values | Can a form instance be created from a configuration in this state? |
| --- | --- | --- | --- | --- |
| `false` | `false` | `true` | The web form configuration has been saved but never activated. | No |
| `true` | `true` | `false` | The web form configuration has been activated, and no changes have been made since it was last activated. | Yes |
| `true` | `true` | `true` | The web form configuration has been activated, and changes have been made since it was last activated. | Yes. The form instance will be generated from the most recently activated version, not the draft. |
| `true` | `false` | `false` | The web form configuration was activated, but it has since been deactivated. | No |
| `true` | `false` | `true` | The web form configuration was activated, but it has since been deactivated. Changes have been made to the configuration since it was last activated. | No |

## Web form configuration version

A [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) version appears in the `versionId` property of the response to the [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) request or an equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call. The initial version ID when a configuration is created is 1.

If you make changes to an activated web form configuration, Docusign maintains two versions of the configuration until you [activate](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=iri1669070601520.html) it again:

- **The currently active version.** This is the version from which [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) are created. It does not include changes made since the configuration was last activated. The details associated with the currently active version are returned in response to `Configurations:getForm` requests with the query parameter `state=active`. The response includes a `hasDraftChanges` property set to `true`, a `formState` of `active`, and a `versionId` that reflects the currently active configuration's version number.
- **The draft version.** This version is not used to create web form instances. It includes changes made in the [Web Forms builder](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=gpc1660591510274.html) since the last time the configuration was activated. To get details associated with this version, send a `Configurations:getForm` request with the query parameter `state=draft`. The response will include a `hasDraftChanges` property set to `true`, a `formState` of `draft`, and a `versionId` that is greater than the active configuration's version number by 1.

Values from a `Configurations:getForm` response for an activated configuration with draft changes where the request includes the query parameter `state=draft`:

```
"isPublished": true,
"isEnabled": true,
"hasDraftChanges": true,
"formState": "draft",
"versionId": 2
```

Values from a `Configurations:getForm` response for the same configuration with draft changes where the request includes the query parameter `state=active`:

```
"isPublished": true,
"isEnabled": true,
"hasDraftChanges": true,
"formState": "active",
"versionId": 1
```

Values from a `Configurations:getForm` response with the query parameter `state=active` after the configuration has been activated again and no longer has draft changes. Note that the `versionId` for the active version of the configuration has been incremented.

```
"isPublished": true,
"isEnabled": true,
"hasDraftChanges": false,
"formState": "active",
"versionId": 2
```

The `Configurations:getForm` request returns a 404 error if the configuration currently has no draft version and the request includes the query parameter `state=draft`. See [Troubleshooting](https://developers.docusign.com/docs/web-forms-api/troubleshooting/) for more information.

The `Configurations:listForms` request returns a `formState` of `draft` for configurations that have draft changes (or have never been activated) and a `formState` of `active` for configurations that have no draft changes.

Docusign recommends tracking version numbers for web form configurations to detect whether the active version of a configuration has changed before attempting to create a web form instance from it, because configuration changes can affect your application. For example, form fields may have been added, removed, or modified.

If an updated web form configuration is activated after a web form instance has been created from the configuration, form submission will fail for the instance created from the now-outdated configuration version. For form submission to succeed, your application must reload the [instance URL](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) to update the instance to the newest version.

## Next steps

- See [Prefill web form instance fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) for information about populating a web form instance with known information about users.
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
