# Tài liệu về Commit trong Git và GitHub

## 1. **Khái niệm về Commit**

Trong Git, **commit** là một thao tác quan trọng để ghi lại các thay đổi vào trong kho mã nguồn (repository). Mỗi commit
đại diện cho một điểm snapshot trong lịch sử phát triển của dự án. Commit giúp theo dõi các thay đổi và lưu lại thông
tin về việc cập nhật mã nguồn hoặc tài liệu của dự án. Mỗi commit có thể kèm theo một thông điệp (commit message) giải
thích về các thay đổi đã được thực hiện.

### 1.1. **Cấu trúc của Commit**

Một commit trong Git bao gồm:

- **Hash (SHA-1)**: Mỗi commit được nhận diện bởi một mã hash duy nhất (một chuỗi ký tự dài), giúp xác định commit đó
  trong toàn bộ lịch sử dự án.
- **Author**: Người thực hiện commit, bao gồm tên và email.
- **Date**: Ngày và giờ thực hiện commit.
- **Message**: Thông điệp mô tả chi tiết các thay đổi đã được thực hiện.

## 2. **Các thao tác cơ bản với Commit**

### 2.1. **Chuẩn bị Commit (Staging)**

Trước khi commit, bạn cần đưa các thay đổi vào vùng staging (giai đoạn chuẩn bị commit). Bạn có thể chọn commit toàn bộ
thay đổi hoặc chỉ một phần cụ thể.

- **Thêm một tệp vào staging**:

```bash
git add <file-name>
```

- **Thêm tất cả các tệp thay đổi vào staging**:

```bash
git add .
```

### 2.2. **Commit các thay đổi**

Khi các thay đổi đã sẵn sàng trong staging, bạn có thể thực hiện commit với thông điệp mô tả chi tiết về những thay đổi
đã thực hiện.

- **Commit với thông điệp mô tả**:

```bash
git commit -m "Mô tả chi tiết các thay đổi"
```

Lưu ý rằng thông điệp commit cần ngắn gọn, rõ ràng, và mô tả chính xác các thay đổi, ví dụ:

```bash
git commit -m "Sửa lỗi hiển thị giao diện trên trình duyệt Safari"
```

### 2.3. **Commit với nhiều tệp thay đổi**

Nếu bạn thay đổi nhiều tệp, bạn có thể commit tất cả chúng hoặc chọn từng tệp một.

- **Commit tất cả thay đổi**:

```bash
git commit -a -m "Thêm tính năng mới cho trang chủ"
```

Lệnh này sẽ tự động thêm tất cả các tệp đã được chỉnh sửa vào staging và commit chúng.

### 2.4. **Commit lại (Amend Commit)**

Khi bạn đã thực hiện commit nhưng muốn thay đổi thông điệp hoặc bổ sung thêm thay đổi, bạn có thể sửa lại commit vừa rồi
mà không tạo thêm một commit mới.

- **Sửa lại commit cuối cùng**:

```bash
git commit --amend
```

Lệnh này cho phép bạn thay đổi thông điệp commit hoặc thêm các thay đổi mới vào commit gần nhất.

### 2.5. **Commit với nhiều thông điệp**

Bạn có thể sử dụng một trình soạn thảo văn bản để viết thông điệp commit dài hoặc chi tiết hơn, thay vì chỉ viết trong
một dòng.

- **Mở trình soạn thảo để viết thông điệp dài**:

```bash
git commit
```

Điều này sẽ mở một trình soạn thảo (như Vim hoặc Nano), nơi bạn có thể viết thông điệp commit nhiều dòng.

## 3. **Thông điệp Commit (Commit Message)**

Thông điệp commit giúp người khác (và chính bạn) hiểu được lý do tại sao một thay đổi được thực hiện. Thông điệp commit
nên tuân thủ một số quy tắc để dễ đọc và dễ hiểu:

- **Chủ đề ngắn gọn (50 ký tự)**: Dòng đầu tiên của thông điệp commit nên mô tả ngắn gọn mục đích thay đổi (không vượt
  quá 50 ký tự).
- **Mô tả chi tiết (tùy chọn, dưới 72 ký tự mỗi dòng)**: Nếu cần thiết, bạn có thể thêm phần mô tả chi tiết về thay đổi
  dưới dòng đầu tiên, mỗi dòng không dài quá 72 ký tự.
- **Không dùng "I" (tôi) trong thông điệp**: Ví dụ: “Sửa lỗi hiển thị” thay vì “Tôi đã sửa lỗi hiển thị”.

Ví dụ thông điệp commit chuẩn:

```
Thêm tính năng đăng nhập bằng Google

Tính năng đăng nhập bằng Google đã được tích hợp vào hệ thống.
Thêm các tệp cấu hình OAuth và cập nhật giao diện người dùng.
```

## 4. **Lịch sử Commit**

Git lưu lại tất cả các commit trong lịch sử dự án, và bạn có thể xem lại các commit này bất cứ lúc nào. Các lệnh sau
giúp bạn xem lại lịch sử commit:

### 4.1. **Xem lịch sử commit**

```bash
git log
```

Lệnh này hiển thị toàn bộ lịch sử commit, từ commit mới nhất đến cũ nhất. Bạn có thể cuộn lên và xuống để xem các
commit.

### 4.2. **Xem lịch sử commit với dạng ngắn gọn**

```bash
git log --oneline
```

Lệnh này sẽ hiển thị lịch sử commit theo dạng mỗi commit trên một dòng, chỉ bao gồm hash ngắn và thông điệp commit.

### 4.3. **Xem lịch sử commit của một tệp**

```bash
git log <file-name>
```

Lệnh này hiển thị lịch sử commit chỉ liên quan đến một tệp cụ thể.

## 5. **Commit và GitHub**

### 5.1. **Push Commit lên GitHub**

Sau khi thực hiện commit trên máy tính cá nhân, bạn cần đẩy các commit đó lên GitHub để chia sẻ với người khác.

- **Push commit lên GitHub**:

```bash
git push origin main
```

Lệnh này sẽ đẩy các commit trong nhánh chính (main) lên GitHub.

### 5.2. **Pull Commit từ GitHub**

Khi bạn làm việc trong môi trường nhóm, có thể có các commit được thực hiện bởi những người khác. Bạn có thể pull các
thay đổi đó từ GitHub về máy của mình.

- **Pull commit từ GitHub**:

```bash
git pull origin main
```

Lệnh này sẽ kéo các commit mới nhất từ GitHub về và hợp nhất chúng vào nhánh hiện tại của bạn.

## 6. **Best Practices khi sử dụng Commit**

- **Commit thường xuyên**: Không nên chờ đợi quá lâu trước khi commit. Commit thường xuyên giúp dễ dàng kiểm soát các
  thay đổi và quản lý lỗi.
- **Viết thông điệp commit rõ ràng**: Mỗi commit nên có một thông điệp rõ ràng để người khác dễ hiểu về những thay đổi
  mà bạn thực hiện.
- **Không commit các tệp nhạy cảm**: Đảm bảo rằng các tệp như mật khẩu hoặc các thông tin nhạy cảm không bị commit vào
  repository.
- **Thực hiện commit với phạm vi nhỏ**: Hãy commit các thay đổi nhỏ và có nghĩa thay vì những commit lớn, khó theo dõi.

## 7. **Tổng kết**

Commit trong Git là một phần quan trọng trong quy trình phát triển phần mềm, giúp theo dõi và lưu trữ các thay đổi của
mã nguồn. Thực hiện commit đúng cách giúp duy trì một lịch sử thay đổi rõ ràng, có thể quản lý và hợp tác hiệu quả trong
nhóm. Hy vọng tài liệu này đã giúp bạn hiểu rõ hơn về commit trong Git và GitHub!
