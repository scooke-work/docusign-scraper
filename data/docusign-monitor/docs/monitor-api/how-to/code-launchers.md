---
title: Code example launchers
source_url: https://developers.docusign.com/docs/monitor-api/how-to/code-launchers/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Monitor API
- Monitor API
- How-to guides
- How-to guides
- Code example launchers
scraped_at: '2026-06-18T21:15:04Z'
---

# Code example launchers

*Code example launchers* are complete projects that show common API integration functions. They enable you to see how to make API and SDK calls, how the code fits into an application, and how that code runs. You can freely clone, download, and run the launchers from the [Docusign GitHub](https://github.com/docusign). They are available in all of our supported SDK programming languages: C#, Java, Node.js, PHP, Python, and Ruby. Each launcher accesses Docusign APIs through the objects and methods available in its own language’s SDK. If you’d like to access the raw API (not with an SDK), we also have launchers available in Bash and PowerShell.

## Code launchers and Quickstart

Most Docusign code examples contained in the code example launchers are also available with [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/). Quickstart enables you to download a ZIP file containing the same set of Developer Center code examples in a specified language that you would get with a code example launcher, but it comes preconfigured with your account data and supports [Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/) and [JSON Web Token (JWT) Grant](https://developers.docusign.com/platform/auth/jwt/) authentication. This enables you to load and run the code examples without any additional configuration steps.

Both Quickstart and code launchers provide a web UI that runs locally and enables you to explore and run your desired code example by choosing the appropriate link.

Use code example launchers or Quickstart to:

- Develop your own integration, using the example as a model
- Learn best practices for implementing a scenario
- See how [Docusign Monitor Authentication](https://developers.docusign.com/docs/monitor-api/monitor101/auth/) works within a sample app

## Examples and languages

Each launcher has its own installation instructions, dependencies, and prerequisites. The README file for each launcher contains the specific details:

- [Bash](https://github.com/docusign/code-examples-bash)
- [C#](https://github.com/docusign/code-examples-csharp)
- [Java](https://github.com/docusign/code-examples-java)
- [Node.js](https://github.com/docusign/code-examples-node)
- [PHP](https://github.com/docusign/code-examples-php)
- [PowerShell](https://github.com/docusign/code-examples-powershell)
- [Python](https://github.com/docusign/code-examples-python)
- [Ruby](https://github.com/docusign/code-examples-ruby)

## Generate test data

When executing Monitor API code examples, it’s useful to have test data in your developer account so that the responses contain realistic values. You can use the [MyAPICalls](https://myapicalls.sampleapps.docusign.com/) sample app to generate this test data. MyAPICalls has a collection of *scenarios,* or use cases, each of which includes a series of API requests. Executing a scenario once will generate one or more [tracked events](https://support.docusign.com/s/document-item?bundleId=gso1581445176035&topicId=crj1659119600990.html) that you can then retrieve using Monitor API requests. You can also configure MyAPICalls to run a scenario repeatedly using unique data each time, enabling you to quickly load a large volume of data into your developer account. This is helpful for testing and demonstrating dashboards that you’ve built with Monitor API calls. MyAPICalls sends API requests to the developer (demo) environment, not production.

Below is a list of MyAPICalls scenarios, and the tracked events that each one generates. To run any of the scenarios listed below, you can either access the scenario page directly via the link in the **Scenario** column, or you can visit the [MyAPICalls](https://myapicalls.sampleapps.docusign.com/) home page and select **Try scenario** for any scenario in the list. See the **Running the sample** panel on the scenario page for execution instructions.
> **Note:** The envelope signed event will be generated only if you complete the signing process for the envelope that the scenario creates.

| Scenario | Events generated |
| --- | --- |
| [Remote Signing with Template](https://myapicalls.sampleapps.docusign.com/scenario/1) | Template created Envelope created Envelope sent Envelope signed |
| [Embedded Signing](https://myapicalls.sampleapps.docusign.com/scenario/2) | Envelope created Envelope sent Envelope signed |
| [Responsive Signing](https://myapicalls.sampleapps.docusign.com/scenario/4) | Envelope created Envelope sent Envelope signed |
| [Phone Authentication](https://myapicalls.sampleapps.docusign.com/scenario/5) | Envelope created Envelope sent Envelope signed |
| [Create Connect Configuration and Receive Envelope Event](https://myapicalls.sampleapps.docusign.com/scenario/6) | Connect configuration created Envelope created Envelope sent Connect event sent Envelope signed |
| [Add a User](https://myapicalls.sampleapps.docusign.com/scenario/7) | Organization member added |
| [Composite Templates: Custom Forms with Shared Signature Document](https://myapicalls.sampleapps.docusign.com/scenario/9) | Template created Envelope created Envelope sent Envelope signed |

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
