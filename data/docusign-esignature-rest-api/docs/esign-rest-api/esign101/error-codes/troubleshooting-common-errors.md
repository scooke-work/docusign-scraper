---
title: Troubleshooting for common errors
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Error codes
- Error codes
- Troubleshooting common errors
scraped_at: '2026-06-18T21:09:48Z'
---

# Troubleshooting for common errors

This page contains troubleshooting recommendations for common API errors.

Error responses consist of an [error code](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/) (typically all uppercase with underscores between words) and an error message that provides details. If the error code you received is listed in this topic, but the error message doesn’t match the one you received, the recommendations may still be relevant and are worth reviewing. You can also check the following resources:

- [Docusign Developer Community](https://community.docusign.com/developer-59)
- [Docusign Developer FAQ](https://support.docusign.com/s/articles/DocuSign-Developer-Support-FAQs?language=en_US&rsc_301.)
- Docusign topics on [Stack Overflow](http://bit.ly/DocuSignAPISO)

If you have a paid support plan or you are enrolled in the [Docusign Partner Program](https://partners.docusign.com/s/join-now), another option is to open a support case with [Docusign Support](https://support.docusign.com/s/contactSupport). See [FAQ: Support for developers and Docusign APIs](https://support.docusign.com/s/articles/FAQ-Support-for-developers-and-Docusign-APIs) for details about support plans
> **Note:** If this topic doesn’t cover an error you received, you can use our rating and feedback form at the bottom of this page to let the Developer Center team know. After you select a rating, you’ll see a text field where you can provide additional information. Please include the exact error code and error message you received, and the request that caused the error. We’ll add it to our list for future enhancements to this page.

Below is a list of error codes covered in this topic:

- [ACCOUNT\_LACKS\_PERMISSIONS](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#account-lacks-permissions)
- [ACCOUNT\_NOT\_AUTHORIZED\_FOR\_ENVELOPE](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#account-not-authorized-for-envelope)
- [AUTHORIZATION\_INVALID\_TOKEN](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#authorization-invalid-token)
- [DOCUMENT\_DOES\_NOT\_EXIST](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#document_does_not_exist)
- [DOCUMENT\_UPLOAD\_NOT\_ALLOWED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#document_upload_not_allowed)
- [EDIT\_LOCK\_ENVELOPE\_ALREADY\_LOCKED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#edit-lock-envelope-already-locked)
- [EDIT\_LOCK\_ENVELOPE\_NOT\_LOCKED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#edit-lock-envelope-not-locked)
- [ENVELOPE\_ALLOWANCE\_EXCEEDED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#envelope-allowance-exceeded)
- [ENVELOPE\_CANNOT\_VOID\_INVALID\_STATE](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#envelope_cannot_void_invalid_state)
- [ENVELOPE\_DOES\_NOT\_EXIST](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#envelope-does-not-exist)
- [ENVELOPE\_INVALID\_STATUS](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#envelope_invalid_status)
- [HOURLY\_APIINVOCATION\_LIMIT\_EXCEEDED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#hourly-apiinvocation-limit-exceeded)
- [HOURLY\_ENVELOPE\_POLLING\_LIMIT\_EXCEEDED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#hourly-envelope-polling-limit-exceeded)
- [INVALID\_CAPTIVE\_RECIPIENT\_OPERATION](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#invalid-captive-recipient-operation)
- [INVALID\_EMAIL\_ADDRESS\_FOR\_RECIPIENT](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#invalid-email-address-for-recipient)
- [INVALID\_RECIPIENT\_ID](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#invalid_recipient_id)
- [INVALID\_REQUEST\_PARAMETER](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#invalid-request-parameter)
- [ONESIGNALLSIGN\_NOT\_SATISFIED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#onesignallsign_not_satisfied)
- [PARTNER\_AUTHENTICATION\_FAILED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#partner-authentication-failed)
- [PAGE\_IMAGE\_NOT\_FOUND](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#page_image_not_found)
- [PLAN\_ITEM\_NOT\_ENABLED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#plan-item-not-enabled)
- [RECIPIENT\_NOT\_IN\_SEQUENCE](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#recipient-not-in-sequence)
- [RESOURCE\_NOT\_FOUND](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#resource-not-found)
- [SIGNATURE\_PROVIDER\_INVALID\_NAME](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#signature-provider-invalid-name)
- [UNABLE\_TO\_LOAD\_DOCUMENT](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#unable_to_load_document)
- [UNKNOWN\_ENVELOPE\_RECIPIENT](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#unknown-envelope-recipient)
- [UNSUPPORTED\_PDF\_CONTENT](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#unsupported-pdf-content)
- [USER\_AUTHENTICATION\_FAILED](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#user-authentication-failed)
- [USER\_DOES\_NOT\_BELONG\_TO\_SPECIFIED\_ACCOUNT](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#user-does-not-belong-to-specified-account)
- [USER\_DOES\_NOT\_EXIST\_IN\_SYSTEM](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#user-does-not-exist-in-system)
- [USER\_LACKS\_MEMBERSHIP](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#user-lacks-membership)
- [USER\_LACKS\_PERMISSIONS](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#user-lacks-permissions)
- [USER\_NOT\_ACCOUNT\_ADMIN](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#user-not-account-admin)
- [USER\_NOT\_ENVELOPE\_SENDER\_OR\_RECIPIENT](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#user-not-envelope-sender-or-recipient)
- [USER\_NOT\_FOUND](https://developers.docusign.com/docs/esign-rest-api/esign101/error-codes/troubleshooting-common-errors/#user-not-found)

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
