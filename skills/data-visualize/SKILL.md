---
name: data-visualize
description: Tạo đồ thị/biểu đồ chính xác bằng matplotlib (Python). Dùng khi cần scatter plot, line chart, bar chart, histogram, heatmap, boxplot, hoặc bất kỳ dạng trực quan hoá dữ liệu nào yêu cầu độ chính xác cao về trục, tỷ lệ, tọa độ.
metadata:
   author: kien-long
   version: "1.0"
---

# Chuyên gia Trực quan hoá Dữ liệu

Bạn đóng vai trò là Chuyên gia Trực quan hoá Dữ liệu (Data Visualization Specialist), tạo các đồ thị chính xác bằng thư viện matplotlib của Python.

## Khi nào dùng skill này

- Khi cần vẽ đồ thị có dữ liệu cụ thể (scatter plot, line chart, bar chart...).
- Khi cần độ chính xác tuyệt đối về tỷ lệ trục, tọa độ điểm, đường thẳng/cong.
- Khi cần các loại biểu đồ phức tạp: histogram, boxplot, heatmap, pie chart, regression line, confusion matrix.
- Ưu tiên hơn SVG khi đồ thị cần tính toán chính xác (đường hồi quy, hàm số, phân phối...).

## Khi KHÔNG dùng skill này

- Sơ đồ ý tưởng / infographic / flowchart → dùng `create-svg` thay vì matplotlib.
- Hình minh hoạ nghệ thuật, nhân vật, bối cảnh → dùng `create-image`.

## Tool

Tool nằm tại: `~/.kiro/skills/data-visualize/scripts/plot.py`

Script này nhận tham số:
- `--type`: loại biểu đồ (`scatter`, `line`, `bar`, `histogram`, `boxplot`, `heatmap`, `pie`, `regression`, `multi_line`).
- `--data`: dữ liệu dạng JSON.
- `--output`: đường dẫn file PNG xuất ra.
- `--config`: cấu hình bổ sung (title, xlabel, ylabel, figsize...) dạng JSON.

## Cách sử dụng

1. Phân tích yêu cầu: xác định loại biểu đồ, dữ liệu, nhãn trục, tiêu đề.
2. Chuẩn bị dữ liệu dưới dạng JSON.
3. Gọi script với các tham số phù hợp.
4. Lưu file PNG vào thư mục assets của dự án.
5. Chèn vào textbook bằng cú pháp markdown.

## Quy tắc thiết kế đồ thị

### Nhãn và tiêu đề
- Tiêu đề đồ thị: rõ ràng, ngắn gọn, fontsize 14, bold.
- Nhãn trục X, Y: ghi rõ đơn vị, fontsize 12.
- Tiếng Việt: matplotlib hỗ trợ Unicode, không cần config thêm nhiều.

### Màu sắc
- Dữ liệu chính: xanh dương `#3498db` hoặc `tab:blue`.
- Đường hồi quy / xu hướng: đỏ `#e74c3c` hoặc `tab:red` (nét đứt).
- Dự đoán / nhấn mạnh: xanh lá `#27ae60` hoặc `tab:green`.
- Phụ trợ: xám `#7f8c8d`.
- Dùng `alpha=0.7` cho điểm dữ liệu để dễ nhìn khi chồng lên nhau.

### Kích thước
- Figsize mặc định: `(10, 6)` inch.
- DPI: 100 (đủ rõ cho web/in).
- Bảo đảm grid nhẹ `alpha=0.3` để dễ đọc tọa độ.

### Tick trên trục x, y (mốc giá trị)
- Mặc định mọi mốc trên trục x và y là số nguyên (ví dụ -3, -2, -1, 0, 1, 2, 3) — không xuất hiện 2.5, 7.5, 12.5... vốn khó đọc.
- Áp dụng tự động cho các loại numeric: `scatter`, `line`, `multi_line`, `histogram`, `regression`, `knn`. Các loại categorical (`bar`, `boxplot`, `pie`, `heatmap`) không bị ảnh hưởng.
- Nếu cần tắt: thêm `"integer_xticks": false` hoặc `"integer_yticks": false` vào config.
- Nếu cần bước nhảy cụ thể (ví dụ trục y nhảy 2 đơn vị: 0, 2, 4, 6...): dùng `"xtick_step": 1` hoặc `"ytick_step": 2` trong config — tham số này ưu tiên hơn `integer_*ticks`.

### Annotation
- Dùng `plt.annotate()` để ghi chú điểm cụ thể.
- Mũi tên annotation: `arrowprops=dict(arrowstyle='->', color='gray')`.

## Ví dụ sử dụng

### Scatter plot + đường hồi quy

```bash
python3 ~/.kiro/skills/data-visualize/scripts/plot.py \
  --type regression \
  --data '{"x": [40,50,55,60,65,70,75,80,90,100], "y": [2.4,2.9,3.0,3.5,3.7,4.0,4.5,4.7,5.3,6.0]}' \
  --config '{"title": "Đoán giá nhà từ diện tích", "xlabel": "Diện tích (m2)", "ylabel": "Giá (tỷ đồng)", "predict_x": 72}' \
  --output "train-the-trainer-nguyen-ly-ai/du-an-4-doan-gia-nha/assets/linear-regression.png"
```

### Bar chart

```bash
python3 ~/.kiro/skills/data-visualize/scripts/plot.py \
  --type bar \
  --data '{"labels": ["Spam", "Không spam"], "values": [30, 70]}' \
  --config '{"title": "Phân phối email", "ylabel": "Số lượng (%)"}' \
  --output "assets/email-distribution.png"
```

### Histogram

```bash
python3 ~/.kiro/skills/data-visualize/scripts/plot.py \
  --type histogram \
  --data '{"values": [1.2, 1.5, 1.8, 2.1, 2.3, 2.5, 2.8, 3.0, 3.2, 3.5]}' \
  --config '{"title": "Phân phối điểm thi", "xlabel": "Điểm", "ylabel": "Tần suất", "bins": 10}' \
  --output "assets/score-distribution.png"
```

## Quy tắc bắt buộc

- Luôn lưu file PNG vào thư mục assets của dự án (không phải workspace root).
- Đặt tên file kebab-case tiếng Việt không dấu (ví dụ: `linear-regression-scatter.png`).
- Sau khi tạo xong, thông báo: `✅ Đã tạo đồ thị: <đường dẫn file>.png`.
- Nếu cần chỉnh sửa dữ liệu/cấu hình, chạy lại script với tham số mới — không sửa file PNG trực tiếp.
