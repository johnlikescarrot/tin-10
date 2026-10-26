#import "theme.typ": *

= PHẦN V. BỘ 02 ĐỀ THI THỬ CHUẨN MA TRẬN KÈM ĐÁP ÁN & HƯỚNG DẪN CHẤM

== 5.1. ĐỀ THI THỬ GIỮA HỌC KÌ I — ĐỀ SỐ 01

#block(
  width: 100%,
  fill: c-bg-soft,
  stroke: 0.7pt + c-navy,
  radius: 5pt,
  inset: (x: 12pt, y: 9pt),
  breakable: false,
  [
    #grid(
      columns: (1fr, 1.3fr),
      align: (center + horizon, center + horizon),
      [
        *TRƯỜNG THPT ........................*\
        *TỔ TIN HỌC*\
        _(Đề thi thử chuẩn Ma trận — Số 01)_
      ],
      [
        *ĐỀ KIỂM TRA GIỮA HỌC KÌ I*\
        *MÔN: TIN HỌC 10 — ĐỊNH HƯỚNG ICT*\
        _Thời gian làm bài: 45 phút (không kể thời gian phát đề)_
      ],
    )
  ],
)

=== PHẦN I. Trắc nghiệm nhiều phương án lựa chọn (5,0 điểm)
_Thí sinh trả lời từ Câu 1 đến Câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án đúng (0,25 điểm/câu)._

#mcq("1", "Nhận biết",
  [Trong các thiết bị sau, thiết bị nào cho phép lưu trữ dữ liệu số với dung lượng lớn, nhỏ gọn và dễ dàng mang theo?],
  [Tờ giấy viết tay.], [Ổ đĩa USB Flash (hoặc thẻ nhớ).], [Bảng phấn đen.], [Bàn phím cơ học.]
)

#mcq("2", "Nhận biết",
  [Một Byte (`1 B`) tương ứng với bao nhiêu bit?],
  [$2$ bit.], [$4$ bit.], [$8$ bit.], [$1024$ bit.]
)

#mcq-stack("3", "Thông hiểu",
  [Trên tấm biển báo giao thông đường bộ có hình vẽ chiếc còi xe nằm trong vòng tròn đỏ gạch chéo. Nhận định nào sau đây là *đúng*?],
  [Hình vẽ trên biển báo là *thông tin*, còn tấm biển kim loại là *tri thức*.],
  [Hình vẽ trên biển báo là *dữ liệu*, còn điều người lái xe hiểu được *"Đoạn đường cấm bóp còi"* là *thông tin*.],
  [Tấm biển kim loại là *thông tin*, còn tiếng còi xe là *vật mang tin*.],
  [Hình vẽ trên biển báo không mang lại bất kì thông tin nào cho người tham gia giao thông.]
)

#mcq("4", "Thông hiểu",
  [Một tệp âm thanh chất lượng cao có dung lượng $10" MB"$. Dung lượng tệp đó tính theo đơn vị Kilobyte (`KB`) là:],
  [$1000" KB"$.], [$1024" KB"$.], [$10.240" KB"$.], [$80" KB"$.]
)

#mcq("5", "Nhận biết",
  [Lĩnh vực ứng dụng nào sau đây thể hiện đóng góp của Tin học trong *quản lí hành chính nhà nước hiện đại*?],
  [Ghi sổ hộ khẩu hoàn toàn bằng bút mực truyền thống.],
  [Triển khai Cổng Dịch vụ công Quốc gia và Chính phủ điện tử.],
  [Vận chuyển công văn liên tỉnh bằng ngựa trạm.],
  [Đóng gạch thủ công ngoài đồng ruộng.]
)

#mcq("6", "Nhận biết",
  [Trong các thiết bị sau đây, thiết bị nào là *thiết bị số* thông dụng hỗ trợ đọc tài liệu điện tử chuyên biệt?],
  [Máy đọc sách điện tử (E-reader).], [Ấm đun nước siêu tốc cơ học.], [Đèn bàn học sợi đốt.], [Quạt hộp điện cơ.]
)

#mcq("7", "Nhận biết",
  [Mạng *ARPANET* — tiền thân trực tiếp của mạng Internet ngày nay — được ra đời vào năm nào?],
  [Năm 1850.], [Năm 1969.], [Năm 2007.], [Năm 2020.]
)

#mcq("8", "Nhận biết",
  [Linh kiện điện tử đặc trưng tạo nên máy tính điện tử *thế hệ thứ hai* (giai đoạn khoảng 1955–1965) là gì?],
  [Đèn điện tử chân không.], [Bóng bán dẫn (Transistor).], [Bánh răng cơ khí bằng đồng.], [Bàn tính gảy hạt gỗ.]
)

#mcq("9", "Nhận biết",
  [Trong các dịch vụ dưới đây, dịch vụ nào *KHÔNG* phải là dịch vụ Điện toán đám mây?],
  [Google Drive.], [Microsoft OneDrive.], [Dropbox.], [Phần mềm Paint chạy ngoại tuyến không nối mạng.]
)

#mcq-stack("10", "Nhận biết",
  [Hệ thống kết nối các thiết bị, đồ vật gắn cảm biến để tự động thu thập và trao đổi dữ liệu với nhau qua Internet được gọi là:],
  [Mạng cục bộ phòng máy (LAN).],
  [Internet vạn vật (IoT — Internet of Things).],
  [Bảng mã kí tự ASCII.],
  [Phần mềm gõ tiếng Việt.]
)

#mcq("11", "Nhận biết",
  [Thiết bị mạng nào thường được dùng để kết nối các máy tính với nhau tạo thành một mạng cục bộ (*LAN*) có dây?],
  [Bộ chuyển mạch (Switch).], [Máy in phun màu.], [Loa vi tính.], [Máy chiếu (Projector).]
)

#mcq("12", "Nhận biết",
  [Tổ chức cung cấp dịch vụ kết nối Internet cho các hộ gia đình và doanh nghiệp (như VNPT, Viettel, FPT) được viết tắt là gì?],
  [CPU.], [RAM.], [ISP.], [USB.]
)

#mcq-stack("13", "Nhận biết",
  [Chương trình máy tính được viết ra với ý đồ xấu nhằm phá hoại hệ thống, đánh cắp dữ liệu hoặc chiếm quyền điều khiển thiết bị gọi chung là gì?],
  [Phần mềm hệ thống.], [Phần mềm nguồn mở.], [Phần mềm độc hại (Malware).], [Phần mềm học liệu mở.]
)

#mcq-stack("14", "Nhận biết",
  [Nguy cơ nào sau đây có thể xảy ra nếu học sinh tham gia mạng xã hội một cách bất cẩn, thường xuyên nhấp vào các đường link lạ chưa kiểm chứng?],
  [Tài khoản được mạng xã hội tự động nâng cấp bảo mật tuyệt đối.],
  [Bị lừa đảo đánh cắp mật khẩu tài khoản (Phishing) hoặc lây nhiễm mã độc vào thiết bị.],
  [Dung lượng RAM vật lí của điện thoại tự động tăng gấp đôi.],
  [Tốc độ sạc pin của điện thoại nhanh hơn.]
)

#mcq-stack("15", "Nhận biết",
  [Khi bị một nhóm tài khoản lạ liên tục nhắn tin đe dọa, tung ảnh ghép xúc phạm trên mạng xã hội, học sinh nên ưu tiên thực hiện việc làm nào trước tiên?],
  [Nhắn tin chửi bới gay gắt lại cả nhóm đó.],
  [Xóa hết tin nhắn ngay lập tức mà không lưu bằng chứng rồi âm thầm chịu đựng một mình.],
  [Không đáp trả, chụp màn hình lưu bằng chứng, chặn/báo cáo vi phạm và báo ngay cho cha mẹ, thầy cô giáo.],
  [Chuyển tiền vào tài khoản của nhóm đó theo lời đe dọa.]
)

#mcq("16", "Thông hiểu",
  [Để dịch nhanh một đoạn văn bản tiếng Anh sang tiếng Việt trực tuyến phục vụ việc đọc tài liệu tham khảo, em nên sử dụng công cụ web nào?],
  [`translate.google.com` (Google Dịch).],
  [Disk Defragmenter.],
  [Task Manager.],
  [Control Panel.]
)

#mcq-stack("17", "Nhận biết",
  [Văn bản pháp luật nào quy định các hành vi bị nghiêm cấm trong hoạt động ứng dụng và phát triển công nghệ thông tin tại Việt Nam (ban hành năm 2006)?],
  [Luật Công nghệ thông tin.], [Luật Lâm nghiệp.], [Luật Hàng hải.], [Luật Khoáng sản.]
)

#mcq-stack("18", "Nhận biết",
  [Vấn đề nào sau đây là hệ lụy tiêu cực về *đạo đức và văn hóa* phát sinh khi giao tiếp thiếu ý thức trên không gian mạng?],
  [Tăng cường khả năng học ngoại ngữ trực tuyến miễn phí.],
  [Hiện tượng ứng xử thiếu văn hóa, bạo lực ngôn từ, miệt thị và xâm phạm đời tư người khác trên mạng xã hội.],
  [Tiết kiệm chi phí in ấn tài liệu giấy cho cơ quan.],
  [Giúp người thân ở xa gọi video thăm hỏi nhau dễ dàng.]
)

#mcq-stack("19", "Thông hiểu",
  [Bạn Quân lấy toàn bộ bài tiểu luận nghiên cứu của một tác giả đăng trên tạp chí khoa học, xóa tên tác giả đó đi rồi điền tên mình vào để nộp lấy điểm. Hành vi của Quân là:],
  [Chia sẻ học liệu mở hợp pháp.],
  [Vi phạm đạo đức học thuật (đạo văn) và xâm phạm quyền nhân thân của tác giả theo Luật Sở hữu trí tuệ.],
  [Bảo vệ sự toàn vẹn của tác phẩm gốc.],
  [Thực hiện quyền tự do ngôn luận hợp pháp.]
)

#mcq-stack("20", "Thông hiểu",
  [Biện pháp nào sau đây giúp việc chia sẻ thông tin trên mạng xã hội đảm bảo *an toàn và hợp pháp*?],
  [Chia sẻ ngay mọi tin đồn giật gân chưa rõ nguồn gốc để cảnh báo bạn bè càng sớm càng tốt.],
  [Đăng công khai ảnh chụp thẻ CCCD và số tài khoản ngân hàng của bạn cùng lớp.],
  [Kiểm chứng thông tin từ nguồn báo chí/cơ quan chính thống trước khi chia sẻ, ghi rõ nguồn tác giả và tôn trọng quyền riêng tư.],
  [Dùng tài khoản phụ không để ảnh thật để đăng tin sai sự thật mà không sợ bị phát hiện.]
)

=== PHẦN II. Trắc nghiệm lựa chọn Đúng/Sai (2,0 điểm)
_Thí sinh trả lời Câu 1 và Câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn Đúng hoặc Sai._

*Câu 1 (1,0 điểm — Chủ đề A.2).* Hiện nay, tại nhiều bệnh viện và gia đình, người dân sử dụng thiết bị đeo y tế thông minh (như *Smartwatch*) kết hợp với điện thoại thông minh để theo dõi chỉ số nhịp tim, giấc ngủ, nồng độ oxy trong máu (`SpO2`) và hỗ trợ khám tư vấn sức khỏe từ xa.
- *a)* Đồng hồ thông minh và điện thoại thông minh là các thiết bị thông minh vì chúng có khả năng hoạt động tự chủ nhất định và kết nối không dây để trao đổi dữ liệu với nhau.
- *b)* Đồng hồ thông minh chỉ là món trang sức hiển thị giờ, hoàn toàn không phải là một hệ thống xử lí thông tin vì nó không có bộ xử lí hay bộ nhớ lưu trữ.
- *c)* Khi phát hiện nhịp tim người đeo tăng bất thường vượt ngưỡng an toàn lúc đang nghỉ ngơi, đồng hồ tự động phát cảnh báo rung trên cổ tay và gửi thông báo tới điện thoại người thân — đây là minh chứng thực tế của chu trình thu nhận, xử lí và truyền thông tin tự động.
- *d)* Nhờ sự kết hợp giữa thiết bị thông minh, mạng Internet và phần mềm y tế số, bác sĩ ở bệnh viện tuyến trên có thể xem dữ liệu chỉ số sức khỏe của bệnh nhân ở xa để tư vấn kịp thời mà bệnh nhân không phải di chuyển vất vả mỗi ngày.

*Câu 2 (1,0 điểm — Chủ đề B.1).* Trường THPT Nguyễn Du xây dựng hệ thống mạng kết nối các máy tính trong phòng thư viện điện tử thành mạng nội bộ để dùng chung cơ sở dữ liệu sách; đồng thời kết nối hệ thống ra mạng Internet để học sinh truy cập học liệu trực tuyến trên *Google Drive* và lắp đặt hệ thống đèn hành lang thông minh *IoT* tự động bật/tắt theo cảm biến chuyển động và ánh sáng tự nhiên.
- *a)* Hệ thống mạng kết nối các máy tính trong phạm vi phòng thư viện thuộc quyền quản lí của nhà trường là mạng cục bộ (*LAN*), còn mạng *Internet* có phạm vi toàn cầu và không thuộc quyền sở hữu riêng của bất kì tổ chức nào.
- *b)* Dịch vụ lưu trữ học liệu trực tuyến *Google Drive* chỉ hoạt động được trên duy nhất chiếc máy tính đã tải tệp lên ban đầu, không thể truy cập được từ điện thoại hay máy tính ở nhà của học sinh.
- *c)* Hệ thống đèn hành lang thông minh *IoT* của trường giúp tiết kiệm điện năng và công sức bảo vệ đi bật/tắt từng công tắc thủ công mỗi ngày nhờ các cảm biến tự động thu thập và xử lí dữ liệu môi trường.
- *d)* Khi học sinh làm bài tập nhóm tại thư viện, việc lưu tài liệu chung trên Điện toán đám mây giúp các thành viên có thể tiếp tục hoàn thiện bài tập tại nhà qua Internet một cách liền mạch, đồng bộ.

=== PHẦN III. Tự luận (3,0 điểm)

*Câu 1 (1,0 điểm — Vận dụng — Chủ đề A.1).*\
*a)* Thực hiện quy đổi các đơn vị lưu trữ dữ liệu sau (ghi rõ phép tính): $3" GB" = dots" MB"$ và $4096" KB" = dots" MB"$.\
*b)* Thẻ nhớ máy ảnh của bạn An còn trống $16" GB"$. Bạn An quay một đoạn video kỉ niệm lớp học có dung lượng $2" GB"$, phần dung lượng còn lại bạn dùng để chụp các bức ảnh chất lượng cao (trung bình mỗi bức ảnh chiếm $4" MB"$). Hỏi bạn An có thể chụp và lưu thêm tối đa bao nhiêu bức ảnh nữa? Nếu sau đó An tải tệp video $2" GB"$ lên đám mây qua đường truyền Internet có tốc độ tải lên ổn định là $64" Mbps"$ (*Megabit/giây*), hãy tính thời gian cần thiết (theo giây) để tải xong tệp video đó.

*Câu 2 (1,0 điểm — Thông hiểu — Chủ đề B.2).*
Tham gia các hoạt động trên Internet một cách bất cẩn và thiếu hiểu biết có thể dẫn tới những nguy cơ và tác hại nào đối với học sinh? Em hãy trình bày ít nhất 04 biện pháp cụ thể để phòng tránh các tác hại đó và tự bảo vệ an toàn dữ liệu cá nhân.

*Câu 3 (1,0 điểm — Vận dụng cao — Chủ đề D.1).*
Để chuẩn bị cho cuộc thi thiết kế ấn phẩm tuyên truyền của trường, bạn T đã tải lậu bản phần mềm đồ họa thương mại đắt tiền kèm công cụ *"bẻ khóa" (crack)* trên một trang web không rõ nguồn gốc. Sau đó, T tìm thấy một bức tranh kĩ thuật số rất đẹp của một họa sĩ đăng trên mạng (có ghi dòng chữ *"Bản quyền thuộc tác giả — Cấm sao chép thương mại và chỉnh sửa"*), T liền cắt bỏ tên họa sĩ, chèn tên mình vào rồi gửi bài dự thi.
Vận dụng kiến thức về bản quyền và các văn bản pháp luật trong môi trường số (Luật Sở hữu trí tuệ, Luật Công nghệ thông tin...), em hãy phân tích các hành vi sai phạm của bạn T, chỉ rõ những hậu quả có thể xảy ra và đề xuất cách làm đúng đắn, hợp pháp cho T.

=== ĐÁP ÁN & HƯỚNG DẪN CHẤM CHI TIẾT — ĐỀ THI THỬ SỐ 01

*1. Phần I — Trắc nghiệm 4 lựa chọn (5,0 điểm — Mỗi câu đúng được 0,25 điểm):*

#set text(size: 8.5pt)
#table(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  inset: (x: 3.5pt, y: 4.5pt),
  stroke: 0.5pt + c-border,
  align: center + horizon,
  fill: (col, row) => if calc.even(row) { c-green-light.lighten(30%) } else { white },

  [*Câu 1*], [*Câu 2*], [*Câu 3*], [*Câu 4*], [*Câu 5*], [*Câu 6*], [*Câu 7*], [*Câu 8*], [*Câu 9*], [*Câu 10*],
  [*B*], [*C*], [*B*], [*C*], [*B*], [*A*], [*B*], [*B*], [*D*], [*B*],
  [*Câu 11*], [*Câu 12*], [*Câu 13*], [*Câu 14*], [*Câu 15*], [*Câu 16*], [*Câu 17*], [*Câu 18*], [*Câu 19*], [*Câu 20*],
  [*A*], [*C*], [*C*], [*B*], [*C*], [*A*], [*A*], [*B*], [*B*], [*C*],
)
#set text(size: 9.7pt)

*2. Phần II — Trắc nghiệm Đúng/Sai (2,0 điểm — Đúng 1 ý: 0,1đ; 2 ý: 0,25đ; 3 ý: 0,5đ; 4 ý: 1,0đ):*
- *Câu 1 (1,0 điểm):* *a) Đúng* | *b) Sai* _(Smartwatch có vi xử lí, bộ nhớ, cảm biến và truyền tin nên chính là một hệ thống xử lí thông tin)_ | *c) Đúng* | *d) Đúng*.
- *Câu 2 (1,0 điểm):* *a) Đúng* | *b) Sai* _(Google Drive cho phép truy cập đồng bộ từ mọi thiết bị có Internet khi đăng nhập đúng tài khoản)_ | *c) Đúng* | *d) Đúng*.

*3. Phần III — Tự luận (3,0 điểm):*
- *Câu 1 (1,0 điểm):*
  + *Ý a (0,5 điểm):* Tính đúng $3" GB" = 3 times 1024 = bold(3072" MB")$ *(0,25đ)*; $4096" KB" = 4096 : 1024 = bold(4" MB")$ *(0,25đ)*.
  + *Ý b (0,5 điểm):*
    - Dung lượng còn lại sau khi lưu video: $16 - 2 = 14" GB" = 14 times 1024 = 14.336" MB"$; số bức ảnh chụp thêm tối đa: $14.336 : 4 = bold(3.584" bức ảnh")$ *(0,25đ)*.
    - Đổi dung lượng video $2" GB" = 2048" MB"$; đổi tốc độ tải lên $64" Mbps" = 64 : 8 = 8" MB/s"$; thời gian truyền xong video: $t = 2048 : 8 = bold(256" giây")$ _(4 phút 16 giây)_ *(0,25đ)*.
- *Câu 2 (1,0 điểm):*
  + *Nêu đúng các nguy cơ & tác hại (0,5 điểm):* (1) Lây nhiễm phần mềm độc hại (*Virus, Worm, Trojan, Ransomware*) gây hỏng hệ thống, mất/mã hóa dữ liệu; (2) Bị lừa đảo trực tuyến (*Phishing*), đánh cắp tài khoản, mật khẩu, thông tin cá nhân và tài chính; (3) Tiếp nhận tin giả (*Fake news*), văn hóa phẩm độc hại hoặc bị bắt nạt trên mạng (*Cyberbullying*) gây tổn thương tâm lí; (4) Nghiện Internet/game online ảnh hưởng sức khỏe và học tập.
  + *Trình bày tối thiểu 04 biện pháp phòng tránh & bảo vệ dữ liệu (0,5 điểm):* (1) Bật phần mềm diệt virus (*Windows Defender...*) & Tường lửa, cập nhật hệ điều hành thường xuyên; (2) Không bấm link lạ, không mở tệp đính kèm khả nghi, không cài phần mềm lậu/crack; (3) Dùng mật khẩu mạnh kèm xác thực 2 yếu tố (*2FA*), tuyệt đối không cung cấp mã OTP, đăng xuất khi dùng máy công cộng; (4) Sao lưu dữ liệu định kì lên đám mây/ổ cứng rời; biết lưu bằng chứng, chặn kẻ xấu và báo cha mẹ/thầy cô khi bị bắt nạt mạng.
- *Câu 3 (1,0 điểm):*
  + *Chỉ rõ 02 hành vi vi phạm pháp luật và đạo đức của T (0,5 điểm):*
    - Thứ nhất: Tải và dùng công cụ *crack* phần mềm đồ họa thương mại là hành vi *bất hợp pháp*, xâm phạm quyền tài sản của nhà sản xuất phần mềm theo *Luật Sở hữu trí tuệ* và *Khoản 3 Điều 12 Luật Công nghệ thông tin*. *(0,25đ)*
    - Thứ hai: Tự ý lấy tranh của họa sĩ, cắt bỏ tên tác giả và mạo danh tên mình đi dự thi là hành vi *đạo văn/đạo tác phẩm*, xâm phạm nghiêm trọng *Quyền nhân thân* (quyền đứng tên tác giả, quyền bảo vệ sự toàn vẹn tác phẩm) và *Quyền tài sản* của họa sĩ. *(0,25đ)*
  + *Phân tích hậu quả & đề xuất giải pháp hợp pháp (0,5 điểm):*
    - *Hậu quả:* T sẽ bị hủy kết quả thi, xử lí kỉ luật, mất uy tín cá nhân; có thể bị chủ sở hữu khiếu nại yêu cầu bồi thường, xử phạt hành chính về hành vi xâm phạm bản quyền; ngoài ra máy tính của T rất dễ bị nhiễm *Trojan/Ransomware* từ file crack. *(0,25đ)*
    - *Giải pháp đúng đắn:* T cần gỡ bỏ phần mềm crack, chuyển sang sử dụng phần mềm thiết kế đồ họa *nguồn mở miễn phí hợp pháp* (như *Inkscape* hoặc *GIMP* được học trong chương trình Tin học 10!), tự mình sáng tạo ấn phẩm hoặc sử dụng hình ảnh có giấy phép mở *Creative Commons* và ghi rõ nguồn tác giả đúng quy định. *(0,25đ)*

#pagebreak()

== 5.2. ĐỀ THI THỬ GIỮA HỌC KÌ I — ĐỀ SỐ 02

#block(
  width: 100%,
  fill: c-bg-soft,
  stroke: 0.7pt + c-teal,
  radius: 5pt,
  inset: (x: 12pt, y: 9pt),
  breakable: false,
  [
    #grid(
      columns: (1fr, 1.3fr),
      align: (center + horizon, center + horizon),
      [
        *TRƯỜNG THPT ........................*\
        *TỔ TIN HỌC*\
        _(Đề thi thử chuẩn Ma trận — Số 02)_
      ],
      [
        *ĐỀ KIỂM TRA GIỮA HỌC KÌ I*\
        *MÔN: TIN HỌC 10 — ĐỊNH HƯỚNG ICT*\
        _Thời gian làm bài: 45 phút (không kể thời gian phát đề)_
      ],
    )
  ],
)

=== PHẦN I. Trắc nghiệm nhiều phương án lựa chọn (5,0 điểm)
_Thí sinh trả lời từ Câu 1 đến Câu 20. Mỗi câu hỏi thí sinh chỉ chọn một phương án đúng (0,25 điểm/câu)._

#mcq("1", "Nhận biết",
  [Trong chu trình xử lí thông tin của máy tính, bộ phận nào đảm nhận vai trò *xử lí dữ liệu trung tâm*?],
  [Bộ xử lí trung tâm (CPU).], [Chuột máy tính.], [Loa tai nghe.], [Tấm lót chuột.]
)

#mcq-stack("2", "Nhận biết",
  [Ưu điểm nào sau đây giải thích vì sao thư viện số hiện đại ngày càng thay thế một phần kho lưu trữ tài liệu giấy truyền thống?],
  [Tài liệu số chiếm diện tích nhà kho gấp hàng trăm lần sách giấy.],
  [Cho phép hàng nghìn độc giả tìm kiếm và truy cập đọc tài liệu nhanh chóng cùng lúc mà không làm hư hại bản gốc.],
  [Tài liệu số không thể sao lưu dự phòng khi cần thiết.],
  [Chỉ tìm kiếm được sách nếu lật thủ công từng trang từ đầu đến cuối.]
)

#mcq-stack("3", "Thông hiểu",
  [Trên màn hình đồng hồ đo tốc độ xe máy điện hiển thị con số `42 km/h`. Người điều khiển xe nhìn thấy và biết mình đang đi đúng tốc độ cho phép trong khu dân cư (tối đa `50 km/h`). Trong tình huống này, con số `42 km/h` trên màn hình là gì?],
  [Tri thức.], [Dữ liệu.], [Vật mang tin.], [Phần mềm diệt virus.]
)

#mcq("4", "Thông hiểu",
  [Trong các dung lượng lưu trữ sau: `2048 KB`, `1 GB`, `500 MB`, `1 TB`, dung lượng nào là *LỚN NHẤT*?],
  [`2048 KB`.], [`1 GB`.], [`500 MB`.], [`1 TB`.]
)

#mcq("5", "Nhận biết",
  [Thành tựu nào sau đây là ví dụ tiêu biểu về ứng dụng của Tin học trong *tự động hóa sản xuất và dịch vụ*?],
  [Dây chuyền robot tự động hàn và sơn vỏ ô tô trong nhà máy thông minh.],
  [Viết thư tay gửi qua bưu tá đường bộ.],
  [Tính tổng tiền hàng bằng que tính tre.],
  [Chép tay từng cuốn sổ điểm học sinh.]
)

#mcq("6", "Nhận biết",
  [Thiết bị nào dưới đây là một *thiết bị thông minh* tiêu biểu trong gia đình hiện đại?],
  [Tivi thông minh (Smart TV) có hệ điều hành, kết nối Wi-Fi và tìm kiếm giọng nói.],
  [Nồi nhôm đun trên bếp củi.],
  [Đồng hồ cát thủy tinh.],
  [Đèn pin lắp pin tiểu thông thường.]
)

#mcq("7", "Nhận biết",
  [Bộ máy tìm kiếm thông tin nổi tiếng *Google Search* chính thức ra đời vào năm nào?],
  [Năm 1945.], [Năm 1969.], [Năm 1998.], [Năm 2022.]
)

#mcq("8", "Nhận biết",
  [Người đề xuất nguyên lí *"Chương trình lưu trữ trong bộ nhớ"* (năm 1945) đặt nền tảng kiến trúc cho hầu hết máy tính điện tử ngày nay là:],
  [John von Neumann.], [Isaac Newton.], [Thomas Edison.], [Louis Pasteur.]
)

#mcq("9", "Nhận biết",
  [Khi soạn thảo tài liệu trực tuyến bằng *Microsoft 365 Online* hoặc *Google Docs* để nhiều thành viên cùng làm việc qua trình duyệt web, công nghệ nền tảng được sử dụng là:],
  [Điện toán đám mây (Cloud Computing).],
  [Đĩa mềm từ tính Floppy Disk.],
  [Băng cát-xét âm thanh.],
  [Cáp đồng trục truyền hình cáp cũ.]
)

#mcq-stack("10", "Nhận biết",
  [Đặc điểm cốt lõi nào tạo nên mạng *Internet vạn vật (IoT)*?],
  [Các thiết bị chỉ kết nối trong 1 căn phòng và hoàn toàn không có cảm biến.],
  [Các đồ vật, thiết bị vật lí gắn cảm biến và phần mềm tự động thu thập, trao đổi dữ liệu với nhau qua Internet.],
  [Bắt buộc con người phải gõ lệnh bàn phím từng giây cho mọi thiết bị.],
  [Chỉ kết nối được tối đa 2 máy tính để bàn với nhau.]
)

#mcq("11", "Nhận biết",
  [Mạng máy tính toàn cầu kết nối hàng triệu mạng máy tính lớn nhỏ trên khắp thế giới lại với nhau được gọi là:],
  [Mạng LAN.], [Mạng Internet.], [Mạng Bluetooth cá nhân.], [Mạng nội bộ phòng học.]
)

#mcq("12", "Nhận biết",
  [Thiết bị nào đóng vai trò định tuyến đường đi cho các gói dữ liệu để kết nối mạng LAN của gia đình/trường học ra mạng Internet?],
  [Bộ định tuyến (Router / Modem Router).], [Tai nghe có dây.], [Máy quét ảnh (Scanner).], [Chuột quang không dây.]
)

#mcq-stack("13", "Nhận biết",
  [Loại phần mềm độc hại nào phải *gắn (ký sinh)* vào một tệp chương trình hợp pháp và chỉ kích hoạt lây lan khi người dùng mở chạy tệp bị nhiễm đó?],
  [Virus máy tính.], [Tường lửa Windows Firewall.], [Trình duyệt Google Chrome.], [Hệ điều hành Android.]
)

#mcq-stack("14", "Nhận biết",
  [Hành vi cố ý sử dụng mạng xã hội, tin nhắn để đe dọa, bôi nhọ, chế giễu, tung tin đồn xấu lặp đi lặp lại nhằm làm tổn thương người khác gọi là:],
  [Học trực tuyến (E-learning).],
  [Bắt nạt trên không gian mạng (Cyberbullying).],
  [Thương mại điện tử (E-commerce).],
  [Sao lưu đám mây (Cloud Backup).]
)

#mcq-stack("15", "Thông hiểu",
  [Để nâng cao mức độ bảo mật tài khoản thư điện tử và mạng xã hội ngay cả khi kẻ gian vô tình biết được mật khẩu, người dùng nên kích hoạt tính năng nào?],
  [Tắt hoàn toàn mật khẩu đăng nhập.],
  [Xác thực hai yếu tố (2FA — yêu cầu thêm mã xác nhận OTP trên điện thoại khi đăng nhập từ thiết bị lạ).],
  [Đặt mật khẩu trùng hệt tên tài khoản.],
  [Ghi mật khẩu dán công khai trên trang cá nhân.]
)

#mcq-stack("16", "Thông hiểu",
  [Lợi ích thiết thực nhất của việc khai thác các nguồn *Học liệu mở (OER)* uy tín trên Internet đối với học sinh THPT là gì?],
  [Giúp học sinh chủ động tự học, tra cứu miễn phí và hợp pháp kho bài giảng, sách số, thí nghiệm ảo phong phú mọi lúc mọi nơi.],
  [Giúp học sinh tải các phần mềm bẻ khóa vi phạm bản quyền nhanh hơn.],
  [Thay thế hoàn toàn việc ăn ngủ và rèn luyện thể chất hằng ngày.],
  [Cho phép sao chép nguyên văn bài của người khác đi thi mà không cần học.]
)

#mcq-stack("17", "Nhận biết",
  [Theo Bộ Quy tắc ứng xử trên mạng xã hội của Bộ Thông tin và Truyền thông (Quyết định 874/QĐ-BTTTT), người dùng mạng xã hội cần tuân thủ các quy tắc chung nào?],
  [Tôn trọng, tuân thủ pháp luật; Lành mạnh; An toàn, bảo mật thông tin; Trách nhiệm.],
  [Ẩn danh tuyệt đối; Tự do công kích; Chia sẻ không kiểm chứng.],
  [Sao chép tự do mọi sản phẩm số không cần xin phép.],
  [Chỉ tuân thủ pháp luật vào giờ hành chính.]
)

#mcq("18", "Nhận biết",
  [Theo Luật Sở hữu trí tuệ, hành vi *sao chép, phân phối chương trình máy tính hoặc tác phẩm số* khi chưa được phép của chủ sở hữu quyền tác giả là xâm phạm nhóm quyền nào?],
  [Quyền tài sản (thuộc Quyền tác giả).], [Quyền tham gia giao thông.], [Quyền khám chữa bệnh.], [Quyền bầu cử.]
)

#mcq-stack("19", "Thông hiểu",
  [Bạn H quay lén toàn bộ bộ phim điện ảnh Việt Nam vừa công chiếu tại rạp bằng điện thoại rồi đăng lên kênh mạng xã hội cá nhân để câu lượt xem và nhận tiền quảng cáo. Nhận định nào sau đây là *đúng*?],
  [Hành vi của H hoàn toàn hợp pháp vì H đã bỏ tiền mua 1 tấm vé vào rạp xem phim.],
  [Hành vi của H vi phạm nghiêm trọng pháp luật về bản quyền (Luật Sở hữu trí tuệ, Luật CNTT), gây thiệt hại kinh tế lớn cho nhà sản xuất phim và có thể bị xử phạt hành chính hoặc truy cứu hình sự.],
  [Hành vi của H được khuyến khích vì giúp quảng bá phim miễn phí.],
  [H chỉ vi phạm nếu quay bằng máy quay chuyên nghiệp, còn quay bằng điện thoại thì không vi phạm.]
)

#mcq-stack("20", "Thông hiểu",
  [Trong quá trình làm bài thuyết trình môn Lịch sử, bạn Vy muốn sử dụng một bức ảnh tư liệu của một nhiếp ảnh gia đăng trên mạng dưới giấy phép *Creative Commons Ghi công (`CC BY`)*. Vy cần làm gì để *đúng pháp luật bản quyền*?],
  [Xóa chữ kí của nhiếp ảnh gia trên ảnh và nhận là ảnh do mình tự chụp.],
  [Đưa bức ảnh vào bài thuyết trình, giữ nguyên sự toàn vẹn của ảnh và *ghi rõ tên tác giả / nguồn trích dẫn* theo đúng yêu cầu giấy phép `CC BY`.],
  [Đem bức ảnh đi đăng kí bản quyền độc quyền mang tên Vy.],
  [Cấm tất cả người khác xem bức ảnh gốc của nhiếp ảnh gia.]
)

=== PHẦN II. Trắc nghiệm lựa chọn Đúng/Sai (2,0 điểm)
_Thí sinh trả lời Câu 1 và Câu 2. Trong mỗi ý a), b), c), d) ở mỗi câu, thí sinh chọn Đúng hoặc Sai._

*Câu 1 (1,0 điểm — Chủ đề A.2).* Một đô thị hiện đại triển khai hệ thống *camera giao thông thông minh tích hợp AI*: camera tự động ghi nhận lưu lượng phương tiện tại ngã tư, nhận diện biển số xe vượt đèn đỏ, gửi dữ liệu về trung tâm điều hành để tự động điều chỉnh thời gian đèn tín hiệu xanh – đỏ giảm ùn tắc và hỗ trợ xử phạt "phạt nguội".
- *a)* Hệ thống camera giao thông tích hợp AI nói trên là thiết bị thông minh vì có khả năng thu nhận hình ảnh, tự động xử lí nhận diện và kết nối truyền dữ liệu về trung tâm qua mạng.
- *b)* Trong nền kinh tế tri thức và cuộc Cách mạng công nghiệp 4.0, các hệ thống thiết bị thông minh như trên hoàn toàn không dùng đến dữ liệu số hay phần mềm máy tính.
- *c)* Hình ảnh biển số xe do camera chụp lại là *dữ liệu*, còn kết luận xác định *"Phương tiện biển số X đã vi phạm lỗi không chấp hành hiệu lệnh đèn tín hiệu lúc 08:15"* rút ra sau khi xử lí là *thông tin*.
- *d)* Việc ứng dụng hệ thống giao thông thông minh giúp giảm tải sức lực cho lực lượng cảnh sát đứng điều tiết trực tiếp ngoài nắng mưa, đồng thời nâng cao ý thức chấp hành luật giao thông của người dân.

*Câu 2 (1,0 điểm — Chủ đề B.1).* Công ty thiết kế kiến trúc Bình Minh kết nối 25 máy tính làm việc trong văn phòng tầng 3 thành một mạng nội bộ để dùng chung máy in khổ lớn; đồng thời công ty thuê dịch vụ lưu trữ đám mây để lưu bản vẽ công trình và trang bị hệ thống báo cháy *IoT* thông minh kết nối Internet tại kho vật liệu.
- *a)* Mạng kết nối 25 máy tính và máy in khổ lớn trong phạm vi tầng 3 của công ty là mạng cục bộ (*LAN*), còn mạng *Internet* giúp nhân viên đi công trường ở tỉnh khác vẫn gửi được báo cáo về công ty.
- *b)* Giữa mạng LAN và mạng Internet không có bất kì điểm khác biệt nào về phạm vi địa lí cũng như quyền sở hữu quản lí.
- *c)* Khi kho vật liệu chẳng may phát sinh khói bất thường vào ban đêm không có người trực, cảm biến khói *IoT* tự động kích hoạt chuông báo động tại chỗ đồng thời gửi cảnh báo khẩn cấp qua Internet tới điện thoại của quản lí và đội phòng cháy.
- *d)* Việc công ty đồng bộ dự phòng các bản vẽ thiết kế quan trọng lên dịch vụ *Điện toán đám mây* giúp bảo toàn dữ liệu công việc ngay cả khi một máy tính cá nhân tại văn phòng bị hỏng ổ cứng đột ngột.

=== PHẦN III. Tự luận (3,0 điểm)

*Câu 1 (1,0 điểm — Vận dụng — Chủ đề A.1).*\
*a)* Thực hiện chuyển đổi các đơn vị lưu trữ thông tin sau (viết rõ phép tính): $5" TB" = dots" GB"$ và $6144" MB" = dots" GB"$.\
*b)* Chiếc USB cá nhân của bạn Bình hiện còn trống $8" GB"$. Bình sao chép vào USB một thư mục tài liệu gồm $128$ tệp đề cương PDF (trung bình mỗi tệp nặng $8" MB"$). Phần dung lượng còn lại của USB, Bình dùng để chép các tệp video bài giảng Tin học 10 (mỗi video có dung lượng $512" MB"$). Hỏi Bình có thể chép thêm tối đa bao nhiêu tệp video bài giảng vào chiếc USB đó?

*Câu 2 (1,0 điểm — Thông hiểu / Vận dụng — Chủ đề B.2).*\
*a)* Phân biệt ngắn gọn cơ chế lây lan giữa *Virus máy tính*, *Sâu máy tính (Worm)* và *Phần mềm nội gián (Trojan Horse)*. Nêu công cụ thông dụng để ngăn ngừa và loại bỏ chúng trên máy tính.\
*b)* Giả sử một người bạn thân của em đang bị kẻ xấu lập trang ẩn danh tung tin đồn bịa đặt, bắt nạt trên mạng xã hội khiến bạn rất hoang mang. Em hãy tư vấn cho bạn quy trình các bước xử lí đúng đắn để tự bảo vệ mình.

*Câu 3 (1,0 điểm — Vận dụng cao — Chủ đề D.1).*
Buổi tối lướt mạng xã hội, anh D thấy một tài khoản lạ đăng bài viết kèm hình ảnh chưa kiểm chứng với tiêu đề giật gân: *"Phát hiện cơ sở sản xuất sữa hộp X gần trường học bỏ chất độc cực mạnh, hàng chục người nhập viện cấp cứu!"*. Để câu lượt tương tác bán hàng online trên trang cá nhân của mình, anh D không hề kiểm tra sự thật mà lập tức sao chép đăng lại bài viết đó kèm lời bình luận bịa đặt khẳng định chắc chắn sự việc có thật và kêu gọi mọi người tẩy chay doanh nghiệp X. Sáng hôm sau, cơ quan chức năng xác minh đây hoàn toàn là tin giả vu khống làm doanh nghiệp X thiệt hại nặng nề và gây hoang mang cho phụ huynh.
Dựa vào Luật Công nghệ thông tin, Luật An ninh mạng và Nghị định xử phạt vi phạm hành chính trong lĩnh vực CNTT, em hãy xác định tính hợp pháp trong hành vi của anh D, giải thích rõ các quy định pháp luật bị vi phạm, hậu quả pháp lí và nêu bài học rút ra khi chia sẻ thông tin trên môi trường số.

=== ĐÁP ÁN & HƯỚNG DẪN CHẤM CHI TIẾT — ĐỀ THI THỬ SỐ 02

*1. Phần I — Trắc nghiệm 4 lựa chọn (5,0 điểm — Mỗi câu đúng được 0,25 điểm):*

#set text(size: 8.5pt)
#table(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  inset: (x: 3.5pt, y: 4.5pt),
  stroke: 0.5pt + c-border,
  align: center + horizon,
  fill: (col, row) => if calc.even(row) { c-green-light.lighten(30%) } else { white },

  [*Câu 1*], [*Câu 2*], [*Câu 3*], [*Câu 4*], [*Câu 5*], [*Câu 6*], [*Câu 7*], [*Câu 8*], [*Câu 9*], [*Câu 10*],
  [*A*], [*B*], [*B*], [*D*], [*A*], [*A*], [*C*], [*A*], [*A*], [*B*],
  [*Câu 11*], [*Câu 12*], [*Câu 13*], [*Câu 14*], [*Câu 15*], [*Câu 16*], [*Câu 17*], [*Câu 18*], [*Câu 19*], [*Câu 20*],
  [*B*], [*A*], [*A*], [*B*], [*B*], [*A*], [*A*], [*A*], [*B*], [*B*],
)
#set text(size: 9.7pt)

*2. Phần II — Trắc nghiệm Đúng/Sai (2,0 điểm — Đúng 1 ý: 0,1đ; 2 ý: 0,25đ; 3 ý: 0,5đ; 4 ý: 1,0đ):*
- *Câu 1 (1,0 điểm):* *a) Đúng* | *b) Sai* _(hệ thống thông minh trong CMCN 4.0 vận hành trực tiếp dựa trên dữ liệu số, phần mềm và AI)_ | *c) Đúng* | *d) Đúng*.
- *Câu 2 (1,0 điểm):* *a) Đúng* | *b) Sai* _(LAN phạm vi hẹp và thuộc sở hữu riêng của tổ chức; Internet phạm vi toàn cầu và không thuộc sở hữu riêng của ai)_ | *c) Đúng* | *d) Đúng*.

*3. Phần III — Tự luận (3,0 điểm):*
- *Câu 1 (1,0 điểm):*
  + *Ý a (0,5 điểm):* Tính đúng $5" TB" = 5 times 1024 = bold(5120" GB")$ *(0,25đ)*; $6144" MB" = 6144 : 1024 = bold(6" GB")$ *(0,25đ)*.
  + *Ý b (0,5 điểm):*
    - Tổng dung lượng $128$ tệp PDF: $128 times 8 = 1024" MB" = 1" GB"$. Dung lượng USB còn lại: $8 - 1 = 7" GB" = 7 times 1024 = 7168" MB"$ *(0,25đ)*.
    - Số tệp video bài giảng chép thêm được tối đa: $7168 : 512 = bold(14" (video)")$ *(0,25đ)*.
- *Câu 2 (1,0 điểm):*
  + *Ý a (0,5 điểm):*
    - *Phân biệt:* *Virus* gắn ký sinh vào tệp hợp pháp và lây khi người dùng chạy tệp; *Worm (Sâu)* là chương trình độc lập tự nhân bản phát tán qua lỗ hổng mạng không cần tệp vật chủ; *Trojan* không tự nhân bản mà giả dạng phần mềm hữu ích lừa người dùng tự cài để mở cửa hậu đánh cắp dữ liệu. *(0,25đ)*
    - *Công cụ phòng chống:* Bật *Tường lửa (Windows Firewall)* và phần mềm diệt virus (*Windows Security / Windows Defender*, Kaspersky, Bitdefender, Bkav...) có cập nhật mẫu nhận diện thường xuyên. *(0,25đ)*
  + *Ý b (0,5 điểm):* Tư vấn đủ 4 bước phòng vệ khi bị bắt nạt trên mạng: *(1) Giữ bình tĩnh, không đáp trả tiêu cực*; *(2) Chụp ảnh màn hình lưu giữ đầy đủ bằng chứng*; *(3) Chặn (Block) và Báo cáo vi phạm (Report)* trang ẩn danh với quản trị mạng xã hội; *(4) Chia sẻ ngay với cha mẹ, giáo viên chủ nhiệm / nhà trường* (và trình báo cơ quan Công an nếu mức độ vu khống, đe dọa nghiêm trọng).
- *Câu 3 (1,0 điểm):*
  + *Xác định tính pháp lí & quy định pháp luật bị vi phạm (0,5 điểm):*
    - Khẳng định hành vi của anh D là *BẤT HỢP PHÁP (vi phạm pháp luật)* dù không phải người viết bài đầu tiên nhưng đã cố ý đăng lại và bịa đặt thêm để câu tương tác bán hàng. *(0,25đ)*
    - Vi phạm trực tiếp *Điều 12 Luật Công nghệ thông tin* và *Điều 8, Điều 16 Luật An ninh mạng* (nghiêm cấm đăng tải, phát tán thông tin sai sự thật gây hoang mang trong Nhân dân, xuyên tạc, vu khống xúc phạm uy tín, gây thiệt hại kinh tế cho tổ chức/doanh nghiệp), đồng thời vi phạm quy định trách nhiệm người dùng mạng xã hội tại *Nghị định 72/2013/NĐ-CP* và *Điều 101 Nghị định 15/2020/NĐ-CP*. *(0,25đ)*
  + *Hậu quả pháp lí & Bài học rút ra (0,5 điểm):*
    - *Hậu quả:* Anh D buộc phải gỡ bỏ bài viết, đăng bài cải chính xin lỗi công khai, bị *xử phạt vi phạm hành chính từ 5 – 10 triệu đồng* (theo Điều 101 Nghị định 15/2020/NĐ-CP sửa đổi bởi NĐ 14/2022/NĐ-CP), phải *bồi thường thiệt hại dân sự* cho doanh nghiệp X (thậm chí bị truy cứu trách nhiệm hình sự nếu gây hậu quả đặc biệt nghiêm trọng). *(0,25đ)*
    - *Bài học ứng xử:* Tuyệt đối không đăng tải hay chia sẻ thông tin chưa được kiểm chứng từ cơ quan chức năng/báo chí chính thống; không vì mục đích câu lượt xem trục lợi mà tiếp tay cho tin giả; luôn tuân thủ pháp luật và có trách nhiệm với từng cú nhấp chuột chia sẻ trên môi trường số. *(0,25đ)*

#v(8pt)

#callout(title: "BẢNG TỔNG KẾT TỐC HÀNH 5 PHÚT TRƯỚC KHI VÀO PHÒNG THI", tone: "memo")[
  + *Công thức đơn vị lưu trữ (Chủ đề A.1):* $1" Byte (B)" = 8" bit (b)"$; dãy bội số cách nhau $1024$ lần: `B` $arrow.r$ `KB` $arrow.r$ `MB` $arrow.r$ `GB` $arrow.r$ `TB` $arrow.r$ `PB` $arrow.r$ `EB` $arrow.r$ `ZB` $arrow.r$ `YB`. Tốc độ mạng `Mbps` đổi ra `MB/s` phải *chia cho 8*!
  + *Phân biệt cốt lõi (Chủ đề A.1 & A.2):* *Dữ liệu* = những gì ghi trên vật mang tin; *Thông tin* = ý nghĩa/sự hiểu biết rút ra; *Thiết bị thông minh* = hoạt động tự chủ (CPU + hệ điều hành/AI + cảm biến) *VÀ* có kết nối mạng.
  + *Mạng, Cloud & IoT (Chủ đề B.1):* *LAN* (phạm vi hẹp, sở hữu riêng) $times.o$ *Internet* (toàn cầu, dùng `TCP/IP`, không thuộc sở hữu riêng ai); *Cloud* (`SaaS` phần mềm như Google Docs/Drive, `PaaS` nền tảng, `IaaS` hạ tầng); *IoT* = vạn vật gắn cảm biến tự trao đổi dữ liệu qua Internet.
  + *An toàn mạng (Chủ đề B.2):* *Virus* (ký sinh tệp) $times.o$ *Worm* (tự bò qua mạng) $times.o$ *Trojan* (giả dạng mở cửa hậu) $times.o$ *Ransomware* (mã hóa tống tiền). Bị *bắt nạt mạng*: Không đáp trả $arrow.r$ Chụp màn hình bằng chứng $arrow.r$ Chặn & Báo cáo $arrow.r$ Báo cha mẹ, thầy cô / Tổng đài `111`.
  + *Pháp luật & Bản quyền số (Chủ đề D.1):* Nắm chắc *Điều 12 Luật CNTT*, *Điều 8 Luật An ninh mạng*, *Điều 101 Nghị định 15/2020/NĐ-CP* (phạt 5–10 triệu cá nhân tung/chia sẻ tin giả, vu khống) và *Luật Sở hữu trí tuệ* (*Quyền nhân thân* + *Quyền tài sản*; không dùng crack, không đạo văn, kiểm chứng trước khi chia sẻ).
]
