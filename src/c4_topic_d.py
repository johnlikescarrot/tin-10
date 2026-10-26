# -*- coding: utf-8 -*-
"""Phần 4 – Chủ đề D (Chủ đề 3 KNTT): Đạo đức, pháp luật, văn hoá số."""
from .blocks import H1, H2, H3, P, LEAD, SMALL, UL, OL, TBL, BOX, PB, SP


def blocks():
    B = [
        H1("PHẦN 4 · CHỦ ĐỀ D: ĐẠO ĐỨC, PHÁP LUẬT VÀ VĂN HOÁ TRONG MÔI TRƯỜNG SỐ"),
        LEAD("Tương ứng **Chủ đề 3** (Bài 11) SGK *Kết nối tri thức với cuộc sống*. "
             "Dù chỉ chiếm **20% đề**, đây là nơi xuất hiện **câu tự luận Vận dụng cao** duy nhất. "
             "Móc nhớ: **3 trụ – 4 nhóm cấm – 3 nguyên tắc chia sẻ**."),

        H2("4.1. Tổng quan: ba trụ cột của ứng xử số"),
        TBL(["Trụ cột", "Câu hỏi tự đặt", "Hệ quả nếu vi phạm"], [
            ["**Đạo đức**", "Việc này có làm tổn thương ai không? Có trung thực không?",
             "Bị lên án, mất uy tín, tổn thương người khác."],
            ["**Pháp luật**", "Hành vi này có bị luật cấm không?",
             "Bị xử phạt hành chính, bồi thường, có thể truy cứu hình sự."],
            ["**Văn hoá**", "Cách nói, cách chia sẻ có lịch sự, tôn trọng không?",
             "Môi trường mạng độc hại, mất đi sự tin cậy."],
        ], widths=[88, 240, 183], fs=8.3),
        P("**Vì sao có nhiều vấn đề nảy sinh?** Vì giao tiếp qua mạng diễn ra **nhanh, rẻ, ẩn danh, "
          "lan truyền rộng** và khó xoá hoàn toàn. Một cú nhấp chuột thiếu suy nghĩ có thể gây hại "
          "cho người khác và để lại hậu quả pháp lí lâu dài."),

        H2("4.2. Bảy hành vi vi phạm thường gặp"),
        TBL(["Nhóm", "Hành vi", "Ví dụ"], [
            ["**Nội dung**", "Đưa thông tin không phù hợp (bạo lực, phản cảm, sai sự thật) lên mạng.",
             "Đăng video đánh nhau, tung tin đồn “trường nghỉ học một tuần”."],
            ["**Nội dung**", "Công bố thông tin cá nhân/tổ chức khi chưa được phép.",
             "Đăng ảnh, số điện thoại, địa chỉ nhà của bạn lên nhóm."],
            ["**Cách gửi**", "Gửi thư rác, tin nhắn rác, spam quảng cáo hàng loạt.",
             "Gửi cùng một tin nhắn quảng cáo cho 500 người không mong muốn."],
            ["**Đối xử**", "Bắt nạt qua mạng.",
             "Lập nhóm chê bai, đăng ảnh chế giễu bạn cùng lớp."],
            ["**Đối xử**", "Lừa đảo qua mạng.",
             "Giả danh nhân viên ngân hàng để lấy mã OTP."],
            ["**Đối xử**", "Ứng xử thiếu văn hoá.",
             "Chửi tục, công kích, sỉ nhục trong phần bình luận."],
            ["**Riêng biệt**", "**Vi phạm bản quyền** dữ liệu và phần mềm.",
             "Tải phần mềm crack, lấy ảnh/nhạc/bài viết của người khác làm của mình."],
        ], widths=[82, 236, 193], fs=8.2),
        BOX("Lỗi sai kinh điển", [
            "Nhiều bạn nghĩ: *“Mình chỉ chia sẻ lại, không phải người viết nên không có lỗi.”* "
            "**Sai.** Luật cấm cả hành vi **cung cấp, trao đổi, truyền đưa, lưu trữ, sử dụng** "
            "thông tin số trái phép – chia sẻ lại tin sai vẫn là vi phạm.",
        ], "warn"),

        H2("4.3. Các văn bản pháp luật cần biết (theo bài 11 SGK)"),
        TBL(["Văn bản", "Năm", "Nội dung cơ bản cần nhớ"], [
            ["**Luật Giao dịch điện tử**", "2005", "Công nhận giá trị pháp lí của giao dịch, "
                                                  "chữ kí và thông điệp dữ liệu điện tử."],
            ["**Luật Công nghệ thông tin**", "2006", "Điều chỉnh hoạt động ứng dụng, phát triển CNTT; "
                                                    "**Điều 12** quy định các hành vi bị nghiêm cấm "
                                                    "về thông tin số."],
            ["**Luật An ninh mạng**", "2018", "Bảo vệ an ninh quốc gia, trật tự an toàn xã hội "
                                             "trên không gian mạng; **Điều 8** liệt kê hành vi bị cấm."],
            ["**Nghị định 90/2008/NĐ-CP**", "2008", "Chống thư rác (spam)."],
            ["**Nghị định 72/2013/NĐ-CP**", "2013", "Quản lí, cung cấp, sử dụng **dịch vụ Internet "
                                                    "và thông tin trên mạng** (quản lí tên miền, "
                                                    "trang thông tin điện tử, mạng xã hội)."],
        ], widths=[152, 48, 311], fs=8.2,
               caption="Bảng 4.1 – Bản đặc tả gốc gọi chung nhóm nghị định là “Nghị định về quản lí, "
                       "cung cấp, sử dụng các sản phẩm và dịch vụ Công nghệ thông tin”; "
                       "trong SGK KNTT đó là các Nghị định 90/2008 và 72/2013."),
        P("**Lưu ý khi làm bài:** pháp luật có thể được sửa đổi, thay thế theo thời gian. "
          "Hãy bám theo **tên văn bản và năm ban hành được nêu trong SGK**; không cần học thuộc "
          "số điều, chỉ cần nắm **tinh thần** và biết nhận diện hành vi."),

        H3("4.3.1. Bốn nhóm hành vi bị cấm (gộp từ Điều 12 Luật CNTT và Điều 8 Luật ANM)"),
        OL([
            "**Xâm hại an ninh quốc gia, trật tự xã hội:** chống Nhà nước, phá hoại khối đoàn kết toàn dân, "
            "xuyên tạc lịch sử, phá hoại cơ sở hạ tầng thông tin, cản trở hoạt động hợp pháp.",
            "**Kích động bạo lực, hận thù, tệ nạn:** kích động chiến tranh, bạo loạn, mê tín dị đoan, "
            "đăng thông tin dâm ô, đồi trụy, xúi giục người khác phạm tội.",
            "**Nói sai sự thật, xúc phạm người khác:** thông tin sai gây hoang mang, xuyên tạc, vu khống, "
            "xúc phạm danh dự nhân phẩm, phân biệt đối xử về giới/chủng tộc/tôn giáo.",
            "**Tiết lộ bí mật, xâm phạm sở hữu trí tuệ, gian lận:** tiết lộ bí mật nhà nước; "
            "xâm phạm quyền sở hữu trí tuệ; giả mạo trang thông tin điện tử; tạo đường dẫn trái phép "
            "tới tên miền hợp pháp; phát tán phần mềm độc hại; quảng cáo hàng hoá, dịch vụ bị cấm.",
        ]),
        BOX("Cách trả lời yêu cầu “trình bày một số nội dung cơ bản” và “giải thích kèm ví dụ”", [
            "**Cấu trúc 4 câu:** (1) nêu tên văn bản + năm; (2) nêu phạm vi điều chỉnh; "
            "(3) nêu 1–2 nhóm hành vi bị cấm; (4) nêu ví dụ minh hoạ và hậu quả.",
            "**Ví dụ mẫu:** “Luật Công nghệ thông tin 2006 điều chỉnh hoạt động ứng dụng và phát triển CNTT. "
            "Điều 12 cấm cung cấp, trao đổi, truyền đưa, lưu trữ thông tin số nhằm xuyên tạc, vu khống, "
            "xúc phạm danh dự nhân phẩm công dân. Ví dụ: đăng lên mạng tin bịa đặt bạn A lấy cắp tiền "
            "của lớp là hành vi trái luật, có thể bị xử phạt và phải bồi thường, xin lỗi công khai.”",
        ], "example"),

        H2("4.4. Bản quyền, quyền tác giả và sản phẩm số"),
        TBL(["Khái niệm", "Nội dung"], [
            ["**Quyền tác giả**", "Quyền của tổ chức, cá nhân đối với tác phẩm do mình sáng tạo hoặc sở hữu. "
                                 "Phát sinh **từ khi tác phẩm được sáng tạo** và thể hiện dưới hình thức "
                                 "vật chất nhất định (không cần đăng kí)."],
            ["**Quyền nhân thân**", "Gắn với tác giả: đặt tên tác phẩm, đứng tên thật/bút danh, "
                                    "được nêu tên khi tác phẩm công bố, bảo vệ sự toàn vẹn của tác phẩm."],
            ["**Quyền tài sản**", "Khai thác tác phẩm để thu lợi: sao chép, làm tác phẩm phái sinh, "
                                  "truyền đạt tới công chúng, cho thuê bản gốc."],
            ["**Bản quyền (copyright)**", "Nhấn mạnh quyền **sao chép, phân phối, khai thác** tác phẩm. "
                                          "Mẹo: *“Quyền tác giả – nhìn người; bản quyền – nhìn bản (tác phẩm)”*."],
            ["**Sản phẩm số**", "Phần mềm, ảnh, nhạc, video, văn bản, cơ sở dữ liệu được lưu dưới dạng dữ liệu số."],
        ], widths=[118, 393], fs=8.2),
        TBL(["Hành vi vi phạm", "Vi phạm diễn ra thế nào?", "Hậu quả"], [
            ["Tải và dùng phần mềm bẻ khoá (crack)",
             "Sao chép, cài đặt phần mềm không có giấy phép; vượt qua biện pháp bảo vệ của tác giả.",
             "Mất an toàn (thường kèm mã độc), bị xử phạt, không được cập nhật."],
            ["Lấy ảnh trên mạng đưa vào bài thuyết trình không ghi nguồn",
             "Sao chép và truyền đạt tác phẩm tới công chúng mà không có sự đồng ý, "
             "không nêu tên tác giả.",
             "Bị yêu cầu gỡ bài, xin lỗi, bồi thường; bài bị đánh giá là đạo văn."],
            ["Đăng lại toàn bộ bài viết/nhạc/phim của người khác",
             "Sao chép nguyên tác phẩm, có thể còn thu lợi từ quảng cáo.",
             "Xử phạt hành chính, bồi thường thiệt hại, tài khoản bị khoá."],
            ["Chép bài của bạn rồi nộp cho giáo viên",
             "Chiếm đoạt quyền nhân thân (tự nhận là tác giả).",
             "Bị kỉ luật, mất điểm, mất uy tín cá nhân."],
        ], widths=[128, 235, 148], fs=8.1),
        P("**Khía cạnh pháp lí của việc sở hữu, sử dụng, trao đổi thông tin số cần nhớ:** "
          "① dữ liệu số là một dạng **tài sản** được pháp luật bảo vệ; ② thông tin cá nhân chỉ được "
          "thu thập, sử dụng khi có sự đồng ý hoặc theo quy định; ③ quyền sử dụng tác phẩm **không đồng nghĩa "
          "với quyền sở hữu** (mua một bài hát không có quyền đăng lại cho mọi người); ④ khi trao đổi "
          "thông tin qua mạng vẫn phải chịu trách nhiệm về nội dung mình phát tán."),
        BOX("Cách tôn trọng bản quyền khi học tập", [
            "Ghi rõ **tên tác giả + nguồn + giấy phép** khi dùng ảnh, nhạc, văn bản của người khác.",
            "Ưu tiên **phần mềm miễn phí hợp pháp / nguồn mở** thay vì bản crack.",
            "**Trích dẫn vừa đủ**, không làm sai lệch ý tác giả; không chép nguyên bài để nộp.",
            "Tự tạo dữ liệu của mình (tự chụp ảnh, tự vẽ, tự viết) là cách an toàn nhất.",
            "Kiểm tra giấy phép chia sẻ (ví dụ Creative Commons: BY, SA, NC, ND) trước khi dùng lại.",
        ], "tip"),

        H2("4.5. Tác hại của việc chia sẻ, phổ biến thông tin bất cẩn"),
        TBL(["Đối tượng", "Tác hại cụ thể"], [
            ["Bản thân", "Bị xử phạt, mất tài khoản, lộ thông tin cá nhân, bị lừa ngược lại, "
                         "ảnh hưởng hồ sơ học tập và cơ hội nghề nghiệp sau này."],
            ["Người khác", "Bị xúc phạm danh dự, bị bôi nhọ, bị lộ bí mật riêng tư, tổn thương tinh thần."],
            ["Cộng đồng", "Tin giả lan nhanh gây hoang mang, kì thị, mất niềm tin vào thông tin chính thống."],
            ["Kinh tế – xã hội", "Gây thiệt hại cho doanh nghiệp, cản trở hoạt động của cơ quan nhà nước, "
                                 "làm giảm động lực sáng tạo nếu bản quyền không được tôn trọng."],
        ], widths=[100, 411], fs=8.3),

        H2("4.6. Biện pháp chia sẻ thông tin an toàn, hợp pháp"),
        OL([
            "**Kiểm tra nguồn:** xác định ai đăng, khi nào, có đáng tin cậy không; đối chiếu ít nhất 2 nguồn.",
            "**Không chia sẻ tin vi phạm pháp luật:** tin sai sự thật, tin kích động bạo lực, "
            "thông tin dâm ô, hàng hoá/dịch vụ bị cấm.",
            "**Tôn trọng bản quyền:** xin phép hoặc dùng nguồn mở, ghi rõ nguồn và tác giả, "
            "không đăng lại nguyên tác phẩm khi chưa được phép.",
            "**Bảo vệ thông tin cá nhân:** không đăng số điện thoại, địa chỉ, CCCD, ảnh riêng tư của "
            "mình và của người khác; che thông tin nhạy cảm trong ảnh chụp màn hình.",
            "**Cân nhắc đạo đức và văn hoá:** dù tin đúng, vẫn tự hỏi “chia sẻ thế này có làm ai tổn thương không?”",
            "**Chủ động báo cáo:** dùng nút báo cáo trên nền tảng; thông báo cho giáo viên, "
            "phụ huynh hoặc cơ quan chức năng khi phát hiện nội dung xấu.",
        ]),
        BOX("Ba nguyên tắc vàng khi chia sẻ (theo SGK)", [
            "1. **Trước khi đăng:** kiểm tra xem tin bài có vi phạm pháp luật không.",
            "2. **Không chia sẻ** tin bài vi phạm pháp luật; biết cách nhận biết tin thật – tin giả.",
            "3. **Dù không vi phạm pháp luật**, vẫn cân nhắc hậu quả, nhất là về mặt đạo đức.",
            "*Tình huống kinh điển:* nhận tin “Trường mình sắp nghỉ một tuần, chuyển cho cả lớp ngay!” "
            "→ hãy kiểm tra website trường/hỏi giáo viên **trước khi chuyển tiếp**.",
        ], "memory"),

        H2("4.7. Khung 5 bước xác định tính hợp pháp của một hành vi (câu Vận dụng cao)"),
        TBL(["Bước", "Câu hỏi dẫn", "Cách trình bày"], [
            ["1", "**Hành vi là gì?**", "Mô tả ngắn gọn, chính xác hành vi đang xét."],
            ["2", "**Ai/ cái gì bị tác động?**", "Nêu người bị hại, dữ liệu, tác phẩm, hệ thống bị ảnh hưởng."],
            ["3", "**Đối chiếu văn bản nào?**", "Nêu tên luật/nghị định và nhóm hành vi bị cấm tương ứng."],
            ["4", "**Hợp pháp hay không?**", "Kết luận dứt khoát + giải thích vì sao."],
            ["5", "**Xử lí thế nào?**", "Đề xuất 2–3 việc nên làm (gỡ bài, xin lỗi, báo cáo, xin phép, ghi nguồn…)."],
        ], widths=[40, 150, 321], fs=8.2),

        H3("4.7.1. Bốn tình huống luyện tập (kèm lời giải mẫu)"),
        BOX("Tình huống 1 – Bắt nạt và hình ảnh cá nhân", [
            "**Đề:** Bạn An chụp ảnh bạn Bình ngủ gật trong giờ học, đăng lên nhóm lớp kèm lời chế giễu. "
            "Hãy xác định tính hợp pháp và đề xuất cách xử lí.",
            "**Gợi ý đáp án:** Hành vi đăng ảnh + lời chế giễu (bước 1) tác động trực tiếp đến hình ảnh, "
            "danh dự và nhân phẩm của Bình (bước 2). Luật Công nghệ thông tin (Điều 12) và Luật An ninh mạng "
            "cấm xuyên tạc, vu khống, xúc phạm danh dự nhân phẩm; việc công bố hình ảnh cá nhân khi chưa "
            "được phép cũng xâm phạm quyền riêng tư (bước 3). **Kết luận: không hợp pháp**, đồng thời vi phạm "
            "đạo đức, văn hoá ứng xử (bước 4). Cách xử lí: An phải **xoá bài ngay, xin lỗi Bình**, "
            "nhờ giáo viên chủ nhiệm hoà giải; Bình nên **lưu bằng chứng (chụp màn hình)** và báo với "
            "thầy cô/bố mẹ; cả lớp không chia sẻ tiếp ảnh đó (bước 5).",
        ], "example"),
        BOX("Tình huống 2 – Vi phạm bản quyền sản phẩm số", [
            "**Đề:** Nhóm làm bài thuyết trình, tải một bản nhạc đang bán trên mạng và 3 ảnh từ một "
            "trang web báo để đưa vào slide, không ghi nguồn, rồi đăng video bài thuyết trình lên mạng xã hội.",
            "**Gợi ý đáp án:** Hành vi sao chép, truyền đạt tác phẩm tới công chúng khi chưa có sự đồng ý "
            "của chủ thể quyền, không nêu tên tác giả (bước 1–2). Theo Luật Công nghệ thông tin "
            "(Điều 12 cấm xâm phạm quyền sở hữu trí tuệ trong hoạt động CNTT) và quy định về quyền tác giả, "
            "quyền tài sản của tác giả bị xâm phạm (bước 3). **Kết luận: không hợp pháp** (bước 4). "
            "Cách xử lí: gỡ video, thay bằng nhạc/ảnh có giấy phép mở hoặc tự tạo, **ghi rõ tác giả + nguồn**, "
            "nếu muốn dùng tác phẩm thương mại phải xin phép và trả nhuận bút; lần sau lập danh mục nguồn "
            "ngay khi làm slide (bước 5).",
        ], "example"),
        BOX("Tình huống 3 – Tin giả", [
            "**Đề:** Nhận được tin nhắn “Trường mình nghỉ học một tuần, chuyển cho cả lớp ngay!”, "
            "không có thông báo chính thức. Bạn nên làm gì?",
            "**Gợi ý đáp án:** Hành vi đang xét là **chuyển tiếp thông tin chưa được kiểm chứng**; "
            "nếu tin sai sẽ gây hoang mang cho học sinh, phụ huynh, ảnh hưởng hoạt động của nhà trường. "
            "Luật Công nghệ thông tin (Điều 12) và Luật An ninh mạng (Điều 8) cấm đưa thông tin sai sự thật "
            "gây hoang mang trong Nhân dân. Vì vậy **không chuyển tiếp ngay**. Cách xử lí: kiểm tra website/"
            "fanpage chính thức của trường, hỏi giáo viên chủ nhiệm; nếu xác định là tin giả, "
            "**báo lại cho người gửi và cả lớp** biết sự thật, báo cáo nội dung sai phạm trên nền tảng. "
            "Chia sẻ lại tin giả dù “chỉ chuyển tiếp” vẫn có thể bị coi là truyền đưa thông tin trái phép.",
        ], "example"),
        BOX("Tình huống 4 – Hành vi hợp pháp để phân biệt", [
            "**Đề:** Bạn Lan mượn một bức ảnh có giấy phép Creative Commons (CC BY) từ Wikimedia Commons, "
            "ghi rõ tên tác giả, nguồn và giấy phép dưới ảnh trong bài báo cáo. Hành vi này có hợp pháp không?",
            "**Gợi ý đáp án:** **Hợp pháp.** Ảnh được tác giả cho phép sử dụng với điều kiện ghi nhận "
            "(BY); Lan đã ghi rõ tên tác giả, nguồn và giấy phép, không làm sai lệch nội dung. "
            "Đây là cách khai thác **học liệu mở** đúng quy định, vừa an toàn về pháp lí vừa thể hiện "
            "văn hoá tôn trọng bản quyền. Lưu ý: nếu giấy phép có thêm điều kiện NC (phi thương mại) "
            "hoặc ND (không sửa đổi) thì phải tuân thủ thêm các điều kiện đó.",
        ], "example"),

        H2("4.8. Ghi nhớ nhanh D1"),
        BOX("D1 trong 6 dòng", [
            "1. **3 trụ:** đạo đức – pháp luật – văn hoá.",
            "2. **7 hành vi vi phạm** = 3 nhóm (nội dung, cách gửi, cách đối xử) + vi phạm bản quyền.",
            "3. **3 văn bản luật:** Luật Giao dịch điện tử 2005, Luật CNTT 2006, Luật ANM 2018; "
            "**2 nghị định:** 90/2008, 72/2013.",
            "4. **4 nhóm cấm:** an ninh quốc gia · bạo lực/tệ nạn · tin sai/xúc phạm · "
            "bí mật/SHTT/gian lận.",
            "5. Quyền tác giả = **nhân thân + tài sản**; phát sinh khi sáng tạo, không cần đăng kí.",
            "6. **3 nguyên tắc chia sẻ** + **khung 5 bước** để chinh phục câu Vận dụng cao.",
        ], "memory"),
        PB(),
    ]
    return B
