---
title: Troubleshoot Spreadsheet Upload Errors
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=ref4dcc5ebd-8791-48fd-98e6-5c5d6bae7bc5.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T15:32:12Z'
---

# Troubleshoot Spreadsheet Upload Errors

Look up troubleshooting steps for resolving errors during the metadata spreadsheet upload.

Look up troubleshooting steps to resolve your validation errors from the metadata spreadsheet upload.

## Error: Invalid file. Upload the CSV file you generated in Docusign.

If you attempt to upload external spreadsheets, including files generated from other Intelligent Agreement Management (IAM) features, the files are rejected:

![A screenshot of the Import data from a spreadsheet dialog box that shows the "Invalid file" error message.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Bulk-metadata-editing_Import-data-from-spreadsheet_Invalid-file.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTY3ODgsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.VReYtu1_7vAeAJAFiZeCIj73u3C9yQv4lUnMV2qwnZo&_LANG=enus "A screenshot of the Import data from a spreadsheet dialog box that shows the \"Invalid file\" error message.")

**Resolution**

Use the Select File option to search for and select the pre-formatted spreadsheet file. This is the file that you downloaded from Agreement Manager and updated with agreement data for the selected agreements.

Complete these tasks to start with a fresh spreadsheet file:

1. [Download the Pre-Formatted Spreadsheet File](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk1b94afc6-712f-4d71-868e-0787867354d8.html&_LANG=enus "Learn how to download the pre-formatted spreadsheet file for a group of documents.")
2. [Edit the Metadata Spreadsheet](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk8710c3f2-c881-4219-96b0-2b287e8b4e03.html&_LANG=enus "Learn how to edit the metadata spreadsheet file to bulk update the agreement data for the selected documents.")
3. [Import Your Edited Metadata Spreadsheet](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk5ab1cd5b-00f7-42a9-bd77-728baadff903.html&_LANG=enus "Learn how to import your edited metadata spreadsheet using the Add (+) menu located on the Agreement Manager homepage.")

## Error: You need permission to edit this agreement

This error message is displayed if you do not have permission to edit the metadata for an agreement. Any of these permissions grant users access to update the agreement metadata:

- Can Manage access to the agreement
- Can Edit access to the agreement
- Organize and manage all agreements access to Agreement Manager agreements and functionality

**Resolution**

Remove the agreement from the metadata spreadsheet file and re-import the data:

1. Open the metadata file and locate the row that contains the relevant agreement.
2. Delete the row from the spreadsheet.
3. Save your changes and close the spreadsheet.
4. Upload the spreadsheet file to Agreement Manager.

## Error: [Field Name] must follow the format: [Number][Space][Currency]

This error message is displayed when a field has an invalid currency format:

![A snippet of the Job status page that highlights the error message for a file that could not be updated.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Bulk-metadata-editing_Job-status_Error-details_NumberSpaceCurrency.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTY3ODgsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.VReYtu1_7vAeAJAFiZeCIj73u3C9yQv4lUnMV2qwnZo&_LANG=enus "A snippet of the Job status page that highlights the error message for a file that could not be updated.")

**Resolution**

Update the cell value in the metadata spreadsheet file and re-import the data:

1. Open the metadata file and locate the row that contains the relevant agreement.
2. Scroll to locate the column and cell for the field with the invalid currency format.
3. Update the value so it follows the required format, [Number][Space][Currency code]. For example, 10000 USD.
4. Save your changes and close the spreadsheet.
5. Upload the spreadsheet file to Agreement Manager.

## Error: [Field Name] must be a valid date and follow the format: MM/DD/YYYY

This error message is displayed when a field has an invalid date format. The date follows the U.S. format, MM/DD/YYYY. It is not localized based on the user's location.

![A snippet of the Job status page that highlights the error message for a file that could not be updated.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Bulk-metadata-editing_Job-status_Error-details_MM-DD-YYYY.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTY3ODgsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.VReYtu1_7vAeAJAFiZeCIj73u3C9yQv4lUnMV2qwnZo&_LANG=enus "A snippet of the Job status page that highlights the error message for a file that could not be updated.")

**Resolution**

Update the cell value in the metadata spreadsheet file and re-import the data:

1. Open the metadata file and locate the row that contains the relevant agreement.
2. Scroll to locate the column and cell for the field with the invalid date format.
3. Update the value so it follows the required format, MM/DD/YYYY.
4. Save your changes and close the spreadsheet.
5. Upload the spreadsheet file to Agreement Manager.

## Error: [Field Name] must follow the format: [Number][Space][Time Unit]

This error message is displayed when a field has an invalid duration format:

![A snippet of the Job status page that highlights the error message for a file that could not be updated.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Bulk-metadata-editing_Job-status_Error-details_NumberSpaceTimeUnit.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTY3ODgsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.VReYtu1_7vAeAJAFiZeCIj73u3C9yQv4lUnMV2qwnZo&_LANG=enus "A snippet of the Job status page that highlights the error message for a file that could not be updated.")

**Resolution**

Update the cell value in the metadata spreadsheet file and re-import the data:

1. Open the metadata file and locate the row that contains the relevant agreement.
2. Scroll to locate the column and cell for the field with the invalid duration format.
3. Update the value so it follows the required format, [Number][Space][Time Unit].

   Note: Common time units are: Years, Months, Weeks, and Days. The time unit value is case-sensitive. Capitalize the first letter. For example, "5 Years" instead of "5 Y" or "5 years".
4. Save your changes and close the spreadsheet.
5. Upload the spreadsheet file to Agreement Manager.

## Error: [Field Name] must follow the format: [Name] | [Role]

This error message is displayed when a Parties cell contains an invalid format or is missing information:

![A snippet of the Job status page that highlights the error message for a file that could not be updated.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Bulk-metadata-editing_Job-status_Error-details_NameRole.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTY3ODgsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.VReYtu1_7vAeAJAFiZeCIj73u3C9yQv4lUnMV2qwnZo&_LANG=enus "A snippet of the Job status page that highlights the error message for a file that could not be updated.")

**Resolution**

Update the cell value in the metadata spreadsheet file and re-import the data:

1. Open the metadata file and locate the row that contains the relevant agreement.
2. Scroll to locate the column and cell for the field with the invalid parties format.
3. Update the value so it follows the required format:

   1. Enter the party name and role, separated with the pipe (vertical line) divider. For example, Fontara | Buyer.

      Important: The Role is required when populating the Parties column. If you are unsure of the role or do not want to include one, use the format: [Party Name] | [None]. For example, Fontara | None.
   2. Enter additional party names and roles as needed. Use semicolons to separate the party values. For example, Fontara | Buyer; Liberty Innovations | Seller;
4. Save your changes and close the spreadsheet.
5. Upload the spreadsheet file to Agreement Manager.

## Error: [Field Name] must be a valid number

This error message is displayed when a field has an invalid number format. Numbers are entered without commas.

Note: Decimals are approved where the field supports them. For example, 2500.75.

**Resolution**

Update the cell value in the metadata spreadsheet file and re-import the data:

1. Open the metadata file and locate the row that contains the relevant agreement.
2. Scroll to locate the column and cell for the field with the invalid number format.
3. Update the value so it follows the required format. Enter digits only, no commas.
4. Save your changes and close the spreadsheet.
5. Upload the spreadsheet file to Agreement Manager.

## Error: [Field Name] exceeds character limit

This error message is displayed if one of your cell values exceeds the maximum character limit for a text field. The spreadsheet supports up to 2,000 characters for custom fields and 400 characters for standard fields.

Important: Depending on how the standard fields are used across the platform, the maximum character limit can vary.

**Resolution**

Update the cell value in the metadata spreadsheet file and re-import the data:

1. Open the metadata file and locate the row that contains the relevant agreement.
2. Scroll to locate the cell that exceeds the maximum character limit.
3. Edit the value so that it is less than the maximum character limit.
4. Save your changes and close the spreadsheet.
5. Upload the spreadsheet file to Agreement Manager.

## Error: Something went wrong when attempting to update the agreement

This generic error message is displayed when an unidentified error occurs. Unidentified errors are issues that do not match any of the specific cases that are logged:

![A snippet of the Job status page that highlights the error message for a file that could not be updated.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Bulk-metadata-editing_Job-status_Error-details_Something-went-wrong.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTY3ODgsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.VReYtu1_7vAeAJAFiZeCIj73u3C9yQv4lUnMV2qwnZo&_LANG=enus "A snippet of the Job status page that highlights the error message for a file that could not be updated.")

**Resolution**

If you receive this error message, try to upload the file again. If the error message persists, contact your system administrator for help. Your administrators have access to logs on their end to triage and monitor such cases.
