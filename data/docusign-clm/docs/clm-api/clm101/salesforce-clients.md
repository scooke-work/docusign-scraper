---
title: Salesforce Client Authentication
source_url: https://developers.docusign.com/docs/clm-api/clm101/salesforce-clients/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- API 101
- API 101
- Salesforce Clients
scraped_at: '2026-06-18T21:48:55Z'
---

# Salesforce Client Authentication

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

Salesforce clients must authenticate by using Web Token (JWT) Grant. However, before you authenticate, you first need to configure your application’s connection to Docusign CLM.

## Prerequisites

Before you can authenticate your Salesforce client, you must:

- Have a [Salesforce developer account](https://developer.salesforce.com/signup).
- Have a [Docusign developer account](https://go.docusign.com/o/sandbox).
- Have created and configured an app in your Docusign Developer Account by following the steps in [Building a Docusign integration](https://developers.docusign.com/platform/build-integration/).
- Have a Docusign CLM account.
- Have installed a package that creates custom metadata and written [Apex](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_intro_what_is_apex.htm) code that uses this package. To get started quickly, you can download [this example package](https://github.com/docusign/code-examples-clm-apex). For more information about Apex, see the [Apex Toolkit Overview](https://developers.docusign.com/docs/salesforce/salesforce101/apex-toolkit/).
- Configure your Salesforce client to connect to Docusign.

## Required data

To authenticate your Salesforce client, you will need this information:

|  |  |
| --- | --- |
| **Data element** | **Description** |
| API Account ID | A globally unique identifier [(GUID)](http://guid.one/) value that identifies your account. To find your API Account ID, log in to your Docusign eSignature account and select **Admin**, then select [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=apiIntegratorKey) from the sidebar. Copy the **API Account ID** value. |
| User ID | To find your User ID, log in to your Docusign eSignature account and select **Admin**, then select [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=apiIntegratorKey) from the sidebar. Copy the **User ID** value. |
| Integration Key | An [integration key](https://developers.docusign.com/platform/configure-app/) that identifies your app. To find your integration key, log in to your Docusign eSignature account and select **Admin**, then select [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=apiIntegratorKey) from the sidebar. Under **My Apps / Integration Keys**, copy the integration key for your Salesforce client. |
| Private Key | The private key that you created and saved when you created and configured your app in your Docusign Developer Account by following the steps in [Building a Docusign integration](https://developers.docusign.com/platform/build-integration/). |

## Configure your Salesforce client to connect to Docusign

To configure your Salesforce client to connect with Docusign, you need to perform the following steps in the Salesforce web application.

### Set up custom metadata in Salesforce

#### Deploy the custom metadata and Apex package to Salesforce

1. If you have not already downloaded the [custom metadata and Apex package](https://github.com/docusign/code-examples-clm-apex), download it now.
2. Deploy the files in the package to Salesforce.org. You can use [Workbench](https://workbench.developerforce.com/login.php) for the installation.
   1. Zip all of the files so that the folders and the .XML file in the **src** folder are at the root of the zip file.
   2. Log in to Workbench and select **Migration > Deploy**.
   3. Select the ZIP file that you downloaded. Check the **Single Package** checkbox and select **Next**.
   4. Select **Deploy**.

#### Add your Docusign information to Salesforce

After you have successfully deployed the source files to your Salesforce organization, you need to add your Docusign information, such as your Docusign API User ID and API Account ID, to Salesforce as custom metadata. These values are used to generate the access token and connect to Docusign.

Log in to the Salesforce web application use these steps to add your Docusign information:

1. Select **Setup > Custom Metadata Types**.
2. Under **DocusignRESTSettings**, select **Manage Records**.
3. Enter the values for your Docusign instance in the following settings:
   - **DSAccount**: Enter the Docusign API Account ID.
   - **DSUserName:** Enter the Docusign User ID.
   - **RequestIntegratorKey**: Enter the Integration Key.
   - **RequestPrivateKey**: Enter the Private Key you created when you created and configured your app in your Docusign Developer Account.

### Set up Remote Site URLs in Salesforce

Next, in the **Remote Site Settings** area of the Salesforce web application, add the following Docusign URLs as **Remote Site URLs**:

1. `https://account-d.docusign.com` for demo accounts.
2. `https://account.docusign.com` for production accounts.
3. The appropriate REST API URL for your environment. You can find this in CLM Admin in the **Integrations** section of the **System Domains** page.

## Obtain consent to impersonate the user for API calls

Next, you need to ask the Docusign user to grant consent for your app to perform actions on their behalf. For service integrations, you can set up a service user and grant consent on this user's behalf.

**Note**: You will need to request special CLM-required scopes.

To complete this step, open this URI in a browser:

```
https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation%20spring_read%20spring_write&client_id=YOUR_INTEGRATION_KEY&redirect_uri=https://localhost.com
```

Make sure that:

1. For the `client_id`, you substitute the correct Integration Key for `YOUR_INTEGRATION_KEY`.
2. The value for the `redirect_uri` parameter matches the redirect URI configured for the Integration Key in your Docusign Developer Account.

When you open the URL in your browser, a consent screen displays. Select **Accept**.

![Screenshot of the prompt for the user to grant consent](https://developers.docusign.com/img/clm-api/consent.jpg?v=2023061320)

After you select **Accept**, you will be redirected to the redirect URI you specified.

## Next steps

To get started with using CLM objects, see [Object API](https://developers.docusign.com/docs/clm-api/clm101/object-api/).

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
