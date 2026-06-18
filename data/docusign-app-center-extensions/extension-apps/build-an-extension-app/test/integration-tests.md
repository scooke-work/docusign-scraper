---
title: Integration tests
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Test
- Test
- Integration Tests
scraped_at: '2026-06-18T19:51:51Z'
---

# Integration tests

The [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/) provides two types of integration tests:

- [Connection tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test): Verify that the extension app can obtain [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) from the external API service or identity provider. This test also replicates the customer experience of configuring a connection after [installing the extension app](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) in the App Center.
- [Extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test): Verify that the extension app can send requests to external API endpoints or [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) endpoints and process the responses. The extension tests available for an extension app depend on which [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) the app uses.

See [Test prerequisites](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-prerequisites) for information about tasks you must complete before you can run these tests.

The tests will run against the external service environment (development, test, or production) configured when the extension app was [registered](https://developers.docusign.com/extension-apps/build-an-extension-app/register/). See [Test against different environments](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-against-different-environments) for information about switching environments.

## Run a connection test

This test obtains [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) from the external API service or identity provider. It uses the [connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) supplied when registering the extension app using a form or the [connection object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) properties supplied in the extension app manifest. Running this test requires you to supply login credentials for the authorization provider.

To run a connection test:

1. Log in to the [Developer Console](https://devconsole.docusign.com).
2. On the **My Extension Apps** page, locate the row for the extension app you want to test.
3. Select the app to open the **App Overview**.
4. In the left navigation, select **App Testing**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1076' width='1776' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Connection test figure 1](https://images.ctfassets.net/aj9z008chlq0/1SF2RF5P3G28B1mv0O310O/a7c8f852b5210087ea00d0a04bb2541e/AppTesting_AppNotInstalled.png?w=1776&h=1076&q=50&fm=png)
5. If a banner displays the message **App is not installed to your developer account**, as shown above, select **Install app**.

   After installation, the banner displays the message **App is installed to your developer account**.

   If you previously installed the extension app and have [updated the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) since then, the updates are automatically applied to your installed version. You do not need to reinstall after updating the registration.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1085' width='1758' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Connection test figure 2](https://images.ctfassets.net/aj9z008chlq0/4aw99m7Otwk4Vb8ZfCuhlW/728055ab4724b12516127162909a8b3b/AppTesting_AppInstalled.png?w=1758&h=1085&q=50&fm=png)
6. Select **Run Test** in the **Connection** row to display the test page:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='452.99999999999994' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Connection test figure 3](https://images.ctfassets.net/aj9z008chlq0/2lyofWYWXk8Z2CT3WIweVu/54793eb81f0496b815c74d4014c62089/ConnectionTest.png?w=600&h=453&q=50&fm=png)
7. Select **Run Test**.
8. When prompted, supply your credentials for the authorization provider.
9. The test executes and test results are displayed.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='264' width='730' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Connection test figure 4](https://images.ctfassets.net/aj9z008chlq0/4UJkYAGirAQ5tNZwM6RkeD/d05a749eea3defec896082b74535dff3/ConnectionTestSucceeded.png?w=730&h=264&q=50&fm=png)

   If the test fails, the results include an error message. See [Connection test errors](https://developers.docusign.com/extension-apps/troubleshooting/#connection-test-errors) for troubleshooting tips.

## Run an extension test

This test launches a request to the external API endpoint or [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/) endpoint configured for an [action](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) or [capability](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/). It uses the value from the [Params URI](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings) setting in the form-based extension app registration process or the extension app manifest [actions.params.uri](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) property. The test confirms that the endpoint is reachable and that the response is in the format Docusign expects. Extension tests use the authorization obtained from a [connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test).

The Developer Console extension tests include all actions and capabilities that are implemented in the extension app registration. Extension tests are executed from the Docusign platform directly to external endpoints. Running extension tests is an important step in extension app development. However, it is also important to test all of the extension app’s actions and capabilities from the [extension point](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/#extension-points), such as eSignature, Agreement Builder, or Agreement Manager. See [Functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) for more information about testing from extension points.

Before you can run an extension test, you must first complete a successful [connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test). If you previously installed the extension app and have [updated the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) since then, the updates are automatically applied to your installed version. You do not need to reinstall after updating the registration.

To run an extension test:

1. Log in to the [Developer Console](https://devconsole.docusign.com).
2. On the **My Extension Apps** page, locate the row for the extension app you want to test.
3. Select the app to open the **App Overview**.
4. In the left navigation, select **App Testing**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1093' width='1750' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Extension test figure 1](https://images.ctfassets.net/aj9z008chlq0/F3OExB7eX5h9La2UeRHuh/3389d91d03170fbb3f2e188ef8d01132/AppTestingAppInstalledConnectionTestComplete.png?w=1750&h=1093&q=50&fm=png)
5. Locate the **Extension** row for the action or capability you want to test.
6. Select **Run Test** in the appropriate row to display the test page.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='784' width='550' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Extension test figure 2](https://images.ctfassets.net/aj9z008chlq0/4oH7PSZLNiP8kV85K5dZNX/890f8c8786f4116404ef3990ac7510a8/ExtensionTest.png?w=550&h=784&q=50&fm=png)
7. Confirm that the endpoint URL shown is correct. This value is populated from the [Params URI](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings) setting in the form-based extension app registration process or the [params.uri](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) property in your extension app manifest and it cannot be edited on this test screen. If it's not correct, [update the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/).
8. Supply request body property values to include with the request. The action contract has details about these properties. You can access action contract details for each extension from the [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) page.
9. Select **Run Test**.
10. The test results and response from the external system are displayed.

    ![](data:image/svg+xml;charset=utf-8,%3Csvg height='398' width='720' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

    ![Extension test result](https://images.ctfassets.net/aj9z008chlq0/7pgpWqrJgXsvu9vuTXLu5J/b259d9b9065710efbe1fdf250b6fa14f/ExtensionTestResult.png?w=720&h=398&q=50&fm=png)

If the test fails, the results include an error message. See [Extension test errors](https://developers.docusign.com/extension-apps/troubleshooting/#extension-test-errors) for troubleshooting tips.

## Next steps

- Learn how to [troubleshoot errors](https://developers.docusign.com/extension-apps/troubleshooting/).
- Get details about the structure of the [extension app manifest](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/).
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
