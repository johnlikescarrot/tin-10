#!/usr/bin/env python3
"""Build the Vietnamese study-guide PDF from Markdown using ReportLab."""
from __future__ import annotations

import argparse
from html import escape
from html.parser import HTMLParser
from pathlib import Path

import markdown
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
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "ON_TAP_GIUA_KI_I_TIN_HOC_10.md"
DEFAULT_OUTPUT = ROOT / "ON_TAP_GIUA_KI_I_TIN_HOC_10.pdf"
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


class Node:
    def __init__(self, tag: str, attrs: dict[str, str] | None = None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children: list[Node | str] = []


class TreeParser(HTMLParser):
    VOID = {"br", "hr", "img", "meta", "link"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs))
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag, dict(attrs)))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data):
        if data:
            self.stack[-1].children.append(data)


def inline_markup(node: Node | str) -> str:
    if isinstance(node, str):
        return escape(node, quote=False).replace("\n", " ")
    tag = node.tag
    content = "".join(inline_markup(child) for child in node.children)
    if tag in {"strong", "b"}:
        return f"<b>{content}</b>"
    if tag in {"em", "i"}:
        return f"<i>{content}</i>"
    if tag == "code":
        return f'<font name="DejaVuSansMono" size="8.2">{content}</font>'
    if tag == "a":
        href = escape(node.attrs.get("href", ""), quote=True)
        return f'<link href="{href}" color="#1769aa">{content}</link>'
    if tag == "br":
        return "<br/>"
    if tag == "sup":
        return f"<super>{content}</super>"
    if tag == "sub":
        return f"<sub>{content}</sub>"
    if tag == "del":
        return f"<strike>{content}</strike>"
    return content


def descendants(node: Node, tag: str) -> list[Node]:
    found = []
    for child in node.children:
        if isinstance(child, Node):
            if child.tag == tag:
                found.append(child)
            found.extend(descendants(child, tag))
    return found


class GuideDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, pagesize=A4, **kwargs)
        frame = Frame(18 * mm, 17 * mm, 174 * mm, 260 * mm, id="body", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates(PageTemplate(id="guide", frames=frame, onPage=self.draw_chrome))

    def draw_chrome(self, canvas, doc):
        if doc.page == 1:
            return
        canvas.saveState()
        width, height = A4
        canvas.setStrokeColor(colors.HexColor("#dbe4ed"))
        canvas.setLineWidth(0.5)
        canvas.line(18 * mm, height - 13 * mm, width - 18 * mm, height - 13 * mm)
        canvas.setFont("DejaVuSans", 7.5)
        canvas.setFillColor(colors.HexColor("#60758a"))
        canvas.drawString(18 * mm, height - 10 * mm, "TIN HỌC 10  •  ÔN TẬP GIỮA HỌC KÌ I")
        canvas.line(18 * mm, 13 * mm, width - 18 * mm, 13 * mm)
        canvas.drawString(18 * mm, 8.5 * mm, "Kết nối tri thức với cuộc sống  |  Tài liệu ôn tập")
        canvas.drawRightString(width - 18 * mm, 8.5 * mm, f"Trang {doc.page}")
        canvas.restoreState()


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="BodyVN", parent=styles["BodyText"], fontName="DejaVuSans", fontSize=9.15, leading=13.0, textColor=colors.HexColor("#203040"), spaceAfter=4.0, alignment=TA_LEFT, allowWidows=0, allowOrphans=0))
    styles.add(ParagraphStyle(name="H1VN", fontName="DejaVuSans-Bold", fontSize=18, leading=23, textColor=colors.HexColor("#123b5d"), spaceBefore=15, spaceAfter=8, keepWithNext=True))
    styles.add(ParagraphStyle(name="H2VN", fontName="DejaVuSans-Bold", fontSize=13.4, leading=17, textColor=colors.HexColor("#176b87"), spaceBefore=11, spaceAfter=5.5, keepWithNext=True))
    styles.add(ParagraphStyle(name="H3VN", fontName="DejaVuSans-Bold", fontSize=10.5, leading=14, textColor=colors.HexColor("#254a67"), spaceBefore=8, spaceAfter=4, keepWithNext=True))
    styles.add(ParagraphStyle(name="BulletVN", parent=styles["BodyVN"], leftIndent=12, firstLineIndent=-8, bulletIndent=0, spaceAfter=2.5))
    styles.add(ParagraphStyle(name="TableVN", fontName="DejaVuSans", fontSize=7.65, leading=10.1, textColor=colors.HexColor("#203040"), spaceAfter=0))
    styles.add(ParagraphStyle(name="TableHeadVN", parent=styles["TableVN"], fontName="DejaVuSans-Bold", textColor=colors.white))
    styles.add(ParagraphStyle(name="QuoteVN", parent=styles["BodyVN"], fontSize=8.8, leading=13, textColor=colors.HexColor("#254a67"), spaceAfter=0))
    styles.add(ParagraphStyle(name="TitleVN", fontName="DejaVuSans-Bold", fontSize=26, leading=33, alignment=TA_CENTER, textColor=colors.HexColor("#123b5d"), spaceAfter=12))
    styles.add(ParagraphStyle(name="SubTitleVN", fontName="DejaVuSans", fontSize=15, leading=21, alignment=TA_CENTER, textColor=colors.HexColor("#176b87"), spaceAfter=8))
    styles.add(ParagraphStyle(name="CoverMetaVN", fontName="DejaVuSans", fontSize=10.5, leading=17, alignment=TA_CENTER, textColor=colors.HexColor("#43586a"), spaceAfter=5))
    return styles


def convert_blocks(node: Node, styles, output: list, top=True):
    children = node.children
    i = 0
    cover_headings_to_skip = 2 if top else 0
    while i < len(children):
        child = children[i]
        if isinstance(child, str):
            if child.strip():
                output.append(Paragraph(escape(child.strip(), quote=False), styles["BodyVN"]))
            i += 1
            continue
        tag = child.tag
        if tag in {"h1", "h2"} and cover_headings_to_skip:
            cover_headings_to_skip -= 1
            i += 1
            continue  # Main title and subtitle are laid out on the designed cover.
        if tag in {"h1", "h2", "h3", "h4"}:
            level = {"h1": "H1VN", "h2": "H2VN", "h3": "H3VN", "h4": "H3VN"}[tag]
            output.append(Paragraph(inline_markup(child), styles[level]))
        elif tag == "p":
            output.append(Paragraph(inline_markup(child), styles["BodyVN"]))
        elif tag in {"ul", "ol"}:
            number = 1
            for item in child.children:
                if not isinstance(item, Node) or item.tag != "li":
                    continue
                parts = []
                for sub in item.children:
                    if isinstance(sub, Node) and sub.tag in {"ul", "ol"}:
                        continue
                    parts.append(inline_markup(sub))
                bullet = f"{number}." if tag == "ol" else "–"
                output.append(Paragraph(" ".join(parts), styles["BulletVN"], bulletText=bullet))
                number += 1
                for sub in item.children:
                    if isinstance(sub, Node) and sub.tag in {"ul", "ol"}:
                        convert_blocks(sub, styles, output, top=False)
        elif tag == "blockquote":
            inner = []
            convert_blocks(child, styles, inner, top=False)
            if inner:
                box = Table([[inner]], colWidths=[173 * mm])
                box.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#eef6fa")),
                    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#c2dbe8")),
                    ("LINEBEFORE", (0, 0), (0, -1), 3, colors.HexColor("#2694ad")),
                    ("LEFTPADDING", (0, 0), (-1, -1), 9),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ]))
                output.append(KeepTogether([box, Spacer(1, 5)]))
        elif tag == "table":
            rows = []
            for tr in descendants(child, "tr"):
                cells = []
                for cell in tr.children:
                    if isinstance(cell, Node) and cell.tag in {"th", "td"}:
                        cells.append(Paragraph("".join(inline_markup(c) for c in cell.children), styles["TableHeadVN"] if cell.tag == "th" else styles["TableVN"]))
                if cells:
                    rows.append(cells)
            if rows:
                max_cols = max(map(len, rows))
                for row in rows:
                    row.extend([Paragraph("", styles["TableVN"])] * (max_cols - len(row)))
                widths = [174 * mm / max_cols] * max_cols
                table = Table(rows, colWidths=widths, repeatRows=1, hAlign="LEFT")
                table.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#176b87")),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f3f7fa")]),
                    ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#cfdae3")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                output.extend([Spacer(1, 3), table, Spacer(1, 7)])
        elif tag == "hr":
            line = Table([['']], colWidths=[174 * mm], rowHeights=[1])
            line.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#cfdae3"))]))
            output.extend([Spacer(1, 4), line, Spacer(1, 6)])
        elif tag == "div":
            convert_blocks(child, styles, output, top=False)
        i += 1


def register_fonts():
    regular = FONT_DIR / "DejaVuSans.ttf"
    bold = FONT_DIR / "DejaVuSans-Bold.ttf"
    mono = FONT_DIR / "DejaVuSansMono.ttf"
    for path in (regular, bold, mono):
        if not path.exists():
            raise FileNotFoundError(f"Unicode font not found: {path}; install DejaVu Sans fonts.")
    pdfmetrics.registerFont(TTFont("DejaVuSans", str(regular)))
    pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", str(bold)))
    pdfmetrics.registerFont(TTFont("DejaVuSansMono", str(mono)))
    pdfmetrics.registerFontFamily("DejaVuSans", normal="DejaVuSans", bold="DejaVuSans-Bold", italic="DejaVuSans", boldItalic="DejaVuSans-Bold")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    register_fonts()
    text = args.source.read_text(encoding="utf-8")
    html = markdown.markdown(text, extensions=["tables", "sane_lists", "smarty"])
    tree = TreeParser()
    tree.feed(html)
    styles = build_styles()

    story = [Spacer(1, 37 * mm), Paragraph("CẨM NANG ÔN TẬP<br/>GIỮA HỌC KÌ I", styles["TitleVN"]),
             Paragraph("TIN HỌC 10", styles["SubTitleVN"]),
             Paragraph("Định hướng Tin học ứng dụng (ICT)", styles["CoverMetaVN"]),
             Paragraph("Theo bộ sách <i>Kết nối tri thức với cuộc sống</i>", styles["CoverMetaVN"]),
             Spacer(1, 9 * mm)]
    cover_box = Table([[Paragraph("<b>PHẠM VI</b><br/>Chủ đề A · Máy tính và xã hội tri thức<br/>Chủ đề B · Mạng máy tính và Internet<br/>Chủ đề D · Đạo đức, pháp luật và văn hoá trong môi trường số<br/><br/><b>45 phút</b> &nbsp; | &nbsp; Trắc nghiệm 7 điểm &nbsp; | &nbsp; Tự luận 3 điểm", styles["CoverMetaVN"])]], colWidths=[145 * mm])
    cover_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#eef6fa")),
        ("BOX", (0, 0), (-1, -1), 0.8, colors.HexColor("#c2dbe8")),
        ("TOPPADDING", (0, 0), (-1, -1), 12), ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.extend([cover_box, Spacer(1, 10 * mm), Paragraph("Tóm lược kiến thức · Kĩ năng thực hành · Đề luyện tập · Đáp án và thang điểm", styles["CoverMetaVN"]), PageBreak()])
    convert_blocks(tree.root, styles, story)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    doc = GuideDocTemplate(str(args.output), title="Cẩm nang ôn tập giữa học kì I – Tin học 10", author="Tài liệu ôn tập Tin học 10", subject="Kết nối tri thức với cuộc sống")
    doc.build(story)
    print(f"Created {args.output} ({args.output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
