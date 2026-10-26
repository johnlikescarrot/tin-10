# -*- coding: utf-8 -*-
"""Phần 3 – Chủ đề B (Chủ đề 2 KNTT): Mạng máy tính và Internet."""
from .blocks import H1, H2, H3, P, LEAD, SMALL, UL, OL, TBL, BOX, PB, SP


def blocks():
    B = [
        H1("PHẦN 3 · CHỦ ĐỀ B: MẠNG MÁY TÍNH VÀ INTERNET"),
        LEAD("Tương ứng **Chủ đề 2** trong SGK *Kết nối tri thức với cuộc sống* (Bài 8, 9, 10). "
             "Chủ đề này chiếm **40% đề**. Trục nhớ: **kết nối → dịch vụ → rủi ro → phòng vệ**."),

        # ------------------------------------------------------------- B1
        H2("3.1. B1 – Khái niệm mạng máy tính, Internet, IoT; phân loại mạng"),
        P("*SGK KNTT Bài 8. Đặc tả: 4 câu Nhận biết, 1 câu đúng/sai (2 ý Thông hiểu + 2 ý Vận dụng).*"),

        H3("3.1.1. Mạng máy tính là gì?"),
        P("**Mạng máy tính** là tập hợp các máy tính và thiết bị được **kết nối với nhau** qua đường truyền "
          "(cáp, sóng vô tuyến) theo một **giao thức** chung, nhằm **chia sẻ tài nguyên và trao đổi dữ liệu**."),
        TBL(["Thành phần", "Vai trò", "Ví dụ"], [
            ["Thiết bị đầu cuối", "Nơi phát và nhận dữ liệu.", "Máy tính, điện thoại, camera IP, máy in"],
            ["Thiết bị kết nối mạng", "Chuyển tiếp dữ liệu đúng đích.", "Hub, Switch, Router, Access Point (Wi-Fi)"],
            ["Đường truyền", "Môi trường mang tín hiệu.", "Cáp xoắn, cáp quang, sóng Wi-Fi, 4G/5G"],
            ["Giao thức", "Bộ quy tắc “ngôn ngữ chung”.", "TCP/IP, HTTP, HTTPS, FTP"],
            ["Phần mềm / dịch vụ", "Ứng dụng chạy trên hạ tầng mạng.", "Trình duyệt web, email, Zoom, Drive"],
        ], widths=[105, 200, 206], fs=8.2),
        P("**Lợi ích:** dùng chung máy in, ổ cứng, đường truyền Internet; chia sẻ tệp dễ dàng; "
          "liên lạc nhanh; làm việc nhóm và học tập từ xa."),

        H3("3.1.2. Phân loại mạng – móc nhớ P – L – M – W"),
        TBL(["Loại", "Tên đầy đủ", "Phạm vi", "Ví dụ"], [
            ["**PAN**", "Personal Area Network", "Vài mét, quanh một người (**Phòng**).",
             "Điện thoại kết nối tai nghe Bluetooth, đồng hồ thông minh."],
            ["**LAN**", "Local Area Network", "Một nhà, một tầng **Lầu**, một trường học, công ty.",
             "Wi-Fi gia đình; phòng máy tính của trường."],
            ["**MAN**", "Metropolitan Area Network", "Quy mô **Mạng phố** / thành phố.",
             "Mạng nối các chi nhánh ngân hàng trong một thành phố."],
            ["**WAN**", "Wide Area Network", "Quốc gia, châu lục, **W**orld.",
             "Mạng của một tập đoàn đa quốc gia; **Internet là WAN lớn nhất**."],
        ], widths=[58, 140, 165, 148], fs=8.2),
        BOX("So sánh LAN và Internet (câu Thông hiểu chắc chắn ra)", [
            "**Tiêu chí:** ① sở hữu ② phạm vi ③ thiết bị kết nối ④ tốc độ/độ trễ ⑤ quản lí ⑥ ví dụ.",
            "**LAN:** thuộc sở hữu **một cá nhân/gia đình/cơ quan**; phạm vi **nhỏ** (nhà, trường, công ty); "
            "kết nối trực tiếp qua **Hub, Switch, Wi-Fi**; tốc độ cao, độ trễ thấp; **một người quản lí**.",
            "**Internet:** **không thuộc sở hữu riêng của ai**, quy mô **toàn cầu**; kết nối qua **Router** "
            "và các **nhà cung cấp dịch vụ Internet (ISP)**; tốc độ phụ thuộc đường truyền; "
            "**nhiều tổ chức cùng quản lí**, dùng chung giao thức **TCP/IP**.",
            "**Câu chốt:** LAN là mạng riêng quy mô nhỏ; Internet là **mạng của các mạng** quy mô toàn cầu.",
        ], "example"),
        BOX("Phân biệt hay bị nhầm", [
            "**Internet ≠ Web.** Internet là hạ tầng kết nối; **World Wide Web (WWW)** là một dịch vụ "
            "trên Internet (cùng với email, FTP, điện toán đám mây, mạng xã hội…).",
            "**Web ≠ website.** Web là hệ thống các trang web liên kết với nhau; website là một tập hợp trang web.",
            "**Địa chỉ IP** là “số nhà” của thiết bị trên mạng; **tên miền/DNS** là “tên người” dễ nhớ "
            "được dịch sang địa chỉ IP (ví dụ `moet.gov.vn`).",
        ], "note"),

        H3("3.1.3. Tác động của mạng máy tính tới đời sống, học tập, làm việc"),
        TBL(["Lĩnh vực", "Thay đổi khi mạng phổ biến", "Ví dụ"], [
            ["Chất lượng cuộc sống", "Thông tin, giải trí, dịch vụ công được truy cập mọi lúc, mọi nơi.",
             "Xem phim trực tuyến, đặt đồ ăn, khám bệnh từ xa, thanh toán không dùng tiền mặt."],
            ["Học tập", "Kho tri thức khổng lồ, cập nhật liên tục; học mọi lúc, mọi nơi.",
             "Lớp học trực tuyến (Zoom, Meet), bài giảng trên YouTube, thư viện số, học liệu mở."],
            ["Làm việc", "Cộng tác từ xa, họp trực tuyến, lưu trữ và xử lí dữ liệu trên đám mây.",
             "Google Docs cho nhiều người sửa cùng lúc; gửi tệp lớn qua Drive thay vì USB."],
            ["Giao tiếp cộng đồng", "Kết nối không giới hạn khoảng cách, phản hồi tức thì.",
             "Zalo, email, mạng xã hội, diễn đàn."],
            ["Kinh tế", "Thương mại điện tử, ngân hàng số, chính phủ số.",
             "Mua hàng online, nộp hồ sơ trực tuyến."],
        ], widths=[100, 240, 171], fs=8.2),
        P("**Câu trả lời mẫu:** “Khi mạng máy tính được sử dụng phổ biến, Internet trở thành kho tri thức "
          "khổng lồ truy cập được ở bất cứ đâu, bất cứ lúc nào. Trong giáo dục, học sinh học trực tuyến và "
          "khai thác học liệu mở; trong công việc, họp trực tuyến và cộng tác trên đám mây; "
          "trong đời sống, mua sắm, giải trí, dịch vụ công đều thực hiện qua mạng.”"),

        H3("3.1.4. Điện toán đám mây và các dịch vụ cụ thể"),
        P("**Khái niệm:** điện toán đám mây là việc **chia sẻ các tài nguyên theo nhu cầu qua Internet**, "
          "miễn phí hoặc trả phí. Tài nguyên có thể là phần mềm, nền tảng hoặc hạ tầng."),
        TBL(["Loại dịch vụ", "Tên đầy đủ", "Thuê cái gì?", "Ví dụ cụ thể"], [
            ["**SaaS**", "Software as a Service", "Thuê **phần mềm ứng dụng** chạy ngay trên trình duyệt.",
             "Google Docs, Gmail, Zoom, Microsoft 365, Netflix."],
            ["**PaaS**", "Platform as a Service", "Thuê **nền tảng** để phát triển ứng dụng.",
             "Google Maps Platform cho app gọi xe; Heroku; Firebase."],
            ["**IaaS**", "Infrastructure as a Service", "Thuê **hạ tầng**: máy chủ, lưu trữ, mạng.",
             "Google Drive, Dropbox, OneDrive, Amazon S3, máy chủ ảo AWS/Azure."],
        ], widths=[92, 122, 175, 122], fs=8.2),
        BOX("Câu trả lời mẫu cho yêu cầu “nêu một số dịch vụ cụ thể của điện toán đám mây”", [
            "**Lưu trữ và đồng bộ tệp:** Google Drive, Dropbox, OneDrive, iCloud.",
            "**Soạn thảo và cộng tác:** Google Docs, Google Sheets, Microsoft 365.",
            "**Thư điện tử:** Gmail, Outlook.",
            "**Họp/học trực tuyến:** Zoom, Google Meet, Microsoft Teams.",
            "**Giải trí:** Netflix, Spotify, YouTube.",
            "**Cho nhà phát triển:** thuê máy chủ ảo, cơ sở dữ liệu, nền tảng bản đồ (IaaS/PaaS).",
        ], "example"),
        P("**Lợi ích:** tính **mềm dẻo** và độ **sẵn sàng cao**, chất lượng cao, **kinh tế hơn** "
          "(không phải đầu tư máy chủ riêng, trả theo nhu cầu). **Hạn chế:** phụ thuộc vào đường truyền, "
          "rủi ro lộ dữ liệu nếu cấu hình sai, chi phí có thể tăng khi dùng nhiều."),

        H3("3.1.5. Internet vạn vật (IoT)"),
        P("**Khái niệm:** IoT (Internet of Things) là việc **liên kết các thiết bị thông minh** với nhau "
          "qua mạng để **tự động thu thập, trao đổi và xử lí dữ liệu** phục vụ các mục đích khác nhau, "
          "hạn chế sự can thiệp của con người."),
        TBL(["Lớp", "Chức năng", "Ví dụ nhà thông minh"], [
            ["1. Thiết bị / cảm biến", "Đo và tạo dữ liệu.", "Cảm biến nhiệt độ, độ ẩm, camera"],
            ["2. Mạng truyền dẫn", "Chuyển dữ liệu đi.", "Wi-Fi, Bluetooth, Zigbee, 4G/5G"],
            ["3. Xử lí / đám mây", "Lưu trữ, phân tích, ra quyết định.", "Máy chủ phân tích, AI"],
            ["4. Ứng dụng / con người", "Hiển thị, điều khiển, cảnh báo.", "Ứng dụng điện thoại bật điều hoà"],
        ], widths=[112, 200, 199], fs=8.2),
        TBL(["Lợi ích của IoT (theo SGK)", "Ví dụ minh hoạ"], [
            ["Thu thập dữ liệu trên **diện rộng**, làm việc ở nơi con người không thể.",
             "Cảm biến giám sát trong lò phản ứng hạt nhân, dưới đáy biển."],
            ["Hoạt động **liên tục, tự động**, cung cấp dữ liệu **tức thời**.",
             "Xe tự lái; cảnh báo thiên tai; theo dõi nhịp tim 24/7."],
            ["**Tiết kiệm chi phí** do giảm bớt lao động.",
             "Thu phí không dừng trên cao tốc; tưới tiêu tự động; đèn đường tự bật tắt."],
        ], widths=[250, 261], fs=8.2),
        BOX("Nêu ví dụ + phát biểu ý kiến cá nhân (dạng câu hỏi mở)", [
            "**Ví dụ:** Trước đây phải ra đồng kiểm tra độ ẩm đất; nay cảm biến gửi dữ liệu về điện thoại "
            "và hệ thống tự tưới khi đất khô. Cuộc sống của nông dân vì thế nhẹ nhàng hơn, "
            "năng suất ổn định hơn.",
            "**Ý kiến cá nhân mẫu:** “Em thấy IoT mang lại lợi ích rất lớn: tiết kiệm thời gian, "
            "giảm rủi ro cho con người và giúp ra quyết định dựa trên dữ liệu thay vì cảm tính. "
            "Tuy nhiên, cần chú ý bảo mật thiết bị và bảo vệ dữ liệu cá nhân, vì một camera hay "
            "đồng hồ thông minh bị xâm nhập có thể làm lộ thông tin riêng tư.”",
        ], "example"),

        H3("3.1.6. Ghi nhớ nhanh B1"),
        BOX("B1 trong 6 dòng", [
            "1. Mạng = **thiết bị + đường truyền + giao thức + dịch vụ**.",
            "2. **P – L – M – W**: Phòng – Lầu – Mạng phố – Thế giới.",
            "3. LAN là mạng riêng nhỏ; **Internet là mạng của các mạng** dùng TCP/IP, không ai sở hữu.",
            "4. **Internet ≠ Web**; IP là số nhà, DNS là tên miền.",
            "5. Đám mây = **IaaS (máy) → PaaS (nền) → SaaS (phần mềm)**.",
            "6. IoT = thiết bị **tự thu – tự gửi – tự xử** dữ liệu; lợi ích đi kèm rủi ro bảo mật.",
        ], "memory"),
        PB(),

        # ------------------------------------------------------------- B2
        H2("3.2. B2 – Sử dụng dịch vụ web và tự bảo vệ khi tham gia mạng"),
        P("*SGK KNTT Bài 9 và Bài 10. Đặc tả: 3 câu Nhận biết, 2 câu Thông hiểu, 4 yêu cầu Vận dụng; "
          "ma trận có thêm 1 câu tự luận Thông hiểu.*"),

        H3("3.2.1. Dịch vụ web, tìm kiếm và đánh giá nguồn tin"),
        TBL(["Khái niệm", "Giải thích ngắn"], [
            ["World Wide Web (Web)", "Hệ thống các trang web liên kết với nhau bằng siêu liên kết, "
                                    "truy cập bằng trình duyệt."],
            ["Trang web / website", "Tập hợp các trang web của một tổ chức/cá nhân, đặt tại một địa chỉ."],
            ["URL", "Địa chỉ của trang web, gồm giao thức + tên miền + đường dẫn "
                    "(ví dụ `https://igiaoduc.vn/`)."],
            ["Trình duyệt", "Phần mềm đọc và hiển thị trang web: Chrome, Edge, Firefox, Safari."],
            ["Công cụ tìm kiếm", "Giúp tìm trang web theo từ khoá: Google, Bing, Cốc Cốc."],
            ["HTTPS", "Giao thức truyền tải web **có mã hoá** – nên ưu tiên khi nhập thông tin cá nhân."],
        ], widths=[118, 393], fs=8.2),
        P("**5 bước đánh giá một nguồn tin trên web** (rất hay hỏi ở câu Thông hiểu):"),
        OL([
            "**Ai viết?** – xác định tác giả, cơ quan phát hành, có uy tín không.",
            "**Khi nào?** – kiểm tra ngày đăng, thông tin còn cập nhật không.",
            "**Ở đâu?** – ưu tiên trang của cơ quan nhà nước, trường học, báo chính thống, tạp chí khoa học.",
            "**Để làm gì?** – phân biệt tin tức, quảng cáo, ý kiến cá nhân, tin châm biếm.",
            "**Đối chiếu** – tìm ít nhất 2 nguồn độc lập cùng nói về một sự kiện trước khi tin và chia sẻ.",
        ]),

        H3("3.2.2. Học liệu mở và xử lí thông tin trên thiết bị số"),
        P("**Học liệu mở (OER – Open Educational Resources)** là tài nguyên giáo dục được chia sẻ "
          "miễn phí hoặc với giấy phép mở, cho phép **sử dụng, sửa đổi, chia sẻ lại hợp pháp** "
          "(thường kèm điều kiện ghi nguồn)."),
        TBL(["Nguồn học liệu mở", "Có gì", "Lưu ý khi dùng"], [
            ["Cổng học liệu số / igiaoduc.vn", "Học liệu số, sách giáo khoa điện tử, bài giảng theo môn, cấp học.",
             "Chọn đúng môn – lớp – chủ đề; ghi tên tác giả bài giảng."],
            ["VOER, Wikipedia, Wikimedia Commons", "Bách khoa tri thức, ảnh/video/âm thanh có giấy phép mở.",
             "Kiểm tra giấy phép cụ thể; vẫn cần ghi nguồn."],
            ["Khan Academy, MIT OpenCourseWare, Coursera", "Bài giảng video, bài tập, tài liệu đại học mở.",
             "Chọn nội dung phù hợp trình độ lớp 10."],
            ["Thư viện số, tạp chí khoa học mở", "Sách, bài báo, số liệu thống kê.",
             "Ghi rõ tên tài liệu, tác giả, năm xuất bản."],
        ], widths=[150, 210, 151], fs=8.2),
        P("**Cách khai thác đúng:** xác định nhu cầu → tìm từ khoá → lọc theo độ tin cậy → đọc mô tả "
          "(tên bài, chủ đề, tác giả) → mở học liệu → **ghi nguồn** vào bài làm. "
          "Tuyệt đối không chép nguyên bài rồi nhận là của mình (xem thêm Phần 4)."),
        BOX("Thực hành: dịch tự động văn bản / tiếng nói (Bài 10 SGK)", [
            "**Bước 1:** truy cập trình dịch (ví dụ Google Translate) → chọn **ngôn ngữ nguồn** "
            "(văn bản cần dịch) và **ngôn ngữ đích** (kết quả).",
            "**Bước 2:** nhập dữ liệu bằng **3 cách**: gõ trực tiếp, **nói qua micro** (giọng nói), "
            "hoặc **tải tệp** (.docx, .xlsx, .pptx, .pdf).",
            "**Bước 3:** đọc kết quả; có thể nghe máy đọc (1 lần = tốc độ thường, 2 lần = chậm).",
            "**Bước 4:** sao chép (Ctrl + C) → dán (Ctrl + V) vào văn bản; **rà soát lại** vì bản dịch "
            "có thể chưa trau chuốt hoặc sai nghĩa.",
            "**Mở rộng:** dùng tính năng **nhập bằng giọng nói** (voice typing) trên điện thoại/máy tính "
            "để soạn văn bản nhanh – đây cũng là một chức năng xử lí thông tin bằng thiết bị số.",
        ], "example"),

        H3("3.2.3. Phần mềm độc hại – nhận diện và phòng chống"),
        P("**Phần mềm độc hại (malware)** là phần mềm được thiết kế để **xâm nhập, phá hoại hoặc "
          "đánh cắp thông tin** trên thiết bị của người dùng mà họ không hay biết."),
        TBL(["Loại", "Đặc điểm cốt lõi", "Đường lây / tác hại"], [
            ["**Virus**", "**Đoạn mã độc**, không phải phần mềm hoàn chỉnh; "
                          "gắn vào phần mềm/tệp khác mới phát tác.",
             "Lây qua tệp, USB, email đính kèm; làm hỏng chương trình, xoá dữ liệu."],
            ["**Worm (sâu)**", "Phần mềm **hoàn chỉnh**, tự nhân bản, **không cần vật chủ**.",
             "Lây qua lỗ hổng bảo mật, mạng; làm tắc nghẽn mạng (Melissa 1999, Code Red 2001)."],
            ["**Trojan (ngựa thành Troia)**", "Đội lốt phần mềm có ích để lừa người dùng cài.",
             "Mở cửa sau cho kẻ xấu điều khiển máy."],
            ["**Spyware**", "Gián điệp: âm thầm thu thập thông tin.", "Đánh cắp mật khẩu, dữ liệu cá nhân."],
            ["**Keylogger**", "Ghi lại thao tác bàn phím, chuột.", "Lộ mật khẩu ngân hàng, tài khoản."],
            ["**Backdoor / Rootkit**", "Tạo tài khoản bí mật / chiếm quyền cao nhất.",
             "Truy cập ngầm, xoá dấu vết, rất khó phát hiện."],
            ["**Ransomware**", "Mã hoá dữ liệu rồi đòi tiền chuộc.", "Mất toàn bộ tệp nếu không có sao lưu."],
            ["**Adware**", "Hiển thị quảng cáo không mong muốn.", "Gây phiền toái, dẫn tới trang độc hại."],
        ], widths=[92, 200, 219], fs=8.1),
        P("**Tác hại chung:** làm hỏng phần mềm khác, xoá dữ liệu, làm tê liệt hệ thống, "
          "đánh cắp thông tin, gây thiệt hại kinh tế (sâu Melissa năm 1999 gây thiệt hại hơn 1 tỉ USD; "
          "Code Red năm 2001 khoảng 2 tỉ USD – theo SGK)."),
        BOX("Câu trả lời mẫu: “Trình bày sơ lược về phần mềm độc hại”", [
            "Phần mềm độc hại là chương trình được tạo ra với ý đồ xấu, xâm nhập máy tính qua tệp, USB, "
            "email hay liên kết lạ. Có nhiều dạng: virus (đoạn mã kí sinh), worm (sâu tự lây qua lỗ hổng), "
            "trojan (đội lốt phần mềm hợp pháp), spyware/keylogger (đánh cắp dữ liệu), ransomware "
            "(mã hoá tệp đòi tiền chuộc). Chúng có thể làm hỏng phần mềm, xoá dữ liệu, tê liệt hệ thống "
            "và gây thiệt hại lớn về kinh tế.",
        ], "example"),
        BOX("Công cụ phòng ngừa và loại bỏ (yêu cầu Vận dụng)", [
            "**Windows Defender / Microsoft Defender:** Start → Settings → Privacy & Security → "
            "Windows Security → Virus & threat protection → **Scan options**. "
            "Có 4 chế độ: **Quét nhanh** (thư mục nguy cơ cao), **Quét toàn bộ** (mọi ổ đĩa), "
            "**Quét tuỳ chọn** (chọn thư mục), **Quét ngoại tuyến**. Sau đó bấm **Scan now**.",
            "**Cách nhanh:** nháy chuột phải vào tệp/thư mục → **Scan with Microsoft Defender**.",
            "**Phần mềm khác:** Bkav (Việt Nam), Kaspersky, Avast, AVG, Bitdefender.",
            "**6 thói quen:** cập nhật hệ điều hành và ứng dụng; không mở liên kết/tệp đính kèm lạ; "
            "tải phần mềm từ nguồn chính thức (không dùng bản crack); quét USB/thẻ nhớ trước khi mở; "
            "bật tường lửa và chương trình chống mã độc; **sao lưu dữ liệu định kì**.",
        ], "tip"),

        H3("3.2.4. Năm nguy cơ khi tham gia Internet và cách tự bảo vệ"),
        TBL(["Nguy cơ", "Biểu hiện", "Tác hại"], [
            ["**Tin giả, tin phản văn hoá**", "Tin đồn, thông tin sai lệch, nội dung bạo lực, dâm ô.",
             "Hoang mang, hiểu sai, vi phạm pháp luật nếu chia sẻ."],
            ["**Lừa đảo trên mạng (phishing)**", "Giả danh ngân hàng/giáo viên, dụ chuyển tiền, đưa link lạ.",
             "Mất tiền, mất tài khoản, lộ dữ liệu."],
            ["**Lộ thông tin cá nhân**", "Đăng ảnh, số điện thoại, địa chỉ, ngày sinh, mã OTP.",
             "Bị mạo danh, quấy rối, tấn công mạng xã hội."],
            ["**Bắt nạt trên mạng**", "Nhắn tin đe doạ, lập nhóm chê bai, tung ảnh chế.",
             "Tổn thương tinh thần, ảnh hưởng học tập, trầm cảm."],
            ["**Nghiện mạng / game**", "Dùng mạng quá nhiều, mất kiểm soát thời gian.",
             "Giảm sức khỏe, kết quả học tập sa sút, rối loạn giấc ngủ."],
        ], widths=[112, 205, 194], fs=8.2),
        BOX("Phòng vệ khi bị bắt nạt trên mạng (theo SGK – câu Nhận biết hay ra)", [
            "① **Không kết bạn dễ dãi** qua mạng; ② **Không trả lời** thư/tin nhắn của kẻ bắt nạt "
            "(đáp trả thường làm tình huống xấu hơn); ③ **Lưu giữ mọi bằng chứng** (chụp màn hình, "
            "lưu tin nhắn, ghi thời gian); ④ **Chia sẻ ngay với bố mẹ hoặc thầy cô**; "
            "⑤ Khi sự việc nghiêm trọng, **báo cơ quan công an** kèm bằng chứng; "
            "⑥ Dùng chức năng **chặn (block) và báo cáo (report)** của nền tảng.",
        ], "tip"),
        BOX("Cách đề phòng tác hại và bảo vệ dữ liệu cá nhân", [
            "**Thông tin cá nhân:** không ghi/chụp nơi người khác dễ đọc; không công khai số điện thoại, "
            "địa chỉ, CCCD, mã OTP; đặt chế độ riêng tư cho tài khoản.",
            "**Mật khẩu:** dùng cụm mật khẩu dài (≥12 kí tự, có chữ hoa, số, kí hiệu), "
            "**không dùng lại** mật khẩu, bật **xác thực 2 yếu tố (2FA)**.",
            "**Thiết bị:** giữ máy không nhiễm phần mềm gián điệp, cập nhật hệ điều hành, "
            "chỉ cài app từ chợ chính thức, kiểm tra quyền ứng dụng (camera, micro, vị trí).",
            "**Mạng:** cẩn trọng với **Wi-Fi công cộng** (tránh nhập mật khẩu ngân hàng), "
            "kiểm tra địa chỉ web có `https://` và đúng tên miền.",
            "**Dữ liệu:** sao lưu định kì (ổ cứng ngoài + đám mây), xoá sạch dữ liệu trước khi "
            "bán/cho thiết bị.",
            "**Ứng xử:** kiểm tra nguồn tin trước khi tin/chia sẻ; nghỉ giải lao, đặt giới hạn "
            "thời gian dùng mạng để tránh nghiện.",
        ], "memory"),

        H3("3.2.5. Ghi nhớ nhanh B2"),
        BOX("B2 trong 6 dòng", [
            "1. Web là **dịch vụ** trên Internet; URL là địa chỉ; HTTPS là bản có mã hoá.",
            "2. 5 bước kiểm tra nguồn tin: **Ai – Khi nào – Ở đâu – Để làm gì – Đối chiếu**.",
            "3. Học liệu mở dùng được miễn phí **nhưng vẫn phải ghi nguồn**.",
            "4. Dịch tự động: **ngôn ngữ nguồn → ngôn ngữ đích**; nhập bằng gõ/nói/tệp; luôn rà soát.",
            "5. 4 tên trộm số: **Virus – Worm – Trojan – Spyware**; phòng bằng Defender + 6 thói quen.",
            "6. **4 KHÔNG – 3 CÓ** để tự bảo vệ bản thân và dữ liệu cá nhân.",
        ], "memory"),
        PB(),
    ]
    return B
