# Inner Join trong SQL Server

## Mục Lục

1. [Tổng quan về Inner Join](#1-tổng-quan-về-inner-join)
   - [Inner Join là gì?](#inner-join-là-gì)
   - [Lợi ích và ứng dụng của Inner Join](#lợi-ích-và-ứng-dụng-của-inner-join)
   - [Cách hoạt động của Inner Join](#cách-hoạt-động-của-inner-join)
2. [Cú pháp và cách sử dụng Inner Join](#2-cú-pháp-và-cách-sử-dụng-inner-join)
   - [Cú pháp Inner Join cơ bản](#cú-pháp-inner-join-cơ-bản)
   - [Ví dụ thực tế sử dụng Inner Join](#ví-dụ-thực-tế-sử-dụng-inner-join)
3. [Kết hợp với các mệnh đề khác](#3-kết-hợp-với-các-mệnh-đề-khác)
   - [Inner Join với WHERE](#inner-join-với-where)
   - [Inner Join với ORDER BY](#inner-join-với-order-by)
   - [Inner Join với GROUP BY](#inner-join-với-group-by)
4. [Lưu ý và thực hành tốt](#4-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Inner Join

#### Inner Join là gì?

**Inner Join** là một loại phép kết nối trong SQL, cho phép bạn kết hợp các bản ghi từ hai hoặc nhiều bảng dựa trên một điều kiện chung. Điều kiện này thường là sự so khớp giữa các cột có mối quan hệ với nhau trong các bảng. 

Kết quả của một **Inner Join** chỉ chứa các bản ghi mà có sự trùng khớp giữa các bảng. Nói cách khác, nếu không có sự trùng khớp giữa hai bảng ở các cột được kết nối, bản ghi đó sẽ không xuất hiện trong kết quả.

Ví dụ, nếu bạn kết nối bảng `employees` với bảng `departments` qua cột `department_id`, **Inner Join** sẽ chỉ trả về các bản ghi có `department_id` tồn tại ở cả hai bảng.

![Inner Join](/assets/images/sql-joins-venn-diagrams-inner-join.webp)

#### Lợi ích và ứng dụng của Inner Join

- **Lọc dữ liệu chính xác**: Giúp bạn chỉ lấy những dữ liệu có mối quan hệ rõ ràng giữa các bảng. Điều này hữu ích trong việc chỉ lấy các bản ghi có sự liên kết logic giữa các bảng.
- **Tối ưu hóa truy vấn**: Bằng cách chỉ lấy các bản ghi có sự kết hợp hợp lệ, bạn sẽ giảm thiểu dữ liệu không cần thiết và cải thiện hiệu suất của các truy vấn.
- **Ứng dụng trong phân tích dữ liệu**: Inner Join thường được sử dụng trong các ứng dụng phân tích dữ liệu khi bạn muốn kết hợp thông tin từ nhiều bảng có quan hệ logic với nhau (ví dụ: kết hợp thông tin của nhân viên và phòng ban).

#### Cách hoạt động của Inner Join

Inner Join hoạt động bằng cách đối chiếu các bản ghi trong hai bảng theo một điều kiện nhất định (thường là cột chung giữa hai bảng). Nếu điều kiện này đúng, các bản ghi này sẽ được kết hợp lại với nhau và xuất hiện trong kết quả. Nếu điều kiện không thỏa mãn, bản ghi sẽ bị loại khỏi kết quả.

Ví dụ:
- Nếu bạn có bảng `employees` và bảng `departments`, và bạn thực hiện một Inner Join giữa hai bảng này dựa trên cột `department_id`, kết quả trả về sẽ chỉ bao gồm những nhân viên thuộc các phòng ban có trong cả hai bảng.

---

### 2. Cú pháp và cách sử dụng Inner Join

#### Cú pháp Inner Join cơ bản

Cú pháp của **Inner Join** trong SQL như sau:

```sql
SELECT column1, column2, ...
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

Trong đó:

- `table1` và `table2` là tên của các bảng mà bạn muốn kết nối.
- `column1, column2, ...` là các cột mà bạn muốn chọn từ kết quả của phép kết nối.
- `ON table1.column = table2.column` là điều kiện để kết nối hai bảng, thường là sự so khớp giữa các cột có liên quan trong hai bảng.

**Lưu ý**: `INNER JOIN` có thể viết tắt là `JOIN`. Nếu không có tiền tố `INNER`, SQL Server mặc định sẽ thực hiện phép `INNER JOIN`.

#### Ví dụ thực tế sử dụng Inner Join

Giả sử bạn có hai bảng: `employees` và `departments`. 

**Bảng employees**:

| employee_id | first_name | last_name | department_id |
| ----------- | ---------- | --------- | ------------- |
| 1           | John       | Doe       | 1             |
| 2           | Jane       | Smith     | 2             |
| 3           | Bob        | Brown     | 1             |
| 4           | Alice      | Green     | 3             |

**Bảng departments**:

| department_id | department_name |
| ------------- | --------------- |
| 1             | HR              |
| 2             | IT              |
| 3             | Finance         |

**Câu lệnh SQL**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
| ---------- | --------- | --------------- |
| John       | Doe       | HR              |
| Jane       | Smith     | IT              |
| Bob        | Brown     | HR              |
| Alice      | Green     | Finance         |

Trong ví dụ này, `INNER JOIN` kết nối bảng `employees` với bảng `departments` dựa trên cột `department_id`. Kết quả trả về chỉ chứa những nhân viên có phòng ban hợp lệ trong bảng `departments`.

---

### 3. Kết hợp với các mệnh đề khác

#### Inner Join với WHERE

Mệnh đề `WHERE` có thể được kết hợp với `INNER JOIN` để lọc các kết quả sau khi kết nối các bảng. Điều này giúp bạn lấy ra những bản ghi thỏa mãn các điều kiện bổ sung.

**Ví dụ**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_name = 'HR';
```

**Kết quả giả định**:

| first_name | last_name | department_name |
| ---------- | --------- | --------------- |
| John       | Doe       | HR              |
| Bob        | Brown     | HR              |

Trong ví dụ này, chỉ những nhân viên thuộc phòng ban "HR" mới được trả về sau khi kết hợp dữ liệu từ hai bảng.

#### Inner Join với ORDER BY

Bạn có thể sắp xếp kết quả trả về của `INNER JOIN` bằng cách sử dụng mệnh đề `ORDER BY`. Điều này giúp bạn kiểm soát cách hiển thị kết quả.

**Ví dụ**:

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
ORDER BY e.first_name;
```

**Kết quả giả định**:

| first_name | last_name | department_name |
| ---------- | --------- | --------------- |
| Alice      | Green     | Finance         |
| Bob        | Brown     | HR              |
| Jane       | Smith     | IT              |
| John       | Doe       | HR              |

Trong ví dụ trên, kết quả của `INNER JOIN` được sắp xếp theo tên nhân viên.

#### Inner Join với GROUP BY

Bạn có thể kết hợp `INNER JOIN` với `GROUP BY` để nhóm các bản ghi theo một cột và thực hiện các phép toán tổng hợp (như `COUNT`, `SUM`, `AVG`, v.v.).

**Ví dụ**:

```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
GROUP BY d.department_name;
```

**Kết quả giả định**:

| department_name | employee_count |
| --------------- | -------------- |
| HR              | 2              |
| IT              | 1              |
| Finance         | 1              |

Trong ví dụ này, chúng ta nhóm các nhân viên theo phòng ban và đếm số nhân viên trong mỗi phòng ban.

---

### 4. Lưu ý và thực hành tốt

- **Hiệu suất**: `INNER JOIN` giúp giảm dữ liệu không cần thiết bằng cách chỉ trả về các bản ghi có sự trùng khớp giữa các bảng. Tuy nhiên, nếu các bảng có kích thước lớn, bạn cần đảm bảo rằng các cột kết nối đã được chỉ mục (indexed) để tối ưu hóa hiệu suất.
- **Mối quan hệ giữa các bảng**: Khi sử dụng `INNER JOIN`, hãy chắc chắn rằng các cột bạn kết nối có mối quan hệ rõ ràng và hợp lý. Nếu không, bạn có thể nhận được kết quả không chính xác hoặc thậm chí bỏ sót dữ liệu quan trọng.
- **Lọc dữ liệu**: Mệnh đề `WHERE` có thể giúp bạn lọc các bản ghi sau khi kết nối bảng. Hãy

 sử dụng nó khi bạn cần thêm điều kiện cụ thể cho các kết quả của mình.
