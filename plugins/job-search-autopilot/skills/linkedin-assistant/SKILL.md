---
name: linkedin-assistant
description: "This skill should be used when the user asks to 'apply on LinkedIn', 'Easy Apply', 'check LinkedIn messages', 'reply to recruiters on LinkedIn', 'find the recruiter for this job', 'write a connection note', 'reach out to the hiring manager', 'review my LinkedIn profile' or 'tune my LinkedIn', or when daily-autopilot reaches the LinkedIn inbox step. It handles LinkedIn Easy Apply, recruiter messages, outreach and profile tuning using the 'JobApplications_claude' Drive workspace, and logs everything to the Tracker."
metadata:
  version: "0.5.0"
---

# LinkedIn Assistant

Everything on LinkedIn that vacancy-scout does not cover: Easy Apply, recruiter messages, outreach and profile tuning. Reads and writes only the `JobApplications_claude` workspace.

## Before starting

1. Locate the workspace and read Settings, the `Data/` docs (Profile, Legend, Writing Style) and the Applications and Vacancies tabs (see `../job-search-setup/references/workspace-layout.md`).
2. Read `../apply-assistant/references/boards/linkedin.md` and `../apply-assistant/references/answer-bank.md`.
3. Use the browser named in Settings `browser` (`chrome` = Claude in Chrome, `built-in` = Claude desktop app browser). Open LinkedIn in a new tab. On a sign-in wall, stop and ask the person to sign in. Never enter passwords.
4. Work at human pace: one page at a time, no bulk scraping. LinkedIn restricts automated accounts; on any warning, captcha, security check or limit message, stop LinkedIn for the day and report.

## Approval rule

Every LinkedIn **message, InMail, connection request and profile edit** needs explicit approval of that exact text ("ok", "yes", "send", "так", "відправляй"), in both `review` and `auto` mode. Only Easy Apply submits may run without approval, and only in `auto` mode within apply-assistant guardrails.

The day's total of Easy Apply submits plus sent outreach stays under `daily_quota`, counting earlier runs from the Applications tab and Runs notes.

## Mode 1: Easy Apply

1. Targets: Vacancies rows with `Platform = linkedin`, `Apply Type = easy_apply` and `Status = shortlisted`, or a LinkedIn job URL the person names.
2. Re-check duplicates against Applications by company and role on every platform, right before drafting. Skip Settings blocklists.
3. Open the job, start Easy Apply and read every step before filling.
4. Fill only from Profile, Legend, Settings and the answer bank:
   - Resume: the uploaded LinkedIn resume matching Settings `cv_label`. If none matches, stop and give the PDF link from `CVs/`.
   - Years per tool: only when Profile or Legend states them. Otherwise leave it for the person in the review doc.
   - Salary: Settings `salary_expectation` only; check the field right before submit.
   - Free-text questions and notes: per Writing Style, 3 to 5 vacancy skills that Profile proves.
5. Follow apply-assistant for the review doc (review mode) or guardrails (auto mode).
6. Snapshot before `Submit application`; confirm `Your application was sent` or `Applied`.
7. Log immediately to Applications (`Platform = linkedin`, `Result = sent`, exact text in Cover Letter). Set vacancy `Status = applied`. Never log an unconfirmed submit.
8. An external `Apply` redirect: set `Apply Type = external` on the vacancy and hand it to apply-assistant.

## Mode 2: Recruiter messages

1. Open LinkedIn Messaging. Read unread threads and threads with new replies since the last check (Runs notes).
2. Match each recruiter thread to an Applications row by company, and by role when stated. No row means inbound outreach.
3. Classify: interview invite, info request (salary, availability, English, CV), test task, rejection, offer, cold outreach, spam.
4. Draft a reply in the thread's language per Writing Style, with Legend standard answers and Settings `salary_expectation`. Blocked companies or domains get a short polite decline draft (iGaming only when the person says it is interview practice).
5. Show drafts together (in the review doc when more than 3). Send each only after approval.
6. Update Applications: `Result` (`hr interview`, `tech interview`, `test task`, `reject`, `offer`, `viewed`), plus a dated line in Notes. Inbound outreach the person wants to pursue gets a new row with `Result = sent` only after a reply is actually sent, and the thread link in Notes.
7. Never accept invites, share contacts beyond Profile, or send files without approval.

## Mode 3: Outreach

1. Input: a vacancy (URL or Vacancies row) or a company the person names.
2. Find up to 3 people from what LinkedIn shows: the job poster, a recruiter or talent partner, and a QA or engineering manager. Do not collect emails or phone numbers.
3. Draft a connection note (max 300 characters) or a message if already connected: the role, 2 to 3 Profile-backed matches, a clear ask. No flattery, no invented facts, vacancy language.
4. Show each draft with the person's name and profile link. Send only after approval, one by one.
5. Log a dated line in the matching Applications or Vacancies Notes: `<date> outreach to <name>, <title>`. Outreach alone never creates an Applications row.

## Mode 4: Profile tuning

1. Open the person's own profile: headline, About, Experience, Skills, Featured, Open to Work.
2. Compare with Profile (source of truth) and Settings `target_roles`, `core_stack`, `locations`. Check that the headline names the target role and core stack, About matches the Profile summary, titles and dates match exactly, `core_stack` skills are in the top skills, nothing on LinkedIn is missing from Profile and no Profile highlight is missing from LinkedIn, and Open to Work titles and locations match Settings.
3. Create `LinkedIn profile review <YYYY-MM-DD>` (Google Doc) in the workspace root: current text, suggested text, reason. Suggestions use only Profile and Legend facts.
4. Edit LinkedIn only for approved items, one section at a time, and confirm each save.

## Inside daily-autopilot

Run Mode 2 steps 1 to 4 and 6 only (read, match, draft, update statuses). Put drafts in the day's review doc. Never send anything during an unattended run.

## Report

Applied (with links), waiting for approval, replies drafted or sent, Applications rows updated, outreach sent, anything stopped and why.

## Rules

- Profile and Legend are the only source of facts; use Legend `Honest gaps` wording for gaps.
- Writing Style wins; defaults: no em dashes, no slashes between words, no filler.
- Never enter passwords, solve captchas, create accounts or change Settings, Profile or Legend.
