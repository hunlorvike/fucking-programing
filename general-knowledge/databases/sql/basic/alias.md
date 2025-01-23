## **🚀 "GIẢI MÃ" ALIAS TRONG SQL SERVER: "BÍ DANH" CHO CỘT VÀ BẢNG CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một khái niệm rất thú vị và hữu ích trong SQL Server:
Alias (bí danh). Đây là một "mẹo" nhỏ giúp code SQL của bạn dễ đọc, dễ hiểu và chuyên nghiệp hơn. Cùng mình "mổ xẻ" nó
nhé!

### **I. ALIAS LÀ GÌ? (NHƯ "BÍ DANH" NGOÀI ĐỜI)**

- **Alias (Bí danh):** Là một tên tạm thời (tên gọi khác) mà bạn gán cho một cột hoặc một bảng trong SQL.
- **Nó hoạt động như thế nào?**
    - Giống như bạn gọi một người bằng "biệt danh": bạn có thể gọi người đó bằng tên thật hoặc biệt danh.
- **Quan trọng vì:**
    - **Dễ đọc:** Giúp code SQL dễ hiểu hơn.
    - **Ngắn gọn:** Giúp code SQL ngắn gọn hơn (tránh gõ tên bảng/cột dài dòng).
    - **Phân biệt:** Giúp phân biệt các cột/bảng trùng tên khi làm việc với nhiều bảng.

### **II. CÁCH SỬ DỤNG ALIAS (CÁCH ĐẶT "BÍ DANH")**

#### **2.1. ALIAS CHO CỘT (ĐẶT "BÍ DANH" CHO "ĐỒ")**

```sql
SELECT column_name AS alias_name
FROM table_name;
```

- **`column_name AS alias_name`:** Đặt bí danh cho cột.
- Có thể dùng `AS` hoặc không (để khoảng trắng cũng hiểu).
- **Ví dụ:**

```sql
SELECT FirstName AS Name, Salary AS Luong
FROM Employees;
```

#### **2.2. ALIAS CHO BẢNG (ĐẶT "BÍ DANH" CHO "TỦ")**

```sql
SELECT column1, column2, ...
FROM table_name AS alias_name;
```

- **`FROM table_name AS alias_name`:** Đặt bí danh cho bảng.
- Có thể dùng `AS` hoặc không.
- **Ví dụ:**

```sql
SELECT e.FirstName, e.Salary
FROM Employees AS e;
```

### **III. CÁC TÌNH HUỐNG NÊN DÙNG ALIAS (KHI NÀO CẦN "BÍ DANH")**

1. **Tên cột/bảng quá dài:** Đặt alias ngắn cho dễ gõ, dễ đọc.
2. **Tên cột/bảng trùng nhau:** Phân biệt các cột, bảng từ nhiều nguồn khác nhau.
3. **Dùng trong `JOIN`:** Đặt alias để code `JOIN` ngắn gọn hơn.
4. **Dùng trong các hàm gộp nhóm (`GROUP BY`):** Để tạo tên cột dễ hiểu hơn.

### **IV. VÍ DỤ THỰC TẾ (XEM "THỰC HÀNH")**

1. **Alias cho cột:**

```sql
SELECT FirstName AS "Họ và Tên", Salary AS Luong
FROM Employees;
```

2. **Alias cho bảng:**

```sql
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees AS e
INNER JOIN Departments AS d
ON e.DepartmentID = d.DepartmentID;
```

3. **Alias trong hàm gộp nhóm:**

```sql
SELECT Department AS "Phòng ban", COUNT(*) AS "Số lượng nhân viên"
FROM Employees
GROUP BY Department;
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Tên alias rõ ràng:** Chọn tên alias ngắn gọn mà vẫn dễ hiểu.
- **Alias tạm thời:** Alias chỉ có hiệu lực trong câu query hiện tại.
- **Không dùng từ khóa SQL:** Tránh dùng các từ khóa SQL làm alias (ví dụ: `SELECT`, `FROM`,...).
- **Dùng trong `JOIN`:** Nên dùng alias để code `JOIN` dễ đọc hơn.

### **VI. KẾT LUẬN (TỔNG KẾT)**

Alias là một "chiêu" nhỏ nhưng rất hữu ích giúp bạn code SQL dễ đọc, dễ hiểu và chuyên nghiệp hơn. Hy vọng qua bài viết
này, các bạn đã nắm vững cách dùng và có thể áp dụng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
