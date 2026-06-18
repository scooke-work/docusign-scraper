---
title: TemplateRecipients Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Templates
- Templates
- Templaterecipients
scraped_at: '2026-06-18T21:10:30Z'
---

# TemplateRecipients Resource

The TemplateRecipients resource allows you manage the recipients of an template.

The exact parameters associated with a recipient depend on the recipient type. There are seven recipient types: Agents, Carbon Copies, Certified Deliveries, Editors, In Person Signers, Intermediaries, and Signers.

Not all recipients are are available to all account types, review you account plan to determine which recipient types are available to you. If you are working in the development environment, all recipient types are available.

Each recipient type is described below:

[Agents](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/#agents): This recipient can add name and email information for recipients that appear after the recipient in routing order.

[Carbon Copies](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/#carboncopies): Use this action if the recipient should get a copy of the template, but the recipient does not need to sign, initial, date or add information to any of the documents. This type of recipient can be placed in any order in the recipient list. The recipient receives a copy of the template when the template reaches the recipient's order in the process flow and when the template is completed.

[Certified Deliveries](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/#certifiedDeliveries): Use this action if the recipient must receive the completed documents for the template to be completed, but the recipient does not need to sign, initial, date or add information to any of the documents.

[Editors](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/#editors): This recipient has the same management and access rights for the template as the sender and can make changes to the template as if they were using the Advanced Correct feature. This recipient can add name and email information, add or change the routing order and set authentication options for the remaining recipients. Additionally, this recipient can edit signature/initial tabs and data fields for the remaining recipients. The recipient must have a Docusign account to be an editor.

[In Person Signers](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/#inPerson): Use this action if the signer is in the same physical location as a Docusign user who will act as a Signing Host for the transaction. The recipient added is the Signing Host and new separate Signer Name field appears after Sign in person is selected.

[Intermediaries](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/#intermediaries): This recipient can, but is not required to, add name and email information for recipients at the same or subsequent level in the routing order (until subsequent Agents, Editors or Intermediaries recipient types are added).

[Signers](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/#signers): Use this action if your recipient must sign, initial, date or add data to form fields on the documents in the template.

### Core JSON Layout

The following shows the core JSON layout for a recipient.

```
"email": "email.name@company.com",
  "name": "recipient name",
  "accessCode": "",
  "addAccessCodeToEmail": false,
  "clientUserIs": null,
  "embeddedRecipientStartURL": "string",
  "customFields": {
    "sample string 1",
    "sample string 2"
  },
  "emailNotification"{
    "emailBody":"email text",
    "emailSubject":"Subject text",
    "supportedLanguage":"en",
  },
  "excludedDocuments": ["2", "4"],
  "idCheckConfigurationName": null,
  "idCheckInformationInput": {
    "addressInformationInput": {
      "addressInformation": {
        "address1": "sample string 1",
        "address2": "sample string 2",
        "city": "sample string 3",
        "state": "sample string 4",
        "zip": "sample string 5",
        "zipPlus4": "sample string 6"
      },
      "displayLevelCode": "sample string 1",
      "receiveInResponse": "sample string 2"
    },
    "dobInformationInput": {
      "dateOfBirth": "sample string 1",
      "displayLevelCode": "sample string 2",
      "receiveInResponse": "sample string 3"
    },
    "ssn4InformationInput": {
      "ssn4": "sample string 1",
      "displayLevelCode": "sample string 2",
      "receiveInResponse": "sample string 3"
    },
    "ssn9InformationInput": {
      "ssn9": "sample string 1",
      "displayLevelCode": "sample string 2"
    }
  },
  "inheritEmailNotificationConfiguration": false,
  "note": "",
  "phoneAuthentication": {
    "recipMayProvideNumber": "sample string 1",
    "validateRecipProvidedNumber": "sample string 2",
    "recordVoicePrint": "sample string 3",
    "senderProvidedNumbers": [
      "sample string 1",
      "sample string 2"
    ]
  },
  "recipientAttachment": null,
  "recipientCaptiveInfo": null,
  "recipientId": "1",
  "requireIdLookup": false,
  "roleName": "",
  "routingOrder": 1,
  "samlAuthentication": {
    "samlAssertionAttributes": [
      {
        "name": "string",
        "value": "string"
      },
      {
        "name": "string",
        "value": "string"
      }
    ]
  },
  "smsAuthentication": {
    "senderProvidedNumbers":[
      "sample string 1",
      "sample string 2"
    ]
  },
  "socialAuthentications": null,
  "templateAccessCodeRequired": false,
  "templateLocked": false,
  "templateRequired": false,
...
```

### Core Recipient Parameters

The following table contains the descriptions for the core properties for a recipient.

| Name | Required? | Schema Type | Description |
| --- | --- | --- | --- |
| email | Yes | Email | Email of the recipient. Notification will be sent to this email id. Maximum Length: 100 characters. |
| name | Yes | String | Full legal name of the recipient. Maximum Length: 100 characters. |
| accessCode | No | String | This optional element specifies the access code a recipient has to enter to validate the identity. Maximum Length: 50 characters. |
| addAccessCodeToEmail | No | Boolean | This optional attribute indicates that the access code is added to the email sent to the recipient; this nullifies the Security measure of Access Code on the recipient. |
| clientUserId | No | String | This specifies whether the recipient is embedded or remote.  If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to **true,** an error is generated on sending. |
| embeddedRecipientStartURL | No | String | This is a sender provided valid URL string for redirecting an embedded recipient. When using this option, the embedded recipient still receives an email from Docusign, just as a remote recipient would, but when the document link in the email is clicked the recipient is redirected, through Docusign, to this URL to complete their actions. When routing to the URL, it is up to the sender's system (the server responding to the URL) to then request a recipient token to launch a signing session.  If the value `SIGN_AT_DOCUSIGN` is used for this node, the recipient is directed to an embedded signing or viewing process directly at Docusign. The signing or viewing action is initiated by the Docusign system and the transaction activity and Certificate of Completion records will reflect this. In all other ways the process is identical to an embedded signing or viewing operation that would be launched by any partner.  It is important to remember that in a typical embedded workflow the authentication of an embedded recipient is the responsibility of the sending application and Docusign expects that senders will follow their own process for establishing the recipient's identity. In this workflow the recipient goes through the sending application before the embedded signing or viewing process in initiated. However, when the sending application sets the `EmbeddedRecipientStartURL` property to `SIGN_AT_DOCUSIGN`, the recipient goes directly to the embedded signing or viewing process bypassing the sending application and any authentication steps the sending application would use. In this case, Docusign recommends that one of the normal Docusign authentication features (Access Code, Phone Authentication, SMS Authentication, etc.) be used to verify the identity of the recipient.  If the `clientUserId` property is NOT set and the `embeddedRecipientStartURL` property is set, Docusign ignores the redirect URL and launch the standard signing process for the email recipient. Information can be appended to the `embeddedRecipientStartURL` property using merge fields. The available merge fields items are: templateId, recipientId, recipientName, recipientEmail, and customFields. The customFields must be part of the recipient or template. The merge fields are enclosed in double brackets.  *Example*: `http://senderHost/[[mergeField1]]/ beginSigningSession? [[mergeField2]]&[[mergeField3]]` |
| customFields | No | customField | An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the template status but otherwise not used by Docusign. String `customField` properties have a maximum length of 100 characters. |
| emailNotification | No | emailNotification | An optional complex type that has information for setting the language for the recipient's email information. It is composed of three elements:  *emailBody*: a string with the email message sent to the recipient. Maximum Length: 10000 characters.  *emailSubject*: a string with the subject of the email sent to the recipient. Maximum Length: 100 characters.  *supportedLanguage*: The simple type enumeration of the language used. The supported languages, with the language value shown in parenthesis, are: Arabic (ar), Bahasa Indonesia (id), Bahasa Melayu (ms) Bulgarian (bg), Czech (cs), Chinese Simplified (zh\_CN), Chinese Traditional (zh\_TW), Croatian (hr), Danish (da), Dutch (nl), English US (en), English UK (en\_GB), Estonian (et), Farsi (fa), Finnish (fi), French (fr), French Canada (fr\_CA), German (de), Greek (el), Hebrew (he), Hindi (hi), Hungarian (hu), Italian (it), Japanese (ja), Korean (ko), Latvian (lv), Lithuanian (lt), Norwegian (no), Polish (pl), Portuguese (pt), Portuguese Brazil (pt\_BR), Romanian (ro),Russian (ru), Serbian (sr), Slovak (sk), Slovenian (sl), Spanish (es),Spanish Latin America (es\_MX), Swedish (sv), Thai (th), Turkish (tr), Ukrainian (uk) and Vietnamese (vi).  **IMPORTANT:** If this is enabled for one recipient, it overrides the Template Subject and `EmailBlurb` property settings. Also, you must set the `emailNotification` property for all recipients. |
| excludedDocuments | No | Array of Strings | Specifies the documents that are not visible to this recipient. Document Visibility must be enabled for the account and the enforceSignerVisibility property must be set to true for the template to use this.  When the enforceSignerVisibility property is set to **true,** documents with tabs can only be viewed by signers that have a tab on that document. Recipients that have an administrative role (Agent, Editor, or Intermediaries) or informational role (Certified Deliveries or Carbon Copies) can always see all the documents in an template, unless they are specifically excluded using this setting when an template is sent. Documents that do not have tabs are always visible to all recipients, unless they are specifically excluded using this setting when an template is sent. |
| idCheckConfigurationName | No | String | Specifies authentication check by name. The names used here must be the same as the authentication type names used by the account (these name can also be found in the web console sending interface in the Identify list for a recipient). This overrides any default authentication setting.  *Example*:  Your account has ID Check and SMS Authentication available and in the web console Identify list these appear as 'ID Check $' and 'SMS Auth $'. To use ID check in an template, the `idCheckConfigurationName` property must be set to `ID Check $`. To use SMS, it must be set to `SMS Auth $` and you must add phone number information to the `smsAuthentication` node. |
| iDCheckInformationInput | No | IdCheckInformationInput | This complex element contains input information related to a recipient ID check. It can include the following information.  *addressInformationInput*: Used to set recipient address information and consists of:  *addressInformation*: consists of six elements, with street2 and zipPlus4 being optional. The elements are: address1, address2, city, state, zip, zipPlus4. The maximum number of characters in each element are: address1/address2 = 150 characters, city = 50 characters, state = 2 characters, and zip/zipPlus4 = 20 characters.  displayLevelCode: Specifies the display level for the recipient. Values are: ReadOnly, Editable, or DoNotDisplay.  *receiveInResponse*: A Boolean element that specifies if the information needs to be returned in the response.  *dobInformationInput*: Used to set recipient date of birth information and consists of:  *dateOfBirth*: Specifies the recipient's date, month and year of birth.  *displayLevelCode*: Specifies the display level for the recipient. Values are: ReadOnly, Editable, or DoNotDisplay.  *receiveInResponse*: A Boolean element that specifies if the information needs to be returned in the response.  *ssn4InformationInput*: Used to set the last four digits of the recipient's SSN information and consists of:  *ssn4*: Specifies the last four digits of the recipient's SSN.  *displayLevelCode*: Specifies the display level for the recipient. Values are: ReadOnly, Editable, or DoNotDisplay.  *receiveInResponse*: A Boolean element that specifies if the information needs to be returned in the response.  *ssn9InformationInput*: Used to set the recipient's SSN information. Note that the ssn9 information can never be returned in the response. The ssn9 input consists of:    *ssn9*: Specifies the recipient's SSN.  *displayLevelCode*: Specifies the display level for the recipient. Values are: ReadOnly, Editable, or DoNotDisplay. |
| inheritEmailNotificationConfiguration | No | Boolean | Optional element. If true and the template recipient creates a Docusign account after signing, the Manage Account Email Notification settings are used as the default settings for the recipient's account. |
| note | No | String | A note that is unique to this recipient. This note is sent to the recipient via the signing email. The note displays in the signing UI near the upper left corner of the document on the signing screen. Maximum Length: 1000 characters. |
| phoneAuthentication | No | RecipientPhoneAuthentication | Optional element. Contains the elements:    *recipMayProvideNumber*:Boolean. When **true** thenrecipient can use whatever phone number they choose to.   *senderProvidedNumbers*: ArrayOfString. A list of phone numbers the recipient can use.   *recordVoicePrint* - Reserved   *validateRecipProvidedNumber* - Reserved |
| recipientAttachment | No | Attachment | Reserved |
| recipientId | No | String | Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document. |
| requireIdLookup | No | Boolean | When **true,** the recipient is required to use the specified ID check method (including Phone and SMS authentication) to validate their identity. |
| roleName | No\* | String | Optional element. Specifies the role name associated with the recipient.  This is required when working with template recipients. |
| routingOrder | Yes | String | This element specifies the routing order of the recipient in the template. |
| samlAuthentication | No | samlAssertionAttributes | Optional element, account must be set up to use SSO to use this. Contains the name/value pair information for the SAML assertion attributes:  *name*: The name of the SAML assertion attribute.  *value*: The value associated with the named SAML assertion attribute. |
| smsAuthentication | No | senderProvidedNumbers | Optional element. Contains the element:  *senderProvidedNumbers*: Array that contains a list of phone numbers the recipient can use for SMS text authentication. |
| socialAuthentications | No | Boolean | Lists the social ID type that can be used for recipient authentication. |
| templateAccessCodeRequired | No | Boolean | Optional element. Used only when working with template recipients. When **true** and the `TemplateLocked` parameter is set to **true,** the sender must enter an access code. |
| templateLocked | No | Boolean | Optional element. Used only when working with template recipients. When **true,** the sender cannot change any attributes of the recipient. |
| templateRequired | No | Boolean | Optional element. Used only when working with template recipients. When **true,** the sender may not remove the recipient. |

## Agents Recipient

This recipient can add name and email information for recipients that appear after the recipient in routing order.

#### Example Agents layout

```
"agents": [{
 <core parameters>
  "canEditRecipientEmails": false,
  "canEditRecipientNames": false
}],
```

The additional parameters for Agents recipient are shown below:

| Name | Required? | Schema Type | Description |
| --- | --- | --- | --- |
| canEditRecipientEmails | No | Boolean | Optional element. When **true,** the Agents Recipient associated with this Recipient can change the Recipient's pre-populated Email address. This element is only active if enabled for the account. |
| canEditRecipientNames | No | Boolean | Optional element. When **true,** the Agents Recipient associated with this recipient can change the recipient's pre-populated name (`UserName`). This element is only active if enabled for the account. |

## Carbon Copies Recipient

Use this type if the recipient should get a copy of the template, but the recipient does not need to sign, initial, date, or add information to any of the documents. This type of recipient can be placed in any order in the recipient list. The recipient receives a copy of the template when the template reaches the recipient's order in the process flow and when the template is completed.

#### Example Carbon Copies layout

```
"carbonCopies": [{
 <core parameters>
```

The Carbon Copies recipient uses only the core parameters.

## Certified Deliveries Recipient

Use this action if the recipient must receive the completed documents for the template to be completed, but the recipient does not need to sign, initial, date, or add information to any of the documents.

#### Example Certified Deliveries layout

```
"certifiedDeliveries": [{
<core parameters>
}],
```

The Certified Deliveries recipient uses only the core parameters.

## Editors Recipient

This recipient has the same management and access rights for the template as the sender and can make changes to the template as if they were using the Advanced Correct feature. This recipient can add name and email information, add or change the routing order and set authentication options for the remaining recipients. Additionally, this recipient can edit signature/initial tabs and data fields for the remaining recipients. The recipient must have a Docusign account to be an editor.

#### Example Editors layout

```
"editors": [{
 <core parameters>
  "canEditRecipientEmails": false,
  "canEditRecipientNames": false
}],
```

The additional parameters for Editors recipient are shown below:

| Name | Required? | Schema Type | Description |
| --- | --- | --- | --- |
| canEditRecipientEmails | No | Boolean | Optional element. When **true,** the Editors Recipient associated with this Recipient can change the Recipient's pre-populated Email address. This element is only active if enabled for the account. |
| canEditRecipientNames | No | Boolean | Optional element. When **true,** the Editors Recipient associated with this recipient can change the recipient's pre-populated name (`UserName`). This element is only active if enabled for the account. |

## In Person Signers Recipient

Use this type if the signer is in the same physical location as a Docusign user who will act as a Signing Host for the transaction. The recipient added is the Signing Host and new separate Signer Name field appears after Sign in person is selected.

#### Example In Person Signers layout

```
"inPersonSigners": [{
  "hostEmail": "signing.host@company.com",
  "hostName": "Mike Host",
 <core parameters>
  "autoNavigation": false,
  "defaultRecipient": false,
  "signInEachLocation": false,
  "signatureInfo": null,
  "signerEmail": "signer.name@company.com",
  "signerName": "MC Clap Your Hands",
  "tabs": {
    "approveTabs": null,
    "checkboxTabs": null,
    "companyTabs": null,
    "dateSignedTabs": null,
    "dateTabs": null,
    "declineTabs": null,
    "emailTabs": null,
    "templateIdTabs": null,
    "fullNameTabs": null,
    "initialHereTabs": null,
    "listTabs": null,
    "noteTabs": null,
    "numberTabs": null,
    "radioGroupTabs": null,
    "signHereTabs": [{
    "signerAttachmentTabs": null,
    "ssnTabs": null,
    "textTabs": null,
    "titleTabs": null,
    "zipTabs": null
  }
}],
```

The additional and changed parameters for In Person Signers recipient are shown below:

| Name | Required? | Schema Type | Description |
| --- | --- | --- | --- |
| hostEmail | Yes | Email | Required element for In Person Signers recipient Type. Maximum Length: 100 characters.  Specifies the email for the signing host. |
| hostName | Yes | String | Required element for In Person Signers recipient Type. Maximum Length: 100 characters.  Specifies the email for the signing host. |
| autoNavigation | No | Boolean | Specifies whether auto navigation is set for the recipient. |
| defaultRecipient | No | Boolean | When **true,** this is the default recipient for the template. This option is used with the CreateTemplateFromTemplatesAndForms method. |
| signInEachLocation | No | Boolean | When **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab (instead of adopting a signature/initial style or only drawing a signature/initial once). |
| signatureInfo | No | String | Optional element only used with recipient types In Person Signers and Signers.  Allows the sender to pre-specify the signature name, signature initials, and signature font used in the signature stamp for the recipient. |
| signerEmail | No | String | Optional element. The email address for an InPersonSigner recipient Type. Maximum Length: 100 characters. |
| signerName | Yes | String | Required element with recipient type In Person Signers. Maximum Length: 100 characters.  The full legal name of a signer for the template. |
| tabs | No | Tab | Optional element only used with recipient types In Person Signers and Signers.  Specifies the Tabs associated with the recipient. See the See the [EnvelopeRecipientTabs resource](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/) for more information about tabs. for more information about tabs. |

## Intermediaries Recipient

This recipient can, but is not required to, add name and email information for recipients at the same or subsequent level in the routing order (until subsequent Agents, Editors or Intermediaries recipient types are added).

#### Example Intermediaries layout

```
"intermediaries": [{
<core parameters>
  "canEditRecipientEmails": false,
  "canEditRecipientNames": false
}],
```

The parameters for Intermediaries recipient are shown below:

| Name | Required? | Schema Type | Description |
| --- | --- | --- | --- |
| canEditRecipientEmails | No | Boolean | Optional element. When **true,** the Agents Recipient associated with this Recipient can change the Recipient's pre-populated Email address. This element is only active if enabled for the account. |
| canEditRecipientNames | No | Boolean | Optional element. When **true,** the Agents Recipient associated with this recipient can change the recipient's pre-populated name (`UserName`). This element is only active if enabled for the account. |

## Signers Recipient

Use this action if your recipient must sign, initial, date, or add data to form fields on the documents in the template.

#### Example Signers layout

```
"Signers": [{
<core parameters>
  "autoNavigation": false,
  "defaultRecipient": false,
  "signInEachLocation": false,
  "signatureInfo": null,
  "tabs": {
    "approveTabs": null,
    "checkboxTabs": null,
    "companyTabs": null,
    "dateSignedTabs": null,
    "dateTabs": null,
    "declineTabs": null,
    "emailTabs": null,
    "templateIdTabs": null,
    "fullNameTabs": null,
    "initialHereTabs": null,
    "listTabs": null,
    "noteTabs": null,
    "numberTabs": null,
    "radioGroupTabs": null,
    "signHereTabs": [{
    "signerAttachmentTabs": null,
    "ssnTabs": null,
    "textTabs": null,
    "titleTabs": null,
    "zipTabs": null
  }
  "deliveryMethod":"",
  "deliveredDateTime":"String Content",
  "signedDateTime":"String Content",
  "offlineAttributes":{
    "deviceName":"String Content",
    "deviceModel":"String Content",
    "gpsLatitude":"String Content",
    "gpsLongitude":"String Content",
    "accountEsignId":"String Content"
  }
}],
```

The additional parameters for Signers recipient are shown below:

| Name | Required? | Schema Type | Description |
| --- | --- | --- | --- |
| autoNavigation | No | Boolean | Specifies whether auto navigation is set for the recipient. |
| defaultRecipient | No | Boolean | When **true,** this is the default recipient for the template. This option is used with the CreateTemplateFromTemplatesAndForms method. |
| signInEachLocation | No | Boolean | When **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab (instead of adopting a signature/initial style or only drawing a signature/initial once). |
| signatureInfo | No | String | Optional element only used with recipient types In Person Signers and Signers.  Allows the sender to pre-specify the signature name, signature initials, and signature font used in the signature stamp for the recipient. |
| signerEmail | No | String | Optional element. The email address for an InPersonSigner recipient Type. Maximum Length: 100 characters. |
| signerName | Yes | String | Required element with recipient type In Person Signers. Maximum Length: 100 characters.  The full legal name of a signer for the template. |
| tabs | No | Tab | Optional element only used with recipient types In Person Signers and Signers.  Specifies the Tabs associated with the recipient. See the See the [EnvelopeRecipientTabs resource](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/) for more information about tabs. section for more information about tabs. |
| deliveryMethod | No | String | Reserved: For Docusign use only. |
| deliveredDateTime | No | DateTime | Reserved: For Docusign use only. |
| signedDateTime | No | DateTime | Reserved: For Docusign use only. |
| offlineAttributes | No |  | Reserved: For Docusign use only. |

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients ```  Adds tabs for a recipient. |
| [createTemplateRecipientPreview](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/createtemplaterecipientpreview/) | POST  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/views/recipient_preview ```  Creates a template recipient preview. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/delete/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients/{recipientId} ```  Deletes the specified recipient file from a template. |
| [deleteList](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/deletelist/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients ```  Deletes recipients from a template. |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/list/) | GET  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients ```  Gets recipient information from a template. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/templates/{templateId}/recipients ```  Updates recipients in a template. |

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
