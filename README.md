# Tin học 10 — Ôn tập giữa học kì I

Học liệu ôn tập bằng tiếng Việt cho môn **Tin học 10, định hướng ICT**, theo phạm vi ma trận/đặc tả trong tài liệu nguồn và các chủ đề tương ứng của bộ sách **Kết nối tri thức với cuộc sống**.

## Tài liệu

- [Bản PDF hoàn chỉnh](docs/on-tap-giua-ki-i-tin-hoc-10.pdf)
- [Bản Markdown có thể chỉnh sửa](docs/on-tap-giua-ki-i-tin-hoc-10.md)
- [Ma trận/đặc tả nguồn](MA%20TRAN%20GIUA%20KI%20I%20-%20LOP%2010.docx)

PDF gồm tóm tắt kiến thức theo chủ đề, yêu cầu cần đạt, ví dụ, checklist ôn tập và đề luyện 45 phút có đáp án/giải thích/rubric. **Tệp DOCX nguồn chỉ có ma trận và đặc tả, không có câu hỏi hay đáp án đề gốc**; vì vậy, câu hỏi trong đề luyện là câu mẫu biên soạn theo cấu trúc nguồn, không được gán là đề chính thức.

## Tạo lại PDF

Cần Python 3 và ReportLab. Từ thư mục kho lưu trữ:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-guide.txt
.venv/bin/python scripts/build_guide.py
```

PDF được tạo tại `docs/on-tap-giua-ki-i-tin-hoc-10.pdf`. Bộ chữ DejaVu Sans cần có tại `/usr/share/fonts/truetype/dejavu/` để bảo đảm hiển thị tiếng Việt.
