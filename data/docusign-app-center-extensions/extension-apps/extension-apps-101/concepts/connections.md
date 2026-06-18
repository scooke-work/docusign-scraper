---
title: Connections
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Concepts
- Concepts
- Connections
scraped_at: '2026-06-18T19:51:50Z'
---

# Connections

A connection is the part of an extension app that defines the parameters required to access an external platform’s APIs. Typically, this will contain authorization data for the account that will make the API calls on that platform. To extend your workflow to multiple external platforms, you can register and apply multiple extension apps, one for each platform.

## Define a connection in the extension app manifest

This JSON snippet demonstrates how to define a connection in an app manifest file. See [Connection schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) for more details.

```
"connections": [
    {
      "name": "authentication",
      "description": "Secure connection to example API proxy",
      "type": "oauth2",
      "params": {
        "provider": "CUSTOM",
        "scopes": [],
        "clientId": "6f22ef90-xxxx-xxxx-xxxx-e4be02783d3c",
        "clientSecret": "6cb7023b-xxxx-xxxx-xxxx-d1c4a56d1001",
        "customConfig": {
          "tokenUrl": "https://example.app/api/oauth/token",
          "authorizationUrl": "https://example.app/api/oauth/code",
          "authorizationParams": {
            "access_type": "offline",
            "prompt": "consent"
          },
          "authorizationMethod": "header",
          "scopeSeparator": " ",
          "requiredScopes": []
        }
      }
    }
  ]
```

## Define a connection using a form

You can also define a connection using a form. After you have [used a form to register your extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), you can update the connection settings on the [extension app's integration details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#access-integrations-details-for-an-extension-app) page.

Use the form to give the connection a unique name and configure the parameters required for authorization with the external platform including scopes, the OAuth2 endpoint, the client ID and secret, and any authorization query parameters. See [Update connection settings](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) for more details on how to configure these values.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1288.0000000000002' width='1404' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the basic info section of the form-based experience for creating a connection](https://images.ctfassets.net/aj9z008chlq0/59a2xlYl9fEnuTwoLs61F3/815e033a4f1c944cebf746a37b83d1c3/ConnectionFormBasedBasicInfo.png?w=1404&h=1288&q=50&fm=png)

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1238' width='1418' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the custom config section of the form-based experience for creating a connection](https://images.ctfassets.net/aj9z008chlq0/3G0iaW9kfFrunCkd0EkSpF/d9045702ec99122eba9947840c6692fc/ConnectionFormBasedCustomConfig.png?w=1418&h=1238&q=50&fm=png)

## Next steps

- [Actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/)
- [Extensions and extension points](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/)
- [Example JSON manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/)
- [Developer Console overview](https://developers.docusign.com/extension-apps/developer-console-overview/)

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
