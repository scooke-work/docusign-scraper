---
title: Composite templates
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/composite/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Templates
- Templates
- Composite
scraped_at: '2026-06-18T20:28:18Z'
---

# Composite templates

You can apply multiple templates (or combine templates with forms or other documents) to a single envelope using composite templates. A *composite template* is an object that holds an array of elements. Each element may contain a document and sets of rules, formatting, and requirements that will be applied to the envelope that you will create.

The JSON structure of a `compositeTemplates` element declaration in your envelope body is shown in the accompanying code block. The `compositeTemplates` element specifies an array of composite templates. Each composite template defined within may include:

- A `document` element specifying the document to which the template data will be applied. If you supply a document in this field, it supersedes any other documents supplied from server or inline templates in this composite template.

  You should use the `document` element when a standard document is used for all signers or in cases where [PDF form field transformation](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/pdf-transform/) will be used to generate tabs. You can then add client-specific elements by applying server templates.
- A `serverTemplates` element containing an array of one or more server-side templates that set the rules, formatting, and data requirements for your documents. Each server template should contain a reference to a [Docusign template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/) that will be applied. The data values for each individual document, such as the default values of each tab, will be supplied by your `inlineTemplates`.

  A server template typically contains the requirements and rules that apply to all documents of a specific type, such as a rental contract. Although you can specify more than one server template per composite template, using a single server template, or none at all, is a best practice. A server template also supplies a document that is used if no `document` field is set.
- An `inlineTemplates` element containing an array of one or more templates that provide recipient-specific data to meet the requirements imposed by your server template(s), such as the names, email addresses, and role names of your recipients. You can also use inline templates to apply your own customized data requirements and rules to your documents. You can add any number of inline templates to your composite template.

**Note:** You can also set a [pdfMetaDataTemplates](https://developers.docusign.com/docs/esign-soap-api/reference/sending-group/pdfmetadatatemplate/) element that specifies the number (0 or 1) of embedded templates in the PDF metadata. If supplied, the PDF metadata template will be overlaid into the envelope in the order of its `sequence` property value.

## **When to use composite templates**

You should use composite templates instead of just using [template references](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/) whenever possible, outside of the simplest workflows. Creating an envelope from a template can be very limited, as you can only specify a single template ID to be the basis of the envelope. If your users need to add additional documents, you will need to rework your integration to use the composite templates instead.

Composite templates support all of the workflows that you can implement with a template reference and have the ability to support workflows that template references cannot. Composite templates are also much easier to modify and update than template reference workflows, enabling you to expand and adapt your workflows more quickly and with less work. See [Why You Should Be Using the Composite Template Model](https://www.docusign.com/blog/dsdev-why-use-composite-templates?_gl=1*1qxl7lc*_gcl_au*NDcwMzg2NzM3LjE3NjczNDg4OTM.) for details.

## **Example composite template definition**

The accompanying example definition shows an envelope composed of three `compositeTemplates` objects, each contributing documents, recipients, and tabs, as follows:

1. The first composite template provides a document in the document property and applies both a server and inline template to it. The server template applies an existing Docusign template (containing tabs and formatting) to the document, while the inline template sets recipient data.
2. The second element provides a document via a server template overlaid by an inline template that sets recipient data.
3. The third element uses the document property to provide a PDF file and sets the file to use PDF form field transformation. It also applies an inline template to apply tabs for the recipient.

1

2

3

4

5

6

7

"compositeTemplates": [

{

"document": {...},

"serverTemplates": [{...}],

"inlineTemplates": [{...}]

}

]

## Applying documents and attributes with composite template elements

### **Adding documents**

Each composite template (a single set of document, server, and inline templates) of your `compositeTemplates` declaration should contribute exactly one document. This document should be supplied by the element’s `document` field or the `serverTemplate`.

If you have specified a document in the `document` property, that document is used. If no `document` value was provided, each template is checked for documents in ascending order of their `sequence` value. The first document reference found will be used as the document for this composite template element.

**Note**: As a best practice, do not use inline templates to contribute documents.

### **Sequence and adding non-document attributes to your envelope**

When using composite templates, attributes are applied to your envelope in ascending order of their `sequence` value. **When you apply an attribute that has already been defined, the existing value will be overwritten by the new value**.

To ensure that your desired attributes are set, it is important to set `sequence` values for your templates. The templates whose values you want to use as final must be applied after all other templates that set those values. For example, if a server template specifies a recipient role and an inline template maps a recipient to that role name, it is essential that the server template be sequenced prior to the inline template.

**Note**: The sequencing of templates takes place within the context of individual composites. Each new composite element will start sequencing at 1, meaning that you don’t need to increment `sequence` values across your entire array of composites. This makes it easy to set the `sequence` value with the logic that is building the individual composite.

For each composite template, the following additional rules are applied:

- When you create an envelope by using a composite template, you should specify any envelope custom fields in your inline template. **Any custom fields that you specify at the root level will be ignored.**
- If you specify in a template that a recipient is locked, once that recipient is overlaid, the recipient attributes can no longer be changed. The only items that can be changed for the recipient in this case are the `email, username`, access code, and `IDCheckInformationInput`.
- Tab matching is based on tab labels, tab types and documents. If a tab label matches but the document is not supplied, the tab is overlaid for all the documents. For example, if you have a simple inline template with only one tab in it with a label and a value, the value will be assigned to all instances of that tab, across all documents in the envelope at the time the value was assigned. However, note that the signature, initial, company, envelope ID, and user name tabs will only be matched and collapsed if they fall in the exact same X and Y locations.
- Role name and tab label matching is case-sensitive.
- A `defaultRecipient` property has been introduced so that you can specify to which recipient the generated tabs from the PDF form are mapped. You can also set PDF form-generated tabs to a recipient other than the default recipient by specifying the mapping of the tab label that is created to one of the template recipients. You can also use tab label wildcarding to map a series of tabs from the PDF form. To use this, you must begin or end a tab label with “\*”, and then the system matches tabs that start with the label .
- If no default recipient is specified, tabs must be explicitly mapped to recipients in order to be generated from the form. Unmapped form objects will not be generated into their Docusign equivalents. In the case of signature/initials tabs, the tabs will be disregarded entirely. In the case of PDF text fields, the field data will be imprinted on the document. In the case of a drop-down menu, the first value will be imprinted.
- Only these field types are extrapolated from the forms: `CheckBox`, `DateTime`, `ListBox`, `Numeric`, `Radio`, `Text`, `Signature`, and `Password`.

  When extrapolating Adobe Digital Signatures, the following Adobe names correspond to Docusign names:
  - Adobe name that contains DocusignSignHere or eSignSignHere = Docusign Signature
  - Adobe name that contains DocusignSignHereOptional or eSignSignHereOptional = Docusign Optional Signature
  - Adobe name that contains DocusignInitialHere or eSignInitialHere = Docusign Initials
  - Adobe name that contains DocusignInitialHereOptional or eSignInitialHereOptional = Docusign Optional Initials
  - Any other Adobe name will default to Docusign Signature
- When extrapolating Adobe text fields, the following Adobe names correspond to Docusign names:
  - Adobe name that contains DocusignSignHere or eSignSignHere = Docusign Signature
  - Adobe name that contains DocusignSignHereOptional or eSignSignHereOptional = Docusign Optional Signature
  - Adobe name that contains DocusignInitialHere or eSignInitialHere = Docusign Initials
  - Adobe name that contains DocusignInitialHereOptional or eSignInitialHereOptional = Docusign Optional Initials
  - Adobe name that contains DocusignEnvelopeID or eSignEnvelopeID = Docusign EnvelopeID
  - Adobe name that contains DocusignCompany or eSignCompany = Docusign Company
  - Adobe name that contains DocusignDateSigned or eSignDateSigned = Docusign DateSigned
  - Adobe name that contains DocusignTitle or eSignTitle = Docusign Title
  - Adobe name that contains DocusignFullName or eSignFullName = Docusign FullName
  - Adobe name that contains DocusignSignerAttachmentOptional or eSignSignerAttachmentOptional = Docusign Optional Signer Attachment
  - Any other name will default to a Docusign data (text) field.

**Note**: Docusign will not transform PDF form fields that have the text "DocusignIgnoreTransform" or "eSignIgnoreTransform" as part of the name of the PDF form field. Adobe date fields can be transformed to Docusign DateSigned fields using the same naming scheme.

PDF form field properties that are extrapolated are: ReadOnly, Required, MaxLength, Positions, and Initial Data.

### **Merging duplicate recipients**

When you use multiple templates to create an envelope, two or more templates may define the same recipient (a recipient with the same role or even the same name as other recipients), creating duplicate recipients. You can automatically merge these duplicate recipients by making sure that each of these duplicate recipients has the same email, user name, and routing order. In this case, any duplicate recipients are merged together after all template overlays have been applied.

Conversely, if you have the same recipient in two different routing orders (perhaps based on two separate roles in templates) and you wish to restrict their actions to their respective roles and routing orders, you can set the envelope attribute of `allowRecipientRecursion` to `true`.

## Best practices for using composite templates

- Create Docusign templates around individual documents, rather than bundling multiple documents in a single template. By keeping them separate, you can easily accommodate a custom envelope payload by mixing in the necessary server templates.
- Design the assembly of envelopes around composites, with each composite template contributing a single document. This helps keep your business logic flexible enough to be modified to handle new or complex use cases without a complete redesign of your envelope construction logic.
- Within an individual composite, do not repeat the same sequence for two templates. The results may appear ambiguous, as the actual sequencing will be based on load order. It is always best to explicitly specify the exact sequencing of templates within an individual composite.
- Consider leaving out the Base64 encoding of documents. Composites provide an additional element ( `compositeTemplateId`) to make it easy to use multipart form requests and pass the documents in their native binary format.

### **Referencing ID values for recipients and documents**

When you create a composite template, you can assign ID values to its recipients and documents. However, when you generate an envelope using that composite template, Docusign will create a new set of IDs for these recipients and documents to avoid conflicts between the ID values of the merged templates. For example, if you create an envelope from a composite template with 2 recipients and assign them the IDs 10 and 11 in your composite templates API call body, then create and send the envelope, these recipient ID values will change. You will no longer be able to update the recipients with a PUT call using the IDs 10 and 11.

Unique recipients are still identified by routing order, name, and email address and documents can still be identified by the document name. To track information across different Composite Templates, use `recipient-customFields` or `document-documentFields`. To retrieve the current recipient and document ids, calls to EnvelopeRecipients:list and EnvelopeDocuments:list may be necessary.

See [From the Trenches: How to track recipients and documents when IDs change](https://www.docusign.com/blog/developers/the-trenches-how-to-track-recipients-and-documents-when-ids-change?_gl=1*aubhif*_gcl_au*NDcwMzg2NzM3LjE3NjczNDg4OTM.) for details.

## Next steps

- See [How to request a signature using a composite template](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-composite-template-embedded/) for a code example demonstrating how to send an envelope built from a composite template.
- See the MyAPICalls sample app scenario [Composite Templates: Custom Forms with Shared Signature Document](https://myapicalls.sampleapps.docusign.com/scenario/9?_gl=1*387ubj*_gcl_au*NDcwMzg2NzM3LjE3NjczNDg4OTM.), which walks you through a sequence of API calls that generate an envelope from composite templates.
- [From the Trenches: How to track recipients and documents when IDs change](https://www.docusign.com/blog/developers/the-trenches-how-to-track-recipients-and-documents-when-ids-change?_gl=1*aubhif*_gcl_au*NDcwMzg2NzM3LjE3NjczNDg4OTM.)

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
