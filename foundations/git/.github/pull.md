# Tài liệu về Pull trong Git và Github

**Pull** trong Git là quá trình tải về các thay đổi mới nhất từ kho lưu trữ từ xa và cập nhật bản sao cục bộ của bạn với
các thay đổi đó. Lệnh này kết hợp hai lệnh: `git fetch` (tải các thay đổi từ kho lưu trữ từ xa) và `git merge` (gộp các
thay đổi đó vào nhánh hiện tại của bạn). Sau khi sử dụng `git pull`, bạn sẽ có bản sao cục bộ của kho lưu trữ đồng bộ
với các thay đổi từ xa.

#### Các bước cơ bản khi sử dụng lệnh **git pull**:

1. **Lệnh Pull cơ bản**:
   Để tải về các thay đổi mới nhất từ kho lưu trữ từ xa và cập nhật nhánh hiện tại của bạn, bạn sử dụng lệnh `git pull`
   theo cú pháp sau:

   ```bash
   git pull <remote> <branch>
   ```

   Trong đó:
    - `<remote>` là tên của kho lưu trữ từ xa (thường là `origin`).
    - `<branch>` là tên nhánh bạn muốn kéo về (thường là `main` hoặc `master`).

   Ví dụ, để kéo các thay đổi mới nhất từ nhánh `main` trong kho lưu trữ từ xa `origin`:

   ```bash
   git pull origin main
   ```

   Lệnh này sẽ tải về các thay đổi mới từ nhánh `main` của kho lưu trữ từ xa `origin` và tự động gộp chúng vào nhánh
   hiện tại của bạn.

2. **Pull các thay đổi mà không gộp (Chỉ Fetch)**:
   Nếu bạn chỉ muốn tải về các thay đổi mà không gộp chúng vào nhánh hiện tại, bạn có thể sử dụng lệnh `git fetch`:

   ```bash
   git fetch <remote> <branch>
   ```

   Ví dụ, để chỉ tải về các thay đổi từ nhánh `main` mà không gộp:

   ```bash
   git fetch origin main
   ```

   Lệnh này sẽ tải về các thay đổi từ kho lưu trữ từ xa nhưng không thay đổi gì trong nhánh cục bộ của bạn cho đến khi
   bạn quyết định gộp chúng.

3. **Pull tất cả các nhánh**:
   Nếu bạn muốn kéo về các thay đổi cho tất cả các nhánh từ kho lưu trữ từ xa, bạn chỉ cần sử dụng lệnh `git pull` mà
   không chỉ định nhánh cụ thể:

   ```bash
   git pull
   ```

   Điều này sẽ kéo về tất cả các thay đổi từ nhánh mà bạn đang làm việc, từ kho lưu trữ từ xa mặc định (thường là
   `origin`).

4. **Pull và tự động giải quyết xung đột**:
   Trong trường hợp có xung đột khi gộp các thay đổi (ví dụ, bạn và người khác đều đã sửa cùng một tệp trong cùng một
   phần), Git sẽ yêu cầu bạn giải quyết xung đột thủ công. Sau khi giải quyết xung đột, bạn cần thực hiện commit để hoàn
   tất quá trình.

   Để giải quyết xung đột, Git sẽ đánh dấu các phần của tệp có sự khác biệt và yêu cầu bạn lựa chọn thay đổi phù hợp.
   Sau khi giải quyết xung đột, bạn có thể thực hiện commit và tiếp tục công việc.

---

### Các bước sau khi sử dụng lệnh **git pull**

Sau khi thực hiện lệnh `git pull`, bạn có thể làm các thao tác sau:

1. **Kiểm tra các thay đổi đã tải về**:
   Bạn có thể xem các thay đổi mới bằng lệnh `git log` để kiểm tra lịch sử commit của nhánh hiện tại và xác nhận các
   thay đổi đã được áp dụng:

   ```bash
   git log
   ```

2. **Kiểm tra trạng thái công việc**:
   Để kiểm tra trạng thái sau khi pull, bao gồm việc có xung đột hay không, bạn có thể sử dụng lệnh:

   ```bash
   git status
   ```

   Điều này sẽ giúp bạn biết liệu có tệp nào cần phải xử lý xung đột hoặc tệp nào chưa được commit.

3. **Push thay đổi sau khi giải quyết xung đột**:
   Nếu bạn đã giải quyết xung đột và thực hiện các thay đổi trong kho lưu trữ cục bộ, bạn có thể đẩy chúng lên kho lưu
   trữ từ xa bằng lệnh `git push`:

   ```bash
   git push origin <tên nhánh>
   ```

   Điều này sẽ cập nhật kho lưu trữ từ xa với các thay đổi mà bạn đã thực hiện.

---

### Các tùy chọn khác khi sử dụng `git pull`

- **Pull với tùy chọn `--rebase`**:
  Khi sử dụng tùy chọn `--rebase`, Git sẽ tái áp dụng các commit cục bộ của bạn lên các commit từ xa thay vì tạo một
  commit mới để gộp chúng. Điều này giúp giữ cho lịch sử commit của bạn gọn gàng hơn mà không tạo ra các commit gộp (
  merge commit).

  ```bash
  git pull --rebase origin main
  ```

  Việc này giúp bạn tránh được các merge commit không cần thiết và giữ lịch sử commit sạch sẽ hơn.

- **Pull vào một nhánh khác**:
  Bạn có thể kéo các thay đổi từ kho lưu trữ từ xa và gộp vào một nhánh khác bằng cách sử dụng lệnh `git pull` và chỉ
  định nhánh đích. Ví dụ:

  ```bash
  git pull origin main:my-feature-branch
  ```

  Điều này sẽ kéo các thay đổi từ nhánh `main` của kho lưu trữ từ xa và gộp chúng vào nhánh `my-feature-branch` cục bộ.

---

### Một số lưu ý khi sử dụng `git pull`

- **Lịch sử commit**:
  Lệnh `git pull` sẽ gộp các thay đổi từ xa vào nhánh cục bộ của bạn. Nếu bạn và người khác đã thực hiện thay đổi đối
  với cùng một tệp hoặc dòng mã, bạn sẽ gặp phải xung đột cần phải giải quyết thủ công.

- **Xung đột khi gộp**:
  Khi có sự thay đổi đồng thời ở cả hai phiên bản, Git sẽ không thể tự động gộp các thay đổi này và yêu cầu bạn giải
  quyết xung đột. Bạn cần mở tệp bị xung đột và lựa chọn thay đổi nào sẽ được giữ lại.

- **Cập nhật nhánh thường xuyên**:
  Để tránh các vấn đề với xung đột lớn, bạn nên sử dụng `git pull` thường xuyên để giữ cho kho lưu trữ của bạn luôn cập
  nhật với các thay đổi từ xa.

- **Không pull quá nhiều nhánh cùng lúc**:
  Nên tránh việc thực hiện pull cho nhiều nhánh cùng một lúc, vì mỗi nhánh có thể có các thay đổi khác nhau, và việc gộp
  chúng có thể gặp phải nhiều vấn đề phức tạp.

---

### Kết luận

Lệnh `git pull` là công cụ quan trọng để cập nhật kho lưu trữ cục bộ của bạn với các thay đổi mới nhất từ kho lưu trữ từ
xa. Bạn có thể tùy chỉnh lệnh pull với các tùy chọn khác nhau như `--rebase` để giữ lịch sử commit sạch sẽ hoặc giải
quyết xung đột khi có sự thay đổi đồng thời. Hãy sử dụng `git pull` thường xuyên để đảm bảo rằng bạn luôn làm việc với
phiên bản cập nhật của kho lưu trữ từ xa.