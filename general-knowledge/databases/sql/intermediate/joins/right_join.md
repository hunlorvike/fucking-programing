# Right Join trong SQL Server

## Mục Lục

1. [Tổng quan về Right Join](#1-tổng-quan-về-right-join)
   - [Right Join là gì?](#right-join-là-gì)
   - [Lợi ích và ứng dụng của Right Join](#lợi-ích-và-ứng-dụng-của-right-join)
   - [Cách hoạt động của Right Join](#cách-hoạt-động-của-right-join)
2. [Cú pháp và cách sử dụng Right Join](#2-cú-pháp-và-cách-sử-dụng-right-join)
   - [Cú pháp Right Join cơ bản](#cú-pháp-right-join-cơ-bản)
   - [Ví dụ thực tế sử dụng Right Join](#ví-dụ-thực-tế-sử-dụng-right-join)
3. [Kết hợp với các mệnh đề khác](#3-kết-hợp-với-các-mệnh-đề-khác)
   - [Right Join với WHERE](#right-join-với-where)
   - [Right Join với ORDER BY](#right-join-với-order-by)
   - [Right Join với GROUP BY](#right-join-với-group-by)
4. [Lưu ý và thực hành tốt](#4-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Right Join

#### Right Join là gì?

**Right Join** (hay **Right Outer Join**) là một loại phép kết nối trong SQL, hoạt động tương tự như **Left Join**, nhưng với một sự khác biệt quan trọng: **Right Join** sẽ trả về tất cả các bản ghi từ bảng bên phải (bảng thứ hai trong phép kết nối) và chỉ các bản ghi tương ứng từ bảng bên trái (bảng đầu tiên). Nếu không có bản ghi tương ứng từ bảng bên trái, kết quả trả về sẽ chứa giá trị `NULL` cho các cột từ bảng bên trái.

Cụ thể, **Right Join** đảm bảo rằng tất cả các bản ghi từ bảng bên phải sẽ có mặt trong kết quả, dù có hoặc không có bản ghi tương ứng trong bảng bên trái.

![Right Join](/assets/images/sql-joins-venn-diagrams-right-outer-join.webp)

#### Lợi ích và ứng dụng của Right Join

- **Giữ lại tất cả dữ liệu từ bảng bên phải**: `Right Join` rất hữu ích khi bạn muốn lấy tất cả dữ liệu từ bảng bên phải mà không bỏ sót bất kỳ bản ghi nào, dù không có dữ liệu tương ứng trong bảng bên trái.
- **Kết hợp dữ liệu thiếu**: Right Join giúp bạn kết hợp dữ liệu từ hai bảng khi có thể có một số giá trị không tồn tại trong bảng bên trái, nhưng bạn vẫn muốn giữ lại các bản ghi từ bảng bên phải.
- **Xử lý dữ liệu thiếu trong bảng bên trái**: Nếu bảng bên trái thiếu dữ liệu mà bạn muốn giữ lại từ bảng bên phải, `Right Join` là lựa chọn thích hợp.

#### Cách hoạt động của Right Join

Right Join hoạt động bằng cách lấy tất cả các bản ghi từ bảng bên phải (bảng thứ hai trong câu truy vấn) và kết nối với bảng bên trái (bảng đầu tiên) nếu có bản ghi tương ứng. Nếu không có bản ghi tương ứng từ bảng bên trái, SQL Server sẽ trả về giá trị `NULL` cho các cột của bảng bên trái.

- Nếu có một bản ghi trong bảng bên phải không tìm thấy bản ghi tương ứng trong bảng bên trái, SQL sẽ trả về bản ghi từ bảng bên phải với các giá trị của bảng bên trái là `NULL`.
- Nếu có một bản ghi trong bảng bên phải có một hoặc nhiều bản ghi tương ứng trong bảng bên trái, SQL sẽ kết nối tất cả những bản ghi đó lại và trả về kết quả.

---

### 2. Cú pháp và cách sử dụng Right Join

#### Cú pháp Right Join cơ bản

Cú pháp của **Right Join** trong SQL như sau:

```sql
SELECT column1, column2, ...
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

Trong đó:

- `table1` và `table2` là tên của các bảng mà bạn muốn kết nối.
- `column1, column2, ...` là các cột bạn muốn chọn từ kết quả của phép kết nối.
- `ON table1.column = table2.column` là điều kiện để kết nối hai bảng, thường là sự so khớp giữa các cột có liên quan trong hai bảng.

**Lưu ý**: `RIGHT JOIN` có thể viết tắt là `RIGHT OUTER JOIN`. Cả hai đều thực hiện cùng một thao tác.

#### Ví dụ thực tế sử dụng Right Join

Giả sử bạn có hai bảng: `employees` và `departments`.

**Bảng employees**:

| employee_id | first_name | last_name | department_id |
| ----------- | ---------- | --------- | ------------- |
| 1           | John       | Doe       | 1             |
| 2           | Jane       | Smith     | 2             |
| 3           | Bob        | Brown     | NULL          |
| 4           | Alice      | Green     | 3             |

**Bảng departments**:

| department_id | department_name |
| ------------- | --------------- |
| 1             | HR              |
| 2             | IT              |
| 3             | Finance         |
| 4             | Marketing       |

**Câu lệnh SQL**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
| ---------- | --------- | --------------- |
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Alice      | Green     | Finance         |
| NULL       | NULL      | Marketing       |

Trong ví dụ trên, kết quả của `RIGHT JOIN` trả về tất cả các phòng ban từ bảng `departments`. Các phòng ban có nhân viên liên kết sẽ hiển thị thông tin nhân viên, còn phòng ban không có nhân viên (như `Marketing`) sẽ trả về giá trị `NULL` cho các cột từ bảng `employees`.

---

### 3. Kết hợp với các mệnh đề khác

#### Right Join với WHERE

Mệnh đề `WHERE` có thể được sử dụng kết hợp với `RIGHT JOIN` để lọc kết quả sau khi thực hiện phép kết nối. Tuy nhiên, bạn cần lưu ý rằng nếu bạn chỉ lọc các bản ghi có giá trị không phải `NULL` từ bảng bên trái, kết quả có thể trở thành một phép `INNER JOIN`.

**Ví dụ**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id
WHERE e.first_name IS NOT NULL;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
| ---------- | --------- | --------------- |
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Alice      | Green     | Finance         |

Trong ví dụ này, mệnh đề `WHERE` lọc ra các bản ghi có nhân viên, vì vậy kết quả chỉ bao gồm các phòng ban có nhân viên.

#### Right Join với ORDER BY

Mệnh đề `ORDER BY` có thể được sử dụng để sắp xếp kết quả trả về sau khi thực hiện phép `RIGHT JOIN`.

**Ví dụ**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id
ORDER BY d.department_name;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
| ---------- | --------- | --------------- |
| Alice      | Green     | Finance         |
| Jane       | Smith     | IT              |
| John       | Doe       | HR              |
| NULL       | NULL      | Marketing       |

Trong ví dụ này, chúng ta sắp xếp kết quả theo tên phòng ban (`department_name`).

#### Right Join với GROUP BY

Kết hợp `RIGHT JOIN` với `GROUP BY` giúp bạn nhóm các kết quả theo một cột và thực hiện các phép toán tổng hợp (như `COUNT`, `SUM`, `AVG`, v.v.).

**Ví dụ**:

```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name;
```

**Kết quả giả định**:

| department_name | employee_count |
| --------------- | -------------- |
| HR              | 1              |
| IT              | 1              |
| Finance         | 1              |
| Marketing       | 0              |

Ở đây, kết quả trả về số lượng nhân viên trong từng phòng ban, bao gồm cả phòng ban không có nhân viên (`Marketing` có `0` nhân viên).

---

### 4. Lưu ý và thực hành tốt

- **Hiệu suất**: Giống như các phép kết nối khác, việc sử dụng `RIGHT JOIN` trên các bảng lớn có thể ảnh hưởng đến hiệu suất của truy vấn. Hãy đảm bảo rằng các bảng có chỉ mục hợp lý để tối ưu hóa hiệu suất.
- **Giá trị NULL**: Khi sử dụng `RIGHT JOIN`, các giá trị `NULL` có thể xuất hiện trong các cột của bảng bên trái nếu không

 có bản ghi tương ứng. Cần phải xử lý các giá trị `NULL` khi làm việc với các phép toán hoặc điều kiện lọc.
- **Sự tương đương với Left Join**: Bạn có thể thay đổi `RIGHT JOIN` thành `LEFT JOIN` và đổi vị trí các bảng, vì chúng hoạt động tương tự, chỉ khác về việc giữ lại bảng nào.
