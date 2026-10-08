# Job Search Autopilot

A cloud-based job search assistant. Everything lives in one reserved Google Drive folder, **JobApplications_claude**: a README, a **Data** folder with information about you (Profile, Legend, Writing Style), CVs, cover letters, review docs and an application tracker. Nothing is stored on your computer.

## What it does

| Skill | Say something like | What happens |
|-------|--------------------|--------------|
| setup-autopilot | "Setup autopilot", "Check my connections" | Checks Google Drive, Docs, Sheets and Gmail connectors and offers Connect buttons for missing ones, checks Claude in Chrome and gives the install link (https://claude.ai/chrome) if it is not set up, checks job board sign-ins and the Drive workspace. Start here. |
| job-search-setup | "Set up my job search" | Creates the Drive folder with a README, a Data folder (Profile, Legend, Writing Style), Tracker (Settings, Applications, Vacancies, Skipped, Runs) and CVs, Cover Letters and Batch Reviews folders. Imports your existing CV and application log. Offers a daily schedule. |
| cv-builder | "Build my CV", "Tailor my CV for this job" | Builds a formatted Google Doc CV from your Profile, tailored versions per vacancy, PDF exports. |
| vacancy-scout | "Find new vacancies" | Scans your boards, scores fit 1 to 5, removes duplicates and blocked companies, fills the Vacancies tab. |
| apply-assistant | "Apply to 10 vacancies", "Apply to this job" | Writes letters and recruiter answers in your style, makes a review doc, submits after approval or automatically in auto mode, logs every send. |
| linkedin-assistant | "Check LinkedIn messages", "Easy Apply to this job", "Find the recruiter", "Review my LinkedIn profile" | Easy Apply with your Profile and Legend, drafts replies to recruiter messages and updates statuses, finds recruiters and hiring managers and drafts connection notes, compares your LinkedIn profile with Profile and suggests edits. Messages, connection requests and profile edits always wait for your ok. |
| reply-tracker | "Check replies" | Reads recruiter emails in Gmail and updates each application's status, checks your calendar for proposed interview slots and adds confirmed interviews after you approve. Shows pipeline stats. |
| daily-autopilot | runs on a schedule | Track replies, scout, draft, submit or prepare for review, log the run, send you a summary. |

## Modes

- **review** (default): it prepares everything and submits only after you say ok.
- **auto**: it submits by itself, but only for strong matches (fit at or above `auto_min_fit`) with inline apply forms and truthful answers for every field, up to `daily_quota` per day. Everything else waits for your approval. It never replies to recruiters for you.

Switch any time in the Tracker's Settings tab, or say "run in auto mode today".

## Getting started

1. Install the plugin.
2. Say "setup autopilot". It checks every connection and tells you what to connect.
3. Say "set up my job search" to create your Drive workspace and import your CV.

## Requirements

- Connectors: **Google Drive**, **Google Docs**, **Google Sheets** (required); **Gmail** (reply tracking and summaries) and **Google Calendar** (interview scheduling) recommended. See CONNECTORS.md in the repository root.
- A browser signed in to your job boards for submitting: Claude in Chrome (default, uses your own Chrome and sign-ins) or the Claude desktop app's built-in browser. Pick it with `browser` in Settings. Scanning works without it.
- For scheduled runs that submit, your computer must be on with the Claude desktop app open.

## Customize

- **Facts:** edit Profile and Legend in the Data folder. Keep `salary_expectation` in Settings in sync with Legend. Every letter is built only from them.
- **Tone and language rules:** edit the Writing Style doc. It always wins over built-in defaults.
- **Filters, boards, quota, mode:** edit the Settings tab.
- **New job board:** add `skills/apply-assistant/references/boards/<board>.md` following the DOU, Djinni or LinkedIn presets, then add the board name to `boards` in Settings.
- **New letter language:** add `skills/apply-assistant/references/languages/<code>.md` (see `uk.md`).

## Sharing

Install from the marketplace repository (see the root README). Each person runs "setup autopilot" and "set up my job search" once; their data stays in their own Drive. Contributions are welcome: see CONTRIBUTING.md in the repository root.
