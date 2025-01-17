# Subquery trong SQL Server

## Mục Lục

1. [Tổng quan về Subquery](#1-tổng-quan-về-subquery)
    - [Subquery là gì?](#subquery-là-gì)
    - [Lợi ích và ứng dụng của Subquery](#lợi-ích-và-ứng-dụng-của-subquery)
    - [Cách hoạt động của Subquery](#cách-hoạt-động-của-subquery)
2. [Cú pháp và cách sử dụng Subquery](#2-cú-pháp-và-cách-sử-dụng-subquery)
    - [Subquery trong SELECT](#subquery-trong-select)
    - [Subquery trong WHERE](#subquery-trong-where)
    - [Subquery trong FROM](#subquery-trong-from)
3. [Các loại Subquery](#3-các-loại-subquery)
    - [Subquery tương đương](#subquery-tương-đương)
    - [Subquery trả về một giá trị](#subquery-trả-về-một-giá-trị)
    - [Subquery trả về nhiều giá trị](#subquery-trả-về-nhiều-giá-trị)
4. [Kết hợp với các mệnh đề khác](#4-kết-hợp-với-các-mệnh-đề-khác)
    - [Subquery với IN](#subquery-với-in)
    - [Subquery với EXISTS](#subquery-với-exists)
    - [Subquery với JOIN](#subquery-với-join)
5. [Lưu ý và thực hành tốt](#5-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Subquery

#### Subquery là gì?

**Subquery**, hay còn gọi là **lệnh con** hoặc **truy vấn phụ**, là một truy vấn được lồng bên trong một truy vấn khác.
Truy vấn con này có thể trả về một hoặc nhiều giá trị, và có thể được sử dụng trong các mệnh đề như `SELECT`, `FROM`,
`WHERE`, `HAVING`. Subquery có thể giúp giảm thiểu số lượng câu lệnh SQL hoặc tạo ra các phép tính phức tạp trong một
câu lệnh SQL duy nhất.

Ví dụ, một subquery có thể được sử dụng để lấy giá trị từ một bảng và sử dụng kết quả đó trong một truy vấn khác.

#### Lợi ích và ứng dụng của Subquery

- **Giảm số lượng truy vấn**: Subquery giúp bạn tránh phải viết nhiều câu lệnh SQL bằng cách kết hợp các truy vấn con
  trong một câu lệnh duy nhất.
- **Linh hoạt**: Subquery có thể được sử dụng trong nhiều ngữ cảnh khác nhau như trong các điều kiện lọc (`WHERE`,
  `HAVING`) hoặc trong danh sách trả về (`SELECT`).
- **Tạo các phép tính phức tạp**: Bạn có thể sử dụng subquery để thực hiện các phép tính hoặc lọc dữ liệu phức tạp mà
  không cần phải tách rời các truy vấn.

#### Cách hoạt động của Subquery

Subquery thực thi riêng biệt, trả về kết quả để được sử dụng trong truy vấn chính. Có ba loại subquery phổ biến:
subquery trả về một giá trị, subquery trả về nhiều giá trị, và subquery trả về một bảng kết quả.

- **Subquery trả về một giá trị**: Thường dùng với các toán tử như `=`, `>`, `<`.
- **Subquery trả về nhiều giá trị**: Dùng với các toán tử như `IN`, `ANY`, `ALL`.
- **Subquery trả về bảng**: Thường được sử dụng trong mệnh đề `FROM`.

---

### 2. Cú pháp và cách sử dụng Subquery

#### Subquery trong SELECT

Bạn có thể sử dụng subquery trong mệnh đề `SELECT` để trả về một giá trị cho mỗi bản ghi trong truy vấn chính.

**Ví dụ**:

Giả sử bạn có bảng `employees` và `departments`, và bạn muốn tìm lương của mỗi nhân viên cùng với số lượng nhân viên
trong cùng bộ phận của họ.

**Bảng employees**:

| employee_id | name  | department_id | salary |
|-------------|-------|---------------|--------|
| 1           | Alice | 1             | 5000   |
| 2           | Bob   | 1             | 6000   |
| 3           | Carol | 2             | 7000   |

**Bảng departments**:

| department_id | department_name |
|---------------|-----------------|
| 1             | HR              |
| 2             | IT              |

**Câu lệnh SQL**:

```sql
SELECT name, salary,
    (SELECT COUNT(*) FROM employees e WHERE e.department_id = d.department_id) AS num_employees
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
```

**Kết quả giả định**:

| name  | salary | num_employees |
|-------|--------|---------------|
| Alice | 5000   | 2             |
| Bob   | 6000   | 2             |
| Carol | 7000   | 1             |

Trong ví dụ trên, subquery trong mệnh đề `SELECT` tính số lượng nhân viên trong cùng bộ phận với nhân viên hiện tại.

#### Subquery trong WHERE

Subquery trong mệnh đề `WHERE` được sử dụng để lọc kết quả dựa trên điều kiện trả về từ một truy vấn con.

**Ví dụ**:

```sql
SELECT name, salary
FROM employees
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'HR');
```

**Kết quả giả định**:

| name  | salary |
|-------|--------|
| Alice | 5000   |
| Bob   | 6000   |

Subquery trong `WHERE` trả về `department_id` của bộ phận 'HR' và lọc những nhân viên thuộc bộ phận này.

#### Subquery trong FROM

Subquery trong mệnh đề `FROM` có thể được sử dụng để tạo ra một bảng tạm để truy vấn chính có thể hoạt động trên đó.

**Ví dụ**:

```sql
SELECT department_id, AVG(salary) AS average_salary
FROM (SELECT department_id, salary FROM employees) AS subquery
GROUP BY department_id;
```

**Kết quả giả định**:

| department_id | average_salary |
|---------------|----------------|
| 1             | 5500           |
| 2             | 7000           |

Subquery trong `FROM` tạo ra một bảng tạm chứa thông tin về bộ phận và lương, từ đó tính lương trung bình cho mỗi bộ
phận.

---

### 3. Các loại Subquery

#### Subquery tương đương

Một subquery tương đương trả về kết quả duy nhất cho mỗi điều kiện trong truy vấn chính. Nó thường được sử dụng với các
toán tử như `=`, `>`, `<`.

**Ví dụ**:

```sql
SELECT name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```

Trong ví dụ này, subquery trả về mức lương cao nhất và tìm nhân viên có mức lương đó.

#### Subquery trả về một giá trị

Subquery trả về một giá trị duy nhất, thường được sử dụng trong các mệnh đề như `WHERE` hoặc `SELECT`.

**Ví dụ**:

```sql
SELECT name
FROM employees
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'IT');
```

Subquery trả về `department_id` của bộ phận 'IT', sau đó truy vấn chính sử dụng giá trị này để lọc các nhân viên trong
bộ phận đó.

#### Subquery trả về nhiều giá trị

Subquery trả về một tập hợp các giá trị và có thể được sử dụng với các toán tử như `IN`, `ANY`, `ALL`.

**Ví dụ**:

```sql
SELECT name, salary
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE department_name IN ('HR', 'IT'));
```

Trong ví dụ này, subquery trả về tất cả các `department_id` cho bộ phận 'HR' và 'IT', sau đó lọc các nhân viên thuộc các
bộ phận này.

---

### 4. Kết hợp với các mệnh đề khác

#### Subquery với IN

Mệnh đề `IN` có thể kết hợp với subquery để kiểm tra nếu giá trị của một cột nằm trong tập hợp các giá trị trả về từ
subquery.

**Ví dụ**:

```sql
SELECT name, salary
FROM employees
WHERE department_id IN (SELECT department_id FROM departments WHERE department_name = 'HR');
```

#### Subquery với EXISTS

Mệnh đề `EXISTS` kiểm tra sự tồn tại của kết quả từ subquery và trả về `TRUE` nếu subquery trả về ít nhất một bản ghi.

**Ví dụ**:

```sql
SELECT name, salary
FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE e.department_id = d.department_id AND d.department_name = 'HR');
```

#### Subquery với JOIN

Subquery cũng có thể được sử dụng kết hợp với mệnh đề `JOIN` để thực hiện các phép tính phức tạp.

**Ví dụ**:

```sql
SELECT e.name, e.salary
FROM employees e
JOIN (SELECT department_id FROM departments WHERE department_name = 'HR') d
ON e.department_id = d

.department_id;
```

---

### 5. Lưu ý và thực hành tốt

- **Hiệu suất**: Subquery có thể ảnh hưởng đến hiệu suất, đặc biệt khi subquery trả về một lượng dữ liệu lớn. Cần xem
  xét tối ưu hóa subquery và sử dụng các chỉ mục nếu cần thiết.
- **Đọc và bảo trì mã**: Đôi khi, sử dụng nhiều subquery có thể làm cho mã SQL trở nên phức tạp và khó bảo trì. Cần cân
  nhắc sử dụng các mệnh đề khác như `JOIN` hoặc các phép toán hiệu quả hơn.
- **Tránh lồng subquery quá sâu**: Việc lồng nhiều subquery có thể làm giảm hiệu suất và dễ gây nhầm lẫn. Hãy cố gắng
  giữ các truy vấn con ở mức đơn giản và dễ hiểu.

---

### Tổng kết

Subquery trong SQL Server là một công cụ mạnh mẽ cho phép bạn lồng một truy vấn vào trong truy vấn khác, giúp tạo ra các
phép tính phức tạp hoặc lọc dữ liệu hiệu quả. Tuy nhiên, việc sử dụng subquery cần phải được thực hiện cẩn thận để tránh
ảnh hưởng đến hiệu suất và dễ dàng bảo trì mã nguồn.
