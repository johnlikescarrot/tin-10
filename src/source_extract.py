# -*- coding: utf-8 -*-
"""Trích xuất toàn bộ nội dung của file .docx gốc (ma trận + đặc tả đề).

Chỉ dùng thư viện chuẩn của Python.  Mục đích: bảo đảm rằng đề cương giữ lại
100% văn bản gốc, đặc biệt là 35 yêu cầu cần đạt trong bảng đặc tả.
"""
from __future__ import annotations

import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

LEVEL_WORDS = ("Nhận biết", "Thông hiểu", "Vận dụng cao", "Vận dụng")


def _norm(s: str) -> str:
    s = s.replace("\u00a0", " ").replace("\t", " ")
    return re.sub(r"\s+", " ", s).strip()


def _paragraph_text(p: ET.Element) -> str:
    out = []
    for t in p.iter():
        if t.tag == W + "t":
            out.append(t.text or "")
        elif t.tag in (W + "tab", W + "br"):
            out.append(" ")
    return _norm("".join(out))


def _cell_paragraphs(tc: ET.Element) -> list[str]:
    return [_paragraph_text(p) for p in tc.findall(W + "p")]


def _attr(tc: ET.Element, name: str) -> str:
    e = tc.find(W + "tcPr/" + W + name)
    return (e.get(W + "val") if e is not None else "") or ""


def _rows(tbl: ET.Element) -> list[list[str]]:
    return [["\n".join(_cell_paragraphs(tc)) for tc in tr.findall(W + "tc")]
            for tr in tbl.findall(W + "tr")]


def _cell_lines(tbl: ET.Element, row: int, col: int) -> list[str]:
    tr = tbl.findall(W + "tr")[row]
    return _cell_paragraphs(tr.findall(W + "tc")[col])


def read_source(docx: str | Path) -> dict:
    with zipfile.ZipFile(docx) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    body = root.find(W + "body")

    intro: list[str] = []
    tables: list[ET.Element] = []
    for child in body:
        if child.tag == W + "p":
            t = _paragraph_text(child)
            if t:
                intro.append(t)
        elif child.tag == W + "tbl":
            tables.append(child)
    if len(tables) < 2:
        raise ValueError("Không tìm thấy đủ 2 bảng (ma trận và đặc tả) trong tài liệu gốc.")

    matrix_tbl, spec_tbl = tables[0], tables[1]

    # --- Ma trận: 6 dòng dữ liệu, 16 cột (TT, chủ đề, đơn vị, 12 mức độ, tổng) ---
    matrix_rows = []
    last_tt = last_chude = ""
    for r in _rows(matrix_tbl)[3:9]:
        cells = [_norm(c.replace("\n", " ")) for c in r]
        tt, chude, donvi = cells[0], cells[1], cells[2]
        if tt:
            last_tt = tt
        if chude:
            last_chude = chude
        matrix_rows.append({
            "tt": last_tt,
            "chude": last_chude,
            "donvi": donvi,
            "levels": cells[3:15],
            "total": cells[15] if len(cells) > 15 else "",
        })

    summary_rows = [[_norm(c.replace("\n", " ")) for c in row]
                    for row in _rows(matrix_tbl)[9:12]]

    # --- Đặc tả: 6 dòng dữ liệu ---
    spec_rows = []
    bullets = []
    last_tt = last_chude = ""
    for ri, r in enumerate(_rows(spec_tbl)[2:8], start=2):
        cells = [_norm(c.replace("\n", " ")) for c in r]
        tt, chude, donvi = cells[0], cells[1], cells[2]
        if tt:
            last_tt = tt
        if chude:
            last_chude = chude
        counts = [cells[i] for i in range(4, 8)]
        lines = _cell_lines(spec_tbl, ri, 3)
        level = ""
        items = []
        for line in lines:
            line = _norm(line)
            if not line:
                continue
            matched = next((lw for lw in LEVEL_WORDS if line == lw), None)
            if matched:
                level = matched
                continue
            if line.startswith(("-", "–", "—", "•")):
                text = re.sub(r"^[-–—•]\s*", "", line)
                item = {"unit": "", "level": level, "text": text, "raw": line}
                items.append(item)
                bullets.append(item)
            else:
                # Dòng mô tả không có gạch đầu dòng (hiếm) vẫn được giữ lại.
                items.append({"heading": line})
        for it in items:
            if "text" in it:
                it["unit"] = donvi
        spec_rows.append({
            "tt": last_tt,
            "chude": last_chude,
            "donvi": donvi,
            "lines": lines,
            "items": items,
            "counts": counts,
        })

    spec_summary = [[_norm(c.replace("\n", " ")) for c in row]
                    for row in _rows(spec_tbl)[8:10]]

    return {
        "intro": intro,
        "matrix_rows": matrix_rows,
        "matrix_summary": summary_rows,
        "spec_rows": spec_rows,
        "spec_summary": spec_summary,
        "bullets": bullets,
    }


UNIT_KEYWORDS = {
    "A1": "Dữ liệu, thông tin và xử lý",
    "A2": "Vai trò của máy tính",
    "A3": "Kĩ năng sử dụng thiết bị số",
    "B1": "Khái niệm mạng máy tính",
    "B2": "Sử dụng dịch vụ web",
    "D1": "Nghĩa vụ tuân thủ pháp lí",
}


def _unit_code(unit_text: str) -> str:
    for code, keyword in UNIT_KEYWORDS.items():
        if keyword in unit_text:
            return code
    return "?"


def audit_coverage(source: dict, answers: list[dict]) -> list[str]:
    """Trả về danh sách lỗi nếu có yêu cầu gốc chưa có đáp án tương ứng."""
    errors = []
    if len(source["bullets"]) != len(answers):
        errors.append(
            f"Số yêu cầu gốc ({len(source['bullets'])}) != số đáp án ({len(answers)})."
        )
    for i, b in enumerate(source["bullets"]):
        if i >= len(answers):
            break
        a = answers[i]
        expected = _unit_code(b["unit"])
        if a.get("unit") and a["unit"] != expected:
            errors.append(
                f"Yêu cầu {i+1}: sai đơn vị kiến thức (đáp án ghi {a['unit']}, "
                f"nguồn là {expected} – {b['unit'][:45]})."
            )
        if not a.get("answer", "").strip():
            errors.append(f"Yêu cầu {i+1}: chưa có đáp án.")
    return errors


if __name__ == "__main__":
    import json
    import sys
    s = read_source(sys.argv[1] if len(sys.argv) > 1 else "MA TRAN GIUA KI I - LOP 10.docx")
    print("INTRO:")
    for x in s["intro"]:
        print("  ", x)
    print("\nMATRIX ROWS:")
    for x in s["matrix_rows"]:
        print("  ", x)
    print("\nMATRIX SUMMARY:", s["matrix_summary"])
    print("\nSPEC SUMMARY:", s["spec_summary"])
    print("\nBULLETS:", len(s["bullets"]))
    for i, b in enumerate(s["bullets"], 1):
        print(f"{i:2d}. [{b['level']}] ({b['unit'][:34]}) {b['text']}")
    with open("/tmp/spec_dump.json", "w") as f:
        json.dump(s, f, ensure_ascii=False, indent=2)
