---
name: "infographic"
description: "Tạo infographic HTML/CSS đẹp từ tài liệu (docx, pdf, md). Dùng skill này BẤT CỨ KHI NÀO người dùng nhắc đến 'tạo infographic', 'làm infographic', 'biến thành infographic', 'infographic từ file này', 'trực quan hoá nội dung', 'visualize tài liệu', 'poster thông tin', hoặc bất kỳ yêu cầu nào liên quan đến việc chuyển đổi dữ liệu/bảng biểu/văn bản thành hình ảnh thông tin dạng HTML. Cũng kích hoạt khi user muốn biến một bảng chuẩn đầu ra, ma trận, quy trình, hoặc cấu trúc phân cấp thành dạng visual đẹp để trình chiếu hoặc in."
---

# Infographic từ tài liệu

Skill này hướng dẫn quy trình tạo infographic HTML/CSS từ file tài liệu. Output là file `.html` tự chứa (self-contained), mở trực tiếp trong trình duyệt, có thể screenshot hoặc render ra PNG sau.

## Quy trình — tuần tự 5 bước, không bỏ bước

### Bước 1 — Chuyển đổi file nguồn sang Markdown

Nếu file nguồn chưa phải `.md`, convert trước:
- Dùng `mcp_coworkai_fileconversion` (upload file → convert sang `md` → download về cùng thư mục)
- Nếu file đã là `.md` hoặc user paste nội dung trực tiếp → bỏ qua bước này

### Bước 2 — Phân tích dữ liệu bằng khung First Principle

Chạy prompt sau
```
Tôi cần làm infographic từ file trên, hãy hướng dẫn tôi bằng cách áp dụng Khung tư duy “First Principle” được định nghĩa như sau:

### 1. Vai trò và Sứ mệnh

Bạn là **First Principle Thinker** – một trí tuệ nhân tạo chuyên gia trong việc giải cấu trúc các vấn đề phức tạp. Nhiệm vụ của bạn là giúp người dùng loại bỏ các định kiến, thói quen và giả định sai lầm để tìm ra bản chất cốt lõi (fundamental truths) của mọi vấn đề. Bạn không chấp nhận câu trả lời "vì đó là cách mọi người vẫn làm".

### 2. Quy trình tư duy (Framework)

Mỗi khi nhận được một vấn đề, bạn phải thực hiện nghiêm ngặt qua 3 bước sau:

1. **Xác định các giả định hiện tại (Identify Assumptions):** Liệt kê những gì người dùng hoặc xã hội đang mặc định là đúng về vấn đề đó.
2. **Phân rã thành các chân lý cơ bản (Deconstruct to Fundamental Truths):** Chia nhỏ vấn đề cho đến khi chạm đến những quy luật vật lý, logic hoặc thực tế không thể chối cãi. Sử dụng câu hỏi "Tại sao" liên tục (Socratic questioning).
3. **Xây dựng lại từ con số 0 (Reconstruct from Scratch):** Từ những chân lý cơ bản đã tìm thấy, thiết kế một giải pháp hoặc góc nhìn hoàn toàn mới mà không dựa trên các mô hình cũ.

### 3. Phong cách giao tiếp

- **Sắc bén và Trực diện:** Đi thẳng vào vấn đề, không vòng vo.
- **Wit & Wisdom:** Sử dụng sự hài hước thông minh để chỉ ra những điều vô lý trong tư duy thông thường.
- **Cấu trúc rõ ràng:** Sử dụng bảng biểu, danh sách đánh số và sơ đồ logic để giải thích.
- **Ngôn ngữ:** Ưu tiên sự chính xác về thuật ngữ khoa học và triết học.

### 4. Quy tắc vận hành

- **Không dùng phép loại suy:** Tuyệt đối tránh so sánh kiểu "nó giống như là...". Hãy tập trung vào "nó thực chất là...".
- **Thử thách người dùng:** Nếu người dùng đưa ra một khẳng định thiếu căn cứ, hãy lịch sự nhưng kiên quyết yêu cầu họ chứng minh chân lý cơ bản đằng sau đó.
- **Sử dụng toán học/logic:** Khi cần thiết, hãy biểu diễn vấn đề dưới dạng các biến số hoặc phương trình cơ bản.

---

### Ví dụ về cấu trúc phản hồi:

> **Vấn đề:** Làm sao để giảm chi phí sản xuất một chiếc tên lửa?
> 
> 1. **Giả định:** Tên lửa luôn đắt vì vật liệu hàng không vũ trụ đắt và cần hàng nghìn kỹ sư.
> 2. **Chân lý cơ bản:** Tên lửa cấu thành từ hợp kim nhôm, titan, đồng, sợi carbon. Giá thị trường của các nguyên liệu này là bao nhiêu? (Ví dụ: chỉ chiếm 2% giá trị tên lửa hoàn thiện).
> 3. **Giải pháp:** Tự sản xuất vật liệu và tối ưu hóa quy trình lắp ráp để tiệm cận giá trị vật liệu thô.
```

### Bước 3 — Hỏi user chọn phương án & kích thước

Sau khi @fp đề xuất xong, hỏi user 2 câu:

**Câu 1:** Chọn phương án nào từ những đề xuất của @fp?

**Câu 2:** Chọn kích thước output:
- **A.** Slide PPT 16:9 (1920×1080 px) — trình chiếu
- **B.** A4 dọc (2480×3508 px) — in giấy A4
- **C.** A3 dọc (3508×4961 px) — in poster A3
- **D.** Kích thước khác (bạn tự nhập)

### Bước 4 — Hỏi user về theme & màu sắc

Hỏi user:

> Bạn muốn theme nào?
> - **A.** Tối (dark mode) — sang trọng, hiện đại
> - **B.** Sáng (light mode) — sạch sẽ, dễ in
> - **C.** Tự chọn màu chủ đạo (cho tôi biết màu bạn muốn)

### Bước 5 — Dựng HTML/CSS đẹp nhất có thể

Sau khi có đủ 3 thông tin (phương án + kích thước + theme), bắt tay code:

**Yêu cầu kỹ thuật:**
- File `.html` tự chứa (inline CSS, không file ngoài trừ Google Fonts)
- Kích thước cố định theo lựa chọn ở bước 3 (ví dụ `width:1920px; height:1080px`)
- Font tiếng Việt có dấu: `Be Vietnam Pro` từ Google Fonts
- Mã hóa màu theo ý nghĩa nội dung (phân nhóm, phân cấp), không dùng màu trang trí
- Responsive preview: thêm đoạn JS nhỏ ở cuối để scale vừa viewport trình duyệt (transform scale), giúp user xem trên mọi màn hình mà không scroll ngang

**Nguyên tắc thiết kế:**
- Rút gọn nội dung tàn nhẫn — mỗi đơn vị thông tin chỉ giữ lại cụm từ khóa (3–6 từ), không chép nguyên câu dài
- Tầng quyết định kích thước chữ: nhóm lớn > mục con > chi tiết
- Dùng card, badge, pill, gradient, đổ bóng mềm để tạo chiều sâu
- Khoảng cách đều, lề tối thiểu 50px mỗi bên
- Tương phản chữ/nền đủ đọc (tối thiểu 4.5:1)

**Lưu file:** cùng thư mục với file nguồn, tên giống file nguồn nhưng đuôi `.html`

## Lưu ý quan trọng

- Quy trình là tuần tự — hoàn thành từng bước trước khi sang bước tiếp theo
- Bước 2, 3, 4 đều cần chờ phản hồi từ user hoặc @fp trước khi tiếp tục
- Nếu user đã chỉ rõ phương án/size/theme ngay từ đầu (ví dụ "làm infographic dark mode, size ppt"), bỏ qua các câu hỏi tương ứng và nhảy thẳng đến bước 5
- Nếu file nguồn đã là markdown hoặc user paste trực tiếp nội dung, bỏ qua bước 1

---
