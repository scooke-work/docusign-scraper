---
title: Data verification extension envelope test
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-verification-envelope/
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
- Data Verification Envelope
scraped_at: '2026-06-18T19:51:53Z'
---

# Data verification extension envelope test

This procedure explains how to set up and execute a [functional test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) that invokes a data verification extension from an eSignature [envelope](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/). Although the example screens are for a bank account verification extension, this procedure can be used with any data verification [extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/).

This test checks the functioning of *connected fields*, which are envelope fields that can be verified by data verification or connected field extensions defined in your account. To set up the test, you add connected fields to an [eSignature template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=dqj1578456412286.html&rsc_301), generate an envelope from the template, and access the envelope via an emailed link. While viewing the envelope, you supply values in the connected fields to confirm that your extension is successfully invoked.

Instead of creating a template, you can add connected fields directly to an envelope. This test procedure specifies adding them to a template so that you can save and reuse it instead of adding connected fields to an envelope every time you want to test. Docusign also supports programmatically creating envelopes that include connected fields. See [Connected fields concepts](https://developers.docusign.com/docs/connected-fields-api/concepts/) for details.

The high-level steps to create and run this test are:

- [Step 1. Add connected fields to a template](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-verification-envelope/#step-1-add-connected-fields-to-a-template)
- [Step 2. Generate and send an envelope](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-verification-envelope/#step-2-generate-and-send-an-envelope)
- [Step 3. Access the envelope and supply data to verify](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/data-verification-envelope/#step-3-access-the-envelope-and-supply-data-to-verify)

Make sure that you’ve completed all the requirements listed for functional tests in [Test prerequisites](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-prerequisites).

**Walkthrough playlist** You can also see video overviews of the data verification extension envelope test using the [Data Verification Reference Implementation](https://github.com/docusign/extension-app-data-verification-reference-implementation) below:

## Step 1. Add connected fields to a template

To add connected fields to a template:

1. Log in to the [eSignature web application](https://account-d.docusign.com/) and select **Templates** from the top navigation.
2. Do one of the following:
   - Follow the procedure in [To edit a template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=uvw1578456369720.html)﻿ if you want to add connected fields to an existing template.
   - Follow the procedure in [To create a template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=lsg1578456368117.html) to create a new template for the test.
3. While creating or editing the template, select **Next** to display the [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html).
4. In the left navigation, select the **Custom Fields** icon.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='232.00000000000003' width='260' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Custom fields icon](https://images.ctfassets.net/aj9z008chlq0/3Rhj2lGBverkb61lzKceay/bd37784a9905b53b8d135cdc9e149eb8/CustomFieldsIcon.png?w=260&h=232&q=50&fm=png)
5. Expand the **Verification** list to display a list of data verification extensions. See [Supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) for a complete list.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='465.00000000000006' width='260' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![List of data verification fields](https://images.ctfassets.net/aj9z008chlq0/3ZfYi6ta2fw5XHhw2HxbXI/04919496e7f8c6f4e95fda6563324892/VerificationList.png?w=260&h=465&q=50&fm=png)
6. Expand the extension you want to test. You'll see a list of connected fields that will appear in the envelope. For example, bank account verification requires an account number, account type, and routing number. These fields correspond to the required request properties for the extension's action contract.

   You can access the action and capability contracts for each [extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) from the [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) page.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='412.99999999999994' width='270' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Bank account verification field list](https://images.ctfassets.net/aj9z008chlq0/6QmsSRqvYPFccxxmzb8FnR/dafcbf06fd34cfc0a986fe584088610c/BankAccountFieldList.png?w=270&h=413&q=50&fm=png)

   If the fields are not enabled, then no extension app with this extension is installed to your account. See [Run a connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) for instructions to install an extension app to your account.
7. Drag the connected field group to the document. You can then move the fields individually to position them as appropriate.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='909' width='1732' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Bank account verification fields on document](https://images.ctfassets.net/aj9z008chlq0/4egqRukWDNw0hkNt2MxyNP/cf8ac182cf388a0c66407bdb1f8ecde9/BankAccountFieldsOnDocument.png?w=1732&h=909&q=50&fm=png)
8. In the properties list on the right, expand **Data Verification**.
9. Confirm that the correct value appears in the **Extension App** field. This is the **App name** you selected when you registered the extension app via the [form-based process](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), or the value from the [name](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) property in the app manifest if you registered the extension app by [uploading an app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/).
10. Select **Must verify to sign** if you want to require successful verification of the data supplied in the envelope in order to complete the signing process. If you leave this option unchecked, data verification will still occur.

    You are not required to add a **Signature** field or any other fields to the template in order to test a data verification extension.
11. Select **Save and Close** to save the template.

Once you've saved the template, you can generate an envelope from it whenever you want to test your extension. For example, if you update your back-end API service code to fix an issue, you can test the fix by generating a new envelope. In the current release, if you [update the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/), you'll need to create a new template or envelope to test with. In a future release, registration changes will automatically be propagated to existing templates.

## Step 2. Generate and send an envelope

Follow the procedure in [Use a Template to Create an Envelope](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=nxv1578456289719.html)﻿ to generate an envelope and email a link to view the envelope. When completing this procedure, supply an address where you can receive email.

## Step 3. Access the envelope and supply data to verify

When you receive the email:

1. Open it and select **Review Document**.
2. Select **Continue** to display the envelope.
3. Enter values in all the connected fields. Each field has a tooltip that lists the type of value expected in the field.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='568' width='1196' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Bank account verification signing view](https://images.ctfassets.net/aj9z008chlq0/zYt7kQET5Wgb7r5Q1uSPU/34f043b504736e2d881f8dc16707ebe1/BankAccountVerificationSigningView.png?w=1196&h=568&q=50&fm=png)
4. When all connected field values have been supplied, Docusign invokes your extension to verify them. A **Verifying data** message is displayed, followed by a message to indicate whether verification succeeded or failed. You should confirm that:
   - Supplying valid values results in successful verification.
   - Supplying invalid values results in failed verification.
   - For a postal address verification extension, supplying an address that results in a partial match returns a list of suggested addresses.
5. Changing any of the values causes the data verification operation to be triggered again.

If your extension is not invoked successfully, run the Developer Console [connection and extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) for the extension app to get detailed error messages and troubleshoot.

## Next steps

- Find out more about [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/).
- Learn how to run [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/).
- See how to use the [App Center preview](https://developers.docusign.com/extension-apps/build-an-extension-app/test/app-center-preview/).

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
