## **🚀 "GIẢI MÃ" CÂU LỆNH UPDATE TRONG SQL SERVER: SỬA DỮ LIỆU TRONG "KHO" CỦA BẠN 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh cực kỳ quan trọng trong SQL Server:
`UPDATE`. Đây là câu lệnh giúp bạn thay đổi dữ liệu đã có trong cơ sở dữ liệu của mình, rất quan trọng để duy trì và cập
nhật thông tin. Cùng mình "mổ xẻ" nó nhé!

### **I. CÂU LỆNH UPDATE LÀ GÌ? (SỬA DỮ LIỆU TRONG "KHO")**

* **`UPDATE`:** Là câu lệnh SQL dùng để *sửa đổi dữ liệu* đã có trong một bảng.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn sửa thông tin trên một thẻ thư viện: bạn tìm đúng thẻ, và sửa lại thông tin trên đó.
* **Quan trọng vì:**
    * **Thay đổi dữ liệu:** Cập nhật thông tin người dùng, sản phẩm, ...
    * **Sửa lỗi:** Sửa lại các thông tin sai trong database.
    * **Duy trì:** Quản lý dữ liệu trong cơ sở dữ liệu.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG UPDATE)**

#### **2.1. CẬP NHẬT MỘT BẢN GHI (SỬA MỘT "MÓN ĐỒ" CỤ THỂ)**

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

* **`UPDATE table_name`:** Chọn bảng cần cập nhật.
* **`SET column1 = value1, ...`:** Gán các giá trị mới cho các cột.
* **`WHERE condition`:** Điều kiện để xác định bản ghi cần cập nhật.

* **Ví dụ:**

```sql
UPDATE Employees
SET Salary = 7000
WHERE EmployeeID = 1;
```

#### **2.2. CẬP NHẬT NHIỀU BẢN GHI (SỬA NHIỀU "MÓN ĐỒ" CÙNG LÚC)**

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

* **`WHERE condition`:** Điều kiện xác định *nhiều bản ghi* cần cập nhật.
* **Ví dụ:**

```sql
UPDATE Employees
SET Department = 'Sales', Salary = 7500
WHERE Department = 'Marketing';
```

### **III. CÁC TÙY CHỌN MỞ RỘNG (CÁC "CHIÊU" NÂNG CAO)**

#### **3.1. UPDATE VỚI WHERE (SỬA CÓ "CHỌN LỌC")**

* `WHERE` là để chọn các bản ghi cần sửa.
* Nếu *không có `WHERE`*, thì sẽ cập nhật *toàn bộ* bảng.

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

* **Ví dụ:**

```sql
UPDATE Employees
SET Salary = 6000
WHERE Department = 'HR';
```

#### **3.2. UPDATE VỚI JOIN (SỬA DỰA TRÊN THÔNG TIN TỪ BẢNG KHÁC)**

```sql
UPDATE table1
SET table1.column1 = table2.column1, ...
FROM table1
JOIN table2
ON table1.column = table2.column
WHERE condition;
```

* **`FROM table1 JOIN table2 ON ...`:** Kết nối hai bảng.
* **`SET table1.column1 = table2.column1, ...`:** Cập nhật giá trị dựa trên bảng khác.
* **`WHERE condition`:** Điều kiện lọc dữ liệu.
* **Ví dụ:**

```sql
UPDATE Employees
SET Employees.Salary = Departments.Budget / Employees.NumEmployees
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = 'IT';
```

### **IV. VÍ DỤ THỰC TẾ (XEM "THỰC HÀNH")**

1. **Cập nhật lương 1 nhân viên:**

```sql
UPDATE Employees
SET Salary = 8000
WHERE EmployeeID = 2;
```

2. **Cập nhật lương tất cả nhân viên trong một phòng ban:**

```sql
UPDATE Employees
SET Salary = Salary + 1000
WHERE Department = 'Sales';
```

3. **Cập nhật lương dựa trên bảng khác (JOIN):**

```sql
UPDATE Employees
SET Employees.Salary = Departments.Budget / Employees.NumEmployees
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = 'HR';
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

* **`WHERE` cẩn thận:** Nếu không có `WHERE` hoặc dùng sai, sẽ cập nhật *toàn bộ* bảng (gây lỗi).
* **Kiểm tra trước:** Dùng `SELECT` trước để xem bản ghi nào sẽ bị ảnh hưởng.
* **Transactions:** Dùng `BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK` khi update quan trọng (để có thể undo).
* **Hiệu suất:** Nếu update nhiều, dùng index, tối ưu code SQL.

### **VI. KẾT LUẬN (TỔNG KẾT)**

`UPDATE` là câu lệnh rất quan trọng để chỉnh sửa dữ liệu trong SQL Server. Hy vọng qua bài viết này, các bạn đã hiểu rõ
hơn về nó và có thể dùng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
