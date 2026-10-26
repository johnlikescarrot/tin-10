# -*- coding: utf-8 -*-
"""Phần 2 – Chủ đề A (Chủ đề 1 KNTT): Máy tính và xã hội tri thức."""
from .blocks import H1, H2, H3, P, LEAD, SMALL, UL, OL, TBL, BOX, PB, SP, CHECK


def blocks():
    B = [
        H1("PHẦN 2 · CHỦ ĐỀ A: MÁY TÍNH VÀ XÃ HỘI TRI THỨC"),
        LEAD("Tương ứng **Chủ đề 1** trong SGK *Kết nối tri thức với cuộc sống* "
             "(Bài 1, 2, 7 là trọng tâm; Bài 3–6 là nền tảng biểu diễn dữ liệu). "
             "Chủ đề này chiếm **40% đề**, gồm 3 đơn vị: **A1** dữ liệu – thông tin, "
             "**A2** thiết bị thông minh, **A3** kĩ năng sử dụng thiết bị số."),
        BOX("Cái nhìn trong 1 phút", [
            "**A1** trả lời: thông tin được **lưu và xử lí** thế nào? → TLXT + đổi đơn vị.",
            "**A2** trả lời: ai **xử lí** thông tin? → thiết bị thông minh, tin học, CMCN 4.0.",
            "**A3** trả lời: con người **thao tác** ra sao? → khởi động, tệp, ứng dụng cài sẵn.",
        ], "memory"),

        # ------------------------------------------------------------- A1
        H2("2.1. A1 – Dữ liệu, thông tin và xử lý thông tin"),
        P("*SGK KNTT Bài 1 (và kiến thức nền Bài 3–6). Đặc tả yêu cầu: 2 câu Nhận biết, "
          "2 câu Thông hiểu, 1 câu tự luận Vận dụng.*"),

        H3("2.1.1. Phân biệt dữ liệu và thông tin"),
        TBL(["Tiêu chí", "Dữ liệu", "Thông tin"], [
            ["Bản chất", "Thông tin đã được **đưa vào máy tính** dưới dạng các kí hiệu "
                         "(số, chữ, bit, tín hiệu) để máy nhận biết và xử lí được.",
             "**Ý nghĩa** mà con người hiểu được sau khi tiếp nhận và giải thích dữ liệu."],
            ["Vai trò", "**Vật mang / nguyên liệu**.", "**Nội dung / kết quả**."],
            ["Ví dụ", "Dãy số `36.5`; các con số nhiệt độ đo hằng ngày; "
                      "tệp `anh.jpg` gồm các bit 0 và 1.",
             "“Bạn bị sốt nhẹ”; “Trái Đất đang ấm dần lên”."],
            ["Đặc điểm", "Có thể **lưu trữ, sao chép, truyền đi** mà không đổi.",
             "Chỉ có nghĩa khi có **ngữ cảnh** và người hiểu nó."],
        ], widths=[76, 220, 215], fs=8.3),
        P("**Bốn mối quan hệ “độc lập tương đối” (rất hay hỏi):**"),
        OL([
            "Cùng **một thông tin** có thể thể hiện bằng **nhiều loại dữ liệu** "
            "(“điểm 9” có thể là chữ số 9, mã nhị phân 1001, hay chữ “giỏi”).",
            "Dữ liệu **không đầy đủ** thì không xác định được chính xác thông tin "
            "(chỉ có số 36.5 chưa biết là nhiệt độ hay cân nặng).",
            "Cùng **một bộ dữ liệu**, cách xử lí khác nhau cho **thông tin khác nhau** "
            "(điểm của cả lớp → điểm trung bình hoặc điểm cao nhất).",
            "**Bộ dữ liệu khác nhau** vẫn có thể dẫn tới **cùng một thông tin** "
            "(nhiều phép đo khác nhau đều kết luận “trời đang mưa”).",
        ]),
        BOX("Ví dụ minh hoạ nên dùng trong bài thi", [
            "**Ví dụ 1:** Bảng nhiệt độ 30 ngày (`31, 32, 33, …`) là **dữ liệu**. "
            "Sau khi phần mềm tính trung bình và vẽ biểu đồ, kết luận “nhiệt độ tăng 1,2 °C” là **thông tin**.",
            "**Ví dụ 2:** Dãy bit trong tệp `nhac.mp3` là **dữ liệu**; giai điệu bạn nghe được là **thông tin**. "
            "Cùng bài hát ấy có thể lưu dưới dạng `.mp3`, `.wav`, `.flac` – cùng thông tin, khác dữ liệu.",
        ], "example"),

        H3("2.1.2. Quá trình xử lí thông tin – móc nhớ TLXT"),
        TBL(["Bước", "Tên", "Điều gì xảy ra", "Ví dụ"], [
            ["1", "**T**hu nhận (vào)", "Dữ liệu đi vào máy từ bàn phím, máy quét, cảm biến, tệp có sẵn.",
             "Nhập điểm kiểm tra; camera chụp ảnh."],
            ["2", "**L**ưu trữ", "Dữ liệu được ghi trên bộ nhớ/ổ cứng/thẻ nhớ/đám mây.",
             "Lưu tệp `diem.xlsx`, ảnh `.jpg`."],
            ["3", "**X**ử lí", "Biến đổi dữ liệu trong bộ nhớ để tạo dữ liệu mới.",
             "Tính điểm trung bình; nén ảnh; mã hoá."],
            ["4", "**T**ruyền / ra kết quả", "Hiển thị cho người hiểu hoặc truyền sang máy khác.",
             "In biểu đồ; gửi ảnh qua Wi-Fi/Zalo."],
        ], widths=[36, 96, 220, 159], fs=8.2),
        P("**Kết luận cốt lõi:** trong máy tính, **xử lí thông tin chính là xử lí dữ liệu**. "
          "Dữ liệu ở đầu ra có thể trở thành dữ liệu đầu vào cho một quá trình xử lí khác."),

        H3("2.1.3. Đơn vị lưu trữ – phải tính được, không chỉ học thuộc"),
        TBL(["Đơn vị", "Kí hiệu", "Giá trị", "Ghi nhớ"], [
            ["bit", "b", "0 hoặc 1 – đơn vị nhỏ nhất", "Máy tính chỉ hiểu 0 và 1"],
            ["byte", "B", "**1 B = 8 bit**", "Nhóm bit nhỏ nhất có thể truy cập"],
            ["Kilobyte", "KB", "1 KB = 2^10 B = **1024 B**", "**K**hoai"],
            ["Megabyte", "MB", "1 MB = 1024 KB = 1 048 576 B", "**M**ì"],
            ["Gigabyte", "GB", "1 GB = 1024 MB", "**G**à"],
            ["Terabyte", "TB", "1 TB = 1024 GB", "**T**ây"],
            ["Petabyte", "PB", "1 PB = 1024 TB", "Dùng cho trung tâm dữ liệu"],
        ], widths=[82, 66, 195, 168], fs=8.3,
               caption="Bảng 2.1 – Các đơn vị hơn kém nhau 2^10 = 1024 lần. "
                       "Mẹo: **Khoai Mì Gà Tây** = K – M – G – T."),
        BOX("Bài tập mẫu có lời giải (dạng câu tự luận Vận dụng)", [
            "**Bài 1.** Đổi 3,5 MB sang KB. → 3,5 × 1024 = **3584 KB**.",
            "**Bài 2.** 5 242 880 B bằng bao nhiêu MB? → 5 242 880 ÷ 1024 = 5120 KB; "
            "5120 ÷ 1024 = **5 MB**.",
            "**Bài 3.** Một USB 8 GB chứa được bao nhiêu ảnh 2 MB? "
            "→ 8 × 1024 = 8192 MB; 8192 ÷ 2 = **4096 ảnh**.",
            "**Bài 4.** Một văn bản 20 trang, mỗi trang 500 kí tự (1 kí tự = 1 B) chiếm bao nhiêu KB? "
            "→ 20 × 500 = 10 000 B ≈ **9,77 KB**.",
            "**Cách làm chung:** xác định chiều đổi (xuống → ×1024, lên → ÷1024), "
            "đếm số bậc, rồi nhân/chia liên tiếp. Luôn ghi đơn vị ở mỗi bước.",
        ], "example"),
        BOX("Lỗi hay mắc", [
            "Đổi **GB → KB** phải nhân **1024 hai lần**, không phải một lần.",
            "Phân biệt **b** (bit) và **B** (byte): 1 B = 8 b. Tốc độ mạng thường tính bằng bit/s.",
            "Đề có thể cho 1 MB = 10^6 B theo cách ghi của nhà sản xuất ổ cứng – "
            "**làm theo đúng quy ước đề bài nêu**; mặc định SGK là 1024.",
        ], "warn"),

        H3("2.1.4. Sự ưu việt của lưu trữ trên thiết bị số"),
        TBL(["Ưu điểm", "Giải thích", "So với lưu trữ truyền thống (giấy, băng từ)"], [
            ["Dung lượng lớn, giá rẻ", "Một thẻ nhớ vài chục GB chứa cả thư viện.", "Tiết kiệm không gian, chi phí."],
            ["Truy xuất và tìm kiếm nhanh", "Gõ từ khoá là ra ngay tệp cần tìm.", "Không phải lật từng trang."],
            ["Sao chép không suy hao", "Bản sao là các bit giống hệt bản gốc.", "Giấy photo, băng từ giảm chất lượng."],
            ["Dễ sửa, dễ xử lí", "Sửa văn bản, cắt ảnh, tính toán tự động.", "Khó chỉnh sửa, dễ hỏng."],
            ["Truyền đi xa, tốc độ cao", "Gửi qua mạng trong vài giây.", "Phải vận chuyển vật lí."],
            ["Bền và dễ bảo vệ", "Sao lưu nhiều bản, đặt mật khẩu, mã hoá.", "Dễ mất, cháy, ẩm mốc."],
        ], widths=[108, 200, 203], fs=8.2),
        P("**Câu trả lời mẫu (Nhận biết):** “Lưu trữ trên thiết bị số cho dung lượng lớn với giá thành rẻ, "
          "tìm kiếm và xử lí nhanh, sao chép không làm giảm chất lượng, truyền đi xa với tốc độ rất lớn "
          "và dễ sao lưu, bảo mật.”"),

        H3("2.1.5. Xử lí và truyền thông tin bằng thiết bị số"),
        P("Một bài Vận dụng thường yêu cầu mô tả cả **chuỗi thao tác**. Hãy trả lời theo trình tự "
          "**nguồn → mã hoá → lưu → xử lí → truyền → giải mã → người nhận**."),
        BOX("Bài mẫu: gửi một bức ảnh cho bạn qua điện thoại", [
            "**Bước 1 (thu nhận):** cảm biến camera đổi ánh sáng thành tín hiệu số → tạo dữ liệu ảnh.",
            "**Bước 2 (xử lí):** chip xử lí ảnh, nén về định dạng `.jpg` để giảm dung lượng.",
            "**Bước 3 (lưu trữ):** tệp được ghi vào bộ nhớ máy (ví dụ 2,4 MB).",
            "**Bước 4 (truyền):** ứng dụng nhắn tin chia tệp thành gói tin, gửi qua Wi-Fi/4G "
            "đến máy chủ rồi tới máy bạn (cần địa chỉ người nhận).",
            "**Bước 5 (nhận và giải mã):** máy bạn giải nén, hiển thị ảnh – lúc này **dữ liệu trở thành thông tin**.",
            "**Nhận xét:** nếu mạng yếu thì thời gian truyền = dung lượng tệp ÷ tốc độ mạng; "
            "vì thế cần nén ảnh trước khi gửi.",
        ], "example"),

        H3("2.1.6. Ôn thêm: biểu diễn dữ liệu (Bài 3–6 – kiến thức nền)"),
        P("*Phần này không nằm trực tiếp trong ma trận nhưng giúp hiểu sâu A1 và là nền tảng cho "
          "các bài sau. Học ở mức nhận biết.*"),
        TBL(["Loại dữ liệu", "Cách biểu diễn trong máy tính", "Từ khoá"], [
            ["Văn bản", "Mỗi kí tự được gán một mã số (ASCII, Unicode/UTF-8).",
             "bảng mã, kí tự, 1 byte (ASCII)",],
            ["Số nguyên", "Biểu diễn trong hệ **nhị phân** (cơ số 2) bằng dãy bit.",
             "bit, 0/1, 2^10 = 1024"],
            ["Dữ liệu logic", "Chỉ có 2 giá trị: **đúng / sai** (true/false).",
             "phép AND, OR, NOT"],
            ["Âm thanh", "Lấy mẫu tín hiệu theo thời gian rồi lượng hoá thành số.",
             "tần số lấy mẫu, `.mp3`, `.wav`"],
            ["Hình ảnh", "Chia thành lưới **điểm ảnh (pixel)**, mỗi pixel có mã màu.",
             "pixel, độ phân giải, `.png`, `.jpg`"],
        ], widths=[84, 300, 127], fs=8.2),

        H3("2.1.7. Ghi nhớ nhanh A1"),
        BOX("A1 trong 6 dòng", [
            "1. **Dữ liệu** là vật mang; **thông tin** là ý nghĩa.",
            "2. Quy trình **TLXT**: Thu – Lưu – Xử – Truyền.",
            "3. 1 B = 8 bit; mỗi bậc **×1024** (Khoai Mì Gà Tây).",
            "4. Xử lí thông tin = **xử lí dữ liệu**.",
            "5. Ưu việt: **nhiều – nhanh – rẻ – không suy hao – dễ truyền – dễ bảo vệ**.",
            "6. Câu tự luận hay hỏi: **đổi đơn vị** hoặc **mô tả quá trình gửi một tệp**.",
        ], "memory"),
        PB(),

        # ------------------------------------------------------------- A2
        H2("2.2. A2 – Vai trò của máy tính và thiết bị thông minh trong nền kinh tế tri thức"),
        P("*SGK KNTT Bài 2. Đặc tả yêu cầu: 4 câu Nhận biết và 1 câu đúng/sai (gồm 2 ý Thông hiểu + 2 ý Vận dụng).*"),

        H3("2.2.1. Thiết bị thông minh là một hệ thống xử lí thông tin"),
        P("**Định nghĩa:** thiết bị thông minh là thiết bị điện tử có khả năng **hoạt động tự chủ** "
          "(không cần con người can thiệp thường xuyên), **tự thích ứng với hoàn cảnh** và "
          "**kết nối với thiết bị khác** để trao đổi dữ liệu. Nhờ **AI**, nhiều thiết bị còn "
          "“bắt chước” một vài hành vi, tư duy của con người."),
        TBL(["Thành phần", "Vai trò trong hệ xử lí thông tin", "Ví dụ"], [
            ["Cảm biến (vào)", "Thu nhận dữ liệu từ môi trường.", "Camera, cảm biến nhiệt độ, GPS, gia tốc kế"],
            ["Bộ vi xử lí (xử)", "Tính toán, ra quyết định, điều khiển.", "Chip ARM, vi điều khiển, AI chip"],
            ["Bộ nhớ (lưu)", "Giữ chương trình và dữ liệu.", "Bộ nhớ trong, thẻ nhớ"],
            ["Kết nối (truyền)", "Trao đổi dữ liệu qua mạng không dây.", "Wi-Fi, Bluetooth, 4G/5G, Zigbee"],
            ["Cơ cấu chấp hành (ra)", "Tác động trở lại môi trường.", "Màn hình, loa, mô tơ, van nước"],
        ], widths=[100, 200, 211], fs=8.2),
        P("**Câu trả lời mẫu (Thông hiểu):** “Điện thoại thông minh là một hệ thống xử lí thông tin vì nó "
          "có đầu vào (micro, camera, cảm ứng), bộ xử lí (chip), bộ nhớ, đầu ra (màn hình, loa) và khả năng "
          "truyền dữ liệu qua Wi-Fi/4G.”"),

        H3("2.2.2. Năm đóng góp cơ bản của tin học đối với xã hội"),
        TBL(["Đóng góp", "Giải thích", "Ví dụ minh hoạ cụ thể"], [
            ["**Quản lí**", "Xử lí nghiệp vụ nhanh, chính xác, tiết kiệm.",
             "Trường học quản lí học sinh; ngân hàng quản lí tài khoản, giao dịch."],
            ["**Tự động hoá**", "Thiết bị chạy theo chương trình thay con người.",
             "Robot hút bụi; robot làm việc trong nhà máy điện hạt nhân, dưới nước."],
            ["**Giải toán khoa học – kĩ thuật**", "Tính toán, mô phỏng, kiểm nghiệm tốc độ cao.",
             "Dự báo thời tiết; mô phỏng va chạm ô tô; giải mã gen."],
            ["**Đổi mới cách làm việc**", "Tăng chất lượng, hiệu quả của nhiều ngành nghề.",
             "Dạy học trực tuyến, mua sắm trực tuyến, làm việc từ xa, y tế từ xa."],
            ["**Giao tiếp cộng đồng**", "Trao đổi thông tin nhanh, không giới hạn khoảng cách.",
             "Thư điện tử, Zalo, mạng xã hội, diễn đàn, YouTube."],
        ], widths=[104, 178, 229], fs=8.2),
        P("**Cách trả lời câu “nêu ví dụ minh hoạ đóng góp của tin học”:** chọn 1 trong 5 nhóm trên, "
          "nêu **bối cảnh cụ thể + lợi ích đo được**. Ví dụ: “Nhờ phần mềm quản lí thư viện, "
          "việc mượn – trả sách từ 5 phút giảm còn 30 giây và không còn nhầm lẫn sách quá hạn.”"),

        H3("2.2.3. Các mốc thành tựu phát triển của ngành tin học"),
        TBL(["Mốc", "Thành tựu", "Ý nghĩa"], [
            ["1946", "Máy tính điện tử ENIAC (thế hệ đèn điện tử chân không).",
             "Máy tính điện tử đầu tiên, mở đầu kỉ nguyên tin học."],
            ["1947 – 1959", "Transitor (1947), mạch tích hợp IC (1958).",
             "Máy tính nhỏ hơn, nhanh hơn, tiêu thụ ít điện hơn (thế hệ 2, 3)."],
            ["1957", "Ngôn ngữ lập trình **FORTRAN** ra đời.",
             "Ngôn ngữ bậc cao đầu tiên: lập trình viên chỉ cần mô tả thuật toán."],
            ["1971", "Bộ vi xử lí Intel 4004.",
             "Mở đầu thế hệ 4 – máy tính cá nhân (PC) trở nên phổ biến."],
            ["1983", "Bộ giao thức **TCP/IP** được dùng cho Internet.",
             "Các mạng khác nhau nói cùng “ngôn ngữ” → Internet hình thành."],
            ["1992 *", "**World Wide Web** ra đời, giúp truy cập Internet dễ dàng.",
             "Web bùng nổ, Internet đến với mọi người. (*Theo SGK KNTT; "
             "nhiều tài liệu ghi 1989–1991.)"],
            ["Thập niên 2000", "Điện thoại thông minh, Wi-Fi, mạng 3G/4G.",
             "Internet di động; mạng xã hội, thương mại điện tử phát triển."],
            ["Thập niên 2010", "Điện toán đám mây, dữ liệu lớn, AI, IoT, CMCN 4.0.",
             "Sản xuất thông minh, xe tự hành, nhà thông minh, trợ lí ảo."],
        ], widths=[92, 220, 199], fs=8.1,
               caption="Bảng 2.2 – Các mốc theo SGK KNTT Bài 2, có bổ sung các mốc nền tảng. "
                       "Khi làm bài, ưu tiên số năm SGK nêu: 1957, 1983, 1992."),
        P("**Bốn nhóm thành tựu cần nhớ tên:** ① **Hệ điều hành** (DOS, Windows, macOS, Android, iOS) – "
          "quản lí phần cứng, tiến trình và giao diện; ② **Mạng và Internet** (TCP/IP, WWW); "
          "③ **Ngôn ngữ lập trình bậc cao** (FORTRAN, C, Pascal, Python, Java); "
          "④ **Hệ quản trị cơ sở dữ liệu** (Oracle, MySQL, MS SQL Server, DB2)."),

        H3("2.2.4. Các thiết bị số thông dụng ngoài máy tính để bàn và laptop"),
        TBL(["Nhóm", "Thiết bị", "Chức năng chính / dữ liệu xử lí"], [
            ["Cá nhân – di động", "Điện thoại thông minh, máy tính bảng, đồng hồ thông minh, "
                                 "thiết bị đeo tay (PDA).",
             "Gọi điện, nhắn tin, định vị, theo dõi sức khỏe; chạy iOS/Android."],
            ["Giải trí tại nhà", "Smart TV, loa thông minh, máy chơi game, đầu phát số.",
             "Xem phim, nghe nhạc, điều khiển bằng giọng nói."],
            ["Ghi hình", "Máy ảnh số, camera an ninh, máy quét (scanner), flycam.",
             "Chuyển ánh sáng thành dữ liệu hình ảnh số."],
            ["Gia dụng thông minh", "Robot hút bụi, tủ lạnh thông minh, bóng đèn thông minh, "
                                   "khoá cửa vân tay.",
             "Cảm biến → tự động điều chỉnh nhiệt độ, ánh sáng, an ninh."],
            ["Giao thông – công nghiệp", "Xe tự hành, cảm biến giao thông, thu phí không dừng, "
                                        "máy bay không người lái, cảm biến trong nhà máy.",
             "Thu thập dữ liệu diện rộng, tự động ra quyết định."],
            ["Y tế – nông nghiệp", "Máy đo đường huyết có kết nối, cảm biến độ ẩm đất, "
                                   "máy bay phun thuốc.",
             "Theo dõi sức khỏe, tưới tiêu chính xác."],
        ], widths=[94, 208, 209], fs=8.1),

        H3("2.2.5. Kinh tế tri thức và Cách mạng công nghiệp 4.0"),
        P("**Kinh tế tri thức** là nền kinh tế chủ yếu dựa vào **tri thức**, trên cơ sở khoa học – công nghệ, "
          "lấy tri thức làm động lực tăng trưởng. **CMCN 4.0** thúc đẩy mạnh mẽ nền kinh tế tri thức."),
        TBL(["Cuộc cách mạng", "Thời kì", "Đặc trưng công nghệ"], [
            ["1", "Cuối thế kỉ XVIII", "Máy hơi nước, cơ khí hoá sản xuất."],
            ["2", "Cuối XIX – đầu XX", "Điện khí hoá, dây chuyền sản xuất hàng loạt."],
            ["3", "Từ những năm 1970", "Điện tử, tự động hoá, công nghệ thông tin."],
            ["**4**", "Đầu thế kỉ XXI (thuật ngữ phổ biến từ 2011)",
             "**Kết nối vạn vật (IoT), dữ liệu lớn (Big Data), trí tuệ nhân tạo (AI), "
             "điện toán đám mây (Cloud)**; sản xuất thông minh."],
        ], widths=[100, 145, 266], fs=8.2),
        P("**Vai trò của thiết bị thông minh:** chúng là **đầu cuối thu thập dữ liệu** và là "
          "**cơ chế thực thi quyết định** trong các hệ thống IoT – nội dung cốt lõi của CMCN 4.0. "
          "Nhờ vậy quá trình thiết kế, mô phỏng, tạo mẫu được thực hiện trên không gian số, "
          "còn sản phẩm được tạo ra trong thế giới vật lí."),
        BOX("Ví dụ “vàng” cho câu Thông hiểu / Vận dụng", [
            "**Xe tự hành:** cảm biến thu dữ liệu biển báo, đường đi, chướng ngại vật → chip tính toán "
            "tốc độ và hướng đi tối ưu → mô tơ điều khiển vô lăng. Đây vừa là **hệ thống xử lí thông tin**, "
            "vừa là **thành tựu của AI + IoT** trong CMCN 4.0.",
            "**Nhà thông minh:** cảm biến nhiệt độ → đám mây phân tích → điều hoà tự bật. "
            "Lợi ích: tiết kiệm điện, tiện lợi; rủi ro: lộ dữ liệu sinh hoạt nếu bảo mật kém.",
            "**Nông nghiệp thông minh:** cảm biến độ ẩm → hệ thống tưới nhỏ giọt tự động → "
            "giảm 30% nước tưới mà năng suất tăng.",
        ], "example"),

        H3("2.2.6. Ghi nhớ nhanh A2"),
        BOX("A2 trong 6 dòng", [
            "1. Thiết bị thông minh = **Cảm biến + Chip + Bộ nhớ + Mạng + Cơ cấu chấp hành**.",
            "2. 5 đóng góp: **Quản lí – Tự động hoá – Giải toán KHKT – Đổi mới nghề nghiệp – Giao tiếp**.",
            "3. 4 thành tựu: **Hệ điều hành – Mạng/Internet – NNLT bậc cao – CSDL**.",
            "4. Mốc nhớ: **1957 FORTRAN · 1983 TCP/IP · 1992 WWW**.",
            "5. Kinh tế tri thức lấy **tri thức** làm động lực; CMCN 4.0 = **AI + IoT + Big Data + Cloud**.",
            "6. Luôn kèm **1 ví dụ cụ thể** khi giải thích vai trò.",
        ], "memory"),
        PB(),

        # ------------------------------------------------------------- A3
        H2("2.3. A3 – Kĩ năng sử dụng thiết bị số của mỗi công dân"),
        P("*SGK KNTT Bài 7. Đặc tả xếp ở mức Vận dụng; ma trận không tách câu riêng – "
          "đây là kĩ năng nền, thường gộp vào câu tự luận.*"),

        H3("2.3.1. Khởi động và tắt thiết bị đúng cách"),
        OL([
            "**Kiểm tra nguồn:** dây nguồn/cục sạc, pin, ổ cắm; đảm bảo tay khô, nơi khô ráo.",
            "**Nhấn và giữ nút nguồn** (nút khoá ở điện thoại, nút Power ở máy tính) cho đến khi xuất hiện logo.",
            "**Chờ hệ điều hành nạp xong** (Windows, Android, iOS…) – không ngắt nguồn giữa chừng.",
            "**Mở khoá / đăng nhập** đúng tài khoản; quan sát thanh trạng thái (pin, Wi-Fi, giờ).",
            "**Sử dụng:** mở ứng dụng, làm việc với tệp; lưu thường xuyên (Ctrl + S).",
            "**Kết thúc:** đóng ứng dụng, lưu công việc, chọn **Shut down / Restart** từ hệ điều hành "
            "(không rút điện đột ngột). Với điện thoại: nhấn giữ nút nguồn → chọn **Tắt nguồn**.",
        ]),

        H3("2.3.2. Làm quen giao diện thiết bị di động"),
        TBL(["Thành phần màn hình", "Chức năng", "Thao tác tương ứng"], [
            ["Thanh trạng thái", "Hiện giờ, % pin, Wi-Fi/4G, thông báo.", "Vuốt từ trên xuống để xem nhanh."],
            ["Biểu tượng ứng dụng (app)", "Mở chương trình cài sẵn hoặc cài thêm.", "Chạm để mở; chạm giữ để di chuyển/xoá."],
            ["Thanh truy cập nhanh", "Các app hay dùng, lặp lại ở mọi trang màn hình.", "Chạm để chuyển app."],
            ["Thanh điều hướng", "Nút **Quay lại (Back)**, **Tổng quan (Overview)** (Android).",
             "Bấm Back để lui; bấm Overview để xem app đang chạy."],
            ["Nút vật lí", "Nút nguồn/khoá, tăng – giảm âm lượng.", "Bấm giữ nguồn để khởi động."],
        ], widths=[118, 205, 188], fs=8.2),
        P("**PDA (trợ thủ số cá nhân)** là thiết bị tích hợp nhiều chức năng: nghe nhạc, xem phim, "
          "gọi điện, quay phim, điều khiển thiết bị từ xa qua USB, thẻ nhớ, Bluetooth, Wi-Fi. "
          "Phổ biến nhất hiện nay là **điện thoại thông minh, máy tính bảng, đồng hồ thông minh** "
          "với hai hệ điều hành chủ yếu là **Android** (Google) và **iOS** (Apple)."),

        H3("2.3.3. Tệp dữ liệu và ứng dụng cài sẵn"),
        TBL(["Nhóm thao tác", "Cách làm", "Lưu ý"], [
            ["Quản lí tệp", "Mở ứng dụng **File Manager / Files / My Files**; chọn thư mục "
                            "(ví dụ `DCIM/Camera`); chạm giữ để **sao chép, di chuyển, chia sẻ, xoá**.",
             "Xoá tệp quan trọng phải sao lưu trước."],
            ["Nhận biết loại tệp", "Dựa vào **phần mở rộng** sau dấu chấm.",
             "`.txt .docx .pdf` văn bản; `.xlsx` bảng tính; `.jpg .png` ảnh; "
             "`.mp3` nhạc; `.mp4` video; `.zip` nén."],
            ["Ứng dụng thiết yếu", "Gọi điện, nhắn tin, danh bạ.", "Có sẵn trên điện thoại."],
            ["Ứng dụng thường có sẵn", "Chụp ảnh & thư viện ảnh, trình duyệt web, email, "
                                      "máy tính, lịch, hẹn giờ, ghi chú, bản đồ.",
             "Dùng ngay không cần cài."],
            ["Ứng dụng cài thêm", "Tải từ **chợ ứng dụng chính thức** (Google Play, App Store): "
                                  "Zoom, MS Teams, Google Drive, OneDrive…",
             "Kiểm tra quyền truy cập trước khi cài."],
            ["Học trực tuyến", "Mở Zoom/Google Meet → nhập mã phòng do giáo viên cung cấp.",
             "Bật micro đúng lúc, tắt khi không nói."],
        ], widths=[100, 260, 151], fs=8.1),
        BOX("Bài tập thực hành tại nhà (tự chấm)", [
            "① Khởi động điện thoại, cho biết tên hệ điều hành và phiên bản.",
            "② Tìm một bức ảnh, xem thông tin tệp (tên, dung lượng KB/MB, ngày tạo).",
            "③ Sao chép ảnh đó vào thư mục mới `ON_TAP_TIN_10`; đổi tên thành `anh_A1.jpg`.",
            "④ Mở trình duyệt, truy cập một nguồn học liệu mở và lưu lại đường dẫn.",
            "⑤ Dùng Google Translate dịch một đoạn văn bản ngắn bằng **giọng nói**.",
        ], "example"),

        H3("2.3.4. Ghi nhớ nhanh A3"),
        BOX("A3 trong 4 dòng", [
            "1. Khởi động: **Nguồn → Logo → Hệ điều hành → Đăng nhập → Làm việc → Shut down**.",
            "2. Màn hình: **trạng thái – biểu tượng app – truy cập nhanh – điều hướng**.",
            "3. Tệp: tên + **phần mở rộng**; thao tác **mở – chọn – sao chép – di chuyển – xoá – chia sẻ**.",
            "4. Ứng dụng cài sẵn dùng ngay; ứng dụng cài thêm chỉ lấy từ **chợ chính thức**.",
        ], "memory"),
        PB(),
    ]
    return B
