// ============================================================================
// TEMPLATE: ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I - TIN HỌC 10 (KẾT NỐI TRI THỨC)
// ============================================================================

#let c-navy = rgb("#16325C")
#let c-navy-light = rgb("#EAF1F8")
#let c-teal = rgb("#0E7490")
#let c-teal-light = rgb("#ECFEFF")
#let c-amber = rgb("#B45309")
#let c-amber-light = rgb("#FFFBEB")
#let c-red = rgb("#B91C1C")
#let c-red-light = rgb("#FEF2F2")
#let c-green = rgb("#15803D")
#let c-green-light = rgb("#F0FDF4")
#let c-purple = rgb("#4338CA")
#let c-purple-light = rgb("#EEF2FF")
#let c-slate = rgb("#334155")
#let c-muted = rgb("#64748B")
#let c-border = rgb("#CBD5E1")
#let c-bg-soft = rgb("#F8FAFC")

#let setup-doc(body) = {
  set document(
    title: "Đề cương ôn tập Giữa kì I - Tin học 10 (Kết nối tri thức với cuộc sống)",
    author: "Tổ Tin học - Biên soạn theo Ma trận & Đặc tả Giữa kì I",
  )

  set page(
    paper: "a4",
    margin: (top: 2.1cm, bottom: 2.0cm, left: 1.8cm, right: 1.8cm),
    header: context {
      if counter(page).get().first() > 1 [
        #set text(size: 8.5pt, fill: c-muted, font: "Be Vietnam Pro")
        #grid(
          columns: (1fr, auto),
          align: (left, right),
          [*ĐỀ CƯƠNG ÔN TẬP GIỮA KÌ I • TIN HỌC 10 (ĐỊNH HƯỚNG ICT)*],
          [_Bộ sách Kết nối tri thức với cuộc sống_],
        )
        #v(-4pt)
        #line(length: 100%, stroke: 0.5pt + c-border)
      ]
    },
    footer: context {
      let pg = counter(page).get().first()
      let total = counter(page).final().first()
      set text(size: 8.5pt, fill: c-muted, font: "Be Vietnam Pro")
      line(length: 100%, stroke: 0.5pt + c-border)
      v(-2pt)
      grid(
        columns: (1fr, auto),
        align: (left, right),
        [Tài liệu ôn tập bám sát 100% Ma trận & Đặc tả đề kiểm tra Giữa kì I],
        [*Trang #pg / #total*],
      )
    },
  )

  set text(
    font: "Be Vietnam Pro",
    size: 9.8pt,
    fill: rgb("#1E293B"),
    lang: "vi",
  )

  set par(
    leading: 0.65em,
    spacing: 1.02em,
    justify: true,
  )

  // Avoid ugly stretched inter-word spacing inside narrow table cells
  show table.cell: set par(justify: false)

  set list(
    indent: 6pt,
    body-indent: 6pt,
    marker: ([#text(fill: c-teal, weight: "bold")[•]], [#text(fill: c-navy)[–]], [◦]),
  )

  set enum(
    indent: 6pt,
    body-indent: 6pt,
  )

  show raw: set text(font: "DejaVu Sans Mono", size: 8.8pt)

  // Heading styles
  show heading.where(level: 1): it => {
    v(10pt, weak: true)
    block(
      width: 100%,
      fill: c-navy,
      radius: 5pt,
      inset: (x: 12pt, y: 9pt),
      breakable: false,
      text(fill: white, size: 12.5pt, weight: "bold")[#upper(it.body)],
    )
    v(6pt, weak: true)
  }

  show heading.where(level: 2): it => {
    v(9pt, weak: true)
    block(
      width: 100%,
      stroke: (left: 4pt + c-teal, bottom: 0.7pt + c-border),
      fill: c-navy-light,
      inset: (left: 10pt, right: 8pt, top: 6pt, bottom: 6pt),
      radius: (right: 4pt),
      breakable: false,
      text(fill: c-navy, size: 10.8pt, weight: "bold")[#it.body],
    )
    v(5pt, weak: true)
  }

  show heading.where(level: 3): it => {
    v(7pt, weak: true)
    block(
      breakable: false,
      text(fill: c-teal, size: 10.2pt, weight: "bold")[#it.body],
    )
    v(3pt, weak: true)
  }

  body
}

// Reusable Callout Boxes with crisp vector tag badges (no missing emoji glyphs)
#let callout(title: "", tag: "", accent: c-teal, bg: c-teal-light, breakable-box: true, body) = {
  block(
    width: 100%,
    fill: bg,
    stroke: (
      left: 3.5pt + accent,
      top: 0.5pt + accent.lighten(60%),
      right: 0.5pt + accent.lighten(60%),
      bottom: 0.5pt + accent.lighten(60%),
    ),
    radius: 4pt,
    inset: (x: 10pt, y: 8pt),
    breakable: breakable-box,
    [
      #if title != "" [
        #if tag != "" [
          #box(
            fill: accent,
            radius: 2.5pt,
            inset: (x: 5pt, y: 1.5pt),
            baseline: 12%,
            text(fill: white, size: 7.3pt, weight: "bold")[#tag],
          )
          #h(4pt)
        ]
        #text(fill: accent.darken(15%), weight: "bold", size: 9.8pt)[#title]
        #v(3pt)
      ]
      #body
    ],
  )
}

#let concept-box(title: "Khái niệm cốt lõi", body) = callout(
  title: title,
  tag: "TRỌNG TÂM",
  accent: c-teal,
  bg: c-teal-light,
  body,
)

#let tip-box(title: "Mẹo ghi nhớ nhanh", body) = callout(
  title: title,
  tag: "MẸO NHỚ",
  accent: c-amber,
  bg: c-amber-light,
  breakable-box: false,
  body,
)

#let warn-box(title: "Lưu ý & Bẫy thường gặp trong phòng thi", body) = callout(
  title: title,
  tag: "CẢNH BÁO",
  accent: c-red,
  bg: c-red-light,
  breakable-box: false,
  body,
)

#let formula-box(title: "Công thức & Quy tắc tính nhanh", body) = callout(
  title: title,
  tag: "QUY TẮC",
  accent: c-purple,
  bg: c-purple-light,
  breakable-box: false,
  body,
)

#let example-box(title: "Ví dụ minh họa & Lời giải mẫu", body) = callout(
  title: title,
  tag: "LỜI GIẢI MẪU",
  accent: c-green,
  bg: c-green-light,
  body,
)

// Level badge
#let badge(lvl) = {
  let (bg, fg) = if lvl == "NB" {
    (rgb("#DBEAFE"), rgb("#1D4ED8"))
  } else if lvl == "TH" {
    (rgb("#DCFCE7"), rgb("#15803D"))
  } else if lvl == "VD" {
    (rgb("#FEF3C7"), rgb("#B45309"))
  } else {
    (rgb("#FEE2E2"), rgb("#B91C1C"))
  }
  box(
    fill: bg,
    radius: 3pt,
    inset: (x: 5pt, y: 1.5pt),
    baseline: 12%,
    text(size: 7.6pt, weight: "bold", fill: fg)[#lvl],
  )
}

// Multiple Choice Question Helper
#let mcq(num, lvl, stem, a, b, c, d, cols: 2) = {
  block(
    width: 100%,
    breakable: false,
    above: 8pt,
    below: 8pt,
    [
      *Câu #num.* #badge(lvl) #h(2pt) #stem
      #v(2.5pt)
      #set par(justify: false)
      #if cols == 2 [
        #grid(
          columns: (1fr, 1fr),
          column-gutter: 12pt,
          row-gutter: 4pt,
          [*A.* #a], [*B.* #b],
          [*C.* #c], [*D.* #d],
        )
      ] else if cols == 4 [
        #grid(
          columns: (1fr, 1fr, 1fr, 1fr),
          column-gutter: 8pt,
          [*A.* #a], [*B.* #b], [*C.* #c], [*D.* #d],
        )
      ] else [
        *A.* #a \
        *B.* #b \
        *C.* #c \
        *D.* #d
      ]
    ],
  )
}

// True/False Question Helper (4 statements a, b, c, d)
#let tfq(num, topic-tag, context-stem, sa, la, sb, lb, sc, lc, sd, ld) = {
  block(
    width: 100%,
    breakable: false,
    stroke: 0.7pt + c-border,
    radius: 4pt,
    inset: 9pt,
    above: 8pt,
    below: 8pt,
    fill: rgb("#FFFFFF"),
    [
      *Câu #num.* #box(fill: c-navy-light, radius: 3pt, inset: (x: 6pt, y: 1.5pt), baseline: 12%, text(size: 7.8pt, weight: "bold", fill: c-navy)[#topic-tag]) #h(2pt) #context-stem
      #v(4pt)
      #table(
        columns: (auto, 1fr, auto),
        inset: (x: 6pt, y: 5pt),
        align: (center + horizon, left + horizon, center + horizon),
        stroke: 0.5pt + c-border,
        fill: (_, row) => if row == 0 { c-bg-soft } else { white },
        [*Ý*], [*Mệnh đề nhận định*], [*Mức độ*],
        [*a)*], [#sa], [#badge(la)],
        [*b)*], [#sb], [#badge(lb)],
        [*c)*], [#sc], [#badge(lc)],
        [*d)*], [#sd], [#badge(ld)],
      )
    ],
  )
}
