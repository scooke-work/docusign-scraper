---
title: Functional tests
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Test
- Test
- Functional Tests
scraped_at: '2026-06-18T19:51:51Z'
---

# Functional tests

Functional tests enable you to launch extension app functionality from a Docusign agreement process to verify that it works correctly for end users.

You can set up a functional test that invokes an extension app from these Docusign features:

- [Workflows](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/): Create an Agreement Builder workflow that invokes your extension app. Execute the test by creating and executing an instance of the workflow. This enables you to run through the workflow steps as an end user would and verify that the extension behaves as expected.
- [Envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/): Create an [eSignature template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=dqj1578456412286.html&rsc_301), add a document to it, and configure fields that invoke your extension app. Execute the test by generating an envelope from the template and completing the signing process. When you enter values in the fields that invoke the extension, you can verify that the extension works correctly.
- [Agreement Manager](https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=adf1702945446135.html): Invoke your extension app to locate files on a cloud storage system and import them into Agreement Manager. As you complete this test, you can verify that the extension can successfully retrieve cloud storage drive, folder, and file information and upload files.

Below is a list of [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), the functional test types that Docusign supports for each extension, and links to procedures for setting up and executing the tests.

| Extension type | Extension | Workflow test procedure | Envelope test procedure | Agreement Manager test procedure |
| --- | --- | --- | --- | --- |
| Connected fields | Connected fields | Not supported in the current release | [Connected fields extension envelope test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/connected-fields-envelope/) | Not supported in the current release |
| Data IO | Data IO | [Data IO extension workflow test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/) | Not supported in the current release | Not supported in the current release |
| Data verification | Bank account owner verification Bank account verification Business FEIN verification Email address verification Phone verification Postal address verification SSN verification | Not supported in the current release | [Data verification extension envelope test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-verification-envelope/) | Not supported in the current release |
| File IO | File input cloud storage | Not supported in the current release | Not supported in the current release | [File input cloud storage extension Agreement Manager test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-input-cloud-storage-agreement-manager/) |
| File IO | File output cloud storage | [File output cloud storage extension workflow test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-cloud-storage-workflow/) | Not supported in the current release | Not supported in the current release |
| File IO | File output system of record | [File output system of record test: Workflow step creates envelopes](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-system-of-record-workflow-step-creates-envelopes/) [File output system of record test: An event triggers the workflow](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-system-of-record-event-triggers-workflow/) | Not supported in the current release | Not supported in the current release |
| File IO | File output tabular format | [File output tabular format extension workflow test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-output-tabular-format-workflow/) | Not supported in the current release | Not supported in the current release |

The tests will run against the external API service environment (development, test, or production) configured in the extension app [registration](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). See [Test against different environments](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-against-different-environments) for information about switching environments.

## Next steps

- Get details about the structure of the [extension app manifest](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/).
- Learn how to run [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/).
- See how to use the [App Center preview](https://developers.docusign.com/extension-apps/build-an-extension-app/test/app-center-preview/).

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
