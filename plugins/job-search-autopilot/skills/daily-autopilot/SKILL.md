---
name: daily-autopilot
description: "This skill should be used when a scheduled task says 'run the job-search-autopilot daily-autopilot skill', or when the user asks to 'run my job search', 'do today's applications', 'run the autopilot', 'run the daily job search'. It runs the full cycle unattended on the 'JobApplications_claude' Drive workspace: track replies, scout vacancies, draft applications, submit in auto mode or prepare a review doc in review mode, log the run, and send a summary."
metadata:
  version: "0.5.0"
---

# Daily Autopilot

Run the whole job search cycle in one pass. Designed for scheduled, unattended sessions: do not wait for answers; record decisions in the Runs tab and the summary.

## Step 0: Load the workspace

Locate `JobApplications_claude` and read Settings (see `../job-search-setup/references/workspace-layout.md`). If the folder is missing, stop and send a summary saying setup is needed (job-search-setup). Read `mode` and `daily_quota`. A mode given in the trigger message overrides Settings for this run.

## Step 1: Track replies

Run the reply-tracker skill. Keep its "action needed" list for the summary.

If `linkedin` is in `boards`, also run linkedin-assistant in its daily-autopilot mode (read LinkedIn messages, update statuses, put reply drafts in the review doc; never send).

## Step 2: Scout

Run the vacancy-scout skill for every board in `boards`.

## Step 3: Draft

Run apply-assistant steps 1 to 4 (pick targets, re-check duplicates, draft, create the review doc) for up to `daily_quota` shortlisted vacancies.

## Step 4: Submit or hand over

- `mode = review`: do not submit. The review doc is the hand-over. The person approves later in a normal conversation ("approve today's review"), and apply-assistant submits and logs.
- `mode = auto`: submit every vacancy passing all auto-mode guardrails in apply-assistant, logging each immediately. Everything else stays in the review doc as "needs approval".
- If no signed-in browser is reachable (computer asleep or app closed), switch this run to review behavior and say so in the summary.

## Step 5: Log the run

Append to the Runs tab: `Run At, Mode, Found, Shortlisted, Drafted, Submitted, Failed, Replies Updated, Review Doc link, Notes`.

## Step 6: Summary

Send the summary with SendUserMessage. When `notify_email` is set and Gmail is connected, also email it to that address with the subject `Job search run <YYYY-MM-DD>`. That email to the person's own address is the only email this skill sends on its own.

Summary content:
1. Action needed first: interviews, test tasks, approvals waiting (with the review doc link).
2. Today: found, shortlisted, submitted (company and role list), failed with reason.
3. Pipeline: response rate and counts from reply-tracker.

## Safety

- Never exceed `daily_quota` submissions per day, counting earlier runs the same day from the Applications tab.
- Never send recruiter inbox replies or emails on the person's behalf (except the summary to themselves).
- Never change Settings, Profile, Legend or Writing Style during an unattended run. Suggest changes in the summary instead.
- On any repeated error with a board (sign-in wall, rate limit), stop that board for the day and report it.
