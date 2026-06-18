---
title: Actions
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Concepts
- Concepts
- Actions
scraped_at: '2026-06-18T19:51:50Z'
---

# Actions

Actions are the individual functions that do the work in your extension app.

When an action is triggered at an applicable [extension point](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/#extension-points), Docusign calls the action’s specified API endpoint. For example, a workflow step is the extension point for an action to write a file to cloud storage. When an executing workflow instance reaches the file output step, the request to write the file is sent to the external API service.

Depending on the type of action being invoked, the response data will be integrated back into your Docusign workflow as a confirmation, a prompt for further action, or values that appear in UI controls.

## Define an action in the app manifest

You can define an action in your extension app’s manifest file, as shown in this example. The definition includes the URL of the endpoint to call when the action is invoked. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for details about the properties.

```
"actions": [
  {
    "name": "write-file",
    "description": "Writes a file to a cloud storage system",
    "template": "FileIO.Version1.WriteFile",
    "connectionsReference": "authentication",
    "params": {
      "uri": "https://fontara.com/api/writefile"
    }
  }
]
```

In addition to defining each action in the `actions` object, the manifest file must reference the actions in the `extensions.actionReferences` array. See [Extension schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) for details.

## Update action settings in a form

When using the form-based experience to [register an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/), corresponding action(s) are added for you when you select an extension. You can then update each action’s settings at the [extension app's integration details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#access-integrations-details-for-an-extension-app) page.

During the form-based extension app registration process, if you select a [file IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), its required actions are automatically added to the app. You can then configure the actions' endpoint URIs and other properties on the [Integration Details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/) page. The extension's optional capabilities can be added or removed only by [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). After you've added capabilities via the manifest file, you can edit them on the Integration Details page. See [Action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) for information about action and capability properties in the app manifest file.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='476.99999999999994' width='1119' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Action Name, Description, URI](https://images.ctfassets.net/aj9z008chlq0/3ugGZWlbrCnElJTw941IGh/44b46b34831b889263e15354fd3cb861/FormBasedUIAction.png?w=1119&h=477&q=50&fm=png)

## Shared actions

An extension app can include multiple [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/). If more than one extension supports the same action or capability, that action or capability can be defined only once for the app, and the extensions will share its definition. For example, if an extension app includes both the file input cloud storage and file output cloud storage extensions, the app can have only one definition for the **List Directory Contents** action, and both extensions will use that definition. Docusign does not support multiple versions of the same action or capability in the same extension app.

## Next steps

- Learn how the [action schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) defines actions within your extension app.
- Explore how [connections](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/) enable Docusign to send requests to an external service.
- Discover how [extensions and extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/) empower you to customize the Docusign experience.
- See [sample app manifest files](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for all supported extensions.

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
