# **HƯỚNG DẪN CHI TIẾT THIẾT KẾ DATABASE**

Database (Cơ sở dữ liệu) là nền tảng quan trọng trong việc lưu trữ, quản lý và xử lý dữ liệu. Thiết kế database hiệu quả
giúp đảm bảo hiệu suất, khả năng mở rộng, và bảo trì của hệ thống. Dưới đây là hướng dẫn chi tiết về các nguyên tắc
thiết kế database.

---

## **I. Tổng Quan về Thiết Kế Database**

Thiết kế database là quy trình tổ chức và cấu trúc dữ liệu nhằm hỗ trợ các ứng dụng hoạt động hiệu quả và dễ bảo trì.
Một database được thiết kế tốt cần:

- **Đáp ứng yêu cầu lưu trữ và xử lý dữ liệu.**
- **Hiệu quả trong truy xuất dữ liệu.**
- **Dễ bảo trì và mở rộng khi ứng dụng phát triển.**
- **Bảo vệ dữ liệu trước lỗi và các nguy cơ bảo mật.**

---

## **II. Các Nguyên Tắc Cơ Bản trong Thiết Kế Database**

### **1. Bình thường hóa (Normalization)**

- **Mục tiêu:** Loại bỏ dư thừa dữ liệu và đảm bảo tính toàn vẹn.
- **Các dạng chuẩn phổ biến:**
    - **1NF (First Normal Form):** Loại bỏ bảng lồng nhau; đảm bảo mỗi ô chứa một giá trị duy nhất.
    - **2NF (Second Normal Form):** Mỗi cột không khóa phải phụ thuộc hoàn toàn vào khóa chính.
    - **3NF (Third Normal Form):** Không có phụ thuộc bắc cầu giữa các thuộc tính không phải khóa.

### **2. Chọn đúng kiểu dữ liệu**

- Lựa chọn kiểu dữ liệu phù hợp để tối ưu hóa dung lượng và hiệu suất:
    - **INTEGER:** Lưu trữ số nguyên.
    - **VARCHAR:** Dữ liệu văn bản có độ dài thay đổi.
    - **DATE/TIME:** Lưu trữ thông tin ngày giờ.
- Tránh sử dụng kiểu dữ liệu quá lớn hoặc không cần thiết (VD: không dùng `TEXT` nếu `VARCHAR` là đủ).

### **3. Tính toàn vẹn dữ liệu (Data Integrity)**

- **Toàn vẹn miền giá trị:** Đảm bảo dữ liệu trong cột nằm trong phạm vi cho phép (VD: giới tính chỉ là `Male` hoặc
  `Female`).
- **Toàn vẹn tham chiếu:** Đảm bảo tính liên kết giữa các bảng qua khóa ngoại.
- **Toàn vẹn thực thể:** Mỗi bản ghi phải có khóa chính duy nhất.

### **4. Khóa chính và khóa ngoại**

- **Khóa chính (Primary Key):** Định danh duy nhất cho từng bản ghi.
    - Ví dụ: `id` trong bảng `users`.
- **Khóa ngoại (Foreign Key):** Duy trì quan hệ giữa các bảng.
    - Ví dụ: `user_id` trong bảng `orders` tham chiếu đến `id` của bảng `users`.

### **5. Tránh dư thừa dữ liệu (Redundancy)**

- Dữ liệu lặp lại làm tăng kích thước database và dễ gây lỗi đồng bộ.
- Sử dụng quan hệ giữa các bảng để giảm thiểu dư thừa.

---

## **III. Quy Trình Thiết Kế Database**

### **1. Thu thập yêu cầu**

- Xác định dữ liệu cần lưu trữ và cách sử dụng chúng:
    - Thông tin người dùng (VD: tên, email, mật khẩu).
    - Quan hệ giữa các đối tượng (VD: mỗi người dùng có nhiều đơn hàng).

### **2. Thiết kế mô hình thực thể - quan hệ (ERD)**

- Sử dụng **Entity-Relationship Diagram** để hình dung các thực thể và mối quan hệ giữa chúng.

### **3. Phân tích các thực thể**

- Xác định thực thể và thuộc tính:
    - **Thực thể (Entity):** Các đối tượng chính (VD: User, Product, Order).
    - **Thuộc tính (Attribute):** Đặc điểm của thực thể (VD: tên, giá).

### **4. Định nghĩa quan hệ**

- Các loại quan hệ phổ biến:
    - **1-1 (One-to-One):** Một người dùng có một hồ sơ.
    - **1-n (One-to-Many):** Một người dùng có nhiều đơn hàng.
    - **n-n (Many-to-Many):** Nhiều người dùng có thể thích nhiều sản phẩm.

---

## **IV. Tối Ưu Hiệu Suất Database**

### **1. Chỉ số (Indexes)**

- Sử dụng **indexes** để tăng tốc truy vấn.
- Chỉ tạo index trên các cột thường xuyên được tìm kiếm hoặc sắp xếp.
    - VD: Cột `email` trong bảng `users`.

### **2. Phân mảnh dữ liệu (Sharding)**

- Chia dữ liệu thành nhiều phân đoạn để giảm tải trên một database duy nhất.

### **3. Bộ nhớ đệm (Caching)**

- Dùng các công cụ như Redis hoặc Memcached để lưu trữ kết quả truy vấn.

### **4. Phân trang dữ liệu (Pagination)**

- Giới hạn số lượng bản ghi trả về mỗi lần:
    - `SELECT * FROM users LIMIT 10 OFFSET 20`.

### **5. Giới hạn kích thước bảng**

- Nếu bảng quá lớn, có thể chia thành các bảng con dựa trên thời gian, khu vực, hoặc nhóm logic.

---

## **V. Các Quy Tắc Đặt Tên**

- Sử dụng tên rõ ràng, dễ hiểu:
    - Bảng: **Danh từ số nhiều** (VD: `users`, `orders`).
    - Cột: **Danh từ hoặc tính từ miêu tả rõ ràng** (VD: `user_id`, `created_at`).
- Sử dụng **snake_case** thay vì camelCase:
    - Đúng: `user_id`.
    - Sai: `userId`.
- Tránh từ khóa SQL làm tên cột (VD: `SELECT`, `TABLE`).

---

## **VI. Tính Toàn Vẹn và Bảo Mật**

### **1. Kiểm tra ràng buộc (Constraints)**

- **NOT NULL:** Đảm bảo một cột không được phép để trống.
- **UNIQUE:** Không cho phép giá trị trùng lặp.
- **CHECK:** Giới hạn giá trị nhập vào (VD: `CHECK(age > 0)`).
- **DEFAULT:** Gán giá trị mặc định nếu không nhập.

### **2. Sao lưu dữ liệu (Backup)**

- Thiết lập lịch trình sao lưu tự động để đảm bảo khôi phục khi xảy ra lỗi.

### **3. Bảo mật database**

- **Phân quyền người dùng:** Hạn chế quyền truy cập cho các tài khoản khác nhau (chỉ SELECT, INSERT, UPDATE với từng
  user).
- **Mã hóa dữ liệu:** Dữ liệu nhạy cảm như mật khẩu cần được mã hóa (VD: Bcrypt, SHA-256).

---

## **VII. Kiểm Thử và Giám Sát Database**

- **Kiểm thử:** Đảm bảo database xử lý tốt với dữ liệu thực tế và dữ liệu lớn.
- **Giám sát:** Sử dụng công cụ như **New Relic** hoặc **Prometheus** để theo dõi hiệu suất và phát hiện lỗi.

---

## **VIII. Ví Dụ Thiết Kế Database**

### **1. Hệ thống quản lý người dùng và đơn hàng**

#### **ERD (Entity-Relationship Diagram):**

- **Bảng `users`:**
    - `id` (Primary Key)
    - `name`
    - `email`
    - `created_at`
- **Bảng `orders`:**
    - `id` (Primary Key)
    - `user_id` (Foreign Key)
    - `total_price`
    - `created_at`

#### **SQL Tạo Bảng**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

---

## **IX. Kết Luận**

Thiết kế database đóng vai trò quan trọng trong việc đảm bảo ứng dụng hoạt động hiệu quả và bền vững. Việc áp dụng các
nguyên tắc trên không chỉ giúp cải thiện hiệu suất, mà còn giúp hệ thống dễ dàng bảo trì và mở rộng trong tương lai.
