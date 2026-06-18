---
title: How extension apps work
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/how-extension-apps-work/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- How Extension Apps Work
scraped_at: '2026-06-18T19:51:48Z'
---

# How extension apps work

An extension app incorporates external platform functionality by defining API call [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/). An *action* is a reference to an external platform endpoint that will be triggered during your agreement process. 

Actions are enabled and applied to your workflows in groupings, called [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/). An *extension* is a set of actions that work together to enable a type of functionality for your workflow. For example, an extension to archive files may require actions to list and to upload files; these actions are enabled together as part of an extension. References to commonly-used actions can be shared between multiple extensions. 

The type of extension defines which actions must be implemented to support it. For example, the file output to cloud storage extension contract requires an action to write files, so all file output extensions must define this type of action. In addition to required actions, an extension can also define optional [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/). *Capabilities* are additional actions that are not required, but can add more functionality to an extension app. For example, the List Drives capability returns a list of cloud storage drives so that the workflow preparer can select one.

Places in Docusign workflows where an action or capability can be triggered are called [extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/#extension-points). For example, an action to write data to a system of record has an extension point for when a webform is [completed](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=wdm1578456348227.html). When this happens, the extension point is triggered and the associated action will write the data back to the system of record. 

The following diagram shows a typical extension app execution flow in the context of verifying bank account data:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1528' width='1366' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image showing the steps in an example extension app execution flow.](https://images.ctfassets.net/aj9z008chlq0/4Tv2JDe1lJvtkMkQ2l8kq4/b1ecd42123c8b8302d8e0817fcd643d0/example_extension_app_execution_flow.png?w=1366&h=1528&q=50&fm=png)

When an action or capability is triggered, it calls an external platform endpoint and returns the response data to Docusign. Depending on which extension point triggered the action, the response data or action prompts may be surfaced to the user through the Docusign UI.

For example, if an extension action calls a data verification endpoint to verify bank account data within an eSignature agreement and errors are found, the Docusign UI will prompt the end user to correct their information.

## Next steps

- See [What's inside an extension app](https://developers.docusign.com/extension-apps/extension-apps-101/inside-an-extension-app/) for details on how to register an extension app in the [Docusign Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/).
- See [Extension app use cases](https://developers.docusign.com/extension-apps/extension-apps-101/use-cases/) for examples of how extension apps can extend Docusign functionality.
- Watch a video on [How to integrate external features using extension apps](https://bcove.video/4itWmK8) for guidance on connecting external services to an extension app.

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
