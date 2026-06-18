---
title: ConnectConfigurations Resource
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Connect
- Connect
- Connectconfigurations
scraped_at: '2026-06-18T20:28:32Z'
---

# ConnectConfigurations Resource

The `ConnectConfigurations` resource enables you to configure the
Docusign Connect service for your account.

You can use this resource to configure account-level webhooks
that send notifications about every envelope sent from your
account. You can set account-level webhooks to listen for events
for envelopes sent by a specific user on your account, by
multiple specific users, or from any of the users on your
account. These events will be tracked, and can be delivered to a
listening application.

**Note:** To create an envelope-level webhook instead of using
account-level webhooks, use the Envelopes::Create method and add
an `eventNotification` object to an envelope object.

Docusign Connect offers two delivery modes:

- Send Individual Messages
- Send Aggregated Messages

By default, the Send Individual Messages mode
is enabled.
You can disable it
(enabling Aggregated Messages mode)
through Docusign Admin
in the **Updates** section.

**Note:** In either mode, Connect
[must be enabled](https://support.docusign.com/s/document-item?bundleId=pik1583277475390&topicId=ctv1583277395112.html)
in your Docusign account. It is not enabled by default.

## Send Individual Messages

Send Individual Messages (SIM) mode is the default.

In this mode Docusign delivers notifications for each
envelope events individually.
When a final recipient completes an envelope,
your listener will receive
a single **Recipient Signed/Completed** event
followed by a single **Envelope Signed/Completed** event
for the final participating party on the agreement.

For more information about SIM mode, see
[Using Connect's Send Individual Messages Feature](https://www.docusign.com/blog/developers/using-connects-send-individual-messages-feature).

## Aggregated Messages

In Aggregated Messages mode,
Connect aggregates similar events
into a single delivery.
Similar or simultaneous events
are aggregated,
so that your listener doesn't
receive extraneous messages.

When the final recipient signs an envelope, the
system delivers a single, aggregated Connect event, rather than
separate Recipient: complete and Envelope: complete messages.
This aggregation process ensures that you only receive the
minimal viable number of messages about an envelope's life cycle.

## Methods Supported

| Method | Description |
| --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/create/) | POST  ```  /restapi/v2.1/accounts/{accountId}/connect ```  Creates a Connect configuration. |
| [createConnectOAuthConfig](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/createconnectoauthconfig/) | POST  ```  /restapi/v2.1/accounts/{accountId}/connect/oauth ```  Set up Connect OAuth for the specified account. |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/delete/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/connect/{connectId} ```  Deletes the specified Connect configuration. |
| [deleteConnectOAuthConfig](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/deleteconnectoauthconfig/) | DEL  ```  /restapi/v2.1/accounts/{accountId}/connect/oauth ```  Delete the Connect OAuth configuration. |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/get/) | GET  ```  /restapi/v2.1/accounts/{accountId}/connect/{connectId} ```  Gets the details about a Connect configuration. |
| [getConnectAllUsers](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/getconnectallusers/) | GET  ```  /restapi/v2.1/accounts/{accountId}/connect/{connectId}/all/users ```  Returns all users from the configured Connect service. |
| [getConnectOAuthConfig](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/getconnectoauthconfig/) | GET  ```  /restapi/v2.1/accounts/{accountId}/connect/oauth ```  Retrieves the Connect OAuth information for the account. |
| [list](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/list/) | GET  ```  /restapi/v2.1/accounts/{accountId}/connect ```  Get Connect configuration information. |
| [listUsers](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/listusers/) | GET  ```  /restapi/v2.1/accounts/{accountId}/connect/{connectId}/users ```  Returns users from the configured Connect service. |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/update/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/connect ```  Updates a specified Connect configuration. |
| [updateConnectOAuthConfig](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/updateconnectoauthconfig/) | PUT  ```  /restapi/v2.1/accounts/{accountId}/connect/oauth ```  Updates the existing Connect OAuth configuration for the account. |

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
