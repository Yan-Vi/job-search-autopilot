---
name: reply-tracker
description: "This skill should be used when the user asks to 'check replies', 'update application statuses', 'did anyone answer', 'track my applications', 'show my job search stats', or when daily-autopilot reaches the tracking step. It reads recruiter emails in Gmail, matches them to rows in the Applications tab of the Tracker in the 'JobApplications_claude' Drive workspace, updates Result, and reports pipeline stats."
metadata:
  version: "0.5.0"
---

# Reply Tracker

Keep the Applications tab's `Result` column current from Gmail, and summarize the pipeline.

## Before starting

1. Locate the workspace and read the Applications tab and the last row of the Runs tab (see `../job-search-setup/references/workspace-layout.md`).
2. Requires the Gmail connector. If missing, report pipeline stats only and suggest connecting Gmail.

## Scan Gmail

1. Search threads newer than the previous run (or 14 days on the first run). Build the query from company names with `Result` in `sent`, `viewed`, `hr interview`, `tech interview`, `test task`, plus board notification senders (e.g. `from:djinni.co`, `from:dou.ua`, `from:linkedin.com`).
2. For each thread, match to an application by company name, role title and board vacancy link. When several rows match, prefer the most recent `Date`. When nothing matches with confidence, list it as unmatched; do not guess.

## Classify

| Email signal | New Result |
|--------------|-----------|
| Rejection wording ("decided to move forward with other candidates", "на жаль") | `reject` |
| Invitation to a call with HR or recruiter | `hr interview` |
| Technical interview invite | `tech interview` |
| Test assignment | `test task` |
| Offer | `offer` |
| Board notification that the CV was viewed | `viewed` |

Only move Result forward (sent → viewed → interview stages → offer or reject). Never overwrite a later stage with an earlier one. Add a short dated note in `Notes` (e.g. `2026-10-06 HR call invite, slots Thu`).

## Calendar (when Google Calendar is connected)

- For interview invites with proposed slots, check the person's calendar and list which slots are free. Do not answer the recruiter.
- Offer to add a confirmed interview or a test-task deadline as a calendar event. Create the event only after the person approves, with company, role, call link and the application URL in the description.
- Never accept or decline invites on the person's behalf.

## Do not

- Do not reply to emails, accept invites or schedule calls. Draft a reply only when the person asks, and show it before sending.
- Do not mark anything as `no answer` automatically; suggest it for applications older than 21 days with no reply and let the person decide.

## Report

- Updated rows: company, role, old → new Result.
- Action needed: interviews and test tasks with dates or deadlines from the email.
- Pipeline: total sent, response rate, counts per Result, per platform, last 7 and 30 days.
- Unmatched emails that look job-related.
