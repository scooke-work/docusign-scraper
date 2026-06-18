---
title: 'Authentication: API User Authentication Flow'
source_url: https://developers.docusign.com/docs/clm-api/clm.cm/clm101/authentication/api-user-authentication-flow/
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
- Api User Authentication Flow
scraped_at: '2026-06-18T21:49:14Z'
---

# Authentication: API User Authentication Flow

Developing with the CLM API is only available for CLM customers with a production account. To purchase a plan to gain access to the CLM API, [contact Docusign Sales](https://www.docusign.com/contact-sales).

API User Authentication flow is intended to be used by back end batch operations for which there is not an end user that authenticates to the API. With API user authentication, a client id is mapped to an API user and then is used in place of a Docusign CLM refresh token to obtain a Docusign CLM API access token. To use this form of authentication the following setup is required:

1. An API User is created in the Docusign CLM address book and given the desired role and security groups needed for the API calls. Note that once a user is made an API user, it cannot be undone, so actual users of the Docusign CLM application should never be created as an API user.
2. The API user is mapped to a client id in Docusign CLM Preferences. To create the mapping, navigate to **Preferences->REST API** in the Docusign CLM user interface. In the **API User Mappings** section your client id can be mapped to the API user created in Step 1. Note that a single Client Id can be mapped to one and only one API User.

![Creating a user in the Docusign CLM address book](https://developers.docusign.com/img/clm-api/apiuseraddressbook.png?v=2023061320 "Creating a user in the Docusign CLM address book")

![Mapping a user to a client ID](https://developers.docusign.com/img/clm-api/apiusermapping.png?v=2023061320 "Mapping a user to a client ID")

After the mapping is created, API user authentication can be used by posting the mapped client id along with the corresponding client secret to the API User Authentication Endpoint. The access token endpoint for the API User Authentication Flow and sample JSON request/response are shown below:

> **Production API User Authentication Endpoint**
>
> ```
> https://auth.springcm.com/api/v201606/apiuser
> ```
>
> **UAT API User Authentication Endpoint**
>
> ```
> https://authuat.springcm.com/api/v201606/apiuser
> ```
>
> The access token can now be used to access the API. It must be passed in the Authorization header for all calls to the Object, Task and Content API. When passing it must be prefixed with “bearer” as shown below:
> `Authorization: bearer [your access token]`

1

2

3

4

5

6

7

headers: Accept: 'application/json',

Content-Type: application/json

uri: https://auth.springcm.com/api/

v201606/apiuser

method: POST

{

"client\_id": [Client Id mapped

to an API User],

"client\_secret": [Client secret

pair for the Client Id]

}

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
