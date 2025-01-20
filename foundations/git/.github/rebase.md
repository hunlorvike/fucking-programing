# Tài liệu về Rebase trong Git và Github

**Rebase** trong Git là một thao tác để di chuyển hoặc hợp nhất các commit từ một nhánh này sang một nhánh khác. So với
**merge**, rebase có mục tiêu làm cho lịch sử commit gọn gàng hơn bằng cách "phát lại" các commit của nhánh này lên
nhánh khác. Đây là công cụ mạnh mẽ giúp bạn tổ chức lịch sử commit của dự án một cách logic và dễ hiểu.

---

## Các bước cơ bản khi sử dụng Rebase trong Git:

1. **Chuyển sang nhánh cần rebase**:
   Trước tiên, hãy đảm bảo rằng bạn đang ở nhánh mà bạn muốn rebase. Ví dụ, bạn muốn rebase nhánh `feature` theo nhánh
   `main`.

    ```bash
    git checkout feature
    ```

2. **Thực hiện rebase**:
   Dùng lệnh `git rebase` để phát lại các commit từ nhánh `feature` lên nhánh `main`.

    ```bash
    git rebase main
    ```

    - Lệnh trên sẽ lấy các commit của nhánh `feature` và "phát lại" chúng lên trên các commit mới nhất của nhánh `main`.

3. **Giải quyết xung đột (nếu có)**:
   Trong trường hợp có xung đột xảy ra trong quá trình rebase, Git sẽ dừng lại và yêu cầu bạn giải quyết từng xung đột
   một. Bạn cần chỉnh sửa file bị xung đột, sau đó đánh dấu rằng xung đột đã được giải quyết bằng cách thêm file vào
   index:

    ```bash
    git add <file bị xung đột>
    ```

   Sau đó, tiếp tục quá trình rebase:

    ```bash
    git rebase --continue
    ```

   Nếu muốn hủy bỏ toàn bộ quá trình rebase và quay lại trạng thái ban đầu, bạn có thể sử dụng:

    ```bash
    git rebase --abort
    ```

4. **Cập nhật nhánh từ xa (nếu cần)**:
   Sau khi hoàn thành rebase, bạn cần đẩy các thay đổi lên kho lưu trữ từ xa. Tuy nhiên, vì rebase thay đổi lịch sử
   commit, bạn sẽ cần sử dụng tùy chọn `--force` hoặc `--force-with-lease` để cập nhật nhánh từ xa.

    ```bash
    git push origin feature --force-with-lease
    ```

---

## Rebase tương tác (Interactive Rebase)

Rebase tương tác là một tính năng mạnh mẽ trong Git, cho phép bạn chỉnh sửa, gộp, xóa, hoặc thay đổi thứ tự của các
commit. Điều này hữu ích khi bạn muốn làm gọn lịch sử commit hoặc sửa đổi các commit trước khi đưa chúng lên kho lưu
trữ.

### Cách thực hiện rebase tương tác:

1. Dùng lệnh `git rebase -i` kèm theo commit bạn muốn bắt đầu chỉnh sửa. Ví dụ, để chỉnh sửa các commit trong nhánh
   `feature` từ 3 commit trước:

    ```bash
    git rebase -i HEAD~3
    ```

2. Git sẽ mở trình soạn thảo mặc định, hiển thị danh sách các commit trong phạm vi đã chọn. Bạn sẽ thấy các từ khóa như
   `pick`, `edit`, `squash`, hoặc `reword`:

    ```plaintext
    pick abc123 Commit message 1
    pick def456 Commit message 2
    pick ghi789 Commit message 3
    ```

3. Thay đổi các từ khóa này để thực hiện các hành động mong muốn:

    - **pick**: Giữ nguyên commit.
    - **reword**: Chỉnh sửa thông điệp commit.
    - **edit**: Tạm dừng tại commit này để bạn chỉnh sửa nội dung.
    - **squash**: Gộp commit này với commit trước đó.
    - **drop**: Xóa commit này.

4. Lưu file và thoát khỏi trình soạn thảo. Git sẽ thực hiện rebase theo các thay đổi bạn chỉ định.

---

## Một số loại Rebase trong Git

- **Upstream Rebase**:
  Rebase nhánh của bạn dựa trên nhánh chính (ví dụ: `main`) để luôn giữ cho nhánh của bạn đồng bộ với những thay đổi mới
  nhất.

  ```bash
  git rebase main
  ```

- **Interactive Rebase**:
  Cho phép bạn chỉnh sửa lịch sử commit như đã trình bày ở phần trên.

- **Autosquash Rebase**:
  Sử dụng tùy chọn `--autosquash` khi rebase để tự động gộp các commit có liên quan (thường dùng với lệnh `--fixup`
  trước đó).

  ```bash
  git rebase -i --autosquash main
  ```

---

## So sánh Rebase và Merge

| **Đặc điểm**           | **Rebase**                                               | **Merge**                                                 |
|------------------------|----------------------------------------------------------|-----------------------------------------------------------|
| **Lịch sử commit**     | Lịch sử commit gọn gàng, không có commit merge.          | Lịch sử hiển thị tất cả các commit, bao gồm commit merge. |
| **Xung đột**           | Yêu cầu giải quyết xung đột tại mỗi commit.              | Giải quyết xung đột trong một lần tại commit merge.       |
| **Cách làm việc nhóm** | Dễ gây rối khi nhiều người làm việc trên cùng một nhánh. | Dễ sử dụng trong làm việc nhóm.                           |
| **Thay đổi lịch sử**   | Có (thay đổi SHA-1 của commit).                          | Không (giữ nguyên lịch sử commit).                        |

---

## Lưu ý khi sử dụng Rebase

1. **Không nên rebase các nhánh đã được chia sẻ với người khác**:
   Vì rebase thay đổi lịch sử commit, nó có thể gây rối cho những người khác đang làm việc trên cùng nhánh.

2. **Rebase để giữ lịch sử sạch sẽ**:
   Khi làm việc trên nhánh cá nhân, hãy sử dụng rebase để sắp xếp lại lịch sử commit trước khi merge vào nhánh chính.

3. **Luôn kiểm tra xung đột**:
   Quá trình rebase dễ xảy ra xung đột, đặc biệt khi làm việc trên các nhánh có nhiều thay đổi.

---

## Kết luận

Rebase là một công cụ mạnh mẽ trong Git để tổ chức lịch sử commit. Khi được sử dụng đúng cách, nó giúp lịch sử dự án trở
nên rõ ràng và dễ theo dõi hơn. Tuy nhiên, bạn cần cẩn trọng khi sử dụng rebase, đặc biệt trong các dự án làm việc nhóm,
để tránh gây ra các vấn đề không mong muốn.
