---
title: Workflow Builder API 101
source_url: https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Workflow Builder API
- Workflow Builder API
- Workflow Builder101
scraped_at: '2026-06-18T17:59:18Z'
---

# Workflow Builder API 101

The Workflow Builder API enables you to create and manage branching end-to-end Workflow Builder workflows that can extend beyond getting an agreement through eSignature. 

Getting an agreement is often only one step in a complex workflow process that can have many steps and many requirements for both before and after agreement. These steps can include collecting customer information, verifying identity, reading and writing data to and from your system of record, getting signatures, or starting follow up actions. This can require using several disparate systems and can be challenging to build, connect, maintain, and automate across systems and teams.

The Workflow Builder API simplifies this process dramatically by enabling you to build workflows that streamline your agreement processes. A workflow is an easily-configurable sequence of steps and conditional logic that defines everything you need to automate your agreement process in one place. 

Workflow Builder workflows support Docusign modules and functionality that enable you perform every step in your complex workflows, including:

- eSignature
- Web forms
- Identity verification
- Read from and write to files
- Get signatures
- Send email

Workflow Builder workflows can use [Extension apps](https://developers.docusign.com/extension-apps/) as steps, extending the Docusign platform by integrating capabilities from third parties . See [Supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) for details on which categories of extensions are supported or browse available extensions on the [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

This diagram shows examples of the kinds of functionality you can add to steps in your Workflow Builder workflows:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='329' width='736' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Diagram showing various Maestro API workflow options](https://images.ctfassets.net/aj9z008chlq0/7bep5yVzDNew0SdNTGr6p7/9de91ccb89984613af7538b0e17fd109/maestroModules.png?w=736&h=329&q=50&fm=png)

You can choose and sequence the steps in your workflow as needed. For example, this enables you to have an ID verification (IDV) step before a web form step to verify a participant’s identity before showing sensitive pre-filled data.

The individual steps in a workflow can be configured to call Docusign endpoints and use Docusign features, get participant data, branch on conditions that you set, and invoke [Extension apps](https://developers.docusign.com/extension-apps/) that you’ve installed and enabled to perform actions (such as archiving files or verifying data) with third-party platforms, as shown in this outline diagram.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='656' width='1058' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Diagram showing an example of how a Workflow Builder workflow is composed of a series of sequential steps](https://images.ctfassets.net/aj9z008chlq0/JOo2iDxDItFzXOr2bSnHS/6693fde593ff923e5e803dead08043b2/workflowBuilderExample.png?w=1058&h=656&q=50&fm=png)

You can build a Workflow Builder workflow entirely within the Workflow Builder API, or use the workflow designer UI for a no-code experience. The Workflow Builder API and UI support the same set of functionality and have the same capabilities.

Once you have created a workflow, you can execute it manually in the workflow designer, load a special URI that is specific to that workflow, or make a POST request to the trigger URL in the Workflow Builder API. See [Workflows](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/) for details or [How to trigger a Workflow Builder workflow](https://developers.docusign.com/docs/workflow-builder-api/how-to/trigger-workflow/) for a full walkthrough.

Check out the [Workflows Sample App](https://workflows.sampleapps.docusign.com/) to see the Workflow Builder API in action.

## Next steps

- Learn about [Workflows](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/)
- Learn about extending the Docusign platform with [Extension apps](https://developers.docusign.com/extension-apps/) and the Docusign [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/)
- See the [Workflow Builder support](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=dnx1696972415150.html) documentation
- Try out the [Workflows Sample App](https://workflows.sampleapps.docusign.com/)

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
