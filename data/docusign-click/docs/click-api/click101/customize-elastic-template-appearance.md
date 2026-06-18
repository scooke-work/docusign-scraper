---
title: Customize elastic template appearance
source_url: https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-appearance/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Click API
- Click API
- API 101
- API 101
- Customize Elastic Template Appearance
scraped_at: '2026-06-18T22:18:20Z'
---

# Customize elastic template appearance

You can customize the appearance of your elastic templates by adding a `style` attribute to their definitions. The `style` attribute contains elements that represent the elements of the elastic template whose appearance you wish to customize. Within each element, you define properties for specifying the colors, font options, button appearance, and other display options for that element.

For example, to set the color of a `documentLink` element, you could define it within the `style` attribute as shown below:

```
style: {
    documentLink: {
        color: '#333'
    }
}
```

Most properties specified within a `style` attribute element correspond exactly to the CSS style properties used to render that element. This means that, except where noted, they accept the same inputs as the corresponding CSS properties and behave in the same ways.

If you provide an invalid input for a `style` attribute element, no error will be generated, but the `style` will not be applied.

**Note**: Elastic template appearance customization is enabled for all developer (demo) accounts, but is not available by default in the production environment. To enable this feature in your production accounts, contact your Docusign Account Manager or Partner Account Manager.

The full list of elements and properties that you can customize within a elastic template `style` attribute are listed below:

**agreeButton**

- backgroundColor: The background color for the button. Corresponds to the CSS [background-color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color) property.
- borderRadius: The radius of the button’s border. Corresponds to the CSS [border-radius](https://www.w3schools.com/cssref/css3_pr_border-radius.asp) property.
- boxShadow: Adds a shadow effect around the button. Corresponds to the CSS [box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow) property.
- fontFamily: The font type used for the button. Corresponds to the CSS [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property.
- fontSize: The size of the button text. Corresponds to the CSS [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) property.
- fontWeight: The thickness of the button text characters. Corresponds to the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property.
- height: The height of the button. Corresponds to the CSS [height](https://developer.mozilla.org/en-US/docs/Web/CSS/height) property.
- margin: The space reserved outside the button’s border. Corresponds to the CSS [margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin) property.
- padding: The space between the element’s border and its content) for the button. Corresponds to the CSS [padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding) property.
- textDecoration: Applies styles such as strikethrough or underscore to button text. Corresponds to the CSS [text-decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/text-decoration) property.
- width: The width of the button. Corresponds to the CSS [width](https://developer.mozilla.org/en-US/docs/Web/CSS/width) property.

You can also define separate sets of styles to apply to different states of the `agreeButton`. The `agreeButton` states that you can define separate style sets for are:

- disabled - These styles are used when the button is disabled
- hover - These styles are used when the cursor is hovering over the button
- focus - These styles are used when the button is focused on

Updating specific settings in the above style sets for an `agreeButton` will override those settings in default styles for that state. If you set styles for the `agreeButton` without specifying one of the categories above, your styles will apply to the default `agreeButton`.

The following JSON snippet demonstrates how to set some example styles for your `agreeButton` states:

```
style: {
    agreeButton: {
        ':disabled': {
            cursor: 'not-allowed',
            opacity: '.1'
        },
        ':focus': {
            outline: '2px solid black'
        },
        ':hover': {
            backgroundColor: 'red'
        }
    },
}
```

**agreementStatement**

- fontFamily: The font type used for the agreement statement text. Corresponds to the CSS [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property.
- fontSize: The size of the agreement statement text. Corresponds to the CSS [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) property.
- fontWeight: The thickness of the agreement statement text characters. Corresponds to the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property.

**container**

- backgroundColor: The background color for the container. Corresponds to the CSS [background-color](https://developer.mozilla.org/en-US/docs/Web/CSS/background-color) property.
- borderColor: The border color for the container. Corresponds to the CSS [border-color](https://developer.mozilla.org/en-US/docs/Web/CSS/border-color) property.
- borderRadius: The radius of the container’s border. Corresponds to the CSS [border-radius](https://www.w3schools.com/cssref/css3_pr_border-radius.asp) property.
- borderStyle: The style (such as dotted or dashed) applied to the container’s border. Corresponds to the CSS [border-style](https://developer.mozilla.org/en-US/docs/Web/CSS/border-style) property.
- borderWidth: The width of the container’s border. Corresponds to the CSS [border-width](https://developer.mozilla.org/en-US/docs/Web/CSS/border-width) property.

**documentLink**

- `color`: The color of the documentLink. Corresponds to the CSS [color](https://developer.mozilla.org/en-US/docs/Web/CSS/color) property.
- `fontFamily`: The font type used for the link text. Corresponds to the CSS [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property.
- `fontSize`: The size of the link text. Corresponds to the CSS [font-size](https://developer.mozilla.org/en-US/docs/Web/CSS/font-size) property.
- `fontWeight`: The thickness of the link text characters. Corresponds to the CSS [font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight) property.

**header**

- `display`: Set a value of '`none`' to disable the header display.

**scrollControl**

- This enables you to choose how the elastic template document is displayed in your browser. See [Position elastic template documents on your web page](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-appearance/#position-elastic-template-documents) for details.

## Set font family

You can specify a `fontFamily` style for some elastic template elements and properties, such as `agreeButton`, `agreementStatement`, and `documentLink`. This enables you to set a font family and specific font to use when displaying the element’s text.

Like the CSS [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/font-family) property, you can set a prioritized comma separated list of one or more font family names and/or generic family names. The browser will select the first font in the list that is installed or that can be downloaded.

The following fonts are supported for elastic template styles:

- **Sans-serif**
  - Arial
  - Arial Narrow
  - Calibri
  - Helvetica
  - Tahoma
  - Verdana
- **Serif**
  - Times New Roman
  - Garamond
  - Georgia
- **Monospace**
  - Courier New
  - Lucida Console

## Position elastic template documents on your web page

You can use the `scrollControl` style attribute to choose how a elastic template document is displayed in your web page. The `scrollControl` attribute can be set to one of the following values:

- **browser**: Using this setting, signers can scroll through the document content within the web page rather than the iframe. This can give you more control over how the document is laid out on your web page than the default scrolling settings.
- **fill\_parent**: Enables you to use your web page display styling for the document height. When this option is set, the iframe will automatically change its height to fill its parent element. Typically, this should be used within a flexbox that is styled and positioned as the document container on your web page. This will also enable support for automatically resizing elastic template documents as the browser window is resized.

If not set to one of the above values, `scrollControl` defaults to null. In this case, the document will use the default iframe display behavior of using a 400px document height (not including the UI around the document).

## Example elastic template definition

The following code block shows a section of an example elastic template definition that includes a style attribute and several style elements:

```
<script>docuSignClick.Clickwrap.render({
    environment: 'https://demo.docusign.net',
    accountId: '9baa6115-xxxx-xxxx-xxxx-7088b86be96d',
    clickwrapId: '0ea010d8-xxxx-xxxx-xxxx-ef3b6b2e29de',
    clientUserId: '464f7988-xxxx-xxxx-xxxx-781ee556ab7a',
    documentData: {
        ...
    },
    style: {
        header: {
            display: 'none'
        },
        container: {
            backgroundColor: '#fff',
            borderWidth: '0'
        },
        agreementStatement: {
            fontWeight: 'normal'
        },
        documentLink: {
            color: '#333',
             fontWeight: 'normal'        },
        agreeButton: {
            boxShadow: '0 2px 2px 2px rgba(0, 0, 0, .2)',
            height: '40px',
            width: '100%',
            margin: '10px 0',
            padding: '3px 0',
            fontSize: '16px',
            fontWeight: 'bold',
            fontFamily: 'Helvetica, Arial, sans-serif',
            textDecoration: 'underline',
            backgroundColor: 'red',
            borderRadius: '20px'
        }
    },
...
</script>
```

**Note:** For compatibility with previous versions of the Click API, elastic templates use clickwrap endpoints.

## Next steps

- [How to customize a elastic template's appearance](https://developers.docusign.com/docs/click-api/how-to/customize-elastic-template-appearance/)
- [Click API concepts](https://developers.docusign.com/docs/click-api/click101/concepts/)
- [API Reference](https://developers.docusign.com/docs/click-api/reference/)

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
