# Tin học 10 – Ôn tập giữa học kì I

Tài liệu ôn tập bằng tiếng Việt cho Tin học 10, định hướng ICT, bộ sách **Kết nối tri thức với cuộc sống**.

## Tài liệu

- [`ON_TAP_GIUA_KI_I_TIN_HOC_10.pdf`](ON_TAP_GIUA_KI_I_TIN_HOC_10.pdf) — bản PDF để đọc/in.
- [`ON_TAP_GIUA_KI_I_TIN_HOC_10.md`](ON_TAP_GIUA_KI_I_TIN_HOC_10.md) — bản Markdown có thể chỉnh sửa.
- [`MA TRAN GIUA KI I - LOP 10.docx`](MA%20TRAN%20GIUA%20KI%20I%20-%20LOP%2010.docx) — ma trận và đặc tả đề gốc.

**Lưu ý về nguồn:** DOCX gốc chỉ có ma trận và bản đặc tả, không có câu hỏi hoặc đáp án đề thi. Cẩm nang nêu rõ điều này; bộ câu hỏi và đáp án ở cuối là phần luyện tập mới, được biên soạn theo phạm vi và cấu trúc ma trận.

## Tạo lại PDF

Cần Python 3, các font DejaVu Sans (có sẵn trong nhiều bản Linux) và các thư viện trong `requirements.txt`.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/build_pdf.py
```

PDF được tạo tại `ON_TAP_GIUA_KI_I_TIN_HOC_10.pdf`.
