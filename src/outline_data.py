# -*- coding: utf-8 -*-
"""Lắp ráp toàn bộ nội dung đề cương thành một danh sách khối duy nhất."""
from __future__ import annotations

from .blocks import PB, TOCBLOCK, QAGROUP, QAITEM
from . import c1_intro, c2_topic_a, c3_topic_b, c4_topic_d, c5_qa, c6_exam, c7_appendix
from .source_extract import audit_coverage


def expand_qabank(source):
    """Ghép 35 yêu cầu nguyên văn (từ .docx) với 35 đáp án (c5_qa.QA_ANSWERS)."""
    assert len(source["bullets"]) == len(c5_qa.QA_ANSWERS), (
        f"Số yêu cầu {len(source['bullets'])} != số đáp án {len(c5_qa.QA_ANSWERS)}"
    )
    out = []
    last_unit = None
    for i, (bullet, meta) in enumerate(zip(source["bullets"], c5_qa.QA_ANSWERS), 1):
        if meta["unit"] != last_unit:
            last_unit = meta["unit"]
            out.append(QAGROUP(c5_qa.UNIT_NAMES[last_unit], c5_qa.UNIT_REF[last_unit]))
        out.append(QAITEM(
            code=f"Câu {meta['code']}",
            question=bullet["text"],
            level=bullet["level"],
            form=meta["form"],
            answer=meta["answer"],
            see=meta.get("see", ""),
        ))
    return out


def build_blocks(source) -> list[dict]:
    errors = audit_coverage(source, c5_qa.QA_ANSWERS)
    if errors:
        raise SystemExit("LỖI ĐỐI SOÁT NỘI DUNG GỐC:\n - " + "\n - ".join(errors))

    intro = c1_intro.blocks(source)
    cover, intro_rest = intro[0], intro[1:]

    def add(items):
        for b in items:
            if b["k"] == "pagebreak" and not b.get("hard"):
                continue  # tránh trang gần như trống do ngắt trang cứng
            blocks.append(b)

    blocks = []
    blocks.append(cover)
    blocks += [PB(hard=True), TOCBLOCK(), PB(hard=True)]
    add(intro_rest)
    add(c2_topic_a.blocks())
    add(c3_topic_b.blocks())
    add(c4_topic_d.blocks())

    part5 = c5_qa.blocks()
    expanded = []
    for b in part5:
        if b["k"] == "qabank":
            expanded += expand_qabank(source)
        else:
            expanded.append(b)
    add(expanded)

    add(c6_exam.blocks())
    add(c7_appendix.src_appendix_blocks(source))
    add(c7_appendix.other_appendix_blocks())
    return blocks
