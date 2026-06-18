---
title: App Center publishing guidelines
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/publish/guidelines/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Publish
- Publish
- Guidelines
scraped_at: '2026-06-18T19:51:51Z'
---

# App Center publishing guidelines

N**ote**: These guidelines will be refined over time to provide more accurate information, and Docusign reserves the right to change them at any time.

Publishing extension apps to the [App Center](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) requires approval from Docusign. Follow these guidelines to have a smoother approval process.

## Technical and functional considerations

### Error-free functionality

Conduct thorough testing of your extension app and address any errors to ensure that your app functions correctly. Focus on edge cases and abnormalities to ensure your app can handle all circumstances. If there are things that are not yet supported, please let us know as part of your submission process for the App Center.

### Security

- Please use secure HTTPS (TLS 1.2 or higher) protocol for all API calls made by your app.
- Avoid including secrets such as passwords in your [extension app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/) or when entering in the form for your extension app, beyond what is absolutely necessary to get your app working. Please consult our [app manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for details about where it’s acceptable to have secrets. You can provide secrets in the envelope you send Docusign to test your app; our envelopes are a secure method to send secret information.
- Consider using security scanning tools to scan your code for any vulnerabilities.

### Performance

Your app users expect a quick response from your app without extended wait times. Docusign encourages you to reduce the response time of your app to enhance user experience.

### Scalability

Your app should be able to handle an increasing number of requests simultaneously without impacting its performance. Docusign recommends that you do load testing to ensure that your app can handle the potential of being used by millions of users.

### Reliability

Your app users rely on your app to function consistently. Ensure that your app maintains availability under varying conditions. Perform thorough testing to identify and address potential points of failure to enhance overall reliability, ensuring uninterrupted service for users.

## Business considerations

The following business requirements are critical for public extension apps. For private extension apps, we recommend following the same guidelines so that your customers’ account administrators can better understand the purpose and value of your app.

### Extension app description

The app’s description should be appropriate and provide an easy-to-understand description of what your extension app does. Do not use technical jargon. Remember that this description should be meaningful for both technical and non-technical Docusign customers who want to use your app. Your app description should also not be confusing or misleading or make false statements about what your app can or cannot do. Your description should be in English and free of typographical errors. (**Note:** Support for localization of your app’s information is not yet available.)

### Company information

Your extension app should use appropriate branding and naming that represent your organization and do not mislead customers about who provided the app. This information should include the company’s email address, website, and phone number. Please note that end customers of your app will use this information to contact you for support. Therefore, make sure this information is accurate.

### Screenshots

You can provide up to four screenshots to show your app’s features and use cases. It is essential to capture high-quality screenshots during your app testing phase, ensuring they accurately reflect your app's current appearance and features. If you modify your app's code, remember to update the screenshots if needed. It is critical to ensure that the information in your screenshots does not include any proprietary, private, or copyrighted material, and is appropriate for public viewing.

### Extension app icon

Ensure that your app icon provides a good representation of your app and does not violate any copyright laws. Do not use other company’s branding information in your extension app icon.

### Use of brand assets

Please check the [Docusign Brand website](https://brand.docusign.com/) for any use of Docusign brand assets such as the Docusign logo.

## Updating a live app

If you’re publishing a [new version](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) of a Live app, the new version has to be approved separately by Docusign. This list of publishing guidelines also applies to subsequent versions of the app. For versions other than the initial 1.0 version, you also must provide a **changelog** (either via the form or using the app’s manifest). This changelog has to explain clearly to customers what changes were made in the app since the last published version.

## Legal considerations

All developers publishing apps on the Docusign App Center must abide by applicable laws and the [Terms and conditions](https://www.docusign.com/legal/terms-and-conditions/app-center-terms). In addition, you must publish your app’s legal terms and privacy policy on your Docusign App Center landing page.

## Next Steps

- [Review the Extension apps 101 overview page](https://developers.docusign.com/extension-apps/)
- [Learn about the Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/)
- [Read about Extension app best practices](https://developers.docusign.com/extension-apps/best-practices/)
- [Check out our Troubleshooting page](https://developers.docusign.com/extension-apps/troubleshooting/)

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
