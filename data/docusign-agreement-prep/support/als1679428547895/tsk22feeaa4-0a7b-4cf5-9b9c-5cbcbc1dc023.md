---
title: Add a Third-Party Field or Table to a Template
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=als1679428547895&topicId=tsk22feeaa4-0a7b-4cf5-9b9c-5cbcbc1dc023.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-22T19:55:19Z'
---

# Add a Third-Party Field or Table to a Template

## Before you begin

- Install the extension app for your third-party system and authorize a connection to your account.
- Create a template with a .docx file and edit the template using the ATB.

With the agreement template builder (ATB), you can insert third-party data fields and tables as sender fields into your templates. These fields act as dynamic placeholders that are automatically populated with data from a specific record in your third-party system when an agreement is generated.

To add third-party data fields, you first select the source object. While you can select only one **source object** per document, you can select multiple additional **related objects**. This gives you access to fields from multiple source objects, stemming from the selected source object for the document.

Note: While Docusign integrates with many systems of record, for illustration purposes, this topic presents how to add Salesforce object fields.

1. In your template editor, select the Sender role, and then select the Agreement Fields dropdown and chose your third-party connection. ![](https://docusign-be-prod.zoominsoftware.io/api/bundle/als1679428547895/page/images/select_connection.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODIxNTgwNzAsInNoZWFmIjoiYWxzMTY3OTQyODU0Nzg5NSJ9.QSdCFXZmo6L5gX0LoOYwCAYNSdBa0x8EGgbpNSrKxHc&_LANG=enus)

   This selection reflects the third-party system you installed and authorized. This help topic is using Salesforce as an example.
2. Search for and select the source object to use for the agreement.

   ![Selecting the source object.](https://docusign-be-prod.zoominsoftware.io/api/bundle/als1679428547895/page/images/select_source_object.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODIxNTgwNzAsInNoZWFmIjoiYWxzMTY3OTQyODU0Nzg5NSJ9.QSdCFXZmo6L5gX0LoOYwCAYNSdBa0x8EGgbpNSrKxHc&_LANG=enus "Selecting the source object.")

   The list of fields for the selected object are presented.
3. Position your cursor where you want to place a field, then select the desired field.
4. (Optional) Select the placed field to open the properties window.
   1. Add a field description.
   2. Enable the Required Field toggle to make the field required.
   3. Select Save.
5. To add a table:
   1. Select the Tables tab.

      The Tables tab displays all related objects that share a many-to-one relationship with your selected source object.
   2. Select the table that you want to add.

      The Create new Dynamic Table window opens.
   3. Select the + symbol for the fields that you want
      to add as columns for your table. Drag to reorder columns as needed.
   4. Select Create.
   5. To edit the table after you create it, select the table and then select
      the Configure table gear icon.
6. To add a field or table for a related object:
   1. Scroll to the bottom of the list of Salesforce fields and select Related Objects.
   2. Position your cursor where you want to insert the field or table and select it from the list.
   3. Adjust the properties as needed.
   4. Select Save.

      ![Example of a chain of multiple related objects to the document source object, "Account".](https://docusign-be-prod.zoominsoftware.io/api/bundle/als1679428547895/page/images/related_objects.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6ImRvY3VzaWduX3Byb2R1Y3Rpb24iLCJleHAiOjE3ODIxNTgwNzAsInNoZWFmIjoiYWxzMTY3OTQyODU0Nzg5NSJ9.QSdCFXZmo6L5gX0LoOYwCAYNSdBa0x8EGgbpNSrKxHc&_LANG=enus "Example of a chain of multiple related objects to the document source object, \"Account\".")

Your third-party field is added to your template document.
