---
title: Recipient authentication
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Recipients
- Recipients
- Authentication
scraped_at: '2026-06-18T21:09:56Z'
---

# Recipient authentication

You can use *recipient authentication* to verify a recipient’s identity and help ensure that they are who they claim to be. Docusign provides several optional methods for recipient authentication for both the eSignature API and Docusign SDKs:

- [Access code authentication](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/ /docs/esign-rest-api/esign101/concepts/recipients/auth/#access-code-authentication)
- [Phone authentication (call or SMS)](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/#phone-authentication-call-or-sms)
- [Knowledge-based authentication (KBA)](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/ /docs/esign-rest-api/esign101/concepts/recipients/auth/#knowledge-based-authentication-kba)
- [ID verification (IDV)](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/#id-verification-idv)

You can also [include a record of your recipient authentication method](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/auth/#create-a-record-of-recipient-authentication-after-embedded-signing) in your certificate of completion after [embedded signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/).

Recipient authentication is also called *multi-factor authentication* because it enables you to enforce more than one authentication method. For example, making a signature request via email would be one authentication factor, but making a signature request via email that also requires ID verification would be two authentication factors.

It is your responsibility as an envelope sender to determine which recipient authentication methods are needed to secure your documents, but keep in mind that enforcing many authentication methods can make signing documents cumbersome for your recipients. Your integrations should consider what is appropriate for the document(s) being signed. For example, if your recipients are simply acknowledging and signing a license agreement, it may not be necessary to enforce KBA authentication.

All recipient authentication methods except ID verification are enabled in the developer (demo) environment for you to test and develop with, but you may incur an additional charge in the Docusign production environment. Check your Docusign plan or contact your account manager to determine if there are any additional costs in production.

Docusign supports authentication and signing workflows that enable customers to meet the requirements of the Food and Drug Administration (FDA) 21 CFR Part 11 regulation. See [CFR Part 11 accounts](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/cfr-part-11-accounts/) for more information.

## Access code authentication

An access code is an alphanumeric phrase that you can set on an envelope before it is sent to recipients. Each recipient is prompted to enter the access code before they are able to open the documents contained in the envelope. Access code requirements are customizable in the [Security Settings page](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=yuz1583277329300.html) in eSignature Admin.

See [How to require access code authentication for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/require-access-code-recipient/) for details on how to implement access code authentication.

## Phone authentication (call or SMS)

Phone authentication requires the recipient to verify access to their phone number by receiving a call or a text message giving them an authentication code that they must enter to gain access to the documents contained in the envelope. Recipients may choose whether to receive the authentication code via call or via text.

Phone authentication may not be enabled for some older developer accounts. If you cannot choose to use phone authentication for your account, [contact support](https://support.docusign.com/s/contactSupport) to request access.

When using phone authentication or a customized identity verification configuration that is based on phone authentication, you must also provide the corresponding workflow ID value along with the API call to authenticate with the identity provider. You can obtain the full list of your workflow IDs using the [IdentityVerifications:list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/identityverifications/list/) endpoint.

See [How to require phone authentication for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/phone-auth/) for details on how to implement phone authentication and specify your workflow ID.

Using SMS authentication may incur additional costs due to sending additional SMS messages.

## Knowledge-based authentication (KBA)

Knowledge-based authentication requires recipients to answer detailed questions about themselves, based on data available in public records (such as their current and former addresses). The Docusign eSignature KBA feature uses an identity verification service from LexisNexis Risk Solutions that validates user identities in real time.

See [How to require knowledge-based authentication (KBA) for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/knowledge-based-authentication/) for details on how to implement KBA authentication.

## ID verification (IDV)

eSignature REST API 2.1 only

[ID verification](https://developers.docusign.com/docs/esign-rest-api/how-to/id-verification/) is a recipient authentication technology that verifies the identity of recipients based on government photo IDs (such as a driver’s license or passport) and electronic IDs. IDV verifies authenticity via visible security features, watermarks, and machine-readable barcodes. The best way to understand how this works is to view this video:

ID verification is available to develop API integrations in developer (demo) accounts, but is not enabled by default. To enable IDV in your developer and/or production accounts, contact your Docusign Account Manager or Partner Account Manager.

After IDV is enabled on your account (either developer or production), it is configured as a workflow on the account. Each account that has IDV enabled is automatically assigned a unique workflow ID, which needs to be supplied along with the API call to authenticate with the identity provider. You can obtain the full list of your workflow IDs using the [IdentityVerifications:list](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/identityverifications/list/) endpoint.

See [How to require ID verification (IDV) for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/id-verification/), for details on how to implement IDV, including retrieving a workflow ID for your account and specifying your workflow ID. You can also review the [IdentityVerifications](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/identityverifications/) resource.

## Create a record of recipient authentication after embedded signing

You can use the `authenticationMethod` parameter of an [EnvelopeViews:createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) method call to record the type of recipient authentication that you used in an [embedded signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/) scenario.

When you set the `authenticationMethod` parameter, you are saying that your app has already authenticated the recipient in the specified manner. After embedded signing has concluded, your certificate of completion will record the specified recipient authentication type.

- In embedded signing, your app should have already authenticated the signer using out-of-band methods (although in-Docusign methods can be added as well).
- The `authenticationInstant`, `assertionId`, and `securityDomain` [EnvelopeViews:createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) parameters are optional. You can use them to record security details about the embedded signing agreement in the certificate of completion, enabling you to relate them back to your internal records to prove validity and non-repudiation.

For example, if you authenticate your recipient’s identity based on their driver’s license ID, you could choose an `authenticationMethod` parameter value of `PaperDocuments`. After signing is completed, the certificate of completion would show that the signer was authenticated using their physical paper ID documents. In this example, the `assertionId` and `authenticationInstant` parameters could be used to reference a record in your systems that provides additional evidence.

You can use the following `authenticationMethod` values:

- Biometric
- Email
- HTTPBasicAuth
- Kerberos
- KnowledgeBasedAuth
- None
- PaperDocuments
- Password
- RSASecureID
- SingleSignOn\_CASiteminder
- SingleSignOn\_InfoCard
- SingleSignOn\_MicrosoftActiveDirectory
- SingleSignOn\_Other
- SingleSignOn\_Passport
- SingleSignOn\_SAML
- Smartcard
- SSLMutualAuth
- X509Certificate

## Next steps

- See [How to require access code authentication for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/require-access-code-recipient/).
- See [How to require phone authentication for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/phone-auth/).
- See [How to require knowledge-based authentication (KBA) for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/knowledge-based-authentication/).
- See [How to require ID verification (IDV) for a recipient](https://developers.docusign.com/docs/esign-rest-api/how-to/id-verification/).
- See the MyAPICalls sample app [Phone Authentication](https://myapicalls.sampleapps.docusign.com/scenario/5) scenario, which walks you through sequence of API calls that retrieve a list of identity verification workflows and create an envelope that requires phone authentication.

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
