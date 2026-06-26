---
name: review-document
description: >
  Chiến lược review tài liệu dài để phát hiện lỗi kiến thức chuyên môn một cách có hệ thống, hạn chế tối đa việc bỏ sót. Dùng skill này BẤT CỨ KHI NÀO người dùng yêu cầu review, kiểm tra, rà soát, đánh giá nội dung kiến thức trong một tài liệu — đặc biệt khi tài liệu dài (>200 dòng). Cũng áp dụng khi người dùng nói "xem có gì sai không", "check lại kiến thức", "review giáo án", "review bài viết" "kiểm tra nội dung", hoặc bất kỳ yêu cầu tương tự nào liên quan đến việc tìm lỗi trong văn bản chuyên môn.
---

# Review tài liệu dài — Chiến lược có hệ thống

## Vì sao cần chiến lược này

Khi đọc tài liệu dài (>200 dòng), việc "quét toàn bộ" trong 1 lượt rất dễ bỏ sót vì:
- Não (kể cả AI) "mỏi" dần — phần sau luôn được review kém kỹ hơn phần đầu.
- Cố bắt mọi loại lỗi cùng lúc khiến không loại nào được kiểm tra kỹ.
- Lỗi nằm ở ranh giới giữa các phần thường bị bỏ qua.

Chiến lược này giải quyết bằng 3 kỹ thuật: **phân khúc văn bản**, **review theo lớp (dạng lỗi)**, và **review theo chủ đề chuyên môn (chiều sâu)**.

---

## Bước 1 — Phân khúc văn bản

Chia tài liệu thành các khúc nhỏ trước khi review. Mỗi khúc đủ nhỏ để không bỏ sót, đủ lớn để giữ ngữ cảnh.

### Quy tắc phân khúc (theo thứ tự ưu tiên)

1. **Ưu tiên đơn vị ngữ nghĩa tự nhiên** — mỗi loại văn bản đều có cấu trúc phân cấp sẵn:
   - Giáo án → bài học
   - Sách → chương
   - Báo cáo → section
   - Hợp đồng → điều khoản
   - Code → file / module / function
   - Văn bản không có heading → đoạn văn (paragraph)

2. **Nếu đơn vị tự nhiên quá lớn, chia tiếp theo ngưỡng kích thước:**
   - Ngưỡng: **300–500 dòng/khúc** (~2000–3000 từ).
   - Dưới 300 dòng: quá nhỏ, tốn overhead chuyển ngữ cảnh.
   - Trên 500 dòng: bắt đầu bỏ sót chi tiết ở cuối khúc.
   - Cắt tại **ranh giới heading gần nhất**, không cắt giữa đoạn.

3. **Nếu văn bản hoàn toàn phẳng (không heading, không cấu trúc):**
   - Chia cơ học ~400 dòng/khúc.
   - Dịch điểm cắt đến cuối đoạn văn gần nhất.

4. **Luôn có overlap giữa các khúc:**
   - Khi đọc khúc sau, đọc lại 5–10 dòng cuối của khúc trước.
   - Lỗi hay nằm ở ranh giới vì não "reset" ngữ cảnh tại đó.

### Ví dụ phân khúc

Một giáo án 2000 dòng gồm 6 bài học:
- Khúc 1: Bài 1 (~400 dòng)
- Khúc 2: Bài 2 (~350 dòng)
- Khúc 3: Bài 3 (~450 dòng) — quá 500 thì chia thành 3a (Tiết 1) + 3b (Tiết 2)
- ...

---

## Bước 2 — Review theo lớp (layered review)

Với **mỗi khúc**, chạy lần lượt các lượt kiểm tra. Mỗi lượt chỉ tập trung vào đúng 1 loại lỗi — giữ 1 tiêu chí trong đầu thay vì cố bắt mọi thứ cùng lúc.

### 6 lượt kiểm tra

**Lượt 1 — Định nghĩa & khái niệm:**
- Chỉ đọc các câu có dạng "X là...", "X được định nghĩa là...", trích dẫn nguồn.
- Kiểm tra: định nghĩa có đúng không? Có đầy đủ không? Nguồn có đáng tin không?
- Lỗi thường gặp: định nghĩa quá hẹp, quá rộng, hoặc nhầm với khái niệm khác.

**Lượt 2 — Thuật ngữ & bản dịch:**
- Chỉ rà soát các cặp thuật ngữ (ví dụ Anh-Việt, hoặc thuật ngữ chuyên ngành).
- Kiểm tra: bản dịch có khớp không? Có nhầm giữa các khái niệm gần nhau không?
- Lỗi thường gặp: dịch sai (Classification vs Recognition), nhầm danh từ với động từ (Label vs Labeling).

**Lượt 3 — Ví dụ & minh họa:**
- Chỉ đọc các ví dụ cụ thể, tình huống minh họa.
- Kiểm tra: ví dụ có đúng với khái niệm đang minh họa không? Có quá lý tưởng hóa không? Có mâu thuẫn với phần khác không?
- Lỗi thường gặp: ví dụ sai loại (dùng ví dụ classification cho regression), ví dụ quá đơn giản gây hiểu sai.

**Lượt 4 — Câu hỏi & đáp án:**
- Chỉ đọc các câu hỏi (trắc nghiệm, tự luận, câu hỏi mở) và đáp án dự kiến.
- Kiểm tra: đáp án có chính xác không? Câu hỏi có rõ ràng không? Có nhiều đáp án đúng không?
- Lỗi thường gặp: đáp án sai, câu hỏi mơ hồ, đáp án đúng nhưng không khớp với kiến thức đã dạy.

**Lượt 5 — Tính nhất quán xuyên suốt:**
- So sánh các khái niệm được dùng ở phần trước với phần sau.
- Kiểm tra: có mâu thuẫn nội bộ không? Cùng 1 thuật ngữ có được dùng nhất quán không?
- Lỗi thường gặp: phần trước nói A là classification, phần sau liệt kê A là ví dụ regression.

**Lượt 6 — Quan hệ logic & nhân quả:**
- Kiểm tra các phát biểu dạng "vì... nên...", "nếu... thì...", "X phụ thuộc vào Y".
- Kiểm tra: logic có đúng không? Quan hệ nhân quả có chính xác không?
- Lỗi thường gặp: nhầm tương quan với nhân quả, phát biểu sai về cơ chế hoạt động.

---

## Bước 3 — Review chuyên sâu theo chủ đề kiến thức (deep-dive review)

Bước 2 review theo **dạng lỗi** (rộng nhưng nông). Bước này review theo **chủ đề kiến thức** (hẹp nhưng sâu). Đây là bước quan trọng nhất để tránh bỏ sót — kinh nghiệm cho thấy phần lớn lỗi bị bỏ sót ở Bước 2 sẽ được phát hiện ở bước này.

### Vì sao cần bước này

Bước 2 quét 6 lượt qua toàn bộ văn bản, mỗi lượt chỉ tìm 1 dạng lỗi. Nhưng lỗi chuyên môn sâu thường nằm ở **mối quan hệ giữa các khái niệm trong cùng 1 chủ đề** — loại lỗi này cần người đọc tập trung hoàn toàn vào 1 chủ đề, đọc mọi phát biểu liên quan đến chủ đề đó, và đối chiếu chúng với nhau. Bước 2 không làm được điều này vì nó phân loại theo dạng lỗi, không phải theo chủ đề.

### Cách thực hiện

1. **Liệt kê tất cả chủ đề kiến thức chính** trong tài liệu. Ví dụ: một giáo án AI có thể có các chủ đề: Supervised Learning, Unsupervised Learning, Regression, Classification, Confidence, Loss, Epoch...

2. **Với mỗi chủ đề**, thu thập TẤT CẢ các câu/đoạn liên quan đến chủ đề đó xuyên suốt tài liệu (dùng grep/search). Đọc chúng liền mạch, không theo thứ tự xuất hiện trong tài liệu mà theo logic kiến thức.

3. **Đối chiếu từng phát biểu** với kiến thức chuẩn của chủ đề đó:
   - Định nghĩa có đúng không?
   - Các ví dụ có khớp với định nghĩa không?
   - Cơ chế hoạt động được mô tả có chính xác không?
   - Các phát biểu trong cùng chủ đề có mâu thuẫn nhau không?
   - Thuật ngữ có được dùng đúng ngữ cảnh không?

4. **Đặc biệt chú ý** các điểm sau (đây là nơi lỗi hay ẩn nhất):
   - Mô tả cơ chế hoạt động (ví dụ: "máy thử và lặp lại" — đó là reinforcement learning, không phải regression).
   - Ví dụ minh họa có đúng loại bài toán không (ví dụ: "thời tiết" là categorical, không phải giá trị số liên tục).
   - Dữ liệu mẫu có phản ánh đúng thực tế không (ví dụ: dữ liệu tuyến tính hoàn hảo R²=1.0 không bao giờ xảy ra).
   - Thuật ngữ Anh-Việt có khớp nhau không (ví dụ: "Multiple Linear Regression" ≠ "hồi quy đa biến").
   - Phân biệt giữa các biến thể của cùng 1 khái niệm (ví dụ: Decision Tree Regression vs Decision Tree Classification).

### Ví dụ

Tài liệu dạy về Regression. Thu thập tất cả câu liên quan:
- Định nghĩa regression ở phần 2.2.1
- Ví dụ "thời tiết" ở phần 2.2.1
- Ví dụ "mưa hay không" ở phần 2.2.1 (đã nói là classification)
- Mô tả cơ chế máy bắn muỗi ở phần 2.2.3
- Bảng so sánh thuật toán ở phần 2.2.2

Đọc liền → phát hiện: "thời tiết" bị liệt kê là regression nhưng trước đó "mưa hay không" đã nói là classification. Mô tả máy bắn muỗi "thử và lặp lại" là reinforcement learning, không phải regression.

---

## Bước 4 — Cross-check giữa các khúc

Sau khi review xong tất cả các khúc và tất cả các chủ đề, chạy 1 lượt cuối cùng kiểm tra tính nhất quán **giữa** các khúc:
- Khái niệm được định nghĩa ở khúc 1 có được dùng đúng ở khúc 4 không?
- Ví dụ ở khúc 2 có mâu thuẫn với định nghĩa ở khúc 5 không?
- Thuật ngữ có được dịch nhất quán xuyên suốt không?

---

## Bước 5 — Ghi kết quả

Với mỗi vấn đề phát hiện, ghi rõ:
1. **Vị trí:** Khúc nào, phần nào, dòng nào.
2. **Nội dung gốc:** Trích dẫn chính xác đoạn có vấn đề.
3. **Vấn đề:** Mô tả lỗi — sai gì, vì sao sai.
4. **Mức độ:** Sai (factually wrong) / Gây nhầm (misleading) / Thiếu chính xác (imprecise) / Thiếu sót (missing) / Mâu thuẫn (contradictory).
5. **Đề xuất sửa:** Câu/đoạn thay thế cụ thể.

Cuối cùng, tổng hợp bảng tóm tắt tất cả vấn đề.

---

## Lưu ý quan trọng

- **Không bỏ qua lượt nào.** Mỗi lượt bắt được loại lỗi mà các lượt khác bỏ sót.
- **Đọc chậm hơn bình thường.** Review không phải đọc hiểu — mục tiêu là tìm lỗi, nên cần đọc từng câu một cách hoài nghi.
- **Ghi chú ngay khi phát hiện.** Không để "nhớ rồi ghi sau" — sẽ quên.
- **Overlap giữa các khúc là bắt buộc**, không phải tùy chọn.
