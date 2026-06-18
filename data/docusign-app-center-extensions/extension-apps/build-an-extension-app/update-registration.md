---
title: Update an extension app registration
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Update Registration
scraped_at: '2026-06-18T19:51:50Z'
---

# Update an extension app registration

You have two options for updating an extension app's registration:

- [Use a form](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-form/): This guided process enables you to update registration details by filling out fields on pages in the Developer Console.
- [Use an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/): In this process, you update registration details by populating values in a JSON file that you upload or paste in the Developer Console app manifest editor.

The Developer Console stores extension app settings in a JSON app manifest file, regardless of whether the app registration was created via the form-based process or by building the manifest file directly. Any extension app's registration details can be updated either through the form-based process or by updating the manifest file.

See [Form-based and app manifest method comparison](https://developers.docusign.com/extension-apps/build-an-extension-app/register/#form-based-and-app-manifest-method-comparison) for guidance about which method might be more useful.

## Extension app statuses that affect updates

You cannot update an extension app's registration details if its status is:

- **In Review.** To update an extension app registration that’s in review, you must first cancel the publishing process to restore it to a Draft state. After the update, you’ll need to resubmit the app if you want to proceed with the review.
- **Approved.** To update an extension app registration that’s been approved for publication to the App Center but not published yet, you’ll need to cancel the publishing process to restore it to a Draft state, and then resubmit the app for review if you still want to publish it to the App Center.
- **Rejected.** To update an extension app registration that’s been rejected during the review, you’ll need to cancel the publishing process to restore it to a Draft state, make changes based on review comments, and then resubmit the app for review if you still want to publish it to the App Center.
- **Live.** To update the registration for a live extension app on the App Center, you must submit a new patch version for review. See [App Versioning](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) for details on what qualifies as a patch version update. Major and minor version updates will be supported in a future release.

## Next steps

Learn how to:

- [Delete an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/delete/)
- [Test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/)
- [Publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/)

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
