# -*- coding: utf-8 -*-
"""Phần 6 – Đề thi thử 45 phút đúng cấu trúc ma trận (có đáp án chi tiết)."""
from .blocks import H1, H2, H3, P, LEAD, TBL, BOX, PB, SP, MCQ, TFQ, FRQ

MCQS = [
    MCQ("Câu 1", "Ưu điểm nào sau đây **KHÔNG** phải là sự ưu việt của việc lưu trữ thông tin "
        "trên thiết bị số?",
        ["Dung lượng lớn với giá thành rẻ", "Sao chép nhiều lần không làm giảm chất lượng",
         "Tìm kiếm và truy xuất rất nhanh", "Dữ liệu bị mòn dần sau mỗi lần đọc"],
        "D", "Thiết bị số lưu dữ liệu dưới dạng bit: đọc – sao chép không làm hao mòn dữ liệu. "
             "Đây là ưu điểm so với giấy, băng từ.", "A1 · Nhận biết"),
    MCQ("Câu 2", "Trong máy tính, **dữ liệu** được hiểu là gì?",
        ["Ý nghĩa mà con người rút ra được", "Thông tin đã được đưa vào máy tính dưới dạng kí hiệu "
         "để máy nhận biết và xử lí được", "Kết luận cuối cùng của một bài toán",
         "Một loại thiết bị đầu ra"],
        "B", "Dữ liệu là vật mang (số, chữ, bit); thông tin là ý nghĩa con người hiểu được.",
        "A1 · Nhận biết"),
    MCQ("Câu 3", "Việc ngân hàng dùng phần mềm quản lí tài khoản và giao dịch của khách hàng "
        "minh hoạ cho đóng góp nào của tin học?",
        ["Quản lí", "Tự động hoá", "Giải quyết bài toán khoa học – kĩ thuật", "Giao tiếp cộng đồng"],
        "A", "Quản lí nghiệp vụ nhanh, chính xác, tiết kiệm là một trong 5 đóng góp cơ bản của tin học.",
        "A2 · Nhận biết"),
    MCQ("Câu 4", "Nhóm nào sau đây gồm **toàn** thiết bị số thông dụng khác ngoài máy tính để bàn "
        "và laptop?",
        ["Bàn phím, chuột, màn hình", "Bảng đen, phấn, sách giáo khoa",
         "Điện thoại thông minh, đồng hồ thông minh, smart TV", "Bút bi, thước kẻ, giá sách"],
        "C", "Điện thoại, đồng hồ thông minh, smart TV đều là thiết bị số có khả năng xử lí và "
             "kết nối dữ liệu.", "A2 · Nhận biết"),
    MCQ("Câu 5", "Theo SGK Kết nối tri thức, mốc năm nào gắn với việc bộ giao thức **TCP/IP** "
        "trở thành nền tảng kết nối Internet?",
        ["1957", "1971", "1983", "1992"], "C",
        "Năm 1983: TCP/IP được dùng cho Internet; 1957 là FORTRAN, 1971 là Intel 4004, "
        "1992 là World Wide Web.", "A2 · Nhận biết"),
    MCQ("Câu 6", "Thành tựu nào gắn với mốc **1992** theo SGK Tin học 10 (Kết nối tri thức)?",
        ["Ngôn ngữ FORTRAN", "Bộ vi xử lí Intel 4004", "Giao thức TCP/IP", "World Wide Web"],
        "D", "World Wide Web giúp truy cập Internet dễ dàng và nhất quán, làm Internet phổ biến.",
        "A2 · Nhận biết"),
    MCQ("Câu 7", "Dịch vụ nào sau đây là ví dụ điển hình của **SaaS** (phần mềm như là dịch vụ)?",
        ["Thuê máy chủ ảo để cài hệ điều hành", "Google Docs dùng trực tiếp trên trình duyệt",
         "Thuê nền tảng bản đồ để phát triển ứng dụng", "Mua ổ cứng gắn ngoài"],
        "B", "SaaS cho thuê phần mềm ứng dụng; IaaS là máy chủ, PaaS là nền tảng phát triển.",
        "B1 · Nhận biết"),
    MCQ("Câu 8", "**Internet vạn vật (IoT)** là gì?",
        ["Mạng cục bộ chỉ dùng trong một gia đình", "Một giao thức mã hoá dữ liệu",
         "Việc liên kết các thiết bị thông minh để tự động thu thập, trao đổi và xử lí dữ liệu",
         "Một dạng virus máy tính lây qua mạng"],
        "C", "IoT kết nối thiết bị thông minh để tự động thu thập – trao đổi – xử lí dữ liệu.",
        "B1 · Nhận biết"),
    MCQ("Câu 9", "Dịch vụ nào sau đây **không** phải là dịch vụ điện toán đám mây?",
        ["Google Drive", "Gmail", "Zoom", "Ổ cứng USB cắm trực tiếp vào máy tính"],
        "D", "Đám mây là chia sẻ tài nguyên **qua Internet**; ổ cứng USB là thiết bị lưu trữ cục bộ.",
        "B1 · Nhận biết"),
    MCQ("Câu 10", "Xét theo phạm vi địa lí, loại mạng nào có quy mô **lớn nhất**?",
        ["PAN", "LAN", "MAN", "WAN"], "D",
        "PAN (vài mét) < LAN (nhà/trường) < MAN (thành phố) < WAN (toàn cầu). Internet là WAN lớn nhất.",
        "B1 · Nhận biết"),
    MCQ("Câu 11", "Loại mã độc nào là **đoạn mã** không phải phần mềm hoàn chỉnh, chỉ phát tác "
        "khi gắn vào một chương trình/tệp khác?",
        ["Worm (sâu máy tính)", "Virus", "Trojan", "Ransomware"], "B",
        "Virus cần vật chủ; worm là phần mềm hoàn chỉnh tự lây qua lỗ hổng bảo mật.",
        "B2 · Nhận biết"),
    MCQ("Câu 12", "Cách xử lí **đúng** khi bị bắt nạt trên mạng là:",
        ["Lập tức đáp trả gay gắt để “răn đe”", "Xoá hết tin nhắn rồi im lặng một mình",
         "Không trả lời, lưu bằng chứng, chặn/báo cáo và chia sẻ với bố mẹ hoặc thầy cô",
         "Kết bạn với nhiều người lạ để nhờ can thiệp"],
        "C", "Theo SGK: không trả lời kẻ bắt nạt, lưu bằng chứng, chia sẻ với người lớn, "
             "báo cơ quan chức năng khi nghiêm trọng.", "B2 · Nhận biết"),
    MCQ("Câu 13", "Đâu **không** phải là nguy cơ khi tham gia Internet thiếu hiểu biết?",
        ["Lộ thông tin cá nhân", "Bị lừa đảo qua mạng", "Bắt nạt trên mạng",
         "Tốc độ tính toán của CPU tăng lên"],
        "D", "5 nguy cơ theo SGK: tin giả/tin phản văn hoá, lừa đảo, lộ thông tin, bắt nạt, nghiện mạng.",
        "B2 · Nhận biết"),
    MCQ("Câu 14", "Công cụ nào sau đây dùng để **ngăn ngừa và loại bỏ phần mềm độc hại** trên Windows?",
        ["Google Translate", "Windows Defender", "Google Docs", "File Manager"],
        "B", "Windows Defender có các chế độ quét nhanh, quét toàn bộ, quét tuỳ chọn, quét ngoại tuyến.",
        "B2 · Nhận biết"),
    MCQ("Câu 15", "Hành vi nào sau đây là vấn đề về **đạo đức, pháp luật, văn hoá** khi giao tiếp "
        "qua mạng trở nên phổ biến?",
        ["Ghi rõ nguồn ảnh trong bài thuyết trình", "Kiểm tra thông tin trước khi chia sẻ",
         "Đăng ảnh bạn học đang ngủ gật kèm lời chế giễu", "Đặt mật khẩu mạnh cho tài khoản"],
        "C", "Hành vi này vừa công bố hình ảnh cá nhân trái phép, vừa bắt nạt và thiếu văn hoá.",
        "D1 · Nhận biết"),
    MCQ("Câu 16", "Văn bản pháp luật nào được ban hành năm **2018**, liên quan trực tiếp đến "
        "an ninh quốc gia trên không gian mạng?",
        ["Luật Giao dịch điện tử", "Luật Công nghệ thông tin", "Luật An ninh mạng",
         "Nghị định 90/2008/NĐ-CP"],
        "C", "Luật An ninh mạng 2018; Luật CNTT là năm 2006, Luật Giao dịch điện tử là 2005.",
        "D1 · Nhận biết"),
    MCQ("Câu 17", "Trong ví dụ về biến đổi khí hậu, phát biểu nào **đúng**?",
        ["Các con số nhiệt độ là thông tin, kết luận “Trái Đất ấm dần lên” là dữ liệu",
         "Các con số nhiệt độ là dữ liệu, kết luận rút ra được là thông tin",
         "Cả hai đều là dữ liệu", "Cả hai đều là thông tin"],
        "B", "Dữ liệu là nguyên liệu (con số); thông tin là ý nghĩa sau khi xử lí và giải thích.",
        "A1 · Thông hiểu"),
    MCQ("Câu 18", "Phát biểu nào **đúng** về mối quan hệ giữa dữ liệu và thông tin?",
        ["Một thông tin chỉ có thể biểu diễn bằng đúng một loại dữ liệu",
         "Dữ liệu không đầy đủ vẫn luôn xác định chính xác thông tin",
         "Cùng một bộ dữ liệu, cách xử lí khác nhau có thể cho thông tin khác nhau",
         "Dữ liệu và thông tin luôn đồng nhất với nhau"],
        "C", "Đây là một trong 4 mối quan hệ “độc lập tương đối” giữa dữ liệu và thông tin.",
        "A1 · Thông hiểu"),
    MCQ("Câu 19", "Trường hợp nào sau đây **không** vi phạm bản quyền?",
        ["Tải và cài phần mềm bẻ khoá (crack)",
         "Dùng ảnh có giấy phép CC BY, ghi rõ tên tác giả, nguồn và giấy phép",
         "Đăng nguyên bài viết của người khác lên blog mà không ghi nguồn",
         "Chép bài làm của bạn rồi nộp cho giáo viên"],
        "B", "Ảnh có giấy phép mở được phép dùng với điều kiện ghi nhận tác giả – đã được đáp ứng.",
        "D1 · Thông hiểu"),
    MCQ("Câu 20", "Phát biểu nào **đúng** về quyền tác giả?",
        ["Chỉ phát sinh sau khi đăng kí tại cơ quan nhà nước",
         "Phát sinh từ khi tác phẩm được sáng tạo và thể hiện dưới hình thức vật chất nhất định",
         "Chỉ bảo vệ phần mềm máy tính", "Chỉ gồm quyền tài sản, không có quyền nhân thân"],
        "B", "Quyền tác giả gồm quyền nhân thân và quyền tài sản; không cần đăng kí để phát sinh.",
        "D1 · Thông hiểu"),
]

TFS = [
    TFQ("Câu 1", "Chủ đề A2 – Thiết bị thông minh và Cách mạng công nghiệp 4.0. "
        "Hãy xác định mỗi ý sau là **Đúng** hay **Sai**.",
        [("a", "Thiết bị thông minh là thiết bị điện tử có thể hoạt động tự chủ, tự thích ứng "
               "với hoàn cảnh và kết nối với thiết bị khác để trao đổi dữ liệu.", "Thông hiểu"),
         ("b", "Chỉ những thiết bị có màn hình cảm ứng mới được coi là thiết bị thông minh.", "Thông hiểu"),
         ("c", "Trong nông nghiệp thông minh, cảm biến độ ẩm gửi dữ liệu qua mạng về bộ xử lí "
               "và hệ thống có thể tự bật tưới khi đất khô.", "Vận dụng"),
         ("d", "Khi áp dụng IoT, mọi quyết định vẫn phải do con người trực tiếp thực hiện "
               "nên doanh nghiệp không tiết kiệm được chi phí lao động.", "Vận dụng")],
        ["Đ", "S", "Đ", "S"],
        "a **Đúng** – đó là định nghĩa thiết bị thông minh. b **Sai** – nhiều thiết bị thông minh "
        "không có màn hình (cảm biến độ ẩm, camera an ninh, khoá vân tay). c **Đúng** – đúng chuỗi "
        "IoT: cảm biến → mạng → xử lí → cơ cấu chấp hành. d **Sai** – IoT hoạt động tự động, "
        "liên tục nên **giảm** chi phí lao động, một trong 3 lợi ích của IoT theo SGK."),
    TFQ("Câu 2", "Chủ đề B1 – Mạng máy tính, điện toán đám mây và IoT. "
        "Hãy xác định mỗi ý sau là **Đúng** hay **Sai**.",
        [("a", "LAN là mạng cục bộ thuộc sở hữu của một cá nhân/gia đình/cơ quan, trong khi "
               "Internet là mạng diện rộng không thuộc sở hữu riêng của ai.", "Thông hiểu"),
         ("b", "Vì Internet có quy mô toàn cầu nên tốc độ truy cập Internet luôn nhanh hơn "
               "và ổn định hơn mạng LAN.", "Thông hiểu"),
         ("c", "Google Docs là ví dụ của SaaS, còn việc thuê máy chủ ảo để lưu trữ dữ liệu "
               "là ví dụ của IaaS.", "Vận dụng"),
         ("d", "Để xây dựng hệ thống thu phí không dừng, chỉ cần lắp camera ở trạm thu phí là đủ, "
               "không cần đường truyền mạng.", "Vận dụng")],
        ["Đ", "S", "Đ", "S"],
        "a **Đúng** – đúng nội dung so sánh LAN và Internet. b **Sai** – tốc độ phụ thuộc đường truyền, "
        "ISP và khoảng cách; LAN thường có độ trễ thấp hơn. c **Đúng** – IaaS là hạ tầng, SaaS là "
        "phần mềm ứng dụng. d **Sai** – IoT bắt buộc phải có mạng truyền dẫn để gửi dữ liệu "
        "từ thiết bị tới nơi xử lí."),
]

FRQS = [
    FRQ("Câu 1", "Em hãy: (a) nêu ít nhất **4 nguy cơ** khi tham gia các hoạt động trên Internet "
        "một cách bất cẩn, thiếu hiểu biết; (b) trình bày **4 biện pháp đề phòng** tương ứng; "
        "(c) chỉ ra **3 việc làm cụ thể** để tự bảo vệ dữ liệu cá nhân.",
        "Thông hiểu · B2 · 1,0 điểm",
        ["**(a) 0,3 điểm** – nêu được ít nhất 4/5 nguy cơ: tin giả và tin phản văn hoá; lừa đảo "
         "(phishing); lộ thông tin cá nhân; bắt nạt trên mạng; nghiện mạng/game.",
         "**(b) 0,4 điểm** – mỗi biện pháp 0,1 điểm: kiểm tra nguồn tin trước khi tin/chia sẻ; "
         "không mở liên kết, tệp đính kèm lạ; cài và cập nhật phần mềm chống mã độc; "
         "không kết bạn dễ dãi, lưu bằng chứng và báo người lớn khi bị bắt nạt; "
         "đặt giới hạn thời gian dùng mạng; cẩn trọng với Wi-Fi công cộng.",
         "**(c) 0,3 điểm** – mỗi việc 0,1 điểm: mật khẩu mạnh + xác thực 2 yếu tố, không chia sẻ "
         "mã OTP; cài đặt riêng tư và không đăng thông tin nhạy cảm; kiểm tra quyền ứng dụng, "
         "cập nhật hệ điều hành, sao lưu dữ liệu định kì.",
         "*Cộng tối đa 1,0 điểm. Học sinh có thể diễn đạt khác nhưng đúng ý vẫn được điểm.*"]),
    FRQ("Câu 2", "Một nhóm học sinh có tệp video `on_tap.mp4` dung lượng **1,5 GB**. Hãy: "
        "(a) đổi dung lượng tệp sang MB và KB; (b) tính số ảnh 3 MB có thể chứa trong một thẻ nhớ "
        "**6 GB**; (c) mô tả ngắn gọn quá trình **xử lí và truyền** tệp ảnh từ điện thoại của em "
        "tới máy của bạn qua mạng.",
        "Vận dụng · A1 · 1,0 điểm",
        ["**(a) 0,35 điểm** – 1,5 GB = 1,5 × 1024 = **1536 MB**; 1536 × 1024 = **1 572 864 KB**. "
         "(Nếu học sinh dùng 1000 nhưng có giải thích quy ước riêng, giáo viên cân nhắc.)",
         "**(b) 0,3 điểm** – 6 GB = 6 × 1024 = 6144 MB; 6144 ÷ 3 = **2048 ảnh**.",
         "**(c) 0,35 điểm** – nêu đúng trình tự: camera/nguồn tạo dữ liệu → mã hoá, nén thành tệp "
         "`.jpg` → lưu vào bộ nhớ → ứng dụng chia thành gói tin và truyền qua Wi-Fi/4G (có địa chỉ "
         "người nhận) → máy bạn nhận, giải mã và hiển thị (dữ liệu trở thành thông tin). "
         "Có thể nói thêm: nén ảnh giúp giảm dung lượng và thời gian truyền.",
         "*Lưu ý: phải ghi rõ đơn vị ở từng bước; sai 1 bậc đổi đơn vị trừ 0,1 điểm.*"]),
    FRQ("Câu 3", "**Tình huống:** Bạn Minh lập một trang web có giao diện giống hệt trang web của "
        "một ngân hàng, gửi đường dẫn qua email cho nhiều người với nội dung “Đăng nhập ngay để "
        "nhận quà”. Khi người dùng nhập tên đăng nhập, mật khẩu và mã OTP, Minh lưu lại các thông "
        "tin đó. Ngoài ra, Minh còn đăng lên mạng bài viết của một tác giả khác mà không ghi nguồn. "
        "Em hãy vận dụng các quy định pháp luật đã học để: (a) xác định tính hợp pháp của từng "
        "hành vi; (b) chỉ ra văn bản pháp luật/nhóm hành vi bị cấm tương ứng; (c) nêu hậu quả và "
        "đề xuất cách xử lí.",
        "Vận dụng cao · D1 · 1,0 điểm",
        ["**(a) 0,25 điểm** – kết luận rõ ràng: cả 3 hành vi (giả mạo trang web ngân hàng, "
         "thu thập mật khẩu/OTP trái phép, đăng lại bài viết không ghi nguồn) đều **không hợp pháp**, "
         "đồng thời vi phạm đạo đức và văn hoá ứng xử số.",
         "**(b) 0,3 điểm** – đối chiếu được: Luật Công nghệ thông tin 2006, Điều 12 cấm giả mạo "
         "trang thông tin điện tử của tổ chức/cá nhân khác, cấm xâm phạm quyền sở hữu trí tuệ; "
         "Nghị định 72/2013/NĐ-CP quy định quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin "
         "trên mạng; Luật An ninh mạng 2018, Điều 8 liên quan hành vi lừa đảo, chiếm đoạt thông tin "
         "trên không gian mạng; quy định về quyền tác giả đối với bài viết đăng lại.",
         "**(c) 0,3 điểm** – hậu quả: người dùng mất tiền/tài khoản, lộ thông tin cá nhân; "
         "tác giả mất quyền lợi; Minh có thể bị xử phạt hành chính, bồi thường dân sự, thậm chí "
         "truy cứu trách nhiệm hình sự. Đề xuất: gỡ trang web giả và bài viết vi phạm, dừng thu thập "
         "và xoá dữ liệu đã lấy, thông báo cho ngân hàng và người bị ảnh hưởng, ghi nguồn/xin phép "
         "tác giả, báo cơ quan chức năng.",
         "**(d) 0,15 điểm** – trình bày theo khung 5 bước rõ ràng, có lí lẽ và ví dụ; khuyến khích "
         "nêu thêm biện pháp phòng tránh cho người dùng (kiểm tra tên miền, `https://`, không chia sẻ OTP)."]),
]

ANSWER_KEY = [
    ("1", "D"), ("2", "B"), ("3", "A"), ("4", "C"), ("5", "C"),
    ("6", "D"), ("7", "B"), ("8", "C"), ("9", "D"), ("10", "D"),
    ("11", "B"), ("12", "C"), ("13", "D"), ("14", "B"), ("15", "C"),
    ("16", "C"), ("17", "B"), ("18", "C"), ("19", "B"), ("20", "B"),
]


def blocks():
    B = [
        H1("PHẦN 6 · ĐỀ THI THỬ GIỮA KÌ I (45 PHÚT) VÀ ĐÁP ÁN CHI TIẾT"),
        LEAD("Đề thi thử được biên soạn **đúng cấu trúc ma trận gốc**: 20 câu trắc nghiệm 4 lựa chọn "
             "(16 Nhận biết + 4 Thông hiểu), 2 câu đúng/sai (mỗi câu 4 ý, gồm 2 ý Thông hiểu + "
             "2 ý Vận dụng) và 3 câu tự luận (Thông hiểu – Vận dụng – Vận dụng cao). "
             "Phần đáp án có giải thích ngay sau mỗi câu."),
        BOX("Hướng dẫn làm bài", [
            "**Thời gian 45 phút.** Gợi ý phân bổ: 20 phút cho trắc nghiệm, 8 phút cho đúng/sai, "
            "15 phút cho tự luận, 2 phút rà soát.",
            "Câu đúng/sai: mỗi ý là một nhận định độc lập; hãy gạch chân từ khoá phủ định "
            "(“chỉ”, “luôn”, “không cần”) trước khi quyết định.",
            "Tự luận: luôn trình bày theo **thứ tự câu hỏi** và ghi rõ đơn vị/công thức ở mỗi bước.",
        ], "tip"),

        H2("6.1. PHẦN I – TRẮC NGHIỆM KHÁCH QUAN (7,0 điểm)"),
        H3("A. 20 câu trắc nghiệm 4 lựa chọn (mỗi câu 0,25 điểm)"),
    ]
    for m in MCQS:
        B.append(m)
    B += [
        H3("B. 2 câu lựa chọn đúng/sai (mỗi câu 1,0 điểm – mỗi ý 0,25 điểm)"),
    ]
    for q in TFS:
        B.append(q)
    B += [
        H2("6.2. PHẦN II – TỰ LUẬN (3,0 điểm)"),
    ]
    for q in FRQS:
        B.append(q)

    # --------------------------------------------------------------- đáp án
    B += [
        PB(hard=True),
        H1("ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM ĐỀ THI THỬ"),
        H2("Đáp án nhanh"),
        TBL(["Câu"] + [n for n, _ in ANSWER_KEY[:10]],
             [["Đáp án"] + [a for _, a in ANSWER_KEY[:10]]],
             widths=[52] + [46] * 10, fs=8.5, zebra=False, align="center"),
        TBL(["Câu"] + [n for n, _ in ANSWER_KEY[10:]],
             [["Đáp án"] + [a for _, a in ANSWER_KEY[10:]]],
             widths=[52] + [46] * 10, fs=8.5, zebra=False, align="center"),
        P("**Câu đúng/sai:** Câu 1 → **a. Đ · b. S · c. Đ · d. S**; "
          "Câu 2 → **a. Đ · b. S · c. Đ · d. S**. Giải thích chi tiết từng ý đã được trình bày "
          "ngay dưới mỗi câu ở mục 6.1B."),
        SP(4),
        H2("Giải thích chi tiết 20 câu trắc nghiệm"),
        TBL(["Câu", "ĐA", "Vì sao"],
            [[m["n"].replace("Câu ", ""), f"**{m['ans']}**", m["explain"]] for m in MCQS],
            widths=[36, 32, 443], fs=8.0,
            caption="Bảng 6.1 – Giải thích đáp án trắc nghiệm."),
        H2("Thang điểm 3 câu tự luận"),
        P("Thang điểm chi tiết đã được trình bày trong khung **“Hướng dẫn chấm”** ngay dưới mỗi câu "
          "tự luận ở mục 6.2 (mỗi câu 1,0 điểm, chia theo các ý a, b, c, d). "
          "Học sinh đạt tối đa khi: (1) trả lời đủ ý, (2) có ví dụ hoặc số liệu cụ thể, "
          "(3) dùng đúng thuật ngữ Tin học và (4) trình bày theo trình tự logic."),
        BOX("Sau khi chấm xong", [
            "Với mỗi câu sai, hãy ghi lại **từ khoá** bạn đã nhầm rồi quay lại mục tương ứng: "
            "A1 → 2.1, A2 → 2.2, A3 → 2.3, B1 → 3.1, B2 → 3.2, D1 → Phần 4.",
            "Nếu sai từ 3 câu Nhận biết trở lên, hãy ôn lại **Bảng 1.2 (6 móc nhớ)** và "
            "**Bảng 5.1 (35 yêu cầu)** trước khi làm lại đề.",
        ], "tip"),
        PB(),
    ]
    return B
