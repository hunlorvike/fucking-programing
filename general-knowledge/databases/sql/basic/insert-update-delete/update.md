# UPDATE trong SQL Server

## Mục Lục

1. [Tổng quan về câu lệnh UPDATE](#1-tổng-quan-về-câu-lệnh-update)
    - [UPDATE là gì?](#update-là-gì)
    - [Lợi ích của câu lệnh UPDATE](#lợi-ích-của-câu-lệnh-update)
    - [Câu lệnh UPDATE hoạt động như thế nào?](#câu-lệnh-update-hoạt-động-như-thế-nào)
2. [Cú pháp cơ bản của câu lệnh UPDATE](#2-cú-pháp-cơ-bản-của-câu-lệnh-update)
    - [Cập nhật một bản ghi](#cập-nhật-một-bản-ghi)
    - [Cập nhật nhiều bản ghi](#cập-nhật-nhiều-bản-ghi)
3. [Các tùy chọn mở rộng của câu lệnh UPDATE](#3-các-tùy-chọn-mở-rộng-của-câu-lệnh-update)
    - [UPDATE với WHERE](#update-với-where)
    - [UPDATE với JOIN](#update-với-join)
4. [Các ví dụ thực tế với UPDATE](#4-các-ví-dụ-thực-tế-với-update)
5. [Lưu ý và thực hành tốt](#5-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về câu lệnh UPDATE

#### UPDATE là gì?

Câu lệnh `UPDATE` trong SQL Server được sử dụng để thay đổi dữ liệu đã có trong bảng. Bạn có thể cập nhật một hoặc nhiều
cột trong bảng với các giá trị mới. Đây là câu lệnh quan trọng để duy trì và chỉnh sửa dữ liệu trong cơ sở dữ liệu.

#### Lợi ích của câu lệnh UPDATE

- **Chỉnh sửa dữ liệu**: Cập nhật giá trị của các bản ghi đã có trong bảng mà không cần phải xóa và thêm lại dữ liệu.
- **Tăng tính linh hoạt**: Cho phép bạn thay đổi thông tin trong bảng dựa trên các điều kiện cụ thể.
- **Sửa lỗi hoặc cập nhật thông tin**: Có thể sử dụng `UPDATE` để sửa các lỗi hoặc bổ sung thông tin cho các bản ghi
  hiện tại.

#### Câu lệnh UPDATE hoạt động như thế nào?

Khi thực thi câu lệnh `UPDATE`, SQL Server thực hiện các bước sau:

1. **Xác định bảng cần cập nhật**: Xác định bảng mà dữ liệu sẽ được thay đổi.
2. **Áp dụng các điều kiện (nếu có)**: Nếu có, áp dụng các điều kiện `WHERE` để xác định bản ghi cần cập nhật.
3. **Cập nhật dữ liệu**: Sau khi xác định các bản ghi, SQL Server sẽ thay đổi các giá trị trong các cột được chỉ định.
4. **Hoàn thành cập nhật**: Dữ liệu mới được lưu trữ và bảng được cập nhật.

---

### 2. Cú pháp cơ bản của câu lệnh UPDATE

#### Cập nhật một bản ghi

Câu lệnh `UPDATE` có thể được sử dụng để thay đổi một bản ghi cụ thể trong bảng bằng cách xác định các cột cần cập nhật
và giá trị mới.

**Cú pháp**:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**Ví dụ**:

```sql
UPDATE employees
SET salary = 7000
WHERE employee_id = 1;
```

Câu lệnh trên sẽ cập nhật lương của nhân viên có `employee_id` là 1 thành 7000.

#### Cập nhật nhiều bản ghi

Câu lệnh `UPDATE` cũng có thể cập nhật nhiều bản ghi cùng lúc nếu điều kiện trong `WHERE` phù hợp với nhiều bản ghi.

**Cú pháp**:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**Ví dụ**:

```sql
UPDATE employees
SET department = 'Sales', salary = 7500
WHERE department = 'Marketing';
```

Câu lệnh trên sẽ cập nhật tất cả nhân viên thuộc phòng ban `Marketing`, thay đổi phòng ban thành `Sales` và lương thành

7500.

---

### 3. Các tùy chọn mở rộng của câu lệnh UPDATE

#### UPDATE với WHERE

`WHERE` là phần quan trọng của câu lệnh `UPDATE` vì nó xác định các bản ghi nào cần được cập nhật. Nếu không có `WHERE`,
toàn bộ bảng sẽ bị cập nhật.

**Cú pháp**:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**Ví dụ**:

```sql
UPDATE employees
SET salary = 6000
WHERE department = 'HR';
```

Câu lệnh này sẽ cập nhật mức lương của tất cả nhân viên thuộc phòng ban `HR` thành 6000.

#### UPDATE với JOIN

Câu lệnh `UPDATE` có thể kết hợp với `JOIN` để cập nhật dữ liệu từ các bảng khác. Đây là một kỹ thuật hữu ích khi bạn
muốn cập nhật dữ liệu dựa trên thông tin từ bảng khác.

**Cú pháp**:

```sql
UPDATE table1
SET table1.column1 = table2.column1, ...
FROM table1
JOIN table2
ON table1.column = table2.column
WHERE condition;
```

**Ví dụ**:

```sql
UPDATE employees
SET employees.salary = departments.budget / employees.num_employees
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE departments.department_name = 'IT';
```

Câu lệnh trên sẽ cập nhật mức lương của tất cả nhân viên trong phòng ban `IT` dựa trên ngân sách của phòng ban và số
lượng nhân viên.

---

### 4. Các ví dụ thực tế với UPDATE

#### Cập nhật lương của một nhân viên cụ thể

**Câu lệnh SQL**:

```sql
UPDATE employees
SET salary = 8000
WHERE employee_id = 2;
```

**Giải thích**:

- Câu lệnh trên sẽ cập nhật lương của nhân viên có `employee_id` là 2 thành 8000.

**Kết quả**:

Lương của nhân viên với `employee_id = 2` sẽ được thay đổi thành 8000.

---

#### Cập nhật lương của tất cả nhân viên trong một phòng ban

**Câu lệnh SQL**:

```sql
UPDATE employees
SET salary = salary + 1000
WHERE department = 'Sales';
```

**Giải thích**:

- Câu lệnh trên sẽ tăng lương của tất cả nhân viên trong phòng ban `Sales` thêm 1000.

**Kết quả**:

Mức lương của tất cả nhân viên trong phòng ban `Sales` sẽ được tăng thêm 1000.

---

#### Cập nhật thông tin nhân viên dựa trên bảng khác

**Câu lệnh SQL**:

```sql
UPDATE employees
SET employees.salary = departments.budget / employees.num_employees
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id
WHERE departments.department_name = 'HR';
```

**Giải thích**:

- Câu lệnh trên sẽ cập nhật mức lương của nhân viên trong phòng ban `HR` dựa trên ngân sách phòng ban chia cho số lượng
  nhân viên trong phòng ban đó.

**Kết quả**:

Mức lương của các nhân viên trong phòng ban `HR` sẽ được tính toán lại và cập nhật dựa trên ngân sách của phòng ban.

---

### 5. Lưu ý và thực hành tốt

- **Sử dụng `WHERE` cẩn thận**: Nếu bạn không sử dụng điều kiện `WHERE` đúng cách, toàn bộ bảng có thể bị cập nhật, gây
  ra lỗi hoặc thay đổi không mong muốn.
- **Kiểm tra trước khi cập nhật**: Trước khi thực thi câu lệnh `UPDATE`, hãy thực hiện một câu lệnh `SELECT` để kiểm tra
  xem những bản ghi nào sẽ bị ảnh hưởng.
- **Sử dụng giao dịch (Transactions)**: Khi thực hiện các cập nhật quan trọng, hãy sử dụng giao dịch (
  `BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK`) để đảm bảo rằng bạn có thể khôi phục thay đổi nếu có sự cố.
- **Chú ý đến hiệu suất**: Việc cập nhật nhiều bản ghi hoặc sử dụng `JOIN` trong câu lệnh `UPDATE` có thể ảnh hưởng đến
  hiệu suất. Hãy tối ưu hóa câu lệnh nếu cần thiết.
