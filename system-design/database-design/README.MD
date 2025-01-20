## **🚀 HƯỚNG DẪN SIÊU DỄ THIẾT KẾ DATABASE CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Chắc chắn ai trong chúng ta cũng từng "vật lộn" với database rồi đúng không? Nó như cái "xương
sống" của mọi ứng dụng, nhưng thiết kế không khéo thì dễ "tắc đường" lắm. Hôm nay mình sẽ chia sẻ kinh nghiệm để các bạn
thiết kế database vừa ngon, vừa bổ, lại vừa dễ bảo trì nhé. Bắt đầu thôi!

### **I. DATABASE LÀ GÌ VÀ TẠI SAO PHẢI QUAN TÂM?**

* **Database (Cơ sở dữ liệu):** Là nơi lưu trữ thông tin của ứng dụng (như kiểu cái kho chứa đồ của bạn ấy).
* **Quan trọng:**
    * **Lưu trữ dữ liệu:** Không có database thì thông tin của bạn "bay màu" hết.
    * **Truy xuất dữ liệu:** Lấy dữ liệu nhanh, không bị chậm chạp.
    * **Quản lý dữ liệu:** Dữ liệu không bị lộn xộn, mất mát.
    * **Mở rộng ứng dụng:** Dễ dàng thêm tính năng mới mà không làm hỏng cấu trúc.

### **II. NGUYÊN TẮC VÀNG TRONG THIẾT KẾ DATABASE (DỄ NHỚ NHƯ ĐẾM NGÓN TAY)**

1. **Bình thường hóa (Normalization) - "Dọn dẹp" dữ liệu:**
    * **Mục tiêu:** Loại bỏ dữ liệu trùng lặp, đảm bảo dữ liệu "sạch".
    * **1NF (First Normal Form):** Mỗi ô chỉ chứa một giá trị, không có bảng lồng nhau.
        * **Ví dụ:** Không nên có cột `address` chứa cả số nhà, tên đường, thành phố. Nên tách thành các cột riêng.
    * **2NF (Second Normal Form):** Các cột không phải khóa phụ thuộc hoàn toàn vào khóa chính.
    * **3NF (Third Normal Form):** Không có phụ thuộc "bắc cầu" (nếu A -> B, B -> C thì không nên có A -> C).
        * **Ví dụ:** Không nên có cột `category_name` trong bảng `products`, vì `category_id` đã đủ rồi.

2. **Chọn đúng kiểu dữ liệu - "Chọn đồ" cho dữ liệu:**
    * `INTEGER`: Số nguyên (1, 2, 3, ...).
    * `VARCHAR`: Chuỗi ký tự (tên, email, ...).
    * `DATE/TIME`: Ngày giờ.
    * `BOOLEAN`: True/False (có/không).
    * **Mẹo:** Dùng kiểu dữ liệu nhỏ nhất có thể để tiết kiệm dung lượng và tăng hiệu suất.
        * Không dùng `TEXT` khi `VARCHAR` đã đủ.

3. **Tính toàn vẹn dữ liệu - "Kiểm tra" dữ liệu:**
    * **Toàn vẹn miền giá trị:** Dữ liệu phải nằm trong phạm vi cho phép.
        * **Ví dụ:** Giới tính chỉ là `Nam` hoặc `Nữ`.
    * **Toàn vẹn tham chiếu:** Đảm bảo liên kết giữa các bảng (dùng khóa ngoại).
    * **Toàn vẹn thực thể:** Mỗi bản ghi phải có khóa chính duy nhất.

4. **Khóa chính và khóa ngoại - "Chìa khóa" và "liên kết":**
    * **Khóa chính (Primary Key):** Định danh duy nhất cho mỗi bản ghi.
        * **Ví dụ:** `id` trong bảng `users`.
    * **Khóa ngoại (Foreign Key):** Kết nối giữa các bảng.
        * **Ví dụ:** `user_id` trong bảng `orders` tham chiếu đến `id` của bảng `users`.

5. **Tránh dư thừa dữ liệu - "Tiết kiệm" dữ liệu:**
    * Dữ liệu lặp lại làm chậm database và dễ gây lỗi.
    * **Mẹo:** Tạo quan hệ giữa các bảng để giảm dư thừa.

### **III. QUY TRÌNH THIẾT KẾ DATABASE (TỪ A ĐẾN Z)**

1. **Thu thập yêu cầu - "Hỏi han" người dùng:**
    * Xác định dữ liệu cần lưu, cách dùng, và mối quan hệ giữa chúng.
        * **Ví dụ:** Thông tin người dùng, sản phẩm, đơn hàng, ...

2. **Thiết kế ERD (Entity-Relationship Diagram) - "Vẽ bản đồ" cho dữ liệu:**
    * Dùng sơ đồ ERD để hình dung các đối tượng và mối quan hệ.
    * **Ví dụ:** Vẽ hình chữ nhật cho thực thể (User, Product), hình thoi cho quan hệ (mua hàng, like).

3. **Phân tích thực thể - "Mổ xẻ" đối tượng:**
    * **Thực thể (Entity):** Các đối tượng chính (User, Product, Order).
    * **Thuộc tính (Attribute):** Đặc điểm của thực thể (tên, giá, email).

4. **Định nghĩa quan hệ - "Kết nối" các đối tượng:**
    * **1-1 (One-to-One):** Một người dùng có một profile.
    * **1-n (One-to-Many):** Một người dùng có nhiều đơn hàng.
    * **n-n (Many-to-Many):** Nhiều người dùng thích nhiều sản phẩm (cần bảng trung gian).

### **IV. TỐI ƯU HIỆU SUẤT DATABASE (CHẠY NHANH NHƯ TÊN LỬA)**

1. **Chỉ số (Indexes) - "Đánh dấu" dữ liệu:**
    * Tăng tốc truy vấn bằng cách tạo index trên các cột hay tìm kiếm.
        * **Ví dụ:** Tạo index cho cột `email` trong bảng `users`.
    * **Mẹo:** Đừng tạo quá nhiều index, sẽ làm chậm quá trình insert/update.

2. **Phân mảnh dữ liệu (Sharding) - "Chia nhỏ" dữ liệu:**
    * Chia database thành nhiều phần để giảm tải.
    * **Ví dụ:** Chia theo vùng, theo thời gian.

3. **Bộ nhớ đệm (Caching) - "Gom" dữ liệu lại:**
    * Dùng Redis hoặc Memcached để lưu kết quả truy vấn.
    * **Mẹo:** Dùng caching cho dữ liệu ít thay đổi.

4. **Phân trang dữ liệu (Pagination) - "Chia nhỏ" kết quả:**
    * Giới hạn số bản ghi trả về.
        * **Ví dụ SQL:** `SELECT * FROM users LIMIT 10 OFFSET 20`.

5. **Giới hạn kích thước bảng - "Chia" bảng lớn:**
    * Nếu bảng quá lớn, chia thành bảng con (theo thời gian, vùng, ...).

### **V. CÁC QUY TẮC ĐẶT TÊN (ĐẸP MÀ LẠI DỄ HIỂU)**

* **Rõ ràng, dễ hiểu:** Ai cũng hiểu ý nghĩa.
* **Bảng:** Danh từ số nhiều (`users`, `orders`).
* **Cột:** Danh từ hoặc tính từ (`user_id`, `created_at`).
* **snake\_case:** `user_id` thay vì `userId`.
* **Tránh:** Từ khóa SQL (`SELECT`, `TABLE`).

### **VI. TÍNH TOÀN VẸN VÀ BẢO MẬT (CỰC KÌ QUAN TRỌNG)**

1. **Ràng buộc (Constraints) - "Luật chơi" cho dữ liệu:**
    * `NOT NULL`: Không cho phép để trống.
    * `UNIQUE`: Không cho phép trùng lặp.
    * `CHECK`: Giới hạn giá trị (`CHECK(age > 0)`).
    * `DEFAULT`: Giá trị mặc định.

2. **Sao lưu dữ liệu (Backup) - "Phòng bệnh" hơn chữa bệnh:**
    * Lập lịch backup tự động để phục hồi khi có sự cố.

3. **Bảo mật database - "Khóa cửa" cẩn thận:**
    * **Phân quyền người dùng:** Hạn chế quyền truy cập cho các tài khoản khác nhau.
    * **Mã hóa dữ liệu:** Mã hóa mật khẩu (Bcrypt, SHA-256).

### **VII. KIỂM THỬ VÀ GIÁM SÁT (KIỂM TRA THƯỜNG XUYÊN)**

* **Kiểm thử:** Kiểm tra với dữ liệu thật và số lượng lớn.
* **Giám sát:** Dùng các công cụ như New Relic hoặc Prometheus để theo dõi hiệu suất và lỗi.

### **VIII. VÍ DỤ THIẾT KẾ DATABASE (THỰC HÀNH LÀ CHÍNH)**

#### **1. Hệ thống quản lý người dùng và đơn hàng**

* **ERD:**
    * Bảng `users` (id, name, email, created_at).
    * Bảng `orders` (id, user_id, total_price, created_at).
    * Quan hệ 1-n giữa `users` và `orders`.
* **SQL Tạo Bảng:**

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

### **IX. KẾT LUẬN**

Thiết kế database là một quá trình cần thời gian và thực hành. Đừng nản nếu gặp khó khăn, hãy cứ từ từ tìm hiểu và áp
dụng các nguyên tắc trên. Chúc các bạn trở thành những "phù thủy" database nhé! 😎
