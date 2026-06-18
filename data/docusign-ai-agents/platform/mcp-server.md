---
title: Build with the Docusign MCP Server (Beta)
source_url: https://developers.docusign.com/platform/mcp-server/
site: developers.docusign.com
breadcrumb:
- Platform 101
- Platform 101
- MCP Server
scraped_at: '2026-06-18T17:32:49Z'
---

# Build with the Docusign MCP Server (Beta)

**Beta notice:** THE DOCUSIGN MCP SERVER IS A BETA FEATURE AND IS PROVIDED “AS IS” AND “AS AVAILABLE” WITHOUT WARRANTY. You acknowledge you may experience bugs or performance issues and the feature may change as Docusign refines it. By using the MCP Server, you acknowledge you do so at your own discretion and risk. Access to certain capabilities is under “limited availability." The Docusign MCP server connects Docusign capabilities to third-party AI-assisted tools. Developers must trust any remote MCP server they use. A malicious server can exfiltrate sensitive data. Running agents in a fully automated fashion increases vulnerability to exposure via prompt-injection attacks. Interaction with the MCP server requires a valid OAuth access token. You are solely responsible for securing your access token and are advised to use least-privileged accounts when connecting. Customers must choose the OAuth grant type appropriate for their use case. Users should have a “human in-the-loop” to confirm tools and accuracy and appropriateness of AI output.

**The MCP Server is now available in Open Beta.** Connect and interact with your Docusign accounts through MCP servers — now available for both developer and production accounts. No intake form or additional approval required.

## What is Docusign MCP?

The [Docusign Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) server introduces a new way for developers to interact with Docusign APIs through natural, conversational AI interfaces. Instead of switching between documentation, API references, and code, you can now use any AI assistant that supports the MCP standard to explore Docusign’s capabilities, including generating access tokens, testing APIs, and automating end-to-end agreement workflows.

## Prerequisites

Before connecting to the Docusign MCP server, you need:

- A Docusign developer account. You can [create one](https://www.docusign.com/developers/sandbox)
- The Docusign MCP server can connect to any AI-assisted tool powered by a [large language model](https://www.ibm.com/think/topics/large-language-models) (LLM) platform. Here are a few examples of tools that support MCP:
  - [Anthropic Claude Desktop](https://claude.ai/)
  - [GitHub Copilot](https://github.com/features/copilot)
  - [Google Gemini CLI](https://geminicli.com/)
  - [Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-365-copilot/microsoft-copilot-studio)

## Connect to the MCP Server

You can connect to the Docusign MCP server through a variety of compatible AI assistants and developer tools. This guide demonstrates how to configure and interact with the Docusign MCP server. Use the following Docusign MCP URLs for the demo and production environments.

| Transport Type | Environment | URL |
| --- | --- | --- |
| Streamable HTTP | Demo | https://mcp-d.docusign.com/mcp |
| Streamable HTTP | Production | https://mcp.docusign.com/mcp |

## Authentication

To interact with the MCP server, you’ll need a valid OAuth access token. Docusign MCP server supports access tokens only for **Confidential Authorization Code Grant** OAuth grant type.

See [Confidential Authorization Code Grant](https://developers.docusign.com/platform/auth/authcode/#confidential-authorization-code-grant) for guidance on your options to get an Confidential Authorization Code Grant OAuth token, or learn about how you can get an access code using the  [Docusign Developer AI Assistant for VS Code](https://developers.docusign.com/tools/ai-assistant-vs-code/#get-an-access-token).

## Explore what’s possible with the Docusign MCP Server

The Docusign MCP Server makes it easier than ever to build and experiment with agreement workflows. You can ask natural language questions and receive clear, actionable answers about Docusign APIs and products directly from your preferred AI assistant or developer tool. It can also enable you to test or execute complex API operations with simple prompts, making tasks such as authentication, API testing, and envelope creation more efficient. Together, these capabilities work together to give you a more efficient, intelligent way to build with Docusign.

| Use case | Example prompts |
| --- | --- |
| Learn about Docusign products | “Help me understand Workflow Builder and how I can use it in my application.”  “My company builds healthcare software with an existing eSign integration. Can we use Docusign to provide agreement insights to our clients?”  “I want to automate the full agreement workflow from creation to signature. What APIs do I use?” |
| Test APIs and automate workflows | “Show me how to implement Docusign APIs in my app and handle authentication securely.”  “Generate a new agreement and send it for signature using my standard client onboarding template.”  “Trigger the Workflow Builder workflow instance for my account.” |

### See the MCP server in action

## Available tools

### Interact with Docusign APIs

For users using our connectors in production, we currently support only seven API groups. As a developer you can launch your MCP-configured AI assistant to explore additional APIs and endpoints:

### Developer capabilities

Beyond APIs, the MCP server empowers you to work smarter through integrated tools that provide instant answers, documentation search, and contextual recommendations inside your workflow.

| **Capability** | **Description** |
| --- | --- |
| `searchDocusignDocs` | Answers Docusign-related questions by searching and reasoning over public Developer Center content and documentation |
| `generateAccessToken` | Provides interactive OAuth access token generation to help create Integration Keys, configure OAuth settings, and obtain access tokens. |
| `getUserInfo` | Gets a user's complete profile, which contains their name, email, account IDs, and organization details. |

## Next steps

- Try the Docusign MCP server with [Anthropic (Claude)](https://developers.docusign.com/platform/mcp-server/anthropic-claude/) to explore its capabilities.
- Try the Docusign MCP server with [GitHub (Copilot)](https://developers.docusign.com/platform/mcp-server/github-copilot/) to explore its capabilities in Microsoft Visual Studio Code.
- Try the Docusign MCP server with [Google Gemini CLI](https://developers.docusign.com/platform/mcp-server/google-gemini-cli/) to explore its capabilities.
- Try the Docusign MCP server with [Microsoft Copilot Studio](https://developers.docusign.com/platform/mcp-server/microsoft-copilot/) to explore its capabilities.
- For more information on using production Docusign account with Docusign MCP server, see [Docusign MCP Server and AI Connector User Guide](https://support.docusign.com/s/document-item?language=en_US&bundleId=ug3906200f-95c6-4a6b-90b1-f928c85961c6&topicId=con1438e5dd-ae84-435f-8b2e-028117782a6d.html&_LANG=enus)
- Share your thoughts on the [Docusign Model Context Protocol Server (beta): Feedback form](https://docusign.co1.qualtrics.com/jfe/form/SV_7OoUal8iiiJO6ZE) to help improve future releases and expand MCP capabilities.

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
