---
title: Delete an extension app
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/delete/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Delete
scraped_at: '2026-06-18T19:51:48Z'
---

# Delete an extension app

An extension app version can only be deleted when it’s in **Draft** status. You cannot delete a version that's going through Docusign review for publication to the App Center—indicated by a status of **In Review**, **Approved**, or **Rejected**. To delete an extension app version in one of these statuses, you must first cancel your request to publish it from the **Publish to App Center** page in the Developer Console. See [Publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) for details.

**Note:** You cannot delete an extension app if its status is **Live**, which means that it’s been published for use by any Docusign App Center user. For assistance with deleting a live extension app, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance.

## Deleting drafts of unpublished and published extension apps

The procedure for deleting a draft varies depending on whether or not the app has ever been published. For an app that has never been published:

1. Open **My Apps** in the [Developer Console](https://devconsole.docusign.com).
2. Select the kebab menu for the extension app, and then select **Delete**.
3. In the confirmation dialog box, choose **Delete**.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1032' width='1920' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Delete a draft extension app](https://images.ctfassets.net/aj9z008chlq0/2IkzHwTVaebLbc3HDtsEa6/b3d4a1fd580ad8da6701d945d258a110/DeleteDraftApp.png?w=1920&h=1032&q=50&fm=png)

For an app that has been published, you cannot delete the Live version, and you can only delete the most recent draft. To delete the most recent draft version of a publish app:

1. Open **My Apps** in the [Developer Console](https://devconsole.docusign.com).
2. Select the relevant app from the list of apps.
3. Select **App Versions** from the left nav menu.
4. If you have a Draft version of the app, you can select **Delete Draft.**
5. In the confirmation dialog box, choose **Delete**.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1032' width='1920' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Deleting a draft version of an extension app](https://images.ctfassets.net/aj9z008chlq0/14fxvjnaYNY5a1EWTzp9eI/ec70163a7dd7ea0ae2a2a2e0a98f1a6c/ExtensionAppVersioningPageDelete.png?w=1920&h=1032&q=50&fm=png)

## Next steps

- [Extension apps 101 overview](https://developers.docusign.com/extension-apps/extension-apps-101/)
- [Developer Console overview](https://developers.docusign.com/extension-apps/developer-console-overview/)
- [Extension app best practices](https://developers.docusign.com/extension-apps/best-practices/)
- [Troubleshooting](https://developers.docusign.com/extension-apps/troubleshooting/)

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
