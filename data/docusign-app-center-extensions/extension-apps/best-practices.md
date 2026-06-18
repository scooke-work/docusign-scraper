---
title: Extension app best practices
source_url: https://developers.docusign.com/extension-apps/best-practices/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Best Practices
scraped_at: '2026-06-18T19:51:49Z'
---

# Extension app best practices

To help ensure your customer has a great experience using your extension app, we recommend you review our list of best practices for building and maintaining your extension apps.

## Naming your app

Your app name should be as descriptive as possible and make it easy for customers to understand what your app does and why they may want to use it. Please don’t use jargon or unfriendly acronyms in the name, and avoid using underscores and other characters that make the name harder to understand. Also, remember that the name is limited to 30 characters, so long names are not allowed.Keep in mind that the name you choose here (you can rename later if you need to) is going to be the name customers see when you publish your extension app to the Docusign App Center. The name should make it clear to customers what your app is about and why they may want to use it. You may want to have your marketing or business development department involved in deciding on the appropriate name for your app.

## Choose your app icon

Your app icon will be shown to users both before they install your extension app and when they choose to use it. It’s important that you pick a high-quality icon that clearly represents your app. If you plan to provide more than one extension app, you should have a different icon for each app.

Docusign recommends providing an icon image that meets these guidelines.

|  |  |  |
| --- | --- | --- |
| **Image feature** | **Recommendation** | **Notes** |
| File type | .PNG, .JPG, or .SVG | .GIF and transparent .PNG files may not render well and will be rejected for publishing to the App Center |
| Aspect ratio | 1:1 (square) |  |
| Dimensions | 100 x 100 pixels | The image will appear in various locations in the Docusign platform, including the [Developer Console](https://devconsole.docusign.com) and the [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/). Depending on the location, it may be resized to dimensions as small as 32 x 32 pixels. |

## Provide all your information

It’s important that you supply all the information pertaining to your new extension app. . Be sure to provide a valid email address for support as well as a valid website that includes relevant information about the app. You are required to provide terms of service and privacy policy links for your customers. If you don’t have these documents, you can use boilerplates from online services that provide legal documentation.Remember that all this information will be available to customers when they explore different apps on the marketplace, before they even install it.

## Provide screenshots of your extension app

Screenshots of your app help customers understand what it does and visualize how it will help them when using Docusign. Your screenshots should be realistic and show the main feature(s) of your extension apps. Don’t use “test” and “demo” and avoid showing clearly fake examples. Use high-resolution screenshots that are not cut off and clearly help explain what your app can do.

## Running your app locally

Developers typically want to run their app on their own computer before deploying it to a server where it will eventually reside. That means that the app does not yet have a publicly available URL and cannot be easily accessed from the internet. Since Docusign servers have to call your app via some public URL, Docusign recommends that you use a tool such as [ngrok](https://www.ngrok.com) to create a tunnel that exposes your developer personal computer on the internet and enables you, as a developer, to keep using localhost addresses while developing and testing your application.

## Testing your app

Before you can publish your app to the App Center, you must test it. It’s important to ensure a high quality for your extension app so that your customers have a smooth experience using it. Please refer to [Test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) for more information.

## Debugging your app

There are two ways to debug your app: using unit tests that call your app directly without Docusign being involved, or using integration testing from Docusign by having your Docusign extension app called by Docusign at the specific extension point you’re trying to debug. To do that, you need to run the scenario that will cause your extension app to be called. For example, if your app extends the connected fields extension, you will need to create a Docusign envelope, add custom fields configured to use your extension app, and send the envelope so that your app is triggered when the signer interacts with those fields.

## Actions in the Developer Console are account-wide

When using the Developer Console to install, uninstall, test, or upgrade any extension apps, any action you take will impact any other user using the same Docusign account. If you work in an organization that includes multiple people who are involved in building extension apps, you should be mindful that you may impact others in your organization.

## Next steps

- Learn more about [Extension app concepts](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/).
- Get an overview of [Extension app use cases](https://developers.docusign.com/extension-apps/extension-apps-101/use-cases/).
- Find out how to [Build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).

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
