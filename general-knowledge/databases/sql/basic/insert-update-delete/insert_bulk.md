### **Câu lệnh INSERT BULK trong SQL Server**

Khi làm việc với lượng dữ liệu lớn, việc chèn dữ liệu vào bảng một cách hiệu quả là rất quan trọng. Câu lệnh `INSERT BULK` giúp bạn chèn nhiều bản ghi vào một bảng trong một lần thực thi, giúp tối ưu hóa quá trình nhập liệu.

---

### **1. Cú pháp cơ bản của INSERT BULK**

Trong SQL Server, không có một câu lệnh `INSERT BULK` trực tiếp, nhưng có thể sử dụng các phương pháp như `BULK INSERT`, `INSERT INTO ... SELECT`, hoặc các công cụ hỗ trợ như `bcp` (Bulk Copy Program) để thực hiện việc chèn dữ liệu hàng loạt.

#### **1.1. Sử dụng BULK INSERT**

Câu lệnh `BULK INSERT` được sử dụng để nhập dữ liệu từ tệp văn bản (file) vào một bảng trong cơ sở dữ liệu. Dữ liệu thường được lưu trữ trong các tệp có định dạng CSV hoặc TSV (tách bằng dấu phẩy hoặc tab).

**Cú pháp**:

```sql
BULK INSERT table_name
FROM 'file_path'
WITH (
    FIELDTERMINATOR = ',',  -- Định nghĩa dấu phân cách cột (thường là dấu phẩy đối với CSV)
    ROWTERMINATOR = '\n',   -- Định nghĩa dấu phân cách giữa các dòng (thường là ký tự xuống dòng)
    FIRSTROW = 2           -- Bỏ qua dòng tiêu đề trong tệp (nếu có)
);
```

**Ví dụ**:

Giả sử bạn có tệp `employees.csv` chứa dữ liệu nhân viên, và bạn muốn chèn tất cả dữ liệu từ tệp này vào bảng `employees` trong cơ sở dữ liệu:

```sql
BULK INSERT employees
FROM 'C:\data\employees.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);
```

Trong ví dụ trên, dữ liệu từ tệp `employees.csv` sẽ được chèn vào bảng `employees`, bỏ qua dòng đầu tiên (dòng tiêu đề).

---

#### **1.2. Sử dụng INSERT INTO ... SELECT**

Một cách khác để chèn dữ liệu hàng loạt là sử dụng câu lệnh `INSERT INTO ... SELECT`, đặc biệt hữu ích khi bạn muốn chèn dữ liệu từ một bảng khác hoặc khi dữ liệu được tạo từ một truy vấn phức tạp.

**Cú pháp**:

```sql
INSERT INTO table_name (column1, column2, ...)
SELECT column1, column2, ...
FROM another_table;
```

**Ví dụ**:

Giả sử bạn muốn sao chép tất cả dữ liệu từ bảng `old_employees` vào bảng `employees`:

```sql
INSERT INTO employees (first_name, last_name, department, salary)
SELECT first_name, last_name, department, salary
FROM old_employees;
```

Câu lệnh này sẽ chèn tất cả các bản ghi từ bảng `old_employees` vào bảng `employees`.

---

#### **1.3. Sử dụng BCP (Bulk Copy Program)**

`bcp` là một công cụ dòng lệnh mạnh mẽ của SQL Server, cho phép bạn sao chép dữ liệu giữa các bảng SQL Server và các tệp văn bản. Công cụ này thường được sử dụng khi bạn cần nhập hoặc xuất lượng lớn dữ liệu.

**Cú pháp**:

```sh
bcp database_name.dbo.table_name in "file_path" -S server_name -U username -P password -c -t,
```

**Ví dụ**:

Chèn dữ liệu từ tệp `employees.csv` vào bảng `employees`:

```sh
bcp mydatabase.dbo.employees in "C:\data\employees.csv" -S localhost -U sa -P mypassword -c -t,
```

Trong đó:

- `-S` chỉ định máy chủ SQL.
- `-U` và `-P` chỉ định tên người dùng và mật khẩu.
- `-c` chỉ định sử dụng kiểu dữ liệu ký tự.
- `-t,` chỉ định dấu phân cách các trường là dấu phẩy.

---

### **2. Các Tùy Chọn Của BULK INSERT**

Khi sử dụng `BULK INSERT`, bạn có thể chỉ định các tùy chọn để kiểm soát cách thức nhập dữ liệu. Dưới đây là các tùy chọn phổ biến:

- **FIELDTERMINATOR**: Định nghĩa ký tự phân cách các cột (ví dụ: dấu phẩy `,` đối với CSV).
- **ROWTERMINATOR**: Định nghĩa ký tự phân cách các dòng (ví dụ: ký tự xuống dòng `\n`).
- **FIRSTROW**: Chỉ định dòng bắt đầu chèn, thường dùng để bỏ qua dòng tiêu đề.
- **TABLOCK**: Khóa toàn bộ bảng khi thực hiện thao tác chèn, giúp cải thiện hiệu suất khi chèn dữ liệu lớn.
- **CHECK_CONSTRAINTS**: Kiểm tra các ràng buộc trong bảng khi thực hiện `BULK INSERT`. Nếu dữ liệu không hợp lệ, thao tác sẽ bị hủy bỏ.
- **KEEPNULLS**: Giữ giá trị NULL trong khi chèn dữ liệu.

**Ví dụ**:

```sql
BULK INSERT employees
FROM 'C:\data\employees.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2,
    TABLOCK,
    CHECK_CONSTRAINTS
);
```

---

### **3. Các Lợi Ích Của BULK INSERT**

- **Tốc độ nhanh**: `BULK INSERT` được tối ưu hóa để xử lý lượng lớn dữ liệu, nhanh hơn nhiều so với việc chèn từng bản ghi một cách thủ công.
- **Hỗ trợ nhiều định dạng tệp**: `BULK INSERT` hỗ trợ các định dạng như CSV, TSV và các tệp có cấu trúc khác.
- **Giảm tải cho cơ sở dữ liệu**: Việc sử dụng `BULK INSERT` giúp giảm bớt gánh nặng của SQL Server khi nhập dữ liệu lớn và giúp hệ thống hoạt động hiệu quả hơn.

---

### **4. Lưu ý và Thực Hành Tốt**

- **Kiểm tra dữ liệu trước khi chèn**: Trước khi sử dụng `BULK INSERT`, đảm bảo dữ liệu trong tệp không chứa lỗi hoặc giá trị không hợp lệ để tránh lỗi khi nhập.
- **Sử dụng chỉ mục tạm thời**: Để tối ưu hiệu suất khi thực hiện nhập liệu hàng loạt, bạn có thể tạm thời tắt các chỉ mục hoặc ràng buộc trước khi thực hiện `BULK INSERT`, và sau đó tái tạo lại chúng.
- **Thực hiện kiểm tra sau khi nhập liệu**: Sau khi dữ liệu được chèn, hãy thực hiện các truy vấn kiểm tra để đảm bảo không có dữ liệu bị thiếu hoặc lỗi.
- **Quản lý lỗi**: Đảm bảo có kế hoạch xử lý các lỗi, đặc biệt khi làm việc với các tệp dữ liệu không xác định hoặc khi dữ liệu không phù hợp với cấu trúc của bảng.

---

### **5. Kết luận**

`BULK INSERT` là một công cụ mạnh mẽ để nhập dữ liệu hàng loạt vào SQL Server, giúp tiết kiệm thời gian và tăng hiệu suất khi làm việc với lượng dữ liệu lớn. Các công cụ và phương pháp khác như `INSERT INTO ... SELECT`, và `bcp` cũng có thể được sử dụng tùy thuộc vào hoàn cảnh và yêu cầu cụ thể của dự án.
