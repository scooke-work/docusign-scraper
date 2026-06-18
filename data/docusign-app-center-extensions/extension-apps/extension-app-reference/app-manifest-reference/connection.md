---
title: Connection schema
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- App Manifest Reference
- App Manifest Reference
- Connection
scraped_at: '2026-06-18T19:51:51Z'
---

# Connection schema

The `connection` object provides information that allows your app to obtain authorization from your chosen external service.

| **Property** | **Type** | **Required?** | **Description** |
| --- | --- | --- | --- |
| `name` | `string` | Yes | The name of the connection. This value must be unique. |
| `id` | `string` | System-generated | The system-generated ID of the connection. This property is read-only. Do **not** include it when uploading your initial manifest. |
| `description` | `string` | Yes | The description of the connection. |
| `type` | `string` | Yes | Connection type. Valid values:  - `oauth2` |
| `params` | [Connection parameters object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/#connection-parameters-schema) | Yes | An object containing the parameters required to access an external platform API. |

### Connection: Parameters schema

| **Property** | **Type** | **Required?** | **Description** |
| --- | --- | --- | --- |
| `provider` | `string` | Yes | Valid values:  - `CUSTOM` |
| `scopes` | `string[]` | Yes | The scopes to request. |
| `clientId` | `string` | Yes | The client ID provided by the external platform. Maximum length: 191 characters |
| `clientSecret` | `string` | Yes | The client secret provided by the external platform. Maximum length: 191 characters |
| `grantType` | `string` | No | The type of [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) that the extension app uses to obtain permission to send requests to the external API service.  Valid values:   - `authorization_code` (default): Authorization Code Grant - `client_credentials`: Client Credentials Grant   Client Credentials Grant is supported only for private extension apps and only for clients in the US. |
| `customConfig` | [Custom configuration object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/#connection-custom-configuration-schema) | Yes | An object to store custom configuration information. |

### Connection: Custom configuration schema

| **Property** | **Type** | **Required?** | **Description** |
| --- | --- | --- | --- |
| `authorizationUrl` | `string` | Yes, if the [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) method is Authorization Code Grant. Not used for Client Credentials Grant. | The OAuth2 authorization endpoint. The URL’s top-level domain must be one of the following:  - `.com` - `.net` - `.org` - `.app` - `.cloud`  Do not include `docusign.` in the domain. |
| `tokenUrl` | `string` | Yes | OAuth2 token endpoint. |
| `authorizationParams` | `object` | No | An object to store any query parameters required for the authorization URL. |
| `authorizationMethod` | `string` | No | Valid values:  - `header` (default) - `body` |
| `scopeSeparator` | `string` | No | The delimiter used to separate the scopes. The default value is a comma. |

A connection object looks like this:

```
{
  "name": "authentication",
  "description": "secure connection to proxy",
  "type": "oauth2",
  "params": {
    "provider": "CUSTOM",
    "scopes": [],
    "clientId": "230546a7-xxxx-xxxx-xxxx-af205d5494ad",
    "clientSecret": "119376b2-xxxx-xxxx-xxxx-aa951d7878eb",
    "grantType": "authorization_code",
    "customConfig": {
      "authorizationUrl": "https://example.com/auth",
      "tokenUrl": "https://example.com/token",
      "authorizationParams": {
        "access_type": "offline",
        "prompt": "consent"
      }
    }
  }
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
