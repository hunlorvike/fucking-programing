## **🚀 "GIẢI MÃ" INDEX TRONG SQL SERVER: "ĐI TẮT" CHO CÂU TRUY VẤN CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm cực kỳ quan trọng trong SQL Server:
Index (Chỉ mục). Đây là một "chiêu thức" lợi hại giúp bạn tăng tốc độ tìm kiếm dữ liệu trong database, như kiểu bạn có "
bản đồ" giúp bạn đi đến đích nhanh hơn vậy. Cùng mình "mổ xẻ" nó nhé!

### **I. INDEX LÀ GÌ? (NHƯ "BẢN ĐỒ" CHO DATABASE)**

- **Index (Chỉ mục):** Là một cấu trúc dữ liệu giúp SQL Server tìm kiếm dữ liệu nhanh hơn trong bảng.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn tìm sách trong thư viện: bạn tra mục lục (index) để biết sách nằm ở đâu, thay vì tìm từng cuốn
      một.
- **Quan trọng vì:**
    - **Tốc độ:** Giúp câu truy vấn (query) chạy nhanh hơn.
    - **Hiệu quả:** Tiết kiệm tài nguyên (CPU, RAM, ...).
    - **Trải nghiệm:** Giúp ứng dụng mượt mà, nhanh hơn.

### **II. CÁC LOẠI INDEX PHỔ BIẾN (CÁC LOẠI "BẢN ĐỒ")**

1. **Clustered Index (Chỉ mục nhóm cụm):**
    - Quy định _thứ tự vật lý_ của dữ liệu trong bảng (dữ liệu được sắp xếp theo thứ tự index).
    - Mỗi bảng _chỉ có một_ clustered index.
    - Thường được tạo trên cột khóa chính (`Primary Key`).
2. **Nonclustered Index (Chỉ mục không nhóm cụm):**
    - Không quy định thứ tự vật lý của dữ liệu (như index ở cuối sách).
    - Mỗi bảng có thể có _nhiều_ nonclustered index.
    - Dùng khi có các cột thường xuyên được tìm kiếm, lọc, ...
3. **Composite Index (Chỉ mục tổng hợp):**
    - Index được tạo trên _nhiều cột_ (giúp tìm kiếm hiệu quả khi có nhiều điều kiện lọc).
    - **Ví dụ:** Index trên `LastName`, `FirstName` giúp truy vấn nhanh hơn nếu thường tìm theo cả họ và tên.
4. **Unique Index:**
    - Đảm bảo _giá trị duy nhất_ của cột (ví dụ: email, số điện thoại).
    - Có thể là clustered hoặc nonclustered.
5. **Full-Text Index:**
    - Dùng cho các cột kiểu chữ (text, varchar), hỗ trợ tìm kiếm toàn văn.

### **III. CÁCH TẠO INDEX (CÁCH "VẼ BẢN ĐỒ")**

```sql
CREATE [UNIQUE] [CLUSTERED | NONCLUSTERED] INDEX index_name
ON table_name (column1 [ASC|DESC], column2 [ASC|DESC], ...);
```

- **`CREATE INDEX index_name`:** Tạo index với tên `index_name`.
- **`ON table_name (column1, column2, ...)`:** Tạo index trên các cột `column1`, `column2`, ...
- **`CLUSTERED | NONCLUSTERED`:** Chọn loại index (clustered hoặc nonclustered).
- **`UNIQUE`:** Tạo unique index (đảm bảo giá trị duy nhất).
- **`ASC|DESC`:** Thứ tự sắp xếp (tăng dần hoặc giảm dần).

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

1. **Tạo nonclustered index trên cột `LastName`:**

```sql
CREATE INDEX idx_lastname ON Employees (LastName);
```

2. **Tạo composite index trên `LastName` và `FirstName`:**

```sql
CREATE INDEX idx_fullname ON Employees (LastName, FirstName);
```

3. **Tạo unique index trên cột `Email`:**

```sql
CREATE UNIQUE INDEX idx_email ON Employees (Email);
```

### **V. KHI NÀO NÊN DÙNG INDEX (KHI NÀO "CẦN BẢN ĐỒ")**

1. **Khi tìm kiếm:** Tạo index cho các cột thường dùng trong `WHERE`, `JOIN`.
2. **Khi sắp xếp:** Tạo index cho các cột dùng trong `ORDER BY`.
3. **Khi kết nối:** Tạo index trên các cột dùng trong `JOIN`.
4. **Khi cần unique:** Tạo unique index khi cần đảm bảo giá trị duy nhất.
5. **Chú ý:** Đừng tạo quá nhiều index, sẽ làm chậm các thao tác ghi (INSERT, UPDATE, DELETE).

### **VI. CÁCH HOẠT ĐỘNG CỦA INDEX (NÓ HOẠT ĐỘNG NHƯ THẾ NÀO?)**

1. **Khi truy vấn:** SQL Server dùng index để tìm dữ liệu nhanh hơn.
2. **`Index Seek`:** SQL Server truy cập trực tiếp vào các trang dữ liệu (tốt nhất).
3. **`Index Scan`:** SQL Server duyệt qua index (chậm hơn `Index Seek`).
4. **`Key Lookup`:** Nếu index không có đủ cột, cần lookup vào bảng gốc (có thể làm chậm).

### **VII. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Chọn index phù hợp:** Chọn đúng cột index (dùng những cột thường xuyên dùng để tìm kiếm).
- **Không lạm dụng index:** Quá nhiều index làm chậm các thao tác ghi (INSERT, UPDATE, DELETE).
- **Composite Index:** Dùng khi tìm kiếm trên nhiều cột.
- **Unique Index:** Dùng khi cần đảm bảo giá trị duy nhất.
- **Tối ưu hóa Query:** Viết câu query tối ưu, tránh `SELECT *`, ...
- **Theo dõi index:** Thường xuyên kiểm tra xem index có còn hiệu quả không.
- **Include column:** Trong trường hợp cần nhiều cột, nhưng chỉ có một số cột thường xuyên được dùng để tìm kiếm, ta có
  thể dùng include column để thêm các cột còn lại để tránh `Key Lookup`, ví dụ
  `CREATE INDEX idx_order_customer on Orders (customerID) INCLUDE (orderDate, TotalAmount)`.
- **Filtered Index:** Ta có thể tạo index dựa trên một điều kiện cụ thể, ví dụ như chỉ số trên các đơn hàng có trạng
  thái là "Pending", điều này sẽ làm chỉ mục nhẹ hơn và nhanh hơn cho các truy vấn chỉ tìm những đơn hàng có trạng thái
  này.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Index là "trợ thủ đắc lực" giúp bạn tăng tốc độ truy vấn trong SQL Server. Hãy sử dụng chúng một cách thông minh để có
được hiệu suất tốt nhất cho ứng dụng của mình. Chúc các bạn code thành công! 😎
