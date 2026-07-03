---
name: giao-an-5512
description: >
  Soạn giáo án (kế hoạch bài dạy) theo đúng Công văn 5512/BGDĐT-GDTrH,
  tức bám khung Phụ lục IV với I. Mục tiêu, II. Thiết bị dạy học và học liệu,
  III. Tiến trình dạy học gồm bốn hoạt động Mở đầu, Hình thành kiến thức,
  Luyện tập, Vận dụng, mỗi hoạt động đủ bốn mục Mục tiêu, Nội dung, Sản phẩm,
  Tổ chức thực hiện. Skill chạy tương tác qua bốn bước: hỏi nội dung muốn soạn,
  hỏi tài liệu tham khảo, đề xuất đề mục lớn chờ duyệt, rồi mới viết chi tiết ra
  file md. Hãy dùng skill này bất cứ khi nào người dùng nói "soạn giáo án",
  "viết giáo án", "giáo án 5512", "kế hoạch bài dạy", "giáo án theo công văn 5512",
  "giáo án THCS", "giáo án THPT", "KHBD", "giáo án phát triển năng lực",
  "soạn bài theo mẫu 5512", "giáo án theo Phụ lục IV", hoặc khi họ đưa một tên bài,
  môn học và lớp rồi muốn có một giáo án hoàn chỉnh theo mẫu của Bộ. Cũng kích hoạt
  khi người dùng đưa sách giáo khoa, chương trình, hay tài liệu và muốn biến thành
  giáo án chuẩn công văn 5512. Không dùng cho giáo án tiểu học theo Công văn 2345,
  cũng không dùng cho khung giáo án 5E rút gọn kiểu dự án.
---

## Khả năng

Soạn một kế hoạch bài dạy hoàn chỉnh, đúng khung Phụ lục IV của Công văn 5512/BGDĐT-GDTrH ngày 18/12/2020, dùng cho cấp trung học cơ sở và trung học phổ thông. Sản phẩm là một file markdown bám sát cấu trúc mà Bộ quy định, đủ chi tiết để giáo viên dùng trực tiếp trên lớp, chứ không phải một bản khung rỗng chỉ có tiêu đề.

Điểm cốt lõi của skill này là cách làm việc tương tác. Giáo án là sản phẩm cá nhân hoá cao: cùng một bài nhưng mỗi giáo viên có định hướng nội dung, đối tượng học sinh, thiết bị và dụng ý sư phạm khác nhau. Vì vậy skill không tự phóng tác một mạch từ đầu đến cuối, mà đi qua bốn bước có điểm dừng để người dùng dẫn dắt: hỏi nội dung, hỏi tài liệu, đề xuất đề mục lớn chờ duyệt, rồi mới viết chi tiết. Sau bốn bước tương tác đó, nếu bài cần hình vẽ (hình hình học, đồ thị, biểu đồ, ảnh minh hoạ tình huống thực tế), skill tiếp tục Bước 5 để bổ sung hình vào giáo án bằng cách gọi các skill/công cụ chuyên biệt (geometry-sketch, data-visualize, create-svg, hoặc MCP tạo ảnh).

## Khi nào dùng

1. Người dùng muốn soạn một giáo án hoặc kế hoạch bài dạy cho một bài học cụ thể ở cấp trung học cơ sở hoặc trung học phổ thông.
2. Người dùng nói rõ theo Công văn 5512, theo mẫu của Bộ, theo Phụ lục IV, hoặc giáo án phát triển năng lực.
3. Người dùng đưa tên bài, môn, lớp và muốn có bản giáo án hoàn chỉnh.
4. Người dùng đưa sách giáo khoa, chương trình hoặc tài liệu tham khảo và muốn chuyển thành giáo án chuẩn 5512.

## Nguyên tắc tương tác quan trọng nhất

Bốn bước dưới đây là các điểm dừng bắt buộc, không phải gợi ý. Mỗi bước phải dừng lại và chờ người dùng trả lời trước khi sang bước sau. Lý do là giáo án phản ánh ý đồ dạy học riêng của từng giáo viên, nên nếu skill tự đoán hết rồi viết luôn một bản dài thì khả năng cao là lệch hướng và người dùng phải viết lại từ đầu, mất công hơn là được giúp. Việc dừng lại hỏi không phải là rườm rà, mà là cách bảo đảm bản viết chi tiết cuối cùng đúng ngay từ lần đầu.

Cụ thể, tuyệt đối không nhảy thẳng tới bước viết chi tiết khi chưa có đề mục lớn được người dùng duyệt. Nếu người dùng nói ngay từ đầu kiểu "cứ soạn luôn đi, không cần hỏi", thì có thể rút gọn: gộp hỏi nội dung và tài liệu thành một lượt, vẫn trình đề mục lớn để họ liếc qua rồi mới viết, vì bước duyệt đề mục là chốt chặn rẻ nhất để tránh viết sai cả bài.

## Bước 1: Hỏi nội dung muốn soạn

Mở đầu bằng việc hỏi người dùng muốn soạn bài gì. Cần thu thập tối thiểu các thông tin sau, hỏi gọn trong một lượt chứ đừng hỏi lắt nhắt từng cái:

1. Tên bài dạy.
2. Môn học hoặc hoạt động giáo dục.
3. Lớp, hoặc ít nhất là cấp trung học cơ sở hay trung học phổ thông.
4. Số tiết dự kiến cho bài.
5. Bộ sách giáo khoa đang dùng nếu có, ví dụ Kết nối tri thức, Chân trời sáng tạo, Cánh Diều, vì cùng một bài nhưng mỗi bộ sách có cách tiếp cận và ngữ liệu khác nhau.

Nếu người dùng đã cung cấp sẵn một phần trong câu đầu tiên thì chỉ hỏi bổ sung phần còn thiếu, không hỏi lại cái đã biết.

## Bước 2: Hỏi tài liệu tham khảo

Sau khi rõ nội dung, hỏi người dùng có tài liệu tham khảo nào để bám vào không. Mục đích là để giáo án đúng với chương trình và ngữ liệu người dùng đang dạy, thay vì bịa nội dung chung chung. Gợi ý các dạng tài liệu:

1. File sách giáo khoa, sách giáo viên, hoặc ảnh chụp trang bài.
2. Yêu cầu cần đạt của bài trong Chương trình giáo dục phổ thông 2018 của môn.
3. Giáo án cũ, tài liệu của tổ chuyên môn, hoặc đường link tham khảo.
4. Ghi chú riêng của người dùng về định hướng, trọng tâm, hoặc đối tượng học sinh.

Nếu người dùng đưa file hoặc đường dẫn, hãy đọc kỹ để lấy yêu cầu cần đạt, mạch kiến thức, ngữ liệu và ví dụ cụ thể. Nếu người dùng nói không có tài liệu gì, thì dựa vào Chương trình giáo dục phổ thông 2018 và kiến thức chuẩn của môn để soạn, và nói rõ là đang soạn theo hiểu biết chung nên người dùng cần đối chiếu lại với sách đang dùng.

## Bước 3: Đề xuất đề mục lớn chờ duyệt

Trước khi viết chi tiết, trình cho người dùng một bản phác đề mục lớn để duyệt. Đây là bước quyết định chất lượng cả giáo án, vì nó chốt mạch bài trước khi đổ công viết câu chữ. Bản phác này gồm:

1. Phần đầu: tên bài, môn, lớp, số tiết đã chốt.
2. Ba nhóm mục tiêu dự kiến: về kiến thức, về năng lực (nêu tên năng lực chung và năng lực đặc thù sẽ nhắm tới), về phẩm chất.
3. Tên bốn hoạt động của tiến trình dạy học, mỗi hoạt động kèm một dòng cho biết ý tưởng cốt lõi và thời lượng dự kiến. Đặt tên hoạt động thể hiện kết quả, ví dụ thay vì chỉ ghi "Hoạt động Mở đầu" thì ghi "Hoạt động 1: Mở đầu - Vì sao nước biển lại mặn?".
4. Nếu bài trải trên nhiều tiết, nêu dự kiến phân bổ hoạt động theo từng tiết.

Trình bản phác này ngắn gọn trên một màn hình, rồi hỏi rõ người dùng có muốn chỉnh gì không, ví dụ thêm bớt hoạt động, đổi trọng tâm, đổi thời lượng. Chỉ khi người dùng đồng ý mới sang bước 4. Nếu người dùng yêu cầu sửa, cập nhật bản phác và trình lại để duyệt lần nữa.

## Bước 4: Viết chi tiết ra file md

Sau khi đề mục lớn được duyệt, đọc file template và viết giáo án chi tiết theo đúng khung.

Template Phụ lục IV nằm tại:
#[[file:.kiro/skills/giao-an-5512/references/Template-KHBD-PL4.md]]

Đọc file template này trước khi viết, bám đúng thứ tự các mục và hệ thống ký hiệu I, II, III rồi 1, 2, 3 rồi a, b, c, d. Đừng thêm mục lạ ngoài khung, cũng đừng bỏ mục nào trong khung.

Viết đủ bốn hoạt động, mỗi hoạt động đủ bốn mục a) Mục tiêu, b) Nội dung, c) Sản phẩm, d) Tổ chức thực hiện. Riêng mục d) Tổ chức thực hiện của mỗi hoạt động phải trình bày theo bốn bước mà Ghi chú 4 của công văn quy định: Giao nhiệm vụ học tập; Thực hiện nhiệm vụ; Báo cáo, thảo luận; Kết luận, nhận định. Đây là phần thể hiện rõ nhất một giáo án có đúng tinh thần 5512 hay không, nên đừng viết gộp chung chung.

## Bước 5: Bổ sung hình ảnh cho giáo án

Sau khi Bước 4 đã tạo ra bản viết chi tiết, rà soát lại giáo án để tìm những chỗ cần hình ảnh làm rõ nội dung, rồi tạo và chèn ảnh vào đúng chỗ. Bước 5 không phải điểm dừng chờ duyệt riêng như Bước 3, mà chạy tiếp ngay sau Bước 4 để hoàn thiện giáo án. Không phải bài nào cũng cần hình - đừng thêm hình chỉ để trang trí. Nhưng nếu có, phải chèn đúng chỗ và dùng đúng công cụ, vì một hình sai tỉ lệ hoặc sai ký hiệu còn tệ hơn không có hình.

### 5.1. Khi nào cần hình

Các mục thường cần hình:

- Bài hình học có định lí, ví dụ, bài tập: mọi hình minh hoạ quan hệ hình học (tam giác, đường tròn, đa giác, hình chiếu, đường cao, tiếp tuyến, hình chóp, lăng trụ...) phải có hình vẽ chính xác kèm theo, đặt ở mục Sản phẩm của hoạt động tương ứng.
- Bài đại số, giải tích, thống kê, xác suất: đồ thị hàm số, biểu đồ tần số, biểu đồ cột/tròn, sơ đồ cây xác suất, hình miền nghiệm của bất phương trình phải có hình đúng tỉ lệ.
- Hoạt động Mở đầu có tình huống thực tế: nếu SGK không có sẵn hình phù hợp, có thể tạo ảnh gợi mở để dùng khi trình chiếu, ví dụ ảnh mô phỏng nguyệt thực, ảnh cầu, ảnh bánh răng.
- Sản phẩm học tập dạng sơ đồ (sơ đồ tư duy, sơ đồ khối, sơ đồ phân loại, bảng tổng kết trực quan): nếu việc trực quan hoá giúp học sinh nhớ và tra cứu tốt hơn bảng chữ thuần.

Các mục thường KHÔNG cần thêm hình: những chỗ mà SGK đã có hình rõ và giáo viên chỉ dùng lại trong sách; các mục hành chính (Trường/Tổ/Thiết bị); bài môn khoa học xã hội thuần lí luận; các mục Tổ chức thực hiện (mô tả thao tác chứ không phải trình bày kiến thức).

### 5.2. Chọn công cụ theo loại hình

Ưu tiên công cụ vẽ chính xác cho hình toán học. Không dùng MCP tạo ảnh cho hình toán, vì mô hình sinh ảnh dễ vẽ sai tỉ lệ, sai ký hiệu, sai quan hệ hình học.

- Hình hình học chính xác (điểm, đoạn, góc, đường tròn, đa giác, ký hiệu vuông góc, hình chóp, lăng trụ): gọi skill geometry-sketch. Skill này dùng TikZ biên dịch thành PNG, đảm bảo hình chuẩn hình học và có thể chỉnh lại được.
- Đồ thị hàm số, biểu đồ thống kê, dữ liệu định lượng: gọi skill data-visualize để dùng matplotlib. Trục, tỉ lệ, số liệu chuẩn xác.
- Sơ đồ tư duy, sơ đồ khối, sơ đồ phân loại, infographic đơn giản: gọi skill create-svg. Nếu cần poster hoặc hình lớn nhiều tầng, gọi skill infographic.
- Ảnh minh hoạ tình huống thực tế, mô hình hoá đời sống (nguyệt thực, cầu, bánh răng, xe, ao hồ, đồng xu, sản phẩm mây tre đan...), tranh khơi gợi cho phần Mở đầu hoặc Vận dụng: gọi MCP tạo ảnh (ví dụ coworkai-generate-image). Nhớ dùng tier `high` nếu ảnh có chữ, và luôn tải ảnh về folder `assets/` cạnh file giáo án, không giữ URL ngoài, vì URL có thể hết hạn khiến giáo án hỏng ảnh về sau.

### 5.3. Vị trí chèn hình trong giáo án

- Hình minh hoạ khái niệm hoặc định lí: chèn ở mục c) Sản phẩm của hoạt động hình thành kiến thức đó, ngay dưới câu chữ mô tả sản phẩm.
- Ảnh gợi mở của Hoạt động Mở đầu: chèn ở mục b) Nội dung, ngay trước câu hỏi khơi gợi.
- Hình bài tập (như hình trong đề bài SGK): chèn ở mục b) Nội dung khi giới thiệu bài, và có thể lặp lại (nếu cần) ở mục c) Sản phẩm phần lời giải.
- Bảng tổng kết trực quan hoặc sơ đồ hệ thống hoá: chèn ngay sau bảng markdown tương ứng, không đặt trước.
- Không đặt hình ở đầu hoạt động (trước cả mục a) Mục tiêu) vì làm loãng cấu trúc.

### 5.4. Quy tắc file và cú pháp

- Lưu ảnh vào thư mục `assets/` cạnh file giáo án. Tạo thư mục nếu chưa có.
- Đặt tên file theo mẫu `hinh-<slug-tên-bài>-<mota-ngan>.png`, ví dụ `hinh-bai17-cat-nhau.png`, `hinh-luc-ma-sat-o-to-phanh.png`. Slug không dấu, nối bằng gạch ngang.
- Chèn bằng cú pháp markdown chuẩn `![alt-text mô tả nội dung hình](assets/tenfile.png)`. Alt-text viết tiếng Việt có dấu, ngắn gọn, mô tả cái hình thể hiện (không lặp lại tên bài).
- Với hình toán học, nếu công cụ vẽ (pdflatex trong geometry-sketch) bị lỗi font khi có chữ tiếng Việt trong hình, chuyển toàn bộ chú thích tiếng Việt sang alt-text markdown, chỉ giữ ký hiệu toán học (chữ Latin, công thức) bên trong hình.
- Với ảnh do MCP tạo ra, kiểm tra bản quyền và tính phù hợp sư phạm trước khi đưa vào giáo án (tránh ảnh có yếu tố không phù hợp với học sinh).

### 5.5. Rà soát sau khi chèn

Đọc lại giáo án và tự kiểm ba câu hỏi:

- Có hoạt động hình học/đại số nào chứa khái niệm quan trọng mà chưa có hình, khiến học sinh sẽ khó hình dung nếu giáo viên chỉ trình bày bằng lời không?
- Có hình nào chèn vào chỉ để "cho đẹp", không giúp làm rõ nhiệm vụ học tập không? Nếu có, gỡ ra để giáo án không bị loãng.
- Alt-text có đủ để giáo viên đọc file (khi chưa mở ảnh) vẫn hiểu ý hình muốn nói không?

Nếu có chỉnh sửa (thêm bớt, đổi hình), làm lại từ 5.2 với hình đó, không sửa vá vào ảnh cũ vì các công cụ vẽ đều re-render nhanh.

## Triết lý một giáo án 5512 có chất lượng

Khung Phụ lục IV rất dễ bị điền một cách hình thức, tức là chép lại đúng các đề mục nhưng nội dung bên trong rỗng và có thể dán vào bài nào cũng được. Một giáo án như vậy qua được hình thức kiểm tra nhưng vô dụng khi lên lớp. Mục tiêu của skill là viết được bản có sức sống thật. Hãy giữ các nguyên tắc sau.

1. Mục tiêu phải đo được và bám yêu cầu cần đạt. Ba nhóm mục tiêu có ba cách viết khác nhau, không được viết trộn phong cách:
   - Về kiến thức viết bằng danh từ (danh hoá nội dung), tức liệt kê các đơn vị kiến thức học sinh cần chiếm lĩnh, ví dụ "Khái niệm acid", "Hai tính chất hoá học chung của dung dịch acid", "Ứng dụng của ba acid thông dụng". Không viết dưới dạng "học sinh nêu được...", "học sinh trình bày được..." ở nhóm này, vì phần biểu hiện hành vi thuộc về nhóm năng lực.
   - Về năng lực viết bằng động từ hành động đo đếm được theo thang Bloom (Nhớ, Hiểu, Vận dụng, Phân tích, Đánh giá, Sáng tạo). Chọn động từ ứng với đúng mức nhận thức cần đạt, ví dụ "phát biểu được", "phân biệt được", "viết và cân bằng được", "phân tích được", "đề xuất được", "thiết kế được", không dùng "hiểu", "nắm được", "biết". Mỗi mục tiêu năng lực nên gắn với một sản phẩm hoặc tiêu chí có thể quan sát được (ví dụ "đề xuất được ít nhất ba biện pháp...", "trình bày được trong 2 phút..."). Khuyến khích ghi chú thêm mức Bloom trong ngoặc để dễ rà soát độ phủ.
   - Về phẩm chất viết bằng động từ hành vi cụ thể của học sinh trong hoạt động và trong đời sống, ví dụ "ghi trung thực kết quả quan sát", "chủ động tìm hiểu nhãn sản phẩm", không viết "nâng cao ý thức", "yêu thích môn học".
   Mỗi mục tiêu về sau phải có ít nhất một hoạt động và một sản phẩm tương ứng để đo, nếu không thì mục tiêu đó là thừa.

2. Mô tả hoạt động, không viết lời thoại. Theo Ghi chú 2 của công văn, giáo án không cần chép lời nói của giáo viên và học sinh, mà mô tả rõ giáo viên làm gì (giao nhiệm vụ, quan sát, gợi ý, nhận xét, đánh giá) và học sinh làm gì (đọc, làm, viết, trình bày, báo cáo). Tránh kiểu kịch bản "GV hỏi: ... HS trả lời: ...".

3. Bốn bước tổ chức phải là một chuỗi liền mạch, không phải bốn cái nhãn. Nhiệm vụ giao ở bước Giao nhiệm vụ phải đúng là cái được thực hiện, được báo cáo, rồi được kết luận. Ở bước Thực hiện nhiệm vụ nên dự kiến trước khó khăn của học sinh và cách giáo viên hỗ trợ, vì đó là phần cho thấy giáo viên thực sự hình dung được lớp học. Ở bước Kết luận, nhận định phải chốt được kiến thức và làm rõ nhiệm vụ tiếp theo, chứ không chỉ khen đúng sai.

4. Ba mục Mục tiêu, Nội dung, Sản phẩm của một hoạt động phải khớp nhau. Nội dung nêu nhiệm vụ học sinh làm; Sản phẩm là kết quả cụ thể quan sát được của chính nhiệm vụ đó; Mục tiêu là năng lực hoặc kiến thức đạt được qua nhiệm vụ đó. Nếu Sản phẩm không phải là đầu ra của Nội dung thì hoạt động bị lỏng.

5. Đánh giá cài xuyên suốt. Theo Ghi chú 3, kiểm tra đánh giá thường xuyên diễn ra ngay trong các hoạt động học qua hỏi đáp, viết, thực hành, thuyết trình, sản phẩm học tập. Hãy để dấu vết đánh giá này trong mục Sản phẩm và mục Tổ chức thực hiện, đừng dồn hết vào cuối bài.

6. Hoạt động Vận dụng gắn thực tiễn và thường giao về nhà. Theo Ghi chú 1, hoạt động Vận dụng chủ yếu giao cho học sinh làm ngoài lớp và chỉ đặt ra với bài có nội dung phù hợp. Thiết kế nhiệm vụ vận dụng gắn với tình huống thực tế của học sinh, không phải chỉ là thêm vài bài tập khó.

7. Bám ngữ liệu của bài, không chung chung. Nếu người dùng đã cung cấp sách giáo khoa hoặc yêu cầu cần đạt, hãy dùng đúng ví dụ, số liệu, ngữ liệu, tên bài tập của bài đó. Một giáo án hay là giáo án mà đọc lên biết ngay là của bài này, không phải bài khác.

## Định dạng và trình bày file

1. Viết bằng tiếng Việt có dấu, văn phong sư phạm, rõ ràng.
2. Dùng markdown headers cho các đề mục để file có cấu trúc điều hướng rõ ràng, không viết đề mục dưới dạng đoạn văn thường:
   - `#` cho tên bài dạy (một dòng duy nhất, ở đầu file, sau khối metadata Trường/Tổ/Giáo viên/Môn/Lớp/Thời gian).
   - `##` cho ba mục lớn I, II, III (I. Mục tiêu; II. Thiết bị dạy học và học liệu; III. Tiến trình dạy học).
   - `###` cho các mục con cấp một: ba nhóm mục tiêu (1. Về kiến thức, 2. Về năng lực, 3. Về phẩm chất) và bốn hoạt động (1. Hoạt động 1..., 2. Hoạt động 2..., 3. Hoạt động 3..., 4. Hoạt động 4...).
   - `####` cho các mục con cấp hai: bốn mục a) Mục tiêu, b) Nội dung, c) Sản phẩm, d) Tổ chức thực hiện trong mỗi hoạt động; hoặc dùng cho tên tiểu hoạt động (Tiểu hoạt động 2.1, 2.2, 2.3) nếu Hoạt động 2 được chia nhỏ.
   - `#####` cho bốn mục a), b), c), d) của tiểu hoạt động khi có phân cấp tiểu hoạt động.
3. Giữ đúng hệ thống ký hiệu bên trong nội dung của công văn: số La Mã I, II, III trong tên các mục lớn; số 1, 2, 3 trong tên các hoạt động và mục con mục tiêu; a, b, c, d trong tên bốn mục của hoạt động; các gạch đầu dòng cho bốn bước tổ chức thực hiện. Header markdown chỉ là lớp cấu trúc bên ngoài, không thay thế các ký hiệu này.
4. Ngoại lệ về đánh số: các ý nhỏ trong ba nhóm mục tiêu (1. Về kiến thức, 2. Về năng lực, 3. Về phẩm chất) dùng gạch đầu dòng, không đánh số 1, 2, 3. Lý do là danh sách này thường thay đổi khi giáo viên chỉnh sửa, đánh số dễ lệch và không phản ánh thứ tự bắt buộc. Riêng năng lực có hai cấp gạch đầu dòng: cấp một cho từng năng lực (năng lực khoa học tự nhiên, năng lực chung); cấp hai cho các thành phần bên trong.
5. Với các phần định lượng như bảng thiết bị hay phân phối tiết, có thể dùng bảng markdown cho dễ đọc.
6. Điền phần đầu (trường, tổ, họ tên giáo viên) bằng chỗ trống để người dùng tự điền, trừ khi họ đã cung cấp.

## Lưu file

Lưu file ở thư mục hiện tại, đặt tên theo mẫu `giao-an-5512-[slug-tên-bài].md`, trong đó slug là tên bài viết thường không dấu nối bằng gạch ngang, ví dụ `giao-an-5512-luc-ma-sat.md`. Nếu người dùng chỉ định nơi lưu khác thì theo ý người dùng. Sau khi lưu, báo đường dẫn file và tóm tắt ngắn gọn những gì đã soạn, mời người dùng xem và yêu cầu chỉnh nếu cần.
