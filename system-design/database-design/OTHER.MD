## **1. Từ Khóa Liên Quan đến Hiệu Năng**

### **1.1. Index (Chỉ Mục)**

- **Ý nghĩa:** Index giúp tăng tốc độ truy vấn dữ liệu bằng cách tạo các cấu trúc tìm kiếm hiệu quả trên các cột thường
  xuyên được truy vấn.
- **Các loại index phổ biến:**
    - **Primary Index (Chỉ mục chính):** Tự động tạo khi bạn chỉ định một khóa chính.
    - **Unique Index (Chỉ mục duy nhất):** Đảm bảo không có giá trị trùng lặp trong cột.
    - **Composite Index (Chỉ mục tổng hợp):** Tạo index trên nhiều cột.
    - **Full-Text Index:** Hỗ trợ tìm kiếm văn bản toàn bộ (full-text search).
- **Cân nhắc:**
    - Index làm tăng tốc độ đọc (SELECT) nhưng có thể làm chậm tốc độ ghi (INSERT, UPDATE, DELETE).
    - Không lạm dụng index trên các cột ít sử dụng.

---

### **1.2. Denormalization (Phi Chuẩn Hóa)**

- **Ý nghĩa:** Khi ưu tiên hiệu năng, đôi khi phải chấp nhận phi chuẩn hóa (không áp dụng đầy đủ 3NF) để giảm số lượng
  bảng cần truy vấn.
- **Ứng dụng:**
    - Dùng trong hệ thống đọc nhiều hơn ghi (read-heavy), ví dụ: các hệ thống báo cáo (reporting systems).
    - Sao chép dữ liệu quan trọng để giảm thời gian truy vấn phức tạp.

---

### **1.3. Partitioning (Phân Vùng)**

- **Ý nghĩa:** Chia dữ liệu lớn thành các phần nhỏ hơn (partition) để tăng tốc độ truy vấn và quản lý dữ liệu dễ dàng
  hơn.
- **Các loại phân vùng:**
    - **Horizontal Partitioning (Phân vùng ngang):** Chia dữ liệu theo hàng (ví dụ: chia theo thời gian, địa lý).
    - **Vertical Partitioning (Phân vùng dọc):** Chia dữ liệu theo cột (ví dụ: chia thông tin cá nhân và thông tin thanh
      toán).
- **Ứng dụng:** Dùng cho bảng có kích thước lớn hoặc truy vấn nhiều trên một tập con dữ liệu cụ thể.

---

### **1.4. Caching (Bộ Nhớ Đệm)**

- **Ý nghĩa:** Sử dụng bộ nhớ đệm để lưu trữ tạm thời các kết quả truy vấn thường xuyên được sử dụng, giúp giảm tải cho
  cơ sở dữ liệu.
- **Công cụ phổ biến:** Redis, Memcached, hoặc cache ngay trong ứng dụng.
- **Ví dụ:** Lưu trữ dữ liệu người dùng đăng nhập để tránh truy vấn lại bảng `Users`.

---

## **2. Từ Khóa Liên Quan đến Tính Toàn Vẹn Dữ Liệu**

### **2.1. Constraints (Ràng Buộc)**

- **Ý nghĩa:** Đảm bảo dữ liệu luôn hợp lệ và toàn vẹn.
- **Các loại ràng buộc:**
    - **Primary Key:** Đảm bảo mỗi hàng là duy nhất.
    - **Foreign Key:** Đảm bảo tính toàn vẹn tham chiếu giữa các bảng.
    - **Unique:** Ràng buộc dữ liệu không trùng lặp.
    - **Check:** Đảm bảo giá trị trong cột thỏa mãn một điều kiện nhất định (ví dụ: tuổi > 18).
    - **Not Null:** Đảm bảo cột không được phép để trống.
- **Ví dụ:**
  ```sql
  CREATE TABLE Orders (
      OrderID INT PRIMARY KEY,
      UserID INT NOT NULL,
      TotalAmount DECIMAL(10,2) CHECK (TotalAmount > 0)
  );
  ```

---

### **2.2. Transactions (Giao Dịch)**

- **Ý nghĩa:** Đảm bảo tất cả các thao tác trong một giao dịch (transaction) được thực hiện thành công hoặc không thực
  hiện gì cả.
- **ACID Properties:**
    - **Atomicity:** Tất cả các thao tác phải thành công hoặc không thao tác nào được thực hiện.
    - **Consistency:** Dữ liệu luôn ở trạng thái hợp lệ.
    - **Isolation:** Các giao dịch không làm ảnh hưởng lẫn nhau.
    - **Durability:** Dữ liệu sẽ không bị mất sau khi giao dịch hoàn thành (kể cả khi hệ thống gặp sự cố).

---

### **2.3. Referential Integrity (Toàn Vẹn Tham Chiếu)**

- **Ý nghĩa:** Đảm bảo các liên kết giữa bảng thông qua **foreign key** luôn hợp lệ.
- **Ví dụ:**
    - Khi một dòng trong bảng cha bị xóa, các dòng liên quan trong bảng con có thể:
        - **CASCADE:** Tự động xóa.
        - **SET NULL:** Đặt giá trị `NULL`.
        - **RESTRICT:** Ngăn việc xóa dòng cha nếu có dòng con.

---

## **3. Từ Khóa Liên Quan đến Tính Mở Rộng**

### **3.1. Scalability (Khả Năng Mở Rộng)**

- **Vertical Scaling (Mở rộng dọc):** Tăng tài nguyên phần cứng (CPU, RAM) của máy chủ hiện tại.
- **Horizontal Scaling (Mở rộng ngang):** Thêm nhiều máy chủ hơn để xử lý dữ liệu song song.
- **Ứng dụng:**
    - **Vertical:** Dùng trong giai đoạn nhỏ, dữ liệu chưa nhiều.
    - **Horizontal:** Áp dụng với hệ thống lớn, có khả năng phát triển.

---

### **3.2. Sharding (Phân Mảnh Dữ Liệu)**

- **Ý nghĩa:** Chia nhỏ dữ liệu thành nhiều cơ sở dữ liệu độc lập để giảm tải.
- **Ví dụ:** Phân mảnh dựa trên ID người dùng (`UserID % 3`), mỗi phần lưu trữ trên một máy chủ khác nhau.

---

## **4. Từ Khóa Liên Quan đến Bảo Mật**

### **4.1. Encryption (Mã Hóa)**

- **Ý nghĩa:** Bảo vệ dữ liệu nhạy cảm bằng cách mã hóa nó trước khi lưu trữ.
- **Ví dụ:**
    - Mã hóa mật khẩu với thuật toán như **bcrypt** hoặc **SHA-256**.
    - Mã hóa dữ liệu thẻ thanh toán với **AES**.

---

### **4.2. Access Control (Kiểm Soát Truy Cập)**

- **Ý nghĩa:** Phân quyền truy cập dữ liệu cho các vai trò khác nhau.
- **Ví dụ:**
    - Quản trị viên có thể đọc/ghi/xóa tất cả dữ liệu.
    - Người dùng thường chỉ có quyền đọc và ghi dữ liệu của họ.

---

### **4.3. Backup and Recovery (Sao Lưu và Khôi Phục)**

- **Ý nghĩa:** Tạo bản sao lưu định kỳ để tránh mất mát dữ liệu.
- **Ví dụ:** Sao lưu cơ sở dữ liệu mỗi ngày và lưu trữ trên các máy chủ khác nhau.

---

## **5. Từ Khóa Liên Quan đến Khả Năng Bảo Trì**

### **5.1. Schema Design (Thiết Kế Schema)**

- **Ý nghĩa:** Tạo cấu trúc hợp lý và dễ mở rộng cho bảng và quan hệ.
- **Ví dụ:**
    - Sử dụng chuẩn đặt tên thống nhất (snake_case hoặc camelCase).
    - Nhóm các bảng liên quan trong một schema cụ thể.

---

### **5.2. Data Archiving (Lưu Trữ Dữ Liệu)**

- **Ý nghĩa:** Di chuyển dữ liệu cũ hoặc không còn sử dụng đến các hệ thống lưu trữ ít tốn kém hơn.
- **Ví dụ:** Lưu trữ các giao dịch cũ hơn 5 năm vào bảng khác.

---

### **5.3. Logging and Monitoring (Ghi Log và Giám Sát)**

- **Ý nghĩa:** Theo dõi hoạt động của cơ sở dữ liệu để phát hiện lỗi hoặc tối ưu hóa hiệu suất.
- **Công cụ phổ biến:** Prometheus, Grafana, ELK Stack.

---

## **Tóm Lại:**

Khi thiết kế cơ sở dữ liệu, bạn cần quan tâm đến:

1. **Hiệu năng:** Index, phân vùng, cache.
2. **Toàn vẹn dữ liệu:** Constraints, Transactions, Referential Integrity.
3. **Mở rộng:** Scalability, Sharding.
4. **Bảo mật:** Mã hóa, kiểm soát truy cập.
5. **Bảo trì:** Schema rõ ràng, lưu trữ dữ liệu lâu dài.

