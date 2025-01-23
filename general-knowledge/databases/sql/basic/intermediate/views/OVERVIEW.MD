## **🚀 "GIẢI MÃ" VIEW TRONG SQL SERVER: "GÓC NHÌN" DỮ LIỆU CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm rất quan trọng trong SQL Server: View (
khung nhìn). Đây là một công cụ giúp bạn tạo ra các "góc nhìn" tùy chỉnh trên dữ liệu, giúp bạn truy vấn dễ dàng, bảo
mật tốt hơn. Cùng mình "mổ xẻ" nó nhé!

### **I. VIEW LÀ GÌ? (NHƯ "KÍNH LỌC" DỮ LIỆU)**

- **View (Khung nhìn):** Là một đối tượng trong SQL Server, được tạo ra từ một câu lệnh `SELECT` (thực chất là một truy
  vấn).
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn nhìn qua một chiếc kính: bạn chỉ thấy những gì bạn muốn thấy (lọc, sắp xếp, ...).
- **Quan trọng vì:**
    - **Đơn giản:** Giúp truy vấn phức tạp trở nên đơn giản hơn.
    - **Bảo mật:** Che giấu một số thông tin nhạy cảm.
    - **Tái sử dụng:** Dùng lại các truy vấn phức tạp nhiều lần.

### **II. CÁCH TẠO VIEW (CÁCH "LÀM KÍNH LỌC")**

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- **`CREATE VIEW view_name AS`:** Tạo view với tên `view_name`.
- **`SELECT column1, column2, ... FROM table_name`:** Câu truy vấn để tạo view.
- **`WHERE condition`:** Điều kiện lọc dữ liệu (nếu cần).

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

#### **1. TẠO VIEW LẤY THÔNG TIN NHÂN VIÊN PHÒNG HR:**

```sql
CREATE VIEW HR_Employees AS
SELECT FirstName, LastName, Email, Salary
FROM Employees
WHERE Department = 'HR';
```

- **Giải thích:** Tạo view `HR_Employees` chứa thông tin nhân viên phòng HR.
- **Dùng:**

```sql
SELECT * FROM HR_Employees;
```

#### **2. TẠO VIEW TÍNH LƯƠNG TRUNG BÌNH THEO PHÒNG BAN:**

```sql
CREATE VIEW DepartmentAvgSalary AS
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department;
```

- **Giải thích:** Tạo view `DepartmentAvgSalary` chứa lương trung bình của các phòng ban.
- **Dùng:**

```sql
SELECT * FROM DepartmentAvgSalary;
```

#### **3. TẠO VIEW DÙNG JOIN:**

```sql
CREATE VIEW EmployeeDetails AS
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees AS e
INNER JOIN Departments AS d
ON e.DepartmentID = d.DepartmentID;
```

- **Giải thích:** Tạo view `EmployeeDetails` chứa tên nhân viên và tên phòng ban.
- **Dùng:**

```sql
SELECT * FROM EmployeeDetails;
```

### **IV. CÁC LOẠI VIEW (NHIỀU KIỂU "KÍNH LỌC")**

1. **Simple View (View đơn giản):** Dựa trên 1 bảng.
2. **Complex View (View phức tạp):** Dựa trên nhiều bảng (dùng `JOIN`), hoặc dùng hàm gộp nhóm.
3. **Materialized View (View vật chất hóa):** Lưu kết quả của query thành bảng (ít dùng trong SQL Server).

### **V. CÁC THAO TÁC VỚI VIEW (LÀM GÌ VỚI "KÍNH LỌC"?)**

1. **`SELECT`:** Dùng để lấy dữ liệu từ view.

   ```sql
   SELECT * FROM HR_Employees;
   ```

2. **`UPDATE`:** Cập nhật dữ liệu qua view (có giới hạn).

   ```sql
   UPDATE HR_Employees
   SET Salary = 6500
   WHERE FirstName = 'John';
   ```

3. **`INSERT`:** Chèn dữ liệu qua view (có giới hạn).

   ```sql
   INSERT INTO HR_Employees (FirstName, LastName, Email, Salary)
   VALUES ('New', 'User', 'newuser@example.com', 5000);
   ```

4. **`DELETE`:** Xóa dữ liệu qua view (có giới hạn).

   ```sql
   DELETE FROM HR_Employees
   WHERE FirstName = 'John';
   ```

5. **`DROP`:** Xóa view.

```sql
DROP VIEW HR_Employees;
```

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **View là query:** View không lưu trữ dữ liệu thực, mà chỉ lưu trữ query.
- **Cập nhật có giới hạn:** Không phải lúc nào cũng có thể `UPDATE`, `INSERT`, `DELETE` qua view.
- **Không dùng `ORDER BY` trong view:** (trừ khi dùng `TOP`, `OFFSET`).
- **Tên rõ ràng:** Đặt tên view rõ ràng, dễ hiểu.
- **Tài liệu hóa:** Viết comment hoặc tài liệu cho các view quan trọng.

### **VII. ỨNG DỤNG (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Đơn giản hóa query:** Dùng lại các query phức tạp.
- **Bảo mật:** Che giấu thông tin nhạy cảm.
- **Tái cấu trúc:** Dễ thay đổi cấu trúc bảng mà không ảnh hưởng đến các query.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

View là một công cụ rất hữu ích giúp bạn quản lý và truy vấn dữ liệu một cách hiệu quả. Hy vọng qua bài viết này, các
bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày của mình. Chúc các bạn code thành công! 😎
