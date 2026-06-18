---
title: Connection behaviors and best practices
source_url: https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Best Practices
- Best Practices
- Connection Behaviors And Best Practices
scraped_at: '2026-06-18T19:51:49Z'
---

# Connection behaviors and best practices

A [connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/) is required for an extension app to obtain [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) from an external service and to send requests to its endpoints. You must establish a connection to the external service after you install an extension app on the Developer Console [testing](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) page or in the [App Center](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=xyw1716318604389.html).

If an extension app’s connection is [deleted](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/#connection-deletion) or [invalidated](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/#connection-invalidation), any Docusign agreement process that calls the extension app will become inoperable. Agreement processes that can be affected include [eSignature envelopes](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=ghu1578456429097.html) and [workflows](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=dnx1696972415150.html).

This topic provides information about connection behaviors and guidance to help ensure that connections function correctly. Some sections in this topic apply to specific [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/), while others apply to all extensions. Applicability is noted at the beginning of each section.

## Connection behaviors

The sections below explain how connections behave when various extension app processes occur.

### Data model definition storage

**Applies to:** Connected fields and data IO extensions

For connected fields extensions and data IO extensions, Docusign executes **Get Type Names** and **Get Type Definitions** actions to obtain information about an external system of record’s [data model](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/). These actions are executed when a connection is established between Docusign and the external system. Docusign stores the data model definition with the connection and uses this information for:

- [Connected fields extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/)
  - Display the available connected fields in the [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html) so that template and envelope preparers can add them to documents
  - Return the available connected fields in response to a Connected Fields API [TabInfo:GetConnectedFieldsTabGroups](https://developers.docusign.com/docs/connected-fields-api/reference/connectedfields/tabinfo/getconnectedfieldstabgroups/) request
  - Process verification requests when users populate connected fields in envelopes
- [Data IO extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-io/)
  - Display the available objects and properties on the [Workflow Builder workflow](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uhm1697826856678.html) configuration screens for data read and data writeback steps
  - Process data search, create, and update requests when end users complete steps in workflow instances

For connected fields extensions, eSignature relies on the data model definition associated with the connection that a preparer selects during template or envelope creation. For data IO extensions, Workflow Builder relies on the data model associated with the connection that a process builder selects during workflow definition.

### Connection deletion

**Applies to:** All extensions

The connection for an extension app that's installed to your developer account will be deleted when you:

- [Uninstall and reinstall](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/) an extension app on the Developer Console Testing page
- [Update the extension app registration](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/) in the Developer Console, which causes an automatic uninstall and reinstall of the app
- [Uninstall and reinstall](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) the extension app in the App Center
- [Delete a connection or reconnect](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=xyw1716318604389.html) in the App Center

When you take an action listed above while logged into your developer account, it affects the extension app's functioning only in your own account. **Live** versions of your extension app that Docusign App Center users have installed in production will not be affected. See [Envelope, template, and workflow repair after connection issues](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/#envelope-template-and-workflow-repair-after-connection-issues) for steps to continue working with existing templates, envelopes, workflows, and workflow instances after a connection deletion in your account.

For an extension app in **Live** status, connection deletion will occur for any production account where the app is installed if the account administrator:

- [Uninstalls and reinstalls](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) the extension app in the App Center
- [Deletes a connection or reconnects](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=xyw1716318604389.html) in the App Center

App Center administrators see this warning when uninstalling an extension app:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='339' width='627' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![App Center uninstall warning](https://images.ctfassets.net/aj9z008chlq0/1nGtd5GiLr2R8ZPP5gapun/0343bc0998f7a393724d303b90b8411c/AppCenterUninstallWarning.png?w=627&h=339&q=50&fm=png)

### Connection invalidation

**Applies to:** All extensions

An extension app’s connection can become invalidated as a result of [authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) issues. Depending on the cause, connection invalidation can affect one, multiple, or all Docusign accounts that have an extension app installed.

Causes of connection invalidation can include:

- Changes to the authorized user's account, such as:
  - A password change
  - The account being deleted or disabled
  - The user revoking consent
  - An account administrator revoking the user’s access token
- Restrictions imposed by the external service, including:
  - Security policy updates
  - Changes to authorized scopes or access to resources
  - Concurrent sign-in limits
  - Login from a new device or location

See [Envelope, template, and workflow repair after connection issues](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/#envelope-template-and-workflow-repair-after-connection-issues) for steps to continue working with existing templates, envelopes, workflows, and workflow instances after a connection invalidation in your account.

## Connection best practices

Follow the guidance in the sections below to help ensure that connections function correctly.

### Connection refresh for minor data model changes

**Applies to:** Connected fields and data IO extensions

If minor data model changes are made in a system of record that’s being accessed by a connected fields or data IO extension in **Live** status, Docusign recommends [refreshing the connection](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=qkv1716320270335.html) for the extension app in the Docusign App Center. A connection refresh should be performed for any accounts that have the extension app installed. This keeps the connections intact and causes Docusign to execute **Get Type Names** and **Get Type Definitions** actions to retrieve the latest data model.

Minor data model changes include updates to property labels, which will not cause breaking changes for existing templates, envelopes, workflows, or workflow instances.

### Version upgrade for major data model updates

**Applies to:** Connected fields and data IO extensions

Major data model updates will cause breaking changes for existing templates, envelopes, workflows, and workflow instances. These include adding a required property to a type, removing a required property, or changing an optional property to be required.

For major data model updates where a connected fields or data IO extension app in **Live** status is accessing the data source, Docusign recommends creating a new [version](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) of the extension app in the Developer Console. You should then [test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/) the new version, [submit](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/#step-3-submit-your-extension-app-for-review-on-the-developer-console) it for Docusign review, and [publish](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/#step-4-publish-your-approved-extension-app) the new version. On publication, existing production accounts that have the previous version installed will be automatically upgraded to the new version with no disruption to the connection and no impact to existing templates, envelopes, workflows, or workflow instances.

### Envelope, template, and workflow repair after connection issues

**Applies to:** All extensions

If an extension app’s connection is deleted or invalidated, an account administrator must [re-establish](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=zsb1714159452358.html) it. Afterward, the administrator can complete the following to make sure existing envelopes, templates, workflows, and workflow instances that used the old connection continue to function:

- Connected fields and data verification extensions:
  - For envelopes that have been sent but not completed by the recipient, follow the procedure to [Correct an Envelope](https://support.docusign.com/s/document-item?bundleId=oeq1643226594604&topicId=ztq1578456332318.html). During the correction process, delete the connected fields from the document, and then add them back.
  - For templates, follow the procedure [To edit a template](https://support.docusign.com/s/document-item?bundleId=xry1643227563338&topicId=uvw1578456369720.html), delete any connected fields from the document, and then add them back.
- Data IO and file IO extensions
  - For workflow instances that are in progress, follow the procedure to [Cancel a Running Instance﻿](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=uqy1698181406489.html), and then [start new instances](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=glx1730400747416.html) if needed.
  - For workflow definitions, [edit them](https://support.docusign.com/s/document-item?bundleId=yff1696971835267&topicId=zlm1698880256815.html) and reconfigure any data read, data writeback, or file output steps.

## Next steps

- Get an overview of the [supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/).
- Review the properties in the [connection schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/).
- Learn how to [test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).

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
