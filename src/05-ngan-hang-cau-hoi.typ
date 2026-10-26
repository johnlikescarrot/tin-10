// =============================================================================
// src/05-ngan-hang-cau-hoi.typ
// Phần III: Ngân hàng câu hỏi & bài tập ôn luyện theo chuyên đề (Có đáp án chi tiết)
// =============================================================================

#import "template.typ": *

#pagebreak()

#part-banner(
  "Phần III",
  "NGÂN HÀNG CÂU HỎI & BÀI TẬP ÔN LUYỆN THEO CHUYÊN ĐỀ",
  "Gồm 50 câu Trắc nghiệm 4 lựa chọn • 08 câu Đúng/Sai (32 mệnh đề) • 09 bài Tự luận phân tầng kèm lời giải & thang điểm",
  accent: c-navy,
)

=== Mục A. Hệ thống 50 câu hỏi Trắc nghiệm nhiều lựa chọn (4 phương án)

==== 1. Chủ đề A: Máy tính và xã hội tri thức (Câu 1 – Câu 20)

#mcq(1, "NB",
  [Trong tin học, khẳng định nào sau đây phát biểu đúng nhất về *dữ liệu*?],
  [Là những hiểu biết của con người về thế giới xung quanh.],
  [Là các con số, văn bản, hình ảnh, âm thanh... được lưu trữ trên vật mang tin hoặc đưa vào máy tính.],
  [Chỉ bao gồm các con số dùng để tính toán trong bảng tính.],
  [Là kết quả suy nghĩ chủ quan chỉ tồn tại trong bộ não con người.],
  cols: 1
)

#mcq(2, "NB",
  [Đơn vị nhỏ nhất dùng để biểu diễn và lưu trữ dữ liệu trong máy tính là gì?],
  [Byte (B)], [Kilobyte (KB)], [Bit (b)], [Megabyte (MB)], cols: 4
)

#mcq(3, "NB",
  [Theo quy ước chuẩn trong Tin học, $1 "Byte (B)"$ bằng bao nhiêu bit và $1 "MB"$ bằng bao nhiêu $"KB"$?],
  [$1 "B" = 8 "bit"; 1 "MB" = 1024 "KB"$],
  [$1 "B" = 10 "bit"; 1 "MB" = 1000 "KB"$],
  [$1 "B" = 16 "bit"; 1 "MB" = 1024 "KB"$],
  [$1 "B" = 8 "bit"; 1 "MB" = 512 "KB"$],
  cols: 2
)

#mcq(4, "NB",
  [Sắp xếp nào dưới đây đúng theo thứ tự *tăng dần* của các đơn vị đo dung lượng dữ liệu?],
  [B, bit, KB, MB, GB, TB],
  [bit, B, KB, GB, MB, TB],
  [bit, B, KB, MB, GB, TB],
  [bit, KB, B, MB, TB, GB],
  cols: 2
)

#mcq(5, "NB",
  [Phương tiện nào sau đây *KHÔNG* phải là thiết bị lưu trữ dữ liệu số?],
  [Ổ cứng thể rắn (SSD)], [Thẻ nhớ MicroSD], [Đĩa quang DVD], [Tờ báo giấy in truyền thống], cols: 2
)

#mcq(6, "NB",
  [Ưu điểm nào sau đây thể hiện sự ưu việt của lưu trữ bằng thiết bị số so với lưu trữ trên giấy?],
  [Không bao giờ cần dùng đến điện năng khi truy xuất dữ liệu.],
  [Dung lượng lưu trữ rất lớn trong kích thước nhỏ gọn, tìm kiếm và sao chép cực nhanh.],
  [Chi phí mua thiết bị ban đầu luôn bằng 0.],
  [Bản sao luôn bị mờ dần sau mỗi lần sao chép.],
  cols: 1
)

#mcq(7, "TH",
  [Bạn Lan nhìn thấy đèn tín hiệu giao thông chuyển sang *màu đỏ* nên dừng xe trước vạch kẻ đường. Trong tình huống này, *thông tin* bạn Lan thu nhận được là gì?],
  [Chiếc cột đèn giao thông đặt ở ngã tư.],
  [Ánh sáng màu đỏ phát ra từ đèn tín hiệu.],
  [Sự hiểu biết rằng "phải dừng xe lại trước vạch kẻ để đảm bảo an toàn và đúng luật".],
  [Mắt của bạn Lan.],
  cols: 1
)

#mcq(8, "TH",
  [Phát biểu nào sau đây *SAI* khi phân biệt giữa thông tin và dữ liệu?],
  [Cùng một thông tin có thể được biểu diễn bằng nhiều dạng dữ liệu khác nhau (chữ, ảnh, âm thanh).],
  [Dữ liệu là hình thức thể hiện, còn thông tin là ý nghĩa rút ra từ dữ liệu.],
  [Với cùng một dữ liệu trên vật mang tin, mọi người ở mọi trình độ đều rút ra lượng thông tin giống hệt nhau.],
  [Thông tin có tính toàn vẹn về mặt ý nghĩa.],
  cols: 1
)

#mcq(9, "TH",
  [Một tệp tài liệu có dung lượng $3 "MB"$. Khi quy đổi sang đơn vị Kilobyte ($"KB"$), dung lượng của tệp đó là:],
  [$3000 "KB"$], [$3072 "KB"$], [$24.576 "KB"$], [$384 "KB"$], cols: 4
)

#mcq(10, "TH",
  [Một dãy gồm $64$ bit liên tiếp trong bộ nhớ máy tính tương đương với bao nhiêu Byte?],
  [$4 "Byte"$], [$8 "Byte"$], [$16 "Byte"$], [$512 "Byte"$], cols: 4
)

#mcq(11, "NB",
  [Thiết bị nào sau đây là *thiết bị thông minh* (Smart device)?],
  [Máy tính bỏ túi Casio thông thường],
  [Đồng hồ cơ học lên dây cót],
  [Đồng hồ thông minh (Smartwatch) kết nối điện thoại và theo dõi nhịp tim],
  [Ổ cắm điện cơ học có công tắc bật/tắt],
  cols: 1
)

#mcq(12, "NB",
  [Thiết bị nào dưới đây là thiết bị số thông dụng *nhưng KHÔNG phải* là thiết bị thông minh?],
  [Điện thoại thông minh (Smartphone)],
  [Máy tính bảng (Tablet)],
  [Máy tính bỏ túi đơn giản chỉ thực hiện các phép tính số học cố định],
  [Robot hút bụi tự động lập bản đồ căn hộ và điều khiển qua Wi-Fi],
  cols: 1
)

#mcq(13, "NB",
  [Chiếc máy tính điện tử số đa năng đầu tiên tiêu biểu cho thế hệ máy tính thứ nhất (dùng đèn điện tử chân không, ra đời năm 1946) có tên là:],
  [IBM PC], [ENIAC], [Deep Blue], [AlphaGo], cols: 4
)

#mcq(14, "NB",
  [Ai là nhà khoa học đã phát minh ra *World Wide Web (WWW)* vào cuối thập niên 1980 – đầu thập niên 1990, thúc đẩy sự bùng nổ của Internet toàn cầu?],
  [Alan Turing], [John von Neumann], [Tim Berners-Lee], [Bill Gates], cols: 4
)

#mcq(15, "NB",
  [Mạng máy tính *ARPANET* (ra đời năm 1969 tại Mỹ) là tiền thân trực tiếp của thành tựu nào ngày nay?],
  [Hệ điều hành Windows], [Mạng Internet toàn cầu], [Ngôn ngữ lập trình Python], [Bàn phím máy tính], cols: 2
)

#mcq(16, "NB",
  [Năm 2016, chương trình trí tuệ nhân tạo nào đã đánh bại nhà vô địch cờ vây thế giới Lee Sedol, đánh dấu bước tiến vượt bậc của Học sâu (*Deep Learning*)?],
  [Deep Blue], [ELIZA], [AlphaGo], [ASIMO], cols: 4
)

#mcq(17, "NB",
  [Cuộc Cách mạng công nghiệp lần thứ tư (*CMCN 4.0*) dựa trên nền tảng cốt lõi nào sau đây?],
  [Động cơ hơi nước và cơ khí hoá ngành dệt.],
  [Năng lượng điện và dây chuyền sản xuất hàng loạt.],
  [Sự hội tụ của hệ thống thực – ảo, IoT, Trí tuệ nhân tạo (AI), Dữ liệu lớn (Big Data) và Điện toán đám mây.],
  [Chỉ sử dụng sức lao động thủ công truyền thống.],
  cols: 1
)

#mcq(18, "NB",
  [Hệ thống Cổng Dịch vụ công Quốc gia giúp người dân đăng kí thủ tục hành chính trực tuyến minh họa trực tiếp nhất cho đóng góp nào của tin học?],
  [Quản lí và điều hành tự động các hoạt động xã hội.],
  [Điều khiển robot hàn lắp ráp công nghiệp nặng.],
  [Giải mã trình tự gen sinh học phân tử.],
  [Chế tạo vật liệu siêu dẫn ngoài vũ trụ.],
  cols: 1
)

#mcq(19, "TH",
  [Vì sao điện thoại thông minh (*Smartphone*) được coi là một *hệ thống xử lí thông tin*?],
  [Vì điện thoại thông minh có màn hình sáng và vỏ kim loại bền đẹp.],
  [Vì nó thực hiện đầy đủ 4 hoạt động: tiếp nhận dữ liệu vào, xử lí, lưu trữ và đưa thông tin ra / truyền thông.],
  [Vì nó có giá thành cao hơn máy tính bỏ túi.],
  [Vì nó chỉ dùng để nghe gọi âm thanh tương tự điện thoại bàn cổ điển.],
  cols: 1
)

#mcq(20, "TH",
  [Trong nền *kinh tế tri thức*, yếu tố nào đóng vai trò quyết định nhất vào việc tạo ra giá trị gia tăng và sự phát triển bền vững?],
  [Khai thác cạn kiệt tài nguyên khoáng sản thô.],
  [Số lượng lao động cơ bắp giá rẻ.],
  [Tri thức khoa học – công nghệ, thông tin và đổi mới sáng tạo.],
  [Diện tích đất canh tác nông nghiệp truyền thống.],
  cols: 1
)

==== 2. Chủ đề B: Mạng máy tính và Internet (Câu 21 – Câu 38)

#mcq(21, "NB",
  [Phát biểu nào sau đây nêu đúng khái niệm *Internet vạn vật (IoT)*?],
  [Là mạng nội bộ chỉ nối các máy tính để bàn trong một phòng thực hành Tin học.],
  [Là việc liên kết các thiết bị thông minh, cảm biến, đồ vật qua Internet để tự động thu thập và trao đổi dữ liệu với nhau.],
  [Là tên một phần mềm diệt virus miễn phí cài trên máy tính cá nhân.],
  [Là dịch vụ chỉ dùng để gửi thư điện tử văn bản thuần túy.],
  cols: 1
)

#mcq(22, "NB",
  [Dịch vụ nào sau đây là dịch vụ lưu trữ dữ liệu trực tuyến dựa trên công nghệ *Điện toán đám mây*?],
  [Google Drive], [Microsoft Paint], [Windows Calculator], [USB Kingston 32 GB], cols: 2
)

#mcq(23, "NB",
  [Khi học sinh mở trình duyệt web để soạn thảo văn bản chung với nhóm trên *Google Docs* mà không cần cài đặt phần mềm vào máy, các em đang sử dụng mô hình đám mây nào?],
  [IaaS (Hạ tầng hướng dịch vụ)],
  [PaaS (Nền tảng hướng dịch vụ)],
  [SaaS (Phần mềm hướng dịch vụ)],
  [LAN (Mạng cục bộ không kết nối Internet)],
  cols: 2
)

#mcq(24, "NB",
  [Về mặt *quyền sở hữu*, mạng Internet có đặc điểm gì khác biệt căn bản so với mạng LAN?],
  [Internet thuộc sở hữu độc quyền của tập đoàn Microsoft.],
  [Internet thuộc sở hữu riêng của một quốc gia duy nhất.],
  [Internet không thuộc quyền sở hữu của bất kì cá nhân hay tổ chức riêng lẻ nào.],
  [Internet có phạm vi nhỏ hơn mạng LAN của một trường học.],
  cols: 1
)

#mcq(25, "TH",
  [Một trường THPT kết nối 40 máy tính trong hai phòng thực hành với 1 máy chủ và 1 máy in dùng chung qua Switch nội bộ. Hệ thống mạng nội bộ này của nhà trường được phân loại là:],
  [Mạng cục bộ (LAN)], [Mạng toàn cầu Internet], [Hệ thống định vị vệ tinh GPS], [Mạng viễn thông xuyên lục địa], cols: 2
)

#mcq(26, "TH",
  [Ứng dụng nào sau đây thể hiện rõ nhất lợi ích của *IoT (Internet vạn vật)* trong lĩnh vực giao thông hiện đại tại Việt Nam?],
  [Người lái xe dừng lại mua vé giấy và trả tiền mặt tại trạm thu phí.],
  [Hệ thống thu phí tự động không dừng ETC tự nhận diện thẻ xe, trừ phí điện tử và mở barie tự động.],
  [Người dân tra cứu bản đồ giấy in xuất bản cách đây 5 năm.],
  [Soạn thảo văn bản báo cáo giao thông trên phần mềm Notepad không nối mạng.],
  cols: 1
)

#mcq(27, "NB",
  [Loại phần mềm độc hại nào *phải gắn (ký sinh) vào một tệp chương trình/tài liệu hợp pháp* và chỉ kích hoạt khi người dùng chạy tệp vật chủ đó?],
  [Virus máy tính], [Sâu máy tính (Worm)], [Ngựa thành Troa (Trojan)], [Tường lửa (Firewall)], cols: 2
)

#mcq(28, "NB",
  [Loại phần mềm độc hại nào là *chương trình độc lập hoàn chỉnh*, có khả năng *tự nhân bản và tự lây lan qua mạng máy tính* mà không cần tệp vật chủ?],
  [Virus máy tính], [Sâu máy tính (Worm)], [Phần mềm soạn thảo Word], [Trình duyệt Chrome], cols: 2
)

#mcq(29, "NB",
  [Phần mềm độc hại *Ngựa thành Troa (Trojan)* xâm nhập vào máy tính bằng phương thức đặc trưng nào?],
  [Tự động nhân bản qua cáp điện nguồn 220V.],
  [Ngụy trang dưới vỏ bọc phần mềm hợp pháp, hữu ích hoặc miễn phí (*crack*) để lừa người dùng tự cài đặt.],
  [Chỉ lây qua đĩa mềm từ tính đời cũ.],
  [Là công cụ bảo mật mặc định của hệ điều hành Windows.],
  cols: 1
)

#mcq(30, "NB",
  [Loại mã độc chuyên *mã hóa toàn bộ dữ liệu trên máy nạn nhân rồi đòi tiền chuộc* mới cung cấp khóa giải mã được gọi là:],
  [Adware], [Spyware], [Ransomware], [Freeware], cols: 4
)

#mcq(31, "NB",
  [Khi không may bị kẻ xấu *bắt nạt trên mạng xã hội* (nhắn tin đe dọa, tung tin bôi nhọ), hành động nào sau đây là *ĐÚNG ĐẮN NHẤT*?],
  [Lập tức dùng lời lẽ thô tục chửi bới, đôi co lại trên mạng để trả đũa.],
  [Giấu kín một mình, tự chịu đựng không dám nói với bất kì ai.],
  [Không đáp trả tiêu cực; chụp màn hình lưu bằng chứng; chặn/báo cáo tài khoản và chia sẻ ngay với cha mẹ, thầy cô.],
  [Chuyển tiền theo mọi yêu cầu của kẻ đe dọa để mong họ xóa bài.],
  cols: 1
)

#mcq(32, "NB",
  [Phần mềm nào sau đây là công cụ thông dụng dùng để *ngăn ngừa và diệt phần mềm độc hại* tích hợp sẵn trên Windows 10/11?],
  [Windows Security (Microsoft Defender)],
  [Microsoft Excel],
  [VLC Media Player],
  [Unikey],
  cols: 2
)

#mcq(33, "NB",
  [Website nào sau đây là *nguồn học liệu mở chính thống tại Việt Nam* phục vụ học sinh, giáo viên học tập và tra cứu miễn phí?],
  [`igiaoduc.vn` (Hệ tri thức Việt số hoá)],
  [Các trang web chia sẻ phim lậu không bản quyền],
  [Các diễn đàn chia sẻ phần mềm bẻ khóa (*crack*)],
  [Các đường link rút gọn trúng thưởng không rõ nguồn gốc],
  cols: 2
)

#mcq(34, "TH",
  [Mật khẩu nào dưới đây được đánh giá là *mật khẩu mạnh và an toàn nhất* cho tài khoản cá nhân?],
  [`12345678`], [`nguyenvanan`], [`01012010`], [`Tr@ngAn#2026!Tin`], cols: 4
)

#mcq(35, "TH",
  [Bạn Minh nhận được một email lạ thông báo *"Tài khoản ngân hàng của bạn sắp bị khóa, hãy bấm ngay vào link `http://nganhang-xacminh-vip.xyz` và nhập mật khẩu + mã OTP"*. Minh nên làm gì?],
  [Nhập ngay mật khẩu và mã OTP vì sợ bị khóa tài khoản.],
  [Tuyệt đối không bấm vào link lạ, không cung cấp OTP vì đây là dấu hiệu lừa đảo giả mạo (*Phishing*); liên hệ tổng đài chính thức của ngân hàng để kiểm tra.],
  [Chuyển tiếp email đó cho tất cả bạn bè cùng bấm vào thử.],
  [Tắt phần mềm diệt virus để mở được đường link nhanh hơn.],
  cols: 1
)

#mcq(36, "TH",
  [Biện pháp nào sau đây giúp khôi phục lại tài liệu học tập quan trọng ngay cả khi ổ cứng máy tính bị hỏng đột ngột hoặc bị nhiễm mã độc tống tiền (*Ransomware*)?],
  [Đặt màn hình nền máy tính màu tối.],
  [Đổi tên tệp tài liệu sang chữ in hoa.],
  [Thực hiện sao lưu dự phòng (*Backup*) định kì dữ liệu lên dịch vụ đám mây hoặc ổ cứng rời tách biệt.],
  [Xóa lịch sử trình duyệt web mỗi tuần.],
  cols: 1
)

#mcq(37, "TH",
  [Để tra cứu nhanh nghĩa Tiếng Việt của một tài liệu khoa học Tiếng Anh định dạng `.pdf` dài 15 trang mà vẫn giữ nguyên bố cục đoạn văn, cách làm hiệu quả nhất trên PC là:],
  [Gõ lại thủ công từng từ một vào từ điển giấy.],
  [Sử dụng chức năng dịch *Tài liệu (Documents)* trên công cụ dịch tự động `translate.google.com` rồi đọc đối chiếu chỉnh sửa thuật ngữ.],
  [Đổi đuôi tệp `.pdf` thành `.mp3`.],
  [Nén tệp `.pdf` thành tệp `.zip`.],
  cols: 1
)

#mcq(38, "TH",
  [Hành động nào sau đây tiềm ẩn nguy cơ cao nhất làm máy tính cá nhân bị nhiễm phần mềm độc hại *Trojan* và *Keylogger*?],
  [Cập nhật bản vá bảo mật từ Windows Update chính thức.],
  [Tải và chạy công cụ bẻ khóa (*crack / keygen*) từ trang web trôi nổi để dùng chùa phần mềm trả phí.],
  [Truy cập Cổng thông tin điện tử của Bộ Giáo dục và Đào tạo.],
  [Bật xác thực hai yếu tố (2FA) cho tài khoản thư điện tử.],
  cols: 1
)

==== 3. Chủ đề D: Đạo đức, pháp luật và văn hoá trong môi trường số (Câu 39 – Câu 50)

#mcq(39, "NB",
  [Văn bản pháp luật nào của Quốc hội quy định *Điều 12 về các hành vi bị nghiêm cấm trong hoạt động công nghệ thông tin* (như vu khống, phát tán virus, xâm phạm sở hữu trí tuệ...)?],
  [Luật Giao thông đường bộ],
  [Luật Công nghệ thông tin năm 2006],
  [Luật Đất đai],
  [Luật Hôn nhân và gia đình],
  cols: 2
)

#mcq(40, "NB",
  [*Luật An ninh mạng* của Việt Nam được Quốc hội thông qua năm 2018 (có hiệu lực từ ngày 01/01/2019) hướng tới mục tiêu trọng tâm nào sau đây?],
  [Khuyến khích sao chép tự do mọi phần mềm thương mại mà không cần trả phí.],
  [Bảo vệ an ninh quốc gia, bảo đảm trật tự, an toàn xã hội trên không gian mạng và quyền, lợi ích hợp pháp của tổ chức, cá nhân.],
  [Cấm hoàn toàn công dân Việt Nam sử dụng mạng xã hội và thư điện tử.],
  [Quy định cấu hình phần cứng bắt buộc của màn hình máy tính.],
  cols: 1
)

#mcq(41, "NB",
  [Theo *Nghị định số 15/2020/NĐ-CP* (Điều 101, sửa đổi bởi NĐ 14/2022/NĐ-CP), hành vi lợi dụng mạng xã hội để *cung cấp, chia sẻ thông tin giả mạo, sai sự thật, xuyên tạc, vu khống, xúc phạm danh dự cá nhân* sẽ bị xử lí như thế nào?],
  [Không bị xử lí vì mạng xã hội là trang cá nhân tự do tuyệt đối.],
  [Chỉ bị nhắc nhở miệng mà không phải gỡ bài.],
  [Bị xử phạt vi phạm hành chính bằng tiền và buộc gỡ bỏ thông tin sai sự thật (nặng hơn có thể bị truy cứu trách nhiệm hình sự).],
  [Được nhà mạng thưởng thêm dung lượng truy cập.],
  cols: 1
)

#mcq(42, "NB",
  [Quyền của tổ chức, cá nhân đối với tác phẩm do mình sáng tạo ra hoặc sở hữu (bao gồm bài viết, hình ảnh, bản nhạc, video, chương trình máy tính...) được pháp luật bảo hộ gọi là:],
  [Quyền tác giả (Bản quyền)], [Quyền miễn trừ giao thông], [Quyền quản trị mạng LAN], [Quyền truy cập Wi-Fi], cols: 2
)

#mcq(43, "NB",
  [Theo Bộ Quy tắc ứng xử trên mạng xã hội (Quyết định 874/QĐ-BTTTT năm 2021), đâu là một trong 4 quy tắc ứng xử chung đối với mọi tổ chức, cá nhân?],
  [Quy tắc ẩn danh tuyệt đối để bình luận tự do.],
  [Quy tắc Tôn trọng, tuân thủ pháp luật; Lành mạnh; An toàn, bảo mật thông tin; Trách nhiệm.],
  [Quy tắc chia sẻ mọi tin đồn càng nhanh càng tốt.],
  [Quy tắc tự do dùng ảnh người khác làm quảng cáo.],
  cols: 1
)

#mcq(44, "NB",
  [Hành vi nào sau đây là *hành vi vi phạm pháp luật* trong môi trường số?],
  [Trích dẫn một câu nói ngắn của học giả trong bài thuyết trình học tập và ghi rõ tên tác giả, nguồn sách.],
  [Cài đặt phần mềm văn phòng mã nguồn mở miễn phí LibreOffice từ trang chủ nhà phát triển.],
  [Bẻ khóa (*crack*) phần mềm thương mại rồi đóng gói bán lại thu lời trên mạng xã hội.],
  [Chia sẻ thông báo lịch thi chính thức từ fanpage của nhà trường.],
  cols: 1
)

#mcq(45, "TH",
  [Bạn K mua 01 tài khoản đọc sách điện tử bản quyền dành riêng cho cá nhân. Sau đó K tải toàn bộ các tệp sách về, xóa thông tin bảo vệ rồi đăng lên nhóm công khai cho hàng nghìn người tải miễn phí. Nhận định nào đúng về việc làm của K?],
  [K hoàn toàn đúng pháp luật vì K đã bỏ tiền mua tài khoản nên có toàn quyền phát tán.],
  [K không vi phạm vì K chia sẻ miễn phí chứ không thu tiền của mọi người.],
  [K đã vi phạm quyền tác giả (quyền tài sản về sao chép, phân phối tác phẩm) theo Luật Sở hữu trí tuệ vì K chỉ mua quyền đọc cá nhân chứ không sở hữu quyền phân phối tác phẩm.],
  [K chỉ vi phạm nội quy lớp học chứ không liên quan tới pháp luật.],
  cols: 1
)

#mcq(46, "TH",
  [Trường hợp sử dụng tác phẩm đã công bố nào dưới đây *KHÔNG* bị coi là xâm phạm quyền tác giả theo Luật Sở hữu trí tuệ?],
  [Sao chép nguyên văn khóa luận của người khác rồi đổi tên tác giả thành tên mình (*đạo văn*).],
  [Trích dẫn hợp lí một đoạn ngắn tác phẩm mà không làm sai ý tác giả để minh họa trong bài viết học tập của mình, không nhằm mục đích thương mại và *ghi rõ tên tác giả, nguồn gốc tác phẩm*.],
  [Quay lén bộ phim đang chiếu rạp phát trực tiếp (*livestream*) trên trang cá nhân để bán hàng.],
  [Tải bộ ảnh nghệ thuật độc quyền của nhiếp ảnh gia, cắt bỏ chữ kí (*watermark*) rồi in lên áo thun để bán.],
  cols: 1
)

#mcq(47, "TH",
  [Do mâu thuẫn nhỏ trong lớp, bạn P tự ý lấy ảnh cá nhân của bạn Q, cắt ghép xuyên tạc kèm lời lẽ xúc phạm rồi đăng lên diễn đàn công khai. Hành vi của P đã xâm phạm những gì?],
  [Chỉ là trò đùa vô hại trên mạng ảo, không vi phạm gì.],
  [Vừa vi phạm chuẩn mực đạo đức, văn hoá ứng xử, vừa vi phạm pháp luật (xâm phạm quyền đối với hình ảnh, danh dự, nhân phẩm công dân theo Bộ luật Dân sự, Luật CNTT và Luật An ninh mạng).],
  [Chỉ làm tốn dung lượng máy chủ của mạng xã hội.],
  [Chỉ vi phạm Luật Giao thông.],
  cols: 1
)

#mcq(48, "TH",
  [Vì sao hành vi vi phạm bản quyền đối với các *sản phẩm số* (phần mềm, nhạc số, phim số, sách điện tử) thường gây thiệt hại nhanh và nghiêm trọng hơn so với sản phẩm vật lí truyền thống?],
  [Vì sản phẩm số dễ sao chép nguyên bản với chi phí gần như bằng 0 và phát tán tức thời cho hàng triệu người qua Internet.],
  [Vì sản phẩm số nặng hàng chục kilôgam nên tốn phí vận chuyển.],
  [Vì pháp luật Việt Nam chưa có quy định bảo hộ chương trình máy tính.],
  [Vì máy tính không thể cài phần mềm có bản quyền.],
  cols: 1
)

#mcq(49, "TH",
  [Trước khi nhấn nút *"Chia sẻ" (Share)* một thông tin giật gân trên mạng xã hội, thói quen nào sau đây giúp học sinh đảm bảo tính *an toàn và hợp pháp*?],
  [Chia sẻ ngay lập tức kẻo bài viết bị xóa mất rồi mới kiểm tra sau.],
  [Kiểm chứng độ xác thực từ các cơ quan báo chí/cổng thông tin chính thống, đánh giá xem nội dung có vi phạm pháp luật, bản quyền hay quyền riêng tư của ai không.],
  [Chỉ cần thấy bài viết có trên 10.000 lượt thích (Like) thì chắc chắn là thông tin thật 100%.],
  [Thêm các lời bình luận kích động để thu hút nhiều người vào tranh cãi.],
  cols: 1
)

#mcq(50, "TH",
  [Khi làm video bài tập nhóm môn Lịch sử để đăng lên YouTube công khai, nhóm học sinh cần nhạc nền minh họa. Giải pháp nào sau đây vừa *đúng luật bản quyền* vừa tiết kiệm chi phí?],
  [Lấy bất kì bài hát nổi tiếng có bản quyền nào ghép vào và tắt phần ghi tên nhạc sĩ.],
  [Sử dụng các bản nhạc miễn phí bản quyền từ Thư viện âm thanh YouTube (*YouTube Audio Library*) hoặc nhạc có giấy phép mở *Creative Commons (CC)* và ghi nguồn đúng quy định của giấy phép.],
  [Dùng phần mềm xóa bản quyền âm thanh trái phép.],
  [Tự nhận mình là người sáng tác bản nhạc nổi tiếng đó.],
  cols: 1
)

==== Bảng đáp án chuẩn & Giải thích nhanh 50 câu Trắc nghiệm 4 lựa chọn

#block(breakable: false)[
  #set text(size: 8.3pt)
  #table(
    columns: (1fr,) * 10,
    inset: 4.5pt,
    stroke: 0.45pt + c-border,
    align: center + horizon,
    fill: (x, y) => if calc.even(y) { rgb("#eff6ff") } else { white },
    [*1. B*], [*2. C*], [*3. A*], [*4. C*], [*5. D*], [*6. B*], [*7. C*], [*8. C*], [*9. B*], [*10. B*],
    [*11. C*], [*12. C*], [*13. B*], [*14. C*], [*15. B*], [*16. C*], [*17. C*], [*18. A*], [*19. B*], [*20. C*],
    [*21. B*], [*22. A*], [*23. C*], [*24. C*], [*25. A*], [*26. B*], [*27. A*], [*28. B*], [*29. B*], [*30. C*],
    [*31. C*], [*32. A*], [*33. A*], [*34. D*], [*35. B*], [*36. C*], [*37. B*], [*38. B*], [*39. B*], [*40. B*],
    [*41. C*], [*42. A*], [*43. B*], [*44. C*], [*45. C*], [*46. B*], [*47. B*], [*48. A*], [*49. B*], [*50. B*],
  )
]

*Giải thích trọng tâm các câu Thông hiểu cần lưu ý:*
- *Câu 8 (C):* Sai vì cùng một dữ liệu (ví dụ bản tin chữ Hán hoặc phim chụp X-quang) nhưng người biết chuyên môn/ngôn ngữ sẽ rút ra thông tin hữu ích, còn người không biết chữ/chuyên môn không rút ra được thông tin đó.
- *Câu 9 (B):* $3 "MB" = 3 times 1024 "KB" = 3072 "KB"$ (không nhân với $1000$). *Câu 10 (B):* $64 "bit" : 8 = 8 "Byte"$.
- *Câu 23 (C):* *Google Docs* là phần mềm ứng dụng chạy trực tiếp trên mây cho người dùng cuối $->$ *SaaS*.
- *Câu 27–30:* Nhớ kĩ bộ tứ mã độc: *Virus* = gắn vật chủ; *Worm* = độc lập tự nhân bản qua mạng; *Trojan* = ngụy trang phần mềm lành/crack mở cửa hậu; *Ransomware* = mã hóa đòi tiền chuộc.
- *Câu 45–46:* Mua bản sao chỉ có *quyền sử dụng cá nhân*, tự ý phát tán công khai là xâm phạm *quyền tài sản (sao chép, phân phối)* của chủ sở hữu quyền tác giả; chỉ trích dẫn ngắn hợp lí phi thương mại và *ghi rõ nguồn + tác giả* mới hợp pháp.

=== Mục B. Ngân hàng 08 câu Trắc nghiệm Đúng/Sai chuẩn định dạng mới (32 mệnh đề)

#tfq(
  "ĐS 01", "Chủ đề A.2 • Thiết bị thông minh",
  [Gia đình bạn Nam vừa trang bị một chiếc *đồng hồ thông minh (Smartwatch)* cho ông nội và một *robot hút bụi thông minh* kết nối với điện thoại qua mạng Wi-Fi trong nhà. Khi thảo luận về các thiết bị này, bạn Nam đưa ra các nhận định sau:],
  [Đồng hồ thông minh là một hệ thống xử lí thông tin vì nó có cảm biến thu nhận nhịp tim (đầu vào), bộ vi xử lí phân tích, bộ nhớ lưu lịch sử sức khỏe và màn hình hiển thị kết quả (đầu ra).],
  [Chiếc máy tính bỏ túi Casio đơn thuần chỉ tính cộng, trừ, nhân, chia cố định và không có khả năng kết nối mạng hay hoạt động tự chủ cũng được xếp vào nhóm thiết bị thông minh.],
  [Khi ông nội đi tập thể dục, đồng hồ thông minh phát hiện nhịp tim tăng bất thường và tự động gửi thông báo cảnh báo về điện thoại của bố Nam thông qua mạng 4G/Wi-Fi; đây là minh họa thiết thực vai trò của thiết bị thông minh trong chăm sóc sức khỏe hiện đại.],
  [Nếu tắt kết nối Wi-Fi của căn nhà, robot hút bụi thông minh lập tức biến thành vật vô tri không còn bất kì bộ xử lí hay bộ nhớ nào bên trong để chạy chế độ hút bụi cơ bản.],
)

#tfq(
  "ĐS 02", "Chủ đề A.2 • Thành tựu Tin học & CMCN 4.0",
  [Trong buổi sinh hoạt câu lạc bộ Tin học với chủ đề *"Lịch sử phát triển máy tính và cuộc Cách mạng công nghiệp 4.0"*, nhóm thuyết trình nêu ra các mệnh đề sau:],
  [Sự ra đời của giao diện đồ họa người dùng (*GUI*) và máy tính cá nhân (*PC*) trong thập niên 1970–1980 đã giúp máy tính trở nên thân thiện, dễ sử dụng đối với đông đảo người dân không chuyên.],
  [Cuộc Cách mạng công nghiệp lần thứ tư (CMCN 4.0) bắt đầu từ cuối thế kỉ XVIII gắn liền với việc phát minh ra động cơ hơi nước.],
  [Tại một nhà máy dệt may hiện đại, việc lắp đặt hàng trăm cảm biến trên máy dệt để thu thập dữ liệu vận hành theo thời gian thực gửi về phần mềm AI dự đoán hỏng hóc trước khi máy ngừng chạy là ứng dụng tiêu biểu của CMCN 4.0.],
  [Trong nền kinh tế tri thức, một doanh nghiệp phần mềm muốn nâng cao năng lực cạnh tranh thì chỉ cần tăng số giờ lao động thủ công mà không cần đầu tư nghiên cứu thuật toán hay đào tạo nhân lực công nghệ cao.],
)

#tfq(
  "ĐS 03", "Chủ đề A.2 • Đóng góp của Tin học đối với xã hội",
  [Bệnh viện Đa khoa tỉnh X triển khai hệ thống *Bệnh án điện tử*, đặt lịch khám trực tuyến qua ứng dụng di động và ứng dụng phần mềm hỗ trợ đọc ảnh chụp cắt lớp CT phổi. Xét các nhận định sau:],
  [Hệ thống đặt lịch khám trực tuyến và quản lí bệnh án điện tử thể hiện đóng góp của tin học trong việc quản lí, điều hành tự động giúp giảm thời gian chờ đợi của người bệnh.],
  [Tin học chỉ hỗ trợ công tác lưu trữ giấy tờ hành chính chứ hoàn toàn không thể ứng dụng vào các bài toán khoa học – y sinh phức tạp như phân tích hình ảnh y khoa hay giải mã gen.],
  [Khi bác sĩ tuyến tỉnh hội chẩn trực tuyến qua video kết hợp chia sẻ dữ liệu ảnh chụp CT thời gian thực với chuyên gia tuyến trung ương để cấp cứu ca bệnh khó, tin học đã giúp xóa bỏ rào cản khoảng cách địa lí trong khám chữa bệnh.],
  [Bệnh viện có thể công khai toàn bộ hồ sơ bệnh án chi tiết và số căn cước công dân của mọi bệnh nhân lên trang web công cộng không cần mật khẩu để người dân tiện tra cứu.],
)

#tfq(
  "ĐS 04", "Chủ đề A.1 & A.2 • Hệ thống xử lí & lưu trữ số",
  [Trường THPT A tiến hành số hóa thư viện truyền thống sang *Thư viện số*: toàn bộ sách tham khảo và học liệu được lưu trữ trên máy chủ kết hợp máy tính bảng tra cứu tại phòng đọc. Xét các nhận định sau:],
  [Các tệp PDF sách điện tử lưu trong ổ cứng máy chủ là *dữ liệu*, còn kiến thức học sinh lĩnh hội được sau khi đọc hiểu nội dung cuốn sách là *thông tin*.],
  [Việc chuyển sang lưu trữ số giúp thư viện tiết kiệm diện tích kệ sách vật lí và cho phép nhiều học sinh cùng tra cứu từ khóa trong một tài liệu chỉ mất vài giây.],
  [Một ổ đĩa lưu trữ chuyên dụng của thư viện còn trống $8 "GB"$ sẽ lưu trữ được tối đa đúng $500$ cuốn sách điện tử, biết dung lượng trung bình mỗi cuốn là $16 "MB"$.],
  [Nếu đường truyền mạng nội bộ truyền dữ liệu với tốc độ thực tế $80 "Mbps"$ (Megabit/giây) thì để tải một video thí nghiệm Vật lí dung lượng $160 "MB"$ (Megabyte) chỉ mất đúng $2$ giây.],
)

#tfq(
  "ĐS 05", "Chủ đề B.1 • So sánh mạng LAN và Internet",
  [Phòng Tin học của trường có 35 máy tính học sinh và 1 máy tính giáo viên được nối với nhau qua bộ chuyển mạch *Switch*, đồng thời nối ra ngoài qua *Router* của nhà mạng viễn thông để truy cập web. Xét các phát biểu sau:],
  [Hệ thống mạng kết nối 36 máy tính và máy in dùng chung bên trong phòng Tin học thuộc quyền sở hữu, quản lí riêng của nhà trường và được gọi là mạng cục bộ (*LAN*).],
  [Mạng Internet toàn cầu mà phòng máy kết nối tới thuộc quyền sở hữu riêng của nhà cung cấp dịch vụ viễn thông (ISP) tại địa phương.],
  [Nếu dây cáp quang từ nhà mạng bên ngoài vào trường tạm thời bị đứt, giáo viên vẫn có thể chia sẻ tệp đề bài tập từ máy giáo viên sang 35 máy học sinh thông qua mạng LAN nội bộ đang hoạt động bình thường.],
  [Để hai học sinh ngồi ở hai tỉnh khác nhau cùng chơi cờ vua trực tuyến và trò chuyện qua mạng, chỉ cần mỗi nhà tự lắp một bộ Switch mạng LAN nội bộ mà không cần đăng kí kết nối Internet.],
)

#tfq(
  "ĐS 06", "Chủ đề B.1 • Dịch vụ Điện toán đám mây",
  [Nhóm của bạn Mai gồm 4 thành viên cùng thực hiện bài thuyết trình môn Tin học 10 bằng cách tạo thư mục chung trên *Google Drive* và cùng biên tập trên tệp *Google Slides*. Xét các nhận định sau:],
  [Google Drive và Google Slides là các dịch vụ cụ thể của công nghệ Điện toán đám mây (*Cloud Computing*) cung cấp cho người dùng qua Internet.],
  [Việc sử dụng Google Slides trực tiếp trên trình duyệt web thuộc mô hình *IaaS (Hạ tầng hướng dịch vụ)* vì học sinh phải tự cài đặt hệ điều hành cho máy chủ của Google.],
  [Khi máy tính cá nhân của Mai bất ngờ bị hỏng ổ cứng ở nhà, Mai vẫn có thể mượn máy tính ở thư viện trường đăng nhập tài khoản Google để mở lại nguyên vẹn bài thuyết trình đã lưu trên đám mây (nếu tài khoản được bảo mật tốt).],
  [Các thành viên trong nhóm có thể làm việc đồng thời trên cùng tệp Google Slides ngay cả khi cả 4 máy tính đều ngắt hoàn toàn kết nối Internet trong suốt quá trình làm việc nhóm.],
)

#tfq(
  "ĐS 07", "Chủ đề B.1 • Internet vạn vật (IoT) trong đời sống",
  [Hợp tác xã nông nghiệp công nghệ cao tại Nghệ An lắp đặt hệ thống *IoT nhà màng trồng dưa lưới*: các cảm biến độ ẩm đất, nhiệt độ, ánh sáng kết nối Internet gửi số liệu liên tục về hệ thống điều khiển tưới nhỏ giọt tự động và ứng dụng trên điện thoại của kĩ sư. Xét các nhận định sau:],
  [Hệ thống trên là ví dụ điển hình của Internet vạn vật (*IoT*) vì các cảm biến và thiết bị tưới được định danh, kết nối mạng và tự động trao đổi dữ liệu để điều khiển mà ít cần con người túc trực thủ công.],
  [Mọi hệ thống IoT chỉ hoạt động được trong phạm vi dưới 2 mét bằng cáp USB và bắt buộc phải có người đứng bấm nút tưới nước mỗi giờ.],
  [Nhờ IoT, hợp tác xã tiết kiệm được lượng nước tưới, phân bón, giảm công lao động thủ công mà vẫn duy trì điều kiện sinh trưởng tối ưu đồng đều cho vườn dưa.],
  [Để tiện cho nhiều người xem, kĩ sư nông nghiệp nên giữ nguyên mật khẩu mặc định `admin / 123456` của bộ điều khiển IoT và đăng công khai địa chỉ điều khiển lên mạng xã hội.],
)

#tfq(
  "ĐS 08", "Chủ đề B.1 & B.2 • Mạng máy tính trong học tập & An toàn số",
  [Lớp 10A sử dụng hệ thống quản lí học tập trực tuyến (*LMS*), khai thác kho học liệu mở `igiaoduc.vn` và trao đổi bài qua nhóm trực tuyến. Xét các mệnh đề nhận định sau:],
  [Sự phổ biến của mạng máy tính và Internet đã làm thay đổi phương thức học tập, cho phép học sinh tiếp cận nguồn tri thức mở đa phương tiện mọi lúc, mọi nơi.],
  [Mọi tệp đính kèm có đuôi `.exe` được gửi từ tài khoản lạ trong các nhóm chat công cộng kèm lời mời *"Phần mềm tăng điểm thi miễn phí"* đều là học liệu mở an toàn tuyệt đối.],
  [Khi tải tài liệu tham khảo Tiếng Anh từ kho học liệu mở, học sinh có thể kết hợp công cụ dịch tự động (như Google Dịch) để nắm nhanh ý chính rồi đối chiếu lại thuật ngữ chuyên môn Tiếng Việt trong SGK.],
  [Để bảo vệ tài khoản học tập trực tuyến của mình khi sử dụng máy tính ở tiệm Internet công cộng, học sinh nên dùng chế độ duyệt web ẩn danh (*Incognito*), không lưu mật khẩu trên trình duyệt và đăng xuất ngay sau khi học xong.],
)

==== Bảng đáp án & Giải thích chi tiết 08 câu Đúng/Sai (32 mệnh đề)

#block(breakable: true)[
  #set text(size: 8.4pt)
  #table(
    columns: (0.65fr, 1.05fr, 3.3fr),
    inset: (x: 6pt, y: 5pt),
    stroke: 0.45pt + c-border,
    fill: (x, y) => if y == 0 { c-teal } else if calc.odd(y) { white } else { c-teal-bg },
    table.header(
      [#text(fill: white, weight: "bold")[Câu]],
      [#text(fill: white, weight: "bold")[Đáp án 4 ý]],
      [#text(fill: white, weight: "bold")[Giải thích cốt lõi từng ý (a, b, c, d)]],
    ),
    [*ĐS 01*], [*a) Đ • b) S*\ *c) Đ • d) S*],
    [*a) Đúng* (đủ 4 khâu Input–Process–Storage–Output). *b) Sai* (máy tính bỏ túi cơ bản chỉ là thiết bị số thông thường, không tự chủ/kết nối mạng). *c) Đúng* (vai trò thiết bị thông minh/IoT y tế). *d) Sai* (mất Wi-Fi chỉ mất kết nối từ xa, chip xử lí và bộ nhớ bên trong robot vẫn chạy chế độ tự hành nội bộ được).],
    [*ĐS 02*], [*a) Đ • b) S*\ *c) Đ • d) S*],
    [*a) Đúng* (GUI + PC phổ cập máy tính). *b) Sai* (động cơ hơi nước TK XVIII là CMCN 1.0, không phải 4.0). *c) Đúng* (cảm biến IoT + Big Data + AI bảo trì dự đoán là đặc trưng CMCN 4.0). *d) Sai* (kinh tế tri thức dựa vào tri thức KH-CN và nhân lực chất lượng cao chứ không phải lao động thủ công).],
    [*ĐS 03*], [*a) Đ • b) S*\ *c) Đ • d) S*],
    [*a) Đúng* (đóng góp quản lí & điều hành tự động). *b) Sai* (tin học đóng vai trò then chốt giải quyết bài toán khoa học y sinh phức tạp). *c) Đúng* (Telehealth xóa khoảng cách địa lí). *d) Sai* (hồ sơ bệnh án và CCCD là dữ liệu cá nhân/bí mật đời tư cần bảo mật tuyệt đối).],
    [*ĐS 04*], [*a) Đ • b) Đ*\ *c) S • d) S*],
    [*a) Đúng* (phân biệt chuẩn dữ liệu vs thông tin). *b) Đúng* (ưu việt lưu trữ số). *c) Sai* vì $8 "GB" = 8 times 1024 = 8192 "MB"$; chia cho $16 "MB"$ được tối đa *$512$ cuốn sách* (chứ không phải $500$ do nhầm $1000$). *d) Sai* vì $160 "MB" = 160 times 8 = 1280 "Mb"$; chia tốc độ $80 "Mbps"$ mất *$16$ giây* (nhầm `MB` với `Mb` mới ra $2$ giây!).],
    [*ĐS 05*], [*a) Đ • b) S*\ *c) Đ • d) S*],
    [*a) Đúng* (mạng LAN phạm vi phòng máy, thuộc sở hữu nhà trường). *b) Sai* (Internet không thuộc quyền sở hữu của bất kì tổ chức hay ISP riêng lẻ nào). *c) Đúng* (LAN vẫn truyền dữ liệu nội bộ qua Switch dù đứt đường ra Internet). *d) Sai* (kết nối hai tỉnh khác nhau bắt buộc cần mạng diện rộng/Internet, LAN chỉ nối phạm vi hẹp).],
    [*ĐS 06*], [*a) Đ • b) S*\ *c) Đ • d) S*],
    [*a) Đúng*. *b) Sai* vì Google Slides là phần mềm ứng dụng cho người dùng cuối chạy trên trình duyệt $->$ thuộc mô hình *SaaS* (không phải IaaS). *c) Đúng* (ưu điểm lưu trữ đám mây không phụ thuộc 1 thiết bị vật lí). *d) Sai* (cộng tác thời gian thực trên đám mây đòi hỏi phải có kết nối Internet để đồng bộ dữ liệu).],
    [*ĐS 07*], [*a) Đ • b) S*\ *c) Đ • d) S*],
    [*a) Đúng* (bản chất IoT). *b) Sai* (IoT kết nối qua Internet không giới hạn 2m và tự động hóa không cần bấm tay mỗi giờ). *c) Đúng* (lợi ích kinh tế – kĩ thuật của IoT nông nghiệp). *d) Sai* (để mật khẩu mặc định và công khai địa chỉ điều khiển khiến tin tặc dễ chiếm quyền phá hoại hệ thống).],
    [*ĐS 08*], [*a) Đ • b) S*\ *c) Đ • d) Đ*],
    [*a) Đúng* (thay đổi phương thức học tập hiện đại). *b) Sai* (tệp `.exe` lạ mạo danh phần mềm miễn phí/gian lận là nguồn lây *Trojan/Virus* cực kì nguy hiểm). *c) Đúng* (vận dụng dịch tự động + học liệu mở đúng cách). *d) Đúng* (nguyên tắc bảo vệ tài khoản trên máy công cộng).],
  )
]

=== Mục C. Hệ thống 09 Bài tập & Câu hỏi Tự luận trọng tâm (Có lời giải & biểu điểm)

#essay-qa(
  "01", "VD", "1,0 điểm • Chủ đề A.1",
  [Một chiếc thẻ nhớ của máy ảnh kĩ thuật số có dung lượng trống thực tế là $32 "GB"$.
  a) Hãy đổi dung lượng trống đó sang đơn vị Megabyte ($"MB"$) và Kilobyte ($"KB"$).
  b) Người thợ ảnh dùng thẻ nhớ này để lưu $5$ đoạn video hậu trường (mỗi đoạn video nặng $1,5 "GB"$) và phần dung lượng còn lại dùng để chụp ảnh chất lượng cao (trung bình mỗi bức ảnh nặng $8 "MB"$). Hỏi người thợ ảnh chụp và lưu thêm được *tối đa bao nhiêu bức ảnh*?],
  [
    - *Ý a (0,50 điểm):* Áp dụng quy tắc chuyển đổi $1 "GB" = 1024 "MB"$ và $1 "MB" = 1024 "KB"$:
      - Dung lượng tính theo Megabyte: $32 "GB" = 32 times 1024 = bold("32.768 MB")$ *(0,25đ)*.
      - Dung lượng tính theo Kilobyte: $32.768 "MB" = 32.768 times 1024 = bold("33.554.432 KB")$ *(0,25đ)*.
    - *Ý b (0,50 điểm):*
      - Tổng dung lượng $5$ đoạn video chiếm chỗ là: $5 times 1,5 "GB" = 7,5 "GB"$. Dung lượng thẻ nhớ còn lại dành để lưu ảnh là: $32 - 7,5 = 24,5 "GB" = 24,5 times 1024 = bold("25.088 MB")$ *(0,25đ)*.
      - Số bức ảnh chất lượng cao lưu thêm được tối đa là: $25.088 : 8 = bold("3.136 (bức ảnh)")$ *(0,25đ)*.
  ]
)

#essay-qa(
  "02", "VD", "1,0 điểm • Chủ đề A.1",
  [Bạn Hùng cần gửi một tệp nén bài tập dự án dung lượng $450 "MB"$ lên kho lưu trữ đám mây của lớp. Đường truyền Internet tại nhà Hùng có tốc độ tải lên (*upload*) thực tế ổn định đạt $60 "Mbps"$ (*Megabit trên giây*).
  a) Hỏi Hùng cần chờ bao nhiêu giây để tải xong tệp dự án đó lên đám mây?
  b) Nếu cùng đường truyền đó tải liên tục trong đúng $2$ phút thì truyền được tối đa bao nhiêu $"GB"$ dữ liệu (làm tròn 2 chữ số thập phân)?],
  [
    - *Ý a (0,50 điểm):*
      - Ta có $1 "Byte (B)" = 8 "bit (b)" arrow.r.double 1 "MB" = 8 "Mb"$. Đổi dung lượng tệp sang Megabit: $450 "MB" = 450 times 8 = bold("3.600 Mb")$ *(0,25đ)*.
      - Thời gian cần thiết để tải xong tệp là: $t = 3.600 : 60 = bold("60 (giây)")$ (tức đúng $1$ phút) *(0,25đ)*.
    - *Ý b (0,50 điểm):*
      - Đổi thời gian $2 "phút" = 120 "giây"$. Tổng lượng dữ liệu truyền được tính theo Megabit là: $120 times 60 = 7.200 "Mb"$. Đổi sang Megabyte: $7.200 : 8 = bold("900 MB")$ *(0,25đ)*.
      - Đổi sang Gigabyte: $900 : 1024 approx bold("0,88 GB")$ *(0,25đ)*.
  ]
)

#essay-qa(
  "03", "VD", "1,0 điểm • Chủ đề A.1",
  [Giả sử trung bình mỗi trang sách giáo khoa thuần văn bản (không kèm hình ảnh) chứa khoảng $2.048$ kí tự và mỗi kí tự chiếm trung bình $2 "Byte"$ bộ nhớ (mã hóa Tiếng Việt Unicode). Hỏi một chiếc USB có dung lượng trống $4 "GB"$ có thể lưu trữ được văn bản tương đương khoảng bao nhiêu cuốn sách dày $256$ trang? Qua kết quả đó, em rút ra nhận xét gì về lưu trữ trên thiết bị số?],
  [
    - Dung lượng của $1$ trang sách là: $2.048 times 2 = 4.096 "Byte" = 4.096 : 1024 = bold("4 KB")$ *(0,25đ)*.
    - Dung lượng của $1$ cuốn sách dày $256$ trang là: $256 times 4 "KB" = 1.024 "KB" = bold("1 MB")$ *(0,25đ)*.
    - Đổi dung lượng trống của USB: $4 "GB" = 4 times 1024 = 4.096 "MB"$. Số cuốn sách lưu trữ được là: $4.096 : 1 = bold("4.096 (cuốn sách)")$ *(0,25đ)*.
    - *Nhận xét (0,25đ):* Chỉ một chiếc USB nhỏ gọn bỏ túi đã chứa được lượng tri thức tương đương cả một thư viện hơn bốn nghìn cuốn sách in, minh chứng rõ rệt tính ưu việt vượt trội về sức chứa, sự gọn nhẹ và tiện lợi của thiết bị lưu trữ số.
  ]
)

#essay-qa(
  "04", "TH", "1,0 điểm • Chủ đề B.2",
  [Em hãy phân biệt sự khác nhau cơ bản giữa ba loại phần mềm độc hại phổ biến: *Virus máy tính*, *Sâu máy tính (Worm)* và *Ngựa thành Troa (Trojan)*. Nêu ít nhất 4 biện pháp thiết thực để phòng tránh các loại phần mềm độc hại này trên máy tính cá nhân.],
  [
    - *Phân biệt 3 loại phần mềm độc hại (0,50 điểm):*
      1. *Virus máy tính:* Không phải chương trình độc lập, phải *gắn (ký sinh) vào tệp vật chủ* hợp pháp; chỉ kích hoạt và lây lan khi người dùng mở/chạy tệp vật chủ đó.
      2. *Sâu máy tính (Worm):* Là *chương trình độc lập hoàn chỉnh*, có khả năng *tự nhân bản và tự động lây lan qua mạng* (email, lỗ hổng mạng, USB) mà không cần tệp vật chủ.
      3. *Ngựa thành Troa (Trojan):* *Không tự nhân bản*, ngụy trang dưới vỏ bọc phần mềm hợp pháp/hữu ích (như game miễn phí, phần mềm *crack*) lừa người dùng tự cài đặt nhằm mở cửa hậu đánh cắp thông tin hoặc chiếm quyền điều khiển.
    - *4 biện pháp phòng tránh hiệu quả (0,50 điểm):*
      1. Cài đặt, bật bảo vệ thời gian thực và cập nhật thường xuyên phần mềm diệt virus uy tín (*Windows Security / Kaspersky / Bitdefender...*) cùng Tường lửa (*Firewall*).
      2. Thường xuyên cập nhật hệ điều hành và trình duyệt web để vá các lỗ hổng bảo mật.
      3. Tuyệt đối không tải và cài đặt phần mềm lậu, phần mềm bẻ khóa (*crack*); chỉ tải ứng dụng từ trang chủ chính thức.
      4. Không bấm vào đường link lạ, không mở tệp đính kèm không rõ nguồn gốc trong email/tin nhắn và quét USB trước khi mở.
  ]
)

#essay-qa(
  "05", "VD", "1,0 điểm • Chủ đề B.2",
  [Bạn H (học sinh lớp 10) phát hiện một tài khoản ẩn danh lập trang giả mạo trên mạng xã hội, đăng ảnh của H kèm những tin đồn bịa đặt ác ý và nhắn tin đe dọa khiến H rất hoang mang, lo sợ không dám đến trường. Nếu là bạn thân cùng lớp với H, em sẽ khuyên và cùng H xử lí tình huống này như thế nào?],
  [
    Em sẽ động viên H bình tĩnh (vì H là nạn nhân, không có lỗi) và cùng H thực hiện *quy trình 4 bước phòng vệ chuẩn*:
    - *Bước 1 – Không đáp trả tiêu cực (0,25đ):* Khuyên H tuyệt đối không nhắn tin chửi bới, đôi co lại với tài khoản ẩn danh và không làm theo các yêu sách đe dọa/tống tiền của kẻ xấu.
    - *Bước 2 – Thu thập & lưu giữ bằng chứng (0,25đ):* Cùng H chụp ảnh màn hình toàn bộ bài đăng bịa đặt, tin nhắn đe dọa, sao lưu đường dẫn (URL) trang giả mạo và mốc thời gian cụ thể.
    - *Bước 3 – Chặn, Báo cáo & Bảo mật tài khoản (0,25đ):* Sử dụng chức năng *Báo cáo vi phạm (Report)* mạo danh/quấy rối và *Chặn (Block)* tài khoản đó trên mạng xã hội; đồng thời chuyển tài khoản của H về chế độ riêng tư, kiểm tra lại mật khẩu.
    - *Bước 4 – Tìm kiếm sự trợ giúp từ người lớn & Cơ quan chức năng (0,25đ):* Khuyên H chia sẻ ngay sự việc (kèm bằng chứng đã lưu) với *bố mẹ và thầy/cô giáo chủ nhiệm, tổ tư vấn tâm lí nhà trường* để được bảo vệ kịp thời; nếu hành vi vu khống, đe dọa tiếp diễn nghiêm trọng thì gia đình trình báo *cơ quan Công an* xử lí theo Luật An ninh mạng.
  ]
)

#essay-qa(
  "06", "VD", "1,0 điểm • Chủ đề B.2",
  [Nhóm của em được giao làm chuyên đề tìm hiểu về *"Năng lượng tái tạo trên thế giới"*. Em hãy trình bày cách vận dụng hiệu quả: (a) Nguồn học liệu mở trên Internet, (b) Công cụ dịch tự động trên PC/thiết bị số và (c) Biện pháp bảo vệ dữ liệu bài làm của nhóm không bị mất mát.],
  [
    - *a) Khai thác nguồn học liệu mở (0,35đ):* Truy cập các kho học liệu mở uy tín trong nước và quốc tế như `igiaoduc.vn` (Hệ tri thức Việt số hoá), `hanhtrangso.nxbgd.vn`, `Khan Academy`, `MIT OpenCourseWare` hoặc các báo cáo khoa học mở để tìm số liệu, sơ đồ, video mô phỏng chính xác và miễn phí hợp pháp (luôn ghi chú lại nguồn tham khảo).
    - *b) Sử dụng chức năng dịch tự động (0,35đ):* Với các bài báo/tài liệu Tiếng Anh, sử dụng *Google Dịch (`translate.google.com`)* trên máy tính (dán đoạn văn hoặc tải tệp `.pdf`/`.docx` vào mục *Tài liệu*) hoặc tính năng dịch qua camera trên điện thoại để nắm nhanh nội dung, sau đó cả nhóm hiệu đính lại câu chữ và thuật ngữ Vật lí/Tin học cho chuẩn xác.
    - *c) Tự bảo vệ dữ liệu của nhóm (0,30đ):* Lưu trữ và cộng tác bài làm trên dịch vụ đám mây (*Google Drive / OneDrive*) có phân quyền chỉ thành viên nhóm mới được chỉnh sửa, đặt mật khẩu mạnh kèm xác thực 2 lớp cho tài khoản trưởng nhóm và sao lưu thêm 1 bản dự phòng ra máy tính cá nhân/USB đã quét sạch virus.
  ]
)

#essay-qa(
  "07", "VDC", "1,0 điểm • Chủ đề D.1",
  [*Tình huống pháp lí 1:* Anh T thấy một bộ sách ôn thi đại học mới xuất bản rất hay nên mua 1 bộ sách giấy về nhà, dùng máy quét (*scan*) thành tệp `.pdf` rồi đăng bài rao bán bản PDF giá rẻ (20.000đ/bản) trong các hội nhóm học sinh trên mạng xã hội. Bạn M mua 1 bản PDF từ anh T rồi tiếp tục đăng công khai lên diễn đàn trường cho mọi người tải miễn phí để "giúp đỡ bạn bè". Vận dụng kiến thức pháp luật trong môi trường số, em hãy nhận xét tính hợp pháp của hành vi anh T và bạn M, nêu hậu quả và đề xuất cách ứng xử đúng.],
  [
    - *1. Xác định tính hợp pháp (0,25đ):* *Cả hành vi của anh T lẫn hành vi của bạn M đều là hành vi BẤT HỢP PHÁP* (vi phạm pháp luật về bản quyền trong môi trường số), dù M chia sẻ không thu tiền.
    - *2. Giải thích căn cứ pháp lí (0,25đ):*
      - Theo *Luật Sở hữu trí tuệ* và *Điều 12 Luật Công nghệ thông tin 2006*, quyền sao chép, phân phối và truyền đạt tác phẩm tới công chúng thuộc độc quyền của tác giả / chủ sở hữu quyền tác giả (nhà xuất bản).
      - Anh T mua 1 bộ sách giấy chỉ có quyền sở hữu đối với cuốn sách vật lí đó để đọc, *không có quyền số hóa, nhân bản và kinh doanh thương mại trái phép*. Bạn M mua bản sao lậu và tiếp tục phát tán công khai cho hàng trăm người tải cũng trực tiếp xâm phạm quyền phân phối tác phẩm của chủ sở hữu bản quyền.
    - *3. Hậu quả pháp lí & xã hội (0,25đ):* Gây thất thoát kinh tế nghiêm trọng cho tác giả và nhà xuất bản; anh T (thu lợi bất chính từ hành vi sao chép lậu) và bạn M có thể bị buộc gỡ bỏ tệp vi phạm, *xử phạt vi phạm hành chính*, buộc *bồi thường thiệt hại dân sự*, thậm chí anh T có thể bị xem xét *trách nhiệm hình sự* nếu quy mô thu lợi bất chính lớn.
    - *4. Cách ứng xử đúng đắn (0,25đ):* Học sinh cần mua sách giấy chính hãng hoặc mua sách điện tử trên nền tảng phát hành bản quyền chính thức (như `hanhtrangso.nxbgd.vn`), hoặc mượn sách tại thư viện trường và khai thác các *nguồn học liệu mở miễn phí hợp pháp*; tuyệt đối không mua bán, tiếp tay phát tán sách lậu PDF.
  ]
)

#essay-qa(
  "08", "VDC", "1,0 điểm • Chủ đề D.1",
  [*Tình huống pháp lí 2:* Nghe tin đồn chưa kiểm chứng ở cổng chợ rằng *"Một cơ sở sản xuất bánh mì Y dùng hóa chất độc hại khiến nhiều người nhập viện"*, chị K vội vàng viết bài khẳng định như thật kèm hình ảnh biển hiệu cơ sở Y đăng lên Facebook cá nhân ở chế độ công khai để thu hút khách vào xem trang bán mỹ phẩm của chị. Chỉ sau 2 giờ đã có hàng nghìn lượt chia sẻ khiến cơ sở Y bị khách hàng tẩy chay dù kết quả kiểm tra của cơ quan y tế xác nhận cơ sở Y hoàn toàn đạt chuẩn an toàn thực phẩm. Hãy vận dụng Luật và Nghị định đã học để đánh giá hành vi của chị K.],
  [
    - *1. Kết luận tính pháp lí (0,25đ):* Hành vi của chị K là *VI PHẠM PHÁP LUẬT NGHIÊM TRỌNG* và trái với đạo đức, quy tắc ứng xử trên mạng xã hội.
    - *2. Căn cứ pháp luật cụ thể (0,25đ):* Chị K đã lợi dụng mạng xã hội đăng tải, lan truyền thông tin sai sự thật, chưa kiểm chứng làm ảnh hưởng uy tín của tổ chức/cá nhân và gây hoang mang dư luận, vi phạm trực tiếp:
      - *Điều 12 Luật Công nghệ thông tin 2006* (cấm xuyên tạc, vu khống, xúc phạm uy tín tổ chức, danh dự công dân);
      - *Điều 8 và Điều 16 Luật An ninh mạng 2018* (cấm thông tin sai sự thật gây hoang mang trong Nhân dân, gây thiệt hại cho hoạt động kinh tế – xã hội);
      - *Điều 5 Nghị định 72/2013/NĐ-CP* và thuộc diện bị xử phạt theo *Điều 101 Nghị định 15/2020/NĐ-CP* (sửa đổi bởi NĐ 14/2022/NĐ-CP).
    - *3. Hậu quả đối với các bên (0,25đ):* Cơ sở Y bị thiệt hại nặng nề về doanh thu và uy tín thương hiệu; xã hội bị nhiễu loạn thông tin. Về phía chị K, chị sẽ bị cơ quan chức năng *xử phạt vi phạm hành chính* (mức phạt đối với cá nhân từ 5 – 10 triệu đồng), buộc gỡ bỏ bài viết, đăng bài cải chính xin lỗi công khai và phải *bồi thường thiệt hại dân sự* cho cơ sở Y (nếu thiệt hại đặc biệt nghiêm trọng có thể bị xử lí hình sự về tội vu khống / đưa trái phép thông tin mạng).
    - *4. Bài học ứng xử hợp pháp (0,25đ):* Khi gặp thông tin liên quan đến an toàn thực phẩm/dịch bệnh chưa rõ thực hư, tuyệt đối không tự ý đăng tải hay chia sẻ câu "view"; chỉ tin và chia sẻ kết luận chính thức từ cơ quan chức năng, báo chí chính thống.
  ]
)

#essay-qa(
  "09", "VDC", "1,0 điểm • Chủ đề D.1",
  [*Tình huống pháp lí 3:* Trong quá trình viết bài thu hoạch môn Ngữ văn đăng lên trang thông tin điện tử của trường, bạn Lan thực hiện hai việc: (1) Trích nguyên văn một đoạn nhận định dài 4 dòng của nhà phê bình văn học Hoài Thanh trong cuốn *"Thi nhân Việt Nam"*, đặt trong dấu ngoặc kép và ghi chú rõ tên tác giả, tên sách, nhà xuất bản; (2) Tải một phần mềm chỉnh sửa ảnh trả phí nhưng dùng công cụ *crack* (bẻ khóa bản quyền) trên mạng để thiết kế ảnh bìa cho bài viết. Hãy xác định tính hợp pháp của từng việc làm (1) và (2) của bạn Lan và giải thích rõ lí do.],
  [
    - *Đánh giá việc làm (1) – Trích dẫn 4 dòng văn học có ghi nguồn: HỢP PHÁP (0,40 điểm):*
      - Theo *Luật Sở hữu trí tuệ* về các trường hợp ngoại lệ không xâm phạm quyền tác giả, việc Lan trích dẫn hợp lí một phần nhỏ tác phẩm đã công bố để bình luận, minh họa trong bài viết học tập của mình (phi thương mại), không làm sai lệch ý tác giả và *đã đặt trong ngoặc kép, ghi rõ tên tác giả cùng nguồn gốc tác phẩm* là hoàn toàn đúng pháp luật và chuẩn mực đạo đức học thuật.
    - *Đánh giá việc làm (2) – Dùng phần mềm chỉnh sửa ảnh bẻ khóa (crack): BẤT HỢP PHÁP (0,40 điểm):*
      - Chương trình máy tính (phần mềm) là đối tượng được bảo hộ quyền tác giả theo *Luật Sở hữu trí tuệ* và *Điều 12 Luật Công nghệ thông tin 2006*. Hành vi dùng công cụ *crack* để vô hiệu hóa biện pháp kĩ thuật bảo vệ bản quyền nhằm sử dụng phần mềm thương mại mà không trả phí cấp phép là *vi phạm pháp luật về sở hữu trí tuệ*, đồng thời tiềm ẩn nguy cơ cao khiến máy tính của Lan bị nhiễm *Trojan/Spyware* gài sẵn trong bộ *crack*.
    - *Giải pháp khắc phục hợp pháp cho Lan (0,20 điểm):* Lan nên gỡ bỏ ngay phần mềm *crack* và thay thế bằng các công cụ thiết kế miễn phí hợp pháp hoặc mã nguồn mở (như *GIMP*, *Inkscape*, *Paint.NET*, hoặc bản miễn phí của *Canva*) để vừa tuân thủ pháp luật vừa an toàn cho máy tính.
  ]
)
