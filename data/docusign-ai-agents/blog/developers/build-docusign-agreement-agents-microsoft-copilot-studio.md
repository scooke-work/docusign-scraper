---
title: Build Agreement Agents in Microsoft Copilot Studio Using the Docusign MCP Connector
source_url: https://www.docusign.com/blog/developers/build-docusign-agreement-agents-microsoft-copilot-studio
site: www.docusign.com
breadcrumb:
- Home
- Home
- Blog
- Blog
- Developers
- Developers
scraped_at: '2026-06-18T17:36:06Z'
---

[Blog](https://www.docusign.com/blog)

# Build Agreement Agents in Microsoft Copilot Studio Using the Docusign MCP Connector

[![Author Purnima Ravichandran](https://images.ctfassets.net/9pvazpst9iwl/1WEcBOTQIlox4mCK1rNEwa/989785567380f733d1cc221262cb8839/PurnimaRavichandran.jpg?fm=avif&q=90&w=500)

Purnima RavichandranPrincipal Partner Solution Architect](https://www.docusign.com/blog/author/purnima-ravichandran)•Updated Jun 16, 2026

---

Summary•6 min read

Learn how to use the Docusign MCP connector in Microsoft Copilot Studio to build no-code conversational agents that surface agreement insights and automate agreement workflows.

![](https://images.ctfassets.net/9pvazpst9iwl/5Z1hvSJQq8wLtRnbgNViuW/af1254d84daa681f64990be3382d3f3e/co_pilot_docusign_draft_5.png?fm=avif&q=90&w=500)

| **Key takeaways** |
| --- |
| **• Docusign MCP connector for Microsoft Copilot Studio:** Builders can use the Docusign MCP connector to create no-code conversational agents that access Docusign capabilities directly in Copilot Studio.  **• Agreement workflows, now conversational:** Agents can help users retrieve agreement status, surface agreement insights, generate agreements, and trigger workflows using natural language.  **• Built for the Microsoft ecosystem:** The connector helps bring Docusign agreement actions into tools like Microsoft 365 Copilot and Teams, so teams can work from the apps they already use.  **• Secure, permission-aware access:** Docusign governs agreement access at the Docusign layer, so agents can only surface insights for agreements users are already permissioned to view. |

AI agents are shifting the agreement lifecycle from static, manual clicks to intelligent, conversational workflows. By using the Docusign connector in [Microsoft Copilot Studio opens in a new tab](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), developers and low-code builders can create agents that understand agreement context, securely access repository data, and take action in real time without writing custom integration code.

This implementation uses the **Model Context Protocol (MCP)** to expose Docusign capabilities as tools that an LLM can reason about. Whether you are automating seller tasks or building an internal procurement bot, this pattern allows Docusign to act as a native part of the Microsoft ecosystem.

In this post, you’ll learn what’s possible today, walk through a real-world scenario, and see how to build your first Docusign agent in Copilot Studio.

## What’s possible today with Docusign in Copilot Studio

### What is Microsoft Copilot Studio?

[Microsoft Copilot Studio opens in a new tab](https://www.microsoft.com/en-us/microsoft-365-copilot/microsoft-copilot-studio) is an end-to-end conversational AI platform that empowers you to create agents using natural language or a graphical interface. With Copilot Studio, you can easily design, test, and publish agents for your needs. You can build a standalone agent or publish to Microsoft 365 Copilot.

### What is the Docusign MCP connector?

The Docusign connector is powered by [**MCP (Model Context Protocol)**](https://developers.docusign.com/platform/mcp-server/), a standard that exposes application capabilities as tools that AI agents can invoke directly. In Copilot Studio, adding the Docusign connector gives your agent access to Docusign capabilities without custom API integration.

Using the Docusign connector in Copilot Studio, your agent can:

- Retrieve agreement status and metadata
- Generate and route agreements for signature
- Surface on-demand insights across one or more agreements
- Trigger actions across the agreement lifecycle

The agent dynamically decides what action to take and when, based on user intent and the logic defined by the agent builder.

Note: The Docusign connector is currently available in the demo environment and will be generally available in production soon. You can use your existing demo account or [sign up](https://www.docusign.com/developers/adlp/sandbox) for a free demo account.

## Agreement agent scenarios

### Scenario 1: Agreement insights and clause extraction

Users can ask:

- “Summarize payment terms and termination clauses from the latest MSA with Fontara”
- "Would giving a discount of 10% to customer *Zaava* violate any clauses with other customers?"
- The agent analyzes the agreement and returns key clauses, summaries of important terms, and contextual insights.

### Scenario 2: Agreement status and tracking

Users can ask:

- "What's the status of the offer letter sent to John Doe?"
- "List agreements pending signature for more than a week"

The agent retrieves real-time agreement metadata including current status, recipient progress, and timestamps.

### Scenario 3: Send agreements using natural language

Users can say:

- “Send an NDA to *Zaava* using the standard template”

The agent identifies the correct template, adds recipients, and sends the agreement.

### Scenario 4: Trigger end-to-end agreement workflows

Agents can orchestrate multi-step processes such as:

- Fetching data from CRM
- Creating agreements and routing for signature
- Storing the signed agreement in SharePoint

The agent kicks off a workflow in Workflow Builder, passing required inputs.

## Use case: Automate seller tasks with a Docusign agent

A sales team can manage agreement tasks through an agent built on Docusign in Microsoft 365 Copilot. Here's how to build it.

Let’s walk through how to build an agent for this use-case in Copilot Studio.

### Step 1: Create a new agent in Copilot Studio

1. Open Copilot Studio from your Microsoft 365 environment.
2. From the left navigation pane, select **Agents** and then **+ New Agent**.
3. Under settings, confirm that **Generative AI orchestration** is enabled
4. Enter a **Name** (for example, “Seller Buddy”) and a description of what the agent should do.
5. Update Instructions to describe the agent's behavior and rules.

*Note: If your Docusign account contains many similarly named templates or workflows, consider specifying the template name or ID directly in the agent's instructions to ensure consistent, predictable behavior & to add guardrails to the agent.*

### Step 2: Add the Docusign connector

1. Go to **Tools** > **Add a tool**, then search for *Docusign MCP* and add the Docusign connector
2. Once added, the connector appears under **Tools**. Click it to view available capabilities.
3. Add any additional tools your agent needs (such as Outlook)

### Step 3: Test the agent

Now that your tools are configured, it’s time to test the agent with prompts.
*Note: Make sure your Docusign demo account includes the required templates, sample agreements, and Workflows needed by the agent.*

Open the **Test** pane on the right-hand side of Copilot Studio and try these prompts:

- **Check agreement status:** "Check if there's an active NDA with SmartFactory Systems"

  - The agent queries Docusign's agreement repository and returns the relevant details
- **Send an agreement:** "Send an NDA to Zaava using the standard NDA template"

  - The agent prompts for any missing details (such as recipient email) and sends the agreement
- **Trigger a workflow:** "Trigger a Workflow to fetch customer details from the CRM and send a Data Processing Agreement to Fontara"

Use the **Activity** tab to verify which Docusign tools were invoked for each prompt. From here, iterate: test different prompts, select your preferred model, and refine the agent's instructions.

### Step 4: Publish the agent

Use the **Channels** tab to deploy your agent to Microsoft 365 Copilot, Microsoft Teams, or any other supported channel.

## How the Docusign connector works

The Docusign connector gives agents access to Docusign IAM capabilities, including context-aware agreement insights retrieval, natural language interaction, and real-time action. By extending Docusign into the tools where your teams already work, agents become a natural part of the agreement lifecycle without sacrificing control or compliance.

Under the hood, [Docusign Iris](https://support.docusign.com/s/document-item?language=en_US&bundleId=fzd1707173174972&topicId=usy1712258503642.html&_LANG=enus) pre-processes agreement metadata, which means:

- **Faster retrieval:** Structured insights enable quick search without parsing full documents
- **Secure and compliant:** Users can only access insights for agreements they're permissioned to view, with access governed at the Docusign layer
- **Efficient token usage:** LLMs query pre-processed metadata rather than raw agreement text

## Additional resources

- [Build with the Docusign MCP Server](https://developers.docusign.com/platform/mcp-server/)
- [Get your free Docusign developer account](https://www.docusign.com/developers/adlp/sandbox)
- [Build agents with Copilot Studio agent builder opens in a new tab](https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/copilot-studio-agent-builder-build)
- [Quickstart: Create and deploy an agent in Copilot Studio opens in a new tab](https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-get-started)
- [Copilot Studio Agent Academy opens in a new tab](https://learn.microsoft.com/en-us/shows/copilot-studio-agent-academy/)

![Author Purnima Ravichandran](https://images.ctfassets.net/9pvazpst9iwl/1WEcBOTQIlox4mCK1rNEwa/989785567380f733d1cc221262cb8839/PurnimaRavichandran.jpg?fm=avif&q=90&w=500)

Purnima RavichandranPrincipal Partner Solution Architect

Purnima Ravichandran is a Principal Partner Solutions Architect at Docusign, specializing in Intelligent Agreement Management (IAM) and Microsoft integrations. With deep Microsoft expertise and a passion for AI, she partners with customers and partners to deliver innovative solutions that accelerate digital transformation.

[More posts from this author](https://www.docusign.com/blog/author/purnima-ravichandran)

Share

[Share to LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Fbuild-docusign-agreement-agents-microsoft-copilot-studio "Share to LinkedIn")[Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Fbuild-docusign-agreement-agents-microsoft-copilot-studio "Share to Facebook")[Share to X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Fbuild-docusign-agreement-agents-microsoft-copilot-studio&text=Build Agreement Agents in Microsoft Copilot Studio Using the Docusign MCP Connector&hashtags=Docusign "Share to X")

Related posts

- [Developers](https://www.docusign.com/blog/developers)Published Jun 16, 2026

  [## How to Configure and Publish an Azure Custom Extension App for Docusign IAM](https://www.docusign.com/blog/developers/configure-deploy-azure-custom-extension-app-docusign-iam)

  ![Author Mohamed Ali](https://images.ctfassets.net/9pvazpst9iwl/66eZQrBN42mOTqQ3MTt4tb/1792588fa2fb4e5fe93b8a4a8481c565/mohamed_ali.jpg?fm=avif&q=90&w=500)

  Mohamed Ali

  [![Featured image for Dobby blog](https://images.ctfassets.net/9pvazpst9iwl/grPE0gIUY4kgyWVIUbgz2/4f435a93c25d796fd91b609d4274afe1/coding-elf-blog-visual.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/configure-deploy-azure-custom-extension-app-docusign-iam)
- [Developers](https://www.docusign.com/blog/developers)Published May 21, 2026

  [## How Developers Can Build Agentic Agreement Workflows on Docusign IAM](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows)

  ![Author Larry Jin](https://images.ctfassets.net/9pvazpst9iwl/5XbuJzjmhsmfVi2Lj9nWwu/f3ae8c298109dd95f1bc755cf0a9ba01/Larry_Jin?fm=avif&q=90&w=500)

  Larry Jin

  [![](https://images.ctfassets.net/9pvazpst9iwl/34FVWrGquLXSTp0qOJcoJY/47b54b4d21c68c896e88cbd3865d6c4d/Momentum26-Developer-Launch_26-05_Blog_My-Agents_1200x900_EN.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows)
- [Developers](https://www.docusign.com/blog/developers)Published May 21, 2026

  [## How to design a verification-first financial onboarding workflow using Docusign IAM and J.P. Morgan Payments](https://www.docusign.com/blog/developers/verification-first-financial-onboarding-docusign-jp-morgan-payments)

  ![Author Niani Byrd](https://images.ctfassets.net/9pvazpst9iwl/KMDcdizn2FYO7YIZgMxHI/e727a59804a2871e7e24a150996465e9/NianiByrd.jpg?fm=avif&q=90&w=500)

  Niani Byrd

  [![](https://images.ctfassets.net/9pvazpst9iwl/6aqrdBpTJUvnQXmLhlxzC6/39964dfa4ffc6e10864f3ed3281d8863/Mo26-Developers-Session-Workflow_26-05_Blog_1200x900_EN__1_.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/verification-first-financial-onboarding-docusign-jp-morgan-payments)

[Developers](https://www.docusign.com/blog/developers)Published Jun 16, 2026

[## How to Configure and Publish an Azure Custom Extension App for Docusign IAM](https://www.docusign.com/blog/developers/configure-deploy-azure-custom-extension-app-docusign-iam)

![Author Mohamed Ali](https://images.ctfassets.net/9pvazpst9iwl/66eZQrBN42mOTqQ3MTt4tb/1792588fa2fb4e5fe93b8a4a8481c565/mohamed_ali.jpg?fm=avif&q=90&w=500)

Mohamed Ali

[![Featured image for Dobby blog](https://images.ctfassets.net/9pvazpst9iwl/grPE0gIUY4kgyWVIUbgz2/4f435a93c25d796fd91b609d4274afe1/coding-elf-blog-visual.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/configure-deploy-azure-custom-extension-app-docusign-iam)

[Developers](https://www.docusign.com/blog/developers)Published May 21, 2026

[## How Developers Can Build Agentic Agreement Workflows on Docusign IAM](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows)

![Author Larry Jin](https://images.ctfassets.net/9pvazpst9iwl/5XbuJzjmhsmfVi2Lj9nWwu/f3ae8c298109dd95f1bc755cf0a9ba01/Larry_Jin?fm=avif&q=90&w=500)

Larry Jin

[![](https://images.ctfassets.net/9pvazpst9iwl/34FVWrGquLXSTp0qOJcoJY/47b54b4d21c68c896e88cbd3865d6c4d/Momentum26-Developer-Launch_26-05_Blog_My-Agents_1200x900_EN.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/momentum-26-agentic-agreement-workflows)

[Developers](https://www.docusign.com/blog/developers)Published May 21, 2026

[## How to design a verification-first financial onboarding workflow using Docusign IAM and J.P. Morgan Payments](https://www.docusign.com/blog/developers/verification-first-financial-onboarding-docusign-jp-morgan-payments)

![Author Niani Byrd](https://images.ctfassets.net/9pvazpst9iwl/KMDcdizn2FYO7YIZgMxHI/e727a59804a2871e7e24a150996465e9/NianiByrd.jpg?fm=avif&q=90&w=500)

Niani Byrd

[![](https://images.ctfassets.net/9pvazpst9iwl/6aqrdBpTJUvnQXmLhlxzC6/39964dfa4ffc6e10864f3ed3281d8863/Mo26-Developers-Session-Workflow_26-05_Blog_1200x900_EN__1_.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/verification-first-financial-onboarding-docusign-jp-morgan-payments)

## Docusign IAM is the agreement platform your business needs

[Start for Free](https://trial.docusign.com)[Explore Docusign IAM](https://www.docusign.com/intelligent-agreement-management)

![Person smiling while presenting](https://images.ctfassets.net/9pvazpst9iwl/1gOiICnusnBqWxB11vmsFs/99a7ee68a05fa07fe6e5e35186e45394/smiling-woman-in-bright-sweater-presents-charts-on-laptop.png?fm=avif&q=90&w=500)
