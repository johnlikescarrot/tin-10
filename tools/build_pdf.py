#!/usr/bin/env python3
"""
Build the Vietnamese midterm-review PDF from the Markdown sources in docs/src/.

Usage (from the repository root):
    python3 tools/build_pdf.py

Requires: reportlab (pip install reportlab) and a DejaVu TTF font.
The script concatenates docs/src/*.md in alphabetical order, writes the merged
Markdown to docs/DeCuong_OnTap_GiuaKiI_TinHoc10_KNTT.md, and renders the PDF
at the repository root. Fonts are looked up in the usual Linux locations;
FONT_DIR may be set to override the search path.
"""

from __future__ import annotations

import html
import os
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "docs" / "src"
MERGED_MD = ROOT / "docs" / "DeCuong_OnTap_GiuaKiI_TinHoc10_KNTT.md"
OUT_PDF = ROOT / "DeCuong_OnTap_GiuaKiI_TinHoc10_KNTT.pdf"

# --------------------------------------------------------------------------
# Palette
# --------------------------------------------------------------------------
NAVY = colors.HexColor("#123A5E")
NAVY_DARK = colors.HexColor("#0C2942")
TEAL = colors.HexColor("#0E7490")
TEAL_LIGHT = colors.HexColor("#E6F2F5")
AMBER = colors.HexColor("#A8620A")
AMBER_LIGHT = colors.HexColor("#FDF3E3")
GREY = colors.HexColor("#4A5568")
LINE = colors.HexColor("#C9D6E0")
BG_SOFT = colors.HexColor("#F4F7FA")
WHITE = colors.white

FONT_DIRS = [
    os.environ.get("FONT_DIR", ""),
    "/usr/share/fonts/truetype/dejavu",
    "/usr/local/share/fonts",
    str(Path.home() / ".fonts"),
]


def find_font(name: str) -> str:
    for d in FONT_DIRS:
        if d and (Path(d) / name).exists():
            return str(Path(d) / name)
    raise SystemExit(f"Không tìm thấy font {name}. Hãy đặt FONT_DIR=/duong/dan/fonts.")


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("DV", find_font("DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("DV-Bold", find_font("DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("DV-Serif", find_font("DejaVuSerif.ttf")))
    pdfmetrics.registerFont(TTFont("DV-Mono", find_font("DejaVuSansMono.ttf")))
    pdfmetrics.registerFontFamily(
        "DV", normal="DV", bold="DV-Bold", italic="DV", boldItalic="DV-Bold"
    )


# --------------------------------------------------------------------------
# Styles
# --------------------------------------------------------------------------
def make_styles():
    s = {}
    s["Body"] = ParagraphStyle(
        "Body", fontName="DV", fontSize=9.6, leading=14.6,
        textColor=colors.HexColor("#1B2733"), alignment=TA_JUSTIFY,
        spaceAfter=5.5, wordWrap=None,
    )
    s["Small"] = ParagraphStyle(
        "Small", parent=s["Body"], fontSize=8.6, leading=12.6, spaceAfter=3.5,
    )
    s["H1"] = ParagraphStyle(
        "H1", fontName="DV-Bold", fontSize=15.2, leading=21,
        textColor=WHITE, backColor=NAVY, borderPadding=(7, 8, 7, 8),
        spaceBefore=13, spaceAfter=12, keepWithNext=True,
    )
    s["H2"] = ParagraphStyle(
        "H2", fontName="DV-Bold", fontSize=12.6, leading=18,
        textColor=WHITE, backColor=TEAL, borderPadding=(5, 7, 5, 7),
        spaceBefore=13, spaceAfter=9, keepWithNext=True,
    )
    s["H3"] = ParagraphStyle(
        "H3", fontName="DV-Bold", fontSize=10.8, leading=15.5,
        textColor=NAVY, spaceBefore=10, spaceAfter=5, keepWithNext=True,
        borderPadding=(0, 0, 0, 0),
    )
    s["H4"] = ParagraphStyle(
        "H4", fontName="DV-Bold", fontSize=9.9, leading=14.2,
        textColor=colors.HexColor("#1B2733"), spaceBefore=7.5,
        spaceAfter=3, keepWithNext=True,
    )
    s["Bullet"] = ParagraphStyle(
        "Bullet", parent=s["Body"], spaceAfter=2.6, leading=13.9,
    )
    s["Bullet2"] = ParagraphStyle(
        "Bullet2", parent=s["Bullet"], fontSize=9.2, leading=13.3,
    )
    s["Note"] = ParagraphStyle(
        "Note", parent=s["Body"], fontSize=9.2, leading=13.6,
        textColor=colors.HexColor("#1E3A4C"), backColor=TEAL_LIGHT,
        borderColor=TEAL, borderWidth=0.9, borderPadding=(6, 7, 6, 7),
        spaceBefore=6, spaceAfter=8,
    )
    s["Warn"] = ParagraphStyle(
        "Warn", parent=s["Note"], backColor=AMBER_LIGHT, borderColor=AMBER,
        textColor=colors.HexColor("#4A3208"),
    )
    s["Answer"] = ParagraphStyle(
        "Answer", parent=s["Body"], fontSize=9.3, leading=13.8,
        backColor=BG_SOFT, borderColor=LINE, borderWidth=0.8,
        borderPadding=(6, 7, 6, 7), spaceBefore=3, spaceAfter=8,
    )
    s["Quote"] = ParagraphStyle(
        "Quote", parent=s["Note"], borderColor=LINE, backColor=BG_SOFT,
    )
    s["TblHead"] = ParagraphStyle(
        "TblHead", fontName="DV-Bold", fontSize=8.5, leading=11.4,
        textColor=WHITE, alignment=TA_LEFT,
    )
    s["TblCell"] = ParagraphStyle(
        "TblCell", fontName="DV", fontSize=8.3, leading=11.5,
        textColor=colors.HexColor("#1B2733"), alignment=TA_LEFT,
    )
    s["TblCellC"] = ParagraphStyle(
        "TblCellC", parent=s["TblCell"], alignment=TA_CENTER,
    )
    s["CoverKicker"] = ParagraphStyle(
        "CoverKicker", fontName="DV-Bold", fontSize=10, leading=15,
        textColor=TEAL, alignment=TA_CENTER,
    )
    s["CoverTitle"] = ParagraphStyle(
        "CoverTitle", fontName="DV-Bold", fontSize=27, leading=35,
        textColor=NAVY_DARK, alignment=TA_CENTER,
    )
    s["CoverSub"] = ParagraphStyle(
        "CoverSub", fontName="DV-Bold", fontSize=14, leading=21,
        textColor=TEAL, alignment=TA_CENTER,
    )
    s["CoverBody"] = ParagraphStyle(
        "CoverBody", parent=s["Body"], fontSize=10.2, leading=16,
        alignment=TA_CENTER, textColor=GREY,
    )
    s["TOCHead"] = ParagraphStyle(
        "TOCHead", fontName="DV-Bold", fontSize=17, leading=23,
        textColor=NAVY, spaceAfter=12,
    )
    return s


# --------------------------------------------------------------------------
# Inline markdown -> reportlab mini-html
# --------------------------------------------------------------------------
def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    # inline code
    text = re.sub(r"`([^`]+)`", r'<font name="DV-Mono" size="8.6" color="#0E7490">\1</font>', text)
    # bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    # soft emphasis -> coloured bold (no italic font registered)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r'<font color="#A8620A"><b>\1</b></font>', text)
    # markdown links -> plain coloured text with the URL when it is external
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<font color="#0E7490">\1</font>', text)
    return text


def rich(text: str, style) -> Paragraph:
    return Paragraph(inline(text), style)


# --------------------------------------------------------------------------
# Document template with running header/footer, TOC, and PDF outlines
# --------------------------------------------------------------------------
class ReviewDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, **kw)
        self.outline_count = 0
        frame = Frame(
            self.leftMargin, self.bottomMargin, self.width, self.height,
            id="main", leftPadding=0, rightPadding=0,
            topPadding=0, bottomPadding=0,
        )
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame], onPage=self.draw_cover),
            PageTemplate(id="body", frames=[frame], onPage=self.draw_body),
        ])

    # -- page decorations -------------------------------------------------
    def draw_cover(self, canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setFillColor(NAVY)
        canvas.rect(0, h - 1.65 * cm, w, 1.65 * cm, stroke=0, fill=1)
        canvas.setFillColor(TEAL)
        canvas.rect(0, h - 1.85 * cm, w, 0.2 * cm, stroke=0, fill=1)
        canvas.setFillColor(BG_SOFT)
        canvas.rect(0, 0, w, 1.25 * cm, stroke=0, fill=1)
        canvas.setFont("DV", 8.4)
        canvas.setFillColor(GREY)
        canvas.drawCentredString(w / 2, 0.72 * cm,
                                 "Tài liệu ôn tập nội bộ · Tin học 10 · Học kì I")
        canvas.setFillColor(WHITE)
        canvas.setFont("DV-Bold", 9.6)
        canvas.drawCentredString(w / 2, h - 1.12 * cm,
                                 "KẾT NỐI TRI THỨC VỚI CUỘC SỐNG  ·  LỚP 10")
        canvas.restoreState()

    def draw_body(self, canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.6)
        canvas.line(self.leftMargin, h - 1.30 * cm, w - self.rightMargin, h - 1.30 * cm)
        canvas.setFont("DV", 7.8)
        canvas.setFillColor(GREY)
        canvas.drawString(self.leftMargin, h - 1.12 * cm,
                          "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I  ·  TIN HỌC 10  ·  KNTT")
        canvas.drawRightString(w - self.rightMargin, h - 1.12 * cm,
                               "Ma trận & đặc tả → kiến thức → câu hỏi → đáp án")
        canvas.line(self.leftMargin, 1.25 * cm, w - self.rightMargin, 1.25 * cm)
        canvas.setFont("DV", 8.2)
        canvas.drawString(self.leftMargin, 0.82 * cm,
                          "Biên soạn từ MA TRAN GIUA KI I - LOP 10.docx")
        canvas.setFont("DV-Bold", 8.8)
        canvas.setFillColor(NAVY)
        canvas.drawRightString(w - self.rightMargin, 0.82 * cm, "Trang %d" % doc.page)
        canvas.restoreState()

    # -- TOC and PDF bookmarks -------------------------------------------
    def beforeDocument(self):
        # multiBuild() renders the story several times; keep bookmark keys
        # identical on every pass so the TOC can converge.
        self.outline_count = 0

    def afterFlowable(self, flowable):
        level = getattr(flowable, "toc_level", None)
        if level is None:
            return
        text = flowable.getPlainText()
        key = "sec-%d" % self.outline_count
        self.outline_count += 1
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=max(0, level - 1), closed=(level > 1))
        if level <= 2:
            self.notify("TOCEntry", (level, text, self.page, key))


# --------------------------------------------------------------------------
# Markdown-ish parser
# --------------------------------------------------------------------------
class Renderer:
    def __init__(self, styles):
        self.s = styles
        self.story = []
        self.col_hint = None
        self.pending_bullets = []

    def add(self, f):
        self.story.append(f)

    def heading(self, text, level):
        style = self.s[{1: "H1", 2: "H2", 3: "H3", 4: "H4"}[level]]
        p = rich(text, style)
        p.toc_level = level
        self.add(p)

    def flush_bullets(self):
        if not self.pending_bullets:
            return
        items = []
        for lvl, txt in self.pending_bullets:
            st = self.s["Bullet"] if lvl <= 1 else self.s["Bullet2"]
            items.append(ListItem(rich(txt, st), leftIndent=12 + 11 * lvl,
                                  value="bulletchar"))
        self.add(ListFlowable(
            items, bulletType="bullet", bulletFontName="DV",
            bulletFontSize=6.6, bulletColor=TEAL,
            leftIndent=13, bulletOffsetY=1.2, start="•",
        ))
        self.add(Spacer(1, 4))
        self.pending_bullets = []

    def table(self, rows, hint):
        header, body = rows[0], rows[1:]
        ncol = len(header)
        # width hint: relative weights
        if hint and len(hint) == ncol:
            weights = [float(x) for x in hint]
        else:
            weights = []
            for c in range(ncol):
                lens = [len(rows[r][c]) for r in range(len(rows)) if c < len(rows[r])]
                avg = (sum(lens) / len(lens)) if lens else 8
                weights.append(max(8, min(46, avg)))
        avail = 17.0 * cm
        total = sum(weights)
        widths = [avail * w / total for w in weights]

        data = [[rich(c, self.s["TblHead"]) for c in header]]
        for row in body:
            row = (row + [""] * ncol)[:ncol]
            data.append([rich(c, self.s["TblCell"]) for c in row])

        t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
        cmds = [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("GRID", (0, 0), (-1, -1), 0.42, LINE),
            ("LINEBELOW", (0, 0), (-1, 0), 1.0, NAVY_DARK),
            ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
            ("TOPPADDING", (0, 0), (-1, -1), 3.6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3.6),
        ]
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), BG_SOFT))
        t.setStyle(TableStyle(cmds))
        self.add(t)
        self.add(Spacer(1, 8))

    def paragraph(self, text):
        self.add(rich(text, self.s["Body"]))

    def render(self, md: str):
        lines = md.split("\n")
        i = 0
        table_buf = []
        while i < len(lines):
            raw = lines[i]
            line = raw.rstrip()
            stripped = line.strip()

            # ---- table rows ----
            if stripped.startswith("|") and stripped.endswith("|"):
                cells = [c.strip() for c in stripped[1:-1].split("|")]
                if not re.match(r"^[\s:\-|]+$", stripped):
                    table_buf.append(cells)
                i += 1
                continue
            if table_buf:
                self.flush_bullets()
                self.table(table_buf, self.col_hint)
                table_buf = []
                self.col_hint = None
                continue

            if not stripped:
                self.flush_bullets()
                i += 1
                continue

            # ---- directives ----
            if stripped.startswith("<!--"):
                m = re.match(r"<!--\s*COLS\s+([\d.,\s]+)\s*-->", stripped)
                if m:
                    self.col_hint = [x.strip() for x in m.group(1).split(",")]
                elif "PAGEBREAK" in stripped:
                    self.flush_bullets()
                    self.add(PageBreak())
                elif "TOC" in stripped:
                    self.flush_bullets()
                    self.add(Paragraph("MỤC LỤC", self.s["TOCHead"]))
                    toc = TableOfContents()
                    toc.levelStyles = [
                        ParagraphStyle("TOC1", fontName="DV-Bold", fontSize=10.2,
                                       leading=19, textColor=NAVY, spaceBefore=7,
                                       firstLineIndent=-12, leftIndent=12),
                        ParagraphStyle("TOC2", fontName="DV", fontSize=9.2,
                                       leading=15.5, textColor=colors.HexColor("#1B2733"),
                                       firstLineIndent=-10, leftIndent=26),
                        ParagraphStyle("TOC3", fontName="DV", fontSize=8.6,
                                       leading=13.5, textColor=GREY,
                                       firstLineIndent=-8, leftIndent=40),
                    ]
                    self.add(toc)
                    self.add(PageBreak())
                else:
                    m2 = re.match(r"<!--\s*SPACER\s+([\d.]+)\s*-->", stripped)
                    if m2:
                        self.add(Spacer(1, float(m2.group(1)) * mm))
                i += 1
                continue

            # ---- headings ----
            m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
            if m:
                self.flush_bullets()
                self.heading(m.group(2), len(m.group(1)))
                i += 1
                continue

            # ---- horizontal rule ----
            if re.match(r"^[-*_]{3,}$", stripped):
                self.flush_bullets()
                self.add(HRFlowable(width="100%", thickness=0.8, color=LINE,
                                    spaceBefore=6, spaceAfter=8))
                i += 1
                continue

            # ---- bullets ----
            m = re.match(r"^(\s*)-\s+(.*)$", line)
            if m:
                lvl = min(2, len(m.group(1)) // 2)
                self.pending_bullets.append((lvl, m.group(2)))
                i += 1
                continue

            # ---- numbered items ----
            m = re.match(r"^\s*(\d+)\.\s+(.*)$", line)
            if m:
                self.flush_bullets()
                self.add(rich("**%s.** %s" % (m.group(1), m.group(2)), self.s["Bullet"]))
                i += 1
                continue

            # ---- callouts ----
            if stripped.startswith(">"):
                self.flush_bullets()
                content = stripped.lstrip(">").strip()
                if content.upper().startswith("LƯU Ý") or content.upper().startswith("CẢNH BÁO") \
                        or content.upper().startswith("SAI "):
                    st = self.s["Warn"]
                elif re.match(r"^\*\*(Đáp án|Hướng dẫn|Gợi ý|Trả lời)", content):
                    st = self.s["Answer"]
                else:
                    st = self.s["Note"]
                self.add(rich(content, st))
                i += 1
                continue

            # ---- plain paragraph ----
            self.flush_bullets()
            self.paragraph(stripped)
            i += 1

        if table_buf:
            self.table(table_buf, self.col_hint)
        self.flush_bullets()
        return self.story


# --------------------------------------------------------------------------
# Cover
# --------------------------------------------------------------------------
def cover_flowables(s):
    f = [
        Spacer(1, 1.2 * cm),
        Paragraph("HỌC KÌ I  ·  NĂM HỌC 2026 – 2027", s["CoverKicker"]),
        Spacer(1, 0.65 * cm),
        Paragraph("ĐỀ CƯƠNG ÔN TẬP<br/>GIỮA KÌ I", s["CoverTitle"]),
        Spacer(1, 0.35 * cm),
        Paragraph("MÔN TIN HỌC  ·  LỚP 10", s["CoverSub"]),
        Spacer(1, 0.2 * cm),
        Paragraph("Bộ sách <b>Kết nối tri thức với cuộc sống</b>", s["CoverBody"]),
        Spacer(1, 0.95 * cm),
    ]
    info = [
        ["Phạm vi kiến thức", "Chủ đề 1, 2, 3 (Bài 1 – 11) – toàn bộ chương trình đã học tới giữa kì I"],
        ["Nguồn biên soạn", "MA TRAN GIUA KI I - LOP 10.docx (ma trận đề + đặc tả đề kiểm tra giữa kì I)"],
        ["Cấu trúc đề", "45 phút · 70% trắc nghiệm + 30% tự luận · 20 TN + 2 ĐS + 3 TL · thang 10 điểm"],
        ["Nội dung tài liệu", "Bản đồ kiến thức · 36 cặp câu hỏi – đáp án từ đặc tả · ngân hàng đề luyện · đáp án chi tiết · toàn văn ma trận gốc"],
    ]
    data = [[rich("**%s**" % a, s["TblCell"]), rich(b, s["TblCell"])] for a, b in info]
    t = Table(data, colWidths=[4.05 * cm, 12.95 * cm], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), TEAL_LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    f += [
        t,
        Spacer(1, 0.9 * cm),
        Paragraph(
            "<b>Nguyên tắc biên soạn:</b> giữ nguyên 100% nội dung của ma trận và đặc tả gốc; "
            "mỗi yêu cầu cần đạt được chuyển thành một cặp câu hỏi – đáp án; "
            "bổ sung phần lí thuyết theo SGK Kết nối tri thức và ngân hàng câu hỏi luyện tập có đáp án.",
            s["Note"],
        ),
        Spacer(1, 0.35 * cm),
        Paragraph("Tài liệu gồm 7 phần và 4 phụ lục · có mục lục và đánh dấu trang (bookmark) để tra cứu nhanh.",
                  s["CoverBody"]),
        NextPageTemplate("body"),
        PageBreak(),
    ]
    return f


# --------------------------------------------------------------------------
def main():
    register_fonts()
    styles = make_styles()

    src_files = sorted(SRC_DIR.glob("*.md"))
    if not src_files:
        raise SystemExit(f"Không có tệp nguồn Markdown trong {SRC_DIR}")
    parts = []
    for p in src_files:
        parts.append("<!-- FILE: %s -->\n" % p.name)
        parts.append(p.read_text(encoding="utf-8").strip() + "\n")
    md = "\n".join(parts)
    MERGED_MD.write_text(md, encoding="utf-8")
    print("Merged Markdown ->", MERGED_MD, "(%d chars)" % len(md))

    doc = ReviewDocTemplate(
        str(OUT_PDF), pagesize=A4,
        leftMargin=2.0 * cm, rightMargin=2.0 * cm,
        topMargin=1.75 * cm, bottomMargin=1.65 * cm,
        title="Đề cương ôn tập giữa kì I - Tin học 10 - Kết nối tri thức",
        author="Biên soạn từ ma trận đề kiểm tra giữa kì I môn Tin học 10",
        subject="Ôn tập giữa kì I Tin học 10; ma trận, đặc tả, câu hỏi và đáp án",
        keywords="Tin học 10, Kết nối tri thức, giữa kì I, ma trận đề, đặc tả, đề cương ôn tập",
    )
    story = cover_flowables(styles)
    r = Renderer(styles)
    story += r.render(md)
    doc.multiBuild(story, maxPasses=6)
    print("PDF ->", OUT_PDF, "(%d bytes)" % OUT_PDF.stat().st_size)


if __name__ == "__main__":
    main()
