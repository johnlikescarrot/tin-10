# -*- coding: utf-8 -*-
"""Phụ lục A (toàn văn tài liệu gốc – sinh tự động) và các phụ lục B, C, D."""
from .blocks import H1, H2, H3, P, LEAD, SMALL, UL, OL, TBL, BOX, PB, SP, CHECK

LEVEL_LABELS = ["NB\nTN", "NB\nĐS", "NB\nTL", "TH\nTN", "TH\nĐS", "TH\nTL",
                "VD\nTN", "VD\nĐS", "VD\nTL", "VDC\nTN", "VDC\nĐS", "VDC\nTL"]


def _verbatim_lines(row):
    """Giữ nguyên dấu gạch đầu dòng của bản gốc (không thêm bullet thứ hai)."""
    out = []
    for line in row["lines"]:
        t = line.strip()
        if not t:
            continue
        if t in ("Nhận biết", "Thông hiểu", "Vận dụng", "Vận dụng cao"):
            out.append(P(f"**{t}**", "small"))
        else:
            out.append(P(t, "verbatim"))
    return out


def src_appendix_blocks(source):
    """Tái tạo nguyên văn 2 bảng của file .docx."""
    B = [
        H1("PHỤ LỤC A · TOÀN VĂN TÀI LIỆU GỐC"),
        LEAD("Phụ lục này được **sinh tự động từ file `MA TRAN GIUA KI I - LOP 10.docx`** "
             "(đọc trực tiếp `word/document.xml`), không qua gõ lại thủ công. "
             "Mục đích: bảo đảm không một dòng nào của tài liệu gốc bị bỏ sót, "
             "kể cả các ô trống và các con số trong ma trận."),

        H2("A.1. Phần văn bản thông tin chung (nguyên văn)"),
        TBL(["STT", "Nội dung nguyên văn"],
            [[str(i), t] for i, t in enumerate(source["intro"], 1)],
            widths=[34, 477], fs=8.4),
        P("*Chú thích:* dòng 6 có “10% Thông biểu” – lỗi chính tả của “Thông hiểu” trong bản gốc; "
          "dòng 9 là tiêu đề của bảng đặc tả. Các dòng này được giữ nguyên, không hiệu đính."),

        H2("A.2. Ma trận đề kiểm tra giữa kì I (nguyên dạng 16 cột)"),
        P("Bảng gốc có 3 dòng tiêu đề ghép cột. Để in vừa khổ A4, phần đầu được gộp thành "
          "các ô hai dòng (ví dụ `NB / TN` = Nhận biết – Trắc nghiệm). **Toàn bộ giá trị ô "
          "được giữ nguyên**, kể cả các ô “2 ý”, “1” và ô trống."),
        TBL(["TT", "Nội dung kiến thức / kĩ năng", "Đơn vị kiến thức / kĩ năng"]
            + LEVEL_LABELS + ["Tổng % điểm"],
            [[r["tt"], r["chude"], r["donvi"]] + r["levels"] + [r["total"]]
             for r in source["matrix_rows"]],
            widths=[18, 82, 104] + [21] * 12 + [46], fs=6.5, zebra=False,
            align="center",
            caption="Bảng A.1 – Ma trận đề (nguyên văn số liệu). "
                    "NB/TH/VD/VDC = 4 mức độ nhận thức; TN/ĐS/TL = 3 hình thức câu hỏi."),
        SP(4),
        H3("Các dòng tổng hợp của ma trận"),
        TBL(["Dòng"] + [x.replace("\n", " ") for x in LEVEL_LABELS],
            [["**Tổng**"] + [x or "—" for x in source["matrix_summary"][0][1:13]]],
            widths=[46] + [38.7] * 12, fs=7.4, zebra=False, align="center"),
        SP(3),
        TBL(["Dòng", "Giá trị nguyên văn (theo thứ tự ô trong bảng gốc)"],
            [["**Tỉ lệ % từng mức độ nhận thức**",
              " · ".join(x or "—" for x in source["matrix_summary"][1])],
             ["**Tỉ lệ chung**",
              " · ".join(x or "—" for x in source["matrix_summary"][2])]],
            widths=[150, 361], fs=8.0),
        P("*Giải mã dòng Tổng:* 16 câu TN Nhận biết · 4 câu TN Thông hiểu · 4 ý ĐS Thông hiểu · "
          "1 câu TL Thông hiểu · 4 ý ĐS Vận dụng · 1 câu TL Vận dụng · 1 câu TL Vận dụng cao. "
          "Dòng “Tỉ lệ % từng mức độ nhận thức” ghi 40 – 30 – 20 – 10 – 10 và dòng “Tỉ lệ chung” "
          "ghi 70 – 30 – 100 (tổng 100%)."),

        H2("A.3. Đặc tả đề kiểm tra giữa kì I (nguyên văn)"),
    ]

    for row in source["spec_rows"]:
        B += [
            H3(f"{row['tt']}. {row['chude']} — {row['donvi']}"),
            TBL(["Mức độ", "Số câu hỏi theo mức độ nhận thức"],
                [["Nhận biết", row["counts"][0] or "(trống)"],
                 ["Thông hiểu", row["counts"][1] or "(trống)"],
                 ["Vận dụng", row["counts"][2] or "(trống)"],
                 ["Vận dụng cao", row["counts"][3] or "(trống)"]],
                widths=[150, 361], fs=8.2, zebra=False),
            P("**Mức độ kiến thức, kĩ năng cần kiểm tra, đánh giá (nguyên văn):**"),
        ]
        B += _verbatim_lines(row)

    B += [
        H3("Dòng tỉ lệ của bảng đặc tả"),
        TBL(["Dòng", "Giá trị nguyên văn"],
            [["**Tỉ lệ %**", " · ".join(source["spec_summary"][0][1:])],
             ["**Tỉ lệ chung**", " · ".join(source["spec_summary"][1][1:])]],
            widths=[150, 361], fs=8.2),

        H2("A.4. Biên bản đối soát: 35/35 yêu cầu được giữ lại"),
        TBL(["Hạng mục đối soát", "Kết quả"], [
            ["Số dòng văn bản thông tin chung", f"**{len(source['intro'])}** dòng – đã chép nguyên văn ở A.1."],
            ["Số dòng dữ liệu của ma trận", f"**{len(source['matrix_rows'])}** đơn vị kiến thức – đủ 12 cột mức độ ở A.2."],
            ["Số dòng tổng hợp của ma trận", "**3** dòng (Tổng, Tỉ lệ %, Tỉ lệ chung) – đủ ở A.2."],
            ["Số dòng dữ liệu của đặc tả", f"**{len(source['spec_rows'])}** đơn vị – đủ nội dung và số câu ở A.3."],
            ["Số yêu cầu cần đạt (dòng gạch đầu dòng)", f"**{len(source['bullets'])}** yêu cầu – "
             "tất cả có mặt nguyên văn ở A.3 và có đáp án ở Phần 5."],
            ["Câu hỏi / đáp án cụ thể trong bản gốc", "**Không có.** Bản gốc là ma trận và đặc tả đề "
             "(7 trang, 859 chữ), không chứa đề thi hay đáp án. Đề cương đã chuyển 35/35 yêu cầu "
             "thành câu hỏi có đáp án và bổ sung đề thi thử ở Phần 6."],
        ], widths=[190, 321], fs=8.2),
        BOX("Ba điểm chưa khớp giữa ma trận và đặc tả (đã được xử lí an toàn)", [
            "**1.** Đặc tả ghi câu tự luận của B2 ở mức **Vận dụng**, nhưng ma trận xếp ở mức "
            "**Thông hiểu**. Đề cương ôn B2 ở cả hai mức và đưa câu tự luận Thông hiểu vào đề thử.",
            "**2.** Đặc tả ghi 4 câu TN của D1 đều ở mức Nhận biết và 2 câu TN Thông hiểu thuộc B2; "
            "ma trận lại xếp D1 = 2 câu Nhận biết + 2 câu Thông hiểu. Vì vậy A1, B2, D1 đều "
            "được luyện câu Thông hiểu.",
            "**3.** Đơn vị A3 (kĩ năng sử dụng thiết bị số) có 2 yêu cầu trong đặc tả nhưng "
            "**không có ô điểm riêng** trong ma trận. Đề cương vẫn trình bày đầy đủ A3 ở mục 2.3 "
            "và dùng chúng trong câu Vận dụng.",
        ], "note"),
        PB(),
    ]
    return B


def other_appendix_blocks():
    return [
        H1("PHỤ LỤC B · ÁNH XẠ SANG SGK KẾT NỐI TRI THỨC VỚI CUỘC SỐNG"),
        LEAD("Bản ma trận gốc dùng kí hiệu **Chủ đề A – B – D** của Chương trình GDPT 2018; "
             "SGK **Kết nối tri thức với cuộc sống** đánh số **Chủ đề 1 – 2 – 3**. "
             "Bảng dưới đây giúp bạn tra cứu đúng bài học trong sách."),
        TBL(["Tên trong bản gốc", "Chủ đề / bài SGK KNTT", "Nội dung trọng tâm", "Vị trí trong đề cương"], [
            ["A. Máy tính và xã hội tri thức", "**Chủ đề 1** – Bài 1, 2, 7 "
                                              "(nền tảng: Bài 3, 4, 5, 6)",
             "Thông tin & xử lí thông tin; thiết bị thông minh; kiểu dữ liệu, nhị phân, "
             "dữ liệu logic, âm thanh, hình ảnh; thực hành thiết bị số.", "Phần 2"],
            ["A1. Dữ liệu, thông tin và xử lý thông tin", "**Bài 1** (+ Bài 3–6)",
             "Dữ liệu ↔ thông tin; quy trình xử lí; đơn vị lưu trữ; ưu việt lưu trữ số.", "2.1"],
            ["A2. Vai trò của máy tính và thiết bị thông minh", "**Bài 2**",
             "Đóng góp của tin học; mốc phát triển; thiết bị thông minh; CMCN 4.0; kinh tế tri thức.", "2.2"],
            ["A3. Kĩ năng sử dụng thiết bị số", "**Bài 7**",
             "PDA, hệ điều hành di động, nút bấm, màn hình, quản lí tệp, ứng dụng cài sẵn.", "2.3"],
            ["B. Mạng máy tính và Internet", "**Chủ đề 2** – Bài 8, 9, 10",
             "Mạng LAN/Internet; đám mây; IoT; an toàn không gian mạng; khai thác tài nguyên Internet.",
             "Phần 3"],
            ["B1. Khái niệm mạng, Internet, IoT", "**Bài 8**",
             "LAN và Internet; vai trò Internet; SaaS/PaaS/IaaS; IoT.", "3.1"],
            ["B2. Dịch vụ web & tự bảo vệ", "**Bài 9 và Bài 10**",
             "Nguy cơ, bắt nạt, phần mềm độc hại, Windows Defender; học liệu mở, dịch tự động.", "3.2"],
            ["D. Đạo đức, pháp luật, văn hoá số", "**Chủ đề 3** – Bài 11",
             "Ứng xử trên môi trường số; luật và nghị định; quyền tác giả, bản quyền; chia sẻ thông tin.",
             "Phần 4"],
        ], widths=[124, 104, 218, 65], fs=8.1,
               caption="Bảng B.1 – Phạm vi giữa kì I theo SGK là **Bài 1 – Bài 11** "
                       "(Chủ đề 4 “Ứng dụng tin học” trở đi nằm sau kì thi)."),
        BOX("Gợi ý khi tra cứu", [
            "Nếu trường bạn dùng bộ sách khác (Cánh Diều, Chân trời sáng tạo) thì tên chủ đề A–B–D "
            "trong bản gốc sẽ trùng trực tiếp; nội dung kiến thức trong đề cương vẫn dùng được "
            "vì cùng bám Chương trình GDPT 2018 môn Tin học.",
            "Bài 3–6 (kiểu dữ liệu, hệ nhị phân, dữ liệu logic, âm thanh/hình ảnh) không nằm "
            "trong ma trận nhưng là kiến thức nền – đã được tóm tắt ở mục 2.1.6.",
        ], "note"),

        H1("PHỤ LỤC C · BẢNG THUẬT NGỮ VÀ TỪ VIẾT TẮT"),
        TBL(["Thuật ngữ / viết tắt", "Tên đầy đủ", "Nghĩa ngắn gọn"], [
            ["**ICT**", "Information and Communication Technology", "Công nghệ thông tin và truyền thông."],
            ["**bit / byte**", "binary digit / byte", "Đơn vị nhỏ nhất (0/1) / nhóm 8 bit."],
            ["**KB, MB, GB, TB**", "Kilo/Mega/Giga/Tera Byte", "Mỗi bậc gấp 1024 lần bậc trước."],
            ["**AI**", "Artificial Intelligence", "Trí tuệ nhân tạo."],
            ["**IoT**", "Internet of Things", "Internet vạn vật."],
            ["**CMCN 4.0**", "Cách mạng công nghiệp lần thứ tư", "AI + IoT + Big Data + Cloud."],
            ["**PDA**", "Personal Digital Assistant", "Trợ thủ số cá nhân (điện thoại, tablet…)."],
            ["**PAN / LAN / MAN / WAN**", "Personal/Local/Metropolitan/Wide Area Network",
             "Mạng cá nhân / cục bộ / đô thị / diện rộng."],
            ["**TCP/IP**", "Transmission Control Protocol / Internet Protocol",
             "Bộ giao thức nền tảng của Internet (1983)."],
            ["**IP / DNS**", "Internet Protocol / Domain Name System",
             "Địa chỉ số của thiết bị / hệ thống dịch tên miền sang IP."],
            ["**WWW / URL / HTTP(S)**", "World Wide Web / Uniform Resource Locator / HyperText Transfer Protocol",
             "Dịch vụ web / địa chỉ trang web / giao thức truyền tải (có mã hoá)."],
            ["**ISP**", "Internet Service Provider", "Nhà cung cấp dịch vụ Internet."],
            ["**SaaS / PaaS / IaaS**", "Software/Platform/Infrastructure as a Service",
             "Phần mềm / nền tảng / hạ tầng như là dịch vụ."],
            ["**OER**", "Open Educational Resources", "Học liệu mở, được phép dùng và chia sẻ có điều kiện."],
            ["**CC (BY, NC, ND, SA)**", "Creative Commons",
             "Giấy phép mở: ghi nhận, phi thương mại, không sửa đổi, chia sẻ tương tự."],
            ["**Malware**", "Malicious Software", "Phần mềm độc hại nói chung."],
            ["**Virus / Worm / Trojan**", "—", "Đoạn mã kí sinh / sâu tự lây / phần mềm nội gián."],
            ["**Spyware / Keylogger / Ransomware**", "—",
             "Gián điệp / ghi bàn phím / mã hoá dữ liệu đòi tiền chuộc."],
            ["**Phishing**", "—", "Lừa đảo giả danh để lấy thông tin, mật khẩu."],
            ["**2FA / OTP**", "Two-Factor Authentication / One-Time Password",
             "Xác thực 2 yếu tố / mật khẩu dùng một lần."],
            ["**Luật CNTT / Luật ANM**", "Luật Công nghệ thông tin 2006 / Luật An ninh mạng 2018",
             "Hai văn bản pháp lí trọng tâm của Bài 11."],
            ["**NĐ 72/2013**", "Nghị định 72/2013/NĐ-CP",
             "Quản lí, cung cấp, sử dụng dịch vụ Internet và thông tin trên mạng."],
        ], widths=[104, 168, 239], fs=8.0),

        H1("PHỤ LỤC D · PHIẾU TỰ KIỂM TRA TRƯỚC KHI VÀO PHÒNG THI"),
        P("Hãy tick vào ô vuông. Nếu còn ô trống, quay lại mục đã ghi trong ngoặc."),
        CHECK("Khối kiến thức A (Chủ đề 1)", [
            "Giải thích được dữ liệu khác thông tin và nêu được 1 ví dụ cụ thể. (2.1.1)",
            "Viết được quy trình TLXT và mô tả được quá trình gửi một tệp. (2.1.2, 2.1.5)",
            "Thuộc bảng đơn vị lưu trữ và làm đúng 3 bài đổi đơn vị liên tiếp. (2.1.3)",
            "Nêu được 6 ưu việt của lưu trữ trên thiết bị số. (2.1.4)",
            "Kể được 5 đóng góp của tin học, mỗi ý kèm 1 ví dụ. (2.2.2)",
            "Nhớ 3 mốc 1957 – 1983 – 1992 và 4 nhóm thành tựu. (2.2.3)",
            "Giải thích được vì sao thiết bị thông minh là hệ thống xử lí thông tin. (2.2.1)",
            "Nêu được vai trò thiết bị thông minh trong CMCN 4.0 kèm ví dụ xe tự hành. (2.2.5)",
            "Kể được 5 nhóm thiết bị số khác ngoài PC/laptop. (2.2.4)",
            "Thực hiện được khởi động, mở/xem/sao chép/xoá tệp và dùng 3 app cài sẵn. (2.3)",
        ]),
        CHECK("Khối kiến thức B (Chủ đề 2)", [
            "Nêu được định nghĩa mạng máy tính và 5 thành phần. (3.1.1)",
            "Phân biệt PAN – LAN – MAN – WAN và so sánh LAN với Internet. (3.1.2)",
            "Trình bày được 3 thay đổi lớn về sống – học – làm việc nhờ mạng. (3.1.3)",
            "Kể được 5 dịch vụ đám mây cụ thể và phân biệt IaaS – PaaS – SaaS. (3.1.4)",
            "Nêu được khái niệm IoT, 4 lớp kiến trúc và 3 lợi ích kèm ví dụ. (3.1.5)",
            "Nêu được 5 nguy cơ khi dùng Internet và 5 cách phòng vệ. (3.2.4)",
            "Nhớ 6 bước xử lí khi bị bắt nạt trên mạng. (3.2.4)",
            "Kể được 8 dạng mã độc và 4 chế độ quét của Windows Defender. (3.2.3)",
            "Mô tả được 3 cách nhập của Google Translate và 5 bước kiểm tra nguồn tin. (3.2.1, 3.2.2)",
            "Kể được 4 nguồn học liệu mở và nhớ phải ghi nguồn. (3.2.2)",
        ]),
        CHECK("Khối kiến thức D (Chủ đề 3)", [
            "Kể được 7 hành vi vi phạm thường gặp trên mạng. (4.2)",
            "Nhớ 3 luật + 2 nghị định và nội dung chính của từng văn bản. (4.3)",
            "Gộp được các hành vi bị cấm thành 4 nhóm và nêu ví dụ cho mỗi nhóm. (4.3.1)",
            "Phân biệt quyền nhân thân – quyền tài sản; bản quyền – quyền tác giả. (4.4)",
            "Phân tích được một vụ vi phạm bản quyền theo “hành vi – cách thức – hậu quả”. (4.4)",
            "Nêu được 6 biện pháp chia sẻ thông tin an toàn, hợp pháp. (4.6)",
            "Nhớ 3 nguyên tắc vàng khi chia sẻ và khung 5 bước xác định tính hợp pháp. (4.6, 4.7)",
            "Giải được 4 tình huống mẫu mà không nhìn đáp án. (4.7.1)",
        ]),
        CHECK("Kĩ năng làm bài", [
            "Đọc xong 35 câu ở Phần 5 và tự trả lời được ít nhất 30 câu. (Phần 5)",
            "Làm xong đề thử Phần 6 trong đúng 45 phút và tự chấm. (Phần 6)",
            "Biết phân bổ 16 câu Nhận biết ở những đơn vị nào. (Phần 0)",
            "Viết được dàn ý 3 câu tự luận trong 5 phút đầu giờ thi.",
        ]),

        H1("LỜI KHUYÊN CUỐI CÙNG TRƯỚC GIỜ THI"),
        BOX("7 điều nên nhớ", [
            "**1. Đọc kĩ từ phủ định:** “KHÔNG”, “chỉ”, “luôn”, “không cần” là nơi đặt bẫy.",
            "**2. 16 câu Nhận biết lấy trước:** làm chắc 4,0 điểm rồi hãy vào câu khó.",
            "**3. Câu đúng/sai:** xét từng ý độc lập; một ý sai không kéo theo các ý khác.",
            "**4. Bài toán đổi đơn vị:** luôn viết `×1024` hay `÷1024` và ghi đơn vị sau mỗi bước.",
            "**5. Câu giải thích:** dùng cấu trúc “Khái niệm → Đặc điểm → Ví dụ cụ thể → Kết luận”.",
            "**6. Câu Vận dụng cao:** dùng khung 5 bước ở mục 4.7; đừng quên nêu tên văn bản pháp luật.",
            "**7. Rà soát 2 phút cuối:** kiểm tra còn sót câu nào chưa tô đáp án, nhất là 2 câu đúng/sai.",
        ], "memory"),
        P("*Chúc bạn ôn tập hiệu quả và đạt kết quả tốt trong bài kiểm tra giữa kì I môn Tin học 10!*"),
        SMALL("Tài liệu được biên soạn từ `MA TRAN GIUA KI I - LOP 10.docx` và đối chiếu với "
              "cấu trúc SGK Tin học 10 – bộ sách Kết nối tri thức với cuộc sống (Bài 1–11). "
              "Các ví dụ, bài tập và đề thi thử là nội dung biên soạn bổ sung nhằm phục vụ ôn tập."),
    ]
