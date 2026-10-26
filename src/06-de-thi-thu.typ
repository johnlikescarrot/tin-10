// =============================================================================
// src/06-de-thi-thu.typ
// Phần IV: Bộ 02 Đề kiểm tra thử Giữa kì I chuẩn cấu trúc 100% (45 phút/đề) + Đáp án
// =============================================================================

#import "template.typ": *

#pagebreak()

#part-banner(
  "Phần IV",
  "BỘ 02 ĐỀ KIỂM TRA THỬ GIỮA KÌ I CHUẨN MA TRẬN (45 PHÚT)",
  "Đề số 01 bám sát 100% Bảng Ma trận • Đề số 02 bám sát 100% Bảng Đặc tả • Có đáp án & thang điểm chấm chi tiết",
  accent: c-navy,
)

// =============================================================================
// ĐỀ KIỂM TRA THỬ SỐ 01
// =============================================================================

#block(
  width: 100%,
  fill: c-blue-bg,
  stroke: 0.8pt + c-blue,
  radius: 6pt,
  inset: 10pt,
  breakable: false,
  [
    #grid(
      columns: (1fr, 1.25fr),
      align: (center + horizon, center + horizon),
      [
        *SỞ GIÁO DỤC VÀ ĐÀO TẠO*\
        *TRƯỜNG THPT ........................*\
        #line(length: 45%, stroke: 0.6pt + c-navy)
      ],
      [
        *ĐỀ KIỂM TRA GIỮA HỌC KÌ I – ĐỀ MINH HOẠ SỐ 01*\
        *Môn: TIN HỌC 10 – ĐỊNH HƯỚNG ICT (Kết nối tri thức)*\
        *Thời gian làm bài: 45 phút* *(không kể thời gian phát đề)*
      ]
    )
  ]
)

=== Đề thi thử số 01 (Chuẩn cấu trúc Bảng Ma trận gốc: 20 TN + 02 ĐS + 03 TL)

==== PHẦN I. Trắc nghiệm nhiều phương án lựa chọn (5,0 điểm: Câu 1 – Câu 20, mỗi câu 0,25 điểm)
*Học sinh trả lời từ Câu 1 đến Câu 20. Mỗi câu hỏi học sinh chỉ chọn một phương án đúng nhất.*

#mcq(1, "NB",
  [Việc lưu trữ dữ liệu trên ổ cứng SSD hoặc thẻ nhớ có ưu điểm nổi bật nào sau đây so với lưu trữ trên sổ sách giấy?],
  [Chỉ đọc được một lần duy nhất rồi tự hủy.],
  [Nhỏ gọn nhưng chứa được khối lượng dữ liệu khổng lồ, tìm kiếm và sao lưu nhanh chóng.],
  [Không thể sao chép sang thiết bị khác.],
  [Dễ bị mối mọt ăn mòn nội dung tệp.],
  cols: 1
)

#mcq(2, "NB",
  [Trong các đơn vị đo dung lượng thông tin dưới đây, đơn vị nào lớn gấp $1024$ lần đơn vị Gigabyte ($"GB"$)?],
  [Megabyte (MB)], [Kilobyte (KB)], [Terabyte (TB)], [Byte (B)], cols: 4
)

#mcq(3, "TH",
  [Bác sĩ xem kết quả xét nghiệm máu có chỉ số đường huyết `11.8 mmol/L` trên phiếu xét nghiệm rồi kết luận bệnh nhân bị tiểu đường. Trong ví dụ này, con số `11.8 mmol/L` là gì?],
  [Thông tin], [Dữ liệu], [Vật mang tin], [Thiết bị ra], cols: 4
)

#mcq(4, "TH",
  [Một tệp ghi âm bài giảng có dung lượng $4 "MB"$. Hỏi tệp đó chiếm bao nhiêu Byte ($"B"$) bộ nhớ?],
  [$4.000.000 "B"$], [$4.096 "B"$], [$4.194.304 "B"$], [$524.288 "B"$], cols: 4
)

#mcq(5, "NB",
  [Dây chuyền robot tự động sơn và hàn khung xe ô tô trong nhà máy thể hiện đóng góp nào của tin học đối với xã hội?],
  [Tự động hóa các thiết bị và quy trình sản xuất.],
  [Thay thế hoàn toàn nhu cầu ăn uống của con người.],
  [Xóa bỏ mọi quy định pháp luật giao thông.],
  [Chỉ dùng để giải trí nghe nhạc.],
  cols: 1
)

#mcq(6, "NB",
  [Trong các thiết bị dưới đây, thiết bị nào là thiết bị số thông dụng (ngoài máy tính để bàn và laptop)?],
  [Bàn là điện cơ học], [Máy ảnh kĩ thuật số], [Quạt trần cơ học], [Bếp củi truyền thống], cols: 2
)

#mcq(7, "NB",
  [Linh kiện điện tử chính đánh dấu sự ra đời của máy tính điện tử thế hệ thứ tư (máy tính cá nhân PC) là:],
  [Đèn điện tử chân không], [Bóng bán dẫn (Transistor)], [Mạch tích hợp cỡ rất lớn (VLSI) – Vi xử lí], [Bánh răng cơ khí], cols: 2
)

#mcq(8, "NB",
  [Năm 1997, chiếc máy tính chuyên dụng nào của hãng IBM đã đánh bại đại kiện tướng cờ vua thế giới Garry Kasparov?],
  [ENIAC], [Deep Blue], [Macintosh], [ARPANET], cols: 4
)

#mcq(9, "NB",
  [Ứng dụng nào sau đây là dịch vụ lưu trữ đám mây do tập đoàn Microsoft cung cấp cho người dùng?],
  [OneDrive], [WinRAR], [Notepad], [Device Manager], cols: 4
)

#mcq(10, "NB",
  [Thuật ngữ viết tắt *IoT* trong tin học hiện đại dùng để chỉ khái niệm nào?],
  [Mạng nội bộ phòng máy], [Internet vạn vật], [Trình duyệt web ẩn danh], [Phần mềm bảng tính], cols: 2
)

#mcq(11, "NB",
  [Mạng máy tính kết nối các thiết bị trong phạm vi địa lí hẹp như một tòa nhà, một trường học hoặc một gia đình được gọi là:],
  [Mạng cục bộ (LAN)], [Mạng toàn cầu Internet], [Mạng viễn thông liên lục địa], [Hệ thống cáp quang biển], cols: 2
)

#mcq(12, "NB",
  [Dịch vụ nào dưới đây thuộc mô hình *Phần mềm hướng dịch vụ (SaaS)* của Điện toán đám mây?],
  [Google Docs (Soạn thảo văn bản trực tuyến)],
  [Ổ đĩa cứng gắn trong HDD],
  [Cáp mạng xoắn đôi UTP],
  [Bộ nguồn máy tính PSU],
  cols: 2
)

#mcq(13, "NB",
  [Phần mềm độc hại âm thầm theo dõi thói quen người dùng hoặc ghi lại thao tác bàn phím để đánh cắp mật khẩu được gọi là:],
  [Phần mềm gián điệp (Spyware / Keylogger)],
  [Phần mềm diệt virus (Antivirus)],
  [Phần mềm học tập mở],
  [Trình điều khiển máy in],
  cols: 2
)

#mcq(14, "NB",
  [Khi bị một nhóm người tung tin đồn ác ý, xúc phạm trên mạng xã hội (*bắt nạt qua mạng*), việc làm nào cần *TRÁNH*?],
  [Chụp ảnh màn hình lưu giữ bằng chứng.],
  [Chặn và báo cáo vi phạm tài khoản bắt nạt.],
  [Chia sẻ với bố mẹ và thầy cô giáo chủ nhiệm.],
  [Nóng giận dùng lời lẽ thô tục chửi bới lại hoặc tự giấu kín chịu đựng một mình.],
  cols: 1
)

#mcq(15, "NB",
  [Nguy cơ nào sau đây thường xảy ra khi người dùng tham gia Internet một cách bất cẩn, thiếu hiểu biết?],
  [Máy tính tự động nâng cấp dung lượng RAM vật lí.],
  [Bị lừa đảo chiếm đoạt tài khoản cá nhân, nhiễm mã độc hoặc tiếp nhận tin giả độc hại.],
  [Tốc độ gõ bàn phím luôn tăng gấp đôi.],
  [Màn hình máy tính tự động tiết kiệm điện tuyệt đối.],
  cols: 1
)

#mcq(16, "NB",
  [Công cụ nào sau đây hỗ trợ người dùng dịch tự động văn bản, tài liệu và giọng nói đa ngôn ngữ trực tuyến phổ biến nhất?],
  [Google Dịch (Google Translate)], [Disk Cleanup], [Task Manager], [Control Panel], cols: 2
)

#mcq(17, "NB",
  [Hành vi cố ý tạo ra và cài đặt phát tán chương trình virus máy tính phá hoại hệ thống thông tin của tổ chức, cá nhân khác bị nghiêm cấm trực tiếp tại *Điều 12* của đạo luật nào?],
  [Luật Công nghệ thông tin năm 2006],
  [Luật Khám bệnh, chữa bệnh],
  [Luật Thủy sản],
  [Luật Lâm nghiệp],
  cols: 2
)

#mcq(18, "NB",
  [Khi giao tiếp qua mạng xã hội trở nên phổ biến, vấn đề tiêu cực nào về văn hoá – đạo đức dễ nảy sinh nhất nếu người dùng thiếu ý thức?],
  [Mọi người đều giao tiếp lịch sự và kiểm chứng tin tức kĩ hơn.],
  [Ứng xử thiếu văn hoá, phát ngôn xúc phạm danh dự người khác và xâm phạm đời sống riêng tư.],
  [Tất cả phần mềm đều tự động có bản quyền miễn phí.],
  [Không còn bất kì tin giả nào xuất hiện.],
  cols: 1
)

#mcq(19, "TH",
  [Bạn T tải một bài báo khoa học trên mạng về, xóa tên tác giả thật rồi điền tên mình vào để nộp dự thi lấy giải thưởng của trường. Hành vi của T vi phạm quyền gì của tác giả bài báo?],
  [Không vi phạm gì vì bài báo đã đăng công khai trên mạng.],
  [Vi phạm nghiêm trọng quyền tác giả (cụ thể là quyền nhân thân đứng tên tác phẩm – hành vi đạo văn) theo Luật Sở hữu trí tuệ.],
  [Chỉ vi phạm quy tắc bảo trì phần cứng máy tính.],
  [Là hành vi khai thác nguồn học liệu mở đúng cách.],
  cols: 1
)

#mcq(20, "TH",
  [Để đảm bảo an toàn và hợp pháp khi đăng ảnh kỉ yếu tập thể lên mạng xã hội, cách làm nào sau đây là phù hợp nhất?],
  [Tự ý chọn những bức ảnh dìm hàng nhạy cảm của bạn bè đăng công khai kèm số điện thoại cá nhân của từng bạn.],
  [Xin ý kiến đồng thuận của các bạn có mặt trong ảnh, không đính kèm thông tin định danh nhạy cảm (số CCCD, địa chỉ nhà riêng) và dùng chú thích văn minh.],
  [Ghép logo thương hiệu lạ để chạy quảng cáo cá cược trực tuyến.],
  [Lấy nhạc có bản quyền thương mại ghép vào để bán video kiếm lời.],
  cols: 1
)

==== PHẦN II. Trắc nghiệm lựa chọn Đúng/Sai (2,0 điểm: Câu 1 – Câu 2, mỗi câu 1,0 điểm)
*Trong mỗi ý a), b), c), d) ở mỗi câu, học sinh chọn Đúng hoặc Sai.*

#tfq(
  "1 (Phần II)", "Chủ đề A.2 • Thiết bị thông minh & CMCN 4.0",
  [Một gia đình hiện đại trang bị *Tivi thông minh (Smart TV)* điều khiển bằng giọng nói Tiếng Việt và hệ thống *điều hoà thông minh* tự điều chỉnh nhiệt độ theo cảm biến nhiệt trong phòng và điều khiển từ xa qua Smartphone. Xét các nhận định sau:],
  [Chiếc Smart TV nói trên là một hệ thống xử lí thông tin vì nó tiếp nhận giọng nói qua micro, xử lí nhận dạng lệnh bằng vi xử lí, lưu trữ ứng dụng trong bộ nhớ và xuất hình ảnh/âm thanh ra màn hình, loa.],
  [Hệ thống điều hoà thông minh và Smart TV chỉ có ý nghĩa trang trí nội thất chứ hoàn toàn không liên quan gì đến xu thế Internet vạn vật (IoT) trong cuộc Cách mạng công nghiệp 4.0.],
  [Trên đường đi làm về lúc trời nắng nóng, người mẹ mở ứng dụng trên điện thoại thông minh qua mạng 4G để bật sẵn điều hoà ở mức $27 degree "C"$ trước 10 phút giúp phòng mát vừa đủ và tiết kiệm điện; đây là ứng dụng thiết thực của thiết bị thông minh có kết nối mạng.],
  [Một chiếc quạt điện cơ học truyền thống chỉ có 3 nút bấm số `1, 2, 3` đóng ngắt mạch điện trực tiếp, không có vi xử lí, không cảm biến và không kết nối mạng cũng được gọi là thiết bị thông minh.],
)

#tfq(
  "2 (Phần II)", "Chủ đề B.1 • Mạng LAN, Internet, Cloud & IoT",
  [Công ty thiết kế kiến trúc X thiết lập mạng nội bộ nối 25 máy tính đồ họa với máy in khổ lớn tại văn phòng, đồng thời sử dụng dịch vụ *OneDrive / Microsoft 365* để lưu trữ bản vẽ và gửi cho khách hàng ở nước ngoài qua Internet. Xét các nhận định sau:],
  [Mạng nội bộ nối 25 máy tính và máy in trong văn phòng Công ty X là mạng *LAN*, thuộc quyền sở hữu và quản lí riêng của Công ty X.],
  [Khác với mạng LAN của Công ty X, mạng *Internet* toàn cầu thuộc quyền sở hữu tư nhân của tập đoàn viễn thông lớn nhất thế giới.],
  [Khi kiến trúc sư đi công tác tại công trường ở tỉnh khác, nhờ lưu bản vẽ trên đám mây *OneDrive*, anh ấy có thể dùng máy tính bảng có kết nối 4G mở xem và cập nhật ngay bản vẽ mới nhất để trao đổi với chủ đầu tư.],
  [Nếu Công ty X muốn gửi bản vẽ dung lượng $50 "MB"$ cho đối tác ở Nhật Bản mà văn phòng bị cắt hoàn toàn kết nối Internet và mạng di động, nhân viên vẫn gửi trực tiếp qua dây cáp mạng LAN nội bộ của văn phòng sang Nhật Bản được.],
)

==== PHẦN III. Tự luận (3,0 điểm: Câu 1 – Câu 3, mỗi câu 1,0 điểm)

- *Câu 1 (1,0 điểm – Thông hiểu • Chủ đề B.2):* Khi tham gia các hoạt động trên Internet một cách bất cẩn và thiếu hiểu biết, học sinh có thể gặp phải những nguy cơ và tác hại nào? Em hãy trình bày ít nhất 4 biện pháp thiết thực để đề phòng các tác hại đó.
- *Câu 2 (1,0 điểm – Vận dụng • Chủ đề A.1):* Một ổ cứng di động còn trống $64 "GB"$. Bạn An chép vào ổ cứng đó $12$ bộ phim tài liệu học tập (mỗi bộ phim nặng $2,5 "GB"$). Phần dung lượng còn trống hoàn toàn được An dùng để lưu các tệp bài giảng âm thanh chất lượng cao, trung bình mỗi tệp nặng $16 "MB"$.
  a) Tính dung lượng còn trống của ổ cứng sau khi chép phim theo đơn vị $"GB"$ và đổi ra đơn vị $"MB"$.
  b) Hỏi bạn An lưu thêm được *tối đa bao nhiêu tệp bài giảng âm thanh*?
- *Câu 3 (1,0 điểm – Vận dụng cao • Chủ đề D.1):* Thấy tài khoản mạng xã hội của mình ít người theo dõi, bạn V (16 tuổi) tự bịa đặt một bản tin giả có tiêu đề *"Phát hiện nước sinh hoạt tại phường Z bị nhiễm chất kịch độc, người dân tuyệt đối ngừng sử dụng ngay"* kèm ảnh chỉnh sửa cắt ghép rồi đăng công khai lên các hội nhóm đông thành viên, gây hoang mang nghiêm trọng cho hàng nghìn hộ dân tại phường Z. Vận dụng kiến thức về Luật Công nghệ thông tin, Luật An ninh mạng và các Nghị định liên quan, em hãy xác định tính hợp pháp của hành vi bạn V, chỉ rõ hậu quả và nêu bài học ứng xử đúng đắn trên môi trường số.

=== Đáp án & Biểu điểm chấm chi tiết – Đề thi thử số 01

==== 1. Phần I – Trắc nghiệm 4 lựa chọn (5,0 điểm: mỗi câu đúng 0,25 điểm)
#block(breakable: false)[
  #set text(size: 8.4pt)
  #table(
    columns: (1fr,) * 10,
    inset: 4.5pt,
    stroke: 0.45pt + c-border,
    align: center + horizon,
    fill: (x, y) => if calc.even(y) { c-blue-bg } else { white },
    [*1. B*], [*2. C*], [*3. B*], [*4. C*], [*5. A*], [*6. B*], [*7. C*], [*8. B*], [*9. A*], [*10. B*],
    [*11. A*], [*12. A*], [*13. A*], [*14. D*], [*15. B*], [*16. A*], [*17. A*], [*18. B*], [*19. B*], [*20. B*],
  )
]
*(Giải thích nhanh Câu 4: $4 "MB" = 4 times 1024 "KB" = 4.096 "KB" = 4.096 times 1024 "B" = 4.194.304 "B"$).*

==== 2. Phần II – Trắc nghiệm Đúng/Sai (2,0 điểm: đúng 1 ý = 0,1đ; 2 ý = 0,25đ; 3 ý = 0,5đ; 4 ý = 1,0đ)
- *Câu 1 (Phần II):* *a) Đúng – b) Sai – c) Đúng – d) Sai* *(b sai vì Smart TV & điều hòa thông minh chính là thành phần tiêu biểu của Smart Home / IoT trong CMCN 4.0; d sai vì quạt cơ chỉ đóng ngắt điện thủ công không phải thiết bị thông minh)*.
- *Câu 2 (Phần II):* *a) Đúng – b) Sai – c) Đúng – d) Sai* *(b sai vì Internet không thuộc quyền sở hữu của bất kì tổ chức riêng lẻ nào; d sai vì mạng LAN chỉ kết nối nội bộ phạm vi hẹp trong văn phòng, không truyền xuyên quốc gia nếu không có Internet/WAN)*.

==== 3. Phần III – Tự luận (3,0 điểm)
- *Câu 1 (1,0 điểm):*
  - *Nêu đủ từ 4 nguy cơ/tác hại trở lên (0,50đ):* (1) Tiếp nhận tin giả, thông tin độc hại/phản văn hoá; (2) Bị lừa đảo trực tuyến (*Phishing*), đánh cắp tài khoản và dữ liệu cá nhân; (3) Bị bắt nạt, quấy rối trên không gian mạng (*Cyberbullying*); (4) Nghiện Internet/game online hại sức khỏe và sao nhãng việc học; (5) Thiết bị nhiễm phần mềm độc hại (Virus, Worm, Trojan, Ransomware) gây mất dữ liệu.
  - *Trình bày 4 biện pháp đề phòng (0,50đ):* (1) Bảo mật tài khoản bằng mật khẩu mạnh + xác thực 2 lớp (2FA), hạn chế công khai thông tin nhạy cảm; (2) Không nhấp link lạ, không tải tệp đính kèm đáng ngờ hay phần mềm *crack*; (3) Luôn kiểm chứng thông tin từ nguồn chính thống; (4) Cài đặt, cập nhật phần mềm diệt virus, bật tường lửa, sao lưu dữ liệu định kì và quản lí thời gian lên mạng khoa học.
- *Câu 2 (1,0 điểm):*
  - *a) (0,50đ):* Dung lượng 12 bộ phim là: $12 times 2,5 = 30 "GB"$. Dung lượng còn trống của ổ cứng là: $64 - 30 = bold("34 GB")$ *(0,25đ)*. Đổi ra Megabyte: $34 "GB" = 34 times 1024 = bold("34.816 MB")$ *(0,25đ)*.
  - *b) (0,50đ):* Số tệp bài giảng âm thanh lưu thêm được tối đa là: $34.816 : 16 = bold("2.176 (tệp)")$ *(lập phép chia đúng 0,25đ; kết quả và đơn vị chuẩn 0,25đ)*.
- *Câu 3 (1,0 điểm):*
  - *Khẳng định tính pháp lí (0,25đ):* Hành vi bịa đặt và phát tán tin giả của V là *bất hợp pháp (vi phạm pháp luật nghiêm trọng)* và vi phạm đạo đức, quy tắc ứng xử trên mạng xã hội.
  - *Căn cứ pháp luật (0,25đ):* Vi phạm *Điều 12 Luật Công nghệ thông tin 2006*, *Điều 8 & Điều 16 Luật An ninh mạng 2018* (nghiêm cấm đưa thông tin sai sự thật gây hoang mang trong Nhân dân, xâm hại trật tự an toàn xã hội) và *Điều 5 Nghị định 72/2013/NĐ-CP*, *Điều 101 Nghị định 15/2020/NĐ-CP*.
  - *Hậu quả (0,25đ):* Gây rối loạn đời sống sinh hoạt và tâm lí của hàng nghìn hộ dân phường Z; V (đủ 16 tuổi – độ tuổi chịu trách nhiệm hành chính đầy đủ theo Luật Xử lí vi phạm hành chính) sẽ bị cơ quan chức năng triệu tập, buộc gỡ bỏ tin giả, đính chính công khai và *xử phạt vi phạm hành chính* (trường hợp gây hậu quả đặc biệt nghiêm trọng có thể bị xem xét trách nhiệm hình sự).
  - *Bài học ứng xử (0,25đ):* Tuyệt đối không bịa đặt, cắt ghép hay chia sẻ thông tin sai sự thật để câu tương tác; luôn thượng tôn pháp luật và chịu trách nhiệm với mọi phát ngôn trên không gian mạng.

#pagebreak()

// =============================================================================
// ĐỀ KIỂM TRA THỬ SỐ 02
// =============================================================================

#block(
  width: 100%,
  fill: c-teal-bg,
  stroke: 0.8pt + c-teal,
  radius: 6pt,
  inset: 10pt,
  breakable: false,
  [
    #grid(
      columns: (1fr, 1.25fr),
      align: (center + horizon, center + horizon),
      [
        *SỞ GIÁO DỤC VÀ ĐÀO TẠO*\
        *TRƯỜNG THPT ........................*\
        #line(length: 45%, stroke: 0.6pt + c-navy)
      ],
      [
        *ĐỀ KIỂM TRA GIỮA HỌC KÌ I – ĐỀ MINH HOẠ SỐ 02*\
        *Môn: TIN HỌC 10 – ĐỊNH HƯỚNG ICT (Kết nối tri thức)*\
        *Thời gian làm bài: 45 phút* *(không kể thời gian phát đề)*
      ]
    )
  ]
)

=== Đề thi thử số 02 (Chuẩn cấu trúc Bảng Đặc tả gốc: 20 TN + 02 ĐS + 03 TL)

==== PHẦN I. Trắc nghiệm nhiều phương án lựa chọn (5,0 điểm: Câu 1 – Câu 20, mỗi câu 0,25 điểm)

#mcq(1, "NB",
  [Trong máy tính số, mọi dữ liệu văn bản, hình ảnh, âm thanh khi đưa vào xử lí và lưu trữ đều được biến đổi thành dãy các kí hiệu nào?],
  [Các chữ cái từ A đến Z], [Dãy các bit `0` và `1`], [Các nốt nhạc Đồ, Rê, Mi], [Các số La Mã I, V, X], cols: 2
)

#mcq(2, "NB",
  [Nhận định nào sau đây nêu đúng đặc điểm sao chép dữ liệu trên các thiết bị lưu trữ số?],
  [Có thể tạo ra nhiều bản sao giống hệt bản gốc 100% với tốc độ rất nhanh để sao lưu dự phòng.],
  [Mỗi lần sao chép tệp văn bản sẽ làm rách một góc màn hình.],
  [Chỉ sao chép được vào ban ngày khi có ánh sáng mặt trời.],
  [Không thể tìm kiếm theo tên tệp sau khi đã lưu.],
  cols: 1
)

#mcq(3, "TH",
  [Cùng xem bức ảnh chụp biển báo giao thông có dòng chữ Tiếng Nhật, người biết Tiếng Nhật hiểu được nội dung chỉ dẫn đường đi, còn người không biết Tiếng Nhật thì không hiểu. Ví dụ này chứng tỏ điều gì?],
  [Bức ảnh không chứa bất kì dữ liệu nào.],
  [Cùng một dữ liệu nhưng thông tin rút ra phụ thuộc vào sự hiểu biết của người tiếp nhận.],
  [Dữ liệu và thông tin là hai khái niệm hoàn toàn đồng nhất trong mọi trường hợp.],
  [Chỉ có âm thanh mới mang lại thông tin cho con người.],
  cols: 1
)

#mcq(4, "TH",
  [Sắp xếp các dung lượng sau theo thứ tự *từ lớn đến nhỏ*: `(1) 2 GB`, `(2) 1500 MB`, `(3) 2048 KB`, `(4) 1 TB`.],
  [(4) $->$ (1) $->$ (2) $->$ (3)],
  [(1) $->$ (4) $->$ (2) $->$ (3)],
  [(4) $->$ (2) $->$ (1) $->$ (3)],
  [(3) $->$ (2) $->$ (1) $->$ (4)],
  cols: 2
)

#mcq(5, "NB",
  [Việc sử dụng siêu máy tính để tính toán mô phỏng khí tượng và dự báo sớm đường đi của áp thấp nhiệt đới, bão lớn thể hiện đóng góp nào của tin học?],
  [Giải quyết các bài toán khoa học – kĩ thuật phức tạp.],
  [Chỉ phục vụ trò chơi điện tử giải trí.],
  [Thay thế hoàn toàn mưa nắng tự nhiên.],
  [Trang trí văn phòng làm việc.],
  cols: 2
)

#mcq(6, "NB",
  [Ngoài máy tính để bàn (PC) và máy tính xách tay (Laptop), thiết bị nào sau đây là một *thiết bị số thông minh* rất phổ biến?],
  [Máy tính bảng (Tablet)], [Thước kẻ nhựa], [Bút chì gỗ], [Bàn tính gảy hạt gỗ], cols: 4
)

#mcq(7, "NB",
  [Nhà bác học nào đã đề xuất kiến trúc máy tính với nguyên lí *"chương trình được lưu trữ trong bộ nhớ chung với dữ liệu"* vào năm 1945?],
  [John von Neumann], [Isaac Newton], [Thomas Edison], [Louis Pasteur], cols: 4
)

#mcq(8, "NB",
  [Công cụ tìm kiếm thông tin trên Web nổi tiếng *Google* chính thức ra đời vào năm nào?],
  [Năm 1946], [Năm 1969], [Năm 1998], [Năm 2020], cols: 4
)

#mcq(9, "NB",
  [Đâu là tập hợp gồm toàn các dịch vụ *lưu trữ đám mây* phổ biến dành cho người dùng cá nhân?],
  [Google Drive, Dropbox, OneDrive, iCloud],
  [Microsoft Paint, Notepad, WordPad, Calculator],
  [Chuột quang, bàn phím cơ, tai nghe, loa],
  [Virus, Worm, Trojan, Spyware],
  cols: 1
)

#mcq(10, "NB",
  [Đặc trưng cốt lõi nhất của hệ thống *Internet vạn vật (IoT)* là gì?],
  [Mọi thao tác truyền dữ liệu đều phải chép tay ra sổ giấy rồi gửi bưu điện.],
  [Các thiết bị, cảm biến có định danh được kết nối mạng để tự động thu thập và trao đổi dữ liệu mà ít cần sự can thiệp trực tiếp của con người.],
  [Chỉ kết nối tối đa 2 máy tính để bàn trong cùng 1 phòng học nhỏ không có Internet.],
  [Không sử dụng bất kì cảm biến hay mạng truyền thông nào.],
  cols: 1
)

#mcq(11, "NB",
  [Thiết bị nào thường được dùng để kết nối các máy tính với nhau bên trong một mạng cục bộ (*LAN*) có dây?],
  [Bộ chuyển mạch (Switch)], [Máy chiếu (Projector)], [Loa vi tính (Speaker)], [Chuột không dây], cols: 2
)

#mcq(12, "NB",
  [Khi một công ty khởi nghiệp thuê máy chủ ảo và ổ đĩa lưu trữ hạ tầng từ Amazon AWS để tự cài đặt hệ thống riêng, công ty đang dùng mô hình đám mây nào?],
  [SaaS (Phần mềm hướng dịch vụ)],
  [IaaS (Hạ tầng hướng dịch vụ)],
  [LAN nội bộ không nối mạng],
  [Thư tín bưu chính truyền thống],
  cols: 2
)

#mcq(13, "NB",
  [Điểm khác biệt căn bản của *Sâu máy tính (Worm)* so với *Virus máy tính* truyền thống là:],
  [Worm là chương trình độc lập hoàn chỉnh, tự nhân bản và lây lan qua mạng mà không cần gắn vào tệp vật chủ.],
  [Worm là phần mềm hợp pháp dùng để dọn rác ổ cứng.],
  [Worm chỉ hoạt động khi máy tính đã rút phích cắm điện và tháo pin.],
  [Worm là tên gọi khác của Tường lửa bảo vệ máy tính.],
  cols: 1
)

#mcq(14, "NB",
  [Hành động nào cần thực hiện đầu tiên để lưu giữ căn cứ xử lí khi phát hiện mình bị một tài khoản lạ nhắn tin vu khống, bắt nạt trên mạng?],
  [Xóa ngay toàn bộ tin nhắn và đập hỏng điện thoại.],
  [Chụp ảnh màn hình các tin nhắn, bình luận vi phạm và lưu lại đường dẫn tài khoản đó làm bằng chứng.],
  [Đăng mật khẩu tài khoản của mình lên trang cá nhân.],
  [Gửi tiền chuộc cho tài khoản lạ.],
  cols: 1
)

#mcq(15, "TH",
  [Tại sao người dùng được khuyến cáo *nên bật xác thực hai yếu tố (2FA)* cho tài khoản thư điện tử và mạng xã hội quan trọng?],
  [Để không cần nhớ tên đăng nhập nữa.],
  [Vì ngay cả khi kẻ gian biết được mật khẩu thì vẫn không thể đăng nhập trái phép nếu không có mã xác thực thứ hai trên thiết bị của chủ tài khoản.],
  [Để tốc độ tải phim tăng gấp 10 lần.],
  [Để tự động xóa hết các tệp văn bản trong máy.],
  cols: 1
)

#mcq(16, "TH",
  [Khi cài đặt một ứng dụng đèn pin miễn phí tải từ nguồn lạ trên điện thoại, ứng dụng này lại yêu cầu quyền *"Đọc tin nhắn SMS, truy cập danh bạ và ghi âm cuộc gọi"*. Cách xử lí an toàn nhất là:],
  [Bấm Đồng ý tất cả ngay lập tức để dùng cho nhanh.],
  [Từ chối cấp quyền bất thường và gỡ cài đặt ứng dụng vì đây là dấu hiệu điển hình của phần mềm gián điệp (*Spyware*) / *Trojan* thu thập dữ liệu trái phép.],
  [Tắt mật khẩu khóa màn hình điện thoại.],
  [Nhập thêm số thẻ ngân hàng vào ứng dụng đó.],
  cols: 1
)

#mcq(17, "NB",
  [Theo *Luật Sở hữu trí tuệ*, chương trình máy tính (phần mềm) được bảo hộ dưới hình thức quyền nào sau đây?],
  [Quyền tác giả (Bản quyền)], [Quyền sở hữu đất nông nghiệp], [Quyền ưu tiên đường sắt], [Quyền miễn thuế nhập khẩu], cols: 2
)

#mcq(18, "NB",
  [Nghị định nào của Chính phủ quy định chi tiết về *quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng* được giới thiệu trong SGK Tin học 10 Kết nối tri thức?],
  [Nghị định 72/2013/NĐ-CP (sửa đổi, bổ sung bởi Nghị định 27/2018/NĐ-CP)],
  [Nghị định xử phạt vi phạm lấn chiếm vỉa hè đường bộ],
  [Nghị định quy định về giống cây trồng lâm nghiệp],
  [Nghị định về đo đạc bản đồ địa giới],
  cols: 1
)

#mcq(19, "NB",
  [Theo *Luật An ninh mạng năm 2018*, hành vi nào dưới đây bị *nghiêm cấm hoàn toàn* trên không gian mạng?],
  [Tra cứu tài liệu ôn thi trên cổng học liệu mở của Bộ GD&ĐT.],
  [Đăng tải thông tin sai sự thật gây hoang mang trong Nhân dân, tấn công mạng hoặc chiếm đoạt tài sản.],
  [Gửi thư điện tử nộp bài tập về nhà cho giáo viên.],
  [Họp phụ huynh trực tuyến qua ứng dụng Google Meet.],
  cols: 1
)

#mcq(20, "NB",
  [Trong môi trường số, hành vi tự ý sao chép nguyên văn bài viết của tác giả khác rồi đăng lên báo tường điện tử dưới tên của mình gọi là:],
  [Đạo văn (vi phạm quyền tác giả)], [Sao lưu dữ liệu hợp pháp], [Mã hóa bảo mật], [Nén tệp dữ liệu], cols: 2
)

==== PHẦN II. Trắc nghiệm lựa chọn Đúng/Sai (2,0 điểm: Câu 1 – Câu 2, mỗi câu 1,0 điểm)

#tfq(
  "1 (Phần II)", "Chủ đề A.2 • Vai trò thiết bị thông minh & Tin học",
  [Một siêu thị hiện đại sử dụng hệ thống *quản lí bán hàng tự động bằng mã vạch/QR*, kết hợp *camera AI thông minh* đếm lưu lượng khách và ứng dụng đặt hàng giao tận nhà trên điện thoại thông minh. Xét các nhận định sau:],
  [Hệ thống quản lí kho và tính tiền tự động bằng mã vạch minh họa đóng góp của tin học trong việc quản lí, điều hành tự động hoạt động kinh doanh chính xác, nhanh chóng.],
  [Camera AI thông minh không phải là hệ thống xử lí thông tin vì nó chỉ có ống kính thủy tinh chứ không hề có khâu tiếp nhận dữ liệu, xử lí, lưu trữ hay truyền dữ liệu qua mạng.],
  [Khi khách hàng dùng ứng dụng trên điện thoại thông minh để chọn mua thực phẩm và thanh toán chuyển khoản QR không dùng tiền mặt, phương thức mua sắm và giao dịch trong xã hội đã thay đổi tiện lợi hơn nhờ thành tựu tin học.],
  [Đầu đọc mã vạch cầm tay đơn giản tại quầy thu ngân (chỉ đọc vạch đen trắng rồi truyền mã số sang máy tính tiền) có khả năng tự lập trình trí tuệ nhân tạo thay thế hoàn toàn hệ thống máy chủ quản lí của cả chuỗi siêu thị.],
)

#tfq(
  "2 (Phần II)", "Chủ đề B.1 • Mạng máy tính, Cloud & IoT",
  [Trường THPT B triển khai mô hình *Trường học thông minh*: các phòng học được phủ sóng Wi-Fi thuộc mạng LAN nhà trường có kết nối Internet cáp quang; nhà trường dùng *Google Workspace* để lưu trữ kế hoạch giảng dạy trên đám mây và lắp hệ thống *đèn hành lang IoT* tự bật sáng khi trời tối có người đi qua. Xét các nhận định sau:],
  [Nhờ mạng máy tính và Internet, giáo viên và học sinh trường THPT B có thể trao đổi học liệu số, nộp và chấm bài trực tuyến thuận tiện ngay cả ngoài giờ lên lớp.],
  [Hệ thống đèn hành lang IoT của trường bắt buộc phải có nhân viên bảo vệ đi bật từng công tắc bằng tay tại mỗi bóng đèn cứ 5 phút một lần thì mới gọi là IoT.],
  [Việc nhà trường lưu trữ biểu mẫu dùng chung trên đám mây giúp các tổ chuyên môn cùng cập nhật số liệu đồng thời theo thời gian thực mà không cần chép qua lại bằng USB thủ công.],
  [Vì mạng LAN của nhà trường đã kết nối ra Internet nên mạng Internet toàn cầu đương nhiên trở thành tài sản thuộc quyền sở hữu riêng của trường THPT B.],
)

==== PHẦN III. Tự luận (3,0 điểm: Câu 1 – Câu 3, mỗi câu 1,0 điểm)

- *Câu 1 (1,0 điểm – Vận dụng • Chủ đề A.1):* Một trường học cần sao lưu kho tư liệu video truyền thống gồm $20$ tệp video Full HD (mỗi tệp nặng $1.536 "MB"$) và $512$ bức ảnh tư liệu (mỗi bức ảnh nặng $4 "MB"$).
  a) Tính tổng dung lượng của toàn bộ kho tư liệu trên theo đơn vị Megabyte ($"MB"$) và đổi sang đơn vị Gigabyte ($"GB"$).
  b) Nhà trường dự định mua một chiếc USB dung lượng thực tế trống là $29 "GB"$ hoặc $58 "GB"$ để chứa trọn vẹn kho tư liệu trong một lần sao lưu. Nhà trường cần chọn loại USB nào và sau khi sao lưu xong USB đó còn trống bao nhiêu $"GB"$?
- *Câu 2 (1,0 điểm – Vận dụng • Chủ đề B.2):* Máy tính cá nhân ở nhà của bạn Linh dạo gần đây xuất hiện nhiều cửa sổ quảng cáo lạ, chạy rất chậm sau khi Linh cắm nhờ chiếc USB của người lạ ngoài tiệm in ấn. Em hãy hướng dẫn Linh: (a) Sử dụng công cụ thông dụng trên máy tính để kiểm tra, loại bỏ phần mềm độc hại; và (b) Các biện pháp tự bảo vệ dữ liệu học tập cá nhân lâu dài trên máy.
- *Câu 3 (1,0 điểm – Vận dụng cao • Chủ đề D.1):* Nhóm làm nội dung video của anh D thường xuyên dùng điện thoại lén quay lại cảnh sinh hoạt riêng tư của người đi đường kèm bình luận châm chọc ngoại hình của họ, đồng thời tải trọn bộ các ca khúc nhạc trẻ có bản quyền ghép vào video để đăng lên fanpage kiếm tiền quảng cáo mà không xin phép cả người trong video lẫn nhạc sĩ/ca sĩ. Hãy vận dụng kiến thức pháp luật môi trường số để phân tích đầy đủ các hành vi vi phạm của nhóm anh D, hậu quả pháp lí và đề xuất cách sáng tạo nội dung số hợp pháp, văn minh.

=== Đáp án & Biểu điểm chấm chi tiết – Đề thi thử số 02

==== 1. Phần I – Trắc nghiệm 4 lựa chọn (5,0 điểm: mỗi câu đúng 0,25 điểm)
#block(breakable: false)[
  #set text(size: 8.4pt)
  #table(
    columns: (1fr,) * 10,
    inset: 4.5pt,
    stroke: 0.45pt + c-border,
    align: center + horizon,
    fill: (x, y) => if calc.even(y) { c-teal-bg } else { white },
    [*1. B*], [*2. A*], [*3. B*], [*4. A*], [*5. A*], [*6. A*], [*7. A*], [*8. C*], [*9. A*], [*10. B*],
    [*11. A*], [*12. B*], [*13. A*], [*14. B*], [*15. B*], [*16. B*], [*17. A*], [*18. A*], [*19. B*], [*20. A*],
  )
]
*(Giải thích nhanh Câu 4: $1 "TB" = 1024 "GB" > 2 "GB" (= 2048 "MB") > 1500 "MB" > 2048 "KB" (= 2 "MB") arrow.r.double$ Thứ tự giảm dần: `(4) -> (1) -> (2) -> (3)`).*

==== 2. Phần II – Trắc nghiệm Đúng/Sai (2,0 điểm)
- *Câu 1 (Phần II):* *a) Đúng – b) Sai – c) Đúng – d) Sai* *(b sai vì Camera AI có cảm biến thu hình, chip AI xử lí nhận diện, bộ nhớ đệm và truyền dữ liệu mạng nên là hệ thống xử lí thông tin; d sai vì đầu đọc mã vạch chỉ là thiết bị thu nhận dữ liệu đầu vào đơn giản)*.
- *Câu 2 (Phần II):* *a) Đúng – b) Sai – c) Đúng – d) Sai* *(b sai vì đèn IoT tự động bật tắt qua cảm biến và bộ điều khiển không cần người bật tay 5 phút/lần; d sai vì Internet không thuộc sở hữu riêng của bất kì trường học hay tổ chức nào)*.

==== 3. Phần III – Tự luận (3,0 điểm)
- *Câu 1 (1,0 điểm):*
  - *a) (0,50đ):* Dung lượng $20$ tệp video: $20 times 1.536 = 30.720 "MB"$; dung lượng $512$ bức ảnh: $512 times 4 = 2.048 "MB"$. Tổng dung lượng kho tư liệu là: $30.720 + 2.048 = bold("32.768 MB")$ *(0,25đ)*. Đổi ra Gigabyte: $32.768 : 1024 = bold("32 GB")$ *(0,25đ)*.
  - *b) (0,50đ):* Vì $32 "GB" > 29 "GB"$ nên chiếc USB $29 "GB"$ không đủ chứa trọn kho tư liệu; nhà trường *bắt buộc phải chọn loại USB dung lượng trống $58 "GB"$* *(0,25đ)*. Sau khi sao lưu xong, dung lượng còn trống trên USB là: $58 - 32 = bold("26 GB")$ *(0,25đ)*.
- *Câu 2 (1,0 điểm):*
  - *a) Quy trình dùng công cụ loại bỏ phần mềm độc hại (0,50đ):* (1) Tạm ngắt mạng nếu nghi ngờ mã độc đang phát tán dữ liệu, mở công cụ *Windows Security (Microsoft Defender)* có sẵn trên Windows (hoặc phần mềm diệt virus uy tín như *Kaspersky, Bitdefender, Bkav* có cập nhật mẫu mới nhất); (2) Chạy chế độ *Quét toàn bộ hệ thống (Full Scan)* và *Quét ổ USB* để cách li, xóa sạch Virus/Adware/Spyware; (3) Kiểm tra mục *Apps & Extensions* trên trình duyệt để gỡ tiện ích quảng cáo lạ và cập nhật bản vá *Windows Update*, bật *Firewall*.
  - *b) Biện pháp tự bảo vệ dữ liệu cá nhân lâu dài (0,50đ):* (1) Thực hiện *sao lưu (Backup)* các tài liệu học tập quan trọng lên đám mây (*Google Drive / OneDrive*) và ổ lưu trữ dự phòng; (2) Luôn quét virus cho USB lạ trước khi mở tệp, tắt tính năng tự động chạy (*AutoPlay*); (3) Đặt mật khẩu mạnh và bật xác thực 2 yếu tố (2FA) cho các tài khoản cá nhân trên máy.
- *Câu 3 (1,0 điểm):*
  - *1. Kết luận tính pháp lí (0,25đ):* Hành vi của nhóm anh D là *vi phạm pháp luật kép* (cả về quyền nhân thân/đời tư công dân lẫn quyền sở hữu trí tuệ) và vi phạm nghiêm trọng văn hoá, đạo đức ứng xử trên không gian mạng.
  - *2. Phân tích rõ 2 nhóm hành vi vi phạm & căn cứ luật (0,25đ):*
    - *Hành vi 1 (Quay lén, đăng hình ảnh đời tư kèm lời châm chọc ngoại hình):* Xâm phạm quyền đối với hình ảnh và quyền về đời sống riêng tư (*Điều 32, Điều 38 Bộ luật Dân sự 2015*), đồng thời xúc phạm danh dự, nhân phẩm công dân bị cấm tại *Điều 12 Luật CNTT 2006*, *Luật An ninh mạng 2018* và *Nghị định 72/2013/NĐ-CP, Nghị định 15/2020/NĐ-CP*.
    - *Hành vi 2 (Sử dụng trái phép nhạc có bản quyền để kiếm tiền quảng cáo):* Xâm phạm *Quyền tác giả và quyền liên quan (quyền tài sản)* theo *Luật Sở hữu trí tuệ* và *Điều 12 Luật CNTT 2006*.
  - *3. Hậu quả pháp lí (0,25đ):* Fanpage bị đánh gậy bản quyền, tắt kiếm tiền hoặc khóa vĩnh viễn; nhóm anh D bị buộc gỡ video, xin lỗi công khai, *xử phạt hành chính*, và phải *bồi thường thiệt hại dân sự* cho cả những người bị quay lén lẫn chủ sở hữu bản quyền âm nhạc.
  - *4. Cách sáng tạo nội dung số hợp pháp, văn minh (0,25đ):* Phải xin phép sự đồng ý của nhân vật trước khi ghi hình và đăng tải, xây dựng nội dung nhân văn lành mạnh theo *Bộ Quy tắc ứng xử MXH (QĐ 874)*; sử dụng kho nhạc miễn phí bản quyền (*Creative Commons / Audio Library*) hoặc mua giấy phép sử dụng âm nhạc hợp pháp.
