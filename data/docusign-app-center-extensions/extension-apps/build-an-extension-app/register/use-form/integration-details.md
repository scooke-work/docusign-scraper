---
title: Update integration details
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Register
- Register
- Use Form
- Use Form
- Integration Details
scraped_at: '2026-06-18T19:51:51Z'
---

# Update integration details

This procedure enables you to use a form to define settings required to obtain [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) and connect to endpoints in the external API service. Instead of using a form, you can define the settings by [creating](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/) or [updating](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/) a JSON app manifest file.

## Access integrations details for an extension app

To access an extension app’s integration details:

1. Log in to the [Developer Console](https://devconsole.docusign.com).
2. On the **My Extension Apps** page, locate the row for the extension app you want to update.
3. Select the app to open the **Overview** page.
4. In the left navigation, select **Integration Details**.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1132' width='1413' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Integration details](https://images.ctfassets.net/aj9z008chlq0/4JPdDP916EOgjh5pq0A74T/7e5eb50469456d6212925a57eb3ad5cd/IntegrationDetailsMainPage.png?w=1413&h=1132&q=50&fm=png)

If the extension app registration is newly created, define both the [connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) and the [extension and action settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings).

If you are updating an existing extension app registration, you can modify only the settings you want to change.

## Update connection settings

[Connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/) settings enable an extension app to obtain authorization from the external API service or identity provider.

To update an extension app’s connection settings:

1. [Access the Integration Details page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#access-integrations-details-for-an-extension-app).
2. Under **Connection**, select **Edit**.
3. Enter or update these values:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='281' width='1221' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Connection name and description](https://images.ctfassets.net/aj9z008chlq0/30bv3Aff0XcAyC2dg5QuCK/858fa6fcf2648fae32277528bc1959c3/IntegrationDetails_ConnectionBasicInformation.png?w=1221&h=281&q=50&fm=png)

   1. **Connection name.** The name of the connection. This value must be unique. This name will appear in these locations: the Developer Console [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) page; the Docusign App Center page where users [install and connect](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) your extension app; and the Workflow Builder workflow step configuration page, for extensions that can be used in a workflow.
   2. **Description.** A description for the connection.

      ![](data:image/svg+xml;charset=utf-8,%3Csvg height='454' width='1214' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

      ![Scopes, Client ID, Client Secret](https://images.ctfassets.net/aj9z008chlq0/60MdICE43vD1UCrw9PI90H/892a60f7253b8db4e8b1fa507aae6d7d/IntegrationDetails_ConnectionParameters.png?w=1214&h=454&q=50&fm=png)
   3. **Scopes.** Any scopes that are required for authorization. See [Scopes](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/#scopes) for more information. If you are supplying more than one scope, separate them with spaces.
   4. **Client ID.** The client ID that is required for [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) with the external platform.
   5. **Client secret.** The client secret that is required for authorization with the external platform.

      ![](data:image/svg+xml;charset=utf-8,%3Csvg height='477' width='1216' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

      ![Authorization URL, Token URL, Authorization Method](https://images.ctfassets.net/aj9z008chlq0/5s4kFiKdKPZi6l48OctXAB/e5c05b7eda44b410a4de8cbc332afd98/IntegrationDetails_ConnectionCustomConfig.png?w=1216&h=477&q=50&fm=png)
   6. **Authorization URL.** The OAuth 2.0 authorization endpoint. When the Docusign platform makes a request to this endpoint, the external service returns an authorization code. The URL’s top-level domain must be one of the following: `.com`, `.net`, `.org`, `.app`, or `.cloud`. Do not include `docusign.` in the domain. If the OAuth 2.0 grant type is Client Credentials, this setting does not appear.
   7. **Token URL.** The OAuth 2.0 token endpoint. When the Docusign platform provides an authorization code in a request to this endpoint, the external service returns an access token that will be included in all subsequent API requests from the extension app to the external service.
   8. **Authorization method.** If you set this value to **header**, when Docusign makes a request to the authorization URL, the client ID and client secret will be sent in the request header. If you set this to **body**, they will be sent in the request body.

      ![](data:image/svg+xml;charset=utf-8,%3Csvg height='266' width='1217' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

      ![Auth Params](https://images.ctfassets.net/aj9z008chlq0/3tV6UDgDkw2ci1tPTnMFgt/e4a970eeb9d34464a5498f94ea6cef9a/IntegrationDetails_ConnectionAuthParams.png?w=1217&h=266&q=50&fm=png)
   9. **Auth params.** A set of query parameters required for the authorization URL. If the OAuth 2.0 grant type is Client Credentials, this setting does not appear.
4. Select **Save**.
5. If prompted, re-enter the client secret and select **Save**.

## Update extension and action settings

For the [file IO extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), you can add or remove [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) only by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). After you've added capabilities via the manifest file, you can edit them on the Integration Details page.

[Extension](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/) and [action](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) settings determine which functionality the extension app offers, such as importing files from or writing files to cloud storage, reading data from or writing it to a system of record, or verifying customer information such as a bank account. These settings also provide the information that the Docusign platform uses to send requests to the external API endpoints that provide this functionality.

To update an extension app’s extension and action settings:

1. [Access the Integration Details page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#access-integrations-details-for-an-extension-app).
2. Under **Extensions & Actions**, locate the extension whose settings you want to define.
3. Select **Edit**.
4. Enter or update these values:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='450' width='1216' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Extension Name and Description](https://images.ctfassets.net/aj9z008chlq0/6WQUgh4SMyRMi96q6sv4nw/d5f3656d822b69aac1055a34cdfca373/IntegrationDetails_ExtensionSettings.png?w=1216&h=450&q=50&fm=png)

   1. **Extension name.** A name for the extension. For file input cloud storage extensions, the name will appear in a list of document sources on the Agreement Manager **Upload Documents** window. For file output cloud storage and file output system of record extensions, the name will appear on the Workflow Builder workflow step selection and step configuration screens.
   2. **Description.** A description for the extension. For file output cloud storage, file output system of record, and data IO extensions, this description will appear on the Workflow Builder workflow step selection screen.
5. For each of the extension's actions, enter or update these values:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='473' width='1221' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Action Name, Description, URI](https://images.ctfassets.net/aj9z008chlq0/2gWREZ6PeRAplbWin2L7XC/c38669afd6b21b8166294b8e49abc1e5/IntegrationDetails_ActionSettings.png?w=1221&h=473&q=50&fm=png)

   1. **Name.** A name for the action. This name will appear on the Developer Console [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) page. For file IO extensions, the name is not editable.
   2. **Description.** A description for the action.
   3. **Params URI.** The URI of the external API endpoint that will be called by the action.
6. Select **Save**.

## Add an extension

To add an extension to an extension app registration:

1. [Access the Integration Details page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#access-integrations-details-for-an-extension-app).
2. Under **Extensions & Actions**, select **Add Extension**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='533' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Add an extension](https://images.ctfassets.net/aj9z008chlq0/6yOVxDD0pCsbwtqqD4dcLu/cb911861d251b09162ed9bde88cc3ec1/IntegrationDetails_AddExtension.png?w=660&h=533&q=50&fm=png)
3. Select an extension type and select **Next**. For information about the available types and the associated extensions, see [Supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/).
4. Depending on the extension type you select, you may be presented with additional choices. For example, these choices are available for data IO:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='245' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Data IO types](https://images.ctfassets.net/aj9z008chlq0/27PJjU1NJGf4hAzsm9nWtf/b7156272121ae810962e814f28432b8d/IntegrationDetails_AddExtensionSelect.png?w=660&h=245&q=50&fm=png)

   Make a selection, and select **Finish**.
5. Populate the extension and action values. See [Update extension and action settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings) for descriptions of the values.
6. Select **Save**.

## Delete an extension

To delete an extension from an extension app registration:

1. [Access the Integration Details page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#access-integrations-details-for-an-extension-app).
2. Under **Extensions & Actions**, locate the extension you want to remove.
3. Select **Delete**.
4. Select **Delete** on the confirmation window.

## Next steps

- Review the procedure to [update the App Center listing](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/) for an extension app.
- See how to update an extension app registration by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/).

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
