# TikZ cheatsheet cho hình học phổ thông

Tổng hợp các snippet hay gặp khi vẽ hình hình học, sắp theo nhu cầu.

## Đặt điểm

```tex
\coordinate (A) at (90:3);          % cực: góc 90°, bán kính 3
\coordinate (B) at (1.5,2);         % Descartes
\coordinate (M) at ($(A)!0.5!(B)$); % trung điểm AB
\coordinate (P) at ($(A)!0.3!(B)$); % chia AB theo tỉ số 3:7
```

## Hình chiếu vuông góc

```tex
% Chân vuông góc từ B xuống đường thẳng AC
\coordinate (H) at ($(A)!(B)!(C)$);
```

## Giao điểm

```tex
% Giao 2 đoạn
\coordinate (P) at (intersection of A--B and C--D);

% Giao đường thẳng và đường tròn (cần thư viện intersections)
\path[name path=line]   (A) -- (B);
\path[name path=circ]   (O) circle (3);
\path[name intersections={of=line and circ, by={P1,P2}}];
```

## Đường tròn

```tex
\draw (O) circle (3);                   % bán kính cứng
\draw let \p1 = ($(O)-(A)$) in
  (O) circle ({veclen(\x1,\y1)});       % bán kính = |OA|
```

## Cung

```tex
\draw (A) arc (start_angle:end_angle:radius);
\draw (A) arc (30:120:2);
```

## Nhãn

```tex
\node[above]       at (A) {$A$};
\node[below right] at (B) {$B$};
\node[left=2pt]    at (C) {$C$};
\node[anchor=south west] at (D) {$D$};   % chỉnh anchor cụ thể
```

Hướng nhãn nên đặt sao cho không đè lên đường khác. Khi điểm nằm trong tam giác, dùng `below right`/`above right` thường an toàn.

## Ký hiệu góc vuông

Vẽ tay bằng 2 đoạn ngắn tạo thành chữ "L" gần đỉnh góc:

```tex
% góc vuông tại P, hai cạnh hướng theo (1,0) và (0,1)
\draw ($(P)+(0.10,0)$) -- ($(P)+(0.10,0.10)$) -- ($(P)+(0,0.10)$);
```

Khi hai cạnh không trùng trục, đổi vector dịch chuyển cho khớp hướng cạnh.

## Cung góc + tên góc

```tex
\usetikzlibrary{angles,quotes}
\pic [draw, "$\alpha$", angle eccentricity=1.3, angle radius=8mm]
  {angle = B--A--C};   % đỉnh góc là A, hai cạnh AB và AC
```

## Đánh dấu đoạn bằng nhau

```tex
\usetikzlibrary{decorations.markings}
\draw[postaction={decorate}, decoration={
    markings, mark=at position 0.5 with {\draw (-0.05,-0.08)--(-0.05,0.08);
                                          \draw (0.05,-0.08)--(0.05,0.08);}}]
  (A) -- (B);
```

Đoạn `(B)--(C)` muốn cùng dấu thì gắn cùng decoration.

## Hệ trục toạ độ (đơn giản, không cần pgfplots)

```tex
\draw[->] (-2.5,0) -- (2.5,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,4) node[above] {$y$};
\foreach \i in {-2,-1,1,2} \draw (\i,0.05) -- (\i,-0.05) node[below] {$\i$};
```

## Tô màu, đậm/nhạt

```tex
\fill[red!20] (A) -- (B) -- (C) -- cycle;     % tô tam giác mờ đỏ
\draw[blue!70!black, very thick] (A) -- (B);
```

## Gợi ý chống "vỡ hình"

- Dùng `scale=1.2` ở `tikzpicture` để hình to vừa phải; tăng tới 1.5 nếu chữ quá nhỏ.
- Dùng `line cap=round, line join=round` để đầu nét mượt hơn.
- Khi nhiều đối tượng chồng chéo, vẽ phụ trợ `dashed` và để chúng vẽ trước (ở trên), nét chính vẽ sau (ở dưới trong code) để chính nằm "trên" trong hình.
