---
title: Update App Center listing
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/
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
- App Center Listing
scraped_at: '2026-06-18T19:51:51Z'
---

# Update App Center listing

This procedure enables you to use a form to define the text and images that appear in the extension app listing in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/). Instead of using a form, you can define the settings by [creating](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/) or [updating](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/) a JSON app manifest file.

## Access App Center listing for an extension app

To access an extension app's App Center listing:

1. Log in to the [Developer Console](https://devconsole.docusign.com).
2. On the **My Extension Apps** page, locate the row for the extension app you want to update.
3. Select the app to open the **Overview** page.
4. In the left navigation, select **App Center Listing**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1526' width='2998' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![App Center Listing page](https://images.ctfassets.net/aj9z008chlq0/47LwKHBJE0Yf3ZUgfuXAsI/e5f2fd4864a2d4071c815d4618017e3a/Screenshot_2025-06-10_at_11.52.05â__AM.png?w=2998&h=1526&q=50&fm=png)
5. If the extension app registration is newly created, define these settings:
   - [Screenshots](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#manage-screenshots)
   - [Basic information](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-basic-information)
   - [App icon](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-app-icon)
   - [Publisher details and contact information](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-publisher-details-and-contact-information)
   - [Distribution details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-distribution-details)

     If you are updating an existing extension app's registration, you can modify only the settings you want to change.

     If you are updating the registration for a published extension app, you must supply a list of changes for the [changelog](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-changelog).

## Manage screenshots

Screenshots appear with your extension app listing in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/). You can provide a maximum of four images. The screenshots will be displayed in the order in which you upload them.

Each screenshot must have a 16:10 aspect ratio. Permitted dimensions range from a minimum of 848x530 pixels to a maximum of 1600x1000 pixels. Docusign recommends using the maximum size. The maximum file size per image is 5 MB. The allowed file types are JPEG and PNG.

**To add a screenshot:**

1. [Access the App Center Listing page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#access-app-center-listing-for-an-extension-app).
2. In the **Screenshots** section, do one of the following:
   - Drag and drop the file.
   - Use the **Select File** option to open a dialog where you can choose a file.

     ![](data:image/svg+xml;charset=utf-8,%3Csvg height='422' width='1250' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

     ![Screenshots](https://images.ctfassets.net/aj9z008chlq0/49xRU48D8M30f1i1C8jzIQ/1c257d9426df205b6d0f712e852a338e/Screenshots.png?w=1250&h=422&q=50&fm=png)
3. A thumbnail of the uploaded file appears in the **Files Uploaded** section.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='253' width='323' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Files uploaded](https://images.ctfassets.net/aj9z008chlq0/71ZA2M5GcZZVkuxNnAV8lr/ca932f76a6693ce75948080221bb527f/FilesUploaded.png?w=323&h=253&q=50&fm=png)

**To update a screenshot:**

1. [Access the App Center Listing page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#access-app-center-listing-for-an-extension-app).
2. In the **Files Uploaded** section, select the screenshot you want to update.
3. On the dialog that appears, select **Upload New File**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='561' width='900' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Updating a screenshot](https://images.ctfassets.net/aj9z008chlq0/1H6hqiVREJ72hSpKeCnIoa/9fb56f5c0a5a7564603149223e0fa8d9/UpdateScreenshot.png?w=900&h=561&q=50&fm=png)
4. Select the new file.
5. Close the dialog.
6. A thumbnail of the new file appears in the **Files Uploaded** section.

**To delete a screenshot:**

1. [Access the App Center Listing page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#access-app-center-listing-for-an-extension-app).
2. In the **Files Uploaded** section, select the screenshot you want to delete.
3. On the dialog that appears, select **Delete**.
4. The thumbnail for the deleted file no longer appears in the **Files Uploaded** section.

## Update basic information

This procedure enables you to update an extension app display name and short and long description.

To update basic information:

1. [Access the App Center Listing page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#access-app-center-listing-for-an-extension-app).
2. In the **Basic information** section, update these fields as needed:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='948' width='2038' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![App name, short description, long description](https://images.ctfassets.net/aj9z008chlq0/4rnGB3f1wSyOSBva21f58o/f48520b3b22604befdd8efc37421b651/Screenshot_2025-06-10_at_11.45.28â__AM.png?w=2038&h=948&q=50&fm=png)

   1. **App name.** The name of your extension app. This value must be unique. Maximum length is 30 characters. This name will appear in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) listing for your extension app. For a data IO extension, this name will appear in [workflows](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html) on the step selection and step configuration screens. For a data verification extension, this name will appear in the eSignature [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html) when adding the extension to an envelope or template.
   2. **Short description.** A description of your extension app that will appear on the Docusign App Center page where users can browse for extension apps to install. The maximum length is 100 characters.
   3. **Long description.** A description of your extension app that will appear on  the Docusign App Center page where users can find detailed information about your extension app. The maximum length is 2,000 characters.
3. Select **Save**.

## Update app icon

The app icon appears with your extension app's name on all list and detail pages in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/). If your extension app is used in [workflows](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html), the app icon appears on the workflow step selection screen, the workflow setup screen, and the step configuration screen. The app icon also appears on the Developer Console extension app list page and all the extension app detail pages.

The app icon must have a 1:1 aspect ratio. The maximum dimensions are 100x100 pixels. Docusign recommends using the maximum dimensions. The maximum file size is 5 MB. The allowed file types are JPEG and PNG.

To update the app icon:

1. [Access the App Center Listing page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#access-app-center-listing-for-an-extension-app).
2. In the **App Icon** section, to add or update an icon image, do one of the following:
   - Drag and drop the file.
   - Use the **Select File** option to open a dialog where you can choose a file.

     ![](data:image/svg+xml;charset=utf-8,%3Csvg height='348' width='1159' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

     ![App icon](https://images.ctfassets.net/aj9z008chlq0/302XCHPT6cbbwobtt1MpxL/2400eda0694b4f98f7ffa5c516a34f69/AppIcon.png?w=1159&h=348&q=50&fm=png)
3. The uploaded file appears in the **App Icon** section.

## Update publisher details and contact information

Publisher details and contact information appear in your extension app listing in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

To update publisher details and contact information:

1. [Access the App Center Listing page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#access-app-center-listing-for-an-extension-app).
2. In the **Publisher details** and **Publisher contact** sections, update these fields as needed:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='649' width='1169' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Publisher details](https://images.ctfassets.net/aj9z008chlq0/521a25a9PC5VbkznRglhsa/d07fa0e8a208ca20256989bd0da93ebf/PublisherDetails.png?w=1169&h=649&q=50&fm=png)

   1. **Published by.** The name of the extension app publisher. This value will appear with your extension app's name in all App Center locations that list your app. This value will also appear on your extension app's detail page in the App Center as the **Developer**.
   2. **Support URL.** The URL at which users can obtain support for your extension app. Your extension app's detail page in the App Center will include this URL as the destination for the **Support** link under **Resources**.
   3. **Terms of service URL.** The URL of your extension app’s terms of service. Your extension app's detail page in the App Center will include this URL as the destination for the **Terms of Service** link under **Resources**.
   4. **Privacy policy URL.** The URL of your extension app’s privacy policy. Your extension app's detail page in the App Center will include this URL as the destination for the **Privacy Policy** link under **Resources**.
   5. **Signup URL.** The URL at which users can create an account with the API service to which your extension app connects. The App Center page where users install your extension app will include this URL as the destination for the **Sign Up** link.

      ![](data:image/svg+xml;charset=utf-8,%3Csvg height='392' width='1174' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

      ![Publisher contact info](https://images.ctfassets.net/aj9z008chlq0/oM7Ts0RI7MpuyAnmkk7KZ/31463005ea7c60678f599f3923f317dd/PublisherContact.png?w=1174&h=392&q=50&fm=png)

      **Note:** You must supply at least one of the next three values.
   6. **Publisher website.** The URL of the app publisher's website. Your extension app's detail page in the App Center will include this URL as the destination for the publisher name link under **Developer**.
   7. **Support email.** The email address of the app publisher. If provided, the email address will be listed on your extension app's detail page in the App Center under **Resources**.
   8. **Support phone.** The phone number at which users can receive support for your extension app. If provided, the phone number will be listed on your extension app's detail page in the App Center under **Resources**.
3. Select **Save**.

## Update distribution details

The distribution details determine which users in the production [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) can install your extension app.

To update distribution details:

1. [Access the App Center Listing page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#access-app-center-listing-for-an-extension-app).
2. Update these fields as needed:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='656' width='1026' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Distribution details](https://images.ctfassets.net/aj9z008chlq0/1JyI3v3sFgP6ZxEP2sUTZc/cb9d3af99d884aacbd63c4e2f3fc53f3/ExtensionAppFormBasedDistributionDetails.png?w=1026&h=656&q=50&fm=png)

   1. **Distribution Type.** Determines whether your extension app will be available in production to all users (public) or only to users in accounts that you specify (private). You cannot change this setting after an extension app has been published. To publish a public extension app, you need to join the [Docusign Partner Program](https://partners.docusign.com/s/join-now). For more information, see [Choosing private distribution instead of public](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/).
   2. **Region.** The allowed regions for the extension app. In order for a Docusign user to install your extension app in the production App Center, their account must be based in one of the selected regions. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for details. You cannot remove regions after an extension app has been published.
3. Select **Save**.

## Update changelog

When you update the registration for a [published](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) extension app, you must populate the **Changelog** field with a list of changes in the new [version](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/). This information will appear with the extension app listing in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/). The **Changelog** field does not appear on the App Center Listing page for extension apps that have not been published.

To update the changelog:

1. [Access the App Center Listing page](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#access-app-center-listing-for-an-extension-app).
2. In the **Changelog** field, list the extension app changes in the new version.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='915' width='1039' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Distribution details with changelog](https://images.ctfassets.net/aj9z008chlq0/7mASdsjJRB45S8Zm9Zz4wn/0d9096032b8af1277ea61199fa38f785/DistributionDetailsWithChangelog.png?w=1039&h=915&q=50&fm=png)
3. Select **Save**.

## Next steps

- Review the procedure to [update the integration details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/) for an extension app.
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
