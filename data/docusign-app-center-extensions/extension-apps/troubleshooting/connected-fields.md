---
title: Troubleshooting for connected fields extensions
source_url: https://developers.docusign.com/extension-apps/troubleshooting/connected-fields/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Troubleshooting
- Troubleshooting
- Connected Fields
scraped_at: '2026-06-18T19:51:49Z'
---

# Troubleshooting for connected fields extensions

This topic provides troubleshooting guidance for issues that may arise when working with [connected fields extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/connected-fields/) in eSignature or in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

## eSignature envelope or template preparation issues

### Issue

In the eSignature [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html), **App Fields** does not appear after you select **Custom Fields**, or you do not see your extension app name under **App Fields**. Connected fields extension apps should appear under **App Fields**.

### Possible causes and recommendations

- The extension app may not be installed or connected to your account. See [Run a connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) for instructions to install and connect it in the Developer Console, or [install and connect](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) it to your account in the App Center.
- When the extension app was connected to your account, Docusign was unable to process the [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names) or [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) response, possibly due to an error in the data model. To check this, run the [extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) for these two actions. You can use the [Concerto VSCode extension](https://concerto.accordproject.org/docs/tools/vscode/) to validate your data model and check for errors.
- The connection to the external service was invalidated due to authorization issues or deleted. [Re-establish](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=zsb1714159452358.html) the connection for the extension app in the Docusign App Center. See [Connection behaviors and best practices](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/) for more information.
- You are working with an eSignature template that you added to your account by uploading a template that was downloaded from another account. However, the account to which you uploaded the template does not have the connected fields extension app installed or connected. See [Run a connection test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) for instructions to install and connect it in the Developer Console, or [install and connect](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=ctg1698170340729.html) it to your account in the App Center.

### Issue

In the eSignature [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html), the list of available connected fields for your extension app is out of date.

### Possible causes and recommendations

- The data model changed after the extension app was connected to your account. [Refresh the connection](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=qkv1716320270335.html) for the extension app in the Docusign App Center. This keeps the connection intact and causes Docusign to execute [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names) and [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) actions to retrieve the latest data model.
- When the extension app was connected to your account, Docusign was unable to process the **Get Type Names** or **Get Type Definitions** response, possibly due to an error in the data model. To check this, run the [extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) for these two actions. You can use the [Concerto VSCode extension](https://concerto.accordproject.org/docs/tools/vscode/) to validate your data model and check for errors.

### Issue

In the eSignature [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html), multiple copies of the extension app are listed with different connection names, but you only expect to see one listing.

### Possible cause and recommendation

Repeatedly running [connection tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) on the Developer Console Testing page causes multiple connections to be created. You can [delete connections](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=pnb1716320193292.html) in the App Center. For an extension app in **Draft** status, you can [uninstall and reinstall](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-a-connection-test) it on the Developer Console Testing page, and then run a new connection test to create a single connection. Because uninstalling and reinstalling in the Developer Console deletes all existing connections, this option is not recommended for extension apps that are being used in production. See [Connection behaviors and best practices](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/) for more information.

### Issue

In the eSignature [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html), a connected field is displayed as required (indicated by an asterisk), but it should be optional.

### Possible causes and recommendations

- The property is marked with the [IsRequiredForVerifyingType decorator](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) in your data model. To check this, run the [extension test](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) for the [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) action and review the response. If the decorator is present for a property that should be optional, remove it from the data model.
- The property is not defined as optional in the data model. By default, Docusign treats properties as required if they are not explicitly defined as optional. Add an `isOptional` property set to `true` in the Concerto definition.

## eSignature envelope signing view issues

### Issue

After populating a value in one or more connected fields, a **Verification failed** error is displayed instead of the expected verification result and message from the external system.

### Possible causes and recommendations

- Your extension app registration is not configured with the correct parameters to connect to the external service. Run the Developer Console [extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) for the [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names), [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions), and [Verify](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#verify) actions, and then check for any errors accessing the external service.
- Docusign does not have an up-to-date data model for your system of record. [Refresh the connection](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=qkv1716320270335.html) for the extension app in the Docusign App Center to update the data model information that Docusign stores. See [Connection behaviors and best practices](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/) for more information.
- The connection to the external service was invalidated due to authorization issues or deleted. [Re-establish](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=zsb1714159452358.html) the connection for the extension app in the Docusign App Center. See [Connection behaviors and best practices](https://developers.docusign.com/extension-apps/best-practices/connection-behaviors-and-best-practices/) for more information.
- If envelopes are being created programmatically via API requests, the connected field values in the [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) request’s `extensionData` objects may be outdated or incorrect. Send a [TabInfo:GetConnectedFieldsTabGroups](https://developers.docusign.com/docs/connected-fields-api/reference/connectedfields/tabinfo/getconnectedfieldstabgroups/) request, and make sure the required values from the response are included in the `Envelopes:create` request. See [Connected fields concepts](https://developers.docusign.com/docs/connected-fields-api/concepts/) for more information.
- During template or envelope preparation, only optional connected fields were added to the document. Verification fails if a document does not contain any required connected fields. In the eSignature [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html), be sure to add required connected fields (marked with an asterisk) to the document, and then send a new envelope.

### Issue

The signing view allows users to enter non-permitted values in a connected field, such as letters in a field that’s intended for numeric values.

### Possible cause and recommendation

The connected field did not have any data validation applied after it was added to the template or envelope in the eSignature [Add Fields view](https://support.docusign.com/s/document-item?bundleId=ulp1643236876813&topicId=odn1578456409392.html). Most Concerto properties appear as text fields in the Add Fields view. See [Transform logic](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/data-model/#transform-logic) for details. To require signers to enter specific types of values, such as numeric values, use the [data validation](https://support.docusign.com/s/document-item?bundleId=gbo1643332197980&topicId=jgd1578456357365.html) feature after adding connected fields to a template or envelope.

## App Center issues

### Issue

When trying to add or refresh a connection, the [connection management](https://support.docusign.com/s/document-item?bundleId=ous1698169987748&topicId=xyw1716318604389.html) page displays a **Data Error** banner.

### Possible cause and recommendation

Adding or refreshing a connection causes Docusign to execute [Get Type Names](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-names) and [Get Type Definitions](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/#get-type-definitions) requests, but Docusign was unable to process both responses, possibly due to an error in the data model. To check this, run the [extension tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/#run-an-extension-test) for these two actions. You can use the [Concerto VSCode extension](https://concerto.accordproject.org/docs/tools/vscode/) to validate your data model and check for errors.

## Next steps

- Get details about [connected fields requests and responses](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/connected-fields/).
- Find out more about [functional tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/functional-tests/).
- Learn how to run [integration tests](https://developers.docusign.com/extension-apps/build-an-extension-app/test/integration-tests/).

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
