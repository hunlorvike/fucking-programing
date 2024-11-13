# Filtering (WHERE) trong SQL Server

## Mục Lục

1. [Tổng quan về Filtering với WHERE](#1-tổng-quan-về-filtering-với-where)
   - [WHERE là gì?](#where-là-gì)
   - [Lợi ích của Filtering](#lợi-ích-của-filtering)
   - [WHERE hoạt động như thế nào?](#where-hoạt-động-như-thế-nào)
2. [Cú pháp của WHERE](#2-cú-pháp-của-where)
   - [Sử dụng điều kiện đơn giản](#sử-dụng-điều-kiện-đơn-giản)
   - [Kết hợp nhiều điều kiện](#kết-hợp-nhiều-điều-kiện)
3. [Các toán tử trong WHERE](#3-các-toán-tử-trong-where)
   - [Toán tử so sánh](#toán-tử-so-sánh)
   - [Toán tử logic](#toán-tử-logic)
   - [Toán tử LIKE](#toán-tử-like)
   - [Toán tử BETWEEN](#toán-tử-between)
   - [Toán tử IN](#toán-tử-in)
4. [Kết hợp WHERE với các mệnh đề khác](#4-kết-hợp-where-với-các-mệnh-đề-khác)
   - [WHERE và SELECT](#where-và-select)
   - [WHERE và JOIN](#where-và-join)
5. [Các ví dụ thực tế với WHERE](#5-các-ví-dụ-thực-tế-với-where)
6. [Lưu ý và thực hành tốt](#6-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Filtering với WHERE

#### WHERE là gì?

Mệnh đề `WHERE` trong SQL Server được sử dụng để lọc các bản ghi dựa trên các điều kiện xác định. Nó giúp bạn chỉ lấy các bản ghi phù hợp với các tiêu chí mà bạn đã đặt ra. `WHERE` là một phần quan trọng trong SQL vì nó giúp xác định chính xác dữ liệu mà bạn muốn truy vấn.

#### Lợi ích của Filtering

- **Lọc dữ liệu**: Giúp giảm khối lượng dữ liệu được truy xuất từ cơ sở dữ liệu, chỉ lấy những bản ghi cần thiết.
- **Tăng hiệu suất**: Việc sử dụng `WHERE` để lọc dữ liệu ngay từ đầu giúp tiết kiệm tài nguyên hệ thống và thời gian xử lý.
- **Tùy chỉnh kết quả truy vấn**: Bạn có thể dễ dàng điều chỉnh kết quả truy vấn theo các tiêu chí cụ thể (ví dụ: theo ngày, theo giá trị cụ thể, v.v.).

#### WHERE hoạt động như thế nào?

1. **Nhận diện điều kiện**: SQL Server sẽ đánh giá điều kiện trong mệnh đề `WHERE` để xác định các bản ghi cần lọc.
2. **Lọc dữ liệu**: Các bản ghi thỏa mãn điều kiện trong `WHERE` sẽ được trả về trong kết quả.
3. **Trả về kết quả**: Dữ liệu chỉ bao gồm các bản ghi thỏa mãn điều kiện mà bạn đã chỉ định.

---

### 2. Cú pháp của WHERE

#### Sử dụng điều kiện đơn giản

Cú pháp cơ bản của `WHERE` là:

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

Trong ví dụ này, `WHERE department = 'HR'` lọc các nhân viên thuộc phòng ban `HR`.

#### Kết hợp nhiều điều kiện

Bạn có thể kết hợp nhiều điều kiện trong mệnh đề `WHERE` bằng cách sử dụng các toán tử logic như `AND`, `OR`.

**Ví dụ**:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE department = 'HR' AND salary > 5000;
```

Trong ví dụ này, câu lệnh sẽ trả về các nhân viên thuộc phòng ban `HR` và có lương trên 5000.

---

### 3. Các toán tử trong WHERE

#### Toán tử so sánh

- `=`: Bằng
- `!=` hoặc `<>`: Khác
- `>`: Lớn hơn
- `<`: Nhỏ hơn
- `>=`: Lớn hơn hoặc bằng
- `<=`: Nhỏ hơn hoặc bằng

**Ví dụ**:

```sql
SELECT first_name, last_name
FROM employees
WHERE salary > 5000;
```

Câu lệnh này sẽ lấy danh sách nhân viên có lương lớn hơn 5000.

#### Toán tử logic

- `AND`: Điều kiện cả hai đều đúng
- `OR`: Điều kiện một trong hai đúng
- `NOT`: Lật ngược điều kiện

**Ví dụ với AND**:

```sql
SELECT first_name, last_name
FROM employees
WHERE department = 'HR' AND salary > 5000;
```

**Ví dụ với OR**:

```sql
SELECT first_name, last_name
FROM employees
WHERE department = 'HR' OR department = 'IT';
```

**Ví dụ với NOT**:

```sql
SELECT first_name, last_name
FROM employees
WHERE NOT department = 'HR';
```

#### Toán tử LIKE

`LIKE` được sử dụng để tìm kiếm một mẫu chuỗi trong cột. Bạn có thể sử dụng ký tự đại diện `%` để đại diện cho bất kỳ chuỗi ký tự nào và `_` để đại diện cho một ký tự.

**Cú pháp**:

```sql
SELECT column1, column2
FROM table_name
WHERE column1 LIKE 'pattern';
```

**Ví dụ**:

```sql
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE 'A%';
```

Câu lệnh trên sẽ trả về các nhân viên có tên bắt đầu bằng chữ cái 'A'.

#### Toán tử BETWEEN

`BETWEEN` được sử dụng để lọc dữ liệu trong một phạm vi giá trị.

**Cú pháp**:

```sql
SELECT column1, column2
FROM table_name
WHERE column1 BETWEEN value1 AND value2;
```

**Ví dụ**:

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 3000 AND 5000;
```

Câu lệnh này sẽ trả về các nhân viên có mức lương trong khoảng từ 3000 đến 5000.

#### Toán tử IN

`IN` được sử dụng để lọc các giá trị trong một danh sách cụ thể.

**Cú pháp**:

```sql
SELECT column1, column2
FROM table_name
WHERE column1 IN (value1, value2, ...);
```

**Ví dụ**:

```sql
SELECT first_name, last_name
FROM employees
WHERE department IN ('HR', 'IT', 'Sales');
```

Câu lệnh trên sẽ trả về các nhân viên thuộc các phòng ban `HR`, `IT` hoặc `Sales`.

---

### 4. Kết hợp WHERE với các mệnh đề khác

#### WHERE và SELECT

`WHERE` thường được kết hợp với `SELECT` để lọc dữ liệu mà bạn muốn truy vấn từ bảng.

**Ví dụ**:

```sql
SELECT first_name, last_name
FROM employees
WHERE department = 'HR';
```

#### WHERE và JOIN

Mệnh đề `WHERE` cũng có thể được kết hợp với các câu lệnh `JOIN` để lọc dữ liệu khi kết hợp nhiều bảng.

**Ví dụ**:

```sql
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.department_id
WHERE departments.department_name = 'HR';
```

---

### 5. Các ví dụ thực tế với WHERE

#### **1. Truy vấn các nhân viên có mức lương trên 5000**

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 5000;
```

**Kết quả giả định**:

| first_name | last_name | salary |
| ---------- | --------- | ------ |
| John       | Doe       | 6000   |
| Sarah      | Smith     | 7000   |
| Michael    | Johnson   | 8000   |

**Giải thích**: Câu lệnh này sẽ trả về các nhân viên có lương lớn hơn 5000, bao gồm John, Sarah, và Michael.

#### **2. Truy vấn các nhân viên thuộc phòng ban IT hoặc HR**

```sql
SELECT first_name, last_name, department
FROM employees
WHERE department IN ('HR', 'IT');
```

**Kết quả giả định**:

| first_name | last_name | department |
| ---------- | --------- | ---------- |
| Alice      | Brown     | HR         |
| Bob        | White     | IT         |
| Charlie    | Green     | HR         |

**Giải thích**: Câu lệnh này sẽ trả về các nhân viên làm việc tại các phòng ban HR hoặc IT, như Alice, Bob và Charlie.

#### **3. Truy vấn nhân viên có lương nằm trong khoảng từ 3000 đến 5000**

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 3000 AND 5000;
```

**Kết quả giả định**:

| first_name | last_name | salary |
| ---------- | --------- | ------ |
| David      | Williams  | 4500   |
| Emma       | Davis     | 3500   |

**Giải thích**: Câu lệnh này sẽ trả về các nhân viên có mức lương trong khoảng từ 3000 đến 5000, như David và Emma.

#### **4. Truy vấn các nhân viên có tên bắt đầu bằng 'J'**

```sql
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE 'J%';
```

**Kết quả giả định**:

| first_name | last_name |
| ---------- | --------- |
| John       | Doe       |
| Jennifer   | Black     |
| Jake       | White     |

**Giải thích**: Câu lệnh này sẽ trả về các nhân viên có tên bắt đầu bằng chữ 'J', như John, Jennifer và Jake.

#### **5. Truy vấn nhân viên có tuổi lớn hơn 30 và lương lớn hơn 4000**

```sql
SELECT first_name, last_name, age, salary
FROM employees
WHERE age > 30 AND salary > 4000;
```

**Kết quả giả định**:

| first_name | last_name | age | salary |
| ---------- | --------- | --- | ------ |
| Michael    | Johnson   | 35  | 6000   |
| Sarah      | Smith     | 32  | 7000   |

**Giải thích**: Câu lệnh này sẽ trả về các nhân viên có độ tuổi trên 30 và mức lương lớn hơn 4000, như Michael và Sarah.

#### **6. Truy vấn các nhân viên không thuộc phòng ban HR**

```sql
SELECT first_name, last_name, department
FROM employees
WHERE NOT department = 'HR';
```

**Kết quả giả định**:

| first_name | last_name | department |
| ---------- | --------- | ---------- |
| Bob        | White     | IT         |
| Charlie    | Green     | Sales      |

**Giải thích**: Câu lệnh này sẽ trả về các nhân viên không làm việc tại phòng ban HR, như Bob và Charlie.

#### **7. Truy vấn các nhân viên có tên bắt đầu bằng 'J' hoặc 'M'**

```sql
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE 'J%' OR first_name LIKE 'M%';
```

**Kết quả giả định**:

| first_name | last_name |
| ---------- | --------- |
| John       | Doe       |
| Michael    | Johnson   |
| Mary       | Lee       |

**Giải thích**: Câu lệnh này sẽ trả về các nhân viên có tên bắt đầu bằng chữ 'J' hoặc 'M', bao gồm John, Michael và Mary.

---

### 6. Lưu ý và thực hành tốt

Dưới đây là một số lưu ý và mẹo giúp bạn sử dụng mệnh đề `WHERE` hiệu quả hơn:

- **Tránh sử dụng WHERE quá rộng**: Khi sử dụng `WHERE`, tránh các điều kiện quá chung chung. Nếu câu lệnh `WHERE` của bạn quá rộng, nó có thể trả về quá nhiều bản ghi và làm giảm hiệu suất của truy vấn. Hãy sử dụng các điều kiện chính xác và có mục đích rõ ràng để tránh việc xử lý dữ liệu không cần thiết.
- **Lọc sớm**: Việc lọc dữ liệu càng sớm trong quá trình truy vấn sẽ giúp bạn tiết kiệm tài nguyên và thời gian. Ví dụ, nếu bạn chỉ cần một số bản ghi cụ thể, hãy sử dụng `WHERE` càng sớm càng tốt để giảm bớt khối lượng dữ liệu.
- **Cẩn thận khi sử dụng LIKE**: Mặc dù `LIKE` là một toán tử hữu ích để tìm kiếm mẫu chuỗi, nhưng nếu bạn sử dụng ký tự đại diện `%` ở đầu chuỗi tìm kiếm (ví dụ: `LIKE '%abc'`), điều này có thể làm giảm hiệu suất của truy vấn vì SQL Server sẽ phải tìm kiếm toàn bộ bảng thay vì sử dụng chỉ số. Tốt hơn là bạn chỉ nên sử dụng `%` ở cuối chuỗi tìm kiếm.
- **Tối ưu hóa kết quả với IN và BETWEEN**: Các toán tử `IN` và `BETWEEN` có thể giúp bạn viết câu lệnh rõ ràng và dễ hiểu hơn. Những toán tử này không chỉ tối ưu hóa quá trình lọc dữ liệu mà còn giúp viết câu lệnh dễ dàng và ngắn gọn hơn, thay vì phải sử dụng nhiều điều kiện `OR` hoặc toán tử so sánh.
- **Sử dụng parantheses khi kết hợp nhiều điều kiện**: Khi bạn kết hợp nhiều điều kiện với `AND`, `OR`, hoặc các toán tử khác, đừng quên sử dụng dấu ngoặc để đảm bảo các điều kiện được đánh giá theo thứ tự mà bạn mong muốn. Việc này giúp tránh được các lỗi logic không mong muốn trong câu lệnh.

Ví dụ:

```sql
SELECT first_name, last_name, department, salary
FROM employees
WHERE (department = 'HR' OR department = 'IT') AND salary > 5000;
```

**Kết quả giả định**:

| first_name | last_name | department | salary |
| ---------- | --------- | ---------- | ------ |
| John       | Doe       | HR         | 6000   |
| Sarah      | Smith     | IT         | 7000   |

**Giải thích**: Câu lệnh này trả về các nhân viên làm việc tại phòng ban HR hoặc IT và có lương lớn hơn 5000.
