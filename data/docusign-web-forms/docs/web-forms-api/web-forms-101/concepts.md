---
title: Web Forms concepts
source_url: https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Web Forms API 101
- Web Forms API 101
- Concepts
scraped_at: '2026-06-18T19:46:29Z'
---

# Web Forms concepts

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

A w*eb form* is a web page containing fields such as text boxes, date fields, and dropdowns that users fill out to provide data that your application will collect.

The Web Forms API supports two types of web forms:

- *Template-based web forms* are derived from an eSignature [template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/). After a user fills out this type of form, an [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) is generated. The user can verify or update values in the envelope and sign it.
- *Standalone web forms* are not associated with an eSignature template. No envelope is generated after a user fills out the web form. This type of web form is used for data collection only.

## Components associated with template-based web forms

eSignature [templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/) and [envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) are components in the creation and processing of template-based web forms. The interaction between templates, envelopes, and web forms is illustrated in this diagram:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='678' width='1128' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Web Form components](https://images.ctfassets.net/aj9z008chlq0/1QEyufKlTAwgsVsazqbQYX/4c9eae7f68f464bd7351cbeceefba3a4/TemplateBasedWebFormComponents.png?w=1128&h=678&q=50&fm=png)

A [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) defines the content and behavior of a web form. The first step in creating a template-based configuration in the [Web Forms builder](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=gpc1660591510274.html) is selecting an [eSignature template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-templates) that serves as the basis for the web form configuration in two ways:

- The Web Forms builder extracts [document](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), [tab](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/), and [recipient](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/) information from the eSignature template to serve as the framework for your web form configuration, which you can edit as needed. You can create multiple web form configurations from the same template.
- A [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates) is also generated when you create a web form configuration. The web form template defines the eSignature envelopes that will be generated from the form. Initially, the web form template is a copy of the original eSignature template used to create the web form configuration; however, once copied, the web form template can be modified as part of the web form configuration, independently of the eSignature template. Each web form configuration has one web form template.

After you have [created](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=euk1665093155272.html) and [activated](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=iri1669070601520.html) a web form configuration, you can create [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) from it via Web Forms API requests. A web form instance is displayed in a browser for a user to fill out and submit. You can create unlimited web form instances from a web form configuration.

When a user submits a completed web form instance, Docusign displays an [eSignature envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) for the user to sign. The envelope includes the documents and tabs defined in the web form template. In the current release, each web form instance is associated with a single envelope.

## Components associated with standalone web forms

The only components associated with standalone web forms are the [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations), which defines the pages, fields, and validation rules for the web form, and [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances), which are generated from the web form configuration and displayed to users in a browser.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='267' width='360' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Standalone web form components](https://images.ctfassets.net/aj9z008chlq0/4mSwds8a3rqrwzEXEyOCph/5da57da2f430718f1775f75a526ef652/StandAloneWebFormComponents.png?w=360&h=267&q=50&fm=png)

See [Create a Standalone Web Form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=pbx1716585514741.html)﻿ for steps to build this type of web form configuration. You must [activate](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=iri1669070601520.html) the configuration before you can create web form instances from it via Web Forms API requests.

## Component details

See these sections for details about web form components:

- [eSignature templates](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-templates)
- [Web form configurations](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations)
- [Web form templates](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates)
- [Web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances)
- [eSignature envelopes](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes)

### eSignature templates

An eSignature [template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/) serves as a blueprint for creating [envelopes](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes). It enables you to define [recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/), [documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/), and [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) in a reusable format from which many envelopes can be generated. An eSignature template also serves as the basis for a template-based [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) and the [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates) that is associated with the configuration. See [Prepare a Template to Import to a Web Form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=xtj1660594293452.html) for guidance on how to ensure that an eSignature template has been configured correctly for use with web forms.

Here is an example of a template definition in the Docusign eSignature web application.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1844.0000000000002' width='1854' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![eSignature template](https://images.ctfassets.net/aj9z008chlq0/2UxUmvfO7Iq5efMXQWTv5I/623bcf42e86bd92653c1a611138c251f/TemplateForWebForm.png?w=1854&h=1844&q=50&fm=png)

**Note:** Standalone web form configurations are not derived from eSignature templates.

### Web form configurations

Each web form has a *web form configuration* that defines the sequence of pages, text and fields on the pages, validation, and conditional logic. You create web form configurations in the [Web Forms builder](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=gpc1660591510274.html), which enables you to:

- Name the web form configuration
- Add and edit form pages
- Add and edit form fields in which users can enter data
- Set validation rules for the data that users enter
- Use conditional logic to show or hide fields and pages
- Define the content for a welcome page at the start of the web form flow and a thank you page to be displayed after users submit web form instances

A preliminary step in [creating a template-based web form configuration](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=euk1665093155272.html) is to select an [eSignature template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-templates) to provide the configuration's framework. When the Web Forms builder generates a new web form configuration from a template, it includes:

- A web form field for each [tab](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) in the template that is one of the following types: text, attachment, checkbox, dropdown, or radio buttons
- A web form page for each [document](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) in the template that includes at least one of the tab types listed above
- A [recipient](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/) for each recipient defined in the template. If the template has multiple recipients, the resulting web form configuration defines one of them as the [primary recipient](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bro1678386015232.html) who fills out both the [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) and [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes). Additional recipients can be configured to fill out both the form instance and envelope or only the envelope. For recipients who do not fill out the form instance, only their name and email address template fields are imported as web form fields, and their remaining template fields are included in the [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates). See [Build a Multiple-Recipient Web Form](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=inc1745950777430.html)﻿ for more information.
- A [Pre-fill data page](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=leh1723234738023.html) that includes any [envelope custom fields](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=qor1583277385137.html) defined in your account. The Pre-fill data page and its fields are not displayed to users, but you can [prefill](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) and [retrieve](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/) these values via API requests for classification and reporting purposes.

**Note:** Attachment fields and envelope custom fields are not supported with standalone web form configurations. Attachment fields are not supported with [remote web form instances](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/).

Here is an example of a template-based web form configuration displayed in the Web Forms builder. It was derived from the eSignature template previously shown and includes a [Signature step](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) in the outline.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1369' width='1699' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Web form configuration](https://images.ctfassets.net/aj9z008chlq0/4RDssfMPMuPA1t4qmCiDfE/83807a9d1199884ff7729636b0063b61/WebFormConfigurationinBuilder.png?w=1699&h=1369&q=50&fm=png)

When you [create a standalone web form configuration](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=pbx1716585514741.html), the Web Forms builder generates a basic framework that includes a welcome page, a blank form page, and thank you page. You must supply the page details, including all form fields. Standalone web form configurations do not include a Signature step in the outline.

### Web form templates

This section is applicable only for template-based web form configurations. Standalone web form configurations are not associated with web form templates.

A *web form template* is an automatically generated copy of the [eSignature template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-templates) that was selected during creation of a template-based [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations). When a user completes and submits a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) generated from the configuration, Docusign displays an [envelope](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#esignature-envelopes) created from the web form template. If the web form template has additional recipients defined, the envelope will also be sent to them.

If you want to make changes in the appearance, behavior, or distribution of envelopes generated from web form instances, you [edit the web form template](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) by accessing it through the Web Forms builder. Updates to the web form template do not change the original eSignature template from which the web form template was copied. Modifying the original eSignature template does not affect any existing web form templates that were copied from it.

### Web form instances

After you've created a [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) in the Web Forms builder and activated it, you can create *web form instances* from that configuration via Web Forms API [Instances:createInstance](https://developers.docusign.com/docs/web-forms-api/reference/webforms/instances/createinstance/) requests or equivalent [SDK](https://developers.docusign.com/docs/web-forms-api/sdks/) method calls. Web form instances are displayed in a browser to users, who populate the fields and submit the form instances. Web form instances may be delivered to recipients in either of two ways:

- [Embedded web form instance delivery](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/): Your Web Forms API integration embeds the web form instance in your web application or redirects the user to the Docusign platform, which displays the form instance. Each instance has a unique, secure URL. See [Web form instance URLs](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) for details.
- [Remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/plan-integration/deliver-remote-instances-to-users/): Recipients are sent an [envelope email](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=pah1578456451991.html) with a link to a web form instance embedded in an envelope.

For more information about your delivery options, see [When to use embedded or remote web form instance delivery](https://developers.docusign.com/docs/web-forms-api/web-forms-101/when-to-use-embedded-or-remote-delivery/).

The fields in a web form instance can be [prefilled](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) with values supplied in the API request that creates the instance. After a user has submitted a form instance, your application can [retrieve the submitted field values](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/), whether prefilled or user-populated. Here is a web form instance created from the web form configuration previously shown.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='923' width='428' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Web form instance displayed in browser](https://images.ctfassets.net/aj9z008chlq0/4C0u7m2xWTlgfF2nDAco2s/67fc24c32c39ae1cfecd4c429b4b50c0/WebFormInstanceDisplayedinBrowser.png?w=428&h=923&q=50&fm=png)

See [Web form instance processing](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/) for details about how web form instances are created and presented to users.

### eSignature envelopes

This section is applicable only for web form instances generated from template-based web form configurations. For instances generated from standalone web form configurations, no envelope is created.

After a user fills out the fields in a [web form instance](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances) that is displayed in a browser and submits the form instance, Docusign displays an eSignature [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) consisting of one or more [documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) that include values from the form instance, as well as other [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) defined in the documents, such as a signature tab. The user can review values in the envelope and sign.

The [web form template](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-templates) that is associated with the [web form configuration](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) determines:

- [Recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/) in addition to the form submitter, if any, who will receive the envelope
- Documents that make up the envelope
- Tabs that appear in the documents

Web form configuration settings determine other envelope behavior, including:

- Whether the envelope is displayed in the user's browser after form submission, known as [embedded signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/), or whether the user receives an emailed link to the signing page, known as [remote signing](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-template-remote/)
- Which form values are displayed in envelope tabs
- Whether the user can edit values that appear in envelope tabs

See [The Signature Page﻿](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bna1674685085797.html) for details about these configuration settings.

An envelope displayed on submission of the web form instance previously shown would look like this:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1735' width='1388' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Envelope generated after form instance submission](https://images.ctfassets.net/aj9z008chlq0/47yFHWjfMOHPoSPmRyn7wi/e8375a6a24bf671eb1043cd8ac8e9cf3/EnvelopeGeneratedFromForm.png?w=1388&h=1735&q=50&fm=png)

## Next steps

- See [API and UI functionality](https://developers.docusign.com/docs/web-forms-api/web-forms-101/api-ui-functionality/) for a summary of key features and whether they are available with the API or the Web Forms builder UI.
- See [Web form instance processing](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/) for an overview of the interaction between a user, a Web Forms API integration, and the Docusign platform.

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
