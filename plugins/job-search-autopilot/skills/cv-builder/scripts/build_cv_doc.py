"""Build Google Docs batchUpdate requests that render a CV-style document
(matching generate_cv.py layout) into an empty doc, appending forward from index 1.

Usage: build_cv_doc.py data.json out_requests.json
"""
import json, sys

FONT = "Arial"
DARK = {"red": 0x22/255, "green": 0x22/255, "blue": 0x22/255}
MID = {"red": 0x55/255, "green": 0x55/255, "blue": 0x55/255}
GRAY = {"red": 0x99/255, "green": 0x99/255, "blue": 0x99/255}
SEP_DARK = {"red": 0x1A/255, "green": 0x1A/255, "blue": 0x1A/255}
CONTENT_W = 595.3 - 2 * 51.0


def u16(s):
    return len(s.encode("utf-16-le")) // 2


def pt(x):
    return {"magnitude": x, "unit": "PT"}


class B:
    def __init__(self):
        self.reqs = []
        self.styles = []
        self.c = 1
        self.bullet_ranges = []

    def text_style(self, start, end, size, bold=False, italic=False, color=None):
        if end <= start:
            return
        if size == 10.2 and not bold and not italic and (color is None or color == DARK):
            return
        self.styles.append({"updateTextStyle": {
            "range": {"startIndex": start, "endIndex": end},
            "textStyle": {
                "fontSize": pt(size), "bold": bold, "italic": italic,
                "foregroundColor": {"color": {"rgbColor": color or DARK}},
            },
            "fields": "fontSize,bold,italic,foregroundColor"}})

    def para_style(self, start, end, align="START", before=0, after=0, border=None,
                   indent_start=0, indent_first=0):
        if align == "START" and not before and not after and not border and not indent_start and not indent_first:
            return
        ps, f = {}, []
        if align != "START": ps["alignment"] = align; f.append("alignment")
        if before: ps["spaceAbove"] = pt(before); f.append("spaceAbove")
        if after: ps["spaceBelow"] = pt(after); f.append("spaceBelow")
        fields = ",".join(f)
        if border:
            color, padding = border
            ps["borderBottom"] = {"color": {"color": {"rgbColor": color}}, "width": pt(0.75),
                                  "padding": pt(padding), "dashStyle": "SOLID"}
            fields = (fields + ",borderBottom").lstrip(",")
        self.styles.append({"updateParagraphStyle": {
            "range": {"startIndex": start, "endIndex": end},
            "paragraphStyle": ps, "fields": fields}})

    def para(self, runs, align="START", before=0, after=0, border=None, bullet=False,
             indent_start=0, indent_first=0):
        """runs: list of (text, size, bold, italic, color)"""
        text = "".join(r[0] for r in runs)
        start = self.c
        self.reqs.append({"insertText": {"location": {"index": start}, "text": text + "\n"}})
        pos = start
        for t, size, bold, italic, color in runs:
            self.text_style(pos, pos + u16(t), size, bold, italic, color)
            pos += u16(t)
        end = start + u16(text) + 1
        self.para_style(start, end, align, before, after, border, indent_start, indent_first)
        if bullet:
            self.bullet_ranges.append((start, end))
        self.c = end

    def section(self, title, before=14):
        self.para([(title, 11.0, True, False, DARK)], before=before, after=0, border=(GRAY, 4))

    def table(self, rows, col0_w, styles, right_align_col1=False, cell_pad_top=0):
        """rows: list of [left, right]; styles: per row (left_style, right_style) as (size,bold,italic,color)"""
        R, C = len(rows), 2
        i = self.c
        # spacer paragraph that Google keeps before every table: make it tiny
        self.reqs.append({"insertTable": {"rows": R, "columns": C, "location": {"index": i}}})
        table_start = i + 1
        # fill last to first
        cell_pos = {}
        for r in range(R):
            for cc in range(C):
                cell_pos[(r, cc)] = i + 4 + r * (2 * C + 1) + 2 * cc
        for r in reversed(range(R)):
            for cc in reversed(range(C)):
                t = rows[r][cc]
                if t:
                    self.reqs.append({"insertText": {"location": {"index": cell_pos[(r, cc)]}, "text": t}})
        # compute final positions after fill (forward)
        shift = 0
        for r in range(R):
            for cc in range(C):
                t = rows[r][cc]
                s = cell_pos[(r, cc)] + shift
                e = s + u16(t)
                size, bold, italic, color = styles[r][cc]
                self.text_style(s, e, size, bold, italic, color)
                align = "END" if (cc == 1 and right_align_col1) else "START"
                self.para_style(s, e + 1, align, before=cell_pad_top, after=cell_pad_top)
                shift += u16(t)
        # spacer paragraph before table
        self.text_style(i, i + 1, 1)
        self.para_style(i, i + 1)
        # borders off, no padding, column widths
        none = {"color": {"color": {"rgbColor": {"red": 1, "green": 1, "blue": 1}}},
                "width": pt(0), "dashStyle": "SOLID"}
        self.styles.append({"updateTableCellStyle": {
            "tableStartLocation": {"index": table_start},
            "tableCellStyle": {"borderTop": none, "borderBottom": none, "borderLeft": none,
                               "borderRight": none, "paddingTop": pt(0), "paddingBottom": pt(0),
                               "paddingLeft": pt(0), "paddingRight": pt(0)},
            "fields": "borderTop,borderBottom,borderLeft,borderRight,paddingTop,paddingBottom,paddingLeft,paddingRight"}})
        for idx, w in ((0, col0_w), (1, CONTENT_W - col0_w)):
            self.styles.append({"updateTableColumnProperties": {
                "tableStartLocation": {"index": table_start}, "columnIndices": [idx],
                "tableColumnProperties": {"widthType": "FIXED_WIDTH", "width": pt(w)},
                "fields": "width,widthType"}})
        self.c = i + 3 + R * (2 * C + 1) + shift

    def finish(self):
        # bullets: group consecutive ranges
        groups = []
        for s, e in self.bullet_ranges:
            if groups and groups[-1][1] == s:
                groups[-1][1] = e
            else:
                groups.append([s, e])
        for s, e in groups:
            self.styles.append({"createParagraphBullets": {
                "range": {"startIndex": s, "endIndex": e}, "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
            self.styles.append({"updateParagraphStyle": {
                "range": {"startIndex": s, "endIndex": e},
                "paragraphStyle": {"indentStart": pt(10), "indentFirstLine": pt(0)},
                "fields": "indentStart,indentFirstLine"}})
        end = self.c
        base = [
          {"updateParagraphStyle": {"range": {"startIndex": 1, "endIndex": end},
            "paragraphStyle": {"namedStyleType": "NORMAL_TEXT", "alignment": "START", "lineSpacing": 100,
              "spaceAbove": pt(0), "spaceBelow": pt(0), "indentStart": pt(0), "indentFirstLine": pt(0)},
            "fields": "namedStyleType,alignment,lineSpacing,spaceAbove,spaceBelow,indentStart,indentFirstLine"}},
          {"updateTextStyle": {"range": {"startIndex": 1, "endIndex": end},
            "textStyle": {"weightedFontFamily": {"fontFamily": FONT}, "fontSize": pt(10.2), "bold": False,
              "italic": False, "foregroundColor": {"color": {"rgbColor": DARK}}},
            "fields": "weightedFontFamily,fontSize,bold,italic,foregroundColor"}}]
        self.reqs = self.reqs + base + self.styles
        self.reqs.append({"updateDocumentStyle": {
            "documentStyle": {"marginTop": pt(51), "marginBottom": pt(51), "marginLeft": pt(51),
                              "marginRight": pt(51),
                              "pageSize": {"width": pt(595.3), "height": pt(841.9)}},
            "fields": "marginTop,marginBottom,marginLeft,marginRight,pageSize"}})
        return self.reqs


def build(d):
    b = B()
    b.para([(d["name"], 22.0, True, False, DARK)], align="CENTER")
    b.para([(d["title"], 11.5, False, False, MID)], align="CENTER", before=2)
    c = d["contact"]
    parts = [p for p in [c.get("location"), c.get("email"), c.get("phone"), c.get("linkedin")] if p]
    b.para([("  •  ".join(parts), 9.5, False, False, DARK)], align="CENTER", before=2, after=4,
           border=(SEP_DARK, 4))

    b.section("SUMMARY", before=10)
    b.para([(d["summary"], 10.2, False, False, DARK)], align="JUSTIFIED", before=4)

    if d.get("key_facts"):
        b.section("KEY FACTS")
        rows = [[k, v] for k, v in d["key_facts"]]
        st = [((10.2, True, False, DARK), (10.2, False, False, DARK)) for _ in rows]
        b.table(rows, 128, st, cell_pad_top=2)

    b.section("WORK EXPERIENCE")
    for job in d["experience"]:
        rows = [[job["company"], job["location"]], [job["title"], job["dates"]]]
        st = [((10.5, True, False, DARK), (9.5, False, False, DARK)),
              ((10.0, False, True, DARK), (10.0, False, False, DARK))]
        b.table(rows, CONTENT_W - 120, st, right_align_col1=True)
        for bl in job["bullets"]:
            b.para([(bl["label"], 10.2, True, False, DARK), (bl["text"], 10.2, False, False, DARK)],
                   align="JUSTIFIED", bullet=True)

    b.section("EDUCATION")
    for edu in d["education"]:
        b.para([(edu["institution"], 10.2, True, False, DARK)], before=6)
        rows = [[g["degree"], g.get("dates", "")] for g in edu["degrees"]]
        st = [((10.2, False, True, DARK), (9.5, False, False, DARK)) for _ in rows]
        b.table(rows, CONTENT_W - 90, st, right_align_col1=True)

    b.section(d.get("skills_title", "SKILLS"))
    rows = [[s["category"], s["value"]] for s in d["skills"]]
    st = [((10.2, True, False, DARK), (10.2, False, False, DARK)) for _ in rows]
    b.table(rows, 128, st, cell_pad_top=4)

    if d.get("certificates"):
        b.section("CERTIFICATES")
        for cert in d["certificates"]:
            b.para([(cert, 10.2, False, False, DARK)], bullet=True)

    if d.get("note"):
        b.para([(d["note"], 8.0, False, True, GRAY)], before=14)
    return b.finish()


if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    reqs = build(data)
    json.dump(reqs, open(sys.argv[2], "w"), ensure_ascii=False)
    print(len(reqs), "requests")
