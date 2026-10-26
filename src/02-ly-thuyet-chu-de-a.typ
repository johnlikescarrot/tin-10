// =============================================================================
// src/02-ly-thuyet-chu-de-a.typ
// Phần II - Chuyên đề 1: Chủ đề A. Máy tính và xã hội tri thức (SGK KNTT 10)
// =============================================================================

#import "template.typ": *

#pagebreak()

#part-banner(
  "Phần II",
  "HỆ THỐNG HOÁ LÍ THUYẾT DỄ NHỚ & GIẢI ĐÁP 100% BẢN ĐẶC TẢ GỐC",
  "Biên soạn chuẩn theo SGK Tin học 10 – Kết nối tri thức với cuộc sống • Trả lời trực tiếp toàn bộ 35/35 yêu cầu cần đạt",
  accent: c-navy,
)

#topic-banner(
  "Chuyên đề 1 • Chủ đề A",
  "MÁY TÍNH VÀ XÃ HỘI TRI THỨC",
  "Phạm vi SGK Kết nối tri thức 10: Bài 1 (Thông tin và xử lí thông tin) • Bài 2 (Vai trò của thiết bị thông minh và tin học) • Bài 7 (Thực hành thiết bị số)",
  "Trọng số: 4,0 điểm (40%)",
  accent: c-blue,
  bg: c-blue-bg,
  bdr: c-blue-bdr,
)

=== A.1. Dữ liệu, thông tin và xử lí thông tin (2,0 điểm: 2 TN NB + 2 TN TH + 1 TL VD)

==== 1. Sơ đồ tư duy & Hệ thống khái niệm cốt lõi

#block(
  width: 100%,
  fill: white,
  stroke: 0.6pt + c-blue-bdr,
  radius: 6pt,
  inset: 10pt,
  breakable: false,
  [
    #align(center)[#text(size: 9pt, weight: "bold", fill: c-navy)[SƠ ĐỒ CHU TRÌNH XỬ LÍ THÔNG TIN CỦA CON NGƯỜI VÀ HỆ THỐNG SỐ]]
    #v(5pt)
    #grid(
      columns: (1fr, auto, 1.15fr, auto, 1fr),
      align: center + horizon,
      column-gutter: 4pt,
      block(width: 100%, fill: c-blue-bg, stroke: 0.7pt + c-blue, radius: 5pt, inset: 7pt)[
        *1. TIẾP NHẬN DỮ LIỆU*\ *(Input / Đầu vào)*\
        #text(size: 8pt, fill: c-muted)[Bàn phím, chuột, micro,\ camera, cảm biến...]
      ],
      text(size: 13pt, weight: "bold", fill: c-blue)[$->$],
      block(width: 100%, fill: rgb("#dbeafe"), stroke: 0.9pt + c-navy, radius: 5pt, inset: 7pt)[
        *2. XỬ LÍ & LƯU TRỮ*\ *(Processing $arrow.l.r$ Storage)*\
        #text(size: 8pt, fill: c-ink)[CPU tính toán, biến đổi dữ liệu;\ RAM / Ổ cứng / Thẻ nhớ lưu trữ]
      ],
      text(size: 13pt, weight: "bold", fill: c-blue)[$->$],
      block(width: 100%, fill: c-teal-bg, stroke: 0.7pt + c-teal, radius: 5pt, inset: 7pt)[
        *3. XUẤT & TRUYỀN TIN*\ *(Output & Truyền thông)*\
        #text(size: 8pt, fill: c-muted)[Màn hình, loa, máy in,\ truyền qua mạng/Internet]
      ],
    )
  ]
)

- *Vật mang tin (Storage medium):* Là phương tiện vật lí dùng để lưu trữ và truyền tải dữ liệu (ví dụ: trang giấy, bia đá, đĩa CD/DVD, thẻ nhớ, USB, ổ cứng HDD/SSD...).
- *Dữ liệu (Data):* Là các con số, văn bản, hình ảnh, âm thanh... được thể hiện và lưu trữ trên vật mang tin. *Trong tin học*, dữ liệu là thông tin đã được đưa vào máy tính (mã hóa thành các dãy *bit* `0` và `1` để máy tính hiểu và xử lí được).
- *Thông tin (Information):* Là *ý nghĩa của dữ liệu*, là những hiểu biết con người thu nhận được về sự vật, hiện tượng thông qua việc tiếp nhận và xử lí dữ liệu trong một bối cảnh cụ thể.

#memory-box(
  "Công thức 1 dòng phân biệt Dữ liệu – Thông tin – Vật mang tin",
  [
    *Vật mang tin* là *"cái chứa"* (tờ giấy khám bệnh / thẻ nhớ) $->$ *Dữ liệu* là *"ký hiệu ghi trên đó"* (`39.5°C`, dòng chữ, bức ảnh X-quang) $->$ *Thông tin* là *"hiểu biết rút ra"* (*"Bệnh nhân đang bị sốt cao, cần hạ sốt ngay"*).
  ]
)

==== 2. Bảng thang bậc đơn vị lưu trữ dữ liệu & Công thức quy đổi chuẩn

- *Bit (`b` – chữ thường, viết tắt của binary digit):* Đơn vị nhỏ nhất biểu diễn dữ liệu trong máy tính, chỉ nhận một trong hai trạng thái `0` hoặc `1`.
- *Byte (`B` – chữ in hoa):* Đơn vị cơ bản đo dung lượng dữ liệu. Quy ước bất di bất dịch: *$1 "Byte (B)" = 8 "bit (b)"$*.
- *Các đơn vị bội của Byte* (trong Tin học phổ thông quy ước theo hệ nhị phân với hệ số nhân *$2^10 = 1024$*):

#block(breakable: false)[
  #set text(size: 8.6pt)
  #table(
    columns: (0.8fr, 1.15fr, 1.3fr, 1.45fr, 1.8fr),
    inset: (x: 6pt, y: 5pt),
    stroke: 0.5pt + c-border,
    align: (center + horizon, left + horizon, center + horizon, center + horizon, left + horizon),
    fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { white } else { c-light },
    table.header(
      [#text(fill: white, weight: "bold")[Kí hiệu]],
      [#text(fill: white, weight: "bold")[Tên gọi đầy đủ]],
      [#text(fill: white, weight: "bold")[Quy đổi liền kề]],
      [#text(fill: white, weight: "bold")[Quy đổi ra Byte]],
      [#text(fill: white, weight: "bold")[Hình dung thực tế dễ nhớ]],
    ),
    [*b*], [Bit], [Đơn vị nhỏ nhất (`0`/`1`)], [$1 "B" = 8 "bit"$], [1 công tắc bật/tắt (1 chữ số nhị phân)],
    [*B*], [Byte], [$1 "B" = 8 "b"$], [$2^0 "B" = 1 "B"$], [1 kí tự chữ cái Tiếng Anh (mã ASCII)],
    [*KB*], [Kilobyte], [$1 "KB" = 1024 "B"$], [$2^10 "B" = 1.024 "B"$], [Khoảng nửa trang văn bản thuần chữ],
    [*MB*], [Megabyte], [$1 "MB" = 1024 "KB"$], [$2^20 "B" approx 1,05 times 10^6 "B"$], [1 bức ảnh chụp ĐT (3–5 MB) / 1 bài hát MP3],
    [*GB*], [Gigabyte], [$1 "GB" = 1024 "MB"$], [$2^30 "B" approx 1,07 times 10^9 "B"$], [1 bộ phim Full HD / dung lượng USB (16–128 GB)],
    [*TB*], [Terabyte], [$1 "TB" = 1024 "GB"$], [$2^40 "B" approx 1,10 times 10^12 "B"$], [Ổ cứng máy tính hiện đại (1–4 TB)],
    [*PB*], [Petabyte], [$1 "PB" = 1024 "TB"$], [$2^50 "B"$], [Trung tâm dữ liệu đám mây (*còn có EB, ZB, YB*)],
  )
]

#pitfall-box(
  "Hai cái bẫy kinh điển học sinh hay mất điểm ở bài toán đổi đơn vị",
  [
    1. *Nhầm `B` (Byte) và `b` (bit):* Khi đề cho tốc độ mạng là `Mbps` (*Megabit/giây*, chữ `b` thường) mà dung lượng tệp là `MB` (*Megabyte*, chữ `B` hoa), bắt buộc phải đổi cùng đơn vị trước khi chia: *$1 "MB" = 8 "Mb"$* (hoặc chia tốc độ `Mbps` cho `8` để ra `MB/s`).
    2. *Nhầm chiều nhân / chia 1024:* Từ *đơn vị lớn sang đơn vị nhỏ* (VD: `GB` $->$ `MB` $->$ `KB` $->$ `B`) thì *NHÂN với 1024* qua mỗi bậc; từ *đơn vị nhỏ sang đơn vị lớn* (VD: `KB` $->$ `MB` $->$ `GB`) thì *CHIA cho 1024* qua mỗi bậc. Khi tính *"lưu được tối đa bao nhiêu tệp/bức ảnh"*, luôn lấy *phần nguyên* của phép chia!
  ]
)

==== 3. Giải đáp trọn vẹn Yêu cầu cần đạt gốc trong Bản đặc tả (Đơn vị A.1)

#spec-qa(
  "A1.1", "NB",
  "Nêu được sự ưu việt của việc lưu trữ dựa trên các thiết bị số.",
  [
    So với phương pháp lưu trữ truyền thống (trên giấy, sổ sách, băng từ...), lưu trữ bằng thiết bị số có *4 ưu điểm vượt trội*:
    1. *Dung lượng lưu trữ cực lớn trong kích thước nhỏ gọn, chi phí thấp:* Một thẻ nhớ hoặc USB nhỏ bằng ngón tay (64 GB – 1 TB) có thể lưu trữ lượng dữ liệu tương đương hàng trăm nghìn cuốn sách in dày hoặc hàng chục nghìn bức ảnh, video độ phân giải cao.
    2. *Tìm kiếm, truy xuất và sắp xếp thông tin cực nhanh, chính xác:* Chỉ mất vài phần giây để tìm đúng một từ khóa trong hàng vạn tệp văn bản thay vì phải lật dở thủ công hàng giờ.
    3. *Sao chép nguyên bản, bảo quản bền lâu, dễ sao lưu dự phòng:* Bản sao dữ liệu số giống bản gốc *100%* không bị suy giảm chất lượng sau nhiều lần sao chép; không lo mối mọt, ẩm mốc như giấy và có thể sao lưu lên đám mây.
    4. *Dễ dàng mang theo, chia sẻ và truy cập từ xa:* Kết hợp với mạng máy tính và Internet, dữ liệu trên thiết bị số có thể chia sẻ tức thời cho nhiều người ở bất kì đâu.
  ]
)

#spec-qa(
  "A1.2 & A1.3", "TH",
  "Phân biệt được thông tin và dữ liệu; Nêu được ví dụ minh hoạ về thông tin và dữ liệu.",
  [
    #table(
      columns: (1fr, 1.35fr, 1.35fr),
      inset: 5.5pt,
      stroke: 0.45pt + c-border,
      fill: (x, y) => if y == 0 { rgb("#dbeafe") } else { white },
      [*Tiêu chí đối chiếu*], [*Dữ liệu (Data)*], [*Thông tin (Information)*],
      [*Bản chất*], [Là *hình thức thể hiện* (con số, chữ viết, hình ảnh, âm thanh, dãy bit `0`/`1` lưu trên vật mang tin).], [Là *nội dung, ý nghĩa* rút ra được từ việc xử lí dữ liệu, đem lại sự hiểu biết cho con người.],
      [*Tính phụ thuộc*], [Tồn tại khách quan trên vật mang tin/máy tính dù người xem có hiểu hay không.], [Phụ thuộc vào kiến thức, ngữ cảnh của người nhận (cùng một dữ liệu có thể cho thông tin khác nhau).],
      [*Tính đa dạng biểu diễn*], [Có nhiều dạng dữ liệu khác nhau (văn bản, âm thanh, hình ảnh) cùng biểu đạt một thông tin.], [Có tính toàn vẹn về mặt ý nghĩa.],
    )
    *Ví dụ minh hoạ chuẩn SGK:*
    - *Ví dụ 1 (Dự báo thời tiết):* Trên màn hình điện thoại hiển thị các con số `38°C`, `Độ ẩm 85%` và biểu tượng đám mây có tia chớp $->$ đó là *dữ liệu*. Nhìn vào đó, bạn An biết được *"Chiều nay trời oi bức và sắp có mưa dông nên đi học cần mang theo áo mưa"* $->$ sự hiểu biết đó là *thông tin*.
    - *Ví dụ 2 (Bảng điểm):* Dãy số `8.5; 9.0; 9.2` lưu trong tệp Excel là *dữ liệu*; kết luận *"Học sinh đạt danh hiệu Học sinh Giỏi môn Tin học"* rút ra sau khi tính điểm trung bình là *thông tin*.
  ]
)

#spec-qa(
  "A1.4 & A1.5", "VD",
  "Chuyển đổi được giữa các đơn vị lưu trữ thông tin: B, KB, MB,...; Xử lí và truyền thông tin bằng thiết bị số.",
  [
    *3 dạng bài toán Vận dụng tiêu biểu cần nắm vững công thức:*
    - *Dạng 1 – Đổi đơn vị trực tiếp:*
      - Ví dụ: $2 "GB" = 2 times 1024 "MB" = 2048 "MB" = 2048 times 1024 "KB" = 2.097.152 "KB"$.
      - Ví dụ: $5120 "KB" = 5120 : 1024 = 5 "MB"$; $64 "bit" = 64 : 8 = 8 "Byte"$.
    - *Dạng 2 – Bài toán tính sức chứa thiết bị lưu trữ:*
      $ "Số lượng tệp tối đa lưu được" = floor("Dung lượng trống của thiết bị (cùng đơn vị)" / "Dung lượng trung bình của 1 tệp") $
      *Ví dụ mẫu:* Một thẻ nhớ còn trống `16 GB`. Hỏi lưu được tối đa bao nhiêu bức ảnh chất lượng cao, biết mỗi bức ảnh có dung lượng trung bình `4 MB`?
      - *Giải:* Đổi $16 "GB" = 16 times 1024 = 16.384 "MB"$. Số bức ảnh lưu được tối đa là: $16.384 : 4 = 4.096$ (bức ảnh).
    - *Dạng 3 – Bài toán tốc độ truyền thông tin qua thiết bị số:*
      $ "Thời gian truyền (giây)" = "Dung lượng tệp tính theo bit (hoặc Mb)" / "Tốc độ đường truyền tính theo bps (hoặc Mbps)" $
      *Ví dụ mẫu:* Tải một tệp video bài giảng dung lượng `300 MB` qua đường truyền mạng có tốc độ ổn định `80 Mbps` (Megabit/giây). Tính thời gian tải tệp?
      - *Giải:* Đổi dung lượng tệp sang Megabit: $300 "MB" = 300 times 8 = 2400 "Mb"$. Thời gian tải tệp là: $t = 2400 : 80 = 30$ (giây).
  ]
)

=== A.2. Vai trò của máy tính và thiết bị thông minh trong nền kinh tế tri thức (2,0 điểm: 4 TN NB + 1 ĐS)

==== 1. Tóm tắt hệ thống kiến thức trọng tâm dễ nhớ

#grid(
  columns: (1fr, 1fr),
  column-gutter: 9pt,
  concept-box(
    "4 cuộc Cách mạng công nghiệp (CMCN)",
    [
      - *CMCN 1.0 (cuối TK XVIII):* Cơ khí hoá bằng *động cơ hơi nước*.
      - *CMCN 2.0 (cuối TK XIX – đầu TK XX):* Điện khí hoá & *dây chuyền sản xuất hàng loạt*.
      - *CMCN 3.0 (từ thập niên 1970):* Tự động hoá sản xuất nhờ *máy tính điện tử & CNTT*.
      - *CMCN 4.0 (đầu TK XXI – nay):* Sản xuất thông minh dựa trên *IoT, AI (Trí tuệ nhân tạo), Big Data (Dữ liệu lớn), Điện toán đám mây*, hệ thống thực – ảo.
    ],
    accent: c-blue, bg: c-blue-bg, bdr: c-blue-bdr, breakable-box: false,
  ),
  concept-box(
    "Kinh tế tri thức & Thiết bị thông minh",
    [
      - *Kinh tế tri thức:* Nền kinh tế trong đó *tri thức khoa học – công nghệ và thông tin* đóng vai trò trực tiếp, quyết định nhất vào việc tạo ra của cải vật chất và giá trị gia tăng.
      - *3 dấu hiệu nhận diện Thiết bị thông minh:*
        1. Có bộ xử lí & phần mềm giúp *hoạt động tự chủ/thích ứng*;
        2. *Tương tác thông minh* với người dùng/môi trường (cảm biến, giọng nói, chạm);
        3. *Có kết nối mạng* (Wi-Fi, Bluetooth, 4G/5G...) để trao đổi dữ liệu.
    ],
    accent: c-teal, bg: c-teal-bg, bdr: c-teal-bdr, breakable-box: false,
  )
)

==== 2. Bảng các mốc thời gian & thành tựu nổi bật của ngành Tin học (Trọng tâm TN Nhận biết)

#block(breakable: true)[
  #set text(size: 8.5pt)
  #table(
    columns: (0.9fr, 1.3fr, 2.3fr),
    inset: (x: 6.5pt, y: 5pt),
    stroke: 0.45pt + c-border,
    fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { white } else { c-light },
    table.header(
      [#text(fill: white, weight: "bold")[Mốc thời gian]],
      [#text(fill: white, weight: "bold")[Thành tựu / Sự kiện tiêu biểu]],
      [#text(fill: white, weight: "bold")[Ý nghĩa đối với sự phát triển của ngành Tin học]],
    ),
    [*1936 – 1945*], [Máy Turing (1936) & Kiến trúc *Von Neumann* (1945)], [Đặt nền móng lí thuyết tính toán và nguyên lí chương trình lưu trữ trong bộ nhớ cho mọi máy tính hiện đại.],
    [*1946*], [Máy tính điện tử số *ENIAC* ra đời tại Mỹ], [Mở đầu kỉ nguyên máy tính điện tử (Thế hệ 1 dùng *đèn điện tử chân không*; tiếp theo là *Transistor* $->$ *IC* $->$ *VLSI/Vi xử lí* $->$ *ULSI/AI*).],
    [*1950 & 1956*], [*Phép thử Turing* (1950); Hội thảo Dartmouth (1956)], [Khai sinh lĩnh vực nghiên cứu *Trí tuệ nhân tạo (AI – Artificial Intelligence)*.],
    [*1969*], [Mạng *ARPANET* ra đời (Bộ Quốc phòng Mỹ)], [Tiền thân trực tiếp của mạng *Internet* toàn cầu ngày nay.],
    [*Thập niên 1970–1980*], [Vi xử lí, máy tính cá nhân (*PC*), giao diện đồ hoạ (*GUI*)], [Đưa máy tính từ phòng thí nghiệm đến từng cá nhân, gia đình, văn phòng nhờ chuột, cửa sổ, biểu tượng trực quan.],
    [*1989 – 1991*], [*Tim Berners-Lee* phát minh *World Wide Web (WWW)*], [Tạo ra hệ thống siêu văn bản toàn cầu, giúp Internet bùng nổ mạnh mẽ khắp thế giới (*Việt Nam chính thức hoà mạng Internet năm 1997*).],
    [*1997 & 1998*], [*Deep Blue* thắng cờ vua thế giới (1997); *Google* ra đời (1998)], [Khẳng định sức mạnh tính toán vượt trội của máy tính và mở ra kỉ nguyên tìm kiếm thông tin trên Web.],
    [*Thập niên 2000*], [Mạng xã hội, Điện toán đám mây, *Smartphone* (2007+)], [Phổ cập thiết bị di động thông minh, kết nối xã hội và lưu trữ đám mây mọi lúc mọi nơi.],
    [*2016 – nay*], [*AlphaGo* thắng cờ vây (2016), Robot *Sophia*, AI tạo sinh], [Bùng nổ Học sâu (*Deep Learning*), Dữ liệu lớn (*Big Data*), *IoT* và chuyển đổi số toàn diện trong CMCN 4.0.],
  )
]

==== 3. Giải đáp trọn vẹn Yêu cầu cần đạt gốc trong Bản đặc tả (Đơn vị A.2 & A.3)

#spec-qa(
  "A2.1 & A2.7", "NB & TH",
  "Trình bày được những đóng góp cơ bản của tin học đối với xã hội và nêu ví dụ minh họa.",
  [
    Tin học có *4 đóng góp cơ bản, toàn diện* đối với xã hội hiện đại (mẹo nhớ: *Quản lí – Tự động – Khoa học – Đời sống*):
    1. *Quản lí và điều hành tự động các hoạt động xã hội – kinh tế:* Tin học hoá công tác lưu trữ hồ sơ, tra cứu, thống kê, điều hành chính xác và minh bạch.
       - *Ví dụ:* Cổng Dịch vụ công Quốc gia (làm hộ chiếu, đăng kí xe trực tuyến), phần mềm quản lí bệnh viện (bệnh án điện tử), quản lí trường học (vnEdu/SMAS), ngân hàng số (chuyển khoản QR 24/7).
    2. *Tự động hoá các thiết bị và dây chuyền sản xuất:* Điều khiển máy móc, robot làm việc chính xác, năng suất cao, thay thế con người trong môi trường độc hại/nguy hiểm.
       - *Ví dụ:* Dây chuyền robot hàn lắp ráp ô tô VinFast/Toyota, hệ thống nhà kính tưới nước tự động, hệ thống thu phí không dừng ETC.
    3. *Giải quyết các bài toán khoa học – kĩ thuật phức tạp:* Thực hiện hàng tỉ phép tính/giây để mô phỏng, dự báo những bài toán khổng lồ.
       - *Ví dụ:* Siêu máy tính dự báo đường đi của bão, mô phỏng khí hậu toàn cầu, giải mã bản đồ gen người, thiết kế mô phỏng khí động học máy bay 3D.
    4. *Thay đổi sâu sắc phương thức giao tiếp, học tập, làm việc, mua sắm và giải trí:* Xoá nhoà khoảng cách địa lí, nâng cao chất lượng sống.
       - *Ví dụ:* Học trực tuyến qua LMS/Zoom, khám bệnh từ xa (*Telehealth*), thương mại điện tử, gọi video quốc tế miễn phí, dịch tự động đa ngôn ngữ.
  ]
)

#spec-qa(
  "A2.2 & A2.4", "NB & TH",
  "Nhận biết một vài thiết bị số thông dụng khác ngoài PC/laptop; Nêu ví dụ cụ thể về thiết bị thông minh.",
  [
    - *Các thiết bị số thông dụng ngoài máy tính để bàn (PC) và laptop:*
      - *Nhóm thiết bị số thông thường (chức năng cố định, không tự chủ/kết nối mạng thông minh):* Máy tính bỏ túi (*Calculator*, VD: Casio fx-580VN X), máy ảnh kĩ thuật số cơ bản, đồng hồ điện tử hiện số đơn thuần, đầu đọc mã vạch, máy nghe nhạc MP3 cổ điển, thẻ nhớ, ổ cứng di động, USB.
      - *Nhóm thiết bị thông minh (ví dụ cụ thể):* Điện thoại thông minh (*Smartphone*), máy tính bảng (*Tablet*), đồng hồ thông minh (*Smartwatch* đo nhịp tim, đếm bước chân, nhận cuộc gọi), tivi thông minh (*Smart TV*), loa thông minh điều khiển bằng giọng nói, robot hút bụi tự lập bản đồ phòng, camera an ninh AI nhận diện khuôn mặt, công tắc/điều hoà thông minh trong *Smart Home*.
  ]
)

#spec-qa(
  "A2.5 & A2.6", "TH",
  "Giải thích vai trò của thiết bị thông minh đối với xã hội và CMCN 4.0; Giải thích vì sao các thiết bị đó cũng là những hệ thống xử lí thông tin.",
  [
    - *Vì sao thiết bị thông minh là một hệ thống xử lí thông tin?*
      Vì bên trong mỗi thiết bị thông minh thực chất là một "máy tính thu nhỏ" thực hiện trọn vẹn *4 hoạt động của chu trình xử lí thông tin*:
      1. *Nhận dữ liệu vào (Input):* Qua màn hình cảm ứng, micro, camera và hệ thống cảm biến (nhiệt độ, gia tốc, nhịp tim, ánh sáng, hồng ngoại...).
      2. *Xử lí dữ liệu (Processing):* Có vi xử lí (CPU/chip xử lí) chạy hệ điều hành và phần mềm/AI để phân tích dữ liệu và ra quyết định.
      3. *Lưu trữ (Storage):* Có bộ nhớ RAM, bộ nhớ Flash (ROM) để lưu hệ điều hành, ứng dụng và dữ liệu người dùng.
      4. *Đưa thông tin ra & Truyền thông (Output):* Hiển thị hình ảnh ra màn hình, phát âm thanh ra loa, điều khiển động cơ/rơ-le và truyền nhận dữ liệu qua Wi-Fi, Bluetooth, 4G/5G.
    - *Vai trò đối với xã hội và cuộc CMCN 4.0:*
      - Là *thành phần cốt lõi tạo nên mạng lưới Internet vạn vật (IoT)*: kết nối thế giới vật lí thực với không gian số ảo.
      - Là *nguồn thu thập dữ liệu thời gian thực khổng lồ* từ mọi lĩnh vực (giao thông, y tế, nông nghiệp, nhà máy) tạo nên *Dữ liệu lớn (Big Data)* nuôi dưỡng *Trí tuệ nhân tạo (AI)*.
      - Giúp tự động hoá thông minh mọi hoạt động sản xuất và đời sống, giải phóng sức lao động và thúc đẩy chuyển đổi số trong nền kinh tế tri thức.
  ]
)

#spec-qa(
  "A3.1 & A3.2", "VD",
  "Kĩ năng sử dụng thiết bị số của mỗi công dân: Khởi động thiết bị số thông dụng; sử dụng tệp dữ liệu, chức năng và phần mềm ứng dụng cơ bản cài sẵn.",
  [
    - *Khởi động & thiết lập cơ bản:* Bật nguồn, mở khóa bảo mật (mật khẩu/PIN/vân tay/khuôn mặt), kết nối Wi-Fi hoặc dữ liệu di động, điều chỉnh âm lượng, độ sáng, ngôn ngữ Tiếng Việt.
    - *Quản lí tệp và thư mục:* Sử dụng *File Explorer* (trên Windows) hoặc ứng dụng *Tệp / Quản lí tệp* (trên điện thoại) để tạo thư mục phân cấp khoa học, đổi tên, sao chép, di chuyển, tìm kiếm, xóa tệp và kiểm tra dung lượng bộ nhớ còn trống; nhận biết phần mở rộng tệp phổ biến (`.docx`, `.pdf`, `.xlsx`, `.jpg`, `.png`, `.mp3`, `.mp4`, `.zip`).
    - *Khai thác phần mềm cài sẵn & trao đổi dữ liệu:* Sử dụng trình duyệt web, máy ảnh, ghi âm, máy tính, lịch/ghi chú; truyền tệp an toàn giữa điện thoại và máy tính qua cáp USB, Bluetooth, thư điện tử hoặc lưu trữ đám mây.
  ]
)
