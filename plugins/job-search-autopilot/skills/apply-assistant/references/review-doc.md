# Review doc template

Create as a Google Doc in `Batch Reviews/` from HTML.

```html
<h1>Review {YYYY-MM-DD} · {platform or all}</h1>
<p><b>Mode:</b> {review|auto} · <b>Goal:</b> {N} · <b>Logged:</b> {k}/{N} · <b>CV:</b> {cv_label} · <b>Letter mode:</b> {default|short}</p>

<h2>Summary</h2>
<table>
<tr><th>#</th><th>Company</th><th>Role</th><th>Published</th><th>Fit</th><th>Lang</th><th>Apply</th><th>Status</th><th>Link</th></tr>
<tr><td>1</td><td>{Company}</td><td>{Role}</td><td>{date}</td><td>{fit}</td><td>{EN}</td><td>{inline|external|manual}</td><td>{needs approval|auto-submitted|failed: reason}</td><td>{url}</td></tr>
</table>

<h2>Skipped and alternates</h2>
<ul><li><s>{Company} · {Role}</s> SKIP: {reason}</li></ul>
<p><b>Alternates:</b> {Company} ({url}), ...</p>

<h2>Drafts</h2>
<!-- one block per actionable vacancy -->
<h3>{n}. {Company} · {Role}</h3>
<p><b>Apply:</b> {inline on board | external: url | manual: reason}</p>
<p><b>Letter:</b></p>
<p>{exact letter text}</p>
<p><b>Recruiter answers:</b></p>
<ul><li><b>{question}</b> {answer}</li></ul>
```

Keep skipped rows visible (struck through) for the audit trail. Replace skips with alternates so the actionable count matches the goal.
