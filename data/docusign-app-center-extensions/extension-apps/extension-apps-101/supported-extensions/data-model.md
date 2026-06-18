---
title: Data model
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- Data Model
scraped_at: '2026-06-18T19:51:49Z'
---

# Data model

Docusign models definitions using the [Concerto](https://concerto.accordproject.org/docs/intro/) open-source schema language. Both the [connected fields extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/) and the [data IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/) use this model. See [Why Concerto?](https://concerto.accordproject.org/docs/why-concerto) for details about the features and advantages of Concerto.

## Transform logic

If your system of record does not already use the Concerto data model, you must implement transform logic that maps your definitions to Concerto data types as part of your **Get Type Definitions** implementation. When **Get Type Definitions** is called, this transform will convert the definitions into a Concerto data model format before returning it to Docusign.

- For more information about Concerto, see the [Concerto](https://concerto.accordproject.org/docs/intro/) open-source documentation.
- For details about Concerto model use with extensions that require it, see:
  - [Connected fields extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/)
  - [Data IO extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/)

There are many ways to map your definitions to Concerto types. The following sections list each data source type and a mapping recommendation to a supported Concerto type. Where applicable, each section also lists the type of value that each Concerto type will be rendered as in workflows (for data IO) and eSignature envelopes (for connected fields).

### Class declarations

**Concerto type:** [Concepts](https://concerto.accordproject.org/docs/design/specification/model-classes) **Rendered in Workflow Builder read and write steps as:** A list of objects from which a preparer can choose one to read from or write to.

**Rendered in eSignature envelopes as:** Connected field groups that can be added to a document.

**Notes:** Concepts are similar to class declarations in most object-oriented languages, in that they may have a super-type and a set of typed [properties](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#properties).

### Properties

Class declarations contain properties, and each property has a unique name within its class declaration. A property takes one of the types listed in the sections below. Expand each section for details.

Every name for a type declaration must be unique, and properties within declarations must be unique. If a data model in a **Get Type Names** or **Get Type Definitions** response violates either of these requirements, this will cause an error. You can use the [Concerto VSCode extension](https://concerto.accordproject.org/docs/tools/vscode/) to validate your data model and check for errors.

### Enumerations

**Concerto type:** [Enumerations](https://concerto.accordproject.org/docs/design/specification/model-enums) **Rendered in Workflow Builder read and write steps as:** Not supported

**Rendered in eSignature envelopes as:** Radio buttons

### Decorators

In Concerto, [decorators](https://concerto.accordproject.org/docs/design/specification/model-decorators) are annotations that can be placed on declarations and properties to extend the metamodel definition.

For connected fields extensions, `term` decorators on concepts and properties appear as display names in eSignature. The `VerifiableType` decorator indicates that an object is verifiable from eSignature envelopes. The `IsRequiredForVerifyingType` decorator indicates that a property is required for verifying the object. See [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) for more information.

For data IO extensions, `term` decorators on concepts and properties appear as display names in Workflow Builder workflows. CRUD operations determine which workflow steps objects and fields appear in. If readable, they appear in the read step. If updateable/creatable, they appear in the write step. See [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) for more information.

## Data type standards

Docusign enforces standards for data values that it sends to and receives from external API services. The external service must be able to accept values in the format that Docusign sends. If the service requires a different format for back-end processing, the service must convert values internally to the required format. Data values that the external service provides in responses to Docusign must also adhere to these standards. If a response from an external service includes a value in an unsupported format, the value may not appear correctly in a Workflow Builder workflow step or in an eSignature envelope. For example, if a returned value for a data IO **Search Records** action is not in a supported format, the web form field that displays that value may be empty at workflow instance run time.

In the current release, data type standards apply to:

- [Date-time values](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#date-time-values)
- [Email addresses](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#email-addresses)
- [Phone numbers](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#phone-numbers)

Standards for other data types will be implemented in future releases.

### Date-time values

Date-time standards are currently applicable only for data IO extensions. The standards will be implemented for connected fields extensions in a future release.

#### Requests from Docusign to the API service

Docusign uses this ISO 8601 UTC format for date-time values in requests to external API services:

`YYYY-MM-DDTHH:mm:ss.SSSZ`

For example:

`2025-03-17T10:45:00.000Z`

The extensions and requests that use this format are:

- [Data IO](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/)
  - [Create Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-create-record)
  - [Patch Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-patch-record)
  - [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records)

#### Responses from the API service

Docusign supports these ISO 8601 formats for date-time values in responses to the data IO extension [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records) action:

| Format | Example | Notes |
| --- | --- | --- |
| `YYYY-MM-DD` | `2024-12-27` | For values in this format, Docusign defaults to a time value of midnight UTC. |
| `YYYY-MM-DDTHH:mm:ssZ` | `2024-12-27T13:24:03Z` |  |
| `YYYY-MM-DDTHH:mm:ss±HH:mm` | `2024-12-27T13:24:03+12:00` |  |
| `YYYY-MM-DDTHH:mm:ss.SZ` | `2024-12-27T13:24:03.9Z` |  |
| `YYYY-MM-DDTHH:mm:ss.SSZ` | `2024-12-27T13:24:03.91Z` |  |
| `YYYY-MM-DDTHH:mm:ss.SSSZ` | `2024-12-27T13:24:03.917Z` |  |
| `YYYY-MM-DDTHH:mm:ss.S±HH:mm` | `2024-12-27T13:24:03.9Z+12:00` |  |
| `YYYY-MM-DDTHH:mm:ss.SS±HH:mm` | `2024-12-27T13:24:03.91Z+12:00` |  |
| `YYYY-MM-DDTHH:mm:ss.SSS±HH:m` | `2024-12-27T13:24:03.917Z+12:00` |  |

### Email addresses

For email addresses, Docusign supports the [Accord Project](https://accordproject.org/) [EmailAddress](https://github.com/accordproject/models/blob/main/src/contact%401.0.0.cto) type. This type has a maximum length of 254 characters.

Using the Accord `EmailAddress` type provides these benefits:

- It adheres to Internet Engineering Task Force (IETF) standards. See the [type definition](https://github.com/accordproject/models/blob/main/src/contact%401.0.0.cto) for details.
- Workflow Builder recognizes this type in an extension app's data model and displays it in the UI as an email address, making it easier for process builders to configure workflows.

If you prefer not to use the Accord `EmailAddress` type, your extension app can define email addresses as strings.

**Note:** The Accord `EmailAddress` type is supported only for data IO extensions.

#### How to specify the Accord Project EmailAddress type

To include the Accord Project `EmailAddress` type as a property for an object in an extension app's data model, make sure that the response to the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) request specifies these values:

- `$class:` `concerto.metamodel@1.0.0.ObjectProperty`
- `name:` `EmailAddress`
- `type.$class:` `concerto.metamodel@1.0.0.TypeIdentifier`
- `type.name:` `EmailAddress`
- `type.namespace:` `org.accordproject.contact@1.0.0`

For example:

```
{
  "$class": "concerto.metamodel@1.0.0.ObjectProperty",
  "name": "EmailAddress",
  "type": {
    "$class": "concerto.metamodel@1.0.0.TypeIdentifier",
    "name": "EmailAddress",
    "namespace": "org.accordproject.contact@1.0.0"
  },
  "isOptional": false,
  "isArray": false,
  "decorators": [
    {
      "$class": "concerto.metamodel@1.0.0.Decorator",
      "name": "Term",
      "arguments": [
        {
          "$class": "concerto.metamodel@1.0.0.DecoratorString",
          "value": "Human Email"
        }
      ]
    },
    {
      "$class": "concerto.metamodel@1.0.0.Decorator",
      "name": "Crud",
      "arguments": [
        {
          "$class": "concerto.metamodel@1.0.0.DecoratorString",
          "value": "Createable,Readable,Updateable"
        }
      ]
    }
  ]
}
```

#### EmailAddress type in requests from Docusign to the API service

If the external API service's response to the **Get Type Definitions** request specifies the Accord `EmailAddress` type for a property, Docusign will use this type for the property in these requests to the external service:

- [Data IO](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/)
  - [Create Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-create-record)
  - [Patch Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-patch-record)
  - [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records)

An example **Create Record** request to the external service using the Accord `EmailAddress` type looks like this:

```
{
  "typeName": "Contact",
  "idempotencyKey": "123-456-789",
  "data": {
    "firstName": "Sally",
    "lastName": "Signer",
    "EmailAddress": "sally.signer@email.com"
  }
}
```

For additional code examples including a data model definition and example search query, see the [data IO reference implementation](https://github.com/docusign/extension-app-data-io-reference-implementation).

#### EmailAddress type in responses from the API service

If the external API service's response to the **Get Type Definitions** request specifies the Accord `EmailAddress` type for a property, Docusign expects the external service to use this type for the property in responses to the **Search Records** action.

#### Adopt the EmailAddress type for production extension apps

If you adopt the Accord Project `EmailAddress` type for an extension app that is in production, Docusign recommends the following to avoid transition issues:

1. After the external data source's data model has been updated with the Accord type, [refresh the connection](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=qkv1716320270335.html) for each Docusign account that has the extension app installed.
2. For each Workflow Builder workflow that uses the extension app, [edit the workflow steps](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=zlm1698880256815.html) that reference the property, and replace the old string version of the property with the updated format.
3. To ensure backward compatibility for workflows that have not been updated, make sure that the external service logic can handle requests regardless of whether they format the property as a string or the Accord type.

### Phone numbers

For phone numbers, Docusign supports the [Accord Project](https://accordproject.org/) [PhoneNumber](https://github.com/accordproject/models/blob/main/src/contact%401.0.0.cto) type. The type includes these properties:

| Property | Type | Occurrence | Description |
| --- | --- | --- | --- |
| `number` | `string` | Required | The phone number. **Note:** Although the Accord definition allows special characters in this value, Docusign requires a normalized format with no special characters such as spaces, brackets, plus signs, or hyphens. Maximum length: 32 |
| `normalizedNumber` | `string` | Optional | The phone number. Maximum length: 15 |
| `extension` | `string` | Optional | A phone extension. Maximum length: 6 |
| `countryCode` | `string` | Required | The country code. Maximum length: 7 |

Using the Accord `PhoneNumber` type provides the following benefits:

- It adheres to International Telecommunication Union (ITU) standards. See the [type definition](https://github.com/accordproject/models/blob/main/src/contact%401.0.0.cto) for details.
- Workflow Builder recognizes this type in the extension app's data model and displays it in the UI as a phone number, making it easier for process builders to configure workflows.
- Sending phone number components to the external system in separate properties makes it easier to apply business logic to the values.

If you prefer not to use the Accord `PhoneNumber` type, your extension app can define phone numbers as strings.

**Note:** The Accord `PhoneNumber` type is supported only for data IO extensions.

#### How to specify the Accord Project PhoneNumber type

To include the Accord Project `PhoneNumber` type as a property for an object in an extension app's data model, the response to the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) request must specify these values:

- `$class:` `concerto.metamodel@1.0.0.ObjectProperty`
- `name:` `PhoneNumber`
- `type.$class:` `concerto.metamodel@1.0.0.TypeIdentifier`
- `type.name:` `PhoneNumber`
- `type.namespace:` `org.accordproject.contact@1.0.0`

For example:

```
{
  "$class": "concerto.metamodel@1.0.0.ObjectProperty",
  "name": "PhoneNumber",
  "type": {
    "$class": "concerto.metamodel@1.0.0.TypeIdentifier",
    "name": "PhoneNumber",
    "namespace": "org.accordproject.contact@1.0.0"
  },
  "isOptional": true,
  "isArray": false,
  "decorators": [
    {
      "$class": "concerto.metamodel@1.0.0.Decorator",
      "name": "Term",
      "arguments": [
        {
          "$class": "concerto.metamodel@1.0.0.DecoratorString",
          "value": "Phone Number"
        }
      ]
    },
    {
      "$class": "concerto.metamodel@1.0.0.Decorator",
      "name": "Crud",
      "arguments": [
        {
          "$class": "concerto.metamodel@1.0.0.DecoratorString",
          "value": "Createable,Readable,Updateable"
        }
      ]
    }
  ]
}
```

#### PhoneNumber type in requests from Docusign to the API service

If the external API service's response to the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions) request specifies the Accord `PhoneNumber` type for a property, Docusign will use this type for the property in these requests to the external service:

- [Data IO](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/)
  - [Create Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-create-record)
  - [Patch Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-patch-record)
  - [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records)

An example **Create Record** request to the external service using the Accord `PhoneNumber` type looks like this:

```
{
  "typeName": "Contact",
  "idempotencyKey": "123-456-789",
  "data": {
    "firstName": "Sally",
    "lastName": "Signer",
    "phoneNumber": {
      "number": "4155551212",
      "normalizedNumber": "4155551212",
      "extension": "444",
      "countryCode": "1"
    }
  }
}
```

For additional code examples including a data model definition and example search query, see the [data IO reference implementation](https://github.com/docusign/extension-app-data-io-reference-implementation).

#### PhoneNumber type in responses from the API service

If the external API service's response to the **Get Type Definitions** request specifies the Accord `PhoneNumber` type for a property, Docusign expects the external service to use this type for the property in responses to the **Search Records** action.

In addition, `PhoneNumber` values must adhere to these requirements:

- `number` and `countryCode` must be included.
- If supplied in the response, the values for `normalizedNumber` and `number` must be the same.
- All `PhoneNumber` property values must be in a normalized format with no special characters such as spaces, brackets, plus signs, or hyphens.

#### Adopt the PhoneNumber type for production extension apps

If you adopt the Accord Project `PhoneNumber` type for an extension app that is in production, Docusign recommends the following to avoid issues with the transition:

1. After the external data source's data model has been updated with the Accord type, [refresh the connection](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=qkv1716320270335.html) for each Docusign account that has the extension app installed.
2. For each workflow that uses the extension app, [edit the workflow steps](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=zlm1698880256815.html) that reference the property, and replace the old string version of the property with the updated format.
3. To ensure backward compatibility for workflows that have not been updated, make sure that the external service logic can handle requests regardless of whether they format the property as a string or the Accord type.

## Next steps

- Find out more about the [data IO extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/).
- Get an overview of the [connected fields extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/).
- Explore the options for [testing](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) an extension app.

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
