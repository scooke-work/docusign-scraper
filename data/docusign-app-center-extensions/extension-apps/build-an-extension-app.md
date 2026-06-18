---
title: Build an extension app
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
scraped_at: '2026-06-18T19:51:48Z'
---

# Build an extension app

This topic covers the general steps to build an extension app. Links to details for each step are provided in the sections below.

The steps are:

1. [Create a developer account](https://developers.docusign.com/extension-apps/build-an-extension-app/#step-1-create-a-developer-account)
2. [Determine which extensions to use](https://developers.docusign.com/extension-apps/build-an-extension-app/#step-2-determine-which-extensions-to-use)
3. [Confirm API service details](https://developers.docusign.com/extension-apps/build-an-extension-app/#step-3-confirm-api-service-details)
4. [Set up your IT infrastructure](https://developers.docusign.com/extension-apps/build-an-extension-app/#step 4-set-up-your-it-infrastructure)
5. [Determine your extension app's availability](https://developers.docusign.com/extension-apps/build-an-extension-app/#step-5-determine-your-extension-apps-availability)
6. [Register your extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/#step-6-register-your-extension-app)
7. [Test your extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/#step-7-test-your-extension-app)
8. [Publish your extension app to the App Center](https://developers.docusign.com/extension-apps/build-an-extension-app/#step-8-publish-your-extension-app-to-the-app-center)
9. [Update extension app registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/#step-9-update-extension-app-registration-details)

## Step 1. Create a developer account

A free Docusign [developer account](https://www.docusign.com/developers/sandbox) gives you access to the tools you’ll need to register, test, and publish extension apps. All users under your account who have admin permissions can use the [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/).

## Step 2. Determine which extensions to use

Review the [supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) so that you can decide which ones to use in your extension app to meet your business needs. Docusign currently supports extensions that:

- Import files from and write files to a cloud storage system
- Export data to tabular format files in a cloud storage system
- Read data from and write data to a system of record
- Import files from and write files to a system of record
- Verify different types of data

Each extension can be triggered from defined points in Docusign agreement processes, known as [extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/#extension-points). Understanding which extension points are available enables you to plan for how your extension app will be used.

## Step 3. Confirm API service details

An extension app calls an API service to perform a function, such as verifying customer data or writing files to cloud storage. You’ll need to configure your extension app to connect to the API endpoints that provide this functionality. From there, the API can provide all the business logic and/or integrate with other systems. You’ll also need to configure the extension app to obtain [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) from the API service or an identity provider.

You'll need this information to configure your extension app:

- URLs for the API endpoints that your extension app will call. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information.
- Parameters that the API requires in requests to its endpoints, as well as the parameters that it returns in the responses. See [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) for information.
- [Authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) details for the API service if your extension app will obtain authorization directly from that service, or for the identity provider if your extension app will use an identity provider for authorization. These details include an authorization URL, token URL, client ID, client secret, and scopes. See [Connection schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) for information.

## Step 4. Set up your IT infrastructure

For an extension app to obtain authorization and send requests to an API service, the following IT infrastructure must be in place:

- [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/): You must build an API proxy if requests to and responses from the API service do not conform to the Docusign action contract schema. You can access the action contracts for each extension from the [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) page.
- [Authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/): Configuration changes may be needed for the API service or identity provider to make sure that Docusign can obtain permission to access API resources.
- [Network](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/network-configuration/): Firewall and ad blocker configuration changes may be needed to make sure that Docusign can send requests to the API service, and to make sure that your users can install your extension app in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

See [Set up your IT infrastructure](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/) for details.

## Step 5. Determine your extension app's availability

Two features of extension apps enable you to control who can access your extension app after you publish it.

If you are a Docusign partner, you can create a *public extension app*, which will be available on production to users under all Docusign accounts. Alternatively, if you are not a partner, you can create a *private extension app*, which will be available on production only to users under accounts that you specify. See [Choosing private distribution instead of public](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/) for details, or [Join now](https://partners.docusign.com/s/join-now) for details on how to join the Docusign partner program.

In addition, you can choose the regions in which your extension app will be available for production use. Users outside your selected regions won’t be able to install your extension app in the production App Center. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for details.

After you have published an extension app to make it live, you cannot change its distribution type (public or private) or remove regions where it is currently available.

## Step 6. Register your extension app

Registering your extension app supplies Docusign with the details required to obtain [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) from your external API service or identity provider and send requests to the API endpoints. Also during the registration process, you provide metadata that is displayed in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) listing for your extension app.

You have two options for registering your extension apps using the Developer Console. You can use a guided web-based interface that walks you through the process of supplying the required details. Or you can manually populate the details in a JSON extension app manifest file. See [Register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/) for details about the two options.

## Step 7. Test your extension app

You can [test your extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) in the Developer Console by launching built-in test functions. They enable you to confirm that:

- Your extension app can use your account credentials to obtain authorization from the API service or identity provider.
- Your extension app can send a request to each API or proxy endpoint and process the response.
- You can install the extension app to your Docusign account.

You can also run a test to confirm that the extension app works correctly when invoked from an envelope or workflow. See [Functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) for details.

## Step 8. Publish your extension app to the App Center

Once you have successfully tested your extension app, you can use the Developer Console to [submit it for review](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/). The review process evaluates business, technical, security, and functional aspects of your extension app. See [App Center publishing guidelines](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/guidelines/) for more information about the evaluation. Your extension app must pass review before you can publish it to the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/). Only published extension apps can be used in production.

You’ll be notified of any issues that Docusign finds during the review, receive guidance on how to correct them, and be able to resubmit the extension app for review after making the updates.

After a successful review, your extension app will appear in **Approved** status in the Developer Console. You can then publish it to the App Center, which makes it available for Docusign users to install and use in production envelopes and workflows.

## Step 9. Update extension app registration details

You may need to [update extension app registration details](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) to address changes in the API service that the app calls, to meet authorization requirements, to accommodate different use cases in the Docusign agreement process, or to update the extension app's display information in the App Center. You can update the registration details via a form-based UI or by editing the extension app manifest.

Updating a published extension app's registration details creates a new version, which must pass a Docusign review before it can be published to the App Center. See [Extension app versioning](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) to learn more about managing versions of your extension app.

## Next steps

- Get an overview of your options to [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/).
- Learn about the process to [test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).
- Find out how to [publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/).
- View a [dashboard](https://developers.docusign.com/extension-apps/build-an-extension-app/monitor-usage/) that displays extension app usage data.

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
