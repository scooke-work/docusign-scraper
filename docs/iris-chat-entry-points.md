# Docusign Iris — chat entry points

Where the **Iris‑powered conversational surfaces** can be initiated. "Iris" is the
AI *engine*, not one chat — it powers several distinct chat / Q&A experiences, each
with its own entry points.

> Grounded in the scraped corpus (`docusign-iris-ai-assistant`,
> `docusign-esignature-support`, `docusign-ai-agents`). Newer Momentum '26 items
> are flagged **early access**; absence here means *not documented*, not
> *unavailable*.

## 1 · AI‑Assisted Review **Chat** — Agreement Desk *(Word add‑in)*
The redline/Q&A chat. Three documented ways to start it:

| # | Start from | Path |
|---|-----------|------|
| ① | **An Agreement Desk request record** | Agreements → **Requests** → open a request → **Documents** tab → **Options → Edit in Word** (or open the **document preview → Edit in Word**) → add‑in opens on the **Chat** tab |
| ② | **The Agreement Desk document preview** | Preview shows the doc *with AI‑Assisted Review* — access chat & playbook features directly |
| ③ | **A local document in Microsoft Word** | Open the doc → **Home ribbon → Docusign AI‑Assisted Review add‑in** → Chat |

*Gated:* requires **playbook / Chat permissions** — included with **Agreement Desk Enterprise and Sales** plans.
Source: *Chat in the Docusign AI‑Assisted Review add‑in for Agreement Desk*.

## 2 · Signing AI **"Ask a question"** — eSignature
AI‑Assisted Agreement Summaries & Q&A.

- **From the eSignature signing/review experience** — open the document → an **AI Summary** displays → select **"Ask a question"** → ask in the *"Ask a question about this document"* field. Answers include **citations** to the source clauses.

Source: *Use Docusign AI‑Assisted Signing Features* / *Introducing AI‑Assisted Agreement Summaries and Q&A in Docusign eSignature*.

## 3 · Agent & external chat *(early access / Beta)*
- **Docusign Iris assistant / Agent Studio** — agents can be **invoked from chat** or deployed to run autonomously (Momentum '26).
- **MCP Server (Beta)** — chat with Docusign from external clients: **Claude, Gemini, ChatGPT**, via natural language.
- **Microsoft Copilot Studio** — build/test agents and chat from the Copilot **Test** pane.

Source: `docusign-ai-agents` (MCP Server, Agent Studio, Copilot Studio).

---

## Not documented in the corpus
- **No free‑form chat panel in the Agreement Manager *Agreement preview* page** — there the AI surface is **suggestions + extraction + data review**, not a conversational chat. The "Ask a question" Q&A only appears for **eSignature** signing.
- **In‑app entry points for the new *Docusign Iris assistant*** (Momentum '26, early access) aren't documented page‑by‑page — confirm those against **live screenshots** if needed.

*Bottom line:* the documented **in‑product** initiation points are **Agreement Desk**
(request record · document preview · Word add‑in) and **eSignature** (signing
experience); **agent/external** chat comes via the Iris assistant, MCP Server, and
Copilot Studio. See [iris-chat-entry-points.html](iris-chat-entry-points.html) for the visual.
