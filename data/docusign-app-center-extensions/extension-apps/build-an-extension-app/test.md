---
title: Test an extension app
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Test
scraped_at: '2026-06-18T19:51:50Z'
---

# Test an extension app

The [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/) testing tools enable you to verify that your extension app has been configured correctly. These types of test are available:

- [Integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/): Confirm that Docusign can use the values supplied during extension app [registration](https://developers.docusign.com/extension-apps/build-an-extension-app/register/) to obtain [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/), send requests to an external API or [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/), and process the responses.
- [Functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/): Confirm that the extension app works as expected when invoked from a Docusign [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) or [workflow](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/workflows/) or from [Agreement Manager](https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=adf1702945446135.html). This type of test enables you to simulate the end user experience for an extension app.
- [App Center preview](https://developers.docusign.com/extension-apps/build-an-extension-app/test/app-center-preview/): Displays extension app details and images so that you can review them. This information will appear in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) after you've [published the extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/). This feature does not exactly replicate the App Center display, but it enables you to confirm that the extension app details you provided in the extension app manifest have been applied correctly.

## Test prerequisites

This table lists prerequisites for each type of test.

| Prerequisite | Required for integration tests | Required for functional tests | Required for App Center preview |
| --- | --- | --- | --- |
| [Register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). | Yes | Yes | Yes |
| Set up an [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) if necessary. | Yes | Yes | No |
| Obtain an account with the [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) provider. You'll need to supply these credentials for testing. The authorization provider is either the external service to which the extension app will send API requests, or an identity provider if you opt to use one for authorization. | Yes | Yes | No |
| Execute a successful [connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) for the extension app. | No | Yes | No |
| Execute successful [extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) for each of the extension app's extensions. | No | Yes | No |

## Test against different environments

While developing an extension app, you may need to test against multiple external service environments, such as a development environment, a test environment, and production.

Currently, extension app [registration](https://developers.docusign.com/extension-apps/build-an-extension-app/register/) supports connection properties for a single external service environment. To switch between environments for testing, you can [update the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#switch-test-environments-by-updating-the-extension-app-registration) when you want to switch environments, or you can [maintain separate extension app registrations](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#switch-test-environments-by-using-separate-extension-app-registrations) for each environment.

If you plan to make your extension app publicly available on the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/), make sure that you have supplied production URLs in your extension app registration before you [submit it for review](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/).

### Switch test environments by updating the extension app registration

If you want to use the same extension app registration for different test environments, complete these steps to switch environments:

1. [Update the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) and change these environment-specific properties:
   - Connection settings
     - If you update these settings using a form, see [Update connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) for steps to modify the **Client ID**, **Client secret**, and the authorization settings.
     - If you update these settings using the extension app manifest, see [Use a manifest file to update a registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). You'll need to update `clientId`, `clientSecret`, and authorization settings in the `customConfig` object. See [Connection schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) for details about these properties.
   - Action and capability settings
     - If you update these settings using a form, see [Update extension and action settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings) for steps to modify the **Params URI** values, which specify the endpoint URLs for each request to the external service.
     - If you update these settings using the extension app manifest, see [Use a manifest file to update a registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). You'll need to update `params.uri` for each action and capability. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for details.
2. After you update the extension app registration, the extension app is automatically reinstalled to your developer account, and you can proceed with running [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) and [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/).

### Switch test environments by using separate extension app registrations

If you choose to maintain separate extension app registrations for each test environment, Docusign recommends naming each non-production version to reflect the environment with which it's intended to be used.

To create an environment-specific copy of an extension app registration:

1. On the [Developer Console](https://devconsole.docusign.com) My Extension Apps page, select **Download Manifest** from the kebab menu of the extension app for which you want to create an environment-specific registration.
2. Edit the downloaded file, and change these environment-specific properties:
   - Enter a unique value for the `name` property.
   - Connection settings: Update `clientId`, `clientSecret`, and authorization settings in the `customConfig` object. See [Connection schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) for details about these properties.
   - Action and capability settings: Update `params.uri` for each action and capability, which specifies the endpoint URL for requests to the external service. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for details.
3. Select **Create App** in the upper right corner of the My Extension Apps page, and then select **By editing the manifest**.
4. Under **Have your own manifest?** select the modified manifest file or drag and drop to upload it.
5. Select **Validate** and correct any validation errors.
6. Select **Create App** to save the registration.
7. You can proceed with running [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) and [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) for the new environment-specific registration.

## Next steps

- Learn how to run [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/).
- Find out more about [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/).
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
