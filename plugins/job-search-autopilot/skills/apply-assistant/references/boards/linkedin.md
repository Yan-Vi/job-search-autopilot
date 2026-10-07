# Board preset: LinkedIn Jobs

## Search

- Search: `https://www.linkedin.com/jobs/search/?keywords=<role>&location=<location>&f_TPR=r604800` (last 7 days). Remote: add `&f_WT=2`.
- Vacancy URL: `https://www.linkedin.com/jobs/view/<job-id>/`. Vacancy ID is the number.
- LinkedIn needs a signed-in browser for reliable listing and applying. WebFetch often hits a sign-in wall.

## Apply

- `Easy Apply`: inline. Multi-step modal; fill each step from Profile, Legend and the answer bank. Review the final step before `Submit application`.
- `Apply` (external): employer site, counts as `external` (review mode only).
- Easy Apply often asks for a CV upload; if the stored resume on LinkedIn is not the current version, stop and ask the person.

## Success signals

- Confirmation `Your application was sent` or the job shows `Applied`.

## Blockers

| Symptom | Action |
|---------|--------|
| Sign-in or security check | Ask the person to sign in |
| Daily Easy Apply limit message | Stop LinkedIn for the day |
| Questions with no truthful answer | Review mode, ask the person |
