#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dựng file PDF "Đề cương ôn tập giữa học kì I - Tin học 10 (Kết nối tri thức)"
từ các tệp nguồn trong thư mục content/.

Cách dùng:  python build/build_pdf.py
Yêu cầu  :  reportlab  (pip install reportlab)
Font     :  DejaVu Sans (có sẵn tại /usr/share/fonts/truetype/dejavu)
"""

import glob
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame,
                                KeepTogether,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_DIR = os.path.join(ROOT, "content")
OUT_PDF = os.path.join(ROOT, "DE_CUONG_ON_TAP_TIN_HOC_10_GIUA_KI_I.pdf")

# --------------------------------------------------------------------------
# Font
# --------------------------------------------------------------------------
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("Body", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("Body-Bold", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Disp", os.path.join(FONT_DIR, "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont("Disp-Bold", os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                              italic="Body", boldItalic="Body-Bold")
pdfmetrics.registerFontFamily("Disp", normal="Disp", bold="Disp-Bold",
                              italic="Disp", boldItalic="Disp-Bold")

# --------------------------------------------------------------------------
# Bảng màu
# --------------------------------------------------------------------------
NAVY = colors.HexColor("#123A63")
NAVY_D = colors.HexColor("#0B2545")
BLUE = colors.HexColor("#1F5C99")
TEAL = colors.HexColor("#0F766E")
ORANGE = colors.HexColor("#B45309")
RED = colors.HexColor("#B91C1C")
GREEN = colors.HexColor("#166534")
GREY = colors.HexColor("#4B5563")
LINE = colors.HexColor("#C6D3E1")
BG_SOFT = colors.HexColor("#F1F6FB")
BG_TIP = colors.HexColor("#ECF7F1")
BG_WARN = colors.HexColor("#FDF3E7")
BG_NOTE = colors.HexColor("#F4F4F5")

PAGE_W, PAGE_H = A4
M_L, M_R, M_T, M_B = 1.75 * cm, 1.6 * cm, 1.85 * cm, 1.65 * cm
FRAME_W = PAGE_W - M_L - M_R


def S(name, **kw):
    base = dict(fontName="Body", fontSize=9.7, leading=13.7,
                textColor=colors.HexColor("#1B1B1B"))
    base.update(kw)
    return ParagraphStyle(name, **base)


ST = {
    "body": S("body", alignment=TA_JUSTIFY, spaceAfter=4.2),
    "lead": S("lead", fontSize=10.4, leading=15.6, textColor=colors.HexColor("#243B53"),
              alignment=TA_JUSTIFY, spaceAfter=7),
    "h1": S("h1", fontName="Body-Bold", fontSize=16, leading=20, textColor=colors.white),
    "h2": S("h2", fontName="Body-Bold", fontSize=12.2, leading=16, textColor=NAVY,
            spaceBefore=11, spaceAfter=4),
    "h3": S("h3", fontName="Body-Bold", fontSize=10.3, leading=14, textColor=TEAL,
            spaceBefore=7.5, spaceAfter=2.6),
    "h4": S("h4", fontName="Body-Bold", fontSize=9.7, leading=13.4, textColor=NAVY_D,
            spaceBefore=5, spaceAfter=1.6),
    "b1": S("b1", leftIndent=13, bulletIndent=3, spaceAfter=2.4),
    "b2": S("b2", leftIndent=26, bulletIndent=16, spaceAfter=2.0),
    "b3": S("b3", leftIndent=39, bulletIndent=29, spaceAfter=1.8),
    "box": S("box", fontSize=9.4, leading=13.2, alignment=TA_JUSTIFY),
    "toc1": S("toc1", fontName="Body-Bold", fontSize=10.1, leading=17, textColor=NAVY),
    "cap": S("cap", fontName="Body-Bold", fontSize=8.7, leading=11.5, textColor=GREY,
             spaceBefore=3, spaceAfter=2),
    "small": S("small", fontSize=8.6, leading=11.8, textColor=GREY),
    "ans": S("ans", fontSize=9.3, leading=13.0, textColor=GREEN, alignment=TA_JUSTIFY),
    "q": S("q", fontSize=9.7, leading=13.6, textColor=colors.HexColor("#111827"),
           spaceBefore=5.5, spaceAfter=2.4),
    "opt": S("opt", fontSize=9.5, leading=12.8, leftIndent=4),
    "th": S("th", fontName="Body-Bold", fontSize=9.0, leading=12.2, textColor=colors.white,
            splitLongWords=0),
    "td": S("td", fontSize=9.0, leading=12.3, splitLongWords=0),
    "tdc": S("tdc", fontSize=9.0, leading=12.3, alignment=TA_CENTER, splitLongWords=0),
}


# --------------------------------------------------------------------------
def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(t):
    t = esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)",
               r'<font color="#124E78">\1</font>', t)
    t = re.sub(r"%%(.+?)%%", r'<font color="#B45309"><b>\1</b></font>', t)
    t = re.sub(r"~~(.+?)~~", r'<font color="#B91C1C"><b>\1</b></font>', t)
    t = re.sub(r"\{\{(.+?)\}\}", r'<font color="#0F766E"><b>\1</b></font>', t)
    return t


def width_list(spec):
    parts = [float(x) for x in spec.split(",")]
    total = sum(parts)
    return [FRAME_W * p / total for p in parts]


def th_style(extra=None, header_bg=NAVY):
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("GRID", (0, 0), (-1, -1), 0.45, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.6),
    ]
    if extra:
        cmds += extra
    return TableStyle(cmds)


class Rule(Flowable):
    def __init__(self, w, thickness=0.9, color=LINE, pad=0):
        Flowable.__init__(self)
        self.w, self.t, self.c, self.pad = w, thickness, color, pad

    def wrap(self, aw, ah):
        return self.w, self.t + self.pad

    def draw(self):
        self.canv.setStrokeColor(self.c)
        self.canv.setLineWidth(self.t)
        self.canv.line(0, 0, self.w, 0)


def h1_band(text, kicker=None):
    label = Paragraph(inline(text), ST["h1"])
    inner = [[label]]
    if kicker:
        inner = [[Paragraph('<font color="#9DC3E6" size="8"><b>%s</b></font>' % inline(kicker),
                            S("kc", fontSize=8, leading=11))],
                 [label]]
    t = Table(inner, colWidths=[FRAME_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (0, 0), 8 if kicker else 10),
        ("BOTTOMPADDING", (-1, -1), (-1, -1), 10),
        ("TOPPADDING", (-1, -1), (-1, -1), 0),
        ("LINEBELOW", (0, -1), (-1, -1), 3, colors.HexColor("#B45309")),
    ]))
    return t


def callout(kind, text, title=None):
    bg, bar, default_title = {
        "box": (BG_SOFT, BLUE, "GHI NHỚ"),
        "tip": (BG_TIP, GREEN, "MẸO GHI NHỚ"),
        "warn": (BG_WARN, ORANGE, "CẨN THẬN"),
        "note": (BG_NOTE, GREY, "LƯU Ý"),
    }[kind]
    body = []
    head = title or default_title
    if head:
        body.append(Paragraph('<font color="%s" size="8.2"><b>%s</b></font>'
                              % (bar.hexval().replace("0x", "#"), inline(head)),
                              S("cot", fontSize=8.2, leading=10.6, spaceAfter=2.5)))
    body.append(Paragraph(inline(text), ST["box"]))
    t = Table([[body]], colWidths=[FRAME_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, bar),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return [Spacer(1, 3.5), t, Spacer(1, 5)]


def answer_block(text, kind="answer"):
    bg, bar, mark, color = (BG_TIP, GREEN, "✔ Đáp án: ", "#14532D") \
        if kind == "answer" else (BG_TIP, GREEN, "• ", "#14532D")
    p = Paragraph('<font color="%s">%s%s</font>' % (color, mark, inline(text)),
                  S("anb", fontSize=9.2, leading=12.8, alignment=TA_JUSTIFY,
                    textColor=colors.HexColor(color)))
    t = Table([[p]], colWidths=[FRAME_W - 12])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, bar),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def chain(steps):
    """Dải các bước có mũi tên: Tiếp nhận → Xử lí → Truyền."""
    n = len(steps)
    arrow_w = 0.55 * cm
    box_w = (FRAME_W - arrow_w * (n - 1)) / n
    cells, widths = [], []
    for k, s in enumerate(steps):
        p = Paragraph('<font color="#FFFFFF" size="9"><b>%s</b></font>' % inline(s),
                      S("chn", fontSize=9, leading=12, alignment=TA_CENTER,
                        textColor=colors.white))
        cells.append(p)
        widths.append(box_w)
        if k < n - 1:
            cells.append(Paragraph('<font color="#1F5C99" size="13">→</font>',
                                   S("arr", fontSize=13, leading=14, alignment=TA_CENTER)))
            widths.append(arrow_w)
    t = Table([cells], colWidths=widths)
    style = [("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("TOPPADDING", (0, 0), (-1, -1), 6),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
             ("LEFTPADDING", (0, 0), (-1, -1), 3),
             ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
    for k in range(0, n):
        idx = k * 2
        style += [("BACKGROUND", (idx, 0), (idx, 0), BLUE),
                  ("BOX", (idx, 0), (idx, 0), 0.4, BLUE)]
    t.setStyle(TableStyle(style))
    return [Spacer(1, 2), t, Spacer(1, 7)]


# --------------------------------------------------------------------------
class Doc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(
            self, filename, pagesize=A4,
            leftMargin=M_L, rightMargin=M_R, topMargin=M_T, bottomMargin=M_B,
            title="Đề cương ôn tập giữa học kì I – Tin học 10 (Kết nối tri thức)",
            author="Biên soạn bám sát Ma trận & Đặc tả đề kiểm tra giữa kì I",
            subject="Tin học 10 – Định hướng ICT", **kw)
        self.toc_entries = []
        cover_frame = Frame(M_L, M_B, FRAME_W, PAGE_H - M_T - M_B, id="cover",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        body_frame = Frame(M_L, M_B, FRAME_W, PAGE_H - M_T - M_B, id="body",
                           leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self.draw_cover_bg),
            PageTemplate(id="body", frames=[body_frame], onPage=self.draw_chrome),
        ])

    def draw_cover_bg(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, PAGE_H - 7.25 * cm, PAGE_W, 7.25 * cm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#0E2E4E"))
        canv.rect(0, 0, PAGE_W, 3.2 * cm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#B45309"))
        canv.rect(0, PAGE_H - 7.40 * cm, PAGE_W, 0.15 * cm, stroke=0, fill=1)
        canv.setFillColor(colors.HexColor("#1F5C99"))
        for i in range(9):
            canv.rect(PAGE_W - 3.0 * cm + (i % 3) * 0.62 * cm,
                      PAGE_H - 2.4 * cm - (i // 3) * 0.62 * cm,
                      0.4 * cm, 0.4 * cm, stroke=0, fill=1)
        canv.restoreState()

    def draw_chrome(self, canv, doc):
        canv.saveState()
        canv.setFont("Body", 7.6)
        canv.setFillColor(colors.HexColor("#7B8794"))
        canv.drawString(M_L, PAGE_H - 1.24 * cm,
                        "ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I  •  TIN HỌC 10  •  KẾT NỐI TRI THỨC")
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.6)
        canv.line(M_L, PAGE_H - 1.40 * cm, PAGE_W - M_R, PAGE_H - 1.40 * cm)
        canv.line(M_L, 1.05 * cm, PAGE_W - M_R, 1.05 * cm)
        canv.setFont("Body", 7.2)
        canv.setFillColor(colors.HexColor("#98A2B3"))
        canv.drawString(M_L, 0.55 * cm,
                        "Biên soạn bám sát Ma trận & Đặc tả đề kiểm tra giữa kì I – Tin học 10")
        canv.setFont("Body", 8.4)
        canv.setFillColor(NAVY)
        canv.drawRightString(PAGE_W - M_R, 0.52 * cm, str(canv.getPageNumber()))
        canv.restoreState()

    def afterFlowable(self, flowable):
        lvl = getattr(flowable, "_toc_level", None)
        if lvl is not None:
            self.toc_entries.append((lvl, flowable._toc_text, self.page))


# --------------------------------------------------------------------------
def parse_files(files):
    lines = []
    for f in files:
        lines.extend(open(f, encoding="utf-8").read().splitlines())
        lines.append("")
    return lines


def build_story(files):
    story, stats = [], {"mcq": 0, "ds": 0, "tl": 0}
    ctr = {"q": 0}
    pending = []

    def flush():
        if not pending:
            return
        avail = PAGE_H - M_T - M_B
        total = 0.0
        for fl in pending:
            try:
                total += fl.wrap(FRAME_W, PAGE_H)[1] + fl.getSpaceBefore() + fl.getSpaceAfter()
            except Exception:
                total = avail
        if total > avail * 0.88 and len(pending) > 2:
            story.append(KeepTogether(pending[:2]))
            story.extend(pending[2:])
        else:
            story.append(KeepTogether(list(pending)))
        pending.clear()
    lines = parse_files(files)
    i, n = 0, len(lines)
    while i < n:
        line = lines[i].strip()
        i += 1
        if not line or line.startswith("//"):
            continue
        if not (line.startswith(("opt|", "opt1|", "answer|", "sol|", "qs|", "ds|", "tl|"))
                or (pending and (line.startswith("+ ") or line.startswith("- ")))):
            flush()

        # ---------- bảng ----------
        if line.startswith("tbl|") or line.startswith("tb|"):
            segs = line.split("|")
            spec = segs[1].strip() if len(segs) > 1 else ""
            caption = segs[2].strip() if len(segs) > 2 and segs[2].strip() else None
            rows = []
            while i < n:
                ln = lines[i].strip()
                i += 1
                if not ln:
                    continue
                if ln.startswith("endtbl") or ln.startswith("te|"):
                    break
                if ln.startswith("th|"):
                    rows.append(("h", [c.strip() for c in ln[3:].split("||")]))
                elif ln.startswith("tr|"):
                    rows.append(("d", [c.strip() for c in ln[3:].split("||")]))
                elif ln.startswith("trc|"):
                    rows.append(("c", [c.strip() for c in ln[4:].split("||")]))
            if not rows:
                continue
            ncol = max(len(r[1]) for r in rows)
            data, cmds = [], [("VALIGN", (0, 0), (-1, -1), "TOP")]
            has_head = rows[0][0] == "h"
            for idx, (kind, cells) in enumerate(rows):
                cells = cells + [""] * (ncol - len(cells))
                stl = ST["th"] if kind == "h" else (ST["tdc"] if kind == "c" else ST["td"])
                data.append([Paragraph(inline(c), stl) if c else "" for c in cells])
            widths = width_list(spec) if spec else [FRAME_W / ncol] * ncol
            tbl = Table(data, colWidths=widths, repeatRows=1 if has_head else 0)
            if has_head:
                cmds += [("BACKGROUND", (0, 0), (-1, 0), NAVY),
                         ("VALIGN", (0, 0), (-1, 0), "MIDDLE")]
                start = 1
            else:
                start = 0
            for k in range(start, len(data)):
                if (k - start) % 2 == 1:
                    cmds.append(("BACKGROUND", (0, k), (-1, k), BG_SOFT))
            tbl.setStyle(th_style(cmds))
            block = []
            if caption:
                block.append(Paragraph(inline(caption), ST["cap"]))
            block.append(tbl)
            block.append(Spacer(1, 6))
            story.append(KeepTogether(block) if len(data) <= 9 else block[0])
            if len(data) > 9:
                story.extend(block[1:])
            continue

        # ---------- khối gọi chú ----------
        m = re.match(r"^(box|tip|warn|note)\|(.*)$", line)
        if m:
            story.extend(callout(m.group(1), m.group(2)))
            continue

        # ---------- các bước ----------
        if line.startswith("chain|"):
            story.extend(chain([s.strip() for s in line[6:].split("||")]))
            continue

        # ---------- điều khiển ----------
        if line.startswith("keep|"):
            continue
        if line.startswith("pb|"):
            story.append(PageBreak())
            continue
        if line.startswith("hr|"):
            story.append(Rule(FRAME_W, 0.7, LINE, 7))
            continue
        if line.startswith("spacer|"):
            story.append(Spacer(1, float(line.split("|")[1])))
            continue

        # ---------- tiêu đề ----------
        if line.startswith("### "):
            story.append(Paragraph(inline(line[4:]), ST["h3"]))
            continue
        if line.startswith("## "):
            txt = line[3:].strip()
            p = Paragraph(inline(txt), ST["h2"])
            p._toc_level, p._toc_text = 2, re.sub(r"[*%~{}]", "", txt)
            story.append(p)
            story.append(Rule(FRAME_W, 0.5, LINE, 4))
            continue
        if line.startswith("# "):
            txt = line[2:].strip().split("|")
            head = txt[0].strip()
            kicker = txt[1].strip() if len(txt) > 1 else None
            if story:
                story.append(CondPageBreak(0.72 * (PAGE_H - M_T - M_B)))
            band = h1_band(head, kicker)
            band._toc_level, band._toc_text = 1, re.sub(r"[*%~{}]", "", head)
            band.keepWithNext = True
            story.append(Spacer(1, 3))
            story.append(band)
            story.append(Spacer(1, 10))
            continue
        if line.startswith("h3|"):
            story.append(Paragraph(inline(line[3:]), ST["h3"]))
            continue
        if line.startswith("h4|"):
            story.append(Paragraph(inline(line[3:]), ST["h4"]))
            continue
        if line.startswith("cap|"):
            story.append(Paragraph(inline(line[4:]), ST["cap"]))
            continue
        if line.startswith("lead|"):
            story.append(Paragraph(inline(line[5:]), ST["lead"]))
            continue
        if line.startswith("small|"):
            story.append(Paragraph(inline(line[6:]), ST["small"]))
            continue
        if line.startswith("center|"):
            story.append(Paragraph(inline(line[7:]), S("ctr", fontSize=9.5, leading=13,
                                                       alignment=TA_CENTER)))
            continue

        # ---------- câu hỏi / đáp án ----------
        if line.startswith("answer|"):
            pending.append(Spacer(1, 2.5))
            pending.append(answer_block(line[7:], "answer"))
            pending.append(Spacer(1, 5))
            continue
        if line.startswith("sol|"):
            pending.append(answer_block(line[4:], "sol"))
            pending.append(Spacer(1, 5))
            continue
        if line.startswith("opt|"):
            parts = [p.strip() for p in line[4:].split("||")]
            cells = [Paragraph(inline(p), ST["opt"]) for p in parts]
            if len(cells) % 2:
                cells.append("")
            rows = [cells[k:k + 2] for k in range(0, len(cells), 2)]
            t = Table(rows, colWidths=[FRAME_W / 2 - 5, FRAME_W / 2 - 5])
            t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("TOPPADDING", (0, 0), (-1, -1), 1.0),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 4),
                                   ("RIGHTPADDING", (0, 0), (-1, -1), 2)]))
            pending.append(t)
            continue
        if line.startswith("opt1|"):
            for p2 in line[5:].split("||"):
                pending.append(Paragraph(inline(p2.strip()), ST["opt"]))
            continue
        if line.startswith("resetq|"):
            ctr["q"] = 0
            continue
        if line.startswith("qs|"):
            stats["mcq"] += 1
            ctr["q"] += 1
            pending.append(Paragraph("<b>Câu %d.</b> %s" % (ctr["q"], inline(line[3:])), ST["q"]))
            continue
        if line.startswith("ds|"):
            stats["ds"] += 1
            ctr["q"] += 1
            pending.append(Paragraph("<b>Câu %d.</b> %s" % (ctr["q"], inline(line[3:])), ST["q"]))
            continue
        if line.startswith("tl|"):
            stats["tl"] += 1
            ctr["q"] += 1
            pending.append(Paragraph("<b>Câu %d</b> <font color=\"#B45309\">(tự luận)</font>. %s"
                                     % (ctr["q"], inline(line[3:])), ST["q"]))
            continue

        # ---------- danh sách ----------
        if line.startswith("- "):
            (pending if pending else story).append(
                Paragraph(inline(line[2:]), ST["b1"], bulletText="•"))
            continue
        if line.startswith("+ "):
            (pending if pending else story).append(
                Paragraph(inline(line[2:]), ST["b2"], bulletText="–"))
            continue
        if line.startswith("* "):
            story.append(Paragraph(inline(line[2:]), ST["b3"], bulletText="·"))
            continue

        story.append(Paragraph(inline(line), ST["body"]))
    flush()
    return story, stats


# --------------------------------------------------------------------------
def cover_story(stats):
    s = [Spacer(1, 0.72 * cm)]
    s.append(Paragraph('<font color="#BBD7F0" size="10.2"><b>TIN HỌC 10  •  ĐỊNH HƯỚNG ICT</b></font>',
                       S("cv1", fontSize=10.2, leading=13)))
    s.append(Spacer(1, 0.30 * cm))
    s.append(Paragraph('<font color="#FFFFFF" size="31" name="Disp-Bold">ĐỀ CƯƠNG</font>',
                       S("cv2", fontSize=31, leading=37)))
    s.append(Paragraph('<font color="#FFFFFF" size="31" name="Disp-Bold">ÔN TẬP</font>',
                       S("cv2b", fontSize=31, leading=37)))
    s.append(Spacer(1, 0.22 * cm))
    s.append(Paragraph('<font color="#F5C17A" size="18" name="Disp-Bold">GIỮA HỌC KÌ I</font>',
                       S("cv3", fontSize=18, leading=23)))
    s.append(Spacer(1, 0.62 * cm))
    s.append(Paragraph('<font color="#123A63" size="11">Bộ sách: <b>Kết nối tri thức với cuộc sống</b></font>',
                       S("cv4", fontSize=11, leading=15)))
    s.append(Rule(FRAME_W, 0.8, colors.HexColor("#B45309"), 0))
    s.append(Spacer(1, 1.55 * cm))

    s.append(Paragraph("Tài liệu được biên soạn trên cơ sở <b>phân tích trực tiếp</b> tệp "
                       "“MA TRẬN GIỮA KÌ I – LỚP 10.docx”: bám đúng cấu trúc đề, đúng 6 đơn vị kiến thức, "
                       "đúng tỉ lệ các mức độ nhận thức và đúng đặc tả năng lực cần kiểm tra của đề giữa học kì I.",
                       S("cv5", fontSize=10.4, leading=16.4,
                         textColor=colors.HexColor("#1F2937"), alignment=TA_JUSTIFY)))
    s.append(Spacer(1, 0.55 * cm))
    rows = [
        [Paragraph('<b>Cấu trúc đề</b>', ST["td"]),
         Paragraph("20 câu trắc nghiệm (5,0 điểm) + 2 câu đúng/sai (2,0 điểm) + 3 câu tự luận (3,0 điểm) — thời gian 45 phút", ST["td"])],
        [Paragraph('<b>Nội dung</b>', ST["td"]),
         Paragraph("Chủ đề A – Máy tính và xã hội tri thức • Chủ đề B – Mạng máy tính và Internet • "
                   "Chủ đề D – Đạo đức, pháp luật và văn hoá trong môi trường số", ST["td"])],
        [Paragraph('<b>Tỉ lệ mức độ</b>', ST["td"]),
         Paragraph("Nhận biết 40% • Thông hiểu 30% • Vận dụng 20% • Vận dụng cao 10%", ST["td"])],
        [Paragraph('<b>Trong tài liệu</b>', ST["td"]),
         Paragraph("Lý thuyết trọng tâm của 6 đơn vị kiến thức • %d câu hỏi có đáp án (%d câu luyện tập "
                   "theo chủ đề + 25 câu đề mô phỏng) • lời giải chi tiết • phụ lục nguyên văn ma trận và đặc tả"
                   % (stats.get("total_q", 0), stats.get("total_q", 0) - 25), ST["td"])],
    ]
    t = Table(rows, colWidths=[3.1 * cm, FRAME_W - 3.1 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
        ("BOX", (0, 0), (-1, -1), 0.7, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BACKGROUND", (0, 0), (0, -1), BG_SOFT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 4.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5.2),
    ]))
    s.append(t)
    s.append(Spacer(1, 0.62 * cm))
    s.append(Paragraph('<font color="#123A63" size="9.6"><b>BỐ CỤC TÀI LIỆU</b></font>',
                       S("cv7", fontSize=9.6, leading=13)))
    s.append(Rule(FRAME_W, 0.6, colors.HexColor("#B45309")))
    s.append(Spacer(1, 5))
    parts = [
        ("0", "Phân tích đề, ma trận rút gọn, lộ trình 7 ngày, kĩ năng phòng thi"),
        ("1 – 3", "Lý thuyết trọng tâm ba chủ đề A, B, D + 72 câu hỏi luyện tập có đáp án"),
        ("4", "Đề mô phỏng giữa học kì I: 25 câu – 10 điểm – 45 phút, đúng cấu trúc ma trận"),
        ("5", "Đáp án, thang điểm chi tiết và hướng dẫn chấm phần tự luận"),
        ("6 – 7", "Nguyên văn ma trận, đặc tả của tệp gốc và sổ tay tra nhanh trước giờ thi"),
    ]
    rows2 = [[Paragraph('<font color="#B45309"><b>Phần %s</b></font>' % a,
                        S("pp", fontSize=8.8, leading=12)),
              Paragraph('<font color="#243B53">%s</font>' % inline(b),
                        S("pp2", fontSize=8.8, leading=12))] for a, b in parts]
    t2 = Table(rows2, colWidths=[2.0 * cm, FRAME_W - 2.0 * cm])
    t2.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.0),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    s.append(t2)
    s.append(Spacer(1, 1.5 * cm))
    s.append(Paragraph('<font color="#D6E6F5" size="8.8">Tài liệu dùng cho học sinh lớp 10 ôn thi giữa học kì I – '
                       'biên soạn và trình bày dưới dạng PDF</font>', S("cv6", fontSize=8.8, leading=12)))
    return s


def toc_story(entries, pages):
    s = [Spacer(1, 2), h1_band("MỤC LỤC", "Cấu trúc tài liệu và cách sử dụng"), Spacer(1, 8)]
    data = []
    for idx, (lvl, txt, _p) in enumerate(entries):
        num = str(pages.get(idx, "")) if pages else "••"
        if lvl == 1:
            data.append([Paragraph(inline(txt), S("t1c", fontName="Body-Bold", fontSize=9.4,
                                                 leading=12.8, textColor=NAVY)),
                         Paragraph("<b>%s</b>" % num, S("tp1", fontSize=9.0, leading=12.8,
                                                        alignment=TA_CENTER, textColor=NAVY))])
        else:
            data.append([Paragraph('<font color="#334E68">%s</font>' % inline(txt),
                                   S("tp2", fontSize=8.5, leading=10.8, leftIndent=12)),
                         Paragraph('<font color="#334E68">%s</font>' % num,
                                   S("tp3", fontSize=8.6, leading=11.4, alignment=TA_CENTER))])
    if not data:
        return s + [Paragraph("(đang cập nhật)", ST["small"])]
    t = Table(data, colWidths=[FRAME_W - 1.4 * cm, 1.4 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#E3EAF2")),
        ("TOPPADDING", (0, 0), (-1, -1), 1.7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.1),
        ("LEFTPADDING", (0, 0), (-1, -1), 2),
    ]))
    s.append(t)
    return s


# --------------------------------------------------------------------------
def main():
    files = sorted(glob.glob(os.path.join(CONTENT_DIR, "*.md")))
    if not files:
        sys.exit("Không tìm thấy tệp nội dung trong %s" % CONTENT_DIR)

    _, stats = build_story(files)
    stats["total_q"] = stats["mcq"] + stats["ds"] + stats["tl"]

    tmp = os.path.join(ROOT, "build", "_tmp.pdf")
    entries, pages, converged = [], {}, False
    for _attempt in range(6):
        story, _ = build_story(files)
        doc = Doc(tmp)
        doc.build([NextPageTemplate("body")] + cover_story(stats) + [PageBreak()] + toc_story(entries, pages) + story)
        new_entries = doc.toc_entries
        new_pages = {i: e[2] for i, e in enumerate(new_entries)}
        if new_entries == entries and new_pages == pages:
            converged = True
            break
        entries, pages = new_entries, new_pages
    if not converged:
        story, _ = build_story(files)
        Doc(tmp).build(cover_story(stats) + [PageBreak()] + toc_story(entries, pages) + story)
    os.replace(tmp, OUT_PDF)

    print("Đã tạo: %s" % OUT_PDF)
    print("Câu hỏi: TN=%d, ĐS=%d, TL=%d (tổng %d)"
          % (stats["mcq"], stats["ds"], stats["tl"], stats["total_q"]))
    print("Mục lục: %d mục" % len(entries))


if __name__ == "__main__":
    main()
