---
title: Docusign JS for embedded signing reference
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/docusign-js-embedded-reference/
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
- Embedding
- Embedding
- Docusign Js Embedded Reference
scraped_at: '2026-06-18T21:09:59Z'
---

# Docusign JS for embedded signing reference

You can use the Docusign JS JavaScript library to:

- Implement [Embedded signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/embedded-signing/) with focused view, focused view/Click to Agree, and classic signing sessions.
- Render web form instance URLs for the Docusign [Web Forms API](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls).

This topic focuses on using Docusign JS for embedded signing. See [Web Forms API](https://developers.docusign.com/docs/web-forms-api/plan-integration/render-instances/#use-docusign-js-to-render-web-form-instance-urls) when using it with the Web Forms API. The library can be used for both purposes on the same web page.

## 1. Install Docusign JS

Add the development or production version of Docusign JS to your web page:

- If your app uses the **Development environment**:
  `<script src="https://js-d.docusign.com/bundle.js"></script>`
- If your app uses the **Production environment**:
  `<script src="https://js.docusign.com/bundle.js"></script>`

**Note**: Do not make a local copy of `bundle.js`, it must match the platform version.

## 2. Add a container element to your DOM

When the Docusign JS mount method is called, it will add an iframe to the DOM element you use as an argument for the method. When the `sessionEnd` event is raised, the library will delete the iframe.

Add an empty block element (such as a `div`) to your DOM to hold the iframe. You must set the block element’s `width` and `height`. You can use `@media` CSS to change the `div`’s width based on the overall screen’s width. Bootstrap and other layout systems can also be used.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

<!DOCTYPE html>

<html>

<head>

<meta charset="utf-8" />

<title>Signing</title>

<style>

html, body {

padding: 0;

margin: 0;

font: 13px Helvetica, Arial, sans-serif;}

/\* container styles \*/

@media (max-width: 768px){

.docusign-agreement-container {width: 50%}}

@media (min-width: 769px) (max-width:

1024px) {

.docusign-agreement-container {width: 70%}}

@media (min-width: 1025px) {

.docusign-agreement-container {width:

100%}}

</style>

## 3. Call EnvelopeViews:createRecipient

Call the [EnvelopeViews:createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) API method and provide values for the [frameAncestors](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/#schema__recipientviewrequest_frameancestors) and [messageOrigins](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/#schema__recipientviewrequest_messageorigins) attributes:

- The [frameAncestors](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/#schema__recipientviewrequest_frameancestors) attribute is an array of HTTP [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) strings, not including anything after the hostname or port. Include the `https://apps-d.docusign.com` origin for the developer environment or `https://apps.docusign.com` for production. Include additional  origins for your app’s ancestor origins that will embed the signing session. Origins must use `https` rather than `http`, with the exception of for `localhost`. The `localhost` origin can’t be used in production.

  **Note:** `frameAncestors` has a limit of 500 characters (for all URLs combined).

  **Examples**:

  ```
  ["https://apps-d.docusign.com", "http://localhost"] # default port
  ["https://apps-d.docusign.com", "http://localhost:8080"] # specific port
  ["https://apps.docusign.com", "https://app1.example.com",
  	"http://app1frame.example.com"] # production
  ```
- The [messageOrigins](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/#schema__recipientviewrequest_messageorigins) attribute is an array of HTTP [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) strings. The array must have one member:
  - `["https://apps-d.docusign.com"] # demo`
  - `["https://apps.docusign.com"] # production`
- The [returnUrl](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/#schema__recipientviewrequest_returnurl) attribute must be set, but will not be used.

All other attributes should be set as usual. 

The [EnvelopeViews:createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) API method’s [url](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/#schema_201_envelopeviews_envelopeviews_url) response is used in the browser with Docusign JS. If you call `createRecipient` on the server, return the url to your browser page.

The `window.loadDocuSign(``integration_key``) RETURNS` `Promise` resolves to a Docusign object, and is called first to obtain the Docusign object. **Performance tip**: This method can be called asynchronously before it is needed to create a signing session. 

The `integration_key` argument is a string that contains your application’s integration key (client ID). Client IDs are not secrets.

### Signing method

The Docusign object includes the `signing` method:

`signing(SigningConfiguration)``RETURNS Signing object`

The `signing` method creates the embedded signing session. It takes as a parameter a `SigningConfiguration` object to control the signing session’s format and style attributes. The returned `Signing` object represents the signing session that will be displayed. See [Signing object methods](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/docusign-js-embedded-reference/#signing-object-methods) for a list of methods.

#### SigningConfiguration object properties

|  |  |  |
| --- | --- | --- |
| Property name | Type | Description |
| `url` | `string` | Required. The signing URL response from [EnvelopeViews:createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/). |
| `displayFormat` | `string` | Required. The signing session’s UX format.   Possible values are:   - `"focused"`: Sets the signing session to use focused view or (if the main documents have no tabs) focused view/Click to Agree - `"default"`: Sets the signing session to use the Docusign classic UX format. |
| `style` | `StyleObject object` | Optional. A `StyleObject` containing style settings for the signing session. |

#### StyleObject properties

Some styling options have not yet been implemented for some display formats.

```
{
 branding: BrandingObject,
 signingNavigationButton: SigningNavigationButtonObject
}
```

The following options are supported for the Docusign JS `StyleObject`:

|  |  |  |
| --- | --- | --- |
| Property name | Type | Description |
| `branding` | `BrandingObject` | A container for objects on which branding style elements can be applied. Currently this consists of the `primaryButton` object. |
| `primaryButton (sub-object of branding)` | `PrimaryButtonObject` | Settings for the primary UX button.   Properties:  - `color`: CSS color value for the text of the button. - `backgroundColor`: CSS color value for the button itself. |
| `signingNavigationButton` | `SigningNavigationButtonObject` | Optional; specifies position and text for the signing button. Properties:  - `finishText`: String with a maximum of 50 characters. - `position`: Accepts one of these values: `'bottom-left'`, `'bottom-center'`, `'bottom-right'`. |
| `signingDeclineButton` | `signingDeclineButtonObject` | Optional; specifies if a Decline button will be shown. This option is not available for all display formats.    Properties:  - `show`: A boolean value that indicates whether to show a Decline button or not. If `false` (default), do not show a Decline button. If `true`, show a Decline button. See [Decline and Approve tab types](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/#tab-types) for more information. - `finishText`**:** String with a maximum of 50 characters that will render on the `signingDeclineButton` |
| `declineModal` | `declineModalObject` | Optional; `show` indicates whether to show a Decline modal or not to require a reason to decline or to decline immediately. Defaults to `false`. |
| `downloadModal` | `downloadModalObject` | Optional; `show` indicates whether to show a download completed document modal after envelope finish. Defaults to `false`. |

#### Example SigningConfiguration object

```
const signingConfiguration = {
    url: recipientViewUrl,
    displayFormat: 'focused',
    style: {
        branding: {
            primaryButton: {
                backgroundColor: 'purple',
                color: 'white'
            }
        },
        signingNavigationButton: {
            finishText: 'Submit',
            position: 'bottom-right'
        },
        signingDeclineButton: {
            show: true, // default value is false
            finishText: 'Decline Button Text'
        },
        declineModal: {
            show: true // default value is false
        },
        downloadModal: {
            show: true // default value is false
        }
    }
}
```

#### Signing object methods

The signing object is used to display the signing session and catch the signing-related events it raises.

|  |  |
| --- | --- |
| **Method name** | **Description** |
| `mount(containerSelectString)` | Adds, then displays the signing session to the DOM. This is a synchronous method that initiates asynchronous side effects (the signing session is displayed). The ready event is raised when the session has been displayed.  The required `containerSelectString` parameter is a CSS selector string that resolves to the container element for the signing session. For example: `"#docusignContainer"` |
| `on(eventName, cbFunction)` | The `on` method adds an event listener.  - The required `cbFunction` parameter is afunction with an **event** argument. - The required `eventName` parameter is a string naming the event.  The following events are supported as `eventName` argument values:  - `ready`: The signing session has been displayed and is ready for the user - `sessionEnd`: The signing session has ended. There are multiple reasons for this event, for which the `event.sessionEndType` string will be set:  ``` 'signing_complete' 'cancel' 'decline' 'exception' 'fax_pending' 'session_timeout' 'ttl_expired' 'viewing_complete' ``` |

## Use Docusign JS with JavaScript

This example uses the JavaScript [module type](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#module) to enable the [await keyword at the top level](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#top_level_await) of the script. See the [Docusign JS GitHub example](https://github.com/docusign/docusign.github.io/blob/master/app-examples/docusign.js-example/index.html) for the full source code.

```
<style>
    .hide {display: none;}
</style>
...
<script type="module">
    let signingUrl; // the EnvelopeViews:createRecipient response
    let clientId; // your app’s IK
    const signingConfiguration = {
        url: signingUrl,
        displayFormat: 'focused',
        style: // see above for an example
    }
    try {
        const docusign = await window.DocuSign.loadDocuSign(clientId);
        const signing = docusign.signing(signingConfiguration);
            
        /** Event handlers **/
        signing.on('ready', (event) => {console.log('UI is rendered')});
        signing.on('sessionEnd', (event) => {
            console.log('sessionEnd', event)}); 
        // Open the signing ceremony
        $(`#main`).addClass("hide"); // JQuery to hide content
        $(`#signing-ceremony`).removeClass("hide"); // Display the container
        signing.mount(`#signing-ceremony`);
    } catch (error) {
        // Any configuration or API limits will be caught here
        console.log ("### Error calling docusign.js");
        console.log (error);              
    }
</script>
```

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
