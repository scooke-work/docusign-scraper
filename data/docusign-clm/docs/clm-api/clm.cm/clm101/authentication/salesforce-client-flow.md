---
title: 'Authentication: Salesforce client flow'
source_url: https://developers.docusign.com/docs/clm-api/clm.cm/clm101/authentication/salesforce-client-flow/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- CLM API
- CLM API
- CLM.CM
- CLM.CM
- API 101
- API 101
- Authentication
- Authentication
- Salesforce Client Flow
scraped_at: '2026-06-18T21:49:14Z'
---

# Authentication: Salesforce client flow

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

With the Salesforce Client Flow, a Salesforce session token and the Org's Partner Server URL is used in place of a Docusign CLM refresh token to obtain a CLM API access token. To use this form of authentication the following setup is required:

1. The Salesforce Organization Id from which session tokens will be used must be mapped to a Docusign CLM account in the CLM account preferences. Docusign CLM supports a single one-to-one mapping of a Salesforce Org to CLM account. When the session token is passed to CLM, it will be verified and then a query is executed to determine the Salesforce organization from which the session originated. The Salesforce Client flow will then determine what CLM account that Salesforce organization is mapped to.
2. Users must be mapped in the CLM Address Book ahead of the authentication request. After determining the CLM account mapping, the Salesforce Client Flow will retrieve the user’s email address from Salesforce and try to map that to a user in the CLM account’s Address Book. Users can be provisioned in CLM using any supported user creation method. These include CLM user sync for Salesforce, bulk CSV upload, the CLM user interface, or the API.
   > **Note:** If the Salesforce Org has installed CLM’s managed package for Salesforce and followed the setup instructions, the above 2 items should already be in place and no further action should need to be taken to start using the Salesforce Client Flow authentication method to the REST API.

The token endpoint for the Salesforce Client Flow and sample JSON request/response are shown below. Note that the Org’s Partner Server API URL must also be passed along with the Salesforce session ID:

> **Production Salesforce Authentication Endpoint**
>
> ```
> https://auth.springcm.com/api/v201606/salesforce
> ```
>
> **UAT Salesforce Authentication Endpoint**
>
> ```
> https://authuat.springcm.com/api/v201606/salesforce
> ```

> **Note:** The Partner WSDL SOAP endpoint can be obtained in a visual force page from the following global variable where xxx represents the version of the API: `{!$Api.Partner_Server_URL__xxx}`

The access token can now be used to access the API. It must be passed in the Authorization header for all calls to the Object, Task and Content API. When passing it must be prefixed with “bearer” as shown below:
`Authorization: bearer [your access token]`

1

2

3

4

5

headers: Accept: 'application/json',

Content-Type: application/json

uri: https://auth.springcm.com/api/

v201606/salesforce

method: POST

{ "session\_id": [Salesforce session],

"api\_url": [Salesforce Partner WSDL SOAP

endpoint for the Org], "client\_id":

[client id passed to the authorization

endpoint], "client\_secret": [client

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
