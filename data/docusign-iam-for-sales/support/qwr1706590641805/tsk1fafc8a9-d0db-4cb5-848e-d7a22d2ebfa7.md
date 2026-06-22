---
title: Format Currency Fields in Salesforce Workflow Steps
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=qwr1706590641805&topicId=tsk1fafc8a9-d0db-4cb5-848e-d7a22d2ebfa7.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-22T19:18:53Z'
---

# Format Currency Fields in Salesforce Workflow Steps

Learn to format currency fields in Read from Salesforce and Writeback to Salesforce steps.

## Before you begin

Before you begin

- Required: Installation of the Salesforce app from Docusign App Center. Review the [Installing Extension Applications for Workflow Builder](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=bgb1697668738892.html&_LANG=enus) topic for more information.
- Required: [Workflows Create permissions](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=gbb1696973048215.html&_LANG=enus) or be an account administrator.
- Required: Create a workflow as described in [Create a Basic Workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uhm1697826856678.html&_LANG=enus). Add steps like [invitation](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=kfx1698167344720.html&_LANG=enus), [web forms](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=gua1698120920620.html&_LANG=enus), [eSignature](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uww1698167288211.html&_LANG=enus) and more to gather recipients, documents, and merge fields for your workflow.

You can create Salesforce workflow steps that read and update Salesforce
data. You can use `currency` fields in Salesforce steps to import and update a record's monetary value.

A currency field is a unified `MonetaryAmount` variable that combines a number and
a currency code. For example: `1000000.00` and
`USD`.

When a workflow uses a Read from Salesforce step to import a Salesforce currency
field, Workflow Builder divides the field into the following elements:

- Value: A `doubleValue` numeric
  amount.
- Currency code: An ISO 4217
  `currencyCode`, often linked to a Salesforce
  `CurrencyIsoCode`.

Workflow Builder combines those elements into a `currency` variable that
contains both elements. Workflows can use each element in
the following ways:

- `Value`: Used in rules and later workflow steps that look for an
  amount.
- `Code`: Used to branch or map on a currency. For example: a workflow contains one branch for `USD` and another
  for `EUR`.

Note: In single-currency Salesforce organizations, Workflow Builder
reads the `Code` from organization-level settings. In
multi-currency organizations, Workflow Builder reads the `CurrencyIsoCode`
from records.

Read from Salesforce example: You want to import currency
amounts like `Annual Revenue` into workflows. You build a workflow
with a Read from Salesforce step and add the Salesforce Annual
Revenue field.

Result: When the workflow runs, Workflow Builder reads the Salesforce
Annual Revenue field and adds it to the agreement as a
currency variable. The variable includes both the numeric amount and the ISO 4217
currency code. The workflow uses this variable in rules, forms, and downstream
steps.

When using Writeback to Salesforce to update a Salesforce currency field, Workflow Builder
sends the following information:

- `doubleValue`: Sends a `doubleValue` numeric
  amount.
- `currencyCode`: Sends an ISO 4217 currency code to pair with
  the numeric amount.

Note:

- In single-currency Salesforce organizations, map the `Value` currency variable to a Salesforce
  `amount` field.
- In multi-currency organizations, map the
  `Code` currency variable to the record's
  `CurrencyIsoCode`.

Writeback to Salesforce example: You want workflows to update
Salesforce currency fields like `Annual Revenue`. You build a
workflow with a Read from Salesforce step and a Writeback to Salesforce step. In the
Read from Salesforce step, you add the Salesforce Annual
Revenue field.

In the Writeback to Salesforce step, you map the Annual
Revenue Salesforce field to the Annual
Revenue.Value workflow field.

Result: When the workflow runs, Workflow Builder adds the Salesforce
`Annual Revenue` currency field to the workflow. A signer changes
an agreement's Annual Revenue value from
`$1,000,000 USD` to `$1,500,000 USD`.
When the workflow completes, Workflow Builder changes the record's Annual Revenue value from
$1,000,000 USD to $1,500,000 USD.

Use this procedure to add a currency field to Read from Salesforce and Writeback to Salesforce
steps:

1. [Create a basic workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uhm1697826856678.html&_LANG=enus) containing
   a [Read from Salesforce](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=idr1713985144297.html&_LANG=enus) step.
2. Open the step to the Which fields would you like to read?
   section.
   1. Select Add or Remove Fields.

      The Add or Remove Fields page displays.
   2. Select the check box next to each Salesforce
      currency type field that you'd like to
      use.
   3. Select Save and Exit.

      The Add or Remove Fields dialog box closes.
      The fields that you selected display.
   4. Select Next.
3. Which records are you reading from?
   1. Salesforce field: Select a currency field from
      the previous step.
   2. Operator: Choose an option like Equal
      to, Less than, and so on.
   3. Workflow field: Select the field and choose
      Manual entry.

      The currency field displays.
   4. Currency: Enter an amount in the field. You can
      only enter numbers, not letters, or symbols.
   5. Select a currency code from the dropdown menu at the left.
      USD is the default value.

      ![A screenshot displays the Which records are you reading from section with a currency field highlighted.](https://docusign-be-prod.zoominsoftware.io/api/bundle/qwr1706590641805/page/images/Workflow_Builder_Read_from_Salesforce_Which_records_are_you_reading_from_currency.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODIxNTU4NTQsInNoZWFmIjoicXdyMTcwNjU5MDY0MTgwNSJ9.eXErGCIk6lC0XUj1BzI0vPYvd86dx_5m-1XS-l1LsC8&_LANG=enus "A screenshot displays the Which records are you reading from section with a currency field highlighted.")
   6. Select Save.
   7. Select Done.
4. Complete the rest of your Read from Salesforce step and select
   Apply.
5. Open the Writeback to Salesforce step to the Which fields are you
   writing to? section.
   1. Select Add or Remove Fields.

      The Add or Remove Fields page displays.
   2. Select the check box next to each Salesforce
      currency type field that you'd like to
      use.
   3. Select Save and Exit.

      The Add or Remove Fields dialog box closes.
      The fields that you selected display.
   4. Select Next.
6. Fields: Configure your Salesforce currency field:
   1. Select the field and choose Manual entry.

      The currency field displays.
   2. Currency: Enter an amount in the field. You can
      only enter numbers, not letters, or symbols.
   3. Select a currency code from the dropdown menu at the left.
      USD is the default value.

      ![A screenshot displays the Which fields are you writing to section with a currency field highlighted.](https://docusign-be-prod.zoominsoftware.io/api/bundle/qwr1706590641805/page/images/Workflow_Builder_Writeback_to_Salesforce_Which_fields_are_you_writing_to_currency.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODIxNTU4NTQsInNoZWFmIjoicXdyMTcwNjU5MDY0MTgwNSJ9.eXErGCIk6lC0XUj1BzI0vPYvd86dx_5m-1XS-l1LsC8&_LANG=enus "A screenshot displays the Which fields are you writing to section with a currency field highlighted.")
   4. Select Save.
   5. Select Next.
7. Which records are you writing to?
   1. Salesforce field: Select a currency field from
      the previous step.
   2. Operator: Choose an option like Equal
      to, Less than, and so on.
   3. Workflow field: Select the field and choose
      Manual entry.

      The currency field displays.
   4. Currency: Enter an amount in the field. You can
      only enter numbers, not letters, or symbols.
   5. Select a currency code from the dropdown menu at the left.
      USD is the default value.
   6. Select Save.
   7. Select Done.
8. Complete the rest of your Send Documents for Signature step and select
   Apply.

You have completed the process. You have added and
configured a currency field in a Read from Salesforce and a Writeback to Salesforce
step. When the workflow runs, Docusign creates an agreement and adds
all mapped contacts and fields. When the workflow completes, Docusign
updates the record's currency field with any changes.
