# Outline buổi seminar "Nhúng AI vào folder trên máy"
## Tổng quan nội dung seminar
## Showcase
- Dịch file pdf sang tiếng Anh và xuất ra docx
- Tổng hợp hoá đơn (pdf, ảnh chụp) xuất ra xlsx
- Tạo slide pptx từ 1 tài liệu (file hoặc link)
- Tạo hình
- Tạo landing page
- Visualize data
- Giải đề toán, vẽ đồ thị, vẽ hình hình học, xuất ra docx

## Lý thuyết và thực hành
- Agent vs Chatbot
- Skill là gì?
- Skill nằm đâu trên máy?
- Import skill như thế nào? Lưu ý an toàn.

> Thực hành: Import workspace skill `pdf` để đọc pdf

- Lựa chọn model tối ưu
- Cửa sổ ngữ cảnh
- File markdown(md) là gì

> Thực hành: Import global skill `skill-creator` từ folder

> Thực hành: Cài extension (Markdown Folio, PDF Viewer) để file có view đẹp

- Tự tạo skill như thế nào?

> Thực hành: Tự tạo 1 skill `summarize` để tóm tắt tài liệu, phạm vi workspace, nhận input là 1 file, output là file md đặt cạnh bên file gốc.

> Thực hành: Import các skill thường dùng (`docx`, `xlsx`, `data-visualize`, , `md-to-docx`, `presentation-content`, `pptx`, `solve-maths-problem`, `geometry-sketch` )

> Thực hành: Di chuyển skill giữa workspace và global

- Cải tiến skill như thế nào?

> Thực hành: Cải tiến skill 'summarize' tóm tắt để trích xuất 10-20 keyword và 5-10 câu hỏi quan trọng mà tài liệu có trả lời, ghi ở đầu file md

> Thực hành 1 skill tóm tắt xịn `process-raw-data`

- Nối nhiều skill như thế nào?
- Human in the loop

> Thực hành: Kết hợp skill `presentation-content` và skill `pptx` để soạn slide từ 1 nội dung cung cấp (file hoặc link)

- Giao quyền nào cho AI chạy tự động? Quyền nào phải hỏi chờ cho phép?

> Thực hành: Chuyển md sang docx theo format tham chiếu

> ~~Thực hành: Giải đề toán (kết hợp với data-visualize, geometry-sketch) và xuất ra docx~~

> Thực hành: Cấu hình MCP với Nspace Cowork

> Thực hành: Dùng MCP tạo ảnh

> Thực hành: Dùng MCP public landing page

> Thực hành: Dùng MCP tạo text to speech







