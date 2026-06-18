---
title: Connect Category
source_url: https://developers.docusign.com/docs/esign-rest-api/reference/connect/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API Reference
- API Reference
- Connect
scraped_at: '2026-06-18T21:09:56Z'
---

# Connect Category

The Connect service enables your application to be called via
HTTPS when an event of interest occurs.

Use the Connect service to "end the polling madness." With
Connect, there is no need for your application to poll Docusign
every 15 minutes to learn the latest about your envelopes.

Instead, you register your interest in one or more types of
envelope or recipient events. Then, when an interesting event
occurs, the Docusign platform will contact your application with
the event's details and data. You can register interest in
envelopes sent by particular users in your account, or for
envelopes sent by any user.

Connect can empower your organization to manage document actions
as they occur, and allows you to track their changes within your
own systems. Upon completion, envelope information, including
document content, can be stored in your own databases or CMS
systems, and these events can be triggered via webhooks
delivering messages to your application.

**Note:** To make API calls to any of the Connect endpoints, you must be an account administrator.

## Incoming Connect Calls

To use the Connect service, your application needs to provide an
HTTPS URL that can be called from the public Internet. If your
application runs on a server behind your organization's firewall,
then you will need to create a "pinhole" in the firewall to allow
the incoming Connect calls from Docusign to reach your
application. You can also use other techniques such as proxy
servers and DMZ networking for receiving the incoming calls.

Connect delivers events over HTTP requests in JSON or XML.
See [Docusign Connect overview](https://developers.docusign.com/platform/webhooks/connect/).

If your application is not configured to accept post messages,
Docusign will NOT return an additional post error response to
your listener application. If you've enabled logging on your
configuration, it will be logged in Admin under the configuration
failure log.

## Per-envelope Connect Configuration

Instead of registering a general Connect configuration and
listener, an individual envelope can have its own Connect
configuration. See the
[`eventNotification`](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/#schema__envelopedefinition_eventnotification)
property for envelopes.

## Historical Publish Endpoint

To submit existing envelopes to an endpoint, use the [EnvelopePublish](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopepublish/) resource.

[ConnectConfiguration](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfiguration/)

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [createConnectSecret](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfiguration/createconnectsecret/) | [deleteConnectSecret](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfiguration/deleteconnectsecret/) | [getConnectSecret](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfiguration/getconnectsecret/) |

[ConnectConfigurations](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/)

Description

Contains information about a Docusign Connect configuration.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [create](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/create/) | [createConnectOAuthConfig](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/createconnectoauthconfig/) | [delete](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/delete/) |
| [deleteConnectOAuthConfig](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/deleteconnectoauthconfig/) | [get](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/get/) | [getConnectAllUsers](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/getconnectallusers/) |
| [getConnectOAuthConfig](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/getconnectoauthconfig/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/list/) | [listUsers](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/listusers/) |
| [update](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/update/) | [updateConnectOAuthConfig](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectconfigurations/updateconnectoauthconfig/) |  |

[ConnectEvents](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/)

Description

Connect event logging information. This object contains sections for regular Connect logs and for Connect failures.

##### Methods Supported

|  |  |  |
| --- | --- | --- |
| [delete](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/delete/) | [deleteFailure](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/deletefailure/) | [deleteList](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/deletelist/) |
| [get](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/get/) | [list](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/list/) | [listFailures](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/listfailures/) |
| [retryForEnvelope](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/retryforenvelope/) | [retryForEnvelopes](https://developers.docusign.com/docs/esign-rest-api/reference/connect/connectevents/retryforenvelopes/) |  |

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
