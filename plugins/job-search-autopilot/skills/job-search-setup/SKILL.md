---
name: job-search-setup
description: "This skill should be used when the user says 'set up my job search', 'create my job search folder', 'set up job-search-autopilot', 'import my CV', 'move my applications to Drive', or when any other job-search-autopilot skill cannot find the 'JobApplications_claude' folder in Google Drive. It creates the reserved Google Drive workspace with its pre-baked structure, imports existing CVs, letters and application logs, and optionally schedules the daily autopilot."
metadata:
  version: "0.4.1"
---

# Job Search Setup

Create one reserved Google Drive workspace per person. Every other skill in this plugin reads and writes only inside it, so nothing is stored on the person's computer.

## Requirements

- Google Drive, Google Docs and Google Sheets connectors connected. If any is missing, run the setup-autopilot checks and show the person how to connect it.
- Gmail connector (optional): needed only for reply tracking and run summaries.

## Step 1: Find or create the root folder

1. Search Drive: `title = 'JobApplications_claude' and mimeType = 'application/vnd.google-apps.folder' and owner = 'me'`.
2. If found, read its **Tracker** spreadsheet's `Settings` tab and report what already exists. Create only the missing pieces. Never overwrite existing files.
3. If not found, create the folder in My Drive root.

## Step 2: Create the pre-baked structure

Create exactly this layout. Profile, Legend and Writing Style always go inside `Data/`. The full contents for each file are in `references/workspace-layout.md`.

```
JobApplications_claude/
├── README                 (Google Doc)  what the folder is, layout, how to use, modes, rules
├── Data/                  information about the person; the only source of facts
│   ├── Profile            (Google Doc)  master facts: experience, skills, education, contacts
│   ├── Legend             (Google Doc)  stories, motivations, standard answers, honest gaps, preferences
│   └── Writing Style      (Google Doc)  tone and language rules for letters and answers
├── job_applications.csv    (original application log, uploaded unchanged if the person has one)
├── Tracker                (Google Sheet) tabs: Settings, Applications, Vacancies, Skipped, Runs
├── CVs/                   master CV + tailored versions (Google Docs, PDF exports)
├── Cover Letters/         one Google Doc per company and role
└── Batch Reviews/         daily review docs for approval before submit
```

- Create Google Docs with `create_file` using `contentMimeType: text/html` and HTML content, so headings and bold text carry over.
- Create the Tracker by uploading CSV for the first tab, then add the other tabs with `update_spreadsheet` (addSheet) and fill headers with `update_values`.
- Use the headers from `references/workspace-layout.md` exactly. Other skills depend on the column order.

## Step 3: Fill the Settings tab

Ask the person for the values below with AskUserQuestion. Group them into at most two rounds. Offer sensible defaults and the free-text option.

| Key | Meaning | Default |
|-----|---------|---------|
| `target_roles` | Role titles to search for | from Profile title |
| `core_stack` | Must-match skills and tools | from Profile skills |
| `boards` | Comma list of board presets | `linkedin` |
| `search_urls` | Optional custom search URLs per board | empty |
| `locations` | Remote, countries, cities | `remote` |
| `min_salary` | Skip listings with a visible salary below this | empty |
| `salary_expectation` | Figure used in every salary field, e.g. `$4000 per month gross` | ask; never guess |
| `blocklist_companies` | Never apply | empty |
| `blocklist_domains` | Industries to skip (e.g. dating, gambling) | empty |
| `seniority` | Allowed levels | `middle, senior` |
| `letter_languages` | Languages letters may be written in | `en` |
| `default_letter_mode` | `default` or `short` | `default` |
| `mode` | `review` or `auto` (see daily-autopilot) | `review` |
| `daily_quota` | Max applications per run | `10` |
| `auto_min_fit` | Minimum fit score 1 to 5 for auto submit | `4` |
| `cv_label` | Version label logged per application | `v1` |
| `notify_email` | Where run summaries go | the person's Gmail |
| `browser` | `chrome` (Claude in Chrome, the person's own Chrome and sign-ins) or `built-in` (Claude desktop app browser) | `chrome` |

Write one key per row: column A key, column B value, column C a short note.

## Step 4: Import existing material (if any)

Ask whether the person has an existing CV, letters or application log. Accept any of:

- A CV in .docx, .pdf, JSON or plain text: extract facts into **Profile** and lay Profile out like the CV with cv-builder `scripts/build_cv_doc.py`, and recreate the CV as a Google Doc in `CVs/` with cv-builder.
- Interview notes or stories: move them into **Legend**. Put a salary expectation into both Legend `Standard answers` and the Settings `salary_expectation` key.
- An applications CSV or spreadsheet: upload the original file unchanged to the root as `job_applications.csv` (`create_file`, `contentMimeType: text/csv`, `disableConversionToGoogleType: true`), then download it and confirm the checksum matches the source. Then map columns to the Applications tab (`Date, Company, Role, URL, Platform, CV, Result, External URL, Cover Letter, Notes`). Fill `Platform` from the URL host. Keep every row. Report the row count before and after; they must match.
- A vacancy database: copy rows into the Vacancies tab.
- Writing rules or existing apply instructions: move tone and language rules into **Writing Style**, and filters into Settings.

Files can come from the chat (attachments), from a folder on the person's computer if linked, or from Drive. After import, tell the person the local copies are no longer needed, but never delete them.

## Step 5: Offer the daily schedule

Offer to create a scheduled task that runs the daily-autopilot skill on weekdays. Ask for the time and confirm the time zone. The scheduled task prompt must be standalone: "Run the job-search-autopilot daily-autopilot skill for the JobApplications_claude workspace in my Google Drive." Note that submitting applications needs a browser session that is signed in to each board, which requires the person's computer to be online.

## Step 6: Verify and report

- Re-list the folder and confirm every item in the layout exists.
- Read back the Settings tab.
- Give the person links to the folder, README, Profile, Writing Style and Tracker, and suggest they review Profile first, since every letter is built from it.
- Write the README last, from the template in `references/workspace-layout.md`, filled with the person's name, boards and mode.

## Rules

- Store everything in the reserved folder. Never write job-search files to the local computer.
- Keep facts in Profile and Legend true to what the person provided. Never invent experience, numbers or tools.
- Do not share the folder with anyone unless the person asks.
