---
title: Use a manifest file to update a registration
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Update Registration
- Update Registration
- Use Manifest
scraped_at: '2026-06-18T19:51:51Z'
---

# Use a manifest file to update a registration

This guide describes the steps for updating an extension app registration by editing a JSON app manifest file. You also have the option of updating an extension app registration [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-form/). See [Form-based and app manifest method comparison](https://developers.docusign.com/extension-apps/build-an-extension-app/register/#form-based-and-app-manifest-method-comparison) for guidance about which method might be more useful.

See [Extension app statuses that affect updates](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/#extension-app-statuses-that-affect-updates) for details about steps you may need to take before you can update an extension app registration.

When you update your extension app registration by editing the manifest file, you will need to re-enter your client secret to save your changes.

## Step 1. Edit your app registration in the Developer Console

Open **My Extension Apps** in the [Developer Console](https://devconsole.docusign.com). Select the kebab menu of the extension app, then select **Edit Manifest.**

![](data:image/svg+xml;charset=utf-8,%3Csvg height='840.0000000000001' width='1931' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the edit manifest option in the Developer Console](https://images.ctfassets.net/aj9z008chlq0/2vinnOx2XDW8IEJcwJf16X/46d232ee6990b737b0477f72889c7d5b/editmanifest.jpg?w=1931&h=840&fl=progressive&q=50&fm=jpg)

## Step 2. Update the extension app manifest

You can edit your manifest directly in the manifest editor or download or copy the manifest to edit it in the IDE of your choice. If you saved your updated manifest as a JSON file, copy and paste your JSON into the manifest editor.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1334' width='2020' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Screenshot of the manifest editor for Edit Manifest](https://images.ctfassets.net/aj9z008chlq0/7Hyds08sD3pcEryfZJk8QU/70b35f7f57e6ae0a6f7af1b929c12773/AppManifestEditor.png?w=2020&h=1334&q=50&fm=png)

To protect sensitive data, the value of `clientSecret` is not displayed in the app manifest editor. You must re-enter this value before you can save updates to an app manifest. The manifest editor also does not display the existing Base64 values of any `data` properties for the icon or screenshots. These values do not need to be reentered unless you want to change them.

## Step 3. Validate your app manifest

When your app manifest is ready, select **Validate** to determine whether your manifest has any errors. See [Troubleshooting manifest errors](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/troubleshooting-manifest-errors/) for a list of possible errors with details on how to troubleshoot them. Once your manifest has passed all validation checks, choose **Save Changes** to finish updating your app registration.

## Next steps

- Learn how to update an extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-form/).
- Get details about [extension app statuses](https://developers.docusign.com/extension-apps/build-an-extension-app/status/).
- Review the process to [publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/).

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
