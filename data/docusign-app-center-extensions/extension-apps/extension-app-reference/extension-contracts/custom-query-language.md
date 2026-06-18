---
title: Custom query language reference
source_url: https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension App Reference
- Extension App Reference
- Extension Contracts
- Extension Contracts
- Custom Query Language
scraped_at: '2026-06-18T19:51:53Z'
---

# Custom query language reference

To implement the `DataIO.Version6.SearchRecords` action, you must translate a query expression from the Docusign custom query language into one supported by your external system. Docusign established this custom language in order to maintain flexibility without depending on any specific external system. This reference page shows how the query objects are structured.

- [IQuery object](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/#iquery-object)
- [IQueryFilter object](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/#iquery-filter-object)
- [IComparisonOperation object](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/#icomparisonoperation-object)
- [IOperand object](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/#ioperand-object)
- [ILogicalOperation object](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/#ilogicaloperation-object)

You can also see an [Example](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/#example) of how to use build a query using these objects.

Note that each object contains a `$class` property that identifies its type. This enables your API proxy to recognize the object type and transform it to the associated type in a different query language.

### IQuery object

The `IQuery` object represents a query of the external system. The query:

- Selects the properties specified by `attributesToSelect...`
- From the table specified by the from `property...`
- And then filters the records based on the `queryFilter`

| **Property** | **Type** | **Description** |
| --- | --- | --- |
| `$class` | `string` | Identifies the object as a query. Will always be:`com.docusign.connected.data.queries@1.0.0.Query` |
| `attributesToSelect` | `string[]` | The list of attributes to select from the table to query. These values correspond to the attributes returned by the `GetTypeDefinitions` action. |
| `from` | `string` | Represents the table to query in the external system. This name corresponds to a record type returned by the `GetTypeNames` action. |
| `queryFilter` | `IQueryFilter` | The filter conditions to apply. |

### IQueryFilter object

The `IQueryFilter` object wraps a comparison operation or logical operation.

| **Property** | **Type** | **Description** |
| --- | --- | --- |
| `$class` | `string` | Identifies the object as a query filter. Will always be:`com.docusign.connected.data.queries@1.0.0.QueryFilter` |
| `operation` | `IComparisonOperation` or `ILogicalOperation` | The operation to filter on |

### IComparisonOperation object

Compares a value from the data table to a constant.

| **Property** | **Type** | **Description** |
| --- | --- | --- |
| `$class` | `string` | Identifies the object as a comparison filter. Will always be: `com.docusign.connected.data.queries@1.0.0.ComparisonOperation` |
| `leftOperand` | `IOperand` | Represents an operand in the comparison operation. The left operand always refers to an attribute, not a literal. |
| `operator` | `string` | The comparison operator. Possible values:  - `EQUALS` - `NOT_EQUALS` - `CONTAINS` - `DOES_NOT_CONTAIN` - `LESS_THAN` - `GREATER_THAN` - `LESS_THAN_OR_EQUALS_TO` - `GREATER_THAN_OR_EQUALS_TO` - `STARTS_WITH` - `DOES_NOT_START_WITH` - `ENDS_WITH` - `DOES_NOT_END_WITH` - `IN` - `NOT_IN` - `BETWEEN` - `LIKE` - `CUSTOM`   **Note:** Although the data IO extension supports the `operator` values listed here, Workflow Builder allows workflow process builders to select only **Equal to** as the operator. |
| `rightOperand` | `IOperand` | Represents an operand in the comparison operation. The right operand always represents a literal. |

### IOperand object

This object represents an operand to use in a comparison. It can either be a value selected from the table in the external system of record, or a literal value.

| **Property** | **Type** | **Description** |
| --- | --- | --- |
| `$class` | `string` | Identifies the object as a comparison operand. Will always be:`com.docusign.connected.data.queries@1.0.0.Operand` |
| `name` | `string` | Represents the operand. If `isLiteral` is `false`, this property refers to an attribute of the selected type in the external system of record. If `isLiteral` is `true`, this property is a literal value. |
| `type` | `string` | The type of the operand. Possible values:  - `STRING` - `INTEGER` - `DOUBLE` - `LONG` - `DATETIME` - `BOOLEAN` - `ENUM` - `LIST` - `RANGE` - `OTHER` |
| `isLiteral` | `boolean` | Is `true` if the operand is a literal value, `false` if the operand is a value selected from the table. |

## ILogicalOperation object

This object combines two operations in a logical AND/OR statement. Each suboperation is an `IComparisonOperation` or `ILogicalOperation`.

| **Property** | **Type** | **Description** |
| --- | --- | --- |
| `$class` | `string` | Identifies the object as a logical operation. Will always be:`com.docusign.connected.data.queries@1.0.0.LogicalOperation` |
| `leftOperation` | `IComparisonOperation` or `ILogicalOperation` | The left side of the logical operation. |
| `operator` | `string` | The logical operator. Possible values:  - `AND` - `OR` |
| `isLiteral` | `IComparisonOperation` or `ILogicalOperation` | The right side of the logical operation. |

## Example

To understand the schema, construct a query to select all `Dog` records for which the dog is `8` or older and the dog’s name starts with "`Francis`". (To implement the search action, you’ll need to perform the opposite transformation: from `IQuery` to your own system’s query language. But this is a useful exercise for understanding.)

Start by setting the root values. The external service has a table for all `Dog` objects. The `Dog` type has properties `age` and `animalName`, which you will use in your query. So the root of the query object will look like this:

```
{
    "$class": "com.docusign.connected.data.queries@1.0.0.Query",
    "attributesToSelect": ["age", "animalName"],
    "from": "Dog",
    "queryFilter": { ... }
}
```

Now construct the `queryFilter`. The base operation is a logical AND statement, because you want records for which the dog’s age is greater than or equal to `8` **AND** the dog’s name starts with "`Francis`". Represent this by setting the operation parameter to a `ILogicalOperation` object.

```
{
    "$class": "com.docusign.connected.data.queries@1.0.0.Query",
    "attributesToSelect": ["age", "animalName"],
    "from": "Dog",
    "queryFilter": {
        "$class": "com.docusign.connected.data.queries@1.0.0.QueryFilter",
        "operation": {
            "$class": "com.docusign.connected.data.queries@LogicalOperation",
            "leftOperation": { // check dog age },
            "operator": "AND",
            "rightOperation": { // check dog name}
        }
    }
}
```

Next, write the `leftOperation` to check the dog’s age. This is a comparison, so use an `IComparisonOperation` object.

The first operand is an `IOperand` object representing the dog’s age. Remember that the query will select that value from the table. Indicate the name with the `dogName` value from the `attributesToSelect` list. Set type to whatever the data type is in the table. Finally, set `isLiteral` to `false`, because this is not a constant value.

For the operator, refer to the possible values in the `IComparisonOperation` schema. You want to check if the dog’s age is greater than or equal to `8`, so use the `GREATER_THAN_OR_EQUALS_TO` value.

The second operand is a constant value of `8`. Set the value in the `name` field, and set `isLiteral` to `true`, because it’s a constant.

```
{
    "$class": "com.docusign.connected.data.queries@1.0.0.Query",
    "attributesToSelect": ["age", "animalName"],
    "from": "Dog",
    "queryFilter": {
        "$class": "com.docusign.connected.data.queries@1.0.0.QueryFilter",
        "operation": {
            "$class": "com.docusign.connected.data.queries@LogicalOperation",
            "leftOperation": {
                "$class": "com.docusign.connected.data.queries@1.0.0.ComparisonOperation",
                "leftOperand": {
                    "$class": "com.docusign.connected.data.queries@1.0.0.Operand",
                    "name": "age",
                    "type": "INTEGER",
                    "isLiteral": false
                },
                "operator": "GREATER_THAN_OR_EQUALS_TO",
                "rightOperand": {
                    "$class": "com.docusign.connected.data.queries@1.0.0.Operand",
                    "name": "8",
                    "type": "INTEGER",
                    "isLiteral": true
                }
            },
            "operator": "AND",
            "rightOperation": { // check dog name}
        }
    }
}
```

Finally, construct the `rightOperation`. Again, this is a comparison, so use an `IComparisonOperation` object. The only difference from the `leftOperation` is that you are using a string, not an integer, and using the `STARTS_WITH` operator. This is the final JSON:

Your completed query construction should look like the following:

```
{
    "$class": "com.docusign.connected.data.queries@1.0.0.Query",
    "attributesToSelect": ["age", "animalName"],
    "from": "Dog",
    "queryFilter": {
        "$class": "com.docusign.connected.data.queries@1.0.0.QueryFilter",
        "operation": {
            "$class": "com.docusign.connected.data.queries@LogicalOperation",
            "leftOperation": {
                "$class": "com.docusign.connected.data.queries@1.0.0.ComparisonOperation",
                "leftOperand": {
                    "$class": "com.docusign.connected.data.queries@1.0.0.Operand",
                    "name": "age",
                    "type": "INTEGER",
                    "isLiteral": false
                },
                "operator": "GREATER_THAN_OR_EQUALS_TO",
                "rightOperand": {
                    "$class": "com.docusign.connected.data.queries@1.0.0.Operand",
                    "name": "8",
                    "type": "INTEGER",
                    "isLiteral": true
                }
            },
            "operator": "AND",
            "rightOperation": {
                "$class": "com.docusign.connected.data.queries@1.0.0.ComparisonOperation",
                "leftOperand": {
                    "$class": "com.docusign.connected.data.queries@1.0.0.Operand",
                    "name": "animalName",
                    "type": "STRING",
                    "isLiteral": false
                },
                "operator": "STARTS_WITH",
                "rightOperand": {
                    "$class": "com.docusign.connected.data.queries@1.0.0.Operand",
                    "name": "Francis",
                    "type": "STRING",
                    "isLiteral": true
                }
            }
        }
    }
}
```

## Next steps

- [Data IO extension overview](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/)
- [Data IO extension workflow test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/)
- [Data IO extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/)

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
