---
title: Document generation
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/
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
- Documents
- Documents
- Document Generation
scraped_at: '2026-06-18T20:28:19Z'
---

# Document generation

eSignature REST API 2.1 only

Document generation enables you to create reusable [templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/) with professionally formatted [documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) that include personalized data. For example, you can create a boilerplate employment offer letter that’s updated with job details from an HR system for each candidate.

To create a document that can be populated with custom data, you include placeholders, known as *sender fields*, that will be replaced with values specific to each agreement before you send an [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/). If the document is an offer of employment, you can define sender fields for the job title, salary, start date, and any other information that varies with each offer.

In addition, you can define conditional sender fields that display text based on values in other sender fields. For example, an employment offer can list a different supervisor name depending on the job title. You can also define [dynamic tables](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#dynamic-tables) that can be populated with agreement-specific values in each row, such as compensation package components and their corresponding amounts in an offer letter.

The custom data values are seamlessly incorporated into the final document that is sent to the recipient. The document looks as if it was generated specifically for that user, with no visible traces of the placeholders.

For example, this Word document contains the sender fields **Candidate\_Name**, **Job\_Title**, and **Start\_Date**. It also contains a dynamic table that includes **Component** and **Details** sender fields that will appear in each row. This table can be populated with as many rows as necessary when the agreement is generated. In addition, the document includes conditional logic to display the appropriate manager name, based on the provided job title.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='717' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Document generation file](https://images.ctfassets.net/aj9z008chlq0/1hsCfqki5Kv5OU9BG5yiFt/07d822cbdd00fc0f2d7452dd58612674/OfferLetterATB.png?w=600&h=717&q=50&fm=png)

In the final document sent to the recipient, the sender fields are replaced with values specific to that agreement and the dynamic table is populated with the number of rows supplied for the agreement, as shown here. Recipients cannot edit these values.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='688' width='600' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Document generation signer view](https://images.ctfassets.net/aj9z008chlq0/28UAY6OmGjDkjxhPH6ndrP/93f3a9a6dc83a76b725947fca957083c/OfferLetterSigning.png?w=600&h=688&q=50&fm=png)

Document generation is available in all developer accounts, but must be purchased for production account plans. Contact [Docusign Support](https://support.docusign.com/s/contactSupport) or your account manager to find out whether document generation is available for your production account plan.

## Document generation process

To create and send [envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/) that use document generation:

1. [Create the document](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#methods-for-creating-documents) or documents that contain sender fields. The documents must be included in a [template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/). See [Methods for creating documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#methods-for-creating-documents) for an overview of the options.
2. [Implement the sequence of API requests](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#implement-sequence-of-api-requests) or SDK methods to create envelopes from the template, populate the documents with custom data, and send the envelopes to recipients.

## Methods for creating documents

For each document that will include sender fields, create a DOCX file. Other file types are not supported with document generation.

Options for creating the file are listed below. For guidance on which editor may be more appropriate to use, see [Choosing Between Document Editors﻿](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=con1f1d1e0b-5f19-4e30-8985-a5f490084b66.html).

- **Recommended:** Use the [Agreement Template Builder](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=jct1697745471160.html) to create a template; add a DOCX file to it; add sender fields, conditional logic, and dynamic tables; and preview the document with sample data.
- **Alternative option:** Use the [Docusign Template Assistant for Word](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=kyy1679958874136.html) add-in to add sender fields, conditional logic, and dynamic tables to a DOCX file; preview the document with sample data; and upload the document to an eSignature template.
- Manually add the [sender field syntax](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=ftc1679700030026.html) to a DOCX file. This method, while not recommended for creating many sender fields, can be used when making minor changes or when configuring dynamic tables in ways not supported in the Agreement Template Builder or the Template Assistant table editor. See [Table definition behaviors and restrictions](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#table-definition-behaviors-and-restrictions) for details.

## Sender field types

Document generation supports the sender field types listed below. The **Field type** column in the table contains the type identifier used in API requests and responses. See [Retrieve and populate sender fields](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#retrieve-and-populate-sender-fields) for an example response.

| Field type | Description | Supported with these document creation methods |
| --- | --- | --- |
| `TextBox` | Freeform text | All |
| `Date` | A date in one of these formats:  - MM/DD/YYYY - DD/MM/YYYY - YYYY/MM/DD | Agreement Template Builder  Template Assistant for Word |
| `Number` | A numeric value that can include:  - An optional period as a decimal separator. Up to two digits of decimal precision are supported. - Optional commas as thousands separators - A leading minus sign to indicate a negative value  Number fields support values from a minimum of -999999999.99 to a maximum of  999999999.99. | Agreement Template Builder  Template Assistant for Word |
| `Select` | A predefined list of allowed values. You can define up to 250 allowed values per select field. Values can contain any character except a semicolon. | Agreement Template Builder  Template Assistant for Word |
| `TableRow` | A definition for a dynamic table. The definition includes a name and the sender fields that appear in the table columns. See [Define table structure](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#define-table-structure) for details. | All |

## File size and field limits

The following limits apply to document generation files created via an editor.

| Limit type | Agreement Template Builder | Docusign Template Assistant for Word |
| --- | --- | --- |
| Maximum file size | 1 MB | 25 MB |
| Maximum number of sender fields per DOCX file | 1,000 | 1,000 |
| Maximum number of sender field values per generated agreement | 100,000 | 100,000 |

When you use [dynamic tables](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#dynamic-tables), the number of sender field values in generated agreements will vary depending on how many table rows are populated. For example, a DOCX file might have 25 sender fields in the text, plus a dynamic table definition containing five columns with a sender field in each column. In this case, the total number of sender fields will be 30. If the dynamic table in a generated agreement has 100 rows, then the total number of sender field values in the agreement will be 525 (five sender field values per table row multiplied by 100 rows, plus the 25 sender field values from the text).

## Implement sequence of API requests

You have several options for implementing a sequence of API requests or SDK methods to customize and send documents to your recipients. The next sections contain example sequences of implementation steps. In the first sequence, the [Agreement Template Builder](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=jct1697745471160.html) is used to create a template, add a DOCX file to it, and add sender fields. In the second sequence, the [Docusign Template Assistant for Word](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=kyy1679958874136.html) is used to create a document with sender fields. The third sequence assumes that you will manually add [sender field syntax](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=ftc1679700030026.html) to the DOCX file.

The eSignature [SDKs](https://developers.docusign.com/docs/esign-rest-api/sdks/) have equivalent methods in all the supported programming languages for each API request referenced in the sample sequences below.

### Sample sequence using the Agreement Template Builder

Below is a sample sequence of document generation implementation steps consisting of API requests and tasks completed in the [Agreement Template Builder](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=jct1697745471160.html).

1. Use the Agreement Template Builder to [create a document generation template](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=ffc1707759927433.html) that includes your DOCX file, and add sender fields, [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/), and [dynamic tables](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#dynamic-tables) to the DOCX file. This is a one-time setup task. Once you have created the template, you can reuse it with multiple envelopes.
2. [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/): Creates a draft envelope from the template.
3. [DocumentGeneration:getEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/getenvelopedocgenformfields/): Retrieves a list of sender fields from the document, including the field names, types, and dynamic table structure.
4. [DocumentGeneration:updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/): Updates sender fields with agreement-specific values that will be displayed in the document in the signing UI. See [Retrieve and populate sender fields](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#retrieve-and-populate-sender-fields) for more information.
5. [Envelopes:update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/): Sends the draft envelope.

### Sample sequence using Docusign Template Assistant for Word

Below is a sample sequence of document generation implementation steps consisting of API requests and tasks completed via the [Docusign Template Assistant for Word](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=kyy1679958874136.html).

1. [Templates:create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/create/): Creates a [template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/). As an alternative to creating a template via an API request, you can [create it in the eSignature web application](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html).
2. Use the Docusign Template Assistant for Word to [add sender fields](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=kgg1680241042480.html) and [dynamic tables](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#dynamic-tables) to the [document](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/).
3. Use the Docusign Template Assistant for Word to [upload the document](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=qwk1702687799547.html) to the template created in step 1. Instead of first creating the template and then uploading a document, you can create a new template during the document upload.
4. [TemplateRecipientTabs:create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/create/): Adds [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) to the document. You can also [add tabs in the eSignature web application](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html). This step and the previous three make up an initial setup process. Once you have completed this process, you can reuse the template with multiple envelopes.
5. [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/): Creates a draft envelope from the template.
6. [DocumentGeneration:getEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/getenvelopedocgenformfields/): Retrieves a list of sender fields from the document, including the field names, types, and table structure for [dynamic tables](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#dynamic-tables).
7. [DocumentGeneration:updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/): Updates sender fields with agreement-specific values that will be displayed in the document in the signing UI. See [Retrieve and populate sender fields](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#retrieve-and-populate-sender-fields) for more information.
8. [Envelopes:update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/): Sends the draft envelope.

### Sample sequence with manually created sender field syntax

Below is a sample sequence of document generation implementation steps consisting of API requests and manual addition of [sender field syntax](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=ftc1679700030026.html) to a DOCX file.

For ease of use and to reduce the risk of syntax errors, Docusign recommends using the [Agreement Template Builder](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=jct1697745471160.html) or the [Docusign Template Assistant for Word](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=kyy1679958874136.html) rather than manually creating sender field syntax.

1. Manually add [sender field syntax](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=ftc1679700030026.html) to a DOCX file.
2. [Templates:create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/create/): Creates a [template](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/). As an alternative to creating a template via an API request, you can [create it in the eSignature web application](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html).
3. [TemplateDocuments:update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/update/): Adds the [document](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/) with sender fields to the template. The document is supplied in this request as a Base64-encoded string. You can also [add a document to a template in the eSignature web application](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html).
4. [TemplateRecipientTabs:create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/create/): Adds [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/) to the document. You can also [add tabs in the eSignature web application](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html). This step and the previous three make up an initial setup process. Once you have completed this process, you can reuse the template with multiple envelopes.
5. [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/): Creates a draft envelope from the template.
6. [DocumentGeneration:getEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/getenvelopedocgenformfields/): Retrieves a list of sender fields from the document, including the field names, types, and table structure for [dynamic tables](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#dynamic-tables).
7. [DocumentGeneration:updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/): Updates sender fields with agreement-specific values that will be displayed in the document in the signing UI. See [Retrieve and populate sender fields](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#retrieve-and-populate-sender-fields) for more information.
8. [Envelopes:update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/): Sends the draft envelope.

A walkthrough of this sequence, including code examples, appears in [How to request a signature by email with document generation](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-document-generation/).

### Retrieve and populate sender fields

Regardless of which method you use to create a DOCX file, Docusign automatically extracts sender field and [dynamic table](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#dynamic-tables) information and stores it with the document in the [docGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/list/#schema_200_templatedocumentsresult_templatedocumentsresult_templatedocuments_docgenformfields) array. When you use the [Agreement Template Builder](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=jct1697745471160.html), this information is automatically extracted when you save the template. For documents created via the [Docusign Template Assistant for Word](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=kyy1679958874136.html), Docusign extracts this information when you upload the document to a template. For documents to which sender field syntax has been added manually, the information is extracted when you add the document to a template via a [TemplateDocuments:update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/update/) API request or equivalent SDK method, or when you [add it to the template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html) in the eSignature web application.

You can retrieve a list of a document's sender field names and types and dynamic table structure via a [DocumentGeneration:getEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/getenvelopedocgenformfields/) request or an equivalent SDK method.

Here's an example of a list of sender fields that were created in the Agreement Template Builder:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='332' width='350' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Sender fields defined in the Agreement Template Builder](https://images.ctfassets.net/aj9z008chlq0/Iga62fJUwaHs8vff3VFoV/a9a31e6aa0ff6a64e833c03d2b47a69f/ATBSenderFieldList.png?w=350&h=332&q=50&fm=png)

The response to a [DocumentGeneration:getEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/getenvelopedocgenformfields/) request for the document includes each field name and type, the dynamic table structure, and other details:

```
{
  "docGenFormFields": [
    {
      "documentId": "ad1fe909-xxxx-xxxx-xxxx-164cf6e20b30",
      "docGenFormFieldList": [
        {
          "label": "Candidate_Name",
          "type": "TextBox",
          "required": "False",
          "name": "sz0Iw",
          "fullyQualifiedPath": "account._4b65f24e_xxxx_xxxx_xxxx_3fb0f92931d4.custom.fields@1/C_Candidate_Name/value"
        },
        {
          "label": "Job_Title",
          "type": "Select",
          "required": "False",
          "name": "Z10dbqD",
          "options": [
            {
              "label": "Software Engineer",
              "value": "Software Engineer",
              "selected": "False"
            },
            {
              "label": "Test Engineer",
              "value": "Test Engineer",
              "selected": "False"
            },
            {
              "label": "Technical Writer",
              "value": "Technical Writer",
              "selected": "False"
            }
          ],
          "fullyQualifiedPath": "account._4b65f24e_xxxx_xxxx_xxxx_3fb0f92931d4.custom.fields@1/C_Job_Title/value"
        },
        {
          "label": "Start_Date",
          "type": "Date",
          "required": "False",
          "name": "ufrpq",
          "fullyQualifiedPath": "account._4b65f24e_xxxx_xxxx_xxxx_3fb0f92931d4.custom.fields@1/C_Start_Date/value"
        },
        {
          "label": "Compensation Package",
          "type": "TableRow",
          "required": "False",
          "name": "Oo1be",
          "rowValues": [
            {
              "docGenFormFieldList": [
                {
                  "label": "Component",
                  "required": "False",
                  "name": "Z1E6uXj"
                },
                {
                  "label": "Details",
                  "required": "False",
                  "name": "_1PuLPK"
                }
              ]
            }
          ],
          "fullyQualifiedPath": "account._4b65f24e_xxxx_xxxx_xxxx_3fb0f92931d4.custom.agreements@1/C_CompensationPackage/c_CompensationPackage"
        }
      ],
      "docGenDocumentStatus": "created"
    }
  ]
}
```

Once you've retrieved the list of sender fields (and the table definition, if the DOCX file includes a dynamic table), you can populate these elements with recipient-specific values via a [DocumentGeneration:updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/) request or equivalent SDK method. The request only needs to reference the name and value for each sender field, as shown in [How to request a signature by email with document generation](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-document-generation/). See [Dynamic tables](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#dynamic-tables) for details about retrieving and populating sender fields that appear in a dynamic table.

Make sure that the sender field names in the `DocumentGeneration:updateEnvelopeDocGenFormFields` request match the `name` values in the `DocumentGeneration:getEnvelopeDocGenFormFields` response. Depending on the method used to create the document, the names might be Docusign-generated strings, like the ones shown in the example response above.

### Validation of sender field values

Docusign does not validate number, date, or select sender field values populated via a [DocumentGeneration:updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/) request or equivalent SDK method. The request can succeed even if a number or date field value is not a valid number or date, or if a select field value is not one of the allowed values. Date, number, and select field validation will be implemented in a future release.

If you [create a document generation envelope](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=ekg1679981354189.html) in the eSignature web application, sender field values are validated upon entry. Number and date field values must be in the correct format. For select fields, the application displays a dropdown that lists only the allowed values.

## Dynamic tables

You can use document generation sender fields in a dynamic table structure that accommodates varying numbers of rows for each agreement. For example, an employment offer might contain a table of compensation package components that differs for each offer. One candidate's offer might include rows for salary and annual bonus, while another offer might include additional rows for company stock and a signing bonus.

### Define table structure

To use a dynamic table, you must define its structure. The table definition includes a name and the sender fields that appear in the columns.

Below is an example dynamic table definition in the [Agreement Template Builder](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=jct1697745471160.html):

![](data:image/svg+xml;charset=utf-8,%3Csvg height='297' width='500' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Dynamic table definition](https://images.ctfassets.net/aj9z008chlq0/6luPYSikhejvatO027UcNO/08ae114882773d17cb927f732eb15021/ATBDynamicTableDefinition.png?w=500&h=297&q=50&fm=png)

The table definition includes the fields that will appear in each data row. The number of rows displayed in each agreement is determined by the API request that populates the sender fields for that agreement. See [Populate dynamic table values](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#populate-dynamic-table-values) for details.

The table name and sender field names entered during table definition do not appear in agreements that are displayed to users. Table column headings are defined as static text in the DOCX file. The column headings cannot be retrieved or populated via API requests.

These methods are available for defining table structure in a DOCX file:

- **Recommended:**  Use the [Agreement Template Builder](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=jct1697745471160.html) to define a dynamic table and insert it into the DOCX file. See [Insert a Dynamic Table﻿](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=kbb1723763558691.html) for details.
- **Alternative option:** Use the [Docusign Template Assistant for Word](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=kyy1679958874136.html) to define a dynamic table and insert it into the DOCX file. See [Create a Dynamic Table With the Template Assistant﻿](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=nhd1712957935412.html) for details.
- Manually add [sender field syntax](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=ftc1679700030026.html) to a table in the DOCX file. Although the preferred method is to use the Agreement Template Builder, you may need to manually add sender field syntax if you are configuring dynamic tables in ways not supported in the Agreement Template Builder. See [Table definition behaviors and restrictions](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#table-definition-behaviors-and-restrictions) for details.

### Table definition behaviors and restrictions

Table definitions are subject to these behaviors and restrictions:

- Table definition names must be unique within a document, for documents that have more than one dynamic table.
- The same sender field can be used in more than one dynamic table, but values are not reused across tables. See [Table value behaviors and restrictions](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#table-value-behaviors-and-restrictions) for details.
- The same sender field can be used both in a dynamic table column and in regular text in the document, but values are not reused between regular text and dynamic tables. See [Table value behaviors and restrictions](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#table-value-behaviors-and-restrictions) for details.
- The same table column can include more than one sender field. For example, for a column that contains a full name, the document creator might need to include two sender fields in the column—one for the first name and one for the last name. However, the Agreement Template Builder and the Docusign Template Assistant for Word only support one sender field per column. To include a second sender field in the same column, the document creator would have to manually add the field to the column in the DOCX file.
- The same sender field can be included in more than one column in the same dynamic table, but you must manually insert the sender field in any additional columns. The Agreement Template Builder and the Docusign Template Assistant for Word do not support inserting the same sender field into more than one column.
- Only `TextBox` type sender fields can be used in dynamic table columns. Other [sender field types](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#sender-field-types) are not supported in dynamic table columns in the current release.
- In the current release, calculations cannot be performed on values from sender fields in dynamic tables.

### Retrieve table definition

To populate rows in a dynamic table, your application must first retrieve the table definition, which lists the sender fields that appear in each row. The table definition, as well as details about all other sender fields in a document generation document, is included in the response to the [DocumentGeneration:getEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/getenvelopedocgenformfields/) request. See [Implement sequence of API requests](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#implement-sequence-of-api-requests) for details about how this request fits into an overall document generation flow.

The following example shows a dynamic table definition from a `DocumentGeneration:getEnvelopeDocGenFormFields` response. Key properties are:

- `type`: The value `TableRow` identifies this as a dynamic table definition.
- `name`: The name of the table definition must be referenced in the [DocumentGeneration:updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/) request to populate table values.
- `rowValues.docGenFormFieldList`: An array of sender fields that will appear in each row. The sender field names must be referenced in the `DocumentGeneration:updateEnvelopeDocGenFormFields` request to populate table values.

```
{
  "label": "Compensation Package",
  "type": "TableRow",
  "required": "False",
  "name": "Oo1be",
  "rowValues": [
    {
      "docGenFormFieldList": [
        {
          "label": "Component",
          "required": "False",
          "name": "Z1E6uXj"
        },
        {
          "label": "Details",
          "required": "False",
          "name": "_1PuLPK"
        }
      ]
    }
  ],
  "fullyQualifiedPath": "account._4b65f24e_xxxx_xxxx_xxxx_3fb0f92931d4.custom.agreements@1/C_CompensationPackage/c_CompensationPackage"
}
```

### Populate dynamic table values

The [DocumentGeneration:getEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/getenvelopedocgenformfields/) response in the previous section contains one `rowValues.docGenFormFieldList` array. This array defines the sender fields that make up a table definition. A [DocumentGeneration:updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/) request, on the other hand, can include multiple `rowValues.docGenFormFieldList` arrays—one for each table row to be displayed to an end user.

The following example shows a section of a `DocumentGeneration:updateEnvelopeDocGenFormFields` request that populates the dynamic table whose definition appears in the previous section. This example includes three rows of values—one for salary, one for bonus, and one for stock. Each `rowValues.docGenFormFieldList` array consists of name/value pairs for the sender fields in one row.

```
{
  "name": "Oo1be",
  "type": "TableRow",
  "rowValues": [
    {
      "docGenFormFieldList": [
        {
          "name": "Z1E6uXj",
          "value": "Salary"
        },
        {
          "name": "_1PuLPK",
          "value": "$100,000.00"
        }
      ]
    },
    {
      "docGenFormFieldList": [
        {
          "name": "Z1E6uXj",
          "value": "Bonus"
        },
        {
          "name": "_1PuLPK",
          "value": "20 percent"
        }
      ]
    },
    {
      "docGenFormFieldList": [
        {
          "name": "Z1E6uXj",
          "value": "Stock"
        },
        {
          "name": "_1PuLPK",
          "value": "5,000 shares"
        }
      ]
    }
  ]
}
```

The dynamic table populated with these values would look like this in the agreement that is displayed to an end user:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='246' width='942' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Dynamic table signing view](https://images.ctfassets.net/aj9z008chlq0/65fXbqxArvINoLcTdcUlka/fded458feb5a948886e18306a13d59df/OfferLetterSigning_DynamicTable.png?w=942&h=246&q=50&fm=png)

See [Implement sequence of API requests](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#implement-sequence-of-api-requests) for details about how the `DocumentGeneration:updateEnvelopeDocGenFormFields` request fits into an overall document generation flow. See [How to request a signature by email with document generation](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-document-generation/) for code examples that demonstrate how to populate a dynamic table.

### Table value behaviors and restrictions

The population of table values via a [DocumentGeneration:updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/) request is subject to these behaviors and restrictions:

- There is no limit on the number of rows that a table can contain. However, a maximum of 100,000 sender fields can be populated in a document, including sender fields in dynamic tables. See [File size and field limits](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/document-generation/#file-size-and-field-limits) for details.
- Each `rowValues.docGenFormFieldList` array that populates values for a row must include a name/value pair for all sender fields in the table definition, even for sender fields that are not being populated.
- For sender fields that should not be populated, set the `value` property in the name/value pair to an empty string. If you omit a name/value pair for a sender field from the `rowValues.docGenFormFieldList` array for a row, an error response will be returned.
- If you don't want to populate any values in a dynamic table, you can omit the entire `TableRow` JSON structure from the `DocumentGeneration:updateEnvelopeDocGenFormFields` request. If it is omitted, the table's heading row and one blank row beneath it will appear in the agreement that the recipient receives.
- If a document has more than one dynamic table, supply a `TableRow` JSON structure in the request for each table, with the corresponding name for the table definition, followed by the `rowValues` array for that table's values.
- Sender field values are not reused across rows in the same table. For example, each r`owValues.docGenFormFieldList` array must include a value for the `Details` sender field for that row.
- A sender field can be populated with only one value per row. If a table definition includes more than one instance of the same sender field, the value provided for that sender field in a `rowValues.docGenFormFieldList` array will be reused for every occurrence of that sender field in the same row.
- Sender field values are not reused across dynamic tables, even if the same sender field name is used in multiple tables.
- If the same sender field name is used in a DOCX file in both a table definition and in regular text outside the table, the `DocumentGeneration:updateEnvelopeDocGenFormFields` request must populate separate values for the regular text instance of the sender field and for each row of the dynamic table. Only one value can be supplied for all non-table instances of the same sender field.

## Document generation support with other eSignature features

The following common eSignature features support document generation:

- [Composite templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/composite/). For a walkthrough and sample API requests, see [Document generation with composite templates](https://www.docusign.com/blog/developers/document-generation-composite-templates).
- [Bulk sending envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/bulk-send/)
- [Sharing templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/sharing/)
- [Basic responsive signing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/responsive#basic)
- [Authoritative copies](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/authoritative-copies/)

These features, however, do not:

- [Elastic templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/elastic-templates/)
- [Binary transfer](https://developers.docusign.com/docs/esign-rest-api/how-to/send-binary/)
- [Supplemental documents](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/documents/supplemental/)
- [PowerForms](https://developers.docusign.com/docs/esign-rest-api/reference/powerforms/powerforms/)

## Next steps

For more information about document generation, see:

- [How to request a signature by email with document generation](https://developers.docusign.com/docs/esign-rest-api/how-to/request-signature-email-document-generation/)
- [DocumentGeneration Resource](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/) in the API reference
- [Document Generation for Docusign eSignature](https://support.docusign.com/s/document-item?bundleId=als1679428547895&topicId=ldx1679428689631.html&_LANG=enus)﻿ in the eSignature User Guide

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
