#!/usr/bin/env python3
"""Biên dịch Đề cương Ôn tập Giữa kì I - Tin học 10 (Kết nối tri thức) ra tệp PDF."""

from pathlib import Path
import typst

ROOT = Path(__file__).resolve().parent
INPUT_TYP = ROOT / "src" / "main.typ"
OUTPUT_PDF = ROOT / "DE-CUONG-ON-TAP-GIUA-KI-I-TIN-HOC-10-KNTT.pdf"
FONT_DIR = ROOT / "src" / "fonts"


def main() -> None:
    typst.compile(
        str(INPUT_TYP),
        output=str(OUTPUT_PDF),
        root=str(ROOT),
        font_paths=[str(FONT_DIR)],
    )
    size_kb = OUTPUT_PDF.stat().st_size / 1024
    print(f"Đã xuất thành công: {OUTPUT_PDF.name} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
