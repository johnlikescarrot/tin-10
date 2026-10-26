# PHẦN 2. CHỦ ĐỀ B – MẠNG MÁY TÍNH VÀ INTERNET|Nơi đề lấy nhiều câu hỏi nhận biết và một câu tự luận thông hiểu
lead|Chủ đề B gồm hai đơn vị kiến thức: (1) Khái niệm mạng máy tính, Internet, IoT và phân loại mạng máy tính; (2) Sử dụng dịch vụ web, tự bảo vệ khi tham gia mạng. Đây là chủ đề có **câu tự luận thông hiểu 1,0 điểm** trong ma trận, thường hỏi về cách phòng tránh tác hại khi tham gia Internet hoặc so sánh LAN với Internet.

## 2.1. Mạng máy tính, Internet, IoT và phân loại mạng

### 2.1.1. Khái niệm mạng máy tính
- **Mạng máy tính** là tập hợp các máy tính (và thiết bị số) được kết nối với nhau bằng đường truyền, cho phép chúng **trao đổi dữ liệu và chia sẻ tài nguyên** (máy in, ổ đĩa, phần mềm, kết nối Internet).
- Mục đích của mạng: chia sẻ tài nguyên, trao đổi thông tin nhanh, dùng chung dữ liệu, cộng tác và làm việc nhóm, tiết kiệm chi phí.
tbl|22,78|Bảng 2.1 – Bốn thành phần cơ bản của một mạng máy tính
th|Thành phần||Vai trò và ví dụ
tr|Thiết bị đầu cuối||Máy tính, điện thoại, máy in mạng, camera IP – nơi tạo ra và sử dụng dữ liệu
tr|Thiết bị kết nối||Switch (bộ chuyển mạch), router (bộ định tuyến), modem, access point (điểm truy cập không dây) – nối các thiết bị lại
tr|Đường truyền||Cáp mạng (cáp xoắn, cáp quang), sóng Wi-Fi, sóng di động, vệ tinh – môi trường truyền tín hiệu
tr|Giao thức truyền thông||Bộ quy tắc chung để các thiết bị “hiểu” nhau: TCP/IP, HTTP, Wi-Fi (IEEE 802.11), Bluetooth
endtbl
box|**Ghi nhớ:** *Có thiết bị, có đường truyền, có giao thức → mới thành mạng.* Thiếu giao thức, các thiết bị chỉ là một tập hợp các máy đứng cạnh nhau nhưng “nói tiếng khác nhau”.

### 2.1.2. Phân loại mạng máy tính
tbl|20,26,54|Bảng 2.2 – Phân loại theo phạm vi địa lí
th|Loại mạng||Phạm vi||Đặc điểm, ví dụ
tr|PAN||Vài mét, quanh một người||Kết nối tai nghe Bluetooth, chia sẻ dữ liệu điện thoại – laptop
tr|LAN||Một phòng, một toà nhà, một trường học, một cơ quan||Tốc độ cao, độ trễ thấp, do một tổ chức quản lí; mạng máy tính trong phòng tin học
tr|MAN||Một thành phố, một khu vực đô thị||Nối nhiều LAN trong cùng thành phố, thường do nhà cung cấp dịch vụ vận hành
tr|WAN||Quốc gia, châu lục, toàn cầu||Phạm vi rộng nhất; **Internet là WAN lớn nhất thế giới**
endtbl
Ngoài cách phân loại theo phạm vi, còn có:
- **Theo cách kết nối:** mạng **có dây** (cáp xoắn, cáp quang) và mạng **không dây** (Wi-Fi, Bluetooth, 4G/5G).
- **Theo kiến trúc (mô hình hoạt động):** mô hình **khách – chủ (client – server)** – có máy chủ cung cấp dịch vụ và các máy khách sử dụng dịch vụ; mô hình **ngang hàng (peer-to-peer)** – các máy bình đẳng, vừa cung cấp vừa sử dụng tài nguyên.

### 2.1.3. Internet và vai trò của Internet
- **Internet** là mạng của các mạng máy tính, liên kết hàng tỉ thiết bị trên toàn cầu, sử dụng chung **bộ giao thức TCP/IP**; không thuộc sở hữu của riêng cá nhân hay tổ chức nào.
- Truy cập Internet thông qua **nhà cung cấp dịch vụ (ISP)** như Viettel, VNPT, FPT.
tbl|24,38,38|Bảng 2.3 – So sánh mạng LAN và Internet (dạng câu hỏi “so sánh” rất dễ gặp)
th|Tiêu chí||Mạng LAN||Internet
tr|Phạm vi||Nhỏ (một phòng, một toà nhà)||Toàn cầu
tr|Quyền sở hữu, quản lí||Một tổ chức/cá nhân quản lí||Không cá nhân/tổ chức nào sở hữu; phối hợp toàn cầu
tr|Tốc độ, độ trễ||Thường nhanh hơn, độ trễ thấp, ổn định||Phụ thuộc nhà cung cấp, có thể trễ và không ổn định
tr|Chi phí||Chi phí lắp đặt ban đầu, không mất phí hàng tháng (nếu chỉ nội bộ)||Thường phải trả phí thuê bao hàng tháng
tr|Giao thức||Có thể dùng TCP/IP hoặc giao thức riêng||Bắt buộc dùng TCP/IP
tr|Phạm vi dịch vụ||Chia sẻ tệp, máy in trong nội bộ||Web, email, học trực tuyến, mạng xã hội, đám mây…
endtbl
h3|Internet đã thay đổi chất lượng cuộc sống, học tập và làm việc như thế nào?
+ **Học tập:** học trực tuyến, học liệu mở, trao đổi với giáo viên qua mạng, học sinh vùng sâu vùng xa tiếp cận tri thức; đồng thời xuất hiện nguy cơ xao nhãng, phụ thuộc màn hình.
+ **Làm việc:** làm việc từ xa, họp trực tuyến, cộng tác trên cùng một tài liệu, dịch vụ công trực tuyến, tìm việc qua mạng; xuất hiện các nghề mới (kĩ sư dữ liệu, chuyên viên an ninh mạng, sáng tạo nội dung số).
+ **Cuộc sống:** mua sắm trực tuyến, thanh toán số, đặt lịch khám, giải trí theo yêu cầu, giữ liên lạc với người thân ở xa; nhưng cũng kéo theo tin giả, lừa đảo trực tuyến và các vấn đề về sức khoẻ tinh thần.
box|**Cách trả lời “trình bày những thay đổi”: ** chia theo **ba lĩnh vực** (học tập – làm việc – đời sống), mỗi lĩnh vực nêu 2 thay đổi tích cực. Nếu câu hỏi yêu cầu “và hạn chế”, thêm 1 – 2 ý về mặt trái. Không kể lan man, không dùng ví dụ quá dài.

### 2.1.4. Điện toán đám mây và các dịch vụ cụ thể
- **Điện toán đám mây (cloud computing)** là mô hình cung cấp **tài nguyên tính toán** (lưu trữ, máy chủ, phần mềm, nền tảng phát triển) **qua Internet**, người dùng không cần sở hữu hạ tầng vật lí mà trả phí theo mức sử dụng.
tbl|13,26,61|Bảng 2.4 – Ba mức dịch vụ điện toán đám mây
th|Mức||Tên đầy đủ||Người dùng nhận được gì – ví dụ
tr|IaaS||Hạ tầng như một dịch vụ||Thuê máy chủ, ổ đĩa, mạng ảo; ví dụ Amazon EC2, Google Compute Engine
tr|PaaS||Nền tảng như một dịch vụ||Môi trường lập trình, cơ sở dữ liệu sẵn có; ví dụ Google App Engine, Heroku
tr|SaaS||Phần mềm như một dịch vụ||Dùng phần mềm qua trình duyệt; ví dụ Gmail, Google Docs, Office 365
endtbl
h3|Các dịch vụ cụ thể mà điện toán đám mây cung cấp cho người dùng
+ **Lưu trữ trực tuyến (lưu trữ tệp):** Google Drive, OneDrive, iCloud, Dropbox – lưu ảnh, tài liệu, sao lưu và truy cập từ nhiều thiết bị.
+ **Bộ ứng dụng văn phòng trực tuyến:** Google Docs/Sheets/Slides, Office 365 – soạn thảo và cộng tác thời gian thực.
+ **Thư điện tử:** Gmail, Outlook – hộp thư trên nền web, không cần máy chủ riêng.
+ **Đồng bộ và sao lưu:** tự động sao lưu ảnh, danh bạ, ghi chú.
+ **Máy chủ và nền tảng cho lập trình viên:** thuê máy chủ ảo, dịch vụ cơ sở dữ liệu, chạy ứng dụng.
+ **Dịch vụ trí tuệ nhân tạo trực tuyến:** nhận dạng giọng nói, dịch tự động, phân tích ảnh.
tbl|34,33,33|Bảng 2.5 – Ưu điểm và hạn chế của điện toán đám mây
th|Ưu điểm||Hạn chế||Cách khắc phục
tr|Không phải đầu tư hạ tầng, chi phí theo nhu cầu||Phụ thuộc chất lượng Internet||Dự phòng đường truyền, lưu bản cục bộ
tr|Truy cập mọi lúc, mọi nơi, nhiều thiết bị||Lo ngại dữ liệu bị lộ, bị truy cập trái phép||Dùng mật khẩu mạnh, xác thực hai bước, mã hoá
tr|Dễ mở rộng dung lượng, dễ sao lưu||Dữ liệu đặt ở nước ngoài, phụ thuộc nhà cung cấp||Chọn nhà cung cấp uy tín, đọc điều khoản
tr|Nhiều người cộng tác trên cùng dữ liệu||Không có Internet thì gần như không dùng được||Sao lưu định kì, dùng chế độ ngoại tuyến
endtbl

### 2.1.5. Internet vạn vật (IoT)
- **IoT (Internet of Things – Internet vạn vật)** là mạng kết nối **các thiết bị, phương tiện, đồ vật** có gắn cảm biến và khả năng truyền dữ liệu, cho phép chúng **tự động thu thập, trao đổi dữ liệu và phối hợp hoạt động** mà không cần con người can thiệp trực tiếp.
tbl|22,78|Bảng 2.6 – Bốn thành phần của một hệ thống IoT
th|Thành phần||Vai trò, ví dụ
tr|Thiết bị cảm biến, cơ cấu chấp hành||Thu thập dữ liệu (nhiệt độ, độ ẩm, ánh sáng) và thực hiện lệnh (bật/tắt thiết bị)
tr|Kết nối mạng||Wi-Fi, Bluetooth, 4G/5G, Zigbee – đưa dữ liệu lên hệ thống
tr|Xử lí, lưu trữ (thường trên đám mây)||Phân tích dữ liệu, ra quyết định, huấn luyện mô hình
tr|Ứng dụng cho người dùng||Ứng dụng điện thoại xem camera, điều khiển đèn, nhận cảnh báo
endtbl
h3|Ví dụ cụ thể về những thay đổi mà IoT đem lại
+ **Nhà thông minh:** đèn tự bật khi trời tối, điều hoà tự điều chỉnh theo nhiệt độ, camera gửi cảnh báo khi có người lạ.
+ **Nông nghiệp thông minh:** cảm biến độ ẩm đất điều khiển tưới tiêu tự động, giúp tiết kiệm nước và tăng năng suất.
+ **Y tế:** vòng đeo tay theo dõi nhịp tim, thiết bị nhắc uống thuốc, cảnh báo té ngã cho người cao tuổi.
+ **Giao thông:** xe tự lái, hệ thống đèn giao thông thích ứng, theo dõi lộ trình xe buýt theo thời gian thực.
+ **Môi trường, đô thị:** trạm quan trắc không khí, quản lí rác thông minh, chiếu sáng công cộng tiết kiệm điện.
box|**Ý kiến cá nhân về lợi ích của IoT (câu hỏi mở, cần lập luận):** IoT giúp cuộc sống tiện lợi, tiết kiệm thời gian và năng lượng, nâng cao an toàn và chất lượng dịch vụ y tế, hỗ trợ ra quyết định dựa trên dữ liệu thực. Tuy nhiên, IoT cũng đặt ra vấn đề **quyền riêng tư** (thiết bị ghi lại thói quen sinh hoạt), **an ninh** (thiết bị yếu bảo mật có thể bị chiếm quyền) và **rác điện tử**. Vì vậy, cần sử dụng thiết bị từ nhà sản xuất uy tín, đổi mật khẩu mặc định, cập nhật phần mềm và chỉ bật thiết bị khi cần.

## 2.2. Sử dụng dịch vụ web và tự bảo vệ khi tham gia mạng

### 2.2.1. Phần mềm độc hại
- **Phần mềm độc hại (malware)** là phần mềm được tạo ra nhằm **gây hại** cho máy tính, thiết bị, dữ liệu hoặc người dùng: phá hoại hệ thống, đánh cắp thông tin, theo dõi, tống tiền, chiếm quyền điều khiển.
tbl|16,32,52|Bảng 2.7 – Các loại phần mềm độc hại thường gặp
th|Loại||Cách hoạt động||Dấu hiệu, ví dụ
tr|Virus||Gắn vào tệp/chương trình, lây lan khi tệp được chạy||Máy chậm, tệp bị hỏng, xuất hiện tệp lạ
tr|Worm (sâu máy tính)||Tự nhân bản và lây lan qua mạng không cần người dùng mở tệp||Mạng chậm bất thường, lưu lượng tăng vọt
tr|Trojan||Giả dạng phần mềm hữu ích để mở “cửa sau” cho kẻ tấn công||Cài ứng dụng “miễn phí” rồi bị chiếm tài khoản
tr|Ransomware||Mã hoá dữ liệu và đòi tiền chuộc||Không mở được tệp, có thông báo đòi tiền
tr|Spyware||Theo dõi, ghi lại thao tác, ăn cắp thông tin đăng nhập||Tự bật camera, bàn phím lạ, quảng cáo bám theo
tr|Adware||Tự động hiện quảng cáo, chuyển hướng trình duyệt||Trình duyệt đổi trang chủ, mở tab lạ
tr|Botnet||Biến máy tính thành “zombie” trong mạng lưới tấn công||Máy tự gửi thư rác, tham gia tấn công từ chối dịch vụ
endtbl
h3|Con đường lây nhiễm và cách phòng
- **Đường lây:** mở tệp đính kèm lạ, tải phần mềm “bẻ khoá”/“miễn phí”, bấm vào liên kết giả mạo, cắm USB không rõ nguồn, dùng Wi-Fi công cộng không an toàn, không cập nhật hệ điều hành.
- **Phòng:** cài và cập nhật phần mềm diệt virus; bật tường lửa; chỉ tải từ kho ứng dụng chính thức; không mở tệp lạ; cập nhật hệ điều hành; sao lưu dữ liệu; kiểm tra kĩ địa chỉ web trước khi đăng nhập.
warn|**Không nên** trả tiền chuộc khi bị ransomware: không đảm bảo lấy lại được dữ liệu và khuyến khích tội phạm. Việc cần làm: ngắt kết nối mạng, giữ nguyên hiện trường, nhờ chuyên gia/báo cơ quan chức năng, khôi phục từ bản sao lưu.

### 2.2.2. Bắt nạt trên mạng (cyberbullying)
- **Bắt nạt trên mạng** là hành vi **cố ý gây tổn thương** người khác thông qua các phương tiện điện tử: nhắn tin xúc phạm, tung tin đồn, bình luận miệt thị, chia sẻ ảnh riêng tư, lập nhóm để cô lập, mạo danh người khác.
- **Hậu quả:** nạn nhân lo âu, trầm cảm, sợ đến trường, giảm kết quả học tập, thậm chí nghĩ đến hành vi tiêu cực; tổn thương lan nhanh và tồn tại lâu trên mạng.
tbl|22,78|Bảng 2.8 – Cách phòng vệ khi bị bắt nạt trên mạng
th|Bước||Việc cần làm
tr|1. Không đáp trả||Không tranh cãi, không trả đũa – điều đó làm sự việc nặng thêm
tr|2. Lưu bằng chứng||Chụp màn hình tin nhắn, bài viết, ghi lại thời gian để làm căn cứ
tr|3. Chặn và báo cáo||Dùng chức năng Block/Report của ứng dụng, mạng xã hội
tr|4. Chia sẻ với người lớn tin cậy||Nói với bố mẹ, thầy cô, nhà tư vấn học đường – không giữ một mình
tr|5. Điều chỉnh quyền riêng tư||Chuyển tài khoản sang chế độ riêng tư, hạn chế chia sẻ thông tin cá nhân
tr|6. Tìm hỗ trợ pháp lí khi cần||Hành vi xúc phạm, đe doạ có thể bị xử lí theo pháp luật
endtbl
box|**Nguyên tắc ứng xử:** không ai có quyền xúc phạm người khác, kể cả trên mạng. Nếu em là **người chứng kiến**, hãy lên tiếng bênh vực nạn nhân hoặc báo cho người lớn – im lặng cũng là tiếp tay.

### 2.2.3. Những nguy cơ và tác hại khi tham gia Internet một cách bất cẩn
tbl|22,44,34|Bảng 2.9 – Nguy cơ và tác hại tương ứng
th|Nguy cơ||Cách xảy ra||Tác hại
tr|Lộ thông tin cá nhân||Chia sẻ số điện thoại, địa chỉ, ảnh thẻ, CCCD lên mạng xã hội||Bị làm phiền, bị mạo danh, bị lừa đảo
tr|Lừa đảo trực tuyến||Giả nhân viên ngân hàng, “trúng thưởng”, việc làm online lương cao||Mất tiền, mất tài khoản
tr|Mất tài khoản||Dùng mật khẩu yếu, dùng chung mật khẩu, bấm link giả||Chiếm đoạt tài khoản, lợi dụng danh tính
tr|Nhiễm phần mềm độc hại||Tải phần mềm crack, mở tệp lạ||Mất dữ liệu, máy bị điều khiển từ xa
tr|Tin giả, thông tin sai lệch||Chia sẻ không kiểm chứng||Hiểu sai, gây hoang mang, ảnh hưởng người khác
tr|Nội dung không phù hợp||Vô tình truy cập trang xấu||Ảnh hưởng tâm lí, lệch lạc nhận thức
tr|Nghiện mạng, nghiện game||Dùng thiết bị quá nhiều giờ||Giảm học tập, rối loạn giấc ngủ, xa rời gia đình
tr|Bị bắt nạt, quấy rối||Bình luận, tin nhắn độc hại||Tổn thương tinh thần, sợ hãi
endtbl

### 2.2.4. Các cách đề phòng tác hại khi tham gia Internet
+ **Bảo mật tài khoản:** mật khẩu mạnh (≥ 8 kí tự, có chữ hoa, số, kí hiệu), không dùng lại mật khẩu, bật **xác thực hai bước**, đăng xuất trên máy lạ.
+ **Hạn chế chia sẻ thông tin cá nhân:** không công khai số điện thoại, địa chỉ nhà, lịch đi học, ảnh giấy tờ; kiểm tra cài đặt quyền riêng tư.
+ **Kiểm chứng thông tin:** với tin gây sốc, hãy tìm nguồn chính thống; không chia sẻ tin chưa kiểm chứng.
+ **Cẩn thận với liên kết và tệp lạ:** kiểm tra tên miền, không bấm link rút gọn đáng ngờ, không mở tệp đính kèm từ người lạ.
+ **Sử dụng công cụ bảo vệ:** phần mềm diệt virus, tường lửa, cập nhật phần mềm, sao lưu định kì.
+ **Quản lí thời gian:** đặt giới hạn thời gian dùng, tắt thông báo không cần thiết, ưu tiên việc học.
+ **Nhờ trợ giúp khi gặp sự cố:** báo ngay cho người lớn, thầy cô; với mất tiền, hãy liên hệ ngân hàng và cơ quan công an.
tip|Nhớ 4 chữ **“DỪNG – NGHĨ – KIỂM TRA – HỎI”** trước khi bấm vào bất cứ liên kết nào: Dừng lại; nghĩ xem có hợp lí không; kiểm tra địa chỉ, người gửi; hỏi người lớn nếu không chắc.

### 2.2.5. Công cụ ngăn ngừa và loại bỏ phần mềm độc hại
- **Phần mềm diệt virus (antivirus):** Windows Defender (có sẵn trên Windows), các phần mềm bảo mật khác. Chức năng: quét nhanh, quét toàn bộ, quét theo lịch, cách li (quarantine), xoá mã độc, cập nhật cơ sở dữ liệu nhận diện.
- **Tường lửa (firewall):** kiểm soát luồng dữ liệu vào/ra, chặn kết nối trái phép.
- **Cập nhật phần mềm và hệ điều hành:** vá lỗ hổng bảo mật – đây là biện pháp hiệu quả nhất nhưng hay bị bỏ qua.
- **Quy trình khi nghi nhiễm mã độc:** ngắt kết nối mạng → khởi động chế độ an toàn → quét toàn bộ bằng phần mềm diệt virus → cách li/xoá tệp nhiễm → đổi toàn bộ mật khẩu → khôi phục dữ liệu từ bản sao lưu → nếu nặng thì cài lại hệ điều hành.

### 2.2.6. Khai thác học liệu mở và sử dụng chức năng xử lí thông tin
- **Học liệu mở (Open Educational Resources – OER)** là tài liệu học tập được công bố công khai, cho phép sử dụng, chia sẻ, có thể chỉnh sửa theo giấy phép mở: sách giáo khoa điện tử, bài giảng video, khoá học trực tuyến (Coursera, edX, VietED, thư viện số của trường đại học).
- **Cách khai thác hiệu quả:** xác định mục tiêu học tập → chọn nguồn uy tín (trường đại học, tổ chức giáo dục, thư viện số) → ghi chép, đối chiếu nhiều nguồn → **trích dẫn nguồn** khi sử dụng → kiểm tra giấy phép trước khi đăng lại.
- **Chức năng xử lí thông tin hữu ích trên thiết bị số:** chuyển văn bản thành tiếng nói (text-to-speech), chuyển tiếng nói thành văn bản (speech-to-text), **dịch tự động** văn bản và giọng nói, nhận dạng chữ trong ảnh (OCR), tìm kiếm bằng hình ảnh, tóm tắt văn bản.
- **Lưu ý khi dùng dịch tự động:** bản dịch máy có thể sai thuật ngữ chuyên ngành, sai sắc thái; cần đọc lại và đối chiếu khi dùng cho bài học, tuyệt đối không dùng để dịch bài kiểm tra (vi phạm quy chế).
- **Tự bảo vệ dữ liệu cá nhân:** phân loại dữ liệu (công khai – nội bộ – bí mật); đặt mật khẩu và mã hoá tệp quan trọng; sao lưu theo quy tắc 3-2-1 (3 bản sao, 2 phương tiện, 1 bản ngoài nơi làm việc); xoá dữ liệu đúng cách trước khi bán/cho thiết bị.

## 2.3. Hệ thống câu hỏi ôn tập Chủ đề B
h3|A. Trắc nghiệm 4 lựa chọn
resetq|
qs|Mạng máy tính là gì?
opt|A. Tập hợp các máy tính được kết nối để trao đổi dữ liệu và chia sẻ tài nguyên||B. Tập hợp các máy tính đặt trong cùng một phòng||C. Phần mềm dùng để duyệt web||D. Thiết bị dùng để kết nối Internet
answer|**A.** Định nghĩa nhấn mạnh hai mục đích: trao đổi dữ liệu và chia sẻ tài nguyên.
qs|Thiết bị nào sau đây là thiết bị kết nối trong mạng máy tính?
opt|A. Máy in||B. Bộ định tuyến (router)||C. Màn hình||D. Ổ cứng di động
answer|**B.** Router cùng switch, modem, access point là thiết bị kết nối.
qs|Mạng LAN thường có phạm vi:
opt|A. Toàn cầu||B. Một quốc gia||C. Một phòng, một toà nhà, một cơ quan||D. Một châu lục
answer|**C.** LAN – mạng cục bộ, phạm vi nhỏ, tốc độ cao.
qs|Internet là mạng có phạm vi:
opt|A. Cục bộ||B. Toàn cầu||C. Một thành phố||D. Một toà nhà
answer|**B.** Internet là WAN lớn nhất, phạm vi toàn cầu.
qs|Giao thức truyền thông chung mà Internet sử dụng là:
opt|A. HTTP||B. TCP/IP||C. FTP||D. SMTP
answer|**B.** TCP/IP là bộ giao thức nền tảng của Internet; HTTP, FTP, SMTP là giao thức ứng dụng chạy trên nền TCP/IP.
qs|Phát biểu nào sau đây **sai** khi so sánh LAN và Internet?
opt|A. LAN có phạm vi nhỏ hơn Internet||B. Internet không thuộc sở hữu của một tổ chức duy nhất||C. LAN luôn có tốc độ chậm hơn Internet||D. Internet yêu cầu dùng giao thức TCP/IP
answer|**C.** Sai: trong phạm vi nhỏ, LAN thường có tốc độ cao và độ trễ thấp hơn.
qs|Điện toán đám mây là gì?
opt|A. Việc lưu trữ dữ liệu trên ổ cứng của máy tính cá nhân||B. Mô hình cung cấp tài nguyên tính toán qua Internet, trả phí theo nhu cầu sử dụng||C. Một loại mạng máy tính cục bộ||D. Phần mềm diệt virus trực tuyến
answer|**B.** Người dùng không cần sở hữu hạ tầng vật lí mà thuê dịch vụ qua Internet.
qs|Dịch vụ nào sau đây là ví dụ của điện toán đám mây?
opt|A. Google Drive||B. Máy tính Casio||C. Ổ cứng gắn trong máy||D. Máy in để bàn
answer|**A.** Google Drive là dịch vụ lưu trữ trực tuyến (SaaS).
qs|Dịch vụ Gmail, Google Docs thuộc mức dịch vụ nào của điện toán đám mây?
opt|A. IaaS||B. PaaS||C. SaaS||D. DaaS
answer|**C.** SaaS – phần mềm như một dịch vụ: người dùng dùng phần mềm qua trình duyệt.
qs|IoT là viết tắt của:
opt|A. Internet of Things||B. Intranet of Technology||C. Information of Things||D. Internet of Telecom
answer|**A.** Internet vạn vật – mạng kết nối các đồ vật, thiết bị có cảm biến và khả năng truyền dữ liệu.
qs|Thiết bị nào sau đây **không** phải là ví dụ điển hình của IoT?
opt|A. Camera an ninh kết nối ứng dụng điện thoại||B. Đồng hồ thông minh đo nhịp tim||C. Quạt giấy cơ học||D. Cảm biến độ ẩm trong nông nghiệp thông minh
answer|**C.** Quạt giấy cơ học không có khả năng thu thập và truyền dữ liệu.
qs|Thành phần nào của hệ thống IoT trực tiếp thu thập dữ liệu từ môi trường?
opt|A. Ứng dụng người dùng||B. Cảm biến||C. Máy chủ đám mây||D. Router Wi-Fi
answer|**B.** Cảm biến là đầu vào của hệ thống IoT.
qs|Phần mềm độc hại là gì?
opt|A. Phần mềm mã nguồn mở miễn phí||B. Phần mềm gây hại cho máy tính, dữ liệu hoặc người dùng||C. Phần mềm hệ điều hành||D. Phần mềm diệt virus
answer|**B.** Định nghĩa bao trùm virus, worm, trojan, ransomware, spyware, adware…
qs|Loại phần mềm độc hại nào mã hoá dữ liệu và đòi tiền chuộc?
opt|A. Worm||B. Adware||C. Ransomware||D. Spyware
answer|**C.** Ransomware – mã độc tống tiền.
qs|Loại phần mềm độc hại nào tự nhân bản và lây lan qua mạng mà không cần người dùng mở tệp?
opt|A. Worm||B. Trojan||C. Adware||D. Rootkit
answer|**A.** Worm (sâu máy tính) tự lây lan, khai thác lỗ hổng mạng.
qs|Hành vi nào sau đây là bắt nạt trên mạng?
opt|A. Góp ý chân thành cho bạn trong nhóm học tập||B. Liên tục gửi tin nhắn miệt thị, chế giễu ngoại hình của bạn||C. Chia sẻ tài liệu học tập cho bạn||D. Nhắc bạn nộp bài đúng hạn
answer|**B.** Đó là hành vi cố ý gây tổn thương qua phương tiện điện tử.
qs|Khi bị bắt nạt trên mạng, việc làm đầu tiên nên là:
opt|A. Đáp trả lại bằng lời lẽ nặng hơn||B. Lưu bằng chứng, chặn và báo cáo, sau đó nhờ người lớn tin cậy||C. Xoá tài khoản và im lặng chịu đựng||D. Công khai thông tin cá nhân của người bắt nạt
answer|**B.** Vừa bảo vệ bản thân vừa có căn cứ để xử lí; đáp trả hay công khai thông tin người khác đều sai và có thể vi phạm pháp luật.
qs|Cách nào sau đây giúp bảo vệ tài khoản tốt nhất?
opt|A. Dùng một mật khẩu cho tất cả tài khoản||B. Đặt mật khẩu là ngày sinh cho dễ nhớ||C. Dùng mật khẩu mạnh, khác nhau cho từng tài khoản và bật xác thực hai bước||D. Chia sẻ mật khẩu cho bạn thân
answer|**C.** Mật khẩu mạnh – không dùng lại – kèm xác thực hai bước là bộ ba bảo mật cơ bản.
qs|Phần mềm nào sau đây giúp phát hiện và loại bỏ phần mềm độc hại?
opt|A. Phần mềm diệt virus||B. Phần mềm soạn thảo văn bản||C. Trình duyệt web||D. Phần mềm nén tệp
answer|**A.** Antivirus có chức năng quét, cách li và xoá mã độc.
qs|Học liệu mở (OER) là:
opt|A. Tài liệu mật của cơ quan nhà nước||B. Tài liệu học tập công bố công khai, được phép sử dụng và chia sẻ theo giấy phép mở||C. Phần mềm trả phí bắt buộc||D. Tài liệu chỉ dùng trong lớp học
answer|**B.** Đặc trưng của OER là công khai và có giấy phép cho phép tái sử dụng.
qs|Chức năng nào sau đây là ví dụ của việc “xử lí thông tin bằng thiết bị số”?
opt|A. Dịch tự động một đoạn văn bản sang tiếng Anh||B. Viết bài bằng bút mực||C. Đọc sách giấy||D. Vẽ hình bằng compa
answer|**A.** Dịch tự động là xử lí văn bản/tiếng nói bằng phần mềm.
h3|B. Trắc nghiệm đúng/sai
resetq|
ds|Mỗi phát biểu sau về mạng máy tính là đúng hay sai?
opt1|a) Thiếu giao thức truyền thông, các thiết bị không thể trao đổi dữ liệu với nhau.||b) Mạng LAN có phạm vi rộng hơn mạng WAN.||c) Internet là mạng WAN lớn nhất hiện nay.||d) Mạng máy tính chỉ dùng để gửi thư điện tử.
answer|a) **Đúng**. b) **Sai** – LAN nhỏ hơn WAN. c) **Đúng**. d) **Sai** – mạng còn dùng để chia sẻ tài nguyên, dữ liệu, máy in, dịch vụ web…
ds|Mỗi phát biểu sau về an toàn thông tin là đúng hay sai?
opt1|a) Đặt mật khẩu giống nhau cho mọi tài khoản là cách bảo mật tốt.||b) Không nên mở tệp đính kèm từ người gửi không quen biết.||c) Bật xác thực hai bước giúp giảm nguy cơ mất tài khoản.||d) Khi bị ransomware, nên trả tiền chuộc ngay để lấy lại dữ liệu.
answer|a) **Sai** – nếu lộ một tài khoản, tất cả đều bị chiếm. b) **Đúng**. c) **Đúng**. d) **Sai** – ngắt mạng, báo người có chuyên môn và khôi phục từ bản sao lưu.
h3|C. Tự luận
resetq|
tl|Trình bày một số cách đề phòng những tác hại khi tham gia các hoạt động trên Internet. (1,0 điểm)
sol|Cần nêu được 4 – 5 nhóm biện pháp, mỗi nhóm kèm một câu giải thích: (1) Bảo mật tài khoản: mật khẩu mạnh, không dùng lại, bật xác thực hai bước; (2) Hạn chế chia sẻ thông tin cá nhân, kiểm tra cài đặt quyền riêng tư; (3) Kiểm chứng thông tin trước khi tin và chia sẻ, không bấm liên kết lạ; (4) Cài phần mềm diệt virus, cập nhật hệ điều hành, sao lưu dữ liệu định kì; (5) Quản lí thời gian sử dụng, không chia sẻ thông tin ngân hàng, mã OTP; (6) Khi gặp sự cố phải báo ngay cho người lớn, thầy cô và cơ quan chức năng.
tl|So sánh mạng LAN và Internet trên các tiêu chí: phạm vi, quyền quản lí, tốc độ, giao thức. (1,0 điểm)
sol|**Phạm vi:** LAN trong một phòng/toà nhà; Internet phạm vi toàn cầu. **Quản lí:** LAN do một tổ chức/cá nhân quản lí; Internet không thuộc sở hữu của ai, được phối hợp vận hành toàn cầu. **Tốc độ:** LAN thường nhanh, độ trễ thấp, ổn định; Internet phụ thuộc nhà cung cấp, có thể trễ. **Giao thức:** LAN có thể dùng TCP/IP hoặc giao thức riêng; Internet bắt buộc dùng TCP/IP. (Có thể thêm: chi phí, phạm vi dịch vụ.)
tl|Nêu khái niệm IoT và ba ví dụ cụ thể về thay đổi trong cuộc sống mà IoT đem lại. Em có đồng ý rằng IoT cũng gây ra một số nguy cơ không? Vì sao? (1,0 điểm)
sol|**Khái niệm:** IoT là mạng kết nối các thiết bị, đồ vật có gắn cảm biến và khả năng truyền dữ liệu, cho phép chúng tự động thu thập, trao đổi dữ liệu và phối hợp hoạt động. **Ví dụ:** nhà thông minh tự điều chỉnh ánh sáng/điều hoà; cảm biến độ ẩm điều khiển tưới tiêu tự động; vòng đeo tay theo dõi nhịp tim và cảnh báo bất thường. **Nguy cơ:** có – thiết bị thu thập dữ liệu thói quen sinh hoạt nên đe doạ quyền riêng tư; nhiều thiết bị bảo mật yếu dễ bị chiếm quyền, bị lợi dụng để tấn công mạng; tăng lượng rác điện tử. Vì vậy cần chọn thiết bị uy tín, đổi mật khẩu mặc định, cập nhật phần mềm thường xuyên.
