---
name: geometry-sketch
description: Vẽ hình hình học từ đề toán bằng TikZ và xuất ra file PNG để chèn vào tài liệu markdown hoặc Word. Kích hoạt skill này bất cứ khi nào người dùng cần vẽ hình minh hoạ cho một bài toán hình học (tam giác, đường tròn, tứ giác, hình chiếu, đường cao, trung tuyến, tiếp tuyến, đường tròn nội/ngoại tiếp...), kể cả khi họ chỉ nói "vẽ hình", "minh hoạ bài này", "hình bài 5", "render hình", hoặc đưa một đề toán hình học và muốn có ảnh kèm theo. Cũng dùng khi cần render lại một đoạn TikZ có sẵn ra PNG, hoặc khi một file markdown có code block ```tikz``` không hiển thị được và cần chuyển thành ảnh nhúng.
---

# geometry-sketch

Skill dùng để biến đề toán hình học thành hình ảnh PNG nhúng được vào markdown/Word.

Lý do tồn tại: viewer markdown phổ thông không render code block ```tikz``` trực tiếp, nên cần biên dịch thành ảnh raster. PNG được chọn vì chạy được mọi nơi, không phụ thuộc Ghostscript hay font đặc biệt.

## Quy trình tổng quát

1. Đọc đề, xác định các đối tượng và quan hệ hình học.
2. Đặt toạ độ cho các điểm anchor, suy ra các điểm còn lại bằng `calc`/`intersections`.
3. Sinh file `.tex` theo skeleton chuẩn (xem mục Skeleton bên dưới).
4. Gọi `scripts/render.sh <file.tex> <output.png>` để biên dịch và xuất PNG.
5. Trả về đường dẫn ảnh và cú pháp markdown `![alt](path)` để dán vào tài liệu.

## Bước 1. Phân tích đề

Liệt kê ra rồi xác nhận với chính mình trước khi vẽ:

- Các điểm: cái nào là "anchor" (đặt toạ độ thẳng), cái nào "derived" (chân vuông góc, trung điểm, giao điểm, trực tâm, tâm đường tròn...).
- Các đối tượng vẽ: đoạn thẳng, đường tròn, cung, tia, đa giác.
- Các quan hệ ràng buộc: vuông góc, song song, tiếp xúc, nội tiếp, ngoại tiếp, đồng quy, đối xứng.
- Các yếu tố nhấn: ký hiệu góc vuông, dấu bằng nhau, đoạn cần làm nổi bật.

Mục tiêu của bước này là tránh đặt toạ độ tuỳ ý rồi bị "lệch", phải sửa nhiều lần.

## Bước 2. Đặt toạ độ

Quy tắc giúp hình cân đối, dễ đọc:

- Khi có đường tròn, đặt tâm ở `(0,0)`, bán kính 3 (đơn vị TikZ). Đặt các điểm trên đường tròn bằng toạ độ cực `(angle:3)` để dễ điều chỉnh vị trí.
- Tam giác nhọn nội tiếp: chọn ba góc trong khoảng `[60°, 300°]`, cách nhau ít nhất 60°, tránh thẳng hàng. Ví dụ tam giác có `AB < AC`: `A=(90:3)`, `B=(200:3)`, `C=(-40:3)`.
- Điểm derived nên dùng cú pháp `calc` thay vì tính tay:
  - Trung điểm `M` của `AB`: `($(A)!0.5!(B)$)`.
  - Hình chiếu của `B` xuống `AC` (chân đường cao): `($(A)!(B)!(C)$)`.
  - Giao của hai đoạn: `(intersection of A--B and C--D)`.
  - Trực tâm: giao của hai đường cao.
- Khi cần giao của một đường thẳng với một đường tròn (ví dụ giao thứ hai của `BD` với `(O)`), cách đơn giản nhất là tính sẵn toạ độ số rồi ghi vào comment để sau dễ chỉnh. Cách "đẹp" hơn là dùng thư viện `intersections` với `name path`, nhưng phức tạp hơn.

Các thư viện cần load mặc định: `calc`, `intersections`, `through`, `angles`, `quotes`, `decorations.markings`.

## Bước 2b. Phối cảnh hình học không gian 3D (hình chóp, lăng trụ, tứ diện)

Khi vẽ hình không gian, PHẢI dùng phối cảnh xiên (cabinet oblique) để tạo chiều sâu. Không được vẽ hình 3D như hình phẳng 2D.

### Hệ trục phối cảnh cabinet

Dùng 3 vector cơ sở để chiếu điểm 3D (x,y,z) lên mặt phẳng vẽ 2D:

```
% Phối cảnh cabinet: trục x sang phải, trục y xiên lên-trái (tạo chiều sâu), trục z lên trên
\newcommand{\xvec}{1,0}        % trục x: sang phải
\newcommand{\yvec}{-0.4,0.25}  % trục y: xiên 30° tạo chiều sâu (hệ số 0.5 rút ngắn)
\newcommand{\zvec}{0,1}        % trục z: lên trên
% Điểm 3D -> 2D: P = x*xvec + y*yvec + z*zvec
```

### Toạ độ chuẩn cho các khối thường gặp

**Hình chóp S.ABCD đáy hình bình hành (hoặc vuông/chữ nhật):**
```latex
% Đáy: A ở gốc, B sang phải, C xiên phải-lên, D xiên trái-lên
\coordinate (A) at (0, 0);
\coordinate (B) at (3, 0);
\coordinate (C) at (3.8, 1.2);   % C = B + yvec direction
\coordinate (D) at (0.8, 1.2);   % D = A + yvec direction
% Đỉnh S lệch nhẹ về phía sau để rõ cấu trúc
\coordinate (S) at (1.6, 3.5);
```

**Tứ diện ABCD:**
```latex
\coordinate (A) at (0, 0);
\coordinate (B) at (3.2, 0);
\coordinate (C) at (2.4, 1.0);   % C lùi ra sau (phía trên-phải)
\coordinate (D) at (1.5, 3.0);   % D ở trên
```

**Lăng trụ ABC.A'B'C':**
```latex
\coordinate (A) at (0, 0);
\coordinate (B) at (2.8, 0);
\coordinate (C) at (1.8, 1.0);
% Tầng trên = tầng dưới + (0, 2.5) offset đứng
\coordinate (A') at (0, 2.5);
\coordinate (B') at (2.8, 2.5);
\coordinate (C') at (1.8, 3.5);
```

**Hình hộp ABCD.A'B'C'D':**
```latex
\coordinate (A) at (0, 0);
\coordinate (B) at (3, 0);
\coordinate (C) at (3.8, 1.0);
\coordinate (D) at (0.8, 1.0);
\coordinate (A') at (0, 2.5);
\coordinate (B') at (3, 2.5);
\coordinate (C') at (3.8, 3.5);
\coordinate (D') at (0.8, 3.5);
```

### Quy tắc cạnh khuất (nét đứt)

**BẮT BUỘC** phân biệt cạnh nhìn thấy (nét liền) và cạnh khuất (nét đứt mỏng):
- Cạnh khuất: `[thin, dashed]` — cạnh ở phía sau bị che bởi mặt trước.
- Cạnh thấy: `[thick]` — nét liền đậm.

Quy tắc xác định cạnh khuất:
- **Hình chóp S.ABCD**: nếu nhìn từ phía trước-trên, cạnh AD và CD thường bị khuất. SA cũng có thể khuất tùy góc nhìn.
- **Tứ diện**: luôn có 1-2 cạnh khuất. Thường là cạnh xa mắt nhất (cạnh nối đỉnh "phía sau").
- **Lăng trụ/hình hộp**: cạnh bên-sau và cạnh đáy-sau bị khuất.

Ví dụ:
```latex
% Hình chóp S.ABCD - cạnh khuất AD, DC, SA
\draw[thick] (A)--(B)--(C); % đáy phía trước
\draw[thin, dashed] (C)--(D)--(A); % đáy phía sau (khuất)
\draw[thick] (S)--(B); \draw[thick] (S)--(C); % cạnh bên thấy
\draw[thin, dashed] (S)--(A); \draw[thin, dashed] (S)--(D); % cạnh bên khuất
```

### Tỉ lệ phải đúng đề bài

Nếu đề nói AB = 2CD, thì trong hình vẽ, đoạn AB phải dài gấp đôi CD thực sự. Không được vẽ gần bằng nhau.

### Nhãn không chồng — QUY TẮC BẮT BUỘC

**Vấn đề thường gặp:** Nhãn bị đè lên cạnh, bị mất do tràn ra ngoài viewBox, hoặc 2 nhãn chồng nhau.

**Nguyên tắc offset tối thiểu:**
- Mỗi nhãn phải có offset (dx, dy) sao cho **tâm ký tự** cách **đỉnh điểm** ít nhất 10px.
- Hai nhãn bất kỳ phải cách nhau tối thiểu 15px (khoảng 1.5 lần font-size).

**Quy tắc vị trí nhãn theo vai trò đỉnh (SVG, viewBox 240×200):**

| Đỉnh | Vị trí nhãn | dx, dy |
|------|-------------|--------|
| S (đỉnh cao nhất) | Phía trên | dx=−5, dy=−12 |
| A (góc dưới-trái) | Bên trái, xuống dưới | dx=−14, dy=+10 |
| B (góc dưới-phải) | Bên phải, xuống dưới | dx=+5, dy=+10 |
| C (đáy sau-phải) | Bên phải | dx=+5, dy=−3 |
| D (đáy sau-trái) | Bên trái | dx=−16, dy=−3 |
| Điểm phụ (M, N, P) | Phía NGƯỢC với cạnh gần nhất | dx=±8, dy=±8 |

**Quy tắc chống trùng lặp nhãn với cạnh:**
- Nếu nhãn nằm trên đường nối 2 đỉnh kế cận → dịch nhãn ra phía ngoài hình (tăng |dx| hoặc |dy|).
- Nếu đỉnh nằm ở góc nhọn (2 cạnh gần nhau) → đặt nhãn phía đối diện góc nhọn.

**Quy tắc "B bị mất" (tràn viewBox):**
- Sau khi project() ra toạ độ SVG, kiểm tra: nếu x < 10 → dx phải ≥ 5; nếu x > 230 → dx phải ≤ −5.
- Nếu y < 10 → dy phải ≥ 12; nếu y > 190 → dy phải ≤ −10.
- Đặc biệt: **Điểm B** thường nằm sát mép phải (vì B=(3,0,0) → projected x ≈ 240). LÚC NÀO CŨNG phải kiểm tra B có tràn không. Nếu tràn, giảm scale hoặc tăng ox.

**Hình chóp SA⊥ — lỗi phổ biến:**
- Khi S nằm thẳng trên A (SA⊥ABCD), S và A có cùng toạ độ x sau project → nhãn S (above) và A (below) sẽ thẳng hàng dọc. KHÔNG được đặt cả 2 cùng dx=0. Dùng: S: dx=−5, A: dx=+5 (hoặc ngược lại) để tách ra.

**Kiểm tra cuối cùng (checklist bắt buộc trước khi output SVG):**
1. Tất cả nhãn nằm trong vùng (5, 5) đến (235, 195) của viewBox?
2. Không có 2 nhãn nào cách nhau < 12px?
3. Không có nhãn nào nằm trên đoạn thẳng (kiểm tra bằng mắt: text center cách line > 6px)?

### SVG inline (cho HTML quiz)

Khi output là file HTML (không phải markdown), dùng SVG inline thay vì PNG. Áp dụng đúng các nguyên tắc phối cảnh trên nhưng bằng SVG coordinates. Quy tắc tương tự:
- Cạnh khuất: `stroke-dasharray="5,4"` + `stroke-width` nhỏ hơn
- Cạnh thấy: nét liền + `stroke-width` dày
- Điểm phụ: `<circle>` nhỏ, nhãn dùng `<text>` đặt offset tránh chồng

### Auto-center & auto-scale (QUAN TRỌNG — chống cắt hình)

Sau khi tính toạ độ 3D cho tất cả các điểm, **PHẢI** chạy bước auto-fit trước khi xuất SVG:

```python
# 1. Project tất cả điểm với scale tạm (scale=1, ox=0, oy=0)
raw_points = [project_raw(p) for p in all_3d_points]  
# project_raw(x,y,z) = (x - 0.4*y, z + 0.25*y)

# 2. Tìm bounding box
min_x = min(p[0] for p in raw_points)
max_x = max(p[0] for p in raw_points)
min_y = min(p[1] for p in raw_points)
max_y = max(p[1] for p in raw_points)

# 3. Tính scale và offset cho viewBox 240×200 (margin 25px mỗi bên cho nhãn)
margin = 25
usable_w = 240 - 2*margin  # 190
usable_h = 200 - 2*margin  # 150
scale_x = usable_w / (max_x - min_x) if max_x > min_x else 40
scale_y = usable_h / (max_y - min_y) if max_y > min_y else 40
scale = min(scale_x, scale_y)

# 4. Center
cx = (min_x + max_x) / 2
cy = (min_y + max_y) / 2
ox = 120 - scale * cx
oy = 100 + scale * cy  # SVG y inverted

# 5. Final projection
def proj(x, y, z):
    rx = x - 0.4*y
    ry = z + 0.25*y
    return (ox + scale*rx, oy - scale*ry)  # oy - because SVG y goes down
```

**Tại sao cần auto-center:** Khi đáy hình chữ nhật dài (AB=3, AD=4), phối cảnh cabinet kéo hình sang phải rất nhiều. Nếu dùng ox=120 cố định, phần phải sẽ tràn ra ngoài viewBox → mất nhãn, mất cạnh.

**Quy tắc margin=25:** Dành 25px mỗi bên cho nhãn text (font-size 11-12 ≈ 8px cao, cần thêm offset). Không bao giờ đặt điểm sát mép viewBox.

### Escape `</` trong `<script>` (QUAN TRỌNG)

Khi nhúng SVG inline vào JS string bên trong thẻ `<script>`, **BẮT BUỘC** escape tất cả `</` thành `<\/` để browser HTML parser không nhầm là đóng tag:
```javascript
fig:'<svg ...><line .../><\/line><text ...>A<\/text><\/svg>'
// KHÔNG ĐƯỢC: </text>, </svg> — browser sẽ đóng <script> sớm!
```

### Escape dấu `'` trong nhãn (A′, B′, C′)

Khi nhãn chứa dấu prime (A', B'), dùng ký tự Unicode `′` (U+2032) thay vì apostrophe `'`:
```
>A′<  ✓  (Unicode prime)
>A'<  ✗  (Breaks JS string fig:'...')
```

## Bước 3. Skeleton file `.tex`

Luôn dùng `standalone` để PDF tự crop sát hình, không có lề thừa.

```latex
\documentclass[border=5pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,intersections,through,angles,quotes,decorations.markings}
\begin{document}
\begin{tikzpicture}[scale=1.2, line cap=round, line join=round]
  % --- Toạ độ ---
  \coordinate (O) at (0,0);
  \coordinate (A) at (90:3);
  % ...

  % --- Đối tượng chính ---
  \draw[thick] (O) circle (3);
  \draw[thick] (A) -- (B) -- (C) -- cycle;

  % --- Đối tượng phụ trợ (dashed/blue) ---
  \draw[blue, dashed] (I) circle (1.5);

  % --- Đối tượng nhấn (red) ---
  \draw[red, thick] (K) -- (D);

  % --- Ký hiệu góc vuông ---
  % vẽ một "khuỷu" 3 đoạn nhỏ tại đỉnh góc vuông
  \draw ($(D)+(-0.10,0.06)$) -- ($(D)+(-0.16,-0.04)$) -- ($(D)+(-0.06,-0.10)$);

  % --- Chấm điểm ---
  \foreach \p in {O,A,B,C} \fill (\p) circle (1.4pt);

  % --- Nhãn ---
  \node[above] at (A) {$A$};
  \node[below left] at (B) {$B$};
  \node[below right] at (C) {$C$};
\end{tikzpicture}
\end{document}
```

Quy ước style giúp hình rõ ràng (yêu cầu: in trắng đen vẫn phân biệt được):

- Nét chính: `thick`, màu đen mặc định, nét liền.
- Nét phụ trợ (đường tròn dựng hình, đường thẳng phụ): `[blue, thick]` nét liền. Chỉ dùng `blue` đậm, không dùng `blue!8`, `blue!50` vì in trắng đen sẽ mờ.
- Nét cần nhấn (kết luận của bài, đoạn cần chứng minh): `[red, thick]` nét liền.
- Nét đứt (`dashed`): chỉ dùng cho mục đích đặc biệt — chứng minh 3 điểm thẳng hàng, chứng minh điểm nằm trên đường thẳng/đường tròn, đường kéo dài giả định để xét giao. Các trường hợp khác dùng nét liền.
- Không dùng `fill=blue!8` hay tô nền nhạt cho đa giác — in trắng đen sẽ không thấy.
- Ký hiệu góc vuông: vẽ tay bằng 2 đoạn ngắn tạo thành chữ "L" gần đỉnh góc, kích thước 0.10-0.12 đơn vị TikZ. Hai cạnh ký hiệu phải bằng nhau, nên tính toạ độ bằng vector đơn vị (Python tính sẵn rồi gán toạ độ tuyệt đối) thay vì dùng `($(D)!0.10!(A)$)` — vì các cạnh tam giác có độ dài khác nhau sẽ làm hai cạnh ký hiệu lệch.
- Tránh dùng package `tkz-euclide` để giữ skill nhẹ.
- Nhãn điểm: dùng `node[above]`, `node[below left]`, `node[below right]`... đặt ở phía mà không bị đè lên đường khác.

## Bước 4. Render

Thư mục `scripts/` chứa `render.sh`. Cách dùng:

```bash
bash ~/.kiro/skills/geometry-sketch/scripts/render.sh <input.tex> <output.png> [max_size]
```

- `input.tex`: đường dẫn file TeX vừa sinh.
- `output.png`: đường dẫn ảnh đầu ra. Thư mục đích sẽ được tạo nếu chưa có.
- `max_size` (tuỳ chọn, mặc định 2400): cạnh dài nhất tính bằng pixel.

Script biên dịch trong thư mục tạm rồi copy PNG ra, không để rác trong workspace. Cần `pdflatex` và `sips` (macOS) hoặc `pdftoppm` (Linux/Poppler).

## Bước 5. Tích hợp output

Sau khi có PNG, trả về cho người dùng dưới dạng cú pháp markdown:

```markdown
![<mô tả ngắn>](<đường dẫn tương đối tới file md>)
```

Quy ước đặt tên file ảnh: `hinh-bai<N>-<motkhia>.png` (ví dụ `hinh-bai5-CMH-can.png`). Vị trí mặc định: thư mục `assets/` ở cùng cấp với file markdown đích. Nếu chưa có, tạo `assets/` rồi đặt ảnh vào.

## Tự kiểm trước khi giao

Đọc lại ảnh và kiểm:

- Các nhãn có bị chồng lên đường thẳng/điểm khác không? Nếu có, đổi `node[above]` sang hướng khác.
- Các điểm có bị quá gần nhau không? Nếu có, điều chỉnh góc của các điểm anchor.
- Đường tròn phụ có nằm gọn trong khung không? Nếu vượt ra ngoài, biên `border` của `standalone` sẽ tự nới, không cần lo.
- Hình có thể hiện đúng tính chất cần chứng minh không? Ví dụ "tam giác cân tại C" thì nhìn vào hình phải thấy `CM ≈ CH`.

Nếu sai, sửa file `.tex`, render lại, ghi đè PNG.

## Khi gặp hình quá phức tạp

Nếu một hình cần >50 dòng TikZ hoặc nhiều giao điểm ràng buộc nhau:

- Tách thành nhiều bước: vẽ phần xương sống trước, render thử, rồi mới thêm các đường phụ.
- Pre-compute toạ độ các điểm khó bằng tay (Python, máy tính), gắn comment giải thích, để lần sau ai đọc cũng hiểu.
- Cân nhắc dùng `templates/` làm điểm khởi đầu thay vì viết từ đầu.

## Templates có sẵn

Thư mục `templates/` chứa các khung TikZ thường gặp. Khi đề bài rơi vào một mẫu quen, copy template, chỉ thay vị trí điểm và đối tượng cần thêm. Xem `templates/README.md` để biết template nào ứng với loại bài nào.

## Ghi chú đặc biệt

- Không nhúng nguyên ```tikz``` vào file markdown vì hầu hết viewer không render được. Luôn xuất ra PNG.
- Không dùng `dvisvgm` để ra SVG khi máy chưa có Ghostscript: SVG sẽ bị mất nội dung TikZ phức tạp.
- Nếu người dùng bảo "vẽ thêm hình cho bài X" trong một file md đã có ảnh, kiểm tra `assets/` xem có ảnh nào trùng tên không, đổi tên để tránh ghi đè ngoài ý muốn.
