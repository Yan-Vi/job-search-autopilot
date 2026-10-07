---
name: setup-autopilot
description: "This skill should be used when the user says 'setup autopilot', 'set up autopilot', 'check my connections', 'what do I need to connect', 'is everything connected', 'prepare job-search-autopilot', or the first time anyone uses the job-search-autopilot plugin. It also runs when another job-search-autopilot skill finds a required tool missing. It checks every connection the plugin needs (Google Drive, Docs, Sheets, Gmail, Claude in Chrome and sign-ins to job boards), offers to connect what is missing, gives the Claude in Chrome install link when the extension is not set up, and hands over to job-search-setup."
metadata:
  version: "0.4.1"
---

# Setup Autopilot

Check that everything the plugin needs is connected, fix what can be fixed in the chat, and tell the person exactly what to do for the rest. Run the checks silently, then report once.

## Step 1: Check connectors

Call `ListConnectors` (load it with ToolSearch if deferred) with keywords `["google drive", "google docs", "google sheets", "gmail", "google calendar"]`.

| Connector | Needed for | Required |
|-----------|-----------|----------|
| Google Drive | Workspace folder, files, PDF export | Yes |
| Google Docs | Profile, CVs, letters, review docs | Yes |
| Google Sheets | Tracker (Settings, Applications, Vacancies) | Yes |
| Gmail | Reply tracking and run summaries | Recommended |
| Google Calendar | Free-time checks for interview slots, adding confirmed interviews and deadlines | Recommended |

For each one, classify:
- **Ready:** `connected: true` and `enabledInChat: true`.
- **Turned off in this chat:** `connected: true`, `enabledInChat: false`. Tell the person to turn it on in this chat's connector settings (the "+" menu next to the message box, then Connectors).
- **Not connected:** missing or `connected: false`. Call `SearchMcpRegistry` with the connector name, then `SuggestConnectors` with the matching `directoryUuid` values so the person gets Connect buttons. Put all missing connectors in one `SuggestConnectors` call.
- **Unknown:** `connected: null`. Try one harmless read (for example Drive `search_files` with `title = 'JobApplications_claude'`). If it works, treat it as ready.

## Step 2: Check the browser

The plugin submits applications through a browser that is signed in to the job boards. Settings `browser` decides which (`chrome` by default).

### Claude in Chrome

1. Look for `mcp__claude-in-chrome__*` tools (ToolSearch with `+claude-in-chrome tabs`). If only `enable__mcp__claude-in-chrome` exists, call it first.
2. Call `mcp__claude-in-chrome__tabs_context_mcp` with `createIfEmpty: true`.
3. If the tools are absent, or the call says the extension is not connected, Claude in Chrome is not set up. Tell the person:
   - Install the extension: **https://claude.ai/chrome**
   - Sign in to the extension with the same Claude account used here.
   - Keep Chrome open on the computer, then say "check again".
4. If it works, close any tab this check created.

### Built-in browser (alternative)

If the person prefers not to install the extension, or Settings `browser` is `built-in`, check for `mcp__Claude_Browser__*` or `mcp__remote-devices__Claude_Browser__*` tools (read the built-in-browser skill first). It is available only while the Claude desktop app is open on their computer. Offer to set Settings `browser` to whichever one works.

### Job board sign-ins

With a working browser, open each board in Settings `boards` (default `dou, djinni, linkedin`) in a new tab and check whether the person is signed in:

| Board | Page to open | Signed in when |
|-------|-------------|----------------|
| Djinni | https://djinni.co/my/inbox/ | The inbox loads and shows the person's name, not a login form |
| DOU | https://jobs.dou.ua/ | The header shows the person's avatar or name, not "Вхід" or "Log in" |
| LinkedIn | https://www.linkedin.com/jobs/ | The jobs feed loads with the profile card |

Only look. Never type passwords or sign in for the person. For a board that is signed out, ask them to sign in themselves in that browser. Close the tabs you opened.

## Step 3: Check the workspace

Search Drive for the `JobApplications_claude` folder.
- Found: list what is in it (Data docs, Tracker, folders) and note anything missing from the layout in `../job-search-setup/references/workspace-layout.md`.
- Not found: offer to run job-search-setup.

## Step 4: Report

Send one checklist, ready items first, then what needs action:

```
Ready
- Google Drive, Google Docs, Google Sheets
- Claude in Chrome, signed in to Djinni and LinkedIn
- Workspace: JobApplications_claude

Needs you
- Gmail: connect it with the button above (needed for reply tracking)
- Google Calendar: connect it with the button above (needed for interview scheduling)
- DOU: sign in at jobs.dou.ua in Chrome
```

Then give the single next step:
- Required connector missing: connect it, then say "check again".
- Everything required ready, no workspace: offer job-search-setup.
- Everything ready: offer to find vacancies (vacancy-scout) or schedule the daily run (job-search-setup Step 5).

## Rules

- Run every check before reporting; do not report one item at a time.
- Do not install anything, change settings, or sign in to anything on the person's behalf. Only check, suggest and link.
- Re-running this skill is safe; it only reads.
- When a later skill fails because a tool is missing, run this skill's checks for that tool only and show the fix.
