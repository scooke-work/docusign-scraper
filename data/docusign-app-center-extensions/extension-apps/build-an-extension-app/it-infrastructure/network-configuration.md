---
title: Network configuration
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/network-configuration/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- IT Infrastructure
- IT Infrastructure
- Network Configuration
scraped_at: '2026-06-18T19:51:51Z'
---

# Network configuration

This section describes network setup required to ensure that Docusign can communicate successfully with your platform.

## Firewall configuration

If your API service, API proxy, or identity provider is protected by a firewall, you must configure it to allow requests from Docusign API addresses that are used to:

- Authorize a Docusign account to connect to your API service when a Docusign user installs and configures your extension app.
- Send requests to your API service when extension app [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) are executed.

See [Docusign endpoint IP addresses](https://www.docusign.com/trust/security/esignature#docusign-endpoint-ip-addresses) for a list of addresses from which the firewall should allow requests. The IP addresses are listed by account region.

Allow IP addresses for all the regions in which you intend to make your extension app available on the production [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/). For example, if you plan to make your extension app available to users in the US and Canada, include the IP addresses for North America-based and Canada-based accounts.

By default, published extension apps are available only to US customers on the production App Center. You can specify availability in additional regions. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for details.

See this table for additional guidance on which regions’ IP addresses you should allow:

| Account region | Allow IP addresses for this region | Notes |
| --- | --- | --- |
| North America-based and demo accounts | Always | All extension apps require these IP addresses for development and testing in the Docusign developer (demo) environment.  These IP addresses are also used for production App Center users whose Docusign accounts are based in the US data centers NA1, NA2, NA3, or NA4. |
| Canada-based accounts | If your extension app will be available to production App Center users whose Docusign account is based in the Canada (CA) data center. |  |
| European Union-based accounts | If your extension app will be available to production App Center users whose Docusign account is based in the European Union (EU) data center. |  |
| Australia-based accounts | If your extension app will be available to production App Center users whose Docusign account is based in the Australia (AU) data center. |  |
| Japan-based accounts | If your extension app will be available to production App Center users whose Docusign account is based in the Japan (JP1) data center. |  |

The Docusign endpoint IP addresses should be added to the allowed lists on all firewalls in all environments that may receive requests from Docusign extension apps. For example, if your platform has separate development, test, and production environments, add the IP addresses to all of their firewalls.

If your firewall is not configured to allow requests from Docusign endpoint IP addresses, you may see any of the following errors when trying to [test your extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/):

- [403 Forbidden](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403)
- [404 Not Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)
- [502 Bad Gateway](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/502)
- [503 Service Unavailable](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503)
- There was an error exchanging the authorization code for a token.
- User Error: Request failed with status code 404

## Ad blocker configuration

If your network runs an ad blocker, you’ll need to add these addresses to its allowed list to install and uninstall extension apps in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/):

- `https://app.optimizely.com`
- `https://app.optimizely.com/*`
- `https://*.app.optimizely.com`
- `https://*.app.optimizely.com/*`
- `https://api.optimizely.com`
- `https://api.optimizely.com/*`
- `https://cdn-prod.optimizely-static.com`
- `https://cdn-prod.optimizely-static.com/*`
- `https://p13n-results-api.optimizely.com/*`
- `*.siteintercept.qualtrics.com`
- `*.zn4o6wz32wpljkntm-docusign.siteintercept.qualtrics.com`

If an ad blocker prohibits access to these addresses, App Center users may see this error when they try to install or uninstall an extension app:

`We encountered an unexpected error. Reload the page and try again.`

Omitting the two `qualtrics.com` domains from the allowed list won't cause issues, but Docusign recommends adding them to the allowed list. This ensures that users will be able to submit feedback to Docusign via a form that appears on some of our pages.

## Next steps

- Get an overview of the process to [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/).
- Find out how to [test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).
- Learn how to [troubleshoot errors](https://developers.docusign.com/extension-apps/troubleshooting/).

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
