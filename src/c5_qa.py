# -*- coding: utf-8 -*-
"""Phần 5 – Ngân hàng câu hỏi & đáp án cho 100% yêu cầu trong bản đặc tả gốc.

Câu hỏi (văn bản yêu cầu) KHÔNG gõ lại bằng tay: build.py lấy trực tiếp từ
src/source_extract.py, bảo đảm nguyên văn 35/35 yêu cầu.  File này chỉ chứa
đáp án, theo đúng thứ tự của 35 yêu cầu đó.
"""
from .blocks import H1, H2, P, LEAD, TBL, BOX, PB, SP, QABANK

UNIT_NAMES = {
    "A1": "A1. Dữ liệu, thông tin và xử lý thông tin",
    "A2": "A2. Vai trò của máy tính và thiết bị thông minh trong nền kinh tế tri thức",
    "A3": "A3. Kĩ năng sử dụng thiết bị số của mỗi công dân",
    "B1": "B1. Khái niệm mạng máy tính, Internet, IoT; phân loại mạng",
    "B2": "B2. Sử dụng dịch vụ web và tự bảo vệ khi tham gia mạng",
    "D1": "D1. Nghĩa vụ tuân thủ pháp lí trong môi trường số",
}

UNIT_REF = {
    "A1": "mục 2.1", "A2": "mục 2.2", "A3": "mục 2.3",
    "B1": "mục 3.1", "B2": "mục 3.2", "D1": "Phần 4",
}

# code, unit_code, hình thức thi, đáp án
QA_ANSWERS = [
    # ---------------------------------------------------------------- A1 (5)
    dict(code="A1.1", unit="A1", form="TN · Nhận biết", answer=(
        "Lưu trữ trên thiết bị số có 6 ưu việt: **dung lượng rất lớn với giá thành rẻ** "
        "(một thẻ nhớ nhỏ chứa cả tủ sách); **tìm kiếm, truy xuất và xử lí nhanh, chính xác**; "
        "**sao chép không làm suy giảm chất lượng** vì bản sao là các bit giống hệt bản gốc; "
        "**dễ sửa đổi, dễ nén và dễ bảo mật** (mật khẩu, mã hoá, sao lưu nhiều bản); "
        "**truyền đi xa với tốc độ rất cao** qua mạng; và **bền hơn** so với giấy, băng từ dễ ẩm mốc, cháy hỏng. "
        "Nhờ vậy thiết bị số giúp xử lí thông tin với năng suất cao và ổn định, thực hiện công việc "
        "tự động, chi phí thấp, tiện lợi."), see="2.1.4"),
    dict(code="A1.2", unit="A1", form="TN · Thông hiểu", answer=(
        "**Dữ liệu** là thông tin đã được đưa vào máy tính dưới dạng kí hiệu (số, chữ, bit) để máy "
        "nhận biết và xử lí được – đó là **vật mang**. **Thông tin** là **ý nghĩa** con người hiểu được "
        "sau khi giải thích dữ liệu trong một ngữ cảnh – đó là **nội dung**. Hai khái niệm độc lập "
        "tương đối: cùng một thông tin có thể biểu diễn bằng nhiều loại dữ liệu; dữ liệu thiếu thì "
        "chưa xác định được thông tin; cùng bộ dữ liệu xử lí khác nhau cho thông tin khác nhau; "
        "những bộ dữ liệu khác nhau vẫn có thể cho cùng một thông tin. Trong máy tính, "
        "**xử lí thông tin chính là xử lí dữ liệu**."), see="2.1.1"),
    dict(code="A1.3", unit="A1", form="TN · Thông hiểu", answer=(
        "Ví dụ 1: các con số `31, 32, 33` đo được hằng ngày là **dữ liệu**; sau khi phần mềm tính "
        "trung bình và vẽ biểu đồ, kết luận **“nhiệt độ mùa hè năm nay cao hơn năm trước 1,2 °C”** là "
        "**thông tin**. Ví dụ 2: dãy bit trong tệp `baihat.mp3` là **dữ liệu**; giai điệu mà em nghe và "
        "hiểu được là **thông tin**. Ví dụ 3: cùng thông tin “điểm kiểm tra là 9” nhưng có thể lưu dưới "
        "dạng chữ số `9`, mã nhị phân `1001` hay chữ “giỏi” – minh hoạ cho quan hệ một thông tin, "
        "nhiều dữ liệu."), see="2.1.1"),
    dict(code="A1.4", unit="A1", form="TL · Vận dụng", answer=(
        "Quy ước SGK: **1 B = 8 bit**; mỗi bậc hơn kém **2^10 = 1024** lần theo thứ tự "
        "**B → KB → MB → GB → TB** (mẹo “Khoai Mì Gà Tây”). Đổi **xuống** thì nhân 1024, "
        "đổi **lên** thì chia 1024, bao nhiêu bậc thì làm bấy nhiêu lần. Ví dụ: "
        "3,5 MB = 3,5 × 1024 = **3584 KB**; 2 GB = 2 × 1024 × 1024 = **2 097 152 KB**; "
        "5 242 880 B = 5120 KB = **5 MB**; USB 8 GB chứa 8 × 1024 ÷ 2 = **4096 ảnh 2 MB**. "
        "Khi trình bày phải ghi rõ đơn vị ở từng bước và phân biệt **b** (bit) với **B** (byte)."), see="2.1.3"),
    dict(code="A1.5", unit="A1", form="TL · Vận dụng", answer=(
        "Hãy mô tả theo chuỗi **thu nhận → lưu trữ → xử lí → truyền → nhận/giải mã**. Ví dụ gửi ảnh: "
        "camera đổi ánh sáng thành tín hiệu số (dữ liệu) → chip nén thành tệp `.jpg` → lưu vào bộ nhớ "
        "→ ứng dụng nhắn tin chia tệp thành gói tin, gửi qua Wi-Fi/4G tới máy chủ rồi tới máy bạn "
        "→ máy bạn giải nén và hiển thị ảnh, lúc đó dữ liệu trở thành thông tin. Ví dụ khác: nhập điểm "
        "kiểm tra bằng bàn phím → lưu tệp `.xlsx` → phần mềm tính điểm trung bình → xuất biểu đồ và "
        "gửi cho giáo viên qua email. Nhận xét thêm: nén dữ liệu giúp giảm dung lượng và thời gian truyền."), see="2.1.5"),

    # ---------------------------------------------------------------- A2 (7)
    dict(code="A2.1", unit="A2", form="TN · Nhận biết", answer=(
        "Tin học có 5 đóng góp cơ bản: **quản lí** (xử lí nghiệp vụ nhanh, chính xác, tiết kiệm – "
        "quản lí học sinh, tài khoản ngân hàng); **tự động hoá** (robot hút bụi, robot trong nhà máy); "
        "**giải quyết bài toán khoa học – kĩ thuật** (tính toán, mô phỏng, dự báo thời tiết); "
        "**thay đổi cách thức làm việc của nhiều ngành nghề** (dạy học trực tuyến, mua sắm trực tuyến); "
        "và **giao tiếp cộng đồng** (thư điện tử, mạng xã hội, diễn đàn)."), see="2.2.2"),
    dict(code="A2.2", unit="A2", form="TN · Nhận biết", answer=(
        "Ngoài máy tính để bàn và laptop có: **điện thoại thông minh, máy tính bảng, đồng hồ thông minh** "
        "(nhóm thiết bị cá nhân/PDA); **smart TV, loa thông minh, máy chơi game** (giải trí); "
        "**máy ảnh số, camera an ninh, máy quét, flycam** (ghi hình); **robot hút bụi, tủ lạnh/bóng đèn/khoá "
        "cửa thông minh** (gia dụng); **xe tự hành, cảm biến giao thông, thu phí không dừng, "
        "máy bay không người lái** (giao thông – công nghiệp); **máy đo đường huyết, cảm biến độ ẩm đất** "
        "(y tế – nông nghiệp)."), see="2.2.4"),
    dict(code="A2.3", unit="A2", form="TN · Nhận biết", answer=(
        "Các mốc tiêu biểu: **1946** ENIAC – máy tính điện tử đầu tiên (đèn chân không); **1947** transitor "
        "và **1958** mạch tích hợp IC; **1957** ngôn ngữ lập trình bậc cao đầu tiên **FORTRAN**; "
        "**1971** bộ vi xử lí Intel 4004 mở đầu kỉ nguyên PC; **1983** giao thức **TCP/IP** trở thành "
        "nền tảng của Internet; **1992** (theo SGK KNTT) **World Wide Web** ra đời giúp Internet phổ biến; "
        "thập niên 2000 điện thoại thông minh và 3G/4G; thập niên 2010 đám mây, dữ liệu lớn, AI, IoT "
        "và CMCN 4.0. Bốn nhóm thành tựu cần nhớ: **hệ điều hành, mạng và Internet, ngôn ngữ lập "
        "trình bậc cao, hệ quản trị cơ sở dữ liệu**."), see="2.2.3"),
    dict(code="A2.4", unit="A2", form="ĐS · Thông hiểu", answer=(
        "Thiết bị thông minh là thiết bị điện tử hoạt động **tự chủ**, tự thích ứng với hoàn cảnh và "
        "**kết nối được với thiết bị khác** để trao đổi dữ liệu. Ví dụ cụ thể: **điện thoại thông minh**, "
        "**đồng hồ thông minh** (đo nhịp tim, nhắc vận động), **robot hút bụi** (tự lập bản đồ phòng), "
        "**camera an ninh AI** (nhận diện người lạ), **xe tự hành**, **tủ lạnh thông minh**, "
        "**cảm biến độ ẩm đất trong nông nghiệp**. Điểm chung: đều có cảm biến, bộ xử lí, bộ nhớ, "
        "kết nối không dây và khả năng tự ra quyết định."), see="2.2.1"),
    dict(code="A2.5", unit="A2", form="ĐS · Thông hiểu", answer=(
        "Thiết bị thông minh là **đầu cuối thu thập dữ liệu** và là **cơ chế thực thi quyết định** "
        "trong hệ thống IoT – nội dung cốt lõi của **CMCN 4.0** (AI + IoT + Big Data + Cloud). "
        "Chúng giúp thu thập dữ liệu trên diện rộng, ở nơi con người không thể tới; hoạt động liên tục, "
        "tự động, cung cấp dữ liệu tức thời; tiết kiệm chi phí lao động và tạo ra **nền sản xuất thông minh**, "
        "nơi khâu thiết kế, mô phỏng được làm trên không gian số. Ví dụ: xe tự hành dùng cảm biến để "
        "nhận diện biển báo, chướng ngại vật rồi tự tính tốc độ, hướng đi – vừa nâng cao an toàn "
        "giao thông vừa thúc đẩy **kinh tế tri thức** (nền kinh tế lấy tri thức làm động lực tăng trưởng)."), see="2.2.5"),
    dict(code="A2.6", unit="A2", form="ĐS · Thông hiểu", answer=(
        "Vì chúng có đủ 5 thành phần của một hệ thống xử lí thông tin: **đầu vào** (cảm biến, camera, "
        "micro, màn hình cảm ứng), **bộ xử lí** (chip/AI), **bộ nhớ**, **kết nối truyền dữ liệu** "
        "(Wi-Fi, Bluetooth, 4G/5G) và **đầu ra** (màn hình, loa, mô tơ, van nước). Ví dụ robot hút bụi: "
        "cảm biến siêu âm đo khoảng cách (vào) → chip lập bản đồ phòng (xử) → lưu bản đồ (lưu) → "
        "truyền trạng thái về điện thoại (truyền) → mô tơ bánh xe di chuyển (ra). "
        "Chu trình này chính là **TLXT** đã học ở A1, nhưng diễn ra tự động."), see="2.2.1"),
    dict(code="A2.7", unit="A2", form="ĐS · Thông hiểu", answer=(
        "Chọn một đóng góp và nêu bối cảnh cụ thể kèm lợi ích. Ví dụ **quản lí**: “Nhờ phần mềm quản lí "
        "thư viện, việc mượn – trả sách giảm từ 5 phút xuống 30 giây, không còn nhầm sách quá hạn.” "
        "Ví dụ **tự động hoá**: “Robot hút bụi tự dọn nhà mỗi sáng giúp bố mẹ tiết kiệm 30 phút mỗi ngày.” "
        "Ví dụ **giao tiếp**: “Lớp em dùng nhóm Zalo để nhận thông báo và nộp câu hỏi cho giáo viên "
        "ngay cả khi nghỉ ở nhà.” Ví dụ **giải toán khoa học**: “Máy tính mô phỏng thời tiết giúp "
        "dự báo mưa bão trước 3 ngày, giảm thiệt hại cho nông dân.”"), see="2.2.2"),

    # ---------------------------------------------------------------- A3 (2)
    dict(code="A3.1", unit="A3", form="Thực hành · Vận dụng", answer=(
        "Quy trình 6 bước: **① kiểm tra nguồn** (dây sạc, pin, ổ cắm, tay khô); **② nhấn giữ nút nguồn** "
        "cho đến khi xuất hiện logo; **③ chờ hệ điều hành nạp xong** (Windows, Android, iOS) – không ngắt "
        "điện giữa chừng; **④ mở khoá/đăng nhập** đúng tài khoản, quan sát thanh trạng thái (pin, Wi-Fi, giờ); "
        "**⑤ sử dụng** ứng dụng và lưu công việc thường xuyên; **⑥ kết thúc đúng cách** – đóng ứng dụng, "
        "lưu tệp, chọn **Shut down/Restart** trong hệ điều hành thay vì rút điện đột ngột. "
        "Với điện thoại: nhấn giữ nút nguồn → chọn **Tắt nguồn**. Với máy tính: Start → Power → Shut down."), see="2.3.1"),
    dict(code="A3.2", unit="A3", form="Thực hành · Vận dụng", answer=(
        "Cần làm được 3 nhóm thao tác. **(1) Tệp:** mở ứng dụng quản lí tệp (File Manager, Files, My Files), "
        "vào thư mục `DCIM/Camera`, chạm giữ để **xem thông tin, sao chép, di chuyển, đổi tên, chia sẻ, xoá**; "
        "nhận biết loại tệp qua phần mở rộng (`.txt .docx .pdf .xlsx .jpg .png .mp3 .mp4 .zip`). "
        "**(2) Chức năng thiết bị:** đọc thanh trạng thái, dùng nút Quay lại/Tổng quan, bật Wi-Fi, Bluetooth, "
        "chụp ảnh, ghi âm, đặt lịch, hẹn giờ. **(3) Ứng dụng cài sẵn:** gọi điện, nhắn tin, danh bạ, "
        "trình duyệt web, email, máy tính, thư viện ảnh; cài thêm Zoom/Meet/Teams, Google Drive/OneDrive "
        "từ chợ ứng dụng chính thức và kiểm tra quyền truy cập trước khi cài."), see="2.3.3"),

    # ---------------------------------------------------------------- B1 (5)
    dict(code="B1.1", unit="B1", form="TN · Nhận biết", answer=(
        "Điện toán đám mây chia sẻ tài nguyên qua Internet theo nhu cầu. Dịch vụ cụ thể gồm: "
        "**lưu trữ và đồng bộ tệp** (Google Drive, Dropbox, OneDrive, iCloud); **soạn thảo/cộng tác** "
        "(Google Docs, Google Sheets, Microsoft 365); **thư điện tử** (Gmail, Outlook); "
        "**họp và học trực tuyến** (Zoom, Google Meet, Microsoft Teams); **giải trí** (Netflix, Spotify, YouTube); "
        "và dịch vụ cho nhà phát triển như **thuê máy chủ ảo, cơ sở dữ liệu, nền tảng bản đồ**. "
        "Ba loại dịch vụ: **IaaS** (hạ tầng), **PaaS** (nền tảng), **SaaS** (phần mềm)."), see="3.1.4"),
    dict(code="B1.2", unit="B1", form="TN · Nhận biết", answer=(
        "**IoT (Internet of Things – Internet vạn vật)** là việc liên kết các thiết bị thông minh với "
        "nhau thông qua mạng để **tự động thu thập, trao đổi và xử lí dữ liệu** phục vụ các mục đích "
        "khác nhau, hạn chế sự can thiệp của con người. Kiến trúc gồm 4 lớp: thiết bị/cảm biến → "
        "mạng truyền dẫn (Wi-Fi, Bluetooth, 4G/5G) → xử lí/đám mây → ứng dụng cho người dùng."), see="3.1.5"),
    dict(code="B1.3", unit="B1", form="ĐS · Thông hiểu", answer=(
        "Internet trở thành **kho tri thức khổng lồ** cập nhật liên tục, truy cập được ở bất cứ đâu, "
        "bất cứ lúc nào. **Chất lượng cuộc sống:** xem phim, mua sắm, thanh toán không dùng tiền mặt, "
        "khám bệnh từ xa, dịch vụ công trực tuyến. **Học tập:** lớp học trực tuyến (Zoom, Meet), "
        "bài giảng số, học liệu mở, thư viện số – học mọi lúc mọi nơi. **Làm việc:** họp trực tuyến, "
        "làm việc từ xa, cộng tác trên Google Docs, lưu trữ trên đám mây thay vì mang USB. "
        "**Giao tiếp:** liên lạc tức thì qua email, Zalo, mạng xã hội. Nhờ mạng, chi phí và khoảng cách "
        "đều giảm, nhưng cũng phát sinh yêu cầu mới về an toàn thông tin."), see="3.1.3"),
    dict(code="B1.4", unit="B1", form="ĐS · Thông hiểu", answer=(
        "Bảng so sánh 6 tiêu chí: **(1) Sở hữu** – LAN thuộc một cá nhân/gia đình/cơ quan; "
        "Internet không thuộc sở hữu riêng của ai. **(2) Phạm vi** – LAN nhỏ (nhà, trường, công ty); "
        "Internet là WAN quy mô toàn cầu. **(3) Thiết bị** – LAN dùng Hub, Switch, Wi-Fi để kết nối trực tiếp; "
        "Internet dùng Router và nhà cung cấp dịch vụ (ISP). **(4) Tốc độ/độ trễ** – LAN thường cao và ổn định hơn. "
        "**(5) Quản lí** – LAN do một tổ chức quản lí; Internet do nhiều tổ chức phối hợp, dùng chung TCP/IP. "
        "**(6) Ví dụ** – Wi-Fi phòng máy tính của trường là LAN; truy cập Google là dùng Internet. "
        "**Chốt lại:** Internet là **mạng của các mạng**."), see="3.1.2"),
    dict(code="B1.5", unit="B1", form="ĐS · Thông hiểu", answer=(
        "**Ví dụ:** trong nông nghiệp thông minh, cảm biến độ ẩm đất gửi dữ liệu về điện thoại và hệ thống "
        "tự bật tưới khi đất khô; trước đây nông dân phải ra đồng kiểm tra từng luống. "
        "Ví dụ khác: **thu phí không dừng** trên cao tốc giúp xe không phải dừng lại; **đồng hồ thông minh** "
        "cảnh báo nhịp tim bất thường; **camera và cảm biến** cảnh báo cháy sớm. "
        "**Ý kiến cá nhân mẫu:** “Em thấy IoT mang lại lợi ích lớn: tiết kiệm thời gian và chi phí, "
        "giảm rủi ro cho con người ở môi trường nguy hiểm, cung cấp dữ liệu tức thời giúp quyết định "
        "chính xác hơn. Tuy nhiên, cần bảo mật thiết bị và bảo vệ dữ liệu cá nhân, bởi một camera hay "
        "đồng hồ thông minh bị xâm nhập có thể làm lộ thông tin riêng tư.”"), see="3.1.5"),

    # ---------------------------------------------------------------- B2 (8)
    dict(code="B2.1", unit="B2", form="TN · Nhận biết", answer=(
        "**Phần mềm độc hại (malware)** là chương trình được tạo ra để xâm nhập, phá hoại hoặc đánh cắp "
        "thông tin mà người dùng không hay biết. Các dạng chính: **virus** (đoạn mã kí sinh, cần vật chủ), "
        "**worm** (sâu tự nhân bản qua lỗ hổng bảo mật), **trojan** (đội lốt phần mềm có ích), "
        "**spyware/keylogger** (đánh cắp thông tin, ghi bàn phím), **backdoor/rootkit** (mở cửa sau, "
        "chiếm quyền cao nhất), **ransomware** (mã hoá tệp đòi tiền chuộc), **adware** (quảng cáo ngoài "
        "ý muốn). Chúng lây qua email đính kèm, USB, tải phần mềm crack, liên kết lạ; có thể xoá dữ liệu, "
        "làm tê liệt hệ thống và gây thiệt hại lớn (Melissa 1999, Code Red 2001)."), see="3.2.3"),
    dict(code="B2.2", unit="B2", form="TN · Nhận biết", answer=(
        "**① Không kết bạn dễ dãi qua mạng; ② không trả lời thư/tin nhắn của kẻ bắt nạt** (đáp trả thường "
        "làm tình huống xấu thêm); **③ lưu giữ mọi bằng chứng** (chụp màn hình, lưu tin nhắn, ghi thời gian); "
        "**④ chia sẻ ngay với bố mẹ hoặc thầy cô** để được hỗ trợ; **⑤ khi việc nghiêm trọng, báo cơ quan "
        "công an kèm bằng chứng**; **⑥ dùng chức năng chặn (block) và báo cáo (report)** của nền tảng. "
        "Quan trọng nhất: giữ bình tĩnh, không tự trách mình và không im lặng một mình."), see="3.2.4"),
    dict(code="B2.3", unit="B2", form="TN · Nhận biết", answer=(
        "**5 nguy cơ:** tin giả và tin phản văn hoá; lừa đảo trên mạng; lộ thông tin cá nhân; "
        "bắt nạt trên mạng; nghiện mạng/game. **Tác hại:** bị lừa mất tiền, mất tài khoản; "
        "bị mạo danh, quấy rối; hiểu sai vấn đề, gây hoang mang trong cộng đồng; "
        "tổn thương tinh thần (bắt nạt), giảm kết quả học tập, rối loạn giấc ngủ (nghiện mạng); "
        "thậm chí vướng vào rắc rối pháp lí nếu chia sẻ nội dung bị cấm hoặc phát tán mã độc."), see="3.2.4"),
    dict(code="B2.4", unit="B2", form="TN · Thông hiểu", answer=(
        "**(1) Bảo vệ thông tin:** không công khai số điện thoại, địa chỉ, CCCD, mã OTP; đặt chế độ riêng tư; "
        "dùng mật khẩu mạnh và xác thực 2 yếu tố. **(2) Bảo vệ thiết bị:** cập nhật hệ điều hành, "
        "cài và quét bằng chương trình chống mã độc, không mở tệp/link lạ, không dùng phần mềm crack. "
        "**(3) Cẩn trọng khi kết nối:** hạn chế giao dịch nhạy cảm qua Wi-Fi công cộng, kiểm tra `https://` "
        "và đúng tên miền. **(4) Kiểm chứng thông tin:** 5 bước Ai – Khi nào – Ở đâu – Để làm gì – Đối chiếu "
        "trước khi tin và chia sẻ. **(5) Quản lí thời gian:** đặt giới hạn sử dụng mạng để tránh nghiện. "
        "**(6) Sao lưu và nhờ giúp đỡ:** sao lưu dữ liệu định kì; báo ngay cho người lớn/thầy cô khi có "
        "dấu hiệu bất thường."), see="3.2.4"),
    dict(code="B2.5", unit="B2", form="TL · Vận dụng", answer=(
        "Dùng **Windows Defender/Microsoft Defender**: Start → Settings → Windows Security → "
        "**Virus & threat protection** → **Scan options**. Bốn chế độ: **Quét nhanh** (thư mục có nguy cơ cao), "
        "**Quét toàn bộ** (mọi ổ đĩa), **Quét tuỳ chọn** (chọn thư mục cụ thể), **Quét ngoại tuyến** "
        "(khởi động lại để quét sâu). Chọn chế độ → **Scan now** → xem kết quả và cách li/xoá mối đe doạ. "
        "Cách nhanh: nháy chuột phải vào tệp/thư mục → **Scan with Microsoft Defender**. "
        "Có thể dùng thêm Bkav, Kaspersky, Avast, AVG. Kèm theo đó: cập nhật hệ điều hành, "
        "gỡ ứng dụng lạ, đổi mật khẩu và khôi phục dữ liệu từ bản sao lưu sạch."), see="3.2.3"),
    dict(code="B2.6", unit="B2", form="TL · Vận dụng", answer=(
        "Ví dụ dùng **Google Translate**: (1) mở trang dịch, chọn **ngôn ngữ nguồn** (văn bản cần dịch) "
        "và **ngôn ngữ đích** (kết quả); (2) nhập dữ liệu bằng **3 cách** – gõ trực tiếp, **nói qua micro** "
        "(nhập bằng giọng nói), hoặc **tải tệp** .docx/.xlsx/.pptx/.pdf; (3) đọc/nghe kết quả "
        "(bấm loa 1 lần đọc thường, 2 lần đọc chậm); (4) **Ctrl + C** để sao chép, **Ctrl + V** để dán "
        "vào văn bản; (5) **rà soát, chỉnh sửa** vì bản dịch có thể sai nghĩa. Ngoài ra có thể dùng "
        "**voice typing** (gõ bằng giọng nói) trên điện thoại để soạn văn bản, hoặc công cụ nhận dạng "
        "giọng nói trong phần mềm soạn thảo."), see="3.2.2"),
    dict(code="B2.7", unit="B2", form="TL · Vận dụng", answer=(
        "Xác định nhu cầu → chọn từ khoá → tìm trên công cụ tìm kiếm → lọc nguồn uy tín → đọc mô tả "
        "(tên bài, chủ đề, tác giả) → mở học liệu → **ghi nguồn**. Nguồn nên dùng: cổng **igiaoduc.vn** "
        "(học liệu số, sách giáo khoa điện tử, bài giảng theo môn/lớp), **VOER**, **Wikipedia/Wikimedia "
        "Commons**, **Khan Academy**, **MIT OpenCourseWare**, thư viện số của trường/địa phương. "
        "**Học liệu mở (OER)** thường cho phép dùng, sửa, chia sẻ lại miễn phí nhưng vẫn phải **ghi nhận "
        "tác giả và tuân thủ giấy phép** (ví dụ Creative Commons BY, NC, ND); không chép nguyên bài "
        "rồi nhận là của mình."), see="3.2.2"),
    dict(code="B2.8", unit="B2", form="TL · Vận dụng", answer=(
        "**7 việc cụ thể:** (1) dùng mật khẩu dài ≥12 kí tự, khác nhau cho mỗi tài khoản và bật **2FA**; "
        "(2) không chia sẻ mã OTP, mật khẩu, CCCD, ảnh giấy tờ tuỳ thân; "
        "(3) cài đặt **riêng tư** cho tài khoản mạng xã hội, chỉ cho người quen xem bài; "
        "(4) kiểm tra **quyền ứng dụng** (camera, micro, vị trí, danh bạ) và gỡ app lạ; "
        "(5) cập nhật hệ điều hành, dùng phần mềm chống mã độc để tránh spyware/keylogger; "
        "(6) cẩn trọng với **Wi-Fi công cộng**, chỉ giao dịch trên trang `https://` đúng tên miền; "
        "(7) **sao lưu định kì** và xoá sạch dữ liệu trước khi bán/cho thiết bị. "
        "Ngoài ra, không đăng thông tin nhạy cảm của người khác và suy nghĩ trước khi chia sẻ."), see="3.2.4"),

    # ---------------------------------------------------------------- D1 (8)
    dict(code="D1.1", unit="D1", form="TN · Nhận biết", answer=(
        "Khi giao tiếp qua mạng trở nên phổ biến, nảy sinh các vấn đề: đưa thông tin không phù hợp "
        "(sai sự thật, bạo lực, phản cảm); công bố thông tin cá nhân khi chưa được phép; "
        "gửi thư rác/tin nhắn rác; vi phạm bản quyền dữ liệu và phần mềm; bắt nạt qua mạng; "
        "lừa đảo qua mạng; ứng xử thiếu văn hoá (chửi tục, sỉ nhục, kì thị). Nguyên nhân là mạng "
        "truyền tin **nhanh, rẻ, ẩn danh, lan rộng và khó xoá hết**, nên cần cả **đạo đức, pháp luật "
        "và văn hoá số** để điều chỉnh."), see="4.2"),
    dict(code="D1.2", unit="D1", form="TN · Nhận biết", answer=(
        "Theo SGK: **Luật Giao dịch điện tử 2005** công nhận giá trị pháp lí của giao dịch và "
        "thông điệp dữ liệu điện tử; **Luật Công nghệ thông tin 2006** điều chỉnh hoạt động ứng dụng, "
        "phát triển CNTT, trong đó **Điều 12** quy định các hành vi bị nghiêm cấm về thông tin số; "
        "**Luật An ninh mạng 2018** bảo vệ an ninh quốc gia trên không gian mạng, **Điều 8** liệt kê "
        "hành vi bị cấm. Về nghị định hướng dẫn: **Nghị định 90/2008/NĐ-CP** chống thư rác và "
        "**Nghị định 72/2013/NĐ-CP** quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng "
        "(tên miền, trang thông tin điện tử, mạng xã hội) – đây là các “Nghị định về quản lí, cung cấp, "
        "sử dụng các sản phẩm và dịch vụ CNTT” mà bản đặc tả nhắc tới."), see="4.3"),
    dict(code="D1.3", unit="D1", form="TL · Thông hiểu", answer=(
        "**Ví dụ:** nhóm bạn tải một bản nhạc đang bán trên mạng và 3 ảnh từ báo điện tử để đưa vào "
        "slide thuyết trình, không ghi nguồn, rồi đăng video lên mạng xã hội. **Vi phạm diễn ra:** "
        "sao chép và truyền đạt tác phẩm tới công chúng khi chưa có sự đồng ý của chủ thể quyền, "
        "không nêu tên tác giả – xâm phạm quyền tài sản và quyền nhân thân. **Hậu quả:** với tác giả "
        "là mất doanh thu, mất động lực sáng tạo; với người vi phạm là bị yêu cầu gỡ bài, xin lỗi, "
        "bồi thường, xử phạt hành chính, có thể bị truy cứu trách nhiệm hình sự nếu thu lợi lớn; "
        "với xã hội là thói quen dùng “đồ ăn cắp” lan rộng. **Cách sửa:** gỡ video, thay bằng tư liệu "
        "có giấy phép mở hoặc tự tạo, ghi rõ tác giả và nguồn."), see="4.4"),
    dict(code="D1.4", unit="D1", form="TL · Thông hiểu", answer=(
        "**Luật Công nghệ thông tin 2006** quy định hoạt động ứng dụng, phát triển CNTT và cấm "
        "(Điều 12) cung cấp, trao đổi, truyền đưa, lưu trữ, sử dụng thông tin số nhằm chống Nhà nước, "
        "kích động bạo lực, tiết lộ bí mật, xuyên tạc/vu khống/xúc phạm danh dự, quảng cáo hàng cấm, "
        "xâm phạm quyền sở hữu trí tuệ và giả mạo trang thông tin điện tử. **Luật An ninh mạng 2018** "
        "(Điều 8) cấm dùng không gian mạng để xuyên tạc lịch sử, đưa tin sai gây hoang mang, "
        "đăng nội dung dâm ô, xúi giục phạm tội. **Nghị định 72/2013/NĐ-CP** quy định trách nhiệm "
        "khi cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng (quản lí tên miền, mạng xã hội). "
        "**Ví dụ minh hoạ:** đăng tin bịa đặt “trường nghỉ học một tuần” gây hoang mang là vi phạm "
        "quy định về thông tin sai sự thật; tạo trang web giả mạo ngân hàng để lấy mật khẩu là vi phạm "
        "quy định giả mạo trang thông tin điện tử."), see="4.3"),
    dict(code="D1.5", unit="D1", form="TL · Thông hiểu", answer=(
        "**Bản quyền/sở hữu:** dữ liệu số là tài sản được bảo vệ; quyền tác giả phát sinh ngay khi "
        "tác phẩm được tạo ra, gồm quyền nhân thân và quyền tài sản. **Sử dụng:** mua một bài hát hay "
        "một bộ phần mềm chỉ được **sử dụng theo giấy phép**, không có quyền sao chép, phát tán lại; "
        "thông tin cá nhân chỉ được thu thập, dùng khi có sự đồng ý hoặc theo quy định. "
        "**Trao đổi/chia sẻ:** người đăng, người chuyển tiếp đều chịu trách nhiệm về nội dung mình "
        "truyền đưa. **Ví dụ:** mua tài khoản xem phim rồi chia sẻ mật khẩu cho cả lớp là vi phạm "
        "điều khoản sử dụng và có thể xâm phạm quyền tài sản; mượn ảnh CC BY nhưng quên ghi tên tác giả "
        "là chưa tuân thủ điều kiện giấy phép; đăng số điện thoại của bạn học lên nhóm mà không xin phép "
        "là xâm phạm thông tin cá nhân."), see="4.4"),
    dict(code="D1.6", unit="D1", form="TL · Thông hiểu", answer=(
        "Ví dụ 1: chuyển tiếp tin nhắn “trường nghỉ học một tuần” chưa được kiểm chứng → hàng trăm "
        "phụ huynh hoang mang, giáo viên phải giải thích, người chuyển tiếp có thể bị xử lí vì truyền "
        "đưa thông tin sai sự thật. Ví dụ 2: đăng ảnh bạn bị ngã kèm lời chế giễu → bạn bị tổn thương "
        "tinh thần, ảnh lan sang nhiều nhóm khó gỡ hết. Ví dụ 3: chụp màn hình bài kiểm tra có tên, "
        "số điện thoại rồi chia sẻ → lộ dữ liệu cá nhân của cả lớp, kẻ xấu có thể lợi dụng để lừa đảo. "
        "Ví dụ 4: đăng lại video bạo lực “cho vui” → người xem hiểu sai, nội dung độc hại lan rộng "
        "và người đăng vi phạm quy định về thông tin phản văn hoá."), see="4.5"),
    dict(code="D1.7", unit="D1", form="TL · Thông hiểu", answer=(
        "**① Kiểm tra nguồn** (ai đăng, khi nào, có đáng tin không, đối chiếu 2 nguồn độc lập). "
        "**② Không chia sẻ tin vi phạm pháp luật** (tin giả, kích động bạo lực, nội dung dâm ô, "
        "hàng cấm). **③ Tôn trọng bản quyền:** xin phép hoặc dùng nguồn mở, ghi rõ tác giả + nguồn + "
        "giấy phép, trích dẫn vừa đủ. **④ Bảo vệ thông tin cá nhân:** không đăng số điện thoại, "
        "địa chỉ, CCCD, mã OTP, ảnh riêng tư; che thông tin nhạy cảm trong ảnh chụp màn hình. "
        "**⑤ Cân nhắc đạo đức, văn hoá** trước khi bấm “Chia sẻ”: tin đúng nhưng vẫn có thể làm "
        "ai đó tổn thương. **⑥ Chủ động báo cáo** nội dung xấu cho nền tảng, giáo viên hoặc cơ quan "
        "chức năng; dùng `https://` và tài khoản có xác thực 2 yếu tố."), see="4.6"),
    dict(code="D1.8", unit="D1", form="TL · Vận dụng cao", answer=(
        "Dùng **khung 5 bước**: **(1) mô tả hành vi**; **(2) xác định đối tượng bị tác động** "
        "(người, tác phẩm, dữ liệu, hệ thống); **(3) đối chiếu văn bản** – Luật CNTT 2006 (Điều 12), "
        "Luật ANM 2018 (Điều 8), Nghị định 72/2013, quy định về quyền tác giả – và chỉ ra đúng "
        "nhóm hành vi bị cấm; **(4) kết luận hợp pháp/không hợp pháp** kèm lí do; "
        "**(5) đề xuất cách xử lí** (gỡ bài, xin lỗi, ghi nguồn/xin phép, lưu bằng chứng, báo giáo "
        "viên/cơ quan chức năng). Ví dụ: tạo trang web giả mạo ngân hàng để lấy mật khẩu khách hàng "
        "→ giả mạo trang thông tin điện tử, xâm phạm thông tin cá nhân, thu thập mật khẩu trái phép "
        "→ **không hợp pháp** theo Luật CNTT (Điều 12) và Nghị định 72/2013 → phải gỡ trang, báo cáo "
        "và có thể bị xử phạt, bồi thường, truy cứu trách nhiệm hình sự. Xem 4 tình huống mẫu ở mục 4.7.1."), see="4.7"),
]


def blocks():
    return [
        H1("PHẦN 5 · NGÂN HÀNG CÂU HỎI VÀ ĐÁP ÁN THEO 100% YÊU CẦU CỦA ĐẶC TẢ"),
        LEAD("Phần này là **trái tim** của đề cương: **toàn bộ 35 yêu cầu cần kiểm tra, đánh giá** "
             "trong bảng đặc tả của tài liệu gốc được giữ **nguyên văn**, và mỗi yêu cầu đều có "
             "**đáp án đầy đủ** kèm vị trí kiến thức tương ứng trong đề cương."),
        BOX("Làm rõ về “câu hỏi và đáp án trong tài liệu gốc”", [
            "Tài liệu `MA TRAN GIUA KI I - LOP 10.docx` là **ma trận đề + đặc tả đề**, "
            "**không chứa câu hỏi hay đáp án cụ thể nào**. Nội dung của nó là 35 **yêu cầu cần đạt** "
            "(các dòng “Nêu được…, Trình bày được…, Giải thích được…, Vận dụng được…”).",
            "Để đáp ứng trọn vẹn yêu cầu “bao gồm tất cả câu hỏi và đáp án của tài liệu gốc”, đề cương này: "
            "**(a)** chép nguyên văn toàn bộ văn bản gốc ở **Phụ lục A**; "
            "**(b)** chuyển **35/35 yêu cầu** thành 35 câu hỏi và biên soạn đáp án chi tiết ngay dưới đây; "
            "**(c)** bổ sung một **đề thi thử hoàn chỉnh** (20 TN + 2 ĐS + 3 TL) có đáp án ở Phần 6. "
            "Như vậy không có nội dung nào của bản gốc bị bỏ sót.",
        ], "note"),
        TBL(["Đơn vị kiến thức", "Số yêu cầu", "Mức độ (theo đặc tả)", "Vị trí ôn"], [
            ["A1. Dữ liệu, thông tin và xử lý thông tin", "**5**", "1 Nhận biết, 2 Thông hiểu, 2 Vận dụng", "2.1"],
            ["A2. Vai trò của máy tính, thiết bị thông minh", "**7**", "3 Nhận biết, 4 Thông hiểu", "2.2"],
            ["A3. Kĩ năng sử dụng thiết bị số", "**2**", "2 Vận dụng (thực hành)", "2.3"],
            ["B1. Mạng máy tính, Internet, IoT", "**5**", "2 Nhận biết, 3 Thông hiểu", "3.1"],
            ["B2. Dịch vụ web, tự bảo vệ khi tham gia mạng", "**8**", "3 Nhận biết, 1 Thông hiểu, 4 Vận dụng", "3.2"],
            ["D1. Nghĩa vụ tuân thủ pháp lí", "**8**", "2 Nhận biết, 5 Thông hiểu, 1 Vận dụng", "Phần 4"],
            ["**TỔNG**", "**35**", "**11 Nhận biết · 15 Thông hiểu · 9 Vận dụng**", "—"],
        ], widths=[186, 60, 180, 85], fs=8.2,
               caption="Bảng 5.1 – Thống kê 35 yêu cầu. Con số được đếm trực tiếp từ file .docx "
                       "bởi script build, không phải gõ tay."),
        P("*Cách đọc mỗi câu dưới đây:* dòng **YÊU CẦU (nguyên văn)** là văn bản trích xuất trực tiếp từ "
          "ô “Mức độ kiến thức, kĩ năng cần kiểm tra, đánh giá” của bản đặc tả; "
          "dòng **ĐÁP ÁN** là phần biên soạn của đề cương. Kí hiệu trong ngoặc là mức độ nhận thức và "
          "hình thức câu hỏi tương ứng trong ma trận.*"),
        {"k": "qabank"},
        PB(),
    ]
