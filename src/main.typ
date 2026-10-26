#import "template.typ": *

#show: setup-doc

// ============================================================================
// TRANG BÌA / BANNER HỌC THUẬT & BẢNG TỔNG QUAN NHANH
// ============================================================================

#block(
  width: 100%,
  fill: c-navy,
  radius: 8pt,
  inset: (x: 18pt, y: 16pt),
  breakable: false,
  [
    #set text(fill: white)
    #set par(justify: false)
    #align(center)[
      #box(
        fill: rgb("#0E7490"),
        radius: 12pt,
        inset: (x: 12pt, y: 4pt),
        text(size: 8.5pt, weight: "bold")[CHƯƠNG TRÌNH GDPT 2018 • BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG],
      )
      #v(6pt)
      #text(size: 18.5pt, weight: "extrabold")[ĐỀ CƯƠNG ÔN TẬP KIỂM TRA GIỮA HỌC KÌ I]
      #v(3pt)
      #text(size: 13pt, weight: "semibold", fill: rgb("#BAE6FD"))[MÔN: TIN HỌC 10 – ĐỊNH HƯỚNG TIN HỌC ỨNG DỤNG (ICT)]
      #v(6pt)
      #line(length: 65%, stroke: 0.8pt + rgb("#38BDF8"))
      #v(4pt)
      #text(size: 9.2pt, fill: rgb("#E2E8F0"))[
        Biên soạn chi tiết bám sát 100% Ma trận & Bảng đặc tả đề kiểm tra Giữa kì I \
        _Hệ thống lý thuyết cô đọng • Mẹo ghi nhớ nhanh • Ngân hàng câu hỏi chuẩn cấu trúc mới • Đề thi thử & Đáp án chi tiết_
      ]
    ]
  ],
)

#v(8pt)

#block(breakable: false)[
  #set par(justify: false)
  #grid(
    columns: (1fr, 1fr, 1fr, 1fr),
    column-gutter: 8pt,
    block(width: 100%, height: 60pt, fill: c-navy-light, stroke: 0.6pt + c-border, radius: 5pt, inset: 7pt)[
      #align(center + horizon)[
        #text(size: 7.6pt, fill: c-muted, weight: "bold")[THỜI GIAN LÀM BÀI] \
        #v(2pt)
        #text(size: 12.5pt, fill: c-navy, weight: "bold")[45 Phút] \
        #text(size: 7.6pt, fill: c-slate)[70% TN – 30% TL]
      ]
    ],
    block(width: 100%, height: 60pt, fill: c-teal-light, stroke: 0.6pt + c-teal.lighten(50%), radius: 5pt, inset: 7pt)[
      #align(center + horizon)[
        #text(size: 7.6pt, fill: c-muted, weight: "bold")[TRẮC NGHIỆM 4 ĐÁP ÁN] \
        #v(2pt)
        #text(size: 12.5pt, fill: c-teal, weight: "bold")[20 Câu (5,0đ)] \
        #text(size: 7.6pt, fill: c-slate)[0,25 điểm / câu]
      ]
    ],
    block(width: 100%, height: 60pt, fill: c-amber-light, stroke: 0.6pt + c-amber.lighten(50%), radius: 5pt, inset: 7pt)[
      #align(center + horizon)[
        #text(size: 7.6pt, fill: c-muted, weight: "bold")[TRẮC NGHIỆM ĐÚNG/SAI] \
        #v(2pt)
        #text(size: 12.5pt, fill: c-amber, weight: "bold")[02 Câu (2,0đ)] \
        #text(size: 7.6pt, fill: c-slate)[8 mệnh đề (A.2 & B.1)]
      ]
    ],
    block(width: 100%, height: 60pt, fill: c-green-light, stroke: 0.6pt + c-green.lighten(50%), radius: 5pt, inset: 7pt)[
      #align(center + horizon)[
        #text(size: 7.6pt, fill: c-muted, weight: "bold")[PHẦN TỰ LUẬN] \
        #v(2pt)
        #text(size: 12.5pt, fill: c-green, weight: "bold")[03 Câu (3,0đ)] \
        #text(size: 7.6pt, fill: c-slate)[1 TH • 1 VD • 1 VDC]
      ]
    ],
  )
]

#v(8pt)

#block(
  width: 100%,
  fill: c-bg-soft,
  stroke: 0.7pt + c-border,
  radius: 5pt,
  inset: (x: 12pt, y: 10pt),
  [
    #text(size: 10.5pt, weight: "bold", fill: c-navy)[#sym.diamond.filled #h(3pt) MỤC LỤC TRA CỨU NHANH ĐỀ CƯƠNG]
    #v(4pt)
    #outline(
      title: none,
      indent: 12pt,
      depth: 2,
    )
  ],
)

#pagebreak()

#include "part1_matrix.typ"
#pagebreak()
#include "part2_theory.typ"
#pagebreak()
#include "part3_questions.typ"
#pagebreak()
#include "part4_mock_exam.typ"
