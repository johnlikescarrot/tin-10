#!/usr/bin/env python3
"""Build the Vietnamese Tin học 10 midterm review PDF from Markdown."""
from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "on-tap-giua-ki-i-tin-hoc-10.md"
OUTPUT = ROOT / "docs" / "on-tap-giua-ki-i-tin-hoc-10.pdf"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

NAVY = colors.HexColor("#18324B")
TEAL = colors.HexColor("#087E8B")
INK = colors.HexColor("#243447")
MUTED = colors.HexColor("#627286")
PALE_BLUE = colors.HexColor("#EDF5F8")
PALE_TEAL = colors.HexColor("#E8F5F3")
PALE_GOLD = colors.HexColor("#FFF7E9")
GRID = colors.HexColor("#D6E0E7")
WHITE = colors.white

PAGE_W, PAGE_H = A4
LEFT = 19 * mm
RIGHT = 19 * mm
TOP = 19 * mm
BOTTOM = 17 * mm
CONTENT_W = PAGE_W - LEFT - RIGHT


def register_fonts() -> None:
    regular = FONT_DIR / "DejaVuSans.ttf"
    bold = FONT_DIR / "DejaVuSans-Bold.ttf"
    mono = FONT_DIR / "DejaVuSansMono.ttf"
    mono_bold = FONT_DIR / "DejaVuSansMono-Bold.ttf"
    for path in (regular, bold, mono, mono_bold):
        if not path.exists():
            raise FileNotFoundError(
                f"Required font not found: {path}. Install the DejaVu Sans font package."
            )
    pdfmetrics.registerFont(TTFont("DejaVu", str(regular)))
    pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(bold)))
    pdfmetrics.registerFont(TTFont("DejaVuMono", str(mono)))
    pdfmetrics.registerFont(TTFont("DejaVuMono-Bold", str(mono_bold)))
    # The minimal workspace font package has no oblique face. Map italics to the
    # regular face rather than letting ReportLab fall back to a non-Unicode font.
    pdfmetrics.registerFontFamily(
        "DejaVu",
        normal="DejaVu",
        bold="DejaVu-Bold",
        italic="DejaVu",
        boldItalic="DejaVu-Bold",
    )


def make_styles():
    base = getSampleStyleSheet()
    styles = {}
    styles["Body"] = ParagraphStyle(
        "Body",
        parent=base["BodyText"],
        fontName="DejaVu",
        fontSize=9.15,
        leading=13.2,
        textColor=INK,
        spaceAfter=5.5,
        alignment=TA_LEFT,
        allowWidows=0,
        allowOrphans=0,
        splitLongWords=1,
    )
    styles["H1"] = ParagraphStyle(
        "H1",
        fontName="DejaVu-Bold",
        fontSize=18,
        leading=23,
        textColor=NAVY,
        spaceBefore=8,
        spaceAfter=11,
        keepWithNext=1,
        borderColor=TEAL,
        borderWidth=0,
        borderPadding=0,
    )
    styles["H2"] = ParagraphStyle(
        "H2",
        fontName="DejaVu-Bold",
        fontSize=12.2,
        leading=16,
        textColor=TEAL,
        spaceBefore=9,
        spaceAfter=5,
        keepWithNext=1,
    )
    styles["H3"] = ParagraphStyle(
        "H3",
        fontName="DejaVu-Bold",
        fontSize=10.2,
        leading=13.5,
        textColor=NAVY,
        spaceBefore=6.5,
        spaceAfter=3.5,
        keepWithNext=1,
    )
    styles["Bullet"] = ParagraphStyle(
        "Bullet",
        parent=styles["Body"],
        leftIndent=14,
        firstLineIndent=0,
        spaceAfter=3.4,
        bulletIndent=0,
        bulletFontName="DejaVu-Bold",
        bulletFontSize=8,
        bulletColor=TEAL,
    )
    styles["Number"] = ParagraphStyle(
        "Number",
        parent=styles["Bullet"],
        bulletColor=NAVY,
    )
    styles["Callout"] = ParagraphStyle(
        "Callout",
        parent=styles["Body"],
        fontSize=8.8,
        leading=12.5,
        spaceAfter=0,
    )
    styles["TableHead"] = ParagraphStyle(
        "TableHead",
        fontName="DejaVu-Bold",
        fontSize=7.7,
        leading=10,
        textColor=WHITE,
        spaceAfter=0,
    )
    styles["TableCell"] = ParagraphStyle(
        "TableCell",
        fontName="DejaVu",
        fontSize=7.55,
        leading=10,
        textColor=INK,
        spaceAfter=0,
    )
    styles["TableCellSmall"] = ParagraphStyle(
        "TableCellSmall",
        parent=styles["TableCell"],
        fontSize=7.15,
        leading=9.35,
    )
    styles["CoverEyebrow"] = ParagraphStyle(
        "CoverEyebrow",
        fontName="DejaVu-Bold",
        fontSize=10,
        leading=14,
        textColor=TEAL,
        alignment=TA_CENTER,
        spaceAfter=7,
    )
    styles["CoverTitle"] = ParagraphStyle(
        "CoverTitle",
        fontName="DejaVu-Bold",
        fontSize=27,
        leading=32,
        textColor=NAVY,
        alignment=TA_CENTER,
        spaceAfter=7,
    )
    styles["CoverCourse"] = ParagraphStyle(
        "CoverCourse",
        fontName="DejaVu-Bold",
        fontSize=22,
        leading=27,
        textColor=TEAL,
        alignment=TA_CENTER,
        spaceAfter=4,
    )
    styles["CoverTrack"] = ParagraphStyle(
        "CoverTrack",
        fontName="DejaVu-Bold",
        fontSize=12,
        leading=16,
        textColor=NAVY,
        alignment=TA_CENTER,
        spaceAfter=7,
    )
    styles["CoverSub"] = ParagraphStyle(
        "CoverSub",
        fontName="DejaVu",
        fontSize=10.3,
        leading=15,
        textColor=MUTED,
        alignment=TA_CENTER,
        spaceAfter=6,
    )
    styles["CoverNote"] = ParagraphStyle(
        "CoverNote",
        fontName="DejaVu",
        fontSize=8.8,
        leading=12.8,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=0,
    )
    styles["TOCTitle"] = ParagraphStyle(
        "TOCTitle",
        fontName="DejaVu-Bold",
        fontSize=18,
        leading=23,
        textColor=NAVY,
        spaceAfter=12,
    )
    styles["TOC0"] = ParagraphStyle(
        "TOC0",
        fontName="DejaVu-Bold",
        fontSize=9.1,
        leading=13,
        leftIndent=0,
        firstLineIndent=0,
        textColor=NAVY,
        spaceBefore=2,
    )
    styles["TOC1"] = ParagraphStyle(
        "TOC1",
        fontName="DejaVu",
        fontSize=8.1,
        leading=11,
        leftIndent=14,
        firstLineIndent=0,
        textColor=INK,
        spaceBefore=1,
    )
    return styles


def escape_inline(text: str) -> str:
    """Convert a small safe subset of Markdown inline syntax to ReportLab XML."""
    code_tokens: dict[str, str] = {}

    def take_code(match: re.Match[str]) -> str:
        token = f"ZXQCODE{len(code_tokens)}QXZ"
        code_tokens[token] = (
            '<font name="DejaVuMono" color="#31485B">'
            + html.escape(match.group(1), quote=False)
            + "</font>"
        )
        return token

    text = re.sub(r"`([^`]+)`", take_code, text)
    text = html.escape(text, quote=False)

    def link(match: re.Match[str]) -> str:
        label = match.group(1)
        href = match.group(2).replace('"', "%22")
        return f'<link href="{href}" color="#087E8B">{label}</link>'

    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    for token, markup in code_tokens.items():
        text = text.replace(token, markup)
    return text


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells)


def build_table(lines: list[str], styles) -> Table:
    rows = [split_table_row(line) for line in lines]
    rows = [row for row in rows if not is_table_separator("|" + "|".join(row) + "|")]
    if not rows:
        return Table([[]])
    ncols = max(len(row) for row in rows)
    normalized = [row + [""] * (ncols - len(row)) for row in rows]

    # Estimate widths from content while preserving enough room for short label/
    # score columns. Paragraphs wrap, so long columns remain readable on A4.
    max_lengths = [
        max((len(row[col]) for row in normalized), default=1)
        for col in range(ncols)
    ]
    min_width = min(52.0, CONTENT_W / ncols * 0.72)
    remaining = CONTENT_W - min_width * ncols
    weights = [max(1.0, min(float(length), 70.0)) for length in max_lengths]
    total = sum(weights)
    widths = [min_width + remaining * weight / total for weight in weights]

    data = []
    for r, row in enumerate(normalized):
        style = styles["TableHead"] if r == 0 else styles["TableCell"]
        data.append([Paragraph(escape_inline(cell), style) for cell in row])

    table = Table(
        data,
        colWidths=widths,
        repeatRows=1,
        hAlign="LEFT",
        splitByRow=1,
        spaceBefore=3,
        spaceAfter=7,
    )
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
    ]
    for row_index in range(1, len(data)):
        if row_index % 2 == 0:
            commands.append(("BACKGROUND", (0, row_index), (-1, row_index), colors.HexColor("#F6F9FB")))
    table.setStyle(commands)
    return table


def make_callout(text: str, styles) -> Table:
    paragraph = Paragraph(escape_inline(text), styles["Callout"])
    callout = Table([[paragraph]], colWidths=[CONTENT_W], hAlign="LEFT", spaceBefore=3, spaceAfter=8)
    callout.setStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), PALE_BLUE),
            ("LINEBEFORE", (0, 0), (0, -1), 3, TEAL),
            ("BOX", (0, 0), (-1, -1), 0.4, colors.HexColor("#D5E7EC")),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ]
    )
    return callout


def parse_markdown(text: str, styles) -> list:
    lines = text.splitlines()
    story = []
    paragraph_lines: list[str] = []
    table_lines: list[str] = []
    quote_lines: list[str] = []
    question_group: list[Paragraph] | None = None

    def flush_question() -> None:
        nonlocal question_group
        if question_group:
            story.append(KeepTogether(question_group))
            question_group = None

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines:
            text_value = " ".join(line.strip() for line in paragraph_lines).strip()
            if text_value:
                story.append(Paragraph(escape_inline(text_value), styles["Body"]))
            paragraph_lines = []

    def flush_table() -> None:
        nonlocal table_lines
        if table_lines:
            story.append(build_table(table_lines, styles))
            table_lines = []

    def flush_quote() -> None:
        nonlocal quote_lines
        if quote_lines:
            text_value = " ".join(line.strip()[1:].strip() for line in quote_lines)
            story.append(make_callout(text_value, styles))
            quote_lines = []

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if stripped == "<!-- PAGEBREAK -->":
            flush_paragraph()
            flush_table()
            flush_quote()
            flush_question()
            story.append(PageBreak())
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph()
            flush_quote()
            flush_question()
            table_lines.append(stripped)
            continue
        else:
            flush_table()

        if stripped.startswith(">"):
            flush_paragraph()
            flush_question()
            quote_lines.append(stripped)
            continue
        else:
            flush_quote()

        if not stripped:
            flush_paragraph()
            continue

        if re.fullmatch(r"-{3,}", stripped):
            flush_paragraph()
            flush_question()
            story.append(Spacer(1, 2))
            rule = Table([[""]], colWidths=[CONTENT_W], rowHeights=[1.2])
            rule.setStyle([("BACKGROUND", (0, 0), (-1, -1), GRID), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)])
            story.append(rule)
            story.append(Spacer(1, 5))
            continue

        heading = re.match(r"^(#{1,3})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            flush_question()
            level = len(heading.group(1))
            name = f"H{level}"
            story.append(Paragraph(escape_inline(heading.group(2)), styles[name]))
            continue

        question_stem = re.match(r"^\*\*Câu\s+\d+\b", stripped)
        if question_stem:
            flush_paragraph()
            flush_question()
            question_group = [Paragraph(escape_inline(stripped), styles["Body"])]
            continue

        choice = re.match(r"^(?:[A-D][.)]|[a-d][.)])\s+", stripped)
        if question_group is not None and choice:
            flush_paragraph()
            question_group.append(Paragraph(escape_inline(stripped), styles["Body"]))
            continue
        elif question_group is not None:
            flush_question()

        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        if bullet:
            flush_paragraph()
            story.append(
                Paragraph(
                    escape_inline(bullet.group(1)),
                    styles["Bullet"],
                    bulletText="•",
                )
            )
            continue

        ordered = re.match(r"^\s*(\d+)[.)]\s+(.+)$", line)
        if ordered:
            flush_paragraph()
            story.append(
                Paragraph(
                    escape_inline(ordered.group(2)),
                    styles["Number"],
                    bulletText=f"{ordered.group(1)}.",
                )
            )
            continue

        paragraph_lines.append(stripped)

    flush_paragraph()
    flush_table()
    flush_quote()
    flush_question()
    return story


class GuideDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(
            LEFT,
            BOTTOM,
            CONTENT_W,
            PAGE_H - TOP - BOTTOM,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
            id="normal",
        )
        self.addPageTemplates([PageTemplate(id="normal", frames=[frame], onPage=self.draw_chrome)])
        self._heading_count = 0

    def beforeDocument(self):
        # multiBuild() reruns the document; stable bookmark names are required
        # for the table-of-contents entries to settle between passes.
        self._heading_count = 0
        super().beforeDocument()

    def draw_chrome(self, canvas, doc):
        if doc.page == 1:
            return
        canvas.saveState()
        canvas.setStrokeColor(GRID)
        canvas.setLineWidth(0.55)
        canvas.line(LEFT, PAGE_H - 12 * mm, PAGE_W - RIGHT, PAGE_H - 12 * mm)
        canvas.setFont("DejaVu-Bold", 7.2)
        canvas.setFillColor(TEAL)
        canvas.drawString(LEFT, PAGE_H - 9.5 * mm, "TIN HỌC 10  •  ÔN TẬP GIỮA HỌC KÌ I")
        canvas.setStrokeColor(GRID)
        canvas.line(LEFT, 12 * mm, PAGE_W - RIGHT, 12 * mm)
        canvas.setFont("DejaVu", 7.2)
        canvas.setFillColor(MUTED)
        canvas.drawString(LEFT, 8.7 * mm, "Định hướng ICT  ·  Kết nối tri thức với cuộc sống")
        canvas.drawRightString(PAGE_W - RIGHT, 8.7 * mm, f"Trang {doc.page}")
        canvas.restoreState()

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        if style_name not in ("H1", "H2"):
            return
        level = 0 if style_name == "H1" else 1
        text = flowable.getPlainText()
        self._heading_count += 1
        key = f"guide-heading-{self._heading_count}"
        self.canv.bookmarkPage(key)
        try:
            self.canv.addOutlineEntry(text[:120], key, level=level, closed=(level > 0))
        except ValueError:
            # A deeply nested/out-of-order outline entry should not prevent PDF
            # generation; the TOC entry remains available.
            pass
        self.notify("TOCEntry", (level, text, self.page, key))


def make_cover(styles) -> list:
    items = [
        Spacer(1, 24 * mm),
        Paragraph("HỌC LIỆU ÔN TẬP", styles["CoverEyebrow"]),
        Paragraph("GIỮA HỌC KÌ I", styles["CoverTitle"]),
        Paragraph("TIN HỌC 10", styles["CoverCourse"]),
        Paragraph("ĐỊNH HƯỚNG ICT", styles["CoverTrack"]),
        Spacer(1, 2 * mm),
        Paragraph("Theo SGK <i>Kết nối tri thức với cuộc sống</i>", styles["CoverSub"]),
        Paragraph("Bám sát ma trận và bản đặc tả đề kiểm tra giữa kì I", styles["CoverSub"]),
        Spacer(1, 8 * mm),
    ]
    banner = Table(
        [[Paragraph("45 PHÚT   ·   10 ĐIỂM   ·   TÓM TẮT LÍ THUYẾT + ĐỀ LUYỆN CÓ ĐÁP ÁN", ParagraphStyle("Banner", fontName="DejaVu-Bold", fontSize=9.1, leading=13, alignment=TA_CENTER, textColor=WHITE))]],
        colWidths=[CONTENT_W - 14 * mm],
        hAlign="CENTER",
    )
    banner.setStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), NAVY),
            ("BOX", (0, 0), (-1, -1), 0, NAVY),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]
    )
    items.extend([banner, Spacer(1, 12 * mm)])
    summary = (
        "**Phạm vi:** dữ liệu và thông tin; vai trò của tin học/thiết bị thông minh; "
        "kĩ năng thiết bị số; mạng, Internet, IoT, điện toán đám mây; dịch vụ web, "
        "an toàn mạng; pháp luật, bản quyền và văn hóa số."
    )
    items.append(make_callout(summary, styles))
    items.append(Spacer(1, 3 * mm))
    source_note = (
        "**Lưu ý về nguồn:** DOCX được cung cấp là ma trận/đặc tả, không có câu hỏi "
        "hay đáp án đề gốc. Đề luyện và đáp án trong tài liệu này là câu mẫu biên soạn "
        "theo đúng cấu trúc ma trận."
    )
    items.append(make_callout(source_note, styles))
    items.append(Spacer(1, 14 * mm))
    items.append(Paragraph("Bản học liệu 1.0  ·  Cập nhật pháp luật đến 26/10/2026", styles["CoverSub"]))
    items.append(Spacer(1, 3 * mm))
    items.append(Paragraph("Tóm tắt theo chủ đề · ví dụ gần gũi · lời giải có giải thích và rubric", styles["CoverSub"]))
    items.append(PageBreak())
    return items


def build_pdf() -> None:
    register_fonts()
    styles = make_styles()
    if not SOURCE.exists():
        raise FileNotFoundError(SOURCE)
    text = SOURCE.read_text(encoding="utf-8")
    body = parse_markdown(text, styles)

    toc = TableOfContents()
    toc.levelStyles = [styles["TOC0"], styles["TOC1"]]
    toc.dotsMinLevel = 0
    toc.dotsMinGlyph = "."

    story = make_cover(styles)
    story.append(Paragraph("MỤC LỤC", styles["TOCTitle"]))
    story.append(toc)
    story.append(PageBreak())
    story.extend(body)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = GuideDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=LEFT,
        rightMargin=RIGHT,
        topMargin=TOP,
        bottomMargin=BOTTOM,
        title="Ôn tập giữa học kì I - Tin học 10, định hướng ICT",
        author="Học liệu ôn tập Tin học 10",
        subject="Đề cương, ma trận và đề luyện theo Kết nối tri thức với cuộc sống",
    )
    doc.multiBuild(story, maxPasses=6)
    print(f"Built {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    build_pdf()
