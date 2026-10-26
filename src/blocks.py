# -*- coding: utf-8 -*-
"""Các khối nội dung trung gian dùng chung cho bản PDF và bản Markdown.

Mỗi khối là một dict.  Văn bản dùng cú pháp gọn:
    **đậm**  *nghiêng*  `mã`  {{từ khoá nhấn mạnh}}
"""
from __future__ import annotations


def H1(t):
    return {"k": "h1", "t": t}


def H2(t):
    return {"k": "h2", "t": t}


def H3(t):
    return {"k": "h3", "t": t}


def P(t, cls="body"):
    return {"k": "p", "t": t, "cls": cls}


def LEAD(t):
    return P(t, "lead")


def SMALL(t):
    return P(t, "small")


def UL(items, cls="ul"):
    return {"k": "list", "items": items, "cls": cls}


def OL(items):
    return {"k": "list", "items": items, "cls": "ol"}


def TBL(head, rows, widths=None, fs=8.4, caption=None, align=None, zebra=True):
    return {"k": "table", "head": head, "rows": rows, "widths": widths,
            "fs": fs, "caption": caption, "align": align, "zebra": zebra}


def BOX(title, lines, kind="tip"):
    """kind: tip | note | warn | example | memory"""
    return {"k": "box", "title": title, "lines": lines, "kind": kind}


def PB(hard=False):
    """hard=True: luôn sang trang mới. hard=False: bị build lược bỏ để tránh trang trống."""
    return {"k": "pagebreak", "hard": hard}


def SP(h=6):
    return {"k": "spacer", "h": h}


def RULE():
    return {"k": "rule"}


def MCQ(n, text, options, ans, explain, tag=""):
    return {"k": "mcq", "n": n, "t": text, "options": options,
            "ans": ans, "explain": explain, "tag": tag}


def TFQ(n, text, statements, answers, explain):
    """Câu đúng/sai: statements = [(nhãn, nội dung, mức độ)], answers = ['Đ','S',...]."""
    return {"k": "tfq", "n": n, "t": text, "statements": statements,
            "answers": answers, "explain": explain}


def FRQ(n, text, tag, rubric):
    return {"k": "frq", "n": n, "t": text, "tag": tag, "rubric": rubric}


def QABANK():
    return {"k": "qabank"}


def QAGROUP(title, ref):
    return {"k": "qagroup", "t": title, "ref": ref}


def QAITEM(code, question, level, form, answer, see):
    return {"k": "qaitem", "code": code, "q": question, "level": level,
            "form": form, "a": answer, "see": see}


def TOCBLOCK():
    return {"k": "toc"}


def COVER():
    return {"k": "cover"}


def CHECK(title, items):
    return {"k": "check", "title": title, "items": items}


def SRCAPPENDIX():
    return {"k": "src_appendix"}
