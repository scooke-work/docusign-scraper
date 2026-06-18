---
title: Customize elastic template fields
source_url: https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Click API
- Click API
- API 101
- API 101
- Customize Elastic Template Fields
scraped_at: '2026-06-18T22:18:20Z'
---

# Customize elastic template fields

You can create customizable fields (also called [tabs](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/tabs/)) within an elastic template using the dynamic content feature. *Dynamic content* enables you to add customized field values to each instance of a elastic signing agreement. For example, by defining the full name and email dynamic content for your elastic template, you can supply these values when you load an instance of it to show your user’s name and email within the agreement document.

Dynamic content field values are set when a URL for a elastic signing agreement is created or when it is embedded. They are not directly editable by users.

The following field types are supported:

| Dynamic content field name | JSON element name | Description |
| --- | --- | --- |
| Full name | `fullName` | A person’s full name. |
| Email | `email` | An email address. |
| Company | `company` | A company name. |
| Job Title | `title` | A job title. |
| Date | `date` | A date and time in YYYY-MM-DD format. |

Each dynamic content field type shares its value with all other fields of the same type in your document. For example, if you define two full name fields, they will both display the same value.

Dynamic content field data is stored in a `documentData` JSON element in your elastic template. The JSON structure of an elastic template with one or more dynamic content fields will look similar to the example below:

```
{
    environment: 'https://demo.docusign.net/',
    accountId: '9baa6115-xxxx-xxxx-xxxx-7088b86be96d',
    clickwrapId: '77daf49f-xxxx-xxxx-xxxx-726342483864',
    clientUserId: 'MyID',
    documentData: {
        email: 'user@example.com',
        fullName: 'myFirstName myLastName',
        company: 'Docusign',
        title: 'Saint Bernard Wrangler Application',
        date: '12/01/2021'
    }
},
```

This topic contains the following sections:

- [add dynamic content](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields/#add-dynamic-content-to-your-elastic-template)
- [View elastic templates that contain dynamic content](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields//#view-elastic-template-dynamic-content)
- [Set dynamic content as you generate the agreement](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields/#set-dynamic-content-generate)
- [Set dynamic content as you render the agreement](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields/#set-dynamic-content-render)
- [Create custom dynamic field types](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields/#create-custom-dynamic-field-types)

## Add dynamic content to your elastic template

You can only add dynamic content to your elastic templates through the UI, rather than programmatically through the API.

To add dynamic content fields to your elastic template:

1. Open the **Templates** panel in the [eSignature web app](https://apps-d.docusign.com/send/templates/).
2. Select the **Elastic Templates** tab.
3. Open the menu to the right of your chosen elastic template's **COPY CODE** button, then choose **Edit**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1422' width='2734' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Select EDIT from the drop-down menu](https://images.ctfassets.net/aj9z008chlq0/01BK4hguadsGQls1BXxySb/5202c708b5d0fd8ef97cfaba33f96cce/ElasticTemplatesEditMenu.png?w=2734&h=1422&q=50&fm=png)
4. Select the document to which you will add the dynamic content, select **Edit**, and then **Edit**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='942.0000000000001' width='1358' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Select the pen icon to edit the document](https://images.ctfassets.net/aj9z008chlq0/4aAR2ECDgHyM1BBLyWQ5xe/b765ee105878cfc70286059d5bbfc71b/EditDocumentsWindow.png?w=1358&h=942&q=50&fm=png)
5. In the **edit** document window, the available fields are displayed in a panel at the left of the screen. Select or drag-and-drop them to add them to your document.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='354' width='646' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Select the fields you want to add to the document](https://images.ctfassets.net/aj9z008chlq0/3rGrcrB9m65UAxzMvtGcOF/9d77360b272979ffc550b022ca01a805/dynamicFieldsAdd.jpg?w=646&h=354&fl=progressive&q=50&fm=jpg)
6. Select **SAVE** in the lower right corner of the screen.
7. Select **SAVE** on the **Edit Documents** window.
8. Select **SAVE & CLOSE** in the lower right corner of the screen.
9. Select an option on the **Require Re-acceptance** window and select **SAVE**. If you select **Yes**, returning users who have previously agreed to this elastic template must agree to it again.
10. Select an option on the **Activate New Version** window. If you select **ACTIVATE NOW**, the changes will immediately appear in all websites and apps where the elastic template is embedded.

You can set values for your dynamic content fields and view them by using the [Test elastic template feature](https://developers.docusign.com/docs/click-api/how-to/test-elastic-template/).

## View elastic templates that contain dynamic content

You can also embed elastic templates and display customized values for the dynamic content fields they contain.

There are two ways to generate elastic templates that contain dynamic content:

- [Set dynamic content as you generate the agreement](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields#set-dynamic-content-generate)**:** In this method, you generate the agreement by passing in the dynamic content values as parameters for the [ClickWraps:createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/) API call. This sets the values as the agreement is created, making this the most secure method of setting and viewing dynamic content.
- [Set dynamic content as you render the agreement](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields#set-dynamic-content-render)**:** You can also choose to set your dynamic content values as you render the agreement.

> **Note:** For compatibility with previous versions of the Click API, elastic templates use clickwrap endpoints.

### Set dynamic content as you generate the agreement

To set customized values for your elastic template agreement's dynamic content fields as you generate it, follow the steps below:

1. Select the **COPY CODE** button for the elastic template to display. It must be activated and contain dynamic content fields to set.
2. In the elastic template details from step 1 of the **Copy Code** dialog box, copy the `documentData` JSON element and paste it into a place where you can edit text, such as Notepad.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1416' width='1474' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Copy the documentData from the UI](https://images.ctfassets.net/aj9z008chlq0/1tuxEcDxTwVxulnnOfXry2/9c2afeb5bb3289a7ae76eb4ea95fec20/CopyCodeWindow.png?w=1474&h=1416&q=50&fm=png)
3. The `documentData` values that you just copied are placeholders for each dynamic content field defined in your document. Replace these placeholders values with the ones you want to use when you view the elastic template.
4. Add quotation marks (`"` characters) around the elements within `documentData`. The following screenshot demonstrates a formatted `documentData` element with custom dynamic field values added to it:

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='271' width='464' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Change the documentData into JSON format in a tool such as Notepad](https://images.ctfassets.net/aj9z008chlq0/6Mc0Q9KvwnPYAi4CfKuQSs/7fab91092ced6d0cd318239f99008c7c/generateDynamicClickwrap2.png?w=464&h=271&q=50&fm=png)
5. Generate the viewing URL by making a [ClickWraps:createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/) method call, providing your account ID and clickwrap ID in the path. For the call body, choose a unique `clientUserId` for the viewer and add the `documentData` JSON element that you created in the previous step, as shown in the example below.

   ```
   {
     "clientUserId": "ExampleUserID",
     "documentData": {
       "fullName": "My example name",
       "email": "example@docusign.com",
       "company": "Docusign",
       "title": "Saint Bernard Wrangler",
       "date": "2021-12-01"
   }
   ```

   **Note**: The [ClickWraps:createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/) method requires that you obtain both the `click.manage` and `click.send` scopes during [Authentication](https://developers.docusign.com/docs/click-api/click101/auth/). If you do not have these scopes, you will receive response code 401 - unauthorized.
6. The [ClickWraps:createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/) method call will return a set of data about the created agreement session. The `agreementUrl` field in the response contains the URL of the agreement session that your recipients can use to open and view it. You can do this in two ways:
   - You can send the URL directly to your recipient to have them view the agreement session.
   - You can use The `agreementUrl` to embed your elastic signing agreement in your web page or app HTML. This enables you to apply your styles to how it is displayed. For example:

     ```
     <div id="ds-terms-of-service"></div>
     <script src="https://demo.docusign.net/clickapi/sdk/latest/docusign-click.js"></script>

     <script>docuSignClick.Clickwrap.render({
     agreementUrl: '<YOUR_AGREEMENT_URL>'
     }, '#ds-terms-of-service');</script>
     ```

     See [How to embed an elastic signing agreement](https://developers.docusign.com/docs/click-api/how-to/embed-elastic-templates/) for a more detailed set of step-by-step instructions on how to embed the elastic signing agreement in your app.

### Set dynamic content as you render the agreement

To set customized values for dynamic content fields when embedding your elastic template, use the following steps:

1. Select the **COPY CODE** button for the elastic template to display. It must be activated and contain dynamic content fields to set.
2. Copy the elastic template details from step 1 of the **Copy Code** dialog box.
3. Update the `documentData` JSON element with values for your dynamic content fields. An example set of elastic template details containing the `documentData` JSON is shown below:

   ```
   <div id="ds-clickwrap"></div>
       <script src="https://demo.docusign.net/clickapi/sdk/latest/docusign-click.js"></script>
       <script>docuSignClick.Clickwrap.render({
       environment: 'https://demo.docusign.net',
       accountId: '9baa6115-xxxx-xxxx-xxxx-7088b86be96d',
       clickwrapId: '0ea010d8-xxxx-xxxx-xxxx-ef3b6b2e29de',
       clientUserId: '464f7988-xxxx-xxxx-xxxx-781ee556ab7a',
       documentData: {
           email: 'user@example.com',
           fullName: 'myFirstName myLastName',
           company: 'Docusign',
           title: 'Saint Bernard Wrangler',
           date: '2021-12-01'
       }
   },

   '#ds-clickwrap');</script>
   ```
4. Embed the elastic template as described in this developer guide: [How to embed an elastic signing agreement](https://developers.docusign.com/docs/click-api/how-to/embed-elastic-templates/).
5. View the responses through your Docusign account on the Manage page or use the Docusign Click API to manage responses. See the [API documentation](https://developers.docusign.com/docs/click-api/reference/) for details.

## Create custom dynamic field types

Every elastic template has a standard set of supported dynamic fields: full name, email, company, job title, and date. In addition to these standard dynamic fields, you can add your own custom dynamic field types when you create an elastic template with the [ClickWraps:createClickwrap](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createclickwrap/) endpoint or through the Docusign web app.

To define new dynamic field types with the API:

1. Add a dataFields entry to your elastic template definition JSON.
2. Within this dataFields entry, add an object that contains a label, type (such as string, number, or date), and name for every new dynamic field type to add.

   The below example elastic template definition demonstrates the syntax for defining custom dynamic field types for each valid format (string, number, and date) within a JSON elastic template definition.
   - Only numeric characters can be input to a number field.
   - Date fields can only accept input in mm/dd/yyyy or [ISO Date](https://www.iso.org/iso-8601-date-and-time-format.html) format.

     ```
     {
       "displaySettings": {
         "consentButtonText": "I Agree",
         "displayName": "Terms of Service",
         "downloadable": true,
         "format": "modal",
         "hasAccept": true,
         "mustRead": true,

         "requireAccept": true,
         "size": "medium",
         "documentDisplay": "document"
       },
       "documents": [
         {
           "documentBase64": "JVBERi…VPRgo=",
           "documentName": "Terms of Service",
           "fileExtension": "pdf",
           "order": 0
         }
       ],
       "dataFields" : [
         {
             "label": "newLabel1",
             "type":"STRING",
             "name":"newkey1"
         },
         {
             "label": "newLabel2",
             "type":"NUMBER",
             "name":"newkey2"
         },
         {
             "label": "newLabel3",
             "type":"DATE",
             "name":"newkey3"
         }
       ],
       "name": "Terms of Service",
       "requireReacceptance": true
     }
     ```
3. When you’ve added all of your custom dynamic fields, call the [ClickWraps:createClickwrap](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createclickwrap/) API endpoint, providing the elastic template JSON that you defined in the previous step. This creates a new elastic template that will include your new types as options when you add dynamic fields.

Use the steps documented in [add dynamic content](https://developers.docusign.com/docs/click-api/click101/customize-elastic-template-fields/#add-dynamic-content-to-your-elastic-template) to add dynamic content to an elastic template document. Your new custom dynamic field types will appear as options when choosing which dynamic fields to add.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='529' width='541' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Shows custom dynamic field types in the elastic template tester](https://images.ctfassets.net/aj9z008chlq0/5brmrOHWPS7tpZESYNf3Ms/7104c8f003a0e70cd2cf3ca5ef434fd9/testCustomDynamicFieldTypes.png?w=541&h=529&q=50&fm=png)

 **Note:** You can also create custom dynamic field types through the Docusign web app UI. See [Bulk Import Data Fields to Insert User Data or Add Metadata to Your Documents](https://support.docusign.com/s/document-item?language=en_US&bundleId=igo1666647424726&topicId=tvt1660113089575.html&_LANG=enus) for details.

## Next steps

- See [How to create an elastic template](https://developers.docusign.com/docs/click-api/how-to/create-elastic-templates/)
- See [How to embed an elastic signing agreement](https://developers.docusign.com/docs/click-api/how-to/embed-elastic-templates/)
- See [How to test an elastic template](https://developers.docusign.com/docs/click-api/how-to/test-elastic-template/)
- See [ClickWraps:createHasAgreed](https://developers.docusign.com/docs/click-api/reference/accounts/clickwraps/createhasagreed/)

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
