# Tài liệu về Switch trong Git và Github

**Switch** trong Git là một lệnh được sử dụng để chuyển đổi giữa các nhánh trong kho lưu trữ cục bộ của bạn. Thay vì sử dụng lệnh `git checkout` để chuyển nhánh (một lệnh có thể gây nhầm lẫn vì nó có nhiều tác dụng khác nhau), Git cung cấp lệnh `git switch` để đơn giản hóa quá trình này. Lệnh `git switch` giúp bạn chuyển giữa các nhánh một cách rõ ràng và trực quan hơn.

#### Các bước cơ bản khi sử dụng lệnh **git switch**:

1. **Lệnh Switch cơ bản**:
   Để chuyển sang một nhánh khác, bạn sử dụng lệnh `git switch` theo cú pháp sau:

   ```bash
   git switch <branch>
   ```

   Trong đó:

   - `<branch>` là tên nhánh mà bạn muốn chuyển đến.

   Ví dụ, để chuyển sang nhánh `develop`:

   ```bash
   git switch develop
   ```

   Lệnh này sẽ chuyển nhánh hiện tại của bạn sang nhánh `develop`. Nếu nhánh này chưa tồn tại, Git sẽ báo lỗi.

2. **Tạo nhánh mới và chuyển đến nhánh đó**:
   Nếu bạn muốn tạo một nhánh mới và chuyển sang nhánh đó ngay lập tức, bạn có thể sử dụng tùy chọn `-c` (create). Cú pháp như sau:

   ```bash
   git switch -c <new-branch>
   ```

   Ví dụ, để tạo nhánh `feature/login` và chuyển ngay sang nhánh đó:

   ```bash
   git switch -c feature/login
   ```

   Lệnh này sẽ tạo nhánh `feature/login` từ nhánh hiện tại và chuyển sang nhánh đó.

3. **Chuyển về nhánh trước đó**:
   Để chuyển lại nhánh trước đó mà bạn đã làm việc, bạn có thể sử dụng cú pháp sau:

   ```bash
   git switch -
   ```

   Lệnh này sẽ giúp bạn quay lại nhánh trước đó mà bạn vừa làm việc.

4. **Kiểm tra trạng thái của nhánh**:
   Trước khi thực hiện lệnh `git switch`, bạn có thể kiểm tra các nhánh có sẵn trong kho lưu trữ của mình bằng lệnh:

   ```bash
   git branch
   ```

   Lệnh này sẽ liệt kê tất cả các nhánh hiện tại của bạn và đánh dấu nhánh bạn đang làm việc trên.

---

### Các bước sau khi sử dụng lệnh **git switch**

Sau khi thực hiện lệnh `git switch`, bạn có thể làm các thao tác sau:

1. **Kiểm tra nhánh hiện tại**:
   Để kiểm tra nhánh hiện tại của bạn sau khi đã chuyển, sử dụng lệnh:

   ```bash
   git branch
   ```

   Điều này sẽ giúp bạn xác nhận rằng bạn đã chuyển sang nhánh mong muốn.

2. **Kiểm tra trạng thái công việc**:
   Để kiểm tra trạng thái của nhánh mới, bao gồm những thay đổi chưa commit, bạn có thể sử dụng lệnh:

   ```bash
   git status
   ```

   Điều này sẽ cho bạn biết nếu có thay đổi chưa được commit hoặc các tệp chưa được theo dõi trong nhánh hiện tại.

3. **Thực hiện thay đổi và commit**:
   Sau khi chuyển sang nhánh mới, bạn có thể tiếp tục thực hiện thay đổi trong dự án. Để commit các thay đổi, sử dụng các lệnh sau:

   ```bash
   git add <file>
   git commit -m "Thông điệp commit"
   ```

4. **Push thay đổi lên kho lưu trữ từ xa**:
   Nếu bạn muốn đẩy các thay đổi lên kho lưu trữ từ xa sau khi chuyển nhánh, sử dụng lệnh:

   ```bash
   git push origin <branch>
   ```

   Điều này sẽ cập nhật kho lưu trữ từ xa với nhánh và các thay đổi của bạn.

---

### Các tùy chọn khác khi sử dụng `git switch`

- **Chuyển nhánh với tùy chọn `--discard-changes`**:
  Khi bạn đang có thay đổi chưa commit và muốn bỏ qua những thay đổi đó khi chuyển sang nhánh khác, bạn có thể sử dụng tùy chọn `--discard-changes`. Lệnh này sẽ chuyển nhánh và hủy bỏ tất cả các thay đổi chưa commit.

  ```bash
  git switch --discard-changes <branch>
  ```

  Ví dụ, để chuyển sang nhánh `develop` và bỏ qua các thay đổi chưa commit:

  ```bash
  git switch --discard-changes develop
  ```

- **Chuyển nhánh khi có thay đổi chưa commit**:
  Nếu bạn có thay đổi chưa commit và muốn chuyển nhánh mà không bỏ qua những thay đổi đó, Git sẽ yêu cầu bạn commit hoặc stash các thay đổi trước khi chuyển nhánh. Để lưu tạm các thay đổi của mình, bạn có thể sử dụng lệnh `git stash` trước khi chuyển nhánh:

  ```bash
  git stash
  git switch <branch>
  ```

  Sau khi chuyển nhánh, bạn có thể áp dụng lại các thay đổi đã lưu bằng lệnh:

  ```bash
  git stash pop
  ```

---

### Một số lưu ý khi sử dụng `git switch`

- **Chuyển nhánh với thay đổi chưa commit**:
  Trước khi chuyển nhánh, hãy chắc chắn rằng bạn đã xử lý tất cả các thay đổi chưa commit. Nếu không, Git sẽ yêu cầu bạn commit, stash, hoặc bỏ qua các thay đổi đó trước khi chuyển nhánh.

- **Kiểm tra nhánh hiện tại**:
  Để tránh các sai sót khi chuyển nhánh, hãy luôn kiểm tra nhánh hiện tại trước khi thực hiện thao tác chuyển nhánh. Điều này sẽ giúp bạn tránh việc làm việc trên nhánh không mong muốn.

- **Sử dụng `git switch` thay cho `git checkout`**:
  Lệnh `git switch` đơn giản hóa quá trình chuyển nhánh, giúp bạn tránh nhầm lẫn với các chức năng khác của `git checkout`. Việc sử dụng `git switch` giúp code của bạn trở nên dễ hiểu và dễ bảo trì hơn.

- **Không quên commit hoặc stash thay đổi trước khi chuyển nhánh**:
  Nếu bạn có thay đổi chưa commit và chuyển nhánh mà không xử lý chúng, Git sẽ không cho phép bạn chuyển nhánh. Hãy nhớ commit hoặc lưu tạm thay đổi bằng `git stash`.

---

### Kết luận

Lệnh `git switch` là công cụ đơn giản và trực quan để chuyển đổi giữa các nhánh trong Git. Bằng cách sử dụng `git switch`, bạn có thể dễ dàng quản lý và điều hướng qua các nhánh của kho lưu trữ cục bộ, giúp việc làm việc trên nhiều tính năng trở nên mượt mà và hiệu quả hơn. Hãy sử dụng `git switch` thay cho `git checkout` khi muốn chuyển nhánh để tránh sự nhầm lẫn và làm việc hiệu quả hơn trong các dự án của bạn.
