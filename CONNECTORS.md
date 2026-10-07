# Connections

Job Search Autopilot works through connectors and a browser that each person sets up in their own Claude account. A plugin cannot carry anyone's sign-ins, and Claude's Google connectors and the Claude in Chrome extension cannot be bundled inside a plugin, so every user connects them once.

The easiest way: after installing, say **"setup autopilot"** in a chat. It checks everything below, shows Connect buttons for what is missing, and gives the Chrome extension link if needed.

## Required

| Connection | Why the plugin needs it | How to connect |
|------------|------------------------|----------------|
| **Google Drive** | Creates and finds the `JobApplications_claude` workspace, uploads files, exports PDFs | Claude: Customize → Connectors → Google Drive → Connect |
| **Google Docs** | Edits Profile, CVs, cover letters and review docs in place | Customize → Connectors → Google Docs → Connect |
| **Google Sheets** | Reads and writes the Tracker (Settings, Applications, Vacancies, Skipped, Runs) | Customize → Connectors → Google Sheets → Connect |

Without these three, nothing can be stored, because the plugin keeps all data in your Drive.

## Recommended

| Connection | Why | How to connect |
|------------|-----|----------------|
| **Claude in Chrome** (browser extension) | Submits applications and reads job board inboxes using your own Chrome and your existing sign-ins | Install from **https://claude.ai/chrome**, sign in to the extension with the same Claude account, keep Chrome open |
| **Gmail** | Reply tracking (reject, interview, offer) and run summaries to yourself | Customize → Connectors → Gmail → Connect |
| **Google Calendar** | Checks your free time when recruiters propose interview slots, and adds confirmed interviews and test-task deadlines to your calendar (only after you approve) | Customize → Connectors → Google Calendar → Connect |

Alternative to Claude in Chrome: the built-in browser in the Claude desktop app. Set `browser` to `built-in` in the Tracker's Settings tab. It works only while the desktop app is open.

## Optional

| Connection | Use |
|------------|-----|
| **Indeed** | Extra vacancy source for vacancy-scout, if you use Indeed |

## Job board sign-ins

The plugin never types passwords. Sign in yourself, once, in the browser the plugin uses:

- Djinni: https://djinni.co
- DOU: https://jobs.dou.ua
- LinkedIn: https://www.linkedin.com/jobs/

## Scheduled runs

The daily autopilot runs in the cloud. Scanning, drafting and reply tracking work any time. Submitting applications needs your computer on with Chrome (or the Claude desktop app) open; otherwise that run prepares a review doc instead.

## Privacy

Connectors act with your own account. Your CV, salary, letters and application history stay in your Google Drive. Nothing personal is stored in this repository.

## For contributors

If you add a feature that needs a new service:

1. Prefer a connector that already exists in Claude's directory, and add it to this file and to the checks in `plugins/job-search-autopilot/skills/setup-autopilot/SKILL.md`.
2. If the service publishes a public remote MCP server (an `https://` URL), you may bundle it in `plugins/job-search-autopilot/.mcp.json`:

   ```json
   {
     "mcpServers": {
       "service-name": { "type": "http", "url": "https://mcp.example.com/mcp" }
     }
   }
   ```

   Users then connect it from the plugin's Connectors tab and sign in with their own account. Never put API keys or tokens in the repository.
