## **🚀 "GIẢI MÃ" LEFT JOIN TRONG SQL SERVER: "KẾT HỢP" DỮ LIỆU CÓ "BÊN TRÁI" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh rất quan trọng trong SQL Server:
`LEFT JOIN`. Đây là một "chiêu thức" giúp bạn kết hợp dữ liệu từ hai bảng, nhưng vẫn giữ lại _tất cả_ dữ liệu từ bảng
bên trái (chưa bên phải). Cùng mình "mổ xẻ" nó nhé!

![Left Join](/assets/images/sql-joins-venn-diagrams-left-outer-join.webp)

### **I. LEFT JOIN LÀ GÌ? (KẾT HỢP DỮ LIỆU KIỂU GÌ?)**

- **`LEFT JOIN`:** Là cách kết hợp các bản ghi từ 2 bảng, lấy _tất cả các bản ghi từ bảng bên trái_ (bảng đầu tiên) và
  các bản ghi tương ứng từ bảng bên phải.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn có 2 danh sách: một danh sách nhân viên và một danh sách phòng ban. `LEFT JOIN` sẽ lấy hết tất
      cả nhân viên, và nếu có phòng ban nào khớp thì lấy tên phòng ban, còn không thì để trống.
- **Quan trọng vì:**
    - **Lấy hết dữ liệu từ bảng trái:** Đảm bảo không bỏ sót bất kỳ bản ghi nào từ bảng bên trái.
    - **Kết hợp có điều kiện:** Kết hợp với bảng bên phải khi có sự liên quan.
    - **Xử lý dữ liệu thiếu:** Cho thấy các bản ghi không có dữ liệu tương ứng ở bảng kia.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG LEFT JOIN)**

```sql
SELECT column1, column2, ...
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

- **`SELECT column1, column2, ...`:** Chọn các cột cần lấy từ các bảng.
- **`FROM table1 LEFT JOIN table2 ON ...`:** Kết hợp 2 bảng với điều kiện `ON`.
- **`LEFT JOIN`:** Lấy tất cả bản ghi từ bảng bên trái.
- **`ON table1.column = table2.column`:** Điều kiện để kết nối (so khớp) 2 bảng.
- **Lưu ý:** `LEFT JOIN` có thể viết tắt là `LEFT OUTER JOIN`.

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có 2 bảng:

- **`Employees`:** (EmployeeID, FirstName, LastName, DepartmentID)
- **`Departments`:** (DepartmentID, DepartmentName)

#### **1. Lấy tất cả nhân viên và phòng ban (nhân viên có thể không có phòng ban):**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d
ON e.DepartmentID = d.DepartmentID;
```

- **Kết quả:** Lấy tất cả nhân viên, nếu có phòng ban tương ứng thì lấy tên phòng ban, nếu không thì để `NULL`.

#### **2. Lọc với `WHERE` (chỉ lấy những nhân viên không có phòng ban):**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d
ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName IS NULL;
```

- **Kết quả:** Lấy các nhân viên không thuộc bất kỳ phòng ban nào.

#### **3. Sắp xếp với `ORDER BY`:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
LEFT JOIN Departments d
ON e.DepartmentID = d.DepartmentID
ORDER BY e.FirstName;
```

- **Kết quả:** Sắp xếp các nhân viên theo tên.

#### **4. Gộp nhóm với `GROUP BY`:**

```sql
SELECT d.DepartmentName, COUNT(e.EmployeeID) AS NumEmployees
FROM Employees e
LEFT JOIN Departments d
ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;
```

- **Kết quả:** Lấy số lượng nhân viên trong từng phòng ban, và cả những người không thuộc phòng ban nào.

### **IV. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Bảng bên trái luôn có:** `LEFT JOIN` _luôn_ lấy hết dữ liệu từ bảng bên trái.
- **`NULL`:** Nếu không có bản ghi tương ứng ở bảng bên phải, sẽ có giá trị `NULL`.
- **`WHERE` cẩn thận:** Nếu dùng `WHERE` để lọc các cột của bảng phải, nên cẩn thận không sẽ thành `INNER JOIN`.
- **Hiệu suất:** Nếu bảng lớn, có thể ảnh hưởng đến hiệu suất (tạo index).

### **V. KẾT LUẬN (TỔNG KẾT)**

`LEFT JOIN` là một cách kết nối bảng rất hữu ích, giúp bạn lấy hết dữ liệu từ bảng bên trái và kết hợp với bảng bên phải
nếu có. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể dùng nó trong nhiều tình huống khác nhau. Chúc
các bạn code thành công! 😎
