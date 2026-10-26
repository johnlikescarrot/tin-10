#!/usr/bin/env python3
"""
Extract every paragraph and every table cell from the source .docx into a
plain-text transcript (docs/NGUON_MA_TRAN_GOC.txt).

This is the first step of the analysis that produced the review outline: it
makes the whole content of MA TRAN GIUA KI I - LOP 10.docx visible in a
diff-friendly text file, including empty cells (rendered as <empty>).

Only the Python standard library is needed.
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "MA TRAN GIUA KI I - LOP 10.docx"
TARGET = ROOT / "docs" / "NGUON_MA_TRAN_GOC.txt"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def paragraph_text(p: ET.Element) -> str:
    parts = []
    for node in p.iter():
        if node.tag == W + "t":
            parts.append(node.text or "")
        elif node.tag == W + "tab":
            parts.append("\t")
        elif node.tag == W + "br":
            parts.append(" / ")
    return "".join(parts)


def cell_text(tc: ET.Element) -> str:
    return "\n".join(paragraph_text(p) for p in tc.findall(W + "p")).strip()


def main() -> None:
    with zipfile.ZipFile(SOURCE) as z:
        names = z.namelist()
        root = ET.fromstring(z.read("word/document.xml"))
        extras = [n for n in names if n.startswith("word/footer") or n.startswith("word/header")]

    lines: list[str] = [
        "BẢN TRÍCH XUẤT TOÀN BỘ NỘI DUNG TỆP NGUỒN",
        f"Tệp: {SOURCE.name}",
        "Phương pháp: đọc word/document.xml bằng xml.etree.ElementTree,",
        "giữ nguyên văn bản của mọi w:t, w:tab, w:br; mỗi ô bảng ghi rõ chỉ số.",
        "Ô trống được ghi là <empty>. Dòng mới trong cùng một ô được ghi là ' / '.",
        f"Các phần phụ khác trong tệp: {', '.join(extras) if extras else 'không có'}",
        "(các footer chỉ chứa 1 kí tự, không có nội dung câu hỏi/đáp án).",
        "=" * 78,
        "",
    ]

    body = root.find(W + "body")
    para_i = 0
    table_i = 0
    for child in body:
        if child.tag == W + "p":
            text = paragraph_text(child)
            if text.strip():
                para_i += 1
                lines.append(f"[Đoạn {para_i}] {text}")
            continue
        if child.tag == W + "tbl":
            table_i += 1
            lines.append("")
            lines.append(f"######## BẢNG {table_i} ########")
            for r, tr in enumerate(child.findall(W + "tr")):
                lines.append(f"--- HÀNG {r} ---")
                for c, tc in enumerate(tr.findall(W + "tc")):
                    value = cell_text(tc).replace("\n", " / ") or "<empty>"
                    lines.append(f"  [{c}] {value}")
            lines.append(f"######## HẾT BẢNG {table_i} ########")
            lines.append("")

    TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {TARGET} ({TARGET.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
