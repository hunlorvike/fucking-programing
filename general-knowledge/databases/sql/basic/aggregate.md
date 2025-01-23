## **🚀 "GIẢI MÃ" CÁC HÀM TỔNG HỢP TRONG SQL SERVER: "TÓM TẮT" DỮ LIỆU CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một nhóm hàm cực kỳ quan trọng trong SQL Server: Các
hàm tổng hợp (Aggregate Functions). Đây là những "chiêu thức" giúp bạn tóm tắt, phân tích dữ liệu một cách nhanh chóng
và hiệu quả. Cùng mình "mổ xẻ" nó nhé!

### **I. HÀM TỔNG HỢP LÀ GÌ? (TÓM TẮT DỮ LIỆU NHƯ THẾ NÀO?)**

* **Hàm tổng hợp (Aggregate Functions):** Là các hàm trong SQL dùng để *tóm tắt* dữ liệu từ nhiều dòng thành một giá trị
  duy nhất.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn tính điểm trung bình của lớp: bạn dùng một hàm (AVG) để gộp điểm của nhiều bạn thành một con số
      duy nhất.
* **Quan trọng vì:**
    * **Tóm tắt thông tin:** Tính tổng, trung bình, số lượng,... một cách nhanh chóng.
    * **Phân tích dữ liệu:** Phân tích, thống kê dữ liệu trong cơ sở dữ liệu.
    * **Báo cáo:** Tạo báo cáo dựa trên thông tin tổng hợp.

### **II. CÁC HÀM TỔNG HỢP PHỔ BIẾN (NHỮNG "CHIÊU" HAY DÙNG)**

1. **`COUNT()`:** Đếm số dòng (bản ghi).
2. **`SUM()`:** Tính tổng các giá trị.
3. **`AVG()`:** Tính giá trị trung bình.
4. **`MIN()`:** Tìm giá trị nhỏ nhất.
5. **`MAX()`:** Tìm giá trị lớn nhất.

### **III. CÁCH DÙNG HÀM TỔNG HỢP (CÚ PHÁP)**

* **Cú pháp:**

```sql
SELECT aggregate_function(column_name)
FROM table_name
WHERE condition;
```

* **`aggregate_function()`:** Hàm tổng hợp (COUNT, SUM, AVG, MIN, MAX).
* **`column_name`:** Cột cần tính toán.
* **`FROM table_name`:** Bảng chứa dữ liệu.
* **`WHERE condition`:** Điều kiện lọc dữ liệu (nếu cần).

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

1. **`COUNT()`:** Đếm số nhân viên trong bảng `Employees`.

```sql
SELECT COUNT(*) AS TotalEmployees
FROM Employees;
```

2. **`SUM()`:** Tính tổng lương của tất cả nhân viên.

```sql
SELECT SUM(Salary) AS TotalSalary
FROM Employees;
```

3. **`AVG()`:** Tính lương trung bình của nhân viên.

```sql
SELECT AVG(Salary) AS AvgSalary
FROM Employees;
```

4. **`MIN()`:** Tìm lương thấp nhất trong bảng `Employees`.

```sql
SELECT MIN(Salary) AS MinSalary
FROM Employees;
```

5. **`MAX()`:** Tìm lương cao nhất trong bảng `Employees`.

```sql
SELECT MAX(Salary) AS MaxSalary
FROM Employees;
```

### **V. KẾT HỢP VỚI `GROUP BY` (GOM NHÓM RỒI MỚI TÓM TẮT)**

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition
GROUP BY column1;
```

* **`GROUP BY column1`:** Nhóm các dòng có cùng giá trị ở cột 1.
* Thường dùng khi muốn tính toán theo nhóm.
* **Ví dụ:** Tính lương trung bình theo từng phòng ban.

```sql
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department;
```

### **VI. KẾT HỢP VỚI `HAVING` (LỌC SAU KHI GOM NHÓM)**

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition
GROUP BY column1
HAVING condition;
```

* **`HAVING condition`:** Lọc các nhóm sau khi đã gom nhóm.
* **Ví dụ:** Tìm phòng ban nào có lương trung bình lớn hơn 7000.

```sql
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 7000;
```

### **VII. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

* **`GROUP BY` nếu dùng hàm tổng hợp:** Dùng khi muốn tính toán theo nhóm.
* **`HAVING` để lọc sau `GROUP BY`:** Dùng khi muốn lọc dữ liệu sau khi đã gom nhóm.
* **`WHERE` để lọc trước `GROUP BY`:** Dùng để lọc dữ liệu trước khi gom nhóm.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Hàm tổng hợp là công cụ rất hữu ích để tóm tắt và phân tích dữ liệu trong SQL Server. Hy vọng qua bài viết này, các bạn
đã hiểu rõ hơn về chúng và có thể sử dụng chúng một cách hiệu quả. Chúc các bạn code thành công! 😎
