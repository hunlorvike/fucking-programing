## **🚀 "GIẢI MÃ" FULL JOIN TRONG SQL SERVER: "KẾT HỢP" DỮ LIỆU ĐỦ CẢ HAI BÊN CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh rất thú vị trong SQL Server: `FULL JOIN`.
Đây là một "chiêu thức" giúp bạn kết hợp dữ liệu từ hai bảng, lấy hết tất cả các bản ghi, không bỏ sót ai. Cùng mình "mổ

![Full join](/assets/images/sql-joins-venn-diagrams-full-outer-join.webp)

### **I. FULL JOIN LÀ GÌ? (KẾT HỢP DỮ LIỆU KIỂU GÌ?)**

- **`FULL JOIN`:** Là kiểu kết nối bảng trong SQL, dùng để _lấy tất cả các bản ghi_ từ _cả hai bảng_, bất kể có khớp
  nhau hay không.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn so sánh 2 danh sách: bạn lấy hết các món đồ từ cả 2 danh sách, nếu có món nào ở danh sách này
      không có ở danh sách kia, thì để trống chỗ đó.
- **Quan trọng vì:**
    - **Lấy hết dữ liệu:** Lấy tất cả thông tin từ cả 2 bảng (dù có khớp hay không).
    - **So sánh:** So sánh sự khác biệt giữa 2 bảng (thấy những gì "thiếu" của nhau).
    - **Báo cáo:** Tạo báo cáo đầy đủ, không bỏ sót dữ liệu.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG FULL JOIN)**

```sql
SELECT column1, column2, ...
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;
```

- **`SELECT column1, column2, ...`:** Chọn các cột cần lấy.
- **`FROM table1 FULL OUTER JOIN table2 ON ...`:** Kết hợp 2 bảng với điều kiện `ON`.
- **`FULL OUTER JOIN`:** Lấy tất cả bản ghi từ cả 2 bảng.
- **`ON table1.column = table2.column`:** Điều kiện để kết nối 2 bảng.
- **Ví dụ:**

```sql
 SELECT e.FirstName, e.LastName, d.DepartmentName
  FROM Employees e
  FULL OUTER JOIN Departments d
  ON e.DepartmentID = d.DepartmentID;
```

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có 2 bảng:

- **`Employees`:** (EmployeeID, FirstName, LastName, DepartmentID)
- **`Departments`:** (DepartmentID, DepartmentName)

#### **1. Lấy tất cả nhân viên và phòng ban:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
FULL OUTER JOIN Departments d
ON e.DepartmentID = d.DepartmentID;
```

- **Kết quả:** Lấy hết tất cả nhân viên, và tất cả phòng ban. Nếu có nhân viên không có phòng ban (hoặc ngược lại), các
  cột tương ứng sẽ hiển thị `NULL`.

#### **2. Lọc kết quả với `WHERE`:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
FULL OUTER JOIN Departments d
ON e.DepartmentID = d.DepartmentID
WHERE e.FirstName IS NULL OR d.DepartmentName IS NULL;
```

- **Kết quả:** Lấy các bản ghi mà hoặc `FirstName` hoặc `DepartmentName` là `NULL`.

#### **3. Sắp xếp kết quả với `ORDER BY`:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
FULL OUTER JOIN Departments d
ON e.DepartmentID = d.DepartmentID
ORDER BY e.FirstName;
```

- **Kết quả:** Sắp xếp các bản ghi theo `FirstName`.

#### **4. Gộp nhóm kết quả với `GROUP BY`:**

```sql
SELECT d.DepartmentName, COUNT(e.EmployeeID) AS NumEmployees
FROM Employees e
FULL OUTER JOIN Departments d
ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;
```

- **Kết quả:** Lấy số lượng nhân viên trong từng phòng ban (kể cả các phòng ban không có nhân viên).

### **IV. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **`NULL`:** Kết quả có thể chứa nhiều giá trị `NULL` (vì lấy hết từ cả 2 bảng).
- **Hiệu suất:** Nếu 2 bảng lớn, query có thể chậm, nên cân nhắc kỹ khi dùng.
- **Thường ít dùng:** Thường chỉ dùng khi thật sự cần lấy hết dữ liệu từ cả 2 bảng.
- **Cẩn thận với các điều kiện:** Nếu lọc bằng `WHERE` cẩn thận không sẽ loại hết cả kết quả.

### **V. KẾT LUẬN (TỔNG KẾT)**

`FULL JOIN` là một cách kết nối bảng đặc biệt, giúp bạn lấy hết dữ liệu từ 2 bảng (dù khớp hay không). Hy vọng qua bài
viết này, các bạn đã hiểu rõ hơn về nó và có thể sử dụng nó một cách hợp lý. Chúc các bạn code thành công! 😎
