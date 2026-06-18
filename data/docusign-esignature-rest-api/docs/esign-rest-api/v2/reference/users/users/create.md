---
title: ': create'
source_url: https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/create/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T21:10:58Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/create/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/create/?explorer=true)

[Users](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/)

# : create

Adds new users to an account.

The body of this request
is an array
of [`Users`](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/create/#/definitions/Users) objects.
For each new user,
you must provide at least
the `userName`
and
an `email`.

The
[`userSettings` property](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/create/#user-settings)
is a [name/value](https://developers.docusign.com/docs/esign-rest-api/v2/reference/users/users/create/#/definitions/nameValue)
list that specifies the actions users can
perform.
In the example below,
Tal Mason
will be able to send envelopes,
and the activation email
will be in French
because the `locale`
is set to `fr`.

```
POST /restapi/v2/accounts/{accountId}/users
Content-Type: application/json
```

```
{
  "newUsers": [
    {
      "userName": "Claire Horace",
      "email": "claire@example.com.com"
    },
    {
      "userName": "Tal Mason",
      "email": "tal@example.com.com",
      "userSettings": [
        {
          "name": "canSendEnvelope",
          "value": "true"
        },
        {
          "name": "locale",
          "value": "fr"
        }
      ]
    }
  ]
}
```

A successful response
is a
`newUsers` array
with information about
the newly created users.
If there was problem creating a user,
that entry will contain
an `errorDetails` property
that describes what went wrong.

```
{
  "newUsers": [
    {
      "userId": "e064a4fc-xxxx-xxxx-xxxx-8bac87ede98a",
      "uri": "/users/e064a4fc-xxxx-xxxx-xxxx-8bac87ede98a",
      "email": "claire@example.com",
      "userName": "Claire Horace",
      "createdDateTime": "0001-01-01T08:00:00.0000000Z",
      "errorDetails": {
        "errorCode": "USER_ALREADY_EXISTS_IN_ACCOUNT",
        "message": "Username and email combination already exists for this account."
      }
    },
    {
      "userId": "a0e6c64b-xxxx-xxxx-xxxx-805ff3c8cffd",
      "uri": "/users/a0e6c64b-xxxx-xxxx-xxxx-805ff3c8cffd",
      "email": "tal@example.com",
      "userName": "Tal Mason",
      "userStatus": "ActivationSent",
      "createdDateTime": "2017-09-15T05:54:36.1265683Z"
    }
  ]
}
```

### User Settings

User settings
specify the capabilities
a newly created user will have.

| Name | Value | Authorization Requried | Description |
| --- | --- | --- | --- |
| allowBulkRecipients | Boolean | Admin | When **true**, this user can use the bulk send functionality. |
| allowRecipientLanguageSelection | Boolean | Admin | When **true**, this user can set the language used in the standard email format for a recipient when creating an envelope. |
| allowSendOnBehalfOf | Boolean | Admin | When **true**, this user can send envelopes 'on behalf of' other users through the API. |
| apiAccountWideAccess | Boolean | Admin | When **true**, this user can send and manage envelopes for the entire account using the DocuSign API. |
| canEditSharedAddressBook | String | Admin | Sets the address book usage and management rights for the user. Possible values:  - `none` - `use_only_shared` - `use_private_and_shared` - `share` |
| canManageAccount | Boolean | Admin & not setting for self | When **true**, this user can manage account settings, manage user settings, add users, and remove users. |
| canManageTemplates | String | Admin & not setting for self | Sets the template usage and management rights for the user. Possible values:  - `none` - `use` - `create` - `share` |
| canSendAPIRequests | Boolean | Admin & [account setting](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Accounts/Accounts/create/#account-settings) `usesAPI` is set | Only needed if integrator key is not used. When **true**, this user can send and manage envelopes using the DocuSign API. |
| canSendEnvelope | Boolean | Admin & not setting for self | When **true**, this user can send envelopes though the DocuSign Console. |
| enableDSPro | Boolean | SysAdmin | When **true**, this user can send and manage envelopes from the DocuSign Desktop Client. |
| enableSequentialSigningAPI | Boolean | SysAdmin | When **true**, this user can define the routing order of recipients for envelopes sent using the DocuSign API. |
| enableSequentialSigningUI | Boolean | SysAdmin | When **true**, this user can define the routing order of recipients while sending documents for signature. |
| enableSignerAttachments | Boolean | Admin | When **true**, this user can add requests for attachments from signers while sending documents. |
| enableSignOnPaperOverride | Boolean | Admin | When **true**, this user can override the account setting that determines if signers may sign their documents on paper as an option to signing electronically. |
| enableTransactionPoint | Boolean | SysAdmin | When **true**, this user can select an envelope from their member console and upload the envelope documents to TransactionPoint. |
| enableVaulting | Boolean | Admin | When **true**, this user can use electronic vaulting for documents. |
| locale | String | Admin | Sets the default language for the user. The supported languages are:  - Chinese Simplified: `zh_CN` - Chinese Traditional: `zh_TW` - Dutch: `nl` - English US: `en` - French: `fr` - German: `de` - Italian: `it` - Japanese: `ja` - Korean: `ko` - Portuguese: `pt` - Portuguese (Brazil): `pt_BR` - Russian: `ru` - Spanish: `es` |
| powerFormAdmin | Boolean | Admin | When **true**, this user can create, manage and download the PowerForms documents. |
| powerFormUser | Boolean | Admin | When **true**, this user can view and download PowerForms documents. |
| selfSignedRecipientEmailDocument | String | Admin | Sets how self-signed documents are presented to the email recipients. This can only be changed if the `selfSignedRecipientEmailDocumentUserOverride` [account setting](https://developers.docusign.com/docs/esign-rest-api/v2/reference/Accounts/Accounts/create/#account-settings) is **true**. This setting overrides the account setting. Possibe values are:  - `include_pdf`: A PDF of the completed document is attached to the email. - `include_link`: A secure link to the self-signed documents is included in the email. |
| vaultingMode | String | Admin | Sets the electronic vaulting mode for the user. Possible values:  - `none` - `estored` - `electronic_original` |

## Request

#### HTTP Request

POST

```
/restapi/v2/accounts/{accountId}/users
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account id GUID. |

\* Required

## SDK Method

### Users::create

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
