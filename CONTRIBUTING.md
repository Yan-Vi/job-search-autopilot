# Contributing

Thanks for helping. Most contributions are plain Markdown: skills are instructions for Claude, not code.

## Good first contributions

- **A new job board:** add `plugins/job-search-autopilot/skills/apply-assistant/references/boards/<board>.md`. Copy the structure of `dou.md` or `djinni.md`: Search (list URLs, pagination, vacancy ID format, whether sign-in is needed), Apply (buttons, form fields, file upload), Success signals, Logging, Blockers.
- **A new letter language:** add `.../apply-assistant/references/languages/<code>.md` (see `uk.md`): openings, closings, terms to translate, terms to keep in English.
- **Fixes to board presets** when a site changes its buttons or URLs.
- **New connections:** follow [CONNECTORS.md](CONNECTORS.md#for-contributors) and add the check to setup-autopilot.
- **New skills** under `plugins/job-search-autopilot/skills/<name>/SKILL.md`.

## Rules for skill files

- Frontmatter needs `name` (matches the folder) and `description`.
- `description`: one line, third person ("This skill should be used when..."), with the phrases a user would say. **No angle brackets** (`<` or `>`) anywhere in it; the installer rejects them.
- Write the body as instructions for Claude, imperative ("Read Settings", not "You should read Settings").
- Keep `SKILL.md` under about 2,000 words; put long material in `references/`.
- Shared layout facts live in `skills/job-search-setup/references/workspace-layout.md`. Change folder, doc or column names there and in every skill that uses them.
- No personal data: no real names, emails, salaries or CV content in examples.
- Safety rules stay: never submit without approval in review mode, never type passwords, never send recruiter replies on the user's behalf without approval.

## Before opening a pull request

1. Validate:

   ```bash
   claude plugin validate ./plugins/job-search-autopilot
   claude plugin validate .
   ```

2. Test locally:

   ```bash
   claude plugin marketplace add ./
   claude plugin install job-search-autopilot@job-search-autopilot
   ```

   Then try the skill you changed in a real chat.

3. Bump `version` in `plugins/job-search-autopilot/.claude-plugin/plugin.json` (patch for fixes, minor for new skills or boards) so users receive the update.

4. In the pull request, say what you changed and how you tested it.

## Questions and ideas

Open an issue.
