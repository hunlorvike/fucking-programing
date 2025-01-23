## **🚀 "GIẢI MÃ" WHERE VS HAVING: "LỌC" DỮ LIỆU TRONG SQL SERVER CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai mệnh đề quan trọng trong SQL Server: `WHERE` và
`HAVING`. Cả hai đều dùng để "lọc" dữ liệu, nhưng lại có cách dùng và mục đích khác nhau. Cùng mình "mổ xẻ" nó nhé!

### **I. WHERE VÀ HAVING LÀ GÌ? (CẢ HAI ĐỀU "LỌC" DỮ LIỆU)**

- **`WHERE`:** Là mệnh đề dùng để _lọc dữ liệu trước khi gộp nhóm (group by)_.
- **`HAVING`:** Là mệnh đề dùng để _lọc dữ liệu sau khi gộp nhóm (group by)_.
- **Tóm lại:**
    - **`WHERE`:** Lọc _từng dòng_ dữ liệu.
    - **`HAVING`:** Lọc _từng nhóm_ dữ liệu.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG WHERE VÀ HAVING)**

#### **2.1. WHERE (LỌC "TRƯỚC KHI CHẾ BIẾN")**

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

- **`WHERE condition`:** Điều kiện để lọc từng dòng dữ liệu.
- **Ví dụ:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Department = 'HR';
```

#### **2.2. HAVING (LỌC "SAU KHI CHẾ BIẾN")**

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

- **`GROUP BY column1`:** Gộp nhóm các dòng theo giá trị ở cột 1.
- **`HAVING condition`:** Điều kiện để lọc các nhóm đã được gộp.
- **Ví dụ:**

```sql
SELECT Department, COUNT(*) AS TotalEmployees
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 5;
```

### **III. SỰ KHÁC BIỆT CHÍNH (ĐỂ THẤY RÕ SỰ KHÁC BIỆT)**

1. **Thời điểm lọc:**
    - `WHERE` lọc trước khi gộp nhóm (trên từng dòng).
    - `HAVING` lọc sau khi gộp nhóm (trên từng nhóm).
2. **Kết hợp với `GROUP BY`:**
    - `WHERE` dùng độc lập, không cần `GROUP BY`.
    - `HAVING` phải dùng với `GROUP BY`.
3. **Điều kiện lọc:**
    - `WHERE` dùng cho điều kiện trên từng cột.
    - `HAVING` dùng cho điều kiện trên các hàm tổng hợp (COUNT, SUM, AVG, ...).

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

#### **4.1. DÙNG WHERE ĐỂ LỌC TỪNG DÒNG:**

```sql
SELECT FirstName, LastName, Salary
FROM Employees
WHERE Salary > 7000;
```

- **Giải thích:** Lấy ra các nhân viên có lương trên 7000 (lọc trên từng dòng).

#### **4.2. DÙNG HAVING ĐỂ LỌC CÁC NHÓM (PHÒNG BAN):**

```sql
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 7000;
```

- **Giải thích:**
    - Gộp nhóm theo phòng ban (`GROUP BY`).
    - Tính lương trung bình của mỗi phòng ban (`AVG(Salary)`).
    - Lọc ra các phòng ban có lương trung bình trên 7000 (`HAVING`).

#### **4.3. KẾT HỢP WHERE VÀ HAVING (LỌC TRƯỚC RỒI LỌC SAU):**

```sql
SELECT Department, COUNT(*) AS TotalEmployees
FROM Employees
WHERE Department != 'HR'  -- Lọc trước, loại bỏ phòng HR
GROUP BY Department
HAVING COUNT(*) > 5;     -- Lọc sau, chỉ lấy phòng có hơn 5 nhân viên
```

- **Giải thích:**
    - Lọc ra các nhân viên không thuộc phòng ban HR (`WHERE`).
    - Gộp nhóm theo phòng ban (`GROUP BY`).
    - Lấy ra các phòng ban có hơn 5 nhân viên (`HAVING`).

### **V. KHI NÀO NÊN DÙNG WHERE, KHI NÀO NÊN DÙNG HAVING? (CHỌN ĐÚNG "VŨ KHÍ")**

- **`WHERE`:**
    - Khi cần lọc dữ liệu _trước khi_ dùng hàm gộp nhóm (`COUNT()`, `SUM()`, `AVG()`, ...).
    - Khi lọc dữ liệu dựa trên giá trị của các cột.
- **`HAVING`:**
    - Khi cần lọc dữ liệu _sau khi_ dùng hàm gộp nhóm.
    - Khi lọc dựa trên kết quả của các hàm tổng hợp.

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **`WHERE` trước `GROUP BY`:** Luôn dùng `WHERE` trước `GROUP BY`.
- **`HAVING` sau `GROUP BY`:** Luôn dùng `HAVING` sau `GROUP BY`.
- **Không dùng `WHERE` cho hàm gộp nhóm:** Không được dùng `WHERE` để lọc trên các hàm gộp nhóm, mà phải dùng `HAVING`.
- **Hiệu suất:** Đôi khi dùng `WHERE` và `HAVING` đúng cách có thể giúp query nhanh hơn (ví dụ, lọc bớt dữ liệu trước
  khi gộp nhóm).

### **VII. KẾT LUẬN (TỔNG KẾT)**

`WHERE` và `HAVING` là hai mệnh đề quan trọng giúp bạn lọc dữ liệu một cách linh hoạt trong SQL. Hy vọng qua bài viết
này, các bạn đã hiểu rõ hơn về chúng và có thể sử dụng chúng một cách hiệu quả. Chúc các bạn code thành công! 😎
