// ============================================================================
// ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I - MÔN TIN HỌC 10
// Bộ sách: Kết nối tri thức với cuộc sống (Định hướng Tin học ứng dụng - ICT)
// ============================================================================

#import "theme.typ": *

#set document(
  title: "Đề cương Ôn tập Giữa Học kì I - Môn Tin học 10 (Kết nối tri thức với cuộc sống - Định hướng ICT)",
  author: "Biên soạn theo Ma trận & Bản đặc tả Giữa kì I - Tin học 10",
)

#set page(
  paper: "a4",
  margin: (top: 21mm, bottom: 20mm, left: 16mm, right: 16mm),
  header: context {
    if counter(page).get().first() > 1 [
      #set text(size: 8pt, fill: c-muted, font: "Be Vietnam Pro")
      #grid(
        columns: (1fr, auto),
        align: (left, right),
        [*ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I — TIN HỌC 10* _(Kết nối tri thức với cuộc sống • Định hướng ICT)_],
        [Tài liệu ôn tập chuẩn Ma trận],
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + c-border)
    ]
  },
  footer: context {
    if counter(page).get().first() > 1 [
      #line(length: 100%, stroke: 0.5pt + c-border)
      #v(-2pt)
      #set text(size: 8pt, fill: c-muted, font: "Be Vietnam Pro")
      #grid(
        columns: (1fr, auto),
        align: (left, right),
        [Môn Tin học 10 — Bộ sách Kết nối tri thức với cuộc sống],
        [*Trang #counter(page).display("1 / 1", both: true)*],
      )
    ]
  },
)

#set text(
  font: "Be Vietnam Pro",
  size: 9.7pt,
  fill: rgb("#1E293B"),
  lang: "vi",
)

#set par(
  justify: true,
  leading: 0.64em,
  spacing: 0.9em,
)

#show table.cell: set par(justify: false)

#set list(
  indent: 0.5em,
  body-indent: 0.45em,
  marker: ([#text(fill: c-teal, weight: "bold")[•]], [#text(fill: c-navy)[◦]], [#text(fill: c-amber)[▪]]),
)

#set enum(
  indent: 0.5em,
  body-indent: 0.45em,
)

#show raw: set text(font: "JetBrains Mono", size: 8.7pt, fill: rgb("#0F172A"))
#show raw.where(block: false): box.with(
  fill: rgb("#F1F5F9"),
  inset: (x: 3.5pt, y: 0pt),
  outset: (y: 1.8pt),
  radius: 2.5pt,
)

// Heading styles
#show heading.where(level: 1): it => {
  v(0.4em)
  block(
    width: 100%,
    fill: c-navy,
    radius: 5pt,
    inset: (x: 12pt, y: 8.5pt),
    breakable: false,
    [
      #set text(fill: white, size: 12pt, weight: "bold")
      #it.body
    ],
  )
  v(0.3em)
}

#show heading.where(level: 2): it => {
  v(0.5em)
  block(
    width: 100%,
    fill: c-navy-light,
    stroke: (left: 4pt + c-navy),
    radius: (right: 4pt),
    inset: (x: 10pt, y: 6pt),
    breakable: false,
    [
      #set text(fill: c-navy-dark, size: 10.6pt, weight: "bold")
      #it.body
    ],
  )
  v(0.22em)
}

#show heading.where(level: 3): it => {
  v(0.38em)
  block(
    breakable: false,
    [
      #set text(fill: c-teal, size: 10pt, weight: "bold")
      #it.body
      #v(-4pt)
      #line(length: 100%, stroke: 0.6pt + c-teal.lighten(55%))
    ],
  )
  v(0.15em)
}

// ============================================================================
// COVER PAGE & TABLE OF CONTENTS
// ============================================================================
#block(
  width: 100%,
  fill: c-navy-dark,
  radius: 7pt,
  inset: (x: 16pt, y: 14pt),
  [
    #align(center)[
      #text(fill: rgb("#93C5FD"), size: 8.6pt, weight: "semibold", tracking: 0.9pt)[CHƯƠNG TRÌNH GDPT 2018 • BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG]
      #v(4pt)
      #line(length: 68%, stroke: 0.9pt + rgb("#38BDF8"))
      #v(6pt)
      #text(fill: white, size: 19pt, weight: "bold")[ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I]
      #v(3pt)
      #text(fill: rgb("#FDE68A"), size: 13.8pt, weight: "bold")[MÔN: TIN HỌC 10 — ĐỊNH HƯỚNG TIN HỌC ỨNG DỤNG (ICT)]
      #v(6pt)
      #text(fill: rgb("#E2E8F0"), size: 9pt, style: "italic")[
        Phân tích chuyên sâu Ma trận & Bản đặc tả gốc • Hệ thống hóa toàn bộ kiến thức & mẹo ghi nhớ nhanh • \
        Giải đáp 100% yêu cầu trong tài liệu gốc • Ngân hàng câu hỏi phân hóa & 02 Đề thi thử chuẩn cấu trúc
      ]
      #v(5pt)
      #line(length: 68%, stroke: 0.9pt + rgb("#38BDF8"))
    ]
  ],
)

#v(5pt)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 7pt,
  block(width: 100%, fill: c-navy-light, stroke: 0.6pt + c-navy.lighten(50%), radius: 5pt, inset: 6pt)[
    #align(center)[
      #text(size: 7.5pt, fill: c-muted, weight: "semibold")[THỜI GIAN LÀM BÀI]\
      #v(1pt)
      #text(size: 11.8pt, fill: c-navy, weight: "bold")[45 PHÚT]\
      #text(size: 7.4pt, fill: c-slate)[Kiểm tra Giữa kì I]
    ]
  ],
  block(width: 100%, fill: c-teal-light, stroke: 0.6pt + c-teal.lighten(50%), radius: 5pt, inset: 6pt)[
    #align(center)[
      #text(size: 7.5pt, fill: c-muted, weight: "semibold")[TRẮC NGHIỆM (70%)]\
      #v(1pt)
      #text(size: 11.8pt, fill: c-teal, weight: "bold")[7,0 ĐIỂM]\
      #text(size: 7.4pt, fill: c-slate)[20 câu 4 LC + 2 câu Đ/S]
    ]
  ],
  block(width: 100%, fill: c-amber-light.lighten(20%), stroke: 0.6pt + c-amber.lighten(40%), radius: 5pt, inset: 6pt)[
    #align(center)[
      #text(size: 7.5pt, fill: c-muted, weight: "semibold")[TỰ LUẬN (30%)]\
      #v(1pt)
      #text(size: 11.8pt, fill: c-amber, weight: "bold")[3,0 ĐIỂM]\
      #text(size: 7.4pt, fill: c-slate)[3 câu (TH • VD • VDC)]
    ]
  ],
  block(width: 100%, fill: c-purple-light.lighten(20%), stroke: 0.6pt + c-purple.lighten(40%), radius: 5pt, inset: 6pt)[
    #align(center)[
      #text(size: 7.5pt, fill: c-muted, weight: "semibold")[PHẠM VI KIẾN THỨC]\
      #v(1pt)
      #text(size: 11.8pt, fill: c-purple, weight: "bold")[CHỦ ĐỀ 1, 2, 3]\
      #text(size: 7.4pt, fill: c-slate)[SGK Kết nối tri thức]
    ]
  ],
)

#v(5pt)

#callout(title: "LỘ TRÌNH 4 BƯỚC ÔN TẬP CHỦ ĐỘNG ĐỂ CHINH PHỤC ĐIỂM 9 – 10", tone: "teal")[
  #set text(size: 9pt)
  #set par(leading: 0.54em, spacing: 0.55em)
  + *Bước 1 — Đọc vị Ma trận & Bản đặc tả (Phần I):* Hiểu rõ cấu trúc đề thi 45 phút (20 câu trắc nghiệm 4 lựa chọn = 5,0đ; 2 câu Đúng/Sai = 2,0đ; 3 câu Tự luận = 3,0đ) và tỉ trọng từng Chủ đề để phân bổ sức học hợp lí.
  + *Bước 2 — Nắm chắc Lý thuyết cốt lõi & Mẹo ghi nhớ nhanh (Phần II):* Học theo sơ đồ bảng đối chiếu, công thức đóng khung và từ khóa vàng cho trọn vẹn các bài thuộc Chủ đề 1, Chủ đề 2, Chủ đề 3 sách _Kết nối tri thức với cuộc sống_.
  + *Bước 3 — Thuộc lòng Đáp án 35 Yêu cầu chuẩn trong Bản đặc tả gốc (Phần III):* Đối chiếu trực tiếp từng yêu cầu đánh giá trong tài liệu `MA TRAN GIUA KI I - LOP 10.docx` với câu trả lời mẫu và ví dụ minh họa chuẩn mực.
  + *Bước 4 — Rèn kỹ năng giải đề & Tự kiểm tra bấm giờ (Phần IV & Phần V):* Luyện tập 45 câu TN 4 lựa chọn, 6 câu Đúng/Sai (24 ý), 10 bài Tự luận trọng tâm và làm thử *02 Đề kiểm tra chuẩn 100% Ma trận* kèm hướng dẫn chấm chi tiết.
]

#v(4pt)

#block(
  width: 100%,
  fill: c-bg-soft,
  stroke: 0.7pt + c-border,
  radius: 6pt,
  inset: (x: 12pt, y: 8pt),
  [
    #text(size: 10pt, weight: "bold", fill: c-navy)[MỤC LỤC CHI TIẾT]
    #v(2pt)
    #set text(size: 8.5pt)
    #show outline.entry: set block(spacing: 0.52em)
    #outline(title: none, indent: 1.1em, depth: 2)
  ],
)

#pagebreak()

#include "part1_matrix.typ"
#pagebreak()
#include "part2_theory.typ"
#pagebreak()
#include "part3_spec_qa.typ"
#pagebreak()
#include "part4_practice.typ"
#pagebreak()
#include "part5_mock_exams.typ"
