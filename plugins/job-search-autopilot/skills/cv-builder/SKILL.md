---
name: cv-builder
description: "This skill should be used when the user asks to 'build my CV', 'update my resume', 'tailor my CV for this job', 'make a CV for a company', 'export my CV to PDF', 'write a cover letter document', or when apply-assistant needs a tailored CV or PDF. It builds CVs and cover letters as formatted Google Docs in the 'JobApplications_claude' Drive workspace from the Profile doc, and exports them to PDF."
metadata:
  version: "0.4.1"
---

# CV Builder

Build CVs and cover letter documents as Google Docs in the reserved workspace. Profile is the only source of facts.

## Before starting

1. Locate the workspace and read Settings, Profile, Legend and Writing Style (see `../job-search-setup/references/workspace-layout.md`). If the workspace is missing, run job-search-setup.
2. If Profile is empty or thin, ask the person for the missing facts before building. Never fill gaps with invented content.

## CV-style layout script

`scripts/build_cv_doc.py data.json out.json` turns CV JSON (name, title, contact, summary, experience with label and text bullets, education with degrees, skills; optional key_facts, certificates, note) into one Google Docs `update_doc` batch that renders the CV layout into an empty doc, appending from index 1: centered header, ruled section headers, borderless two-column tables for company and dates, real bullets, skills table, A4 with 51pt margins. To rebuild an existing doc in place (same link), prepend `deleteContentRange` [1, body end - 1] and `deleteParagraphBullets` [1, 2], and guard with the doc's `revisionId`. After the write, export to PDF and look at the pages.

## Build the master CV

1. Compose HTML using the template in `references/cv-template.md`.
2. Create or replace `CV – Master` in `CVs/` with `create_file` (`contentMimeType: text/html`, `parentId` = CVs folder). When replacing, create the new Doc first, then move the old one to trash only after the person confirms.
3. Keep it to 2 pages. Bullets follow the pattern `Label:` in bold plus one concrete sentence.

## Tailor for a vacancy

Use when the person asks, or when apply-assistant reports the master CV under-represents the vacancy's core requirements.

1. Read the vacancy text. List its must-have skills and domain.
2. Reorder and reword summary, bullets and skills to put matching real experience first. Do not add skills or tools the Profile does not contain.
3. Save as `CV – <Company> – <Role>` in `CVs/`. Set the Settings `cv_label` style label in the doc subtitle (e.g. `v3-tailored`).
4. Show the person a short diff: what moved up, what was reworded.

## Cover letter documents

When a vacancy needs a formal letter (not a short form message), build it from `references/cover-letter-template.md` and save to `Cover Letters/` as `<YYYY-MM-DD> <Company> – <Role>`. Follow Writing Style: up to 3 paragraphs (opening, evidence, call to action).

## Export to PDF

1. Download the Doc with `download_file_content` and `exportMimeType: application/pdf`.
2. Upload the PDF to the same folder with `create_file` (`contentMimeType: application/pdf`, `base64Content`, `disableConversionToGoogleType: true`), named like the Doc with `.pdf`.
3. Give the person the link. For uploads to job boards, the person may need to attach the file themselves, since browser automation cannot open the system file picker.

## Quality check (always)

- Read the created Doc back with `read_doc` and confirm all sections exist and nothing is truncated.
- Check against Writing Style: no em dashes, no filler words, no unverifiable numbers.
- Confirm name, email, phone and links match Profile exactly.
