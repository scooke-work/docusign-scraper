---
title: ': create'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accounts/create/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:26Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accounts/create/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accounts/create/?explorer=true)

[Accounts](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accounts/)

# : create

Creates new Docusign accounts.
You can use this method to create
a single account
or up to 100 accounts at a time.

**Note:** This method is restricted to partner integrations.
You must work with Docusign Professional Services
or Docusign Business Development,
who will provide you with the Distributor Code
and Distributor Password
that you need to include in the request body.

When creating a single account,
the body of the request is a
[`newAccountRequest`](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accounts/create/#/definitions/newAccountRequest)
object.

Example:

```
{
  "newAccountRequest": [
    {
      "accountName":"Test Account",
      "distributorCode":"MY_DIST_CODE",
      "distributorPassword":"MY_DIST_PWD",
      "initialUser":{
        "email":"user@emaildomain.com",
        "firstName":"John",
        "middleName": "Harry",
        "lastName":"Doe",
        "suffixName": "",
        "userName": "John Doe",
        "jobTitle": "Engineer",
        "company": "Test Company"
      },
      "addressInformation":{
        "address1": "1234 Main Street",
        "address2": "Suite 100",
        "city": "Seattle",
        "state": "WA",
        "postalCode": "98101",
        "country": "US",
        "phone": "1234567890",
        "fax": "1234567891"
      },
      "planInformation":{
        "planId":"37085696-xxxx-xxxx-xxxx-7ea067752959"
      },
      "referralInformation":{
        "includedSeats": "1",
        "referralCode": "code",
        "referrerName": "name"
      }
    }
  ]
}
```

If the request succeeds,
it returns a
201 (Created) HTTP response code.
The response returns the new account ID, password, and the default user
information for each newly created account.

When creating multiple accounts,
the body of the request is a
`newAccountRequests`
object,
which contains one or more
[`newAccountDefinition`](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accounts/create/#/definitions/newAccountDefinition)
objects.
You can create up to 100 new accounts
at a time this way.

The body for a multi-account
creation request
looks like this in JSON:

```
{
  "newAccountRequests": [
    {
      "accountName": "accountone",
      . . .
    },
    {
      "accountName": "accounttwo",
      . . .
    }
  ]
}
```

A multi-account request
looks like this in XML:

```
<newAccountsDefinition xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.docusign.com/restapi">
  <newAccountRequests>
    <newAccountDefinition>
      . . .
    </newAccountDefinition>
    <newAccountDefinition>
      . . .
    </newAccountDefinition>
  </newAccountRequests>
</newAccountsDefinition>
```

A multi-account creation request
may succeed (report a 201 code)
even if some accounts could not be created.
In this case, the `errorDetails` property
in the response contains specific information
about the failure.

## Request

#### HTTP Request

POST

```
/restapi/v2.1/accounts
```

## SDK Method

### Accounts::create

## Request Body

## Responses

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
