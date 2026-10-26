#import "template.typ": *

= Phần I. Cấu trúc đề, Ma trận & Đặc tả kiểm tra Giữa kì I

== 1.1. Quy định chung về đề kiểm tra Giữa kì I (Theo tài liệu gốc)

#callout(title: "Thông số cấu trúc đề kiểm tra Giữa kì I – Môn Tin học 10 (Định hướng ICT)", accent: c-navy, bg: c-navy-light)[
  - *Môn kiểm tra:* Tin học 10 – Định hướng Tin học ứng dụng (ICT) – Bộ sách _Kết nối tri thức với cuộc sống_.
  - *Thời gian làm bài:* *45 phút* (không kể thời gian phát đề).
  - *Hình thức kiểm tra:* Kết hợp giữa *trắc nghiệm* và *tự luận* (tỉ lệ *70% trắc nghiệm*, *30% tự luận*).
  - *Phân bổ mức độ nhận thức toàn đề:*
    - *70% Trắc nghiệm (7,0 điểm):* 40% Nhận biết (4,0 điểm) + 20% Thông hiểu (2,0 điểm) + 10% Vận dụng (1,0 điểm).
    - *30% Tự luận (3,0 điểm):* 10% Thông hiểu (1,0 điểm) + 10% Vận dụng (1,0 điểm) + 10% Vận dụng cao (1,0 điểm).
    - *Tổng tỉ lệ theo 4 mức độ:* *40% Nhận biết – 30% Thông hiểu – 20% Vận dụng – 10% Vận dụng cao*.
  - *Cấu trúc chi tiết các phần trong đề thi:*
    + *Phần trắc nghiệm (7,0 điểm):*
      - *Trắc nghiệm nhiều lựa chọn (TN):* *20 câu* hỏi trắc nghiệm 4 lựa chọn (A, B, C, D), mỗi câu đúng được *0,25 điểm* $arrow.r$ tổng *5,0 điểm*.
      - *Trắc nghiệm Đúng/Sai (ĐS):* *02 câu*, mỗi câu gồm 4 ý (a, b, c, d) chọn Đúng hoặc Sai, mỗi câu tối đa *1,0 điểm* $arrow.r$ tổng *2,0 điểm*. _(Quy ước chấm chuẩn: đúng 1 ý được 0,1đ; đúng 2 ý được 0,25đ; đúng 3 ý được 0,5đ; đúng cả 4 ý được 1,0đ)._
    + *Phần tự luận (3,0 điểm):* Gồm *03 câu* (*01 câu Thông hiểu*: 1,0 điểm; *01 câu Vận dụng*: 1,0 điểm; *01 câu Vận dụng cao*: 1,0 điểm).
]

== 1.2. Bảng Ma trận đề kiểm tra Giữa kì I (Nguyên bản từ `MA TRAN GIUA KI I - LOP 10.docx`)

#block(width: 100%)[
  #set text(size: 7.9pt)
  #set par(justify: false, leading: 0.5em)
  #table(
    columns: (18pt, 1.15fr, 1.45fr, 19pt, 19pt, 17pt, 19pt, 22pt, 17pt, 19pt, 22pt, 17pt, 19pt, 19pt, 17pt, 46pt),
    inset: (x: 3pt, y: 4.5pt),
    align: (col, row) => if row <= 2 or col == 0 or col >= 3 { center + horizon } else { left + horizon },
    stroke: 0.5pt + c-border,
    fill: (_, row) => if row <= 2 { c-navy-light } else if row >= 9 { c-bg-soft } else { white },

    table.cell(rowspan: 3)[*TT*],
    table.cell(rowspan: 3)[*Nội dung kiến thức / kĩ năng*],
    table.cell(rowspan: 3)[*Đơn vị kiến thức / kĩ năng*],
    table.cell(colspan: 12)[*Mức độ nhận thức*],
    table.cell(rowspan: 3)[*Tổng % điểm*],

    table.cell(colspan: 3)[*Nhận biết*],
    table.cell(colspan: 3)[*Thông hiểu*],
    table.cell(colspan: 3)[*Vận dụng*],
    table.cell(colspan: 3)[*Vận dụng cao*],

    [_*TN*_], [_*ĐS*_], [_*TL*_],
    [_*TN*_], [_*ĐS*_], [_*TL*_],
    [_*TN*_], [_*ĐS*_], [_*TL*_],
    [_*TN*_], [_*ĐS*_], [_*TL*_],

    table.cell(rowspan: 3)[*1*],
    table.cell(rowspan: 3)[*Chủ đề A.* Máy tính và xã hội tri thức],
    [1. Dữ liệu, thông tin và xử lý thông tin.],
    [2], [], [], [2], [], [], [], [], [1], [], [], [], [20% \ (2 điểm)],

    [2. Vai trò của máy tính và các thiết bị thông minh trong nền kinh tế tri thức],
    [4], [], [], [], [2 ý], [], [], [2 ý], [], [], [], [], [20% \ (2 điểm)],

    [3. Kĩ năng sử dụng thiết bị số của mỗi công dân.],
    [], [], [], [], [], [], [], [], [], [], [], [], [],

    table.cell(rowspan: 2)[*2*],
    table.cell(rowspan: 2)[*Chủ đề B.* Mạng máy tính và Internet],
    [1. Khái niệm mạng máy tính, Internet, IoT. Phân loại mạng máy tính],
    [4], [], [], [], [2 ý], [], [], [2 ý], [], [], [], [], [20% \ (2 điểm)],

    [2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng],
    [4], [], [], [], [], [1], [], [], [], [], [], [], [20% \ (2 điểm)],

    [*3*],
    [*Chủ đề D.* Đạo đức, pháp luật và văn hoá trong môi trường số],
    [1. Nghĩa vụ tuân thủ pháp lí trong môi trường số],
    [2], [], [], [2], [], [], [], [], [], [], [], [1], [20% \ (2 điểm)],

    table.cell(colspan: 3)[*Tổng*],
    [_*16*_], [], [], [_*4*_], [_*4 ý*_], [_*1*_], [], [_*4 ý*_], [_*1*_], [], [], [_*1*_], [],

    table.cell(colspan: 3)[*Tỉ lệ % từng mức độ nhận thức*],
    table.cell(colspan: 3)[*40%*],
    table.cell(colspan: 3)[*30%*],
    table.cell(colspan: 3)[*20%*],
    table.cell(colspan: 3)[*10%*],
    [*10đ*],

    table.cell(colspan: 3)[*Tỉ lệ chung*],
    table.cell(colspan: 6)[*70% (Trắc nghiệm)*],
    table.cell(colspan: 6)[*30% (Tự luận)*],
    [*100%*],
  )
]

== 1.3. Bảng Đặc tả đề kiểm tra Giữa kì I (Nguyên bản từ `MA TRAN GIUA KI I - LOP 10.docx`)

#block(width: 100%)[
  #set text(size: 8.2pt)
  #set par(justify: false, leading: 0.54em)
  #table(
    columns: (18pt, 0.95fr, 1.05fr, 2.55fr, 34pt, 34pt, 34pt, 36pt),
    inset: (x: 4.5pt, y: 5pt),
    align: (col, row) => if row <= 1 or col == 0 or col >= 4 { center + horizon } else { left + top },
    stroke: 0.5pt + c-border,
    fill: (_, row) => if row <= 1 { c-navy-light } else if row >= 8 { c-bg-soft } else { white },

    table.header(
      table.cell(rowspan: 2)[*TT*],
      table.cell(rowspan: 2)[*Nội dung kiến thức / kĩ năng*],
      table.cell(rowspan: 2)[*Đơn vị kiến thức / kĩ năng*],
      table.cell(rowspan: 2)[*Mức độ kiến thức, kĩ năng cần kiểm tra, đánh giá*],
      table.cell(colspan: 4)[*Số câu hỏi theo mức độ nhận thức*],
      [*Nhận biết*], [*Thông hiểu*], [*Vận dụng*], [*Vận dụng cao*],
    ),

    table.cell(rowspan: 3)[1],
    table.cell(rowspan: 3)[*Chủ đề A.* Máy tính và xã hội tri thức],
    [1. Dữ liệu, thông tin và xử lý thông tin],
    [
      *Nhận biết:*
      – Nêu được sự ưu việt của việc lưu trữ dựa trên các thiết bị số. \
      *Thông hiểu:*
      – Phân biệt được thông tin và dữ liệu. \
      – Nêu được ví dụ minh hoạ về thông tin và dữ liệu. \
      *Vận dụng:*
      – Chuyển đổi được giữa các đơn vị lưu trữ thông tin: B, KB, MB,... \
      – Xử lí và truyền thông tin bằng thiết bị số.
    ],
    [2 (TN)], [2 (TN)], [1 (TL)], [],

    [2. Vai trò của máy tính và các thiết bị thông minh trong nền kinh tế tri thức],
    [
      *Nhận biết:*
      – Trình bày được những đóng góp cơ bản của tin học đối với xã hội. \
      – Nhận biết được một vài thiết bị số thông dụng khác ngoài máy tính để bàn và laptop. \
      – Giới thiệu được các thành tựu nổi bật ở một số mốc thời gian để minh hoạ sự phát triển của ngành tin học. \
      *Thông hiểu:*
      – Nêu được ví dụ cụ thể về thiết bị thông minh. \
      – Giải thích được vai trò của những thiết bị thông minh đối với sự phát triển của xã hội và cuộc cách mạng công nghiệp 4.0. \
      – Giải thích được các thiết bị đó cũng là những hệ thống xử lí thông tin. \
      – Nêu được ví dụ minh họa về những đóng góp cơ bản của tin học đối với xã hội.
    ],
    [4 (TN)], [1 (ĐS)], [], [],

    [3. Kĩ năng sử dụng thiết bị số của mỗi công dân.],
    [
      *Vận dụng:*
      – Khởi động được một số thiết bị số thông dụng. \
      – Sử dụng được các tệp dữ liệu, các chức năng và phần mềm ứng dụng cơ bản cài sẵn trên các thiết bị đó.
    ],
    [], [], [], [],

    table.cell(rowspan: 2)[2],
    table.cell(rowspan: 2)[*Chủ đề B.* Mạng máy tính và Internet],
    [1. Khái niệm mạng máy tính, Internet, IoT. Phân loại mạng máy tính.],
    [
      *Nhận biết:*
      – Nêu được một số dịch vụ cụ thể mà Điện toán đám mây cung cấp cho người dùng. \
      – Nêu được khái niệm Internet vạn vật (IoT). \
      *Thông hiểu:*
      – Trình bày được những thay đổi về chất lượng cuộc sống, phương thức học tập và làm việc trong xã hội mà ở đó mạng máy tính được sử dụng phổ biến. \
      – So sánh được mạng LAN và Internet. \
      – Nêu được ví dụ cụ thể về thay đổi trong cuộc sống mà IoT đem lại. Phát biểu ý kiến cá nhân về lợi ích của IoT.
    ],
    [4 (TN)], [1 (ĐS)], [], [],

    [2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng],
    [
      *Nhận biết:*
      – Trình bày được sơ lược về phần mềm độc hại. \
      – Nêu được một vài cách phòng vệ khi bị bắt nạt trên mạng. \
      – Nêu được những nguy cơ và tác hại nếu tham gia các hoạt động trên Internet một cách bất cẩn và thiếu hiểu biết. \
      *Thông hiểu:*
      – Trình bày được một số cách đề phòng những tác hại khi tham gia các hoạt động trên Internet. \
      *Vận dụng:*
      – Sử dụng được một số công cụ thông dụng để ngăn ngừa và loại bỏ phần mềm độc hại. \
      – Sử dụng được một số chức năng xử lí thông tin trên máy PC và thiết bị số, ví dụ dịch tự động văn bản hay tiếng nói. \
      – Khai thác được một số nguồn học liệu mở trên Internet. \
      – Biết cách tự bảo vệ dữ liệu của cá nhân.
    ],
    [2 (TN)], [2 (TN)], [1 (TL)], [],

    [3],
    [*Chủ đề D.* Đạo đức, pháp luật và văn hoá trong môi trường số],
    [Nghĩa vụ tuân thủ pháp lí trong môi trường số],
    [
      *Nhận biết:*
      – Nêu được một số vấn đề nảy sinh về pháp luật, đạo đức, văn hoá khi việc giao tiếp qua mạng trở nên phổ biến. \
      – Trình bày được một số nội dung cơ bản của Luật Công nghệ thông tin, Nghị định về quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin, Luật An ninh mạng. \
      *Thông hiểu:*
      – Nêu được ví dụ minh họa sự vi phạm bản quyền thông tin và sản phẩm số. Giải thích được sự vi phạm đã diễn ra như thế nào và có thể dẫn tới hậu quả gì. \
      – Giải thích được một số nội dung cơ bản của Luật Công nghệ thông tin, Nghị định về quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin, Luật An ninh mạng. Nêu được ví dụ minh họa. \
      – Giải thích được một số khía cạnh pháp lí của vấn đề bản quyền, của việc sở hữu, sử dụng và trao đổi thông tin trong môi trường số. Nêu được ví dụ minh hoạ. \
      – Nêu được ví dụ về những tác hại của việc chia sẻ và phổ biến thông tin một cách bất cẩn. \
      – Nêu được một vài biện pháp đơn giản và thông dụng để nâng cao tính an toàn và hợp pháp của việc chia sẻ thông tin trong môi trường số. \
      *Vận dụng:*
      – Vận dụng được Luật và Nghị định nêu trên để xác định được tính hợp pháp của một hành vi nào đó trong lĩnh vực quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin.
    ],
    [4 (TN)], [], [], [1 (TL)],

    table.cell(colspan: 4)[*Tỉ lệ %*],
    [40%], [30%], [20%], [10%],

    table.cell(colspan: 4)[*Tỉ lệ chung*],
    table.cell(colspan: 2)[*70%*],
    table.cell(colspan: 2)[*30%*],
  )
]

== 1.4. Ánh xạ Ma trận sang Bài học SGK _Kết nối tri thức_ & Chiến lược ôn tập

#table(
  columns: (1.1fr, 1.35fr, 1.35fr, 1.2fr),
  inset: 6pt,
  align: (left + horizon, left + horizon, left + horizon, left + horizon),
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  [*Đơn vị trong Ma trận*], [*Bài học tương ứng trong SGK Tin 10 – KNTT*], [*Cấu trúc câu hỏi & Điểm số*], [*Trọng tâm chắc chắn ra thi*],
  [*Chủ đề A – Mục 1* \ _(2,0 điểm – 20%)_],
  [*Chủ đề 1 – Bài 1:* Thông tin và xử lí thông tin _(kèm bảng đơn vị dữ liệu)_],
  [• 2 TN Nhận biết (0,5đ) \ • 2 TN Thông hiểu (0,5đ) \ • *1 Tự luận Vận dụng (1,0đ)*],
  [Phân biệt _Thông tin – Dữ liệu – Vật mang tin_; ưu điểm thiết bị số; *bài toán đổi đơn vị B, KB, MB, GB, TB & truyền dữ liệu*.],
  [*Chủ đề A – Mục 2* \ _(2,0 điểm – 20%)_],
  [*Chủ đề 1 – Bài 2:* Vai trò của thiết bị thông minh và tin học đối với xã hội],
  [• 4 TN Nhận biết (1,0đ) \ • *1 câu Đúng/Sai (1,0đ)* _(2 ý Thông hiểu + 2 ý Vận dụng)_],
  [Nhận diện *thiết bị thông minh*; giải thích hệ thống xử lí thông tin; vai trò trong *CMCN 4.0*; các *mốc lịch sử Tin học & AI*.],
  [*Chủ đề A – Mục 3* \ _(Thực hành tích hợp)_],
  [*Chủ đề 1 – Bài 7:* Thực hành sử dụng thiết bị số thông dụng],
  [• Tích hợp kiến thức nền tảng (0 câu viết riêng)],
  [Khởi động/tắt thiết bị đúng cách, quản lí tệp/thư mục, sử dụng phần mềm cài sẵn.],
  [*Chủ đề B – Mục 1* \ _(2,0 điểm – 20%)_],
  [*Chủ đề 2 – Bài 8:* Mạng máy tính trong cuộc sống hiện đại],
  [• 4 TN Nhận biết (1,0đ) \ • *1 câu Đúng/Sai (1,0đ)* _(2 ý Thông hiểu + 2 ý Vận dụng)_],
  [So sánh *LAN và Internet*; dịch vụ *Điện toán đám mây* (SaaS, PaaS, IaaS); khái niệm & ứng dụng thực tế của *IoT*.],
  [*Chủ đề B – Mục 2* \ _(2,0 điểm – 20%)_],
  [*Chủ đề 2 – Bài 9:* An toàn trên không gian mạng & *Bài 10:* Thực hành khai thác tài nguyên trên Internet],
  [• 4 TN (NB/TH) (1,0đ) \ • *1 Tự luận Thông hiểu / Vận dụng (1,0đ)*],
  [Phân biệt *Virus – Worm – Trojan*; phòng vệ khi bị *bắt nạt qua mạng*; bảo vệ dữ liệu cá nhân; *Google Dịch* & *Học liệu mở (OER)*.],
  [*Chủ đề D – Mục 1* \ _(2,0 điểm – 20%)_],
  [*Chủ đề 3 – Bài 11:* Ứng xử trên môi trường số. Nghĩa vụ tôn trọng bản quyền],
  [• 4 TN (2 NB + 2 TH) (1,0đ) \ • *1 Tự luận Vận dụng cao (1,0đ)*],
  [*Luật CNTT, Luật An ninh mạng, Luật SHTT, Nghị định 72/2013/NĐ-CP*; vi phạm *bản quyền số*; *phân tích tính hợp pháp của hành vi thực tế*.],
)

#tip-box(title: "Phân tích kỹ thuật từ tài liệu Ma trận & Đặc tả gốc giúp học sinh không bị bất ngờ")[
  Khi đối chiếu chi tiết *Bảng Ma trận* và *Bảng Đặc tả* trong tệp gốc, em cần lưu ý 2 điểm rất quan trọng để ôn tập bao phủ 100%:
  1. *Về 02 câu Trắc nghiệm Đúng/Sai (2,0 điểm):* Bảng Đặc tả ghi gọn `1 (ĐS)` ở cột Thông hiểu cho mục `A.2` và `B.1`, trong khi Bảng Ma trận tách chi tiết mỗi câu Đúng/Sai gồm *2 ý Thông hiểu + 2 ý Vận dụng*. Do đó, trong mỗi câu Đúng/Sai (4 ý a, b, c, d), 2 ý đầu thường kiểm tra hiểu bản chất khái niệm và 2 ý sau gắn với tình huống thực tế!
  2. *Về sự hoán đổi nhẹ giữa mục `B.2` và `D.1`:* Tổng điểm mỗi mục đều cố định là *2,0 điểm (4 câu TN + 1 câu TL)*. Ở mục `B.2`, câu Tự luận (1,0 điểm) có thể hỏi ở mức *Thông hiểu* (cách phòng tránh tác hại Internet, xử lí khi bị bắt nạt trên mạng) hoặc *Vận dụng* (cách diệt mã độc, bảo vệ dữ liệu cá nhân, khai thác học liệu mở). Đề cương này cung cấp đầy đủ lý thuyết và bài tập mẫu cho *cả hai hướng*!
]
