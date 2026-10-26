// =============================================================================
// src/04-ly-thuyet-chu-de-d.typ
// Phần II - Chuyên đề 3: Chủ đề D. Đạo đức, pháp luật và văn hoá trong môi trường số
// =============================================================================

#import "template.typ": *

#topic-banner(
  "Chuyên đề 3 • Chủ đề D",
  "ĐẠO ĐỨC, PHÁP LUẬT VÀ VĂN HOÁ TRONG MÔI TRƯỜNG SỐ",
  "Phạm vi SGK Kết nối tri thức 10: Bài 11 (Ứng xử trên môi trường số. Nghĩa vụ tôn trọng bản quyền)",
  "Trọng số: 2,0 điểm (20% • Có câu TL Vận dụng cao)",
  accent: c-purple,
  bg: c-purple-bg,
  bdr: c-purple-bdr,
)

=== D.1. Nghĩa vụ tuân thủ pháp lí trong môi trường số (2,0 điểm: 4 TN + 1 TL Vận dụng cao)

==== 1. Bảng tổng hợp nhanh các Văn bản pháp luật cốt lõi (Theo SGK Tin học 10 KNTT)

#block(breakable: true)[
  #set text(size: 8.5pt)
  #table(
    columns: (1.25fr, 1.55fr, 1.6fr),
    inset: (x: 6.5pt, y: 5pt),
    stroke: 0.45pt + c-border,
    fill: (x, y) => if y == 0 { c-purple } else if calc.odd(y) { white } else { c-purple-bg },
    table.header(
      [#text(fill: white, weight: "bold")[Văn bản pháp luật]],
      [#text(fill: white, weight: "bold")[Nội dung / Điều khoản trọng tâm cần nhớ]],
      [#text(fill: white, weight: "bold")[Các hành vi điển hình bị nghiêm cấm / xử lí]],
    ),
    [*1. Luật Công nghệ thông tin năm 2006*\ *(Luật số 67/2006/QH11)*],
    [*Điều 12 – Các hành vi bị nghiêm cấm trong hoạt động CNTT:* Quy định toàn diện các hành vi cấm khi cung cấp, trao đổi, truyền đưa, lưu trữ thông tin số.],
    [Chống Nhà nước; kích động bạo lực, đồi trụy, tệ nạn, mê tín dị đoan; *xuyên tạc, vu khống, xúc phạm uy tín tổ chức, danh dự, nhân phẩm công dân*; phát tán virus/phần mềm độc hại; *xâm phạm quyền sở hữu trí tuệ* trong CNTT.],
    [*2. Luật An ninh mạng năm 2018*\ *(Luật số 24/2018/QH14)*],
    [*Điều 8, Điều 16–18, Điều 29:* Bảo vệ an ninh quốc gia, trật tự an toàn xã hội và quyền lợi hợp pháp của tổ chức, cá nhân (đặc biệt bảo vệ trẻ em) trên không gian mạng.],
    [Đăng tải *thông tin sai sự thật gây hoang mang trong Nhân dân*, gây thiệt hại kinh tế - xã hội; *tấn công mạng, gián điệp mạng, chiếm đoạt tài sản*, đánh cắp dữ liệu cá nhân, làm nhục/vu khống nghiêm trọng người khác.],
    [*3. Nghị định quản lí Internet & xử phạt hành chính*\ *(NĐ 72/2013/NĐ-CP; NĐ 15/2020/NĐ-CP sửa đổi bởi NĐ 14/2022)*],
    [
      - *Điều 5 NĐ 72/2013/NĐ-CP:* Các hành vi bị cấm khi cung cấp, sử dụng dịch vụ Internet & thông tin trên mạng.
      - *Điều 101 NĐ 15/2020/NĐ-CP:* Mức phạt tiền đối với vi phạm quy định về trách nhiệm sử dụng mạng xã hội.
    ],
    [Cung cấp, chia sẻ thông tin giả mạo, sai sự thật, xuyên tạc, vu khống, xúc phạm danh dự cá nhân; tiết lộ bí mật đời tư; chia sẻ đường dẫn thông tin cấm (*phạt hành chính 10–20 triệu đồng với tổ chức; 5–10 triệu đồng với cá nhân*, buộc gỡ bỏ thông tin).],
    [*4. Luật Sở hữu trí tuệ năm 2005*\ *(sửa đổi 2009, 2019, 2022)*],
    [Bảo hộ *Quyền tác giả (Bản quyền – Copyright)* đối với tác phẩm văn học, nghệ thuật, khoa học và sản phẩm số (phần mềm, CSDL, bài viết, ảnh, nhạc, video...). Gồm *Quyền nhân thân* & *Quyền tài sản*.],
    [Sao chép, công bố, phân phối, làm tác phẩm phái sinh hoặc khai thác thương mại tác phẩm/phần mềm *mà không xin phép và trả thù lao* cho chủ sở hữu bản quyền (*crack* phần mềm, in lậu/scan PDF sách, *re-up* video kiếm tiền, đạo văn).],
    [*5. Bộ luật Dân sự 2015 & Bộ Quy tắc ứng xử MXH*\ *(QĐ 874/QĐ-BTTTT năm 2021)*],
    [
      - *Điều 32, 38 BLDS 2015:* Quyền đối với hình ảnh & quyền về đời sống riêng tư, bí mật cá nhân.
      - *4 quy tắc ứng xử MXH:* Tôn trọng pháp luật – Lành mạnh – An toàn bảo mật – Trách nhiệm.
    ],
    [Tự ý chụp, đăng tải hình ảnh cá nhân, tin nhắn riêng tư, thông tin đời tư của người khác lên mạng khi chưa được sự đồng ý của người đó.],
  )
]

==== 2. Giải đáp trọn vẹn Yêu cầu cần đạt gốc trong Bản đặc tả (Đơn vị D.1: D1.1 – D1.8)

#spec-qa(
  "D1.1", "NB",
  "Nêu được một số vấn đề nảy sinh về pháp luật, đạo đức, văn hoá khi việc giao tiếp qua mạng trở nên phổ biến.",
  [
    Khi giao tiếp trên không gian mạng bùng nổ (nhờ tính ẩn danh, tốc độ lan truyền tức thời và phạm vi rộng), hàng loạt vấn đề tiêu cực nảy sinh về cả 3 phương diện:
    1. *Về văn hoá & đạo đức:* Sử dụng ngôn từ thiếu chuẩn mực, chửi tục, công kích cá nhân, miệt thị ngoại hình/vùng miền (*body shaming*), bắt nạt hội đồng trên mạng, cổ xúy lối sống lệch chuẩn, vô cảm, câu "like" / câu "view" bất chấp đạo lí.
    2. *Về quyền riêng tư & uy tín cá nhân:* Tự ý tiết lộ thông tin cá nhân, tung tin nhắn riêng tư, ghép ảnh bôi nhọ danh dự, nhân phẩm của cá nhân hoặc hạ thấp uy tín tổ chức/doanh nghiệp.
    3. *Về pháp luật & bản quyền:* Phát tán tin giả (*fake news*) gây hoang mang xã hội; vi phạm bản quyền phần mềm và tác phẩm số tràn lan; lừa đảo chiếm đoạt tài sản trực tuyến, đánh bạc qua mạng, phát tán mã độc và tuyên truyền chống phá Nhà nước.
  ]
)

#spec-qa(
  "D1.2 & D1.4", "NB & TH",
  "Trình bày và giải thích một số nội dung cơ bản của Luật CNTT, Nghị định về quản lí/cung cấp/sử dụng sản phẩm & dịch vụ CNTT, Luật An ninh mạng; Nêu ví dụ minh họa.",
  [
    - *Giải thích tinh thần cốt lõi của hệ thống pháp luật môi trường số:* Không gian mạng không phải là "vùng vô luật pháp" — mọi quyền tự do ngôn luận và chia sẻ thông tin trên mạng đều phải nằm trong khuôn khổ *không xâm hại an ninh quốc gia, trật tự xã hội và quyền, lợi ích hợp pháp của tổ chức, cá nhân khác*:
      1. *Luật Công nghệ thông tin (Điều 12):* Cấm lợi dụng CNTT để xuyên tạc, vu khống, xúc phạm danh dự công dân, phá hoại hệ thống thông tin, tạo/phát tán virus và xâm phạm quyền sở hữu trí tuệ.
         - *Ví dụ:* Viết phần mềm gián điệp gửi qua tin nhắn để đánh cắp tài khoản của người khác là vi phạm Điều 12 Luật CNTT.
      2. *Nghị định 72/2013/NĐ-CP & Nghị định 15/2020/NĐ-CP (Điều 101):* Quy định rõ trách nhiệm của người dùng mạng xã hội phải chịu trách nhiệm về nội dung mình đăng tải, lưu trữ, truyền đưa; nghiêm cấm chia sẻ thông tin giả mạo, sai sự thật, đồi trụy, mê tín dị đoan.
         - *Ví dụ:* Một tài khoản Facebook đăng tin bịa đặt *"Vỡ đập thủy điện / Dịch bệnh lạ chết người tại địa phương"* để câu tương tác thu hút bán hàng online $->$ vi phạm Luật An ninh mạng và Điều 101 Nghị định 15/2020/NĐ-CP, bị cơ quan chức năng phạt hành chính và buộc gỡ bài, đính chính công khai.
      3. *Luật An ninh mạng 2018 (Điều 8, 16, 29):* Ngăn chặn, xử lí nghiêm các hành vi tấn công mạng, khủng bố mạng, chiếm đoạt tài sản, tung tin sai sự thật gây hoang mang dư luận và bảo vệ trẻ em khỏi nội dung xâm hại trên mạng.
  ]
)

#spec-qa(
  "D1.3 & D1.5", "TH",
  "Giải thích khía cạnh pháp lí của vấn đề bản quyền, sở hữu, sử dụng và trao đổi thông tin số; Nêu ví dụ vi phạm bản quyền, giải thích cơ chế vi phạm và hậu quả.",
  [
    - *Khía cạnh pháp lí của Quyền tác giả (Bản quyền – Luật Sở hữu trí tuệ):*
      - Chủ sở hữu quyền tác giả có *Quyền nhân thân* (đứng tên tác giả, công bố tác phẩm, bảo vệ sự toàn vẹn tác phẩm) và *Quyền tài sản* (độc quyền sao chép, phân phối, truyền đạt tác phẩm tới công chúng, cho thuê bản sao chương trình máy tính...).
      - *Phân biệt quyền sở hữu bản sao và quyền tác giả:* Khi mua một cuốn sách điện tử hay một bản quyền phần mềm cài cho 1 máy, người mua *chỉ có quyền sử dụng hợp pháp theo giấy phép (License)* chứ *không trở thành chủ sở hữu quyền tác giả*, nên không được phép tự ý nhân bản để bán lại hay phát tán công khai lên mạng.
      - *Ngoại lệ hợp pháp:* Pháp luật cho phép trích dẫn hợp lí một phần nhỏ tác phẩm để bình luận, minh họa trong bài học/nghiên cứu của mình mà không cần xin phép hay trả tiền, với điều kiện *không làm sai lệch ý tác giả, không nhằm mục đích thương mại và bắt buộc ghi rõ tên tác giả, nguồn gốc tác phẩm*.
    - *Ví dụ minh họa vi phạm bản quyền, diễn biến & hậu quả:*
      - *Ví dụ:* Bạn H tải một bộ phim Việt Nam đang chiếu rạp bị quay lén (*bản cam*) rồi đăng lại lên kênh mạng xã hội cá nhân để kéo lượt xem và bật kiếm tiền quảng cáo; hoặc cài đặt phần mềm đồ họa bẻ khóa (*crack*).
      - *Giải thích sự vi phạm diễn ra như thế nào:* H đã thực hiện hành vi *sao chép và truyền đạt tác phẩm đến công chúng trái phép* mà không được sự đồng ý của nhà sản xuất/chủ sở hữu bản quyền. Do dữ liệu số sao chép tức thời không tốn chi phí, chỉ từ một lượt đăng tải đã phát tán cho hàng chục nghìn người xem lậu.
      - *Hậu quả:* (1) Gây thiệt hại doanh thu nặng nề cho đoàn làm phim/nhà phát triển phần mềm, làm triệt tiêu động lực sáng tạo; (2) Người vi phạm bị khóa kênh, *xử phạt hành chính*, buộc *bồi thường thiệt hại dân sự*, thậm chí bị *truy cứu trách nhiệm hình sự* nếu thu lợi bất chính lớn; (3) Riêng hành vi dùng phần mềm *crack* còn khiến máy tính của chính người dùng rất dễ nhiễm *Trojan/Ransomware*.
  ]
)

#spec-qa(
  "D1.6 & D1.7", "TH",
  "Nêu ví dụ về tác hại của việc chia sẻ thông tin bất cẩn; Nêu một vài biện pháp đơn giản, thông dụng để nâng cao tính an toàn và hợp pháp khi chia sẻ thông tin số.",
  [
    - *Ví dụ về tác hại của việc chia sẻ thông tin bất cẩn:*
      - *Ví dụ 1 (Chia sẻ tin chưa kiểm chứng):* Thấy bài đăng kêu gọi từ thiện giả mạo hoặc tin đồn *"cửa hàng X bán thực phẩm bẩn"* chưa có kết luận cơ quan chức năng nhưng vội vàng ấn *Chia sẻ (Share)* kèm lời lẽ bức xúc $->$ tiếp tay cho lừa đảo hoặc làm cửa hàng X điêu đứng phá sản oan, còn bản thân người chia sẻ bị xử phạt hành chính vì lan truyền tin sai sự thật.
      - *Ví dụ 2 (Lộ dữ liệu cá nhân & xâm phạm đời tư):* Chụp ảnh thẻ căn cước công dân (CCCD) hoặc vé máy bay có mã QR đăng khoe lên mạng xã hội khiến kẻ gian lấy thông tin đi vay tín dụng đen/hủy chuyến bay; hoặc quay lén khoảnh khắc nhạy cảm của bạn cùng lớp đăng lên nhóm công khai gây tổn thương tâm lí nặng nề cho bạn.
    - *5 biện pháp đơn giản, thiết thực để chia sẻ thông tin an toàn & hợp pháp:*
      1. *Kiểm chứng đa chiều trước khi chia sẻ:* Chỉ chia sẻ tin tức từ báo chí, cổng thông tin chính thống; luôn tự hỏi *5 chữ vàng*: *Đúng sự thật không? – Hợp pháp không? – Tôn trọng bản quyền/riêng tư không? – Có ích không? – Văn minh không?*
      2. *Tôn trọng bản quyền sản phẩm số:* Ưu tiên dùng phần mềm mã nguồn mở/miễn phí hợp pháp hoặc mua bản quyền; dùng ảnh/nhạc có giấy phép mở (*Creative Commons*); luôn *ghi rõ nguồn và tên tác giả* khi trích dẫn.
      3. *Xin phép trước khi đăng thông tin của người khác:* Tuyệt đối không đăng ảnh, video, số điện thoại hay tin nhắn riêng tư của bạn bè/người khác khi chưa được họ đồng ý.
      4. *Che chắn dữ liệu cá nhân nhạy cảm:* Làm mờ mã vạch, số CCCD, địa chỉ nhà, số tài khoản, biển số xe và giới hạn chế độ hiển thị bài viết (*Chỉ bạn bè*) với thông tin cá nhân.
      5. *Giữ gìn văn hoá ứng xử số:* Bình luận lịch sự, tích cực; không hùa theo đám đông công kích, miệt thị người khác.
  ]
)

#spec-qa(
  "D1.8", "VDC",
  "Vận dụng Luật và Nghị định nêu trên để xác định tính hợp pháp của một hành vi cụ thể trong quản lí, cung cấp, sử dụng sản phẩm và dịch vụ CNTT.",
  [
    *KHUNG 4 BƯỚC "ĂN TRỌN 1,0 ĐIỂM" KHI GIẢI CÂU TỰ LUẬN VẬN DỤNG CAO (CHỦ ĐỀ D):*
    - *Bước 1 – Khẳng định dứt khoát tính pháp lí (0,25đ):* Nêu rõ hành vi của nhân vật trong tình huống là *Hợp pháp* hay *Bất hợp pháp (Vi phạm pháp luật và đạo đức môi trường số)* (nếu tình huống có nhiều hành vi thì tách rõ từng hành vi).
    - *Bước 2 – Chỉ rõ bản chất vi phạm & Căn cứ pháp luật (0,25đ):*
      - Nếu là *tung tin giả, vu khống, bôi nhọ trên MXH* $->$ Vi phạm *Điều 12 Luật CNTT 2006*, *Điều 8/16 Luật An ninh mạng 2018* và *Điều 5 NĐ 72/2013/NĐ-CP (xử phạt theo Điều 101 NĐ 15/2020/NĐ-CP)*.
      - Nếu là *sao chép lậu phần mềm (crack), bán PDF sách lậu, re-up phim/nhạc kiếm tiền, đạo văn* $->$ Vi phạm *Quyền tác giả theo Luật Sở hữu trí tuệ* và *Điều 12 Luật CNTT 2006*.
      - Nếu là *tự ý đăng ảnh/tin nhắn riêng tư người khác* $->$ Xâm phạm *quyền đối với hình ảnh, bí mật đời tư (Bộ luật Dân sự 2015)* và *Luật CNTT / Luật An ninh mạng*.
      - Nếu là *hack tài khoản, phát tán virus/mã độc, lừa đảo qua mạng* $->$ Vi phạm nghiêm trọng *Điều 12 Luật CNTT 2006* và *Điều 8 Luật An ninh mạng 2018*.
    - *Bước 3 – Phân tích tác hại / hậu quả (0,25đ):* Nêu tác hại đối với nạn nhân/chủ sở hữu/xã hội VÀ chế tài pháp lí đối với người vi phạm (phạt hành chính, bồi thường thiệt hại, khóa tài khoản, thậm chí xử lí hình sự).
    - *Bước 4 – Tư vấn cách xử lí / ứng xử đúng đắn (0,25đ):* Đề xuất hành động khắc phục cụ thể, hợp pháp và văn minh cho nhân vật trong tình huống.
  ]
)
