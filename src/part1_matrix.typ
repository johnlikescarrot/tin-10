#import "theme.typ": *

= PHẦN I. PHÂN TÍCH MA TRẬN & BẢN ĐẶC TẢ ĐỀ KIỂM TRA GIỮA KÌ I

== 1.1. Thông tin chung & Cấu trúc đề thi (Theo tài liệu gốc)

Tài liệu gốc `MA TRAN GIUA KI I - LOP 10.docx` quy định khung kiểm tra đánh giá định kì Giữa Học kì I môn *Tin học 10 — Định hướng Tin học ứng dụng (ICT)* theo Chương trình Giáo dục phổ thông 2018 (bộ sách *Kết nối tri thức với cuộc sống*) với các thông số chuẩn sau:

- *Thời gian làm bài:* *45 phút* _(không kể thời gian phát đề)_.
- *Hình thức kiểm tra:* Kết hợp giữa *Trắc nghiệm (70%)* và *Tự luận (30%)* trên thang điểm *10,0 điểm*.
- *Cấu trúc đề và phân bố điểm chi tiết:*
  - *Mức độ nhận thức toàn đề:* *70% trắc nghiệm* _(40% Nhận biết; 20% Thông hiểu; 10% Vận dụng)_, *30% tự luận* _(10% Thông hiểu; 10% Vận dụng; 10% Vận dụng cao)_. Tổng hợp chung toàn bài thi: *40% Nhận biết (4,0 điểm) — 30% Thông hiểu (3,0 điểm) — 20% Vận dụng (2,0 điểm) — 10% Vận dụng cao (1,0 điểm)*.
  - *Phần trắc nghiệm (7,0 điểm):*
    + *Dạng 1 — Trắc nghiệm nhiều phương án lựa chọn (4 lựa chọn A, B, C, D):* Gồm *20 câu*, mỗi câu đúng đạt *0,25 điểm* $arrow.r$ Tổng *5,0 điểm*.
    + *Dạng 2 — Trắc nghiệm lựa chọn Đúng/Sai:* Gồm *02 câu*, mỗi câu có *4 ý (a, b, c, d)* xoay quanh một ngữ cảnh thực tiễn, tối đa *1,0 điểm/câu* $arrow.r$ Tổng *2,0 điểm*. _(Theo quy định chấm thi chuẩn của Bộ GD&ĐT: trả lời đúng 1 ý trong 1 câu được 0,1 điểm; đúng 2 ý được 0,25 điểm; đúng 3 ý được 0,5 điểm; đúng cả 4 ý được trọn vẹn 1,0 điểm)._
  - *Phần tự luận (3,0 điểm):* Gồm *03 câu hỏi* phân hóa rõ rệt theo 3 cấp độ tư duy:
    + *01 câu mức Thông hiểu:* *1,0 điểm*.
    + *01 câu mức Vận dụng:* *1,0 điểm*.
    + *01 câu mức Vận dụng cao:* *1,0 điểm*.

== 1.2. Bảng Ma trận đề kiểm tra Giữa kì I (Nguyên bản từ tài liệu gốc)

#set text(size: 8.1pt)
#table(
  columns: (18pt, 1.08fr, 1.32fr, 17pt, 21pt, 16pt, 17pt, 22pt, 16pt, 16pt, 22pt, 16pt, 16pt, 17pt, 16pt, 42pt),
  inset: (x: 3pt, y: 4.5pt),
  align: (col, row) => if row < 3 { center + horizon } else if col == 1 or col == 2 { left + horizon } else { center + horizon },
  stroke: 0.5pt + c-border,
  fill: (col, row) => if row < 3 { c-navy.lighten(88%) } else if row >= 9 { c-bg-soft } else { white },

  table.cell(rowspan: 3)[*TT*],
  table.cell(rowspan: 3)[*Nội dung kiến thức/\ kĩ năng*],
  table.cell(rowspan: 3)[*Đơn vị kiến thức/\ kĩ năng*],
  table.cell(colspan: 12)[*Mức độ nhận thức*],
  table.cell(rowspan: 3)[*Tổng %\ điểm*],

  table.cell(colspan: 3)[*Nhận biết*],
  table.cell(colspan: 3)[*Thông hiểu*],
  table.cell(colspan: 3)[*Vận dụng*],
  table.cell(colspan: 3)[*Vận dụng cao*],

  [*_TN_*], [*_ĐS_*], [*_TL_*],
  [*_TN_*], [*_ĐS_*], [*_TL_*],
  [*_TN_*], [*_ĐS_*], [*_TL_*],
  [*_TN_*], [*_ĐS_*], [*_TL_*],

  // Chủ đề A
  table.cell(rowspan: 3)[*1*],
  table.cell(rowspan: 3)[*Chủ đề A. Máy tính và xã hội tri thức*],
  [1. Dữ liệu, thông tin và xử lý thông tin.],
  [2], [], [], [2], [], [], [], [], [1], [], [], [],
  [20%\ (2 điểm)],

  [2. Vai trò của máy tính và các thiết bị thông minh trong nền kinh tế tri thức],
  [4], [], [], [], [2 ý], [], [], [2 ý], [], [], [], [],
  [20%\ (2 điểm)],

  [3. Kĩ năng sử dụng thiết bị số của mỗi công dân.],
  [], [], [], [], [], [], [], [], [], [], [], [],
  [],

  // Chủ đề B
  table.cell(rowspan: 2)[*2*],
  table.cell(rowspan: 2)[*Chủ đề B. Mạng máy tính và Internet*],
  [1. Khái niệm mạng máy tính, Internet, IoT. Phân loại mạng máy tính],
  [4], [], [], [], [2 ý], [], [], [2 ý], [], [], [], [],
  [20%\ (2 điểm)],

  [2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng],
  [4], [], [], [], [], [1], [], [], [], [], [], [],
  [20%\ (2 điểm)],

  // Chủ đề D
  [*3*],
  [*Chủ đề D. Đạo đức, pháp luật và văn hoá trong môi trường số*],
  [1. Nghĩa vụ tuân thủ pháp lí trong môi trường số],
  [2], [], [], [2], [], [], [], [], [], [], [], [1],
  [20%\ (2 điểm)],

  // Tổng
  table.cell(colspan: 3)[*Tổng*],
  [*_16_*], [], [], [*_4_*], [*_4 ý_*], [*_1_*], [], [*_4 ý_*], [*_1_*], [], [], [*_1_*], [],

  table.cell(colspan: 3)[*Tỉ lệ % từng mức độ nhận thức*],
  table.cell(colspan: 3)[*40*],
  table.cell(colspan: 3)[*30*],
  table.cell(colspan: 3)[*20*],
  table.cell(colspan: 3)[*10*],
  [*10*],

  table.cell(colspan: 3)[*Tỉ lệ chung*],
  table.cell(colspan: 6)[*70*],
  table.cell(colspan: 6)[*30*],
  [*100*],
)
#set text(size: 9.7pt)

#v(2pt)
#text(size: 8.4pt, fill: c-muted, style: "italic")[
  *Chú thích kí hiệu trong bảng:* *TN* = Trắc nghiệm 4 lựa chọn (0,25đ/câu); *ĐS* = Trắc nghiệm Đúng/Sai (mỗi câu gồm 4 ý: 2 ý Thông hiểu + 2 ý Vận dụng = 1,0đ/câu); *TL* = Tự luận (1,0đ/câu). Ở dòng cuối "Tỉ lệ chung", 70% là tỉ lệ phần Trắc nghiệm (7,0 điểm) và 30% là tỉ lệ phần Tự luận (3,0 điểm).
]

== 1.3. Bản Đặc tả đề kiểm tra Giữa kì I (Nguyên bản từ tài liệu gốc)

_Lưu ý: Trong tệp gốc `MA TRAN GIUA KI I - LOP 10.docx`, có 02 yêu cầu cần đạt được giáo viên đánh dấu màu nổi bật (một mục tô màu xanh lá và một mục tô màu đỏ). Bảng dưới đây giữ nguyên toàn bộ nội dung gốc và thể hiện rõ các điểm nhấn đó:_

#set text(size: 8.2pt)
#table(
  columns: (18pt, 0.85fr, 0.95fr, 2.65fr, 34pt, 34pt, 34pt, 38pt),
  inset: (x: 4.5pt, y: 5pt),
  align: (col, row) => if row < 2 { center + horizon } else if col >= 4 or col == 0 { center + horizon } else { left + top },
  stroke: 0.5pt + c-border,
  fill: (col, row) => if row < 2 { c-navy.lighten(88%) } else if row >= 8 { c-bg-soft } else { white },

  table.header(
    table.cell(rowspan: 2)[*TT*],
    table.cell(rowspan: 2)[*Nội dung kiến thức/kĩ năng*],
    table.cell(rowspan: 2)[*Đơn vị kiến thức/kĩ năng*],
    table.cell(rowspan: 2)[*Mức độ kiến thức, kĩ năng\ cần kiểm tra, đánh giá*],
    table.cell(colspan: 4)[*Số câu hỏi theo các mức độ nhận thức*],

    [*Nhận biết*], [*Thông hiểu*], [*Vận dụng*], [*Vận dụng cao*],
  ),

  // Chủ đề A
  table.cell(rowspan: 3)[1],
  table.cell(rowspan: 3)[*Chủ đề A. Máy tính và xã hội tri thức*],
  [1. Dữ liệu, thông tin và xử lý thông tin],
  [
    *Nhận biết*\
    – Nêu được sự ưu việt của việc lưu trữ dựa trên các thiết bị số.\
    *Thông hiểu*\
    – Phân biệt được thông tin và dữ liệu,\
    – Nêu được ví dụ minh hoạ về thông tin và dữ liệu.\
    *Vận dụng*\
    – Chuyển đổi được giữa các đơn vị lưu trữ thông tin: B, KB, MB,...\
    – Xử lí và truyền thông tin bằng thiết bị số.
  ],
  [2 (TN)], [2 (TN)], [1 (TL)], [],

  [2. Vai trò của máy tính và các thiết bị thông minh trong nền kinh tế tri thức],
  [
    *Nhận biết*\
    – Trình bày được những đóng góp cơ bản của tin học đối với xã hội.\
    – Nhận biết được một vài thiết bị số thông dụng khác ngoài máy tính để bàn và laptop.\
    – Giới thiệu được các thành tựu nổi bật ở một số mốc thời gian để minh hoạ sự phát triển của ngành tin học.\
    *Thông hiểu*\
    – Nêu được ví dụ cụ thể về thiết bị thông minh.\
    – Giải thích được vai trò của những thiết bị thông minh đối với sự phát triển của xã hội và cuộc cách mạng công nghiệp 4.0.\
    – Giải thích được các thiết bị đó cũng là những hệ thống xử lí thông tin.\
    – Nêu được ví dụ minh họa về những đóng góp cơ bản của tin học đối với xã hội.
  ],
  [4 (TN)], [1 (ĐS)], [], [],

  [3. Kĩ năng sử dụng thiết bị số của mỗi công dân.],
  [
    *Vận dụng*\
    – Khởi động được một số thiết bị số thông dụng\
    – Sử dụng được các tệp dữ liệu, các chức năng và phần mềm ứng dụng cơ bản cài sẵn trên các thiết bị đó.
  ],
  [], [], [], [],

  // Chủ đề B
  table.cell(rowspan: 2)[2],
  table.cell(rowspan: 2)[*Chủ đề B. Mạng máy tính và Internet*],
  [1. Khái niệm mạng máy tính, Internet, IoT. Phân loại mạng máy tính.],
  [
    *Nhận biết*\
    – Nêu được một số dịch vụ cụ thể mà Điện toán đám mây cung cấp cho người dùng.\
    – Nêu được khái niệm Internet vạn vật (IoT).\
    *Thông hiểu*\
    – Trình bày được những thay đổi về chất lượng cuộc sống, phương thức học tập và làm việc trong xã hội mà ở đó mạng máy tính được sử dụng phổ biến.\
    – So sánh được mạng LAN và Internet.\
    – Nêu được ví dụ cụ thể về thay đổi trong cuộc sống mà IoT đem lại. Phát biểu ý kiến cá nhân về lợi ích của IoT.
  ],
  [4 (TN)], [1 (ĐS)], [], [],

  [2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng],
  [
    *Nhận biết*\
    – Trình bày được sơ lược về phần mềm độc hại.\
    – Nêu được một vài cách phòng vệ khi bị bắt nạt trên mạng.\
    #text(fill: c-green, weight: "semibold")[– Nêu được những nguy cơ và tác hại nếu tham gia các hoạt động trên Internet một cách bất cẩn và thiếu hiểu biết. _(Đánh dấu xanh trong bản gốc)_]\
    *Thông hiểu*\
    – Trình bày được một số cách đề phòng những tác hại khi tham gia các hoạt động trên Internet\
    *Vận dụng*\
    – Sử dụng được một số công cụ thông dụng để ngăn ngừa và loại bỏ phần mềm độc hại.\
    – Sử dụng được một số chức năng xử lí thông tin trên máy PC và thiết bị số, ví dụ dịch tự động văn bản hay tiếng nói.\
    – Khai thác được một số nguồn học liệu mở trên Internet\
    – Biết cách tự bảo vệ dữ liệu của cá nhân.
  ],
  [2 (TN)], [2 (TN)], [1 (TL)], [],

  // Chủ đề D
  [3],
  [*Chủ đề D. Đạo đức, pháp luật và văn hoá trong môi trường số*],
  [Nghĩa vụ tuân thủ pháp lí trong môi trường số],
  [
    *Nhận biết*\
    – Nêu được một số vấn đề nảy sinh về pháp luật, đạo đức, văn hoá khi việc giao tiếp qua mạng trở nên phổ biến.\
    – Trình bày được một số nội dung cơ bản của Luật Công nghệ thông tin, Nghị định về quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin, Luật An ninh mạng.\
    *Thông hiểu*\
    #text(fill: c-red, weight: "semibold")[– Nêu được ví dụ minh họa sự vi phạm bản quyền thông tin và sản phẩm số. Giải thích được sự vi phạm đã diễn ra như thế nào và có thể dẫn tới hậu quả gì. _(Đánh dấu đỏ trong bản gốc)_]\
    – Giải thích được một số nội dung cơ bản của Luật Công nghệ thông tin, Nghị định về quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin, Luật An ninh mạng. Nêu được ví dụ minh họa.\
    – Giải thích được một số khía cạnh pháp lí của vấn đề bản quyền, của việc sở hữu, sử dụng và trao đổi thông tin trong môi trường số. Nêu được ví dụ minh hoạ.\
    – Nêu được ví dụ về những tác hại của việc chia sẻ và phổ biến thông tin một cách bất cẩn.\
    – Nêu được một vài biện pháp đơn giản và thông dụng để nâng cao tính an toàn và hợp pháp của việc chia sẻ thông tin trong môi trường số.\
    *Vận dụng*\
    – Vận dụng được Luật và Nghị định nêu trên để xác định được tính hợp pháp của một hành vi nào đó trong lĩnh vực quản lí, cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin.
  ],
  [4 (TN)], [], [], [1 (TL)],

  table.cell(colspan: 4)[*Tỉ lệ %*],
  [40%], [30%], [20%], [10%],

  table.cell(colspan: 4)[*Tỉ lệ chung*],
  table.cell(colspan: 2)[*70%*],
  table.cell(colspan: 2)[*30%*],
)
#set text(size: 9.7pt)

== 1.4. Phân tích chuyên sâu Ma trận — Đối chiếu SGK Kết nối tri thức & Chiến lược làm bài

=== a) Bảng ánh xạ từ Ma trận sang Sách giáo khoa Tin học 10 — Kết nối tri thức với cuộc sống

Trong Chương trình GDPT 2018, các chủ đề được đánh kí hiệu chữ cái (*Chủ đề A, B, D...*), còn trong sách giáo khoa *Tin học 10 — Kết nối tri thức với cuộc sống*, các chủ đề được đánh số thứ tự (*Chủ đề 1, 2, 3...*). Bảng dưới đây giúp học sinh tra cứu chính xác tuyệt đối từng bài học trong SGK tương ứng với Ma trận đề thi:

#set text(size: 8.6pt)
#table(
  columns: (1.05fr, 1.25fr, 1.35fr, 0.95fr),
  inset: (x: 6pt, y: 5.5pt),
  stroke: 0.5pt + c-border,
  fill: (col, row) => if row == 0 { c-teal.lighten(86%) } else if calc.odd(row) { white } else { c-bg-soft },
  align: (left + horizon, left + horizon, left + horizon, center + horizon),

  [*Chủ đề trong Ma trận*], [*Đơn vị kiến thức kiểm tra*], [*Bài học tương ứng trong SGK Kết nối tri thức*], [*Cấu trúc câu & Điểm*],

  [*Chủ đề A*\ Máy tính và xã hội tri thức\ *(4,0 điểm — 40%)*],
  [1. Dữ liệu, thông tin và xử lý thông tin],
  [*Chủ đề 1 — Bài 1:* Thông tin và xử lí thông tin _(liên hệ bổ trợ đơn vị dữ liệu ở Bài 3, 4, 6)_],
  [4 câu TN (1,0đ)\ + 1 câu TL VD (1,0đ)\ = *2,0 điểm*],

  [*Chủ đề A*\ _(tiếp theo)_],
  [2. Vai trò của máy tính và thiết bị thông minh trong nền kinh tế tri thức],
  [*Chủ đề 1 — Bài 2:* Vai trò của thiết bị thông minh và tin học đối với xã hội],
  [4 câu TN (1,0đ)\ + 1 câu Đ/S (1,0đ)\ = *2,0 điểm*],

  [*Chủ đề A*\ _(tiếp theo)_],
  [3. Kĩ năng sử dụng thiết bị số của mỗi công dân _(kiến thức nền thực hành)_],
  [*Chủ đề 1 — Bài 7:* Thực hành sử dụng thiết bị số thông dụng _(bổ trợ: Bài 3, 4, 5, 6)_],
  [Tích hợp thực hành\ _(nắm vững nền tảng)_],

  [*Chủ đề B*\ Mạng máy tính và Internet\ *(4,0 điểm — 40%)*],
  [1. Khái niệm mạng máy tính, Internet, IoT. Phân loại mạng máy tính],
  [*Chủ đề 2 — Bài 8:* Mạng máy tính trong cuộc sống hiện đại],
  [4 câu TN (1,0đ)\ + 1 câu Đ/S (1,0đ)\ = *2,0 điểm*],

  [*Chủ đề B*\ _(tiếp theo)_],
  [2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng],
  [*Chủ đề 2 — Bài 9:* An toàn trên không gian mạng\ *Chủ đề 2 — Bài 10:* Thực hành khai thác tài nguyên trên Internet],
  [4 câu TN (1,0đ)\ + 1 câu TL TH/VD (1,0đ)\ = *2,0 điểm*],

  [*Chủ đề D*\ Đạo đức, pháp luật và văn hoá trong môi trường số\ *(2,0 điểm — 20%)*],
  [1. Nghĩa vụ tuân thủ pháp lí trong môi trường số],
  [*Chủ đề 3 — Bài 11:* Ứng xử trên môi trường số. Nghĩa vụ tôn trọng bản quyền],
  [4 câu TN (1,0đ)\ + 1 câu TL VDC (1,0đ)\ = *2,0 điểm*],
)
#set text(size: 9.7pt)

=== b) Nhận xét quan trọng khi đối chiếu Bảng 1 (Ma trận) và Bảng 2 (Bản đặc tả)

#callout(title: "PHÂN TÍCH KỸ THUẬT GIÚP HỌC SINH KHÔNG BỊ BẤT NGỜ TRONG PHÒNG THI", tone: "memo")[
  Khi đọc kỹ hai bảng trong tài liệu gốc `MA TRAN GIUA KI I - LOP 10.docx`, ta nhận thấy sự thống nhất tuyệt đối về tổng điểm từng đơn vị (mỗi đơn vị chính đều *2,0 điểm*, tổng 5 đơn vị = *10,0 điểm*) nhưng có 3 điểm trình bày cần lưu ý:
  + *Ở câu Trắc nghiệm Đúng/Sai (Chủ đề A.2 và Chủ đề B.1):* Bảng 2 ghi gọn là `1 (ĐS)` ở cột Thông hiểu, trong khi Bảng 1 tách chi tiết thành *2 ý Thông hiểu + 2 ý Vận dụng* (= 4 ý/câu). Như vậy mỗi câu Đúng/Sai luôn gồm 2 mệnh đề kiểm tra hiểu bản chất và 2 mệnh đề gắn với tình huống thực tế.
  + *Ở Chủ đề B.2 và Chủ đề D.1:* Tổng số câu vẫn là *4 câu TN + 1 câu TL* mỗi đơn vị, chỉ hoán đổi nhẹ vị trí cột Nhận biết / Thông hiểu giữa hai bảng (Bảng 1 xếp 4 TN Nhận biết ở B.2 và 2 NB + 2 TH ở D.1; Bảng 2 ghi 2 NB + 2 TH ở B.2 và 4 TN ở D.1; tương tự câu Tự luận B.2 ở mức Thông hiểu/Vận dụng). Do đó, đề cương này ôn luyện *cả hai mức Nhận biết và Thông hiểu/Vận dụng* cho B.2 và D.1 để đảm bảo an toàn 100%.
  + *Hai nội dung được giáo viên tô màu trực tiếp trong Bản đặc tả gốc:*
    - *Màu xanh lá (Chủ đề B.2):* Nguy cơ, tác hại khi tham gia Internet bất cẩn, thiếu hiểu biết và cách phòng tránh $arrow.r$ *Trọng tâm số 1 cho câu Tự luận 1,0 điểm của Chủ đề B*.
    - *Màu đỏ (Chủ đề D.1):* Ví dụ vi phạm bản quyền thông tin & sản phẩm số, giải thích hành vi, hậu quả pháp lí và vận dụng Luật CNTT / Luật An ninh mạng / Nghị định quản lí CNTT $arrow.r$ *Trọng tâm số 1 cho câu Tự luận Vận dụng cao 1,0 điểm của Chủ đề D*.
]

=== c) Chiến thuật phân bổ 45 phút trong phòng thi

- *Phút 01 – 12 (12 phút) — Giải quyết 20 câu Trắc nghiệm 4 lựa chọn (5,0 điểm):* Trung bình 35 giây/câu. Đọc kỹ từ khóa phủ định (*"KHÔNG phải"*, *"ngoại trừ"*, *"SAI"*), khoanh ngay các câu Nhận biết chắc chắn, đánh dấu câu phân vân để quay lại sau.
- *Phút 13 – 20 (08 phút) — Giải quyết 02 câu Trắc nghiệm Đúng/Sai (2,0 điểm):* Phải đọc thật kỹ cả 4 ý `a, b, c, d` vì sai 1 ý sẽ giảm một nửa số điểm của câu (từ `1,0đ` xuống `0,5đ`!). Cẩn trọng với các từ tuyệt đối hóa như *"luôn luôn"*, *"chỉ có duy nhất"*, *"mọi thiết bị điện đều là thiết bị thông minh"*, *"không cần sự cho phép của tác giả"*.
- *Phút 21 – 40 (20 phút) — Trình bày 03 câu Tự luận (3,0 điểm):*
  - *Câu TL 1 (Chủ đề A.1 — khoảng 6 phút):* Viết rõ công thức quy đổi ($1" Byte" = 8" bit"$, $1" KB" = 1024" B"$, $1" MB" = 1024" KB"$, $1" GB" = 1024" MB"$), đổi cùng đơn vị trước khi nhân/chia, ghi đầy đủ đơn vị và lời kết luận.
  - *Câu TL 2 (Chủ đề B.2 — khoảng 6 phút):* Trình bày tách ý gạch đầu dòng rõ ràng (nguy cơ $arrow.r$ tác hại $arrow.r$ biện pháp phòng vệ cụ thể).
  - *Câu TL 3 (Chủ đề D.1 — khoảng 8 phút):* Áp dụng công thức *4 bước phân tích tình huống pháp lí*: *(1) Kết luận hợp pháp hay vi phạm pháp luật* $arrow.r$ *(2) Chỉ rõ căn cứ luật định (Luật Sở hữu trí tuệ / Luật CNTT / Luật An ninh mạng / Nghị định 15/2020/NĐ-CP)* $arrow.r$ *(3) Chỉ rõ hậu quả đối với nạn nhân & người vi phạm* $arrow.r$ *(4) Đề xuất cách hành xử đúng pháp luật, văn minh*.
- *Phút 41 – 45 (05 phút) — Rà soát toàn bài:* Kiểm tra lại phép nhân/chia với $1024$ và $8$, kiểm tra đủ 20 đáp án Phần I và đủ 8 ô Đúng/Sai Phần II (tuyệt đối không bỏ trống bất kì ý trắc nghiệm nào).
