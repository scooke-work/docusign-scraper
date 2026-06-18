---
title: Calculated fields
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/calculated-fields/
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
- Tabs
- Tabs
- Calculated Fields
scraped_at: '2026-06-18T20:28:18Z'
---

# Calculated fields

You can use *calculated fields*, also known as *formula tabs*, to apply a formula to user input from other tabs and to display a calculated final result. If the values of the tabs providing input to the calculated field change, the value of the calculated field will also change.

Calculated fields have a type of `formulaTab`, and can draw their input from [number fields](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/number-fields/), `dateTabs`, and `dateSignedTabs`. A calculated field must draw its input exclusively from number fields or `dateTabs/dateSignedTabs`; it cannot accept both numeric and date values at the same time.

## Numeric formulas

To set the numeric formula of a calculated field, and to specify its inputs, you set its formula property and enter the mathematical formula to be used, specifying the `tabLabels` of the `inputTabs` to be used as variables.

For example, the following code demonstrates how to use a numeric formula to calculate the total price of an object by adding the amount of tax. The subtotal is entered in one tab, and another read-only tab supplies the tax rate.

```
{
    "tabs": {
        "numberTabs": [{
            "tabLabel": "subTotal",
            ...
        }, {
            "tabLabel": "tax",
            "value": "0.05",
            "locked": "true",
            "xPosition": "50",
            "yPosition": "100",
            "documentId": "1",
            "pageNumber": "1"
        }],
        "formulaTabs": [{
            "tabLabel": "calculatedPrice",
            "formula": "([subTotal] * [tax]) + [subTotal]",
            "xPosition": "80",
            "yPosition": "100",
            "documentId": "1",
            "pageNumber": "1"
        }]
    }
}
```

## Date formulas

You can perform date-time operations and create formulas using a set of predefined date functions. You can use the following date-related functions to create date formulas:

- `AddDays(d1,n1)` : Returns a date calculated by adding or subtracting a number of days **(n1)** to or from a date **(d1)**. To subtract, a minus sign (-) is used before **(n1)**.
- `AddMonths(d1,n1)` : Returns a date calculated by adding or subtracting a number of months **(n1)** to or from a date **(d1)**. To subtract, a minus sign (-) is used before **(n1)**.
- `AddYears(d1,n1)` : Returns a date calculated by adding or subtracting a number of years **(n1)** to or from a date **(d1)**. To subtract, a minus sign (-) is used before **(n1)**.
- `DateDiff(d1,d2)` : Calculates the number of days between two dates **(d1-d2)**.
- `Day(d)` : Returns the current day of the month as a value, 1 through 31.
- `Days(d)` : Returns the number of days in the month for the specified date field **(d)**.

For example, if you had a contract that will be valid for 30 days, starting from the [date](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/create/#schema__enveloperecipienttabs_datesignedtabs) the document is signed, you could use the following tabs definition to calculate the contract expiration date using the `AddDays(d1,n1)` function:

```
{
    "tabs": {
        "dateSignedTabs": [{
            "tabLabel": "todaysDate",
            ...
        }],
        "formulaTabs": [{
            "tabLabel": "contractLength",
            "formula": "AddDays([todaysDate], 30)",
            "xPosition": "150",
            "yPosition": "75",
            "documentId": "1",
            "pageNumber": "1"
        }]
    }
}
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
