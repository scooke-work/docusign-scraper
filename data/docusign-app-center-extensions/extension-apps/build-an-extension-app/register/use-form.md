---
title: Use a form to register an extension app
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Register
- Register
- Use Form
scraped_at: '2026-06-18T19:51:50Z'
---

# Use a form to register an extension app

This procedure explains how to register an extension app using a form. You also have the option of registering an extension app by [constructing a JSON app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/). See [Form-based and app manifest method comparison](https://developers.docusign.com/extension-apps/build-an-extension-app/register/#form-based-and-app-manifest-method-comparison) for guidance about which method might be more useful.

Before starting this procedure, make sure that you have completed or obtained the items listed in [Prerequisites for registering an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/#prerequisites-for-registering-an-extension-app).

To register an extension app using a form:

1. Log in to the [Developer Console](https://devconsole.docusign.com).
2. Select **Create App**, and then **Using a form-based experience**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='192' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Create App button](https://images.ctfassets.net/aj9z008chlq0/3a4x0KO4kOv1fotFfo277W/f30742da1235f199e76a02ac2e74082f/CreateApp_UsingForm.png?w=600&h=192&q=50&fm=png)
3. Enter basic information about the app:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='368' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Basic extension app information](https://images.ctfassets.net/aj9z008chlq0/1XHAhijDgwAjmYRnQmI5q5/2523da8a141a03f339a7dbc31a53f736/AppBasicInfo.png?w=660&h=368&q=50&fm=png)

   1. **App name.** The name of your extension app. This value must be unique; the maximum length is 30 characters. This name will appear in the [Docusign App Center](https://apps.docusign.com/app-center) listing for your extension app. For a data IO extension, this name will appear in [workflows](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html) on the step selection and step configuration screens. For a data verification extension, this name will appear in the [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html) when adding the extension to an envelope or template.
   2. **Published by.** The name of the extension app publisher. This value will appear with your extension app's name in all App Center locations that list your app. This value will also appear on your extension app's detail page in the App Center as the **Developer**.
   3. **Support email.** The email address of the extension app publisher. This will appear under **Resources** in the App Center listing.
4. Supply these values:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='397.00000000000006' width='500' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Distribution settings](https://images.ctfassets.net/aj9z008chlq0/29zz84B2MpGIKwVJZVK7zN/676be4e532142f1334202b37d90af420/DistributionType.png?w=500&h=397&q=50&fm=png)

   1. **Distribution Type.** Determines whether your extension app will be available in production to all users (public distribution) or only to users in accounts that you specify. To publish a public extension app, you must join the [Docusign Partner Program](https://partners.docusign.com/s/join-now). For more information, see [Choosing private distribution instead of public](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/).
      **Note:** Once an app has been published, its distribution type cannot be changed.
   2. **Connection Grant Type**. Determines whether your extension app will use [Authorization Code Grant](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/#authorization-code-grant) or [Client Credentials Grant](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/#client-credentials-grant) to authorize its access to your platform. Client Credentials Grant can only be selected if your **Distribution Type** is set to **Private**.
5. Select the extensions to include. See [Supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) for descriptions of each extension, their extension points, and links to more information.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='554' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Extension type selection](https://images.ctfassets.net/aj9z008chlq0/nEi5C1tfcom3RGMkV6Lg5/b40bb51d5e02e742ba4efac55f68c780/FormBasedExtensionSelection.png?w=660&h=554&q=50&fm=png)

   If you select **File Input Output**, you can select from the [supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) of that type.

   When registering an extension app, you cannot include both a [file output system of record extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-system-of-record/) and a [file output cloud storage extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-output-cloud-storage/) in the same app. If you need to use both types of output in workflows, register a separate app for each extension.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='426' width='782' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![File IO extension type](https://images.ctfassets.net/aj9z008chlq0/2n5jRwANky0dJCrXI1coPH/4b1050fe4001ac685e03c994a7d1a4d8/FileIOOptionsFormBased.png?w=782&h=426&q=50&fm=png)

   If you select **Data Input Output**, you have the option to select whether the extension app will only read data from a system of record or whether it will both read from and write to the system of record.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='245.99999999999997' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Data Input Output extension type selected](https://images.ctfassets.net/aj9z008chlq0/FkpKrbDMVqQTi4UGUtqL5/5a4f21e7d87731aa668a572c0c34fbed/FormBasedExtensionSelectionDataIO.png?w=660&h=246&q=50&fm=png)

   If you select **Data Verification**, you can select the type of data the extension app will verify.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='486.99999999999994' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Extension Type Data Verification selected](https://images.ctfassets.net/aj9z008chlq0/68gKWENoHaZGoGX7KoVKOU/accafcb3e3301712eb0e3e7d4c6cd432/FormBasedExtensionSelectionDataVerification.png?w=660&h=487&q=50&fm=png)
6. Select **Create App**.
7. A basic extension app registration and app manifest file are created, and the extension app **Overview** page is displayed.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1201' width='1446' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Overview page](https://images.ctfassets.net/aj9z008chlq0/4sIIKGejSjBwabPXoqLjN1/73a14c40079883a2a8eeef06edda430b/Overview.png?w=1446&h=1201&q=50&fm=png)

## Steps to complete extension app registration

Although your extension app registration has been created, you must complete these additional steps to supply all the required information:

- [Update the App Center listing](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/): Define the text and images that will be displayed to App Center users.
- [Update the integration details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/): Define the settings required to obtain authorization and connect to the external API endpoints for the [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/). You must complete this step before you can use the Developer Console's extension app [testing features](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).

  During the form-based extension app registration process, if you select a [file IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), its required actions are automatically added to the app. You can then configure the actions' endpoint URIs and other properties on the [Integration Details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/) page. The extension's optional capabilities can be added or removed only by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). After you've added capabilities via the manifest file, you can edit them on the Integration Details page. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action and capability properties in the app manifest file.

## Next steps

- Find out how to register an extension app [using an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/).
- Review the options for [updating extension app registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/).
- Learn how to [test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).

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
