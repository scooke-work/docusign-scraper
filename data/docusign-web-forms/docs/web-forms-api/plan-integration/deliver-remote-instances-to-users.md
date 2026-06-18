---
title: Deliver remote web form instances to users
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Deliver remote web form instances to users
scraped_at: '2026-06-18T19:46:29Z'
---

# Deliver remote web form instances to users

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

A Web Forms API integration launches an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call to create a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) from a [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations). If the request properties indicate that a remote web form instance is to be created, Docusign sends an [envelope email](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=pah1578456451991.html) to each user defined in the request. Depending on the web form configuration, the link in the email may do either of the following:

- Take the user to a web form instance that is embedded in an [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes). After the user populates and submits the form instance, they sign and complete the envelope.
- Take the user directly to the envelope, if the web form configuration does not specify that web form instance submission is required for the user.

**Note:** Instead of delivering web form instances to users, your integration can embed form instances in your website or redirect users to form instance URLs. See [When to use embedded or remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/) for details.

## Roles determine web form instance behavior for users

Roles are defined in a [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations). For each role, several options can be set:

- Whether users associated with the role fill out a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) and [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes), or just the envelope
- The order in which users in each role complete the web form instance and/or envelope. If the configuration specifies a routing order with multiple steps, a user will not receive an envelope email until the users at previous steps in the routing order have completed the web form instance and/or envelope.

  **Note:** When your integration sends an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request, the envelope email is immediately sent to all users whose role is assigned to the first step of the routing order.
- The web form instance view that will be displayed to users in that role. When a remote web form instance is delivered to more than one user, each user sees a different view of the instance with form fields that are relevant only to them.
- Which tabs the user populates on the eSignature envelope that each user completes. Although all users who fill out a web form instance see the same envelope, they complete different tabs on the envelope. Tab assignments for each role are configured in the [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates).
- Whether or not a user is required to verify their identity before proceeding to a web form instance or envelope. Identity verification can be enabled in the web form template. See [Add Phone Authentication for a Recipient﻿](https://support.docusign.com/s/document-item?bundleId=gav1643676262430&topicId=lsb1578456522697.html) for more information.

See [Build a Multiple-Recipient Web Form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=inc1745950777430.html)﻿ for details on how to define a web form configuration with multiple roles and set options associated with each role.

## Requirements to create remote web form instances

To create remote web form instances, your Web Forms API integration must:

1. Ensure that it creates instances from a [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) that supports remote web form instances. See [Web form configuration support for remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-support-for-remote-web-form-instances) for information about how to verify remote instance support.
2. In the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method call, include this property to designate the instance as remote:
   `"sendOption": "now"`
3. Supply required values for users who will receive envelope emails. See the next sections for details.

## Required user values for remote web form instances

For remote web form instances, the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request must include values that define each user who will receive the envelope email. User values are supplied as follows:

- At minimum, user values must be provided for the primary recipient role in the [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations). A primary recipient role is required for every configuration, and users in that role fill out both a web form instance and envelope.
- User values for additional recipient roles can be omitted from the `Instances:createInstance` request. Those recipients will be removed from the envelope process unless hard-coded user values already exist on the [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates).

The next sections describe user values that are supplied in an `Instances:createInstance` request.

### Name

A name consists of the user’s first and last name. This value appears in the [envelope email](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=pah1578456451991.html). The API integration’s business logic should supply the name for each user.

### Email address

This is the email address to which the envelope email will be sent. The API integration’s business logic should supply the email address for each user.

### Phone number

If a role requires a phone number as part of identity verification, the `Instances:createInstance` request must supply a phone number for a user with that role. When the user selects the link in the envelope email, they are routed to a page where they enter the access code sent to them via SMS or phone call. On successful identity verification, the user proceeds to the web form instance or envelope. See [Add Phone Authentication for a Recipient﻿](https://support.docusign.com/s/document-item?bundleId=gav1643676262430&topicId=lsb1578456522697.html) for information about how to enable identity verification in a template.

### Role name

**Note:** If an [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request supplies recipient information in the [formValues](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_formvalues) object instead of the [recipients](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_recipients) object, role names are not needed in the request.

A role name associates an envelope email recipient with a web form configuration role. You can obtain role names for a configuration from the `roleName` property in the [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) response’s `recipientInfoMap` object. You can also obtain a configuration’s role names by viewing the web form configuration in the [Web Forms builder](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=gpc1660591510274.html).

## Options to supply required user values

User information can be supplied in one of two objects in the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request:

- [recipients](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/#supply-user-values-in-the-recipients-object)
- [formValues](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/#supply-user-values-in-the-formValues-object)

### Supply user values in the recipients object

The [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request’s [recipients](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_recipients) object can supply the required role name, name, email address, and phone number for each user. For example:

```
{
  "sendOption": "now",
  "recipients": [
    {
      "roleName": "signer1",
      "name": "Sally Signer",
      "email": "sally.signer@email.com",
      "phoneNumber": {
        "countryCode": "1",
        "nationalNumber": "4155551212"
      }
    },
    {
      "roleName": "signer2",
      "name": "Steven Signer",
      "email": "steven.signer@email.com",
      "phoneNumber": {
        "countryCode": "1",
        "nationalNumber": "2065551212"
      }
    }
  ]
}
```

### Supply user values in the formValues object

The [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request’s [formValues](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_formvalues) object can be used to define each recipient’s name, email address, and phone number. If you define these values in the `formValues` object, you can omit the [recipients](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_recipients) object from the `Instances:createInstance` request.

To supply these values in the `formValues` object, include key/value pairs for each recipient’s name, email address, and phone number. The key in each key/value pair is the `componentName` for the field that is returned in a [Configurations:getForm](https://developers.docusign.com/docs/web-forms-api/reference/webforms/configurations/getform/) response. These fields must be mapped to recipients on the [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates) as part of the web form configuration. See [Form field definitions](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#form-field-definitions) for details.

For example:

```
{
  "sendOption": "now",
  "formValues": {
    "account_owner_name": "Sally Signer",
    "account_owner_email": "sally.signer@email.com",
    "account_owner_phone": {
      "countryCode": "1",
      "nationalNumber": "4155551212"
    }
    "account_approver_name": "Steven Signer",
    "account_approver_email": "steven.signer@email.com",
    "account_approver_phone": {
      "countryCode": "1",
      "nationalNumber": "2065551212"
    }
  }
}
```

**Note:** If a name, email address, or phone number for a remote web form instance recipient is populated in both the `recipients` object and the `formValues` object, the values must match. If they do not, Docusign returns an error in response to the `Instances:createInstance` request.

## Additional prefill requirements for remote web form instances

These additional requirements for [prefilling](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) values apply when creating a remote web form instance:

- If the web form instance includes required [envelope custom fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#envelope-custom-fields), their values must be prefilled.
- If the web form configuration has rules that include or omit documents from the envelope based on the value of web form fields, those field values must be prefilled. See [Add Conditional Rules to a Web Form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=kff1668121038223.html)﻿ for more information.

## Next steps

- Get an overview of the remote web form instance flow in [Web form instance processing](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/).
- See [How to create and send a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-send-instance/) for code examples that demonstrate the creation of a remote web form instance.

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
