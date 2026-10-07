# CV HTML template

Google Docs converts this HTML on upload. Use inline styles only; Docs ignores `<style>` blocks. Use a single sans-serif font (Arial or Helvetica).

```html
<html><body style="font-family:Arial;font-size:10pt">
<p style="font-size:20pt;margin:0"><b>{Name}</b></p>
<p style="font-size:12pt;margin:0">{Title}</p>
<p style="font-size:9pt;margin:0">{Location} · {Email} · {Phone} · {LinkedIn}</p>
<hr>
<p style="font-size:11pt"><b>SUMMARY</b></p>
<p>{3 to 4 sentences from Profile summary, tuned to target roles}</p>
<hr>
<p style="font-size:11pt"><b>EXPERIENCE</b></p>
<!-- repeat per job, newest first -->
<p style="margin:0"><b>{Title}</b>, {Company} · {Location}</p>
<p style="margin:0;font-size:9pt">{Dates}</p>
<ul>
  <li><b>{Label}:</b> {one concrete sentence}</li>
</ul>
<hr>
<p style="font-size:11pt"><b>EDUCATION</b></p>
<p style="margin:0">{Degree}, {Institution} · {Dates}</p>
<hr>
<p style="font-size:11pt"><b>SKILLS</b></p>
<table style="font-size:9.5pt">
  <tr><td><b>{Group}</b></td><td>{tools, comma separated}</td></tr>
</table>
</body></html>
```

## Rules

- 3 to 5 bullets for the current role, 2 to 4 for older roles.
- Labels are 1 to 3 words ending with a colon: `Automation from zero:`, `Test planning:`.
- Every bullet maps to a fact in Profile or Legend.
- Skills grouped by type (languages, frameworks, tools, practices), not one long line.
