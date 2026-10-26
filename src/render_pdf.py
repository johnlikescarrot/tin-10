# -*- coding: utf-8 -*-
"""Kết xuất danh sách khối nội dung sang PDF A4 bằng ReportLab."""
from __future__ import annotations

import re
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, HRFlowable, LongTable,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = ROOT / "assets" / "fonts"

# ------------------------------------------------------------------ màu sắc
NAVY = colors.HexColor("#15344B")
TEAL = colors.HexColor("#0E7472")
ORANGE = colors.HexColor("#C4622D")
GREEN = colors.HexColor("#2E7D57")
PURPLE = colors.HexColor("#5B4A8A")
TEXT = colors.HexColor("#20303C")
MUTED = colors.HexColor("#5F7280")
GRID = colors.HexColor("#C9D8DE")
ZEBRA = colors.HexColor("#F4F9FA")
PALE = colors.HexColor("#EEF5F6")
WHITE = colors.white

BOX_KINDS = {
    "tip": (TEAL, colors.HexColor("#EAF6F5")),
    "note": (NAVY, colors.HexColor("#EDF3F7")),
    "warn": (ORANGE, colors.HexColor("#FFF3E8")),
    "example": (GREEN, colors.HexColor("#EDF7F0")),
    "memory": (PURPLE, colors.HexColor("#F2EFFA")),
}

PAGE_W, PAGE_H = A4
LEFT = RIGHT = 42
CONTENT_W = PAGE_W - LEFT - RIGHT


# ------------------------------------------------------------------ font
def register_fonts():
    files = {
        "BVP": "BeVietnamPro-Regular.ttf",
        "BVP-Bold": "BeVietnamPro-Bold.ttf",
        "BVP-Italic": "BeVietnamPro-Italic.ttf",
        "BVP-BoldItalic": "BeVietnamPro-BoldItalic.ttf",
        "BVP-Medium": "BeVietnamPro-Medium.ttf",
    }
    for name, fn in files.items():
        path = FONT_DIR / fn
        if not path.exists():
            raise SystemExit(f"Thiếu font: {path}. Hãy chạy tools/fetch_fonts.py hoặc dùng font hệ thống.")
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily(
        "BVP", normal="BVP", bold="BVP-Bold",
        italic="BVP-Italic", boldItalic="BVP-BoldItalic")


# Be Vietnam Pro không có các kí tự mũi tên / số tròn / sao.  Thay bằng kí tự
# tương đương có trong font để PDF không bị ô trống.  (Bản Markdown giữ nguyên.)
SYMBOL_MAP = str.maketrans({
    "\u2192": "\u00bb",   # →  -> »
    "\u2194": "\u2039\u203a",  # ↔ -> ‹›
    "\u2460": "(1)", "\u2461": "(2)", "\u2462": "(3)",
    "\u2463": "(4)", "\u2464": "(5)", "\u2465": "(6)",
    "\u2605": "\u2022",   # ★ -> •
})


def inline(text):
    """Chuyển markup gọn sang markup của ReportLab (đã escape XML)."""
    s = escape(str(text))
    s = re.sub(r"\*\*(.+?)\*\*", lambda m: "<b>" + m.group(1) + "</b>", s, flags=re.S)
    s = re.sub(r"\*(.+?)\*", lambda m: "<i>" + m.group(1) + "</i>", s, flags=re.S)
    s = re.sub(r"`(.+?)`",
               lambda m: '<font face="BVP-Medium" color="#0E7472">' + m.group(1) + "</font>",
               s, flags=re.S)
    s = re.sub(r"\{\{(.+?)\}\}",
               lambda m: '<font color="#C4622D"><b>' + m.group(1) + "</b></font>",
               s, flags=re.S)
    return s.replace("\n", "<br/>").translate(SYMBOL_MAP)


def plain(text):
    """Bỏ markup để dùng cho mục lục / chú thích."""
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", str(text))
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    s = s.replace("`", "").replace("{{", "").replace("}}", "")
    return s.replace("\n", " ")


# ------------------------------------------------------------------ styles
def make_styles():
    S = {}
    S["H1"] = ParagraphStyle(
        "H1", fontName="BVP-Bold", fontSize=13.2, leading=18.5,
        textColor=WHITE, backColor=NAVY, borderPadding=(7, 9, 7, 9),
        spaceBefore=17, spaceAfter=11, leftIndent=0, keepWithNext=1,
        allowWidows=0, allowOrphans=0)
    S["TOCTitle"] = ParagraphStyle(
        "TOCTitle", parent=S["H1"], spaceBefore=0)
    S["H2"] = ParagraphStyle(
        "H2", fontName="BVP-Bold", fontSize=11.2, leading=15.5,
        textColor=TEAL, spaceBefore=14, spaceAfter=5,
        borderPadding=(0, 0, 2, 0), keepWithNext=1,
        allowWidows=0, allowOrphans=0)
    S["H3"] = ParagraphStyle(
        "H3", fontName="BVP-Bold", fontSize=9.8, leading=13.5,
        textColor=NAVY, spaceBefore=10, spaceAfter=4, keepWithNext=1,
        allowWidows=0, allowOrphans=0)
    S["body"] = ParagraphStyle(
        "body", fontName="BVP", fontSize=9.15, leading=13.9,
        textColor=TEXT, alignment=TA_JUSTIFY, spaceAfter=5.5)
    S["lead"] = ParagraphStyle(
        "lead", fontName="BVP", fontSize=9.6, leading=14.8,
        textColor=NAVY, backColor=PALE, borderPadding=(7, 8, 7, 8),
        alignment=TA_JUSTIFY, spaceBefore=3, spaceAfter=10)
    S["small"] = ParagraphStyle(
        "small", fontName="BVP", fontSize=8.25, leading=12.1,
        textColor=MUTED, alignment=TA_JUSTIFY, spaceAfter=4)
    S["verbatim"] = ParagraphStyle(
        "verbatim", fontName="BVP", fontSize=8.5, leading=12.4,
        textColor=TEXT, alignment=TA_JUSTIFY, leftIndent=14,
        spaceAfter=2.5)
    S["bullet"] = ParagraphStyle(
        "bullet", fontName="BVP", fontSize=9.05, leading=13.6,
        textColor=TEXT, alignment=TA_JUSTIFY, leftIndent=13,
        bulletIndent=2, bulletFontName="BVP", bulletFontSize=8.5,
        spaceAfter=3.2)
    S["number"] = ParagraphStyle(
        "number", fontName="BVP", fontSize=9.05, leading=13.6,
        textColor=TEXT, alignment=TA_JUSTIFY, leftIndent=16,
        bulletIndent=1, bulletFontName="BVP-Bold", bulletFontSize=8.8,
        spaceAfter=3.2)
    S["caption"] = ParagraphStyle(
        "caption", fontName="BVP-Italic", fontSize=8.0, leading=11.6,
        textColor=MUTED, spaceBefore=2, spaceAfter=5, alignment=TA_LEFT)
    S["boxtitle"] = ParagraphStyle(
        "boxtitle", fontName="BVP-Bold", fontSize=9.3, leading=13.2,
        textColor=NAVY, spaceAfter=4)
    S["boxline"] = ParagraphStyle(
        "boxline", fontName="BVP", fontSize=8.85, leading=13.2,
        textColor=TEXT, alignment=TA_JUSTIFY, leftIndent=12,
        bulletIndent=2, bulletFontName="BVP", bulletFontSize=8.2,
        spaceAfter=2.6)
    S["qhead"] = ParagraphStyle(
        "qhead", fontName="BVP-Bold", fontSize=9.35, leading=13.4,
        textColor=WHITE, spaceAfter=0)
    S["qq"] = ParagraphStyle(
        "qq", fontName="BVP-Italic", fontSize=9.0, leading=13.5,
        textColor=NAVY, alignment=TA_JUSTIFY, spaceAfter=3)
    S["qa"] = ParagraphStyle(
        "qa", fontName="BVP", fontSize=9.0, leading=13.6,
        textColor=TEXT, alignment=TA_JUSTIFY, spaceAfter=2)
    S["option"] = ParagraphStyle(
        "option", fontName="BVP", fontSize=8.95, leading=12.8,
        textColor=TEXT, alignment=TA_LEFT)
    S["ansline"] = ParagraphStyle(
        "ansline", fontName="BVP", fontSize=8.6, leading=12.4,
        textColor=GREEN, alignment=TA_JUSTIFY, spaceAfter=3)
    # cover
    S["cv_kicker"] = ParagraphStyle("cv_kicker", fontName="BVP-Medium", fontSize=10,
                                    leading=15, textColor=TEAL, alignment=TA_CENTER,
                                    spaceAfter=16)
    S["cv_title"] = ParagraphStyle("cv_title", fontName="BVP-Bold", fontSize=29,
                                   leading=36, textColor=NAVY, alignment=TA_CENTER,
                                   spaceAfter=2)
    S["cv_title2"] = ParagraphStyle("cv_title2", fontName="BVP-Bold", fontSize=29,
                                    leading=36, textColor=TEAL, alignment=TA_CENTER,
                                    spaceAfter=12)
    S["cv_sub"] = ParagraphStyle("cv_sub", fontName="BVP-Bold", fontSize=15,
                                 leading=22, textColor=NAVY, alignment=TA_CENTER,
                                 spaceAfter=6)
    S["cv_small"] = ParagraphStyle("cv_small", fontName="BVP", fontSize=9.8,
                                   leading=15, textColor=MUTED, alignment=TA_CENTER,
                                   spaceAfter=6)
    S["cv_note"] = ParagraphStyle("cv_note", fontName="BVP", fontSize=8.4,
                                  leading=12.6, textColor=MUTED, alignment=TA_JUSTIFY)
    S["toc0"] = ParagraphStyle("toc0", fontName="BVP-Bold", fontSize=9.7,
                               leading=17, textColor=NAVY, spaceBefore=6)
    S["toc1"] = ParagraphStyle("toc1", fontName="BVP", fontSize=8.7,
                               leading=13.6, textColor=TEXT, leftIndent=17,
                               firstLineIndent=-9)
    return S


# ------------------------------------------------------------------ helpers
def _cell(text, size, bold=False, color=TEXT, align=TA_LEFT):
    st = ParagraphStyle(
        f"cell{size}{'b' if bold else ''}{color}{align}",
        fontName="BVP-Bold" if bold else "BVP",
        fontSize=size, leading=size * 1.36,
        textColor=color, alignment=align)
    return Paragraph(inline(text), st)


def make_table(block, S):
    head = block["head"]
    rows = block["rows"]
    fs = block.get("fs", 8.4)
    widths = block.get("widths") or [CONTENT_W / len(head)] * len(head)
    scale = min(1.0, CONTENT_W / sum(widths))
    widths = [w * scale for w in widths]
    ncol = len(head)

    out = []
    if block.get("caption"):
        out.append(Paragraph(inline(block["caption"]), S["caption"]))

    hrows = 1 if head and not isinstance(head[0], list) else len(head)
    hdata = [head] if hrows == 1 else head
    data = [[_cell(c, fs, bold=True, color=WHITE, align=TA_CENTER) for c in row]
            for row in hdata]
    body_align = TA_CENTER if block.get("align") == "center" else TA_LEFT
    for r in rows:
        rr = list(r) + [""] * (ncol - len(r))
        data.append([_cell(c, fs, align=body_align) for c in rr[:ncol]])

    pad = 1.4 if fs < 7 else 4
    tbl = LongTable(data, colWidths=widths, repeatRows=hrows, splitByRow=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, hrows - 1), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE" if fs < 7 else "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("LINEBELOW", (0, hrows - 1), (-1, hrows - 1), 0.9, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), pad),
        ("RIGHTPADDING", (0, 0), (-1, -1), pad),
        ("TOPPADDING", (0, 0), (-1, -1), 3.4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.4),
    ]
    if block.get("zebra", True):
        style.append(("ROWBACKGROUNDS", (0, hrows), (-1, -1), [WHITE, ZEBRA]))
    tbl.setStyle(TableStyle(style))
    out.append(tbl)
    out.append(Spacer(1, 7))
    return out


def make_box(block, S, accent=None, bg=None, title_prefix=""):
    kind = block.get("kind", "tip")
    accent, bg = BOX_KINDS[kind] if accent is None else (accent, bg or WHITE)
    data = [[Paragraph(inline(title_prefix + block["title"]), S["boxtitle"])]]
    for line in block["lines"]:
        data.append([Paragraph(inline(line), S["boxline"], bulletText="•")])
    t = LongTable(data, colWidths=[CONTENT_W - 10], splitByRow=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, accent),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 2),
        ("TOPPADDING", (0, 1), (-1, -1), 1.5),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [t, Spacer(1, 8)]


def make_qaitem(block, S):
    accent, bg = TEAL, colors.HexColor("#F0F8F7")
    head = f"{block['code']}  ·  {block['form']}"
    hd = ParagraphStyle("qahd", fontName="BVP-Bold", fontSize=9.0, leading=12.8,
                        textColor=WHITE)
    data = [
        [Paragraph(inline(head), hd)],
        [Paragraph("<b>YÊU CẦU (nguyên văn):</b> " + inline(block["q"]), S["qq"])],
        [Paragraph("<b>ĐÁP ÁN:</b> " + inline(block["a"]), S["qa"])],
        [Paragraph("<b>Xem thêm:</b> mục " + inline(block["see"]), S["small"])],
    ]
    t = LongTable(data, colWidths=[CONTENT_W - 10], splitByRow=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), TEAL),
        ("BACKGROUND", (0, 1), (0, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.4, TEAL),
        ("BOX", (0, 0), (-1, -1), 0.3, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [t, Spacer(1, 7)]


def make_mcq(block, S):
    out = [Paragraph(f"<b>{inline(block['n'])}.</b> " + inline(block["t"]), S["body"])]
    opts = block["options"]
    labels = "ABCD"
    data = []
    for i in range(0, len(opts), 2):
        row = []
        for j in (i, i + 1):
            if j < len(opts):
                row.append(Paragraph(f"<b>{labels[j]}.</b> " + inline(opts[j]), S["option"]))
            else:
                row.append("")
        data.append(row)
    t = Table(data, colWidths=[CONTENT_W / 2 - 4, CONTENT_W / 2 - 4])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7FAFB")),
        ("BOX", (0, 0), (-1, -1), 0.3, GRID),
        ("INNERGRID", (0, 0), (-1, -1), 0.25, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    out += [t, Spacer(1, 3)]
    out.append(Paragraph(
        f"<b>Đáp án: {block['ans']}.</b> " + inline(block["explain"])
        + f" <font color='#8A9AA4'>[{inline(block['tag'])}]</font>", S["ansline"]))
    out.append(Spacer(1, 5))
    return out


def make_tfq(block, S):
    out = [Paragraph(f"<b>{inline(block['n'])}.</b> " + inline(block["t"]), S["body"])]
    data = [["Ý", "Nhận định", "Mức độ", "Đ/S"]]
    for i, (lab, text, level) in enumerate(block["statements"]):
        data.append([lab, text, level, block["answers"][i]])
    t = LongTable(
        [[_cell(c, 8.2, bold=(r == 0), color=(WHITE if r == 0 else TEXT),
                align=TA_CENTER if (r == 0 or j in (0, 2, 3)) else TA_LEFT)
          for j, c in enumerate(row)]
         for r, row in enumerate(data)],
        colWidths=[26, CONTENT_W - 26 - 68 - 36, 68, 36], repeatRows=1, splitByRow=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, ZEBRA]),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.2),
    ]))
    out += [t, Spacer(1, 3),
            Paragraph("<b>Giải thích:</b> " + inline(block["explain"]), S["ansline"]),
            Spacer(1, 6)]
    return out


def make_frq(block, S):
    out = [Paragraph(f"<b>{inline(block['n'])}.</b> " + inline(block["t"]), S["body"]),
           Paragraph("<b>" + inline(block["tag"]) + "</b>", S["small"])]
    out += make_box({"title": "Hướng dẫn chấm / gợi ý đáp án",
                     "lines": block["rubric"], "kind": "example"}, S)
    return out


def make_check(block, S):
    out = [Paragraph("<b>" + inline(block["title"]) + "</b>", S["H3"])]
    data = [["", item] for item in block["items"]]
    rows = [["", Paragraph(inline(item), ParagraphStyle(
        f"chk{i}", fontName="BVP", fontSize=8.9, leading=13.2, textColor=TEXT,
        alignment=TA_JUSTIFY))] for i, item in enumerate(block["items"])]
    t = LongTable(rows, colWidths=[16, CONTENT_W - 16], splitByRow=1)
    st = [("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("LEFTPADDING", (0, 0), (-1, -1), 2),
          ("RIGHTPADDING", (0, 0), (-1, -1), 3),
          ("TOPPADDING", (0, 0), (-1, -1), 3),
          ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]
    for i in range(len(rows)):
        st.append(("BOX", (0, i), (0, i), 0.55, MUTED))
    t.setStyle(TableStyle(st))
    out += [t, Spacer(1, 8)]
    return out


def make_cover(S):
    out = [
        Spacer(1, 52),
        Paragraph("TÀI LIỆU ÔN TẬP DÀNH CHO HỌC SINH LỚP 10", S["cv_kicker"]),
        Spacer(1, 14),
        Paragraph("ĐỀ CƯƠNG ÔN TẬP", S["cv_title"]),
        Paragraph("GIỮA KÌ I", S["cv_title2"]),
        HRFlowable(width="62%", thickness=1.4, color=ORANGE,
                   spaceBefore=4, spaceAfter=14, hAlign="CENTER"),
        Paragraph("MÔN TIN HỌC 10", S["cv_sub"]),
        Paragraph("Theo bộ sách KẾT NỐI TRI THỨC VỚI CUỘC SỐNG", S["cv_small"]),
        Paragraph("Biên soạn từ <b>Ma trận</b> và <b>Đặc tả đề kiểm tra giữa kì I</b>",
                  S["cv_small"]),
        Spacer(1, 22),
    ]
    info = [
        ["45 phút", "10 điểm", "3 chủ đề · 6 đơn vị", "35 yêu cầu cần đạt"],
        ["Thời gian làm bài", "Thang điểm", "Phạm vi ôn tập (Bài 1–11)",
         "100% có câu hỏi và đáp án"],
    ]
    data = []
    for r, row in enumerate(info):
        data.append([Paragraph(inline(c), ParagraphStyle(
            f"cvi{r}{j}", fontName="BVP-Bold" if r == 0 else "BVP",
            fontSize=12 if r == 0 else 7.6, leading=17 if r == 0 else 11,
            textColor=NAVY if r == 0 else MUTED, alignment=TA_CENTER))
            for j, c in enumerate(row)])
    t = Table(data, colWidths=[CONTENT_W / 4] * 4)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.7, TEAL),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, GRID),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    out += [t, Spacer(1, 24)]
    out += make_box({
        "title": "CÁCH DÙNG ĐỀ CƯƠNG NÀY",
        "kind": "note",
        "lines": [
            "**Bước 1 –** đọc Phần 0 để biết đề thi hỏi gì, rồi nhìn Bản đồ kiến thức (Phần 1).",
            "**Bước 2 –** học lần lượt Phần 2, 3, 4: mỗi phần có sơ đồ, bảng kiến thức, "
            "ví dụ và hộp “Ghi nhớ nhanh”.",
            "**Bước 3 –** tự trả lời 35 câu ở Phần 5 (đây là toàn bộ yêu cầu của bản đặc tả gốc).",
            "**Bước 4 –** làm đề thi thử ở Phần 6 trong 45 phút và tự chấm theo đáp án.",
            "**Bước 5 –** tick Phiếu tự kiểm tra ở Phụ lục D; ô nào chưa tick thì quay lại mục tương ứng.",
        ]}, S)
    out += [
        Spacer(1, 10),
        Paragraph("Ghi chú trung thực: tài liệu gốc là <b>ma trận + đặc tả đề</b>, "
                  "không chứa sẵn câu hỏi và đáp án. Đề cương giữ nguyên toàn bộ văn bản gốc ở "
                  "<b>Phụ lục A</b>, chuyển 35/35 yêu cầu thành câu hỏi có đáp án ở <b>Phần 5</b> "
                  "và bổ sung đề thi thử có đáp án ở <b>Phần 6</b>.", S["cv_note"]),
        NextPageTemplate("Body"),
    ]
    return out


# ------------------------------------------------------------------ doc template
class OutlineDoc(BaseDocTemplate):
    def __init__(self, filename, **kw):
        BaseDocTemplate.__init__(self, filename, **kw)
        cover_frame = Frame(LEFT, 46, CONTENT_W, PAGE_H - 46 - 46, id="cover")
        body_frame = Frame(LEFT, 46, CONTENT_W, PAGE_H - 52 - 46, id="body")
        self.addPageTemplates([
            PageTemplate(id="Cover", frames=[cover_frame], onPage=self.cover_page),
            PageTemplate(id="Body", frames=[body_frame], onPage=self.body_page),
        ])

    @staticmethod
    def cover_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H - 12, PAGE_W, 12, stroke=0, fill=1)
        canvas.setFillColor(TEAL)
        canvas.rect(0, 0, PAGE_W, 7, stroke=0, fill=1)
        canvas.setFont("BVP", 8)
        canvas.setFillColor(MUTED)
        canvas.drawCentredString(PAGE_W / 2, 24, "Đề cương ôn tập giữa kì I · Tin học 10 · Kết nối tri thức với cuộc sống")
        canvas.restoreState()

    @staticmethod
    def body_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H - 27, PAGE_W, 27, stroke=0, fill=1)
        canvas.setFont("BVP-Bold", 7.4)
        canvas.setFillColor(WHITE)
        canvas.drawString(LEFT, PAGE_H - 18,
                          "ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I  ·  TIN HỌC 10  ·  KẾT NỐI TRI THỨC VỚI CUỘC SỐNG")
        canvas.setStrokeColor(GRID)
        canvas.setLineWidth(0.5)
        canvas.line(LEFT, 39, PAGE_W - RIGHT, 39)
        canvas.setFont("BVP", 7.4)
        canvas.setFillColor(MUTED)
        canvas.drawString(LEFT, 27, "Biên soạn từ MA TRAN GIUA KI I - LOP 10.docx")
        canvas.drawRightString(PAGE_W - RIGHT, 27, f"Trang {doc.page}")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            if flowable.style.name == "H1":
                self.notify("TOCEntry", (0, plain(flowable.getPlainText()), self.page, None))
            elif flowable.style.name == "H2":
                self.notify("TOCEntry", (1, plain(flowable.getPlainText()), self.page, None))


# ------------------------------------------------------------------ render
def render(blocks, out_path):
    register_fonts()
    S = make_styles()
    story = []
    for b in blocks:
        k = b["k"]
        if k == "cover":
            story += make_cover(S)
        elif k == "toc":
            story.append(Paragraph("MỤC LỤC", S["TOCTitle"]))
            toc = TableOfContents()
            toc.levelStyles = [S["toc0"], S["toc1"]]
            toc.dotsMinLevel = 0
            story += [toc, Spacer(1, 10)]
            story.append(Paragraph(
                "Gợi ý: in riêng Bảng 1.2 (6 móc nhớ) và Bảng 5.1 (35 yêu cầu) "
                "để mang theo ôn tập nhanh.", S["small"]))
        elif k == "h1":
            story.append(Paragraph(inline(b["t"]), S["H1"]))
        elif k == "h2":
            # keepWithNext giữ tiêu đề với khối nội dung ngay sau (không chèn
            # flowable trung gian, nếu không tiêu đề có thể bị bỏ lại cuối trang).
            story.append(Paragraph(inline(b["t"]), S["H2"]))
        elif k == "h3":
            story.append(Paragraph(inline(b["t"]), S["H3"]))
        elif k == "p":
            story.append(Paragraph(inline(b["t"]), S.get(b.get("cls", "body"), S["body"])))
        elif k == "list":
            style = S["number"] if b["cls"] == "ol" else S["bullet"]
            for i, item in enumerate(b["items"], 1):
                bt = f"{i}." if b["cls"] == "ol" else "•"
                story.append(Paragraph(inline(item), style, bulletText=bt))
            story.append(Spacer(1, 3))
        elif k == "table":
            story += make_table(b, S)
        elif k == "box":
            story += make_box(b, S)
        elif k == "pagebreak":
            story.append(PageBreak())
        elif k == "spacer":
            story.append(Spacer(1, b.get("h", 6)))
        elif k == "rule":
            story.append(HRFlowable(width="100%", thickness=0.6, color=GRID,
                                    spaceBefore=5, spaceAfter=5))
        elif k == "mcq":
            story += make_mcq(b, S)
        elif k == "tfq":
            story += make_tfq(b, S)
        elif k == "frq":
            story += make_frq(b, S)
        elif k == "qagroup":
            story.append(Paragraph(
                inline(b["t"]) + f"  <font size='8' color='#5F7280'>(ôn ở {inline(b['ref'])})</font>",
                S["H2"]))
        elif k == "qaitem":
            story += make_qaitem(b, S)
        elif k == "check":
            story += make_check(b, S)
        elif k in ("qabank", "src_appendix"):
            raise RuntimeError(f"Khối {k} chưa được mở rộng bởi outline_data.build_blocks().")
        else:
            raise RuntimeError(f"Không biết khối: {k}")

    doc = OutlineDoc(
        str(out_path), pagesize=A4,
        leftMargin=LEFT, rightMargin=RIGHT, topMargin=52, bottomMargin=46,
        title="Đề cương ôn tập giữa kì I - Tin học 10 (Kết nối tri thức với cuộc sống)",
        author="Đề cương ôn tập Tin học 10",
        subject="Ma trận và đặc tả đề kiểm tra giữa kì I môn Tin học 10")
    doc.multiBuild(story)
    return out_path
