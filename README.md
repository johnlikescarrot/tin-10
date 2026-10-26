# Đề cương Ôn tập Giữa học kì I – Tin học 10 (Kết nối tri thức với cuộc sống)

Kho lưu trữ bao gồm tài liệu gốc Ma trận & Đặc tả kiểm tra giữa kì I và **Đề cương ôn tập Giữa học kì I môn Tin học 10 (Định hướng Tin học ứng dụng – ICT)** biên soạn chi tiết theo bộ sách **Kết nối tri thức với cuộc sống** (Chương trình GDPT 2018).

## 📄 Tài liệu chính (PDF hoàn chỉnh)

- **[`DE_CUONG_ON_TAP_GIUA_KI_I_TIN_HOC_10_KNTT.pdf`](./DE_CUONG_ON_TAP_GIUA_KI_I_TIN_HOC_10_KNTT.pdf)** *(38 trang A4, trình bày chuẩn in ấn)*
- Tài liệu đầu vào gốc: [`MA TRAN GIUA KI I - LOP 10.docx`](./MA%20TRAN%20GIUA%20KI%20I%20-%20LOP%2010.docx)

## 🧭 Cấu trúc nội dung Đề cương

1. **Phần I – Cấu trúc đề, Ma trận & Bảng đặc tả kiểm tra Giữa kì I:**
   - Trích xuất đầy đủ 100% quy định cấu trúc đề (45 phút; 70% trắc nghiệm gồm 20 câu 4 lựa chọn + 02 câu Đúng/Sai; 30% tự luận gồm 03 câu Thông hiểu – Vận dụng – Vận dụng cao), Bảng Ma trận và Bảng Đặc tả từ tệp gốc.
   - Bảng ánh xạ chi tiết từng đơn vị kiến thức sang các bài học trong SGK *Tin học 10 – Kết nối tri thức với cuộc sống* (Bài 1, Bài 2, Bài 7, Bài 8, Bài 9, Bài 10, Bài 11) và phân tích chiến lược ôn tập.
2. **Phần II – Hệ thống hóa lý thuyết trọng tâm & Mẹo ghi nhớ nhanh:**
   - **Chủ đề A. Máy tính và xã hội tri thức (4,0 điểm – 40%):** Phân biệt *Thông tin – Dữ liệu – Vật mang tin*, quy trình xử lí thông tin, ưu điểm thiết bị số, bảng chuyển đổi đơn vị lưu trữ (`bit`, `Byte`, `KB`, `MB`, `GB`, `TB`, `PB`) & công thức tính dung lượng/truyền tin, nhận diện *Thiết bị thông minh*, vai trò trong *CMCN 4.0* & *Kinh tế tri thức*, niên biểu các mốc lịch sử phát triển ngành Tin học & AI.
   - **Chủ đề B. Mạng máy tính và Internet (4,0 điểm – 40%):** Thành phần mạng máy tính, bảng so sánh *Mạng LAN và Internet*, *Điện toán đám mây* (`SaaS`, `PaaS`, `IaaS`), *Internet vạn vật (IoT)*, phân biệt phần mềm độc hại (*Virus – Worm – Trojan – Ransomware*), quy tắc 4 bước *K–L–C–B* phòng vệ khi bị bắt nạt trên mạng, bảo vệ dữ liệu cá nhân, công cụ dịch tự động (*Google Dịch*) và *Nguồn học liệu mở (OER)*.
   - **Chủ đề D. Đạo đức, pháp luật và văn hoá trong môi trường số (2,0 điểm – 20%):** Tổng hợp nội dung cốt lõi của *Luật Công nghệ thông tin*, *Luật An ninh mạng*, *Nghị định 72/2013/NĐ-CP* (cùng các nghị định quản lí/xử phạt vi phạm trên mạng), *Luật Sở hữu trí tuệ* (bản quyền số) và **Công thức 4 bước** giải câu Tự luận Vận dụng cao.
3. **Phần III – Ngân hàng câu hỏi ôn tập theo Ma trận (Có đáp án & giải thích 100%):**
   - **45 câu** Trắc nghiệm 4 lựa chọn phân theo Chủ đề A, B, D kèm bảng đáp án và giải thích.
   - **08 câu lớn (32 mệnh đề)** Trắc nghiệm Đúng/Sai chuẩn định dạng mới tập trung vào đơn vị `A.2` và `B.1` kèm giải thích chi tiết từng ý `a, b, c, d`.
   - **10 câu** Tự luận trọng tâm (Thông hiểu – Vận dụng – Vận dụng cao) kèm hướng dẫn trình bày đạt điểm tối đa.
4. **Phần IV – Đề kiểm tra thử Giữa kì I chuẩn 100% Ma trận (45 phút) & Đáp án – Thang điểm:**
   - 01 đề thi thử hoàn chỉnh khớp từng ô Ma trận (20 câu TN + 02 câu ĐS + 03 câu TL), đáp án – biểu điểm chi tiết và **Bảng tổng kết 10 điểm vàng soát nhanh 5 phút cuối trước giờ thi**.

## 🛠️ Cấu trúc thư mục & Biên dịch lại PDF

```text
├── DE_CUONG_ON_TAP_GIUA_KI_I_TIN_HOC_10_KNTT.pdf   # Tệp PDF đề cương hoàn chỉnh
├── MA TRAN GIUA KI I - LOP 10.docx                 # Tệp Ma trận & Đặc tả gốc
├── src/                                            # Mã nguồn Typst theo từng phần
│   ├── main.typ
│   ├── template.typ
│   ├── part1_matrix.typ
│   ├── part2_theory.typ
│   ├── part3_questions.typ
│   └── part4_mock_exam.typ
└── scripts/
    └── build_pdf.py                                # Script tự động tải font Be Vietnam Pro & biên dịch PDF
```

Để biên dịch lại tệp PDF từ mã nguồn:

```bash
pip install typst
python3 scripts/build_pdf.py
```
