---
title: SigningGroups Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/signinggroups/signinggroups/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Signinggroups
- Signinggroups
- Signinggroups
scraped_at: '2026-06-18T21:10:27Z'
---

# SigningGroups Resource

The SigningGroups resource provides methods that enable you to manage [signing groups](https://support.docusign.com/s/document-item?bundleId=gav1643676262430&topicId=zgn1578456447934.html).

Signing groups enable you to create a group of people to which an envelope is sent. Any member of that group can open an envelope and sign the documents in the envelope with their own signature, even though a signature field was not directly assigned to them. When the signing group option is used, group members that open and sign the envelope are tracked in the envelope history and certificate.

When one group member opens the envelope, it is temporarily locked and if other members try to open the envelope they will see a message saying the envelope is currently opened. If the group member exits the envelope without finishing the lock expires, allowing other group members to open and complete the envelope.

When the envelope is complete, all members of the group will receive a completed notification and can access the completed envelope.
The envelope history and Certificate of Completion will show that the envelope was sent to a signing group and record which members viewed and signed the envelope.

An account can have a maximum of 50 signing groups. Each signing group can have a maximum of 50 group members.

The signing groups feature is only supported in certain Docusign Enterprise and System Automated Premium plans. To access this functionality, contact your Account Manager or Docusign Support ([support@docusign.com](mailto:support@docusign.com)) for assistance.

Next steps:

- Learn [how to create a signing group via the API](https://www.docusign.com/blog/dsdev-common-api-tasks-create-a-signing-group).
- Learn [how to request a signature from a signing group](https://www.docusign.com/blog/developers/common-api-tasks-requesting-signature-signing-group).

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/signinggroups/signinggroups/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/signing_groups ```  Creates a signing group. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/signinggroups/signinggroups/delete/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/signing_groups ```  Deletes one or more signing groups. |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/signinggroups/signinggroups/get/) | GET  ```  /restapi/v2.1/accounts/{accountId}/signing_groups/{signingGroupId} ```  Gets information about a signing group. |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/signinggroups/signinggroups/list/) | GET  ```  /restapi/v2.1/accounts/{accountId}/signing_groups ```  Gets a list of the Signing Groups in an account. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/signinggroups/signinggroups/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/signing_groups/{signingGroupId} ```  Updates a signing group. |
| [updateList](https://developers.docusign.com/docs/esign-rest-api/reference/signinggroups/signinggroups/updatelist/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/signing_groups ```  Updates signing group names. |

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
