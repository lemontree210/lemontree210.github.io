Title: Lena Shakurova on automation + other people that can teach you to automate routine tasks 
Date: 2025-09-01 21:00
Category: Automation
Tags: Automation, AI, n8n, Zapier, Make.com, Airtable, API, Apify, OpenRouter, Tavily, Pyrus, Relevance AI, Relay.app, Pipedream, Notion, Gmail, Calendar Management, Telegram, Content Automation, Lead Generation, Workflow, No-code, Low-code, Integration, Vector Search, AI Agents, Clutch, Instantly, Perplexity, MindStudio, Workflow Automation  

I watched [this video on automation](https://www.youtube.com/watch?v=7JVrmSDVHW4) by Lena Shakurova and I thought I could use a summary.

## I should only consider automating a process if:

- It's a standard process with multiple steps
- I have no time to do the task manually
- I'm not organized enough to follow through with the whole process properly 
<!-- PELICAN_END_SUMMARY -->

***

## Use cases that I found relevant for me

- **Calendar:** Multi-step event creation, integrating text/voice, Google Calendar, Zoom, and notification workflows.
- **Knowledge Organization:** For example, a Telegram bot classifies and routes notes, links, and to-dos into the correct Notion tables or categories.
- **Post-Meeting Calls:** AI agent analyzes call transcripts to update CRM automatically, create action lists, or write follow-up emails.
- **Content Creation:** Repurposing (e.g., YouTube to LinkedIn posts), automated newsletters, content distribution across platforms.
- **Freelance Outreach:** Automated job notification and personalized message drafting for platforms like Upwork.
- **Lead Generation:** Automated process using Clutch (company database), Apify (data extraction), Airtable (database), Instantly (email campaigns).
- **Research:**
    - Competitor research with Perplexity and Tavily.
    - Custom “deep research” assistants for extended literature and citation extraction into PDFs.
- **Automated Executive Assistant:** Multi-purpose agent integrating several routine functions via Telegram, Notion, etc..

The key component in many workflows is an AI block that performs a classification task (e.g. to what category an email that just landed in your inbox belongs).

***

## Apps/Services

Some of them were not directly mentioned in Lena's video.

### API and Workflow Integration

- **[Make.com](https://www.make.com)**: Visual, no-code workflow automation for thousands of apps including Apify, Airtable.
- **[n8n](https://n8n.io)**: Low-code workflow builder, supports AI blocks, API connections, custom automations.
- **[Pipedream](https://pipedream.com)**: Automation platform for developers to build workflows across APIs.
- **[Relay.app](https://relay.app)**: User-friendly tool for creating workflow automations (including Google Calendar).
- **[Relevance AI](https://relevanceai.com)**: Agentic workflow development environment for automating business processes.
- **[Zapier](https://zapier.com)**: Popular online automation tool to link web apps, manage triggers and actions.

#### Brief comparison of Make.com, n8n, Pipedream, Relay.app, Relevance AI and Zapier

| Platform | Hosting | Target Users | Best For | Unique Strengths | Key Limits | Integrations |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| **Make.com** | Cloud only | Power users, Ops teams | Advanced visual workflows | Powerful scenario builder, data tools | No self-host, module limits | 1500+ |
| **n8n** | Cloud/Self-host | Technical, privacy-focused | Custom automations, self-hosting | Unlimited on-prem, code nodes | Learning curve, fewer connectors | 400+ |
| **Pipedream** | Cloud only | Developers | Code-heavy, serverless builds | Serverless code, JS/Python in flow | Dev-oriented, not “no-code” | 1,000+ (API focus) |
| **Relay.app** | Cloud only | Small teams, beginners | Simple automations, fast setup | Intuitive UI, easy onboarding | Less depth, fewer connectors | 50+ |
| **Zapier** | Cloud only | All business, non-tech | Plug-and-play, largest app catalog | Simplicity, 7,000+ integrations | Price at scale, limited complexity | 7,000+ |
| **Relevance AI** | Cloud only | AI/Analytics teams, data ops | AI agents with workflow, analytics | LLM-based agent flows, built-in vectors | Credit model, smaller catalog | 100+ core apps |

Pricing as of 2025

| Platform | Free Plan | Entry Paid Plan | Scale/Team Pricing |
| :-- | :-- | :-- | :-- |
| Make.com | Yes (limits) | ~\$9/mo (billed annually) | Up to \$29, \$59, custom (ops-based) |
| n8n | Yes (self-host) | \$20/mo (cloud) | Cloud Pro/Business: \$50–\$250+/mo |
| Pipedream | Yes (credits) | \$29/mo (basic) | \$49 advanced, custom at enterprise |
| Relay.app | Yes | \$9/mo (Pro) | \$59/mo (Teams), custom |
| Zapier | Yes (basic tasks) | \$29.99/mo (Professional) | \$73/mo+ (Team), Business \$103/mo+ |
| Relevance AI | Yes* | \$19/mo (Pro, 1 user) | \$199/mo (Team, 10 users), \$599+ |

- *Relevance AI’s free plan offers ~100 credits/day, 1 user, 10MB knowledge, with paid tiers scaling users, operations, and AI capabilities. Pricing is credit-based.

Summary:

- **Make.com** is good for visual, complex automations with robust data tools and a moderate price curve.
- **n8n** is great because of self-hosting option (the only one that can be self-hosted, it seems) and great customization.
- **Pipedream** is developer-centric with serverless, code-heavy flows, best for those comfortable writing JavaScript or Python.
- **Relay.app** is focused on ease-of-use and onboarding for small teams and non-technical users.
- **Relevance AI** fills a specialized niche as the most AI-centric workflow tool in this lineup, ideal for businesses aiming to build autonomous, customizable AI agents for analytics, content, sales etc.
- **Zapier** is seen as the easiest for non-techs and has the broadest app ecosystem, but costs rise quickly.

For maximum affordability and control, n8n Community is ideal; for a plug-and-play experience, Relay.app or Zapier excel; for advanced automation and data handling, Make.com stands out.

### Data Collection, Processing and Storage

- **[Airtable](https://airtable.com)**: Online relational database for storing, organizing, and integrating structured data.
- **[Apify](https://apify.com)**: Platform for web scraping and workflow automations, can output data to Airtable or Google Sheets.
- **[OpenRouter](https://openrouter.ai)**: Unified API gateway for access to hundreds of AI models (Anthropic, Google, Meta, Mistral).


### Lead Generation and Outreach

- **[Clutch](https://clutch.co)**: Business directory for finding leads and company info.
- **[Instantly](https://instantly.ai)**: Tool for scaling and automating cold email campaigns.
- **[Upwork](https://upwork.com)**: Freelance platform where automations can monitor listings, draft responses.


### Media Creation and Processing

- **[Creatomate](https://creatomate.com)**: Video automation API, used to generate and edit media for content workflows.
- **[Replicate](https://replicate.com)**: Image generation via model APIs, used for content/video automation.
- **[11labs](https://11labs.io)**: Text-to-speech API for automating audio generation in videos.


### Research and Reference Tools

- **[Perplexity](https://perplexity.ai)**: Just mentioning it here, I know what it is :)
- **[Tavily](https://tavily.com)**: Intelligent research agent for summarizing and extracting citations from web sources.
- **[Superhuman](https://superhuman.com)**: AI-powered advanced email client.


### Others

- **[MindStudio](https://mindstudio.com)**: No-code platform for building AI-driven applications.
- **[Pyrus](https://pyrus.com)**: Workflow, task, and communication platform with document management, approval flows, and email/task integrations. Designed for modern teams, it integrates with external apps and features no-code customization.

***

## People and Additional Links

- **[Lena Shakurova](https://www.linkedin.com/in/lena-shakurova/)** ([YouTube](https://www.youtube.com/@LenaShakurova)): AI advisor, workflow automation expert, founder of Pars Labs and Chatbotly, organizer of AI automation courses.
  - [Lena's n8n automation templates library](https://maven.com/p/f5c898/60-n8n-automation-tutorials)

Lena did a wonderful job mentioning all other experts and referencing their videos.

- **Nate Herk** ([YouTube](https://www.youtube.com/@nateherk)): Educator, n8n and AI automation tutorial creator, known for actionable video blueprints.
- **[Roberto H Luna](https://www.linkedin.com/in/robertohluna/)** ([YouTube](https://www.youtube.com/@robertohluna)): Founder sharing advanced AI agentic workflows for meetings, automating post-call actions and CRM updates.
- **[Clarence Nap](https://www.linkedin.com/in/clarence-nap/)**: On [his YouTube channel](https://www.youtube.com/@ClarenceAutomations), he demonstrated lead generation stack (Clutch, Apify, Airtable, Instantly); known for operational sales automations .
- **[Leon van Zyl](https://www.linkedin.com/in/leonvanzyl/)** ([YouTube](https://www.youtube.com/@leonvanzyl)): AI automation educator, workflow builder focusing on beginner-friendly n8n use cases.

_Note: the base of the summary was created by AI, with manual editing afterwards._
