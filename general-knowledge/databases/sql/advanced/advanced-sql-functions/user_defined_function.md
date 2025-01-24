## **🚀 "GIẢI MÃ" USER-DEFINED FUNCTIONS (UDFs): "HÀM RIÊNG" TRONG SQL SERVER CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm rất quan trọng trong SQL Server:
User-Defined Functions (Hàm do người dùng định nghĩa). Đây là một "chiêu thức" giúp bạn tạo ra các "hàm riêng" để tái sử
dụng logic tính toán và mở rộng khả năng của SQL. Cùng mình "mổ xẻ" nó nhé!

### **I. USER-DEFINED FUNCTIONS (UDFs) LÀ GÌ? (NHƯ "HÀM RIÊNG" TRONG SQL)**

- **User-Defined Functions (UDFs):** Là các hàm do người dùng _tự định nghĩa_ (tự viết) trong SQL Server để thực hiện
  một nhiệm vụ cụ thể.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn tự tạo một "công cụ" trong phần mềm: bạn tạo ra công cụ đó, và sau đó dùng nó để làm việc.
- **Quan trọng vì:**
    - **Tái sử dụng:** Dùng lại logic tính toán ở nhiều nơi.
    - **Mở rộng SQL:** Thêm các hàm không có sẵn trong SQL Server.
    - **Đơn giản hóa:** Làm code dễ đọc và dễ bảo trì hơn.
    - **Tối ưu:** Có thể tối ưu các thao tác phức tạp.

### **II. CÁCH TẠO UDFs (CÁCH "CHẾ TẠO CÔNG CỤ")**

```sql
CREATE FUNCTION function_name (
    @parameter1 datatype,
    @parameter2 datatype,
    ...
)
RETURNS datatype
AS
BEGIN
    -- Câu lệnh SQL
    RETURN value;
END;
```

- **`CREATE FUNCTION function_name`:** Tạo hàm với tên `function_name`.
- **`(@parameter1 datatype, ...)`:** Các tham số đầu vào (nếu có).
- **`RETURNS datatype`:** Kiểu dữ liệu trả về của hàm.
- **`AS BEGIN ... END`:** Nội dung của hàm (code SQL).
- **`RETURN value`:** Trả về giá trị của hàm.

### **III. CÁC LOẠI UDFs (NHIỀU LOẠI "CÔNG CỤ")**

1. **Scalar Functions (Hàm vô hướng):**
    - Trả về _một giá trị đơn_.
    - Thường dùng để tính toán hoặc xử lý dữ liệu.
2. **Table-Valued Functions (Hàm trả về bảng):**
    - Trả về _một bảng_.
    - Thường dùng để lọc dữ liệu hoặc dùng trong `JOIN`.
        - **Inline Table-Valued Functions:** Chỉ có một câu lệnh `SELECT` trong thân hàm.
        - **Multi-statement Table-Valued Functions:** Có nhiều câu lệnh SQL, và dùng biến bảng.

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

#### **1. SCALAR FUNCTION (TÍNH TUỔI TỪ NGÀY SINH):**

```sql
CREATE FUNCTION dbo.CalculateAge (@BirthDate DATE)
RETURNS INT
AS
BEGIN
    DECLARE @Age INT;
    SET @Age = DATEDIFF(year, @BirthDate, GETDATE());
    RETURN @Age;
END;
```

- **Giải thích:**
    - Tạo hàm tên `CalculateAge` nhận `BirthDate` và trả về tuổi (kiểu `INT`).
    - Dùng hàm `DATEDIFF` để tính tuổi (năm hiện tại trừ năm sinh).
- **Dùng:**

```sql
SELECT FirstName, LastName, dbo.CalculateAge(BirthDate) AS Age
FROM Employees;
```

#### **2. INLINE TABLE-VALUED FUNCTION (LẤY NHÂN VIÊN THEO PHÒNG BAN):**

```sql
CREATE FUNCTION dbo.GetEmployeesByDepartment (@Department VARCHAR(100))
RETURNS TABLE
AS
RETURN
    SELECT FirstName, LastName, Email, Salary
    FROM Employees
    WHERE Department = @Department;
```

- **Giải thích:**

    - Tạo hàm `GetEmployeesByDepartment` nhận tên phòng ban và trả về danh sách nhân viên.
    - Hàm chỉ có 1 câu lệnh select trả về table.

- **Dùng:**

```sql
SELECT * FROM dbo.GetEmployeesByDepartment('HR');
```

#### **3. MULTI-STATEMENT TABLE-VALUED FUNCTION (LẤY ĐƠN HÀNG THEO THÁNG):**

```sql
CREATE FUNCTION dbo.GetOrdersByMonth (@Year INT, @Month INT)
RETURNS @OrdersTable TABLE (
    OrderID INT,
    OrderDate DATE,
    CustomerID INT
)
AS
BEGIN
    INSERT INTO @OrdersTable
    SELECT OrderID, OrderDate, CustomerID
    FROM Orders
    WHERE YEAR(OrderDate) = @Year AND MONTH(OrderDate) = @Month;
    RETURN;
END;
```

- **Giải thích:**
    - Tạo hàm `GetOrdersByMonth` nhận năm và tháng và trả về danh sách đơn hàng.
    - Dùng biến bảng (`@OrdersTable`) để lưu kết quả.
- **Dùng:**

```sql
SELECT * FROM dbo.GetOrdersByMonth(2024, 5);
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Tên rõ ràng:** Đặt tên hàm dễ hiểu (để dễ dùng).
- **Comment:** Viết comment để giải thích logic hàm.
- **Kiểm thử:** Test kỹ trước khi dùng.
- **Quyền:** Phân quyền cho người dùng được phép dùng hàm.
- **Hiệu suất:** Cẩn thận khi dùng hàm trong các query lớn (có thể ảnh hưởng đến hiệu suất).
- **Hạn chế:** Không dùng trong các trường hợp cần thay đổi dữ liệu (nên dùng stored procedure nếu cần).

### **VI. ƯU ĐIỂM CỦA UDFs (NHỮNG ĐIỂM "ĐÁNG YÊU")**

- **Tái sử dụng:** Dùng lại code SQL ở nhiều nơi.
- **Mở rộng SQL:** Thêm các chức năng mà SQL Server không có sẵn.
- **Đơn giản:** Làm query phức tạp dễ hiểu hơn.
- **Tối ưu:** Có thể tối ưu hóa các logic tính toán phức tạp.

### **VII. NHƯỢC ĐIỂM CỦA UDFs (ĐIỂM "KHÓ CHỊU")**

- **Hiệu suất:** Có thể làm chậm query (nếu viết không tốt).
- **Khó debug:** Đôi khi khó theo dõi lỗi trong UDF.
- **Không thay đổi dữ liệu:** Không dùng để thay đổi dữ liệu (như INSERT, UPDATE, DELETE) trong bảng.

### **VIII. ỨNG DỤNG (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Tính toán:** Tính toán tuổi, số ngày, giá trị, ...
- **Định dạng:** Định dạng dữ liệu (chuỗi, ngày, giờ, ...).
- **Lọc dữ liệu:** Lọc dữ liệu theo các điều kiện phức tạp.
- **Tái sử dụng logic:** Dùng lại các logic phức tạp ở nhiều nơi.

### **IX. KẾT LUẬN (TỔNG KẾT)**

User-Defined Functions (UDFs) là một công cụ mạnh mẽ giúp bạn mở rộng khả năng của SQL Server, tạo các hàm riêng để tái
sử dụng code. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về chúng và có thể áp dụng vào công việc hàng ngày. Chúc
các bạn code thành công! 😎
