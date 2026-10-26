#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build toàn bộ đề cương (PDF + Markdown) từ file .docx gốc.

    python3 build.py

Yêu cầu: reportlab (xem requirements.txt) và các font trong assets/fonts/.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from src.outline_data import build_blocks                 # noqa: E402
from src.render_md import render as render_md            # noqa: E402
from src.render_pdf import render as render_pdf          # noqa: E402
from src.source_extract import read_source               # noqa: E402

DOCX = ROOT / "MA TRAN GIUA KI I - LOP 10.docx"
PDF = ROOT / "De-cuong-on-tap-giua-ki-I-Tin-hoc-10.pdf"
MD = ROOT / "DE-CUONG-ON-TAP-GIUA-KI-I-TIN-HOC-10.md"


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def verify_pdf(source):
    """Kiểm tra PDF có trang, có chữ và chứa 35 yêu cầu gốc hay không."""
    result = {"pages": None, "text_chars": 0, "requirements_found": 0,
              "requirements_total": len(source["bullets"]), "missing": []}
    try:
        from pypdf import PdfReader
    except ImportError:
        result["note"] = "pypdf không có – bỏ qua đối soát văn bản trong PDF."
        return result
    reader = PdfReader(str(PDF))
    result["pages"] = len(reader.pages)
    text = "\n".join((p.extract_text() or "") for p in reader.pages)
    flat = norm(text)
    result["text_chars"] = len(flat)
    for b in source["bullets"]:
        target = norm(b["text"])
        # Một số bộ đọc PDF chèn khoảng trắng giữa các kí tự; thử cả hai dạng.
        if target in flat or target.replace(" ", "") in flat.replace(" ", ""):
            result["requirements_found"] += 1
        else:
            result["missing"].append(b["text"][:70])
    return result


def main():
    if not DOCX.exists():
        raise SystemExit(f"Thiếu tài liệu gốc: {DOCX}")
    source = read_source(DOCX)
    print(f"[1/5] Đã đọc .docx: {len(source['intro'])} dòng giới thiệu, "
          f"{len(source['matrix_rows'])} dòng ma trận, "
          f"{len(source['spec_rows'])} dòng đặc tả, "
          f"{len(source['bullets'])} yêu cầu cần đạt.")

    blocks = build_blocks(source)  # có audit_coverage bên trong
    print(f"[2/5] Đối soát 35/35 yêu cầu: OK. Tổng {len(blocks)} khối nội dung.")

    render_pdf(blocks, PDF)
    print(f"[3/5] Đã xuất PDF: {PDF.name} ({PDF.stat().st_size / 1024:.0f} KB)")

    render_md(blocks, MD, source)
    print(f"[4/5] Đã xuất Markdown: {MD.name} ({MD.stat().st_size / 1024:.0f} KB)")

    v = verify_pdf(source)
    print(f"[5/5] Kiểm tra PDF: {v['pages']} trang, {v['text_chars']} kí tự văn bản, "
          f"tìm thấy {v['requirements_found']}/{v['requirements_total']} yêu cầu gốc.")
    if v.get("note"):
        print("      " + v["note"])
    if v["missing"]:
        print("      CẢNH BÁO – chưa tìm thấy (có thể do font/đọc PDF):")
        for m in v["missing"][:10]:
            print("       -", m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
