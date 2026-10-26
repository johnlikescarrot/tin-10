# -*- coding: utf-8 -*-
"""Trang bìa, Phần 0 (đọc vị đề thi) và Phần 1 (bản đồ kiến thức)."""
from .blocks import (H1, H2, H3, P, LEAD, SMALL, UL, OL, TBL, BOX, PB, SP,
                     RULE, CHECK)

LEVEL_HEADS = ["NB\nTN", "NB\nĐS", "NB\nTL", "TH\nTN", "TH\nĐS", "TH\nTL",
               "VD\nTN", "VD\nĐS", "VD\nTL", "VDC\nTN", "VDC\nĐS", "VDC\nTL"]


def _compact_matrix(source):
    """Chuyển ma trận 12 cột mức độ về dạng bảng gọn, không mất số liệu."""
    groups = [(0, 3, "Nhận biết"), (3, 6, "Thông hiểu"),
              (6, 9, "Vận dụng"), (9, 12, "Vận dụng cao")]
    labels = ["TN", "ĐS", "TL"]
    head = ["Đơn vị kiến thức / kĩ năng", "Nhận biết", "Thông hiểu",
            "Vận dụng", "Vận dụng cao", "Tổng % điểm"]
    rows = []
    for r in source["matrix_rows"]:
        cells = []
        for a, b, _ in groups:
            bits = [f"**{labels[i-a]}:** {r['levels'][i]}"
                    for i in range(a, b) if r["levels"][i].strip()]
            cells.append("  ·  ".join(bits) if bits else "—")
        unit = r["donvi"].strip().rstrip(".")
        if not r["total"]:
            unit += "  *(kĩ năng thực hành – không tách câu riêng)*"
        rows.append([unit] + cells + [r["total"] or "—"])
    tot = source["matrix_summary"][0]
    rows.append(["**TỔNG**",
                 f"**{tot[1]} câu TN**",
                 f"**{tot[4]} câu TN + {tot[5]} (ĐS) + {tot[6]} câu TL**",
                 f"**{tot[8]} (ĐS) + {tot[9]} câu TL**",
                 f"**{tot[12]} câu TL**", "**100% / 10 điểm**"])
    return TBL(head, rows, widths=[133, 82, 101, 75, 61, 59], fs=7.9,
               caption="Bảng 0.2 – Ma trận đề (dạng gọn). NB = nhận biết, TH = thông hiểu, "
                       "VD = vận dụng, VDC = vận dụng cao; TN = trắc nghiệm, "
                       "ĐS = đúng/sai, TL = tự luận. Bản đầy đủ 16 cột ở Phụ lục A.2.")


def blocks(source):
    B = []
    B += [{"k": "cover"}]

    # ------------------------------------------------------------------ Phần 0
    B += [
        H1("PHẦN 0 · ĐỌC VỊ ĐỀ THI – HỌC ĐÚNG TRỌNG TÂM"),
        LEAD("Trước khi học thuộc, hãy biết **đề hỏi gì, hỏi bao nhiêu và hỏi ở mức độ nào**. "
             "Phần này chép lại trung thực toàn bộ thông tin cấu trúc đề từ tài liệu gốc "
             "và giải mã chúng thành một kế hoạch ôn tập cụ thể."),

        H2("0.1. Cấu trúc đề kiểm tra (nguyên văn tài liệu gốc)"),
        TBL(["Thông tin", "Nội dung"], [
            ["Thời gian", "45 phút"],
            ["Hình thức", "Kết hợp trắc nghiệm và tự luận: **70% trắc nghiệm – 30% tự luận**."],
            ["Mức độ đề", "70% trắc nghiệm (40% Nhận biết; 20% Thông hiểu; 10% Vận dụng); "
                          "30% tự luận (10% Thông hiểu; 10% Vận dụng; 10% Vận dụng cao)."],
            ["Trắc nghiệm", "**7,0 điểm** = 20 câu 4 lựa chọn × 0,25 điểm + 2 câu đúng/sai × 1,0 điểm."],
            ["Tự luận", "**3,0 điểm** = 1 câu thông hiểu + 1 câu vận dụng + 1 câu vận dụng cao, mỗi câu 1,0 điểm."],
            ["Tổng", "10 điểm. Cần đạt 16 câu nhận biết chắc chắn trước khi luyện 3 câu tự luận."],
        ], widths=[95, 416]),
        BOX("Chú ý khi đọc bản gốc", [
            "Tài liệu gốc viết **“10% Thông biểu”** ở dòng “Mức độ đề”. Đây là lỗi chính tả của "
            "**“Thông hiểu”** (cùng dòng đã có 20% Thông hiểu ở phần trắc nghiệm). Đề cương này "
            "hiểu theo đúng bảng tỉ lệ: **Nhận biết 40% – Thông hiểu 30% – Vận dụng 20% – Vận dụng cao 10%**.",
            "Tên các chủ đề trong bản gốc là **A – B – D** (kí hiệu Chương trình 2018). "
            "Sách **Kết nối tri thức với cuộc sống** gọi tương ứng là **Chủ đề 1 – 2 – 3**. "
            "Bảng ánh xạ đầy đủ ở Phụ lục B.",
        ], "note"),

        H2("0.2. Ma trận đề: đủ 100% số liệu ở dạng dễ nhìn"),
        P("Ma trận gốc có 12 cột mức độ nhận thức. Dưới đây là dạng gọn **không bỏ sót ô nào**; "
          "bản sao nguyên dạng 16 cột được đặt ở Phụ lục A.2 để bạn đối chiếu."),
        _compact_matrix(source),
        SP(4),
        TBL(["Mức độ", "Tỉ lệ", "Quy ra điểm", "Dạng câu", "Chiến lược"], [
            ["Nhận biết", "40%", "4,0 điểm", "16 câu TN", "Học thuộc định nghĩa, ví dụ, mốc năm – lấy trọn 4 điểm."],
            ["Thông hiểu", "30%", "3,0 điểm", "4 câu TN + 2 câu ĐS (8 ý) + 1 câu TL", "Giải thích được, so sánh được, nêu ví dụ."],
            ["Vận dụng", "20%", "2,0 điểm", "1 câu ĐS (4 ý) + 1 câu TL", "Làm được bài tập đổi đơn vị, thao tác, tình huống."],
            ["Vận dụng cao", "10%", "1,0 điểm", "1 câu TL", "Phân tích tình huống pháp lí, đề xuất cách xử lí."],
        ], widths=[80, 45, 66, 120, 200], fs=8.2,
               caption="Bảng 0.3 – Ý nghĩa của 4 mức độ nhận thức (theo dòng “Tổng” của ma trận gốc)."),

        H2("0.3. Trọng số điểm: ưu tiên ôn phần nào?"),
        P("Năm đơn vị kiến thức đều chiếm **20% (2 điểm)**; đơn vị A3 (kĩ năng sử dụng thiết bị số) "
          "không tách câu riêng nhưng là kĩ năng nền cho các câu vận dụng. Gộp theo chủ đề:"),
        TBL(["Chủ đề (KNTT)", "Tên trong bản gốc", "Đơn vị", "Tỉ lệ", "Mức ưu tiên"], [
            ["**Chủ đề 1**", "A. Máy tính và xã hội tri thức", "A1, A2, A3", "**40%** (4 điểm)", "**Rất cao (5/5)**"],
            ["**Chủ đề 2**", "B. Mạng máy tính và Internet", "B1, B2", "**40%** (4 điểm)", "**Rất cao (5/5)**"],
            ["**Chủ đề 3**", "D. Đạo đức, pháp luật, văn hoá số", "D1", "**20%** (2 điểm)", "**Cao (4/5)**"],
        ], widths=[82, 158, 58, 92, 121], fs=8.4),
        BOX("Kết luận nhanh", [
            "**8/10 điểm** nằm ở Chủ đề A và B. Nếu chỉ có 1 tối, hãy ôn **A1 + A2 + B1 + B2**.",
            "**16/20 câu trắc nghiệm** là mức Nhận biết: học kĩ các bảng định nghĩa ở Phần 2–4 là có ngay 4,0 điểm.",
            "Đừng bỏ **A3**: dù không có câu riêng, các thao tác với tệp và thiết bị thường xuất hiện trong câu tự luận vận dụng.",
        ], "memory"),

        H2("0.4. Năm điểm cần lưu ý khi đối chiếu ma trận với đặc tả"),
        OL([
            "**A3 không có ô điểm riêng.** Đặc tả vẫn nêu 2 yêu cầu (khởi động thiết bị; dùng tệp và ứng dụng cài sẵn). "
            "Hãy học như kĩ năng thực hành, không phải kiến thức ghi nhớ.",
            "**Hai câu Đúng/Sai** được ghép từ 8 ý: 4 ý Thông hiểu + 4 ý Vận dụng; "
            "mỗi câu có 2 ý Thông hiểu (từ A2 hoặc B1) và 2 ý Vận dụng (cùng chủ đề). "
            "Luyện dạng này kĩ vì mỗi ý vẫn được chấm điểm riêng.",
            "**Mức độ của câu tự luận:** ma trận xếp 1 câu TH (B2), 1 câu VD (A1), 1 câu VDC (D1); "
            "đặc tả lại ghi câu TL của B2 ở mức Vận dụng. Cứ ôn **cao hơn một mức** để an toàn.",
            "**Phân bổ 4 câu TN Thông hiểu:** ma trận cho A1 2 câu và D1 2 câu; đặc tả cho A1 2 câu và B2 2 câu. "
            "Vì vậy A1, B2, D1 đều cần luyện câu Thông hiểu.",
            "**Chủ đề D có ít câu nhưng khó nhất:** 2 câu Nhận biết, 2 câu Thông hiểu và 1 câu tự luận Vận dụng cao. "
            "Đây là nơi duy nhất xuất hiện mức Vận dụng cao – hãy dành thời gian cho phần tình huống pháp lí.",
        ]),

        H2("0.5. Lộ trình ôn tập 5 ngày (mỗi ngày 45–60 phút)"),
        TBL(["Ngày", "Việc cần làm", "Tài liệu trong đề cương", "Tự kiểm tra"], [
            ["1", "Nắm khung đề + toàn bộ định nghĩa A1, A2", "Phần 0, 2.1, 2.2", "Trả lời được 6 móc nhớ ở 1.2"],
            ["2", "A3 thực hành + B1 mạng, đám mây, IoT", "2.3, 3.1", "Làm 10 câu đổi đơn vị và so sánh LAN/Internet"],
            ["3", "B2 an toàn + web + học liệu mở", "3.2", "Kể được 5 nguy cơ và 5 cách phòng tránh"],
            ["4", "D1 pháp luật, bản quyền, chia sẻ thông tin", "Phần 4", "Giải 4 tình huống ở 4.7"],
            ["5", "Ngân hàng 35 câu + làm đề thử 45 phút", "Phần 5, Phần 6", "Tự chấm và xem lại lỗi sai ở 1.4"],
        ], widths=[38, 170, 130, 173], fs=8.2),
        PB(),
    ]

    # ------------------------------------------------------------------ Phần 1
    B += [
        H1("PHẦN 1 · BẢN ĐỒ TRI THỨC TRONG MỘT TRANG"),
        LEAD("Hãy hình dung toàn bộ chương trình là **một dòng chảy thông tin**: "
             "con người tạo ra dữ liệu → thiết bị xử lí → mạng truyền đi → pháp luật và đạo đức "
             "giữ cho dòng chảy ấy an toàn. Ba chủ đề vì thế **không rời rạc**."),

        H2("1.1. Sơ đồ tư duy tổng hợp"),
        TBL(["Nhánh", "Câu hỏi trung tâm", "Từ khoá phải thuộc", "Bài SGK KNTT"], [
            ["**A. Máy tính và xã hội tri thức**\n*(Chủ đề 1)*",
             "Thông tin là gì, ai xử lí và bằng thiết bị nào?",
             "Dữ liệu ↔ thông tin · TLXT · bit/byte · thiết bị thông minh · "
             "kinh tế tri thức · CMCN 4.0 · thiết bị số cá nhân",
             "Bài 1–7"],
            ["**B. Mạng máy tính và Internet**\n*(Chủ đề 2)*",
             "Thông tin đi qua đâu và bị đe doạ thế nào?",
             "LAN ↔ Internet · TCP/IP · đám mây IaaS/PaaS/SaaS · IoT · "
             "web & học liệu mở · phần mềm độc hại · 5 nguy cơ",
             "Bài 8–10"],
            ["**D. Đạo đức, pháp luật, văn hoá số**\n*(Chủ đề 3)*",
             "Ai chịu trách nhiệm khi thông tin được chia sẻ?",
             "3 trụ: đạo đức – pháp luật – văn hoá · Luật CNTT 2006 · "
             "Luật ANM 2018 · NĐ 72/2013 · bản quyền · 3 nguyên tắc chia sẻ",
             "Bài 11"],
        ], widths=[112, 105, 220, 74], fs=8.1,
               caption="Bảng 1.1 – Ba nhánh của đề cương. Đọc từ trên xuống dưới chính là chiều đi của thông tin."),

        H2("1.2. Sáu “móc nhớ” giúp nhớ cả chương trình"),
        TBL(["Móc nhớ", "Nội dung", "Dùng ở đâu"], [
            ["**TLXT**", "**T**hu nhận → **L**ưu trữ → **X**ử lí → **T**ruyền (và đưa ra kết quả). "
                         "Trong máy tính, xử lí thông tin chính là xử lí dữ liệu.", "A1"],
            ["**Khoai Mì Gà Tây**", "**K**B – **M**B – **G**B – **T**B: mỗi bậc gấp **1024 = 2^10** lần bậc trước. "
                                    "1 B = 8 bit.", "A1"],
            ["**D – T – K**", "**D**ữ liệu → **T**hiết bị → **K**ĩ năng: cấu trúc 3 bài của Chủ đề A.", "A1, A2, A3"],
            ["**P – L – M – W**", "**P**hòng (PAN) → **L**ầu (LAN) → **M**ạng phố (MAN) → "
                                 "**W**orld (WAN/Internet): phạm vi tăng dần.", "B1"],
            ["**I – P – S**", "Đám mây: **I**aaS (hạ tầng) → **P**aaS (nền tảng) → **S**aaS (phần mềm). "
                              "Càng lên càng gần người dùng.", "B1"],
            ["**3 – 4 – 3**", "**3** văn bản luật chính · **4** nhóm hành vi bị cấm · "
                              "**3** nguyên tắc khi chia sẻ thông tin.", "D1"],
        ], widths=[104, 342, 65], fs=8.3,
               caption="Bảng 1.2 – Học thuộc 6 dòng này, bạn có ngay “dàn ý” để triển khai mọi câu tự luận."),
        BOX("Mẹo ghi nhớ thêm", [
            "**4 KHÔNG – 3 CÓ** khi lên mạng: Không tiết lộ thông tin cá nhân · Không mở liên kết lạ · "
            "Không tin và không chuyển tin giả · Không đáp trả kẻ bắt nạt; Có mật khẩu mạnh + xác thực 2 yếu tố · "
            "Có sao lưu và cập nhật · Có người lớn/thầy cô để nhờ giúp.",
            "**4 tên trộm số:** Virus (đoạn mã kí sinh), Worm (sâu tự lây), Trojan (nội gián đội lốt), "
            "Spyware (gián điệp đánh cắp dữ liệu).",
        ], "tip"),

        H2("1.3. Công thức và quy trình phải thuộc lòng"),
        TBL(["Tên", "Công thức / quy trình", "Ví dụ nhanh"], [
            ["Đổi đơn vị xuống", "Nhân 1024 cho mỗi bậc đi xuống (GB → MB → KB → B).",
             "2 GB = 2 × 1024 = 2048 MB = 2 097 152 KB"],
            ["Đổi đơn vị lên", "Chia 1024 cho mỗi bậc đi lên (B → KB → MB → GB).",
             "3 145 728 B = 3072 KB = 3 MB"],
            ["Số tệp chứa được", "Dung lượng thiết bị ÷ dung lượng một tệp (cùng đơn vị).",
             "USB 2 GB chứa 2 × 1024 ÷ 4 = 512 ảnh 4 MB"],
            ["Quy trình xử lí (A1)", "Tiếp nhận → Lưu trữ → Xử lí → Kết quả/Truyền → Người nhận.",
             "Nhiệt độ các năm → phần mềm → biểu đồ ấm lên"],
            ["Thiết bị thông minh (A2)", "Cảm biến (vào) → Vi xử lí (xử) → Mạng (truyền) → Cơ cấu (ra).",
             "Xe tự hành: camera → chip → điều khiển vô lăng"],
            ["IoT (B1)", "Thiết bị → Mạng → Đám mây/xử lí → Ứng dụng cho người dùng.",
             "Cảm biến đất → Wi-Fi → máy chủ → tưới tự động"],
            ["Xác định hợp pháp (D1)", "Hành vi → Đối tượng bị ảnh hưởng → Đối chiếu luật → Kết luận → Cách xử lí.",
             "Đăng ảnh bạn chế giễu → xâm phạm nhân phẩm → trái luật"],
        ], widths=[104, 262, 145], fs=8.1),

        H2("1.4. 12 lỗi sai thường gặp và cách sửa"),
        TBL(["Lỗi hay mắc", "Sửa lại cho đúng"], [
            ["Nhầm **1 KB = 1000 B**.", "Trong Tin học phổ thông: **1 KB = 1024 B = 2^10 B**. "
                                        "(Một số nhà sản xuất dùng 1000 – cần đọc kĩ đề bài.)"],
            ["Nói **dữ liệu và thông tin là một**.", "Dữ liệu là **vật mang** (con số, kí tự, bit); "
                                                     "thông tin là **ý nghĩa** con người hiểu được."],
            ["Nói **Internet là World Wide Web**.", "Internet là **hạ tầng mạng**; Web là **một dịch vụ** chạy trên Internet."],
            ["Nói **LAN lớn hơn Internet**.", "LAN là mạng cục bộ, phạm vi nhỏ; Internet là mạng diện rộng toàn cầu (WAN)."],
            ["Gọi **đám mây là một máy tính cụ thể**.", "Đám mây là **chia sẻ tài nguyên qua Internet** theo nhu cầu."],
            ["Nhầm **SaaS là cho thuê máy chủ**.", "IaaS = hạ tầng/máy chủ; PaaS = nền tảng; SaaS = phần mềm ứng dụng."],
            ["Cho rằng **IoT chỉ là điện thoại**.", "IoT là **kết nối mọi thiết bị thông minh** để thu thập, trao đổi, xử lí dữ liệu tự động."],
            ["Nói **virus là phần mềm hoàn chỉnh**.", "Virus là **đoạn mã** cần vật chủ; Worm mới là phần mềm hoàn chỉnh tự lây."],
            ["Nghĩ **chỉ chia sẻ lại tin giả thì không có lỗi**.", "Pháp luật cấm cả **cung cấp, trao đổi, truyền đưa, lưu trữ, sử dụng** thông tin số trái phép."],
            ["Nghĩ **cần đăng kí mới có quyền tác giả**.", "Quyền tác giả **phát sinh khi tác phẩm được sáng tạo** và thể hiện dưới hình thức vật chất nhất định."],
            ["Nhầm **bản quyền = quyền tác giả hoàn toàn**.", "Quyền tác giả gồm quyền nhân thân + quyền tài sản; "
                                                             "bản quyền nhấn vào quyền **sao chép, khai thác** tác phẩm."],
            ["Bỏ qua **A3** vì ma trận không có câu riêng.", "A3 là kĩ năng nền; các câu vận dụng thường yêu cầu thao tác với tệp, ứng dụng."],
        ], widths=[196, 315], fs=8.1),
        PB(),
    ]
    return B
