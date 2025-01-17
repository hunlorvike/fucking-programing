# Quản Lý Nhánh (Branching) trong Git

## Mục Lục

1. [Tạo và Xóa Nhánh](#1-tạo-và-xóa-nhánh)

    - [Tạo Nhánh Mới](#tạo-nhánh-mới)
    - [Xóa Nhánh](#xóa-nhánh)

2. [Quản Lý Nhánh](#2-quản-lý-nhánh)

    - [Gộp Nhánh với `git merge`](#gộp-nhánh-với-git-merge)
    - [Rebase Nhánh với `git rebase`](#rebase-nhánh-với-git-rebase)
    - [Sự Khác Biệt giữa Merge và Rebase](#sự-khác-biệt-giữa-merge-và-rebase)

3. [Chiến Lược Branching](#3-chiến-lược-branching)

    - [Git Flow](#git-flow)
    - [GitHub Flow](#github-flow)

4. [Tóm Tắt](#4-tóm-tắt)

---

### 1. Tạo và Xóa Nhánh

#### Tạo Nhánh Mới

Để tạo một nhánh mới trong Git, sử dụng lệnh:

-   Tạo nhánh mới nhưng không chuyển sang nhánh đó:

    ```bash
    git branch <branch-name>
    ```

-   Tạo nhánh mới và chuyển ngay sang nhánh đó:
    ```bash
    git checkout -b <branch-name>
    ```

Ví dụ:

```bash
git checkout -b feature/new-feature
```

#### Xóa Nhánh

Để xóa nhánh không còn cần thiết, sử dụng lệnh:

-   Xóa một nhánh đã được merge vào nhánh khác:

    ```bash
    git branch -d <branch-name>
    ```

-   Xóa một nhánh chưa được merge (buộc xóa):
    ```bash
    git branch -D <branch-name>
    ```

Ví dụ:

```bash
git branch -D feature/old-feature
```

---

### 2. Quản Lý Nhánh

#### Gộp Nhánh với `git merge`

**Mục đích:** Kết hợp thay đổi từ nhánh khác vào nhánh hiện tại.

-   Gộp nhánh cụ thể vào nhánh hiện tại:
    ```bash
    git merge <branch-name>
    ```

Ví dụ:

```bash
git merge feature/new-feature
```

**Ưu điểm:**

-   Lịch sử commit đầy đủ, bao gồm cả merge commit.
-   Dễ dàng theo dõi nguồn gốc thay đổi.

#### Rebase Nhánh với `git rebase`

**Mục đích:** Di chuyển các commit của nhánh hiện tại lên đầu nhánh cơ sở (base branch).

-   Rebase nhánh hiện tại với nhánh khác:
    ```bash
    git rebase <branch-name>
    ```

Ví dụ:

```bash
git rebase main
```

**Ưu điểm:**

-   Lịch sử commit gọn gàng, không có merge commit.
-   Thích hợp cho việc làm việc cá nhân trên nhánh feature.

#### Sự Khác Biệt giữa Merge và Rebase

| **Merge**                  | **Rebase**                    |
| -------------------------- | ----------------------------- |
| Tạo một commit hợp nhất.   | Không tạo commit hợp nhất.    |
| Lịch sử chứa tất cả merge. | Lịch sử gọn gàng, tuyến tính. |
| Thích hợp cho team lớn.    | Thích hợp cho cá nhân.        |

---

### 3. Chiến Lược Branching

#### Git Flow

**Git Flow** là chiến lược branching phổ biến, phù hợp với các dự án lớn.

-   **Các nhánh chính:**

    -   `main`: Chứa phiên bản chính thức, đã được phát hành.
    -   `develop`: Chứa mã nguồn phát triển, sẽ được merge vào `main` sau khi hoàn thiện.

-   **Các nhánh phụ:**
    -   `feature`: Nhánh tính năng, được tạo từ `develop`.
    -   `release`: Nhánh chuẩn bị phát hành, được tạo từ `develop`.
    -   `hotfix`: Nhánh sửa lỗi khẩn cấp, được tạo từ `main`.

**Quy trình cơ bản:**

1. Tạo nhánh `feature` từ `develop`.
2. Phát triển tính năng, sau đó merge vào `develop`.
3. Tạo nhánh `release` khi chuẩn bị phát hành.
4. Merge `release` vào `main` khi phát hành xong.
5. Sửa lỗi trên `hotfix` và merge vào cả `main` và `develop`.

#### GitHub Flow

**GitHub Flow** là chiến lược đơn giản, phù hợp với dự án nhỏ hoặc triển khai liên tục (CI/CD).

-   Chỉ có một nhánh chính: `main`.
-   Các nhánh tính năng (`feature`) được tạo trực tiếp từ `main`.
-   Sau khi hoàn thành, nhánh tính năng được merge trở lại `main`.

**Quy trình cơ bản:**

1. Tạo nhánh `feature` từ `main`.
2. Phát triển và kiểm tra tính năng.
3. Gửi Pull Request và yêu cầu review.
4. Merge Pull Request vào `main`.

---

### 4. Tóm Tắt

**Quản lý nhánh (branching)** là một phần không thể thiếu để làm việc hiệu quả trong nhóm và duy trì lịch sử thay đổi của dự án.

-   **Tạo và Xóa Nhánh:** Sử dụng `git branch` để tạo hoặc xóa nhánh.
-   **Quản Lý Nhánh:** Sử dụng `git merge` hoặc `git rebase` để kết hợp thay đổi giữa các nhánh.
-   **Chiến Lược Branching:**
    -   **Git Flow:** Phù hợp với dự án lớn.
    -   **GitHub Flow:** Phù hợp với dự án nhỏ hoặc CI/CD.
