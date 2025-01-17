# Left Join trong SQL Server

## Mục Lục

1. [Tổng quan về Left Join](#1-tổng-quan-về-left-join)
    - [Left Join là gì?](#left-join-là-gì)
    - [Lợi ích và ứng dụng của Left Join](#lợi-ích-và-ứng-dụng-của-left-join)
    - [Cách hoạt động của Left Join](#cách-hoạt-động-của-left-join)
2. [Cú pháp và cách sử dụng Left Join](#2-cú-pháp-và-cách-sử-dụng-left-join)
    - [Cú pháp Left Join cơ bản](#cú-pháp-left-join-cơ-bản)
    - [Ví dụ thực tế sử dụng Left Join](#ví-dụ-thực-tế-sử-dụng-left-join)
3. [Kết hợp với các mệnh đề khác](#3-kết-hợp-với-các-mệnh-đề-khác)
    - [Left Join với WHERE](#left-join-với-where)
    - [Left Join với ORDER BY](#left-join-với-order-by)
    - [Left Join với GROUP BY](#left-join-với-group-by)
4. [Lưu ý và thực hành tốt](#4-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Left Join

#### Left Join là gì?

**Left Join** (hay **Left Outer Join**) là một loại phép kết nối trong SQL, cho phép bạn kết hợp dữ liệu từ hai bảng dựa
trên một điều kiện chung. Tuy nhiên, khác với `INNER JOIN`, **Left Join** sẽ trả về tất cả các bản ghi từ bảng bên
trái (bảng đầu tiên trong phép kết nối) và chỉ những bản ghi tương ứng từ bảng bên phải (bảng thứ hai trong phép kết
nối). Nếu không có bản ghi nào phù hợp ở bảng bên phải, kết quả trả về sẽ chứa giá trị `NULL` cho các cột từ bảng bên
phải.

Nói cách khác, `LEFT JOIN` luôn đảm bảo rằng mọi bản ghi từ bảng bên trái đều được trả về, dù có hoặc không có bản ghi
tương ứng trong bảng bên phải.

![Left Join](/assets/images/sql-joins-venn-diagrams-left-outer-join.webp)

#### Lợi ích và ứng dụng của Left Join

- **Giữ lại tất cả dữ liệu từ bảng bên trái**: Left Join rất hữu ích khi bạn muốn lấy tất cả dữ liệu từ bảng bên trái mà
  không bỏ sót bản ghi nào, dù không có dữ liệu tương ứng từ bảng bên phải.
- **Kết hợp dữ liệu không hoàn chỉnh**: Left Join giúp bạn kết hợp dữ liệu từ hai bảng khi có thể có một số giá trị
  không tồn tại trong bảng bên phải, nhưng bạn vẫn muốn giữ lại các bản ghi từ bảng bên trái.
- **Xử lý dữ liệu bị thiếu**: Khi làm việc với dữ liệu bị thiếu hoặc không đầy đủ, Left Join giúp bạn dễ dàng phát hiện
  các bản ghi không có dữ liệu liên quan trong bảng thứ hai.

#### Cách hoạt động của Left Join

Left Join hoạt động bằng cách lấy tất cả các bản ghi từ bảng bên trái (bảng đầu tiên trong câu truy vấn) và kết nối với
bảng bên phải (bảng thứ hai) nếu có bản ghi tương ứng. Nếu không có bản ghi tương ứng từ bảng bên phải, SQL Server sẽ
trả về giá trị `NULL` cho các cột của bảng bên phải.

- Nếu có một bản ghi trong bảng bên trái không tìm thấy bản ghi tương ứng trong bảng bên phải, SQL sẽ trả về bản ghi từ
  bảng bên trái với các giá trị của bảng bên phải là `NULL`.
- Nếu có một bản ghi trong bảng bên trái có một hoặc nhiều bản ghi tương ứng trong bảng bên phải, SQL sẽ kết nối tất cả
  những bản ghi đó lại và trả về kết quả.

---

### 2. Cú pháp và cách sử dụng Left Join

#### Cú pháp Left Join cơ bản

Cú pháp của **Left Join** trong SQL như sau:

```sql
SELECT column1, column2, ...
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

Trong đó:

- `table1` và `table2` là tên của các bảng mà bạn muốn kết nối.
- `column1, column2, ...` là các cột mà bạn muốn chọn từ kết quả của phép kết nối.
- `ON table1.column = table2.column` là điều kiện để kết nối hai bảng, thường là sự so khớp giữa các cột có liên quan
  trong hai bảng.

**Lưu ý**: `LEFT JOIN` có thể viết tắt là `LEFT OUTER JOIN`. Cả hai đều thực hiện cùng một thao tác.

#### Ví dụ thực tế sử dụng Left Join

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

**Câu lệnh SQL**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
|------------|-----------|-----------------|
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Bob        | Brown     | NULL            |
| Alice      | Green     | Finance         |

Trong ví dụ trên, kết quả của `LEFT JOIN` trả về tất cả các nhân viên từ bảng `employees`. Nhân viên Bob không có
`department_id`, do đó, giá trị của `department_name` sẽ là `NULL`.

---

### 3. Kết hợp với các mệnh đề khác

#### Left Join với WHERE

Mệnh đề `WHERE` có thể được sử dụng kết hợp với `LEFT JOIN` để lọc kết quả sau khi thực hiện phép kết nối. Tuy nhiên,
bạn cần lưu ý rằng nếu bạn chỉ lọc các bản ghi có giá trị không phải `NULL` từ bảng bên phải, kết quả sẽ trở thành một
phép `INNER JOIN`.

**Ví dụ**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_name IS NOT NULL;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
|------------|-----------|-----------------|
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Alice      | Green     | Finance         |

Trong ví dụ này, mặc dù chúng ta sử dụng `LEFT JOIN`, nhưng mệnh đề `WHERE` lọc ra các bản ghi có phòng ban hợp lệ, vì
vậy kết quả chỉ bao gồm những nhân viên có phòng ban.

#### Left Join với ORDER BY

Mệnh đề `ORDER BY` có thể được sử dụng để sắp xếp kết quả trả về sau khi thực hiện phép `LEFT JOIN`.

**Ví dụ**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id
ORDER BY e.first_name;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
|------------|-----------|-----------------|
| Alice      | Green     | Finance         |
| Bob        | Brown     | NULL            |
| Jane       | Smith     | IT              |
| John       | Doe       | HR              |

Trong ví dụ này, chúng ta sắp xếp kết quả theo tên nhân viên (`first_name`).

#### Left Join với GROUP BY

Kết hợp `LEFT JOIN` với `GROUP BY` giúp bạn nhóm các kết quả theo một cột và thực hiện các phép toán tổng hợp (như
`COUNT`, `SUM`, `AVG`, v.v.).

**Ví dụ**:

```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name;
```

**Kết quả giả định**:

| department_name | employee_count |
|-----------------|----------------|
| HR              | 1              |
| IT              | 1              |
| Finance         | 1              |
| NULL            | 1              |

Ở đây, kết quả trả về số lượng nhân viên trong từng phòng ban, bao gồm cả những nhân viên không có phòng ban (dòng
`NULL`).

---

### 4. Lưu ý và thực hành tốt

- **Hiệu suất**: Mặc dù `LEFT JOIN` trả về tất cả bản ghi từ bảng bên trái, việc sử dụng nó trong các truy vấn với nhiều
  bảng hoặc bảng lớn có thể làm giảm hiệu suất. Hãy chắc chắn rằng các bảng đã được chỉ mục hợp lý để tối ưu hóa hiệu
  suất.
- **Giá trị NULL**: Khi sử dụng `LEFT JOIN`, hãy lưu ý rằng nếu không có bản ghi tương ứng trong bảng bên phải,

giá trị trả về sẽ là `NULL`. Do đó, hãy xử lý các giá trị `NULL` khi cần thiết, đặc biệt trong các phép toán hoặc điều
kiện.

- **Ứng dụng phân tích dữ liệu**: `LEFT JOIN` rất hữu ích khi bạn làm việc với dữ liệu phân tích, khi muốn giữ lại tất
  cả các bản ghi từ một bảng và kết hợp thông tin từ một bảng khác có thể thiếu dữ liệu.
