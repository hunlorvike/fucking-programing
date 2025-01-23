## **🚀 "GIẢI MÃ" CÂU LỆNH INSERT TRONG SQL SERVER: THÊM DỮ LIỆU VÀO "KHO" CỦA BẠN 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một câu lệnh cực kỳ quan trọng trong SQL Server:
`INSERT`. Đây là câu lệnh giúp bạn thêm dữ liệu vào cơ sở dữ liệu của mình. Cùng mình "mổ xẻ" nó nhé!

### **I. CÂU LỆNH INSERT LÀ GÌ? (THÊM DỮ LIỆU VÀO "KHO")**

* **`INSERT`:** Là câu lệnh SQL dùng để thêm dữ liệu mới vào một bảng trong cơ sở dữ liệu.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn thêm đồ mới vào tủ: bạn mở tủ (chọn bảng), và cho đồ (dữ liệu) vào.
* **Quan trọng vì:**
    * **Thêm dữ liệu:** Cập nhật thông tin mới, duy trì dữ liệu hệ thống.
    * **Nhập liệu:** Nhập dữ liệu từ nhiều nguồn khác nhau.
    * **Quản lý:** Quản lý dữ liệu trong cơ sở dữ liệu.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG INSERT)**

#### **2.1. CHÈN MỘT BẢN GHI (THÊM MỘT "MÓN ĐỒ" MỚI)**

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

* **`INSERT INTO table_name`:** Chọn bảng cần thêm dữ liệu.
* **`(column1, column2, ...)`:** Liệt kê các cột cần thêm dữ liệu.
* **`VALUES (value1, value2, ...)`:** Liệt kê các giá trị tương ứng.
* **Ví dụ:**

```sql
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('John', 'Doe', 'HR', 6000);
```

#### **2.2. CHÈN NHIỀU BẢN GHI (THÊM NHIỀU "MÓN ĐỒ" MỚI)**

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...),
       (value1, value2, ...),
       ...;
```

* **`VALUES (...) , (...) , ...`:** Thêm nhiều dòng dữ liệu cùng lúc.
* **Ví dụ:**

```sql
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Jane', 'Smith', 'IT', 7000),
       ('Jim', 'Brown', 'Sales', 8000);
```

### **III. CÁC TÙY CHỌN MỞ RỘNG (CÁC "CHIÊU" NÂNG CAO)**

#### **3.1. INSERT VỚI SELECT (THÊM DỮ LIỆU TỪ BẢNG KHÁC)**

```sql
INSERT INTO table_name (column1, column2, ...)
SELECT column1, column2, ...
FROM source_table
WHERE condition;
```

* **`SELECT ... FROM source_table`:** Chọn dữ liệu từ bảng khác.
* **`WHERE condition`:** Thêm điều kiện lọc dữ liệu (nếu cần).
* **Ví dụ:**

```sql
INSERT INTO Employees (FirstName, LastName, Department, Salary)
SELECT FirstName, LastName, Department, Salary
FROM NewEmployees
WHERE HireDate > '2024-01-01';
```

#### **3.2. INSERT VỚI VALUES (THÊM GIÁ TRỊ CỤ THỂ)**

* Chèn các giá trị trực tiếp vào các cột.
* (Đã nói ở phần trên, nhưng nhắc lại để các bạn nhớ).

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### **IV. VÍ DỤ THỰC TẾ (XEM "THỰC HÀNH")**

1. **Chèn 1 nhân viên:**

```sql
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Alice', 'Johnson', 'Marketing', 5500);
```

2. **Chèn nhiều nhân viên:**

```sql
INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES ('Michael', 'Scott', 'HR', 6500),
       ('Dwight', 'Schrute', 'Sales', 7000);
```

3. **Chèn từ bảng khác:**

```sql
INSERT INTO Employees (FirstName, LastName, Department, Salary)
SELECT FirstName, LastName, Department, Salary
FROM NewEmployees
WHERE Department = 'HR';
```

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

* **Kiểm tra dữ liệu:** Dữ liệu phải đúng kiểu (int, string, ...).
* **Dùng SELECT trước khi INSERT:** Kiểm tra dữ liệu trước khi insert (khi insert từ bảng khác).
* **Primary Key:** Không được vi phạm khóa chính (primary key) và khóa ngoại (foreign key).
* **Tránh trùng lặp:** Dùng `DISTINCT` hoặc `WHERE` để tránh trùng lặp.

### **VI. KẾT LUẬN (TỔNG KẾT)**

`INSERT` là câu lệnh cơ bản để thêm dữ liệu vào cơ sở dữ liệu SQL Server. Hy vọng qua bài viết này, các bạn đã hiểu rõ
hơn về nó và có thể sử dụng nó một cách hiệu quả. Chúc các bạn code thành công! 😎
