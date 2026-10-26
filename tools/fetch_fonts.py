#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tải font Be Vietnam Pro (SIL OFL 1.1) từ kho google/fonts qua GitHub API.

Font được dùng để PDF hiển thị đúng tiếng Việt.  Chạy lại script này nếu thư mục
assets/fonts bị thiếu.  Yêu cầu mạng tới api.github.com.
"""
from __future__ import annotations

import base64
import json
import urllib.request
from pathlib import Path

BASE = "https://api.github.com/repos/google/fonts/contents/ofl/bevietnampro/"
FILES = [
    "BeVietnamPro-Regular.ttf",
    "BeVietnamPro-Italic.ttf",
    "BeVietnamPro-Medium.ttf",
    "BeVietnamPro-Bold.ttf",
    "BeVietnamPro-BoldItalic.ttf",
    "OFL.txt",
]
DEST = Path(__file__).resolve().parent.parent / "assets" / "fonts"


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        target = DEST / name
        if target.exists() and target.stat().st_size > 1000:
            print("có sẵn:", name)
            continue
        req = urllib.request.Request(BASE + name, headers={"User-Agent": "tin-10-outline-builder"})
        with urllib.request.urlopen(req, timeout=45) as r:
            payload = json.load(r)
        target.write_bytes(base64.b64decode(payload["content"]))
        print("đã tải:", name, target.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
