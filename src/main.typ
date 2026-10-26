// =============================================================================
// src/main.typ
// Điểm vào biên dịch chính cho Đề cương Ôn tập Giữa kì I - Tin học 10 (KNTT)
// =============================================================================

#import "template.typ": *

#show: setup-study-guide

// ============================= TRANG BÌA & TỔNG QUAN ==========================
#block(
  width: 100%,
  fill: c-navy,
  radius: 10pt,
  inset: (x: 22pt, y: 20pt),
  breakable: false,
  [
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      [
        #box(
          fill: rgb("#1e3a5f"),
          stroke: 0.6pt + rgb("#38bdf8"),
          radius: 12pt,
          inset: (x: 10pt, y: 3.5pt),
          text(size: 8pt, weight: "bold", fill: rgb("#bae6fd"), tracking: 0.6pt)[
            CHƯƠNG TRÌNH GDPT 2018 • ĐỊNH HƯỚNG TIN HỌC ỨNG DỤNG (ICT)
          ]
        )
      ],
      [
        #text(size: 8.5pt, weight: "semibold", fill: rgb("#93c5fd"))[Bộ sách: *Kết nối tri thức với cuộc sống*]
      ]
    )
    #v(10pt)
    #text(size: 21pt, weight: "extrabold", fill: white)[ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I]
    #v(4pt)
    #text(size: 15.5pt, weight: "bold", fill: rgb("#38bdf8"))[MÔN TIN HỌC LỚP 10 — TÀI LIỆU HỆ THỐNG HOÁ TOÀN DIỆN]
    #v(8pt)
    #line(length: 100%, stroke: 0.7pt + rgb("#334155"))
    #v(6pt)
    #text(size: 9.4pt, fill: rgb("#e2e8f0"))[
      Biên soạn bám sát *100% Ma trận & Bản đặc tả gốc* (`MA TRAN GIUA KI I - LOP 10.docx`): Hệ thống hoá lí thuyết cô đọng dễ thuộc • Giải đáp trực tiếp *35/35 yêu cầu cần đạt* • Ngân hàng *50 câu TN 4 lựa chọn + 08 câu Đúng/Sai + 09 bài Tự luận* • *02 Đề thi thử 45 phút* có lời giải & thang điểm chi tiết.
    ]
    #v(10pt)
    #grid(
      columns: (1fr, 1fr, 1fr, 1fr),
      column-gutter: 8pt,
      block(width: 100%, fill: rgb("#163554"), radius: 6pt, inset: 8pt)[
        #text(size: 7.5pt, fill: rgb("#93c5fd"))[THỜI GIAN LÀM BÀI]\
        #text(size: 12pt, weight: "bold", fill: white)[45 Phút]
      ],
      block(width: 100%, fill: rgb("#163554"), radius: 6pt, inset: 8pt)[
        #text(size: 7.5pt, fill: rgb("#93c5fd"))[CẤU TRÚC ĐIỂM SỐ]\
        #text(size: 12pt, weight: "bold", fill: white)[70% TN • 30% TL]
      ],
      block(width: 100%, fill: rgb("#163554"), radius: 6pt, inset: 8pt)[
        #text(size: 7.5pt, fill: rgb("#93c5fd"))[SỐ LƯỢNG CÂU HỎI]\
        #text(size: 11.2pt, weight: "bold", fill: white)[20 TN + 2 ĐS + 3 TL]
      ],
      block(width: 100%, fill: rgb("#163554"), radius: 6pt, inset: 8pt)[
        #text(size: 7.5pt, fill: rgb("#93c5fd"))[MA TRẬN NHẬN THỨC]\
        #text(size: 10.8pt, weight: "bold", fill: white)[40•30•20•10 (%)]
      ],
    )
  ]
)

#v(8pt)

// Ba thẻ tóm tắt 3 Chủ đề trọng tâm ngay trang đầu
#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 8pt,
  block(width: 100%, fill: c-blue-bg, stroke: 0.6pt + c-blue-bdr, radius: 6pt, inset: 9pt)[
    #pill("Chủ đề A • 4,0 điểm (40%)", bg: c-blue, fg: white)
    #v(4pt)
    *Máy tính và xã hội tri thức*\
    #text(size: 8.4pt, fill: c-muted)[• Bài 1: Thông tin, dữ liệu, đổi đơn vị B–TB\ • Bài 2: Thiết bị thông minh & CMCN 4.0\ • Bài 7: Kĩ năng sử dụng thiết bị số]
  ],
  block(width: 100%, fill: c-teal-bg, stroke: 0.6pt + c-teal-bdr, radius: 6pt, inset: 9pt)[
    #pill("Chủ đề B • 4,0 điểm (40%)", bg: c-teal, fg: white)
    #v(4pt)
    *Mạng máy tính và Internet*\
    #text(size: 8.4pt, fill: c-muted)[• Bài 8: LAN, Internet, Đám mây, IoT\ • Bài 9: Mã độc, chống bắt nạt mạng\ • Bài 10: Dịch tự động & Học liệu mở]
  ],
  block(width: 100%, fill: c-purple-bg, stroke: 0.6pt + c-purple-bdr, radius: 6pt, inset: 9pt)[
    #pill("Chủ đề D • 2,0 điểm (20%)", bg: c-purple, fg: white)
    #v(4pt)
    *Đạo đức, pháp luật môi trường số*\
    #text(size: 8.4pt, fill: c-muted)[• Bài 11: Luật CNTT, Luật An ninh mạng\ • Nghị định 72/2013 & NĐ 15/2020\ • Luật SHTT (Bản quyền) & Ứng xử MXH]
  ],
)

#v(8pt)

// Hộp Mục lục tự động
#block(
  width: 100%,
  fill: c-light,
  stroke: 0.6pt + c-border,
  radius: 7pt,
  inset: (x: 14pt, y: 11pt),
  breakable: true,
  [
    #text(size: 11pt, weight: "extrabold", fill: c-navy)[MỤC LỤC TRA CỨU NHANH ĐỀ CƯƠNG]
    #v(4pt)
    #line(length: 100%, stroke: 0.5pt + c-border)
    #v(4pt)
    #set text(size: 9pt)
    #outline(
      title: none,
      indent: 12pt,
      depth: 2,
    )
  ]
)

#pagebreak()

// ========================== NỘI DUNG CÁC PHẦN CHÍNH ===========================
#include "01-ma-tran-va-chien-luoc.typ"
#include "02-ly-thuyet-chu-de-a.typ"
#include "03-ly-thuyet-chu-de-b.typ"
#include "04-ly-thuyet-chu-de-d.typ"
#include "05-ngan-hang-cau-hoi.typ"
#include "06-de-thi-thu.typ"
