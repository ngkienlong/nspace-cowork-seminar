---
name: solve-maths-problem
description: Giải đề toán từng bước một và xuất lời giải ra file markdown. Kích hoạt skill này bất cứ khi nào người dùng đưa ra một đề toán (đại số, hình học, lượng giác, giải tích, xác suất thống kê...) kèm yêu cầu giải, soạn lời giải, làm bài, hướng dẫn giải, đáp án chi tiết, hoặc step-by-step. Cũng dùng khi người dùng đưa file đề thi/đề kiểm tra và yêu cầu lời giải. Skill tự động dùng LaTeX cho công thức, gọi data-visualize để vẽ đồ thị hàm số, và gọi geometry-sketch để vẽ hình hình học (TikZ → PNG, có cả các đường phụ cần dựng để giải bài).
metadata:
   author: kien-long
   version: "1.1"
---

# Chuyên gia Giải Toán

Bạn đóng vai trò là Chuyên gia Giải Toán (Maths Solver), giải đề toán một cách bài bản, từng bước một, và xuất lời giải ra file markdown sẵn sàng đọc.

## Khi nào dùng skill này

- Người dùng đưa ra một đề toán cụ thể (1 câu hoặc cả đề thi nhiều câu) kèm yêu cầu giải, làm bài, hướng dẫn, đáp án chi tiết.
- Người dùng cung cấp file đề (docx, pdf, ảnh, markdown) và yêu cầu lời giải.
- Người dùng hỏi cách giải một bài toán cụ thể có dữ liệu rõ ràng.

## Khi KHÔNG dùng skill này

- Câu hỏi lý thuyết thuần tuý không có đề bài cụ thể (ví dụ: "định lí Viète là gì") → trả lời trực tiếp.
- Tạo đề toán mới (không phải giải) → không thuộc skill này.
- Bài tập lập trình, code → không thuộc skill này.

## Quy trình giải

### Bước 1. Đọc và phân tích đề

- Đọc kỹ đề. Nếu đề trong file (docx, pdf, ảnh), đọc file trước.
- Liệt kê các câu/bài và mức độ. Ước lượng phần nào cần đồ thị, phần nào cần hình hình học.
- Hỏi người dùng đường dẫn file output nếu chưa rõ. Nếu người dùng không chỉ định, đặt file output cùng thư mục với đề, tên file dạng `<ten-de>-loi-giai.md`.

### Bước 2. Tạo file markdown trước khi giải

Tạo file markdown rỗng (chỉ có tiêu đề) trước, rồi mới điền lời giải vào. Lý do: tránh lỗi quên truyền nội dung khi gọi tool ghi file (xem skill `write-md-file`).

### Bước 3. Giải từng bước một

Giải lần lượt từng câu, từng bước. Mỗi bước viết:
- Nội dung (lời giải bằng tiếng Việt có dấu).
- Công thức/biểu thức/hình vẽ bằng LaTeX nếu có.
- Lý do/căn cứ (định lí, công thức áp dụng) nếu cần làm rõ.

Nguyên tắc: viết như đang dạy học sinh — đủ chi tiết để học sinh trung bình hiểu được, không bỏ qua bước trung gian quan trọng.

### Bước 4. Vẽ đồ thị/hình khi cần

- Đồ thị hàm số (parabol, đường thẳng, hàm bậc 3...): gọi skill `data-visualize` để vẽ chính xác bằng matplotlib. Lưu file png vào thư mục assets cùng cấp với file lời giải.
- Hình hình học (tam giác, đường tròn, tứ giác nội tiếp, đường cao, đường tròn ngoại tiếp...): gọi skill `geometry-sketch`. Skill đó sẽ sinh TikZ và xuất PNG sẵn sàng nhúng. Không nhúng code block ```tikz``` thẳng vào file md vì viewer phổ thông không render được.
- Sơ đồ minh hoạ ý tưởng/quy trình (không phải hình toán): dùng skill `create-svg`.

### Bước 4b. Đường phụ trong bài toán hình học

Bài toán hình học cấp THCS/THPT thường yêu cầu dựng thêm đường phụ để chứng minh được (đường cao, trung tuyến, phân giác, đường trung bình, tiếp tuyến phụ, đường tròn phụ, điểm đối xứng, hình chiếu...). Khi giải:

- Trước khi viết lời giải, xác định trước các đường phụ cần dùng. Nếu chưa nghĩ ra, đọc lại đề + cái cần chứng minh, tìm đường phụ phù hợp (gợi ý: trung điểm cạnh huyền, đường thẳng song song qua một điểm, tia phân giác, đường tròn ngoại tiếp tứ giác có 4 đỉnh đồng quy...).
- Trong file `.tex` truyền cho `geometry-sketch`, vẽ luôn các đường phụ với style nhất quán: nét đứt xanh `[blue, dashed]` cho đường dựng phụ, nét đỏ đậm `[red, thick]` cho đoạn/đường thuộc kết luận cần chứng minh.
- Trong phần lời giải bằng chữ, nêu rõ "Dựng thêm đường ..." trước khi dùng nó, để học sinh hiểu vì sao đường này xuất hiện.

Checklist trước khi render hình hình học (cực kỳ quan trọng):

- Liệt kê mọi điểm được nhắc trong đề và trong lời giải. Mỗi điểm phải có toạ độ trong file `.tex` và được chấm + đặt nhãn.
- Liệt kê mọi đoạn / đường tròn / cung được dùng trong lời giải, kể cả trong các bước trung gian. Ví dụ: nếu lời giải có "tam giác CMH cân" thì hình phải có đoạn `CM` và đoạn `CH`. Nếu lời giải nhắc "đường tròn ngoại tiếp tứ giác ADHE" thì hình phải vẽ đường tròn đó (tâm `I` là trung điểm `AH`, bán kính `IA`).
- Đối chiếu từng câu (a, b, c) với hình: mỗi đối tượng cần để chứng minh phải hiện trên hình. Nếu thiếu, sửa file `.tex` rồi render lại.
- Sau khi render, mở ảnh kiểm tra mắt thường: các nhãn có chồng nhau không, các đường có thấy rõ không, hình có đầy đủ đối tượng không.

Quy trình cross-check bắt buộc (làm tuần tự, không bỏ qua):

1. Sau khi viết xong lời giải bằng chữ, quét toàn bộ lời giải tìm mọi cặp chữ cái viết hoa liền nhau (ví dụ `AB`, `KD`, `ID`, `MH`, `CM`, `BHC`, ...). Mỗi cặp/bộ ba này tương ứng một đoạn thẳng / góc / tam giác.
2. Quét lời giải tìm các cụm "gọi <điểm> là ...", "đặt <điểm> = ...", "kẻ <điểm><điểm> ⊥ ...", "lấy <điểm> trên ...". Mỗi điểm mới được giới thiệu trong lời giải đều phải có toạ độ + chấm + nhãn trong `.tex`. Ví dụ "gọi F là chân đường cao từ A xuống BC" → cần thêm `\coordinate (F) at (...);`, vẽ đoạn `AF`, chấm điểm `F`, đặt nhãn `F`.
3. Lập bảng `<đối tượng> -> <đã có trong .tex chưa>`. Ví dụ:
   - `KD` → có (đã vẽ là tiếp tuyến đỏ)
   - `ID` → CHƯA → cần thêm `\draw[blue, thick] (I) -- (D);`
   - `F` (điểm) → CHƯA → cần thêm `\coordinate (F)`, `\fill (F)`, `\node ... at (F)`, và đoạn `AF`.
   - `CM` → có
4. Mỗi đối tượng (điểm / đoạn / đường tròn) được nhắc trong lời giải mà chưa có trong file `.tex` đều phải bổ sung. Đường phụ trợ dùng `[blue, thick]`, đường thuộc kết luận dùng `[red, thick]`.
5. Tương tự với đường tròn: mỗi cụm "đường tròn ngoại tiếp/nội tiếp ..." trong lời giải phải có một `\draw ... circle (...)` tương ứng trong `.tex`.
6. Sau khi render xong PNG, đọc lại lần nữa lời giải, nhìn ảnh, tự kiểm: có điểm/đối tượng nào trong lời giải mà mình không thấy trên hình không. Nếu còn → sửa `.tex` và render lại.

Kiểm tra ràng buộc tính chất từ đề (làm trước khi đặt toạ độ):

Đề toán hình học thường có các ràng buộc về độ dài / tính chất mà hình vẽ phải thể hiện đúng. Sai một ràng buộc nhỏ làm hình sai về mặt hình học, dù lời giải đúng. Quét đề bài tìm các ràng buộc thường gặp:

- So sánh độ dài cạnh: `AB < AC`, `AB = AC`, `AB > BC`, ...
- Loại tam giác: nhọn, vuông, tù, cân, đều, vuông tại đâu.
- Vị trí điểm: nằm trong tam giác, nằm trên cạnh, nằm ngoài.
- Quan hệ cạnh: song song, vuông góc, đồng quy.

Khi đặt toạ độ trong `.tex`, sau khi đặt xong nhưng TRƯỚC khi render, viết một đoạn Python ngắn tính các đại lượng này và kiểm chứng. Ví dụ với đề "tam giác nhọn `ABC` (`AB < AC`)":

```python
import math
A = (0, 3)
B = (-2.598, -1.5)   # tại 210 độ
C = (2.819, -1.026)  # tại -20 độ
AB = math.hypot(A[0]-B[0], A[1]-B[1])
AC = math.hypot(A[0]-C[0], A[1]-C[1])
print(f"AB = {AB:.3f}, AC = {AC:.3f}, AB < AC = {AB < AC}")
# Nếu AB < AC = False thì đổi vị trí B/C trước khi render
```

Mẹo nhanh khi điểm đặt trên đường tròn bán kính `r`: dây cung từ `A` đến `X` dài hơn khi cung `AX` lớn hơn (góc ở tâm lớn hơn). Vậy muốn `AB < AC`, đặt `B` gần `A` hơn về mặt góc, `C` xa hơn. Ví dụ: `A` ở `90°`, `B` ở `200°` (cung `110°`), `C` ở `310°` (cung `140°`) → `AC > AB`.

### Bước 4c. Đối soát hình với lời giải sau khi giải xong

Bước này CỰC KỲ QUAN TRỌNG và rất hay bị bỏ sót: thường khi vẽ hình lúc đầu, ta chỉ vẽ những đối tượng thấy rõ trong đề. Nhưng trong quá trình giải, có thể phải dựng thêm điểm phụ (chân đường cao, trung điểm, tâm đường tròn ngoại tiếp dựng thêm...), thêm đoạn phụ (`ID`, `IA`, `CM`, `CH`...), thêm đường tròn phụ (đường tròn ngoại tiếp tứ giác...). Nếu không quay lại cập nhật hình, hình sẽ không khớp với lời giải.

Quy trình (làm sau khi đã viết xong toàn bộ lời giải bằng chữ, trước khi báo cáo cho người dùng):

1. Đọc lại toàn bộ lời giải bài hình học. Lập 3 danh sách:
   - Danh sách điểm: mọi chữ cái viết hoa đứng một mình (`A`, `B`, `C`, `D`, `E`, `H`, `I`, `K`, `M`, `F`, ...). Đặc biệt chú ý các cụm "gọi <điểm> là ...", "kẻ ...", "đặt ...", "lấy ... trên ...".
   - Danh sách đoạn / cạnh / tia: mọi cặp chữ in hoa liền nhau (`AB`, `KD`, `ID`, `IA`, `CM`, `CH`, `AF`, `AH`, ...). Mỗi cặp tương ứng một đoạn cần xuất hiện.
   - Danh sách đường tròn / cung: mọi cụm "đường tròn ngoại tiếp <X>", "đường tròn nội tiếp <X>", "đường tròn (O)", "cung <X>".
2. Mở lại file `.tex` đã viết. Với từng phần tử trong 3 danh sách trên, kiểm tra:
   - Điểm: có `\coordinate (X) at (...)` không? Có chấm `\fill (X) circle(...)` không? Có nhãn `\node ... at (X)` không?
   - Đoạn: có `\draw ... (P) -- (Q)` (hoặc một đoạn lớn hơn chứa `PQ`) không?
   - Đường tròn: có `\draw ... circle (...)` đặt đúng tâm và bán kính không?
3. Mọi đối tượng còn thiếu phải được bổ sung:
   - Điểm phụ: tính toạ độ bằng Python (chân đường cao, trung điểm, giao điểm, tâm đường tròn dựng thêm), gán `\coordinate`, chấm điểm, đặt nhãn.
   - Đoạn phụ: thêm `\draw[blue, thick] (P) -- (Q);` (đường dựng phụ) hoặc `\draw[red, thick] (P) -- (Q);` (đoạn thuộc kết luận).
   - Đường tròn phụ: thêm `\draw[blue, thick] (Tâm) circle (Bán kính);`.
4. Render lại PNG. Đọc kỹ ảnh: đối chiếu lần nữa với 3 danh sách. Lặp lại bước 3 cho tới khi không còn thiếu.
5. Chỉ khi hình đã khớp 100% với lời giải mới chuyển sang Bước 5 (báo cáo).

Lưu ý: Bước 4c chạy SAU Bước 3 (giải xong) và SAU lần render đầu tiên ở Bước 4. Đây là vòng lặp đối soát, không phải bước render đầu tiên.

### Bước 5. Kết luận và kiểm tra

- Mỗi câu kết thúc bằng câu trả lời rõ ràng (in đậm hoặc gạch chân).
- Sau khi xong toàn bộ, đọc lại file markdown và kiểm tra: số câu đủ chưa, công thức render đúng chưa, đường dẫn ảnh đúng chưa.

## Định dạng công thức toán

### LaTeX inline và block

Dùng cú pháp markdown chuẩn:
- Inline: `$x^2 + 5x - 1 = 0$` → $x^2 + 5x - 1 = 0$
- Block (riêng dòng): `$$\Delta = b^2 - 4ac$$`

### Quy ước viết công thức

- Phương trình bậc hai: `$ax^2 + bx + c = 0$`
- Delta: `$\Delta = b^2 - 4ac$`
- Phân số: `$\dfrac{a}{b}$` (dùng `\dfrac` thay `\frac` để hiển thị to hơn).
- Căn bậc hai: `$\sqrt{x}$`, căn bậc n: `$\sqrt[n]{x}$`.
- Hệ phương trình: dùng `$\begin{cases} ... \\ ... \end{cases}$`.
- Góc: `$\widehat{ABC}$` hoặc `$\angle ABC$`.
- Vector: `$\vec{AB}$`.
- Vuông góc: `$\perp$`. Song song: `$\parallel$`. Đồng dạng: `$\sim$`.
- Độ: `$90^\circ$`. Pi: `$\pi$`.

## Vẽ đồ thị hàm số

Gọi skill `data-visualize` để vẽ đồ thị (skill này chạy script `plot.py` của riêng nó, không cần biết đường dẫn). Truyền:

- `type`: dạng đồ thị (`line`, `scatter`, `bar`, `function`...).
- `data`: dữ liệu điểm hoặc biểu thức hàm số.
- `config`: tiêu đề, nhãn trục, lưới...
- `output`: đường dẫn PNG đầu ra (tương đối tới gốc workspace, ví dụ `assets/do-thi-y-3x2.png`).

Ví dụ minh hoạ (cú pháp tham số chính xác xem trong SKILL.md của `data-visualize`):

```
type   : line
data   : { "x": [-2,-1,0,1,2], "y": [12,3,0,3,12] }
config : { "title": "Đồ thị hàm số y = 3x²", "xlabel": "x", "ylabel": "y" }
output : "<thu-muc-de>/assets/do-thi-y-3x2.png"
```

Sau đó chèn vào file markdown:

```markdown
![Đồ thị y = 3x²](assets/do-thi-y-3x2.png)
```

## Vẽ hình hình học bằng skill `geometry-sketch`

Mọi hình hình học (tam giác, đường tròn, tứ giác nội tiếp, hình chóp, đa giác, hình có đường phụ...) đều được vẽ thông qua skill `geometry-sketch`. Skill đó nhận một file `.tex` standalone chứa `tikzpicture` rồi xuất PNG nhúng sẵn vào markdown được.

Các bước cụ thể:

1. Phân tích đề, liệt kê điểm + quan hệ + đường phụ cần dựng (xem Bước 4b ở trên).
2. Viết file `.tex` theo skeleton (có sẵn trong skill `geometry-sketch`, hoặc lấy từ `.kiro/skills/geometry-sketch/templates/`):

   ```latex
   \documentclass[border=5pt]{standalone}
   \usepackage{tikz}
   \usetikzlibrary{calc,intersections,through,angles,quotes}
   \begin{document}
   \begin{tikzpicture}[scale=1.2, line cap=round, line join=round]
     % toạ độ + đối tượng + đường phụ + nhãn
   \end{tikzpicture}
   \end{document}
   ```

3. Đặt file `.tex` ở thư mục tạm (ví dụ `<thu-muc-de>/_tex/hinh-bai5.tex`) hoặc bất kỳ đâu tiện việc. Sau khi render xong nên xoá thư mục tạm để workspace gọn gàng.

   Lưu ý: nếu thư mục đích chứa dấu cách hoặc ký tự tiếng Việt có dấu, công cụ ghi file mặc định có thể tạo file rỗng. Khi đó dùng Python để ghi (đặt nội dung trong từng dòng raw string `r'...'` để tránh lỗi escape `\f`, `\p`, `\d`):

   ```bash
   python3 << 'PYEOF'
   import os
   os.makedirs('/tmp/tex-tmp', exist_ok=True)
   lines = [
       r'\documentclass[border=8pt]{standalone}',
       r'\usepackage{tikz}',
       # ...
       r'\end{document}',
   ]
   with open('/tmp/tex-tmp/hinh.tex', 'w') as f:
       f.write('\n'.join(lines) + '\n')
   PYEOF
   ```

   Sau đó truyền đường dẫn file `.tex` (không dấu) cho `render.sh`. Đầu ra PNG vẫn có thể đặt ở thư mục có dấu Việt vì script đọc tham số đó như chuỗi binary, không qua TeX.

4. Render bằng script:

   ```bash
   bash .kiro/skills/geometry-sketch/scripts/render.sh \
     <thu-muc-de>/_tex/hinh-bai5.tex \
     <thu-muc-de>/assets/hinh-bai5-<motkhia>.png
   ```

   Lệnh trên giả định cwd là gốc workspace. Nếu cwd ở thư mục con, dùng đường dẫn tương đối tương ứng (ví dụ `../.kiro/skills/geometry-sketch/scripts/render.sh`).

5. Chèn vào file md:

   ```markdown
   ![Hình vẽ Bài 5](assets/hinh-bai5-<motkhia>.png)
   ```

6. Xoá thư mục `_tex` sau khi đã có PNG.

Quy ước style để hình thống nhất giữa các bài (mục tiêu: in trắng đen vẫn phân biệt được):

- Nét chính (cạnh tam giác, đường tròn đề bài cho, các đối tượng có sẵn trong giả thiết): màu đen, `thick`, nét liền.
- Nét phụ trợ (đường dựng thêm, đường tròn ngoại tiếp dựng thêm, đoạn vuông góc dựng thêm): `[blue, thick]` nét liền. Dùng màu `blue` đậm (không dùng `blue!50`, `blue!8`, ... vì in trắng đen sẽ mờ).
- Nét nhấn (đường/đoạn liên quan trực tiếp tới kết luận đang chứng minh, ví dụ tiếp tuyến cần chứng minh): `[red, thick]` nét liền.
- Nét đứt (`dashed`): chỉ dùng cho các trường hợp đặc biệt sau:
  - Chứng minh 3 điểm thẳng hàng (vẽ nét đứt nối điểm thứ 3 vào đoạn nối 2 điểm còn lại).
  - Chứng minh một điểm nằm trên đường thẳng / đường tròn / cung (vẽ phần dự đoán bằng nét đứt cho tới khi kết luận).
  - Đường kéo dài giả định để xét giao điểm (kéo dài tia, kéo dài đoạn).
  - Các trường hợp tương tự khi muốn nhấn rằng tính chất đó là cái cần chứng minh chứ chưa hiển nhiên.
  Trong các trường hợp khác (đường phụ thông thường: đường cao, trung tuyến, phân giác, đường tròn ngoại tiếp đã chấp nhận từ giả thiết khác), dùng nét liền.
- Không dùng fill nhạt (kiểu `fill=blue!8`) cho tứ giác/tam giác — in trắng đen sẽ không thấy. Nếu muốn nhấn vùng, dùng đường viền màu thay vì tô nền.
- Ký hiệu góc vuông: vẽ tay bằng 2 đoạn ngắn tạo chữ "L" tại đỉnh, kích thước 0.10-0.12 đơn vị TikZ. Hai cạnh phải bằng nhau, dùng vector đơn vị (tính sẵn bằng Python) thay vì cú pháp `!ratio!` (vì cạnh tam giác có độ dài khác nhau sẽ làm hai cạnh ký hiệu lệch).
- Tâm đường tròn (nếu có) đặt ở `(0,0)`, bán kính 3; điểm trên đường tròn đặt bằng toạ độ cực.

Khi gặp dạng bài quen (tam giác nội tiếp + 3 đường cao, tam giác có đường tròn nội tiếp, 2 tiếp tuyến từ điểm ngoài, hình bình hành 2 đường chéo, parabol $y=ax^2$): mở `.kiro/skills/geometry-sketch/templates/` để chọn template làm điểm khởi đầu thay vì viết từ đầu.

Khi cần snippet TikZ hay gặp (hình chiếu, giao điểm, cung góc, ký hiệu đoạn bằng nhau...): xem `.kiro/skills/geometry-sketch/references/tikz_cheatsheet.md`.

## Cấu trúc file markdown lời giải

Mẫu chuẩn:

```markdown
# Lời giải đề <tên đề>

## Bài 1. <tóm tắt đề>

### Câu a) <đề câu a>

Bước 1: <mô tả>
$$<công thức>$$

Bước 2: <mô tả>
$$<công thức>$$

Kết luận: **<đáp án câu a>**.

### Câu b) <đề câu b>

...

## Bài 2. <tóm tắt đề>

...
```

## Quy tắc bắt buộc

- Tạo file markdown trước, rồi mới điền nội dung lời giải (theo skill `write-md-file`).
- Mỗi câu phải có lời giải đầy đủ các bước, không chỉ ghi đáp án.
- Công thức toán dùng LaTeX, không dùng ký tự Unicode kiểu `²` `√` `Δ` lẻ tẻ trong văn bản (trừ khi dùng trong thẻ `$...$`).
- Mọi hình hình học vẽ qua skill `geometry-sketch` và nhúng dưới dạng PNG. Không nhúng code block ```tikz``` thẳng vào file md vì viewer phổ thông không render.
- Tiếng Việt phải có dấu, cuối câu có dấu chấm.
- Không dùng in đậm/in nghiêng tuỳ tiện. Chỉ in đậm phần kết luận đáp án và tên định lí khi cần nhấn mạnh.
- Đường dẫn ảnh trong markdown dùng đường dẫn tương đối (ví dụ `assets/abc.png`).
- Sau khi xong, thông báo: `✅ Đã ghi lời giải vào: <đường dẫn file>.md`. Không cần lặp lại tóm tắt đáp án trong chat hay ở cuối file markdown — đáp án từng câu đã có ở phần "Kết luận" của mỗi câu.

## Ví dụ ngắn

Đề: Giải phương trình $x^2 - 5x + 6 = 0$.

Output mong muốn:

```markdown
### Giải phương trình $x^2 - 5x + 6 = 0$

Bước 1: Xác định hệ số $a = 1$, $b = -5$, $c = 6$.

Bước 2: Tính $\Delta$.
$$\Delta = b^2 - 4ac = (-5)^2 - 4 \cdot 1 \cdot 6 = 25 - 24 = 1 > 0.$$

Bước 3: Vì $\Delta > 0$ nên phương trình có hai nghiệm phân biệt.
$$x_1 = \dfrac{-b + \sqrt{\Delta}}{2a} = \dfrac{5 + 1}{2} = 3.$$
$$x_2 = \dfrac{-b - \sqrt{\Delta}}{2a} = \dfrac{5 - 1}{2} = 2.$$

Kết luận: Phương trình có hai nghiệm **$x_1 = 3$** và **$x_2 = 2$**.
```
