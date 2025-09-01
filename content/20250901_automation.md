Title: Lena Shakurova on Automation
Date: 2025-09-01 21:00
Category: Automation
Tags: n8n, 


I've watched [a video on Automation](https://www.youtube.com/watch?v=7JVrmSDVHW4) by Lena Shakurova and thought I'd use a summary.

The base of the summary was created by Perplexity, with some manual editing afterwards.

## When to Automate

- **Standard process with multiple steps**
- **No time to do the task manually**
- **Disorganization hinders proper completion**
- **Running experiments at scale**
[^2_1]

***

## Use cases that I found relevant for me

- **Calendar:** Multi-step event creation, integrating text/voice, Google Calendar, Zoom, and notification workflows. Example: AI Foundations YouTube channel—“AI agent use cases in n8n”.[^2_1]
- **Knowledge Organization:** Telegram bot classifies and routes notes, links, and to-dos into the correct Notion tables or categories.[^2_1]
- **Post-Meeting Calls:** AI agent analyzes call transcripts to update CRM automatically, create action lists, or write follow-up emails. See Roberto H Luna’s workflow.[^2_2][^2_1]
- **Content Creation:** Repurposing (e.g., YouTube to LinkedIn posts), automated newsletters, YouTube shorts agent, content distribution across platforms.[^2_1]
- **Freelance Outreach:** Automated job notification and personalized message drafting for platforms like Upwork.[^2_1]
- **Lead Generation:** Automated process using Clutch (company database), Apify (data extraction), Airtable (database), Instantly (email campaigns). See Clarence's stack example.[^2_3][^2_1]
- **Research:**
    - Competitor research with Perplexity and Tavily.
    - Custom “deep research” assistants for extended literature and citation extraction into PDFs.[^2_1]
- **Automated Executive Assistant:** Multi-purpose agent integrating several routine functions via Telegram, Notion, etc..[^2_1]

***

## Apps/Services

Some of them were not directly mentioned in Lena's video.

### API and Workflow Integration

- **Make.com**: Visual, no-code workflow automation for thousands of apps including Apify, Airtable.[^2_6]
- **n8n**: Low-code workflow builder, supports AI blocks, API connections, custom automations.[^2_1]
- **Pipedream**: Automation platform for developers to build workflows across APIs.[^2_1]
- **Relay.app**: User-friendly tool for creating workflow automations (including Google Calendar).[^2_7]
- **Relevance AI**: Agentic workflow development environment for automating business processes.[^2_1]
- **Zapier**: Popular online automation tool to link web apps, manage triggers and actions.[^2_8][^2_9]

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
| Make.com | Yes (limits) | ~\$9/mo (billed annually) | Up to \$29, \$59, custom (ops-based)[^4_1][^4_2] |
| n8n | Yes (self-host) | \$20/mo (cloud) | Cloud Pro/Business: \$50–\$250+/mo |
| Pipedream | Yes (credits) | \$29/mo (basic) | \$49 advanced, custom at enterprise |
| Relay.app | Yes | \$9/mo (Pro) | \$59/mo (Teams), custom |
| Zapier | Yes (basic tasks) | \$29.99/mo (Professional) | \$73/mo+ (Team), Business \$103/mo+ |
| Relevance AI | Yes* | \$19/mo (Pro, 1 user) | \$199/mo (Team, 10 users), \$599+ |

- *Relevance AI’s free plan offers ~100 credits/day, 1 user, 10MB knowledge, with paid tiers scaling users, operations, and AI capabilities. Pricing is credit-based.[^4_3][^4_4]

Summary:

- **Make.com** is good for visual, complex automations with robust data tools and a moderate price curve, but only offers cloud hosting.[^3_10][^3_2]
- **n8n** is loved by technical and privacy-conscious users for its open-source self-hosting, deep customization, and AI friendliness, with the most favorable pricing for the self-hosted Community Edition.[^3_3][^3_4][^3_10]
- **Pipedream** is developer-centric with serverless, code-heavy flows, best for those comfortable writing JavaScript or Python.[^3_6][^3_5]
- **Relay.app** is focused on ease-of-use and onboarding for small teams and non-technical users, with streamlined pricing and beginner-friendly workflows.[^3_11][^3_7]
- **Relevance AI** fills a specialized niche as the most AI-centric workflow tool in this lineup, ideal for businesses aiming to build autonomous, customizable AI agents for a range of tasks spanning analytics, content, sales, and operations.[^5_10][^5_2][^5_3]
- **Zapier** remains the easiest for non-techs and has the broadest app ecosystem, but costs rise quickly as usage or workflow complexity increases.[^3_9][^3_10]

Each tool fits different skill levels, workflow complexity, and hosting needs. For max affordability and control, n8n Community is ideal; for a plug-and-play experience, Relay.app or Zapier excel; for advanced automation and data handling, Make.com stands out; Pipedream is excellent for developer-centric automations.
[^3_12][^3_13][^3_14]


### Data Collection, Processing and Storage

- **Airtable**: Online relational database for storing, organizing, and integrating structured data.[^2_16][^2_3]
- **Apify**: Platform for web scraping and workflow automations, can output data to Airtable or Google Sheets.[^2_3][^2_6][^2_16]
- **OpenRouter**: Unified API gateway for access to hundreds of AI models (Anthropic, Google, Meta, Mistral).[^2_5]

### Lead Generation and Outreach

- **Clutch**: Business directory for finding leads and company info.[^2_1]
- **Instantly**: Tool for scaling and automating cold email campaigns.[^2_1]
- **Upwork**: Freelance platform where automations can monitor listings, draft responses.[^2_1]

### Media Creation and Processing

- **Creatomate**: Video automation API, used to generate and edit media for content workflows.[^2_1]
- **Flux/Replicate**: Image generation via model APIs, used for content/video automation.[^2_1]
- **11labs**: Text-to-speech API for automating audio generation in videos.[^2_1]


### Research and Reference Tools

- **Perplexity**: AI-powered research and information retrieval tool (direct answers, citations).[^2_20]
- **Tavily**: Intelligent research agent for summarizing and extracting citations from web sources.[^2_21][^2_22][^2_23]
- **Superhuman**: AI-powered advanced email client (mentioned in general automation discussions).


### Team Workflow and Task Management

- **Pyrus**: Workflow, task, and communication platform with document management, approval flows, and email/task integrations. Designed for modern teams, it integrates with external apps and features no-code customization.[^2_24][^2_25][^2_26][^2_27][^2_28][^2_29]


### Others (Mentioned/Implied)

- **MindStudio**: No-code platform for building AI-driven applications.[^2_1]

***

## People Referenced

- **Lena Shakurova** (author): AI advisor, workflow automation expert, founder of Pars Labs and Chatbotly, organizer of AI automation courses.[^2_1]
- **Nate Herk**: Educator, n8n and AI automation tutorial creator, known for actionable video blueprints.[^2_1]
- **Leon van Zyl**: AI automation educator, workflow builder focusing on beginner-friendly n8n use cases.[^2_30][^2_31]
- **Roberto H Luna**: Founder sharing advanced AI agentic workflows for meetings, automating post-call actions and CRM updates.[^2_2]
- **Clarence | AI Automation**: Demonstrated lead generation stack (Clutch, Apify, Airtable, Instantly); known for operational sales automations [^2_1].

***

## Additional links

- [AI Foundations YouTube on Calendar Automation \& AI agents](https://youtube.com/watch?v=ZXtVvroop_U)[^2_1]
- [Apify + Airtable Integration by Make.com](https://www.make.com/en/integrations/apify/airtable)[^2_6]
- [Leon van Zyl YouTube](https://youtube.com/watch?v=UeFi5oV9UpY)[^2_30]
- [Roberto H Luna LinkedIn: Revealing my AI meeting workflow](https://www.linkedin.com/posts/robertohluna_revealing-my-ai-meeting-workflow-how-i-activity-7290101067038507009-wVKl)[^2_2]
- [Lena's n8n automation tutorial library](https://maven.com/p/f5c898/60-n8n-automation-tutorials)[^2_1]
- [Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)[^2_32]

## Sources

[^2_1]: https://www.youtube.com/watch?v=7JVrmSDVHW4

[^2_2]: https://www.linkedin.com/posts/robertohluna_revealing-my-ai-meeting-workflow-how-i-activity-7290101067038507009-wVKl

[^2_3]: https://www.make.com/en/integrations/apify/airtable

[^2_4]: https://blog.google/products/gemini/google-gemini-deep-research/

[^2_5]: https://ai-sdk.dev/providers/community-providers/openrouter

[^2_6]: https://www.youtube.com/watch?v=C3q2UZAaYgE

[^2_7]: https://www.relay.app/blog/google-calendar-automation

[^2_8]: https://gmelius.com/blog/gmail-workflow

[^2_9]: https://zapier.com/apps/airtable/integrations/apify

[^2_10]: https://automations.io/integrations/gmail/

[^2_11]: https://botize.com/en/app/telegrambot

[^2_12]: https://sendpulse.com/knowledge-base/chatbot/telegram/create-flow

[^2_13]: https://www.reddit.com/r/commandline/comments/181yu25/telegram_automation/

[^2_14]: https://www.zoom.com/en/products/workflow-automation/

[^2_15]: https://www.workato.com/integrations/zoom

[^2_16]: https://latenode.com/integrations/airtable/apify

[^2_17]: https://clickup.com/blog/google-sheets-automation/

[^2_18]: https://workspace.google.com/marketplace/app/sheet_automation_automate_google_sheets/250108887537

[^2_19]: https://matthiasfrank.de/en/notion-automations/

[^2_20]: https://www.digitalocean.com/resources/articles/what-is-perplexity-ai

[^2_21]: https://theresanaiforthat.com/ai/tavily/

[^2_22]: https://www.futuretools.io/tools/tavily

[^2_23]: https://blog.tavily.com/companyresearcher/

[^2_24]: https://play.google.com/store/apps/details?id=net.papirus.androidclient\&hl=en

[^2_25]: https://pyrus.com/en

[^2_26]: https://pyrus.com/en/workflows

[^2_27]: https://apps.apple.com/us/app/pyrus-team-communication/id385251753

[^2_28]: https://www.getapp.com/project-management-planning-software/a/pyrus/

[^2_29]: https://en.wikipedia.org/wiki/Pyrus_(software)

[^2_30]: https://www.linkedin.com/posts/n8n_leon-van-zyl-just-dropped-a-great-tutorial-activity-7355869766609162240-mD2Y

[^2_31]: https://brunswickai.net/2023/08/01/exploring-ai-automation-with-leon-van-zyl-build-applications-without-writing-code/

[^2_32]: https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research

[^2_33]: https://clickup.com/blog/google-calendar-automations/

[^3_1]: https://thedigitalprojectmanager.com/tools/make-pricing/

[^3_2]: https://nicksaraev.com/n8n-vs-make-2025/

[^3_3]: https://www.youtube.com/watch?v=Am54LhN2NLk

[^3_4]: https://zeabur.com/blogs/n8n-pricing-shift-self-hosting-business-costs-zeabur-guide

[^3_5]: https://www.trustradius.com/products/pipedream/pricing

[^3_6]: https://pipedream.com/pricing

[^3_7]: https://www.g2.com/products/relay-app/pricing

[^3_8]: https://www.getapp.com/customer-service-support-software/a/relay/

[^3_9]: https://www.activepieces.com/blog/zapier-pricing

[^3_10]: https://www.digidop.com/blog/n8n-vs-make-vs-zapier

[^3_11]: https://www.relay.app/blog/n8n-vs-zapier

[^3_12]: https://www.reddit.com/r/automation/comments/1jd4hxv/what_are_the_best_nocode_automation_platforms/

[^3_13]: https://www.ikigaiteck.io/best-automation-tools-zapier-make-n8n-pipedream-compared

[^3_14]: https://www.vellum.ai/blog/best-n8n-alternatives

[^4_1]: https://thedigitalprojectmanager.com/tools/make-pricing/

[^4_2]: https://nicksaraev.com/n8n-vs-make-2025/

[^4_3]: https://aihungry.com/tools/relevance-ai/pricing

[^4_4]: https://www.eesel.ai/blog/relevance-ai-pricing

[^4_5]: https://smythos.com/developers/agent-comparisons/n8n-vs-relevance-ai/

[^4_6]: https://www.youtube.com/watch?v=WUyzLD0FPnM

[^4_7]: https://relevanceai.com/blog/the-definitive-guide-understanding-ai-agents-vs-ai-workflows

[^4_8]: https://www.lindy.ai/blog/relevanceai-vs-n8n

[^4_9]: https://www.whalesync.com/blog/best-ai-workflow-automation-tools-2025

[^4_10]: https://www.autonoly.com/comparison/relevance

[^4_11]: https://www.digidop.com/blog/n8n-vs-make-vs-zapier

[^4_12]: https://relevanceai.com/agent-templates-tasks/workflow-automation-ai-agents

[^4_13]: https://www.youtube.com/watch?v=dnksJk8daac
