---
title: Extension app glossary
source_url: https://developers.docusign.com/extension-apps/glossary/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Glossary
scraped_at: '2026-06-18T19:51:49Z'
---

# Extension app glossary

This page defines common terms used in reference to extension apps.

### **Action**

Actions are the individual functions that do the work in your extension app. They specify the external platform endpoints to call from your Docusign envelopes and workflows. An action’s definition must include:

- A specific external platform endpoint to call when the action is triggered
- The required parameters to make the call

If registering an extension app via a manifest file:

- A reference to the external platform connection to use for the action
- A template identifier that specifies the action contract. This determines the request and response contract to be used as well as the extension points that will trigger the action. Template identifiers are predefined by Docusign.

Actions are executed at a defined point (an extension point) in a Docusign envelope or workflow when specified by an extension app.

### **API proxy**

An intermediary server that translates between external APIs and Docusign. An API proxy is needed only if requests to and responses from the external service endpoints do not conform to the Docusign action or capability contract schema. The proxy provides a mapping that transforms extension app requests to the external API's required format, and transforms the API’s responses to the format that Docusign expects.

### **App approval**

Before an extension app can be published in the Docusign App Center, it must pass a Docusign review. The review process verifies that the app complies with Docusign policies for security and API usage. Once an extension app passes Docusign review, it is approved and the developer can publish it to the App Center.

### **App Center**

A tool, accessible through the Docusign user experience, that enables Docusign users to browse, find, and install Docusign extension apps. It is the place to which developers publish their extension apps for public consumption or for use by selected customers. See [Choosing private distribution instead of public](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/) for more information.

### **App manifest editor**

A tool in the Developer Console with which developers can register and edit their extension app manifest, a JSON file that specifies the elements of an extension app. The app manifest editor provides features to edit your app manifest, download or copy it as a file, format the contents, and validate the JSON.

### **Capability**

Capabilities provide optional features that can be added to an extension's base functionality. While [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) are required, capabilities are optional. Capabilities can be implemented alongside the required actions to incorporate additional functionality into your extension app.

### **Connection**

An object, configured in the form-based extension app registration experience or specified in an extension app’s manifest file, that holds the parameters required to connect to an external platform’s APIs. Typically, this will contain authorization data for the account that will make the API calls on that platform.

### **Developer Console**

The developer tool for managing the entire lifecycle of extension apps. The Developer Console provides features to accomplish the following with extension apps:

- Register: Specify the app’s connection, extensions, actions, and capabilities
- Test: Verify the ability to connect to external APIs and exchange information correctly, and execute in the context of a Docusign envelope or workflow
- Manage: Review, modify, update, or delete
- Submit for Docusign review prior to publishing
- Publish to the App Center for public use or distribution to selected customers

### **Extension**

A group of actions and capabilities that support a type of external functionality, such as data verification or file output cloud storage. Each extension has an *extension contract* (set by the extension object’s template, specified in the manifest file by its template property) that identifies its type and the required actions or capabilities that you must implement to use it.

### **Extension app**

A type of partner application that enables a developer to enhance the functionality of Docusign envelopes or workflows by incorporating features from external platforms, such as Google Drive or Stripe, through calling their APIs. In contrast to API integrations, which are self-contained and distributed, hosted, or installed by their own developers, extension apps execute on the Docusign platform, are accessed through the Docusign App Center, and function within the Docusign user experience.

### **Extension app manifest**

A JSON file that provides metadata used to specify the elements of an extension app: its connection, its extensions, and its actions and capabilities, as well as metadata such as a title, description, icon, and screenshots that provide data needed for its being listed in the App Center. Extension app manifest files are validated against the JSON extension app manifest schema, maintained by Docusign, before they are approved for publication.

### **Extension point**

A place in a Docusign core functionality (such as an eSignature envelope or Agreement Builder workflow), predefined by Docusign, at which an action or capability can be invoked. When execution reaches an extension point, any relevant actions belonging to enabled extensions will be triggered.

### **Form-based experience**

In the Developer Console, a user experience that enables extension app developers to register an extension app by configuring the app’s properties in a [form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/). The form enables the developer to specify the app’s connection, extensions, actions, and capabilities; the properties thus specified are then used by the Developer Console to register an extension app manifest.

### **Agreement Builder**

Agreement Builder is a Docusign platform service that enables customers to build and digitize their agreement processes, called *workflows*, with Docusign and partner services. Docusign provides the Agreement Builder UI, an interactive workflow builder, to enable users to create and manage such workflows without using code; and the Agreement Builder API, which gives developers the ability to do the same from within their Docusign integrations.

### **Agreement Builder API**

The Agreement Builder API is an interface that enables developers to manage their automated workflows programmatically through REST-based calls.

### **Agreement Manager**

A foundational component of Docusign Intelligent Agreement Management (IAM), Docusign Agreement Manager is a platform service in the form of a smart repository built specifically to tackle the complexities of agreement management. More than just document storage, Agreement Manager is powered by Docusign AI, which identifies and stores key attributes of an agreement and makes them available for searching, filtering and serving up powerful insights.

### **Agreement Manager API**

The Agreement Manager API is an interface that enables developers to query Agreement Manager for AI-extracted data from the Agreement Manager smart agreement repository.

### **Private apps**

Private apps are extension apps published to the App Center in private mode. Developers can make these private apps available to specific accounts, allowing those accounts to adopt the extension and integrate it into their own Agreement Builder workflows. Private apps are only available to the accounts specified by the developer; accounts that haven’t been given access to the app cannot view or install it from the App Center. Before being published in private mode, extension apps must first pass a Docusign review.

### **Public apps**

Public apps are extension apps that have been [published to the App Center](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) in public mode, and therefore available for use by all Docusign customers. Publishing to the App Center makes an extension app discoverable by other Docusign users in other accounts, who can then adopt the extension app and incorporate it into their own Agreement Builder workflows. To be published, extension apps must first pass Docusign review.

### **Reference implementation**

An example implementation for a specific use case, developed by Docusign to help extension app developers learn how to work with extensions and build their own extension apps. Reference implementations are published as code repositories (“repos”) on the [Docusign GitHub](https://github.com/docusign) project.

### **Sample/default app manifest**

The default app manifest is loaded in the manifest editor as a developer attempts to register a new extension app. The default app manifest has sample data that can be used for testing, and it can be updated to reflect the real values of the application you wish to build.

### **Testing**

Docusign offers developers the means to test their extension apps before publishing. When viewing an extension app in the Developer Console, a developer can select App Testing and then choose from automated test options offered by Docusign that include testing the app’s connection properties as well as its ability to call all the API endpoints called by the extension. From the Developer Console, a developer can also launch the App Center to test the display of the app’s information, install it to their account, and ensure that it behaves correctly when invoked from within Docusign.

### Workflow

A sequence of execution steps that you can define and call in your apps. This sequence of steps can include Docusign functionality such as getting user information using web forms, requesting a signature, conditional logic, and triggering extensions from enabled extension apps. Workflows are created and managed through the Agreement Builder API and the [Workflow Designer](https://apps-d.docusign.com/send/workflows/).

### Workflow instance

When a workflow is triggered, an individual copy of its definition is activated. A workflow instance is created for a specific set of participants and holds the data for their agreement process.

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
