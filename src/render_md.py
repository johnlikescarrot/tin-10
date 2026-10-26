# -*- coding: utf-8 -*-
"""Kết xuất danh sách khối nội dung sang Markdown (bản dễ đọc, dễ review trên PR)."""
from __future__ import annotations

import re


def md(text):
    s = re.sub(r"\{\{(.+?)\}\}", r"**\1**", str(text))
    return s.replace("\n", "<br>")


def _row(cells):
    return "| " + " | ".join(md(c).replace("|", "\\|") for c in cells) + " |"


def _table(block):
    head = block["head"]
    hrows = [head] if not isinstance(head[0], list) else head
    ncol = len(head[0]) if isinstance(head[0], list) else len(head)
    out = []
    if block.get("caption"):
        out.append("*" + md(block["caption"]) + "*")
        out.append("")
    for row in hrows:
        out.append(_row(list(row) + [""] * (ncol - len(row))))
    out.append("|" + "---|" * ncol)
    for row in block["rows"]:
        cells = list(row) + [""] * (ncol - len(row))
        out.append(_row(cells[:ncol]))
    out.append("")
    return out


def _box(block):
    out = [f"> **{md(block['title'])}**", ">"]
    for line in block["lines"]:
        out.append("> - " + md(line))
    out.append("")
    return out


def render(blocks, out_path, source=None):
    lines = [
        "# ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I – TIN HỌC 10",
        "",
        "**Bộ sách:** Kết nối tri thức với cuộc sống  ·  **Thời gian làm bài:** 45 phút  ·  "
        "**Thang điểm:** 10 điểm",
        "",
        "> Biên soạn từ `MA TRAN GIUA KI I - LOP 10.docx`. Tài liệu gốc là ma trận + đặc tả đề "
        "(không chứa câu hỏi/đáp án cụ thể); đề cương giữ nguyên toàn bộ văn bản gốc ở Phụ lục A, "
        "chuyển 35/35 yêu cầu thành câu hỏi có đáp án ở Phần 5 và bổ sung đề thi thử ở Phần 6.",
        "",
        "---",
        "",
    ]

    # Mục lục tự sinh (không có số trang trong bản Markdown)
    toc = [b for b in blocks if b["k"] in ("h1", "h2")]
    lines += ["## MỤC LỤC", ""]
    for b in toc:
        prefix = "" if b["k"] == "h1" else "  "
        lines.append(f"{prefix}- {md(b['t'])}")
    lines += ["", "---", ""]

    for b in blocks:
        k = b["k"]
        if k in ("cover", "toc", "qabank", "src_appendix"):
            continue
        elif k == "h1":
            lines += ["", "# " + md(b["t"]), ""]
        elif k == "h2":
            lines += ["", "## " + md(b["t"]), ""]
        elif k == "h3":
            lines += ["", "### " + md(b["t"]), ""]
        elif k == "p":
            lines += [md(b["t"]), ""]
        elif k == "list":
            for i, item in enumerate(b["items"], 1):
                mark = f"{i}." if b["cls"] == "ol" else "-"
                lines.append(f"{mark} {md(item)}")
            lines.append("")
        elif k == "table":
            lines += _table(b)
        elif k == "box":
            lines += _box(b)
        elif k == "pagebreak":
            # Markdown không có khái niệm trang; tiêu đề đã đủ để phân mục.
            continue
        elif k == "rule":
            lines += ["", "---", ""]
        elif k == "spacer":
            continue
        elif k == "mcq":
            lines += [f"**{md(b['n'])}.** {md(b['t'])}", ""]
            for lab, opt in zip("ABCD", b["options"]):
                lines.append(f"- **{lab}.** {md(opt)}")
            lines += ["", f"> **Đáp án: {b['ans']}.** {md(b['explain'])} "
                      f"*[{md(b['tag'])}]*", ""]
        elif k == "tfq":
            lines += [f"**{md(b['n'])}.** {md(b['t'])}", ""]
            lines += _table({"head": ["Ý", "Nhận định", "Mức độ", "Đ/S"],
                             "rows": [[lab, txt, lvl, ans]
                                      for (lab, txt, lvl), ans
                                      in zip(b["statements"], b["answers"])]})
            lines += ["> **Giải thích:** " + md(b["explain"]), ""]
        elif k == "frq":
            lines += [f"**{md(b['n'])}.** {md(b['t'])}", "",
                      f"*{md(b['tag'])}*", ""]
            lines += _box({"title": "Hướng dẫn chấm / gợi ý đáp án", "lines": b["rubric"]})
        elif k == "qagroup":
            lines += ["", "## " + md(b["t"]) + f" *(ôn ở {md(b['ref'])} )*", ""]
        elif k == "qaitem":
            lines += [f"**{md(b['code'])}** · `{md(b['form'])}`", "",
                      "> **YÊU CẦU (nguyên văn):** " + md(b["q"]), "",
                      "**ĐÁP ÁN:** " + md(b["a"]), "",
                      f"*Xem thêm: mục {md(b['see'])}.*", ""]
        elif k == "check":
            lines += ["", "### " + md(b["title"]), ""]
            for item in b["items"]:
                lines.append(f"- [ ] {md(item)}")
            lines.append("")
        else:
            raise RuntimeError(f"Không biết khối: {k}")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return out_path
