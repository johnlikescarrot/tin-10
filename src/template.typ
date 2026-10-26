// =============================================================================
// src/template.typ
// Hệ thống giao diện & thành phần trình bày cho Đề cương Ôn tập Giữa kì I - Tin 10
// Bộ sách: Kết nối tri thức với cuộc sống (Định hướng ICT)
// =============================================================================

// Bảng màu học thuật hiện đại, tương phản cao, in ấn & xem trên màn hình đều sắc nét
#let c-navy       = rgb("#0f2942")
#let c-navy-soft  = rgb("#1e3a5f")
#let c-blue       = rgb("#1d4ed8")
#let c-blue-bg    = rgb("#eff6ff")
#let c-blue-bdr   = rgb("#93c5fd")

#let c-teal       = rgb("#0f766e")
#let c-teal-bg    = rgb("#f0fdfa")
#let c-teal-bdr   = rgb("#5eead4")

#let c-purple     = rgb("#6d28d9")
#let c-purple-bg  = rgb("#f5f3ff")
#let c-purple-bdr = rgb("#c4b5fd")

#let c-amber      = rgb("#b45309")
#let c-amber-bg   = rgb("#fffbeb")
#let c-amber-bdr  = rgb("#fcd34d")

#let c-rose       = rgb("#be123c")
#let c-rose-bg    = rgb("#fff1f2")
#let c-rose-bdr   = rgb("#fda4af")

#let c-green      = rgb("#15803d")
#let c-green-bg   = rgb("#f0fdf4")
#let c-green-bdr  = rgb("#86efac")

#let c-ink        = rgb("#1e293b")
#let c-muted      = rgb("#475569")
#let c-light      = rgb("#f8fafc")
#let c-border     = rgb("#cbd5e1")

// Huy hiệu mức độ nhận thức
#let level-badge(lvl) = {
  let (bg, fg, bdr) = if lvl == "NB" or lvl == "Nhận biết" {
    (rgb("#dbeafe"), rgb("#1e40af"), rgb("#93c5fd"))
  } else if lvl == "TH" or lvl == "Thông hiểu" {
    (rgb("#ccfbf1"), rgb("#115e59"), rgb("#5eead4"))
  } else if lvl == "VD" or lvl == "Vận dụng" {
    (rgb("#fef3c7"), rgb("#92400e"), rgb("#fcd34d"))
  } else {
    (rgb("#ffe4e6"), rgb("#9f1239"), rgb("#fda4af"))
  }
  box(
    inset: (x: 5.5pt, y: 2pt),
    radius: 3pt,
    fill: bg,
    stroke: 0.5pt + bdr,
    baseline: 15%,
    text(size: 7.8pt, weight: "bold", fill: fg)[#lvl]
  )
}

// Huy hiệu dạng nhãn nhỏ
#let pill(label, bg: c-navy, fg: white) = box(
  inset: (x: 7pt, y: 2.5pt),
  radius: 10pt,
  fill: bg,
  baseline: 15%,
  text(size: 8pt, weight: "semibold", fill: fg)[#label]
)

// Banner mở đầu mỗi Phần lớn (Phần I, II, III, IV)
#let part-banner(part-num, title, subtitle, accent: c-navy) = {
  v(4pt)
  block(
    width: 100%,
    fill: accent,
    radius: 7pt,
    inset: (x: 16pt, y: 12pt),
    breakable: false,
    sticky: true,
    [
      #text(size: 8pt, weight: "bold", fill: rgb("#7dd3fc"), tracking: 0.8pt)[ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I • TIN HỌC 10 (KNTT)]
      #v(3pt)
      #heading(level: 1, outlined: true)[#upper(part-num) — #title]
      #if subtitle != none [
        #v(3pt)
        #text(size: 9pt, fill: rgb("#e2e8f0"))[#subtitle]
      ]
    ]
  )
  v(5pt)
}

// Banner mở đầu mỗi Chủ đề trong Phần Lí thuyết
#let topic-banner(code, title, lessons, weight-info, accent: c-blue, bg: c-blue-bg, bdr: c-blue-bdr) = {
  v(6pt)
  block(
    width: 100%,
    fill: bg,
    stroke: (left: 4.5pt + accent, top: 0.6pt + bdr, right: 0.6pt + bdr, bottom: 0.6pt + bdr),
    radius: (right: 6pt, left: 2pt),
    inset: (x: 13pt, y: 10pt),
    breakable: false,
    sticky: true,
    [
      #grid(
        columns: (1fr, auto),
        column-gutter: 8pt,
        align: (left + horizon, right + horizon),
        [#text(size: 8.3pt, weight: "bold", fill: accent, tracking: 0.5pt)[CHƯƠNG TRÌNH TIN HỌC 10 • ĐỊNH HƯỚNG ICT]],
        [#pill(weight-info, bg: accent, fg: white)]
      )
      #v(3pt)
      #heading(level: 2, outlined: true)[#code: #title]
      #v(2pt)
      #text(size: 8.8pt, style: "italic", fill: c-muted)[#lessons]
    ]
  )
  v(4pt)
}

// Hộp khái niệm / kiến thức cốt lõi
#let concept-box(title, body, accent: c-blue, bg: c-blue-bg, bdr: c-blue-bdr, breakable-box: true) = {
  block(
    width: 100%,
    fill: bg,
    stroke: (left: 3.5pt + accent, top: 0.5pt + bdr, right: 0.5pt + bdr, bottom: 0.5pt + bdr),
    radius: 5pt,
    inset: (x: 11pt, y: 9pt),
    above: 7pt,
    below: 7pt,
    breakable: breakable-box,
    [
      #text(size: 9.5pt, weight: "bold", fill: accent)[#title]
      #v(3pt)
      #body
    ]
  )
}

// Hộp mẹo ghi nhớ nhanh / từ khóa vàng
#let memory-box(title, body) = concept-box(
  [GHI NHỚ NHANH • #title],
  body,
  accent: c-amber,
  bg: c-amber-bg,
  bdr: c-amber-bdr,
  breakable-box: false,
)

// Hộp cảnh báo lỗi sai / bẫy đề thi thường gặp
#let pitfall-box(title, body) = concept-box(
  [LƯU Ý TRÁNH BẪY ĐỀ THI • #title],
  body,
  accent: c-rose,
  bg: c-rose-bg,
  bdr: c-rose-bdr,
  breakable-box: false,
)

// Hộp giải đáp trực tiếp từng Yêu cầu cần đạt trong Bản đặc tả gốc (.docx)
#let spec-qa(code, level, prompt, answer) = {
  block(
    width: 100%,
    fill: white,
    stroke: 0.65pt + c-border,
    radius: 5pt,
    inset: 0pt,
    above: 7pt,
    below: 7pt,
    breakable: true,
    [
      #block(
        width: 100%,
        fill: rgb("#f1f5f9"),
        stroke: (bottom: 0.6pt + c-border),
        radius: (top: 5pt),
        inset: (x: 10pt, y: 6.5pt),
        breakable: false,
        sticky: true,
        [
          #level-badge(level)
          #h(4pt)
          #text(size: 8.6pt, weight: "bold", fill: c-navy)[Đặc tả gốc \[#code\]: ]
          #text(size: 9.1pt, weight: "semibold", fill: c-ink)[#prompt]
        ]
      )
      #block(
        width: 100%,
        inset: (x: 11pt, y: 8pt),
        [#answer]
      )
    ]
  )
}

// Hộp câu hỏi Trắc nghiệm 4 lựa chọn
#let mcq(num, level, stem, opt-a, opt-b, opt-c, opt-d, cols: 2) = {
  block(
    width: 100%,
    above: 6pt,
    below: 6pt,
    breakable: false,
    [
      #text(weight: "bold", fill: c-navy)[Câu #num ] #level-badge(level) #h(2pt) #stem
      #v(3pt)
      #if cols == 2 {
        grid(
          columns: (1fr, 1fr),
          column-gutter: 12pt,
          row-gutter: 4pt,
          [*A.* #opt-a],
          [*B.* #opt-b],
          [*C.* #opt-c],
          [*D.* #opt-d],
        )
      } else if cols == 4 {
        grid(
          columns: (1fr, 1fr, 1fr, 1fr),
          column-gutter: 8pt,
          [*A.* #opt-a],
          [*B.* #opt-b],
          [*C.* #opt-c],
          [*D.* #opt-d],
        )
      } else {
        stack(
          spacing: 3.5pt,
          [*A.* #opt-a],
          [*B.* #opt-b],
          [*C.* #opt-c],
          [*D.* #opt-d],
        )
      }
    ]
  )
}

// Hộp câu hỏi Trắc nghiệm Đúng/Sai (4 mệnh đề a, b, c, d)
#let tfq(num, topic-tag, context-stem, st-a, st-b, st-c, st-d) = {
  block(
    width: 100%,
    fill: rgb("#fafcff"),
    stroke: 0.6pt + c-border,
    radius: 5pt,
    inset: (x: 10pt, y: 8pt),
    above: 7pt,
    below: 7pt,
    breakable: false,
    [
      #text(weight: "bold", fill: c-navy)[Câu #num ] #pill(topic-tag, bg: c-teal, fg: white) #h(3pt) #context-stem
      #v(4pt)
      #table(
        columns: (auto, 1fr, auto),
        inset: (x: 6pt, y: 4.5pt),
        stroke: 0.45pt + c-border,
        align: (center + horizon, left + horizon, center + horizon),
        fill: (x, y) => if y == 0 { rgb("#e2e8f0") } else { white },
        [*Ý*], [*Mệnh đề nhận định*], [*Mức độ*],
        [*a)*], [#st-a], [#level-badge("TH")],
        [*b)*], [#st-b], [#level-badge("TH")],
        [*c)*], [#st-c], [#level-badge("VD")],
        [*d)*], [#st-d], [#level-badge("VD")],
      )
    ]
  )
}

// Hộp câu hỏi Tự luận có kèm lời giải chi tiết
#let essay-qa(num, level, points, question, solution) = {
  block(
    width: 100%,
    stroke: 0.65pt + c-border,
    radius: 5pt,
    inset: 0pt,
    above: 8pt,
    below: 8pt,
    breakable: true,
    [
      #block(
        width: 100%,
        fill: rgb("#eff6ff"),
        stroke: (bottom: 0.6pt + c-blue-bdr),
        radius: (top: 5pt),
        inset: (x: 11pt, y: 7pt),
        breakable: false,
        sticky: true,
        [
          #text(weight: "bold", fill: c-navy)[Bài tự luận #num ]
          #level-badge(level)
          #h(4pt)
          #pill(points, bg: c-navy-soft, fg: white)
          #v(3pt)
          #text(weight: "medium", fill: c-ink)[#question]
        ]
      )
      #block(
        width: 100%,
        fill: white,
        inset: (x: 11pt, y: 8pt),
        [
          #text(size: 8.8pt, weight: "bold", fill: c-green)[HƯỚNG DẪN GIẢI CHI TIẾT & THANG ĐIỂM:]
          #v(3pt)
          #solution
        ]
      )
    ]
  )
}

// Hàm thiết lập toàn bộ trang tài liệu
#let setup-study-guide(doc) = {
  set document(
    title: "Đề cương Ôn tập Giữa kì I - Môn Tin học 10 (Kết nối tri thức với cuộc sống)",
    author: "Tài liệu Ôn tập Tin học 10 - Định hướng ICT",
  )

  set page(
    paper: "a4",
    margin: (top: 20mm, bottom: 19mm, left: 17mm, right: 17mm),
    header: context {
      if counter(page).get().first() > 1 [
        #set text(size: 8pt, fill: c-muted)
        #grid(
          columns: (1fr, auto),
          align: (left + bottom, right + bottom),
          [ĐỀ CƯƠNG ÔN TẬP GIỮA HỌC KÌ I • TIN HỌC 10 (ĐỊNH HƯỚNG ICT)],
          [*Bộ sách: Kết nối tri thức với cuộc sống*]
        )
        #v(-4pt)
        #line(length: 100%, stroke: 0.5pt + c-border)
      ]
    },
    footer: context {
      if counter(page).get().first() > 1 [
        #line(length: 100%, stroke: 0.5pt + c-border)
        #v(-3pt)
        #set text(size: 8pt, fill: c-muted)
        #grid(
          columns: (1fr, auto),
          align: (left + top, right + top),
          [Bám sát 100% Ma trận & Bản đặc tả Đề kiểm tra Giữa kì I (Chủ đề A, B, D)],
          [
            #box(
              fill: rgb("#e2e8f0"),
              inset: (x: 7pt, y: 2pt),
              radius: 8pt,
              text(weight: "bold", fill: c-navy)[
                Trang #counter(page).display("1 / 1", both: true)
              ]
            )
          ]
        )
      ]
    }
  )

  set text(
    font: "Be Vietnam Pro",
    lang: "vi",
    size: 9.5pt,
    fill: c-ink,
  )

  set par(
    leading: 0.58em,
    spacing: 0.72em,
    justify: true,
  )

  set list(indent: 6pt, body-indent: 5pt, spacing: 0.55em)
  set enum(indent: 6pt, body-indent: 5pt, spacing: 0.55em)

  show raw: set text(font: "DejaVu Sans Mono", size: 8.6pt)

  show outline.entry.where(level: 1): it => {
    v(3pt, weak: true)
    strong(text(fill: c-navy, size: 9.2pt)[#it])
  }

  show outline.entry.where(level: 2): it => {
    text(fill: c-ink, size: 8.8pt)[#it]
  }

  show heading: set block(sticky: true)

  show heading.where(level: 1): it => {
    set text(size: 14.2pt, weight: "extrabold", fill: white)
    it.body
  }

  show heading.where(level: 2): it => {
    set text(size: 12.2pt, weight: "bold", fill: c-navy)
    it.body
  }

  show heading.where(level: 3): it => {
    v(4pt)
    block(
      sticky: true,
      breakable: false,
      [
        #box(width: 4pt, height: 10pt, fill: c-blue, radius: 1.5pt, baseline: 12%)
        #h(5pt)
        #text(size: 10.6pt, weight: "bold", fill: c-navy)[#it.body]
      ]
    )
    v(2pt)
  }

  show heading.where(level: 4): it => {
    v(2pt)
    block(
      sticky: true,
      breakable: false,
      text(size: 9.8pt, weight: "bold", fill: c-navy-soft)[#it.body]
    )
    v(1pt)
  }

  doc
}
