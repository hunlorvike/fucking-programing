# Tài liệu về Clone trong Git và Github

**Clone** trong Git là quá trình sao chép một kho lưu trữ (repository) từ xa vào máy tính của bạn. Lệnh này giúp bạn tạo
một bản sao đầy đủ của kho lưu trữ, bao gồm tất cả các nhánh, commit, và lịch sử của kho lưu trữ đó. Sau khi clone, bạn
có thể làm việc với kho lưu trữ đó như là một bản sao riêng biệt.

#### Các bước cơ bản khi sử dụng lệnh **git clone**:

1. **Lệnh Clone cơ bản**:
   Để sao chép một kho lưu trữ từ xa về máy tính của bạn, bạn sử dụng lệnh `git clone` theo cú pháp sau:

   ```bash
   git clone <url của kho lưu trữ>
   ```

   Ví dụ, nếu bạn muốn clone kho lưu trữ từ GitHub:

   ```bash
   git clone https://github.com/username/repository.git
   ```

   Lệnh này sẽ tải về toàn bộ kho lưu trữ, bao gồm tất cả các nhánh và commit.

2. **Clone vào thư mục tùy chỉnh**:
   Nếu bạn muốn clone kho lưu trữ vào một thư mục cụ thể (không phải theo mặc định tên kho lưu trữ), bạn có thể chỉ định
   tên thư mục đích ngay sau URL của kho lưu trữ:

   ```bash
   git clone <url của kho lưu trữ> <tên thư mục>
   ```

   Ví dụ:

   ```bash
   git clone https://github.com/username/repository.git my-folder
   ```

   Điều này sẽ tạo thư mục `my-folder` và clone kho lưu trữ vào đó.

3. **Clone chỉ với một nhánh**:
   Nếu bạn chỉ muốn clone một nhánh duy nhất thay vì toàn bộ các nhánh của kho lưu trữ, bạn có thể sử dụng tùy chọn
   `--single-branch`:

   ```bash
   git clone --single-branch -b <tên nhánh> <url của kho lưu trữ>
   ```

   Ví dụ, để clone chỉ nhánh `develop`:

   ```bash
   git clone --single-branch -b develop https://github.com/username/repository.git
   ```

   Điều này giúp tiết kiệm băng thông và không tải toàn bộ các nhánh không cần thiết.

4. **Clone với tùy chọn `--depth` (clone sâu)**:
   Nếu bạn chỉ muốn clone một phần lịch sử commit (ví dụ, chỉ lấy một số commit gần đây nhất), bạn có thể sử dụng tùy
   chọn `--depth`:

   ```bash
   git clone --depth <số lượng commit> <url của kho lưu trữ>
   ```

   Ví dụ, để clone chỉ lấy 1 commit gần nhất:

   ```bash
   git clone --depth 1 https://github.com/username/repository.git
   ```

   Tùy chọn này hữu ích khi bạn chỉ cần phiên bản mới nhất mà không cần toàn bộ lịch sử commit.

---

### Các bước sau khi clone

Sau khi bạn đã clone kho lưu trữ, bạn có thể thực hiện các thao tác sau:

1. **Kiểm tra các nhánh có sẵn**:
   Kho lưu trữ đã clone về sẽ bao gồm tất cả các nhánh. Bạn có thể xem các nhánh có sẵn bằng cách sử dụng lệnh:

   ```bash
   git branch -a
   ```

   Điều này sẽ liệt kê tất cả các nhánh, cả nhánh cục bộ và nhánh từ xa.

2. **Chuyển nhánh**:
   Bạn có thể chuyển sang một nhánh khác bằng lệnh `git checkout`. Ví dụ, nếu bạn muốn chuyển sang nhánh `develop`:

   ```bash
   git checkout develop
   ```

3. **Pull các thay đổi mới từ kho lưu trữ từ xa**:
   Sau khi clone, nếu có các thay đổi mới được đẩy lên kho lưu trữ từ xa, bạn có thể cập nhật bản sao cục bộ của mình
   bằng lệnh `git pull`:

   ```bash
   git pull origin main
   ```

   Điều này sẽ tải các thay đổi mới từ nhánh `main` trong kho lưu trữ từ xa về.

---

### Các tùy chọn khác khi sử dụng `git clone`

- **Clone kho lưu trữ qua SSH**:
  Nếu bạn sử dụng SSH để kết nối với kho lưu trữ từ xa, bạn có thể clone kho lưu trữ bằng URL SSH thay vì HTTP. Ví dụ:

  ```bash
  git clone git@github.com:username/repository.git
  ```

  Đây là phương thức thường được sử dụng khi bạn đã cấu hình SSH keys với GitHub hoặc các dịch vụ Git từ xa khác.

- **Clone với các submodules**:
  Nếu kho lưu trữ có các submodules (kho lưu trữ con bên trong kho lưu trữ chính), bạn có thể sử dụng tùy chọn
  `--recursive` để clone cả các submodules:

  ```bash
  git clone --recursive <url của kho lưu trữ>
  ```

  Nếu bạn quên sử dụng `--recursive` khi clone, bạn có thể sử dụng lệnh sau để cập nhật các submodules sau đó:

  ```bash
  git submodule update --init --recursive
  ```

---

### Một số lưu ý khi sử dụng `git clone`

- **Kho lưu trữ từ xa và bản sao cục bộ**:
  Sau khi clone, bạn sẽ có một bản sao cục bộ của kho lưu trữ. Bản sao này là một kho lưu trữ đầy đủ với lịch sử commit,
  nhánh, và các tag, có thể hoạt động độc lập cho đến khi bạn thực hiện các thao tác push hoặc pull.

- **Lịch sử commit**:
  Kho lưu trữ được clone có đầy đủ lịch sử commit, vì vậy bạn có thể xem lại các phiên bản trước và điều tra bất kỳ thay
  đổi nào từ quá khứ.

- **Đẩy thay đổi lên kho lưu trữ từ xa**:
  Sau khi thực hiện các thay đổi và commit trong bản sao cục bộ, bạn có thể đẩy chúng lên kho lưu trữ từ xa sử dụng lệnh
  `git push`:

  ```bash
  git push origin <tên nhánh>
  ```

---

### Kết luận

Lệnh `git clone` là công cụ mạnh mẽ để sao chép kho lưu trữ từ xa về máy tính của bạn và bắt đầu làm việc với nó. Bạn có
thể tùy chỉnh lệnh clone với nhiều tùy chọn khác nhau để chỉ lấy một phần kho lưu trữ hoặc chỉ sao chép một nhánh duy
nhất. Sau khi clone, bạn có thể tiếp tục thực hiện các thay đổi, commit, và đẩy các thay đổi đó lên kho lưu trữ từ xa.
