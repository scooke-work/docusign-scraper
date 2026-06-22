---
title: 'Docusign Intelligent Agreement Management (IAM) for Sales: Salesforce'
source_url: https://support.docusign.com/s/document-item?language=en_US&bundleId=map8c30aa94-7e9f-4950-92fc-dd22c6d9f835&topicId=con650f4cbe-fdc5-4dbb-8d98-9ef991726ed9.html&_LANG=enus
site: support.docusign.com
breadcrumb: []
scraped_at: '2026-06-22T19:15:46Z'
---

# Docusign Intelligent Agreement Management (IAM) for Sales: Salesforce

Learn about how to integrate Docusign products to create, send, manage,
and track agreements in Salesforce.

Important: This feature is only available to IAM for Sales
customers. Contact [Docusign support](https://support.docusign.com/s/?language=en_US&_gl=1*74elk4*_gcl_au*MTY5ODQyMjA2MC4xNzY5NjM1OTA1LjE5ODM3MTQzNjguMTc2OTYzNjIwNC4xNzY5NjM2MjA0) or [Docusign sales](https://www.docusign.com/contact-sales)
for more information.

## What is Intelligent Agreement Management (IAM) for Sales?

You can use Docusign IAM for Sales to run the entire contract process for your sales and legal teams. With Docusign IAM
for Sales, you can generate, send, manage, track, and store agreements, all without
leaving Salesforce.

IAM for Sales can manage everything from simple
template-based NDA generation to complex negotiated contract workflows.

## IAM for Sales prerequisites

To create IAM solutions for Salesforce, complete the following tasks:

- Purchase a [Docusign Intelligent Agreement
  Management (IAM) for Sales](https://www.docusign.com/intelligent-agreement-management?utm_source=bing&utm_medium=cpc&utm_campaign=GBL_XX_PRF_UPS_2410_SEMIAM&utm_term=docusign%20iam&campaignid=569731866&adgroupid=1178678316174006&location=84406&device=c&matchtype=e&extensionid=&creative=73667602015411&keyword=docusign%20iam&placement=&network=o&msclkid=3287ee64f2c01f69bcd686665f40e7da) license. This license includes Docusign eSignature, Workflow Builder, Agreement Prep,
  Agreement Desk, Agreement Manager, and the Docusign for
  Salesforce connector.
- [Install the Salesforce app from the Docusign App
  Center](https://support.docusign.com/s/document-item?bundleId=map8c30aa94-7e9f-4950-92fc-dd22c6d9f835&topicId=jxo1706295810553.html&_LANG=enus "Learn to install the Salesforce app in your Docusign account and connect it to your Salesforce organization.").
- Create a workflow containing Salesforce steps.
- Install Docusign Apps Launcher for Salesforce v8.4
  or higher in your [Salesforce production organization](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tKg000000D3Vk) or [Salesforce sandbox organization](https://test.salesforce.com/packaging/installPackage.apexp?p0=04tKg000000D3Vk).
- [Add a Start with Docusign action to a
  layout](https://support.docusign.com/s/document-item?bundleId=map8c30aa94-7e9f-4950-92fc-dd22c6d9f835&topicId=tsk32e505bf-436a-47b1-b7f6-55e6ad614ec5.html&_LANG=enus "Learn to build a new Lightning web component action to start a Docusign workflow from a record.").

## How do I use IAM in Salesforce?

Docusign has a number of products that you can use to create an IAM
for Sales experience in Salesforce:

- [Apps Launcher for Salesforce](https://support.docusign.com/s/document-item?bundleId=gab1637077302276&topicId=jgh1637077647417.html&_LANG=enus)
- [Workflow Builder for Salesforce](https://support.docusign.com/s/document-item?bundleId=qwr1706590641805&topicId=bqi1705961132077.html&_LANG=enus)
- [Agreement Manager for Salesforce](https://support.docusign.com/s/document-item?bundleId=pwq1747797355782&topicId=bky1747764447701.html&_LANG=enus)
- [Agreement Desk for Salesforce](https://support.docusign.com/s/document-item?bundleId=map8c30aa94-7e9f-4950-92fc-dd22c6d9f835&topicId=con007504df-80b7-41f7-aa5f-1daa72bcc257.html&_LANG=enus "Learn about using Docusign Agreement Desk in Salesforce to streamline your agreement process.")

You can use these products separately, or you can use them together to provide an
integrated system that manages agreements from creation to completion.

Table 1. IAM for Sales Features and Benefits

| Feature | Benefit | IAM for Sales Exclusive? |
| --- | --- | --- |
| CRM-Embedded User Experience | Agreement tools for all phases of the agreement process. Embedded or accessible in CRM (Generation, Agreement Desk, eSignature, Agreement Manager.) | YES |
| CRM AI Agent Integration | Interactive Agreement status, search, and Q&A from Salesforce, Agentforce, or Microsoft 365 Copilot. | YES |
| Agreement Desk | Communication, context, transparency, and status for sales, legal, and other teams negotiating and approving B2B Sales Agreement. | NO |
| Document Generation & Agreement Template Builder | Customized contract generation using CRM data for sales agreements, made accessible through an intuitive, drag-and-drop template setup. | NO |
| eSignature | Legally binding agreements that are automated using CRM user, and customer data. | NO |
| Workflow Builder | Automation and acceleration of otherwise manual agreement processes. | NO |
| Agreement Manager | When embedded in CRM pages, contextually accurate access to all agreements relevant to an account, opportunity, quote, or contact. | Partial (Not available in CX) |
| CRM Data Connector (App Center Extension App) | Data and file read and write supporting all IAM products and services. | Partial (Also available in CX) |

## IAM for Sales key use cases

General Legal Request
:   Create requests that require legal team action. These are often procurement contracts sent from the buyer, contracting
    requests, or questions that require legal work.

Negotiated Interactive Sales Order
:   Create sales contract templates that include an MSA or terms and conditions, along with a price quote. This scenario uses pre-built contract templates, combined with stakeholder approvals and buyer negotiation. It can all be started by a sales request from a CRM system.

Interactive Onboarding/Consent form
:   Create onboarding and consent forms containing standardized contract language. These are often used in both B2B and B2C sales scenarios. These forms are not negotiated, and are often PDFs pre-filled with customer data.

One-Click NDA
:   Create simple, standard contracts that only require legal approval if a buyer
    decides to negotiate terms. This is often the first
    agreement that is sent to a customer.

## Sample setup

You install Docusign Apps Launcher 8.4 in your Salesforce
organization.

You add a Start with Docusign action to your layouts. Users can select the action to start workflows from records.

You add the Docusign Agreement Desk component your layouts.
Users can view and act on workflow requests from the component.

You add the Docusign Agreements component to view Docusign Agreement Manager on your layouts. Users can view and act on
completed Docusign agreements from the component.

## Sample IAM for Sales flow

Sam Sales selects the Start with Docusign button on the Acme,
Inc. opportunity. The list of available Docusign workflows
displays. Sam selects the Start button for the
MSA workflow. The MSA web form opens, containing pre-filled
data imported from the Acme record. The pre-filled data saves Sam time and the risk
of error. Sam adds a supplemental document to the form and selects
Submit. The MSA workflow starts, sending tasks to all
workflow participants.

Sam sees the MSA request displayed in the Acme record's Agreement Desk component, with a status of Ready for Review/Signature. Sam selects the request to open it. Sam selects the Documents tab and chooses the Send via Email option. Sam enters recipient email addresses, adds a quick message, and selects Send.

Recipients complete their workflow tasks, and the next day, Sam receives a
notification that the Acme MSA is ready for review. He selects the Acme MSA request
in the Agreement Requests component and selects the Send for
signature button. The agreement opens, displaying all changes that
the recipients made. After a quick review, Sam selects the
Send button.

A representative at Acme completes the request by reviewing and signing the MSA. Docusign Agreement Manager's AI feature extracts terms from the agreement
and writes the data back to Acme's Salesforce record. The completed agreement
displays in the Acme record's Agreement Manager component. Sam can see details like the
agreement name, party, effective date, and expiration date.
