---
title: Custom Field Extractions
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=condece8d7e-2da8-4e5f-8ba4-3f0175c2a625.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-18T15:46:44Z'
---

# Custom Field Extractions

Read about the custom field extractions, including entry points for creating new fields and a review of the AI detection setup wizard.

 

Custom field extractions are used to capture business-specific data points that standard extractions might not track. For example, use custom fields to capture terms, dates, amounts, and other details that are important to your organization.

Note: Administrators automatically have access to configure agreement data. For non-administrator users, this feature requires Organize and manage all agreements access to Agreement Manager. These tasks are primarily completed by administrators and contract managers.

You can configure each field once with a name, definition, and example agreements that show the target data. The AI model learns from those examples to detect and surface the values in your agreements, including selected historical agreements.

Custom field extractions expand your agreement insights to include unique, business-specific data points. Other benefits include:

- Reduced manual data entry.
- Improved data quality and consistency.
- Enhanced agreement insights and tailored reporting.

See the [Custom Extractions](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=yrx1747083411531.html&_LANG=enus "Read about custom extractions, including how these data points bring value to our organization.") topic to learn more about the custom extraction process.

## Supported custom field types

Custom fields capture specific, unique information that isn't covered by standard agreement fields. Agreement Manager supports these custom field types:![A snippet of the Add a field dialog box that shows the available field types for your custom fields.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Add-custom-field_Field-type-options.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Add a field dialog box that shows the available field types for your custom fields.")

- Text
- Number
- Date
- Dropdown

When using the Dropdown field type, you must provide a list of options for the dropdown:

![A snippet of the Add a field dialog box that shows the Options field for adding dropdown options.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Add-custom-field_Options-for-dropdown-type.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Add a field dialog box that shows the Options field for adding dropdown options.")

See the [Update Custom Dropdown Fields](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tskf056e8d3-baa4-41f2-8f71-12d0bb5c735b.html&_LANG=enus "Learn how to update the dropdown options for custom fields with the Dropdown field type.") topic to learn more about configuring custom dropdown fields.

Restriction: When integrating Docusign CLM with IAM, 'dropdown' field types cannot be mapped. For example, CLM attributes that correspond to custom dropdown fields in Agreement Manager cannot be mapped.

## 'Add a field' entry points

Use the Add a field function to configure new custom fields. For example, provide a name and specify the field type, agreement types, and category for the new field. Once created, enable the AI detection and activate the custom extraction.

You can launch the Add a field function from a number of entry points in Agreement Manager:

**Data management entry points**

The data management options are located in the  (gear) menu on the Agreement Manager homepage:

- Manage Fields page (Settings > Fields): Select the + Add Fields option from the top right.

  ![A snippet of the Manage Fields page that highlights the + Add Fields option in the top right.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extractions_Entry-point_Manage-Fields-page.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Manage Fields page that highlights the + Add Fields option in the top right.")
- Manage Agreement Types page (Settings > Agreement Types): Select the + Add Fields option from the agreement type detail page for a selected type.

  ![A snippet of the Manage Agreement Types page that highlights the + Add Fields option in the agreement type detail view.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extractions_Entry-point_Manage-Agreement-Types.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Manage Agreement Types page that highlights the + Add Fields option in the agreement type detail view.")

  See the topic to learn more about using this option.

**Agreement preview entry points**

There are two entry points for creating new fields from the Agreement preview page:

- Add (+) menu (Details pane): Expand the menu from the top of the Details pane and select the Add a Field option.

  Tip: Use this option to add metadata to an agreement without tying it to a specific sentence or clause. For example, you want to create a field to capture data about the agreement, like 'internal owner' or 'risk rating'. This information is not tied to a specific sentence or clause in the document.

  ![A snippet of the Agreement preview page that highlights the Add a Field option in the top right of the Details pane.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extractions_Entry-point_Agreement-Preview_Details.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Agreement preview page that highlights the Add a Field option in the top right of the Details pane.")
- Text highlighting (Preview pane): Highlight the relevant value from the preview pane. After selecting the text that you want to track, a menu opens. Select the Track with AI option.

  Tip: Use this option when you want to track content that is directly associated with specific text in the agreement. For example, you want to track a specific clause, sentence, or value in the agreement.

  ![A snippet of the Agreement preview page that shows a highlighted field value and the Track with AI option.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extractions_Entry-point_Agreement-preview_Track-with-AI.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Agreement preview page that shows a highlighted field value and the Track with AI option.")

See the [Create Custom Fields from the Agreement Preview](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk0830ea60-9b29-4efa-b73f-9eb15b2d6561.html&_LANG=enus "Learn how to create custom fields from the Agreement preview page for a selected agreement.") topic to learn more about using the Agreement preview options.

## Define custom field details

All of these entry points launch the Add a Field dialog box. However, the experience differs based on where you launched the feature.

**From data management pages:**

Complete the Add a Field dialog box to configure the custom field details. Enter a unique name and specify the field type, agreement types, and category:

![A screenshot of the Add a field dialog box that is used to configure new custom fields.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extractions_Add-a-field-dialog-box_basic-version.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A screenshot of the Add a field dialog box that is used to configure new custom fields.")

See the [Add Custom Fields to Agreement Types](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=hcn1736879099815.html&_LANG=enus "Learn how to create and add custom fields to the custom and standard agreement types in your account.") topic to learn about adding new fields from the data management pages.

**From the Agreement preview page:**

When accessing this function from the Agreement preview page, you have the option to initiate the AI setup. The dialog box has two parts: field configuration and AI setup initiation.

![A snippet of the Add a Field dialog box that shows the additional AI setup options.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extraction_Add-a-Field-dialog-box_new-experience.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Add a Field dialog box that shows the additional AI setup options.")

**Configure the field:**

Complete the top part of the Add a Field dialog box to define the new custom field:

![A snippet of the Add a Field dialog box that shows the required fields for defining a new field.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extractions_Add-a-field_top-portion.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Add a Field dialog box that shows the required fields for defining a new field.")

Enter a unique Field name and specify the Field type and Category for the field. The Agreement types field defaults to the agreement type of the current document. Select additional agreement types as needed.

**Initiate AI setup:**

Complete the bottom part of the Add a Field dialog box to initiate the AI detection setup process:

![A snippet of the Add a Field dialog box that shows the options for initiating the AI detection setup for the field.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extractions_Add-a-field_bottom-portion.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A snippet of the Add a Field dialog box that shows the options for initiating the AI detection setup for the field.")

The Use AI to find this field in future agreements option is selected by default. Leave this option selected if you want to surface the custom field in other agreements. For example, in newly completed agreements and in selected historical documents.

Tip: Deselect this option to opt out of AI detection for the field. It will not be surfaced in your other documents. You can Save the field configuration and add the AI detection later from the data management pages.

Provide a detailed definition for the custom field. This description informs the AI model of the field's purpose and use. The Refine with AI option displays after you enter at least 50 characters. Use this option to standardize and refine your definition.

Once you save your configuration, the Track this field with AI setup wizard opens.

Important: The Track this field with AI wizard is only launched when you add fields from the Agreement preview page. If you access the Add a Field function from the other entry points, the legacy AI detection setup wizard opens. Both follow the same high-level process steps.

See the [Create Custom Fields from the Agreement Preview](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk0830ea60-9b29-4efa-b73f-9eb15b2d6561.html&_LANG=enus "Learn how to create custom fields from the Agreement preview page for a selected agreement.") topic to learn about adding new fields from the Agreement preview page.

## 'Track this field with AI' setup wizard

When you create new custom fields from the Agreement preview page, the Track this field with AI setup wizard launches. Complete three steps to start tracking the custom field extraction with AI:

![A screenshot of the Track this field with AI setup wizard that displays when you create custom fields from the Agreement preview page.](https://docusign-be-prod.zoominsoftware.io/api/bundle/pqz1702943441912/page/images/Custom-field-extractions_Track-this-field-with-AI_setup-wizard.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODE3OTc2NDUsInNoZWFmIjoicHF6MTcwMjk0MzQ0MTkxMiJ9.WKDB4jc10g6HdauwcKGvb91Xo7oSHCkBRgz7SgKikVg&_LANG=enus "A screenshot of the Track this field with AI setup wizard that displays when you create custom fields from the Agreement preview page.")

1. **Define the field.** This step describes what the AI model should be looking for and what the data means. See these topics to learn more about defining the custom field for AI detection:

   - [Add Custom Fields to Agreement Types](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=hcn1736879099815.html&_LANG=enus "Learn how to create and add custom fields to the custom and standard agreement types in your account.")
   - [Create Custom Fields from the Agreement Preview](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk0830ea60-9b29-4efa-b73f-9eb15b2d6561.html&_LANG=enus "Learn how to create custom fields from the Agreement preview page for a selected agreement.")
2. **Select examples.** This step provides examples to show the AI model how the field value is displayed in your agreements. See the [Add Examples of Your Custom Fields](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tskcb56face-b8de-4cf9-85ce-6eac3669dd82.html&_LANG=enus "Learn how to complete the second step of the AI detection set-up process, Select examples.") topic for steps to complete this task.
3. **Test for accuracy.** This step helps you confirm that the AI model is finding the right data in your agreements. See these topics to learn more about testing for accuracy and activating the extraction:

   - [Test the Extraction Accuracy for Your Custom Fields](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=wjr1740452628309.html&_LANG=enus "Learn how to test the AI detection accuracy for your custom fields and refining the results to improve accuracy.")
   - [Activate Your Custom Fields](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk443eb55b-5980-4fa6-b145-e00b3415cdbe.html&_LANG=enus "Learn how to activate the AI detection for a custom field and surface it in selected historical agreements.")

Important: Use the Finish Later option to save your progress and finish the AI detection set-up later. Using this option ends the Track this field with AI experience. See the [Enable AI Detection for Your Custom Fields](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk02bd31a2-b125-4d53-b632-20d9972163a8.html&_LANG=enus "Learn how to enable the AI detection for your custom fields. Once activated, the field is surfaced in your new agreements automatically.") topic for steps to finish the process.

Once activated, the custom extraction is surfaced in your new agreements by default. The new data points are included in your agreement insights, such as filters, searches, dashboards, and reports.

You can select specific historical agreements to process for the new field. See the [Find Custom Fields in Specific Documents](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=tsk79824e36-d51d-4477-a5ca-7228cde30fb2.html&_LANG=enus "Learn how to use the Find On Specific Documents function to surface custom fields in selected agreements.") topic to learn about processing your historical agreements for custom fields.
