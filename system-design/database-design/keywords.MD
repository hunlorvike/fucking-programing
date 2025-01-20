## **🔥 TỪ ĐIỂN "THẦN CHÚ" THIẾT KẾ DATABASE CHO DÂN CODE 🔥**

Yo các bạn sinh viên IT! Hôm nay mình sẽ cùng nhau "giải mã" các từ khóa "bí ẩn" trong thiết kế database. Những từ này
nghe có vẻ "cao siêu" nhưng thực ra rất gần gũi và cần thiết cho dân code chúng mình. Cùng mình khám phá nhé!

### **1. TỪ KHÓA LIÊN QUAN ĐẾN HIỆU NĂNG (CHẠY NHANH NHƯ TÊN LỬA)**

#### **1.1. Index (Chỉ Mục) - "Đánh Dấu" Dữ Liệu:**

* **Ý nghĩa:** Giúp tìm kiếm dữ liệu nhanh hơn bằng cách tạo cấu trúc tìm kiếm đặc biệt trên các cột (như kiểu đánh dấu
  trang sách ấy).
* **Các loại index:**
    * **Primary Index (Chỉ mục chính):** Tự tạo khi có khóa chính (như kiểu số chứng minh thư, mỗi người có 1 cái).
    * **Unique Index (Chỉ mục duy nhất):** Đảm bảo dữ liệu không trùng lặp (như kiểu email, mỗi người có 1 cái).
    * **Composite Index (Chỉ mục tổng hợp):** Tạo index trên nhiều cột (như kiểu tìm theo tên và địa chỉ).
    * **Full-Text Index:** Hỗ trợ tìm kiếm toàn văn (như kiểu tìm kiếm trên Google).
* **Cân nhắc:**
    * **Ưu:** Đọc (SELECT) nhanh hơn.
    * **Nhược:** Ghi (INSERT, UPDATE, DELETE) chậm hơn.
    * **Mẹo:** Không lạm dụng index, chỉ dùng cho cột hay tìm kiếm thôi.

#### **1.2. Denormalization (Phi Chuẩn Hóa) - "Ăn Gian" Để Nhanh Hơn:**

* **Ý nghĩa:** Đôi khi ta phải "chấp nhận" vi phạm các quy tắc chuẩn hóa (như 3NF) để giảm số bảng cần truy vấn và tăng
  tốc độ.
* **Khi nào dùng:**
    * Hệ thống đọc nhiều hơn ghi (ví dụ: hệ thống báo cáo).
    * Cần truy vấn dữ liệu phức tạp.
    * **Ví dụ:** Thay vì tách bảng `users` và `orders`, ta có thể thêm thông tin `user_name` vào bảng `orders` để không
      cần JOIN.

#### **1.3. Partitioning (Phân Vùng) - "Chia Nhỏ" Dữ Liệu:**

* **Ý nghĩa:** Chia bảng lớn thành các phần nhỏ hơn để dễ quản lý và truy vấn nhanh hơn.
* **Các loại:**
    * **Horizontal Partitioning (Phân vùng ngang):** Chia theo hàng (ví dụ: chia theo năm, theo khu vực).
    * **Vertical Partitioning (Phân vùng dọc):** Chia theo cột (ví dụ: chia thông tin cá nhân và thông tin thanh toán).
* **Mẹo:** Dùng cho bảng quá lớn hoặc khi truy vấn trên 1 phần nhỏ dữ liệu.

#### **1.4. Caching (Bộ Nhớ Đệm) - "Gom" Dữ Liệu Lại:**

* **Ý nghĩa:** Lưu trữ tạm thời kết quả truy vấn ở bộ nhớ đệm để lần sau dùng lại luôn, không cần truy vấn database nữa.
* **Công cụ:** Redis, Memcached.
* **Ví dụ:** Lưu thông tin người dùng đã đăng nhập để không cần truy vấn lại database mỗi lần.

### **2. TỪ KHÓA LIÊN QUAN ĐẾN TÍNH TOÀN VẸN DỮ LIỆU (DỮ LIỆU "SẠCH")**

#### **2.1. Constraints (Ràng Buộc) - "Luật Lệ" Cho Dữ Liệu:**

* **Ý nghĩa:** Đảm bảo dữ liệu luôn hợp lệ và đúng định dạng.
* **Các loại ràng buộc:**
    * **Primary Key:** Mỗi bản ghi có 1 "chứng minh thư" riêng.
    * **Foreign Key:** Đảm bảo liên kết giữa các bảng là đúng (như kiểu liên kết giữa user và order).
    * **Unique:** Dữ liệu không bị trùng lặp (như email).
    * **Check:** Kiểm tra dữ liệu có hợp lệ không (ví dụ: `age > 18`).
    * **Not Null:** Cột không được để trống.
* **Ví dụ:**

```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    UserID INT NOT NULL,
    TotalAmount DECIMAL(10,2) CHECK (TotalAmount > 0)
);
```

#### **2.2. Transactions (Giao Dịch) - "Đảm Bảo" Tất Cả Thành Công:**

* **Ý nghĩa:** Đảm bảo một nhóm thao tác (như insert, update) hoặc là thành công hết, hoặc là thất bại hết, không có
  chuyện "nửa nạc nửa mỡ".
* **ACID Properties:**
    * **Atomicity:** Hoặc tất cả, hoặc không cái nào.
    * **Consistency:** Dữ liệu luôn ở trạng thái đúng.
    * **Isolation:** Các giao dịch không làm ảnh hưởng lẫn nhau.
    * **Durability:** Dữ liệu không bị mất khi giao dịch thành công.

#### **2.3. Referential Integrity (Toàn Vẹn Tham Chiếu) - "Liên Kết" Đúng:**

* **Ý nghĩa:** Đảm bảo liên kết giữa các bảng (qua khóa ngoại) luôn đúng.
* **Ví dụ:** Khi xóa người dùng, các đơn hàng liên quan có thể:
    * `CASCADE`: Tự động xóa luôn.
    * `SET NULL`: Đặt lại `NULL`.
    * `RESTRICT`: Không cho xóa nếu còn đơn hàng.

### **3. TỪ KHÓA LIÊN QUAN ĐẾN TÍNH MỞ RỘNG (PHÁT TRIỂN KHÔNG GIỚI HẠN)**

#### **3.1. Scalability (Khả Năng Mở Rộng) - "Lớn Mạnh" Hơn:**

* **Ý nghĩa:** Khả năng đáp ứng khi số lượng người dùng hoặc dữ liệu tăng lên.
* **Các loại:**
    * **Vertical Scaling (Mở rộng dọc):** Tăng sức mạnh phần cứng của server (CPU, RAM).
        * **Mẹo:** Phù hợp khi dữ liệu chưa nhiều.
    * **Horizontal Scaling (Mở rộng ngang):** Thêm nhiều server (phân tán dữ liệu).
        * **Mẹo:** Phù hợp khi dữ liệu lớn và có khả năng phát triển.

#### **3.2. Sharding (Phân Mảnh Dữ Liệu) - "Chia Nhỏ" Để Gánh Đỡ:**

* **Ý nghĩa:** Chia dữ liệu ra nhiều database để giảm tải.
* **Ví dụ:** Chia theo ID người dùng, mỗi database chứa 1 nhóm người dùng.

### **4. TỪ KHÓA LIÊN QUAN ĐẾN BẢO MẬT (DỮ LIỆU "AN TOÀN")**

#### **4.1. Encryption (Mã Hóa) - "Bọc" Dữ Liệu Kín Đáo:**

* **Ý nghĩa:** Mã hóa dữ liệu nhạy cảm (password, thông tin thẻ) để tránh bị đánh cắp.
* **Ví dụ:** Dùng bcrypt hoặc SHA-256 để mã hóa password.

#### **4.2. Access Control (Kiểm Soát Truy Cập) - "Phân Quyền" Truy Cập:**

* **Ý nghĩa:** Phân quyền cho từng user, ai được làm gì trên dữ liệu.
* **Ví dụ:** Admin có quyền đọc/ghi tất cả, user thường chỉ có quyền đọc dữ liệu của mình.

#### **4.3. Backup and Recovery (Sao Lưu và Khôi Phục) - "Bản Sao Lưu" Quan Trọng:**

* **Ý nghĩa:** Tạo bản sao dữ liệu định kỳ để tránh mất mát.
* **Mẹo:** Sao lưu thường xuyên và lưu ở nhiều nơi khác nhau.

### **5. TỪ KHÓA LIÊN QUAN ĐẾN KHẢ NĂNG BẢO TRÌ (DỄ DÀNG CHĂM SÓC)**

#### **5.1. Schema Design (Thiết Kế Schema) - "Bản Vẽ" Database:**

* **Ý nghĩa:** Tạo cấu trúc rõ ràng, dễ mở rộng cho database.
* **Mẹo:**
    * Dùng chuẩn đặt tên thống nhất (snake\_case hoặc camelCase).
    * Nhóm các bảng liên quan vào chung 1 schema.

#### **5.2. Data Archiving (Lưu Trữ Dữ Liệu) - "Dọn Dẹp" Dữ Liệu:**

* **Ý nghĩa:** Chuyển dữ liệu cũ, ít dùng sang nơi lưu trữ khác để giảm tải cho database chính.
* **Ví dụ:** Lưu trữ các giao dịch cũ hơn 5 năm vào bảng khác.

#### **5.3. Logging and Monitoring (Ghi Log và Giám Sát) - "Theo Dõi" Database:**

* **Ý nghĩa:** Theo dõi hoạt động database để phát hiện lỗi và tối ưu hiệu suất.
* **Công cụ:** Prometheus, Grafana, ELK Stack.

### **TÓM LẠI:**

Khi thiết kế database, bạn cần quan tâm đến:

1. **Hiệu năng:** Index, partitioning, caching.
2. **Toàn vẹn dữ liệu:** Constraints, transactions, referential integrity.
3. **Mở rộng:** Scalability, sharding.
4. **Bảo mật:** Encryption, access control.
5. **Bảo trì:** Schema design, data archiving.

Hy vọng những "thần chú" này sẽ giúp các bạn "lên level" trong thiết kế database nhé! Chúc các bạn thành công! 😎
