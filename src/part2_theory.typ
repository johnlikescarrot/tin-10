#import "theme.typ": *

= PHẦN II. HỆ THỐNG HÓA KIẾN THỨC TRỌNG TÂM & MẸO GHI NHỚ NHANH

== 2.1. CHỦ ĐỀ 1 (CHỦ ĐỀ A): MÁY TÍNH VÀ XÃ HỘI TRI THỨC

=== BÀI 1. THÔNG TIN VÀ XỬ LÍ THÔNG TIN

*1. Phân biệt bộ tứ khái niệm nền tảng: Vật mang tin — Dữ liệu — Thông tin — Tri thức*

Trong đời sống và trong tin học, quá trình nhận thức luôn đi theo chuỗi chuyển hóa liên tục: *Vật mang tin* chứa *Dữ liệu* $arrow.r$ con người/máy tính xử lí, diễn giải tạo thành *Thông tin* $arrow.r$ tích lũy, khái quát hóa tạo thành *Tri thức*.

#set text(size: 8.6pt)
#table(
  columns: (0.85fr, 1.55fr, 1.6fr),
  inset: (x: 6pt, y: 5.5pt),
  stroke: 0.5pt + c-border,
  fill: (col, row) => if row == 0 { c-navy.lighten(88%) } else if calc.odd(row) { white } else { c-bg-soft },
  align: (left + horizon, left + top, left + top),

  [*Khái niệm*], [*Bản chất cốt lõi (Từ khóa nhận diện)*], [*Ví dụ minh họa trực quan*],

  [*Vật mang tin*\ _(Storage Medium)_],
  [Là *phương tiện vật chất* dùng để lưu trữ và truyền tải dữ liệu (giấy, bảng đá, đĩa CD/DVD, thẻ nhớ, ổ cứng HDD/SSD, USB, sóng điện từ...).],
  [Tờ giấy kiểm tra, tấm biển báo giao thông, chiếc thẻ nhớ MicroSD, ổ cứng máy tính.],

  [*Dữ liệu*\ _(Data)_],
  [Là *những gì được ghi lên vật mang tin* (con số, chữ viết, kí hiệu, hình ảnh, âm thanh...). Trong máy tính, dữ liệu là thông tin đã được mã hóa thành *dãy bit nhị phân (`0` và `1`)* để máy xử lí.],
  [Con số `39,5` hiển thị trên màn hình nhiệt kế điện tử; dòng chữ `"Mưa to, gió giật cấp 8"` trong tin nhắn; tệp âm thanh `.mp3`.],

  [*Thông tin*\ _(Information)_],
  [Là *ý nghĩa* rút ra được từ dữ liệu sau khi tiếp nhận và xử lí; đem lại *sự hiểu biết* cho con người về thế giới xung quanh và về chính bản thân mình.],
  [Hiểu được bệnh nhân đang bị *sốt cao* (từ số `39,5°C`); biết chiều nay *cần mang áo mưa và hạn chế ra đường* (từ bản tin thời tiết).],

  [*Tri thức*\ _(Knowledge)_],
  [Là những *hiểu biết có tính hệ thống, quy luật, khái quát cao* được con người đúc kết từ nhiều thông tin qua học tập, trải nghiệm; dùng để ra quyết định và giải quyết vấn đề.],
  [Quy luật y khoa: *"Trẻ nhỏ sốt trên 38,5°C cần chườm ấm, bù điện giải và dùng thuốc hạ sốt đúng liều lượng theo cân nặng"*.],
)
#set text(size: 9.7pt)

- *Mối quan hệ biện chứng cần nhớ:*
  + *Dữ liệu là hình thức thể hiện, Thông tin là nội dung ý nghĩa:* Cùng một thông tin có thể biểu diễn bằng nhiều dạng dữ liệu khác nhau (ví dụ: thông tin *"Cấm hút thuốc"* có thể thể hiện bằng dòng chữ tiếng Việt, dòng chữ `"No Smoking"` hoặc hình vẽ điếu thuốc gạch chéo).
  + *Tính tương đối của thông tin:* Cùng một dữ liệu nhưng với những người có vốn *tri thức* khác nhau có thể rút ra lượng thông tin khác nhau (ví dụ: bản chụp X-quang phổi cung cấp rất nhiều thông tin bệnh lí cho bác sĩ chuyên khoa nhưng người không có chuyên môn khó rút ra thông tin).

*2. Chu trình xử lí thông tin trong máy tính (4 hoạt động cơ bản)*

Mọi hệ thống xử lí thông tin bằng máy tính đều gồm *4 hoạt động gắn kết chặt chẽ*:

#block(
  width: 100%,
  fill: c-bg-soft,
  stroke: 0.6pt + c-teal.lighten(40%),
  radius: 5pt,
  inset: 9pt,
  breakable: false,
  [
    #set par(justify: false)
    #grid(
      columns: (1fr, auto, 1fr, auto, 1fr),
      align: (center + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
      column-gutter: 5pt,
      block(fill: c-teal-light, stroke: 0.6pt + c-teal, radius: 4pt, inset: 6pt, width: 100%)[
        *1. TIẾP NHẬN (INPUT)*\
        #text(size: 8pt)[Thu nhận dữ liệu từ thế giới ngoài qua *Thiết bị vào*: bàn phím, chuột, micro, camera, cảm biến, máy quét.]
      ],
      text(size: 13pt, weight: "bold", fill: c-teal)[$arrow.r$],
      block(fill: c-navy-light, stroke: 0.6pt + c-navy, radius: 4pt, inset: 6pt, width: 100%)[
        *2. XỬ LÍ (PROCESSING)*\
        #text(size: 8pt)[Tính toán, phân tích, biến đổi dữ liệu tạo thông tin mới do *CPU (Bộ xử lí trung tâm)* thực hiện.\ $arrow.t.b$ *3. LƯU TRỮ (STORAGE)*\ Bộ nhớ trong (RAM/ROM) & Bộ nhớ ngoài (SSD, HDD, USB, Cloud).]
      ],
      text(size: 13pt, weight: "bold", fill: c-teal)[$arrow.r$],
      block(fill: c-amber-light.lighten(20%), stroke: 0.6pt + c-amber, radius: 4pt, inset: 6pt, width: 100%)[
        *4. XUẤT / TRUYỀN (OUTPUT)*\
        #text(size: 8pt)[Đưa thông tin ra *Thiết bị ra* (màn hình, loa, máy in, máy chiếu) hoặc truyền qua mạng tới thiết bị khác.]
      ],
    )
  ],
)

*3. Đơn vị đo lượng dữ liệu và quy tắc chuyển đổi chuẩn SGK Kết nối tri thức*

- *Bit (`b` — viết tắt của _binary digit_):* Là *đơn vị nhỏ nhất* dùng để biểu diễn và lưu trữ dữ liệu trong máy tính. Mỗi bit chỉ nhận một trong hai trạng thái kí hiệu là `0` hoặc `1`. Một dãy gồm $n$ bit biểu diễn được $2^n$ trạng thái (thông tin) khác nhau.
- *Byte (`B` — viết chữ B in hoa):* Là đơn vị lưu trữ dữ liệu cơ bản: *$1" Byte (B)" = 8" bit (b)"$* (biểu diễn được $2^8 = 256$ trạng thái).
- *Bảng các đơn vị bội số của Byte (theo chuẩn nhị phân $2^(10) = 1024$ trong Bài 1 SGK Kết nối tri thức):*

#set text(size: 8.4pt)
#table(
  columns: (0.8fr, 1.15fr, 1.45fr, 1.25fr, 1.35fr),
  inset: (x: 5pt, y: 4.5pt),
  stroke: 0.5pt + c-border,
  fill: (col, row) => if row == 0 { c-navy.lighten(88%) } else if calc.odd(row) { white } else { c-bg-soft },
  align: (center + horizon, left + horizon, center + horizon, center + horizon, left + horizon),

  table.header(
    [*Kí hiệu*], [*Tên đọc đầy đủ*], [*Quy đổi từ đơn vị liền trước*], [*Tính theo lũy thừa Byte*], [*Cảm nhận dung lượng thực tế*],
  ),
  [*B*], [Byte], [$1" B" = 8" bit"$], [$2^0" B" = 1" B"$], [1 kí tự chữ cái tiếng Anh (ASCII)],
  [*KB*], [Kilobyte], [$1" KB" = 1024" B"$], [$2^(10)" B"$], [1 trang văn bản ngắn không ảnh],
  [*MB*], [Megabyte], [$1" MB" = 1024" KB"$], [$2^(20)" B"$], [1 bức ảnh chụp ĐT / 1 bài hát MP3],
  [*GB*], [Gigabyte], [$1" GB" = 1024" MB"$], [$2^(30)" B"$], [1 bộ phim Full HD / dung lượng USB],
  [*TB*], [Terabyte], [$1" TB" = 1024" GB"$], [$2^(40)" B"$], [Ổ cứng máy tính cá nhân hiện đại],
  [*PB*], [Petabyte], [$1" PB" = 1024" TB"$], [$2^(50)" B"$], [Hệ thống lưu trữ trung tâm dữ liệu],
  [*EB*], [Exabyte], [$1" EB" = 1024" PB"$], [$2^(60)" B"$], [Dữ liệu đám mây quy mô toàn cầu],
  [*ZB*], [Zettabyte], [$1" ZB" = 1024" EB"$], [$2^(70)" B"$], [Tổng lưu lượng Internet thế giới/năm],
  [*YB*], [Yottabyte], [$1" YB" = 1024" ZB"$], [$2^(80)" B"$], [Đơn vị lớn nhất trong bảng chuẩn],
)
#set text(size: 9.7pt)

#callout(title: "CÔNG THỨC ĐÓNG KHUNG & MẸO GHI NHỚ NHANH BÀI 1", tone: "memo")[
  - *Câu thần chú nhớ thứ tự 9 đơn vị Byte:* #strong[B]ạn (*B*) — #strong[K]hông (*KB*) — #strong[M]ang (*MB*) — #strong[G]iày (*GB*) — #strong[T]hì (*TB*) — #strong[P]hải (*PB*) — #strong[E]m (*EB*) — #strong[Z]ữ (*ZB*) — #strong[Y]ên (*YB*).
  - *Quy tắc nhân/chia khi đổi đơn vị:*
    + Đổi từ *đơn vị LỚN sang đơn vị NHỎ* liền kề $arrow.r$ *NHÂN với `1024`* _(riêng từ Byte sang bit thì *NHÂN với `8`*)_.
    + Đổi từ *đơn vị NHỎ sang đơn vị LỚN* liền kề $arrow.r$ *CHIA cho `1024`* _(riêng từ bit sang Byte thì *CHIA cho `8`*)_.
  - *Bẫy kinh điển giữa `b` (bit) và `B` (Byte) trong bài toán tốc độ mạng:* Tốc độ mạng Internet thường tính bằng *`Mbps`* (*Megabit/giây*, chữ `b` viết thường!), trong khi dung lượng tệp tin tính bằng *`MB`* (*Megabyte*, chữ `B` viết hoa!). Vì $1" Byte" = 8" bit"$, nên tốc độ tải thực tế tính theo `MB/s` là: $"Tốc độ (MB/s)" = "Tốc độ (Mbps)" / 8$. Ví dụ: Mạng `80 Mbps` tải tối đa được $80 : 8 = 10" MB/giây"$.
]

*4. Sự ưu việt của việc lưu trữ, xử lí và truyền thông tin bằng thiết bị số*

So với phương pháp thủ công truyền thống (ghi chép sổ sách giấy tờ, gửi thư bưu điện, tính nhẩm), thiết bị số mang lại *4 ưu điểm vượt trội*:
+ *Lưu trữ dung lượng khổng lồ trong kích thước siêu nhỏ gọn, chi phí thấp, bền vững:* Một thẻ nhớ hay ổ SSD nhỏ bằng lòng bàn tay lưu được hàng trăm GB — tương đương hàng trăm nghìn cuốn sách dày; dễ dàng sao chép dự phòng mà không làm giảm chất lượng bản sao (khác với photocopy giấy hay băng từ cũ).
+ *Tìm kiếm và truy xuất thông tin tức thời:* Chỉ mất vài phần nghìn giây để tìm chính xác một từ khóa giữa hàng triệu trang tài liệu số hóa.
+ *Xử lí tự động tốc độ cực cao và chính xác tuyệt đối:* Máy tính hiện đại thực hiện hàng tỉ phép tính mỗi giây (GFLOPS/TFLOPS), làm việc liên tục 24/7 không sai sót do mệt mỏi.
+ *Truyền thông tin tốc độ ánh sáng, không giới hạn khoảng cách địa lí:* Thông qua mạng máy tính và Internet, văn bản, âm thanh, hình ảnh, video được truyền đi khắp thế giới gần như tức thời tới một hoặc hàng triệu người nhận cùng lúc.

=== BÀI 2. VAI TRÒ CỦA THIẾT BỊ THÔNG MINH VÀ TIN HỌC ĐỐI VỚI XÃ HỘI

*1. Thiết bị số và Thiết bị thông minh (Smart Devices)*

- *Thiết bị số thông dụng ngoài máy tính để bàn (PC) và máy tính xách tay (Laptop):* Máy tính bảng (Tablet), điện thoại thông minh (Smartphone), đồng hồ thông minh (Smartwatch), tivi thông minh (Smart TV), máy ảnh kĩ thuật số, máy quay kĩ thuật số, máy đọc sách điện tử (Kindle), thiết bị định vị GPS, thiết bị y tế số, thẻ nhớ/ổ cứng di động, bộ định tuyến mạng (Router)...
- *Khái niệm Thiết bị thông minh:* Là thiết bị điện tử *có thể hoạt động một cách tự chủ* ở mức độ nhất định (nhờ được tích hợp bộ vi xử lí, bộ nhớ, hệ điều hành/phần mềm thông minh, hệ thống cảm biến và ngày càng có thêm Trí tuệ nhân tạo — AI) đồng thời *có khả năng kết nối mạng* (Wi-Fi, Bluetooth, 4G/5G, NFC...) để trao đổi dữ liệu với các thiết bị khác và tương tác linh hoạt với người dùng/môi trường.
- *Giải thích vì sao Thiết bị thông minh cũng là một Hệ thống xử lí thông tin:* Mỗi thiết bị thông minh giống như một máy tính thu nhỏ vì thực hiện trọn vẹn *4 hoạt động xử lí thông tin*:
  + *(1) Thu nhận dữ liệu:* Màn hình cảm ứng, micro, camera, cảm biến ánh sáng/nhiệt độ/gia tốc/nhịp tim/GPS;
  + *(2) Xử lí dữ liệu:* Chip vi xử lí trung tâm (CPU/SoC) chạy hệ điều hành (Android, iOS, watchOS...) và ứng dụng;
  + *(3) Lưu trữ dữ liệu:* Bộ nhớ RAM và bộ nhớ lưu trữ Flash tích hợp;
  + *(4) Xuất & Truyền thông tin:* Màn hình hiển thị, loa phát âm thanh, mô-tơ rung và mô-đun truyền thông không dây (Wi-Fi, 5G, Bluetooth).

#callout(title: "BẪY TRẮC NGHIỆM CẦN TRÁNH: PHÂN BIỆT THIẾT BỊ THÔNG MINH VÀ THIẾT BỊ ĐIỆN TỬ THƯỜNG", tone: "warn")[
  Không phải mọi thiết bị điện tử hay thiết bị số đều là *thiết bị thông minh*!
  - *KHÔNG phải thiết bị thông minh:* Máy tính bỏ túi thông thường (ví dụ Casio fx-570VN/580VNX), đồng hồ điện tử đeo tay chỉ xem giờ/bấm giờ, quạt điện điều khiển từ xa hồng ngoại thông thường, bóng đèn sợi đốt/LED thường, đầu đĩa DVD cũ $arrow.r$ vì chúng *không có hệ điều hành/khả năng tự thích ứng ngữ cảnh* và *không kết nối mạng trao đổi dữ liệu*.
  - *LÀ thiết bị thông minh:* Điện thoại thông minh, máy tính bảng, đồng hồ thông minh (Smartwatch đo nhịp tim đồng bộ điện thoại), robot hút bụi tự vẽ bản đồ laser & điều khiển qua App, camera AI nhận diện khuôn mặt báo động qua Internet.
]

*2. Vai trò của thiết bị thông minh trong Cuộc cách mạng công nghiệp lần thứ tư (CMCN 4.0) và Kinh tế tri thức*

- *4 cuộc Cách mạng công nghiệp trong lịch sử nhân loại:*
  + *CMCN 1.0 (cuối TK XVIII):* Cơ khí hóa với *động cơ hơi nước*.
  + *CMCN 2.0 (cuối TK XIX – đầu TK XX):* Sản xuất hàng loạt dựa trên *điện năng* và dây chuyền lắp ráp.
  + *CMCN 3.0 (từ thập niên 1970):* Tự động hóa sản xuất dựa trên *máy tính điện tử, điện tử và CNTT*.
  + *CMCN 4.0 (đầu TK XXI đến nay):* Hệ thống sản xuất thông minh kết nối thế giới thực – thế giới số – thế giới sinh học, dựa trên các công nghệ trụ cột: *Internet vạn vật (IoT)*, *Trí tuệ nhân tạo (AI)*, *Dữ liệu lớn (Big Data)*, *Điện toán đám mây (Cloud Computing)*, robot tự hành, công nghệ sinh học, in 3D...
- *Vai trò cốt lõi của thiết bị thông minh đối với CMCN 4.0 & Kinh tế tri thức:*
  + Là *tế bào nền tảng cấu thành mạng lưới IoT*: hàng tỉ cảm biến và thiết bị thông minh liên tục thu thập dữ liệu thời gian thực từ thế giới vật lí, truyền lên đám mây tạo thành nguồn *Dữ liệu lớn (Big Data)* để *AI* phân tích, tối ưu hóa và điều khiển tự động.
  + Là *công cụ lao động và tiêu dùng thiết yếu của Nền kinh tế tri thức* (nền kinh tế lấy *tri thức khoa học – công nghệ* làm động lực chủ yếu tạo ra của cải thay vì chỉ dựa vào tài nguyên thiên nhiên và lao động cơ bắp): giúp con người làm việc di động mọi lúc mọi nơi, thanh toán số, học tập suốt đời và sáng tạo giá trị mới.

*3. Các mốc thời gian & Thành tựu nổi bật trong lịch sử phát triển ngành Tin học*

#set text(size: 8.5pt)
#table(
  columns: (0.95fr, 1.35fr, 1.7fr),
  inset: (x: 5.5pt, y: 5pt),
  stroke: 0.5pt + c-border,
  fill: (col, row) => if row == 0 { c-navy.lighten(88%) } else if calc.odd(row) { white } else { c-bg-soft },
  align: (center + horizon, left + horizon, left + top),

  table.header(
    [*Mốc thời gian*], [*Thành tựu / Cột mốc tiêu biểu*], [*Ý nghĩa lịch sử đối với ngành Tin học & Xã hội*],
  ),
  [*1936*], [Mô hình *Máy Turing* _(Alan Turing)_], [Đặt nền móng lí thuyết toán học cho máy tính điện tử đa năng hiện đại.],
  [*1945 – 1946*], [Kiến trúc *Von Neumann* & Máy tính *ENIAC*], [Ra đời máy tính điện tử thế hệ 1 (đèn điện tử chân không) và nguyên lí chương trình lưu trữ trong bộ nhớ.],
  [*5 thế hệ\ máy tính*], [1: Đèn chân không (1945–1955) $arrow.r$ 2: Bán dẫn Transistor (1955–1965) $arrow.r$ 3: Mạch tích hợp IC (1965–1974) $arrow.r$ 4: Vi xử lí VLSI / PC (1974–1990) $arrow.r$ 5: ULSI & AI (1990–nay)], [Máy tính ngày càng thu nhỏ kích thước, giảm điện năng, giảm giá thành nhưng tăng tốc độ & dung lượng hàng triệu lần.],
  [*Thập niên\ 1950 – 1960*], [*Hệ điều hành* & *Ngôn ngữ lập trình bậc cao* _(FORTRAN 1957, COBOL...)_], [Giúp con người lập trình bằng câu lệnh gần ngôn ngữ tự nhiên và giao tiếp thuận tiện với máy tính (đặc biệt khi giao diện đồ họa GUI ra đời).],
  [*1969 & 1983*], [Mạng *ARPANET* (1969) & giao thức *TCP/IP* (1983)], [Khai sinh mạng *Internet* kết nối các mạng máy tính trên quy mô toàn cầu.],
  [*1990 – 1991\ & 1998*], [*World Wide Web (WWW)* _(Tim Berners-Lee)_ & Máy tìm kiếm *Google* (1998)], [Tạo cuộc cách mạng chia sẻ, duyệt siêu văn bản và tra cứu tri thức nhân loại dễ dàng cho mọi người dân.],
  [*Thập niên\ 2000*], [*Mạng xã hội* (Facebook 2004, YouTube 2005), *Smartphone* (iPhone 2007, Android 2008), *Điện toán đám mây*], [Đưa máy tính và Internet vào túi áo từng cá nhân; bùng nổ kết nối xã hội và dịch vụ trực tuyến di động.],
  [*1997, 2011,\ 2016 – nay*], [*Trí tuệ nhân tạo (AI)*: Deep Blue thắng cờ vua (1997), IBM Watson (2011), *AlphaGo* thắng cờ vây (2016), Robot Sophia, AI tạo sinh], [Máy tính có khả năng học máy, nhận diện giọng nói/hình ảnh, xử lí ngôn ngữ tự nhiên và hỗ trợ ra quyết định thông minh.],
)
#set text(size: 9.7pt)

*4. Năm đóng góp cơ bản của Tin học đối với xã hội (Kèm ví dụ cụ thể)*

+ *Quản lí xã hội và kinh tế hiện đại:* Tin học hóa quản lí nhà nước (*Chính phủ điện tử, Cổng Dịch vụ công Quốc gia, định danh điện tử VNeID*), quản lí ngân hàng, hàng không, bệnh viện, trường học (sổ điểm điện tử).
+ *Tự động hóa sản xuất và dịch vụ:* Dây chuyền robot lắp ráp ô tô, máy CNC, hệ thống thu phí tự động không dừng *ETC*, tưới tiêu nông nghiệp tự động.
+ *Giải quyết các bài toán khoa học – kĩ thuật quy mô lớn:* Siêu máy tính dự báo bão/biến đổi khí hậu, mô phỏng khí động học máy bay, giải mã bản đồ gen người, nghiên cứu vắc-xin và dược phẩm mới.
+ *Đổi mới toàn diện giáo dục, y tế, thương mại:* Học trực tuyến (*E-learning*, kho học liệu mở), khám chữa bệnh từ xa (*Telemedicine*), thương mại điện tử (*Shopee, Tiki...*), ngân hàng số (*Mobile Banking, QR Pay*).
+ *Thay đổi phương thức giao tiếp, làm việc và nâng cao đời sống văn hóa – giải trí:* Thư điện tử, gọi video xuyên quốc gia, làm việc từ xa, báo điện tử, truyền hình số, âm nhạc và điện ảnh kĩ thuật số.

=== BÀI 7. THỰC HÀNH SỬ DỤNG THIẾT BỊ SỐ THÔNG DỤNG (ĐƠN VỊ A.3)

- *Quy trình khởi động và tắt thiết bị số đúng kĩ thuật:*
  + *Khởi động:* Bấm nút nguồn (*Power*) để nạp hệ điều hành (Windows/macOS trên PC; Android/iOS trên điện thoại), sau đó xác thực mở khóa (mật khẩu, mã PIN, vân tay, khuôn mặt).
  + *Tắt máy an toàn:* Đóng các tệp đang làm việc (lưu dữ liệu) $arrow.r$ chọn lệnh *Shut down* (trên PC) hoặc *Tắt nguồn / Power off* bằng phần mềm. *Tuyệt đối tránh rút phích điện đột ngột* hoặc nhấn giữ cưỡng bức nút nguồn khi không bị treo máy vì dễ gây hỏng hệ thống tệp tin, lỗi hệ điều hành và giảm tuổi thọ ổ cứng.
  + *Phân biệt các chế độ nguồn:* *Sleep* (ngủ tạm thời, lưu trạng thái trên RAM, tốn rất ít điện, bật lại cực nhanh); *Hibernate* (ngủ đông, lưu trạng thái vào ổ cứng, ngắt hẳn điện); *Restart* (khởi động lại hoàn toàn để cập nhật phần mềm/khắc phục xung đột bộ nhớ).
- *Quản lí tệp (File) và thư mục (Folder) khoa học:*
  + Sử dụng *File Explorer* (trên Windows) hoặc ứng dụng *Tệp / Files* (trên Smartphone) để tổ chức cây thư mục phân cấp hợp lí theo môn học/chủ đề; thành thạo các thao tác tạo mới (`New`), đổi tên (`Rename`), sao chép (`Ctrl + C`), cắt/di chuyển (`Ctrl + X`), dán (`Ctrl + V`), tìm kiếm và nén/giải nén tệp (`.zip`, `.rar`).
  + *Nhận diện phần mở rộng tệp thông dụng:* Văn bản (`.txt`, `.docx`, `.pdf`); Bảng tính (`.xlsx`); Trình chiếu (`.pptx`); Hình ảnh (`.jpg`, `.png`, `.gif`, `.bmp`, `.svg`); Âm thanh (`.mp3`, `.wav`); Video (`.mp4`, `.avi`, `.mkv`); Chương trình thực thi trên Windows (`.exe`, `.msi` — *cần đặc biệt cảnh giác mã độc khi tải từ nguồn lạ!*).

=== CHUYÊN MỤC BỔ TRỢ TOÀN DIỆN CHỦ ĐỀ 1 SGK KẾT NỐI TRI THỨC (TÓM TẮT BÀI 3, 4, 5, 6)

#callout(title: "TÓM TẮT CỐT LÕI BÀI 3 – 6 GIÚP BAO QUÁT 100% CHƯƠNG TRÌNH SGK KẾT NỐI TRI THỨC", tone: "teal")[
  _Mặc dù Ma trận đề Giữa kì I Định hướng ICT tập trung kiểm tra trực tiếp vào Bài 1, Bài 2 và kĩ năng Bài 7 của Chủ đề 1, việc nắm gọn 4 ý cốt lõi của Bài 3, 4, 5, 6 giúp học sinh hiểu sâu bản chất số hóa dữ liệu trong máy tính:_
  - *Bài 3 — Dữ liệu văn bản:* Máy tính mã hóa kí tự bằng bảng mã. *Bảng mã ASCII* cổ điển dùng `7 bit` (128 kí tự, mở rộng `8 bit` = 1 Byte cho 256 kí tự tiếng Anh). *Bộ mã quốc tế Unicode* mã hóa thống nhất mọi ngôn ngữ thế giới (trong đó có *tiếng Việt có dấu*); phổ biến nhất là chuẩn *UTF-8* (dùng từ `1` đến `4 Byte` cho một kí tự; kí tự tiếng Anh chiếm `1 Byte`, kí tự tiếng Việt có dấu chiếm `2` hoặc `3 Byte`).
  - *Bài 4 — Hệ nhị phân và dữ liệu số nguyên:* Máy tính dùng hệ nhị phân (cơ số 2, gồm `0` và `1`) vì mạch điện tử có 2 trạng thái ổn định (có điện / không có điện).
    + *Đổi cơ số $2 arrow.r 10$:* Nhân từng chữ số với lũy thừa của $2$ theo vị trí từ phải sang trái (bắt đầu từ $2^0$). Ví dụ: $1101_2 = 1 dot 2^3 + 1 dot 2^2 + 0 dot 2^1 + 1 dot 2^0 = 8 + 4 + 0 + 1 = 13_(10)$.
    + *Đổi cơ số $10 arrow.r 2$:* Chia liên tiếp số nguyên dương cho $2$, viết các số dư theo thứ tự *từ dưới lên trên*. Ví dụ: $13 = 1101_2$. Quy tắc cộng nhị phân: $0+0=0$; $0+1=1$; $1+0=1$; $1+1=10_2$ (viết $0$ nhớ $1$).
  - *Bài 5 — Dữ liệu lôgic:* Chỉ nhận 2 giá trị *Đúng (`True` / `1`)* hoặc *Sai (`False` / `0`)*. Ba phép toán lôgic cơ bản: *`AND`* (Và — chỉ Đúng khi *cả hai cùng Đúng*); *`OR`* (Hoặc — Đúng khi *ít nhất một vế Đúng*); *`NOT`* (Phủ định — đảo Đúng thành Sai và ngược lại).
  - *Bài 6 — Dữ liệu âm thanh và hình ảnh:*
    + *Âm thanh số:* Biến đổi sóng âm liên tục thành dãy số qua *lấy mẫu* (tần số lấy mẫu cao & độ sâu bit lớn $arrow.r$ âm thanh trung thực hơn nhưng dung lượng lớn hơn; `.wav` không nén, `.mp3` nén có giảm bớt chi tiết).
    + *Hình ảnh số:* *Ảnh Bitmap* tạo bởi lưới *điểm ảnh (pixel)*; độ phân giải là tích số cột $times$ số hàng pixel (ví dụ `1920 x 1080`); hệ màu *RGB* `24-bit` dùng `3 Byte/pixel` (mỗi màu Đỏ – Lục – Lam `8 bit`) biểu diễn $2^(24) approx 16,7$ triệu màu. *Ảnh Vector* lưu bằng công thức hình học (như trong Inkscape — `.svg`), phóng to không bị vỡ răng cưa.
]

== 2.2. CHỦ ĐỀ 2 (CHỦ ĐỀ B): MẠNG MÁY TÍNH VÀ INTERNET

=== BÀI 8. MẠNG MÁY TÍNH TRONG CUỘC SỐNG HIỆN ĐẠI

*1. Khái niệm Mạng máy tính & So sánh Mạng cục bộ (LAN) với Mạng Internet*

- *Mạng máy tính:* Là hệ thống gồm hai hay nhiều máy tính và thiết bị số được kết nối với nhau bằng đường truyền vật lí (cáp xoắn đôi, cáp quang) hoặc không dây (sóng Wi-Fi, Bluetooth, 4G/5G, vệ tinh) tuân theo các giao thức truyền thông nhằm *trao đổi dữ liệu* và *dùng chung tài nguyên* (máy in, ổ đĩa mạng, phần mềm, kết nối Internet).
- *Bảng so sánh đối xứng 6 tiêu chí giữa Mạng LAN và Mạng Internet (Rất hay ra câu Thông hiểu & Đúng/Sai!):*

#set text(size: 8.6pt)
#table(
  columns: (1.0fr, 1.45fr, 1.55fr),
  inset: (x: 6pt, y: 5pt),
  stroke: 0.5pt + c-border,
  fill: (col, row) => if row == 0 { c-navy.lighten(88%) } else if calc.odd(row) { white } else { c-bg-soft },
  align: (left + horizon, left + top, left + top),

  [*Tiêu chí so sánh*], [*Mạng cục bộ — LAN _(Local Area Network)_*], [*Mạng Internet _(International Network)_*],
  [*1. Phạm vi địa lí*], [Nhỏ, hẹp: trong một phòng máy, một hộ gia đình, một tòa nhà, trường học, bệnh viện hoặc xí nghiệp.], [*Toàn cầu* (kết nối hàng triệu mạng máy tính và hàng tỉ thiết bị khắp các châu lục).],
  [*2. Quy mô kết nối*], [Từ vài thiết bị đến vài trăm thiết bị số nội bộ.], [Hàng tỉ máy tính, máy chủ, điện thoại và thiết bị IoT trên toàn thế giới.],
  [*3. Quyền sở hữu\ & Quản lí*], [*Thuộc quyền sở hữu riêng* và do một cá nhân, gia đình hoặc một cơ quan, tổ chức xác định tự quản lí.], [*Không thuộc quyền sở hữu của bất kì cá nhân, tổ chức hay quốc gia nào* (do các tổ chức chuẩn hóa quốc tế điều phối chung và các nhà mạng ISP vận hành từng phần).],
  [*4. Phương thức &\ Thiết bị kết nối*], [Kết nối trực tiếp qua cáp mạng LAN hoặc Wi-Fi nội bộ nhờ *Switch* (bộ chuyển mạch), *Access Point* (bộ thu phát Wi-Fi).], [Các mạng LAN/mạng thành phần kết nối qua *Router* (bộ định tuyến), đường trục cáp quang biển, vệ tinh của nhà cung cấp dịch vụ *ISP* (Viettel, VNPT, FPT...), dùng bộ giao thức chuẩn *TCP/IP*.],
  [*5. Chi phí sử dụng*], [Chủ sở hữu tự đầu tư thiết bị ban đầu, truyền dữ liệu nội bộ không mất cước thuê bao hàng tháng.], [Người dùng phải trả cước thuê bao kết nối cho nhà cung cấp dịch vụ Internet (*ISP*).],
  [*6. Độ an toàn &\ Bảo mật*], [Môi trường khép kín nội bộ nên *ít nguy cơ bị tấn công từ bên ngoài hơn* (nếu chưa nối ra Internet).], [Môi trường mở toàn cầu nên *tiềm ẩn nhiều nguy cơ* tấn công mạng, lừa đảo, mã độc nếu thiếu biện pháp bảo vệ.],
)
#set text(size: 9.7pt)

*2. Điện toán đám mây (Cloud Computing)*

- *Khái niệm:* *Điện toán đám mây* là mô hình phân phối, cung cấp các tài nguyên và dịch vụ máy tính (máy chủ, bộ nhớ lưu trữ, cơ sở dữ liệu, mạng, phần mềm ứng dụng, công cụ trí tuệ nhân tạo...) *theo nhu cầu qua Internet*. Người dùng có thể truy cập sử dụng mọi lúc, mọi nơi trên nhiều thiết bị mà không cần tự đầu tư, lắp đặt hệ thống máy chủ phức tạp tại chỗ.
- *Ba loại hình dịch vụ Điện toán đám mây phổ biến (Theo SGK Kết nối tri thức Bài 8):*
  + *SaaS (`Software as a Service` — Phần mềm hướng dịch vụ):* Nhà cung cấp vận hành toàn bộ phần mềm trên đám mây; người dùng cuối chỉ cần mở trình duyệt web hoặc ứng dụng để sử dụng ngay.
    - *Ví dụ cụ thể rất quen thuộc:* Lưu trữ đám mây (*Google Drive, Microsoft OneDrive, Dropbox, iCloud*); Soạn thảo & văn phòng trực tuyến (*Google Docs, Google Sheets, Google Slides, Microsoft 365 Online, Canva*); Thư điện tử web (*Gmail, Outlook*); Họp & học trực tuyến (*Zoom, Google Meet, Microsoft Teams*).
  + *PaaS (`Platform as a Service` — Nền tảng hướng dịch vụ):* Cho thuê nền tảng môi trường phát triển ứng dụng (hệ điều hành, hệ quản trị CSDL, công cụ lập trình) để các nhà phát triển xây dựng và chạy phần mềm web mà không lo quản trị phần cứng. *Ví dụ:* Google App Engine, Heroku, Azure App Services.
  + *IaaS (`Infrastructure as a Service` — Hạ tầng hướng dịch vụ):* Cho thuê hạ tầng phần cứng ảo hóa cơ bản (máy chủ ảo VPS, dung lượng ổ đĩa, hạ tầng mạng); doanh nghiệp thuê tự cài hệ điều hành và phần mềm riêng. *Ví dụ:* Amazon Web Services (AWS EC2), Google Compute Engine, Viettel Cloud.
- *Lợi ích vượt trội của Điện toán đám mây:* Linh hoạt, tiện lợi (truy cập mọi nơi có Internet); đồng bộ và cộng tác nhóm theo thời gian thực (nhiều người cùng sửa 1 tệp Google Docs); tiết kiệm chi phí mua sắm và bảo trì phần cứng; độ tin cậy cao (dữ liệu vẫn an toàn trên mây ngay cả khi máy tính cá nhân bị hỏng ổ cứng hoặc thất lạc).

*3. Internet vạn vật (IoT — Internet of Things)*

- *Khái niệm:* *Internet vạn vật (IoT)* là hệ thống liên mạng kết nối các *đồ vật, thiết bị vật lí xung quanh ta* (xe cộ, thiết bị gia dụng, máy móc nông nghiệp, thiết bị y tế, đèn đường, camera...) được gắn *cảm biến (sensors)*, chip xử lí, phần mềm và kết nối mạng, giúp chúng *tự động thu thập, trao đổi dữ liệu với nhau qua Internet* và thực hiện hành động thông minh mà *ít cần (hoặc không cần) sự can thiệp trực tiếp liên tục của con người*.
- *Lợi ích và các ví dụ thực tiễn tiêu biểu của IoT làm thay đổi cuộc sống:*
  + *Nhà thông minh (Smart Home):* Điều hòa tự điều chỉnh nhiệt độ theo cảm biến phòng; đèn tự bật khi có người bước vào; bình nóng lạnh/nồi cơm/rèm cửa bật tắt từ xa qua điện thoại; cảm biến khói phát hiện cháy lập tức hú còi và gửi cảnh báo đến điện thoại chủ nhà.
  + *Giao thông thông minh (Smart Transportation):* Trạm thu phí tự động không dừng *ETC* nhận diện thẻ định danh dán trên ô tô giúp xe qua trạm không cần dừng trả tiền mặt, giảm ùn tắc; hệ thống đèn giao thông tự động điều chỉnh chu kì xanh – đỏ dựa trên mật độ phương tiện; định vị hành trình xe buýt thời gian thực.
  + *Nông nghiệp thông minh (Smart Agriculture):* Hệ thống cảm biến đo độ ẩm đất, nhiệt độ, ánh sáng trong nhà kính tự động kích hoạt van tưới nhỏ giọt và phun sương chính xác theo nhu cầu cây trồng, tiết kiệm nước và nhân công.
  + *Y tế thông minh (Smart Healthcare):* Thiết bị đeo thông minh theo dõi liên tục nhịp tim, huyết áp, nồng độ oxy máu của người cao tuổi, tự động báo động kèm vị trí GPS cho bác sĩ và gia đình khi phát hiện dấu hiệu bất thường.
- *Những thay đổi sâu sắc của xã hội khi mạng máy tính và Internet phổ biến:*
  + *Về phương thức học tập:* Chuyển từ học thụ động giới hạn trong lớp học sang *học tập mọi lúc, mọi nơi, học suốt đời* qua lớp học trực tuyến, thư viện số, thí nghiệm ảo và kho học liệu mở toàn cầu.
  + *Về phương thức làm việc:* Làm việc từ xa (*Work from home*), cộng tác nhóm xuyên biên giới, hội nghị truyền hình tiết kiệm thời gian và chi phí đi lại, hình thành nhiều nghề nghiệp số mới.
  + *Về chất lượng cuộc sống:* Mua sắm thương mại điện tử, thanh toán không tiền mặt, giải trí đa phương tiện theo yêu cầu, thực hiện thủ tục hành chính công trực tuyến ngay tại nhà.

=== BÀI 9. AN TOÀN TRÊN KHÔNG GIAN MẠNG

*1. Những nguy cơ và tác hại khi tham gia Internet bất cẩn, thiếu hiểu biết* _(Trọng tâm đánh dấu xanh trong Bản đặc tả)_

+ *Lây nhiễm phần mềm độc hại (Malware):* Làm máy tính chạy chậm, treo máy, hỏng hệ điều hành, bị xóa sạch hoặc bị mã hóa tống tiền toàn bộ dữ liệu quan trọng.
+ *Lừa đảo trực tuyến (Phishing/Scam) & Đánh cắp thông tin cá nhân, tài chính:* Tin tặc dùng trang web giả mạo ngân hàng/mạng xã hội, tin nhắn trúng thưởng, đường link bình chọn giả hoặc công nghệ *Deepfake* giả giọng nói/khuôn mặt người thân để chiếm đoạt tài khoản, mã OTP và tiền trong ngân hàng; rò rỉ dữ liệu cá nhân dẫn tới bị quấy rối hoặc mạo danh vay nợ.
+ *Tiếp nhận thông tin độc hại, giả mạo (Fake news), phản văn hóa:* Gây hoang mang tâm lí, lệch lạc nhận thức, lối sống hoặc bị lôi kéo vào các hành vi vi phạm pháp luật (cá độ, tín dụng đen, thử thách nguy hiểm).
+ *Bắt nạt trên không gian mạng (Cyberbullying):* Bị đe dọa, tung tin đồn vu khống, ghép ảnh chế giễu, công kích hội đồng trên mạng xã hội — diễn ra *24/7*, tốc độ lan truyền cực nhanh tới đám đông lớn và lưu vết lâu dài trên mạng, gây khủng hoảng tinh thần, trầm cảm nghiêm trọng cho nạn nhân.
+ *Nghiện Internet, mạng xã hội và trò chơi trực tuyến:* Lãng phí thời gian, sa sút học tập, suy giảm thị lực, cong vẹo cột sống, rối loạn giấc ngủ và thu hẹp giao tiếp lành mạnh ngoài đời thực.

*2. Phân biệt rõ các loại Phần mềm độc hại (Malware — Malicious Software)*

#set text(size: 8.5pt)
#table(
  columns: (0.95fr, 1.55fr, 1.5fr),
  inset: (x: 5.5pt, y: 5pt),
  stroke: 0.5pt + c-border,
  fill: (col, row) => if row == 0 { c-navy.lighten(88%) } else if calc.odd(row) { white } else { c-bg-soft },
  align: (left + horizon, left + top, left + top),

  [*Loại mã độc*], [*Cơ chế hoạt động & Lây lan đặc trưng*], [*Tác hại điển hình*],
  [*Virus máy tính*\ _(Computer Virus)_], [*Không phải chương trình độc lập*; phải *gắn (ký sinh)* đoạn mã độc vào một tệp chương trình/tài liệu hợp pháp. Chỉ kích hoạt và lây lan khi người dùng *mở/chạy tệp bị nhiễm*.], [Làm hỏng/xóa tệp tin, làm sai lệch hoạt động chương trình, chiếm tài nguyên làm treo máy.],
  [*Sâu máy tính*\ _(Worm)_], [Là *chương trình hoàn chỉnh độc lập*; có khả năng *tự nhân bản và tự động phát tán qua mạng* bằng cách khai thác lỗ hổng bảo mật mà *không cần gắn vào tệp khác* hay chờ người dùng kích hoạt.], [Làm tắc nghẽn băng thông mạng tốc độ cực nhanh, lây nhiễm hàng loạt máy tính trong mạng LAN/Internet.],
  [*Phần mềm nội gián*\ _(Trojan Horse — Ngựa thành Troa)_], [*Không tự nhân bản*, nhưng *ngụy trang* dưới vỏ bọc phần mềm hợp pháp hấp dẫn (game miễn phí, phần mềm "bẻ khóa" crack) để *lừa người dùng tự tải về và cài đặt*.], [*Mở cửa hậu (Backdoor)* cho tin tặc điều khiển máy từ xa, cài *Spyware* (gián điệp), *Keylogger* (ghi lén bàn phím lấy mật khẩu), *Adware* (quảng cáo độc hại).],
  [*Mã độc tống tiền*\ _(Ransomware)_], [Lây qua email lừa đảo, tệp đính kèm độc hại, lỗ hổng hệ thống hoặc Trojan tải về.], [*Mã hóa khóa chặt toàn bộ dữ liệu* của nạn nhân và hiển thị thông báo đòi trả tiền chuộc để lấy khóa giải mã.],
)
#set text(size: 9.7pt)

#callout(title: "MẸO GHI NHỚ SIÊU NHANH 3 LOẠI MÃ ĐỘC CƠ BẢN (SGK BÀI 9)", tone: "memo")[
  - *Virus* = *"Ký sinh tệp"* (phải bám vào tệp vật chủ + cần người dùng bấm chạy mới lây).
  - *Worm (Sâu)* = *"Độc lập tự bò qua mạng"* (tự nhân bản + tự chui qua lỗ hổng mạng không cần tệp vật chủ).
  - *Trojan (Ngựa gỗ)* = *"Giả dạng quà tặng mở cửa hậu"* (không tự nhân bản, lừa người dùng tự cài để rước gián điệp vào nhà).
]

*3. Biện pháp phòng tránh tác hại trên Internet, chống mã độc, tự bảo vệ dữ liệu & ứng phó bắt nạt qua mạng*

- *Công cụ và thói quen ngăn ngừa, loại bỏ phần mềm độc hại:*
  + Luôn bật *Tường lửa (Firewall)* của hệ điều hành và sử dụng *phần mềm diệt virus uy tín* (*Windows Security / Windows Defender* tích hợp sẵn trên Windows, *Kaspersky, Bitdefender, Norton, Bkav, Avast...*); thường xuyên cập nhật mẫu nhận diện virus mới và cập nhật bản vá bảo mật hệ điều hành, trình duyệt.
  + Không mở tệp đính kèm lạ (`.exe`, `.scr`, `.bat`, `.zip` không rõ nguồn) hoặc nhấp vào liên kết đáng ngờ trong email/tin nhắn; chỉ tải phần mềm từ trang chủ chính thức; *không dùng phần mềm bẻ khóa (crack)*; quét virus cho USB/ổ cứng ngoài trước khi mở tệp.
- *Nguyên tắc vàng tự bảo vệ dữ liệu cá nhân:*
  + Thiết lập *mật khẩu mạnh* (độ dài từ 8–12 kí tự trở lên, gồm chữ HOA, chữ thường, chữ số và kí tự đặc biệt như `@, #, !, $`; không đặt theo ngày sinh, tên riêng, `123456`); dùng mật khẩu khác nhau cho các tài khoản quan trọng.
  + Kích hoạt *Xác thực hai yếu tố (2FA)* và *tuyệt đối không tiết lộ mật khẩu hay mã OTP* cho bất kì ai (kể cả người tự xưng là nhân viên ngân hàng hay công an).
  + Cài đặt chế độ riêng tư trên mạng xã hội; hạn chế đăng công khai số CCCD, địa chỉ nhà, số điện thoại, vé máy bay có mã vạch; luôn *đăng xuất (Log out)* và không lưu mật khẩu khi dùng máy tính công cộng; sao lưu dữ liệu quan trọng định kì lên ổ cứng rời và đám mây.
- *Quy trình 4 bước phòng vệ chuẩn khi bị bắt nạt trên không gian mạng (Cyberbullying):*
  + *Bước 1 — Không đáp trả:* Giữ bình tĩnh, *không đôi co, chửi bới trả đũa* kẻ bắt nạt vì càng phản ứng tiêu cực càng khiến sự việc bị kích động, lan rộng.
  + *Bước 2 — Lưu giữ bằng chứng:* Chụp ảnh màn hình tin nhắn, bình luận ác ý, đường dẫn tài khoản và thời điểm diễn ra để làm bằng chứng xác thực.
  + *Bước 3 — Chặn và Báo cáo:* Sử dụng tính năng *Chặn (Block)* để ngắt liên lạc và *Báo cáo vi phạm (Report)* với nhà quản trị mạng xã hội để gỡ nội dung xấu.
  + *Bước 4 — Tìm kiếm sự trợ giúp tin cậy:* Kể ngay sự việc với *bố mẹ, thầy cô giáo chủ nhiệm, chuyên gia tư vấn tâm lí học đường*; nếu có hành vi vu khống nghiêm trọng, tống tiền hoặc đe dọa an toàn thân thể, cần trình báo ngay *cơ quan Công an* hoặc gọi *Tổng đài Quốc gia bảo vệ trẻ em `111`*.

=== BÀI 10. THỰC HÀNH KHAI THÁC TÀI NGUYÊN TRÊN INTERNET

- *Sử dụng công cụ xử lí ngôn ngữ & dịch tự động (Ví dụ: Google Dịch — `translate.google.com`):*
  + Hỗ trợ dịch nhanh giữa hơn 100 ngôn ngữ (Anh, Pháp, Trung, Nhật, Hàn... sang tiếng Việt và ngược lại) dưới nhiều hình thức đầu vào tiện lợi: *(1) Nhập văn bản trực tiếp*; *(2) Dịch tiếng nói / hội thoại trực tiếp qua Micro*; *(3) Dịch chữ trên hình ảnh tải lên hoặc soi Camera trực tiếp*; *(4) Dịch nguyên tệp tài liệu (`.docx`, `.pdf`, `.pptx`, `.xlsx`) giữ nguyên bố cục*; *(5) Dịch toàn bộ trang web qua địa chỉ URL*.
  + *Lưu ý khi sử dụng:* Công cụ dịch tự động dùng trí tuệ nhân tạo hỗ trợ nắm ý nhanh rất hiệu quả, nhưng người học cần *đọc hiểu, kiểm tra lại ngữ cảnh và thuật ngữ chuyên môn* thay vì sao chép máy móc.
- *Khai thác nguồn Học liệu mở trên Internet (OER — Open Educational Resources):*
  + *Khái niệm:* Học liệu mở là các tài liệu học tập, giảng dạy và nghiên cứu (sách điện tử, bài giảng video, mô phỏng thí nghiệm ảo, đề luyện tập, khóa học trực tuyến...) được cung cấp *miễn phí, công khai hợp pháp* với giấy phép mở cho phép người học truy cập, sử dụng để tự học và nâng cao trình độ.
  + *Các nguồn học liệu mở uy tín học sinh lớp 10 nên khai thác:* Hệ tri thức Việt số hóa & Kho học liệu số Bộ GD&ĐT (*`igiaoduc.vn`*), Hành trang số NXB Giáo dục Việt Nam (*`hanhtrangso.nxbgd.vn`*), *`olm.vn`*, *Khan Academy* (`vi.khanacademy.org`), *MIT OpenCourseWare*, các khóa học miễn phí trên *Coursera / edX*, thí nghiệm tương tác *PhET Colorado*.

== 2.3. CHỦ ĐỀ 3 (CHỦ ĐỀ D): ĐẠO ĐỨC, PHÁP LUẬT VÀ VĂN HÓA TRONG MÔI TRƯỜNG SỐ

=== BÀI 11. ỨNG XỬ TRÊN MÔI TRƯỜNG SỐ. NGHĨA VỤ TÔN TRỌNG BẢN QUYỀN

*1. Những vấn đề nảy sinh về đạo đức, văn hóa và pháp luật trong môi trường số*

Khi giao tiếp qua mạng trở nên phổ biến (phạm vi lan truyền rộng, tốc độ tức thời, tâm lí tưởng rằng mình đang "ẩn danh" sau màn hình), nhiều vấn đề tiêu cực đã nảy sinh:
- *Về văn hóa & đạo đức:* Sử dụng ngôn từ thiếu chuẩn mực, công kích cá nhân, nói tục chửi thề; vô cảm trước nỗi đau người khác hoặc cổ xúy trào lưu phản cảm; đăng ảnh/thông tin riêng tư của bạn bè, người khác khi chưa xin phép; gian lận học tập, đạo văn.
- *Về pháp luật:* Tung tin giả (*Fake news*) gây hoang mang dư luận; vu khống, xúc phạm danh dự, nhân phẩm cá nhân và uy tín tổ chức; xâm phạm bản quyền phần mềm, âm nhạc, điện ảnh, sách báo; lừa đảo chiếm đoạt tài sản, đánh bạc trực tuyến, phát tán mã độc, xâm nhập trái phép tài khoản và cơ sở dữ liệu.

*2. Các văn bản pháp luật trọng tâm điều chỉnh hành vi trong môi trường số tại Việt Nam*

#callout(title: "TÓM TẮT HỆ THỐNG PHÁP LUẬT CỐT LÕI CẦN NHỚ ĐỂ LÀM CÂU TỰ LUẬN VẬN DỤNG CAO", tone: "law")[
  + *Luật Công nghệ thông tin (Luật số 67/2006/QH11 — trọng tâm Điều 12 về các hành vi bị nghiêm cấm):*
    - Nghiêm cấm cung cấp, trao đổi, truyền đưa, lưu trữ, sử dụng thông tin số nhằm: chống Nhà nước CHXHCN Việt Nam, phá hoại khối đại đoàn kết toàn dân; kích động bạo lực, tuyên truyền chiến tranh xâm lược, gây hận thù giữa các dân tộc; *xuyên tạc, vu khống, xúc phạm uy tín của tổ chức, danh dự, nhân phẩm, uy tín của công dân*; quảng bá đồi trụy, tệ nạn xã hội, mê tín dị đoan, phá hoại thuần phong mỹ tục.
    - Nghiêm cấm *xâm phạm quyền sở hữu trí tuệ* trong hoạt động CNTT; giả mạo trang thông tin điện tử của tổ chức, cá nhân khác; tạo ra và cài đặt chương trình virus máy tính hoặc phần mềm gây hại.
  + *Luật An ninh mạng (Luật số 24/2018/QH14 — trọng tâm Điều 8, Điều 16, 17, 18, 26, 29):*
    - Nghiêm cấm sử dụng không gian mạng để đăng tải, phát tán *thông tin sai sự thật gây hoang mang trong Nhân dân*, gây thiệt hại cho hoạt động kinh tế – xã hội, gây khó khăn cho hoạt động của cơ quan nhà nước hoặc người thi hành công vụ; *xúc phạm nghiêm trọng danh dự, uy tín, nhân phẩm của người khác*.
    - Nghiêm cấm chiếm đoạt tài sản, tổ chức đánh bạc qua mạng, gián điệp mạng, tấn công mạng, phát tán mã độc, thu thập/mua bán trái phép thông tin cá nhân; bảo vệ quyền của trẻ em trên không gian mạng.
  + *Nghị định quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng & Nghị định xử phạt vi phạm hành chính:*
    - *Nghị định số 72/2013/NĐ-CP* (sửa đổi bởi Nghị định 27/2018/NĐ-CP và cập nhật bởi Nghị định 147/2024/NĐ-CP): Quy định rõ quyền và nghĩa vụ của người sử dụng mạng xã hội — phải *chịu trách nhiệm về nội dung thông tin do mình lưu trữ, cung cấp, truyền đưa trên mạng xã hội*, bảo vệ bí mật nhà nước, bí mật đời tư và tuân thủ quy định về bản quyền.
    - *Nghị định số 15/2020/NĐ-CP* (sửa đổi bổ sung bởi Nghị định 14/2022/NĐ-CP — đặc biệt *Điều 101*): Quy định xử phạt vi phạm hành chính cụ thể đối với hành vi lợi dụng mạng xã hội để cung cấp, chia sẻ thông tin giả mạo, thông tin sai sự thật, xuyên tạc, vu khống, xúc phạm uy tín cơ quan, tổ chức, danh dự, nhân phẩm của cá nhân; chia sẻ thông tin cổ súy hủ tục, mê tín, dâm ô, bạo lực; tiết lộ bí mật đời tư cá nhân (mức phạt tiền từ 10–20 triệu đồng đối với tổ chức, *5–10 triệu đồng đối với cá nhân*, buộc gỡ bỏ thông tin sai phạm).
  + *Luật Sở hữu trí tuệ (Luật số 50/2005/QH11, sửa đổi bổ sung 2009, 2019, 2022):* Bảo hộ *Quyền tác giả (Bản quyền — Copyright)* đối với các tác phẩm văn học, nghệ thuật, khoa học, bao gồm cả *chương trình máy tính (phần mềm)* và *sưu tập dữ liệu*.
]

*3. Bản quyền thông tin và sản phẩm số — Khía cạnh pháp lí & Hệ lụy khi vi phạm* _(Trọng tâm đánh dấu ĐỎ trong Bản đặc tả)_

- *Hai nhóm quyền thuộc Quyền tác giả (theo Luật Sở hữu trí tuệ):*
  + *Quyền nhân thân:* Quyền đặt tên cho tác phẩm; đứng tên thật hoặc bút danh trên tác phẩm (*được nêu tên khi tác phẩm được trích dẫn, sử dụng*); công bố hoặc cho phép người khác công bố tác phẩm; *bảo vệ sự toàn vẹn của tác phẩm* (cấm người khác tự ý sửa chữa, cắt xén, xuyên tạc gây phương hại đến danh dự, uy tín tác giả).
  + *Quyền tài sản:* Quyền làm tác phẩm phái sinh (dịch, chuyển thể, cải biên); biểu diễn trước công chúng; *sao chép tác phẩm*; *phân phối, truyền đạt tác phẩm đến công chúng qua mạng viễn thông và môi trường kĩ thuật số*; cho thuê bản gốc hoặc bản sao chương trình máy tính, bản ghi âm, ghi hình. Tác giả/chủ sở hữu quyền tác giả được hưởng nhuận bút, thù lao và lợi ích vật chất hợp pháp từ các quyền này.
- *Nhận diện các hành vi VI PHẠM bản quyền thông tin và sản phẩm số điển hình:*
  + Tải, cài đặt, sử dụng hoặc chia sẻ công cụ *bẻ khóa (crack, keygen, patch)* phần mềm thương mại có bản quyền mà không mua giấy phép sử dụng (License).
  + Quay lén phim đang chiếu tại rạp (*camrip / livestream*) rồi đăng lên mạng xã hội câu lượt xem; tải sách điện tử (ebook), khóa học trả phí, bản nhạc có bản quyền rồi tự ý nhân bản chia sẻ công khai hoặc rao bán thu lợi bất chính.
  + Sao chép nguyên văn bài viết, bức ảnh nghệ thuật, video, đoạn mã nguồn của người khác rồi đăng dưới tên mình (*đạo văn — Plagiarism*) hoặc sử dụng thương mại mà không xin phép chủ sở hữu.
  + Mua 1 tài khoản/1 giấy phép phần mềm chỉ dành cho 1 máy cá nhân nhưng tự ý bẻ giới hạn cài cho cả phòng máy kinh doanh trái thỏa thuận cấp phép (*EULA*).
- *Các hành vi HỢP PHÁP không xâm phạm bản quyền:*
  + Trích dẫn hợp lí một phần nhỏ tác phẩm để bình luận, minh họa trong bài viết/học tập của mình mà không làm sai ý tác giả và *có ghi rõ tên tác giả, nguồn gốc tác phẩm*.
  + Sử dụng các *phần mềm nguồn mở / phần mềm miễn phí* (như LibreOffice, Inkscape, GIMP, Python, trình duyệt Firefox...) hoặc các tư liệu phát hành theo giấy phép mở *Creative Commons (CC)* đúng điều kiện ghi công của tác giả.
- *Hậu quả của hành vi vi phạm bản quyền và chia sẻ thông tin bất cẩn:*
  + *Về kinh tế – xã hội:* Gây thiệt hại doanh thu nghiêm trọng cho tác giả và doanh nghiệp sản xuất phần mềm/nội dung số, làm triệt tiêu động lực sáng tạo trí tuệ; chia sẻ tin giả gây hoang mang xã hội, thiệt hại kinh tế cho người dân và doanh nghiệp bị vu khống.
  + *Về pháp lí & an toàn cá nhân:* Người vi phạm bị buộc gỡ bỏ nội dung, khóa tài khoản, *xử phạt hành chính bằng tiền*, *buộc bồi thường thiệt hại dân sự*, thậm chí bị *truy cứu trách nhiệm hình sự* nếu gây hậu quả nghiêm trọng hoặc thu lợi bất chính lớn; mặt khác máy tính cài phần mềm crack rất dễ bị nhiễm *Trojan, Spyware, Ransomware*.

*4. Biện pháp nâng cao tính an toàn, văn hóa và hợp pháp khi chia sẻ thông tin trong môi trường số*

#callout(title: "QUY TẮC VÀNG KHI CHIA SẺ THÔNG TIN TRÊN MẠNG (DỄ THUỘC — ĐỦ Ý CHẤM ĐIỂM)", tone: "teal")[
  + *Kiểm chứng trước khi chia sẻ (Nguyên tắc 5 câu hỏi `THINK`):* Trước khi đăng bài hay nhấn nút *Share*, hãy tự hỏi thông tin đó có: *`T`rue* (Đúng sự thật, có nguồn chính thống kiểm chứng không?) — *`H`elpful* (Có ích không?) — *`I`nspiring* (Tích cực, lành mạnh không?) — *`N`ecessary* (Cần thiết không?) — *`K`ind* (Tử tế, có xúc phạm hay xâm phạm đời tư ai không?).
  + *Tôn trọng bản quyền tuyệt đối:* Xin phép chủ sở hữu trước khi đăng tải lại tác phẩm có bản quyền; luôn *ghi rõ tên tác giả và nguồn trích dẫn*; ưu tiên sử dụng phần mềm có bản quyền hợp pháp hoặc phần mềm nguồn mở, kho tư liệu giấy phép mở Creative Commons.
  + *Bảo vệ quyền riêng tư của mình và người khác:* Không tự ý đăng ảnh mặt, thông tin cá nhân, bảng điểm, tin nhắn riêng của người khác khi chưa được họ đồng ý; phân quyền chia sẻ phù hợp (Chỉ mình tôi / Bạn bè thay vì Công khai tràn lan).
  + *Tuân thủ Bộ Quy tắc ứng xử trên mạng xã hội (Quyết định 874/QĐ-BTTTT):* Ứng xử văn minh, lịch sự, thượng tôn pháp luật (*Tôn trọng, tuân thủ pháp luật — Lành mạnh — An toàn, bảo mật thông tin — Trách nhiệm*).
]
