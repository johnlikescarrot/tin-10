# PHẦN 3. CHỦ ĐỀ B – MẠNG MÁY TÍNH VÀ INTERNET (40% = 4,0 ĐIỂM)

## 3.1. Tổng quan: 2 đơn vị – 3 bài học – 3 từ khoá

<!-- COLS 21,29,19,31 -->
| Đơn vị (ma trận) | Bài SGK KNTT | Từ khoá | Trọng tâm câu hỏi |
| --- | --- | --- | --- |
| B1. Khái niệm mạng máy tính, Internet, IoT. Phân loại mạng máy tính | Bài 8. Mạng máy tính trong cuộc sống hiện đại | MẠNG | LAN/WAN/Internet; Hub–Switch–Router; điện toán đám mây SaaS/PaaS/IaaS; IoT |
| B2. Sử dụng dịch vụ web. Tự bảo vệ khi tham gia mạng | Bài 9. An toàn trên không gian mạng; Bài 10. Thực hành khai thác tài nguyên trên Internet | AN TOÀN + KHAI THÁC | Nguy cơ, malware, bắt nạt, phòng vệ; Google Dịch, học liệu mở, bản đồ số, bảo vệ dữ liệu cá nhân |

---

## 3.2. Đơn vị B1 – Mạng máy tính, Internet, IoT (Bài 8)

### 3.2.1. Mạng máy tính là gì? Phân loại thế nào?

**Mạng máy tính** là tập hợp các máy tính và thiết bị được kết nối với nhau qua đường truyền (cáp, sóng vô tuyến, cáp quang…) theo một giao thức chung, nhằm **trao đổi dữ liệu và dùng chung tài nguyên** (tệp, máy in, đường truyền Internet).

Hai nhóm thiết bị trong sơ đồ mạng:

- **Thiết bị đầu cuối:** máy tính để bàn, laptop, máy chủ (server), máy in, điện thoại, camera IP.
- **Thiết bị kết nối:** **Hub** (bộ chia – chuyển tiếp dữ liệu cho mọi cổng), **Switch** (bộ chuyển mạch – chuyển tiếp đúng cổng đích trong LAN), **Router** (bộ định tuyến – nối các LAN với nhau và nối LAN ra Internet), **Access Point/ Wi-Fi**, modem.

**Phân loại theo phạm vi địa lí** (cách phân loại hay hỏi nhất):

<!-- COLS 18,30,52 -->
| Loại mạng | Tên đầy đủ | Đặc điểm |
| --- | --- | --- |
| **LAN** | Local Area Network – mạng cục bộ | Phạm vi nhỏ: gia đình, phòng máy, trường học, công ty; thuộc sở hữu của một cá nhân/tổ chức xác định |
| **MAN** | Metropolitan Area Network – mạng đô thị (mở rộng) | Phạm vi một thành phố/khu vực đô thị |
| **WAN** | Wide Area Network – mạng diện rộng | Được tạo bằng cách liên kết nhiều LAN hoặc các máy tính đơn lẻ ở xa nhau; **Internet là một WAN có quy mô toàn cầu** |
| **PAN** | Personal Area Network (mở rộng) | Phạm vi cá nhân vài mét: Bluetooth giữa điện thoại và tai nghe, đồng hồ |

Ngoài ra có thể phân loại theo **quyền sở hữu** (mạng riêng/ mạng công cộng), theo **cấu trúc** (hình sao, hình vòng, hình bus…), theo **môi trường truyền** (có dây/ không dây).

### 3.2.2. So sánh mạng LAN và Internet (dạng TH chắc chắn có)

<!-- COLS 20,40,40 -->
| Tiêu chí | Mạng cục bộ (LAN) | Internet |
| --- | --- | --- |
| Phạm vi, quy mô | Nhỏ: gia đình, cơ quan, trường học | Toàn cầu |
| Cách kết nối | Kết nối trực tiếp trong mạng qua Hub, Switch, Wi-Fi | Kết nối qua **Router** thông qua các **nhà cung cấp dịch vụ Internet (ISP)** như VNPT, Viettel, FPT |
| Quyền sở hữu | Có chủ sở hữu rõ ràng (cá nhân/gia đình/cơ quan) | Không thuộc sở hữu của riêng ai; được điều phối kĩ thuật và chính sách bởi các tổ chức quốc tế, các tổ chức/cá nhân tự nguyện tham gia |
| Địa chỉ & định tuyến | Switch/Hub chỉ chuyển tiếp dữ liệu **trong nội bộ LAN** | Khi Router thấy địa chỉ nhận không nằm trong LAN, nó gửi dữ liệu qua **cổng INTERNET (WAN)** |
| Ví dụ | Mạng Wi-Fi của trường học, mạng nội bộ ngân hàng | Truy cập website, gửi email, học trực tuyến xuyên quốc gia |

> **Mẹo nhớ:** *"Switch nối trong, Router nối ngoài"*. Cổng LAN và cổng INTERNET trên Router được phân biệt chính để quyết định dữ liệu đi đâu.

### 3.2.3. Internet đã làm thay đổi cuộc sống, học tập, làm việc thế nào?

<!-- COLS 20,42,38 -->
| Lĩnh vực | Thay đổi tích cực | Mặt trái cần lưu ý |
| --- | --- | --- |
| Chất lượng cuộc sống | Giao tiếp không giới hạn khoảng cách; mua sắm, thanh toán, giải trí, y tế từ xa; thiết bị nhà thông minh | Tin giả, nghiện mạng, lộ thông tin, mua phải hàng giả |
| Học tập | Học liệu mở, bài giảng trực tuyến, lớp học ảo (Zoom, Google Meet), từ điển & dịch tự động, thư viện số | Gian lận khi học online, sao chép bài, khó kiểm chứng nguồn tài liệu |
| Làm việc | Làm việc từ xa, họp trực tuyến, cộng tác trên tài liệu đám mây, điện toán đám mây giảm chi phí hạ tầng | Rủi ro bảo mật dữ liệu doanh nghiệp, ranh giới công việc – nghỉ ngơi mờ nhạt |
| Kinh tế | Thương mại điện tử, khởi nghiệp công nghệ, kinh tế chia sẻ, việc làm mới (lập trình, phân tích dữ liệu) | Khoảng cách số giữa các vùng miền, tội phạm mạng |

Bài 8 còn nhấn mạnh: **Internet là kho tri thức chung khổng lồ**: có thể tìm thấy trên Internet hầu hết thông tin cần biết và nhiều dịch vụ thông tin sẵn có – nhưng phải biết chọn nguồn tin cậy.

### 3.2.4. Điện toán đám mây (Cloud Computing)

**Khái niệm:** Điện toán đám mây là việc **chia sẻ/ phân phối các tài nguyên công nghệ thông tin** (phần mềm, nền tảng, máy chủ, nơi lưu trữ…) **theo nhu cầu qua Internet**, miễn phí hoặc trả phí **theo mức sử dụng**. Người dùng đăng kí thuê bao, thoả thuận hạn mức và được cấp tài khoản truy cập; tài nguyên được hình dung như "đâu đó trên mây" nên không cần tự mua và quản lí toàn bộ thiết bị.

Ba loại dịch vụ cơ bản (học thuộc bảng này):

<!-- COLS 12,32,26,30 -->
| Loại | Viết tắt của | Thuê cái gì | Ví dụ |
| --- | --- | --- | --- |
| **SaaS** | Software as a Service | Phần mềm ứng dụng dùng cho công việc thông thường | Google Docs, Gmail, Zoom, Microsoft 365 |
| **PaaS** | Platform as a Service | Nền tảng/ công cụ để tạo ra sản phẩm khác, kể cả phần mềm ứng dụng | Nền tảng cơ sở dữ liệu đám mây, môi trường phát triển ứng dụng web, Google Maps API |
| **IaaS** | Infrastructure as a Service | Hạ tầng phần cứng: máy chủ, thiết bị lưu trữ, mạng | Google Drive, Dropbox, OneDrive, thuê máy chủ ảo (VPS) |

> **Mẹo nhớ:** *"SaaS dùng – PaaS dựng – IaaS giữ"*: SaaS dùng phần mềm có sẵn, PaaS dựng sản phẩm mới, IaaS giữ dữ liệu/máy chủ.

**Lợi ích:** giảm chi phí đầu tư ban đầu, dùng bao nhiêu trả bấy nhiêu, truy cập mọi nơi mọi thiết bị, dễ mở rộng, tự động sao lưu. **Rủi ro:** phụ thuộc vào đường truyền và nhà cung cấp, cần bảo mật tài khoản, cần đọc kĩ điều khoản về dữ liệu cá nhân.

### 3.2.5. Kết nối vạn vật (IoT)

**Khái niệm:** IoT (Internet of Things – Internet vạn vật/ kết nối vạn vật) là việc **liên kết các thiết bị thông minh** (có cảm biến, phần mềm, khả năng xử lí) qua mạng để **tự động thu thập, trao đổi và xử lí dữ liệu** phục vụ các mục đích khác nhau, **không nhất thiết có sự tương tác trực tiếp của con người với máy tính**.

**Lợi ích của IoT:**

- Thu thập dữ liệu **trên diện rộng**, liên tục 24/7, theo thời gian thực, thay con người ở môi trường nguy hiểm/khó tiếp cận.
- Giảm chi phí thu thập và xử lí dữ liệu; tự động hoá quy trình; hỗ trợ ra quyết định nhanh và chính xác.
- Tạo ra dịch vụ mới: nhà thông minh, thành phố thông minh, nông nghiệp chính xác, y tế từ xa, giao thông thông minh.

**Ví dụ cụ thể:**

<!-- COLS 28,72 -->
| Ứng dụng | Cách IoT hoạt động và lợi ích |
| --- | --- |
| Thu phí không dừng (ETC) | Thẻ RFID trên kính ô tô được đầu đọc tại trạm nhận diện → hệ thống tự trừ tiền → xe không phải dừng, giảm ùn tắc |
| Nhà thông minh | Cảm biến nhiệt độ/ độ ẩm/ khói gửi dữ liệu về trung tâm → tự bật điều hoà, tắt đèn, báo cháy về điện thoại |
| Camera giao thông thông minh | Camera nhận diện biển số, mật độ xe → tự điều chỉnh đèn tín hiệu, cảnh báo tai nạn về trung tâm |
| Đồng hồ thông minh | Đo nhịp tim, bước chân, giấc ngủ → cảnh báo sức khoẻ, gửi dữ liệu cho bác sĩ |
| Nông nghiệp thông minh | Cảm biến độ ẩm đất → tự bật tưới nhỏ giọt đúng lượng nước cần thiết, tiết kiệm nước và phân bón |

> **Phát biểu quan điểm mẫu (dùng cho câu TH/VDC):** "Theo em, lợi ích lớn nhất của IoT là **khả năng thu thập dữ liệu tự động, tức thời trên diện rộng**, nhờ đó con người ra quyết định dựa trên số liệu thật thay vì phỏng đoán – ví dụ cảm biến độ ẩm giúp tưới tiêu đúng lúc, vừa tăng năng suất vừa tiết kiệm nước. Tuy nhiên, IoT cũng làm tăng nguy cơ lộ dữ liệu cá nhân; vì vậy khi dùng thiết bị IoT cần đổi mật khẩu mặc định, cập nhật phần mềm và chỉ chia sẻ dữ liệu thật sự cần thiết."

### 3.2.6. TOÀN BỘ CÂU HỎI – ĐÁP ÁN TỪ ĐẶC TẢ ĐƠN VỊ B1 (6 yêu cầu)

**Câu B1.1 [NB].** Hãy nêu một số dịch vụ cụ thể mà Điện toán đám mây cung cấp cho người dùng.

> **Yêu cầu gốc (nguyên văn):** «Nêu được một số dịch vụ cụ thể mà Điện toán đám mây cung cấp cho người dùng.»

> **Đáp án:** Ba nhóm dịch vụ: (1) **SaaS** – thuê phần mềm ứng dụng: Google Docs, Gmail, Zoom, Microsoft 365; (2) **PaaS** – thuê nền tảng để phát triển/ vận hành sản phẩm: nền tảng cơ sở dữ liệu đám mây, môi trường lập trình web, Google Maps API; (3) **IaaS** – thuê hạ tầng phần cứng: máy chủ ảo, nơi lưu trữ dữ liệu như Google Drive, Dropbox, OneDrive. Ngoài ra có thể kể: dịch vụ sao lưu tự động, phát video trực tuyến, điện toán/máy học theo yêu cầu. Đặc điểm chung: dùng qua Internet, đăng kí tài khoản, trả theo mức sử dụng.

**Câu B1.2 [NB].** Hãy nêu khái niệm Internet vạn vật (IoT).

> **Yêu cầu gốc (nguyên văn):** «Nêu được khái niệm Internet vạn vật (IoT).»

> **Đáp án:** IoT (Internet of Things) là việc liên kết các thiết bị thông minh được gắn cảm biến, phần mềm và khả năng xử lí thông qua mạng máy tính/ Internet để chúng **tự động thu thập, trao đổi và xử lí dữ liệu** phục vụ các mục đích khác nhau, không nhất thiết có sự tương tác trực tiếp giữa con người với máy tính. Nói cách khác, IoT biến các đồ vật thường thành "đồ vật biết nói chuyện" với nhau. Ví dụ: cảm biến độ ẩm tự gửi lệnh tưới cây, thẻ ETC tự trừ phí đường bộ.

**Câu B1.3 [TH].** Hãy trình bày những thay đổi về chất lượng cuộc sống, phương thức học tập và làm việc khi mạng máy tính được sử dụng phổ biến.

> **Yêu cầu gốc (nguyên văn):** «Trình bày được những thay đổi về chất lượng cuộc sống, phương thức học tập và làm việc trong xã hội mà ở đó mạng máy tính được sử dụng phổ biến.»

> **Đáp án:** (1) **Cuộc sống**: liên lạc tức thời qua mạng xã hội/ gọi video không còn bị giới hạn bởi khoảng cách; mua sắm, thanh toán điện tử, đọc báo, xem phim, khám bệnh từ xa; nhà thông minh tự điều khiển nhiệt độ, ánh sáng, an ninh. (2) **Học tập**: lớp học ảo qua Zoom/ Google Meet, bài giảng và sách giáo khoa số trên igiaoduc.vn, thư viện số, công cụ dịch tự động và diễn đàn học tập; học mọi lúc mọi nơi, cá nhân hoá theo năng lực. (3) **Làm việc**: làm việc từ xa, họp trực tuyến, cộng tác thời gian thực trên tài liệu đám mây (Google Docs), chia sẻ tài nguyên máy in/ máy chủ, thuê hạ tầng đám mây thay vì đầu tư máy chủ riêng. Bên cạnh lợi ích là các thách thức: tin giả, lộ dữ liệu, nghiện mạng, khoảng cách số – đòi hỏi người dùng có kĩ năng số và ý thức pháp luật.

**Câu B1.4 [TH].** Hãy so sánh mạng LAN và Internet.

> **Yêu cầu gốc (nguyên văn):** «So sánh được mạng LAN và Internet.»

> **Đáp án:** (1) **Phạm vi**: LAN nhỏ (gia đình, trường học, cơ quan); Internet toàn cầu. (2) **Kết nối**: LAN nối trực tiếp qua Hub/ Switch/ Wi-Fi; Internet kết nối qua Router và nhà cung cấp dịch vụ (ISP). (3) **Sở hữu**: LAN có chủ sở hữu xác định; Internet không thuộc sở hữu riêng của ai, được các tổ chức quốc tế điều phối. (4) **Định tuyến**: Switch/ Hub chỉ chuyển dữ liệu trong nội bộ LAN; Router phát hiện địa chỉ đích ngoài LAN thì chuyển ra cổng Internet. Kết luận: Internet thực chất là mạng diện rộng (WAN) được tạo nên từ rất nhiều LAN liên kết với nhau.

**Câu B1.5 [TH].** Hãy nêu ví dụ cụ thể về thay đổi trong cuộc sống mà IoT đem lại.

> **Yêu cầu gốc (nguyên văn):** «Nêu được ví dụ cụ thể về thay đổi trong cuộc sống mà IoT đem lại.»

> **Đáp án:** Ví dụ 1: **thu phí không dừng ETC** – thẻ RFID trên ô tô được đầu đọc nhận diện và hệ thống tự trừ phí, xe không phải dừng chờ, giảm ùn tắc và khí thải. Ví dụ 2: **nhà thông minh** – cảm biến khói phát hiện cháy, tự động ngắt điện, mở khoá cửa và gửi cảnh báo về điện thoại chủ nhà dù họ đang đi vắng. Ví dụ 3: **đồng hồ thông minh** – đo nhịp tim liên tục, phát hiện bất thường và gửi cảnh báo cho người thân/bác sĩ. Ví dụ 4: **nông nghiệp thông minh** – cảm biến độ ẩm đất tự điều khiển tưới nhỏ giọt, tiết kiệm 30–40% nước.

**Câu B1.6 [TH].** Em hãy phát biểu ý kiến cá nhân về lợi ích của IoT.

> **Yêu cầu gốc (nguyên văn):** «Phát biểu ý kiến cá nhân về lợi ích của IoT.»

> **Đáp án mẫu (có thể diễn đạt lại):** "Em cho rằng lợi ích lớn nhất của IoT là dữ liệu được thu thập **tự động, liên tục và tức thời trên diện rộng**, giúp con người quyết định dựa trên số liệu thật: bác sĩ theo dõi nhịp tim bệnh nhân từ xa, nông dân tưới đúng lượng nước, thành phố điều chỉnh đèn giao thông theo lưu lượng xe. Nhờ đó tiết kiệm thời gian, giảm chi phí, tăng an toàn. Tuy nhiên, IoT chỉ thật sự có ích khi dữ liệu được bảo vệ: cần đổi mật khẩu mặc định, cập nhật phần mềm thiết bị, mã hoá đường truyền và chỉ thu thập dữ liệu cần thiết, tránh biến tiện ích thành công cụ theo dõi người dùng."

---

## 3.3. Đơn vị B2 – Sử dụng dịch vụ web và tự bảo vệ khi tham gia mạng (Bài 9, 10)

### 3.3.1. Các nguy cơ khi tham gia Internet

<!-- COLS 22,38,40 -->
| Nguy cơ | Biểu hiện | Hậu quả |
| --- | --- | --- |
| **Tin giả, tin phản văn hoá** | Tin bịa đặt, giật gân, nội dung bạo lực, nhảm nhí, độc hại | Nhận thức sai, hoang mang xã hội, tổn hại danh dự người khác |
| **Lừa đảo trực tuyến (phishing)** | Giả mạo ngân hàng/người quen gửi link, yêu cầu OTP, mời đầu tư "lãi cao", trúng thưởng ảo | Mất tiền, bị chiếm đoạt tài khoản, bị lộ dữ liệu |
| **Lộ thông tin cá nhân** | Đăng ảnh CCCD, số điện thoại, địa chỉ, tài khoản ngân hàng; dùng Wi-Fi công cộng không mã hoá | Bị mạo danh, bị quấy rối, mất tiền trong tài khoản |
| **Bắt nạt trên mạng (cyberbullying)** | Xỉ vả, lăng nhục, đưa tin bịa đặt, đe doạ tung ảnh riêng tư, tẩy chay tập thể | Ảnh hưởng nghiêm trọng tới tâm lí, nạn nhân tự cô lập, trầm cảm |
| **Phần mềm độc hại** | Virus, worm, trojan, ransomware tải qua link lạ/ phần mềm bẻ khoá | Mất dữ liệu, máy bị tê liệt, bị tống tiền, mất tài khoản |

> **Vì sao bắt nạt trên mạng nguy hiểm hơn ngoài đời?** Vì (1) nó xảy ra **dai dẳng, bất cứ lúc nào**, kể cả khi nạn nhân ở nhà; (2) người bắt nạt có thể **ẩn danh**, khó đối phó; (3) số người theo dõi, bình luận có thể **rất đông**, gây áp lực nặng nề; (4) nội dung xấu **lan nhanh và khó xoá hẳn** (bị chụp màn hình, chia sẻ lại).

### 3.3.2. Phần mềm độc hại (malware) – bảng tổng hợp phải thuộc

**Phần mềm độc hại** là phần mềm được viết ra với **ý đồ xấu**, gây ra các tác động không mong muốn cho người dùng và hệ thống. Theo cơ chế lây nhiễm có **2 loại chính là virus và worm**; ngoài ra **Trojan** là phần mềm nội gián ít chú trọng lây lan.

<!-- COLS 14,20,30,36 -->
| Loại | Tính hoàn chỉnh | Cơ chế lây nhiễm / xâm nhập | Tác hại chính |
| --- | --- | --- | --- |
| **Virus** | Không hoàn chỉnh – chỉ là đoạn mã độc, phải gắn vào phần mềm khác | Khi chạy phần mềm đã nhiễm, mã độc vào bộ nhớ, chèn sang phần mềm khác → hoàn thành chu kì lây lan | Làm hỏng phần mềm, xoá dữ liệu, tê liệt hệ thống |
| **Worm (sâu máy tính)** | Là phần mềm hoàn chỉnh, tự nhân bản | Lợi dụng lỗ hổng bảo mật của hệ điều hành hoặc lừa người dùng chạy liên kết/ tệp đính kèm | Lây lan nhanh qua mạng, làm nghẽn mạng, tê liệt máy chủ (tấn công DoS), tống tiền (WannaCry 2017) |
| **Trojan (ngựa thành Troa)** | Phần mềm hoàn chỉnh, ngụy trang thành tiện ích hợp pháp | Người dùng tự tải về và cài đặt, tưởng là phần mềm có ích | Hoạt động nội gián: đánh cắp thông tin, chiếm quyền điều khiển máy |

**Các biến thể của Trojan cần nhớ tên:**

- **Spyware** – phần mềm gián điệp: âm thầm thu thập thông tin rồi gửi ra ngoài.
- **Keylogger** – dạng spyware ghi lại thao tác bàn phím/chuột để đánh cắp mật khẩu.
- **Backdoor** – tạo tài khoản bí mật ("cửa sau") để kẻ xấu truy cập ngầm vào máy.
- **Rootkit** – chiếm quyền cao nhất của hệ thống, có thể xoá dấu vết xâm nhập.

**Mốc thảm hoạ để lấy ví dụ:** sâu **Melissa (1999)** thiệt hại hơn 1 tỉ USD; **Code Red (2001)** lợi dụng lỗi Windows, thiệt hại khoảng 2 tỉ USD trong 10 ngày; **WannaCry (2017)** mã hoá dữ liệu đòi tiền chuộc trên diện rộng.

**Cách phòng chống phần mềm độc hại (5 việc):** (1) thận trọng khi chép tệp từ USB, thẻ nhớ, ổ cứng rời hoặc tải từ mạng – đặc biệt phần mềm bẻ khoá/ crack; (2) **không mở liên kết hoặc tệp đính kèm** trong email/tin nhắn lạ, gọi điện xác minh người gửi; (3) cài và **cập nhật thường xuyên** phần mềm diệt virus/ Windows Security, bật tường lửa; (4) cập nhật hệ điều hành và ứng dụng để vá lỗ hổng; (5) sao lưu dữ liệu định kì (3-2-1: 3 bản, 2 thiết bị, 1 bản ngoài máy).

**Cách phòng vệ khi bị bắt nạt trên mạng (5 việc):** (1) **không kết bạn dễ dãi**, hạn chế công khai thông tin cá nhân; (2) **không trả lời, không tranh luận** với kẻ bắt nạt trên diễn đàn (tránh "thêm dầu vào lửa"); (3) **lưu giữ toàn bộ bằng chứng** (chụp màn hình, lưu link, thời gian); (4) **chia sẻ ngay với bố mẹ, thầy cô, bạn tin cậy**; (5) dùng chức năng **chặn/ báo cáo** của nền tảng; khi việc nghiêm trọng, **báo cơ quan công an kèm bằng chứng**.

### 3.3.3. Dịch vụ web và tài nguyên Internet phục vụ học tập (Bài 10)

Internet là **kho tài nguyên chung rất lớn**. Ba nhóm dịch vụ SGK yêu cầu khai thác được:

<!-- COLS 24,38,38 -->
| Dịch vụ | Cách sử dụng | Lưu ý khi dùng |
| --- | --- | --- |
| **Dịch tự động (Google Translate)** | Vào `translate.google.com` → chọn ngôn ngữ nguồn (văn bản cần dịch) và ngôn ngữ đích → nhập trực tiếp, đọc bằng micro/ giọng nói, hoặc nháy "Tài liệu" để dịch tệp Word/ Excel/ PowerPoint/ PDF → nháy "Dịch" → nghe phát âm bằng biểu tượng loa → chọn bản dịch, Ctrl+C rồi Ctrl+V vào tệp văn bản | Bản dịch máy **chưa đủ tự nhiên**, cần đọc lại, sửa thuật ngữ và kiểm chứng; không nên nộp nguyên bản dịch |
| **Học liệu mở (OER)** | Truy cập `https://igiaoduc.vn/` → thư mục cấp 1 gồm **Học liệu số, Sách giáo khoa, Dư địa chí** → mở thư mục cấp 2 (lớp) → cấp 3 (môn) → chọn bài giảng điện tử/ tài liệu → xem phần mô tả rồi mở học liệu | Chọn đúng lớp, môn, tên bài; kiểm tra tác giả/ nguồn; tôn trọng **giấy phép bản quyền** (CC), ghi rõ nguồn khi trích dẫn |
| **Bản đồ số (Google Maps)** | Vào `google.com/maps` → gõ địa danh → chọn gợi ý đúng → chuyển chế độ bản đồ giao thông/ vệ tinh bằng nút "Lớp bản đồ" → chọn "Chỉ đường", nhập điểm đi – điểm đến → xem khoảng cách và thời gian ước tính theo phương tiện | Thời gian ước tính thay đổi theo tình trạng giao thông; không nên chia sẻ vị trí thời gian thực công khai |

Khái niệm **học liệu mở (Open Educational Resources)** được dùng rộng rãi từ năm **2002**, khi Học viện Công nghệ Massachusetts (MIT) đưa toàn bộ nội dung giảng dạy của mình lên Internet để sử dụng miễn phí. Học liệu mở giúp ai cũng có thể học, nhưng "mở" **không có nghĩa là được tuỳ tiện chép mà không ghi nguồn** (xem Chủ đề D).

### 3.3.4. Tự bảo vệ dữ liệu cá nhân – "lá chắn 5 lớp"

<!-- COLS 8,28,64 -->
| Lớp | Biện pháp | Cách làm cụ thể |
| --- | --- | --- |
| 1 | **Mật khẩu mạnh** | Dài ≥ 12 kí tự, gồm chữ hoa, chữ thường, số, kí hiệu; mỗi tài khoản một mật khẩu riêng; dùng trình quản lí mật khẩu; không chia sẻ OTP/mã PIN cho ai |
| 2 | **Xác thực 2 yếu tố (2FA)** | Bật xác minh qua ứng dụng/ SMS/ khoá bảo mật cho email, mạng xã hội, ngân hàng |
| 3 | **Cẩn trọng khi chia sẻ** | Không đăng ảnh CCCD, vé máy bay (mã vạch), hoá đơn, số điện thoại, lịch trình cá nhân; hỏi ý kiến người khác trước khi đăng ảnh có mặt họ; kiểm tra quyền riêng tư của bài viết |
| 4 | **An toàn thiết bị & đường truyền** | Cập nhật hệ điều hành, dùng phần mềm diệt virus, khoá màn hình, không dùng Wi-Fi công cộng không mã hoá cho giao dịch ngân hàng (dùng 4G/VPN), tắt Bluetooth khi không dùng |
| 5 | **Sao lưu & kiểm soát quyền ứng dụng** | Sao lưu định kì lên ổ cứng rời/đám mây; rà soát và thu hồi quyền truy cập camera, micro, vị trí của ứng dụng không cần thiết; xoá tài khoản không dùng |

### 3.3.5. TOÀN BỘ CÂU HỎI – ĐÁP ÁN TỪ ĐẶC TẢ ĐƠN VỊ B2 (8 yêu cầu)

**Câu B2.1 [NB].** Hãy trình bày sơ lược về phần mềm độc hại.

> **Yêu cầu gốc (nguyên văn):** «Trình bày được sơ lược về phần mềm độc hại.»

> **Đáp án:** Phần mềm độc hại (malware) là phần mềm viết ra với ý đồ xấu, gây tác động không mong muốn cho người dùng. Theo cơ chế lây nhiễm có hai loại là **virus** (đoạn mã độc không hoàn chỉnh, phải gắn vào phần mềm khác; lây khi chạy phần mềm đã nhiễm) và **worm** (sâu máy tính – phần mềm hoàn chỉnh tự nhân bản, lây qua lỗ hổng hệ điều hành hoặc lừa người dùng chạy liên kết). **Trojan** là phần mềm nội gián ngụy trang thành tiện ích, gồm các biến thể spyware, keylogger, backdoor, rootkit, chuyên đánh cắp thông tin và chiếm quyền điều khiển máy. Tác hại: làm hỏng phần mềm, xoá/mã hoá dữ liệu đòi tiền chuộc, tê liệt hệ thống, mất tài khoản và tiền bạc. Phòng ngừa bằng cách không mở tệp/link lạ, không dùng phần mềm bẻ khoá, cập nhật hệ điều hành, dùng phần mềm diệt virus và sao lưu dữ liệu.

**Câu B2.2 [NB].** Hãy nêu một vài cách phòng vệ khi bị bắt nạt trên mạng.

> **Yêu cầu gốc (nguyên văn):** «Nêu được một vài cách phòng vệ khi bị bắt nạt trên mạng.»

> **Đáp án:** (1) Không kết bạn dễ dãi, không công khai thông tin cá nhân; (2) **không trả lời thư/tin nhắn, không tranh luận** với kẻ bắt nạt trên diễn đàn; (3) **lưu giữ tất cả bằng chứng** (chụp màn hình, lưu link, ghi thời gian); (4) **chia sẻ ngay với bố mẹ, thầy cô** hoặc người lớn tin cậy để được hỗ trợ; (5) dùng chức năng chặn và báo cáo tài khoản vi phạm của nền tảng; (6) khi sự việc nghiêm trọng (đe doạ, tống tiền, tung ảnh riêng tư), **báo cơ quan công an kèm theo bằng chứng**.

**Câu B2.3 [NB].** Hãy nêu những nguy cơ và tác hại nếu tham gia các hoạt động trên Internet một cách bất cẩn và thiếu hiểu biết.

> **Yêu cầu gốc (nguyên văn):** «Nêu được những nguy cơ và tác hại nếu tham gia các hoạt động trên Internet một cách bất cẩn và thiếu hiểu biết.»

> **Đáp án:** Các nguy cơ: (1) **tin giả, tin phản văn hoá** → nhận thức lệch lạc, tin vào lời khuyên y tế/tài chính sai; (2) **lừa đảo qua mạng** (giả mạo người thân vay tiền, link phishing đánh cắp OTP, "trúng thưởng", "việc nhẹ lương cao") → mất tiền, chiếm đoạt tài khoản; (3) **lộ thông tin cá nhân** (ảnh CCCD, số điện thoại, tài khoản ngân hàng, vị trí) → bị mạo danh, quấy rối, mất tiền; (4) **bắt nạt trên mạng** → tổn thương tâm lí kéo dài, trầm cảm, tự cô lập; (5) **phần mềm độc hại** khi tải phần mềm crack/ mở link lạ → mất dữ liệu, máy tê liệt, bị tống tiền; (6) **vi phạm pháp luật** do chia sẻ tin sai sự thật/ nội dung cấm → bị xử phạt, ảnh hưởng hồ sơ cá nhân. Hậu quả chung: thiệt hại tài sản, danh dự, sức khoẻ tinh thần và trách nhiệm pháp lí.

**Câu B2.4 [TH].** Hãy trình bày một số cách đề phòng những tác hại khi tham gia các hoạt động trên Internet.

> **Yêu cầu gốc (nguyên văn):** «Trình bày được một số cách đề phòng những tác hại khi tham gia các hoạt động trên Internet»

> **Đáp án:** Có 6 nhóm biện pháp: (1) **Kiểm chứng thông tin** – đọc từ nhiều nguồn chính thống, kiểm tra ngày đăng/tác giả, không vội chia sẻ tin chưa rõ; (2) **Bảo vệ tài khoản** – mật khẩu mạnh, bật 2FA, không dùng chung mật khẩu, không nhập OTP trên trang lạ, kiểm tra kĩ tên miền (https + đúng tên thương hiệu); (3) **Giữ kín dữ liệu cá nhân** – không đăng giấy tờ, mã QR thanh toán, ảnh có địa chỉ nhà/trường; thiết lập chế độ riêng tư; (4) **An toàn kĩ thuật** – cập nhật hệ điều hành/trình duyệt, cài và cập nhật phần mềm diệt virus, bật tường lửa, không cài phần mềm bẻ khoá, không cắm USB lạ, hạn chế Wi-Fi công cộng khi giao dịch; (5) **Ứng xử văn minh** – không công kích, không phát tán nội dung độc hại, tôn trọng quyền riêng tư của người khác; (6) **Sao lưu và báo cáo** – sao lưu dữ liệu định kì, khi có sự cố thì lưu bằng chứng và báo cho thầy cô/bố mẹ/cơ quan chức năng.

**Câu B2.5 [VD].** Em hãy nêu cách sử dụng một số công cụ thông dụng để ngăn ngừa và loại bỏ phần mềm độc hại.

> **Yêu cầu gốc (nguyên văn):** «Sử dụng được một số công cụ thông dụng để ngăn ngừa và loại bỏ phần mềm độc hại.»

> **Đáp án:** Quy trình 4 bước với công cụ cụ thể: (1) **Phòng ngừa** – bật *Windows Security/Microsoft Defender Antivirus* (hoặc phần mềm diệt virus uy tín), bật tính năng bảo vệ thời gian thực và tường lửa; bật tự động cập nhật Windows và trình duyệt. (2) **Kiểm tra** – mở Windows Security → *Virus & threat protection* → *Scan options* → chọn *Full scan* để quét toàn bộ ổ đĩa; quét riêng tệp vừa tải về bằng chuột phải → *Scan with Microsoft Defender*. (3) **Xử lí** – nếu phát hiện mã độc, chọn *Quarantine* (cách li) rồi *Remove/Delete*; không mở lại tệp đó; đổi ngay mật khẩu các tài khoản quan trọng từ một thiết bị sạch. (4) **Khôi phục** – khôi phục dữ liệu từ bản sao lưu; nếu hệ thống hỏng nặng thì dùng *System Restore*/ cài lại hệ điều hành. Kèm theo: gỡ các tiện ích (extension) lạ trong trình duyệt, xoá bộ nhớ cache, kiểm tra danh sách chương trình khởi động cùng Windows.

**Câu B2.6 [VD].** Hãy mô tả cách sử dụng một số chức năng xử lí thông tin trên máy PC và thiết bị số, ví dụ dịch tự động văn bản hay tiếng nói.

> **Yêu cầu gốc (nguyên văn):** «Sử dụng được một số chức năng xử lí thông tin trên máy PC và thiết bị số, ví dụ dịch tự động văn bản hay tiếng nói.»

> **Đáp án:** Với **dịch văn bản**: truy cập `translate.google.com` → chọn ngôn ngữ nguồn (ví dụ tiếng Việt) và ngôn ngữ đích (tiếng Anh) → gõ/ dán văn bản vào khung bên trái → bản dịch hiện bên phải → nháy biểu tượng loa để nghe phát âm → nháy biểu tượng ⇆ để đổi chiều dịch và so sánh ngược. Với **dịch tiếng nói**: nháy biểu tượng micro, cho phép trình duyệt dùng micro, nói câu cần dịch → phần mềm nhận dạng giọng nói thành văn bản rồi dịch. Với **dịch tệp tài liệu**: nháy "Tài liệu" → "Tìm tệp trên máy tính của bạn" → chọn tệp .docx/ .xlsx/ .pptx/ .pdf → nháy "Dịch" → nhận bản dịch trên cửa sổ riêng → Ctrl+C/ Ctrl+V để lưu vào tệp văn bản, sau đó **đọc lại và chỉnh sửa** thuật ngữ. Ngoài ra có thể dùng tính năng **dịch camera/ ảnh** trên điện thoại để dịch biển báo, thực đơn; dùng **nhận dạng chữ viết tay** và **chính tả/ gợi ý ngữ pháp** trong phần mềm soạn thảo.

**Câu B2.7 [VD].** Em hãy nêu cách khai thác một số nguồn học liệu mở trên Internet.

> **Yêu cầu gốc (nguyên văn):** «Khai thác được một số nguồn học liệu mở trên Internet»

> **Đáp án:** Quy trình 5 bước: (1) Xác định nhu cầu (môn, lớp, tên bài, dạng tài liệu: bài giảng/ sách/ đề thi). (2) Truy cập kho học liệu mở `https://igiaoduc.vn/` (hoặc các kho tương tự như thuvienhoclieu.com, MIT OpenCourseWare, Khan Academy, Wikimedia Commons). (3) Đi theo cây thư mục: cấp 1 gồm **Học liệu số – Sách giáo khoa – Dư địa chí** → chọn "Học liệu số" → cấp 2 chọn **Lớp 10** → cấp 3 chọn môn **Tin học** → danh sách học liệu hiện ra, nháy vào học liệu để xem mô tả (tên bài, chủ đề, tác giả). (4) Mở bài giảng điện tử, nghe giảng, tải tài liệu về máy, ghi chép có chọn lọc. (5) **Kiểm chứng và trích nguồn**: đối chiếu với SGK, ghi rõ tên tác giả/đường dẫn khi dùng lại, tôn trọng giấy phép (CC BY, CC BY-SA…). Không nên tải tài liệu từ trang lạ có nhiều quảng cáo/ yêu cầu cài phần mềm không rõ nguồn gốc.

**Câu B2.8 [VD].** Em biết cách tự bảo vệ dữ liệu của cá nhân như thế nào?

> **Yêu cầu gốc (nguyên văn):** «Biết cách tự bảo vệ dữ liệu của cá nhân.»

> **Đáp án:** Áp dụng "lá chắn 5 lớp" ở mục 3.3.4: (1) đặt **mật khẩu mạnh, khác nhau cho từng tài khoản**, bật xác thực 2 yếu tố, không chia sẻ OTP/mã PIN; (2) **không công khai** họ tên đầy đủ kèm ngày sinh, số điện thoại, CCCD, địa chỉ, tài khoản ngân hàng, lịch trình, ảnh đồng phục có tên trường; (3) thiết lập **quyền riêng tư** trên mạng xã hội (bạn bè thay vì công khai), hỏi ý kiến người khác trước khi đăng ảnh có mặt họ; (4) **an toàn kĩ thuật**: cập nhật hệ điều hành, dùng phần mềm diệt virus, không nhập mật khẩu trên Wi-Fi công cộng không mã hoá, rà soát quyền camera/micro/vị trí của ứng dụng, khoá màn hình; (5) **sao lưu và xử lí sự cố**: sao lưu định kì, khi nghi lộ dữ liệu thì đổi mật khẩu ngay, thông báo nhà cung cấp dịch vụ và báo cơ quan chức năng nếu có thiệt hại.

## 3.4. Tóm tắt cuối Chủ đề B và 8 lỗi sai thường gặp

**Bảng "biết – làm được":**

<!-- COLS 50,50 -->
| Em phải BIẾT | Em phải LÀM ĐƯỢC |
| --- | --- |
| Mạng máy tính, LAN, WAN, Internet, ISP, Hub, Switch, Router, TCP/IP, WWW, đám mây, SaaS/PaaS/IaaS, IoT, malware, virus/worm/trojan, spyware/keylogger/backdoor/rootkit, phishing, bắt nạt trên mạng, học liệu mở, 2FA | So sánh LAN–Internet; phân loại dịch vụ đám mây; nhận diện loại mã độc qua cơ chế lây; nêu 5 cách phòng vệ; mô tả quy trình dịch tệp bằng Google Dịch; khai thác igiaoduc.vn; thiết lập bảo vệ dữ liệu cá nhân |

**8 lỗi sai hay gặp:**

- Nhầm **Router thành thiết bị nối trong LAN** (Switch/Hub mới nối trong LAN; Router nối LAN ra ngoài).
- Nhầm **LAN có quy mô toàn cầu**; thực tế Internet mới là WAN toàn cầu.
- Nhầm **SaaS là thuê máy chủ** (đúng: IaaS thuê hạ tầng, PaaS thuê nền tảng, SaaS thuê phần mềm).
- Nói IoT **chỉ kết nối qua Internet**; thực tế các thiết bị có thể nối qua Bluetooth, Zigbee, mạng nội bộ rồi mới lên Internet.
- Cho rằng **Trojan là virus**; Trojan là phần mềm nội gián, không có cơ chế tự lây như virus/worm.
- Cho rằng **virus là phần mềm hoàn chỉnh**; virus chỉ là đoạn mã độc phải gắn vào phần mềm khác.
- Nghĩ **học liệu mở = dùng thoải mái không cần ghi nguồn**; vẫn phải tôn trọng giấy phép bản quyền.
- Mở **link lạ hoặc cài phần mềm crack** rồi mới chạy diệt virus – đáng lẽ phải phòng ngừa từ đầu.

<!-- PAGEBREAK -->
