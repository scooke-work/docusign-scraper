---
title: Review extension app logs
source_url: https://developers.docusign.com/extension-apps/troubleshooting/review-logs/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Troubleshooting
- Troubleshooting
- Review Logs
scraped_at: '2026-06-18T19:51:49Z'
---

# Review extension app logs

The Developer Console All Logs feature enables you to review details about installs and uninstalls of an extension app. If you request assistance with an installation issue in the [Docusign Developer Community](https://community.docusign.com/developer-59), a Docusign support representative may ask you to provide details from the log.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='845' width='1738' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Developer Console logs page](https://images.ctfassets.net/aj9z008chlq0/6mwa5Obqx06VyzVU6DBpTN/2cf7c5d1aac6e9350f6ffe78ae2b1473/AllLogs.png?w=1738&h=845&q=50&fm=png)

## Access extension app logs

To access an extension app’s logs:

1. Log in to the [Developer Console](https://devconsole.docusign.com).
2. On the **My Extension Apps** page, locate the row for the extension app you want to update.
3. Select the app to open the **Overview** page.
4. In the left navigation, select **All Logs**.

## Apply log filters

You can filter the logs by date or environment. By default, logs are loaded for the last 30 days for the demo environment.

To change the date range:

1. Select the date filter.
2. Select one of these options and select **Apply**:
   - **Last 30 days**
   - **Last 6 month**
   - **Last year**
3. You can also select **Custom Date Range**, specify a range using one of these options, and select **Apply**:
   - **Between:** Define a start date and end date. Results include activity on the start and end dates, as well as between them.
   - **Before:** Select a date to return data from activity on and before that date.
   - **After:** Select a date to return data from activity on and after that date.

The page reloads and the content reflects the selected date range.

To change the environment:

1. Select the environment filter.
2. Select one of these options and then select **Apply**:
   - **Demo**
   - **Production**

The page reloads and the content reflects from the selected environment. See [Developer and production environments](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/#developer-and-production-environments) for details about the difference between these environments.

## Review log details

To review log details, select **View All** on the **Install and Uninstall Logs** tile. The list of logs loads. Each row in the list represents an installation or uninstallation of the extension app. You can [apply filters](https://developers.docusign.com/extension-apps/troubleshooting/review-logs/#apply-log-filters) to limit the number of results.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='797' width='1825' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Log detail page](https://images.ctfassets.net/aj9z008chlq0/4pkkE05NcuDKeSuiCc1UDL/4054f432927aa292971fdbd99d0a3ded/LogsPage.png?w=1825&h=797&q=50&fm=png)

To view details about an installation or uninstallation, select **View Details**. The following information is displayed:

![](data:image/svg+xml;charset=utf-8,%3Csvg height='619' width='800' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Log details](https://images.ctfassets.net/aj9z008chlq0/3K3Z39kTkV4eyXIRcrFhoE/c51344929e9c5d6c78138f646cad9980/LogDetails.png?w=800&h=619&q=50&fm=png)

| Field | Description |
| --- | --- |
| Timestamp (UTC) | The date and time at which the install or uninstall process finished. |
| App Instance ID | A unique ID representing the instance of your extension app that was installed or uninstalled. |
| App ID | A unique system-generated identifier for the extension app. |
| App Name | The unique name defined in the extension app’s [Basic information](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/#update-basic-information) and in the extension app manifest [name](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) property. |
| App Version | A unique ID representing the [version](https://developers.docusign.com/extension-apps/build-an-extension-app/versioning/) of the extension app. |
| Account ID | The Docusign account to or from which the extension app was installed or uninstalled. |
| Extension Type | A list of [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/) that the extension app implements. |
| Status | `success` if the install or uninstall succeeded, or `failed` if it did not succeed. |
| Duration (MS) | The length of time in milliseconds for the install or uninstall process. |
| Debug ID (Trace Token) | A unique ID that Docusign can use to troubleshoot the cause of a failure. |
| Status Message | One of the following:  - `Created app instance: [app instance ID]` if an installation succeeded - `Delete app instance [app instance ID]` if an uninstall succeeded |

Select the **Download CSV** button to download a CSV file that contains the following information for each log file listed:

- Timestamp
- Status (`success` or `failed`)
- Duration in milliseconds of the installation or uninstallation process
- Debug ID
- Status message

## Next steps

- Review the options to [test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).
- Learn more about the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/).

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
