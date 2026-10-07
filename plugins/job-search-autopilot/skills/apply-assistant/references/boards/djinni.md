# Board preset: Djinni (djinni.co)

## Search

- List: `https://djinni.co/jobs/?primary_keyword=<keyword>` (repeat `primary_keyword` for several, e.g. `QA`, `QA Automation`). Pagination: `&page=2`.
- Vacancy URL: `https://djinni.co/jobs/<job-id>-<slug>/`. Vacancy ID is the leading number.
- Public listings render without sign-in. Applying needs a browser signed in as the candidate.
- If a list item click is blocked by an overlay, open the vacancy by direct URL.

## Apply

1. Open the vacancy. Apply button: `Відгукнутися на вакансію`.
2. Fill the cover letter and any recruiter questions. Djinni may autofill compensation from the profile; set it to Settings `salary_expectation`, re-read the field right before submit, and report any change. If autofill keeps overriding it, tell the person to update the salary in their Djinni profile.
3. Submit button: `Надіслати відгук`.

## Success signals

- URL contains `?applied=ok`, or the page shows `Відкрити діалог`.

## Before applying

- Check `https://djinni.co/my/inbox/` for an existing thread with the same company and role. If one exists, reply there instead (approval required).

## Blockers

| Symptom | Action |
|---------|--------|
| EU-only country warning, no apply button | Skip (location filter) |
| Platform minimum experience above profile | Skip |
| `Неактивна` on vacancy page | Mark `closed` |
| "You were offered this vacancy" with inbox thread | Reply in thread |
