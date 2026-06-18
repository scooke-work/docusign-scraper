---
title: 'Docusign Maestro: Tips for a Streamlined Setup and Workflow'
source_url: https://www.docusign.com/blog/maestro-tips-streamlined-setup-workflow
site: www.docusign.com
breadcrumb:
- Home
- Home
- Blog
- Blog
- Intelligent Agreement Management
- Intelligent Agreement Management
scraped_at: '2026-06-18T18:04:50Z'
---

[Blog](https://www.docusign.com/blog)

# Docusign Maestro: Tips for a Streamlined Setup and Workflow

Published Jun 10, 2024

---

Summary•8 min read

Here is everything you need to know before starting to build your first Docusign Maestro workflow for intelligent agreement management.

![en-US](https://images.ctfassets.net/9pvazpst9iwl/7BjnYjaK8ece552wLbtbNh/170606909955b8d33da39480562900c6/Maestro.png?fm=avif&q=90&w=500)

- - [Common use cases](https://www.docusign.com/blog/maestro-tips-streamlined-setup-workflow#common-use-cases)
  - [Things to know before getting started](https://www.docusign.com/blog/maestro-tips-streamlined-setup-workflow#things-to-know-before-getting-started)

  - [Tips & tricks for building a Maestro workflow](https://www.docusign.com/blog/maestro-tips-streamlined-setup-workflow#tips-tricks-for-building-a-maestro-workflow)

Here is what you need to know before starting to build your first Docusign Maestro workflow. Maestro is a core platform service that’s part of [Docusign IAM](https://www.docusign.com/intelligent-agreement-management) and helps your team create custom workflows by connecting all of the seemingly separate pieces of their agreement process into one cohesive workflow — all without writing a single line of code.

## Common use cases

Here are a few popular use cases organizations can deploy:

- **Automate customer payment collection.** Automate customer payments using [Web Forms](https://www.docusign.com/blog/create-web-forms) and eSignature to collect payment information, and then connect to third-party apps like Salesforce to update CRM records.
- **Simplify account maintenance.** Use a Web Form to capture customer information (e.g. address, billing info, etc.). Use those details to populate the [Identity Verification (IDV)](https://www.docusign.com/products/identify) step so the customer has less information to enter.
- **Onboard new rental properties.** Accept new property rental applications via a Docusign Web Form. Completed applications can be routed to Google Drive for the rental management team to review and contact applicants.
- **Streamline NDA processes**. Use Identity Verification (IDV) to authenticate the client before they review and securely sign with eSignature.
- **Automate buyer transactions**. Automate real estate purchase workflows using Docusign IDV and Web Forms so agents can save time, reduce errors, and provide buyers with a hassle-free experience.
- **Accelerate contract renewals.** Improve contract renewals and delight customers with a convenient contract renewal experience. Your sales teams can generate prefilled contracts from Salesforce then use a simple Web Form to collect missing contract details. After eSignature, updated contract data is written back to Salesforce, and a copy of the contract can be automatically saved in Google Drive.

## Things to know before getting started

### Familiarize yourself with Templates and Web Forms

Two vital components of Maestro are Docusign Templates and [Web Forms](https://www.docusign.com/products/web-forms), both essential to the agreement process by helping you streamline data collection, eliminate redundancies for your signers, and collect signatures faster.

Templates are blueprints for repeatable envelopes — streamlining the sending process so you can collect signatures faster. To learn how to use Docusign Templates, we have a variety of instructional materials, how-to videos, and informative support guides:

- [Template Library](https://dsucustomers.docusign.com/page/km-template-library): Download free templates for your industry and specific use cases, then upload them to your account to start using them.
- [Contract and Form Templates Guide](https://www.docusign.com/blog/templates-contracts-forms-docusign) blog goes over how to save and reuse templates, which frees up valuable time and energy for your organization.
- [Working with Templates](https://support.docusign.com/s/document-item?language=en_US&rsc_301=&bundleId=xry1643227563338&topicId=dqj1578456412286.html) is a comprehensive guide that goes over every facet of creating, editing, and deleting templates from your Docusign account.

Web Forms allow you to capture data and dynamically populate content into agreements for signature — all from a URL that you can share with customers via email, website, or SMS.

Check out the [Web Forms Get Started page](https://www.docusign.com/products/web-forms/getting-started?_gl=1*1lxryb6*_up*MQ..&gclid=CjwKCAjwl4yyBhAgEiwADSEjeJUVLYRpS-XihVZ0SMF7AODvendKH04qFcVFDk50sukjqKm04Rq6ORoCnnUQAvD_BwE) to get up and running quickly and easily.

### Leverage Docusign App Center

Maestro integrates with popular applications you may already use that can be found in the new [Docusign App Center](https://apps.docusign.com/app-center) — like Salesforce, Google Drive, Dropbox, Stripe, ServiceNow and HubSpot.

Seamlessly add these applications into your agreement workflow with Maestro and in doing so, remove the complexities and bottlenecks of patching separate systems together in the agreement process.

Learn how to use the App Center, including how to install and manage your apps, all in this [helpful guide](https://support.docusign.com/s/document-item?language=en_US&bundleId=ous1698169987748&topicId=ijy1698170251179.html).

### Maestro user permissions

Creating agreement workflows using Maestro requires specific user permissions. By default, all account administrators have the required permissions. However, note that individual account users must check with their account administrator to ensure they’re enabled to use Maestro.

Check out this [Support guide](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=gbb1696973048215.html) to learn how to set user permissions for Maestro.

### Workflow participants and starting variables

When you create a Maestro workflow, you must consider the different roles of participants and any data that must be provided to them at the beginning of the agreement process. Starting variables are these pieces of vital information passed along from one step to the next in your Maestro workflow.

Consider the following questions, to help you create starting variables:

- Who from your organization needs information in an agreement?
- What vital information, like name an email, should be pre-populated into each step of the agreement process?

Learn more about workflow participants and starting variables in this guide:

- [Workflow Setup: Participants and Starting Variables FAQ](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=ypt1698264964168.html)

## Tips & tricks for building a Maestro workflow

We’ll walk you through some best practices for building a Maestro workflow in step-by-step fashion. Dive into the section that best suits what you’re interested in, depending on the workflow steps you plan to use.

### Create workflow-specific Web Forms

In order to deploy Web Forms within your Maestro workflow, you’ll first need to make a workflow-specific copy of an existing Web Form.

- Navigate to Templates on the top navigation, then find My Web Forms under the Web Forms section of the lower-left hand Templates navigation.
- Select the Web Form to duplicate for your Maestro workflow by clicking the three dots on the right, then click on Create Workflow Version.

- Notice your Workflow Copy Web Form as “Inactive” in Status. You’ll need to open it up to activate it by selecting Open.
- Now, you’ll see your workflow-specific Web Form. Here you can edit it as you’d like by selecting each Outline piece on the left hand side of the menu. Once it’s in a good place to use in your Maestro workflow, hit the Activate button. Now, it’s ready to deploy in your Maestro workflow.

### Define starting variables

[Starting variables](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=ypt1698264964168.html&_LANG=enus) represent dynamic inputs in your Maestro workflow, which can exchange vital information from one step of your workflow to the next. Additionally, you can create a new starting variable as you begin your workflow, especially if it’s the first step — as you won’t have any previously created variables to choose from.

Note, you don’t have to necessarily use Identity Verification (IDV) as a Maestro workflow step when defining a starting variable; you can define a starting variable with other workflow steps.

The following steps use IDV and an example to showcase how to define a starting variable:

- After configuring IDV in your workflow, you’ll find a yellow window (in step 3) telling you to add a variable while setting up IDV. Note, you don’t necessarily need to add a starting variable here, but it is very helpful in mapping that to your participant’s identity.
- Click Add Starting Variable to move on:

- Scroll down on the following Workflow Setup screen, all the way to the bottom, then select Add Variable, then Text (most common).
- Next, you can type in a starting variable of your choice. Additionally, there are Numbers and two advanced options to choose from.

- For this example, add Name as your starting variable, then hit Save.
- From here, you can choose the variable you just created from the following dropdown menu, before hitting Apply.

When you link this up to the next step of the workflow, this starting variable should be visible to hand off this vital information collected in the first IDV step. This way, your recipients won’t have to re-enter all of their information in the next step saving time and increasing accuracy in data collection.

### Branching Logic Options and Configuration

Branching Logic is a great way to appropriately funnel your workflow participants through by applying required logic before they can make it to the next step in the agreement process.

- It’s simple to deploy into your workflow. Simply click the blue + icon, then scroll down to Add a Branching Rule.
- Next hit configure.
- You’ll now be introduced to the following Branching Rule options, which allow you to choose the logic you’d like to introduce to this workflow, along with the defined rules and what to look for.

- Additionally, you’ll need to choose a starting variable. This can be something you just created or a vital piece of information from a previous workflow step.
- If you take the Name variable we created for the IDV section above, you could do something like the following:

This would then only allow recipients to pass through to the next step if their name from the first Identity Verification step is listed as Jessica. There are many more ways to implement these branching rules, but for the sake of simplicity we wanted to outline a very simple use case here.

You can learn more about how to configure this [Branch Logic here](https://support.docusign.com/s/document-item?language=en_US&bundleId=yff1696971835267&topicId=mnv1698169910928.html), if you’re interested.

### Ready to start building your Maestro workflow?

Looking to start building your workflow using the steps we’ve outlined? Learn more about [Docusign Maestro](https://www.docusign.com/products/platform/maestro).

[Log in](https://account.docusign.com/) to get started today with Maestro. If you need more information on this vital platform service before making an educated purchasing decision, visit our [Plans and Pricing page](https://ecom.docusign.com/plans-and-pricing/iam?utm_source=google&utm_medium=cpc&utm_campaign=GBL_XX_PRF_NEW_2401_SEMBranded&utm_term=docusign+pricing&campaignid=14964582893&adgroupid=127314395726&location=9031955&device=c&matchtype=e&extensionid=&creative=647597912345&keyword=docusign+pricing&placement=&network=g&gclid=CjwKCAjwyJqzBhBaEiwAWDRJVDLxvCk0vUFcfMZ8ami_9i4Ofh8AwaMp5SSStZJMgqUuSfwJhUYQ7hoC3VAQAvD_BwE&gad_source=1) to learn more.

## Table of contents

- [Common use cases](https://www.docusign.com/blog/maestro-tips-streamlined-setup-workflow#common-use-cases)

- [Things to know before getting started](https://www.docusign.com/blog/maestro-tips-streamlined-setup-workflow#things-to-know-before-getting-started)

- [Tips & tricks for building a Maestro workflow](https://www.docusign.com/blog/maestro-tips-streamlined-setup-workflow#tips-tricks-for-building-a-maestro-workflow)

Related topics

[Workflow Builder](https://www.docusign.com/products/platform/workflow-builder)

Share

[Share to LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fmaestro-tips-streamlined-setup-workflow "Share to LinkedIn")[Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fmaestro-tips-streamlined-setup-workflow "Share to Facebook")[Share to X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fmaestro-tips-streamlined-setup-workflow&text=Docusign Maestro: Tips for a Streamlined Setup and Workflow&hashtags=Docusign "Share to X")

Related posts

- [Intelligent Agreement Management](https://www.docusign.com/blog/topics/intelligent-agreement-management)Published Jun 12, 2026

  [## The Top Ways to Use AI for Contract Management and Workflow Automation](https://www.docusign.com/blog/top-ways-to-use-ai-for-contract-management-and-workflow-automation)

  [![Top Ways to Use AI for Contract Management and Workflow Automation](https://images.ctfassets.net/9pvazpst9iwl/7jSpzwtXLGXdjACj9Q0uR1/1834edcfc545282c6dfaea367dd85efa/AI-for-Contract-Management_26-06_Blog_1200x900_EN__1_.jpg?fm=avif&q=90&w=500)](https://www.docusign.com/blog/top-ways-to-use-ai-for-contract-management-and-workflow-automation)
- [Intelligent Agreement Management](https://www.docusign.com/blog/topics/intelligent-agreement-management)Published Jun 2, 2026

  [## How Housing Authorities Can Streamline HUD Tenant Recertification with Docusign IAM](https://www.docusign.com/blog/how-housing-authorities-can-streamline-hud-tenant-recertification-with-docusign-iam)

  Lee Fisher

  [![](https://images.ctfassets.net/9pvazpst9iwl/708o6LjITU7kM6GPusXMzX/2e032fc7ce149893e9a56bb3eaad1b7e/Government_HUD_blog.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/how-housing-authorities-can-streamline-hud-tenant-recertification-with-docusign-iam)
- [Intelligent Agreement Management](https://www.docusign.com/blog/topics/intelligent-agreement-management)Published Jun 2, 2026

  [## Managing OMB Memorandum M-26-10 Compliance: Why Federal Agencies Need an AI-Powered System of Record](https://www.docusign.com/blog/managing-omb-memorandum-m-26-10-compliance-why-federal-agencies-need-an-ai-powered-system-of-record)

  Lee Fisher

  [![](https://images.ctfassets.net/9pvazpst9iwl/y7js1x56CcK4IwblvsWFj/d6b2e1266424470cbdf1396856a89e9c/Government_OMB_Procurement_blog.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/managing-omb-memorandum-m-26-10-compliance-why-federal-agencies-need-an-ai-powered-system-of-record)

[Intelligent Agreement Management](https://www.docusign.com/blog/topics/intelligent-agreement-management)Published Jun 12, 2026

[## The Top Ways to Use AI for Contract Management and Workflow Automation](https://www.docusign.com/blog/top-ways-to-use-ai-for-contract-management-and-workflow-automation)

[![Top Ways to Use AI for Contract Management and Workflow Automation](https://images.ctfassets.net/9pvazpst9iwl/7jSpzwtXLGXdjACj9Q0uR1/1834edcfc545282c6dfaea367dd85efa/AI-for-Contract-Management_26-06_Blog_1200x900_EN__1_.jpg?fm=avif&q=90&w=500)](https://www.docusign.com/blog/top-ways-to-use-ai-for-contract-management-and-workflow-automation)

[Intelligent Agreement Management](https://www.docusign.com/blog/topics/intelligent-agreement-management)Published Jun 2, 2026

[## How Housing Authorities Can Streamline HUD Tenant Recertification with Docusign IAM](https://www.docusign.com/blog/how-housing-authorities-can-streamline-hud-tenant-recertification-with-docusign-iam)

Lee Fisher

[![](https://images.ctfassets.net/9pvazpst9iwl/708o6LjITU7kM6GPusXMzX/2e032fc7ce149893e9a56bb3eaad1b7e/Government_HUD_blog.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/how-housing-authorities-can-streamline-hud-tenant-recertification-with-docusign-iam)

[Intelligent Agreement Management](https://www.docusign.com/blog/topics/intelligent-agreement-management)Published Jun 2, 2026

[## Managing OMB Memorandum M-26-10 Compliance: Why Federal Agencies Need an AI-Powered System of Record](https://www.docusign.com/blog/managing-omb-memorandum-m-26-10-compliance-why-federal-agencies-need-an-ai-powered-system-of-record)

Lee Fisher

[![](https://images.ctfassets.net/9pvazpst9iwl/y7js1x56CcK4IwblvsWFj/d6b2e1266424470cbdf1396856a89e9c/Government_OMB_Procurement_blog.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/managing-omb-memorandum-m-26-10-compliance-why-federal-agencies-need-an-ai-powered-system-of-record)

## Docusign IAM is the agreement platform your business needs

[Start for Free](https://trial.docusign.com)[Explore Docusign IAM](https://www.docusign.com/intelligent-agreement-management)

![Person smiling while presenting](https://images.ctfassets.net/9pvazpst9iwl/1gOiICnusnBqWxB11vmsFs/99a7ee68a05fa07fe6e5e35186e45394/smiling-woman-in-bright-sweater-presents-charts-on-laptop.png?fm=avif&q=90&w=500)
