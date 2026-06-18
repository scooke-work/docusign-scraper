---
title: EnvelopeRecipients Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Envelopes
- Envelopes
- Enveloperecipients
scraped_at: '2026-06-18T21:10:00Z'
---

# EnvelopeRecipients Resource

The EnvelopeRecipients resource enables you manage the recipients of an envelope.
All recipient types share a set of [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters),
but some recipient types have additional parameters.
You specify the recipient type using the `recipientType` parameter. The recipient types are as follows:

| Recipient type | Description |
| --- | --- |
| [Agent](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#agent-recipient) | Agent recipients can add name and email information for recipients that appear after the agent in routing order. |
| [Carbon Copy](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#carbon-copy-recipient) | Carbon copy recipients get a copy of the envelope but don't need to sign, initial, date, or add information to any of the documents. This type of recipient can be used in any routing order. Carbon copy recipients receive their copy of the envelope when the envelope reaches the recipient's order in the process flow and when the envelope is completed. |
| [Certified Delivery](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#certified-delivery-recipient) | Certified delivery recipients must receive the completed documents for the envelope to be completed. However, they don't need to sign, initial, date, or add information to any of the documents. |
| [Editor](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#editor-recipient) | Editors have the same management and access rights for the envelope as the sender. They can make changes to the envelope as if they were using the Advanced Correct feature. This recipient can add name and email information, add or change the routing order, set authentication options, and can edit signature/initial tabs and data fields for the remaining recipients. The recipient must have a Docusign account to be an editor. |
| [In-Person Signer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#in-person-signer-recipient) | In-person signer recipients are Docusign users who act as signing hosts in the same physical location as the signer. |
| [Intermediary](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#intermediary-recipient) | Intermediaries are recipients who can, but are not required to, add name and email information for recipients at the same or subsequent level in the routing order, unless subsequent agents, editors, or intermediaries are added. |
| [Seal](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#seal-recipient) | Electronic seal recipients represent legal entities rather than individuals. Organizations and governments can use electronic seals to show evidence of origin and integrity of documents. |
| [Signer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#signer-recipient) | Signers are recipients who must sign, initial, date, or add data to form fields on the documents in the envelope. |
| [Witness](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#witness-recipient) | Witnesses are recipients whose signatures affirm that the identified signers have signed the documents in the envelope. |

Not all recipients are are available to all account types.
Review your account plan to determine which recipient types are available to you.
All recipient types are available in the development environment.

## Core Recipient Parameters

All recipients, regardless of type, have the same common core parameters.
The following table contains the descriptions for the core properties for all recipient types:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| email | Yes | Email | Email of the recipient. Notification will be sent to this email id. Maximum Length: 100 characters. |
| name | Yes | String | Full legal name of the recipient. Maximum Length: 100 characters.  **Note:** If you are creating an envelope with Docusign EU advanced signature enabled, ensure that recipient names do not contain any of the following characters: **^ : \ @ , + <** |
| accessCode | No | String | This optional element specifies the access code a recipient has to enter to validate the identity. Maximum Length: 50 characters. |
| addAccessCodeToEmail | No | Boolean | This optional attribute indicates that the access code is added to the email sent to the recipient; this nullifies the Security measure of Access Code on the recipient. |
| agentCanEditEmail | No | Boolean | When **true,** the agent recipient associated with this recipient can change the recipient's pre-populated email address. This element is only active if enabled for the account. |
| agentCanEditName | No | Boolean | When **true,** the agent recipient associated with this recipient can change the recipient's pre-populated name (`UserName`). This element is only active if enabled for the account. |
| clientUserId | No | String | This specifies whether the recipient is embedded or remote.  If the `clientUserId` property is not null then the recipient is embedded. Note that if the `ClientUserId` property is set and either `SignerMustHaveAccount` or `SignerMustLoginToSign` property of the account settings is set to **true,** an error is generated on sending. Maximum length: 100 characters. |
| embeddedRecipientStartURL | No | String | This is a sender provided valid URL string for redirecting an embedded recipient. When using this option, the embedded recipient still receives an email from Docusign, just as a remote recipient would, but when the document link in the email is clicked the recipient is redirected, through Docusign, to this URL to complete their actions. When routing to the URL, it is up to the sender's system (the server responding to the URL) to then request a recipient token to launch a signing session.  If the value `SIGN_AT_DOCUSIGN` is used for this node, the recipient is directed to an embedded signing or viewing process directly at Docusign. The signing or viewing action is initiated by the Docusign system and the transaction activity and Certificate of Completion records will reflect this. In all other ways the process is identical to an embedded signing or viewing operation that would be launched by any partner.  It is important to remember that in a typical embedded workflow the authentication of an embedded recipient is the responsibility of the sending application and Docusign expects that senders will follow their own process for establishing the recipient's identity. In this workflow the recipient goes through the sending application before the embedded signing or viewing process in initiated. However, when the sending application sets the `EmbeddedRecipientStartURL` property to `SIGN_AT_DOCUSIGN`, the recipient goes directly to the embedded signing or viewing process bypassing the sending application and any authentication steps the sending application would use. In this case, Docusign recommends that one of the normal Docusign authentication features (Access Code, Phone Authentication, SMS Authentication, etc.) be used to verify the identity of the recipient.  If the `clientUserId` property is NOT set and the `embeddedRecipientStartURL` property is set, Docusign ignores the redirect URL and launch the standard signing process for the email recipient. Information can be appended to the `embeddedRecipientStartURL` property using merge fields. The available merge fields items are: envelopeId, recipientId, recipientName, recipientEmail, and customFields. The customFields must be part of the recipient or envelope. The merge fields are enclosed in double brackets.  *Example*: `http://senderHost/[[mergeField1]]/ beginSigningSession? [[mergeField2]]&[[mergeField3]]` |
| customFields | No | customField | An optional array of strings that allows the sender to provide custom data about the recipient. This information is returned in the envelope status but otherwise not used by Docusign. String `customField` properties have a maximum length of 100 characters. |
| emailNotification | No | emailNotification | An optional property that has information for setting the language for the recipient's email information. It is composed of three elements:  *emailBody*: a string with the email message sent to the recipient. Maximum Length: 10000 characters.  *emailSubject*: a string with the subject of the email sent to the recipient. Maximum Length: 100 characters.  *supportedLanguage*: The simple type enumeration (two-letter code) for the language to use for the standard email format and the signing view for the recipient. To retrieve the possible values, use the [Accounts::listSupportedLanguages method](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/accounts/listsupportedlanguages/).  **Note:** You can set the `emailNotification` property separately for each recipient. If you set the value only for certain recipients, the other recipients will inherit the this value from the top-level `emailSubject` and `emailBlurb`. |
| excludedDocuments | No | Array of Strings | Specifies the documents that are not visible to this recipient. Document Visibility must be enabled for the account and the enforceSignerVisibility property must be set to true for the envelope to use this.  When the enforceSignerVisibility property is set to **true,** documents with tabs can only be viewed by signers that have a tab on that document. Recipients that have an administrative role (Agent, Editor, or Intermediaries) or informational role (Certified Deliveries or Carbon Copies) can always see all the documents in an envelope, unless they are specifically excluded using this setting when an envelope is sent. Documents that do not have tabs are always visible to all recipients, unless they are specifically excluded using this setting when an envelope is sent. |
| idCheckConfigurationName | No | String | Specifies authentication check by name. The names used here must be the same as the authentication type names used by the account (these name can also be found in the web console sending interface in the Identify list for a recipient). This overrides any default authentication setting.  *Example*:  Your account has ID Check and SMS Authentication available and in the web console Identify list these appear as 'ID Check $' and 'SMS Auth $'. To use ID check in an envelope, the `idCheckConfigurationName` property must be set to `ID Check $`. To use SMS, it must be set to `SMS Auth $` and you must add phone number information to the `smsAuthentication` node. |
| iDCheckInformationInput | No | IdCheckInformationInput | This complex element contains input information related to a recipient ID check. It can include the following information.  *addressInformationInput*: Used to set recipient address information and consists of:  *addressInformation*: consists of six elements, with address2 and postalCodePlus4 being optional. The elements are: address1, address2, city, stateOrProvince, postalCode, postalCodePlus4. The maximum number of characters in each element are: address1/address2 = 150 characters, city = 50 characters, stateOrProvince = 2 characters, and postalCode/postalCodePlus4 = 20 characters.  displayLevelCode: Specifies the display level for the recipient. Values are: ReadOnly, Editable, or DoNotDisplay.  *receiveInResponse*: A Boolean element that specifies if the information needs to be returned in the response.  *dobInformationInput*: Used to set recipient date of birth information and consists of:  *dateOfBirth*: Specifies the recipient's date, month and year of birth.  *displayLevelCode*: Specifies the display level for the recipient. Values are: ReadOnly, Editable, or DoNotDisplay.  *receiveInResponse*: A Boolean element that specifies if the information needs to be returned in the response.  *ssn4InformationInput*: Used to set the last four digits of the recipient's SSN information and consists of:  *ssn4*: Specifies the last four digits of the recipient's SSN.  *displayLevelCode*: Specifies the display level for the recipient. Values are: ReadOnly, Editable, or DoNotDisplay.  *receiveInResponse*: A Boolean element that specifies if the information needs to be returned in the response.  *ssn9InformationInput*: Used to set the recipient's SSN information. Note that the ssn9 information can never be returned in the response. The ssn9 input consists of:    *ssn9*: Specifies the recipient's SSN.  *displayLevelCode*: Specifies the display level for the recipient. Values are: ReadOnly, Editable, or DoNotDisplay. |
| inheritEmailNotificationConfiguration | No | Boolean | Optional element. If true and the envelope recipient creates a Docusign account after signing, the Manage Account Email Notification settings are used as the default settings for the recipient's account. |
| note | No | String | A note that is unique to this recipient. This note is sent to the recipient via the signing email. The note displays in the signing UI near the upper left corner of the document on the signing screen. Maximum Length: 1000 characters. |
| phoneAuthentication | No | RecipientPhoneAuthentication | Optional element. Contains the elements:    *recipMayProvideNumber*:Boolean. When **true** thenrecipient can use whatever phone number they choose to.   *senderProvidedNumbers*: ArrayOfString. A list of phone numbers the recipient can use. |
| recipientId | No | String  The string must be formatted as an integer or a GUID. | Unique for the recipient. It is used by the tab element to indicate which recipient is to sign the Document. |
| requireIdLookup | No | Boolean | When **true,** the recipient is required to use the specified ID check method (including Phone and SMS authentication) to validate their identity. |
| roleName | No\* | String | Optional element. Specifies the role name associated with the recipient.  This is required when working with template recipients. |
| routingOrder | Yes | String | This element specifies the routing order of the recipient in the envelope. |
| smsAuthentication | No | senderProvidedNumbers | Optional. Contains the element:  *senderProvidedNumbers*: Array that contains a list of phone numbers the recipient can use for SMS text authentication. |
| templateAccessCodeRequired | No | Boolean | Optional. Used only when working with template recipients. When **true** and the `TemplateLocked` parameter is set to **true,** the sender must enter an access code. |
| templateLocked | No | Boolean | Optional. Used only when working with template recipients. When **true,** the sender cannot change any attributes of the recipient. |
| templateRequired | No | Boolean | Optional. Used only when working with template recipients. When **true,** the sender may not remove the recipient. |
| identityVerification | No | identityVerification | Optional. Specifies ID Verification applied on an envelope by workflow ID.  See the [list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/identityverifications/list/) method in the [IdentityVerifications](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/identityverifications/) resource for more information on how to retrieve workflow IDs available for an account.  This can be used in addition to other [recipient authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/) methods.  Note that ID Verification and ID Check are two distinct methods. ID Verification checks recipients' identity by verifying their ID while ID Check relies on data available on public records (such as current and former address). |

## Agent Recipient

An agent recipient can add name and email information for recipients that appear after the agent in routing order.

In addition to the [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters), this recipient type has the following parameters:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| documentVisibility | No | documentVisibility | A complex type that specifies which documents are visible to this recipient. |

## Carbon Copy Recipient

Carbon copy recipients receive a copy of the envelope but don't need to sign, initial,
date or add information to any of the documents. You can place this type of recipient in any routing order.
Carbon copy recipients receive their copy of the envelope when the envelope
reaches the recipient's order in the process flow and when the envelope is completed.

In addition to the [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters), this recipient type has the following parameters:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| documentVisibility | No | documentVisibility | A complex type that specifies which documents are visible to this recipient. |

## Certified Delivery Recipient

Certified delivery recipients must receive the completed documents for the envelope to be completed. However, they don't need to sign, initial, date or add information to any of the documents.

In addition to the [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters), this recipient type has the following parameters:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| documentVisibility | No | documentVisibility | A complex type that specifies which documents are visible to this recipient. |

## Editor Recipient

Editors have the same management and access rights for the envelope as the sender.
They can make changes to the envelope as if they were using the Advanced Correct feature.
This recipient can add name and email information,
add or change the routing order and set authentication options for the remaining recipients.
Additionally, this recipient can edit signature/initial tabs and data fields for the remaining recipients.
The recipient must have a Docusign account to be an editor.

In addition to the [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters), this recipient type has the following parameters:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| documentVisibility | No | documentVisibility | A complex type that specifies which documents are visible to this recipient. |

## In-Person Signer Recipient

An in-person recipient is a Docusign user, acting as a Signing Host, who is in the same physical location as the signer.

The following restrictions apply to using electronic notary when sending documents:

- Authentication methods are allowed for the signer but not the notary.
- The Sign On Paper, Document Markup, Field Markup and Change Signer options cannot be used for the documents.
- Tabs may be assigned to the signer, but cannot be assigned to the notary.

See [eNotary Resources](https://support.docusign.com/s/document-item?bundleId=gko1642535666104&topicId=jiv1635359045452.html) in the Docusign Support Center for more information about how the eNotary feature works.

In addition to the [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters), this type adds the following parameters:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| inPersonSigningType | No | String | Specifies whether the envelope uses the eNotary feature. The accepted values are:  - `inPersonSigner` The envelope uses the normal in-person signing flow. - `notary`: The envelope uses the eNotary signing flow. |
| notaryHost | Yes, when `inPersonSigningType` is `notary` | NotaryHost | Sets the information for the notary host for the notary in person signing flow. The following information is required:  - `recipientId`: A unique ID (an integer or a GUID) for the notary signing host. - `name`: Specifies the notary's full legal name. - `email`: Specifies the notary's email address. |
| autoNavigation | No | Boolean | Specifies whether auto navigation is set for the recipient. |
| defaultRecipient | No | Boolean | When **true,** this is the default recipient for the envelope. This option is used when creating an envelope from a template. |
| documentVisibility | No | documentVisibility | A complex type that specifies which documents are visible to this recipient. |
| hostName | Yes, when `inPersonSigningType` is `inPersonSigner` | String | The name of the signing host. This is the Docusign user that is hosting the in-person signing session. |
| hostEmail | Yes, when `inPersonSigningType` is `inPersonSigner` | String | The email address of the signing host. This is the Docusign user that is hosting the in-person signing session. |
| signerName | Yes, when `inPersonSigningType` is `inPersonSigner` | String | The in-person signer's full legal name. |
| Name | Yes, when `inPersonSigningType` is `notary` | String | The full legal name of the signer in an eNotary flow. |
| email | Yes, when `inPersonSigningType` is `notary` | String | The signer's email address in an eNotary flow. |
| recipientSuppliesTabs | No | Boolean | Indicates whether the recipient supplies tabs in the document. |
| signatureInfo | No | Object | Optional element only used with the recipient types In Person Signers, Signers, and Witnesses. Includes properties that enable the sender to pre-specify the signature name, signature initials, and signature font used in the signature stamp for the recipient. |
| signInEachLocation | No | Boolean | When **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab (instead of adopting a signature/initial style or only drawing a signature/initial once). |
| tabs | No | Tab | Optional element only used with recipient types In Person Signers and Signers.  Specifies the Tabs associated with the recipient. See the [EnvelopeRecipientTabs resource](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/) for more information about tabs. |

## Intermediary Recipient

An intermediary is a recipient who can, but is not required to,
add name and email information for recipients
at the same or subsequent level in the routing order,
unless subsequent agents, editors or intermediaries are added.

In addition to the [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters), this recipient type has the following parameters:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| documentVisibility | No | documentVisibility | A complex type that specifies which documents are visible to this recipient. |

## Seal Recipient

An electronic seal recipient is a legal entity rather than an actual person.
Electronic Seals can be used by organizations and governments to show evidence
of origin and integrity of documents.
Even though electronic seals can be represented by a tab in a document,
they do not require user interaction and apply automatically in the order specified by the sender.
The sender is therefore the person authorizing usage of the electronic seal in the flow.

Electronic seal recipients rely on a subset of core properties, described as follows, plus the `recipientSignatureProviders` parameter:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| recipientId | Yes | String  The string must be formatted as an integer or a GUID. | Indicates the unique ID of the applied electronic seal. |
| routingOrder | No (default: 1) | String | Specifies the routing order of the electronic seal in the envelope.  The routing order assigned to your electronic seal cannot be shared with another recipient. It is recommended that you set a routing order for your electronic seals.. |
| recipientSignatureProviders | Yes | String | Indicates which electronic seal to apply on documents when creating an envelope. |

By default, Electronic Seals apply to all documents in an envelope.
However, the `sealDocumentsWithTabsOnly` property (see `recipientSignatureProvider`)
allows you to seal only documents that have `signHere` tabs set for the Electronic Seal recipients.

## Signer Recipient

A signer is a recipient who must sign, initial, date, or add data to form fields on the documents in the envelope.

In addition to the [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters), this recipient type adds the following parameters:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| autoNavigation | No | Boolean | Specifies whether auto navigation is set for the recipient. |
| defaultRecipient | No | Boolean | When **true,** this is the default recipient for the envelope. This option is used when creating an envelope from a template. |
| documentVisibility | No | documentVisibility | A complex type that specifies which documents are visible to this recipient. |
| isBulkRecipient | No | Boolean | Indicates whether the recipient is a bulk send recipient or not. |
| recipientSuppliesTabs | No | Boolean | Indicates whether the recipient supplies tabs in the document. |
| signInEachLocation | No | Boolean | When **true** and the feature is enabled in the sender's account, the signing recipient is required to draw signatures and initials at each signature/initial tab (instead of adopting a signature/initial style or only drawing a signature/initial once). |
| signatureInfo | No | String | Optional element only used with recipient types In Person Signers, Signers, and Witnesses. Includes properties that enable the sender to pre-specify the signature name, signature initials, and signature font used in the signature stamp for the recipient. |
| signerEmail | No | String | Optional element. The email address for an In-Person Signer recipient Type. Maximum Length: 100 characters. |
| signerName | Yes | String | Required element with recipient type In Person Signers. Maximum Length: 100 characters.  The full legal name of a signer for the envelope. |
| tabs | No | Tab | Optional element only used with recipient types In Person Signers and Signers.  Specifies the Tabs associated with the recipient. See the [EnvelopeRecipientTabs resource](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/) for more information about tabs. |

## Witness Recipient

A witness is a recipient whose signature affirms that the identified signers have signed the documents in the envelope.

In addition to the [core parameters](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/#core-recipient-parameters), this recipient type adds the following parameters:

| Name | Required | Schema Type | Description |
| --- | --- | --- | --- |
| autoNavigation | No | Boolean | Specifies whether auto navigation is set for the recipient. |
| defaultRecipient | No | Boolean | When **true,** this is the default recipient for the envelope. This option is used when creating an envelope from a template. |
| documentVisibility | No | documentVisibility | A complex type that specifies which documents are visible to this recipient. |
| isBulkRecipient | No | Boolean | Indicates whether the recipient is a bulk send recipient or not. |
| recipientSignatureProviders | Yes | String | Indicates which electronic seal to apply on documents when creating an envelope. |
| recipientSuppliesTabs | No | Boolean | Indicates whether the recipient supplies tabs in the document. |
| recipientType | Yes | String | Indicates the recipient type. |
| requireSignerCertificate | No | Boolean | Indicates whether the envelope requires a signer certificate for this recipient. |
| requireSignOnPaper | No | Boolean | Specifies whether the signer must print, sign, and upload or fax the signed documents to Docusign. |
| signatureInfo | No | Object | Optional element only used with recipient types In Person Signers, Signers, and Witnesses. Includes properties that enable the sender to pre-specify the signature name, signature initials, and signature font used in the signature stamp for the recipient. |
| signInEachLocation | No | Boolean | When **true** and the feature is enabled in the sender's account, specifies that the signing recipient is required to sign and initial at each signature/initial tab (instead of once). |
| signingGroupId | No | String | The ID of the [signing group](https://support.docusign.com/s/document-item?bundleId=gav1643676262430&topicId=zgn1578456447934.html). |
| signingGroupName | No | String | The display name for the signing group. Maximum Length: 100 characters. |
| signingGroupUsers | No | userInfo | A complex type that contains information about the users in the signing group. |
| witnessFor | Yes | String | Indicates the person or party for whom the recipient is a witness. |
| witnessForGuid | Yes | String | GUID identifying the person or party for whom the recipient is a witness. |

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients ```  Adds one or more recipients to an envelope. |
| [createEnvelopeRecipientPreview](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/createenveloperecipientpreview/) | POST  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient_preview ```  Creates an envelope recipient preview. |
| [createRecipientManualReviewView](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/createrecipientmanualreviewview/) | POST  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/views/identity_manual_review ```  Create the link to the page for manually reviewing IDs. |
| [createRecipientProofFileResourceToken](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/createrecipientprooffileresourcetoken/) | POST  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId}/identity_proof_token ```  Creates a resource token for a sender to request ID Evidence data. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/delete/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients/{recipientId} ```  Deletes a recipient from an envelope. |
| [deleteList](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/deletelist/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients ```  Deletes recipients from an envelope. |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/list/) | GET  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients ```  Gets the status of recipients for an envelope. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/recipients ```  Updates recipients in a draft envelope or corrects recipient information for an in-process envelope. |

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
