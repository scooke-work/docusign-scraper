---
title: API proxy
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- IT Infrastructure
- IT Infrastructure
- API Proxy
scraped_at: '2026-06-18T19:51:50Z'
---

# API proxy

An API proxy serves as an intermediary between a Docusign extension app and the external API service to which it sends requests. If requests are not in the format required by the API endpoints, or if the responses are not in the format that Docusign expects, you'll need to build and host an API proxy that transforms the requests and responses to the correct format before passing them on to their destinations. If the API’s endpoint requests and responses conform to Docusign specifications, an API proxy is not needed.

When an API proxy is in use, an extension app sends its requests to proxy endpoints instead of directly to the external service endpoints, and the proxy routes them to the service. Conversely, the API service sends its responses to the proxy, which then routes them to the extension app.

## API proxy settings in the extension app registration

Each endpoint that your extension app calls is represented in the extension app [registration](https://developers.docusign.com/extension-apps/build-an-extension-app/register/) as an [action](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) or [capability](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/). For example, if the extension app calls endpoints to list drives in a cloud storage system, list directories, and write a file to the specified drive and directory, the extension app registration would include an action or capability for each of those operations. Each action or capability definition includes the endpoint URI for that request. When an API proxy is in use, the URI specifies the proxy endpoint.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='581' width='1129' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![API proxy request flow](https://images.ctfassets.net/aj9z008chlq0/3kIVThFujjbPg7vEjUZW5m/5e161864a562398085f3b1e965bf3085/APIProxyRequestFlow.png?w=1129&h=581&q=50&fm=png)

If you register an extension app using a form, you can supply the proxy endpoint URIs when you [update the integration details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/). The other option is to supply the proxy endpoint URIs while [editing the app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/).

When an API proxy is in use, endpoint requests from the extension app will include the access token that the external service or identity provider returned during [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/). The API proxy should validate the token before passing the request on to the external API endpoint.

## Determine whether your extension app needs an API proxy

To determine whether your extension app needs an API proxy, evaluate the Docusign action contract for each [action](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capability](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) included in your extension app registration:

- Compare the request parameters in the contract with the values that the external API endpoints require.
- Compare the response parameters that the external service returns with the expected response values in the contract.

If there is any mismatch between a Docusign contract definition and the external API request or response, you'll need to set up an API proxy to handle the incompatibility.

You can access the action and capability contracts for each [extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) from the [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) page.

## Requirements

Here's a list of requirements for API proxies.

| **Feature** | **Requirement** |
| --- | --- |
| Interface type | REST |
| Authorization method | Authorization Code Grant (OAuth2) |
| Endpoint protocol | HTTPS |
| Synchronous response time limit | 10 seconds. Docusign will consider requests to have failed if no response is received within this time limit. |

## Next steps

- Learn more about [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/).
- See [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) to access the action and capability contracts for each extension.
- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).

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
