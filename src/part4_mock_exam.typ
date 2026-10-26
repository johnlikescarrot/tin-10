#import "template.typ": *

= Phần IV. Đề kiểm tra thử Giữa kì I chuẩn 100% Ma trận & Đáp án

#block(
  width: 100%,
  stroke: 1pt + c-navy,
  radius: 5pt,
  inset: 10pt,
  fill: c-bg-soft,
  breakable: false,
  [
    #grid(
      columns: (1fr, 1.2fr),
      align: (center + horizon, center + horizon),
      [
        *TRƯỜNG THPT ..............................* \
        *TỔ TIN HỌC* \
        #line(length: 45%, stroke: 0.6pt + c-navy)
      ],
      [
        *ĐỀ KIỂM TRA ĐÁNH GIÁ GIỮA HỌC KÌ I* \
        *Môn: TIN HỌC 10 – ĐỊNH HƯỚNG ICT* \
        _Bộ sách: Kết nối tri thức với cuộc sống_ \
        *Thời gian làm bài: 45 phút* _(không kể thời gian phát đề)_
      ],
    )
    #v(4pt)
    #line(length: 100%, stroke: 0.5pt + c-border)
    #v(2pt)
    *Họ và tên thí sinh:* ........................................................................ *Lớp:* 10....... *Số báo danh:* ....................
  ],
)

== PHẦN I. Câu trắc nghiệm nhiều lựa chọn (5,0 điểm)
_Thí sinh trả lời từ Câu 1 đến Câu 20 (mỗi câu đúng được 0,25 điểm). Mỗi câu hỏi thí sinh chỉ chọn một phương án._

// Câu 1: A (A.1 - NB)
#mcq(1, "NB",
  [Trong các đơn vị đo dung lượng thông tin sau đây, đơn vị nào có giá trị quy đổi bằng $1024 "MB"$?],
  [1 Gigabyte (GB).], [1 Kilobyte (KB).], [1 Byte (B).], [1 Terabyte (TB).],
  cols: 4
)

// Câu 2: D (A.1 - NB)
#mcq(2, "NB",
  [Nhận định nào sau đây nêu đúng ưu điểm vượt trội của việc lưu trữ dữ liệu trên thiết bị số (như ổ cứng SSD, thẻ nhớ)?],
  [Chỉ cho phép đọc dữ liệu một lần duy nhất rồi tự hủy.],
  [Kích thước cồng kềnh và tốn diện tích kho bãi hơn sách giấy.],
  [Không thể sao chép hay gửi dữ liệu đi xa qua mạng.],
  [Gọn nhẹ, lưu trữ dung lượng lớn, tìm kiếm nhanh và dễ dàng sao chép, truyền tải.],
  cols: 1
)

// Câu 3: C (A.1 - TH)
#mcq(3, "TH",
  [Bác sĩ xem phim chụp X-quang phổi và bảng chỉ số xét nghiệm máu của bệnh nhân trên màn hình máy tính, từ đó kết luận bệnh nhân bị viêm phế quản nhẹ. Trong tình huống này, *kết luận bệnh nhân bị viêm phế quản nhẹ* là gì?],
  [Vật mang tin.], [Thiết bị đầu vào.], [Thông tin.], [Bộ nhớ ngoài.],
  cols: 4
)

// Câu 4: B (A.1 - TH)
#mcq(4, "TH",
  [Phát biểu nào sau đây phân biệt *ĐÚNG* giữa dữ liệu và thông tin?],
  [Dữ liệu chỉ tồn tại trong đầu con người, còn thông tin là chiếc USB chứa tệp.],
  [Dữ liệu là hình thức biểu diễn (chữ, số, hình ảnh, âm thanh,...), còn thông tin là ý nghĩa, sự hiểu biết rút ra từ dữ liệu.],
  [Mọi dữ liệu chỉ mang lại duy nhất một thông tin giống hệt nhau cho tất cả mọi người.],
  [Thông tin không thể biểu diễn bằng nhiều dạng dữ liệu khác nhau.],
  cols: 1
)

// Câu 5: A (A.2 - NB)
#mcq(5, "NB",
  [Ngoài máy tính để bàn (PC) và máy tính xách tay (Laptop), thiết bị nào sau đây là *thiết bị số thông minh* phổ biến trong đời sống hiện nay?],
  [Máy tính bảng (Tablet) và điện thoại thông minh (Smartphone).],
  [Bàn là điện cơ điều chỉnh nhiệt bằng núm xoay cơ học.],
  [Quạt trần điện cơ thông thường.],
  [Thước kẻ nhựa học sinh.],
  cols: 2
)

// Câu 6: C (A.2 - NB)
#mcq(6, "NB",
  [Đóng góp cơ bản nào sau đây của ngành Tin học thể hiện rõ nét nhất trong lĩnh vực *quản lí hành chính nhà nước*?],
  [Chế tạo phân bón hóa học cho cây lúa.],
  [Xây dựng cầu bê tông cốt thép vượt sông.],
  [Triển khai Chính phủ điện tử, định danh điện tử và cổng dịch vụ công trực tuyến cho người dân.],
  [Khai thác quặng sắt trong hầm lò thủ công.],
  cols: 1
)

// Câu 7: D (A.2 - NB)
#mcq(7, "NB",
  [Mạng máy tính *ARPANET* – tiền thân trực tiếp của mạng Internet ngày nay – được ra đời vào năm nào?],
  [Năm 1945.], [Năm 1956.], [Năm 1998.], [Năm 1969.],
  cols: 4
)

// Câu 8: B (A.2 - NB)
#mcq(8, "NB",
  [Năm 1997, siêu máy tính nào của hãng IBM đã giành chiến thắng trước đại kiện tướng cờ vua thế giới Garry Kasparov?],
  [ENIAC.], [Deep Blue.], [ELIZA.], [ASIMO.],
  cols: 4
)

// Câu 9: C (B.1 - NB)
#mcq(9, "NB",
  [Ứng dụng nào sau đây là dịch vụ soạn thảo và lưu trữ trực tuyến dựa trên công nghệ *Điện toán đám mây (Cloud Computing)*?],
  [Notepad cài cục bộ trên Windows XP.],
  [Máy tính bỏ túi cầm tay.],
  [Google Docs và OneDrive.],
  [Phần mềm Paint ngoại tuyến.],
  cols: 2
)

// Câu 10: A (B.1 - NB)
#mcq(10, "NB",
  [Thuật ngữ viết tắt *IoT* trong lĩnh vực mạng và công nghệ số có nghĩa tiếng Việt là gì?],
  [Internet vạn vật.], [Mạng cục bộ nội bộ.], [Trí tuệ nhân tạo.], [Thương mại điện tử.],
  cols: 4
)

// Câu 11: D (B.1 - NB)
#mcq(11, "NB",
  [Thiết bị kết nối mạng nào thường dùng để nối các máy tính và máy in trong cùng một mạng cục bộ (LAN) quy mô phòng học hoặc văn phòng?],
  [Tai nghe Bluetooth.], [Màn hình LCD.], [Máy quét mã vạch.], [Bộ chuyển mạch (Switch).],
  cols: 2
)

// Câu 12: B (B.1 - NB)
#mcq(12, "NB",
  [Theo phạm vi địa lí, hai loại mạng máy tính thường gặp nhất được phân chia trong bài học là gì?],
  [Mạng âm thanh và mạng hình ảnh.],
  [Mạng cục bộ (LAN) và mạng toàn cầu (Internet / WAN).],
  [Mạng bàn phím và mạng màn hình.],
  [Mạng phần mềm và mạng ổ cứng.],
  cols: 2
)

// Câu 13: A (B.2 - NB)
#mcq(13, "NB",
  [Loại phần mềm độc hại nào là một *phần mềm hoàn chỉnh*, có khả năng tự nhân bản và tự động lây lan nhanh qua mạng máy tính mà không cần gắn vào tệp vật chủ?],
  [Sâu máy tính (Worm).], [Trình duyệt Chrome.], [Học liệu mở OER.], [Google Dịch.],
  cols: 2
)

// Câu 14: C (B.2 - NB)
#mcq(14, "NB",
  [Hành động nào sau đây là *KHÔNG NÊN LÀM* khi em bị một tài khoản lạ nhắn tin xúc phạm, bắt nạt trên mạng xã hội?],
  [Chụp ảnh màn hình tin nhắn để lưu giữ bằng chứng.],
  [Sử dụng chức năng Chặn (Block) và Báo cáo vi phạm (Report).],
  [Nhắn tin chửi bới gay gắt đáp trả và hẹn gặp đánh nhau bên ngoài.],
  [Chia sẻ sự việc với cha mẹ hoặc giáo viên chủ nhiệm để được hỗ trợ.],
  cols: 1
)

// Câu 15: D (B.2 - NB)
#mcq(15, "NB",
  [Tác hại nào sau đây có thể xảy ra nếu người dùng nghiện trò chơi trực tuyến và sử dụng Internet thiếu kiểm soát nhiều giờ liền mỗi đêm?],
  [Giúp tăng cường thị lực và chiều cao vượt trội.],
  [Giúp máy tính tự động diệt sạch mọi loại mã độc.],
  [Giúp tiết kiệm tối đa hóa đơn tiền điện hằng tháng.],
  [Suy giảm sức khỏe thể chất, tinh thần, rối loạn giấc ngủ và sa sút kết quả học tập.],
  cols: 1
)

// Câu 16: B (B.2 - NB)
#mcq(16, "NB",
  [Hình thức tấn công mạng mà kẻ gian lập ra các trang web hoặc email *giả mạo ngân hàng, cơ quan uy tín* để lừa người dùng nhập mật khẩu, mã OTP gọi là gì?],
  [Sao lưu đám mây (Cloud Backup).],
  [Lừa đảo trực tuyến (Phishing).],
  [Khai thác học liệu mở (OER).],
  [Cập nhật bản vá bảo mật (Update).],
  cols: 2
)

// Câu 17: C (D.1 - NB)
#mcq(17, "NB",
  [Văn bản pháp luật nào của Việt Nam quy định các hành vi bị nghiêm cấm trong hoạt động ứng dụng và phát triển công nghệ thông tin (tại Điều 12)?],
  [Luật Lâm nghiệp.], [Luật Thủy sản.], [Luật Công nghệ thông tin.], [Luật Du lịch.],
  cols: 2
)

// Câu 18: A (D.1 - NB)
#mcq(18, "NB",
  [Theo quy định của *Luật An ninh mạng*, hành vi nào sau đây bị pháp luật *nghiêm cấm*?],
  [Đăng tải thông tin bịa đặt, sai sự thật gây hoang mang trong nhân dân hoặc tấn công, phát tán mã độc trên không gian mạng.],
  [Tham khảo sách giáo khoa điện tử trên trang Hành trang số của Nhà xuất bản Giáo dục.],
  [Sử dụng mật khẩu mạnh và xác thực hai yếu tố cho tài khoản cá nhân.],
  [Báo cáo các trang web lừa đảo cho cơ quan chức năng có thẩm quyền.],
  cols: 1
)

// Câu 19: D (D.1 - TH)
#mcq(19, "TH",
  [Bạn V tải một bức ảnh nghệ thuật có đăng kí bản quyền của một nhiếp ảnh gia về máy, dùng phần mềm xóa chữ kí tên tác giả trên góc ảnh rồi gửi dự thi cuộc thi ảnh của trường dưới tên của chính mình. Hành vi của V đã vi phạm điều gì?],
  [Không vi phạm gì vì bức ảnh được đăng trên mạng Internet nên ai cũng được lấy làm của mình.],
  [Chỉ vi phạm quy tắc đặt tên tệp tin của hệ điều hành Windows.],
  [Là hành vi hợp pháp đáng khích lệ vì giúp bức ảnh được nhiều người biết đến hơn.],
  [Vi phạm quyền tác giả (cả quyền nhân thân và quyền tài sản) theo quy định của Luật Sở hữu trí tuệ.],
  cols: 1
)

// Câu 20: C (D.1 - TH)
#mcq(20, "TH",
  [Để nâng cao tính an toàn và hợp pháp khi chia sẻ thông tin trong môi trường số, mỗi học sinh cần thực hiện thói quen nào sau đây?],
  [Chia sẻ ngay lập tức mọi tin đồn giật gân chưa rõ nguồn gốc để cảnh báo bạn bè.],
  [Tự ý đăng tải bảng điểm, địa chỉ nhà và ảnh riêng tư của bạn cùng lớp khi chưa xin phép.],
  [Kiểm chứng độ tin cậy của nguồn tin trước khi chia sẻ, tôn trọng bản quyền và quyền riêng tư của người khác.],
  [Dùng phần mềm bẻ khóa (Crack) chia sẻ lên hội nhóm để tiết kiệm chi phí cho mọi người.],
  cols: 1
)

== PHẦN II. Câu trắc nghiệm Đúng/Sai (2,0 điểm)
_Thí sinh trả lời Câu 1 và Câu 2. Trong mỗi ý *a), b), c), d)* ở mỗi câu, thí sinh chọn *Đúng* hoặc *Sai*._

#tfq(1, "Câu 1 • Chủ đề A.2 (1,0 điểm)",
  [Gia đình bác An lắp đặt hệ thống *điều hòa thông minh* và *camera an ninh AI* kết nối Wi-Fi với điện thoại thông minh của bác, đồng thời trong phòng bếp có một chiếc *lò vi sóng cơ* chỉnh thời gian bằng núm vặn cơ học.],
  [Điện thoại thông minh và camera an ninh AI đều là các hệ thống xử lí thông tin vì có cảm biến/ống kính thu nhận dữ liệu đầu vào, vi xử lí phân tích, bộ nhớ lưu trữ và đưa cảnh báo ra màn hình/loa.], "TH",
  [Chiếc lò vi sóng cơ chỉ có núm vặn hẹn giờ cơ học, không kết nối mạng và không có phần mềm tự thích ứng cũng được xếp vào nhóm thiết bị thông minh của CMCN 4.0.], "TH",
  [Khi bác An đang làm việc ở cơ quan cách nhà 15 km, bác mở ứng dụng trên điện thoại có kết nối Internet để bật sẵn điều hòa trước khi về 10 phút là ứng dụng thực tế vai trò của thiết bị thông minh trong đời sống hiện đại.], "VD",
  [Nếu camera an ninh AI phát hiện có người lạ cạy cửa ban đêm, thiết bị tự động bật còi báo động tại chỗ và gửi ngay đoạn video cảnh báo về điện thoại cho bác An kịp thời xử lí.], "VD"
)

#tfq(2, "Câu 2 • Chủ đề B.1 (1,0 điểm)",
  [Một công ty thiết kế đồ họa kết nối 25 máy tính làm việc trong tòa nhà văn phòng thành một mạng cục bộ (*LAN*), đồng thời thuê gói đường truyền cáp quang để kết nối *Internet* và sử dụng dịch vụ lưu trữ đám mây *OneDrive* cho nhân viên làm việc nhóm.],
  [Mạng LAN của công ty có phạm vi trong tòa nhà văn phòng và thuộc quyền sở hữu, quản trị của chính công ty đó; trái lại mạng Internet có phạm vi toàn cầu và không thuộc sở hữu của riêng cá nhân hay tổ chức nào.], "TH",
  [Dịch vụ lưu trữ đám mây OneDrive bắt buộc nhân viên chỉ mở được tệp thiết kế trên đúng 01 chiếc máy tính cố định duy nhất tại bàn làm việc ở công ty, không thể truy cập từ laptop ở nhà.], "TH",
  [Khi nhân viên thiết kế đi gặp khách hàng bên ngoài, họ có thể dùng máy tính bảng kết nối 4G/5G đăng nhập tài khoản OneDrive để trình chiếu ngay bản vẽ mới nhất vừa được đồng nghiệp cập nhật tại văn phòng.], "VD",
  [Trong trường hợp đường cáp quang Internet bên ngoài tòa nhà gặp sự cố mất kết nối, các máy tính trong văn phòng vẫn có thể chia sẻ tệp qua mạng LAN nội bộ và in tài liệu qua máy in mạng trong phòng.], "VD"
)

== PHẦN III. Câu hỏi Tự luận (3,0 điểm)

*Câu 1 (1,0 điểm – Mức độ Thông hiểu – Chủ đề B.2):* \
Tham gia môi trường mạng Internet mang lại nhiều lợi ích học tập nhưng cũng tiềm ẩn không ít rủi ro mất an toàn. Em hãy trình bày *04 cách cụ thể để đề phòng những tác hại khi tham gia các hoạt động trên Internet* và bảo vệ an toàn dữ liệu cá nhân của mình.

*Câu 2 (1,0 điểm – Mức độ Vận dụng – Chủ đề A.1):* \
Ổ đĩa lưu trữ đám mây phục vụ học tập của bạn Khoa hiện còn trống dung lượng khả dụng là `4 GB`. Bạn Khoa tải lên ổ đĩa đó `1` tệp video bài giảng Tin học nặng `1,5 GB` và `256` tệp tài liệu PDF (trung bình mỗi tệp PDF nặng `2 MB`).
a) Hỏi sau khi tải lên toàn bộ các tệp nói trên, ổ đĩa của Khoa còn trống bao nhiêu `MB`? _(Cho biết $1 "GB" = 1024 "MB"$)._
b) Phần dung lượng trống còn lại đó có thể lưu thêm tối đa bao nhiêu tệp ghi âm bài nghe tiếng Anh, biết mỗi tệp ghi âm có dung lượng `8 MB`?

*Câu 3 (1,0 điểm – Mức độ Vận dụng cao – Chủ đề D.1):* \
_Tình huống:_ Thấy một trung tâm luyện thi uy tín vừa phát hành bộ sách điện tử (E-book) và video bài giảng có đăng kí bản quyền giá 600.000 đồng, bạn D đã mua 01 tài khoản học tập hợp pháp. Tuy nhiên sau đó, D tự ý tải toàn bộ video và E-book về máy, xóa logo bản quyền của trung tâm rồi lập một nhóm kín trên mạng xã hội để bán lại trọn bộ tài liệu đó cho nhiều người khác với giá 50.000 đồng/người nhằm thu lợi riêng. \
Vận dụng các kiến thức pháp luật trong môi trường số đã học (*Luật Sở hữu trí tuệ, Luật Công nghệ thông tin, Luật An ninh mạng, Nghị định về quản lí Internet*), em hãy xác định hành vi của bạn D có hợp pháp không? Giải thích rõ lí do, nêu hậu quả có thể xảy ra và đưa ra lời khuyên đúng pháp luật cho D.

#v(6pt)
#align(center)[*— HẾT ĐỀ KIỂM TRA —*]

== ĐÁP ÁN & HƯỚNG DẪN CHẤM ĐỀ KIỂM TRA THỬ GIỮA KÌ I

=== 1. Đáp án Phần I – Trắc nghiệm nhiều lựa chọn (5,0 điểm – Mỗi câu đúng 0,25 điểm)

#table(
  columns: (1fr,) * 10,
  inset: 5pt,
  align: center + horizon,
  stroke: 0.5pt + c-border,
  fill: (_, row) => if calc.even(row) { c-navy-light } else { white },
  [*1. A*], [*2. D*], [*3. C*], [*4. B*], [*5. A*], [*6. C*], [*7. D*], [*8. B*], [*9. C*], [*10. A*],
  [*11. D*], [*12. B*], [*13. A*], [*14. C*], [*15. D*], [*16. B*], [*17. C*], [*18. A*], [*19. D*], [*20. C*],
)
_(Kiểm chứng phân bố đáp án chuẩn: 5 câu A, 5 câu B, 5 câu C, 5 câu D; đúng 16 câu Nhận biết + 4 câu Thông hiểu khớp 100% Ma trận)._

=== 2. Đáp án Phần II – Trắc nghiệm Đúng/Sai (2,0 điểm – Mỗi câu tối đa 1,0 điểm)
_Quy tắc tính điểm mỗi câu: Đúng 1 ý được `0,1 điểm`; đúng 2 ý được `0,25 điểm`; đúng 3 ý được `0,5 điểm`; đúng cả 4 ý được `1,0 điểm`._
- *Câu 1 (Chủ đề A.2):* *a) Đúng* — *b) Sai* _(lò vi sóng cơ thông thường không kết nối mạng, không tự chủ thông minh)_ — *c) Đúng* — *d) Đúng*.
- *Câu 2 (Chủ đề B.1):* *a) Đúng* — *b) Sai* _(ưu điểm cốt lõi của Điện toán đám mây là truy cập mọi lúc, mọi nơi trên mọi thiết bị có Internet)_ — *c) Đúng* — *d) Đúng*.

=== 3. Hướng dẫn chấm Phần III – Tự luận (3,0 điểm)

#table(
  columns: (0.6fr, 3.6fr, 0.8fr),
  inset: 6pt,
  align: (center + horizon, left + top, center + horizon),
  stroke: 0.5pt + c-border,
  fill: (_, row) => if row == 0 { c-navy-light } else { white },
  table.header([*Câu*], [*Nội dung đáp án & Yêu cầu cần đạt*], [*Điểm*]),
  [*Câu 1* \ _(1,0đ)_ \ _TH – B.2_],
  [
    Học sinh nêu đúng, rõ ràng 04 biện pháp thiết thực đề phòng tác hại trên Internet và bảo vệ dữ liệu cá nhân (mỗi ý đúng được `0,25 điểm`):
    - *Ý 1 – Bảo mật tài khoản truy cập:* Đặt mật khẩu mạnh (tối thiểu 8 kí tự gồm chữ hoa, chữ thường, số, kí tự đặc biệt), bật xác thực 2 yếu tố (2FA) và luôn đăng xuất khi sử dụng máy tính công cộng.
    - *Ý 2 – Phòng chống phần mềm độc hại & lừa đảo:* Cài đặt, bật và cập nhật thường xuyên phần mềm diệt virus / tường lửa (*Windows Security/Defender,...*); tuyệt đối không nhấp vào đường link lạ, email giả mạo (*Phishing*) và không tải tệp/phần mềm bẻ khóa không rõ nguồn gốc.
    - *Ý 3 – Tự bảo vệ thông tin riêng tư & dữ liệu quan trọng:* Không đăng công khai thông tin nhạy cảm (CCCD, mật khẩu, mã OTP, địa chỉ riêng); sao lưu dữ liệu học tập quan trọng định kì lên đám mây hoặc ổ cứng ngoài.
    - *Ý 4 – Khai thác mạng văn minh, điều độ và biết tự vệ:* Kiểm chứng thông tin từ nguồn chính thống trước khi tin/chia sẻ; giới hạn thời gian dùng mạng hợp lí; khi gặp bắt nạt/lừa đảo trên mạng cần lưu bằng chứng, chặn tài khoản và báo ngay cho cha mẹ, thầy cô.
  ],
  [*1,0 điểm* \ _(4 × 0,25đ)_],

  [*Câu 2* \ _(1,0đ)_ \ _VD – A.1_],
  [
    - *a) Tính phần dung lượng trống còn lại theo `MB` (0,5 điểm):*
      + Đổi dung lượng khả dụng ban đầu và dung lượng tệp video sang `MB`: \
        $4 "GB" = 4 times 1024 = 4096 " (MB)"$; $quad 1,5 "GB" = 1,5 times 1024 = 1536 " (MB)"$. _(0,25đ)_
      + Tổng dung lượng của `256` tệp PDF là: $256 times 2 = 512 " (MB)"$. \
        Dung lượng trống còn lại trên ổ đĩa là: $4096 - (1536 + 512) = 4096 - 2048 = 2048 " (MB)"$. _(0,25đ)_
    - *b) Tính số tệp ghi âm tối đa lưu thêm được (0,5 điểm):*
      + Số tệp ghi âm tối đa lưu thêm được vào `2048 MB` trống là: \
        $2048 : 8 = 256 " (tệp ghi âm)"$. _(0,5đ)_
  ],
  [*1,0 điểm* \ _(0,5đ + 0,5đ)_],

  [*Câu 3* \ _(1,0đ)_ \ _VDC – D.1_],
  [
    - *Bước 1 – Kết luận tính pháp lí:* Khẳng định hành vi tự ý tải, xóa logo bản quyền và rao bán lại bộ E-book, video bài giảng của bạn D là *KHÔNG HỢP PHÁP (Vi phạm pháp luật nghiêm trọng)*. _(0,25đ)_
    - *Bước 2 – Giải thích căn cứ pháp lí:* Dù D mua tài khoản học hợp pháp nhưng D chỉ có *quyền sử dụng cá nhân* theo điều khoản cấp phép, không có quyền tác giả. Việc xóa logo tác giả, sao chép và bán lại thu lợi bất chính đã xâm phạm *quyền nhân thân* (bảo vệ sự toàn vẹn tác phẩm, đứng tên) và *quyền tài sản* (sao chép, phân phối thương mại) theo *Luật Sở hữu trí tuệ*, đồng thời vi phạm *Điều 12 Luật Công nghệ thông tin* (và các quy định quản lí thông tin trên mạng tại *Nghị định 72/2013/NĐ-CP*, *Luật An ninh mạng*). _(0,25đ)_
    - *Bước 3 – Nêu hậu quả:* Gây thất thoát doanh thu và uy tín của trung tâm luyện thi; bạn D sẽ bị khóa tài khoản học, bị xử lí kỉ luật, buộc nộp lại số tiền thu lợi bất chính, bồi thường thiệt hại dân sự và bị xử phạt hành chính (thậm chí xử lí hình sự nếu quy mô thu lợi bất chính lớn). _(0,25đ)_
    - *Bước 4 – Lời khuyên đúng pháp luật:* D phải dừng ngay việc rao bán, giải tán nhóm chia sẻ lậu, xóa các bản sao trái phép, chủ động xin lỗi và khắc phục hậu quả với trung tâm; chỉ sử dụng tài khoản đúng mục đích tự học cá nhân hoặc giới thiệu bạn bè đăng kí chính thức / sử dụng các *nguồn học liệu mở (OER)* miễn phí hợp pháp. _(0,25đ)_
  ],
  [*1,0 điểm* \ _(4 × 0,25đ)_],
)

#v(8pt)

#callout(
  title: "BẢNG TỔNG KẾT 10 ĐIỂM VÀNG SOÁT NHANH 5 PHÚT CUỐI TRƯỚC GIỜ THI",
  tag: "TỔNG KẾT",
  accent: c-navy,
  bg: c-navy-light,
  breakable-box: false,
)[
  1. *Bộ ba khái niệm Bài 1:* *Vật mang tin* = phương tiện chứa (giấy, USB, ổ cứng) • *Dữ liệu* = chữ, số, hình, âm biểu diễn • *Thông tin* = ý nghĩa, hiểu biết rút ra.
  2. *Đổi đơn vị chuẩn nhị phân:* $1 "Byte" = 8 "bit"$; các bậc liền kề $"B" arrow.l.r "KB" arrow.l.r "MB" arrow.l.r "GB" arrow.l.r "TB"$ nhân/chia *$1024$* ($2^(10)$). Tính số tệp hoàn chỉnh nhớ *lấy phần nguyên*; đổi tốc độ mạng `Mbps` sang `MB/s` nhớ *chia cho 8*.
  3. *Thiết bị thông minh (Bài 2):* Có vi xử lí + phần mềm hoạt động *tự chủ nhất định* + *kết nối mạng* (Smartphone, Smartwatch, Robot hút bụi, Camera AI). _Máy tính bỏ túi Casio cơ bản KHÔNG phải thiết bị thông minh!_
  4. *Mốc lịch sử cần thuộc lòng:* *ENIAC* (1945–1946) • *AI Dartmouth* (1956) • *ELIZA* (1965) • *ARPANET* (1969) • *TCP/IP* (1983) • *WWW – Tim Berners-Lee* (1989–1991) • *Deep Blue & Internet VN* (1997) • *ASIMO* (2000) • *AlphaGo* (2016).
  5. *So sánh LAN và Internet (Bài 8):* *LAN* = phạm vi hẹp, *có chủ sở hữu xác định*, an toàn nội bộ cao; *Internet* = phạm vi toàn cầu, *không thuộc sở hữu của bất kì ai*, môi trường mở nhiều nguy cơ.
  6. *Điện toán đám mây & IoT:* *SaaS* cung cấp phần mềm cho người dùng cuối (_Google Drive, Docs, Gmail, OneDrive_); *IoT* liên kết đồ vật gắn cảm biến qua Internet tự động thu thập và trao đổi dữ liệu (_Smart Home, thu phí ETC, nông nghiệp thông minh_).
  7. *Phân biệt 3 mã độc (Bài 9):* *Virus* = kí sinh tệp vật chủ (chưa phải phần mềm hoàn chỉnh) • *Worm (Sâu)* = phần mềm hoàn chỉnh tự nhân bản qua mạng • *Trojan* = ngụy trang phần mềm tốt lừa cài đặt để ăn cắp dữ liệu.
  8. *Phòng vệ bắt nạt trên mạng (K–L–C–B):* *Không đáp trả* nóng giận $arrow.r$ *Lưu bằng chứng* (chụp màn hình) $arrow.r$ *Chặn & Báo cáo* $arrow.r$ *Báo ngay cha mẹ, thầy cô / Công an*.
  9. *Dịch vụ Web & Học liệu mở (Bài 10):* Công cụ dịch tự động (*Google Dịch*: văn bản, tiếng nói, ảnh, tệp, web); Học liệu mở OER miễn phí hợp pháp (*Hệ tri thức Việt số hóa `itrithuc.vn`, Hành trang số, Khan Academy*).
  10. *Công thức 4 bước câu Pháp luật Vận dụng cao (Bài 11):* *Kết luận Hợp pháp/Bất hợp pháp* $arrow.r$ *Viện dẫn Luật SHTT / Luật CNTT (Đ.12) / Luật An ninh mạng (Đ.8) / NĐ 72 & NĐ 15* $arrow.r$ *Phân tích hậu quả* $arrow.r$ *Đề xuất cách khắc phục đúng luật*.
]

