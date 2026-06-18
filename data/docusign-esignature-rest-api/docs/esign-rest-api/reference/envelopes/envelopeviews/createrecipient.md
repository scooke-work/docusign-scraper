---
title: ': createRecipient'
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/
site: developers.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T20:28:21Z'
---

[API Reference](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/)[API Explorer](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/?explorer=true)

[EnvelopeViews](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/)

# : createRecipient

Returns a URL that enables you to
[embed the recipient view](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/)
of the
Docusign UI in your applications. If the recipient is a signer,
then the view will provide the signing ceremony.

This method is only used with envelopes in the `sent` status.

Due to screen space issues, Docusign recommends using [Focused View](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-focused-view/) if you plan to include the Docusign signing elements inside an `<iframe>` object.
For iOS devices, Docusign recommends using a WebView.

### The returned URL

The URL returned in this method's response is intended to be used
immediately to redirect the signer to the recipient view.
You can open the recipient view
in the current browser or in a new tab.
After the signer is redirected to the
recipient view, they must interact with the Docusign system
periodically or their session will time out.

The returned URL can be used only once and
expires after 5 minutes.
Do not store or email the returned URL.

If you want to invite someone to an embedded signing session via
email, the email invitation's URL must be to your application.
When invoked, your app should request a `recipientView` URL from
Docusign and then redirect the signer to that URL.

### How to specify the default language

You can append the `locale`
query parameter
to the URL returned by this method
to specify a language.

The language for the recipient view
follows this order or precedence:

- The language specified by the sender for the recipient.
- The `locale` parameter appended to the URL.
- The account language if the signer has a Docusign account.
- The language used in a previous signing if the signer is return signer.
- The browser language.

For example, to set the default language
to Canadian French, you would add this query parameter
to the returned URL:

```
...&locale=fr_CA
```

## Authentication

Your application is responsible for authenticating the identity
of the recipient or signer when you use this method. Use the
following parameters to record how the recipient
was authenticated.

- `assertionId`
- `authenticationInstant`
- `authenticationMethod`
- `clientUserId`
- `securityDomain`

At a minimum, `authenticationMethod` and `clientUserId` are
required. The information that you provide is included in the
envelope's certificate of completion.

## Sending to a remote signer

You can request a signing session for a remote recipient
who has a Docusign account.

Authenticate the request using the recipient's
credentials, and do not specify a `clientUserId`.
This differs from the typical behavior where the
request is authenticated using the sender's credentials,
and the recipient has a `clientUserId` defined.

## Redirecting back to returnUrl

After the signer completes or ends the signing ceremony, Docusign
redirects the user's browser back to your app via the
`returnUrl` that you supplied in the request.

The signer may be redirected through various Docusign
subdomains, depending on the region of the account sending the
envelope. Please consult [Allowlists for Docusign eSignature service](https://www.docusign.com/trust/security/esignature#allowlists-for-docusign-esignature-service)
in **Security for Docusign eSignature**
when setting up your allowlists

### The event status parameter

Docusign appends an `event` query parameter to the `returnUrl` with the
outcome of the signing ceremony. Your app can use this event
parameter to determine the next step for the envelope.
Do not fetch the envelope status by using
[Envelopes: get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/)
or a similar method because doing so
will probably hit [request and polling limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/).

| event query parameter | Meaning |
| --- | --- |
| signing\_complete | The recipient has signed the document. |
| access\_code\_failed | The recipient failed to provide the correct access code needed for recipient authentication. |
| cancel | The recipient decided to finish later. |
| decline | The recipient declined to sign the document. |
| exception | An exception has occurred on the server during the signing session. |
| fax\_pending | Recipient has a fax pending. |
| id\_check\_failed | The recipient failed to complete identity verification correctly. |
| session\_timeout | The recipient did not sign the document in time. The timeout is set to 20 minutes. |
| ttl\_expired | The token was not used within the timeout period or the token has already been accessed. |
| viewing\_complete | The recipient did not need to sign but has completed the viewing ceremony. |

Because a user can cancel redirection, close their
browser after signing, or spoof the landing URL,
you should not rely on the `returnUrl`
alone as the single source of truth for envelope
status for your integration.

### Maintaining State

After the recipient completes the recipient view (or signing
ceremony), they are redirected to your application. Your
application can recover state information about the transaction
by storing information in a cookie, or by including query
parameters in the `returnUrl` field. For example.
`https://myapp.example.com/docusign_return?myState=12345` When the
user is redirected to your app, the `event` query parameter will
be appended. In this example, prevent spoofing by not using a
guessable value as the state value.

### Related topics

- [How to request a signature through your app](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-in-app-embedded/)
- [How to request a signature using a composite template](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-composite-template-embedded/)
- [How to send an envelope via your app](https://developers.docusign.com/docs/esign-rest-api/how-to/embedded-sending/)
- [How to set envelope tab values](https://developers.docusign.com/docs/esign-rest-api/how-to/set-envelope-tab-values/)
- [How to set tab values in a template](https://developers.docusign.com/docs/esign-rest-api/how-to/set-template-tab-values/)
- [How to request a signature using focused view](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-focused-view/)

## Request

#### HTTP Request

POST

```
/restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}/views/recipient
```

## Parameters

| Path Parameters |  |  |
| --- | --- | --- |
| accountId \* | string | The external account number (int) or account ID GUID. |
| envelopeId \* | string | The ID of the draft envelope or template to preview. |

\* Required

## SDK Method

### Envelopes::createRecipientView

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
