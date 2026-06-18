---
title: Agreement Manager Concepts
source_url: https://developers.docusign.com/docs/agreement-manager-api/concepts
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Agreement Manager API
- Agreement Manager API
- Concepts
scraped_at: '2026-06-18T14:17:04Z'
---

# Agreement Manager Concepts

The following sections describe the objects and key terms used by Docusign Agreement Manager and the Agreement Manager API. See [Work with the Agreement Manager API schema](https://developers.docusign.com/docs/agreement-manager-api/concepts/work-with-agreement-manager-schema/) for details on the Agreement Manager API object model.

### Agreement

An agreement is a commitment between two or more parties that creates an obligation to perform (or not perform) a particular duty. Typically, agreements will contain a lot of other data, such as documents that describe the agreement being struck, parties who are involved in the agreement, dates defining the boundaries of the agreement, and many more. An agreement stored in Docusign Agreement Manager has the following retrievable data:

- A comprehensive overview of the agreement, including its title, type, status, summary, and more. This includes involved parties and related agreements.
- A full set of provisions that define the terms and conditions of the agreement, used for compliance and auditing purposes.
- A set of metadata that acts as a history for the agreement, such as creation and modification dates, parties, and user-defined fields.

Significant portions of this data may be generated as AI-assisted insights, but you can review, validate, and accept or modify these values manually through the UI.See [Key agreement properties and objects](https://developers.docusign.com/docs/agreement-manager-api/concepts/work-with-agreement-manager-schema/#key-agreement-properties-and-objects) for details.

### Document

Documents are artifacts associated with agreements that typically define the terms of the agreement to be made. An agreement’s documents are stored in Docusign Agreement Manager, and AI insights are generated from the contents of your agreement documents.

Unlike in Docusign eSignature, documents in the developer environment that are stored in Agreement Manager are not purged monthly. Instead, they will persist until the admin deletes the account.

### Parties

A party is a person, entity, or group of entities who take part in an agreement. Typically, this means agreeing with other parties to do something together, although it can include other stakeholders. For example, in an agreement to purchase a home, the parties might include the buyer and the seller. If the buyer or seller have agents, these agents may be parties to separate agreements outlining fees, terms of service, etc. 

A party can include one or more other parties. This means that you can manually create logical groups of parties such as “Microsoft” that may contain multiple Microsoft parties such as “Legal” or “Azure”, then select and filter results for any or all of them.

### AI Insights

Whenever you upload documents in Docusign Agreement Manager or complete a Docusign envelope, those documents are added to your account’s Agreement Manager repository. Agreement Manager then uses AI to analyze your documents and apply sets of Insights to them, automatically populating metadata about the agreement based on the contents of the documents. This can include (but is not limited to):

- The parties involved in the agreement
- The renewal date for the agreement
- Pricing details for the agreement
- Jurisdiction
- Terms
- The type of agreement
- A set of agreement provisions

Document metadata that has been populated by AI and not manually confirmed by an account user is marked with a purple star to the left of its value. You can open the agreement entry in the Agreement Manager UI and review or update these fields to confirm the data and remove this flag.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='394' width='232' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image of a UI screen showing navigator agreement attributes.](https://images.ctfassets.net/aj9z008chlq0/619RdoXFH8wZLmVXTKGoc4/8af15671d84ce8415f7e0948e9c338a4/NavigatorDetails.png?w=232&h=394&q=50&fm=png)

### Category and type

An agreement’s category object identifies the general purpose of the agreement, each of which is associated with a set of agreement types. For example, an agreement might have a category of Business services and a type of order form or a category of human resources and a type of offer letter.  See [Key agreement properties and objects](https://developers.docusign.com/docs/agreement-manager-api/concepts/work-with-agreement-manager-schema/#key-agreement-properties-and-objects) for details.

### Provisions

An agreement's provisions object contains a list of properties that define the agreement parameters. For example, a statement of work's provisions include properties such as an execution date, a total value, and a payment due date. Each agreement has multiple provisions.

## Next steps

- [What is Agreement Manager](https://developers.docusign.com/docs/agreement-manager-api/concepts/what-is-agreement-manager/)
- [How-to guides](https://developers.docusign.com/docs/agreement-manager-api/how-to/)
- [Typical Agreement Manager Roles and Use Cases](https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=gao1702944481420.html)
- [Agreement Manager Search Capabilities](https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=qzl1712244340883.html)

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
