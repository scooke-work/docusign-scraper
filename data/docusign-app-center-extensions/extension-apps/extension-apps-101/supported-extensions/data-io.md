---
title: Data IO extension overview
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Supported Extensions
- Supported Extensions
- Data IO
scraped_at: '2026-06-18T19:51:51Z'
---

# Data IO extension overview

Data IO is an [extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) that enables you to read data from and write data to your system of record. After creating an extension app that implements data IO, you can integrate that functionality into your automation and Docusign scenarios, such as creating automation that responds to a job offer agreement by creating an account for the new employee in your system of record. You can also publish your completed extension app to the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) for other Docusign users to find, install, and use.

Data IO includes two capabilities that can be configured as steps in [Workflow Builder](https://developers.docusign.com/docs/workflow-builder-api/) workflows:

- The [data input](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/#input-data) capability retrieves data from your system of record, such as Salesforce, ServiceNow, or Stripe.
- The [data output](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/#output-data) capability transmits your data from Docusign to update your system of record.

See [Data IO extension workflow test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/) for details on how the data IO extension is displayed to users in the UI and learn how it maps to the extension action contracts.

These screenshots show an example of how these capabilities are displayed in the Workflow Builder UI, in both **Add a step** and **Step configuration**.

**Workflow Builder add steps UI:**

![](data:image/svg+xml;charset=utf-8,%3Csvg height='286' width='273' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image of the Maestro workflow designer UI showing the option to add either data input or data output steps.](https://images.ctfassets.net/aj9z008chlq0/2PU6KIILsgHyrf00l52we7/49af2c2fe7c866ff601c99f1d48aecf7/DataIOActionsMaestro.png?w=273&h=286&q=50&fm=png)

**Workflow Builder data input configuration UI:**

![](data:image/svg+xml;charset=utf-8,%3Csvg height='831' width='602' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image of the UI options for configuring a data read step in the Maestro workflow designer.](https://images.ctfassets.net/aj9z008chlq0/1fE2b3tWujRDjDOQeS07OX/e1970f858a32233d28edca81b267aded/ReadSalesforce.png?w=602&h=831&q=50&fm=png)

**Workflow Builder data output configuration UI:**

![](data:image/svg+xml;charset=utf-8,%3Csvg height='878' width='611' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![An image showing the options to configure a data ouptut step in the Maestro workflow designer.](https://images.ctfassets.net/aj9z008chlq0/ZSCkihrZYc407uAW6Uq16/3a09b64dbd837fb196531361c9fc0c8e/WriteSalesforce.png?w=611&h=878&q=50&fm=png)

You can implement data input as a standalone capability without also implementing data output. To do this, implement only the [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts), [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts), and [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts) actions. Note that you cannot implement data output as a standalone capability, because it uses the data input actions to find the records to update. If your extension must write data to your system of record, you must implement all five data IO actions.

> **Note:** If your app only needs to create new records and does not need to update them, you can choose to only create a full implementation for [Create Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts). In this case you still need to define [Patch Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts), but it does not need to contain any code.

|  |  |  |
| --- | --- | --- |
| **Action name** | **Executed when** | **Description** |
| [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts) | The extension app establishes or refreshes a connection. | Gets the names of the types that are used by your system of record.  In the manifest, this action is named `DataIO.Version6.GetTypeNames`. |
| [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts) | The extension app establishes or refreshes a connection. Called directly after **Get Type Names**. | Gets a set of type definitions from your system of record and returns their equivalents in the [Concerto](https://concerto.accordproject.org/docs/intro/) data model format.  DocuSign uses the [Concerto](https://concerto.accordproject.org/docs/intro/) data model to map the data read from your system of record. If your system of record does not already use the Concerto data model, you must implement transform logic that defines how your records map to Concerto data types before they can be read. This transform logic should be implemented within your **Get Type Definitions** action, and is called whenever the action is executed. See [Data model](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/) for details on the data model structure.  In the manifest, this action is named `DataIO.Version6.GetTypeDefinitions`. |
| [Create Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts) | When a [data output](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/#output-data) step is executed and no query is provided, or the query does not find a record to update. | Creates a new entry in your system of record.  In the manifest, this action is named `DataIO.Version6.CreateRecord`. |
| [Patch Record](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts) | When a [data output](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/#output-data) step is executed and your provided query finds a record to update. | Updates an existing entry in your system of record.   In the manifest, this action is named `DataIO.Version6.PatchRecord`. |
| [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts) | When a [data input](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/#input-data) or [data output](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/#output-data) step is executed. | Gets specific entries from your system of record.  In the manifest, this action is named `DataIO.Version6.SearchRecords`. |

## Get type names and definitions

When your data IO extension app is run and your [Connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/) is established prior to any steps being executed, your extension app will automatically get the types and type definitions of the objects that your system of record is configured to expose:

1. Your workflow calls [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#action-contracts) to get the set of types that your system of record exposes for Docusign. The types are returned as an array of string names.
2. Next, it calls [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-get-type-definitions), inputting the types returned by **Get Types**. This returns the full definitions of each type that your system of record exposes for Docusign.

**Important**: Docusign models data input and output definitions using a flexible schema in [Concerto](https://concerto.accordproject.org/docs/intro/). If your system of record does not already use the Concerto data model, you must implement logic to convert your type definitions into Concerto format as part of your response to the **Get Type Definitions** call.

See [Data model](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/) for recommendations on mapping types or [Concerto specification](https://concerto.accordproject.org/docs/category/specification) for details on specific types, syntax, and examples.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1736' width='1288' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A diagram showing each step in data IO that is executed to get type names and definitions for Docusign, your extension app, and your system of record.](https://images.ctfassets.net/aj9z008chlq0/dvPzEdwSIpf1suGGSJHRH/d2ced8b15448ac3c9f6666106b1cc3ee/ExampleGetTypesFlow.png?w=1288&h=1736&q=50&fm=png)

## Input data

When you add a data input step in the [workflow designer](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=pps1696973636517.html), you configure that step by:

- Choosing the type of record to retrieve.
- Applying filters to specify which set of records to look through.
- Specifying the attributes of the specific records to retrieve.

When your data input workflow step is reached during execution, the [Search Records](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/#dataio-version6-search-records) action is called to run your query and retrieve the records. Once the records are retrieved, you can use these values in subsequent workflow steps. **Important**: Docusign uses a simple custom query language to filter and select records without dependencies on any specific external systems. To implement the **Search Records** action, you must create transform logic to convert the query expression into one supported by your system of record. See [Custom query language reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/) for details on the query language structure and syntax.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1630' width='1163' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A diagram showing each step in data IO that is executed to input data for Docusign, your extension app, and your system of record.](https://images.ctfassets.net/aj9z008chlq0/2txS6S3oRHmocb8lMFk1dG/111a3731eda44a13726715fc206b9800/ExampleDataRead.png?w=1163&h=1630&q=50&fm=png)

## Output data

When you add a data output step in the [workflow designer](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=pps1696973636517.html), you configure that step by choosing whether it creates or updates a record.

**To create a record**:

1. Select the type of record to create.
2. Do not set any filter conditions for the step’s query.
3. Provide data attributes to populate the record. Any attributes that are required by the record type in your system of record must be provided.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1305' width='1249' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A diagram showing each step in data IO that is executed to create a record. Includes steps for Docusign, your extension app, and your system of record.](https://images.ctfassets.net/aj9z008chlq0/7163tSvcYuoPPG1H8ATN0w/ffdafe275b464d5b03ef2c56da6a3e74/DataWritebackCreate.png?w=1249&h=1305&q=50&fm=png)

**To update a record**:

1. Select the type of record to create.
2. Set one or more filter conditions that result in exactly one matching record being found. If more than one record is returned, an error will be generated. If no records are found, a **Create Record**call will be made instead.
3. Provide data attributes to be added to the record. Any values of these attributes already present in the record will be overwritten.

When your data output step is reached during execution, the following logic is run:

1. If you provide one or more search filter conditions, a **Search Records**action is performed to find any record matching your query.
2. If the results of this query are empty, the internal Docusign system will create a record by invoking the **Create Record** action on the app, which will return a `recordId`.
3. If the query returns a record, that record’s `recordId` is used to call **Patch Record**and update the record’s attribute values. An error will be generated if more than one record is returned.
4. You can then use the returned `recordId` to identify the record to use and work with in future steps of your workflow.

**Important**: Docusign uses a simple custom query language to filter and select records without dependencies on any specific external systems. To implement the **Search Records** action, you must create transform logic to convert the query expression into one supported by your system of record. See [Custom query language reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/custom-query-language/) for details on the query language structure and syntax.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='2015.0000000000002' width='1212' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A diagram showing each step in data IO that is executed to update a record. Shows steps for Docusign, your extension app, and your system of record.](https://images.ctfassets.net/aj9z008chlq0/3GpPwrYnxmml8H5l7HdAxL/3031b6ae7245a043bfd902c5c82bf996/DataWritebackUpdate.png?w=1212&h=2015&q=50&fm=png)

## Next steps

- See [Data IO extension workflow test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-io-workflow/) for details on how the data IO extension is displayed to users in the UI and learn how it maps to the extension action contracts.
- See details about the data IO contracts and objects in the [Data IO extension contract reference](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/).
- Learn how to implement [foreign-key relationships](https://developers.docusign.com/extension-apps-101/supported-extensions/data-io/related-objects/) in a data IO extension app.
- After creating an extension app that implements data IO, you can integrate that functionality into your automation and Docusign scenarios, such as creating automation that responds to a job offer agreement by creating an account for the new employee in your system of record. You can also publish your completed extension app to the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) for other Docusign users to find, install, and use.

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
