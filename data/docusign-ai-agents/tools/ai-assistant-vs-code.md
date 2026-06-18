---
title: Docusign Developer AI Assistant for VS Code (Beta)
source_url: https://developers.docusign.com/tools/ai-assistant-vs-code/
site: developers.docusign.com
breadcrumb:
- Tools
- Tools
- Docusign Developer AI Assistant for VS Code
scraped_at: '2026-06-18T17:32:52Z'
---

# Docusign Developer AI Assistant for VS Code (Beta)

We’re currently running a beta for the Docusign Developer AI Assistant for VS Code, an AI-powered assistant to help developers generate tokens, orchestrate APIs, configure brands, and resolve integration issues faster. Install the extension from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=DocuSign.docusign-copilot).

The Docusign Developer AI Assistant for VS Code provides an AI-powered experience to help developers build integrations.

- Developers can ask questions to the extension. The extension includes a [question and answer](https://developers.docusign.com/tools/visual-studio-code-extension/#docusign-Q-and-A) functionality that responds to Docusign-specific questions.
- Developers can use the extension to [get an access token](https://developers.docusign.com/tools/visual-studio-code-extension/#get-an-access-token) that can be used for [authentication](https://developers.docusign.com/platform/auth/).
- Developers can use this extension to [create or update brand](https://developers.docusign.com/tools/ai-assistant-vs-code/#update-brand-files-using-vs-code-extension) files in a Docusign account.

## Prerequisites

Before you can use the Docusign Developer AI Assistant for VS Code, you will need:

- A [GitHub Copilot](https://github.com/features/copilot) license or free trial.
- A Docusign developer account. You can [create one](https://www.docusign.com/developers/sandbox) for free at the [Developer Center](https://developers.docusign.com/).
- [Visual Studio Code](https://code.visualstudio.com/download). Be sure to install the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) in VS Code.

## Docusign Q&A

To ask a question about Docusign, type `@docusign`, followed by your question, in the Copilot chat window. The Developer AI Assistant can answer questions about Docusign integrations, addressing topics such as authentication and how to use [Docusign SDKs](https://developers.docusign.com/docs/sdks/)

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1268' width='810' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot showing the Copilot chat box](https://images.ctfassets.net/aj9z008chlq0/4NgABFk6GMbc0DWS4Ivd5s/c41ae712cabd1e824b07611e48c01d1b/AskCopilot.png?w=810&h=1268&q=50&fm=png)

## Get an access token

The Docusign Developer AI Assistant for VS Code can also help developers get started with authentication, automating some of the manual configuration that is usually required when setting up an [Integration key](https://developers.docusign.com/platform/configure-app/#integration-key) (IK). The Developer AI Assistant streamlines the [process of generating an access token](https://developers.docusign.com/platform/auth/confidential-authcode-get-token/) and lets you generate a token with the simple `/getAccessToken` slash command.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='840' width='804' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the Docusign Copilot extension generating an access token](https://images.ctfassets.net/aj9z008chlq0/4ZYiGgk4SLgMZqAFCITU33/a9048c7ef1e7d1cd49b36dfc9b96f03b/CopilotStep1.png?w=804&h=840&q=50&fm=png)

To invoke Docusign Developer AI Assistant, use Ctrl+Alt+I on Windows and Cmd+Shift+I on Mac. After logging in, you will be asked to answer some questions to help determine the [authentication type](https://developers.docusign.com/platform/auth/choose/) that your integration will use. Then the Developer AI Assistant will help you to set up an [integration key](https://developers.docusign.com/platform/configure-app/#integration-key) (IK). Choose whether you want to generate an IK automatically, receive instructions on how to create an IK in the Docusign Admin UI, or use an existing IK.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1556' width='794' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the options displayed by Copilot when creating an integration key.](https://images.ctfassets.net/aj9z008chlq0/1bbCmg37NQ1yrvDYoPF8YL/176b547379ac097e77e8b99d5279f745/CopilotStep2.png?w=794&h=1556&q=50&fm=png)

If you choose to generate an IK through the Developer AI Assistant, you will be prompted to enter some information about the new IK. Once the IK has been created, you will see a confirmation like the one below in your chat window. In this example, an RSA key pair was generated for use with JWT authentication. If you choose Authorization Code Grant, the output will look slightly different.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='830' width='810' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the RSA key pair generated by Copilot](https://images.ctfassets.net/aj9z008chlq0/3BSq8k2g6c5pIsoAh4i7Px/ed709f5a7107541a0a1cc47fd6fac6ba/GeneratedRSAKey.png?w=810&h=830&q=50&fm=png)

The Developer AI Assistant will continue to guide you through granting consent and generating an access token that will appear in the **OUTPUT** tab.

You can continue to use the Developer AI Assistant to learn how to use this access token to make calls to Docusign APIs including the [eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/) and [more](https://developers.docusign.com/docs/).

![](data:image/svg+xml;charset=utf-8,%3Csvg height='906' width='1600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the Docusign Visual Studio Code extension after an access token has been generated](https://images.ctfassets.net/aj9z008chlq0/4unFwiJJJabwCnbKVced1J/53d6a5de135f331d944e3af172c450c7/VisualStudioCopilotExtension.png?w=1600&h=906&q=50&fm=png)

## Update brand files using VS code extension

Docusign administrators can manage their brand details either through the Docusign eSignature admin user interface or the Docusign Developer AI Assistant for VS Code extension. Using the VS Code extension, administrators can create, download, and update brand files directly within the Visual Studio Code. This allows administrators to configure brand settings in Visual Studio Code and easily upload the brand files to their Docusign account. For more details on brand functionalities, see [Brands](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=lfr1583277366660.html).

Brand file updates using the VS Code extension are now available in demo environments only. This feature is in beta and not currently available in production.

Updating brand files directly in Visual Studio Code provides following benefits:

- Streamlines brand files management.
- Enables real-time editing, previewing, and verification.
- Removes manual file handling and uploading steps in the Docusign eSignature administrator interface.

Administrators can access these features using the Docusign Developer AI Assistant for VS Code extension via the command palette (**Ctrl+Shift+P** on Windows/Linux or **Cmd+Shift+P** on macOS). With this extension, administrators can update brand XML files, including email templates, headers, footers, colors, fonts, logos, etc.

## Create a New Brand

To create a new brand in your Docusign account using VS Code:

1. Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and run **Create Docusign Brand.**

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='152' width='603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![create docusign brand command](https://images.ctfassets.net/aj9z008chlq0/7qeglWI5xfKqG2YR5hqFXE/75fde72e84a9dff05b1715219e1e7ef0/create-docusign-brand.png?w=603&h=152&q=50&fm=png)
2. If prompted, sign in to your Docusign developer account and select your account.
3. Enter a name for the new brand and press Enter.
4. Choose a location to save the brand files.

   A success message will appear, and the brand files will open in a new VS Code window. You can also verify the new brand in your eSignature [Admin Brand settings](https://apps-d.docusign.com/admin/brands).

## Download a Brand

To download files for an existing brand in your Docusign account using VS Code:

1. Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and run **Download Docusign Brand**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='161' width='598' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![download-docusign-brand](https://images.ctfassets.net/aj9z008chlq0/kagMqjLuqKosEudFb793s/b17d274bb976be15f199460290186482/download-docusign-brand.png?w=598&h=161&q=50&fm=png)
2. If prompted, sign in to your Docusign developer account and select your account.
3. Select a brand from the list.
4. Choose a folder to save the brand files.

   The brand files will be downloaded and opened in a new VS Code window, including:

- **logo/** - contains brand logos
- **resources/ -** contains email templates and other assets. For more information, refer [Docusign Signing Resource File Guide](https://support.docusign.com/s/document-item?language=en_US&bundleId=docusign-signing-resource-file-guide&topicId=docusign-signing-resource-file-guide.pdf&_LANG=enus).
- **brand.json** - contains brand profile information

## Editing Brand Files

After you have downloaded the brand files into your preferred directory, the following file and folder structure will appear in your **VS Code** window:

| Path | Description |
| --- | --- |
| `/logo` | Contains the brand's logo image files. |
| `/resources` | Contains email templates and other assets used for brand customization. |
| `/resources/email/mockdata/values.yaml` | Lists the placeholder values used across all email templates. Modifying this file allows you to make global changes to your templates simultaneously during the development process.   **Note**: The values defined in this file are used **for local testing and development**. They are not uploaded when updating brand files to the server. To make the changes in the server, use [Admin Brand settings](https://apps-d.docusign.com/admin/brands) page. |
| `/resources/email/templates/` | Contains the actual email templates available for editing and previewing. |
| `brand.json` | Contains brand’s core metadata, including the brand ID, name, and supported languages. |

 **Real-Time Previewing**You can view your changes instantly without leaving your workspace. As you edit the files in `/resources/email/templates/`, you can open a **live preview** window directly within VS Code. This allows you to visualize layout adjustments, CSS tweaks, and content changes in real time, ensuring your design is perfect before updating the brand files.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='680' width='1500' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![brand files preview in vs code]()

**Dynamic Data & Conditional Logic**The values.yaml file contains the following values:

- **Placeholder Values:** Use keys from `values.yaml` to inject dynamic content (like brand names or links) throughout your templates. This ensures consistency and makes global updates at once.
- **Conditional Logic:** Uses conditional flags in values.yaml to toggle specific sections of an email based on your brand requirements. For example, the `IsEnvelopeContainingSingleDocument` flag controls grammatical plurality: setting it to **true** displays text in the singular form, while **commenting it out** defaults the text to the plural form.

**Note:** To disable a condition, you must **comment out** the line in the values.yaml file. Do **not** simply set the value to False, as the system will not recognize this as a disabled state.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='479' width='1492' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![vs code condition](https://images.ctfassets.net/aj9z008chlq0/2hYCmupR6HkTz9xw94qu9x/c1b3859dd46b0bc900bc606759f608b1/vscodecondition.png?w=1492&h=479&q=50&fm=png)

## Updating a Brand

**Prerequisite:** Make sure your VS Code workspace contains the latest downloaded brand files from your Docusign account.

After editing the brand files, you can either:

- Update the brand files in your Docusign account, or
- Clone the brand files to create a new copy in your account

**Update the brand files folder**To update brand files in your Docusign account:

1. Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and run **Update Docusign Brand**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='150.00000000000003' width='603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![update-docusign-brand](https://images.ctfassets.net/aj9z008chlq0/1MicXiAWh1E5Aca6RSul4f/b9176259f47fe50ec6a1f7b194bbce11/update-docusign-brand.png?w=603&h=150&q=50&fm=png)
2. Select Update <brandname> Files.

   The extension will:
   - Combine local brand.json, resources, and logos
   - Push changes to your Docusign account
   - Update email templates (only **en-US** is supported) and other resources
   - Upload XML files and brand logos

If successful, a confirmation message appears. You can also verify the new brand in your eSignature [Admin Brand settings](https://apps-d.docusign.com/admin/brands). For validation errors, rectify the error and repeat the commands.

**Clone the brand files folder**To save modified brand files as a new brand:

1. Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P) and run **Update Docusign Brand**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='150.00000000000003' width='603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![update-docusign-brand](https://images.ctfassets.net/aj9z008chlq0/1MicXiAWh1E5Aca6RSul4f/b9176259f47fe50ec6a1f7b194bbce11/update-docusign-brand.png?w=603&h=150&q=50&fm=png)
2. Select Clone and Update <brandname> Files.

   The extension will:
   - Combine local brand.json, resources, and logos
   - Push changes to your Docusign account
   - Update email templates (only en-US is supported) and other resources
   - Upload XML files and brand logos
   - Create a new brand with the name suffixed by \_cloned and download the files to your machine
   A success message will appear, and the cloned brand files will open in a new VS Code window for editing.

## Try it out

Check out the Docusign Developer AI Assistant for VS Code for yourself and try the following use cases:

- Let the Developer AI Assistant generate an access token to help you get started with your first API integration.
- Ask the Developer AI Assistant which authentication type is right for your use case.
- Ask the Developer AI Assistant about Docusign features, APIs, and best practices. It’s your personal guide for quick, accurate answers while you work.
- Save time by letting the Developer AI Assistant create the necessary boilerplate code for integrating Docusign APIs in your preferred programming language.

## Next steps

- Learn more about [Docusign SDKs](https://developers.docusign.com/docs/sdks/).
- Check out our [Postman collections](https://developers.docusign.com/tools/postman/).
- Explore all of the [tools](https://developers.docusign.com/tools/overview/) available to help developers build integrations.

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
