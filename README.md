# Đề cương ôn tập giữa kì I – Tin học 10 (Kết nối tri thức)

Tài liệu ôn tập toàn diện cho kì kiểm tra giữa kì I môn Tin học lớp 10, được biên soạn từ tệp nguồn
`MA TRAN GIUA KI I - LOP 10.docx` (ma trận đề + đặc tả đề kiểm tra giữa kì I) và đối chiếu nội dung
với bộ SGK **Tin học 10 – Kết nối tri thức với cuộc sống** (Chủ đề 1, 2, 3; Bài 1–11).

## 📄 Tài liệu chính

**[`DeCuong_OnTap_GiuaKiI_TinHoc10_KNTT.pdf`](DeCuong_OnTap_GiuaKiI_TinHoc10_KNTT.pdf)** — 56 trang, có mục lục,
bookmark PDF, running header/footer và số trang. Mở trực tiếp để học.

Nội dung gồm 7 phần và 4 phụ lục:

| Phần | Nội dung |
| --- | --- |
| Lời nói đầu | Phân tích tệp nguồn, kí hiệu, ghi chú các điểm chưa khớp giữa ma trận và đặc tả |
| 0 | Bản đồ kiến thức 3 trụ – 9 từ khoá, phân bổ điểm |
| 1 | Cấu trúc đề 45 phút, ma trận điểm, chiến lược làm bài |
| 2 | Chủ đề A: thông tin/dữ liệu, đơn vị lưu trữ, thiết bị thông minh, kĩ năng số (+ ôn bổ trợ Bài 3–6) |
| 3 | Chủ đề B: LAN/Internet, đám mây, IoT, an toàn mạng, khai thác tài nguyên web |
| 4 | Chủ đề D: pháp luật số, bản quyền, chia sẻ thông tin an toàn – hợp pháp |
| 5 | Ngân hàng 20 TN + 2 ĐS + 3 TL đúng cấu trúc đề (thêm 13 câu luyện), đáp án và thang điểm chấm |
| 6 | Lịch ôn 7 ngày, mẹo làm bài, lỗi sai thường gặp, checklist trước giờ thi |
| Phụ lục A | **Toàn văn ma trận và đặc tả gốc** + bảng đối chiếu 36 yêu cầu cần đạt |
| Phụ lục B–D | Đối chiếu SGK, bảng thuật ngữ, tài liệu tham khảo |

> **Về "câu hỏi và đáp án" của tài liệu gốc:** tệp .docx chỉ chứa ma trận đề và đặc tả (không có câu hỏi/đáp án
> dạng trắc nghiệm hay bài giải mẫu). Vì vậy đề cương (1) chép lại **toàn văn, không lược bỏ** mọi dòng và mọi ô
> của hai bảng gốc (Phụ lục A), (2) chuyển **toàn bộ 36 yêu cầu cần đạt** thành 36 cặp câu hỏi – đáp án mẫu có
> đánh mã `A1.1 … D.8`, giữ nguyên câu chữ gốc tại dòng "Yêu cầu gốc (nguyên văn)", và (3) bổ sung ngân hàng câu
> hỏi theo đúng cấu trúc đề kèm đáp án chi tiết. Phụ lục A.4 cho phép kiểm tra 36/36 yêu cầu đều có mặt.

## 🗂 Cấu trúc thư mục

```
DeCuong_OnTap_GiuaKiI_TinHoc10_KNTT.pdf   ← tài liệu PDF hoàn chỉnh (deliverable)
docs/
  DeCuong_OnTap_GiuaKiI_TinHoc10_KNTT.md  ← bản Markdown gộp (nguồn của PDF)
  NGUON_MA_TRAN_GOC.txt                   ← bản trích xuất đầy đủ nội dung .docx
  src/00..07-*.md                         ← các chương nguồn Markdown theo thứ tự
tools/
  extract_docx.py                         ← trích xuất .docx → NGUON_MA_TRAN_GOC.txt
  build_pdf.py                            ← dựng PDF từ docs/src/*.md bằng ReportLab
MA TRAN GIUA KI I - LOP 10.docx           ← tài liệu gốc (không chỉnh sửa)
```

## 🔧 Tự dựng lại PDF

Yêu cầu Python 3.9+, `reportlab` và font DejaVu TTF
(trên Ubuntu/Debian: `/usr/share/fonts/truetype/dejavu`). Có thể chỉ định thư mục font qua `FONT_DIR`.

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install reportlab
python3 tools/extract_docx.py     # tuỳ chọn: cập nhật lại bản trích xuất
python3 tools/build_pdf.py        # gộp Markdown và xuất PDF
```

`pypdf` (hoặc PyMuPDF) chỉ cần nếu muốn kiểm tra số trang/văn bản của PDF sau khi dựng.

## ✅ Kiểm chứng nhanh

- 36/36 yêu cầu cần đạt của đặc tả gốc có câu hỏi – đáp án tương ứng (Phụ lục A.4).
- 8/8 dòng mở đầu, 12/12 hàng ma trận và 8/8 hàng đặc tả được chép lại nguyên vẹn (Phụ lục A.1–A.3).
- 38 câu hỏi luyện tập (Câu 1–38), đáp án, giải thích và thang điểm chấm đầy đủ (Phần 5).
- PDF có 56 trang, 94 bookmark điều hướng, mục lục có số trang.
