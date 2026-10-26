# Đề cương ôn tập giữa học kì I – Tin học 10 (Kết nối tri thức)

Repo này chứa **đề cương ôn tập giữa học kì I môn Tin học 10 – định hướng ICT**, được biên soạn
bằng cách phân tích trực tiếp tệp ma trận/đặc tả của đề kiểm tra (`MA TRAN GIUA KI I - LOP 10.docx`)
và bám sát bộ sách **Kết nối tri thức với cuộc sống**.

## Sản phẩm

| Tệp | Nội dung |
| --- | --- |
| `DE_CUONG_ON_TAP_TIN_HOC_10_GIUA_KI_I.pdf` | **Sản phẩm chính** – đề cương 49 trang, bản in được (A4) |
| `MA TRAN GIUA KI I - LOP 10.docx` | Tệp nguồn: ma trận + bảng đặc tả của đề |
| `content/*.md` | Nội dung nguồn của đề cương (Markdown có thẻ định dạng riêng) |
| `build/build_pdf.py` | Script dựng PDF (Python + ReportLab) |

## Nội dung đề cương

| Phần | Nội dung |
| --- | --- |
| 0 | Phân tích cấu trúc đề, ma trận rút gọn, ánh xạ đặc tả → mục ôn tập, lộ trình 7 ngày, kĩ năng phòng thi |
| 1 | Chủ đề A – Máy tính và xã hội tri thức: dữ liệu/thông tin, đơn vị lưu trữ, thiết bị thông minh, kĩ năng dùng thiết bị số |
| 2 | Chủ đề B – Mạng máy tính và Internet: LAN/Internet, điện toán đám mây, IoT, phần mềm độc hại, bắt nạt trên mạng, bảo vệ dữ liệu |
| 3 | Chủ đề D – Đạo đức, pháp luật, văn hoá trong môi trường số: bản quyền, Luật CNTT 2006, Nghị định 72/2013, Luật An ninh mạng 2018 |
| 4 | Đề mô phỏng: 20 câu trắc nghiệm + 2 câu đúng/sai + 3 câu tự luận (10 điểm, 45 phút) |
| 5 | Đáp án, thang điểm và hướng dẫn chấm chi tiết |
| 6 | **Nguyên văn** ma trận và bảng đặc tả của tệp gốc (bảo đảm không bỏ sót nội dung nào) + bảng đối chiếu |
| 7 | Sổ tay tra nhanh trước giờ thi: con số, mô hình, thuật ngữ, mốc thời gian, khung trả lời |

Toàn bộ **72 câu hỏi luyện tập theo chủ đề** (trắc nghiệm 4 lựa chọn, đúng/sai, tự luận) và
**25 câu của đề mô phỏng** đều có đáp án kèm giải thích.

## Dựng lại PDF

```bash
python3 -m venv .venv
.venv/bin/pip install reportlab
.venv/bin/python build/build_pdf.py
```

Yêu cầu: Python 3.9+, font **DejaVu Sans** (mặc định có trong `/usr/share/fonts/truetype/dejavu`,
đủ dấu tiếng Việt). Script tự dựng mục lục có số trang (lặp nhiều lượt cho tới khi số trang hội tụ).

## Định dạng nội dung (`content/*.md`)

Mỗi dòng bắt đầu bằng một thẻ, ví dụ:

```
# TIÊU ĐỀ PHẦN|Dòng mô tả nhỏ
## Tiêu đề mục (vào mục lục cấp 2)
### Tiểu mục
Đoạn văn thường (hỗ trợ **đậm**, *nhấn*, %%màu cam%%)
- gạch đầu dòng cấp 1
+ gạch đầu dòng cấp 2
tbl|30,40,30|Chú thích bảng
th|Cột 1||Cột 2||Cột 3
tr|ô||ô||ô
trc|ô giữa||ô giữa||ô giữa
endtbl
box|Nội dung khung GHI NHỚ
tip|Mẹo ghi nhớ        (warn|cẩn thận, note|lưu ý)
chain|Bước 1||Bước 2||Bước 3
qs|Câu hỏi trắc nghiệm      (opt|A. …||B. …||C. …||D. …)
ds|Câu hỏi đúng/sai         (opt1|a) …||b) …||c) …||d) …)
tl|Câu hỏi tự luận
answer|Đáp án
sol|Lời giải / hướng dẫn chấm
```

## Ghi chú

- Tệp `.docx` gốc **chỉ chứa ma trận và bảng đặc tả**, không chứa câu hỏi/đáp án cụ thể. Vì vậy
  toàn bộ nội dung tệp gốc được tái hiện nguyên văn ở Phần 6, còn mọi yêu cầu cần đạt trong đặc tả
  được chuyển thành câu hỏi – đáp án ở Phần 1–3 và đề mô phỏng ở Phần 4–5.
- Đơn vị lưu trữ dùng bội số **1024** theo cách trình bày của sách Tin học 10 (Kết nối tri thức).
