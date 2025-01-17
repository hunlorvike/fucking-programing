# Tài liệu về Cài Đặt và Cấu Hình Git

## 1. **Khái niệm về Git**

**Git** là hệ thống quản lý phiên bản phân tán, cho phép nhiều người dùng làm việc với các tệp tin mã nguồn mà không bị
xung đột. Git giúp theo dõi lịch sử thay đổi, khôi phục các phiên bản trước đó của dự án và hỗ trợ nhiều tính năng mạnh
mẽ để phát triển phần mềm hiệu quả.

## 2. **Cài Đặt Git**

### 2.1. **Cài Đặt trên Windows**

Để cài đặt Git trên Windows, bạn làm theo các bước sau:

1. Truy cập vào trang tải Git tại [https://git-scm.com](https://git-scm.com).
2. Tải phiên bản Git phù hợp với hệ điều hành của bạn (Windows).
3. Mở tệp cài đặt và làm theo các hướng dẫn trên màn hình.
4. Chọn các tùy chọn cài đặt mặc định (điều này sẽ bao gồm việc cài đặt Git Bash, một công cụ dòng lệnh giúp sử dụng Git
   dễ dàng hơn).

### 2.2. **Cài Đặt trên macOS**

Trên macOS, Git có thể được cài đặt dễ dàng thông qua Homebrew hoặc từ tệp cài đặt:

1. **Sử dụng Homebrew**:

    - Mở Terminal và chạy lệnh sau để cài đặt Homebrew (nếu chưa cài đặt):
      ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```
    - Sau đó, chạy lệnh sau để cài đặt Git:
      ```bash
      brew install git
      ```

2. **Cài Đặt thủ công**:
    - Truy cập [https://git-scm.com](https://git-scm.com) và tải tệp cài đặt cho macOS.
    - Mở tệp tải về và làm theo các hướng dẫn.

### 2.3. **Cài Đặt trên Linux**

Trên Linux, Git có thể được cài đặt qua các trình quản lý gói của từng bản phân phối:

- **Ubuntu/Debian**:

  ```bash
  sudo apt update
  sudo apt install git
  ```

- **CentOS/Fedora**:

  ```bash
  sudo yum install git
  ```

- **Arch Linux**:
  ```bash
  sudo pacman -S git
  ```

## 3. **Cấu Hình Git Ban Đầu**

Sau khi cài đặt Git thành công, bạn cần cấu hình Git để đảm bảo rằng các thông tin cá nhân của bạn được sử dụng trong
mỗi commit.

### 3.1. **Cấu Hình Tên Người Dùng và Email**

Git yêu cầu bạn khai báo tên và email của bạn để liên kết với các commit. Bạn có thể sử dụng lệnh sau để thiết lập:

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@example.com"
```

- Lệnh `--global` có nghĩa là các thiết lập này sẽ áp dụng cho tất cả các dự án Git trên máy tính của bạn. Nếu bạn muốn
  cấu hình cho một dự án cụ thể, bỏ `--global`.

### 3.2. **Cấu Hình Editor Mặc Định**

Git sử dụng editor để bạn có thể nhập thông điệp commit. Bạn có thể thay đổi editor mặc định bằng lệnh:

```bash
git config --global core.editor "vi"
```

Bạn có thể thay thế `"vi"` bằng bất kỳ editor nào bạn yêu thích, ví dụ `"nano"`, `"code"` (VSCode), `"subl"` (Sublime
Text).

### 3.3. **Kiểm Tra Cấu Hình**

Để kiểm tra các thiết lập cấu hình hiện tại của Git, bạn có thể sử dụng lệnh:

```bash
git config --list
```

Lệnh này sẽ hiển thị tất cả các thông tin cấu hình hiện tại, bao gồm tên người dùng, email và các thiết lập khác.

## 4. **Kiểm Tra và Cập Nhật Cấu Hình Git**

Nếu bạn muốn thay đổi một thiết lập đã cấu hình, bạn có thể sử dụng lại lệnh `git config`. Ví dụ:

- Để thay đổi tên người dùng:

  ```bash
  git config --global user.name "Tên mới"
  ```

- Để thay đổi email:

  ```bash
  git config --global user.email "emailmoi@example.com"
  ```

- Để thay đổi editor mặc định:
  ```bash
  git config --global core.editor "nano"
  ```

## 5. **Tổng kết**

Việc cài đặt và cấu hình Git đúng cách là bước đầu tiên để bạn có thể sử dụng Git hiệu quả trong việc quản lý mã nguồn.
Hãy chắc chắn rằng bạn đã cấu hình tên người dùng, email và editor mặc định để Git có thể sử dụng thông tin này trong
mọi commit và thao tác quản lý mã nguồn.
