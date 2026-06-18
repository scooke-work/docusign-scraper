---
title: Setting tabs in HTML documents
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/responsive/setting-tabs/
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
- Responsive signing
- Responsive signing
- Setting Tabs
scraped_at: '2026-06-18T21:09:59Z'
---

# Setting tabs in HTML documents

When you create an HTML document for a [Advanced responsive signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/responsive#advanced) workflow, you can set tabs for that document in one of two ways:

- [Adding HTML blocks](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/responsive/setting-tabs#addingHtml) that contain the tab definitions to the document’s HTML source. Each Docusign tab has a corresponding HTML tag that you can use to add and configure that tab within the document definition.
- [Embedding JSON markers](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/responsive/setting-tabs#embeddingJson) into the HTML that represents tabs. These markers will be replaced by tabs when the document is processed.

**Note:** Only inline styles will be reflected in the processed document. Any styles defined outside the page, such as `<style>` tag elements in the `<head>` section or CSS, will not be applied.

## Define tabs as HTML

You can configure the properties of the tabs you have added as HTML elements using attributes. Any value set in this way will override the tab's default values.

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

{

"recipients": {

"signers": [{

"name": "Example J. Simpson",

"email": "ejs@example.com",

"recipientId": "1",

"routingOrder": "1"

}]

},

"status": "sent",

"emailSubject": "Please DocuSign: Contract",

"documents": [{

"name" : "Example contract",

"documentId" : "1",

"htmlDefinition": {

"source": "<div><div><button

data-ds-type=\"approve\" name=\"Approve\"

title=\"I agree\">I Agree</button><p>I agree

to the terms of this contract.</p></

div><ds-signature data-ds-recipient-id=\"1\"

|  |  |  |
| --- | --- | --- |
| **Tab property** | **HTML attribute** | **Default value** |
| AutoEmail | data-ds-autoemail | true |
| Bold | font-weight | "" |
| Checked | checked | false |
| Color | color | "" |
| ConditionalParent | data-ds-conditional-parent | "" |
| ConditionalParentValue | data-ds-conditional-value | "" |
| Disabled | disabled | false |
| FontFamily | font-family | "" |
| FontSize | font-size | "" |
| Height | height | 0 |
| Italic | font-style | "" |
| Label | name | "" |
| Locked | readonly | false |
| MaxLength | maxlength | 0 |
| Pattern | pattern | "" |
| PatternMessage | data-ds-pattern-message | "" |
| Role | data-ds-role | "" |
| RecipientId | data-ds-recipient-id | "" |
| Required | required | true |
| ScaleValue | data-ds-scale | "" |
| Shared | data-ds-shared | false |
| SharedRequireInitial | data-ds-shared-require-initial | false |
| TextGrow | data-ds-autogrow | true |
| Title | title | "" |
| Value | value | "" |
| Width | width | size | Size |

## Define tabs as JSON markers

Instead of defining tabs as HTML, you can embed JSON markers referencing your tab definitions directly into the document’s HTML source. These markers will be replaced by tabs when the document is processed.

Each JSON marker contains one element, `tabLabel`, which indicates which tab will be placed. Each `tabLabel` should have a unique value and must match one of the tab definitions set in the API request, as shown in the associated example definition:

## JSON marker Radio tabs

Radio tabs use a unique behavior. When placing a radio tab, the JSON must include the groupName and value properties, which must map to a radio button within a group, as shown in the example below.
**Inline JSON marker:**

```
  {{"groupName": "myRadio", "value": "radio1"}}
  {{"groupName": "myRadio", "value": "radio2"}}
```

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

19

20

{

"recipients": {

"signers": [

{

"name": "Example J. Simpson",

"email": "ejs@example.com",

"recipientId": "1",

"routingOrder": "1",

"tabs": {

"approveTabs": [

{

"name": "Approve",

"tabLabel": "exampleApproveTab",

"documentId": "1",

"recipientId": "1",

"pageNumber": "1"

}

],

"signHereTabs": [

{

## Supported HTML, attribute, and CSS elements

**Allowed HTML element list**

- a
- abbr
- acronym
- address
- area
- article
- aside
- b
- bdi
- big
- blockquote
- body
- br
- button
- caption
- center
- cite
- code
- col
- colgroup
- data
- datalist
- dd
- del
- details
- dfn
- dir
- div
- dl
- dt
- em
- fieldset
- figure
- figcaption
- font
- footer
- form
- h1
- h2
- h3
- h4
- h5
- h6
- head
- header
- hr
- html
- i
- img
- input
- ins
- kbd
- keygen
- label
- legend
- li
- main
- map
- mark
- menu
- menuitem
- meter
- nav
- ol
- optgroup
- option
- output
- p
- pre
- progress
- q
- rp
- rt
- ruby
- s
- samp
- section
- select
- small
- span
- strike
- strong
- sub
- sup
- summary
- table
- tbody
- td
- textarea
- tfoot
- th
- thead
- time
- tr
- tt
- u
- ul
- var
- wbr

**Allowed HTML attribute list**

- abbr
- accept
- accept-charset
- accesskey
- action
- align
- alt
- autocomplete
- autosave
- axis
- bgcolor
- border
- cellpadding
- cellspacing
- char
- charoff
- charset
- checked
- challenge
- cite
- class
- clear
- cols
- colspan
- color
- compact
- contenteditable
- coords
- data-navigate-to
- data-qa
- data-action
- data-icon-closed
- data-icon-open
- data-display
- datetime
- dir
- disabled
- draggable
- dropzone
- enctype
- for
- frame
- headers
- height
- high
- href
- hreflang
- hspace
- id
- ismap
- keytype
- lang
- label
- list
- longdesc
- low
- max
- maxlength
- media
- method
- min
- multiple
- name
- nohref
- noshade
- novalidate
- nowrap
- open
- optimum
- pattern
- placeholder
- prompt
- pubdate
- radiogroup
- readonly
- rel
- required
- rev
- reversed
- rows
- rowspan
- rules
- scope
- selected
- shape
- size
- span
- spellcheck
- src
- start
- step
- style
- summary
- tabindex
- target
- title
- type
- usemap
- valign
- value
- vspace
- width
- wrap

**Allowed HTML CSS list**

- align
- align-content
- align-items
- align-self
- background
- background-attachment
- background-clip
- background-color
- background-image
- background-origin
- background-position
- background-repeat
- background-repeat-x
- background-repeat-y
- background-size
- border
- border-bottom
- border-bottom-color
- border-bottom-left-radius
- border-bottom-right-radius
- border-bottom-style
- border-bottom-width
- border-collapse
- border-color
- border-image
- border-image-outset
- border-image-repeat
- border-image-slice
- border-image-source
- border-image-width
- border-left
- border-left-color
- border-left-style
- border-left-width
- border-radius
- border-right
- border-right-color
- border-right-style
- border-right-width
- border-spacing
- border-style
- border-top
- border-top-color
- border-top-left-radius
- border-top-right-radius
- border-top-style
- border-top-width
- border-width
- bottom
- caption-side
- clear
- clip
- color
- content
- counter-increment
- counter-reset
- cursor
- direction
- display
- empty-cells
- flex
- flex-direction
- flex-flow
- flex-grow
- flex-shrink
- flex-wrap
- float
- font
- font-family
- font-feature-settings
- font-kerning
- font-language-override
- font-size
- font-size-adjust
- font-stretch
- font-style
- font-synthesis
- font-variant
- font-variant-alternates
- font-variant-caps
- font-variant-east-asian
- font-variant-ligatures
- font-variant-numeric
- font-variant-position
- font-weight
- grid-area
- grid-column
- grid-column-end
- grid-column-gap
- grid-column-start
- grid-gap
- grid-row
- grid-row-end
- grid-row-gap
- grid-row-start
- grid-template-area
- grid-template-columns
- grid-template-rows
- height
- justify-content
- justify-self
- left
- letter-spacing
- line-height
- list-style
- list-style-image
- list-style-position
- list-style-type
- margin
- margin-bottom
- margin-left
- margin-right
- margin-top
- max-height
- max-width
- min-height
- min-width
- opacity
- orphans
- outline
- outline-color
- outline-offset
- outline-style
- outline-width
- overflow
- overflow-wrap
- overflow-x
- overflow-y
- padding
- padding-bottom
- padding-left
- padding-right
- padding-top
- page-break-after
- page-break-before
- page-break-inside
- quotes
- right
- table-layout
- text-align
- text-decoration
- text-decoration-color
- text-decoration-line
- text-decoration-skip
- text-decoration-style
- text-indent
- text-shadow
- text-transform
- top
- unicode-bidi
- vertical-align
- visibility
- white-space
- widows
- width
- word-break
- word-spacing
- word-wrap
- z-index

**Allowed URI Schemes**

- data
- http
- https

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
