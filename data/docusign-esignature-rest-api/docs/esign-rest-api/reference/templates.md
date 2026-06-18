---
title: Templates Category
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/templates/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Templates
scraped_at: '2026-06-18T21:09:56Z'
---

# Templates Category

Use the Templates category to manage your account's templates.

This section shows you how to perform the following tasks:

- Create, list, get, update, and delete templates.
- Manage the notification and group sharing settings for templates.
- Fetch and rotate pages from a document used by a template.

You can create templates either programmatically or through the Docusign web interface and then used by your application.

Additionally, [composite templates](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/templates/composite/) enable you to create a single envelope using a combination of multiple templates and documents. It's **highly recommended** that you use composite templates for your integration to make it more flexible and enable future modifications.

[TemplateCustomFields](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatecustomfields/)

Description

A template custom field enables you to prepopulate custom metadata for all new envelopes that are created by using a specific template. You can then use the custom data for sorting, organizing, searching, and other downstream processes.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatecustomfields/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatecustomfields/delete/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatecustomfields/list/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatecustomfields/update/) |  |  |

[TemplateDocumentFields](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentfields/)

Description

Template document fields

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentfields/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentfields/delete/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentfields/list/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentfields/update/) |  |  |

[TemplateDocumentHtmlDefinitions](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenthtmldefinitions/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenthtmldefinitions/list/) |  |  |

[TemplateDocumentResponsiveHtmlPreview](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentresponsivehtmlpreview/)

Description

This resource is used to create a responsive preview of a specific template document.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentresponsivehtmlpreview/create/) |  |  |

[TemplateDocuments](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/)

Description

Template documents

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/get/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/list/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/update/) | [updateList](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocuments/updatelist/) |  |

[TemplateDocumentTabs](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/get/) |
| [getByPage](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/getbypage/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumenttabs/update/) |  |

[TemplateDocumentVisibility](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentvisibility/)

Description

Document Visibility enables senders to control the visibility of the documents in an envelope at the recipient level. For example, if the parties associated with a legal proceeding should have access to different documents, the Document Visibility feature enables you to keep all of the documents in the same envelope and set view permissions for the documents by recipient. This functionality is enabled for envelopes and templates. It is not available for PowerForms.

**Note:** Before you use Document Visibility, you should be aware of the following information:

- Document Visibility must be enabled for your account by your Docusign administrator.
- A document cannot be hidden from a recipient if the recipient has tabs assigned to them on the document.
- When the Document Visibility setting hides a document from a recipient, the document also does not appear in the recipient's list of envelopes, documents, or page images.
- Carbon Copy, Certified Delivery (Needs to Sign), Editor, and Agent recipients can always see all of the documents associated with the envelope or template.

The Document Visibility feature has multiple settings that specify the options that senders have when sending documents. For more information, see [Use Document Visibility to Control Recipient Access](https://support.docusign.com/s/document-item?bundleId=gbo1643332197980&topicId=eui1578456411411.html).

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentvisibility/get/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentvisibility/update/) | [updateList](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatedocumentvisibility/updatelist/) |

[TemplateHtmlDefinitions](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatehtmldefinitions/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatehtmldefinitions/list/) |  |  |

[TemplateLocks](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatelocks/)

Description

This section provides information about template locks. You use template locks to prevent others from making changes to a template while you are modifying it.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatelocks/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatelocks/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatelocks/get/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templatelocks/update/) |  |  |

[TemplateRecipients](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/)

Description

Template recipients

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/create/) | [createTemplateRecipientPreview](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/createtemplaterecipientpreview/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/delete/) |
| [deleteList](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/deletelist/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/list/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipients/update/) |

[TemplateRecipientTabs](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/)

Description

Template tabs

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/delete/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/list/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templaterecipienttabs/update/) |  |  |

[TemplateResponsiveHtmlPreview](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templateresponsivehtmlpreview/)

Description

This resource is used to create a responsive preview of all of the documents associated with a template.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templateresponsivehtmlpreview/create/) |  |  |

[Templates](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/)

Description

Template management

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/create/) | [deleteDocumentPage](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/deletedocumentpage/) | [deleteGroupShare](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/deletegroupshare/) |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/get/) | [getDocumentPageImage](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/getdocumentpageimage/) | [getNotificationSettings](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/getnotificationsettings/) |
| [getPageImages](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/getpageimages/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/list/) | [rotateDocumentPage](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/rotatedocumentpage/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/update/) | [updateGroupShare](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/updategroupshare/) | [updateNotificationSettings](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/updatenotificationsettings/) |
| [updateTemplates](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/updatetemplates/) | [updateTemplatesAutoMatch](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/updatetemplatesautomatch/) |  |

[TemplateViews](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templateviews/)

Description

A TemplateView contains a URL that you can embed in your application to generate a template view that uses the Docusign user interface (UI).

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [createEdit](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templateviews/createedit/) |  |  |

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
