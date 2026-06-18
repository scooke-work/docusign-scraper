---
title: Extensions and extension points
source_url: https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Extension Apps 101
- Extension Apps 101
- Concepts
- Concepts
- Extensions And Extension Points
scraped_at: '2026-06-18T19:51:50Z'
---

# Extensions and extension points

An extension contains the actions needed to support a type of external functionality, such as verifying data or writing files to cloud storage. Extensions can be defined in the [app manifest](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/#extensions) or through the [form-based experience](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#add-an-extension).

## Define an extension in the app manifest

In the app manifest, an extension is defined as a JSON object. Each extension has an *extension contract* (set by the `extension` object’s `template` property) that identifies its type, the required [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/), and the optional [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) that you implement to use it. See [Extension schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/extension/) for a list of supported `template` values and details about extension properties.

**Note:** The action names in the extension's `actionReferences` object must match the names in the [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) objects.

Example extension implementation:

```
"extensions": [
  {
    "name": "My File Output Cloud Storage Extension",
    "description": "Used to write files to cloud storage",
    "template": "FileIO.Version1.FileOutputCloudStorage",
    "actionReferences": [
      "list-directory-contents",
      "list-drives",
      "write-file"
    ],
    "capabilities": [
      "FileIO.Version1.ListDirectoryContents",
      "FileIO.Version1.ListDrives"
    ]
  }
]
```

## Define an extension using a form

Extensions can also be added to extension apps using a form. When you register an extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/), you will be prompted to choose the extensions that you want to include. See [Supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) for descriptions of each type, their extension points, and links to more information.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='554' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Extension type selection](https://images.ctfassets.net/aj9z008chlq0/nEi5C1tfcom3RGMkV6Lg5/b40bb51d5e02e742ba4efac55f68c780/FormBasedExtensionSelection.png?w=660&h=554&q=50&fm=png)

If you select **Data Input Output**, you have the option to select whether the extension app will only read data from a system of record or whether it will both read from and write to the system of record.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='245.99999999999997' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Data Input Output extension type selected](https://images.ctfassets.net/aj9z008chlq0/FkpKrbDMVqQTi4UGUtqL5/5a4f21e7d87731aa668a572c0c34fbed/FormBasedExtensionSelectionDataIO.png?w=660&h=246&q=50&fm=png)

If you select **Data Verification**, you can select the type of data the extension app will verify.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='486.99999999999994' width='660' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Extension Type Data Verification selected](https://images.ctfassets.net/aj9z008chlq0/68gKWENoHaZGoGX7KoVKOU/accafcb3e3301712eb0e3e7d4c6cd432/FormBasedExtensionSelectionDataVerification.png?w=660&h=487&q=50&fm=png)

If you select **File Input Output**, you must make an additional selection.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='426' width='782' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![File IO extension type](https://images.ctfassets.net/aj9z008chlq0/2n5jRwANky0dJCrXI1coPH/4b1050fe4001ac685e03c994a7d1a4d8/FileIOOptionsFormBased.png?w=782&h=426&q=50&fm=png)

Extensions can also be updated at the [extension app's integration details](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/integration-details/#access-integrations-details-for-an-extension-app) page.

## Extension points

An extension point is a location in the Docusign UI or a stage in a Docusign agreement process where an extension app can be invoked. eSignature envelopes, Agreement Builder workflows, Agreement Manager, and the **Add Fields** page in the prepare process are all extension points. For example, a file output cloud storage extension can be triggered to write a file generated during a Agreement Builder workflow to an external cloud storage system.

## Next steps

- Learn more about [connections](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/).
- Review the characteristics of [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) and [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/).
- See [sample app manifest files](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/) for different extensions.
- Get an overview of the [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/).

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
