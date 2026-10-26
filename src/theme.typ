// Shared palette & pedagogical UI components for Typst

#let c-navy = rgb("#1B365D")
#let c-navy-dark = rgb("#0F2342")
#let c-navy-light = rgb("#EBF1F8")
#let c-teal = rgb("#0F766E")
#let c-teal-light = rgb("#E6F5F3")
#let c-amber = rgb("#B45309")
#let c-amber-light = rgb("#FEF3C7")
#let c-red = rgb("#B91C1C")
#let c-red-light = rgb("#FEE2E2")
#let c-green = rgb("#15803D")
#let c-green-light = rgb("#DCFCE7")
#let c-purple = rgb("#6D28D9")
#let c-purple-light = rgb("#F3E8FF")
#let c-slate = rgb("#334155")
#let c-muted = rgb("#64748B")
#let c-border = rgb("#CBD5E1")
#let c-bg-soft = rgb("#F8FAFC")

#let callout(title: "", tone: "info", body) = {
  let (bg, border, title-col) = if tone == "memo" {
    (c-amber-light.lighten(38%), c-amber, c-amber)
  } else if tone == "warn" {
    (c-red-light.lighten(38%), c-red, c-red)
  } else if tone == "answer" {
    (c-green-light.lighten(38%), c-green, c-green)
  } else if tone == "law" {
    (c-purple-light.lighten(38%), c-purple, c-purple)
  } else if tone == "teal" {
    (c-teal-light.lighten(25%), c-teal, c-teal)
  } else {
    (c-navy-light.lighten(20%), c-navy, c-navy)
  }
  block(
    width: 100%,
    fill: bg,
    stroke: (
      left: 3.5pt + border,
      top: 0.5pt + border.lighten(55%),
      right: 0.5pt + border.lighten(55%),
      bottom: 0.5pt + border.lighten(55%),
    ),
    radius: 4pt,
    inset: (x: 10pt, y: 8pt),
    breakable: true,
    [
      #if title != "" [
        #block(breakable: false, below: 5pt)[
          #text(fill: title-col, weight: "bold", size: 9.6pt)[#title]
        ]
      ]
      #body
    ],
  )
}

#let badge(label, col: c-navy) = box(
  fill: col.lighten(86%),
  stroke: 0.5pt + col.lighten(35%),
  radius: 3pt,
  inset: (x: 5pt, y: 1.6pt),
  baseline: 15%,
  text(size: 7.6pt, weight: "bold", fill: col)[#label],
)

#let level-col(level) = {
  if level == "Nhận biết" { c-teal }
  else if level == "Thông hiểu" { c-navy }
  else if level == "Vận dụng" { c-amber }
  else { c-red }
}

#let mcq(num, level, stem, a, b, c, d) = block(
  width: 100%,
  breakable: false,
  spacing: 0.72em,
  [
    #text(weight: "bold", fill: c-navy)[Câu #num.] #badge(level, col: level-col(level)) #stem
    #v(2pt)
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 12pt,
      row-gutter: 3.5pt,
      [*A.* #a],
      [*B.* #b],
      [*C.* #c],
      [*D.* #d],
    )
  ],
)

#let mcq-stack(num, level, stem, a, b, c, d) = block(
  width: 100%,
  breakable: false,
  spacing: 0.72em,
  [
    #text(weight: "bold", fill: c-navy)[Câu #num.] #badge(level, col: level-col(level)) #stem
    #v(2pt)
    #pad(left: 6pt)[
      *A.* #a \
      *B.* #b \
      *C.* #c \
      *D.* #d
    ]
  ],
)

#let qa-card(code, level, highlight: none, question, answer) = {
  let border-col = if highlight == "red" { c-red } else if highlight == "green" { c-green } else { c-navy.lighten(25%) }
  let hdr-bg = if highlight == "red" { c-red-light.lighten(25%) } else if highlight == "green" { c-green-light.lighten(25%) } else { c-navy-light.lighten(20%) }
  block(
    width: 100%,
    stroke: 0.6pt + border-col.lighten(30%),
    radius: 4pt,
    clip: true,
    breakable: true,
    spacing: 0.8em,
    [
      #block(
        width: 100%,
        fill: hdr-bg,
        inset: (x: 9pt, y: 6pt),
        breakable: false,
        [
          #text(weight: "bold", fill: c-navy-dark)[#code] #h(4pt) #badge(level, col: level-col(level))
          #if highlight == "red" [ #h(4pt) #badge("Trọng tâm GV đánh dấu ĐỎ", col: c-red) ]
          #if highlight == "green" [ #h(4pt) #badge("Trọng tâm GV đánh dấu XANH", col: c-green) ]
          #v(2pt)
          #text(weight: "semibold", fill: rgb("#0F172A"))[#question]
        ],
      )
      #block(
        width: 100%,
        fill: white,
        inset: (x: 10pt, y: 7pt),
        [#answer],
      )
    ],
  )
}
