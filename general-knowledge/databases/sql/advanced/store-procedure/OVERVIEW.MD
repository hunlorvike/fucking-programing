## **🚀 "GIẢI MÃ" STORED PROCEDURES: "HÀM" TRONG DATABASE CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm cực kỳ quan trọng trong SQL Server:
Stored Procedures (Thủ tục lưu trữ). Đây là một "chiêu thức" lợi hại giúp bạn đóng gói các câu lệnh SQL thành một "hàm"
để tái sử dụng, tăng hiệu suất và bảo mật. Cùng mình "mổ xẻ" nó nhé!

### **I. STORED PROCEDURE LÀ GÌ? (NHƯ "HÀM" TRONG DATABASE)**

- **Stored Procedure (Thủ tục lưu trữ):** Là một tập hợp các câu lệnh SQL được _lưu trữ_ trong cơ sở dữ liệu (database).
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn tạo một "macro" trong Excel: bạn ghi lại một loạt các thao tác, rồi lần sau chỉ cần gọi "macro"
      đó là thực hiện y hệt.
- **Quan trọng vì:**
    - **Tái sử dụng:** Dùng lại các câu lệnh phức tạp ở nhiều nơi.
    - **Hiệu suất:** Chạy nhanh hơn (do đã biên dịch trước).
    - **Bảo mật:** Che giấu logic database (không ai thấy code SQL bên trong).
    - **Quản lý:** Quản lý code database dễ hơn.

### **II. CÁCH TẠO STORED PROCEDURE (CÁCH "GHI MACRO")**

```sql
CREATE PROCEDURE procedure_name
    @parameter1 datatype,
    @parameter2 datatype,
    ...
AS
BEGIN
    -- Câu lệnh SQL
END;
```

- **`CREATE PROCEDURE procedure_name`:** Tạo stored procedure với tên `procedure_name`.
- **`@parameter1 datatype, ...`:** Các tham số đầu vào (nếu có).
- **`AS BEGIN ... END`:** Khối code SQL.

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

1. **Tạo stored procedure lấy thông tin nhân viên theo Department:**

```sql
CREATE PROCEDURE GetEmployeesByDepartment
    @DepartmentName VARCHAR(100)
AS
BEGIN
    SELECT FirstName, LastName, Email, Salary
    FROM Employees
    WHERE Department = @DepartmentName;
END;
```

- **Giải thích:** Tạo procedure tên `GetEmployeesByDepartment` để lấy thông tin nhân viên theo tên phòng ban (tham số).

2. **Tạo stored procedure tính tổng lương của một phòng ban:**

```sql
CREATE PROCEDURE GetTotalSalaryByDepartment
    @DepartmentName VARCHAR(100)
AS
BEGIN
    SELECT Department, SUM(Salary) AS TotalSalary
    FROM Employees
    WHERE Department = @DepartmentName
    GROUP BY Department;
END;
```

- **Giải thích:** Tạo procedure tên `GetTotalSalaryByDepartment` để tính tổng lương theo tên phòng ban.

3. **Tạo stored procedure thêm mới nhân viên:**

```sql
CREATE PROCEDURE AddNewEmployee
    @FirstName VARCHAR(100),
    @LastName VARCHAR(100),
    @Department VARCHAR(100),
    @Salary DECIMAL(10,2)
AS
BEGIN
    INSERT INTO Employees (FirstName, LastName, Department, Salary)
    VALUES (@FirstName, @LastName, @Department, @Salary);
END;
```

- **Giải thích:** Tạo procedure tên `AddNewEmployee` để thêm mới nhân viên vào bảng.

### **IV. CÁCH GỌI STORED PROCEDURE (CÁCH DÙNG "MACRO")**

```sql
EXEC procedure_name @parameter1 = value1, @parameter2 = value2, ...;
```

- **`EXEC procedure_name`:** Gọi procedure với tên `procedure_name`.
- **`@parameter1 = value1, ...`:** Truyền giá trị cho các tham số (nếu có).
- **Ví dụ:**

```sql
EXEC GetEmployeesByDepartment @DepartmentName = 'HR';
```

```sql
EXEC GetTotalSalaryByDepartment @DepartmentName = 'IT';
```

```sql
EXEC AddNewEmployee @FirstName = 'Jane', @LastName = 'Doe', @Department = 'Sales', @Salary = 6000;
```

### **V. ƯU ĐIỂM CỦA STORED PROCEDURE (ĐIỂM "ĐÁNG YÊU")**

- **Tái sử dụng:** Code một lần, dùng nhiều nơi.
- **Hiệu suất:** Chạy nhanh hơn vì đã biên dịch trước (lần đầu gọi).
- **Bảo mật:** Không để lộ code SQL cho người dùng.
- **Dễ quản lý:** Code database tập trung, dễ quản lý.

### **VI. NHƯỢC ĐIỂM CỦA STORED PROCEDURE (ĐIỂM "KHÓ CHỊU")**

- **Khó debug:** Khó debug hơn so với các câu lệnh SQL thông thường.
- **Khó quản lý phiên bản:** Cần chú ý khi có thay đổi (nhất là khi nhiều người cùng làm).

### **VII. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Tên rõ ràng:** Đặt tên procedure dễ hiểu.
- **Comment:** Viết comment cho các procedure phức tạp.
- **Kiểm thử:** Test kỹ trước khi dùng (chạy thử, kiểm tra lỗi).
- **Quyền:** Phân quyền cho người dùng được phép chạy procedure.
- **Tối ưu:** Cần tối ưu code SQL bên trong procedure.

### **VIII. ỨNG DỤNG (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Logic nghiệp vụ:** Đóng gói các nghiệp vụ phức tạp.
- **Bảo mật:** Kiểm soát quyền truy cập dữ liệu.
- **Báo cáo:** Tạo các báo cáo tổng hợp.
- **Tái sử dụng:** Dùng lại các truy vấn, các thao tác thường dùng.

### **IX. KẾT LUẬN (TỔNG KẾT)**

Stored Procedure là một công cụ mạnh mẽ giúp bạn tổ chức, bảo mật và tối ưu code database của mình. Hy vọng qua bài viết
này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày. Chúc các bạn code thành công! 😎
