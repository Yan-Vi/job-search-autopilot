# Board preset: DOU (jobs.dou.ua)

## Search

- List: `https://jobs.dou.ua/vacancies/?category=<category>` (e.g. `QA`, `Python`, `Front End`). Add `&remote` for remote only. Search: `https://jobs.dou.ua/vacancies/?search=<query>`.
- Pagination: DOU loads more with a "More vacancies" button; with WebFetch, also try the RSS feed `https://jobs.dou.ua/vacancies/feeds/?category=<category>`.
- Vacancy URL: `https://jobs.dou.ua/companies/<company-slug>/vacancies/<vacancy-id>/`. Vacancy ID is the number.
- Listing pages render without sign-in (WebFetch works). Applying needs a browser signed in to DOU.

## Apply

1. Open the vacancy page. The apply control is `Відгукнутися` or `Відгукнутися на вакансію`.
2. Check whether the response stays on DOU (inline form) or opens the employer site (external). External counts as `external` for auto-mode guardrails.
3. Inline: fill the message field. If the form requires a CV file (`Прикріпіть резюме`), stop and ask the person to attach the PDF from `CVs/`.
4. Submit button: `Відправити`.

## Success signals

- URL contains `?sent`, or the page shows a sent confirmation.
- External: employer confirmation page.

## Logging

- `URL`: DOU vacancy URL (with `?sent` if shown).
- `External URL`: employer apply URL when submit happened off DOU.

## Blockers

| Symptom | Action |
|---------|--------|
| No apply button | Archived or already applied: mark `closed` or check Applications |
| Login wall | Ask the person to sign in |
| Existing recruiter thread for this role | Do not re-apply; reply in the thread (approval required) |
| External captcha or account creation | Manual |
