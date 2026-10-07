# Job Search Autopilot

A Claude plugin that runs your job search from one Google Drive folder: it keeps your profile and CVs, finds vacancies on DOU, Djinni and LinkedIn, writes cover letters in your style, applies (with your approval or automatically), and tracks recruiter replies in Gmail.

Nothing personal lives in this repository. Each user's data stays in their own Google Drive.

## Install

**Claude app (web or desktop):** Customize → Plugins → Add → Add marketplace → enter `OWNER/job-search-autopilot`, then install **job-search-autopilot**.

**Claude Code:**

```bash
claude plugin marketplace add OWNER/job-search-autopilot
claude plugin install job-search-autopilot@job-search-autopilot
```

Then in a chat, say **"setup autopilot"**. It checks your connections (Google Drive, Docs, Sheets, Gmail, Google Calendar, Claude in Chrome) and tells you what to connect. After that, say **"set up my job search"**.

What each connection is for and how to connect it: [CONNECTORS.md](CONNECTORS.md).

See [the plugin README](plugins/job-search-autopilot/README.md) for skills, modes and settings.

## Repository layout

```text
.claude-plugin/marketplace.json        marketplace catalog
plugins/job-search-autopilot/
  .claude-plugin/plugin.json           plugin manifest (version lives here)
  README.md                            user guide
  skills/
    setup-autopilot/                   connection checks
    job-search-setup/                  Drive workspace and import
      references/workspace-layout.md   folder, docs and Tracker layout (shared by all skills)
    cv-builder/                        CVs and letters as Google Docs
      scripts/build_cv_doc.py          CV layout to Google Docs batchUpdate
    vacancy-scout/                     find and score vacancies
    apply-assistant/                   letters, review doc, submit, log
      references/boards/               job board presets (dou, djinni, linkedin)
      references/languages/            letter language presets (uk)
    reply-tracker/                     Gmail status tracking
    daily-autopilot/                   scheduled full cycle
```

## Contributing

New services: see the contributor notes in [CONNECTORS.md](CONNECTORS.md#for-contributors).

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
