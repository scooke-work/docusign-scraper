---
title: Best practices for handling alerts
source_url: https://developers.docusign.com/docs/monitor-api/monitor101/best-practices-handling-alerts/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Monitor API
- Monitor API
- API 101
- API 101
- Best practices for handling Alerts
scraped_at: '2026-06-18T21:15:04Z'
---

# Best practices for handling alerts

Docusign Monitor includes pre-built alerts for common types of suspicious activity, and enables you to create custom alerts using the Monitor API. Because alerts can be triggered by malicious or authorized activity, we provide several options so you can appropriately respond to potential threats as they are investigated and resolved.

Sample alert types:

- User fails six or more login attempts in an hour
- Admin disables a user-authentication requirement
- Admin initiates a bulk user export
- User downloads 20 or more envelopes in an hour
- User logs in from a location more than 100 km from any previous location

## Corrective actions

When an administrator or security operations team receives an alert from Monitor, they should act quickly to investigate the alert and respond appropriately. For example, if a user fails too many consecutive login attempts, an administrator could reset that user’s password—or take one of the following actions:

### Close a user's membership

If an account has been flagged as compromised, you can close that account to prevent additional activity while you investigate.

**Required privileges:** Docusign Administrator, or eSignature Administrator on the same organization account as the user.

To close the account:

1. Select **Users** in the main menu.
2. Select the user from the display.
3. From the **Actions** menu, select **Close**.

For more information, see [Manage eSignature users](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=pik1583277475390&topicId=ixb1583277365937.html&_LANG=enus).

### Revoke the user's administrator privileges

If a delegated admin account is flagged as compromised because of suspicious activity, you can revoke admin privileges while you investigate.

**Required privileges:** Docusign Administrator

To revoke the user's admin privileges:

1. From the **Docusign Admin** dashboard, click **Administrators**.
2. Locate the administrator you want to remove.
3. From the **Actions** menu, select **Remove**.
4. Choose **Confirm**.

Alternatively, you can change the user profile as described in the User Details section in [User Management](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=rrf1583359212854&topicId=jni1583359185567.html&_LANG=enus).

### Force a password reset

If an account shows signs of suspicious activity, you can notify the account owner and force a password reset to help prevent unauthorized access.

**Required privileges:** eSignature Administrator on the user's account

To force a password reset:

1. Select **Users** in the main menu.
2. Select the user from the display.
3. From the **Actions** menu, select **Reset Password**.

For more information, see the Reset User Password section in [Manage Users](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=rrf1583359212854&topicId=jni1583359185567.html&_LANG=enus).

### Transfer a user's envelopes and templates

If a user account has been compromised, you can transfer their envelopes and templates to a secure user account.

**Required privileges:** eSignature Administrator on the user's account

To transfer a user's envelopes and templates:

1. Select **Users** in the main menu.
2. Select the user from the display.
3. From the **Actions** menu, select **Transfer Envelopes** or **Transfer Templates**.

For more information, see the Transfer envelopes or templates between users section in [Transfer Envelopes or Templates](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=pik1583277475390&topicId=vyz1583277376194.html&_LANG=enus).

### Revoke the user's eSignature administrator privileges

If an eSignature admin account is flagged as compromised because of suspicious activity, you can revoke eSignature admin privileges while you investigate.

**Required privileges:** Docusign Administrator

To revoke a user's eSignature administrator privileges:

- From the **Docusign Admin dashboard**:
  1. Select **Users** and search for the user by email address. The user’s profile appears.
  2. In the **Actions** tab, select **Edit**.
  3. In the **Enable Applications** section, in eSignature select a new permission profile for the user.
- From the **Monitor Alert History** page:
  1. When the **Alert History** panel is opened for a particular alert, choose **Manage User**. The user’s profile appears.
  2. In the **Actions** tab, select **Edit**.
  3. In the **Enable Applications** section, in eSignature select a new permission profile for the user.

For more information see the View and manage details for a user section in [User Management](https://support.docusign.com/s/document-item?language=en_US&rsc_301&bundleId=rrf1583359212854&topicId=jni1583359185567.html&_LANG=enus).

### Restore the user's envelopes

If envelopes were transferred from a potentially compromised account, and that account has been cleared after an investigation, those envelopes can be restored to the original user.

**Required privileges:** eSignature account administrator

To restore a user's envelopes:

1. Select **Docusign eSignature Agreements** tab in the main menu.
2. In the **Envelopes** section, select **Deleted**.
3. Select the deleted envelopes and then move them to the desired folder.

## Next steps

- Review the Event and Alert objects in the [API reference](https://developers.docusign.com/docs/monitor-api/reference/)
- See the [list of tracked alerts](https://developers.docusign.com/docs/monitor-api/monitor101/events-alerts/#list-of-tracked-events)

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
