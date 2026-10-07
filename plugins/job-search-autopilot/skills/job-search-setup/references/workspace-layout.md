# Workspace layout

Exact contents for every file `job-search-setup` creates. Other skills locate files by these names, so keep names unchanged.

## Locating the workspace (all skills)

1. Search Drive: `title = 'JobApplications_claude' and mimeType = 'application/vnd.google-apps.folder' and owner = 'me'`.
2. List children with `parentId = '<folder id>'` to get IDs for README, Tracker and the subfolders (Data, CVs, Cover Letters, Batch Reviews).
3. List children of `Data/` to get IDs for Profile, Legend and Writing Style. For older workspaces where these docs sit in the root, use them there.
4. Read Settings from the Tracker `Settings` tab (`Settings!A:C`).
5. If the folder does not exist, run job-search-setup first.

## Folder tree

```
JobApplications_claude/
├── README
├── Data/
│   ├── Profile
│   ├── Legend
│   └── Writing Style
├── job_applications.csv   (original application log, kept as uploaded)
├── Tracker
├── CVs/
├── Cover Letters/
└── Batch Reviews/
```

## Data/Profile (Google Doc)

Laid out exactly like the CV (centered name, gray title, contact line with a dark rule, section headers with gray rules, two-column company and dates rows, bold-label bullets, two-column skills table), plus KEY FACTS and CERTIFICATES sections. Build it with cv-builder `scripts/build_cv_doc.py` (in place, same link). The HTML below is the fallback for a first draft.

```html
<h1>Profile</h1>
<p><i>Source of truth for every CV and letter. Keep facts real and specific.</i></p>
<h2>Header</h2>
<p><b>Name:</b> </p><p><b>Title:</b> </p><p><b>Location:</b> </p>
<p><b>Email:</b> </p><p><b>Phone:</b> </p><p><b>LinkedIn:</b> </p><p><b>Portfolio / GitHub:</b> </p>
<h2>Summary</h2><p></p>
<h2>Key facts</h2>
<ul><li>Years in the field: </li><li>Main stack: </li><li>Also used: </li><li>Domains: </li><li>Languages spoken: </li></ul>
<h2>Experience</h2>
<h3>Company · Location · Title · Dates</h3>
<ul><li><b>Label:</b> one concrete sentence.</li></ul>
<h2>Education</h2><ul><li>Degree, institution, dates</li></ul>
<h2>Skills</h2><ul><li>Group: tools</li></ul>
<h2>Certificates</h2><ul><li></li></ul>
```

## Data/Legend (Google Doc)

Sections: `Career story`, `Projects in detail` (one H3 per project: context, my role, what I did, result), `Interview stories` (conflict, failure, success, leadership), `Standard answers` (English level, salary expectation (keep in sync with Settings `salary_expectation`), notice period, relocation, why leaving), `Honest gaps` (what I have not done, and the closest related experience), `Preferences` (what I want and do not want in a role).

## Data/Writing Style (Google Doc)

Pre-baked defaults. The person edits freely; skills always obey this doc over their own defaults.

```html
<h1>Writing Style</h1>
<h2>General</h2>
<ul>
<li>Short, concrete, vacancy-specific. One idea per sentence.</li>
<li>No em dashes. Use commas, colons or full stops.</li>
<li>No filler words: seamlessly, leveraging, spearheaded, passionate, dynamic.</li>
<li>No invented numbers. Every metric must be real and defensible.</li>
<li>No slashes between words in letters (write "web and API", not "web/API").</li>
<li>Write the letter in the vacancy's language when it is in letter_languages; otherwise English.</li>
</ul>
<h2>Letter modes</h2>
<p><b>default:</b> up to 2 paragraphs. Opening with role and fit, evidence from Profile, closing proposition.</p>
<p><b>short:</b> one paragraph, 3 to 5 vacancy-relevant skills, closing proposition. No colons or semicolons.</p>
<h2>Openings</h2><p>EN: Hello! I'm interested in this vacancy. I have relevant experience with ...</p>
<h2>Closings</h2><p>EN: Will be happy to discuss the project</p>
<h2>Recruiter answers</h2><p>2 to 4 sentences. Answer in the language of the question. Use Legend standard answers.</p>
<h2>Language-specific rules</h2><p>(add rules per language here)</p>
```

## Tracker (Google Sheet)

### Settings
`Key | Value | Note` (see job-search-setup Step 3 for keys)

### Applications
`Date | Company | Role | URL | Platform | CV | Result | External URL | Cover Letter | Notes`

- `Result` values: `sent`, `viewed`, `reject`, `hr interview`, `tech interview`, `test task`, `offer`, `no answer`, `withdrawn`.
- One row per submitted application. Never add skipped vacancies here.

### Vacancies
`Platform | Vacancy ID | Company | Title | URL | Published | Location | Remote | Salary | Apply Type | External Apply URL | Fit | Status | Skip Reason | First Seen | Last Seen`

- Key: `Platform` + `Vacancy ID`. Update existing rows instead of duplicating.
- `Status`: `new`, `shortlisted`, `drafted`, `applied`, `skipped`, `closed`.
- `Fit`: 1 to 5 score from vacancy-scout.

### Skipped
`Date | Company | Role | URL | Reason`

### Runs
`Run At | Mode | Found | Shortlisted | Drafted | Submitted | Failed | Replies Updated | Review Doc | Notes`

## CVs folder

- `CV – Master` (Google Doc): built from Profile by cv-builder.
- `CV – <Company> – <Role>` (Google Doc): tailored versions, only when requested or when a vacancy needs a different emphasis.
- PDF exports next to each Doc when an application needs a file.

## Cover Letters folder

One Google Doc per application: `<YYYY-MM-DD> <Company> – <Role>`, holding the exact submitted text and recruiter answers.

## Batch Reviews folder

One Google Doc per run: `Review <YYYY-MM-DD> <platform or all>`. Template in apply-assistant `references/review-doc.md`.

## README (Google Doc, root)

Written last by job-search-setup. Fill the braces.

```html
<h1>JobApplications_claude</h1>
<p>Cloud workspace for {Name}'s job search, managed by the <b>job-search-autopilot</b> Claude plugin. Everything for CVs, cover letters and application tracking lives here. Created {YYYY-MM-DD}.</p>
<h2>Folder layout</h2>
<ul>
<li><b>Data/</b>: information about me. Profile (facts), Legend (stories, standard answers, preferences), Writing Style (tone and language rules). Every CV, letter and answer is built only from these.</li>
<li><b>Tracker</b>: Settings, Applications, Vacancies, Skipped, Runs.</li>
<li><b>CVs/</b>: master CV and tailored versions, with PDF exports.</li>
<li><b>Cover Letters/</b>: exact submitted text per application.</li>
<li><b>Batch Reviews/</b>: daily review docs approved before submit.</li>
</ul>
<h2>How to use</h2>
<ul><li>"Find new vacancies"</li><li>"Apply to 10 vacancies"</li><li>"Tailor my CV for this job"</li><li>"Check replies"</li><li>"Run my job search"</li></ul>
<h2>Modes</h2>
<p><b>review</b>: prepares everything, submits after my approval. <b>auto</b>: submits strong matches with simple on-site forms by itself, up to the daily limit. Current mode: {mode}. Boards: {boards}. Browser: {browser}.</p>
<h2>Rules</h2>
<ul><li>No invented facts, numbers or tools.</li><li>No duplicate applications across platforms.</li><li>Every sent application is logged immediately with the exact text.</li><li>Claude never enters passwords; it uses my signed-in browser sessions.</li></ul>
<h2>Editing</h2><p>Edit the Data docs and Settings freely. Keep file and folder names unchanged.</p>
```
