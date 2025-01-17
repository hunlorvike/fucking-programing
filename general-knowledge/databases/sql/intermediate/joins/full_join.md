# Full Join trong SQL Server

## Mục Lục

1. [Tổng quan về Full Join](#1-tổng-quan-về-full-join)
    - [Full Join là gì?](#full-join-là-gì)
    - [Lợi ích và ứng dụng của Full Join](#lợi-ích-và-ứng-dụng-của-full-join)
    - [Cách hoạt động của Full Join](#cách-hoạt-động-của-full-join)
2. [Cú pháp và cách sử dụng Full Join](#2-cú-pháp-và-cách-sử-dụng-full-join)
    - [Cú pháp của Full Join](#cú-pháp-của-full-join)
    - [Ví dụ thực tế sử dụng Full Join](#ví-dụ-thực-tế-sử-dụng-full-join)
3. [Kết hợp với các mệnh đề khác](#3-kết-hợp-với-các-mệnh-đề-khác)
    - [Full Join với WHERE](#full-join-với-where)
    - [Full Join với ORDER BY](#full-join-với-order-by)
    - [Full Join với GROUP BY](#full-join-với-group-by)
4. [Lưu ý và thực hành tốt](#4-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Full Join

#### Full Join là gì?

**Full Join** (hay còn gọi là **Full Outer Join**) trong SQL là một phép kết nối giữa hai bảng mà trả về tất cả các bản
ghi từ cả hai bảng, với các giá trị `NULL` được điền vào các cột không có bản ghi khớp từ một bảng.

Khác với các loại join khác như **Inner Join**, **Left Join**, hoặc **Right Join**, **Full Join** không bỏ qua các bản
ghi không khớp mà sẽ giữ lại tất cả các bản ghi từ cả hai bảng, và khi không có bản ghi khớp giữa hai bảng, cột không
khớp sẽ chứa giá trị `NULL`.

![Full join](/assets/images/sql-joins-venn-diagrams-full-outer-join.webp)

#### Lợi ích và ứng dụng của Full Join

- **Giữ lại tất cả bản ghi từ cả hai bảng**: Full Join hữu ích khi bạn cần kết hợp tất cả dữ liệu từ hai bảng, không
  quan tâm đến việc các bản ghi có khớp nhau hay không.
- **Xử lý dữ liệu không đồng nhất**: Khi bạn làm việc với dữ liệu không hoàn chỉnh từ hai bảng, Full Join cho phép bạn
  xem tất cả các bản ghi và dễ dàng xác định đâu là các bản ghi không có bản ghi tương ứng.
- **Phân tích và báo cáo dữ liệu**: Full Join rất hữu ích trong các báo cáo hoặc phân tích dữ liệu khi bạn cần lấy tất
  cả thông tin, kể cả khi có dữ liệu thiếu trong một trong các bảng.

#### Cách hoạt động của Full Join

**Full Join** kết hợp kết quả của **Left Join** và **Right Join**. Nó trả về tất cả các bản ghi từ cả hai bảng. Khi một
bản ghi trong bảng bên trái không có bản ghi khớp trong bảng bên phải, kết quả sẽ có giá trị `NULL` cho các cột từ bảng
bên phải. Tương tự, khi một bản ghi trong bảng bên phải không có bản ghi khớp trong bảng bên trái, kết quả sẽ có giá trị
`NULL` cho các cột từ bảng bên trái.

---

### 2. Cú pháp và cách sử dụng Full Join

#### Cú pháp của Full Join

```sql
SELECT column1, column2, ...
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;
```

- `column1, column2, ...`: Các cột bạn muốn chọn từ bảng.
- `table1, table2`: Hai bảng bạn muốn kết nối.
- `column`: Cột dùng để nối giữa hai bảng.

#### Ví dụ thực tế sử dụng Full Join

Giả sử bạn có hai bảng: `employees` và `departments`.

**Bảng employees**:

| employee_id | first_name | last_name | department_id |
|-------------|------------|-----------|---------------|
| 1           | John       | Doe       | 1             |
| 2           | Jane       | Smith     | 2             |
| 3           | Bob        | Brown     | NULL          |
| 4           | Alice      | Green     | 3             |

**Bảng departments**:

| department_id | department_name |
|---------------|-----------------|
| 1             | HR              |
| 2             | IT              |
| 3             | Finance         |
| 4             | Marketing       |

#### **1. Full Outer Join**

Câu lệnh SQL:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
|------------|-----------|-----------------|
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Bob        | Brown     | NULL            |
| Alice      | Green     | Finance         |
| NULL       | NULL      | Marketing       |

Ở đây, **Full Outer Join** trả về tất cả các nhân viên và tất cả các phòng ban. Nếu một nhân viên không có phòng ban,
cột `department_name` sẽ là `NULL`, và nếu một phòng ban không có nhân viên, các cột từ bảng `employees` sẽ là `NULL`.

#### **2. Full Outer Join với điều kiện lọc (WHERE)**

Bạn có thể kết hợp **Full Join** với mệnh đề **WHERE** để lọc kết quả. Tuy nhiên, hãy lưu ý rằng nếu bạn muốn loại bỏ
các bản ghi có giá trị `NULL`, bạn sẽ cần sử dụng điều kiện lọc trong mệnh đề **WHERE**.

Câu lệnh SQL:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id
WHERE e.first_name IS NOT NULL AND d.department_name IS NOT NULL;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
|------------|-----------|-----------------|
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Alice      | Green     | Finance         |

Trong trường hợp này, chúng ta chỉ lấy các bản ghi có cả nhân viên và phòng ban tương ứng, loại bỏ các bản ghi có giá
trị `NULL` trong các cột `first_name` hoặc `department_name`.

---

### 3. Kết hợp với các mệnh đề khác

#### Full Join với WHERE

Mệnh đề **WHERE** có thể được sử dụng với **Full Join** để lọc dữ liệu. Bạn có thể lọc các bản ghi có giá trị `NULL`
hoặc các điều kiện khác trong kết quả truy vấn.

**Ví dụ**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id
WHERE e.first_name IS NULL OR d.department_name IS NULL;
```

Câu lệnh trên sẽ chỉ trả về các bản ghi mà hoặc `first_name` hoặc `department_name` có giá trị `NULL`.

#### Full Join với ORDER BY

Bạn có thể sử dụng **ORDER BY** với **Full Join** để sắp xếp kết quả trả về.

**Ví dụ**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id
ORDER BY e.first_name;
```

Câu lệnh trên sẽ sắp xếp kết quả theo tên của nhân viên (`first_name`).

#### Full Join với GROUP BY

Mệnh đề **GROUP BY** có thể được kết hợp với **Full Join** khi bạn muốn nhóm các kết quả theo một hoặc nhiều cột.

**Ví dụ**:

```sql
SELECT d.department_name, COUNT(e.employee_id) AS number_of_employees
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name;
```

Câu lệnh trên sẽ trả về số lượng nhân viên trong mỗi phòng ban. Nếu phòng ban không có nhân viên, kết quả sẽ trả về `0`
cho số lượng nhân viên.

---

### 4. Lưu ý và thực hành tốt

- **Sử dụng Full Join khi cần giữ lại tất cả dữ liệu**: **Full Join** là công cụ mạnh mẽ khi bạn muốn giữ lại tất cả các
  bản ghi từ cả hai bảng, kể cả khi không có bản ghi tương ứng.
- **Cẩn thận với `NULL`**: Khi sử dụng **Full Join**, bạn cần xử lý các giá trị `NULL` khi làm việc với các điều kiện
  lọc hoặc phép toán.
- **Hiệu suất**: Vì **Full Join** yêu cầu xử lý tất cả các bản ghi từ hai bảng, nó có thể tốn nhiều tài nguyên hơn so
  với các loại join khác như **Inner Join** hoặc **Left Join**. Hãy đảm bảo rằng bạn chỉ sử dụng **Full Join** khi thật
  sự cần thiết.
- **Kết hợp với mệnh đề khác**: Hãy kết hợp **Full Join** với các mệnh đề như **WHERE**, **ORDER BY**, hoặc **GROUP BY**
  để tinh chỉnh kết

quả truy vấn của bạn.
