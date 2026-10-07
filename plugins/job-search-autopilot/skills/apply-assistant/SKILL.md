---
name: apply-assistant
description: "This skill should be used when the user asks to 'apply to this job', 'apply to N vacancies', 'prepare applications', 'write a cover letter for this vacancy', 'answer recruiter questions', 'bulk apply', 'reply to the recruiter', or when daily-autopilot reaches the apply step. It writes vacancy-specific letters and recruiter answers from Profile, Legend and Writing Style, builds a review doc, submits in review mode (after approval) or auto mode (within guardrails), and logs every submission to the Tracker in the 'JobApplications_claude' Drive workspace."
metadata:
  version: "0.4.1"
---

# Apply Assistant

Turn shortlisted vacancies into submitted, logged applications.

## Before starting

1. Locate the workspace. Read Settings, the `Data/` docs (Profile, Legend, Writing Style), and the Applications and Vacancies tabs (see `../job-search-setup/references/workspace-layout.md`).
2. Read the board preset in `references/boards/<platform>.md` for each platform in the batch.
3. Read `references/answer-bank.md` for recruiter question handling.
4. For each letter language other than English, check Writing Style for language rules. If none exist and a preset is available in `references/languages/`, apply it.

## Modes

Read `mode` from Settings unless the person states a mode for this request.

### review (default)

Never submit or send anything without explicit approval. Words like "apply", "submit" or "send" in the request mean prepare, not click. Approval is an explicit reply such as "ok", "yes", "send", "так", "відправляй".

### auto

Submit without asking, only when every guardrail passes. Any vacancy failing a guardrail falls back to review and goes into the review doc.

Guardrails:
- Fit is at least `auto_min_fit`.
- The vacancy passed all vacancy-scout filters and is not a duplicate on any platform.
- Apply is inline on the board (no external ATS, no account creation, no captcha, no required file upload).
- Every required form field can be answered truthfully from Profile, Legend or the answer bank. Salary fields use Settings `salary_expectation` (or Legend standard answers) only, and the value shown in the form right before submit must match it.
- The day's submitted count stays under `daily_quota`.
- Never auto-send replies in recruiter inbox threads. Those always need approval.

## Steps

1. **Pick targets.** Take vacancies with `Status = shortlisted`, newest first, up to `daily_quota`, plus 2 to 3 alternates. For a single vacancy the person names, read it directly and run the same filters.
2. **Re-check duplicates** against Applications by company and role across all platforms, immediately before drafting.
3. **Draft.** For each target write the letter in the mode from `default_letter_mode` (or the person's request) and the vacancy language. Draft answers to known recruiter questions. Use only facts from Profile and Legend.
4. **Review doc.** Create `Review <YYYY-MM-DD> <platform or all>` in `Batch Reviews/` using `references/review-doc.md`. Set vacancy `Status = drafted`.
5. **Approve (review mode)** by sharing the review doc link and a short summary. Apply edits the person asks for, then ask again. In auto mode, skip this step for vacancies passing all guardrails.
6. **Submit** through the browser named in Settings `browser` (`chrome` = Claude in Chrome, `built-in` = the Claude desktop app browser; default `chrome`). If that browser is unreachable, use the other one only in review mode with the person present; in unattended runs, stop submitting and report. Follow the board preset. Fill fields, take a snapshot before clicking submit, and confirm the success signal the preset lists.
7. **Log immediately** after each confirmed submit: append to Applications (`Date, Company, Role, URL, Platform, CV, Result=sent, External URL, Cover Letter, Notes`), using the exact submitted text. Set vacancy `Status = applied`. Save the letter Doc in `Cover Letters/` when the letter is longer than a short form message.
8. **Report** submitted, waiting for approval, failed with reason, and the review doc link.

## Failure handling

- Browser or connector missing: run the setup-autopilot checks for that tool and show the fix (Claude in Chrome install link: https://claude.ai/chrome).

- Sign-in wall: stop that board and tell the person to sign in in the browser. Do not try to sign in for them.
- Required CV upload: fill everything else, stop, give the PDF link from `CVs/`, and ask the person to attach and submit. Log only after they confirm it was sent.
- Captcha, passkey or new account: stop and leave it in the review doc as manual.
- Disabled submit button: re-read the form, check required fields once, then stop and report.
- Never log a vacancy that was not confirmed as sent.

## Writing rules (always)

Writing Style overrides everything here. Defaults when Writing Style is silent:
- Vacancy-specific: name 3 to 5 skills from the vacancy that Profile proves.
- No invented tenure, tools, domains or numbers. For an honest gap, use the Legend `Honest gaps` wording.
- No em dashes, no filler, no slashes between words.
