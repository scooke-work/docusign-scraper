---
title: API and UI functionality
source_url: https://developers.docusign.com/docs/web-forms-api/web-forms-101/api-ui-functionality/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Web Forms API
- Web Forms API
- Web Forms API 101
- Web Forms API 101
- API and UI functionality
scraped_at: '2026-06-18T19:46:29Z'
---

# API and UI functionality

The Web Forms API is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/?language=en_US) or your account manager to find out whether the Web Forms API is available for your production account plan.

In the current release, [web form configurations](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-configurations) can be created only with the [Web Forms builder](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=gpc1660591510274.html) UI in the eSignature web application. For creating and managing [web form instances](https://developers.docusign.com/docs/web-forms-api/web-forms-101/concepts/#web-form-instances), you must use the Web Forms API.

This table lists key Web Forms features and indicates which are supported in the Web Forms API and which are supported in the Web Forms builder.

| Feature | Supported in Web Forms API | Supported in Web Forms builder | Notes |
| --- | --- | --- | --- |
| Create, copy, modify, activate, or delete a web form configuration | No | Yes. See [Process to Build a Web Form﻿](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=qsr1660594082818.html) and related topics. | The ability to download a web form configuration, upload it to create a new configuration, and activate configurations will be supported in a future Web Forms API release. |
| [Create a web form instance](https://developers.docusign.com/docs/web-forms-api/how-to/create-embed-web-form-instance/) that is secure and unique to a user session | Yes | No | Although the Web Forms builder enables you to [get a web form URL](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=bxf1660605149279.html) to send to users, this URL is publicly accessible and not unique. See [Web form instance URLs](https://developers.docusign.com/docs/web-forms-api/plan-integration/instance-urls/) for details about security features available when using the API. |
| Programmatically [prefill](https://developers.docusign.com/docs/web-forms-api/plan-integration/prefill-instance-fields/) web form instance data | Yes | No | [Prefilling via the Web Forms builder](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=kwe1689726153105.html) requires you to construct a URL with query parameters. |
| Monitor [web form instance status](https://developers.docusign.com/docs/web-forms-api/plan-integration/track-instance-and-envelope-status/#web-form-instance-status) | Yes | No |  |
| Programmatically [retrieve data](https://developers.docusign.com/docs/web-forms-api/plan-integration/retrieve-submitted-values/) submitted in a web form instance | Yes | No | The Web Forms builder [CSV download](https://support.docusign.com/s/document-item?bundleId=gmi1660583110357&topicId=fld1681156856298.html) feature can be used to download user-entered data manually. This data is also available in the [Web Forms Data Report](https://support.docusign.com/s/document-item?bundleId=cnu1642812012214&topicId=vsu1689289293172.html). |
| Email a remote web form instance to users | Yes | No | The same web form configuration can be used to create both embedded and remote web form instances. However, individual web form instances support either embedded or remote delivery, but not both. |

## Next steps

- See [Web form instance processing](https://developers.docusign.com/docs/web-forms-api/web-forms-101/instance-processing/) for an overview of the interaction between a user, a Web Forms API integration, and the Docusign platform.
- See [Plan a Web Forms API integration](https://developers.docusign.com/docs/web-forms-api/plan-integration/) for an overview of the implementation details that you should consider before starting work on your application.

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
