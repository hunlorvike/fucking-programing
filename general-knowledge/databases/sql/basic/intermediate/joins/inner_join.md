## **🚀 "GIẢI MÃ" INNER JOIN TRONG SQL SERVER: "KẾT HỢP" DỮ LIỆU CÓ "ĐÔI" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh cực kỳ quan trọng trong SQL Server:
`INNER JOIN`. Đây là "chiêu thức" giúp bạn kết hợp dữ liệu từ hai hay nhiều bảng lại với nhau, lấy ra những bản ghi có "
liên quan". Cùng mình "mổ xẻ" nó nhé!

![Inner Join](/assets/images/sql-joins-venn-diagrams-inner-join.webp)

### **I. INNER JOIN LÀ GÌ? (KẾT HỢP DỮ LIỆU KIỂU GÌ?)**

- **`INNER JOIN`:** Là cách kết hợp các bản ghi từ 2 hay nhiều bảng dựa trên một _điều kiện khớp_.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn ghép cặp: bạn chỉ ghép các món đồ có liên quan với nhau (ví dụ: giày với tất, áo với quần).
- **Quan trọng vì:**
    - **Kết hợp dữ liệu:** Lấy thông tin từ nhiều bảng có liên quan.
    - **Lọc dữ liệu:** Chỉ lấy những bản ghi có "cặp".
    - **Phân tích:** Tổng hợp thông tin từ nhiều nguồn khác nhau.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG INNER JOIN)**

```sql
SELECT column1, column2, ...
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

- **`SELECT column1, column2, ...`:** Chọn các cột (cột dữ liệu) cần lấy.
- **`FROM table1 INNER JOIN table2 ON ...`:** Kết hợp 2 bảng với điều kiện `ON`.
- **`INNER JOIN`:** Kết nối các bản ghi có điều kiện khớp.
- **`ON table1.column = table2.column`:** Điều kiện để kết nối 2 bảng (điều kiện khớp).
- **Lưu ý:** `INNER JOIN` có thể viết tắt là `JOIN` (mặc định sẽ là INNER JOIN nếu không có gì khác).

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có 2 bảng:

- **`Employees`:** (EmployeeID, FirstName, LastName, DepartmentID)
- **`Departments`:** (DepartmentID, DepartmentName)

1. **Lấy tên nhân viên và phòng ban (có sự khớp):**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
INNER JOIN Departments d
ON e.DepartmentID = d.DepartmentID;
```

- **Giải thích:** Lấy tên nhân viên và tên phòng ban (chỉ lấy những người có phòng ban tương ứng).

2. **Lọc với `WHERE`:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
INNER JOIN Departments d
ON e.DepartmentID = d.DepartmentID
WHERE d.DepartmentName = 'HR';
```

- **Giải thích:** Lấy tên nhân viên và tên phòng ban (chỉ lấy những người thuộc phòng HR).

3. **Sắp xếp với `ORDER BY`:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
INNER JOIN Departments d
ON e.DepartmentID = d.DepartmentID
ORDER BY e.FirstName;
```

- **Giải thích:** Lấy tên nhân viên và tên phòng ban, sắp xếp theo tên nhân viên.

4. **Gộp nhóm với `GROUP BY`:**

```sql
SELECT d.DepartmentName, COUNT(e.EmployeeID) AS NumEmployees
FROM Employees e
INNER JOIN Departments d
ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;
```

- **Giải thích:** Lấy số lượng nhân viên trong từng phòng ban.

### **IV. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **`ON` cẩn thận:** Điều kiện `ON` phải chính xác, để kết hợp đúng.
- **Chỉ lấy bản ghi khớp:** Nếu không có bản ghi khớp, thì sẽ không có trong kết quả.
- **Alias:** Nên dùng alias (e, d) để code ngắn gọn dễ đọc.
- **Performance:** Nếu bảng lớn, cần chú ý đến hiệu suất (tạo index).

### **V. KẾT LUẬN (TỔNG KẾT)**

`INNER JOIN` là một cách kết hợp bảng rất quan trọng, giúp bạn lấy dữ liệu có liên quan từ nhiều bảng khác nhau. Hy vọng
qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể sử dụng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
