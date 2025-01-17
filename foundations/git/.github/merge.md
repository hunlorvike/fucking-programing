# Tài liệu về Merge trong Git và  Github

**Merge** trong Git là một thao tác kết hợp hai nhánh (branches) lại với nhau. Thông thường, khi làm việc với Git, bạn
sẽ tạo ra các nhánh riêng biệt để phát triển các tính năng mới mà không ảnh hưởng đến mã nguồn chính (thường là nhánh
`main` hoặc `master`). Sau khi hoàn thành, bạn sẽ cần **merge** nhánh của mình vào nhánh chính để tích hợp các thay đổi.

#### Các bước cơ bản khi sử dụng merge trong Git:

1. **Kiểm tra nhánh hiện tại**:
   Đầu tiên, hãy chắc chắn rằng bạn đang ở nhánh mà bạn muốn thực hiện merge vào. Ví dụ, bạn muốn merge từ nhánh
   `feature` vào nhánh `main`.

   ```bash
   git checkout main
   ```

2. **Cập nhật nhánh chính**:
   Trước khi merge, hãy chắc chắn rằng nhánh chính của bạn đã được cập nhật với các thay đổi mới nhất từ kho lưu trữ từ
   xa.

   ```bash
   git pull origin main
   ```

3. **Merge nhánh**:
   Để merge một nhánh khác vào nhánh hiện tại, bạn sử dụng lệnh `git merge`. Giả sử bạn muốn merge nhánh `feature` vào
   nhánh `main`:

   ```bash
   git merge feature
   ```

4. **Giải quyết xung đột (conflict)**:
   Trong trường hợp Git không thể tự động kết hợp các thay đổi (do có sự thay đổi cùng một dòng mã trong cả hai nhánh),
   sẽ xảy ra xung đột. Git sẽ thông báo cho bạn và yêu cầu bạn giải quyết xung đột đó thủ công bằng cách chỉnh sửa các
   file bị xung đột. Sau khi giải quyết xung đột, bạn sẽ cần phải đánh dấu các file đó đã được sửa và commit lại:

   ```bash
   git add <file bị xung đột>
   git commit
   ```

5. **Hoàn thành merge**:
   Sau khi merge thành công, bạn có thể kiểm tra lại lịch sử commit với lệnh:

   ```bash
   git log
   ```

6. **Push các thay đổi lên kho lưu trữ từ xa**:
   Cuối cùng, sau khi merge thành công, bạn có thể đẩy các thay đổi lên kho lưu trữ từ xa (nếu cần).

   ```bash
   git push origin main
   ```

---

### Một số loại merge trong Git

- **Fast-forward merge**:
  Nếu nhánh chính không có thay đổi nào mới kể từ lần bạn tạo nhánh con, Git sẽ tự động thực hiện merge mà không tạo ra
  commit merge riêng biệt. Điều này được gọi là "fast-forward merge". Ví dụ, nếu bạn chỉ thay đổi nhánh `feature` mà
  không có bất kỳ thay đổi nào trên nhánh `main`, Git sẽ tự động di chuyển con trỏ `main` đến commit cuối cùng của nhánh
  `feature`.

- **Merge với commit riêng**:
  Khi nhánh chính có các thay đổi mới, Git sẽ tạo ra một commit mới để kết hợp nhánh `feature` vào nhánh chính. Đây là
  loại merge phổ biến và sẽ tạo ra một điểm merge trong lịch sử commit.

- **Rebase vs Merge**:
    - `git rebase` là một phương pháp thay thế để kết hợp các thay đổi. Rebase sẽ thay đổi lịch sử commit, trong khi
      merge tạo ra một commit mới giữ lại lịch sử của cả hai nhánh.
    - Merge giữ lại tất cả các commit riêng biệt của nhánh con, trong khi rebase sẽ "chỉnh sửa" các commit của nhánh con
      sao cho chúng trở thành một chuỗi liên tiếp, giúp lịch sử commit gọn gàng hơn.

---

### Các tùy chọn merge phổ biến

- **--no-ff**: Tùy chọn này buộc Git tạo một commit merge ngay cả khi có thể thực hiện merge theo kiểu fast-forward.

  ```bash
  git merge --no-ff feature
  ```

- **--squash**: Khi bạn không muốn giữ lại lịch sử commit của nhánh con mà chỉ muốn gộp tất cả các thay đổi thành một
  commit duy nhất, bạn có thể sử dụng `--squash`.

  ```bash
  git merge --squash feature
  ```

- **--abort**: Nếu merge gặp xung đột và bạn muốn hủy bỏ quá trình merge và quay lại trạng thái trước đó, bạn có thể sử
  dụng lệnh `--abort`.

  ```bash
  git merge --abort
  ```

---

### Lưu ý

- Trước khi thực hiện merge, bạn nên luôn kiểm tra sự khác biệt giữa các nhánh bằng cách sử dụng lệnh `git diff` để hiểu
  rõ các thay đổi.
- Việc giải quyết xung đột trong Git có thể là một quá trình phức tạp. Bạn cần chú ý kỹ khi chỉnh sửa các file bị xung
  đột để tránh mất dữ liệu quan trọng.
- Bạn có thể sử dụng công cụ hỗ trợ giải quyết xung đột, chẳng hạn như **Git Mergetool**, nếu muốn có một giao diện đồ
  họa để giải quyết xung đột.

---

### Kết luận

Việc sử dụng merge trong Git là một kỹ năng quan trọng trong quá trình phát triển phần mềm, đặc biệt là khi làm việc
nhóm. Việc hiểu rõ các loại merge, cách giải quyết xung đột và các tùy chọn merge có thể giúp bạn quản lý mã nguồn hiệu
quả hơn.
