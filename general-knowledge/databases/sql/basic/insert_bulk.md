## **🚀 "GIẢI MÃ" INSERT BULK TRONG SQL SERVER: THÊM DỮ LIỆU HÀNG LOẠT "NHANH NHƯ CHỚP" CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một "chiêu thức" cực kỳ hữu ích trong SQL Server:
`INSERT BULK`. Đây là câu lệnh giúp bạn chèn một lượng lớn dữ liệu vào database siêu nhanh, thay vì "nhỏ giọt" từng
dòng. Cùng mình "mổ xẻ" nó nhé!

### **I. INSERT BULK LÀ GÌ? (THÊM NHIỀU DỮ LIỆU VÀO "KHO" CÙNG LÚC)**

* **`INSERT BULK`:** Là các cách để chèn *nhiều bản ghi* vào bảng trong SQL Server *cùng một lúc*, thay vì chèn từng
  dòng một.
* **Nó hoạt động như thế nào?**
    * Giống như khi bạn bỏ cả thùng đồ vào tủ, thay vì bỏ từng món.
* **Quan trọng vì:**
    * **Nhanh hơn:** Chèn dữ liệu nhanh hơn nhiều so với `INSERT` thông thường.
    * **Hiệu quả:** Xử lý dữ liệu lớn hiệu quả hơn.
    * **Linh hoạt:** Hỗ trợ nhiều cách khác nhau để import dữ liệu.

### **II. CÁC CÁCH INSERT BULK (NHIỀU "CHIÊU" IMPORT DỮ LIỆU)**

#### **2.1. `BULK INSERT` (NHẬP DỮ LIỆU TỪ FILE)**

```sql
BULK INSERT table_name
FROM 'file_path'
WITH (
    FIELDTERMINATOR = ',',   -- Dấu phân cách cột (CSV: ",")
    ROWTERMINATOR = '\n',   -- Dấu phân cách dòng (xuống dòng)
    FIRSTROW = 2            -- Bỏ qua dòng tiêu đề (nếu có)
);
```

* **`BULK INSERT table_name`:** Chọn bảng cần chèn dữ liệu.
* **`FROM 'file_path'`:** Chọn file chứa dữ liệu (CSV, TXT,...).
* **`WITH (...)`:** Các tùy chọn:
    * **`FIELDTERMINATOR`:** Dấu phân cách cột.
    * **`ROWTERMINATOR`:** Dấu phân cách dòng.
    * **`FIRSTROW`:** Bỏ qua dòng đầu tiên (dòng tiêu đề).

* **Ví dụ:**

```sql
BULK INSERT Employees
FROM 'C:\data\employees.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
```

#### **2.2. `INSERT INTO ... SELECT` (NHẬP DỮ LIỆU TỪ BẢNG KHÁC)**

```sql
INSERT INTO table_name (column1, column2, ...)
SELECT column1, column2, ...
FROM another_table
WHERE condition;
```

* **`INSERT INTO table_name (...)`:** Chọn bảng cần chèn dữ liệu.
* **`SELECT ... FROM another_table`:** Chọn dữ liệu từ bảng khác.
* **`WHERE condition`:** Điều kiện lọc dữ liệu (nếu cần).

* **Ví dụ:**

```sql
INSERT INTO Employees (FirstName, LastName, Department, Salary)
SELECT FirstName, LastName, Department, Salary
FROM OldEmployees
WHERE Department = 'HR';
```

#### **2.3. `BCP` (BULK COPY PROGRAM) (DÙNG LỆNH CMD)**

* Là một công cụ dòng lệnh (command line), mạnh mẽ hơn, dùng để import/export dữ liệu hàng loạt.
* **Cú pháp:**

```bash
bcp database_name.dbo.table_name in "file_path" -S server_name -U username -P password -c -t,
```

* **Ví dụ:**

```bash
bcp mydatabase.dbo.employees in "C:\data\employees.csv" -S localhost -U sa -P mypassword -c -t,
```

### **III. CÁC TÙY CHỌN THƯỜNG DÙNG (KHI DÙNG `BULK INSERT`)**

* **`FIELDTERMINATOR`:** Dấu phân cách cột (`,`, `|`, ...).
* **`ROWTERMINATOR`:** Dấu phân cách dòng (`\n`, `\r\n`, ...).
* **`FIRSTROW`:** Số dòng đầu tiên bỏ qua (dùng khi có header).
* **`TABLOCK`:** Khóa toàn bộ bảng khi insert (tăng tốc độ khi insert nhiều).
* **`CHECK_CONSTRAINTS`:** Kiểm tra các ràng buộc (primary key, foreign key).
* **`KEEPNULLS`:** Giữ giá trị `NULL` khi import dữ liệu.

### **IV. VÍ DỤ THỰC TẾ (XEM "THỰC HÀNH")**

1. **Nhập nhân viên từ CSV:**

```sql
BULK INSERT Employees
FROM 'C:\data\employees.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK,
    CHECK_CONSTRAINTS
);
```

2. **Nhập từ bảng khác:**

```sql
INSERT INTO Employees (FirstName, LastName, Department, Salary)
SELECT FirstName, LastName, Department, Salary
FROM NewEmployees
WHERE Department = 'HR';
```

3. **Nhập dùng `BCP`:**

```bash
bcp mydatabase.dbo.employees in "C:\data\employees.csv" -S localhost -U sa -P mypassword -c -t,
```

### **V. LỢI ÍCH CỦA `INSERT BULK` (TẠI SAO NÊN DÙNG?)**

* **Nhanh:** Xử lý dữ liệu lớn nhanh hơn nhiều so với `INSERT` thường.
* **Hỗ trợ nhiều format:** Hỗ trợ các file CSV, TXT, ...
* **Giảm tải database:** Giúp database chạy nhanh hơn khi nhập nhiều dữ liệu.

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

* **Kiểm tra dữ liệu:** Dữ liệu trong file phải đúng format.
* **Chỉ mục:** Có thể tạm tắt index khi import (tăng tốc độ), rồi bật lại sau.
* **Kiểm tra sau import:** Sau khi import xong, kiểm tra lại dữ liệu.
* **Xử lý lỗi:** Chuẩn bị trước các lỗi có thể xảy ra (dữ liệu không hợp lệ, ...)

### **VII. KẾT LUẬN (TỔNG KẾT)**

`INSERT BULK` là một "chiêu thức" cực kỳ lợi hại để nhập dữ liệu nhanh và hiệu quả trong SQL Server. Hy vọng qua bài
viết này, các bạn đã hiểu rõ hơn về nó và có thể sử dụng nó một cách "ngon lành". Chúc các bạn code thành công! 😎
