---
name: write-md-file
description: >
  Quy trình đáng tin cậy để tạo và ghi nội dung vào file markdown (.md), đặc biệt file dài (>50 dòng).
  Dùng skill này BẤT CỨ KHI NÀO cần tạo file .md mới hoặc ghi thêm nội dung vào file .md đã có
  Skill này ngăn chặn lỗi phổ biến nhất: gọi fsWrite/fsAppend mà quên truyền tham số text.
---
# Quy trình ghi file Markdown đáng tin cậy

## Vì sao cần skill này

Lỗi phổ biến nhất khi ghi file markdown dài là gọi `fsWrite` hoặc `fsAppend` **mà không truyền tham số `text`** — dẫn đến lỗi `Expected string, received null at path ["text"]` và file rỗng. Lỗi này đặc biệt hay xảy ra khi nội dung dài (>300 dòng) vì có xu hướng "tách thao tác" sai cách: gọi tool trước rồi định ghi sau. Thực tế `fsWrite` và `fsAppend` là **atomic** — path + text phải gửi **cùng một lệnh**.

## Quy tắc bắt buộc

### Quy tắc 1 — Mỗi lần gọi `fsWrite` hoặc `fsAppend` PHẢI có tham số `text` chứa nội dung thật

Không bao giờ gọi `fsWrite(path=...)` mà không có `text="nội dung thật"`. Không có khái niệm "mở file rỗng rồi ghi sau" — `fsWrite` là atomic.

Nếu chỉ muốn tạo file rỗng (hiếm khi cần), dùng `executeBash` với lệnh `touch`.

### Quy tắc 2 — Với file dài (>50 dòng), chia nội dung thành 2-3 khúc logic

Cách chia:

1. **Lần 1:** Gọi `fsWrite` với khúc đầu tiên (ví dụ: phần 1-2 của giáo trình). Tham số `text` chứa đầy đủ nội dung khúc 1.
2. **Lần 2+:** Gọi `fsAppend` cho các khúc tiếp theo. Mỗi lần `fsAppend` đều có tham số `text` chứa đầy đủ nội dung khúc đó.

Cách chia khúc hợp lý:

- Theo heading lớn (## Phần 1-2 / ## Phần 3 / ## Phần 4-6).
- Mỗi khúc khoảng 200-400 dòng — đủ lớn để có ý nghĩa, đủ nhỏ để không bị cắt.

### Quy tắc 3 — Khi tool báo lỗi `Expected string, received null at path ["text"]`, DỪNG NGAY

Lỗi này có nghĩa duy nhất: **bạn quên truyền tham số `text`**. Không lặp lại cùng lệnh. Sửa ngay bằng cách gọi lại tool với `text` đầy đủ.

### Quy tắc 4 — Kiểm tra file sau khi ghi

Sau khi ghi xong toàn bộ nội dung, chạy:

```bash
wc -l <đường-dẫn-file>
```

Nếu file có 0 dòng → ghi thất bại, cần ghi lại. Nếu số dòng hợp lý (>50 cho file dài) → thành công.

## Ví dụ đúng

### Tạo file markdown ngắn (<50 dòng)

Một lần gọi `fsWrite` duy nhất:

```
fsWrite(
  path="project/readme.md",
  text="# Tên dự án\n\nMô tả ngắn...\n\n## Cài đặt\n\n..."
)
```

### Tạo file markdown dài (pusví dụ: giáo trình ~600 dòng)

Chia thành 2 khúc:

```
// Khúc 1: Phần 1-2 (Giới thiệu + Kiến thức nền tảng)
fsWrite(
  path="du-an-1/textbook.md",
  text="# Dự án 1: ...\n\n## 1. Giới thiệu\n\n...\n\n## 2. Kiến thức nền tảng\n\n...\n\n---\n"
)

// Khúc 2: Phần 3-6 (Thực hành + Nâng cao + Ôn tập + Thuật ngữ)
fsAppend(
  path="du-an-1/textbook.md",
  text="\n## 3. Hướng dẫn thực hành\n\n...\n\n## 4. Nâng cao\n\n...\n\n## 5. Câu hỏi ôn tập\n\n...\n\n## 6. Thuật ngữ\n\n..."
)

// Kiểm tra
executeBash(command="wc -l du-an-1/textbook.md")
// Kết quả mong đợi: ~600 dòng
```

## Ví dụ SAI (tuyệt đối tránh)

```
// ❌ SAI — gọi fsWrite không có text
fsWrite(path="du-an-1/textbook.md")
// → Lỗi: Expected string, received null at path ["text"]
// → File rỗng hoặc không tạo được

// ❌ SAI — lặp lại cùng lỗi nhiều lần
fsWrite(path="du-an-1/textbook.md")  // lỗi lần 1
fsWrite(path="du-an-1/textbook.md")  // lỗi lần 2
fsAppend(path="du-an-1/textbook.md") // lỗi lần 3
// → Lặp 3+ lần cùng lỗi = không chấp nhận được

// ❌ SAI — tạo file rỗng bằng touch rồi quên fsAppend có text
executeBash(command="touch du-an-1/textbook.md")
fsAppend(path="du-an-1/textbook.md") // vẫn thiếu text!
```

## Checklist nhanh trước mỗi lần ghi file .md

- [ ] Tôi đã chuẩn bị nội dung text đầy đủ cho lần gọi tool này chưa?
- [ ] Tham số `text` có chứa nội dung thật (không phải null/rỗng) chưa?
- [ ] Nếu file dài, tôi đã chia thành 2-3 khúc logic chưa?
- [ ] Sau khi ghi xong, tôi sẽ kiểm tra bằng `wc -l` chưa?
