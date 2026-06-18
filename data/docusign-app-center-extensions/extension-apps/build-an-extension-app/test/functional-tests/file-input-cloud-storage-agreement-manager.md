---
title: File input cloud storage extension Agreement Manager test
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/file-input-cloud-storage-agreement-manager/
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
- File Input Cloud Storage Agreement Manager
scraped_at: '2026-06-18T19:51:53Z'
---

# File input cloud storage extension Agreement Manager test

This procedure explains how to set up and execute a [functional test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/) that invokes a [file input cloud storage extension](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/file-input-cloud-storage/) from [Docusign Agreement Manager](https://support.docusign.com/s/document-item?language=en_US&bundleId=pqz1702943441912&topicId=adf1702945446135.html).

Make sure that you’ve completed all the requirements listed for functional tests in [Test prerequisites](https://developers.docusign.com/extension-apps/build-an-extension-app/test/#test-prerequisites).

1. Log in to the [eSignature web application](https://account-d.docusign.com/).
2. Select **Agreements** from the top navigation.
3. Select **Completed** from the left navigation. The [Agreement List Table](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=yjz1702945473104.html) is displayed.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='695' width='1680' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Navigator Agreement List Table](https://images.ctfassets.net/aj9z008chlq0/4LF18W4QApdFVNmTozBGoK/84125b68d89928adc5e397c9b498e565/Navigator_AgreementListTable.png?w=1680&h=695&q=50&fm=png)
4. Select **Add Documents** and then **Upload**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='191' width='288' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Upload documents](https://images.ctfassets.net/aj9z008chlq0/ulG5QqNuSqTCHhw0ztSeV/6f3eee772552227a3f265e0c46426662/AddDocumentsUpload.png?w=288&h=191&q=50&fm=png)

   If The **Add Documents** option does not appear, your user permissions may need to be updated. See [User and Group Management](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=eut1712157553977.html) for details.
5. On the **Upload Documents** window, select **Select File**, and select your extension app from the list. Your app's listing uses the value of the [extensions.name](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) property in the app manifest.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='284' width='353' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Select extension app](https://images.ctfassets.net/aj9z008chlq0/3EeSyObvEoqF4HMDk6ZkBt/4331e96fa4c57a5eec4dcce374bfdad1/Navigator_SelectExtensionApp_testprocedure.png?w=353&h=284&q=50&fm=png)

   If the extension app is not [installed and connected](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) to your account, it will not appear in the list.
6. Select a [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/).

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='208' width='565' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Select a connection](https://images.ctfassets.net/aj9z008chlq0/B9Hf7LYqROjtLVDSxorwG/6336384cda74725380f3b2abc33d45ed/SelectConnection.png?w=565&h=208&q=50&fm=png)
7. If the extension app implements the optional [List Drives](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-drives) capability, Docusign launches a request to retrieve a list of cloud storage drives or similar container types, and displays the list on the **Select Files** window. Make a selection from the list.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='339' width='538' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Select drive](https://images.ctfassets.net/aj9z008chlq0/2zexxOW2tvCESlAzKaPbtj/a700a8da04e1459bd201f2e8f801a052/Navigator_SelectDrive_testprocedure.png?w=538&h=339&q=50&fm=png)
8. After selection of a drive, or after selection of your extension app if **List Drives** is not implemented, Docusign launches a [List Directory Contents](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#list-directory-contents) request. The list of folders and files in the response is displayed on the **Select Files** window.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='516' width='708' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Select folder](https://images.ctfassets.net/aj9z008chlq0/4axv7hHxjHzpDBRpgF7zKE/9f7df04c2b14bed82002ceeaaa550b58/Navigator_SelectFolder_testprocedure.png?w=708&h=516&q=50&fm=png)

   You can select a folder to display its contents. This launches another **List Directory Contents** request.
9. To test the [Search](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#search) action, enter a string in the **Search** field. The **Select Files** window displays the list of matching files and folders returned in the response.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='521' width='690' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Search](https://images.ctfassets.net/aj9z008chlq0/2bEdgx6mLbcq8l6q9EHCs/b843ba36c5956a2c83eb459237e01e87/Navigator_Search_testprocedure.png?w=690&h=521&q=50&fm=png)
10. To test the [Get File](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file) action, select one or more files, and select **Submit**. Docusign sends a separate **Get File** request for each selected file.
11. To check the status of the upload, from the Agreement List Table, select **Monitor All Jobs** from the kebab menu.

    ![](data:image/svg+xml;charset=utf-8,%3Csvg height='152' width='280' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

    ![Monitor upload jobs](https://images.ctfassets.net/aj9z008chlq0/3lWSU5zcad0yB54Zan1ZM/515e64ac8b8e4d792d4eea0c6dc7cdb9/MonitorAllJobs.png?w=280&h=152&q=50&fm=png)

    The status of the upload job is:
    **Transferring** on successful processing of the initial [Get File request](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#get-file-request-to-the-external-service) and response.
    **Upload to Agreement Manager complete** after successful processing of the [callback request](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/file-input-cloud-storage/#callback-request-to-docusign) and response.

    ![](data:image/svg+xml;charset=utf-8,%3Csvg height='645' width='1725' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

    ![Upload jobs](https://images.ctfassets.net/aj9z008chlq0/3vWuJR38uaYBXY5tC5yJlX/94c326d13755c41b1ea6657dba40003a/UploadJobs.png?w=1725&h=645&q=50&fm=png)

    After the upload is complete, the files appear in the Agreement List Table, and AI processing begins. AI processing time varies. See [Processing Agreements](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=rvw1736364838500.html) for details.
12. Select a file name in the Agreement List Table to view the [Agreement Preview Page](https://support.docusign.com/s/document-item?bundleId=pqz1702943441912&topicId=mut1702945643401.html), which displays the file and AI-extracted agreement data.

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
