---
title: Extension app manifest
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Concepts
- Concepts
- Extension App Manifest
scraped_at: '2026-06-18T19:51:50Z'
---

# Extension app manifest

An extension app’s JSON app manifest file contains its publisher and metadata, its connection settings, and the actions and capabilities that it can execute.

See an [example extension app use case](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) with manifest or view the [app manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for a full list of supported elements.

As an alternative to registering an extension app by constructing a manifest file, you can register it [using a guided, form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/).

An extension app will connect to a single external platform. The extension app’s manifest file defines:

- **A** [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/). This connection holds the parameters required to access the external platform’s APIs, typically authorization data for the account that will make the API calls on that platform. To extend your workflow to multiple external platforms, you can create and apply multiple extension apps, one for each platform.
- **Any number of** [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/). An extension is a group of related external [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) that are displayed and enabled together in the Developer Console. Extensions represent sets of workflow tasks, such as archiving data or validating sets of input data.

  The value of the extension’s `template` property determines which external platform actions your extension app must implement to support its functionality. For example, a data validation extension contract must implement at least one action to validate a dataset.

  **Note:** The action names in the extension's `actionReferences` object must match the names in the `actions` objects.
- **Any number of** [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/). Actions specify the external platform endpoints to call from your Docusign workflows. Each action calls into a specific external platform API endpoint (such as to archive a document) when an applicable [extension point](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/#extension-points) trigger is reached (such as to write a file to cloud storage), and the response data will be integrated back into your Docusign workflow, when possible, as a confirmation or prompt for further action.

  The value of the action’s `template` property determines which specific request/response contracts and sets of extension points it will use. See [Actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) for details about these IDs and a full listing.
- **Any number of** [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/). Capabilities are optional actions that an extension app can implement to offer features beyond the base functionality defined by required actions. Like actions, they use specific request/response contracts and may be invoked at designated extension points to enhance the workflow with additional behaviors. See [Capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) for implementation details.
- A set of metadata that describes the extension app, publisher, and distribution options. This metadata is referenced when the extension app is published in the App Center.

  See [Publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) for details on the requirements and best practices for setting this metadata in order to pass validation and review.

This diagram illustrates how the pieces of an extension app manifest file are organized.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1404' width='2688' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Image showing an example extension app manifest organization, including an action shared between two extensions](https://images.ctfassets.net/aj9z008chlq0/3cp2lXql1UzUy4LB4Mb1LV/41979f2577100e1082eb0b09fd99ffe5/Example_extension_app_manifest_organization.png?w=2688&h=1404&q=50&fm=png)

After you have created your extension app manifest, you can begin [testing](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) and publish your extension app to the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

## Example app manifest

```
{
  "name": "File Output Cloud Storage",
  "description": {
    "short": "This is a sample short description",
    "long": "This is a sample long description"
  },
  "termsOfServiceUrl": "https://www.fontara.com/tos",
  "privacyUrl": "https://www.fontara.com/privacy-security",
  "supportUrl": "https://www.fontara.com/support",
  "publisher": {
    "name": "Sample Publisher",
    "email": "sampleemail@fontara.com"
  },
  "connections": [
    {
      "name": "authentication",
      "description": "Secure connection to sample extension app",
      "type": "oauth2",
      "params": {
        "provider": "CUSTOM",
        "clientId": "[omitted]",
        "clientSecret": "[omitted]",
        "scopes": [],
        "grantType": "authorization_code",
        "customConfig": {
          "authorizationMethod": "header",
          "authorizationParams": {
            "prompt": "consent",
            "access_type": "offline"
          },
          "authorizationUrl": "https://fontara.com/api/oauth/authorize",
          "requiredScopes": [],
          "scopeSeparator": " ",
          "tokenUrl": "https://fontara.com/api/oauth/token",
          "refreshScopes": []
        }
      }
    }
  ],
  "icon": {
    "data": "[omitted]",
    "mediaType": "image/png"
  },
  "screenshots": [],
  "extensions": [
    {
      "name": "File Output Cloud Storage",
      "description": "Used to store files to cloud storage",
      "template": "FileIO.Version1.FileOutputCloudStorage",
      "actionReferences": [
        "write-file",
        "list-drives",
        "list-directory-contents"
      ],
      "capabilities": [
        "FileIO.Version1.ListDirectoryContents",
        "FileIO.Version1.ListDrives"
      ]
    }
  ],
  "actions": [
    {
      "name": "write-file",
      "description": "This is a description of my write file action",
      "template": "FileIO.Version1.WriteFile",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://fontara.com/api/writefile"
      }
    },
    {
      "name": "list-drives",
      "description": "This is a description of my list drives action",
      "template": "FileIO.Version1.ListDrives",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://fontara.com/api/listdrives"
      }
    },
    {
      "name": "list-directory-contents",
      "description": "This is a description of my list directory contents action",
      "template": "FileIO.Version1.ListDirectoryContents",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://fontara.com/api/listdirectorycontents"
      }
    }
  ],
  "signupUrl": "https://www.fontara.com/signup",
  "changelog": "",
  "publicationRegions": [
    "US"
  ],
  "distribution": "PUBLIC"
}
```

## Next steps

- See an [Example JSON manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/).
- Learn more about [connections](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/).
- Learn more about [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/).
- Learn more about [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/).
- Browse the complete list of [extensions and extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/).

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
