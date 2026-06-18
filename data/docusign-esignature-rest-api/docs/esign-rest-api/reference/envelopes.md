---
title: Envelopes Category
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Envelopes
scraped_at: '2026-06-18T20:28:16Z'
---

# Envelopes Category

The eSignature API Envelope category includes the resources and methods for sending and managing envelopes and envelope data.

Envelopes are the key objects in the Docusign platform. As a result, they are complex data structures with few required fields. See the [How-to guides](https://developers.docusign.com/docs/esign-rest-api/how-to/) for examples and solutions.

To learn more about envelopes, see [Envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/).

[ChunkedUploads](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/)

Description

The ChunkedUploads resource provides methods to complete integrity checks, and to add, commit, retrieve, initiate and delete chunked uploads.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [commit](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/commit/) | [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/delete/) |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/get/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/chunkeduploads/update/) |  |

[Comments](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/comments/)

Description

Details about envelope comments.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/comments/get/) |  |  |

[DocumentGeneration](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/)

Description

Document Generation for eSignature allows you to
dynamically generate
documents from a Word template to send for
signature within the eSignature sending workflow.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [getEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/getenvelopedocgenformfields/) | [updateEnvelopeDocGenFormFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentgeneration/updateenvelopedocgenformfields/) |  |

[DocumentResponsiveHtmlPreview](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentresponsivehtmlpreview/)

Description

This resource is used to create a responsive preview of a specific document.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/documentresponsivehtmlpreview/create/) |  |  |

[EnvelopeAttachments](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeattachments/)

Description

The EnvelopeAttachments resource provides methods that allow you to
associate files with an envelope.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeattachments/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeattachments/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeattachments/get/) |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeattachments/list/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeattachments/update/) |  |

[EnvelopeConsumerDisclosures](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeconsumerdisclosures/)

Description

Details about envelope consumer disclosures.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeconsumerdisclosures/get/) | [getDefault](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeconsumerdisclosures/getdefault/) |  |

[EnvelopeCustomFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopecustomfields/)

Description

An envelope custom field enables you to collect custom data about envelopes on a per-envelope basis. You can then use the custom data for sorting, organizing, searching, and other downstream processes. For example, you can use custom fields to copy envelopes or data to multiple areas in Salesforce. eOriginal customers can eVault their documents from the web app on a per-envelope basis by setting an envelope custom field with a name like "eVault with eOriginal?" to "Yes" or "No".

When a user creates an envelope, the envelope custom fields display in the **Envelope Settings** section of the Docusign console. Envelope recipients do not see the envelope custom fields. For more information, see [Envelope Custom Fields](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=qor1583277385137.html).

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopecustomfields/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopecustomfields/delete/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopecustomfields/list/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopecustomfields/update/) |  |  |

[EnvelopeDocumentFields](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentfields/)

Description

Envelope document fields

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentfields/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentfields/delete/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentfields/list/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentfields/update/) |  |  |

[EnvelopeDocumentHtmlDefinitions](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenthtmldefinitions/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenthtmldefinitions/get/) |  |  |

[EnvelopeDocuments](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/)

Description

Envelope documents

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/get/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/list/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/update/) | [updateList](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocuments/updatelist/) |  |

[EnvelopeDocumentTabs](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/)

Description

Document tabs are tabs that are associated with a document rather than with a recipient.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/get/) |
| [getByPage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/getbypage/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumenttabs/update/) |  |

[EnvelopeDocumentVisibility](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentvisibility/)

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
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentvisibility/get/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentvisibility/update/) | [updateRecipientsDocumentVisibility](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopedocumentvisibility/updaterecipientsdocumentvisibility/) |

[EnvelopeEmailSettings](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeemailsettings/)

Description

Envelope email settings

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeemailsettings/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeemailsettings/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeemailsettings/get/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeemailsettings/update/) |  |  |

[EnvelopeFormData](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeformdata/)

Description

This object contains the data that recipients have entered into the form fields associated with an envelope.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeformdata/get/) |  |  |

[EnvelopeHtmlDefinitions](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopehtmldefinitions/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopehtmldefinitions/list/) |  |  |

[EnvelopeLocks](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopelocks/)

Description

Envelope locks let you lock an envelope to prevent any changes while you are updating an envelope.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopelocks/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopelocks/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopelocks/get/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopelocks/update/) |  |  |

[EnvelopePublish](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopepublish/)

Description

The EnvelopePublish resource allows you to submit existing envelopes to any webhook.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [createHistoricalEnvelopePublishTransaction](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopepublish/createhistoricalenvelopepublishtransaction/) |  |  |

[EnvelopeRecipients](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/)

Description

Envelope recipients

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/create/) | [createEnvelopeRecipientPreview](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/createenveloperecipientpreview/) | [createRecipientManualReviewView](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/createrecipientmanualreviewview/) |
| [createRecipientProofFileResourceToken](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/createrecipientprooffileresourcetoken/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/delete/) | [deleteList](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/deletelist/) |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/list/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipients/update/) |  |

[EnvelopeRecipientTabs](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/)

Description

All of the tabs associated with a recipient. Each property is a list of a type of tab.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/delete/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/list/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/enveloperecipienttabs/update/) |  |  |

[Envelopes](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/)

Description

Envelope creation, management

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) | [deleteDocumentPage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/deletedocumentpage/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/) |
| [getNotificationSettings](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getnotificationsettings/) | [getPageImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getpageimage/) | [getPageImages](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getpageimages/) |
| [getRecipientInitialsImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getrecipientinitialsimage/) | [getRecipientSignature](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getrecipientsignature/) | [getRecipientSignatureImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/getrecipientsignatureimage/) |
| [listAuditEvents](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/listauditevents/) | [listStatus](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatus/) | [listStatusChanges](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/liststatuschanges/) |
| [rotateDocumentPage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/rotatedocumentpage/) | [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/) | [updateNotificationSettings](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/updatenotificationsettings/) |
| [updateRecipientInitialsImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/updaterecipientinitialsimage/) | [updateRecipientSignatureImage](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/updaterecipientsignatureimage/) |  |

[EnvelopeShares](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeshares/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [createEnvelopesShares](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeshares/createenvelopesshares/) |  |  |

[EnvelopeTemplates](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetemplates/)

Description

Envelope templates

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [apply](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetemplates/apply/) | [applyToDocument](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetemplates/applytodocument/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetemplates/delete/) |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetemplates/list/) | [listByDocument](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetemplates/listbydocument/) |  |

[EnvelopeTransferRules](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetransferrules/)

Description

This resource provides methods that enable account administrators to create and manage envelope transfer rules.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetransferrules/create/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetransferrules/delete/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetransferrules/get/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetransferrules/update/) | [updateEnvelopeTransferRule](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopetransferrules/updateenvelopetransferrule/) |  |

[EnvelopeViews](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/)

Description

Provides a URL that you can embed in your application
to provide access to the Docusign UI.

### Related topics

- [Embedded signing and sending](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/embedding/)
- [Send an envelope via your app](https://developers.docusign.com/docs/esign-rest-api/how-to/embedded-sending/)
- [Introducing customizable embedded sending](https://www.docusign.com/blog/developers/introducing-customizable-embedded-sending)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [createConsole](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createconsole/) | [createCorrect](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createcorrect/) | [createEdit](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createedit/) |
| [createRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createrecipient/) | [createSender](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createsender/) | [createSharedRecipient](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/createsharedrecipient/) |
| [deleteEnvelopeCorrectView](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeviews/deleteenvelopecorrectview/) |  |  |

[EnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/)

Description

Describes the workflow for an envelope or template.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [createEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/createenvelopeworkflowstepdefinition/) | [createTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/createtemplateworkflowstepdefinition/) | [deleteEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopedelayedroutingdefinition/) |
| [deleteEnvelopeScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopescheduledsendingdefinition/) | [deleteEnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopeworkflowdefinition/) | [deleteEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopeworkflowstepdefinition/) |
| [deleteTemplateDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplatedelayedroutingdefinition/) | [deleteTemplateScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplatescheduledsendingdefinition/) | [deleteTemplateWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplateworkflowdefinition/) |
| [deleteTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplateworkflowstepdefinition/) | [getEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopedelayedroutingdefinition/) | [getEnvelopeScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopescheduledsendingdefinition/) |
| [getEnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopeworkflowdefinition/) | [getEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopeworkflowstepdefinition/) | [getTemplateDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/gettemplatedelayedroutingdefinition/) |
| [getTemplateScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/gettemplatescheduledsendingdefinition/) | [getTemplateWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/gettemplateworkflowdefinition/) | [getTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/gettemplateworkflowstepdefinition/) |
| [updateEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopedelayedroutingdefinition/) | [updateEnvelopeScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopescheduledsendingdefinition/) | [updateEnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopeworkflowdefinition/) |
| [updateEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopeworkflowstepdefinition/) | [updateTemplateDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updatetemplatedelayedroutingdefinition/) | [updateTemplateScheduledSendingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updatetemplatescheduledsendingdefinition/) |
| [updateTemplateWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updatetemplateworkflowdefinition/) | [updateTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updatetemplateworkflowstepdefinition/) |  |

[NotaryJournals](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/notaryjournals/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/notaryjournals/list/) |  |  |

[ResponsiveHtmlPreview](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/responsivehtmlpreview/)

Description

This resource is used to create a responsive preview of all of the documents in an envelope.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/responsivehtmlpreview/create/) |  |  |

[TabsBlob](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/tabsblob/)

Description

Reserved for Docusign.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [getTabsBlob](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/tabsblob/gettabsblob/) | [putTabsBlob](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/tabsblob/puttabsblob/) |  |

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
