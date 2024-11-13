# INSERT trong SQL Server

## Mục Lục

1. [Tổng quan về câu lệnh INSERT](#1-tổng-quan-về-câu-lệnh-insert)
   - [INSERT là gì?](#insert-là-gì)
   - [Lợi ích của câu lệnh INSERT](#lợi-ích-của-câu-lệnh-insert)
   - [Câu lệnh INSERT hoạt động như thế nào?](#câu-lệnh-insert-hoạt-động-như-thế-nào)
2. [Cú pháp cơ bản của câu lệnh INSERT](#2-cú-pháp-cơ-bản-của-câu-lệnh-insert)
   - [Chèn một bản ghi mới vào bảng](#chèn-một-bản-ghi-mới-vào-bảng)
   - [Chèn nhiều bản ghi vào bảng](#chèn-nhiều-bản-ghi-vào-bảng)
3. [Các tùy chọn mở rộng của câu lệnh INSERT](#3-các-tùy-chọn-mở-rộng-của-câu-lệnh-insert)
   - [INSERT với SELECT](#insert-với-select)
   - [INSERT với VALUES](#insert-với-values)
4. [Các ví dụ thực tế với INSERT](#4-các-ví-dụ-thực-tế-với-insert)
5. [Lưu ý và thực hành tốt](#5-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về câu lệnh INSERT

#### INSERT là gì?

Câu lệnh `INSERT` trong SQL Server được sử dụng để thêm dữ liệu mới vào bảng trong cơ sở dữ liệu. Đây là một trong những câu lệnh cơ bản của SQL, thường xuyên được sử dụng trong các tác vụ ghi dữ liệu vào bảng.

#### Lợi ích của câu lệnh INSERT

- **Thêm dữ liệu vào bảng**: Cho phép chèn các bản ghi mới vào bảng để duy trì dữ liệu trong hệ thống.
- **Tăng khả năng quản lý dữ liệu**: Giúp duy trì dữ liệu động khi hệ thống cần cập nhật các thông tin mới.
- **Hỗ trợ nhập liệu từ nhiều nguồn**: Có thể kết hợp `INSERT` với các câu lệnh khác như `SELECT` để nhập liệu từ các nguồn khác nhau.

#### Câu lệnh INSERT hoạt động như thế nào?

Khi thực thi câu lệnh `INSERT`, SQL Server thực hiện các bước sau:

1. **Xác định bảng đích**: Xác định bảng mà dữ liệu mới sẽ được chèn vào.
2. **Chèn bản ghi**: Dữ liệu mới sẽ được thêm vào bảng tương ứng.
3. **Cập nhật bảng**: Sau khi thực thi thành công, dữ liệu mới được lưu trữ và bảng được cập nhật.

---

### 2. Cú pháp cơ bản của câu lệnh INSERT

#### Chèn một bản ghi mới vào bảng

Câu lệnh `INSERT` có thể được sử dụng để chèn một bản ghi mới vào bảng bằng cách cung cấp giá trị cho các cột tương ứng.

**Cú pháp**:

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

**Ví dụ**:

```sql
INSERT INTO employees (first_name, last_name, department, salary)
VALUES ('John', 'Doe', 'HR', 6000);
```

Câu lệnh trên sẽ chèn một bản ghi mới vào bảng `employees` với các giá trị tương ứng cho các cột `first_name`, `last_name`, `department`, và `salary`.

#### Chèn nhiều bản ghi vào bảng

Nếu bạn muốn chèn nhiều bản ghi cùng lúc, có thể cung cấp nhiều tập giá trị trong câu lệnh `INSERT`.

**Cú pháp**:

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...),
       (value1, value2, ...),
       ...;
```

**Ví dụ**:

```sql
INSERT INTO employees (first_name, last_name, department, salary)
VALUES ('Jane', 'Smith', 'IT', 7000),
       ('Jim', 'Brown', 'Sales', 8000);
```

Câu lệnh trên sẽ chèn hai bản ghi mới vào bảng `employees`.

---

### 3. Các tùy chọn mở rộng của câu lệnh INSERT

#### INSERT với SELECT

Câu lệnh `INSERT` có thể được kết hợp với câu lệnh `SELECT` để chèn dữ liệu từ một bảng khác vào bảng đích.

**Cú pháp**:

```sql
INSERT INTO table_name (column1, column2, ...)
SELECT column1, column2, ...
FROM source_table
WHERE condition;
```

**Ví dụ**:

```sql
INSERT INTO employees (first_name, last_name, department, salary)
SELECT first_name, last_name, department, salary
FROM new_employees
WHERE hire_date > '2024-01-01';
```

Câu lệnh trên sẽ chèn các bản ghi từ bảng `new_employees` vào bảng `employees`, chỉ với những nhân viên có ngày tuyển dụng sau ngày 1 tháng 1 năm 2024.

#### INSERT với VALUES

Trong câu lệnh `INSERT` với `VALUES`, bạn có thể cung cấp các giá trị trực tiếp vào các cột của bảng. Điều này hữu ích khi bạn có dữ liệu cụ thể muốn thêm vào.

**Cú pháp**:

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

Ví dụ này đã được trình bày trong phần trên, khi chúng ta chèn một bản ghi với các giá trị cụ thể.

---

### 4. Các ví dụ thực tế với INSERT

#### Chèn một nhân viên mới vào bảng employees

**Câu lệnh SQL**:

```sql
INSERT INTO employees (first_name, last_name, department, salary)
VALUES ('Alice', 'Johnson', 'Marketing', 5500);
```

**Giải thích**:

- Chèn một bản ghi mới vào bảng `employees` với thông tin của nhân viên Alice, thuộc phòng ban `Marketing`, và có mức lương là 5500.

**Kết quả**:

Bản ghi mới sẽ được thêm vào bảng `employees` sau khi thực thi câu lệnh.

---

#### Chèn nhiều nhân viên cùng lúc vào bảng employees

**Câu lệnh SQL**:

```sql
INSERT INTO employees (first_name, last_name, department, salary)
VALUES ('Michael', 'Scott', 'HR', 6500),
       ('Dwight', 'Schrute', 'Sales', 7000);
```

**Giải thích**:

- Chèn hai bản ghi vào bảng `employees` cho các nhân viên `Michael Scott` và `Dwight Schrute` với các thông tin phòng ban và lương tương ứng.

**Kết quả**:

Cả hai bản ghi sẽ được chèn vào bảng `employees`.

---

#### Chèn dữ liệu từ một bảng khác vào bảng employees

**Câu lệnh SQL**:

```sql
INSERT INTO employees (first_name, last_name, department, salary)
SELECT first_name, last_name, department, salary
FROM new_employees
WHERE department = 'HR';
```

**Giải thích**:

- Chèn các nhân viên từ bảng `new_employees` vào bảng `employees`, chỉ với những nhân viên thuộc phòng ban `HR`.

**Kết quả**:

Các nhân viên trong phòng ban `HR` từ bảng `new_employees` sẽ được chèn vào bảng `employees`.

---

### 5. Lưu ý và thực hành tốt

- **Kiểm tra dữ liệu đầu vào**: Trước khi chèn dữ liệu, hãy đảm bảo các giá trị nhập vào phù hợp với loại dữ liệu của các cột.
- **Sử dụng `SELECT` trước khi `INSERT`**: Trước khi thực hiện chèn dữ liệu từ bảng khác, hãy kiểm tra dữ liệu với câu lệnh `SELECT` để đảm bảo bạn đang chèn đúng dữ liệu.
- **Sử dụng các khóa chính (Primary Keys)**: Đảm bảo rằng dữ liệu bạn chèn không vi phạm các ràng buộc khóa chính hoặc khóa ngoại trong bảng.
- **Tránh chèn dữ liệu trùng lặp**: Sử dụng các phương thức kiểm tra như `DISTINCT` hoặc điều kiện `WHERE` để tránh chèn các bản ghi trùng lặp.
