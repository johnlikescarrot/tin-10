#import "template.typ": *

= Phần II. Hệ thống hóa lý thuyết trọng tâm & Mẹo ghi nhớ nhanh

== Chủ đề A. Máy tính và xã hội tri thức (4,0 điểm – 40% đề thi)

=== Đơn vị kiến thức A.1. Dữ liệu, thông tin và xử lí thông tin _(Bài 1 – SGK Kết nối tri thức)_

#concept-box(title: "1. Phân biệt Thông tin – Dữ liệu – Vật mang tin – Tri thức")[
  - *Thông tin (Information):* Là tất cả những gì mang lại cho con người *sự hiểu biết, nhận thức* về thế giới xung quanh (sự vật, sự kiện, hiện tượng) và về chính bản thân mình.
  - *Dữ liệu (Data):* Là các con số, văn bản, hình ảnh, âm thanh,... dùng để *biểu diễn thông tin*. Trong tin học, *dữ liệu là thông tin đã được đưa vào máy tính* (mã hóa thành dãy bit nhị phân `0` và `1`) để máy tính nhận biết và xử lí được.
  - *Vật mang tin (Storage/Carrier Medium):* Là *phương tiện vật lí* dùng để lưu trữ và truyền tải dữ liệu (ví dụ: trang giấy, tấm biển báo, đĩa CD, thẻ nhớ, ổ cứng, USB,...).
  - *Mối quan hệ cốt lõi:* Từ *Dữ liệu* $arrow.r$ qua tiếp nhận và xử lí tạo ra *Thông tin* $arrow.r$ đúc kết, khái quát hóa thành *Tri thức* (hiểu biết tích lũy có thể áp dụng giải quyết vấn đề mới).
]

#table(
  columns: (0.9fr, 1.35fr, 1.35fr, 1.4fr),
  inset: 6pt,
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  [*Tình huống thực tế*], [*Vật mang tin* _(Phương tiện)_], [*Dữ liệu* _(Hình thức biểu diễn)_], [*Thông tin* _(Ý nghĩa rút ra)_],
  [Xem dự báo thời tiết trên điện thoại], [Điện thoại thông minh (bộ nhớ/màn hình)], [Con số `36°C`, kí hiệu đám mây mưa, chữ `"Chiều tối mưa rào"`], [Biết hôm nay trời nắng nóng và chiều có mưa để chuẩn bị áo mưa khi ra ngoài.],
  [Bảng điểm học kì dán trên bảng tin], [Tờ giấy in trên bảng tin lớp], [Các chữ cái tên học sinh và các con số `8.5`, `9.0`, `7.8`,...], [Biết kết quả học tập, thứ hạng và môn nào cần cố gắng hơn.],
  [Đèn tín hiệu giao thông ở ngã tư], [Cột đèn tín hiệu giao thông], [Ánh sáng màu đỏ và con số đếm ngược `25`], [Biết phải dừng phương tiện trước vạch kẻ đường thêm 25 giây.],
  [Tệp bài giảng lưu trong USB], [Thiết bị nhớ USB], [Các tệp văn bản `.docx`, hình ảnh `.jpg`, âm thanh `.mp3`], [Nội dung bài học mà học sinh hiểu được sau khi mở và đọc/nghe.],
)

#tip-box(title: "Mẹo phân biệt cực nhanh không bao giờ nhầm trong câu Trắc nghiệm")[
  - Hỏi *cái cầm nắm được / nơi chứa* (tờ giấy, ổ cứng, USB, thẻ nhớ, đĩa quang) $arrow.r$ chọn *Vật mang tin*.
  - Hỏi *con số, dòng chữ, bức ảnh, đoạn âm thanh, tệp tin trong máy tính* $arrow.r$ chọn *Dữ liệu*.
  - Hỏi *ý nghĩa, sự hiểu biết, điều rút ra để ra quyết định* $arrow.r$ chọn *Thông tin*.
  - *Tính chất quan trọng:* Cùng một thông tin có thể biểu diễn bằng nhiều dạng dữ liệu khác nhau; ngược lại, từ cùng một bộ dữ liệu, những người có trình độ/mục đích khác nhau có thể rút ra những thông tin khác nhau.
]

*2. Quá trình xử lí thông tin bằng máy tính (Thiết bị số):*
Quá trình xử lí thông tin của máy tính gồm *4 hoạt động cơ bản* liên kết chặt chẽ:
#align(center)[
  #block(
    width: 96%,
    fill: c-bg-soft,
    stroke: 0.7pt + c-teal,
    radius: 5pt,
    inset: 8pt,
    breakable: false,
    [
      *1. Tiếp nhận dữ liệu vào (Input)* _(Bàn phím, chuột, micro, camera, cảm biến)_ $arrow.r$ *2. Xử lí dữ liệu (Processing)* _(Bộ xử lí trung tâm CPU biến đổi dữ liệu thành thông tin mới)_ $arrow.r$ *3. Đưa thông tin ra (Output)* _(Màn hình, loa, máy in)_ \
      $arrow.t.b$ *4. Lưu trữ dữ liệu (Storage)* _(RAM, ổ cứng HDD/SSD, thẻ nhớ, đám mây – diễn ra xuyên suốt quá trình)_
    ],
  )
]

*3. Sự ưu việt của việc lưu trữ, xử lí và truyền thông tin trên thiết bị số:* _(Trọng tâm Nhận biết)_
1. *Dung lượng lưu trữ khổng lồ trong kích thước nhỏ gọn:* Một thẻ nhớ/ổ cứng nhỏ gọn có thể chứa hàng trăm nghìn cuốn sách, hàng chục nghìn bức ảnh hay hàng trăm giờ video chất lượng cao.
2. *Tốc độ xử lí cực nhanh và độ chính xác cao:* Máy tính thực hiện hàng tỉ phép tính mỗi giây, làm việc liên tục, bền bỉ, không bị mệt mỏi hay sai sót cảm tính như con người.
3. *Tìm kiếm và truy xuất tức thời:* Chỉ mất vài phần giây để tìm đúng một từ khóa hay một tệp tin giữa kho dữ liệu khổng lồ.
4. *Dễ dàng sao chép, chỉnh sửa và bảo quản lâu dài:* Sao lưu bản sao nguyên vẹn 100%, không bị ố vàng, mối mọt như giấy truyền thống; chi phí lưu trữ tính trên mỗi đơn vị dữ liệu rất rẻ.
5. *Truyền tải thông tin siêu tốc trên phạm vi toàn cầu:* Gửi tệp, hình ảnh, âm thanh qua mạng máy tính/Internet gần như tức thời tới bất kì đâu trên thế giới.

*4. Các đơn vị lưu trữ dữ liệu & Bài toán chuyển đổi đơn vị:* _(Trọng tâm Tự luận Vận dụng – 1,0 điểm)_
- Đơn vị nhỏ nhất để biểu diễn và lưu trữ dữ liệu trong máy tính là *bit* (ký hiệu *b*, viết tắt của _binary digit_), chỉ nhận một trong hai giá trị `0` hoặc `1`.
- Đơn vị đo lượng dữ liệu cơ bản là *Byte* (ký hiệu *B* viết hoa): *$1 "Byte (B)" = 8 "bit (b)"$*.
- Bảng các đơn vị bội số chuẩn trong Tin học (theo hệ nhị phân cơ số 2, SGK _Kết nối tri thức_ Bảng 1.1):

#table(
  columns: (0.9fr, 1.2fr, 1.3fr, 1.6fr),
  inset: 5.5pt,
  align: (center + horizon, left + horizon, center + horizon, left + horizon),
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  [*Ký hiệu*], [*Tên gọi đầy đủ*], [*Giá trị quy đổi chuẩn*], [*Ví dụ ước lượng thực tế dễ nhớ*],
  [*b* _(chữ thường)_], [Bit _(Binary digit)_], [Đơn vị nhỏ nhất (`0` hoặc `1`)], [Trạng thái bật/tắt của 1 bóng đèn/công tắc điện.],
  [*B* _(chữ hoa)_], [Byte], [*$1 "B" = 8 "bit"$*], [1 kí tự tiếng Anh không dấu (mã ASCII) tốn 1 Byte.],
  [*KB*], [Kilobyte], [*$1 "KB" = 1024 "B" = 2^(10) "B"$*], [Khoảng nửa trang văn bản thuần chữ (~500 từ).],
  [*MB*], [Megabyte], [*$1 "MB" = 1024 "KB" = 2^(20) "B"$*], [1 bức ảnh chụp điện thoại (3–5 MB) hoặc 1 bài hát MP3 (4 MB).],
  [*GB*], [Gigabyte], [*$1 "GB" = 1024 "MB" = 2^(30) "B"$*], [1 bộ phim chuẩn Full HD dài ~1,5–2 giờ (2–4 GB).],
  [*TB*], [Terabyte], [*$1 "TB" = 1024 "GB" = 2^(40) "B"$*], [Ổ cứng máy tính cá nhân thông dụng (512 GB – 2 TB).],
  [*PB*], [Petabyte], [*$1 "PB" = 1024 "TB" = 2^(50) "B"$*], [Kho dữ liệu của các trung tâm dữ liệu đám mây lớn.],
)

#formula-box(title: "Quy tắc đổi đơn vị & Công thức giải bài toán dung lượng – truyền tin")[
  - *Thang đo liền kề:* $"Byte (B)" arrow.l.r^(1024) "KB" arrow.l.r^(1024) "MB" arrow.l.r^(1024) "GB" arrow.l.r^(1024) "TB" arrow.l.r^(1024) "PB"$ _(riêng $"B" arrow.l.r^(8) "bit"$!)_
  - *Đổi từ đơn vị LỚN sang đơn vị NHỎ:* *NHÂN* với $1024$ cho mỗi bậc nhảy _(VD: $3 "GB" = 3 times 1024 = 3072 "MB"$)._
  - *Đổi từ đơn vị NHỎ sang đơn vị LỚN:* *CHIA* cho $1024$ cho mỗi bậc nhảy _(VD: $2048 "KB" = 2048 : 1024 = 2 "MB"$)._
  - *Số lượng tệp tối đa lưu được* $= "Phần nguyên của" lr((frac("Dung lượng trống của thiết bị nhớ", "Dung lượng 1 tệp")), size: #100%)$ _(phải đưa về *cùng một đơn vị đo* trước khi chia!)_.
  - *Thời gian truyền tệp qua mạng* $= frac("Dung lượng tệp", "Tốc độ truyền thực tế")$ _(chú ý đổi tốc độ mạng từ *bit/s* sang *Byte/s* bằng cách *chia cho 8*: $1 "MB/s" = 8 "Mbps"$ khi quy đổi theo thang tương ứng)_.
]

#warn-box(title: "2 Bẫy cực hay mất điểm ở câu Tự luận đổi đơn vị")[
  1. *Nhầm chữ `b` thường (bit) và chữ `B` hoa (Byte):* $1 "Byte" = 8 "bit"$. Nhà mạng thường ghi tốc độ đường truyền là `80 Mbps` (*Megabit trên giây*), tức tốc độ tải thực tế tính theo Megabyte/giây là $80 : 8 = 10 "MB/giây"$.
  2. *Quên lấy phần nguyên khi tính số tệp/bức ảnh/video:* Số lượng tệp tin hoàn chỉnh lưu được luôn phải là *số nguyên dương* (làm tròn xuống phần nguyên, phần dư không đủ chứa thêm 1 tệp trọn vẹn).
]

#example-box(title: "Bài giải mẫu chuẩn thang điểm Tự luận Vận dụng (1,0 điểm)")[
  *Đề bài:* Một thẻ nhớ có dung lượng khả dụng là `16 GB`. Bạn An đã lưu trong thẻ nhớ đó một đoạn video bài giảng nặng `2 GB`, phần dung lượng trống còn lại bạn dùng để lưu các bức ảnh kỉ niệm (mỗi bức ảnh có dung lượng trung bình `4 MB`).
  a) Hỏi phần dung lượng trống còn lại của thẻ nhớ là bao nhiêu `MB`?
  b) Bạn An có thể lưu thêm tối đa bao nhiêu bức ảnh vào thẻ nhớ đó?

  *Lời giải trình bày mẫu:*
  - *a)* Dung lượng trống còn lại của thẻ nhớ tính theo đơn vị `GB` là: $16 - 2 = 14 " (GB)"$. \
    Đổi sang đơn vị `MB` (với $1 "GB" = 1024 "MB"$): $14 times 1024 = 14.336 " (MB)"$.
  - *b)* Số bức ảnh tối đa bạn An có thể lưu thêm vào phần dung lượng trống đó là: \
    $14.336 : 4 = 3.584 " (bức ảnh)"$.
]

=== Đơn vị kiến thức A.2. Vai trò của máy tính và thiết bị thông minh trong nền kinh tế tri thức _(Bài 2 – SGK)_

#concept-box(title: "1. Thiết bị số thông dụng & Thiết bị thông minh (Smart Devices)")[
  - *Một số thiết bị số thông dụng ngoài PC và Laptop:* Điện thoại thông minh (*Smartphone*), máy tính bảng (*Tablet*), đồng hồ thông minh (*Smartwatch*), tivi thông minh (*Smart TV*), máy ảnh kĩ thuật số, thiết bị đọc sách điện tử (*E-reader*), loa thông minh, robot hút bụi thông minh, camera an ninh AI,...
  - *Khái niệm Thiết bị thông minh:* Là thiết bị điện tử có thể *hoạt động một cách tự chủ* ở mức độ nhất định nhờ *phần mềm điều khiển cài sẵn*, có *khả năng kết nối mạng* (Wi-Fi, 4G/5G, Bluetooth,...) để trao đổi dữ liệu với các thiết bị khác hoặc người dùng, và có khả năng *hỗ trợ/tương tác thông minh theo ngữ cảnh*.
]

#table(
  columns: (1.2fr, 1.9fr, 1.9fr),
  inset: 6pt,
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  [*Tiêu chí đối chiếu*], [*Thiết bị thông minh* _(Smart Device)_], [*Thiết bị điện tử / số thông thường*],
  [*Khả năng xử lí & phần mềm*], [Có bộ vi xử lí, hệ điều hành/phần mềm thông minh, có thể cài thêm ứng dụng hoặc tự thích ứng.], [Chỉ thực hiện chức năng cố định theo mạch điện tử định sẵn, không tự học hay mở rộng chức năng.],
  [*Khả năng kết nối*], [Kết nối không dây/có dây (Internet, Wi-Fi, Bluetooth, 4G/5G) để đồng bộ và trao đổi dữ liệu.], [Thường hoạt động độc lập, không có khả năng kết nối mạng trao đổi dữ liệu tự động.],
  [*Ví dụ điển hình* \ _(Rất hay hỏi Đúng/Sai!)_], [*Smartphone, Tablet, Smartwatch, Smart TV, Robot hút bụi tự vẽ bản đồ, Camera AI nhận diện khuôn mặt.*], [*Máy tính bỏ túi Casio cơ bản, đồng hồ điện tử chỉ xem giờ, quạt điện cơ, ấm siêu tốc thường, USB.*],
)

*2. Vì sao các thiết bị thông minh cũng là những hệ thống xử lí thông tin?* _(Yêu cầu Thông hiểu trọng tâm)_
Bởi vì mỗi thiết bị thông minh thực chất là một *máy tính thu nhỏ*, có đầy đủ *4 thành phần/hoạt động* của một hệ thống xử lí thông tin hoàn chỉnh:
- *Đầu vào (Input):* Thu nhận dữ liệu trực tiếp qua màn hình cảm ứng, micro, camera hoặc các *cảm biến* (nhịp tim, nhiệt độ, gia tốc, khoảng cách,...).
- *Xử lí (Processing):* Có chip vi xử lí (CPU/SoC) và hệ điều hành, phần mềm xử lí dữ liệu thu được.
- *Lưu trữ (Storage):* Có bộ nhớ trong (RAM, ROM/Flash) để lưu hệ điều hành, ứng dụng và dữ liệu người dùng.
- *Đầu ra (Output) & Truyền thông:* Hiển thị kết quả qua màn hình, phát âm thanh qua loa, rung cảnh báo, điều khiển cơ cấu chấp hành hoặc gửi dữ liệu qua mạng tới thiết bị khác.

*3. Vai trò đối với sự phát triển xã hội, CMCN 4.0 và Kinh tế tri thức:*
- *Kinh tế tri thức:* Là nền kinh tế trong đó *tri thức là yếu tố quan trọng nhất* quyết định sự phát triển, tạo ra giá trị gia tăng và của cải vật chất. Máy tính, mạng Internet và thiết bị thông minh là *công cụ then chốt* để thu thập dữ liệu, sáng tạo, phổ biến và khai thác tri thức.
- *Cách mạng công nghiệp lần thứ tư (CMCN 4.0):* Dựa trên sự hội tụ của công nghệ số (*IoT, Trí tuệ nhân tạo AI, Dữ liệu lớn Big Data, Điện toán đám mây*). Thiết bị thông minh đóng vai trò là *"giác quan" và "cánh tay nối dài"* kết nối thế giới thực với không gian số, thúc đẩy nhà máy thông minh, nông nghiệp thông minh, giao thông thông minh, y tế số và đô thị thông minh.

*4. Những đóng góp cơ bản của Tin học đối với xã hội:*
1. *Quản lí và tự động hóa:* Tin học hóa quản lí nhà nước (Chính phủ điện tử, dịch vụ công trực tuyến VNeID), quản lí doanh nghiệp, ngân hàng, hàng không, dây chuyền sản xuất tự động.
2. *Giải quyết các bài toán khoa học – kĩ thuật lớn:* Dự báo thời tiết, mô phỏng khí hậu, giải mã gen, thiết kế tàu vũ trụ, cầu đường, kiến trúc.
3. *Giáo dục và đào tạo:* Học trực tuyến (*E-learning*), lớp học thông minh, thư viện số, phần mềm mô phỏng thí nghiệm ảo, kho học liệu mở.
4. *Y tế và chăm sóc sức khỏe:* Hồ sơ sức khỏe điện tử, khám chữa bệnh từ xa (*Telemedicine*), chẩn đoán hình ảnh hỗ trợ bởi AI, thiết bị y tế đeo tay theo dõi bệnh nhân.
5. *Kinh tế – Thương mại – Tài chính:* Thương mại điện tử (*Shopee, Tiki,...*), ngân hàng số (*Mobile Banking*), thanh toán không dùng tiền mặt (QR Code, ví điện tử).
6. *Giao tiếp và đời sống văn hóa – giải trí:* Thư điện tử, mạng xã hội, gọi video xuyên biên giới, báo điện tử, âm nhạc/phim trực tuyến, nâng cao chất lượng sống.

*5. Niên biểu các mốc thành tựu nổi bật minh họa sự phát triển của ngành Tin học:* _(SGK Kết nối tri thức – Bài 2)_

#table(
  columns: (0.85fr, 1.35fr, 2.8fr),
  inset: 5.5pt,
  align: (center + horizon, left + horizon, left + horizon),
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  [*Mốc thời gian*], [*Thành tựu / Sự kiện tiêu biểu*], [*Ý nghĩa nổi bật đối với sự phát triển Tin học & Xã hội*],
  [*1945 – 1946*], [Máy tính *ENIAC* (Mỹ)], [Chiếc máy tính điện tử số vạn năng đầu tiên trên thế giới, mở đầu kỉ nguyên máy tính điện tử.],
  [*1956*], [Hội thảo *Dartmouth* (Mỹ)], [Thuật ngữ *"Trí tuệ nhân tạo" (AI)* chính thức ra đời, khai sinh lĩnh vực nghiên cứu AI.],
  [*1965*], [Chương trình *ELIZA*], [Do Joseph Weizenbaum (MIT) phát triển – cho phép con người trò chuyện với máy tính bằng văn bản ngôn ngữ tự nhiên.],
  [*1969*], [Mạng *ARPANET*], [Mạng máy tính đầu tiên tại Mỹ dựa trên chuyển mạch gói – *tiền thân trực tiếp của mạng Internet*.],
  [*1983*], [Giao thức *TCP/IP*], [Bộ giao thức truyền thông TCP/IP chính thức áp dụng trên ARPANET, đánh dấu sự ra đời của Internet hiện đại.],
  [*1989 – 1991*], [*World Wide Web (WWW)*], [Do *Tim Berners-Lee* phát minh (công bố rộng rãi năm 1991–1992), tạo bước ngoặt đưa Internet phổ cập toàn cầu.],
  [*1997*], [*Deep Blue* & *Internet Việt Nam*], [Siêu máy tính *Deep Blue* (IBM) thắng vua cờ vua Garry Kasparov; ngày *19/11/1997* Việt Nam chính thức kết nối Internet.],
  [*1998*], [Máy tìm kiếm *Google*], [Làm thay đổi căn bản cách nhân loại tra cứu và tiếp cận kho tri thức khổng lồ trên Web.],
  [*2000*], [Robot hình người *ASIMO*], [Do Honda chế tạo – robot đầu tiên đi bằng hai chân linh hoạt, lên xuống cầu thang và tương tác với người.],
  [*2004 – 2007*], [Mạng xã hội & Smartphone], [Facebook (2004), YouTube (2005), iPhone (2007) thúc đẩy bùng nổ truyền thông xã hội và thiết bị thông minh.],
  [*2011*], [Hệ thống *IBM Watson*], [Chiến thắng các nhà vô địch con người trong chương trình truyền hình đố vui _Jeopardy!_ (hiểu ngôn ngữ tự nhiên).],
  [*2016*], [Chương trình *AlphaGo*], [AI của Google DeepMind đánh bại nhà vô địch cờ vây thế giới Lee Sedol (4–1) – cột mốc lớn của Học sâu (_Deep Learning_).],
)

=== Đơn vị kiến thức A.3. Kĩ năng sử dụng thiết bị số của mỗi công dân _(Bài 7 – Tích hợp thực hành)_
- *Khởi động và tắt thiết bị số đúng quy trình:* Bật nút nguồn (*Power*) để hệ điều hành nạp vào bộ nhớ; khi kết thúc phải chọn lệnh *Shut down* (trên PC) hoặc tắt nguồn bằng phần mềm thay vì rút phích điện đột ngột để tránh hỏng ổ cứng và mất dữ liệu đang mở.
- *Quản lí tệp và thư mục khoa học:* Tổ chức cây thư mục theo chủ đề/môn học; đặt tên tệp ngắn gọn, rõ nghĩa; nhận biết phần mở rộng tệp phổ biến (`.docx`, `.pdf`, `.xlsx`, `.pptx`, `.jpg`, `.png`, `.mp3`, `.mp4`, `.exe`).
- *Sử dụng chức năng & phần mềm cơ bản cài sẵn:* Kết nối Wi-Fi/Bluetooth, điều chỉnh âm lượng/độ sáng, chụp màn hình (`PrtSc` hoặc `Windows + Shift + S`), trình duyệt web, công cụ ghi chú, máy tính (*Calculator*), trình quản lí tệp (*File Explorer*).

== Chủ đề B. Mạng máy tính và Internet (4,0 điểm – 40% đề thi)

=== Đơn vị kiến thức B.1. Mạng máy tính, Internet, Cloud Computing và IoT _(Bài 8 – SGK Kết nối tri thức)_

#concept-box(title: "1. Khái niệm Mạng máy tính & Các thành phần cơ bản")[
  - *Mạng máy tính (Computer Network):* Là hai hay nhiều máy tính và các thiết bị số được kết nối với nhau để *truyền, trao đổi dữ liệu* và *dùng chung tài nguyên* (dữ liệu, phần mềm, thiết bị ngoại vi như máy in, máy quét, bộ nhớ mạng).
  - *3 thành phần chính của một mạng máy tính:*
    1. *Các thiết bị đầu cuối:* Máy tính để bàn, laptop, điện thoại thông minh, máy tính bảng, máy in mạng, camera IP,...
    2. *Thiết bị kết nối mạng & Môi trường truyền dẫn:*
       - _Môi trường truyền dẫn:_ Có dây (cáp xoắn đôi UTP, cáp quang) hoặc không dây (sóng vô tuyến Wi-Fi, Bluetooth, 4G/5G, vệ tinh).
       - _Thiết bị kết nối:_ Bộ chuyển mạch (*Switch* – nối các thiết bị trong cùng mạng LAN), bộ định tuyến (*Router* – dẫn đường dữ liệu giữa các mạng khác nhau / ra Internet), bộ thu phát không dây (*WAP / Wi-Fi Access Point*), *Modem* (chuyển đổi tín hiệu số $arrow.l.r$ tín hiệu tương tự/quang của nhà mạng ISP).
    3. *Phần mềm mạng & Giao thức truyền thông (Protocol):* Hệ điều hành mạng, ứng dụng mạng và các bộ quy tắc giao tiếp (như *TCP/IP*).
]

*2. Phân loại mạng máy tính – So sánh mạng LAN và mạng Internet:* _(Trọng tâm Thông hiểu & Đúng/Sai)_

#table(
  columns: (1.15fr, 1.9fr, 1.95fr),
  inset: 6pt,
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  [*Tiêu chí so sánh*], [*Mạng cục bộ – LAN* _(Local Area Network)_], [*Mạng Internet* _(Mạng toàn cầu)_],
  [*1. Phạm vi địa lí*], [Phạm vi *nhỏ, hẹp*: trong một phòng, một gia đình, một tòa nhà, trường học hoặc cơ quan.], [Phạm vi *toàn cầu*: kết nối khắp các quốc gia và châu lục trên thế giới.],
  [*2. Quy mô kết nối*], [Số lượng thiết bị ít (từ vài thiết bị đến vài trăm thiết bị đầu cuối).], [Quy mô khổng lồ, liên kết hàng triệu mạng LAN/WAN với hàng tỉ thiết bị số.],
  [*3. Quyền sở hữu* \ _(Câu bẫy cực hay ra!)_], [*Có chủ sở hữu xác định* (thuộc về một cá nhân, hộ gia đình, nhà trường hoặc doanh nghiệp tự đầu tư, quản trị).], [*Không thuộc quyền sở hữu của bất kì cá nhân, tổ chức hay quốc gia riêng lẻ nào.*],
  [*4. Phương thức kết nối*], [Kết nối trực tiếp qua cáp mạng nội bộ, Switch hoặc bộ phát Wi-Fi trong khuôn viên.], [Kết nối thông qua Router, hệ thống đường trục viễn thông, cáp quang biển, vệ tinh của các nhà mạng (ISP).],
  [*5. Độ an toàn, bảo mật*], [Môi trường khép kín nội bộ nên *dễ kiểm soát và độ an toàn cao hơn*.], [Môi trường mở công cộng nên *tiềm ẩn nhiều nguy cơ mất an toàn* (mã độc, tấn công mạng, lừa đảo).],
)

*3. Thay đổi chất lượng cuộc sống, phương thức học tập và làm việc nhờ mạng máy tính:*
- *Phương thức học tập:* Chuyển từ học truyền thống giới hạn trong lớp học sang *học tập mọi lúc, mọi nơi (E-learning)*, lớp học trực tuyến (*Zoom, Google Meet, MS Teams*), tra cứu học liệu đa phương tiện, kiểm tra đánh giá trực tuyến, tự học suốt đời.
- *Phương thức làm việc:* Làm việc từ xa (*Work from home*), cộng tác trực tuyến thời gian thực trên cùng một tài liệu từ nhiều quốc gia, tự động hóa quy trình văn phòng, hình thành nhiều nghề nghiệp số mới.
- *Chất lượng cuộc sống:* Giao tiếp tức thời chi phí thấp (nhắn tin, gọi video), mua sắm trực tuyến, thanh toán điện tử, đặt xe, khám bệnh từ xa, giải trí theo yêu cầu, dịch vụ hành chính công trực tuyến tiết kiệm thời gian đi lại.

*4. Điện toán đám mây (Cloud Computing):* _(Trọng tâm Nhận biết & Đúng/Sai)_
- *Khái niệm:* Là mô hình cung cấp và phân phối các tài nguyên máy tính (máy chủ, bộ nhớ lưu trữ, cơ sở dữ liệu, mạng, phần mềm,...) thông qua mạng Internet theo nhu cầu sử dụng ("thuê dùng qua mạng thay vì phải tự mua sắm, cài đặt toàn bộ trên máy cá nhân").
- *3 mô hình dịch vụ Điện toán đám mây cơ bản (SGK Bài 8):*
  1. *SaaS (_Software as a Service_ – Phần mềm dạng dịch vụ):* Cung cấp phần mềm ứng dụng chạy trực tiếp trên trình duyệt/mạng cho người dùng cuối. *Ví dụ cụ thể:* _Google Docs, Google Sheets, Microsoft 365 Online, Gmail, Zoom, Google Drive, Dropbox, iCloud, OneDrive_.
  2. *PaaS (_Platform as a Service_ – Nền tảng dạng dịch vụ):* Cung cấp môi trường, công cụ nền tảng để các lập trình viên phát triển và triển khai ứng dụng web.
  3. *IaaS (_Infrastructure as a Service_ – Hạ tầng dạng dịch vụ):* Cho thuê hạ tầng phần cứng ảo hóa (máy chủ ảo, dung lượng lưu trữ lớn, thiết bị mạng).
- *Ưu điểm vượt trội:* Truy cập dữ liệu mọi lúc mọi nơi trên nhiều thiết bị chỉ cần có Internet; dễ dàng chia sẻ và cộng tác nhóm; tiết kiệm chi phí đầu tư phần cứng; dữ liệu được nhà cung cấp sao lưu chuyên nghiệp (dù máy cá nhân hỏng vẫn không mất tệp trên đám mây).

*5. Internet vạn vật (IoT – Internet of Things):* _(Trọng tâm Nhận biết, Thông hiểu & Đúng/Sai)_
- *Khái niệm:* *IoT* là hệ thống liên kết các thiết bị số, máy móc, phương tiện, đồ vật gắn *cảm biến (sensors)* và phần mềm thông qua mạng Internet, giúp chúng có khả năng *tự động thu thập, trao đổi dữ liệu và phối hợp hoạt động với nhau* mà *không cần sự can thiệp trực tiếp thường xuyên của con người*.
- *Các ví dụ thực tiễn tiêu biểu về thay đổi do IoT mang lại:*
  - *Nhà thông minh (Smart Home):* Đèn tự bật khi có người, điều hòa tự chỉnh nhiệt độ theo thời tiết và giấc ngủ, khóa cửa vân tay báo tin nhắn về điện thoại chủ nhà khi có đột nhập.
  - *Giao thông thông minh:* Hệ thống thu phí điện tử không dừng (*ETC*) tự động nhận diện thẻ định danh trên ô tô và trừ tiền qua tài khoản giúp xóa bỏ ùn tắc tại trạm thu phí; đèn tín hiệu điều tiết theo mật độ xe thực tế.
  - *Nông nghiệp thông minh:* Cảm biến đo độ ẩm đất, nhiệt độ, ánh sáng trong nhà kính gửi dữ liệu lên đám mây để hệ thống tự động bật van tưới nhỏ giọt đúng lượng nước cây cần.
  - *Y tế thông minh:* Vòng đeo tay y tế đo nhịp tim, nồng độ oxy máu 24/7 của người cao tuổi, tự động gửi cảnh báo khẩn cấp và định vị GPS tới bác sĩ/người thân khi phát hiện bất thường.
- *Ý kiến đánh giá lợi ích & lưu ý về IoT:* IoT giúp *tiết kiệm thời gian, nhân lực, năng lượng*, giải phóng con người khỏi các công việc giám sát lặp đi lặp lại, xử lí tức thời ở những môi trường nguy hiểm/rộng lớn. Tuy nhiên, cần chú ý *đổi mật khẩu mặc định và bảo mật thiết bị IoT* (như camera gia đình) để tránh bị tin tặc chiếm quyền xâm phạm đời tư.

=== Đơn vị kiến thức B.2. Sử dụng dịch vụ Web & Tự bảo vệ khi tham gia mạng _(Bài 9 & Bài 10 – SGK)_

*1. Nguy cơ và tác hại khi tham gia Internet một cách bất cẩn, thiếu hiểu biết:*
- *Lộ lọt, bị đánh cắp thông tin cá nhân và tài chính:* Đăng công khai số CCCD, địa chỉ nhà, số điện thoại, mật khẩu hoặc sập bẫy lừa đảo trực tuyến (*Phishing* – trang web/tin nhắn giả mạo ngân hàng, trúng thưởng, tuyển dụng việc nhẹ lương cao).
- *Nhiễm phần mềm độc hại:* Tải tệp lậu, phần mềm bẻ khóa (*crack*), nhấn vào đường link lạ làm hỏng hệ điều hành, mất sạch dữ liệu hoặc bị tống tiền.
- *Tiếp xúc thông tin giả mạo (Fake news), độc hại, lừa đảo:* Tin và làm theo thông tin sai sự thật gây thiệt hại sức khỏe, tiền bạc hoặc hoang mang tâm lí.
- *Bị bắt nạt, quấy rối trên không gian mạng (Cyberbullying):* Bị chế giễu, tung tin đồn thất thiệt, ghép ảnh bôi nhọ gây khủng hoảng tâm lí, trầm cảm.
- *Nghiện Internet, mạng xã hội, trò chơi trực tuyến:* Suy giảm thị lực, rối loạn giấc ngủ, xao nhãng học tập, thu mình khỏi giao tiếp thực tế.

*2. Phần mềm độc hại (Malware) & Công cụ phòng chống:* _(Trọng tâm Nhận biết & Vận dụng)_
- *Khái niệm:* *Phần mềm độc hại (Malware – Malicious Software)* là các phần mềm được viết ra với ý đồ xấu nhằm gây hại cho thiết bị số, phá hoại hệ thống, đánh cắp dữ liệu hoặc trục lợi bất chính.

#table(
  columns: (1.05fr, 1.3fr, 1.35fr, 1.3fr),
  inset: 5.5pt,
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  [*Loại mã độc*], [*Bản chất cấu tạo*], [*Cơ chế lây lan đặc trưng*], [*Tác hại chính*],
  [*Virus máy tính*], [*Không phải* phần mềm hoàn chỉnh (chỉ là các đoạn mã độc).], [Phải gắn (*kí sinh*) vào một phần mềm/tệp vật chủ; lây lan khi người dùng *mở/chạy tệp bị nhiễm*.], [Làm hỏng/xóa tệp dữ liệu, làm chậm hoặc tê liệt hệ điều hành.],
  [*Worm* _(Sâu máy tính)_], [Là một *phần mềm hoàn chỉnh*, độc lập.], [*Tự nhân bản* và *tự động lây lan qua mạng* (lỗ hổng bảo mật, email, liên kết) không cần tệp vật chủ.], [Làm nghẽn băng thông mạng tốc độ cao, mở đường cho mã độc khác.],
  [*Trojan* _(Ngựa thành Troia)_], [Phần mềm nội gián *ngụy trang* dưới vỏ bọc phần mềm hợp pháp/miễn phí hấp dẫn.], [*Không tự nhân bản*; dụ người dùng tự tải về và cài đặt (như công cụ crack, game lậu).], [Âm thầm mở cửa hậu (*Backdoor*), đánh cắp mật khẩu (*Spyware/Keylogger*), điều khiển máy từ xa (*Botnet*).],
  [*Ransomware* _(Mã độc tống tiền)_], [Biến thể nguy hiểm kết hợp cơ chế Trojan/Worm.], [Qua email lừa đảo đính kèm tệp giả mạo hóa đơn, liên kết độc hại, lỗ hổng hệ thống.], [*Mã hóa toàn bộ dữ liệu* của nạn nhân và đòi tiền chuộc mới cấp khóa giải mã.],
)

- *Các công cụ thông dụng để ngăn ngừa và loại bỏ phần mềm độc hại:*
  - Phần mềm bảo mật tích hợp sẵn trên hệ điều hành Windows: *Windows Security / Windows Defender* và tường lửa *Windows Defender Firewall*.
  - Các phần mềm diệt virus chuyên dụng uy tín: *Kaspersky, Bitdefender, Norton, Avast, ESET, Bkav Pro,...*
  - *Nguyên tắc sử dụng hiệu quả:* Bật chế độ bảo vệ thời gian thực (*Real-time protection*); cập nhật cơ sở dữ liệu nhận diện virus và bản vá hệ điều hành thường xuyên; quét USB và tệp tải từ mạng về trước khi mở.

#tip-box(title: "Quy tắc 4 Bước Vàng phòng vệ khi bị Bắt nạt trên mạng (Nhớ cụm: K – L – C – B)")[
  1. *K – Không đáp trả:* Giữ bình tĩnh, tuyệt đối *không đôi co, chửi bới lại* kẻ bắt nạt trên mạng vì càng phản ứng gay gắt càng kích thích đối phương tấn công mạnh hơn.
  2. *L – Lưu giữ bằng chứng:* Chụp ảnh màn hình (*Screenshot*) toàn bộ tin nhắn, bình luận, bài đăng ác ý, tên tài khoản, đường dẫn URL và thời gian xảy ra sự việc.
  3. *C – Chặn và Báo cáo:* Sử dụng tính năng *Chặn (Block)* để cắt đứt liên lạc và *Báo cáo vi phạm (Report)* với quản trị viên mạng xã hội để gỡ nội dung xấu.
  4. *B – Báo cho người tin cậy / Cơ quan chức năng:* Tâm sự, nhờ sự giúp đỡ ngay của *cha mẹ, người thân, thầy cô giáo chủ nhiệm*; nếu hành vi nghiêm trọng (đe dọa an toàn, tống tiền, vu khống nặng nề) cần trình báo *cơ quan Công an*.
]

*3. Biện pháp đề phòng tác hại trên Internet & Tự bảo vệ dữ liệu cá nhân:*
- *Bảo mật tài khoản:* Đặt *mật khẩu mạnh* (tối thiểu 8 kí tự, kết hợp chữ hoa, chữ thường, chữ số và kí tự đặc biệt như `Tr@ngAn#2026`, không dùng ngày sinh/123456); bật *xác thực hai yếu tố (2FA/OTP)*; luôn *đăng xuất (Log out)* và không lưu mật khẩu trên máy tính công cộng.
- *Cảnh giác giao dịch & liên kết:* Không nhấp vào đường link lạ, không tải tệp không rõ nguồn gốc; tuyệt đối *không cung cấp mã OTP ngân hàng/mật khẩu* cho bất kì ai (kể cả người tự xưng công an, nhân viên ngân hàng).
- *Bảo vệ dữ liệu cá nhân:* Thiết lập quyền riêng tư (*Privacy*) trên mạng xã hội; thực hiện *sao lưu dữ liệu quan trọng định kì* ra ổ cứng ngoài hoặc dịch vụ lưu trữ đám mây (*Google Drive, OneDrive*).
- *Sử dụng mạng lành mạnh:* Kiểm chứng thông tin từ các trang báo chính thống (`.gov.vn`, thông tấn xã) trước khi tin; sắp xếp thời gian dùng Internet hợp lí, cân bằng học tập và vận động thể chất.

*4. Sử dụng dịch vụ Web xử lí thông tin & Khai thác nguồn học liệu mở (Bài 10 – SGK):*
- *Công cụ dịch tự động đa năng (ví dụ Google Dịch – `translate.google.com`):* Giúp xóa rào cản ngôn ngữ với các chức năng xử lí thông tin thông minh trên PC và điện thoại:
  - Dịch *văn bản* nhập trực tiếp giữa hơn 100 ngôn ngữ (có chế độ tự phát hiện ngôn ngữ nguồn).
  - Dịch *tiếng nói / giọng nói* trực tiếp qua Micro và phát âm chuẩn bản ngữ qua Loa.
  - Dịch chữ trên *hình ảnh* (tải ảnh lên hoặc soi Camera điện thoại qua Google Lens).
  - Dịch nguyên vẹn *tệp tài liệu* (`.docx`, `.pdf`, `.pptx`, `.xlsx`) và dịch toàn bộ *trang web* qua địa chỉ URL.
- *Nguồn học liệu mở trên Internet (OER – Open Educational Resources):*
  - Là các tài liệu học tập, giảng dạy và nghiên cứu (sách điện tử, bài giảng, video, khóa học, phần mềm mô phỏng,...) thuộc phạm vi công cộng hoặc được phát hành theo *giấy phép mở*, cho phép người học *truy cập, sử dụng miễn phí và hợp pháp*.
  - *Một số nguồn học liệu mở tiêu biểu:* Hệ tri thức Việt số hóa (`itrithuc.vn`), Hành trang số NXB Giáo dục (`hanhtrangso.nxbgd.vn`), khóa học mở của Học viện MIT (`ocw.mit.edu`), `Khan Academy`, bách khoa toàn thư mở `Wikipedia`, thư viện học liệu mở quốc gia.

== Chủ đề D. Đạo đức, pháp luật và văn hoá trong môi trường số (2,0 điểm – 20% đề thi)

=== Đơn vị kiến thức D.1. Nghĩa vụ tuân thủ pháp lí trong môi trường số _(Bài 11 – SGK Kết nối tri thức)_

*1. Các vấn đề nảy sinh về đạo đức, văn hóa và pháp luật khi giao tiếp qua mạng phổ biến:*
Do đặc điểm *ẩn danh, lan truyền cực nhanh, phạm vi rộng và khó thu hồi triệt để* của môi trường số, nhiều vấn đề tiêu cực đã phát sinh:
- *Về văn hóa – đạo đức:* Sử dụng ngôn từ tục tĩu, thiếu tôn trọng, công kích cá nhân ("anh hùng bàn phím"), vô cảm trước nỗi đau người khác, cổ xúy lối sống lệch chuẩn, bắt nạt tập thể trên mạng.
- *Về pháp luật:* Tung tin giả (*Fake news*) gây hoang mang dư luận; vu khống, bịa đặt xúc phạm danh dự, nhân phẩm cá nhân và uy tín tổ chức; tự ý tiết lộ bí mật đời tư cá nhân; lừa đảo chiếm đoạt tài sản; *xâm phạm bản quyền* phần mềm và tác phẩm số; tấn công mạng, phát tán mã độc, chống phá Nhà nước.

*2. Nội dung cơ bản của các văn bản pháp luật Việt Nam điều chỉnh môi trường số:* _(Trọng tâm Nhận biết, Thông hiểu & Vận dụng cao)_

#table(
  columns: (1.25fr, 2.25fr, 1.5fr),
  inset: 5.5pt,
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  [*Văn bản pháp luật*], [*Nội dung quy định cốt lõi cần nhớ*], [*Ví dụ hành vi vi phạm bị nghiêm cấm*],
  [*1. Luật Công nghệ thông tin* \ _(Số 67/2006/QH11 – đặc biệt Điều 12)_], [Quy định về hoạt động ứng dụng và phát triển CNTT, quyền và nghĩa vụ của tổ chức/cá nhân. *Điều 12 nghiêm cấm:* cung cấp, trao đổi, truyền đưa, lưu trữ thông tin số nhằm chống Nhà nước; kích động bạo lực, đồi trụy, tệ nạn xã hội, mê tín dị đoan; *xuyên tạc, vu khống, xúc phạm uy tín tổ chức, danh dự, nhân phẩm công dân*; *xâm phạm quyền sở hữu trí tuệ* trong hoạt động CNTT.], [Lập trang web phát tán văn hóa phẩm đồi trụy; bẻ khóa và kinh doanh phần mềm lậu; cản trở trái phép hệ thống CNTT.],
  [*2. Nghị định về quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng* \ _(NĐ 72/2013/NĐ-CP – Điều 5; cập nhật NĐ 27/2018, NĐ 147/2024; xử phạt theo NĐ 15/2020/NĐ-CP)_], [Cụ thể hóa quản lí Internet, mạng xã hội, trang thông tin điện tử. *Nghiêm cấm:* lợi dụng dịch vụ Internet gây phương hại an ninh quốc gia; tiết lộ bí mật nhà nước, bí mật đời tư cá nhân; *giả mạo tổ chức, cá nhân và phát tán thông tin giả mạo, thông tin sai sự thật* xâm hại quyền và lợi ích hợp pháp của người khác; quảng cáo hàng hóa/dịch vụ bị cấm. _(Theo Điều 101 NĐ 15/2020/NĐ-CP: chia sẻ tin giả, sai sự thật, vu khống trên MXH có thể bị phạt hành chính từ 10–20 triệu đồng đối với tổ chức, 5–10 triệu đồng đối với cá nhân)._], [Tạo tài khoản Facebook giả mạo danh nghĩa nhà trường/cơ quan công an; đăng tin thất thiệt về dịch bệnh/vỡ đê để câu lượt tương tác.],
  [*3. Luật An ninh mạng* \ _(Số 24/2018/QH14 – đặc biệt Điều 8, Điều 16, Điều 29)_], [Bảo vệ an ninh quốc gia và trật tự an toàn xã hội trên không gian mạng. *Điều 8 nghiêm cấm:* thông tin chống Nhà nước, xuyên tạc lịch sử, *bịa đặt, sai sự thật gây hoang mang trong nhân dân*, *xúc phạm nghiêm trọng danh dự, nhân phẩm người khác*, lừa đảo chiếm đoạt tài sản, tấn công mạng, phát tán mã độc, xâm nhập trái phép hệ thống thông tin. *Điều 29* quy định quyền được bảo vệ của trẻ em trên không gian mạng.], [Xâm nhập trái phép tài khoản mạng của người khác; tung tin đồn thất thiệt gây hỗn loạn thị trường; ghép ảnh bôi nhọ danh dự bạn học.],
  [*4. Luật Sở hữu trí tuệ* \ _(2005, sửa đổi 2009, 2019, 2022)_], [Bảo hộ *Quyền tác giả (Bản quyền)* đối với tác phẩm văn học, nghệ thuật, khoa học và sản phẩm số (bài viết, bức ảnh, bản nhạc, video, cơ sở dữ liệu, *chương trình máy tính*), gồm: \ • *Quyền nhân thân:* Đặt tên, đứng tên tác giả, công bố tác phẩm, bảo vệ sự toàn vẹn của tác phẩm. \ • *Quyền tài sản:* Làm tác phẩm phái sinh, sao chép, phân phối, truyền đạt tới công chúng, cho thuê chương trình máy tính.], [Tải tiểu thuyết/khóa học có bản quyền rồi đăng công khai hoặc bán lại kiếm lời không xin phép tác giả; đạo văn, xóa tên tác giả trên ảnh.],
)

#concept-box(title: "3. Bản quyền thông tin & Sản phẩm số – Phân biệt Đúng / Sai pháp luật")[
  - *Mua bản sao phần mềm có bản quyền (License)* có nghĩa là người mua được *quyền sử dụng hợp pháp* phần mềm đó theo điều khoản cấp phép (ví dụ cài trên 1 máy tính cá nhân), *KHÔNG đồng nghĩa* với việc mua quyền tác giả để tự ý nhân bản, bẻ khóa hay đem bán lại cho nhiều người khác!
  - *Các hành vi VI PHẠM bản quyền điển hình & hậu quả:*
    1. *Sử dụng phần mềm bẻ khóa (Crack / Keygen lậu):* Xâm phạm quyền tài sản của nhà sản xuất phần mềm; hậu quả là vừa vi phạm pháp luật, vừa có nguy cơ cực cao bị nhiễm *Trojan, Spyware, Ransomware* cài ẩn trong công cụ crack.
    2. *Sao chép bài viết, hình ảnh, nhạc, phim, mã nguồn có bản quyền* mà không xin phép hoặc không trích dẫn nguồn (mạo danh tác giả / dùng cho mục đích thương mại, kiếm tiền quảng cáo): Xâm phạm quyền nhân thân và quyền tài sản.
    3. *Quay lén phim trong rạp chiếu phim (Camcord) rồi phát tán lên mạng xã hội:* Gây thiệt hại kinh tế nặng nề cho nhà sản xuất phim, có thể bị xử phạt hành chính hàng chục triệu đồng hoặc truy cứu trách nhiệm hình sự nếu thu lợi bất chính lớn.
  - *Các hành vi HỢP PHÁP được khuyến khích:*
    - Mua bản quyền chính hãng hoặc sử dụng *phần mềm nguồn mở / miễn phí* (như _LibreOffice, Ubuntu, GIMP, Python, Inkscape_).
    - Khai thác tài nguyên có giấy phép *Creative Commons (CC)* hoặc *Học liệu mở (OER)* đúng điều kiện ghi công tác giả.
    - *Trích dẫn hợp lí* một phần nhỏ tác phẩm để minh họa trong bài học tập, nghiên cứu khoa học (không nhằm mục đích thương mại, không làm sai lệch ý tác giả và *bắt buộc ghi rõ tên tác giả, nguồn gốc tác phẩm*).
]

*4. Tác hại của việc chia sẻ thông tin bất cẩn & 6 Biện pháp nâng cao tính an toàn, hợp pháp:*
- *Ví dụ tác hại khi chia sẻ bất cẩn:*
  - Thấy bài viết giật gân chưa kiểm chứng (như tin đồn thực phẩm giả, bắt cóc, dịch bệnh) đã vội nhấn *Share (Chia sẻ)* $arrow.r$ tiếp tay lan truyền tin giả, gây hoang mang xã hội, làm thiệt hại uy tín doanh nghiệp/cá nhân vô tội và chính người chia sẻ cũng bị xử phạt vi phạm hành chính.
  - Tự ý đăng ảnh chụp dìm hàng bạn bè, bảng điểm cá nhân, số điện thoại/địa chỉ nhà của người khác lên hội nhóm công khai $arrow.r$ xâm phạm quyền riêng tư (Điều 38 Bộ luật Dân sự, Luật An ninh mạng), dẫn đến nạn nhân bị quấy rối, bắt nạt.
  - Khoe ảnh vé máy bay (lộ mã đặt chỗ PNR), thẻ căn cước công dân, thẻ ngân hàng lên mạng $arrow.r$ kẻ xấu lợi dụng hủy chuyến bay, vay tín dụng đen hoặc đánh cắp tài khoản.
- *6 Biện pháp đơn giản và thông dụng để chia sẻ thông tin an toàn, hợp pháp:*
  1. *Kiểm chứng nguồn tin trước khi chia sẻ:* Chỉ tin và chia sẻ thông tin từ cơ quan nhà nước, báo chí chính thống; tuyệt đối không chia sẻ tin đồn thất thiệt, chưa xác thực.
  2. *Tôn trọng quyền riêng tư:* Luôn *xin phép* trước khi chụp ảnh, ghi âm, quay video hoặc đăng tải thông tin cá nhân của người khác lên mạng.
  3. *Tôn trọng bản quyền tác giả:* Xin phép chủ sở hữu khi sử dụng sản phẩm số có bản quyền; ghi rõ tên tác giả và nguồn trích dẫn; ưu tiên dùng phần mềm có bản quyền hoặc phần mềm nguồn mở miễn phí.
  4. *Bảo mật thông tin nhạy cảm của bản thân và gia đình:* Không đăng công khai CCCD, thẻ học sinh, địa chỉ chi tiết, lịch trình vắng nhà, mật khẩu, mã OTP; kiểm soát chế độ hiển thị bài viết (*Chỉ mình tôi / Bạn bè*).
  5. *Ứng xử văn minh, có văn hóa:* Tuân thủ *Bộ Quy tắc ứng xử trên mạng xã hội* (Quyết định 874/QĐ-BTTTT năm 2021): ngôn từ lịch sự, tích cực, không kích động thù hận, không xúc phạm danh dự người khác.
  6. *Suy nghĩ kĩ về "dấu vết số" trước khi nhấn Đăng/Chia sẻ:* Mọi nội dung đăng lên mạng đều để lại dấu vết lâu dài và người đăng phải chịu trách nhiệm pháp lí về hành vi của mình.

#formula-box(title: "Công thức 4 Bước Vàng lấy trọn 1,0 điểm câu Tự luận Vận dụng cao (Chủ đề D)")[
  Khi đề bài nêu một tình huống cụ thể (VD: bạn X tải phần mềm crack, chia sẻ tin đồn thất thiệt, quay lén phim, đăng ảnh chế giễu bạn,...) và hỏi *"Hành vi đó có hợp pháp không? Vì sao? Nêu hậu quả và lời khuyên"*, em hãy trình bày đủ *4 ý chuẩn*:
  1. *Bước 1 – Khẳng định rõ tính pháp lí (0,25đ):* Khẳng định ngay hành vi đó là *KHÔNG HỢP PHÁP (Vi phạm pháp luật và chuẩn mực đạo đức trên môi trường số)* _(hoặc Hợp pháp nếu tình huống đúng luật)_.
  2. *Bước 2 – Nêu căn cứ pháp lí & bản chất vi phạm (0,25đ):* Chỉ rõ hành vi đã vi phạm quy định nào:
     - Liên quan phần mềm lậu, sao chép nhạc/phim/sách/ảnh không phép $arrow.r$ Vi phạm *Luật Sở hữu trí tuệ* (quyền tác giả) và *Điều 12 Luật Công nghệ thông tin*.
     - Liên quan tung tin giả, vu khống, xúc phạm danh dự, xâm phạm đời tư, tấn công mạng $arrow.r$ Vi phạm *Luật An ninh mạng (Điều 8)*, *Điều 12 Luật CNTT* và *Nghị định 72/2013/NĐ-CP (cùng NĐ 15/2020/NĐ-CP)*.
  3. *Bước 3 – Phân tích hậu quả / tác hại (0,25đ):* Đối với nạn nhân/tác giả/xã hội (thiệt hại kinh tế, tổn thương tinh thần, gây hoang mang dư luận) và đối với chính người vi phạm (nhiễm mã độc, bị kỉ luật nhà trường, phạt hành chính, bồi thường dân sự hoặc xử lí hình sự).
  4. *Bước 4 – Đề xuất cách xử lí / ứng xử đúng pháp luật (0,25đ):* Gỡ bỏ ngay bài đăng/tệp vi phạm, đính chính và xin lỗi (nếu xúc phạm/tung tin sai), thay thế bằng phần mềm nguồn mở/có bản quyền hoặc trích dẫn hợp pháp.
]
