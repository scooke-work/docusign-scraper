---
title: Shared access
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/shared-access/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Envelopes
- Envelopes
- Shared Access
scraped_at: '2026-06-18T21:09:57Z'
---

# Shared access

The shared access feature enables you to send and manage envelopes on behalf of other users in your account. Using shared access, you can manage an account user’s envelope inbox, send, and even [set up a delegate to sign envelopes on their behalf](https://support.docusign.com/s/document-item?rsc_301=&bundleId=jux1643235969954&topicId=bbk1637048103951.html). Shared access is often used for delegating work when a colleague is unavailable or for teams who use a shared account for sending and managing envelopes.

You can use shared access through the [Docusign eSignature UI](https://app.docusign.com/) or the [Authorizations resource](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/authorizations/).

- The UI enables you to use the full range of shared access functionality, including sharing access from one user to another, sending an envelope on behalf of another user, or managing envelopes on behalf of another user. See [Shared access to envelopes](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=rdu1656546423934.html) for details on using this feature through the UI.
- The API enables you to manage shared access permissions between your account users. Future releases may expand upon this functionality to call API endpoints that enable you to match all shared access UI functionality using the API.

## Managing authorizations

You can use the Authorization REST API to create, update, and delete authorizations for your account’s users. An *authorization* is the set of permissions granted to one user (an *agent*) within your account to act on behalf of another (a *principal*). Once an authorization is created, the agent user may then use shared access to send, manage, or sign envelopes on behalf of the principal user, depending on the type of authorization that was granted. All API calls an agent makes must include the header `X-Specific-Header: {AGENT_ACCOUNT_ID}` to authenticate and identify the agent making the request.

**Note**: To create an authorization for a user in your account, you must create the authorization as the principal or be an admin for your account.

There are four types of authorization that a principal user can grant to an agent to act on their behalf:

- **Manage:** Enables the agent to manage envelopes on behalf of the principal user as though they were the principal. Agents with the manage permission cannot send envelopes on behalf of the principal.
- **Send:** Enables the agent to send and manage envelopes on behalf of the principal user.
- **Sign:** Enables the agent to sign envelopes on behalf of the principal user. This is used for the [Delegated signing](https://support.docusign.com/s/document-item?rsc_301=&bundleId=jux1643235969954&topicId=bbk1637048103951.html) feature.
- **Edit**: Enables the agent to manage envelopes on behalf of the principal user, just like the manage permission, but also enables the agent to correct, void, and resend envelopes.

When you create or update an authorization in the API, you choose the type of authorization by setting the permission field in the request body to send, manage, edit, or sign.

See [How to share access to an envelope inbox](https://developers.docusign.com/docs/esign-rest-api/how-to/shared-access/) for a code example demonstrating how to create and manage authorizations.

**Note**: Sending and managing envelopes on behalf of other users has specific Docusign eSignature plan requirements. Contact your account representative for more information.

The following table shows which envelope actions are supported by each permission:

| **Envelope Action** | **Send** | **Edit** | **Manage** | **Sign** |
| --- | --- | --- | --- | --- |
| Sign as a delegate |  |  |  | X |
| Send envelope | X |  |  |  |
| Edit draft or save as draft | X |  |  |  |
| Correct | X | X |  |  |
| Void | X | X |  |  |
| Resend | X | X |  |  |
| Copy (with field data) | X |  |  |  |
| Forward | X |  |  |  |
| Download | X | X | X |  |
| View history | X | X | X |  |
| Move | X | X | X |  |
| Delete | X |  |  |  |
| View form data | X | X | X |  |
| Export CSVs | X | X | X |  |
| Create custom folders | X | X | X |  |
| Rename, move, delete custom folders | X | X | X |  |

## Next steps

- See how to [How to share access to an envelope inbox](https://developers.docusign.com/docs/esign-rest-api/how-to/shared-access/).
- Read the [Authorizations resource](https://developers.docusign.com/docs/esign-rest-api/reference/accounts/authorizations/) for full details of the API.
- See [Shared access to envelopes](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=rdu1656546423934.html) for details on using this feature through the UI.

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
