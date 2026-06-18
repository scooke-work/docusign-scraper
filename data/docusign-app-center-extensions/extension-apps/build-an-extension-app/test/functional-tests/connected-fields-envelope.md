---
title: Connected fields extension envelope test
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/connected-fields-envelope/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Test
- Test
- Functional Tests
- Functional Tests
- Connected Fields Envelope
scraped_at: '2026-06-18T19:51:52Z'
---

# Connected fields extension envelope test

This procedure explains how to set up and execute a [functional test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) that invokes a [connected fields extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/) from an eSignature [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/).

This test checks the functioning of *connected fields*, which are envelope fields that can be verified by data verification or connected field extensions defined in your account. To set up the test, you add connected fields to an [eSignature template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=dqj1578456412286.html&rsc_301), generate an envelope from the template, and access the envelope via an emailed link. While viewing the envelope, you supply values in the connected fields to confirm that your extension is successfully invoked.

Instead of creating a template, you can add connected fields directly to an envelope. This test procedure specifies adding them to a template so that you can save and reuse it instead of adding connected fields to an envelope every time you want to test. Docusign also supports programmatically creating envelopes that include connected fields. See [Connected fields concepts](https://developers.docusign.com/docs/connected-fields-api/concepts/) for details.

The high-level steps to create and run this test are:

- [Step 1. Add connected fields to a template](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/connected-fields-envelope/#step-1-add-connected-fields-to-a-template)
- [Step 2. Generate and send an envelope](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/connected-fields-envelope/#step-2-generate-and-send-an-envelope)
- [Step 3. Access the envelope and supply data to verify](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/connected-fields-envelope/#step-3-access-the-envelope-and-supply-data-to-verify)

Make sure that you’ve completed all the requirements listed for functional tests in [Test prerequisites](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-prerequisites).

## Step 1. Add connected fields to a template

To add connected fields to a template:

1. Log in to the [eSignature web application](https://account-d.docusign.com/) and select **Templates** from the top navigation.
2. Do one of the following:
   - Follow the procedure in [To edit a template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=uvw1578456369720.html)﻿ if you want to add connected fields to an existing template.
   - Follow the procedure in [To create a template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html) to create a new template for the test.
3. While creating or editing the template, select **Next** to display the [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html).
4. In the left navigation, select the **Custom Fields** icon.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='248' width='185' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Custom fields icon](https://images.ctfassets.net/aj9z008chlq0/2BDLSs50vmtPosdZLQhNrJ/8242b162b6a8c0c100c13574399e52f8/CustomFieldsIcon.png?w=185&h=248&q=50&fm=png)
5. Expand the **App Fields** list. Then expand the entry that corresponds to your extension app name to display the list of connected fields. In the example shown here, the extension app name is **Transfer Authorization**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='575' width='395' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![App Fields list](https://images.ctfassets.net/aj9z008chlq0/6rhzrJdP56CTEC5S4LjFzd/7bc2c2fe4d048233f830a55b00faa9e7/AppFieldsListFunctionalTest.png?w=395&h=575&q=50&fm=png)

   The connected fields list includes every external system property under an object that has been marked with the `VerifiableType` decorator in the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) response. Properties that include the `IsRequiredForVerifyingType` decorator appear with an asterisk to indicate that they are required.

   If **App Fields** does not appear after you select **Custom Fields**, or if you do not see your extension app name under **App Fields**, then the extension app may not be installed or connected to your account. See [Run a connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) for instructions to install and connect it. Another potential cause is that Docusign was unable to process the [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names) or [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) response, possibly due to an error in the data model. To check this, run the [extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) for these two actions. You can use the [Concerto VSCode extension](https://concerto.accordproject.org/docs/tools/vscode/) to validate your data model and check for errors.
6. Drag any required connected field to the document. When you do so, all required connected fields will be added as a group.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='665' width='750' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Connected fields added to document as group](https://images.ctfassets.net/aj9z008chlq0/2Z61W0DPhlRSaip7XD99ut/5cc745917bb2836aa404e9a5415cf353/ConnectedFieldsOnDocBeforeRearrangeFunctionalTest.png?w=750&h=665&q=50&fm=png)

   If you want to include optional connected fields, drag them to the document, and they will be added to the field group. If you add an optional connected field to a document but do not include the required connected fields, verification will fail when you populate the optional field during envelope signing.
7. In the properties list on the right, expand **Data Verification**.
8. Confirm that your extension app name appears in the **Extension App** field.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='166' width='275' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Extension app name in properties for field](https://images.ctfassets.net/aj9z008chlq0/1y3z9z6yGw4u4tkDP30hu9/56f8332c88e2e51022eec5edded8b065/MustVerifyToSign.png?w=275&h=166&q=50&fm=png)
9. Select **Must verify to sign** to require successful verification of the envelope data to complete the signing process. If you leave this option unchecked, verification will still occur.

   You are not required to add a **Signature** field or any other fields to the template in order to test a connected fields extension.
10. Move the fields on the document to position them as appropriate.

    ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1573' width='1204' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

    ![Custom fields on document](https://images.ctfassets.net/aj9z008chlq0/39vIeV1wWTkhPNV1UHYH8X/ed87a5ef8f4705e7128710b920f4f459/CustomFieldsOnDocumentFunctionalTest.png?w=1204&h=1573&q=50&fm=png)
11. Apply [data validation](https://support.docusign.com/s/document-item?bundleId=gbo1643332197980&topicId=jgd1578456357365.html) to any connected fields that require it. For example, if you want a field to be populated with numbers only, select the **Numbers** validation option. See [Transform logic](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#transform-logic) for details about the default envelope field types for each data source type.
12. Select **Save and Close** to save the template.

Once you’ve saved the template, you can generate an envelope from it whenever you want to test your extension. For example, if you update your back-end API service code to fix an issue, you can test the fix by generating a new envelope. If you [update the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/), you’ll need to take additional steps before running this test again. See [Connection best practices](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/#connection-best-practices) for details.

## Step 2. Generate and send an envelope

Follow the procedure in [Use a Template to Create an Envelope](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=nxv1578456289719.html)﻿ to generate an envelope and email a link to view the envelope. When completing this procedure, supply an address where you can receive email.

## Step 3. Access the envelope and supply data to verify

When you receive the email:

1. Open it and select **Review Document**.
2. Enter values in all the connected fields. Each field has a tooltip that lists the `value` returned for the property in the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) response.
3. When all required connected field values have been supplied, Docusign invokes your extension to verify them. A **Verifying data** message is displayed, followed by a message to indicate whether verification succeeded or failed.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='1602' width='1494' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Connected fields verification succeeded](https://images.ctfassets.net/aj9z008chlq0/47IZtpsHsvxq2bLrcLLqwK/e290831b4b4ebc35d8390451346960ce/Signing_VerificationSucceededFunctionalTest.png?w=1494&h=1602&q=50&fm=png)
4. Confirm that:
   - Supplying valid values results in successful verification.
   - Supplying invalid values results in failed verification.
   - The verification messages returned with the responses appear as expected.
   - Any suggested values in the responses are autofilled as expected.
5. Changing any of the required connected field values causes the verification operation to be triggered again.

If your extension is not invoked successfully, run the Developer Console [connection and extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) for the extension app to get detailed error messages and troubleshoot.

## Next steps

- Find out more about [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/).
- Learn how to run [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/).
- Get an overview of the process to [publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/).

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
