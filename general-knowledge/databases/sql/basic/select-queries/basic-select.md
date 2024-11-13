# Basic SELECT trong SQL Server

## Mục Lục

1. [Tổng quan về câu lệnh SELECT](#1-tổng-quan-về-câu-lệnh-select)
   - [SELECT là gì?](#select-là-gì)
   - [Lợi ích của câu lệnh SELECT](#lợi-ích-của-câu-lệnh-select)
   - [Câu lệnh SELECT hoạt động như thế nào?](#câu-lệnh-select-hoạt-động-như-thế-nào)
2. [Cú pháp cơ bản của câu lệnh SELECT](#2-cú-pháp-cơ-bản-của-câu-lệnh-select)
   - [Chọn các cột cụ thể](#chọn-các-cột-cụ-thể)
   - [Chọn tất cả các cột](#chọn-tất-cả-các-cột)
3. [Các tùy chọn mở rộng của câu lệnh SELECT](#3-các-tùy-chọn-mở-rộng-của-câu-lệnh-select)
   - [WHERE](#where)
   - [ORDER BY](#order-by)
   - [DISTINCT](#distinct)
4. [Kết hợp nhiều bảng trong SELECT](#4-kết-hợp-nhiều-bảng-trong-select)
   - [JOIN](#join)
   - [INNER JOIN, LEFT JOIN](#inner-join-left-join)
5. [Các ví dụ thực tế với SELECT](#5-các-ví-dụ-thực-tế-với-select)
6. [Lưu ý và thực hành tốt](#6-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về câu lệnh SELECT

#### SELECT là gì?

Câu lệnh `SELECT` trong SQL Server là câu lệnh được sử dụng để truy vấn và lấy dữ liệu từ một hoặc nhiều bảng trong cơ sở dữ liệu. Đây là câu lệnh cơ bản và quan trọng nhất trong SQL vì nó cho phép người dùng truy xuất thông tin cần thiết từ các bảng.

#### Lợi ích của câu lệnh SELECT

- **Truy xuất dữ liệu**: Cho phép lấy dữ liệu từ các bảng, phù hợp cho việc phân tích và xử lý dữ liệu.
- **Lọc dữ liệu**: Sử dụng kết hợp với các điều kiện để chỉ lấy các bản ghi cần thiết.
- **Sắp xếp và nhóm dữ liệu**: Giúp người dùng có thể trình bày dữ liệu theo cách dễ hiểu.

#### Câu lệnh SELECT hoạt động như thế nào?

Khi thực thi câu lệnh `SELECT`, SQL Server thực hiện các bước sau:

1. **Tìm kiếm bảng**: Xác định bảng dữ liệu mà câu lệnh `SELECT` truy vấn.
2. **Lọc dữ liệu**: Nếu có, áp dụng các điều kiện từ `WHERE` để lọc các bản ghi cần thiết.
3. **Sắp xếp kết quả**: Nếu có `ORDER BY`, dữ liệu sẽ được sắp xếp theo yêu cầu.
4. **Trả về kết quả**: Sau khi xử lý, kết quả được trả về cho người dùng.

---

### 2. Cú pháp cơ bản của câu lệnh SELECT

#### Chọn các cột cụ thể

Câu lệnh `SELECT` có thể được sử dụng để truy vấn một hoặc nhiều cột cụ thể từ bảng.

**Cú pháp**:

```sql
SELECT column1, column2, ...
FROM table_name;
```

**Ví dụ**:

```sql
SELECT first_name, last_name
FROM employees;
```

Trong ví dụ trên, `SELECT` chỉ lấy dữ liệu từ hai cột `first_name` và `last_name` trong bảng `employees`.

#### Chọn tất cả các cột

Nếu bạn muốn lấy tất cả các cột trong bảng, bạn có thể sử dụng ký hiệu `*` thay vì liệt kê từng cột.

**Cú pháp**:

```sql
SELECT *
FROM table_name;
```

**Ví dụ**:

```sql
SELECT *
FROM employees;
```

Câu lệnh này sẽ trả về tất cả các cột trong bảng `employees`.

---

### 3. Các tùy chọn mở rộng của câu lệnh SELECT

#### WHERE

`WHERE` được sử dụng để lọc các bản ghi dựa trên một điều kiện nhất định.

**Cú pháp**:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Ví dụ**:

```sql
SELECT first_name, last_name
FROM employees
WHERE department = 'HR';
```

Câu lệnh này sẽ chỉ lấy dữ liệu của các nhân viên làm việc trong phòng ban `HR`.

#### ORDER BY

`ORDER BY` giúp sắp xếp kết quả theo một hoặc nhiều cột, có thể theo thứ tự tăng dần (ASC) hoặc giảm dần (DESC).

**Cú pháp**:

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC | DESC], column2 [ASC | DESC];
```

**Ví dụ**:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;
```

Câu lệnh này sẽ sắp xếp danh sách nhân viên theo mức lương từ cao xuống thấp.

#### DISTINCT

`DISTINCT` được sử dụng để loại bỏ các bản ghi trùng lặp trong kết quả truy vấn.

**Cú pháp**:

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

**Ví dụ**:

```sql
SELECT DISTINCT department
FROM employees;
```

Câu lệnh này sẽ trả về danh sách các phòng ban mà không bị trùng lặp.

---

### 4. Kết hợp nhiều bảng trong SELECT

#### JOIN

`JOIN` là một kỹ thuật trong SQL dùng để kết hợp dữ liệu từ nhiều bảng dựa trên mối quan hệ giữa các bảng đó.

**Cú pháp**:

```sql
SELECT column1, column2, ...
FROM table1
JOIN table2
ON table1.column = table2.column;
```

#### INNER JOIN, LEFT JOIN

- **INNER JOIN**: Trả về các bản ghi có sự kết hợp khớp giữa hai bảng.
- **LEFT JOIN**: Trả về tất cả các bản ghi từ bảng bên trái và các bản ghi khớp từ bảng bên phải.

**Ví dụ với INNER JOIN**:

```sql
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;
```

**Ví dụ với LEFT JOIN**:

```sql
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;
```

Câu lệnh `LEFT JOIN` sẽ trả về tất cả các nhân viên, kể cả những người không có phòng ban tương ứng.

---

### 5. Các ví dụ thực tế với SELECT

#### Truy vấn tất cả thông tin về nhân viên có lương trên 5000

**Câu lệnh SQL**:

```sql
SELECT *
FROM employees
WHERE salary > 5000;
```

**Giải thích**:

- Truy vấn này sẽ trả về tất cả các cột trong bảng `employees` nhưng chỉ với các nhân viên có lương (`salary`) lớn hơn 5000.

**Kết quả có thể xảy ra**:

| employee_id | first_name | last_name | department | salary |
| ----------- | ---------- | --------- | ---------- | ------ |
| 1           | John       | Doe       | HR         | 6000   |
| 2           | Jane       | Smith     | IT         | 7000   |
| 3           | Jim        | Brown     | Sales      | 8000   |

---

#### Truy vấn tên và lương của nhân viên, sắp xếp theo lương giảm dần

**Câu lệnh SQL**:

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;
```

**Giải thích**:

- Truy vấn này sẽ trả về các nhân viên với tên và lương của họ, sắp xếp theo lương từ cao đến thấp.

**Kết quả có thể xảy ra**:

| first_name | last_name | salary |
| ---------- | --------- | ------ |
| Jim        | Brown     | 8000   |
| Jane       | Smith     | 7000   |
| John       | Doe       | 6000   |

---

#### Truy vấn danh sách phòng ban mà không bị trùng lặp

**Câu lệnh SQL**:

```sql
SELECT DISTINCT department
FROM employees;
```

**Giải thích**:

- Truy vấn này sẽ trả về danh sách các phòng ban trong công ty mà không có sự trùng lặp.

**Kết quả có thể xảy ra**:

| department |
| ---------- |
| HR         |
| IT         |
| Sales      |

---

#### Truy vấn danh sách nhân viên cùng với tên phòng ban của họ

**Câu lệnh SQL**:

```sql
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.department_id;
```

**Giải thích**:

- Truy vấn này sẽ kết hợp bảng `employees` và bảng `departments`, trả về tên của nhân viên và tên phòng ban mà họ thuộc về.

**Kết quả có thể xảy ra**:

| first_name | last_name | department_name |
| ---------- | --------- | --------------- |
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Jim        | Brown     | Sales           |

---

#### Truy vấn danh sách nhân viên và tên phòng ban của họ, bao gồm cả những nhân viên không thuộc phòng ban nào (LEFT JOIN)

**Câu lệnh SQL**:

```sql
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
LEFT JOIN departments
ON employees.department_id = departments.department_id;
```

**Giải thích**:

- Truy vấn này sử dụng `LEFT JOIN`, vì vậy nó sẽ trả về tất cả các nhân viên, kể cả những người không thuộc phòng ban nào. Nếu nhân viên không có phòng ban, cột `department_name` sẽ có giá trị NULL.

**Kết quả có thể xảy ra**:

| first_name | last_name | department_name |
| ---------- | --------- | --------------- |
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Jim        | Brown     | Sales           |
| Bob        | White     | NULL            |

---

#### Truy vấn danh sách nhân viên có tên bắt đầu bằng "J", sắp xếp theo họ (last_name)

**Câu lệnh SQL**:

```sql
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE 'J%'
ORDER BY last_name ASC;
```

**Giải thích**:

- Truy vấn này sẽ chỉ trả về các nhân viên có tên bắt đầu bằng chữ cái "J" và sắp xếp kết quả theo họ (last_name) theo thứ tự tăng dần.

**Kết quả có thể xảy ra**:

| first_name | last_name |
| ---------- | --------- |
| Jane       | Smith     |
| Jim        | Brown     |
| John       | Doe       |

### 6. Lưu ý và thực hành tốt

- **Chọn chỉ các cột cần thiết**: Để giảm thiểu tải hệ thống và cải thiện hiệu suất, hãy chọn chỉ các cột mà bạn thực sự cần.
- **Sử dụng `WHERE` để lọc dữ liệu sớm**: Lọc dữ liệu ngay từ đầu thay vì lấy tất cả rồi mới lọc.
- **Chú ý đến hiệu suất khi sử dụng `JOIN`**: Kết hợp nhiều bảng có thể làm giảm hiệu suất, vì vậy hãy chắc chắn sử dụng các chỉ mục và tối ưu câu lệnh của bạn.
- **Sắp xếp dữ liệu một cách hợp lý**: Sử dụng `ORDER BY` để sắp xếp kết quả, nhưng cần chú ý đến hiệu suất nếu bạn đang làm việc với một bộ dữ liệu lớn.
