---
title: C# SDK setup and configuration
source_url: https://developers.docusign.com/docs/esign-rest-api/sdks/csharp/setup-and-configuration/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- SDKs
- SDKs
- Csharp
- Csharp
- Setup and configuration
scraped_at: '2026-06-18T21:09:54Z'
---

# C# SDK setup and configuration

## Adding the SDK to your project

The C# eSignature SDK is provided as a NuGet package named [DocuSign.eSign.dll](https://www.nuget.org/packages/DocuSign.eSign.dll/). By default, you will always get the latest stable version of the SDK. Prerelease versions (either release candidate (rc) or beta) can also be downloaded as shown below.

There are two ways to add the package to your project: via the Visual Studio UI or the command line.

### Adding the C# SDK to your project using the Visual Studio UI

1. Open Visual Studio and load the solution you wish to use.
2. Open the **Solution Explorer** window and right-click the desired project in the solution.
3. Select **Manage NuGet Packages…** (shown below).

   ![](https://developers.docusign.com/img/CSharpSDK_fig1.png?v=20260610.1)

4. In the **NuGet Package Manager** window, select the **Browse** tab on the left.

   ![](https://developers.docusign.com/img/CSharpSDK_fig2.png?v=20260610.1)

5. In the **Search** textbox, enter "Docusign" to find all Docusign-related packages.
   **DocuSign.eSign.dll** "by Docusign" (publisher) should be displayed first in the search results. Select it.

   ![](https://developers.docusign.com/img/CSharpSDK_fig3.png?v=20260610.1)

6. Select **Install** to install the latest version of the package.

   **Note:** You can install earlier versions by expanding the drop-down menu to the right of **Version**. You can also install release candidate (rc) and beta versions by selecting the **Include prerelease** checkbox to the right of the **Search** textbox.
7. Acknowledge the license agreement by selecting **I Accept** on the **License Acceptance** screen.

You have now successfully downloaded, configured, and installed the Docusign eSignature SDK for your project. To confirm the package is available in your project, you can go back to the **Solution Explorer** window and expand the **Dependencies > Packages** section of the project. You should see **DocuSign.eSign.dll** (version number) listed.

![](https://developers.docusign.com/img/CSharpSDK_fig6.png?v=20260610.1)

**Note:** If you expand the DocuSign.eSign.dll package, you will see the additional dependencies that are automatically installed by the NuGet package manager.

### Adding the C# SDK to your project using the command line

1. Open the NuGet Package Manager command line from the Visual Studio menu bar by selecting **Tools > NuGet Package Manager > Package Manager Console**.
2. From the **Package Manager Console**, run the following command:

   ```
       Install-Package DocuSign.eSign.dll
   ```

   ![](https://developers.docusign.com/img/CSharpSDK_fig4.png?v=20260610.1)

The command above will automatically install the latest stable version. If desired, you can specify a specific version by using the `-Version` switch. For example, this command installs version 5.2.0 of the Docusign C# eSignature package:

```
    Install-Package DocuSign.eSign.dll -Version 5.2.0
```

## Including the SDK library

After you have installed the DocuSign.eSign.dll package, you will need to find the public classes that are required to complete various eSignature tasks. To do that, add the main namespaces as `using` statements in your C# code.

Here are the three main `using` statements for the commonly required namespaces:

```
using DocuSign.eSign.Api;
using DocuSign.eSign.Model;
using DocuSign.eSign.Client;
```

### [DocuSign.eSign.Api namespace](https://github.com/docusign/docusign-esign-csharp-client/tree/master/sdk/src/DocuSign.eSign/Api)

This namespace is used for endpoint categories. Each class under this namespace corresponds to one of the categories listed in the left menu of the [Docusign eSignature REST API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/). You will need to use this namespace to make calls to the public methods that initiate REST API calls to the Docusign eSignature REST API.

**Note:** Hereafter in the SDK documentation, the term “API object” will refer to [eSignature REST API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/) objects.

An [API category](https://developers.docusign.com/docs/esign-rest-api/reference/) contains all methods for each API resource in that category. For example, the C# SDK [EnvelopesApi](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Api/EnvelopesApi.cs) class includes the `CreateEnvelope` method. This method corresponds to the [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) method of the API [Envelopes](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/) resource.

The C# SDK method names roughly correspond to the API Resource:method names.

The API Resource:method page for each endpoint lists the API SDK Method in the **SDK Method** box. The C# method name will be the PascalCase version of the API SDK Method name. For example, the API SDK Method `Envelopes::createEnvelope`, listed toward the bottom of the [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) page, is the C# method `CreateEnvelope`.

Some API endpoints also use HTTP query parameters. Within the API, such query parameters use snake\_case. For example, the [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) API method includes an optional query parameter, `change_routing_order`. Within the SDK, the API’s query parameters are added as an elective `options` parameter after the request object.

**Example:** The `CreateEnvelope` method signature is:

```
    public EnvelopeSummary CreateEnvelope (string accountId, EnvelopeDefinition envelopeDefinition = null, EnvelopesApi.CreateEnvelopeOptions options = null);
```

The `CreateEnvelopeOptions` class is used to set the API method’s query parameters. The class is defined as:

```
    public class CreateEnvelopeOptions
    {
        public string cdseMode {get; set;}
        public string changeRoutingOrder {get; set;}
        public string completedDocumentsOnly {get; set;}
        public string mergeRolesOnDraft {get; set;}
        public string tabLabelExactMatches {get; set;}
    }
```

The class attributes in camelCase correspond to the API endpoint’s query parameters.

### [DocuSign.eSign.Model namespace](https://github.com/docusign/docusign-esign-csharp-client/tree/master/sdk/src/DocuSign.eSign/Model)

This namespace includes the data structures used for sending and receiving data from the eSignature API endpoints. By using these classes instead of generic JSON objects, C# developers can develop with the Docusign eSignature API more easily and quickly than by using JSON directly.

There’s a one-to-one correspondence between the objects described in the [API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/) and the classes in the DocuSign.eSign.Model namespace. The API object names use flatcase (all lowercase without spaces) while the corresponding SDK models use PascalCase. For example, the API object [paymentgatewayaccount](https://developers.docusign.com/docs/esign-rest-api/reference/payments/paymentgatewayaccounts/list/#response200_paymentgatewayaccount) corresponds to the C# model [PaymentGatewayAccount](https://github.com/docusign/docusign-esign-csharp-client/blob/master/sdk/src/DocuSign.eSign/Model/PaymentGatewayAccount.cs).

**Note:** The API object name is often not the same as the corresponding model in the C# SDK.

Object attribute names in the API use camelCase. The corresponding properties of the C# SDK are in PascalCase.

### [DocuSign.eSign.Client namespace](https://github.com/docusign/docusign-esign-csharp-client/tree/master/sdk/src/DocuSign.eSign/Client)

This namespace contains the classes needed to manage the overall API experience. These classes handle instantiating a client element to make API calls, authentication, and exception handling. You will need to include this namespace to be able to use the Docusign eSignature API correctly.

### Using the SDK

To make eSignature REST API calls with the SDK, you need:

- A current `accessToken`.
- The `basePath` for the API call.
- For most API calls, you’ll also need the relevant `accountId`. Note that it is common for a user to be a member of multiple accounts.

### Modifying the default HTTP Request timeout

By default, ASP.NET applications have a 90-second timeout for HTTP requests. In rare cases API calls may take longer, and you may need to increase the timeout to accommodate these calls. Follow instructions provided by Microsoft at [Request timed out error when you use the DataAdapter method in an ASP.NET application](https://docs.microsoft.com/en-us/troubleshoot/developer/webapps/aspnet/site-behavior-performance/request-timed-out-dataadapter) to increase the timeout period for HTTP requests made from your application when using the Docusign C# SDK.

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
