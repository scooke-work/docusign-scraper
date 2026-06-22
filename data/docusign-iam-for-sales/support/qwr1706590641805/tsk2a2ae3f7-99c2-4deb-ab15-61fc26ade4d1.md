---
title: Prepare Your Salesforce Organization to Use a Start with Docusign Action
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=qwr1706590641805&topicId=tsk2a2ae3f7-99c2-4deb-ab15-61fc26ade4d1.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-22T19:18:55Z'
---

# Prepare Your Salesforce Organization to Use a Start with Docusign Action

Learn to prepare your Salesforce organization to start Docusign Workflow Builder workflows from Salesforce.

## Before you begin

[Purchase a Docusign Intelligent Agreement
Management (IAM) for Sales application](https://www.docusign.com/intelligent-agreement-management?utm_source=bing&utm_medium=cpc&utm_campaign=GBL_XX_PRF_UPS_2410_SEMIAM&utm_term=docusign%20iam&campaignid=569731866&adgroupid=1178678316174006&location=84406&device=c&matchtype=e&extensionid=&creative=73667602015411&keyword=docusign%20iam&placement=&network=o&msclkid=3287ee64f2c01f69bcd686665f40e7da)

Important:

- This feature is only available to IAM for Sales customers. Contact [Docusign support](https://support.docusign.com/s/?language=en_US&_gl=1*74elk4*_gcl_au*MTY5ODQyMjA2MC4xNzY5NjM1OTA1LjE5ODM3MTQzNjguMTc2OTYzNjIwNC4xNzY5NjM2MjA0) or [Docusign
  sales](https://www.docusign.com/contact-sales) for more information.
- Do not follow these steps if you already have Docusign
  Apps Launcher v8.4 or higher installed. Only follow these steps to add a
  Start with Docusign component or action in an
  organization with v8.3 or lower installed.

.

With [Docusign
Workflow Builder](https://support.docusign.com/s/document-item?bundleId=qwr1706590641805&topicId=bqi1705961132077.html&_LANG=enus), you can create workflows to
automate your agreement process. If you want to start workflows from Salesforce, you
can add a Start with Docusign action or component to your
layouts. Users can start a workflow by selecting Start next
to a workflow name. To start workflows from Salesforce, you must prepare your
organization.

Use this procedure to prepare your Salesforce organization to start workflows from
Salesforce:

1. As a Salesforce and Docusign administrator, [Install Docusign Apps
   Launcher version 8.4 or higher](https://support.docusign.com/s/document-item?bundleId=srl1586134368658&topicId=ogj1586134254571.html&_LANG=enus).
   - [Install for Salesforce production](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tKg000000D3Vk).
   - [Install for Salesforce sandbox](https://test.salesforce.com/packaging/installPackage.apexp?p0=04tKg000000D3Vk).
2. [Disconnect and reconnect Docusign and Salesforce](https://support.docusign.com/s/document-item?bundleId=srl1586134368658&topicId=ntr1586134210309.html&_LANG=enus).

   Important: Disconnecting removes Docusign access from all Salesforce users. Disconnecting does not remove users from your connected Docusign account.
3. [Open Docusign Apps Launcher](https://support.docusign.com/s/document-item?bundleId=srl1586134368658&topicId=etv1586134206174.html&_LANG=enus).
4. Go to Docusign Setup >  User Management.
5. [Re-add your Docusign users](https://support.docusign.com/s/document-item?bundleId=srl1586134368658&topicId=uwf1586134275195.html&_LANG=enus).

   Important: Users must [re-activate their Docusign access in Salesforce](https://support.docusign.com/s/document-item?bundleId=vbw1648698462634&topicId=ymi1586134213877.html&_LANG=enus). After re-activating,
   users can access Agreement Desk in the Docusign Agreement
   Requests component.

You have completed the task. You have prepared your Salesforce organization to start
workflows from Salesforce.

## Next steps

Complete the following tasks to finish your integration setup:

- [Build a workflow to be triggered by a
  Start with Docusign action](https://support.docusign.com/s/document-item?bundleId=qwr1706590641805&topicId=tskccafc250-9431-4f0c-9518-d4526d9128b1.html&_LANG=enus "Learn to build a workflow that can be triggered by a Start with Docusign action.").
- [Build a Start with Docusign action](https://support.docusign.com/s/document-item?bundleId=qwr1706590641805&topicId=tsk32e505bf-436a-47b1-b7f6-55e6ad614ec5.html&_LANG=enus "Learn to build a new Lightning web component action to start a Docusign workflow from a record.").
- [Add a Start with Docusign action to a layout](https://support.docusign.com/s/document-item?bundleId=qwr1706590641805&topicId=tskb637a1ca-b7ba-4604-97f7-f5f2d5f899f6.html&_LANG=enus "Learn to add a Start with Docusign action to a page layout to start workflows.") .
- [Grant user permissions to start
  workflows from Salesforce](https://support.docusign.com/s/document-item?bundleId=qwr1706590641805&topicId=tsk3640d081-197c-4f31-990a-0309487e92a8.html&_LANG=enus "Learn to assign a custom Docusign permission profile so that standard users can execute Workflow Builder workflows from Salesforce.").
