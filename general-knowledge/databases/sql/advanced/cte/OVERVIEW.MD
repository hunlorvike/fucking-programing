## **🚀 "GIẢI MÃ" CTE (COMMON TABLE EXPRESSIONS) TRONG SQL SERVER: "TRUY VẤN TẠM" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm rất quan trọng trong SQL Server: Common Table Expressions (CTE). Nghe có vẻ "lạ tai" nhưng thực ra rất hữu ích khi bạn cần viết các query phức tạp. Cùng mình "mổ xẻ" nó nhé!

### **I. CTE (COMMON TABLE EXPRESSIONS) LÀ GÌ? (NHƯ "BẢNG TẠM" TRONG QUERY)**

-   **CTE (Common Table Expressions):** Là một _tập kết quả tạm thời_ được định nghĩa trong một câu lệnh SQL, và có thể được tham chiếu đến trong câu lệnh đó.
-   **Nó hoạt động như thế nào?**
    -   Giống như khi bạn tạo một biến tạm để lưu kết quả tính toán: bạn có thể dùng biến tạm đó trong các công thức tính tiếp theo.
-   **Quan trọng vì:**
    -   **Chia nhỏ:** Chia nhỏ truy vấn phức tạp thành các phần nhỏ hơn, dễ đọc hơn.
    -   **Tái sử dụng:** Dùng lại logic tính toán ở nhiều nơi.
    -   **Đệ quy:** Cho phép tạo các truy vấn đệ quy (ví dụ: tìm cấp bậc nhân viên trong công ty).

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG CTE)**

```sql
WITH cte_name AS (
    SELECT column1, column2, ...
    FROM table_name
    WHERE condition
)
SELECT column1, column2, ...
FROM cte_name
WHERE condition;
```

-   **`WITH cte_name AS (...)`:** Tạo CTE với tên `cte_name`, bên trong là câu truy vấn `SELECT`.
-   **`SELECT column1, column2, ... FROM cte_name`:** Sử dụng CTE `cte_name` trong truy vấn chính.
-   **`WHERE condition`:** Các điều kiện lọc (nếu cần).

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có bảng:

-   **`Employees`:** (EmployeeID, FirstName, LastName, Department, Salary)

#### **1. CTE ĐƠN GIẢN (LẤY TÊN VÀ LƯƠNG NHÂN VIÊN PHÒNG IT):**

```sql
WITH IT_Employees AS (
    SELECT FirstName, LastName, Salary
    FROM Employees
    WHERE Department = 'IT'
)
SELECT *
FROM IT_Employees;
```

-   **Giải thích:**
    -   Tạo CTE `IT_Employees` để lấy thông tin nhân viên phòng IT.
    -   Dùng `SELECT * FROM IT_Employees` để lấy dữ liệu từ CTE.

#### **2. CTE DÙNG TRONG JOIN (LẤY TÊN NHÂN VIÊN VÀ LƯƠNG TRUNG BÌNH THEO PHÒNG BAN):**

```sql
WITH AvgSalaryByDepartment AS (
    SELECT Department, AVG(Salary) AS AvgSalary
    FROM Employees
    GROUP BY Department
)
SELECT e.FirstName, e.LastName, a.AvgSalary
FROM Employees e
JOIN AvgSalaryByDepartment a
ON e.Department = a.Department;
```

-   **Giải thích:**
    -   Tạo CTE `AvgSalaryByDepartment` để tính lương trung bình của từng phòng ban.
    -   Dùng `JOIN` để kết hợp thông tin nhân viên và lương trung bình.

#### **3. CTE ĐỆ QUY (TÌM CẤP DƯỚI CỦA MỘT NHÂN VIÊN):**

Giả sử ta có bảng `EmployeeHierarchy` (EmployeeID, ManagerID, EmployeeName), trong đó ManagerID chỉ ra người quản lý trực tiếp.

```sql
WITH EmployeeHierarchyCTE AS (
    SELECT EmployeeID, ManagerID, EmployeeName, 0 AS Level
    FROM EmployeeHierarchy
    WHERE EmployeeID = 100 -- EmployeeID cần tìm
    UNION ALL
    SELECT e.EmployeeID, e.ManagerID, e.EmployeeName, Level + 1
    FROM EmployeeHierarchy e
    INNER JOIN EmployeeHierarchyCTE c ON e.ManagerID = c.EmployeeID
)
SELECT EmployeeID, EmployeeName, Level
FROM EmployeeHierarchyCTE
ORDER BY Level;
```

-   **Giải thích:**
    -   Tạo CTE đệ quy `EmployeeHierarchyCTE` để tìm tất cả các cấp dưới của nhân viên có `EmployeeID = 100`.
    -   Phần đầu (anchor) chọn nhân viên có ID là 100, Level = 0.
    -   Phần đệ quy chọn các nhân viên là cấp dưới dựa trên `ManagerID`.
    -   Dùng `UNION ALL` để kết hợp kết quả của cả phần anchor và phần đệ quy.

### **IV. ƯU ĐIỂM CỦA CTE (NHỮNG ĐIỂM "ĐÁNG YÊU")**

-   **Dễ đọc:** Chia nhỏ query phức tạp thành các phần nhỏ dễ hiểu.
-   **Tái sử dụng:** Dùng lại CTE ở nhiều nơi trong cùng một query.
-   **Đệ quy:** Có thể dùng để tạo truy vấn đệ quy (tính toán theo cấp).
-   **Thay thế View:** Đôi khi dùng CTE thay vì tạo view (nếu chỉ dùng trong query hiện tại).

### **V. NHƯỢC ĐIỂM CỦA CTE (ĐIỂM "KHÓ CHỊU")**

-   **Chỉ dùng trong 1 query:** CTE chỉ tồn tại trong câu query hiện tại.
-   **Không có chỉ mục:** Không tạo được index cho CTE.
-   **Phức tạp hơn khi mới làm quen:** Có thể mất thời gian để làm quen với CTE đệ quy.

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

-   **Đặt tên rõ ràng:** Đặt tên CTE dễ hiểu, mô tả được mục đích.
-   **Dùng khi cần thiết:** Không nên dùng CTE quá nhiều, làm query khó đọc.
-   **Khi dùng đệ quy:** Cần có điểm dừng, để tránh vòng lặp vô hạn.
-   **Hiệu suất:** Có thể không cải thiện hiệu suất (chỉ giúp code dễ hiểu).

### **VII. KẾT LUẬN (TỔNG KẾT)**

CTE là một công cụ mạnh mẽ giúp bạn viết các truy vấn phức tạp một cách dễ dàng hơn trong SQL Server. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày. Chúc các bạn code thành công! 😎
