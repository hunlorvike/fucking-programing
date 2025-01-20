## **🔥 TÀI LIỆU THIẾT KẾ DATABASE CHO CMS: DÀNH CHO DÂN CODE 🔥**

Yo các bạn sinh viên IT! Hôm nay mình sẽ cùng các bạn "mổ xẻ" cách thiết kế database cho một hệ thống quản lý nội dung (
CMS). Đây là một phần cực kỳ quan trọng, giúp ứng dụng của bạn chạy mượt mà, dữ liệu được tổ chức gọn gàng. Mình sẽ cố
gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé!

### **1. TỔNG QUAN: DATABASE CHO CMS LÀ GÌ?**

* **CMS (Content Management System):** Hệ thống quản lý nội dung (bài viết, hình ảnh, video, ...). Ví dụ: WordPress,
  Joomla.
* **Database:** Nơi lưu trữ tất cả dữ liệu của CMS (như cái "kho" của CMS).
* **Mục tiêu:**
    * **Mở rộng dễ dàng:** Thêm tính năng mới không làm "rối tung" cấu trúc cũ.
    * **Hiệu năng cao:** Truy vấn nhanh, không bị "delay".
    * **Toàn vẹn dữ liệu:** Dữ liệu "sạch", không bị lỗi.
    * **Quản lý quyền hạn:** Phân quyền rõ ràng (ai được làm gì).

### **2. ERD (ENTITY-RELATIONSHIP DIAGRAM) - SƠ ĐỒ QUAN HỆ THỰC THỂ**

* **Thực thể (Entities):** Các đối tượng chính của hệ thống:
    1. `Users` (người dùng).
    2. `Roles` (vai trò).
    3. `Permissions` (quyền hạn).
    4. `Articles` (bài viết).
    5. `Categories` (danh mục).
    6. `Tags` (thẻ).
    7. `Comments` (bình luận).
    8. `Media` (file đính kèm).
    9. `Settings` (cài đặt).
    10. `Webhooks` (thông báo sự kiện).

### **3. CẤU TRÚC BẢNG (NHỮNG CHIẾC "TỦ" CHỨA DỮ LIỆU)**

Mình sẽ đi chi tiết từng bảng để các bạn dễ hình dung nhé:

#### **3.1. BẢNG `users` (NGƯỜI DÙNG)**

| Cột          | Kiểu Dữ Liệu   | Ghi Chú                              |
|--------------|----------------|--------------------------------------|
| `id`         | `INT` (PK, AI) | Khóa chính, tự tăng.                 |
| `username`   | `VARCHAR(50)`  | Tên đăng nhập (duy nhất).            |
| `email`      | `VARCHAR(100)` | Email (duy nhất).                    |
| `password`   | `VARCHAR(255)` | Mật khẩu (đã mã hóa).                |
| `first_name` | `VARCHAR(50)`  | Tên.                                 |
| `last_name`  | `VARCHAR(50)`  | Họ.                                  |
| `role_id`    | `INT` (FK)     | Vai trò (tham chiếu đến `roles.id`). |
| `created_at` | `TIMESTAMP`    | Ngày tạo.                            |
| `updated_at` | `TIMESTAMP`    | Ngày cập nhật.                       |

* **Mẹo:** Nên mã hóa password để tăng tính bảo mật (dùng Bcrypt, SHA-256).

#### **3.2. BẢNG `roles` (VAI TRÒ)**

| Cột           | Kiểu Dữ Liệu   | Ghi Chú                 |
|---------------|----------------|-------------------------|
| `id`          | `INT` (PK, AI) | Khóa chính, tự tăng.    |
| `name`        | `VARCHAR(50)`  | Tên vai trò (duy nhất). |
| `description` | `TEXT`         | Mô tả vai trò.          |
| `created_at`  | `TIMESTAMP`    | Ngày tạo.               |
| `updated_at`  | `TIMESTAMP`    | Ngày cập nhật.          |

#### **3.3. BẢNG `permissions` (QUYỀN HẠN)**

| Cột           | Kiểu Dữ Liệu   | Ghi Chú               |
|---------------|----------------|-----------------------|
| `id`          | `INT` (PK, AI) | Khóa chính, tự tăng.  |
| `name`        | `VARCHAR(50)`  | Tên quyền (duy nhất). |
| `description` | `TEXT`         | Mô tả quyền.          |
| `created_at`  | `TIMESTAMP`    | Ngày tạo.             |
| `updated_at`  | `TIMESTAMP`    | Ngày cập nhật.        |

#### **3.4. BẢNG `role_permissions` (QUAN HỆ N-N GIỮA VAI TRÒ VÀ QUYỀN HẠN)**

| Cột             | Kiểu Dữ Liệu | Ghi Chú                                      |
|-----------------|--------------|----------------------------------------------|
| `role_id`       | `INT` (FK)   | Vai trò (tham chiếu đến `roles.id`).         |
| `permission_id` | `INT` (FK)   | Quyền hạn (tham chiếu đến `permissions.id`). |
| `created_at`    | `TIMESTAMP`  | Ngày tạo.                                    |

* **Mẹo:** Bảng này dùng để quản lý mối quan hệ nhiều-nhiều giữa `roles` và `permissions`.

#### **3.5. BẢNG `articles` (BÀI VIẾT)**

| Cột           | Kiểu Dữ Liệu                            | Ghi Chú                                    |
|---------------|-----------------------------------------|--------------------------------------------|
| `id`          | `INT` (PK, AI)                          | Khóa chính, tự tăng.                       |
| `title`       | `VARCHAR(255)`                          | Tiêu đề bài viết.                          |
| `content`     | `TEXT`                                  | Nội dung bài viết.                         |
| `author_id`   | `INT` (FK)                              | Tác giả (tham chiếu đến `users.id`).       |
| `category_id` | `INT` (FK)                              | Danh mục (tham chiếu đến `categories.id`). |
| `status`      | `ENUM('draft', 'pending', 'published')` | Trạng thái bài viết.                       |
| `created_at`  | `TIMESTAMP`                             | Ngày tạo.                                  |
| `updated_at`  | `TIMESTAMP`                             | Ngày cập nhật.                             |

* **Mẹo:** Nên dùng `ENUM` cho các cột có giá trị cố định (như `status`).

#### **3.6. BẢNG `categories` (DANH MỤC)**

| Cột           | Kiểu Dữ Liệu   | Ghi Chú              |
|---------------|----------------|----------------------|
| `id`          | `INT` (PK, AI) | Khóa chính, tự tăng. |
| `name`        | `VARCHAR(100)` | Tên danh mục.        |
| `description` | `TEXT`         | Mô tả danh mục.      |
| `created_at`  | `TIMESTAMP`    | Ngày tạo.            |
| `updated_at`  | `TIMESTAMP`    | Ngày cập nhật.       |

#### **3.7. BẢNG `tags` (THẺ)**

| Cột    | Kiểu Dữ Liệu   | Ghi Chú              |
|--------|----------------|----------------------|
| `id`   | `INT` (PK, AI) | Khóa chính, tự tăng. |
| `name` | `VARCHAR(50)`  | Tên thẻ (duy nhất).  |

#### **3.8. BẢNG `article_tags` (QUAN HỆ N-N GIỮA BÀI VIẾT VÀ THẺ)**

| Cột          | Kiểu Dữ Liệu | Ghi Chú                                  |
|--------------|--------------|------------------------------------------|
| `article_id` | `INT` (FK)   | Bài viết (tham chiếu đến `articles.id`). |
| `tag_id`     | `INT` (FK)   | Thẻ (tham chiếu đến `tags.id`).          |

#### **3.9. BẢNG `comments` (BÌNH LUẬN)**

| Cột          | Kiểu Dữ Liệu   | Ghi Chú                                      |
|--------------|----------------|----------------------------------------------|
| `id`         | `INT` (PK, AI) | Khóa chính, tự tăng.                         |
| `content`    | `TEXT`         | Nội dung bình luận.                          |
| `author_id`  | `INT` (FK)     | Người bình luận (tham chiếu đến `users.id`). |
| `article_id` | `INT` (FK)     | Bài viết (tham chiếu đến `articles.id`).     |
| `created_at` | `TIMESTAMP`    | Ngày tạo.                                    |

#### **3.10. BẢNG `media` (FILE ĐÍNH KÈM)**

| Cột           | Kiểu Dữ Liệu   | Ghi Chú                                   |
|---------------|----------------|-------------------------------------------|
| `id`          | `INT` (PK, AI) | Khóa chính, tự tăng.                      |
| `file_name`   | `VARCHAR(255)` | Tên file.                                 |
| `file_path`   | `TEXT`         | Đường dẫn file.                           |
| `file_type`   | `VARCHAR(50)`  | Loại file (image, video, ...).            |
| `uploaded_by` | `INT` (FK)     | Người upload (tham chiếu đến `users.id`). |
| `created_at`  | `TIMESTAMP`    | Ngày tạo.                                 |

#### **3.11. BẢNG `settings` (CÀI ĐẶT)**

| Cột     | Kiểu Dữ Liệu   | Ghi Chú                  |
|---------|----------------|--------------------------|
| `id`    | `INT` (PK, AI) | Khóa chính, tự tăng.     |
| `key`   | `VARCHAR(100)` | Tên cấu hình (duy nhất). |
| `value` | `TEXT`         | Giá trị cấu hình.        |

#### **3.12. BẢNG `webhooks` (THÔNG BÁO SỰ KIỆN)**

| Cột          | Kiểu Dữ Liệu   | Ghi Chú                   |
|--------------|----------------|---------------------------|
| `id`         | `INT` (PK, AI) | Khóa chính, tự tăng.      |
| `url`        | `TEXT`         | URL webhook.              |
| `events`     | `JSON`         | Danh sách sự kiện (JSON). |
| `created_at` | `TIMESTAMP`    | Ngày tạo.                 |

* **Mẹo:** `JSON` type giúp lưu nhiều sự kiện trong một cột.

### **4. TỐI ƯU HÓA DATABASE (CHO NHANH HƠN)**

1. **Indexing (Tạo index):**
    * Tạo index trên các cột thường xuyên dùng để tìm kiếm (ví dụ: `articles.title`, `categories.name`, `tags.name`).
    * Dùng **composite index** cho các cột dùng chung (`articles.status`, `articles.category_id`).
2. **Foreign Key Constraints:** Đảm bảo dữ liệu giữa các bảng luôn nhất quán.
3. **Partitioning (Chia nhỏ bảng):** Dùng cho các bảng lớn như `articles`, `comments` để tăng hiệu suất.
4. **Caching (Dùng bộ nhớ đệm):** Dùng Redis hoặc Memcached để giảm tải cho database.
5. **Backup & Recovery (Sao lưu và phục hồi):** Lên lịch backup thường xuyên, có phương án phục hồi nhanh.

### **KẾT LUẬN**

Thiết kế database cho CMS có thể hơi phức tạp, nhưng nếu nắm vững các nguyên tắc cơ bản và áp dụng đúng cách, bạn hoàn
toàn có thể tạo ra một database mạnh mẽ, dễ quản lý và mở rộng. Hãy nhớ rằng, việc thiết kế database không chỉ là kiến
thức lý thuyết, mà còn là quá trình thực hành và tích lũy kinh nghiệm. Chúc các bạn thành công! 💪
