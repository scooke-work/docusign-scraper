---
title: Register an extension app
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/register/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Register
scraped_at: '2026-06-18T19:51:50Z'
---

# Register an extension app

When you register an extension app in the [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/), you configure parameters that determine how the app functions as well as metadata that describes the app. These settings include:

- The [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) the extension app uses
- Parameters required to obtain [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) and connect to external API endpoints
- The distribution type: [public or private](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/)
- The description, icon, screenshots, and other details that appear in the extension app's [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) listing

You have two options for app registration:

- [Use a guided form-based UI](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/): This process enables you to register an extension app by filling out fields in the Developer Console.
- [Use an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/): In this process, you register the extension app by populating values in a JSON file that you upload or paste into the Developer Console app manifest editor.

## Form-based and app manifest method comparison

This table shows which extension app registration method is more useful in various scenarios.

| If you want to | Select this method | Because |
| --- | --- | --- |
| Register an extension app using the easiest method | Form-based | This method presents all required fields in a user-friendly UI and guides you through the process of populating the fields. |
| Spend less time troubleshooting | Form-based | This method ensures that you can only supply valid values for extension app settings, and it automatically populates some values to reduce the risk of errors. |
| Enable non-technical users in your organization to define App Center listing details | Form-based | The Developer Console has a dedicated page where the description, icon, screenshots, and other App Center listing details can be defined, and it's separate from the technical settings related to authorization and API endpoints. |
| Register a new extension app by copying an existing app's details | App manifest file | This method enables you to download the app manifest file for an existing extension app, modify it, and register a new extension app by uploading the modified file. |
| Update multiple settings via a search and replace | App manifest file | This method enables you to quickly replace multiple values either directly in the app manifest editor or by downloading the manifest, replacing values, and uploading the new version. |
| Test an extension app using a [reference implementation](https://www.docusign.com/blog/developers/fast-track-your-extension-apps-with-reference-implementations) that Docusign provides on GitHub | App manifest file | The GitHub repos include preconfigured manifest files that require only minor modifications to work with a local copy of a reference implementation. You can upload your modified file to register a sample extension app that enables you to test with the reference implementation. |

## Manifest is created regardless of registration method

When you register an extension app via a form, the Developer Console saves the app details in a manifest file. You can update app details by editing this file or using the form-based UI. Similarly, extension apps registered via a manifest file can be updated through either the form-based UI or by editing the manifest file directly. See [Update an extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) for details about how to use each method.

## Prerequisites for registering an extension app

These prerequisites apply for both the form-based and app manifest file methods for registering an extension app:

- You will need a Docusign [developer account](https://www.docusign.com/developers/sandbox) with admin privileges.
- If your app will use external API service endpoints that don’t conform to the Docusign [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/), you may need to set up an [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) to translate the external API’s requests and responses to the format that Docusign expects.
- You will need to obtain the external service, identity provider, and API proxy information that you will need to configure your extension app. This includes endpoint URLs, [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) details, and required parameters in requests to the endpoints and in the responses.

## Next steps

- Learn how to register an extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/).
- Find out how to register an extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/).
- Review the options for [updating extension app registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/).

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
