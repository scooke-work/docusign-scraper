---
title: App manifest reference
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- App Manifest Reference
scraped_at: '2026-06-18T19:51:49Z'
---

# App manifest reference

Each extension app is defined by a manifest file in JSON format. This section describes the root object of the manifest schema.

**Note:** The maximum size for the manifest file is 8 MB.

| Property | Type | Required? | Description |
| --- | --- | --- | --- |
| `id` | `string` | System-generated | The system-generated ID of the extension app. This property is read-only. Do **not** include it when uploading your initial manifest. |
| `name` | `string` | Yes | The name of your app. This value must be unique. Maximum length is 30 characters. |
| `distribution` | `string` | Yes | Determines whether your extension app will be private or public. Valid values:   - `PUBLIC` (default) - `PRIVATE`  Values are case-sensitive. Once the app is published, you cannot modify this value. For more information, see [Choosing private distribution instead of public](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/). |
| `description` | `object` | Yes | An object providing a short and long description for your app. |
| `description.short` | `string` | Yes | A short description of your extension app. Maximum length is 100 characters. |
| `description.long` | `string` | Yes | A long description of your extension app. Maximum length is 2,000 characters. |
| `publicationRegions` | `array of strings` | No | The regions in which the extension app will be available after it is published to the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/). A production App Center user can install your extension app if their account is based in a Docusign data center that corresponds to one of the specified regions.  Valid values:   - `AU`: Australia. Data center: AU. - `CA`: Canada. Data center: CA. - `EU`: European Union. Data center: EU. - `JP`: Japan. Data center: JP1. - `US` (default): United States. Data centers: NA1, NA2, NA3, NA4.  This example `publicationRegions` property would make your extension app available to users whose accounts are based in any of the data centers AU, CA, EU, JP1, NA1, NA2, NA3, or NA4: `"publicationRegions": ["AU","CA","EU","JP","US"]`  After an extension app has been published, you can add regions, but you cannot remove them. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for more information. |
| `termsOfServiceUrl` | `string` | Yes | The URL of your app’s terms of service. |
| `privacyUrl` | `string` | Yes | The URL of your app’s privacy policy. |
| `supportUrl` | `string` | Yes | The URL at which users can receive support for your app. |
| `signupUrl` | `string` | Not when creating your app, but required to publish the app | The URL at which users of your app can create an account with the API service to which your app connects. |
| `publisher` | `object` | Yes | The app publisher’s information. Within this object, you must provide `publisher.name` and at least one of the following properties:  - `publisher.email` - `publisher.phone` - `publisher.website` |
| `publisher.name` | `string` | Yes | The name of the app publisher. |
| `publisher.email` | `string` | Required if both `phone` and `website` are omitted | The email address of the app publisher. |
| `publisher.phone` | `string` | Required if both `email` and `website` are omitted | The phone number of the app publisher. |
| `publisher.website` | `string` | Required if both `email` and `phone` are omitted | The URL of the app publisher's website. |
| `icon` | `object` | No | An object providing an icon for your app. |
| `icon.data` | `base64` | Yes, when `icon` is included | The Base64 representation of your app’s icon. The app icon must have a 1:1 aspect ratio and be a maximum size of 100x100 pixels. The maximum file size is 5MB. |
| `icon.mediaType` | `string` | Yes, when `icon` is included | The media type of the icon. Valid values:  - `image/jpeg` - `image/png` |
| `screenshots` | `Array of JSON objects` | No | A list of screenshots representing your app. You can provide a maximum of four images. In the Developer Console and App Center, the screenshots will be displayed in the order listed in your manifest. |
| `screenshots[].data` | `base64` | Yes, for each object in the `screenshots` array | The Base64 representation of a single screenshot. The screenshot must have a 16:10 aspect ratio. The minimum dimensions are 848x530 pixels, and the maximum dimensions are 1600x1000 pixels. The maximum file size is 5 MB. |
| `screenshots[].mediaType` | `string` | Yes, for each object in the `screenshots` array | The media type of the screenshot. Valid values:  - `image/jpeg` - `image/png` |
| `connections` | `[`[Connection object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/)`]` | Yes | A list of connections. Each app can have a maximum of one connection. |
| `extensions` | `[`[Extension object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/)`]` | No | A list of extensions. |
| `actions` | `[`[Action object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/)`]` | No | A list of [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) that the extension app implements. Actions and capabilities define the endpoints that invoke functionality provided by the external API service. |
| `changelog` | `string` | Yes, when updating a manifest to v1.1 or higher. Cannot be set when creating an app or updating a v1.0 draft. | A brief summary of changes made to the app since it was last published. This value will be displayed in the Developer Console and App Center.  The maximum length is 191 characters. |

A basic manifest looks like this.

```
{
  "name": "Account beneficiary update",
  "description": {
    "short": "Writes beneficiary documents to cloud storage",
    "long": "This app is designed to write completed account beneficiary documents to a cloud storage system."
  },
  "termsOfServiceUrl": "https://www.fontara.com/tos",
  "privacyUrl": "https://www.fontara.com/privacy-security",
  "supportUrl": "https://www.fontara.com/support",
  "publisher": {
    "name": "Fontara",
    "email": "sample@fontara.com"
  },
  "connections": [
    {
      "name": "authentication",
      "description": "Secure connection to sample extension app",
      "type": "oauth2",
      "params": {
        "provider": "CUSTOM",
        "clientId": "8d606a57-xxxx-xxxx-xxxx-219e80c7ed16",
        "clientSecret": "lfvZIUH…leaGCreU=",
        "scopes": [],
        "grantType": "authorization_code",
        "customConfig": {
          "authorizationMethod": "header",
          "authorizationParams": {
            "prompt": "consent",
            "access_type": "offline"
          },
          "authorizationUrl": "https://www.fontara.com/api/oauth/authorize",
          "requiredScopes": [],
          "scopeSeparator": " ",
          "tokenUrl": "https://www.fontara.com/api/oauth/token",
          "refreshScopes": []
        }
      }
    }
  ],
  "icon": {
    "data": "iVBORw...SuQmCC",
    "mediaType": "image/png"
  },
  "screenshots": [],
  "extensions": [
    {
      "name": "My File Output Cloud Storage Extension",
      "description": "Writes files to cloud storage",
      "template": "FileIO.Version1.FileOutputCloudStorage",
      "actionReferences": [
        "list-directory-contents",
        "list-drives",
        "write-file"
      ],
      "capabilities": [
        "FileIO.Version1.ListDirectoryContents",
        "FileIO.Version1.ListDrives"
      ]
    }
  ],
  "actions": [
    {
      "name": "list-directory-contents",
      "description": "Returns a list of folders on a cloud storage system",
      "template": "FileIO.Version1.ListDirectoryContents",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://www.fontara.com/api/listdirectorycontents"
      }
    },
    {
      "name": "list-drives",
      "description": "Returns a list of drives on a cloud storage system",
      "template": "FileIO.Version1.ListDrives",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://www.fontara.com/api/listdrives"
      }
    },
    {
      "name": "write-file",
      "description": "Writes a file to a cloud storage system",
      "template": "FileIO.Version1.WriteFile",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://www.fontara.com/api/writefile"
      }
    }
  ],
  "signupUrl": "https://www.fontara.com/signup",
  "publicationRegions": [
    "US"
  ],
  "distribution": "PUBLIC"
}
```

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
