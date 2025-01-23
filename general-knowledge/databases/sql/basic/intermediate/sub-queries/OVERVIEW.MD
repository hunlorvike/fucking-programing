## **🚀 "GIẢI MÃ" SUBQUERY TRONG SQL SERVER: "QUERY CON" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm cực kỳ quan trọng và hay dùng trong SQL
Server: Subquery (Truy vấn con). Đây là một "chiêu thức" giúp bạn làm những điều phức tạp với database bằng cách "lồng"
một truy vấn vào trong một truy vấn khác. Cùng mình "mổ xẻ" nó nhé!

### **I. SUBQUERY LÀ GÌ? (TRUY VẤN LỒNG TRONG QUERY)**

- **Subquery (Truy vấn con):** Là một câu lệnh `SELECT` được _lồng bên trong_ một câu lệnh SQL khác.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn làm một bài toán lớn, bạn cần phải giải quyết các bài toán nhỏ trước (bài toán con), rồi mới
      dùng kết quả của bài toán nhỏ để giải bài toán lớn (truy vấn chính).
- **Quan trọng vì:**
    - **Linh hoạt:** Tạo ra các truy vấn phức tạp, mạnh mẽ hơn.
    - **Giảm code:** Thay vì viết nhiều câu lệnh, dùng subquery để làm trong 1 câu lệnh.
    - **Tái sử dụng:** Có thể dùng lại subquery ở nhiều nơi.

### **II. CÁCH DÙNG SUBQUERY (LỒNG "QUERY" VÀO "QUERY")**

#### **2.1. SUBQUERY TRONG `SELECT` (TẠO CỘT TÍNH TOÁN)**

```sql
SELECT column1, column2, (SELECT some_value FROM some_table WHERE condition) AS calculated_column
FROM table_name;
```

- Subquery trả về _một giá trị_, dùng để tạo cột tính toán.
- **Ví dụ:** Tính số lượng nhân viên trong mỗi phòng ban:

```sql
SELECT name, salary,
    (SELECT COUNT(*) FROM Employees e WHERE e.DepartmentID = d.DepartmentID) AS NumEmployees
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```

#### **2.2. SUBQUERY TRONG `WHERE` (LỌC DỰA TRÊN KẾT QUẢ QUERY KHÁC)**

```sql
SELECT column1, column2, ...
FROM table_name
WHERE column_name IN/=/</>/... (SELECT ... FROM another_table WHERE condition);
```

- Subquery dùng để _lọc_ dữ liệu, trả về một giá trị hoặc tập hợp các giá trị.
- **Ví dụ:** Lấy nhân viên ở phòng ban IT:

```sql
SELECT name, salary
FROM Employees
WHERE DepartmentID = (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'IT');
```

#### **2.3. SUBQUERY TRONG `FROM` (TẠO BẢNG TẠM)**

```sql
SELECT column1, column2, ...
FROM (SELECT ... FROM another_table WHERE ...) AS subquery_alias
WHERE condition;
```

- Subquery tạo ra một _bảng tạm_ (table) cho truy vấn chính dùng.
- **Ví dụ:** Tính lương trung bình cho từng phòng ban:

```sql
SELECT DepartmentID, AVG(Salary) AS AvgSalary
FROM (SELECT DepartmentID, Salary FROM Employees) AS Sub
GROUP BY DepartmentID;
```

### **III. CÁC LOẠI SUBQUERY (CÓ NHIỀU "KIỂU" LỒNG)**

1. **Subquery tương đương:** Trả về _một giá trị_ (thường dùng với `=`, `>`, `<`, ...).
2. **Subquery trả về 1 giá trị:** Trả về _một giá trị duy nhất_.
3. **Subquery trả về nhiều giá trị:** Trả về _một tập hợp giá trị_ (dùng với `IN`, `ANY`, `ALL`).
4. **Subquery trả về bảng:** Trả về _một bảng_ (dùng trong `FROM`).

### **IV. KẾT HỢP SUBQUERY (DÙNG "COMBO" CÁC "CHIÊU")**

#### **4.1. SUBQUERY VỚI `IN` (KIỂM TRA CÓ TRONG TẬP HỢP)**

```sql
SELECT name, salary
FROM Employees
WHERE DepartmentID IN (SELECT DepartmentID FROM Departments WHERE DepartmentName IN ('HR', 'IT'));
```

#### **4.2. SUBQUERY VỚI `EXISTS` (KIỂM TRA TỒN TẠI)**

```sql
SELECT name, salary
FROM Employees e
WHERE EXISTS (SELECT 1 FROM Departments d WHERE e.DepartmentID = d.DepartmentID AND d.DepartmentName = 'HR');
```

#### **4.3. SUBQUERY VỚI `JOIN` (KẾT HỢP DỮ LIỆU)**

```sql
SELECT e.name, e.salary
FROM Employees e
JOIN (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'HR') d
ON e.DepartmentID = d.DepartmentID;
```

### **V. VÍ DỤ THỰC TẾ (XEM "THỰC HÀNH")**

1. **Lấy nhân viên lương cao nhất:**

```sql
SELECT name, salary
FROM Employees
WHERE salary = (SELECT MAX(salary) FROM Employees);
```

2. **Lấy nhân viên ở phòng ban HR hoặc IT:**

```sql
SELECT name, salary
FROM Employees
WHERE DepartmentID IN (SELECT DepartmentID FROM Departments WHERE DepartmentName IN ('HR', 'IT'));
```

3. **Lấy nhân viên có phòng ban HR (dùng EXISTS):**

```sql
SELECT name, salary
FROM Employees e
WHERE EXISTS (SELECT 1 FROM Departments d WHERE e.DepartmentID = d.DepartmentID AND d.DepartmentName = 'HR');
```

4. **Lấy tên và lương nhân viên, kết hợp với tên phòng ban (dùng JOIN với subquery):**

```sql
SELECT e.name, e.salary
FROM Employees e
JOIN (SELECT DepartmentID FROM Departments WHERE DepartmentName = 'HR') d
ON e.DepartmentID = d.DepartmentID;
```

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Hiệu suất:** Subquery có thể làm chậm query (nhất là khi subquery trả về nhiều dữ liệu).
- **Độ phức tạp:** Subquery có thể làm code khó hiểu (tránh lồng quá nhiều).
- **Dùng khi cần thiết:** Không nên dùng subquery khi có cách khác đơn giản hơn (ví dụ: dùng `JOIN` thay vì subquery).
- **Index:** Có thể cần index để subquery chạy nhanh hơn.
- **Xem Execution Plan:** Dùng Execution Plan để kiểm tra tốc độ subquery.

### **VII. KẾT LUẬN (TỔNG KẾT)**

Subquery là một công cụ rất hữu ích giúp bạn tạo ra các truy vấn phức tạp và linh hoạt hơn trong SQL Server. Hy vọng qua
bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày của mình. Chúc các bạn code thành
công! 😎
