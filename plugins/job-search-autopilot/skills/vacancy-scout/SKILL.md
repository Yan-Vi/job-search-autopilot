---
name: vacancy-scout
description: "This skill should be used when the user asks to 'find vacancies', 'scan job boards', 'look for new jobs', 'what's new on DOU/Djinni/LinkedIn', 'refresh the vacancy list', or when daily-autopilot runs. It collects listings from the boards in Settings, scores fit against Profile, removes duplicates and blocked companies, and writes results to the Vacancies tab of the Tracker in the 'JobApplications_claude' Drive workspace."
metadata:
  version: "0.5.0"
---

# Vacancy Scout

Find fresh vacancies, score them, and keep the Vacancies tab current. Do not apply or write letters here.

## Before starting

1. Locate the workspace and read Settings, Profile and the Applications, Vacancies and Skipped tabs (see `../job-search-setup/references/workspace-layout.md`).
2. Read the board preset for each board in `boards` from `../apply-assistant/references/boards/<board>.md`. For a board with no preset, use `search_urls` from Settings and generic page reading.

## Collect

For each board:

1. Build search URLs from the preset, `target_roles`, `locations` and any `search_urls`.
2. Read listing pages with WebFetch first. Use a browser only when the page needs sign-in or does not render (the preset says which). Follow pagination until listings are older than 14 days or 5 pages, whichever comes first.
3. For each listing capture: platform, vacancy ID (from the URL), company, title, URL, published date, location, remote, salary, apply type (inline or external).
4. Open the vacancy page for shortlisted candidates only, to read requirements.

## Deduplicate

- Key is `Platform` + `Vacancy ID`. Update `Last Seen` and changed fields on existing rows. Never touch `Status`, `Fit` or `Skip Reason` of existing rows unless the vacancy closed (`Status = closed`).
- Cross-platform duplicate: same company and same or clearly overlapping role title already in Applications (any platform). Mark `skipped` with reason `already applied on <platform>`. Different roles at the same company are fine.

## Filter

Mark `skipped` with a reason when any rule hits:

- Company in `blocklist_companies`, or domain in `blocklist_domains`.
- Seniority outside `seniority`.
- Location or work format outside `locations`.
- Visible salary below `min_salary`.
- Vacancy closed, archived or with no apply option.
- Board-specific blockers from the preset (e.g. platform experience filters).

Log every skip to the Skipped tab as well.

## Score fit (1 to 5)

| Score | Meaning |
|-------|---------|
| 5 | Title matches `target_roles`, most `core_stack` items required, domain known from Profile |
| 4 | Title matches, core stack largely matches, some gaps |
| 3 | Adjacent role or half the stack matches |
| 2 | Weak match, mostly different stack |
| 1 | Unrelated |

Set `Status = shortlisted` for fit 3 and above that pass filters; `new` otherwise. Sort shortlist by `Published` descending, then fit.

## Write and report

- Write new and updated rows to the Vacancies tab in one batch (`append_values` for new, `update_values` for changed rows).
- Report: found, new, shortlisted, skipped by reason, and the top 10 shortlisted with fit and link.
