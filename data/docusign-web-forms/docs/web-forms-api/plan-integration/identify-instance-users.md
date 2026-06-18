---
title: Identify web form instance users
source_url: https://developers.docusign.com/docs/web-forms-api/plan-integration/identify-instance-users/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Plan an integration
- Plan an integration
- Identify web form instance users
scraped_at: '2026-06-18T19:46:29Z'
---

# Identify web form instance users

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

Your application displays [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) to users, who complete two tasks for each form instance:

- Enter values in form fields and submit the form instance.
- Sign an [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) that Docusign automatically generates after web form instance submission if the instance was created from a [template-based](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) web form configuration. The envelope typically includes values from the web form instance for the user to review.

**Note:** It is not required that all web form instance recipients complete both a form instance and an envelope. See the [Web Forms](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=brp1660583998599.html) user documentation for details.

A web form instance and/or envelope may be routed to additional recipients as specified in the web form configuration. However, the way the web form instance is completed varies depending on its [delivery method](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/). Embedded web form instances can only be completed by a single user in the view that is either embedded in your web application or to which the user is redirected at Docusign. Additional users access the web form instance via a link in an envelope email. For remote web form instances, all users access the web form instance and/or envelope via an email. See [Build a Multiple-Recipient Web Form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=inc1745950777430.html) and [Limitations and Considerations for Web Forms](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=hjv1686940185785.html)﻿ for more information.

Your application should use an identifier that is available in your backend system to identify the primary user who fills out a web form instance and/or envelope. The identifier can be an email address, account number, or any other unique value. For embedded instances, this identifier must be passed in the [clientUserId](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_clientuserid), which is a required property for embedded web form instances in the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) API request and equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method calls. This will associate that user identifier with the web form instance throughout the processing of the instance. The maximum length for a `clientUserId` value is 100 characters.

For remote web form instances, `clientUserId` is not a required property. Users can be identified and differentiated by the [roleName](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_recipients_rolename) property in the [recipients](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_recipients) array. See [Deliver remote web form instances to users](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/) for more details on defining remote web form instance participants.

You can use these identifiers in Web Forms API requests for the following purposes:

- Retrieve data from your system of record to [prefill web form instance fields](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) with known information about the user
- Check the [status of web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/#web-form-instance-status) associated with the user
- [Retrieve user-entered form values](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/) to write data back to the system of record

An additional property of the `Instances:createInstance` request that can help your application identify web form instances is the [tags](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_tags) object, which can be populated with an array of string values to associate metadata with an instance. The `tags` values are included in the responses to the [Instances:getInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/getinstance/) request, which returns information for a specific instance; the [Instances:listInstances](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/listinstances/) request, which returns information for all instances created from a web form configuration; and equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method calls.

## Example requests

The following sample request bodies for the `Instances:createInstances` method demonstrate valid request structures for both embedded and remote web form instance scenarios.

**Embedded instance (single user with** **`clientUserId`****)**

```
{
    "clientUserId": "1234-5678-abcd-0201c",
    "tags": ["embedded-instance", "single-home-purchase"]
    "formValues": {
        "name": "Sally Signer",
        "email": "sally.signer@email.com"
    },
}
```

**Remote web form instance (multiple users with** **`roleName`****)**

```
{
    "sendOption": "now",
    "tags": ["remote-instance", "duplex-purchase"],
    "recipients": [
        {
            "roleName": "signer1",
            "name": "Sally Signer",
            "email": "sally.signer@email.com"
        },
        {
            "roleName": "signer2",
            "name": "Andrew Autograph",
            "email": "andrew.autograph@email.com"
        }
    ]
}
```

## Create a record of recipient authentication

For envelopes that are associated with web form instances, Docusign creates [certificates of completion](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=gpa1578456339545.html) that list envelope details and events. Details about your web application's envelope recipient authentication method can be recorded in certificates of completion.

To record authentication information, include these properties in the [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) request, and their values will appear in certificates of completion:

- [authenticationMethod](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_authenticationmethod)
- [authenticationInstant](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_authenticationinstant)
- [assertionId](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_assertionid)
- [securityDomain](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/#schema__createinstancerequestbody_securitydomain)

These authentication properties can be used only for envelopes displayed in an [embedded signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/) view. Embedded signing is used when the web form configuration's [Initiate signing session from email](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) setting is not enabled. These properties are not supported with remote web form instances or web form instances created from [standalone](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-configuration-details/#web-form-configuration-type) web form configurations.

## Next steps

- See [How to create and embed a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-embed-web-form-instance/) for code examples that include a `clientUserId`.
- Learn [How to create and send a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-send-instance/) with code examples that include the `recipients` array.
- See [Web form instance URLs](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) for details about what makes web form instance URLs that your application displays to users unique and secure.

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
