# Quản Lý Commit trong Git

## Mục Lục

1. [Thực Hiện Commit](#1-thực-hiện-commit)

    - [Thêm Tệp Vào Khu Vực Chờ](#thêm-tệp-vào-khu-vực-chờ)
    - [Thực Hiện Commit](#thực-hiện-commit)
    - [Các Tùy Chọn của Lệnh `git commit`](#các-tùy-chọn-của-lệnh-git-commit)

2. [Lịch Sử Commit](#2-lịch-sử-commit)

    - [Xem Lịch Sử Commit](#xem-lịch-sử-commit)
    - [So Sánh Thay Đổi Giữa Các Commit](#so-sánh-thay-đổi-giữa-các-commit)
    - [Xem Chi Tiết Một Commit Cụ Thể](#xem-chi-tiết-một-commit-cụ-thể)

3. [Sửa Lỗi Commit](#3-sửa-lỗi-commit)

    - [Sửa Commit Cuối Cùng](#sửa-commit-cuối-cùng)
    - [Sửa Commit Trong Lịch Sử Với `git rebase`](#sửa-commit-trong-lịch-sử-với-git-rebase)

4. [Tóm Tắt](#4-tóm-tắt)

---

### 1. Thực Hiện Commit

#### Thêm Tệp Vào Khu Vực Chờ

Trước khi thực hiện commit, bạn cần thêm tệp vào khu vực chờ (staging area) bằng lệnh sau:

- Thêm một tệp cụ thể:

  ```bash
  git add <file>
  ```

- Thêm tất cả các tệp đã thay đổi:
  ```bash
  git add .
  ```

#### Thực Hiện Commit

Sau khi thêm tệp vào staging area, sử dụng lệnh sau để thực hiện commit:

- Commit với một thông điệp:

  ```bash
  git commit -m "Thông điệp commit"
  ```

- Commit với thông điệp được viết trong trình soạn thảo:
  ```bash
  git commit
  ```

#### Các Tùy Chọn của Lệnh `git commit`

- **Commit tất cả các thay đổi theo dõi** (bỏ qua bước `git add`):

  ```bash
  git commit -a -m "Commit tất cả các thay đổi"
  ```

- **Sửa commit cuối cùng** (nếu quên thêm tệp hoặc cần chỉnh sửa thông điệp):
  ```bash
  git commit --amend
  ```

---

### 2. Lịch Sử Commit

#### Xem Lịch Sử Commit

- Hiển thị danh sách commit đầy đủ:

  ```bash
  git log
  ```

- Hiển thị danh sách commit ngắn gọn (1 dòng mỗi commit):

  ```bash
  git log --oneline
  ```

- Hiển thị log với biểu đồ nhánh:
  ```bash
  git log --oneline --graph --all
  ```

#### So Sánh Thay Đổi Giữa Các Commit

- So sánh thay đổi trong tệp kể từ commit trước:

  ```bash
  git diff
  ```

- So sánh thay đổi của một tệp cụ thể:

  ```bash
  git diff <file>
  ```

- So sánh hai commit bất kỳ:
  ```bash
  git diff <commit1> <commit2>
  ```

#### Xem Chi Tiết Một Commit Cụ Thể

- Xem chi tiết commit cụ thể:

  ```bash
  git show <commit-hash>
  ```

- Xem commit gần nhất:
  ```bash
  git show
  ```

---

### 3. Sửa Lỗi Commit

#### Sửa Commit Cuối Cùng

Nếu commit cuối cùng có lỗi, bạn có thể sửa lại bằng lệnh:

1. Thêm tệp bị thiếu:

    ```bash
    git add <file>
    ```

2. Sửa commit:
    ```bash
    git commit --amend
    ```

> **Lưu ý:** Chỉ sửa commit cuối cùng nếu commit chưa được đẩy lên remote.

#### Sửa Commit Trong Lịch Sử Với `git rebase`

Để sửa nhiều commit trong lịch sử:

1. Mở giao diện chỉnh sửa:

    ```bash
    git rebase -i HEAD~<số lượng commit>
    ```

   Ví dụ: Sửa 3 commit gần nhất:

    ```bash
    git rebase -i HEAD~3
    ```

2. Trong giao diện, chọn:

    - `pick`: Giữ nguyên commit.
    - `edit`: Sửa commit.
    - `squash`: Gộp commit với commit trước đó.

3. Sau khi chỉnh sửa, tiếp tục rebase:
    ```bash
    git rebase --continue
    ```

---

### 4. Tóm Tắt

**Quản lý commit trong Git** là một phần quan trọng để duy trì lịch sử thay đổi rõ ràng và dễ hiểu trong dự án.

- **Thực Hiện Commit:** Dùng `git add` và `git commit` để lưu thay đổi.
- **Lịch Sử Commit:** Sử dụng `git log`, `git diff`, và `git show` để xem lịch sử commit và so sánh thay đổi.
- **Sửa Lỗi Commit:** Sử dụng `git commit --amend` hoặc `git rebase` để chỉnh sửa commit.

Hãy đảm bảo bạn hiểu rõ các lệnh này để quản lý mã nguồn hiệu quả hơn! 😊
