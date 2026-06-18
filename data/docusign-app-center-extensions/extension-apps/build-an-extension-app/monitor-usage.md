---
title: Monitor extension app usage
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/monitor-usage/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Monitor Usage
scraped_at: '2026-06-18T19:51:48Z'
---

# Monitor extension app usage

The Developer Console Dashboard enables you to monitor usage of your extension app. You can track the number of accounts to which the extension app has been installed and uninstalled over time.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1503' width='1987' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Extension app dashboard](https://images.ctfassets.net/aj9z008chlq0/71cszliKMlNIMAMNxSEVR8/42232c86c2f3498a2d52183c2aa3cf0b/Dashboard.png?w=1987&h=1503&q=50&fm=png)

## Access the extension app dashboard

To access an extension app’s dashboard:

1. Log in to the [Developer Console](https://devconsole.docusign.com).
2. On the **My Extension Apps** page, locate the row for the extension app you want to update.
3. Select the app to open the **Overview** page.
4. In the left navigation, select **Dashboard**.

## Apply dashboard filters

The dashboard enables you to filter the data by date or environment. By default, the dashboard loads with data from the last 30 days for the demo environment.

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

## Review dashboard data

The dashboard displays data in three sections.

The **Installs** tile displays the total number of unique accounts that installed your app during the selected date range on the selected environment. Multiple installs to the same account are not counted separately.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='235' width='458' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Installs tile](https://images.ctfassets.net/aj9z008chlq0/11XlZ26hJxqEQ1sH41FTyL/e84bd61a2d9cabad301422765f85ade9/InstallsTile.png?w=458&h=235&q=50&fm=png)

The **Install Trends** chart shows the number of unique accounts that installed your app by date.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='595' width='1577' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Install trends](https://images.ctfassets.net/aj9z008chlq0/6ySKVwWPg0brmlmZV8bToR/5022c05237bffc056c6748d5b6599eb6/InstallTrends.png?w=1577&h=595&q=50&fm=png)

The **Uninstall Trends** chart shows the number of unique accounts that uninstalled your app by date.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='594' width='1575' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Uninstall trends](https://images.ctfassets.net/aj9z008chlq0/4ezPmh4SeymhLGgVOfFaoI/660e1cd78f653f4182731bbb30de697d/UninstallTrends.png?w=1575&h=594&q=50&fm=png)

The install and uninstall numbers reflect the following:

- Installs and uninstalls are counted regardless of whether they are initiated from the Developer Console or the App Center.
- If the extension app was installed but not connected, it is still counted in the totals.

## Next steps

- Learn about [supported extensions](https://developers.docusign.com/extension-apps/extension-apps-101/supported-extensions/).
- Review [example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/).

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
