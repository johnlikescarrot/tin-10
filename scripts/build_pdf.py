#!/usr/bin/env python3
"""
Script biên dịch Đề cương ôn tập Giữa kì I - Tin học 10 (Kết nối tri thức)
từ mã nguồn Typst (src/main.typ) sang tệp PDF hoàn chỉnh.
"""

from pathlib import Path
import base64
import json
import urllib.request
import typst

ROOT = Path(__file__).resolve().parent.parent
SRC_FILE = ROOT / "src" / "main.typ"
OUT_PDF = ROOT / "DE_CUONG_ON_TAP_GIUA_KI_I_TIN_HOC_10_KNTT.pdf"
FONT_CACHE = Path("/tmp/fonts")


def ensure_fonts() -> list[str]:
    FONT_CACHE.mkdir(parents=True, exist_ok=True)
    needed = [
        "BeVietnamPro-Regular.ttf",
        "BeVietnamPro-Italic.ttf",
        "BeVietnamPro-Medium.ttf",
        "BeVietnamPro-SemiBold.ttf",
        "BeVietnamPro-Bold.ttf",
        "BeVietnamPro-BoldItalic.ttf",
        "BeVietnamPro-ExtraBold.ttf",
    ]
    if not all((FONT_CACHE / f).exists() for f in needed):
        url = "https://api.github.com/repos/google/fonts/contents/ofl/bevietnampro"
        req = urllib.request.Request(url, headers={"User-Agent": "tin10-pdf-builder"})
        items = json.loads(urllib.request.urlopen(req, timeout=30).read().decode())
        for item in items:
            name = item.get("name", "")
            if name in needed and not (FONT_CACHE / name).exists():
                r2 = urllib.request.Request(item["url"], headers={"User-Agent": "tin10-pdf-builder"})
                d2 = json.loads(urllib.request.urlopen(r2, timeout=30).read().decode())
                (FONT_CACHE / name).write_bytes(base64.b64decode(d2["content"]))

    paths = [str(FONT_CACHE)]
    sys_dejavu = Path("/usr/share/fonts/truetype/dejavu")
    if sys_dejavu.exists():
        paths.append(str(sys_dejavu))
    return paths


def main() -> None:
    font_paths = ensure_fonts()
    pdf_bytes = typst.compile(str(SRC_FILE), font_paths=font_paths)
    OUT_PDF.write_bytes(pdf_bytes)
    print(f"Compiled successfully: {OUT_PDF} ({len(pdf_bytes):,} bytes)")


if __name__ == "__main__":
    main()
