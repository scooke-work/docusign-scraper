---
title: Extension app concepts
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/concepts/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Concepts
scraped_at: '2026-06-18T19:51:50Z'
---

# Extension app concepts

This page describes concepts used in extension app workflows. For details on extension apps, or your process for building an extension app, see [Extension apps 101 overview](https://developers.docusign.com/extension-apps/extension-apps-101/) or [Build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).

### Action

*Actions* are the individual functions that do the work in your extension app. They specify the external platform endpoints to call from your Docusign agreement process. Each action has an *action contract* (set by the action object’s template property in the app manifest or in the [form-based UI](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings)) that identifies its type and the inputs/outputs that it uses

See [Actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) for details, an example definition, and a list of supported action types.

### App Center

The *App Center* is the location where users can find, purchase, install, and incorporate approved, partner-built extension apps into their Docusign workflows. Before you can publish your extension app into the App Center, it must first pass a review.

### App manifest

The *app manifest* is a JSON file that provides metadata used to specify the elements of an extension app: its [connections](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/), its [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/), and its [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/), as well as metadata such as a title, description, icon, and screenshots that provide data needed for its being listed in the App Center. Extension app manifest files are validated against the JSON extension app manifest schema, maintained by Docusign, before they are approved for publication.

See an [Example JSON manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) or view the [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for a full list of supported elements. As an alternative to the app manifest, you can also register an extension app using [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/).

### Capabilities

Capabilities define optional features that enhance the user experience, such as browsing folders or listing drives. While not required, they’re necessary if your extension app needs to support these types of interactions. For example, if a user should be able to select a storage location, your extension must implement the relevant capabilities. Without them, the associated UI elements will not appear at the applicable [extension point](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/#extension-points). Capabilities vary by extension and use case, but follow a consistent structure across contexts. 

See Capabilities for details and an example definition.

### Connection

A *connection* is an object, configured in the form-based extension app registration experience or specified in an extension app’s manifest file, that holds the parameters required to connect to an external platform’s APIs. Typically, this will contain authorization data for the account that will make the API calls on that platform. This can be defined in the [app manifest](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/#connections) or through the [form-based experience](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings). 

See [Connections](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/) for details and an example definition.

### Developer Console

The *Developer Console* is the web application used to create, test, and manage extension apps. 

See [Developer Console overview](https://developers.docusign.com/extension-apps/developer-console-overview/)  for details or open the [Developer Console](https://devconsole.docusign.com) to create or manage an extension app.

### Extension

An *extension* is a group of actions that support a type of external functionality, such as data verification or file archive. Each extension has an *extension contract* (set by the extension object’s template, specified in the manifest file by its template property) that identifies its type and the required actions that you must implement to use it. This can be defined in the [app manifest](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/#extensions) or through the [form-based experience](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#add-an-extension).

See [Extensions and extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/) for details, an example definition, and a list of supported extensions.

### Extension point

An *extension point* is a place in a Docusign agreement process where an extension app can invoke external functionality. An extension point is associated with actions of specific types, which will be triggered whenever that extension point is reached in a workflow.

For example, a file archive action is associated with the eSignature extension point. When an envelope is completed, any enabled file archive action will be triggered.

See [Extensions and extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/) for details, an example definition, and a list of supported extensions.

### Workflows and Workflow Builder API

*Workflows,* which are created and managed through the Workflow Builder API and the [Workflow Designer](https://apps-d.docusign.com/send/workflows/), are sequences of execution steps that you can define and call in your apps. This sequence of steps can include Docusign functionality such as getting user information using web forms, requesting a signature, conditional logic, and triggering extensions from enabled extension apps. 

See [Workflow Builder API 101 overview](https://developers.docusign.com/docs/workflow-builder-api/workflow-builder101/) for details.

## Next steps

- Learn how to configure [connections](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/) for your extension app.
- Discover how [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) power the essential behaviors of your extension app.
- See how different extension types integrate with Docusign products in [Extensions and extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/).
- Review the structure and contents of a manifest in an [Example JSON manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/).
- Use the [Developer Console overview](https://developers.docusign.com/extension-apps/developer-console-overview/)  to start building and managing your extension app.

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
