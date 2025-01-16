# TÀI LIỆU THIẾT KẾ DATABASE HỆ THỐNG QUẢN LÝ NỘI DUNG (CMS)

## **1. Tổng Quan**

Thiết kế cơ sở dữ liệu cho hệ thống CMS cần đảm bảo: 
- **Tính mở rộng**: Hỗ trợ thêm các tính năng mới trong tương lai mà không thay đổi cấu trúc cơ bản.
- **Hiệu năng cao**: Tối ưu hóa cho các truy vấn thường xuyên như tìm kiếm, phân trang, và sắp xếp.
- **Tính toàn vẹn dữ liệu**: Ràng buộc rõ ràng, tránh dữ liệu lỗi.
- **Quản lý phân quyền**: Hỗ trợ RBAC/ABAC cho các vai trò và quyền hạn.

Hệ thống sử dụng **Relational Database Management System (RDBMS)** (như MySQL, PostgreSQL), hoặc cơ chế kết hợp **NoSQL** cho các tính năng đặc biệt như tìm kiếm toàn văn.

---

## **2. Thiết Kế Sơ Đồ ERD (Entity-Relationship Diagram)**

### **Các Thực Thể Chính**

1. **Users**: Quản lý thông tin người dùng.
2. **Roles**: Vai trò trong hệ thống.
3. **Permissions**: Quyền hạn tương ứng với vai trò hoặc người dùng.
4. **Articles**: Bài viết do người dùng tạo ra.
5. **Categories**: Danh mục chứa bài viết.
6. **Tags**: Gắn thẻ cho bài viết để phân loại.
7. **Comments**: Quản lý bình luận.
8. **Media**: Quản lý file đính kèm hoặc hình ảnh.
9. **Settings**: Quản lý cấu hình hệ thống.
10. **Webhooks**: Đăng ký và lưu trữ sự kiện.

---

## **3. Cấu Trúc Bảng**

### **3.1. Bảng `users`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `username`     | VARCHAR(50)       | Tên đăng nhập (unique)                  |
| `email`        | VARCHAR(100)      | Email (unique)                          |
| `password`     | VARCHAR(255)      | Mã hóa mật khẩu                         |
| `first_name`   | VARCHAR(50)       | Tên                                     |
| `last_name`    | VARCHAR(50)       | Họ                                      |
| `role_id`      | INT (FK -> roles.id) | Vai trò của người dùng                  |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |
| `updated_at`   | TIMESTAMP         | Ngày cập nhật                           |

---

### **3.2. Bảng `roles`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `name`         | VARCHAR(50)       | Tên vai trò (unique)                    |
| `description`  | TEXT              | Mô tả vai trò                           |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |
| `updated_at`   | TIMESTAMP         | Ngày cập nhật                           |

---

### **3.3. Bảng `permissions`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `name`         | VARCHAR(50)       | Tên quyền hạn (unique)                  |
| `description`  | TEXT              | Mô tả quyền hạn                         |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |
| `updated_at`   | TIMESTAMP         | Ngày cập nhật                           |

---

### **3.4. Bảng `role_permissions`** *(Quan hệ N-N giữa roles và permissions)*

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `role_id`      | INT (FK -> roles.id) | Vai trò                                |
| `permission_id`| INT (FK -> permissions.id) | Quyền hạn                            |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |

---

### **3.5. Bảng `articles`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `title`        | VARCHAR(255)      | Tiêu đề bài viết                        |
| `content`      | TEXT              | Nội dung bài viết                       |
| `author_id`    | INT (FK -> users.id) | Tác giả                                |
| `category_id`  | INT (FK -> categories.id) | Danh mục của bài viết                |
| `status`       | ENUM('draft', 'pending', 'published') | Trạng thái bài viết          |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |
| `updated_at`   | TIMESTAMP         | Ngày cập nhật                           |

---

### **3.6. Bảng `categories`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `name`         | VARCHAR(100)      | Tên danh mục                            |
| `description`  | TEXT              | Mô tả danh mục                          |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |
| `updated_at`   | TIMESTAMP         | Ngày cập nhật                           |

---

### **3.7. Bảng `tags`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `name`         | VARCHAR(50)       | Tên thẻ (unique)                        |

---

### **3.8. Bảng `article_tags`** *(Quan hệ N-N giữa articles và tags)*

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `article_id`   | INT (FK -> articles.id) | Bài viết                               |
| `tag_id`       | INT (FK -> tags.id) | Thẻ                                     |

---

### **3.9. Bảng `comments`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `content`      | TEXT              | Nội dung bình luận                      |
| `author_id`    | INT (FK -> users.id) | Người bình luận                        |
| `article_id`   | INT (FK -> articles.id) | Bài viết liên quan                     |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |

---

### **3.10. Bảng `media`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `file_name`    | VARCHAR(255)      | Tên file                                |
| `file_path`    | TEXT              | Đường dẫn file                          |
| `file_type`    | VARCHAR(50)       | Loại file (image, video, document,...)  |
| `uploaded_by`  | INT (FK -> users.id) | Người tải lên                          |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |

---

### **3.11. Bảng `settings`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `key`          | VARCHAR(100)      | Tên khóa cấu hình (unique)              |
| `value`        | TEXT              | Giá trị cấu hình                        |

---

### **3.12. Bảng `webhooks`**

| Tên Cột        | Kiểu Dữ Liệu      | Ghi Chú                                  |
|-----------------|-------------------|------------------------------------------|
| `id`           | INT (PK, AUTO_INCREMENT) | Khóa chính                             |
| `url`          | TEXT              | URL webhook                             |
| `events`       | JSON              | Danh sách sự kiện hỗ trợ                |
| `created_at`   | TIMESTAMP         | Ngày tạo                                |

---

## **4. Tối Ưu Hóa**

1. **Indexing**:
   - Tạo index trên các cột thường xuyên được tìm kiếm: `articles.title`, `categories.name`, `tags.name`.
   - Sử dụng **Composite Index** trên các cột hay dùng cùng nhau, ví dụ: `articles.status`, `articles.category_id`.

2. **Foreign Key Constraints**:
   - Đảm bảo ràng buộc dữ liệu giữa các bảng: `users`, `articles`, `categories`.

3. **Partitioning**:
   - Sử dụng partition table cho bảng lớn như `articles`, `comments`.

4. **Caching**:
   - Tích hợp **Redis** hoặc **Memcached** để giảm tải truy vấn cơ sở dữ liệu.

5. **Backup & Recovery**:
   - Lên lịch backup hàng ngày và cơ chế phục hồi dữ liệu nhanh chóng.

---

**Kết luận**: Với thiết kế trên, hệ thống CMS sẽ đáp ứng được các yêu cầu quản lý nội dung, đảm bảo tính bảo mật, toàn vẹn dữ liệu và hiệu suất cao. Tiếp tục cải tiến dựa trên phản hồi và nhu cầu thực tế.