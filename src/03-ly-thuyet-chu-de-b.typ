// =============================================================================
// src/03-ly-thuyet-chu-de-b.typ
// Phần II - Chuyên đề 2: Chủ đề B. Mạng máy tính và Internet (SGK KNTT 10)
// =============================================================================

#import "template.typ": *

#topic-banner(
  "Chuyên đề 2 • Chủ đề B",
  "MẠNG MÁY TÍNH VÀ INTERNET",
  "Phạm vi SGK Kết nối tri thức 10: Bài 8 (Mạng máy tính trong cuộc sống hiện đại) • Bài 9 (An toàn trên không gian mạng) • Bài 10 (Thực hành khai thác tài nguyên trên Internet)",
  "Trọng số: 4,0 điểm (40%)",
  accent: c-teal,
  bg: c-teal-bg,
  bdr: c-teal-bdr,
)

=== B.1. Khái niệm mạng máy tính, Internet, IoT & Phân loại mạng (2,0 điểm: 4 TN NB + 1 ĐS)

==== 1. Kiến thức cốt lõi & Bảng so sánh vàng LAN – Internet – Cloud – IoT

- *Mạng máy tính:* Là hệ thống gồm hai hay nhiều máy tính và thiết bị số được kết nối với nhau (qua cáp mạng hoặc sóng vô tuyến) nhằm *truyền dữ liệu* và *chia sẻ tài nguyên dùng chung* (tệp tin, máy in, bộ nhớ, đường truyền...).
- *Các thiết bị kết nối mạng thường gặp:* Vỉ mạng (*NIC*), bộ chuyển mạch (*Switch* – kết nối các máy trong mạng LAN), bộ định tuyến (*Router* – dẫn đường gói tin liên mạng/kết nối ra Internet), bộ thu phát Wi-Fi (*Access Point / Modem*).

#spec-qa(
  "B1.4", "TH",
  "So sánh được mạng LAN (Local Area Network) và mạng Internet.",
  [
    #set text(size: 8.6pt)
    #table(
      columns: (1.05fr, 1.45fr, 1.5fr),
      inset: (x: 6pt, y: 5pt),
      stroke: 0.45pt + c-border,
      fill: (x, y) => if y == 0 { c-teal } else if calc.odd(y) { white } else { c-teal-bg },
      table.header(
        [#text(fill: white, weight: "bold")[Tiêu chí so sánh]],
        [#text(fill: white, weight: "bold")[Mạng cục bộ (LAN)]],
        [#text(fill: white, weight: "bold")[Mạng Internet]],
      ),
      [*1. Phạm vi địa lí*],
      [*Phạm vi hẹp:* Trong một phòng máy, một tầng lầu, tòa nhà, trường học, bệnh viện, gia đình hoặc cơ quan.],
      [*Phạm vi toàn cầu:* Kết nối hàng triệu mạng máy tính khắp các quốc gia, châu lục trên toàn thế giới.],
      [*2. Quyền sở hữu* *(hay hỏi thi nhất!)*],
      [*Có chủ sở hữu xác định:* Thuộc quyền sở hữu và quản lí riêng của một cá nhân, gia đình, trường học hoặc tổ chức.],
      [*Không thuộc quyền sở hữu của bất kì cá nhân hay tổ chức riêng lẻ nào* (mạng công cộng toàn cầu cùng tuân chuẩn TCP/IP).],
      [*3. Quy mô kết nối*],
      [Nhỏ đến trung bình (từ vài thiết bị đến vài trăm máy tính, máy in).],
      [Cực lớn (hàng chục tỉ máy tính, điện thoại, máy chủ, thiết bị IoT).],
      [*4. Phương thức truyền dẫn*],
      [Chủ yếu dùng cáp xoắn đôi nội bộ (UTP), cáp quang nội bộ hoặc sóng Wi-Fi qua Switch/Access Point.],
      [Đường truyền viễn thông diện rộng do ISP cung cấp: cáp quang biển/quốc gia, vệ tinh, 4G/5G, hệ thống Router liên mạng.],
      [*5. Tính ổn định & An toàn*],
      [Tốc độ nội bộ cao, ổn định, ít phụ thuộc bên ngoài, dễ kiểm soát bảo mật nội bộ.],
      [Phụ thuộc đường truyền ISP; môi trường mở nên tiềm ẩn nhiều rủi ro tấn công mạng, virus, đánh cắp dữ liệu.],
    )
    *Điểm giống nhau:* Đều kết nối các thiết bị số để trao đổi dữ liệu và chia sẻ tài nguyên theo các giao thức truyền thông.
  ]
)

#spec-qa(
  "B1.1", "NB",
  "Nêu được một số dịch vụ cụ thể mà Điện toán đám mây (Cloud Computing) cung cấp cho người dùng.",
  [
    - *Khái niệm:* *Điện toán đám mây (Cloud Computing)* là mô hình cung cấp tài nguyên máy tính (lưu trữ, máy chủ, cơ sở dữ liệu, phần mềm...) qua *Internet* theo nhu cầu sử dụng mọi lúc, mọi nơi.
    - *Các dịch vụ đám mây cụ thể, quen thuộc nhất với người dùng:*
      1. *Dịch vụ lưu trữ đám mây (Cloud Storage):* `Google Drive`, `Microsoft OneDrive`, `Dropbox`, `Apple iCloud`, `Box`, `Mega` (lưu trữ, đồng bộ, sao lưu và chia sẻ tệp trực tuyến).
      2. *Phần mềm ứng dụng trực tuyến – SaaS (Software as a Service):* Soạn thảo & bảng tính trực tuyến (`Google Docs`, `Google Sheets`, `Google Slides`, `Microsoft 365 Online`), thư điện tử nền web (`Gmail`, `Outlook Web`), họp & học trực tuyến (`Zoom`, `Google Meet`, `Microsoft Teams`), thiết kế trực tuyến (`Canva`).
      3. *Nền tảng & Hạ tầng đám mây (dành cho nhà phát triển/doanh nghiệp):* *PaaS* (nền tảng phát triển web/ứng dụng) và *IaaS* (thuê máy chủ ảo, hạ tầng mạng như `Amazon AWS`, `Google Cloud`, `Microsoft Azure`, `Viettel Cloud`).
  ]
)

#memory-box(
  "Phân biệt 3 mô hình Điện toán đám mây trong 5 giây (SaaS – PaaS – IaaS)",
  [
    - *SaaS (Software – Phần mềm):* Dành cho *người dùng cuối* mở trình duyệt dùng ngay (`Google Docs`, `Gmail`, `Google Drive`, `Zoom`).
    - *PaaS (Platform – Nền tảng):* Dành cho *lập trình viên* thuê môi trường (hệ điều hành + CSDL) để viết và chạy phần mềm.
    - *IaaS (Infrastructure – Hạ tầng):* Dành cho *quản trị hệ thống/công ty* thuê phần cứng ảo hoá (máy chủ ảo VPS, ổ lưu trữ, mạng).
  ]
)

#spec-qa(
  "B1.2 & B1.5", "NB & TH",
  "Nêu khái niệm Internet vạn vật (IoT); Nêu ví dụ cụ thể về thay đổi trong cuộc sống mà IoT đem lại và phát biểu ý kiến cá nhân về lợi ích của IoT.",
  [
    - *Khái niệm IoT (Internet of Things – Internet vạn vật):* Là hệ thống liên kết các đồ vật, máy móc, phương tiện, cảm biến và thiết bị thông minh có gắn định danh và kết nối Internet, giúp chúng *tự động thu thập, trao đổi dữ liệu với nhau và thực thi công việc mà không cần (hoặc rất ít cần) sự can thiệp trực tiếp của con người*.
    - *Ví dụ thực tiễn sinh động về thay đổi cuộc sống nhờ IoT:*
      - *Giao thông thông minh:* Trạm *thu phí tự động không dừng ETC* trên quốc lộ/cao tốc tự nhận diện thẻ định danh dán trên ô tô, trừ tiền điện tử và mở barie trong 1–2 giây mà xe không phải dừng mua vé giấy.
      - *Nhà thông minh (Smart Home):* Cảm biến khói phát hiện rò rỉ khí gas tự động ngắt van, bật quạt thông gió, hú còi và gửi cảnh báo tức thời đến điện thoại chủ nhà dù đang đi công tác xa.
      - *Nông nghiệp thông minh:* Cảm biến đo độ ẩm đất, nhiệt độ, ánh sáng trong nhà màng dưa lưới tự động kích hoạt hệ thống tưới nhỏ giọt đúng lượng nước cây cần.
      - *Y tế thông minh:* Đồng hồ thông minh theo dõi nhịp tim người cao tuổi 24/7, tự động gửi định vị GPS và cảnh báo cấp cứu cho bác sĩ/người thân khi phát hiện té ngã hoặc rối loạn nhịp tim.
    - *Ý kiến đánh giá về lợi ích của IoT:* IoT mang lại bước nhảy vọt về chất lượng sống và năng suất xã hội: giúp *giám sát và phản ứng tức thời theo thời gian thực*, hoạt động bền bỉ cả ở nơi khắc nghiệt/nguy hiểm, *tiết kiệm thời gian – năng lượng – nhân lực*, giảm thiểu sai sót chủ quan của con người (song người dùng cũng cần chú ý đổi mật khẩu mặc định của thiết bị IoT để đảm bảo bảo mật riêng tư).
  ]
)

#spec-qa(
  "B1.3", "TH",
  "Trình bày những thay đổi về chất lượng cuộc sống, phương thức học tập và làm việc trong xã hội có mạng máy tính sử dụng phổ biến.",
  [
    - *Thay đổi phương thức học tập:* Chuyển từ học thụ động giới hạn trong lớp học sang *học mọi lúc, mọi nơi* qua lớp học trực tuyến (*E-learning*), thư viện số, phòng thí nghiệm ảo, kho học liệu mở toàn cầu, tạo điều kiện *học tập suốt đời*.
    - *Thay đổi phương thức làm việc & kinh tế:* Xuất hiện làm việc từ xa (*Work from home*), họp trực tuyến xuyên biên giới, cộng tác đồng thời trên cùng một tài liệu đám mây; thúc đẩy *Thương mại điện tử*, *Ngân hàng số* thanh toán không tiền mặt và *Chính phủ điện tử*.
    - *Nâng cao chất lượng cuộc sống & giao tiếp:* Kết nối tức thời với chi phí rất thấp (nhắn tin, gọi video), tiếp cận tin tức và giải trí đa phương tiện theo yêu cầu, đặt lịch khám bệnh/mua vé trực tuyến nhanh gọn không phải xếp hàng chờ đợi.
  ]
)

=== B.2. Sử dụng dịch vụ Web & Tự bảo vệ khi tham gia mạng (2,0 điểm: 4 TN + 1 TL)

==== 1. Bảng phân biệt chi tiết các loại Phần mềm độc hại (Malware) – Cực hay ra thi!

#spec-qa(
  "B2.1", "NB",
  "Trình bày được sơ lược về phần mềm độc hại (Malware).",
  [
    *Phần mềm độc hại (Malware – Malicious Software)* là các chương trình máy tính được viết ra với mục đích xấu nhằm xâm nhập trái phép, gây rối hoạt động thiết bị, đánh cắp thông tin cá nhân, phá hủy hoặc mã hóa dữ liệu tống tiền người dùng.
    #v(3pt)
    #set text(size: 8.4pt)
    #table(
      columns: (1.05fr, 1.35fr, 1.6fr),
      inset: (x: 6pt, y: 4.5pt),
      stroke: 0.45pt + c-border,
      fill: (x, y) => if y == 0 { c-navy } else if calc.odd(y) { white } else { c-light },
      table.header(
        [#text(fill: white, weight: "bold")[Loại mã độc]],
        [#text(fill: white, weight: "bold")[Cơ chế tồn tại & lây lan đặc trưng]],
        [#text(fill: white, weight: "bold")[Tác hại chính & Dấu hiệu nhận diện]],
      ),
      [*1. Virus máy tính*],
      [*Không phải chương trình độc lập*; phải *ký sinh (gắn) vào một tệp vật chủ* hợp pháp (`.exe`, `.docx` có macro...). Chỉ kích hoạt khi người dùng mở/chạy tệp vật chủ.],
      [Tự nhân bản lây sang các tệp khác trong máy, làm hỏng tệp, xóa dữ liệu, làm treo/chậm hệ thống.],
      [*2. Sâu máy tính*\ *(Worm)*],
      [*Là chương trình độc lập hoàn chỉnh*; *tự nhân bản và tự động phát tán qua mạng* (email, lỗ hổng bảo mật mạng, USB) mà không cần tệp vật chủ.],
      [Lây lan cực nhanh làm tắc nghẽn băng thông mạng, làm quá tải máy chủ và mở đường tải thêm mã độc khác.],
      [*3. Ngựa thành Troa*\ *(Trojan Horse)*],
      [*Không tự nhân bản*; *ngụy trang dưới vỏ bọc phần mềm hữu ích/hấp dẫn* (game miễn phí, phần mềm bẻ khóa *crack*) lừa người dùng tự cài đặt.],
      [Âm thầm mở "cửa hậu" (*Backdoor*) cho tin tặc chiếm quyền điều khiển máy từ xa hoặc đánh cắp dữ liệu.],
      [*4. Phần mềm gián điệp*\ *(Spyware / Keylogger)*],
      [Ẩn mình chạy ngầm trong hệ thống mà người dùng không hề hay biết.],
      [Theo dõi thói quen duyệt web, ghi lại thao tác gõ phím (*Keylogger*) để đánh cắp mật khẩu, tài khoản ngân hàng.],
      [*5. Mã độc tống tiền*\ *(Ransomware)*],
      [Xâm nhập qua email lừa đảo (*Phishing*), liên kết độc hại hoặc lỗ hổng hệ điều hành.],
      [*Mã hóa toàn bộ dữ liệu* quan trọng trên máy (hoặc khóa màn hình) rồi đòi tiền chuộc mới cấp khóa giải mã.],
      [*6. Quảng cáo độc hại*\ *(Adware)*],
      [Thường đi kèm các bộ cài phần mềm miễn phí không rõ nguồn gốc.],
      [Tự động bật cửa sổ quảng cáo dày đặc, tự đổi trang chủ trình duyệt và dẫn hướng tới trang web lừa đảo.],
    )
  ]
)

#memory-box(
  "3 từ khóa phân biệt nhanh Virus – Worm – Trojan trong trắc nghiệm",
  [
    - Thấy *"gắn/ẩn vào tệp vật chủ, chờ người dùng chạy tệp mới lây"* $==>$ chọn ngay *Virus*.
    - Thấy *"chương trình độc lập, tự nhân bản lây lan qua mạng"* $==>$ chọn ngay *Worm (Sâu máy tính)*.
    - Thấy *"ngụy trang phần mềm hợp pháp/crack, không tự nhân bản, nội gián/mở cửa hậu"* $==>$ chọn ngay *Trojan*.
  ]
)

==== 2. Giải đáp trọn vẹn Yêu cầu cần đạt gốc về An toàn mạng & Khai thác Web (B2.2 – B2.8)

#spec-qa(
  "B2.3 & B2.4", "NB & TH",
  "Nêu những nguy cơ, tác hại nếu tham gia Internet bất cẩn/thiếu hiểu biết; Trình bày các cách đề phòng tác hại khi tham gia Internet.",
  [
    #grid(
      columns: (1fr, 1.1fr),
      column-gutter: 8pt,
      [
        *5 nguy cơ & tác hại chính khi bất cẩn:*
        1. *Tin giả, thông tin độc hại/phản văn hoá:* Bị dẫn dắt nhận thức lệch lạc, hoang mang, chia sẻ tin sai dẫn đến vi phạm pháp luật.
        2. *Lừa đảo trực tuyến & lộ dữ liệu cá nhân (Phishing):* Bị mạo danh ngân hàng/người quen chiếm đoạt tiền, mất tài khoản mạng xã hội.
        3. *Bị bắt nạt qua mạng (Cyberbullying):* Bị bôi nhọ, đe dọa, cô lập 24/7 gây khủng hoảng tâm lí, trầm cảm.
        4. *Nghiện Internet, nghiện game online:* Suy giảm thị lực, mất ngủ, cong vẹo cột sống, sao nhãng học tập và xa rời đời sống thực.
        5. *Nhiễm phần mềm độc hại:* Hỏng hệ điều hành, mất sạch dữ liệu học tập/công việc hoặc bị tống tiền.
      ],
      [
        *5 nguyên tắc vàng đề phòng tác hại:*
        1. *Bảo mật tài khoản chặt chẽ:* Đặt mật khẩu mạnh ($>= 8$ kí tự gồm chữ hoa, chữ thường, số, kí tự đặc biệt), bật *xác thực 2 lớp (2FA/OTP)*, đăng xuất khỏi máy lạ.
        2. *Thận trọng trước mọi cú nhấp chuột:* Không bấm vào link lạ, không mở tệp đính kèm từ email đáng ngờ, kiểm tra kĩ tên miền `https://` tránh web giả mạo.
        3. *Chọn lọc & kiểm chứng thông tin:* Đối chiếu tin tức trên các báo điện tử, cổng thông tin chính thống trước khi tin và chia sẻ.
        4. *Bảo vệ thiết bị:* Không tải phần mềm lậu / *crack*, cập nhật hệ điều hành và bật tường lửa + phần mềm diệt virus.
        5. *Quản lí thời gian hợp lí:* Cân bằng giữa dùng mạng với vận động thể chất, học tập và giao tiếp gia đình.
      ]
    )
  ]
)

#spec-qa(
  "B2.2", "NB",
  "Nêu được một vài cách phòng vệ khi bị bắt nạt trên mạng (Cyberbullying).",
  [
    Khi bản thân (hoặc bạn bè) bị bắt nạt trên mạng, cần bình tĩnh thực hiện *Quy trình 4 bước phòng vệ chuẩn ("KHÔNG – LƯU – CHẶN – BÁO")*:
    1. *KHÔNG đáp trả nóng giận:* Tuyệt đối không chửi bới, đôi co lại với kẻ bắt nạt trên mạng vì sẽ càng kích động đối phương và làm lan rộng sự việc.
    2. *LƯU giữ đầy đủ bằng chứng:* Chụp ảnh màn hình tin nhắn, bình luận ác ý, lưu đường dẫn (URL) trang cá nhân của kẻ bắt nạt và thời gian xảy ra.
    3. *CHẶN (Block) & BÁO CÁO (Report):* Sử dụng tính năng chặn liên lạc và báo cáo hành vi quấy rối/xúc phạm tới ban quản trị mạng xã hội để khóa tài khoản vi phạm; đồng thời khóa chế độ riêng tư trang cá nhân.
    4. *BÁO cho người lớn tin cậy & Cơ quan chức năng:* Tâm sự ngay với *cha mẹ, thầy cô giáo chủ nhiệm/tư vấn tâm lí học đường* để được bảo vệ, hỗ trợ; nếu bị đe dọa an toàn, tống tiền hoặc vu khống nghiêm trọng, cần trình báo *cơ quan Công an*.
  ]
)

#spec-qa(
  "B2.5 & B2.8", "VD",
  "Sử dụng công cụ thông dụng để ngăn ngừa, loại bỏ phần mềm độc hại; Biết cách tự bảo vệ dữ liệu cá nhân.",
  [
    - *Công cụ ngăn ngừa & loại bỏ phần mềm độc hại thông dụng:*
      - Bật *Tường lửa (Windows Defender Firewall)* để kiểm soát kết nối mạng trái phép và bật cập nhật tự động (*Windows Update*) vá lỗ hổng bảo mật.
      - Cài đặt và cập nhật cơ sở dữ liệu mẫu nhận diện của *phần mềm diệt virus (Antivirus)* uy tín: *Windows Security / Microsoft Defender* (tích hợp sẵn miễn phí trên Windows 10/11), *Kaspersky*, *Bitdefender*, *Norton*, *Avast*, *McAfee*, *Bkav Pro*... Thực hiện quét định kì toàn máy và *luôn quét USB / tệp tải từ Internet trước khi mở*.
    - *Cách tự bảo vệ dữ liệu cá nhân hiệu quả:*
      - Thực hiện *sao lưu dự phòng (Backup)* dữ liệu quan trọng định kì theo nguyên tắc lưu ở ít nhất 2 nơi (ổ cứng ngoài + lưu trữ đám mây như Google Drive/OneDrive) để không mất dữ liệu khi máy hỏng hay dính *Ransomware*.
      - Không công khai số CCCD, địa chỉ nhà riêng, số điện thoại, thẻ ngân hàng, mã OTP lên mạng xã hội; đặt mật khẩu/mã hóa cho tệp chứa thông tin nhạy cảm; không lưu mật khẩu tự động trên máy tính công cộng.
  ]
)

#spec-qa(
  "B2.6 & B2.7", "VD",
  "Sử dụng chức năng xử lí thông tin trên PC/thiết bị số (ví dụ dịch tự động văn bản/tiếng nói); Khai thác nguồn học liệu mở trên Internet.",
  [
    - *Sử dụng công cụ dịch tự động đa phương thức (tiêu biểu: Google Dịch – `translate.google.com`):*
      - *Trên PC:* Nhập/dán đoạn văn bản ngoại ngữ để dịch tức thời; tải nguyên tệp tài liệu (`.docx`, `.pdf`, `.pptx`) lên mục *Tài liệu (Documents)* để dịch giữ nguyên bố cục; bấm biểu tượng *Micro* để dịch giọng nói hoặc *Loa* để nghe phát âm chuẩn.
      - *Trên Smartphone:* Mở ứng dụng *Google Translate / Google Lens*, hướng camera vào trang sách/biển báo nước ngoài để dịch trực tiếp trên hình ảnh hoặc bật chế độ *Hội thoại* để phiên dịch song ngữ hai chiều theo thời gian thực.
    - *Khai thác nguồn học liệu mở (OER – Open Educational Resources) phục vụ tự học:*
      - *Khái niệm:* Nguồn học liệu mở là các tài nguyên giáo dục (sách điện tử, bài giảng video, mô phỏng thí nghiệm, câu hỏi ôn tập...) được chia sẻ công khai, miễn phí và hợp pháp trên Internet.
      - *Các địa chỉ học liệu mở uy tín học sinh lớp 10 nên khai thác:*
        1. *Hệ tri thức Việt số hoá (`igiaoduc.vn`)* và Kho bài giảng e-Learning của Bộ GD&ĐT (`elearning.moet.edu.vn`): Kho bài giảng, SGK và học liệu chuẩn chương trình Việt Nam.
        2. *Hành trang số (`hanhtrangso.nxbgd.vn`)* của NXB Giáo dục Việt Nam: Sách giáo khoa điện tử và bài tập bổ trợ bộ sách *Kết nối tri thức với cuộc sống*.
        3. *Nền tảng quốc tế:* `Khan Academy` (Toán, Khoa học, Tin học miễn phí có phụ đề), `MIT OpenCourseWare`, các khóa học mở trên `Coursera` / `edX`, mô phỏng khoa học `PhET Colorado`.
  ]
)
