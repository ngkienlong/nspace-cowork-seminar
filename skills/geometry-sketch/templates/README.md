# Templates

Mỗi template là một file `.tex` đã chạy được, làm điểm khởi đầu để chỉnh sửa.
Khi gặp dạng bài tương ứng, copy template ra workspace, đổi điểm và thêm đối tượng cần thiết, rồi gọi `render.sh`.

| Template                          | Dạng bài                                                                 |
|-----------------------------------|-------------------------------------------------------------------------|
| `triangle_circle.tex`             | Tam giác nhọn nội tiếp đường tròn, có sẵn 3 đường cao và trực tâm $H$. |
| `triangle_inscribed_circle.tex`   | Tam giác có đường tròn nội tiếp, tâm $I$.                                |
| `circle_tangent.tex`              | Đường tròn $(O)$ với một điểm ngoài và 2 tiếp tuyến.                     |
| `parallelogram.tex`               | Hình bình hành/hình thoi, có hai đường chéo.                             |
| `coord_parabola.tex`              | Parabol $y = ax^2$ trên hệ trục toạ độ, có lưới ô và bảng giá trị mẫu.   |

Quy ước chung của tất cả template:

- `standalone` với `border=5pt`.
- Dùng `tikz` + thư viện `calc, intersections, through, angles, quotes`.
- Tâm đường tròn (nếu có) ở `(0,0)`, bán kính 3.
- Style: nét chính thick đen, phụ trợ blue dashed, nhấn red thick.

Mở từng file `.tex` để xem comment giải thích từng đoạn.
