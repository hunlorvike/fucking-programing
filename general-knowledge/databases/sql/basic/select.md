Tuyệt vời! Chúng ta sẽ cùng nhau "mổ xẻ" câu lệnh `SELECT` trong SQL Server, một trong những câu lệnh quan trọng nhất
trong thế giới SQL. Mình sẽ trình bày theo phong cách sinh viên, dễ hiểu, có thêm ví dụ trực quan và mẹo nhỏ để các bạn
dễ nắm bắt hơn nhé!

---

## **🚀 "GIẢI MÃ" CÂU LỆNH SELECT TRONG SQL SERVER: "LẤY" DỮ LIỆU TỪ "KHO" CỦA BẠN 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh cực kỳ quan trọng trong SQL Server:
`SELECT`. Đây là câu lệnh giúp bạn lấy dữ liệu từ database, như kiểu bạn đi "lấy đồ" trong kho dữ liệu của mình vậy.
Cùng mình "mổ xẻ" nó nhé!

### **I. CÂU LỆNH SELECT LÀ GÌ? (LẤY DỮ LIỆU TỪ "KHO")**

* **`SELECT`:** Là câu lệnh SQL dùng để *lấy dữ liệu* từ một hoặc nhiều bảng trong cơ sở dữ liệu.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn đi lấy đồ trong tủ: bạn chọn tủ (bảng), và lấy ra những món đồ (dữ liệu) bạn muốn.
* **Quan trọng vì:**
    * **Xem dữ liệu:** Lấy thông tin để xem, hiển thị, phân tích, ...
    * **Lọc dữ liệu:** Chọn ra dữ liệu phù hợp với yêu cầu.
    * **Báo cáo:** Tạo báo cáo dựa trên dữ liệu trong database.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG SELECT)**

#### **2.1. LẤY DỮ LIỆU TỪ MỘT BẢNG (LẤY "ĐỒ" TỪ MỘT TỦ)**

```sql
SELECT column1, column2, ...
FROM table_name;
```

* **`SELECT column1, column2, ...`:** Chọn các cột (cột dữ liệu) cần lấy.
* **`FROM table_name`:** Chọn bảng chứa dữ liệu.
* **Ví dụ:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees;
```

#### **2.2. LẤY TẤT CẢ DỮ LIỆU (LẤY HẾT "ĐỒ" TRONG TỦ)**

```sql
SELECT *
FROM table_name;
```

* **`SELECT *`:** Chọn *tất cả* các cột.
* **`FROM table_name`:** Chọn bảng chứa dữ liệu.
* **Ví dụ:**

```sql
SELECT *
FROM Employees;
```

### **III. CÁC TÙY CHỌN MỞ RỘNG (CÁC "CHIÊU" LẤY DỮ LIỆU)**

#### **3.1. `WHERE` (LẤY DỮ LIỆU CÓ ĐIỀU KIỆN)**

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

* **`WHERE condition`:** Điều kiện lọc dữ liệu (chỉ lấy dữ liệu thỏa mãn).
* **Ví dụ:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Department = 'HR';
```

#### **3.2. `ORDER BY` (SẮP XẾP KẾT QUẢ)**

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 ASC/DESC;
```

* **`ORDER BY column1 ASC/DESC`:** Sắp xếp theo cột 1 theo thứ tự tăng dần (ASC) hoặc giảm dần (DESC).
* **Ví dụ:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees
ORDER BY Salary DESC;
```

#### **3.3. `LIMIT` hoặc `TOP` (LẤY MỘT SỐ LƯỢNG NHẤT ĐỊNH)**

* `LIMIT` (trong MySQL, PostgreSQL,...):

```sql
SELECT column1, column2, ...
FROM table_name
LIMIT n;
```

* `TOP` (trong SQL Server):

```sql
SELECT TOP (n) column1, column2, ...
FROM table_name;
```

* **Ví dụ:**

```sql
SELECT TOP (5) FirstName, LastName, Salary
FROM Employees
ORDER BY Salary DESC;
```

#### **3.4. `JOIN` (LẤY DỮ LIỆU TỪ NHIỀU BẢNG)**

```sql
SELECT table1.column1, table2.column2, ...
FROM table1
JOIN table2
ON table1.column = table2.column;
```

* **`JOIN table2 ON ...`:** Kết nối 2 bảng theo điều kiện.
* Có nhiều kiểu `JOIN`: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`, ...
* **Ví dụ:**

```sql
SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

#### **3.5. `GROUP BY` (GOM NHÓM DỮ LIỆU)**

```sql
SELECT column1, COUNT(*), SUM(column2), ...
FROM table_name
GROUP BY column1;
```

* **`GROUP BY column1`:** Nhóm các dòng có cùng giá trị ở cột 1.
* Dùng với các hàm gộp nhóm (`COUNT()`, `SUM()`, `AVG()`, ...).
* **Ví dụ:**

```sql
SELECT Department, COUNT(*) AS TotalEmployees, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department;
```

#### **3.6. `HAVING` (LỌC DỮ LIỆU SAU KHI GOM NHÓM)**

```sql
SELECT column1, COUNT(*), SUM(column2), ...
FROM table_name
GROUP BY column1
HAVING condition;
```

* **`HAVING condition`:** Lọc các nhóm sau khi đã gom nhóm.
* **Ví dụ:**

```sql
SELECT Department, COUNT(*) AS TotalEmployees
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5;
```

### **IV. VÍ DỤ THỰC TẾ (XEM "THỰC HÀNH")**

1. **Lấy tên và lương của tất cả nhân viên:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees;
```

2. **Lấy tất cả thông tin của nhân viên:**

```sql
SELECT *
FROM Employees;
```

3. **Lấy tên và lương của nhân viên phòng HR:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Department = 'HR';
```

4. **Lấy 5 nhân viên có lương cao nhất:**

```sql
SELECT TOP (5) FirstName, LastName, Salary
FROM Employees
ORDER BY Salary DESC;
```

5. **Lấy tên nhân viên và tên phòng ban:**

```sql
SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
FROM Employees
INNER JOIN Departments
ON Employees.DepartmentID = Departments.DepartmentID;
```

6. **Lấy số lượng và lương trung bình của mỗi phòng ban:**

```sql
SELECT Department, COUNT(*) AS TotalEmployees, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department;
```

7. **Lấy các phòng ban có nhiều hơn 5 nhân viên:**

```sql
SELECT Department, COUNT(*) AS TotalEmployees
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5;
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

* **`WHERE` cẩn thận:** Dùng `WHERE` để lọc dữ liệu (nếu không sẽ lấy hết dữ liệu).
* **`ORDER BY` khi cần:** Dùng khi muốn sắp xếp kết quả.
* **`LIMIT/TOP` khi cần:** Dùng khi cần lấy một số lượng bản ghi nhất định.
* **`JOIN` khi cần:** Dùng để lấy dữ liệu từ nhiều bảng.
* **`GROUP BY/HAVING` khi cần:** Dùng để gộp nhóm và lọc sau khi gộp.
* **Performance:** Đảm bảo câu query tối ưu để database chạy nhanh.

### **VI. KẾT LUẬN (TỔNG KẾT)**

`SELECT` là câu lệnh quan trọng nhất trong SQL, giúp bạn lấy và xử lý dữ liệu từ database. Hy vọng qua bài viết này, các
bạn đã hiểu rõ hơn về nó và có thể sử dụng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
