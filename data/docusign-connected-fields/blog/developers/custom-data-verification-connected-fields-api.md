---
title: 'From NIGO to STP: A developer''s guide to custom data verification and the
  Connected Fields API'
source_url: https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api
site: www.docusign.com
breadcrumb:
- Home
- Home
- Blog
- Blog
- Developers
- Developers
scraped_at: '2026-06-18T18:27:07Z'
---

[Blog](https://www.docusign.com/blog)

# From NIGO to STP: A developer's guide to custom data verification and the Connected Fields API

[![Author Julie Gordon](https://images.ctfassets.net/9pvazpst9iwl/6pWetjZY1gCV6eGt1gtX4J/66fc155e0053c16de36ebc64a6baf9c2/JGordonNewPhoto400x400.jpeg?fm=avif&q=90&w=500)

Julie GordonSr. Programmer Writer](https://www.docusign.com/blog/author/julie-gordon)•Published Apr 16, 2025

---

Summary•11 min read

Implement a Docusign custom data verification solution that integrates seamlessly with your system of record to ensure the accuracy of agreement data.

![](https://images.ctfassets.net/9pvazpst9iwl/1ZAoOA9PEOU8QGOVVQQ0ZS/b113517ee82ef916ea353f569906ca79/Release_1_developer_blog_-_connected_fields_api_-_custom_DV.jpg?fm=avif&q=90&w=500)

- - [How to build custom data verification for eSignature flows](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#how-to-build-custom-data-verification-for-esignature-flows)
  - [Implementation components](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#implementation-components)

  - [Implement connected fields extension app logic](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#implement-connected-fields-extension-app-logic)
  - [Register and test the extension app](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#register-and-test-the-extension-app)
  - [Implement a Connected Fields API integration](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#implement-a-connected-fields-api-integration)
  - [Move to production](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#move-to-production)
  - [Get started with custom data verification](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#get-started-with-custom-data-verification)
  - [Additional resources](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#additional-resources)

Reprocessing agreements that are not in good order (NIGO) imposes costs to organizations in time, money, and customer satisfaction. But there is a solution: [Docusign for Developers](https://www.docusign.com/blog/docusign-discover-2024), a new suite of agreement APIs and tools. Docusign for Developers enables you to build a custom data verification application that generates agreements, verifies their values against your system of record, and enables users to correct data before submittal. Your implementation can be fully customized to your organization's data model and business logic. The result: Straight-through processing (STP) for agreements that avoids costly manual intervention and provides a more seamless customer experience.

This blog post walks you through the implementation of a custom data verification solution. The use case described here applies to corporate developers who are implementing an application that is tailored to their organization's services and data and will be available only to internal users. Custom data verification can also be implemented by independent software vendors (ISVs), who can then publish their applications for distribution to Docusign customers on the [App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

## How to build custom data verification for eSignature flows

The examples in this walkthrough demonstrate how to build custom data verification for an eSignature [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) that authorizes a financial transfer. Envelope fields whose values are to be verified are called *connected fields*. Each connected field can be mapped to a property in your system of record. When a user completes the connected fields in the envelope signing UI, Docusign sends your system a verification request that includes the values.

Your system applies its verification logic and returns the result in its response to Docusign, which displays the result to the user. In the response, your system also supplies custom messages that provide guidance about the information the user must enter. In addition, your system can return autofill values for connected fields based on known information about the user.

If verification succeeds, the user can complete and submit the envelope to Docusign.

## Implementation components

This implementation requires two major components that are developed and hosted externally to Docusign.

One component is a connected fields [extension app](https://developers.docusign.com/extension-apps/). An *extension app* is an application that provides additional functionality for Docusign agreement processes via requests to an external API service. For a connected fields extension app, Docusign sends API requests to:

- Retrieve information about the objects and properties in the system of record that envelope values can be verified against
- Send user-entered connected field values from envelopes for the external service to verify. The service verifies the values against the system of record and sends Docusign the results.

The other component is a [Connected Fields API](https://developers.docusign.com/docs/connected-fields-api/) integration. The integration sends requests to Docusign API endpoints to:

- Retrieve a list of connected fields available for use in envelopes sent from your Docusign account. The available connected fields depend on which connected fields extension apps are installed to your account.
- Construct and send eSignature envelopes that include connected fields

The sequence of calls to extension app API service endpoints and Docusign API endpoints in this scenario is:

In this diagram, steps 1 through 6 are setup steps that do not need to be repeated unless a data model change affects the objects and properties available for verification. Steps 7 through 12 occur every time an envelope is generated.

**Note:** To explore connected fields extension app requests and responses, you can clone our connected fields [reference implementation opens in a new tab](https://github.com/docusign/extension-app-connected-fields-reference-implementation/) from GitHub, run it locally, or deploy it to the cloud, and follow the readme instructions to send test requests.

## Implement connected fields extension app logic

Your extension app API service must return information to Docusign about which values can be verified against your system of record. For the example use case, the mapping between connected fields to be displayed in envelopes and the external data source properties against which they will be verified might be:

| **Envelope connected field** | **External data source property** | **External data type** |
| --- | --- | --- |
| Account Number | `account_num` | `string` |
| Source Fund | `source_fund` | `string` |
| Destination Fund | `destination_fund` | `string` |
| Amount to Transfer | `balance` | `double` |
| Transfer Date | `transferDate` | `datetime` |
| Type of Account | `typeOfAccount` | `enum` |
| Owner Email | `email` | `object` |
| Account Owner Name | `ownername` | `object` |

The extension app must also process verification requests for user-entered connected field values and return the results.

The three requests from Docusign that your extension app must respond to appear in the next sections, along with sample responses. Detailed information about the request and response formats appears in the [connected fields extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/).

### Get Type Names request

Docusign sends this request to obtain a list of objects in your system of record that support verification. An example [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names) response for the use case in this blog post would be:

```
{
  "typeNames": [
    {
      "typeName": "EmailAddress",
      "label": "Email Address"
    },
    {
      "typeName": "OwnerName",
      "label": "Account Owner Name"
    },
    {
      "typeName": "Account",
      "label": "Account Info"
    }
  ]
}
```

In the response above, the object that envelope values are to be verified against is `Account`. The `EmailAddress` and `OwnerName` types contain properties that will be included as embedded objects within the `Account` type.

### Get Type Definitions request

Docusign sends this request to retrieve definitions of the properties in your system of record that support verification. The [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) response must follow the [Concerto opens in a new tab](https://concerto.accordproject.org/docs/intro/) data model and include [decorators opens in a new tab](https://concerto.accordproject.org/docs/design/specification/model-decorators) that mark objects as verifiable. The `VerifiableType` decorator on an object indicates that envelope values can be verified against its properties. The properties that a **Get Type Definitions** response includes for an object will be rendered as a *field group* in eSignature envelopes. A verification request will be sent only when all required values in the field group have been populated, or when one of the values is changed. The `IsRequiredForVerifyingType` decorator indicates that the connected field associated with the property must be populated in an envelope before a verification request will be sent to the external system.

An example **Get Type Definitions** response for the transfer authorization use case would be:

```
{
  "declarations": [
    {
      "$class": "concerto.metamodel@1.0.0.ConceptDeclaration",
      "name": "EmailAddress",
      "isAbstract": false,
      "properties": [
        {
          "$class": "concerto.metamodel@1.0.0.StringProperty",
          "name": "email",
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Email Address"
                }
              ]
            }
          ],
          "lengthValidator": {
            "$class": "concerto.metamodel@1.0.0.StringLengthValidator",
            "maxLength": 256
          }
        }
      ],
      "decorators": [
        {
          "$class": "concerto.metamodel@1.0.0.Decorator",
          "name": "VerifiableType"
        },
        {
          "$class": "concerto.metamodel@1.0.0.Decorator",
          "name": "Term",
          "arguments": [
            {
              "$class": "concerto.metamodel@1.0.0.DecoratorString",
              "value": "Email Address"
            }
          ]
        }
      ]
    },
    {
      "$class": "concerto.metamodel@1.0.0.ConceptDeclaration",
      "name": "OwnerName",
      "isAbstract": false,
      "properties": [
        {
          "$class": "concerto.metamodel@1.0.0.StringProperty",
          "name": "ownername",
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Account Owner Name"
                }
              ]
            }
          ],
          "lengthValidator": {
            "$class": "concerto.metamodel@1.0.0.StringLengthValidator",
            "maxLength": 256
          }
        }
      ],
      "decorators": [
        {
          "$class": "concerto.metamodel@1.0.0.Decorator",
          "name": "VerifiableType"
        },
        {
          "$class": "concerto.metamodel@1.0.0.Decorator",
          "name": "Term",
          "arguments": [
            {
              "$class": "concerto.metamodel@1.0.0.DecoratorString",
              "value": "Account Owner Name"
            }
          ]
        }
      ]
    },
    {
      "$class": "concerto.metamodel@1.0.0.ConceptDeclaration",
      "name": "Account",
      "isAbstract": false,
      "properties": [
        {
          "$class": "concerto.metamodel@1.0.0.StringProperty",
          "name": "account_num",
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Account Number"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.ObjectProperty",
          "name": "ownername",
          "type": {
            "$class": "concerto.metamodel@1.0.0.TypeIdentifier",
            "name": "OwnerName"
          },
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Account Owner Name"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.ObjectProperty",
          "name": "email",
          "type": {
            "$class": "concerto.metamodel@1.0.0.TypeIdentifier",
            "name": "EmailAddress"
          },
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Owner Email"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.StringProperty",
          "name": "source_fund",
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Source Fund"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.StringProperty",
          "name": "destination_fund",
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Destination Fund"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.DoubleProperty",
          "name": "balance",
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Amount to Transfer"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.DateTimeProperty",
          "name": "transferDate",
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Transfer Date"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.ObjectProperty",
          "name": "typeOfAccount",
          "type": {
            "$class": "concerto.metamodel@1.0.0.TypeIdentifier",
            "name": "TypeOfAccount"
          },
          "isArray": false,
          "isOptional": false,
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "IsRequiredForVerifyingType"
            },
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Type of Account"
                }
              ]
            }
          ]
        }
      ],
      "decorators": [
        {
          "$class": "concerto.metamodel@1.0.0.Decorator",
          "name": "VerifiableType"
        },
        {
          "$class": "concerto.metamodel@1.0.0.Decorator",
          "name": "Term",
          "arguments": [
            {
              "$class": "concerto.metamodel@1.0.0.DecoratorString",
              "value": "Account Info"
            }
          ]
        }
      ]
    },
    {
      "$class": "concerto.metamodel@1.0.0.EnumDeclaration",
      "name": "TypeOfAccount",
      "properties": [
        {
          "$class": "concerto.metamodel@1.0.0.EnumProperty",
          "name": "brokerage",
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Brokerage"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.EnumProperty",
          "name": "cash_management",
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "Cash Management"
                }
              ]
            }
          ]
        },
        {
          "$class": "concerto.metamodel@1.0.0.EnumProperty",
          "name": "ira",
          "decorators": [
            {
              "$class": "concerto.metamodel@1.0.0.Decorator",
              "name": "Term",
              "arguments": [
                {
                  "$class": "concerto.metamodel@1.0.0.DecoratorString",
                  "value": "IRA"
                }
              ]
            }
          ]
        }
      ],
      "decorators": [
        {
          "$class": "concerto.metamodel@1.0.0.Decorator",
          "name": "Term",
          "arguments": [
            {
              "$class": "concerto.metamodel@1.0.0.DecoratorString",
              "value": "Type of Account"
            }
          ]
        }
      ]
    }
  ]
}
```

### Verify request

Docusign sends this request when a user has populated all required connected fields in an envelope. When it receives this request, the extension app must apply business logic to the user-entered values to determine whether verification passes. The app should return the verification result, messages for the signing UI to display to the user, and autofill values if appropriate.

An example [Verify](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#verify) response for envelope values that failed verification, including a suggested autofill value, would be:

```
{
  "verified": false,
  "verifyResponseMessage": "Verification failed.",
  "verifyFailureReason": "The account has no position in the supplied source fund. It has position in the suggested fund. Please verify again.",
  "verificationResultCode": "VALIDATION_ERRORS",
  "suggestions": [
    {
      "account_num": "123456789",
      "source_fund": "Corporate Bond Fund",
      "destination_fund": "Growth Stock Fund",
      "balance": 10000.00,
      "transfer_date": "2025-03-05T00:00:00.000Z",
      "typeOfAccount": "brokerage",
      "email": "sally.signer@email.com",
      "ownername": "Sally Signer"
    }
  ]
}
```

**Note:** Values for all connected fields in a field group must be supplied in the `suggestions` array. For fields where no autofill value is being returned, the property should be populated with the user-entered value from the original **Verify** request.

### IT infrastructure to support the extension app

When setting up the infrastructure on the system that will host the extension app, consider the following features that you may need to implement:

- [API proxy](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/api-proxy/): Required if requests from Docusign are not in the format required by the extension app's API endpoints, or if the responses are not in the format that Docusign expects.
- [Authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/): The extension app must support the authorization parameters that Docusign sends and meet the authorization response requirements.
- [Network configuration](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/network-configuration/): Review the network setup required to ensure that Docusign can communicate successfully with the extension app.

## Register and test the extension app

### Registration

Any extension app that will be called from Docusign agreement processes must be registered with Docusign. Registration provides Docusign with information it needs to obtain authorization from the extension app and send requests to its endpoints.

In addition, registration sets the distribution options. If you want the extension app to be available only to users in your organization or to specific Docusign accounts, then register it as a private extension app. To make it available to any Docusign account, register it as public. See [Choosing private distribution instead of public](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/) for more information. You can also determine the regions in which the extension app will be available. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for a list of supported regions and additional details.

You can register the extension app in the [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/) using [a guided, form-based UI](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/) or by uploading a JSON [extension app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/). Below is a sample app manifest file for an extension app that implements connected fields. Authorization parameters, including endpoint URLs, appear in the `connections` object. The `extensions` object specifies that this is a connected fields extension. The `actions` object defines each request type that Docusign will send to the external service, including the endpoint URL. See [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for details about the file structure and properties.

```
{
  "name": "Transfer Authorization",
  "publicationRegions": [
    "US"
  ],
  "distribution": "PRIVATE",
  "description": {
    "short": "Perform real-time custom data verification.",
    "long": "Send user-supplied envelope values to an external service for verification against a system of record."
  },
  "publisher": {
    "name": "Sample Extension App Inc.",
    "email": "info@samplecompany.com",
    "phone": "111-222-3333",
    "website": "https://www.info@samplecompany.com/"
  },
  "termsOfServiceUrl": "https://www.samplecompany.com/tos",
  "privacyUrl": "https://www.samplecompany.com/privacy-security",
  "supportUrl": "https://www.samplecompany.com/support",
  "signupUrl": "https://www.samplecompany.com/signup",
  "icon": {
    "data": "iVBORw…ggg==",
    "mediaType": "image/png"
  },
  "connections": [
    {
      "name": "authentication",
      "description": "Secure connection to Sample Extension App",
      "type": "oauth2",
      "params": {
        "provider": "CUSTOM",
        "scopes": [],
        "clientId": "8d606a57-xxxx-xxxx-xxxx-219e80c7ed16",
        "clientSecret": "lfvZIUH…leaGCreU=",
        "customConfig": {
          "tokenUrl": "https://sampleextensionapp.com/api/oauth/token",
          "authorizationUrl": "https://sampleextensionapp.com/api/oauth/authorize",
          "authorizationParams": {
            "access_type": "offline",
            "prompt": "consent"
          },
          "authorizationMethod": "header",
          "scopeSeparator": " ",
          "requiredScopes": []
        }
      }
    }
  ],
  "extensions": [
    {
      "name": "Connected Fields Extension",
      "description": "Performs real-time custom data verification",
      "template": "ConnectedFields.Version1.ConnectedFields",
      "actionReferences": [
        "Verify Action",
        "GetTypeNames Action",
        "GetTypeDefinitions Action"
      ]
    }
  ],
  "actions": [
    {
      "name": "Verify Action",
      "description": "Sends envelope values for verification by an external service",
      "template": "ConnectedFields.Version1.Verify",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://sampleextensionapp.com/api/connectedfields/verify"
      }
    },
    {
      "name": "GetTypeNames Action",
      "description": "Gets the type names in a system of record",
      "template": "DataIO.Version6.GetTypeNames",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://sampleextensionapp.com/api/connectedfields/getTypeNames"
      }
    },
    {
      "name": "GetTypeDefinitions Action",
      "description": "Gets the type definitions in a system of record",
      "template": "DataIO.Version6.GetTypeDefinitions",
      "connectionsReference": "authentication",
      "params": {
        "uri": "https://sampleextensionapp.com/api/connectedfields/getTypeDefinitions"
      }
    }
  ],
  "screenshots": []
}
```

### Testing

After you've registered your extension app with Docusign, you can use these Developer Console testing features to make sure that Docusign can access the extension app:

- [Connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test): Verifies that Docusign can obtain authorization from the extension app
- [Extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test): Verify that Docusign can send requests to the extension app or API proxy endpoints and process the responses
- [Functional test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/connected-fields-envelope/): Confirms that verification requests work when invoked by a user populating connected fields in an envelope

## Implement a Connected Fields API integration

To create and send envelopes with connected fields programmatically, your API integration must implement, at minimum, two API requests to Docusign. These are described in the next sections.

### Request to retrieve connected fields available in the account

A Connected Fields API [TabInfo:GetConnectedFieldsTabGroups](https://developers.docusign.com/docs/connected-fields-api/reference/connectedfields/tabinfo/getconnectedfieldstabgroups/) request retrieves information about the connected fields extension apps installed and connected to your account, and the required connected fields associated with each extension app.

The response below reflects the connected fields from the example use case. The next section lists the response values that must be included in the request to create an envelope.

```
[
  {
    "appId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
    "tabs": [
      {
        "extensionData": {
          "extensionGroupId": "6c065fef-xxxx-xxxx-xxxx-3c285cf9e306",
          "actionInputKey": "email",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "EmailAddress",
            "supportedOperation": "VerifyType",
            "propertyName": "email",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/EmailAddress/verify"
          }
        },
        "tabType": "text",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.EmailAddress[0].email"
      },
      {
        "extensionData": {
          "extensionGroupId": "1174f397-xxxx-xxxx-xxxx-86d813afe0f4",
          "actionInputKey": "ownername",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "OwnerName",
            "supportedOperation": "VerifyType",
            "propertyName": "ownername",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/OwnerName/verify"
          }
        },
        "tabType": "text",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.OwnerName[0].ownername"
      },
      {
        "extensionData": {
          "extensionGroupId": "a2f6c6ef-xxxx-xxxx-xxxx-4769923b0595",
          "actionInputKey": "account_num",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "Account",
            "supportedOperation": "VerifyType",
            "propertyName": "account_num",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/Account/verify"
          }
        },
        "tabType": "text",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.Account[0].account_num"
      },
      {
        "extensionData": {
          "extensionGroupId": "a2f6c6ef-xxxx-xxxx-xxxx-4769923b0595",
          "actionInputKey": "source_fund",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "Account",
            "supportedOperation": "VerifyType",
            "propertyName": "source_fund",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/Account/verify"
          }
        },
        "tabType": "text",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.Account[0].source_fund"
      },
      {
        "extensionData": {
          "extensionGroupId": "a2f6c6ef-xxxx-xxxx-xxxx-4769923b0595",
          "actionInputKey": "destination_fund",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "Account",
            "supportedOperation": "VerifyType",
            "propertyName": "destination_fund",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/Account/verify"
          }
        },
        "tabType": "text",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.Account[0].destination_fund"
      },
      {
        "extensionData": {
          "extensionGroupId": "a2f6c6ef-xxxx-xxxx-xxxx-4769923b0595",
          "actionInputKey": "balance",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "Account",
            "supportedOperation": "VerifyType",
            "propertyName": "balance",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/Account/verify"
          }
        },
        "tabType": "text",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.Account[0].balance"
      },
      {
        "extensionData": {
          "extensionGroupId": "a2f6c6ef-xxxx-xxxx-xxxx-4769923b0595",
          "actionInputKey": "transferDate",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "Account",
            "supportedOperation": "VerifyType",
            "propertyName": "transferDate",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/Account/verify"
          }
        },
        "tabType": "date",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.Account[0].transferDate"
      },
      {
        "extensionData": {
          "extensionGroupId": "a2f6c6ef-xxxx-xxxx-xxxx-4769923b0595",
          "actionInputKey": "typeOfAccount",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "Account",
            "supportedOperation": "VerifyType",
            "propertyName": "typeOfAccount",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/Account/verify"
          }
        },
        "tabType": "radiogroup",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.Account[0].typeOfAccount",
        "radios": [
          "brokerage",
          "cash_management",
          "ira"
        ]
      },
      {
        "extensionData": {
          "extensionGroupId": "a2f6c6ef-xxxx-xxxx-xxxx-4769923b0595",
          "actionInputKey": "ownername/ownername",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "Account",
            "supportedOperation": "VerifyType",
            "propertyName": "ownername",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/Account/verify"
          }
        },
        "tabType": "text",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.Account[0].ownername.ownername"
      },
      {
        "extensionData": {
          "extensionGroupId": "a2f6c6ef-xxxx-xxxx-xxxx-4769923b0595",
          "actionInputKey": "email/email",
          "publisherName": "Sample Extension App Inc.",
          "applicationName": "Transfer Authorization",
          "actionContract": "",
          "extensionName": "",
          "actionName": "",
          "extensionPolicy": "None",
          "requiredForExtension": true,
          "connectedFieldsData": {
            "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0",
            "typeName": "Account",
            "supportedOperation": "VerifyType",
            "propertyName": "email",
            "supportedUri": "/connected-data/v1/connected-objects/com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0/Account/verify"
          }
        },
        "tabType": "text",
        "tabLabel": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsIjg1NGQxNGY5LTY4NmMtNGIzYi1hNzY0LTk4MDAzOTI4ZGFjYSIsMF0@1.0.0.Account[0].email.email"
      }
    ]
  }
]
```

See the Developer Center for complete [Connected Fields API documentation](https://developers.docusign.com/docs/connected-fields-api/), including information about authentication, the endpoint, and code examples.

### Request to create envelope with connected fields

To create an envelope with connected fields, you can use an eSignature REST API [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) request. The request includes a `tabs` object that defines all the envelope fields that a user can populate. This includes standard fields, such as a signature field (`signHereTab` type), and connected fields whose values will be verified against the system of record.

To identify a field as a connected field, include an `extensionData` object in the field definition. The properties in this object must be populated with these values from the `TabInfo:GetConnectedFieldsTabGroups` response:

| **extensionData property** | **Description** |
| --- | --- |
| `applicationId` | The unique ID associated with the extension app. This ID is assigned when an extension app is [registered](https://developers.docusign.com/extension-apps/build-an-extension-app/register/) with Docusign. This value should be the same for each connected field in a field group. |
| `applicationName` | The extension app name that was provided when it was registered. This value should be the same for each connected field in a field group.  **Note:** If the extension app name is changed, any API requests that reference this name must be updated to use the new name. |
| `requiredForExtension` | `true` if the field must be populated in the signing UI before Docusign sends a verification request to the external system. |
| `extensionPolicy` | This value should be set to `None`. Additional values will be supported in a future release. |
| `connectedFieldsData.typeSystemNamespace` | The fully qualified namespace for the type system being verified. This value should be the same for each connected field in a field group.  **Note:** If the extension app's connection changes, for example, due to a reinstall of the extension app to the account, the `typeSystemNamespace` must be updated in `Envelopes:create` requests. Send a `TabInfo:GetConnectedFieldsTabGroups` request, extract the new `typeSystemNamespace` value, and use it in `Envelopes:create` requests going forward. If this value is not updated for the new connection, a **Verification failed** message will appear in the signing UI when verification is triggered. See [Connection behaviors and best practices](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#connection-behaviors-and-best-practices) for more information. |
| `connectedFieldsData.typeName` | The name of the type on the external system that this value will be verified against. This is the same as the `typeName` that the extension app returned to Docusign in its response to the [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names) request. This value should be the same for each connected field in a field group.  **Note:** For embedded objects, the `TabInfo:GetConnectedFieldsTabGroups` response includes two definitions — one for the type and one for the embedded object property within the type to be verified. In the example response shown above, the connected fields group for the `Account` type includes two embedded object properties: `ownername` and `email`. When sending the `Envelopes:create` request, do not use the values from the type definition. Instead, include the values from the embedded object property definition, which will have the `typeName` of the type in which the object is embedded. In this example, when defining a connected field for `email`, you would use the values from the `TabInfo:GetConnectedFieldsTabGroups` response where the `property` is `email` and `typeName` is `Account`. |
| `connectedFieldsData.propertyName` | The name of the property on the external system that this value will be verified against. This is the same value as the `name` that the extension app returned to Docusign in its response to the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) request. |
| `extensionGroupId` | A unique UUID for the field group. All connected fields in the same group must have the same value for this property.  **Note:** The `extensionGroupId` is unique in each `TabInfo:GetConnectedFieldsTabGroups` response. It is not necessary to update this value in the `Envelopes:create` request after sending a new `TabInfo:GetConnectedFieldsTabGroups` request. |
| `actionInputKey` | The input data key required for data verification. |

Below is an `Envelopes:create` request that incorporates values from the example `TabInfo:GetConnectedFieldsTabGroups` response.

```
{
  "emailSubject": "Please sign this fund transfer authorization",
  "documents": [
    {
      "documentBase64": "JVBERi0...JUVPRgo=",
      "name": "Transfer Request",
      "fileExtension": "pdf",
      "documentId": "1"
    }
  ],
  "recipients": {
    "signers": [
      {
        "email": "sallysigner@email.com",
        "name": "Sally Signer",
        "recipientId": "1",
        "routingOrder": "1",
        "tabs": {
          "signHereTabs": [
            {
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Signature",
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "15",
              "anchorXOffset": "22"
            }
          ],
          "dateSignedTabs": [
            {
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Date",
              "anchorCaseSensitive": true,
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "0",
              "anchorXOffset": "22",
              "value": "[todaysDate]"
            }
          ],
          "textTabs": [
            {
              "tabLabel": "accountOwnerName",
              "tooltip": "Account Owner Name",
              "extensionData": {
                "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
		   "applicationName": "Transfer Authorization",
                "requiredForExtension": true,
                "extensionPolicy": "None",
                "connectedFieldsData": {
                  "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                  "typeName": "Account",
                  "propertyName": "ownername"
                },
                "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                "actionInputKey": "ownername/ownername"
              },
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Name",
              "width": "75",
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "-5",
              "anchorXOffset": "22"
            },
            {
              "tabLabel": "emailAddress",
              "tooltip": "Email Address",
              "extensionData": {
                "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
		   "applicationName": "Transfer Authorization",
                "requiredForExtension": true,
                "extensionPolicy": "None",
                "connectedFieldsData": {
                  "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                  "typeName": "Account",
                  "propertyName": "email"
                },
                "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                "actionInputKey": "email/email"
              },
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Email",
              "width": "100",
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "-5",
              "anchorXOffset": "22"
            },
            {
              "tabLabel": "accountNumber",
              "tooltip": "Account Number",
              "extensionData": {
                "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
		   "applicationName": "Transfer Authorization",
                "requiredForExtension": true,
                "extensionPolicy": "None",
                "connectedFieldsData": {
                  "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                  "typeName": "Account",
                  "propertyName": "account_num"
                },
                "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                "actionInputKey": "account_num"
              },
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Account number",
              "width": "75",
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "-5",
              "anchorXOffset": "22"
            },
            {
              "tabLabel": "sourceFund",
              "tooltip": "Source Fund",
              "extensionData": {
                "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
		   "applicationName": "Transfer Authorization",
                "requiredForExtension": true,
                "extensionPolicy": "None",
                "connectedFieldsData": {
                  "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                  "typeName": "Account",
                  "propertyName": "source_fund"
                },
                "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                "actionInputKey": "source_fund"
              },
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Source fund",
              "width": "150",
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "-5",
              "anchorXOffset": "22"
            },
            {
              "tabLabel": "destinationFund",
              "tooltip": "Destination Fund",
              "extensionData": {
                "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
		   "applicationName": "Transfer Authorization",
                "requiredForExtension": true,
                "extensionPolicy": "None",
                "connectedFieldsData": {
                  "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                  "typeName": "Account",
                  "propertyName": "destination_fund"
                },
                "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                "actionInputKey": "destination_fund"
              },
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Destination fund",
              "width": "150",
              "anchorCaseSensitive": true,
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "-5",
              "anchorXOffset": "22"
            },
            {
              "tabLabel": "amountToTransfer",
              "tooltip": "Amount to Transfer",
              "extensionData": {
                "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
		   "applicationName": "Transfer Authorization",
                "requiredForExtension": true,
                "extensionPolicy": "None",
                "connectedFieldsData": {
                  "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                  "typeName": "Account",
                  "propertyName": "balance"
                },
                "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                "actionInputKey": "balance"
              },
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Amount to transfer",
              "width": "100",
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "-5",
              "anchorXOffset": "22"
            }
          ],
          "dateTabs": [
            {
              "tabLabel": "transferDate",
              "tooltip": "Transfer Date",
              "extensionData": {
                "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
		   "applicationName": "Transfer Authorization",
                "requiredForExtension": true,
                "extensionPolicy": "None",
                "connectedFieldsData": {
                  "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                  "typeName": "Account",
                  "propertyName": "transferDate"
                },
                "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                "actionInputKey": "transferDate"
              },
              "documentId": "1",
              "pageNumber": 1,
              "anchorString": "Transfer date",
              "width": "75",
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "-5",
              "anchorXOffset": "22"
            }
          ],
          "checkboxTabs": [
            {
              "tabLabel": "prospectus",
              "anchorString": "Send prospectus for destination fund",
              "anchorHorizontalAlignment": "right",
              "anchorYOffset": "-5",
              "anchorXOffset": "22",
              "tabGroupLabels": [
                "checkboxgroup1"
              ]
            }
          ],
          "radioGroupTabs": [
            {
              "tabLabel": "typeOfAccount",
              "tooltip": "Type of Account",
              "extensionData": {
                "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
		   "applicationName": "Transfer Authorization",
                "requiredForExtension": true,
                "extensionPolicy": "None",
                "connectedFieldsData": {
                  "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                  "typeName": "Account",
                  "propertyName": "typeOfAccount"
                },
                "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                "actionInputKey": "typeOfAccount"
              },
              "documentId": "1",
              "pageNumber": 1,
              "radios": [
                {
                  "tabLabel": "typeOfAccount",
                  "value": "brokerage",
                  "extensionData": {
                    "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
			"applicationName": "Transfer Authorization",
                    "requiredForExtension": true,
                    "extensionPolicy": "None",
                    "connectedFieldsData": {
                      "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                      "typeName": "Account",
                      "propertyName": "typeOfAccount"
                    },
                    "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                    "actionInputKey": "typeOfAccount"
                  },
                  "pageNumber": 1,
                  "documentId": "1",
                  "anchorString": "Brokerage",
                  "anchorHorizontalAlignment": "left",
                  "anchorYOffset": "-6",
                  "anchorXOffset": "-30"
                },
                {
                  "tabLabel": "typeOfAccount",
                  "value": "cash_management",
                  "extensionData": {
                    "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
			"applicationName": "Transfer Authorization",
                    "requiredForExtension": true,
                    "extensionPolicy": "None",
                    "connectedFieldsData": {
                      "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                      "typeName": "Account",
                      "propertyName": "typeOfAccount"
                    },
                    "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                    "actionInputKey": "typeOfAccount"
                  },
                  "pageNumber": 1,
                  "documentId": "1",
                  "anchorString": "Cash management",
                  "anchorHorizontalAlignment": "left",
                  "anchorYOffset": "-5",
                  "anchorXOffset": "-30"
                },
                {
                  "tabLabel": "typeOfAccount",
                  "value": "ira",
                  "extensionData": {
                    "applicationId": "19eaa3f4-xxxx-xxxx-xxxx-034c47986310",
			"applicationName": "Transfer Authorization",
                    "requiredForExtension": true,
                    "extensionPolicy": "None",
                    "connectedFieldsData": {
                      "typeSystemNamespace": "com.docusign.connecteddata._WyIxY2FmMmNjOS1iNjAyLTRjMjgtOTAyMy0xNGQ2M2MxY2VkNmIiLDAsIjE5ZWFhM2Y0LTEyNTUtNGJmYi05ZmE0LTAzNGM0Nzk4NjMxMCIsImU1OTA1MjZhLTBkY2ItNGJiNC1hN2E5LTRkZDNiODFjYTU2NSIsMF0@1.0.0",
                      "typeName": "Account",
                      "propertyName": "typeOfAccount"
                    },
                    "extensionGroupId": "8c7abecd-xxxx-xxxx-xxxx-xxxx-7cb462366bb6",
                    "actionInputKey": "typeOfAccount"
                  },
                  "pageNumber": 1,
                  "documentId": "1",
                  "anchorString": "IRA",
                  "anchorHorizontalAlignment": "left",
                  "anchorYOffset": "-4",
                  "anchorXOffset": "-30"
                }
              ]
            }
          ]
        }
      }
    ]
  },
  "status": "sent"
}
```

See the Developer Center for complete [eSignature API documentation](https://developers.docusign.com/docs/esign-rest-api/), including information about authentication, the endpoints, and code examples.

## Move to production

To use a custom data verification implementation in production, you must complete the following:

- Connected fields extension app: [Submit the app for Docusign review](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/). After Docusign approves it, you can publish it to make it available for use in the production environment.
- Connected Fields API integration: [Request a Go-Live review](https://developers.docusign.com/platform/go-live/). After the integration passes review, you can select a production account into which to promote the integration.

**Note:** You must be a Docusign partner in order to publish a public extension app. Production API integrations must belong to a paid or a partner production Docusign account. See [Join now](https://partners.docusign.com/s/join-now) for details on how to join the Docusign partner program.

## Get started with custom data verification

Get started with your own custom data verification solution to streamline agreement processing. The [Docusign for Developers](https://www.docusign.com/blog/docusign-discover-2024) suite of tools provides everything you need to develop an application tailored to your organization's or your customers' specific business cases. The resulting workflow improvements will enhance efficiency and customer satisfaction. To take the first steps, visit the [Docusign Developer Center](https://developers.docusign.com) to sign up for a free developer account and learn more, or explore the benefits of the [Docusign Partner Program](https://partners.docusign.com/s/).

## Additional resources

- Read an [introduction](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/) to the connected fields extension.
- Get details about connected fields extension [requests and responses](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/).
- Clone the connected fields [reference implementation repo opens in a new tab](https://github.com/docusign/extension-app-connected-fields-reference-implementation/) to test requests and responses.
- See the example code in the Connected Fields API [how-to guide](https://developers.docusign.com/docs/connected-fields-api/send-envelope-with-data-verification-fields/).
- Watch a [video opens in a new tab](https://bcove.video/4l51CpM) about integrating data verification using the Connected Fields API.

![Author Julie Gordon](https://images.ctfassets.net/9pvazpst9iwl/6pWetjZY1gCV6eGt1gtX4J/66fc155e0053c16de36ebc64a6baf9c2/JGordonNewPhoto400x400.jpeg?fm=avif&q=90&w=500)

Julie GordonSr. Programmer Writer

Julie Gordon joined Docusign in 2021. As a member of the Developer Content and Advocacy team, she creates content, media, and code to help developers learn how to use Docusign technology. With a background in software quality assurance and technical writing, she produces meticulously researched and tested documentation of APIs, developer tools, and low-code/no-code platforms.

[More posts from this author](https://www.docusign.com/blog/author/julie-gordon)

## Table of contents

- [How to build custom data verification for eSignature flows](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#how-to-build-custom-data-verification-for-esignature-flows)
- [Implementation components](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#implementation-components)

- [Implement connected fields extension app logic](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#implement-connected-fields-extension-app-logic)

- [Register and test the extension app](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#register-and-test-the-extension-app)

- [Implement a Connected Fields API integration](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#implement-a-connected-fields-api-integration)
- [Move to production](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#move-to-production)

- [Get started with custom data verification](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#get-started-with-custom-data-verification)
- [Additional resources](https://www.docusign.com/blog/developers/custom-data-verification-connected-fields-api#additional-resources)

Share

[Share to LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Fcustom-data-verification-connected-fields-api "Share to LinkedIn")[Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Fcustom-data-verification-connected-fields-api "Share to Facebook")[Share to X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Fcustom-data-verification-connected-fields-api&text=From NIGO to STP: A developer's guide to custom data verification and the Connected Fields API&hashtags=Docusign "Share to X")

Related posts

- [Developers](https://www.docusign.com/blog/developers)Published Jun 16, 2026

  [## How to Configure and Publish an Azure Custom Extension App for Docusign IAM](https://www.docusign.com/blog/developers/configure-deploy-azure-custom-extension-app-docusign-iam)

  ![Author Mohamed Ali](https://images.ctfassets.net/9pvazpst9iwl/66eZQrBN42mOTqQ3MTt4tb/1792588fa2fb4e5fe93b8a4a8481c565/mohamed_ali.jpg?fm=avif&q=90&w=500)

  Mohamed Ali

  [![Featured image for Dobby blog](https://images.ctfassets.net/9pvazpst9iwl/grPE0gIUY4kgyWVIUbgz2/4f435a93c25d796fd91b609d4274afe1/coding-elf-blog-visual.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/configure-deploy-azure-custom-extension-app-docusign-iam)
- [Developers](https://www.docusign.com/blog/developers)Published May 21, 2026

  [## How Developers Can Build Agentic Agreement Workflows on Docusign IAM](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows)

  ![Author Larry Jin](https://images.ctfassets.net/9pvazpst9iwl/5XbuJzjmhsmfVi2Lj9nWwu/f3ae8c298109dd95f1bc755cf0a9ba01/Larry_Jin?fm=avif&q=90&w=500)

  Larry Jin

  [![](https://images.ctfassets.net/9pvazpst9iwl/34FVWrGquLXSTp0qOJcoJY/47b54b4d21c68c896e88cbd3865d6c4d/Momentum26-Developer-Launch_26-05_Blog_My-Agents_1200x900_EN.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows)
- [Developers](https://www.docusign.com/blog/developers)Published May 21, 2026

  [## How to design a verification-first financial onboarding workflow using Docusign IAM and J.P. Morgan Payments](https://www.docusign.com/blog/developers/verification-first-financial-onboarding-docusign-jp-morgan-payments)

  ![Author Niani Byrd](https://images.ctfassets.net/9pvazpst9iwl/KMDcdizn2FYO7YIZgMxHI/e727a59804a2871e7e24a150996465e9/NianiByrd.jpg?fm=avif&q=90&w=500)

  Niani Byrd

  [![](https://images.ctfassets.net/9pvazpst9iwl/6aqrdBpTJUvnQXmLhlxzC6/39964dfa4ffc6e10864f3ed3281d8863/Mo26-Developers-Session-Workflow_26-05_Blog_1200x900_EN__1_.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/verification-first-financial-onboarding-docusign-jp-morgan-payments)

[Developers](https://www.docusign.com/blog/developers)Published Jun 16, 2026

[## How to Configure and Publish an Azure Custom Extension App for Docusign IAM](https://www.docusign.com/blog/developers/configure-deploy-azure-custom-extension-app-docusign-iam)

![Author Mohamed Ali](https://images.ctfassets.net/9pvazpst9iwl/66eZQrBN42mOTqQ3MTt4tb/1792588fa2fb4e5fe93b8a4a8481c565/mohamed_ali.jpg?fm=avif&q=90&w=500)

Mohamed Ali

[![Featured image for Dobby blog](https://images.ctfassets.net/9pvazpst9iwl/grPE0gIUY4kgyWVIUbgz2/4f435a93c25d796fd91b609d4274afe1/coding-elf-blog-visual.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/configure-deploy-azure-custom-extension-app-docusign-iam)

[Developers](https://www.docusign.com/blog/developers)Published May 21, 2026

[## How Developers Can Build Agentic Agreement Workflows on Docusign IAM](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows)

![Author Larry Jin](https://images.ctfassets.net/9pvazpst9iwl/5XbuJzjmhsmfVi2Lj9nWwu/f3ae8c298109dd95f1bc755cf0a9ba01/Larry_Jin?fm=avif&q=90&w=500)

Larry Jin

[![](https://images.ctfassets.net/9pvazpst9iwl/34FVWrGquLXSTp0qOJcoJY/47b54b4d21c68c896e88cbd3865d6c4d/Momentum26-Developer-Launch_26-05_Blog_My-Agents_1200x900_EN.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows)

[Developers](https://www.docusign.com/blog/developers)Published May 21, 2026

[## How to design a verification-first financial onboarding workflow using Docusign IAM and J.P. Morgan Payments](https://www.docusign.com/blog/developers/verification-first-financial-onboarding-docusign-jp-morgan-payments)

![Author Niani Byrd](https://images.ctfassets.net/9pvazpst9iwl/KMDcdizn2FYO7YIZgMxHI/e727a59804a2871e7e24a150996465e9/NianiByrd.jpg?fm=avif&q=90&w=500)

Niani Byrd

[![](https://images.ctfassets.net/9pvazpst9iwl/6aqrdBpTJUvnQXmLhlxzC6/39964dfa4ffc6e10864f3ed3281d8863/Mo26-Developers-Session-Workflow_26-05_Blog_1200x900_EN__1_.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/verification-first-financial-onboarding-docusign-jp-morgan-payments)

## Docusign IAM is the agreement platform your business needs

[Start for Free](https://trial.docusign.com)[Explore Docusign IAM](https://www.docusign.com/intelligent-agreement-management)

![Person smiling while presenting](https://images.ctfassets.net/9pvazpst9iwl/1gOiICnusnBqWxB11vmsFs/99a7ee68a05fa07fe6e5e35186e45394/smiling-woman-in-bright-sweater-presents-charts-on-laptop.png?fm=avif&q=90&w=500)
