# Đề cương ôn tập giữa kì I – Tin học 10 (Kết nối tri thức với cuộc sống)

Tài liệu ôn tập toàn diện, có cấu trúc dễ nhớ, được biên soạn từ file gốc
`MA TRAN GIUA KI I - LOP 10.docx` và đối chiếu với SGK Tin học 10 bộ sách
**Kết nối tri thức với cuộc sống** (Bài 1–11).

## Sản phẩm

| File | Mô tả |
| --- | --- |
| **`De-cuong-on-tap-giua-ki-I-Tin-hoc-10.pdf`** | Bản PDF hoàn chỉnh (A4, ~46 trang) – **file nộp chính**. |
| `DE-CUONG-ON-TAP-GIUA-KI-I-TIN-HOC-10.md` | Cùng nội dung ở dạng Markdown để đọc/review nhanh trên GitHub. |

## Kết quả phân tích tài liệu gốc

`MA TRAN GIUA KI I - LOP 10.docx` là **ma trận đề + đặc tả đề** kiểm tra giữa kì I
môn Tin học 10 (định hướng ICT), gồm 9 dòng văn bản thông tin chung, bảng ma trận
(6 đơn vị kiến thức × 12 cột mức độ nhận thức), bảng đặc tả (6 đơn vị) và
**35 yêu cầu cần đạt**. Tài liệu **không chứa câu hỏi hay đáp án cụ thể** nào.

Để đáp ứng yêu cầu “bao gồm tất cả câu hỏi và đáp án của tài liệu gốc”, đề cương:

1. chép **nguyên văn toàn bộ tài liệu gốc** ở **Phụ lục A** (sinh tự động từ
   `word/document.xml`, không gõ lại tay);
2. chuyển **35/35 yêu cầu** trong đặc tả thành 35 câu hỏi kèm **đáp án đầy đủ**
   ở **Phần 5**;
3. bổ sung **đề thi thử 45 phút đúng cấu trúc ma trận** (20 câu TN + 2 câu đúng/sai
   + 3 câu tự luận) kèm đáp án, giải thích và thang điểm ở **Phần 6**.

Script build có bước **đối soát tự động**: nếu số yêu cầu trong `.docx` thay đổi,
nếu thiếu đáp án hoặc đáp án gán sai đơn vị kiến thức, quá trình build sẽ dừng với
thông báo lỗi.

## Cấu trúc đề cương

- **Phần 0** – Đọc vị đề thi: cấu trúc đề, ma trận, trọng số điểm, 5 điểm lưu ý khi
  đối chiếu ma trận với đặc tả, lộ trình ôn 5 ngày.
- **Phần 1** – Bản đồ kiến thức 1 trang: sơ đồ tư duy, 6 “móc nhớ”, bảng công thức,
  12 lỗi sai thường gặp.
- **Phần 2–4** – Toàn bộ kiến thức 3 chủ đề (A/B/D ↔ Chủ đề 1/2/3 KNTT), mỗi đơn vị
  có bảng kiến thức, ví dụ, bài tập mẫu và hộp “Ghi nhớ nhanh”.
- **Phần 5** – Ngân hàng 35 câu hỏi & đáp án theo 100% yêu cầu của đặc tả.
- **Phần 6** – Đề thi thử + đáp án chi tiết.
- **Phụ lục A–D** – Toàn văn tài liệu gốc và biên bản đối soát, ánh xạ sang SGK
  KNTT, bảng thuật ngữ Anh–Việt, phiếu tự kiểm tra.

## Build lại

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python build.py
```

`build.py` sẽ:

1. đọc `.docx` bằng `src/source_extract.py` (chỉ dùng thư viện chuẩn);
2. đối soát 35 yêu cầu với 35 đáp án trong `src/c5_qa.py`;
3. xuất PDF bằng ReportLab + font **Be Vietnam Pro** (`assets/fonts/`);
4. xuất Markdown tương ứng;
5. dùng `pypdf` kiểm tra PDF có chứa đủ 35 yêu cầu gốc hay không.

Font có thể tải lại bằng `python3 tools/fetch_fonts.py` (lấy từ kho
`google/fonts` qua GitHub API); giấy phép **SIL Open Font License 1.1** nằm tại
`assets/fonts/OFL.txt`.

## Cấu trúc mã nguồn

```
build.py                  Điểm vào: đọc .docx → PDF + Markdown → kiểm tra
src/
  blocks.py               Định nghĩa các khối nội dung trung gian
  source_extract.py       Trích xuất ma trận + đặc tả từ .docx, đối soát
  outline_data.py         Lắp ráp toàn bộ nội dung
  c1_intro.py             Trang bìa, Phần 0, Phần 1
  c2_topic_a.py           Chủ đề A (Bài 1, 2, 7 + nền tảng Bài 3–6)
  c3_topic_b.py           Chủ đề B (Bài 8, 9, 10)
  c4_topic_d.py           Chủ đề D (Bài 11)
  c5_qa.py                35 đáp án cho 35 yêu cầu của đặc tả
  c6_exam.py              Đề thi thử + đáp án, thang điểm
  c7_appendix.py          Các phụ lục (A sinh tự động từ .docx)
  render_pdf.py           Kết xuất PDF (ReportLab)
  render_md.py            Kết xuất Markdown
tools/fetch_fonts.py      Tải lại font Be Vietnam Pro
assets/fonts/             Font + giấy phép OFL
```

## Tài liệu tham khảo đối chiếu nội dung SGK

- Mục lục SGK Tin học 10 – Kết nối tri thức với cuộc sống (Bài 1–11):
  <https://giaokhoaonline.com/tin-hoc-lop-10-ket-noi-tri-thuc/>
- Tóm tắt lí thuyết Bài 1, 2, 7, 8, 9, 10, 11 (VietJack):
  <https://vietjack.com/tin-hoc-10-kn/ly-thuyet-tin-hoc-lop-10-ket-noi.jsp>
- Lí thuyết Bài 11 – ứng xử trên môi trường số, nghĩa vụ tôn trọng bản quyền:
  <https://tailieumoi.vn/bai-viet/14277/ly-thuyet-tin-hoc-10-bai-11-ket-noi-tri-thuc-2023-ung-xu-tren-moi-truong-so-nghia-vu-ton-trong-ban-quyen>
- Luật Công nghệ thông tin 2006, Điều 12 –
  <https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Luat-cong-nghe-thong-tin-2006-67-2006-QH11-12987.aspx>
- Nghị định 72/2013/NĐ-CP –
  <https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-72-2013-ND-CP-quan-ly-cung-cap-su-dung-dich-vu-Internet-va-thong-tin-tren-mang-201110.aspx>

*Các ví dụ, bài tập, câu hỏi trắc nghiệm và đề thi thử là nội dung biên soạn bổ sung
phục vụ ôn tập; phần trích dẫn pháp luật bám theo nội dung SGK, người học nên kiểm
tra văn bản hiện hành khi áp dụng thực tế.*
