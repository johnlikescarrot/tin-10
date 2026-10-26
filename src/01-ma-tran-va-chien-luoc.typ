// =============================================================================
// src/01-ma-tran-va-chien-luoc.typ
// Phần I: Phân tích chi tiết Ma trận & Bản đặc tả gốc + Chiến lược làm bài
// =============================================================================

#import "template.typ": *

#part-banner(
  "Phần I",
  "PHÂN TÍCH MA TRẬN, BẢN ĐẶC TẢ & CHIẾN LƯỢC ÔN THI GIỮA KÌ I",
  "Tổng hợp nguyên bản và giải mã chi tiết tài liệu gốc \"MA TRAN GIUA KI I - LOP 10.docx\" (Định hướng ICT – Kết nối tri thức)",
  accent: c-navy,
)

=== 1. Tổng quan cấu trúc đề kiểm tra từ tài liệu gốc

Qua phân tích toàn văn tệp nguồn `MA TRAN GIUA KI I - LOP 10.docx`, tài liệu gốc cung cấp *Ma trận đề kiểm tra giữa kì I* (Bảng 1) và *Bản đặc tả đề kiểm tra giữa kì I* (Bảng 2) cho môn *Tin học 10 – Định hướng Tin học ứng dụng (ICT)* theo Chương trình GDPT 2018 (bộ sách *Kết nối tri thức với cuộc sống*), gồm *03 Chủ đề (A, B, D)*, *06 Đơn vị kiến thức* và *35 Yêu cầu cần đạt cụ thể*. Tài liệu gốc không đính kèm câu hỏi rời rạc mà quy định khung đặc tả chuẩn để ra đề; do đó đề cương này giải đáp trực tiếp *100% (35/35) yêu cầu cần đạt* trong bản đặc tả gốc, đồng thời biên soạn đầy đủ hệ thống câu hỏi luyện tập và 02 đề thi thử bám sát từng ô ma trận.

#grid(
  columns: (1fr, 1fr, 1fr),
  column-gutter: 8pt,
  block(
    width: 100%, fill: c-blue-bg, stroke: 0.6pt + c-blue-bdr, radius: 5pt, inset: 9pt,
    [
      #text(size: 8pt, weight: "bold", fill: c-blue)[PHẦN I • TRẮC NGHIỆM 4 LỰA CHỌN]
      #v(2pt)
      #text(size: 13pt, weight: "extrabold", fill: c-navy)[20 câu • 5,0 điểm]
      #v(2pt)
      #text(size: 8.5pt, fill: c-ink)[• Mỗi câu đúng: *0,25 điểm*\ • Gồm: *16 câu Nhận biết* (4,0đ) + *4 câu Thông hiểu* (1,0đ)]
    ]
  ),
  block(
    width: 100%, fill: c-teal-bg, stroke: 0.6pt + c-teal-bdr, radius: 5pt, inset: 9pt,
    [
      #text(size: 8pt, weight: "bold", fill: c-teal)[PHẦN II • TRẮC NGHIỆM ĐÚNG/SAI]
      #v(2pt)
      #text(size: 13pt, weight: "extrabold", fill: c-navy)[02 câu • 2,0 điểm]
      #v(2pt)
      #text(size: 8.5pt, fill: c-ink)[• Mỗi câu 4 ý a, b, c, d (*1,0 điểm*)\ • Mỗi câu gồm: *2 ý Thông hiểu* + *2 ý Vận dụng* (rơi vào A.2 & B.1)]
    ]
  ),
  block(
    width: 100%, fill: c-purple-bg, stroke: 0.6pt + c-purple-bdr, radius: 5pt, inset: 9pt,
    [
      #text(size: 8pt, weight: "bold", fill: c-purple)[PHẦN III • TỰ LUẬN]
      #v(2pt)
      #text(size: 13pt, weight: "extrabold", fill: c-navy)[03 câu • 3,0 điểm]
      #v(2pt)
      #text(size: 8.5pt, fill: c-ink)[• *1 câu Thông hiểu* (1,0đ)\ • *1 câu Vận dụng* (1,0đ)\ • *1 câu Vận dụng cao* (1,0đ)]
    ]
  )
)

#v(4pt)

- *Thời gian làm bài:* *45 phút* (không kể thời gian phát đề).
- *Tỉ lệ hình thức:* *70% Trắc nghiệm* (7,0 điểm) – *30% Tự luận* (3,0 điểm).
- *Tỉ lệ mức độ nhận thức toàn đề:* *40% Nhận biết* (4,0đ) – *30% Thông hiểu* (3,0đ) – *20% Vận dụng* (2,0đ) – *10% Vận dụng cao* (1,0đ).

=== 2. Bảng Ma trận Đề kiểm tra Giữa kì I (Nguyên bản chuẩn hoá từ file .docx)

#block(breakable: false)[
  #set text(size: 7.8pt)
  #table(
    columns: (19pt, 1.12fr, 1.38fr, 20pt, 20pt, 17pt, 20pt, 23pt, 17pt, 20pt, 23pt, 17pt, 20pt, 20pt, 17pt, 45pt),
    inset: (x: 3pt, y: 3.3pt),
    stroke: 0.45pt + c-border,
    align: (x, y) => if y < 3 or x == 0 or x >= 3 { center + horizon } else { left + horizon },
    fill: (x, y) => if y == 0 { c-navy } else if y == 1 { rgb("#1e3a5f") } else if y == 2 { rgb("#e2e8f0") } else if y >= 9 { rgb("#f1f5f9") } else { white },
    table.header(
      table.cell(rowspan: 3)[#text(fill: white, weight: "bold")[TT]],
      table.cell(rowspan: 3)[#text(fill: white, weight: "bold")[Nội dung kiến thức / kĩ năng]],
      table.cell(rowspan: 3)[#text(fill: white, weight: "bold")[Đơn vị kiến thức / kĩ năng]],
      table.cell(colspan: 12)[#text(fill: white, weight: "bold")[Mức độ nhận thức]],
      table.cell(rowspan: 3)[#text(fill: white, weight: "bold")[Tổng %\ điểm]],
      table.cell(colspan: 3)[#text(fill: white, weight: "bold")[Nhận biết]],
      table.cell(colspan: 3)[#text(fill: white, weight: "bold")[Thông hiểu]],
      table.cell(colspan: 3)[#text(fill: white, weight: "bold")[Vận dụng]],
      table.cell(colspan: 3)[#text(fill: white, weight: "bold")[VD cao]],
      [*TN*], [*ĐS*], [*TL*], [*TN*], [*ĐS*], [*TL*], [*TN*], [*ĐS*], [*TL*], [*TN*], [*ĐS*], [*TL*],
    ),
    table.cell(rowspan: 3)[*1*],
    table.cell(rowspan: 3)[*Chủ đề A.*\ Máy tính và xã hội tri thức],
    [1. Dữ liệu, thông tin và xử lí thông tin],
    [2], [], [], [2], [], [], [], [], [1], [], [], [], [*20%*\ (2,0đ)],
    [2. Vai trò của máy tính và các thiết bị thông minh trong nền kinh tế tri thức],
    [4], [], [], [], [2 ý], [], [], [2 ý], [], [], [], [], [*20%*\ (2,0đ)],
    [3. Kĩ năng sử dụng thiết bị số của mỗi công dân],
    [], [], [], [], [], [], [], [], [], [], [], [], [—],

    table.cell(rowspan: 2)[*2*],
    table.cell(rowspan: 2)[*Chủ đề B.*\ Mạng máy tính và Internet],
    [1. Khái niệm mạng máy tính, Internet, IoT. Phân loại mạng máy tính],
    [4], [], [], [], [2 ý], [], [], [2 ý], [], [], [], [], [*20%*\ (2,0đ)],
    [2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng #super[\*]],
    [4], [], [], [], [], [1], [], [], [], [], [], [], [*20%*\ (2,0đ)],

    [*3*],
    [*Chủ đề D.*\ Đạo đức, pháp luật và văn hoá trong môi trường số],
    [1. Nghĩa vụ tuân thủ pháp lí trong môi trường số #super[\*]],
    [2], [], [], [2], [], [], [], [], [], [], [], [1], [*20%*\ (2,0đ)],

    table.cell(colspan: 3)[*Tổng số câu / số ý*],
    [*16*], [], [], [*4*], [*4 ý*], [*1*], [], [*4 ý*], [*1*], [], [], [*1*], [*25 câu*],
    table.cell(colspan: 3)[*Tỉ lệ % từng mức độ nhận thức*],
    table.cell(colspan: 3)[*40%*],
    table.cell(colspan: 3)[*30%*],
    table.cell(colspan: 3)[*20%*],
    table.cell(colspan: 3)[*10%*],
    [*100%*],
    table.cell(colspan: 3)[*Tỉ lệ chung (Trắc nghiệm / Tự luận)*],
    table.cell(colspan: 6)[*70% Trắc nghiệm (7,0 điểm)*],
    table.cell(colspan: 6)[*30% Tự luận (3,0 điểm)*],
    [*10,0đ*],
  )
]

=== 3. Bảng Đặc tả Đề kiểm tra Giữa kì I (Nguyên bản 35 yêu cầu cần đạt từ file .docx)

#block(breakable: true)[
  #set text(size: 8.1pt)
  #table(
    columns: (0.85fr, 2.55fr, 34pt, 34pt, 34pt, 36pt),
    inset: (x: 5.5pt, y: 4.5pt),
    stroke: 0.45pt + c-border,
    align: (x, y) => if y < 2 or x >= 2 { center + horizon } else { left + horizon },
    fill: (x, y) => if y == 0 { c-navy } else if y == 1 { rgb("#1e3a5f") } else if y >= 8 { rgb("#f1f5f9") } else { white },
    table.header(
      table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Đơn vị kiến thức]],
      table.cell(rowspan: 2)[#text(fill: white, weight: "bold")[Mức độ kiến thức, kĩ năng cần kiểm tra, đánh giá (Nguyên văn .docx)]],
      table.cell(colspan: 4)[#text(fill: white, weight: "bold")[Số câu theo mức độ]],
      [#text(fill: white, weight: "bold")[NB]],
      [#text(fill: white, weight: "bold")[TH]],
      [#text(fill: white, weight: "bold")[VD]],
      [#text(fill: white, weight: "bold")[VDC]],
    ),
    [*A.1.* Dữ liệu, thông tin và xử lí thông tin\ *(Giải đáp: A1.1–A1.5)*],
    [*Nhận biết:* Nêu được sự ưu việt của việc lưu trữ dựa trên các thiết bị số.\ *Thông hiểu:* Phân biệt được thông tin và dữ liệu; Nêu được ví dụ minh hoạ về thông tin và dữ liệu.\ *Vận dụng:* Chuyển đổi được giữa các đơn vị lưu trữ thông tin: B, KB, MB,...; Xử lí và truyền thông tin bằng thiết bị số.],
    [2\ (TN)], [2\ (TN)], [1\ (TL)], [],

    [*A.2.* Vai trò của máy tính và thiết bị thông minh\ *(Giải đáp: A2.1–A2.7)*],
    [*Nhận biết:* Trình bày những đóng góp cơ bản của tin học đối với xã hội; Nhận biết một vài thiết bị số thông dụng khác ngoài PC và laptop; Giới thiệu các thành tựu nổi bật ở một số mốc thời gian minh hoạ sự phát triển của ngành tin học.\ *Thông hiểu:* Nêu ví dụ cụ thể về thiết bị thông minh; Giải thích vai trò của thiết bị thông minh đối với sự phát triển của xã hội và CMCN 4.0; Giải thích các thiết bị đó cũng là những hệ thống xử lí thông tin; Nêu ví dụ minh hoạ đóng góp cơ bản của tin học đối với xã hội.],
    [4\ (TN)], [1\ (ĐS)], [], [],

    [*A.3.* Kĩ năng sử dụng thiết bị số\ *(Giải đáp: A3.1–A3.2)*],
    [*Vận dụng:* Khởi động được một số thiết bị số thông dụng; Sử dụng được các tệp dữ liệu, các chức năng và phần mềm ứng dụng cơ bản cài sẵn trên các thiết bị đó.],
    [], [], [], [],

    [*B.1.* Khái niệm mạng, Internet, IoT. Phân loại mạng\ *(Giải đáp: B1.1–B1.5)*],
    [*Nhận biết:* Nêu một số dịch vụ cụ thể mà Điện toán đám mây cung cấp cho người dùng; Nêu khái niệm Internet vạn vật (IoT).\ *Thông hiểu:* Trình bày những thay đổi về chất lượng cuộc sống, phương thức học tập và làm việc trong xã hội có mạng máy tính phổ biến; So sánh mạng LAN và Internet; Nêu ví dụ cụ thể về thay đổi trong cuộc sống mà IoT đem lại, phát biểu ý kiến cá nhân về lợi ích của IoT.],
    [4\ (TN)], [1\ (ĐS)], [], [],

    [*B.2.* Sử dụng dịch vụ web. Tự bảo vệ trên mạng\ *(Giải đáp: B2.1–B2.8)*],
    [*Nhận biết:* Trình bày sơ lược về phần mềm độc hại; Nêu một vài cách phòng vệ khi bị bắt nạt trên mạng; Nêu những nguy cơ và tác hại nếu tham gia Internet bất cẩn, thiếu hiểu biết.\ *Thông hiểu:* Trình bày một số cách đề phòng những tác hại khi tham gia Internet.\ *Vận dụng:* Sử dụng công cụ thông dụng để ngăn ngừa, loại bỏ phần mềm độc hại; Sử dụng chức năng xử lí thông tin trên PC/thiết bị số (VD dịch tự động văn bản/tiếng nói); Khai thác nguồn học liệu mở trên Internet; Biết cách tự bảo vệ dữ liệu cá nhân.],
    [2\ (TN)], [2\ (TN)], [1\ (TL)], [],

    [*D.1.* Nghĩa vụ tuân thủ pháp lí trong môi trường số\ *(Giải đáp: D1.1–D1.8)*],
    [*Nhận biết:* Nêu một số vấn đề nảy sinh về pháp luật, đạo đức, văn hoá khi giao tiếp qua mạng phổ biến; Trình bày một số nội dung cơ bản của Luật CNTT, Nghị định quản lí/cung cấp/sử dụng sản phẩm & dịch vụ CNTT, Luật An ninh mạng.\ *Thông hiểu:* Nêu ví dụ vi phạm bản quyền thông tin & sản phẩm số, giải thích sự vi phạm diễn ra thế nào và hậu quả; Giải thích nội dung cơ bản của Luật CNTT, Nghị định, Luật An ninh mạng + ví dụ; Giải thích khía cạnh pháp lí của bản quyền, sở hữu, sử dụng, trao đổi thông tin số + ví dụ; Nêu ví dụ tác hại chia sẻ thông tin bất cẩn; Nêu biện pháp đơn giản nâng cao tính an toàn và hợp pháp khi chia sẻ thông tin số.\ *Vận dụng:* Vận dụng Luật và Nghị định để xác định tính hợp pháp của một hành vi cụ thể.],
    [4\ (TN)], [], [], [1\ (TL)],

    table.cell(colspan: 2)[*Tỉ lệ % từng mức độ nhận thức / Tỉ lệ chung*],
    [*40%*], [*30%*], [*20%*], [*10%*],
  )
]

=== 4. Đối chiếu Ma trận với SGK "Kết nối tri thức với cuộc sống" & Lưu ý quan trọng

#block(breakable: true)[
  #set text(size: 8.6pt)
  #table(
    columns: (1.2fr, 1.4fr, 1.3fr, 1.2fr),
    inset: (x: 7pt, y: 5.5pt),
    stroke: 0.5pt + c-border,
    fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { white } else { c-light },
    table.header(
      [#text(fill: white, weight: "bold")[Đơn vị kiến thức trong Ma trận]],
      [#text(fill: white, weight: "bold")[Bài học tương ứng (SGK KNTT 10)]],
      [#text(fill: white, weight: "bold")[Cơ cấu câu hỏi cần ôn]],
      [#text(fill: white, weight: "bold")[Trọng tâm ra đề chắc chắn]],
    ),
    [*A.1.* Dữ liệu, thông tin và xử lí thông tin *(2,0đ)*],
    [*Bài 1.* Thông tin và xử lí thông tin *(kết hợp đơn vị lưu trữ ở Bài 1, 4, 6)*],
    [2 TN (NB) + 2 TN (TH) + *1 Tự luận (VD)*],
    [Ưu việt lưu trữ số; phân biệt Thông tin – Dữ liệu; *bài toán đổi đơn vị B, KB, MB, GB, TB & tốc độ truyền*.],
    [*A.2.* Vai trò máy tính & thiết bị thông minh *(2,0đ)*],
    [*Bài 2.* Vai trò của thiết bị thông minh và tin học đối với xã hội],
    [4 TN (NB) + *1 câu Đúng/Sai* (2 ý TH + 2 ý VD)],
    [4 đóng góp của tin học; các mốc lịch sử tin học; CMCN 4.0; giải thích thiết bị thông minh là hệ thống xử lí thông tin.],
    [*A.3.* Kĩ năng sử dụng thiết bị số *(0đ trên giấy)*],
    [*Bài 7.* Thực hành sử dụng thiết bị số thông dụng],
    [Tích hợp thực hành / lồng ghép hiểu biết thực tế],
    [Quản lí tệp/thư mục, phần mềm cài sẵn, kết nối và truyền dữ liệu giữa các thiết bị số.],
    [*B.1.* Mạng máy tính, Internet, Cloud, IoT *(2,0đ)*],
    [*Bài 8.* Mạng máy tính trong cuộc sống hiện đại],
    [4 TN (NB) + *1 câu Đúng/Sai* (2 ý TH + 2 ý VD)],
    [So sánh *LAN và Internet*; dịch vụ *Điện toán đám mây* (SaaS/PaaS/IaaS, Google Drive...); khái niệm & lợi ích *IoT*.],
    [*B.2.* Sử dụng dịch vụ web. Tự bảo vệ trên mạng *(2,0đ)*],
    [*Bài 9.* An toàn trên không gian mạng\ *Bài 10.* Thực hành khai thác tài nguyên trên Internet],
    [4 TN (NB/TH) + *1 Tự luận (TH/VD)*],
    [Virus, Worm, Trojan, Spyware, Ransomware; cách xử lí khi bị *bắt nạt qua mạng*; bảo vệ dữ liệu; Google Dịch & Học liệu mở.],
    [*D.1.* Nghĩa vụ tuân thủ pháp lí trong môi trường số *(2,0đ)*],
    [*Bài 11.* Ứng xử trên môi trường số. Nghĩa vụ tôn trọng bản quyền],
    [4 TN (NB/TH) + *1 Tự luận (VDC)*],
    [Luật CNTT 2006 (Đ.12), Luật An ninh mạng 2018, Luật SHTT (bản quyền), NĐ 72/2013 & NĐ 15/2020; *phân tích hành vi vi phạm*.],
  )
]

#pitfall-box(
  "Điểm chênh nhỏ giữa Bảng 1 (Ma trận) và Bảng 2 (Đặc tả) trong file .docx gốc",
  [
    Khi đối chiếu kĩ hai bảng trong tệp `MA TRAN GIUA KI I - LOP 10.docx`, có một sự hoán đổi vị trí nhẹ nhưng *tổng số câu toàn đề không đổi* (vẫn đúng 16 TN NB + 4 TN TH + 2 ĐS + 3 TL):
    - *Ở Đơn vị B.2 (An toàn mạng & Dịch vụ web):* Bảng Ma trận ghi `4 TN (NB) + 1 TL (TH)`, còn Bảng Đặc tả ghi `2 TN (NB) + 2 TN (TH) + 1 TL (VD)`.
    - *Ở Đơn vị D.1 (Pháp luật môi trường số):* Bảng Ma trận ghi `2 TN (NB) + 2 TN (TH) + 1 TL (VDC)`, còn Bảng Đặc tả ghi `4 TN (NB) + 1 TL (VDC)`.
    *Giải pháp an toàn 100%:* Đề cương này cung cấp trọn bộ câu hỏi bao phủ cả hai phương án (Đề thử số 01 theo sát Bảng Ma trận; Đề thử số 02 theo sát Bảng Đặc tả) để học sinh hoàn toàn chủ động trước mọi cách ra đề của giáo viên!
  ]
)

=== 5. Chiến lược phân bổ 45 phút & Quy tắc tính điểm Đúng/Sai mới

#block(breakable: false)[
  #grid(
    columns: (1.12fr, 0.88fr),
    column-gutter: 10pt,
    concept-box(
      "Lộ trình 45 phút làm bài tối ưu (Mục tiêu 9,5 – 10 điểm)",
      [
        1. *Phút 01 – 12 (12 phút):* Giải quyết trọn vẹn *20 câu TN 4 lựa chọn* (5,0đ). Đọc kĩ từ khóa phủ định (*"KHÔNG phải"*, *"NGOẠI TRỪ"*, *"SAI"*), khoanh chắc 16 câu Nhận biết trước, suy luận loại trừ 4 câu Thông hiểu.
        2. *Phút 13 – 20 (08 phút):* Tập trung cao độ cho *02 câu Đúng/Sai* (2,0đ) thuộc bài Thiết bị thông minh (A.2) và Mạng/Cloud/IoT (B.1). Đọc từng ý `a, b, c, d` độc lập.
        3. *Phút 21 – 40 (20 phút):* Trình bày mạch lạc *03 câu Tự luận* (3,0đ):
           - *Câu TL 1 (1,0đ – Đổi đơn vị lưu trữ / truyền tin):* Ghi rõ công thức quy đổi ($1" KB" = 1024" B"$...), lời giải từng bước và đáp số kèm đơn vị.
           - *Câu TL 2 (1,0đ – An toàn mạng / Học liệu mở):* Trình bày thành các gạch đầu dòng rõ ý (nhận diện mối nguy $->$ cách xử lí/phòng tránh cụ thể).
           - *Câu TL 3 (1,0đ – Tình huống pháp lí VDC):* Áp dụng khung 4 bước: *(1) Kết luận hợp pháp hay vi phạm $->$ (2) Chỉ rõ hành vi & căn cứ luật $->$ (3) Phân tích hậu quả $->$ (4) Đề xuất cách ứng xử đúng*.
        4. *Phút 41 – 45 (05 phút):* Rà soát lại phiếu tô trắc nghiệm, kiểm tra đơn vị `bit (b)` và `Byte (B)` ở bài tính toán.
      ],
      accent: c-navy,
      bg: c-light,
      bdr: c-border,
      breakable-box: false,
    ),
    concept-box(
      "Quy tắc chấm điểm câu Đúng/Sai (GDPT 2018)",
      [
        Mỗi câu Trắc nghiệm Đúng/Sai có *4 mệnh đề (a, b, c, d)*, tối đa *1,0 điểm/câu*:
        #v(3pt)
        #table(
          columns: (1fr, 1fr),
          inset: 4.5pt,
          stroke: 0.45pt + c-teal-bdr,
          align: center,
          fill: (x, y) => if y == 0 { rgb("#ccfbf1") } else { white },
          [*Số ý trả lời đúng*], [*Điểm đạt được*],
          [Đúng *1 ý*], [*0,10 điểm*],
          [Đúng *2 ý*], [*0,25 điểm*],
          [Đúng *3 ý*], [*0,50 điểm*],
          [Đúng cả *4 ý*], [*1,00 điểm*],
        )
        #v(3pt)
        *Cảnh báo:* Sai chỉ *1 ý* trong 4 ý sẽ mất ngay *0,50 điểm* (tương đương mất 2 câu trắc nghiệm 4 lựa chọn!). Vì vậy tuyệt đối không đọc lướt ở 2 ý vận dụng `c)` và `d)`.
      ],
      accent: c-teal,
      bg: c-teal-bg,
      bdr: c-teal-bdr,
      breakable-box: false,
    )
  )
]

=== 6. Bảng tổng rà soát thần tốc 10 trọng tâm cốt lõi "5 phút trước phòng thi"

#block(breakable: false)[
  #set text(size: 8.3pt)
  #table(
    columns: (22pt, 1.15fr, 2.65fr),
    inset: (x: 6pt, y: 4.5pt),
    stroke: 0.45pt + c-border,
    align: (center + horizon, left + horizon, left + horizon),
    fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { white } else { c-light },
    table.header(
      [#text(fill: white, weight: "bold")[\#]],
      [#text(fill: white, weight: "bold")[Chủ điểm câu hỏi]],
      [#text(fill: white, weight: "bold")[Từ khóa chốt điểm tuyệt đối không được nhầm]],
    ),
    [*1*], [*Dữ liệu vs Thông tin*], [*Dữ liệu* = con số, chữ, ảnh, âm thanh, dãy bit lưu trên vật mang tin; *Thông tin* = ý nghĩa/hiểu biết rút ra.],
    [*2*], [*Đổi đơn vị lưu trữ*], [*$1 "Byte (B)" = 8 "bit (b)"$*; các bậc tiếp theo nhân/chia *$1024$*: `B` $arrow.l.r$ `KB` $arrow.l.r$ `MB` $arrow.l.r$ `GB` $arrow.l.r$ `TB` $arrow.l.r$ `PB`.],
    [*3*], [*Thiết bị thông minh*], [Có *xử lí tự chủ + tương tác thông minh + kết nối mạng*; bản chất là 1 *hệ thống xử lí thông tin* (Vào–Xử lí–Lưu–Ra).],
    [*4*], [*Mốc lịch sử & CMCN 4.0*], [1945 *Von Neumann*; 1946 *ENIAC*; 1969 *ARPANET*; 1989–1991 *WWW (Tim Berners-Lee)*; 1997 *Deep Blue*; 2016 *AlphaGo*; *CMCN 4.0* = IoT + AI + Big Data + Cloud.],
    [*5*], [*LAN vs Internet*], [*LAN*: phạm vi hẹp (phòng/trường), *có chủ sở hữu riêng*. *Internet*: phạm vi toàn cầu, *không thuộc sở hữu của ai*.],
    [*6*], [*Đám mây & IoT*], [*SaaS* = phần mềm cho người dùng cuối (`Google Docs/Drive`); *IoT* = vật dụng gắn cảm biến nối mạng *tự động trao đổi dữ liệu* (ETC, Smart Home).],
    [*7*], [*Bộ tứ Malware*], [*Virus* = gắn tệp vật chủ; *Worm* = độc lập tự nhân bản qua mạng; *Trojan* = ngụy trang phần mềm lành / *crack*; *Ransomware* = mã hóa tống tiền.],
    [*8*], [*Chống bắt nạt mạng*], [Quy tắc 4 bước *KHÔNG – LƯU – CHẶN – BÁO*: Không đôi co $->$ Chụp màn hình lưu bằng chứng $->$ Block/Report $->$ Báo cha mẹ, thầy cô, Công an.],
    [*9*], [*Văn bản pháp luật số*], [*Điều 12 Luật CNTT 2006*; *Luật An ninh mạng 2018*; *Nghị định 72/2013 & Điều 101 NĐ 15/2020*; *Luật Sở hữu trí tuệ* (Quyền tác giả); *QĐ 874* ứng xử MXH.],
    [*10*], [*Bản quyền sản phẩm số*], [Mua bản sao chỉ có *quyền sử dụng cá nhân*, cấm tự ý nhân bản/phát tán/dùng *crack*; chỉ trích dẫn ngắn phi thương mại *có ghi rõ nguồn & tác giả* mới hợp pháp.],
  )
]
