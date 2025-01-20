## **🔥 TÀI LIỆU SIÊU CẤP THIẾT KẾ API CHO HỆ THỐNG CMS (DÀNH CHO DÂN CODE)** 🔥

Hello các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "mổ xẻ" cách thiết kế API cho một hệ thống quản lý nội dung (
CMS). Nghe có vẻ "khoai" nhưng thực ra rất thú vị và hữu ích đấy. Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm
theo ví dụ trực quan để các bạn dễ "nuốt" nhé. Let's go!

### **1. TỔNG QUAN: TẠI SAO CẦN API CHO CMS?**

* **CMS (Content Management System):** Là hệ thống giúp bạn quản lý nội dung (bài viết, hình ảnh, video) trên website.
  Ví dụ: WordPress, Joomla, Drupal.
* **API:** Là "cầu nối" giúp các ứng dụng "nói chuyện" với CMS. Thay vì làm mọi thứ trên giao diện web, bạn có thể dùng
  API để tự động hóa các tác vụ.
* **Ví dụ:**
    * Ứng dụng mobile lấy danh sách bài viết từ CMS.
    * Ứng dụng khác tự động đăng bài lên CMS.
    * Ứng dụng phân tích dữ liệu lấy thông tin người dùng từ CMS.

**Mục tiêu của API:**

* **Dễ dùng:** Ai cũng có thể tích hợp, không cần phải là chuyên gia CMS.
* **Mạnh mẽ:** Làm được mọi thứ bạn cần trên CMS.
* **An toàn:** Bảo vệ dữ liệu của bạn.
* **Linh hoạt:** Dễ dàng thay đổi, nâng cấp.

### **2. CẤU TRÚC URL (ĐỊA CHỈ CỦA API)**

* **Base URL:** `https://api.ourcms.com/api/v1` (giống như "địa chỉ nhà" của API).
* **Tài nguyên (Resources):** Các "đối tượng" mà API quản lý:
    * `/articles`: Quản lý bài viết.
    * `/categories`: Quản lý danh mục.
    * `/users`: Quản lý người dùng.
    * `/permissions`: Quản lý quyền.
    * `/media`: Quản lý file media (hình ảnh, video).
    * `/comments`: Quản lý bình luận.
    * `/settings`: Cài đặt hệ thống.
    * `/webhooks`: Thông báo sự kiện.

### **3. XÁC THỰC VÀ ỦY QUYỀN (BẢO VỆ DỮ LIỆU!)**

* **Xác thực (Authentication):** Xác định xem ai đang dùng API.
    * **JWT (JSON Web Token):** Giống như "vé vào cửa".
        * Token được gửi qua header: `Authorization: Bearer <token>`.
        * Hoặc cookie `access_token`.
        * Dùng refresh token để lấy token mới.
    * **API Key:** Cho các ứng dụng không cần xác thực người dùng (ví dụ: lấy dữ liệu công khai).
        * Gửi qua header: `X-API-Key: <api_key>`.
    * **HTTPS:** Mọi kết nối đều phải dùng HTTPS (mã hóa dữ liệu, an toàn hơn).

* **Ủy quyền (Authorization):** Quyết định xem người dùng được làm gì.
    * **RBAC (Role-Based Access Control):** Phân quyền theo vai trò (admin, editor, author, viewer).
    * **ABAC (Attribute-Based Access Control):** Phân quyền dựa trên thuộc tính (ví dụ: chỉ cho phép người cùng phòng
      ban sửa bài viết của nhau).

### **4. CÁC ENDPOINT CHÍNH (NHỮNG CON ĐƯỜNG DẪN ĐẾN DỮ LIỆU)**

Mình sẽ liệt kê các endpoint phổ biến nhất cho CMS, kèm theo ví dụ dễ hiểu:

#### **4.1. QUẢN LÝ BÀI VIẾT (`/articles`)**

| Method   | URL                       | Chức năng                            | Payload (Request Body)                                                                        |
|----------|---------------------------|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `GET`    | `/articles`               | Lấy danh sách bài viết               | (Query Params): Phân trang, lọc, sắp xếp.                                                     |
| `GET`    | `/articles/{id}`          | Lấy thông tin chi tiết bài viết      | -                                                                                             |
| `POST`   | `/articles`               | Tạo bài viết mới                     | `{ title, content, author_id, category_id, tags, status, thumbnail }`.                        |
| `PUT`    | `/articles/{id}`          | Cập nhật toàn bộ bài viết            | `{ title, content, author_id, category_id, tags, status, thumbnail }`.                        |
| `PATCH`  | `/articles/{id}`          | Cập nhật một phần bài viết           | `{ title?, content?, author_id?, category_id?, tags?, status?, thumbnail? }` (`?`: tùy chọn). |
| `DELETE` | `/articles/{id}`          | Xóa bài viết                         | -                                                                                             |
| `GET`    | `/articles/{id}/comments` | Lấy danh sách bình luận của bài viết | (Query Params)                                                                                |
| `POST`   | `/articles/{id}/comments` | Thêm bình luận vào bài viết          | `{ content, author_id }`.                                                                     |

* **Trạng thái:** `draft` (nháp), `pending` (chờ duyệt), `published` (đã đăng).

**Ví dụ:**

* `GET /articles?page=2&limit=10&sort=-created_at`: Lấy 10 bài viết ở trang 2, sắp xếp theo thời gian tạo giảm dần.
* `POST /articles`: Tạo bài viết mới (gửi kèm JSON data).

#### **4.2. QUẢN LÝ DANH MỤC (`/categories`)**

| Method   | URL                         | Chức năng                   | Payload (Request Body)    |
|----------|-----------------------------|-----------------------------|---------------------------|
| `GET`    | `/categories`               | Lấy danh sách danh mục      | (Query Params)            |
| `GET`    | `/categories/{id}`          | Lấy chi tiết danh mục       | -                         |
| `POST`   | `/categories`               | Tạo danh mục mới            | `{ name, description }`   |
| `PUT`    | `/categories/{id}`          | Cập nhật toàn bộ danh mục   | `{ name, description }`   |
| `PATCH`  | `/categories/{id}`          | Cập nhật một phần danh mục  | `{ name?, description? }` |
| `DELETE` | `/categories/{id}`          | Xóa danh mục                | -                         |
| `GET`    | `/categories/{id}/articles` | Lấy bài viết thuộc danh mục | (Query Params)            |

#### **4.3. QUẢN LÝ NGƯỜI DÙNG (`/users`)**

| Method   | URL                    | Chức năng                    | Payload (Request Body)                                             |
|----------|------------------------|------------------------------|--------------------------------------------------------------------|
| `GET`    | `/users`               | Lấy danh sách người dùng     | (Query Params)                                                     |
| `GET`    | `/users/{id}`          | Lấy chi tiết người dùng      | -                                                                  |
| `POST`   | `/users`               | Tạo người dùng mới           | `{ username, password, email, first_name, last_name, role }`       |
| `PUT`    | `/users/{id}`          | Cập nhật toàn bộ người dùng  | `{ username?, password?, email?, first_name?, last_name?, role? }` |
| `PATCH`  | `/users/{id}`          | Cập nhật một phần người dùng | `{ username?, password?, email?, first_name?, last_name?, role? }` |
| `DELETE` | `/users/{id}`          | Xóa người dùng               | -                                                                  |
| `GET`    | `/users/{id}/articles` | Lấy bài viết của người dùng  | (Query Params)                                                     |

* **Vai trò:** `admin`, `editor`, `author`, `viewer`, ... hoặc vai trò tự tạo.

#### **4.4. QUẢN LÝ QUYỀN (`/permissions`)**

| Method   | URL                                 | Chức năng                 | Payload (Request Body)           |
|----------|-------------------------------------|---------------------------|----------------------------------|
| `GET`    | `/permissions`                      | Lấy danh sách quyền       | (Query Params)                   |
| `GET`    | `/permissions/{id}`                 | Lấy chi tiết quyền        | -                                |
| `POST`   | `/permissions`                      | Tạo quyền mới             | `{ name, description }`          |
| `PUT`    | `/permissions/{id}`                 | Cập nhật quyền            | `{ name, description }`          |
| `PATCH`  | `/permissions/{id}`                 | Cập nhật một phần quyền   | `{ name?, description? }`        |
| `DELETE` | `/permissions/{id}`                 | Xóa quyền                 | -                                |
| `GET`    | `/users/{id}/permissions`           | Lấy quyền của người dùng  | (Query Params)                   |
| `POST`   | `/users/{id}/permissions`           | Thêm quyền cho người dùng | `{ permissions_ids: [1, 2, 3] }` |
| `DELETE` | `/users/{id}/permissions/{perm_id}` | Xóa quyền của người dùng  | -                                |

#### **4.5. QUẢN LÝ MEDIA (`/media`)**

| Method   | URL           | Chức năng           | Payload (Request Body) |
|----------|---------------|---------------------|------------------------|
| `GET`    | `/media`      | Lấy danh sách media | (Query Params)         |
| `GET`    | `/media/{id}` | Lấy chi tiết media  | -                      |
| `POST`   | `/media`      | Upload media mới    | `FormData` (file)      |
| `DELETE` | `/media/{id}` | Xóa media           | -                      |

#### **4.6. QUẢN LÝ BÌNH LUẬN (`/comments`)**

| Method   | URL              | Chức năng                   | Payload (Request Body)                  |
|----------|------------------|-----------------------------|-----------------------------------------|
| `GET`    | `/comments`      | Lấy danh sách bình luận     | (Query Params)                          |
| `GET`    | `/comments/{id}` | Lấy chi tiết bình luận      | -                                       |
| `POST`   | `/comments`      | Tạo bình luận mới           | `{ content, author_id, article_id }`    |
| `PUT`    | `/comments/{id}` | Cập nhật toàn bộ bình luận  | `{ content, author_id, article_id }`    |
| `PATCH`  | `/comments/{id}` | Cập nhật một phần bình luận | `{ content?, author_id?, article_id? }` |
| `DELETE` | `/comments/{id}` | Xóa bình luận               | -                                       |

#### **4.7. QUẢN LÝ CÀI ĐẶT (`/settings`)**

| Method | URL         | Chức năng                         | Payload (Request Body)                                     |
|--------|-------------|-----------------------------------|------------------------------------------------------------|
| `GET`  | `/settings` | Lấy toàn bộ cài đặt hệ thống      | -                                                          |
| `PUT`  | `/settings` | Cập nhật toàn bộ cài đặt hệ thống | `{site_name, description, theme, logo, contact_email,...}` |

#### **4.8. QUẢN LÝ WEBHOOKS (`/webhooks`)**

| Method   | URL              | Chức năng              | Payload (Request Body) |
|----------|------------------|------------------------|------------------------|
| `GET`    | `/webhooks`      | Lấy danh sách webhooks | (Query Params)         |
| `GET`    | `/webhooks/{id}` | Lấy chi tiết webhook   | -                      |
| `POST`   | `/webhooks`      | Đăng ký webhook mới    | `{ url, events }`      |
| `PUT`    | `/webhooks/{id}` | Cập nhật webhook       | `{ url?, events? }`    |
| `DELETE` | `/webhooks/{id}` | Xóa webhook            | -                      |

* **Sự kiện webhook:** `article.created`, `article.updated`, `article.deleted`, `category.created`, `category.updated`,
  `category.deleted`, `user.registered`, `user.updated`, `comment.created`, `comment.deleted`

### **5. THAM SỐ TRUY VẤN (QUERY PARAMETERS) - LỌC DỮ LIỆU**

* `sort`: Sắp xếp (ví dụ: `sort=-created_at` - sắp xếp theo thời gian tạo giảm dần).
* `filter`: Lọc (ví dụ: `filter[category_id]=1` - chỉ lấy bài viết có `category_id` là 1).
* `search`: Tìm kiếm (ví dụ: `search=keyword`).
* `fields`: Chọn trường trả về (ví dụ: `fields=id,title,created_at` - chỉ trả về 3 trường này).
* `page`: Số trang (ví dụ: `page=1`).
* `per_page`: Số bản ghi mỗi trang (ví dụ: `per_page=20`).
* `status`: Lọc theo trạng thái (ví dụ: `status=published`).

**Ví dụ:**

`GET /articles?sort=-created_at&filter[author]=123&search=API&page=1&per_page=10&fields=id,title,created_at`

### **6. ĐỊNH DẠNG PHẢN HỒI (JSON)**

* **Thành công:**

```json
{
  "data": {
    "id": 1,
    "title": "Hướng dẫn API",
    "content": "Nội dung chi tiết...",
    "author": {
      "id": 123,
      "name": "Nguyễn Văn A"
    },
    "created_at": "2023-12-01T12:00:00Z"
  },
    "meta": {
        "page": 1,
        "per_page": 10,
        "total": 100
    }
}
```

* **Lỗi:**

```json
{
  "error": {
    "code": "INVALID_PARAMETER",
    "message": "Tham số 'title' không hợp lệ",
    "details": {
      "field": "title",
      "reason": "Độ dài tối thiểu là 5 ký tự"
    }
  }
}
```

* **Mã lỗi:** Dùng các mã lỗi có ý nghĩa: `INVALID_PARAMETER`, `UNAUTHORIZED`, `NOT_FOUND`, `SERVER_ERROR`, ...

### **7. BẢO MẬT (NHỚ LÀM CHO CẨN THẬN)**

* **HTTPS:** Bắt buộc phải dùng.
* **Validate input:** Kiểm tra kỹ dữ liệu đầu vào để tránh SQL Injection, XSS.
* **Rate Limiting:** Giới hạn số lần gọi API trong 1 khoảng thời gian để tránh bị "tấn công"
    * Header:
        * `X-RateLimit-Limit: 1000` (Yêu cầu tối đa).
        * `X-RateLimit-Remaining: 998` (Yêu cầu còn lại).
        * `X-RateLimit-Reset: 1692000000` (Thời gian reset).
* **CORS:** Chỉ cho phép các domain được phép gọi API.
* **Bảo mật password:** Không lưu password dạng text.
* **CSRF:** Dùng CSRF token nếu cần.

### **8. HIỆU SUẤT (CHẠY NHANH NHƯ CHỚP)**

* **Caching:** Dùng `ETag`, `Last-Modified`, `Cache-Control` để cache dữ liệu.
* **Nén dữ liệu:** Dùng Gzip hoặc Brotli để giảm kích thước response.
* **Phân trang:** Chia nhỏ dữ liệu khi trả về danh sách dài.
* **Lazy loading:** Chỉ tải dữ liệu cần thiết.
* **CDN:** Dùng CDN cho file media.
* **Database indexing:** Tạo index cho các cột thường tìm kiếm.

### **9. TÀI LIỆU API (CẦN THIẾT NHƯ "CƠM BỮA")**

* **Swagger/OpenAPI:** Tạo tài liệu API tương tác, dễ dùng.
* **Nội dung tài liệu:**
    * Mô tả endpoint, method, tham số.
    * Ví dụ request/response.
    * Mã lỗi.
    * Hướng dẫn xác thực, ủy quyền.
    * Ví dụ dùng query params.
* **Postman:** Dùng Postman collection để dễ test API.

### **10. WEBHOOKS (THÔNG BÁO SỰ KIỆN)**

* Endpoint đăng ký webhook: `/webhooks` (POST).
* Sự kiện hỗ trợ: `article.created`, `article.updated`, `article.deleted`, ...
* Webhook payload: Thông tin chi tiết về sự kiện.
* Cơ chế retry (thử lại) nếu webhook trả về lỗi.

### **11. MỘT SỐ CÂN NHẮC KHÁC**

* **Content Negotiation:** Hỗ trợ các định dạng dữ liệu khác (XML, ...).
* **Logging:** Ghi lại request/response để debug.
* **Giám sát API:** Theo dõi hiệu suất, lỗi.
* **Thống kê API:** Lấy dữ liệu về cách sử dụng API.
* **I18n:** Hỗ trợ đa ngôn ngữ qua header `Accept-Language`.

### **KẾT LUẬN**

Thiết kế API cho CMS không hề khó nếu bạn hiểu rõ nguyên tắc và thực hành nhiều. Hãy nhớ rằng, một API tốt là API dễ
dùng, mạnh mẽ, an toàn và linh hoạt. Hy vọng tài liệu này sẽ giúp các bạn "lên tay" nhanh chóng. Chúc các bạn thành
công! 😎
