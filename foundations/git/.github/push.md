# Tài liệu về Push trong Git và Github

**Push** trong Git là quá trình đẩy các thay đổi từ kho lưu trữ cục bộ của bạn lên kho lưu trữ từ xa. Khi bạn thực hiện
các thay đổi trong bản sao cục bộ của mình và thực hiện commit, bạn cần sử dụng lệnh `git push` để chia sẻ những thay
đổi đó với người khác trong dự án hoặc sao lưu chúng vào kho lưu trữ từ xa.

#### Các bước cơ bản khi sử dụng lệnh **git push**:

1. **Lệnh Push cơ bản**:
   Để đẩy các thay đổi từ nhánh cục bộ của bạn lên nhánh từ xa tương ứng, bạn sử dụng lệnh `git push` theo cú pháp sau:

   ```bash
   git push <remote> <branch>
   ```

   Trong đó:

    - `<remote>` là tên của kho lưu trữ từ xa (thường là `origin`).
    - `<branch>` là tên nhánh bạn muốn đẩy thay đổi lên (thường là `main`, `master`, hoặc bất kỳ nhánh nào bạn đang làm
      việc).

   Ví dụ, để đẩy các thay đổi từ nhánh `main` lên kho lưu trữ từ xa `origin`:

   ```bash
   git push origin main
   ```

   Lệnh này sẽ đẩy các commit trong nhánh `main` từ bản sao cục bộ của bạn lên kho lưu trữ từ xa `origin`.

2. **Push một nhánh mới lên từ xa**:
   Nếu bạn tạo một nhánh mới trong kho lưu trữ cục bộ và muốn đẩy nhánh đó lên kho lưu trữ từ xa, bạn sử dụng lệnh sau:

   ```bash
   git push -u <remote> <branch>
   ```

   Tùy chọn `-u` sẽ thiết lập nhánh từ xa theo mặc định cho nhánh cục bộ của bạn, giúp Git nhớ rằng nhánh cục bộ này sẽ
   được đẩy lên nhánh từ xa đó trong các lần push sau.

   Ví dụ, để đẩy nhánh mới `feature-branch` lên từ xa:

   ```bash
   git push -u origin feature-branch
   ```

   Lệnh này sẽ đẩy nhánh `feature-branch` lên kho lưu trữ từ xa `origin` và thiết lập liên kết giữa nhánh cục bộ và
   nhánh từ xa.

3. **Push tất cả các nhánh**:
   Nếu bạn muốn đẩy tất cả các nhánh cục bộ của mình lên kho lưu trữ từ xa, bạn có thể sử dụng lệnh sau:

   ```bash
   git push --all <remote>
   ```

   Ví dụ:

   ```bash
   git push --all origin
   ```

   Điều này sẽ đẩy tất cả các nhánh cục bộ lên kho lưu trữ từ xa `origin`.

4. **Push chỉ các tag**:
   Git cũng hỗ trợ việc đẩy các tag (mốc đánh dấu) từ kho lưu trữ cục bộ lên kho lưu trữ từ xa. Để đẩy một tag cụ thể,
   bạn sử dụng lệnh:

   ```bash
   git push <remote> <tag-name>
   ```

   Ví dụ, để đẩy tag `v1.0` lên kho lưu trữ từ xa:

   ```bash
   git push origin v1.0
   ```

   Để đẩy tất cả các tag, bạn có thể sử dụng lệnh sau:

   ```bash
   git push --tags
   ```

---

### Các bước sau khi sử dụng lệnh **git push**

Sau khi thực hiện lệnh `git push`, bạn có thể làm các thao tác sau:

1. **Kiểm tra trạng thái của kho lưu trữ từ xa**:
   Để kiểm tra xem các thay đổi đã được đẩy lên kho lưu trữ từ xa hay chưa, bạn có thể sử dụng lệnh `git log` để kiểm
   tra lịch sử commit của nhánh từ xa.

   Để xem lịch sử commit của nhánh từ xa, bạn có thể sử dụng:

   ```bash
   git log origin/<branch>
   ```

   Ví dụ, để xem lịch sử commit của nhánh `main` từ kho lưu trữ từ xa `origin`:

   ```bash
   git log origin/main
   ```

2. **Kiểm tra kho lưu trữ từ xa**:
   Sau khi đẩy thay đổi, bạn có thể kiểm tra kho lưu trữ từ xa để đảm bảo rằng các thay đổi đã được đẩy lên thành công.
   Nếu bạn sử dụng GitHub hoặc GitLab, bạn có thể vào trang web của kho lưu trữ từ xa để xác nhận.

3. **Pull các thay đổi sau khi push**:
   Đôi khi, bạn có thể cần phải kéo các thay đổi mới nhất từ kho lưu trữ từ xa về sau khi đẩy các thay đổi của mình.
   Điều này giúp bạn giữ kho lưu trữ cục bộ của mình đồng bộ với kho lưu trữ từ xa.

   Để thực hiện việc này, bạn sử dụng lệnh `git pull`:

   ```bash
   git pull origin main
   ```

---

### Các tùy chọn khác khi sử dụng `git push`

- **Push với tùy chọn `--force`**:
  Tùy chọn `--force` (hoặc `-f`) có thể được sử dụng để buộc đẩy các thay đổi lên kho lưu trữ từ xa, ngay cả khi có sự
  không khớp giữa lịch sử commit của nhánh cục bộ và nhánh từ xa. Tuy nhiên, việc sử dụng `--force` cần được thận trọng
  vì nó có thể ghi đè lên các thay đổi từ người khác.

  ```bash
  git push --force origin main
  ```

  Lệnh này sẽ đẩy các thay đổi của bạn lên nhánh `main` từ xa, ghi đè lên bất kỳ thay đổi nào có thể đã có trên nhánh
  đó.

- **Push chỉ các tệp cụ thể**:
  Git không hỗ trợ đẩy các tệp riêng lẻ mà không thực hiện commit. Tuy nhiên, bạn có thể commit các tệp riêng biệt và
  sau đó đẩy các thay đổi của mình. Nếu chỉ muốn đẩy các tệp đã được commit, bạn có thể dùng các tùy chọn trong
  `git commit` để chọn tệp cần commit, sau đó sử dụng `git push` để đẩy.

---

### Một số lưu ý khi sử dụng `git push`

- **Tránh push quá nhiều thay đổi cùng lúc**:
  Trước khi thực hiện `git push`, hãy chắc chắn rằng bạn đã kiểm tra kỹ các thay đổi và commit của mình. Việc đẩy quá
  nhiều thay đổi không cần thiết hoặc sai sót có thể gây rối loạn kho lưu trữ.

- **Push đến nhánh đúng**:
  Hãy đảm bảo rằng bạn đang đẩy các thay đổi vào nhánh đúng. Nếu bạn đẩy vào nhánh sai, có thể gây ra xung đột hoặc mất
  mát dữ liệu.

- **Đẩy sau khi commit**:
  Để đẩy các thay đổi lên kho lưu trữ từ xa, bạn cần thực hiện commit trước đó. `git push` chỉ đẩy các thay đổi đã được
  commit, vì vậy đừng quên commit các thay đổi trước khi thực hiện push.

- **Lưu ý về việc sử dụng `--force`**:
  Tùy chọn `--force` có thể rất nguy hiểm nếu không được sử dụng đúng cách. Nó có thể làm mất các thay đổi của người
  khác, vì vậy chỉ sử dụng khi bạn chắc chắn rằng bạn muốn ghi đè lịch sử commit.

---

### Kết luận

Lệnh `git push` là công cụ quan trọng để chia sẻ và cập nhật kho lưu trữ từ xa với các thay đổi mà bạn thực hiện trong
kho lưu trữ cục bộ. Bạn có thể đẩy các nhánh, tag hoặc tất cả các nhánh của mình lên kho lưu trữ từ xa. Hãy sử dụng
`git push` cẩn thận và thường xuyên để giữ kho lưu trữ của bạn được cập nhật và đồng bộ với các cộng tác viên khác.
