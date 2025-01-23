## **🚀 "GIẢI MÃ" RIGHT JOIN TRONG SQL SERVER: "KẾT NỐI" DỮ LIỆU CÓ "BÊN PHẢI" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh cũng khá thú vị trong SQL Server:
`RIGHT JOIN`. Đây là một "chiêu thức" giúp bạn kết hợp dữ liệu từ hai bảng, nhưng lần này lại "ưu tiên" lấy hết dữ liệu
từ bảng bên phải. Cùng mình "mổ xẻ" nó nhé!

![Right Join](/assets/images/sql-joins-venn-diagrams-right-outer-join.webp)

### **I. RIGHT JOIN LÀ GÌ? (KẾT HỢP DỮ LIỆU KIỂU GÌ?)**

- **`RIGHT JOIN`:** Là cách kết hợp các bản ghi từ 2 bảng, lấy _tất cả các bản ghi từ bảng bên phải_ (bảng thứ hai) và
  các bản ghi tương ứng từ bảng bên trái.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn có 2 danh sách: một danh sách phòng ban và một danh sách nhân viên. `RIGHT JOIN` sẽ lấy hết tất
      cả các phòng ban, và nếu có nhân viên nào khớp thì lấy thông tin nhân viên, còn không thì để trống.
- **Quan trọng vì:**
    - **Lấy hết dữ liệu từ bảng phải:** Đảm bảo không bỏ sót bản ghi nào từ bảng bên phải.
    - **Kết hợp có điều kiện:** Kết hợp với bảng bên trái khi có sự liên quan.
    - **Xử lý dữ liệu thiếu:** Cho thấy các bản ghi không có dữ liệu tương ứng ở bảng bên trái.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG RIGHT JOIN)**

```sql
SELECT column1, column2, ...
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

- **`SELECT column1, column2, ...`:** Chọn các cột (cột dữ liệu) cần lấy.
- **`FROM table1 RIGHT JOIN table2 ON ...`:** Kết hợp 2 bảng với điều kiện `ON`.
- **`RIGHT JOIN`:** Lấy tất cả bản ghi từ bảng bên phải.
- **`ON table1.column = table2.column`:** Điều kiện để kết nối (so khớp) 2 bảng.
- **Lưu ý:** `RIGHT JOIN` có thể viết tắt là `RIGHT OUTER JOIN`.

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có 2 bảng:

- **`Employees`:** (EmployeeID, FirstName, LastName, DepartmentID)
- **`Departments`:** (DepartmentID, DepartmentName)

#### **1. Lấy tất cả phòng ban và nhân viên (phòng ban có thể không có nhân viên):**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d
ON e.DepartmentID = d.DepartmentID;
```

- **Kết quả:** Lấy hết tất cả các phòng ban, nếu có nhân viên tương ứng thì lấy thông tin nhân viên, nếu không thì để
  `NULL`.

#### **2. Lọc với `WHERE` (chỉ lấy phòng ban không có nhân viên):**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d
ON e.DepartmentID = d.DepartmentID
WHERE e.FirstName IS NULL;
```

- **Kết quả:** Lấy các phòng ban không có nhân viên.

#### **3. Sắp xếp với `ORDER BY`:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d
ON e.DepartmentID = d.DepartmentID
ORDER BY d.DepartmentName;
```

- **Kết quả:** Sắp xếp các bản ghi theo tên phòng ban.

#### **4. Gộp nhóm với `GROUP BY`:**

```sql
SELECT d.DepartmentName, COUNT(e.EmployeeID) AS NumEmployees
FROM Employees e
RIGHT JOIN Departments d
ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;
```

- **Kết quả:** Lấy số lượng nhân viên trong từng phòng ban, bao gồm cả các phòng ban không có nhân viên.

### **IV. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Bảng bên phải luôn có:** `RIGHT JOIN` _luôn_ lấy hết dữ liệu từ bảng bên phải.
- **`NULL`:** Nếu không có bản ghi tương ứng ở bảng bên trái, sẽ có giá trị `NULL`.
- **`WHERE` cẩn thận:** Nếu dùng `WHERE` để lọc các cột của bảng trái, nên cẩn thận không sẽ bỏ qua các bản ghi không
  khớp.
- **Hiệu suất:** Nếu bảng lớn, có thể ảnh hưởng đến hiệu suất (tạo index).
- **Tương tự `LEFT JOIN`:** Có thể dùng `LEFT JOIN` và đảo 2 bảng để có kết quả tương tự.

### **V. KẾT LUẬN (TỔNG KẾT)**

`RIGHT JOIN` là một cách kết nối bảng rất hữu ích, giúp bạn lấy hết dữ liệu từ bảng bên phải và kết hợp với bảng bên
trái nếu có. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể dùng nó trong nhiều tình huống khác nhau.
Chúc các bạn code thành công! 😎
