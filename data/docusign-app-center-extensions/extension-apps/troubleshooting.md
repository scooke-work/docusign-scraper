---
title: Troubleshooting
source_url: https://developers.docusign.com/extension-apps/troubleshooting/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Troubleshooting
scraped_at: '2026-06-18T19:51:49Z'
---

# Troubleshooting

This topic provides troubleshooting guidance for these types of errors:

- [Connection test errors](https://developers.docusign.com/extension-apps/troubleshooting/#connection-test-errors)
- [Extension test errors](https://developers.docusign.com/extension-apps/troubleshooting/#extension-test-errors)
- [Errors caused by an ad blocker](https://developers.docusign.com/extension-apps/troubleshooting/#errors-caused-by-an-ad-blocker)

## Connection test errors

The errors below may be displayed when you [run a connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) on the Developer Console Testing page.

| **Error message** | **Description** | **Troubleshooting** |
| --- | --- | --- |
| A refresh token was not returned from the token server. | The API service or the identity provider has not been configured to supply refresh tokens. | Check the API service documentation to confirm that refresh tokens are supported and to find out what is required to enable them. If you’re using an identity provider, make sure that it's configured to allow refresh tokens. See [Authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) for more information. |
| There was an error creating the connection instance. | An internal system error occurred when the API service or the identity provider returned an authorization code to the Docusign platform. | Retry the test. If the issue is persistent, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. |
| There was an error creating the OAuth token. | An internal system error occurred when the API service or the identity provider returned an authorization code to the Docusign platform. | Retry the test. If the issue is persistent, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. |
| There was an error exchanging the authorization code for a token. | The Docusign platform was unable to exchange the authorization code for an access token. This can be caused by:  - An invalid token URL in the extension app manifest - An invalid or expired authorization code returned by the API service or the identity provider - A network or internet issue when the Docusign platform attempted to exchange the authorization code for an access token - The authorization service or identity provider service not being available | - Check the [Token URL](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) in the connection settings or the [connections.params.customConfig.tokenUrl](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/#connection-custom-configuration-schema) in the extension app manifest and make sure that the value is correct. - Check the authorized user's account with the API service or identity provider, and make sure that the user has permissions for all of the [Scopes](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-connection-settings) specified in the connection settings or the [scopes](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/#connection-parameters-schema) specified in the extension app manifest. - Confirm that the authorization service or identity provider service is running. - Confirm that the API service or identity provider firewall is configured to allow requests from Docusign IP addresses. See [Firewall configuration](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/network-configuration/#firewall-configuration) for details. |
| There was an error persisting the OAuth token. | While exchanging the authorization code for an access token, the Docusign platform was unable to save the access token, possibly due to network issues. | Retry the test. If the issue is persistent, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. |
| There was a problem initializing the connection test. | The Docusign platform was unable to generate the authorization URL or initiate the connection test. | Retry the test. If the issue is persistent, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. |

## Extension test errors

The errors below may be displayed when you [run an extension test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) on the Developer Console Testing page.

| **Error message** | **Description** | **Troubleshooting** |
| --- | --- | --- |
| [error from API service] | Docusign successfully sent the request, but an error response was returned. The Developer Console displays the error details received from the API service. | - Review the API service documentation to determine why it could not process the request. - For HTTP errors such as 403 Forbidden, 404 Not Found, 502 Bad Gateway, or 503 Service Unavailable, confirm that the API service firewall is configured to allow requests from Docusign IP addresses. See [Firewall configuration](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/network-configuration/#firewall-configuration) for details. |
| Error executing the extension | The JSON request body is missing a required property, includes a property that is invalid, or otherwise does not conform to the expected schema. | Check the [action](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) or [capability](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) contract for the request, update the request body if it doesn't conform to the contract, and retry the test.  You can access the action and capability contracts for each extension from the [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) page. |
| Error scheduling execution | An internal system error occurred. | Retry the test. If the issue is persistent, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. |
| Failed to insert actionTest: createActionTest - AppVersion with id [ID] could not be found. | The extension app manifest has been updated since the extension app was installed to your account. | Uninstall the extension app and reinstall it. See [Run a connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) for installation instructions. |
| Failed to insert actionTest: Invalid record returned | An internal system error occurred. | Retry the test. If the issue is persistent, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance. |
| User Error: Request failed with status code 404 | The Docusign platform was unable to reach the endpoint path. | - Check [Params URI](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#update-extension-and-action-settings) in the [action](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) or [capability](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) settings or [actions.params.uri](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/action/) in the extension app manifest and make sure that it's correct and reachable. - Confirm that the API service firewall is configured to allow requests from Docusign IP addresses. See [Firewall configuration](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/network-configuration/#firewall-configuration) for details. |

## Errors caused by an ad blocker

### Description

When you try to install an extension app to your account in the [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) or uninstall an app, this error message is displayed:

`We encountered an unexpected error. Reload the page and try again.`

### Cause

This issue can occur when your device or network is running an ad blocker.

### Resolution

Either disable the ad blocker, or add [these domains](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/network-configuration/#ad-blocker-configuration) to the allowed list for the ad blocker.

If disabling the ad blocker or adding the domains to the allowed list doesn't resolve the issue, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance.

## Next steps

- Find out how to [test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).
- Get details about the structure of the [extension app manifest](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/).
- Retrieve [logs](https://developers.docusign.com/extension-apps/troubleshooting/review-logs/) of extension app installations and other activity.

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
