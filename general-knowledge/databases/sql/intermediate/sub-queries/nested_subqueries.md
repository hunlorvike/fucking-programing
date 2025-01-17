# Nested Subqueries trong SQL Server

## Mục Lục

1. [Tổng quan về Nested Subqueries](#1-tổng-quan-về-nested-subqueries)
    - [Nested Subqueries là gì?](#nested-subqueries-là-gì)
    - [Phân loại Subqueries](#phân-loại-subqueries)
2. [Cú pháp và cách sử dụng Nested Subqueries](#2-cú-pháp-và-cách-sử-dụng-nested-subqueries)
    - [Ví dụ cơ bản về Nested Subqueries](#ví-dụ-cơ-bản-về-nested-subqueries)
    - [Nested Subqueries trong các mệnh đề khác nhau](#nested-subqueries-trong-các-mệnh-đề-khác-nhau)
3. [Ứng dụng của Nested Subqueries](#3-ứng-dụng-của-nested-subqueries)
    - [Lọc dữ liệu đa cấp](#lọc-dữ-liệu-đa-cấp)
    - [Tìm kiếm giá trị phức tạp](#tìm-kiếm-giá-trị-phức-tạp)
    - [Kết hợp với các hàm tổng hợp](#kết-hợp-với-các-hàm-tổng-hợp)
4. [Hiệu suất và lưu ý khi sử dụng Nested Subqueries](#4-hiệu-suất-và-lưu-ý-khi-sử-dụng-nested-subqueries)
    - [Vấn đề hiệu suất](#vấn-đề-hiệu-suất)
    - [Các phương án tối ưu hóa](#các-phương-án-tối-ưu-hóa)
5. [Tổng kết](#5-tổng-kết)

---

### 1. Tổng quan về Nested Subqueries

#### Nested Subqueries là gì?

**Nested Subqueries** là các truy vấn con (subqueries) lồng nhau bên trong một truy vấn khác. Một Nested Subquery có thể
được đặt trong một subquery khác, tạo ra các lớp lồng nhau để xử lý các điều kiện hoặc phép tính phức tạp.

Ví dụ:

```sql
SELECT employee_id, name
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = (
        SELECT department_id
        FROM departments
        WHERE department_name = 'Sales'
    )
);
```

Trong ví dụ này:

- Subquery thứ nhất tính `department_id` cho phòng ban "Sales".
- Subquery thứ hai tính mức lương trung bình cho phòng ban đó.
- Truy vấn chính lọc nhân viên có lương cao hơn mức trung bình.

---

#### Phân loại Subqueries

Subqueries, bao gồm cả Nested Subqueries, có thể được phân loại dựa trên cách sử dụng và sự phụ thuộc:

1. **Self-contained Subqueries**:
    - Không phụ thuộc vào truy vấn chính.
    - Có thể chạy độc lập.

   Ví dụ:
   ```sql
   SELECT name
   FROM employees
   WHERE salary > (SELECT AVG(salary) FROM employees);
   ```

2. **Correlated Subqueries**:
    - Phụ thuộc vào truy vấn chính.
    - Mỗi hàng trong truy vấn chính kích hoạt subquery.

   Ví dụ:
   ```sql
   SELECT e1.name
   FROM employees e1
   WHERE e1.salary > (
       SELECT AVG(e2.salary)
       FROM employees e2
       WHERE e2.department_id = e1.department_id
   );
   ```

3. **Nested Subqueries**:
    - Là các subqueries lồng vào nhau nhiều cấp.

---

### 2. Cú pháp và cách sử dụng Nested Subqueries

#### Ví dụ cơ bản về Nested Subqueries

**Ví dụ**: Tìm nhân viên có mức lương cao hơn mức lương trung bình của tất cả nhân viên trong phòng ban "Sales".

**Bảng employees**:
| employee_id | name | department_id | salary |
| ----------- | ----- | ------------- | ------ |
| 1 | Alice | 1 | 5000 |
| 2 | Bob | 1 | 6000 |
| 3 | Carol | 2 | 7000 |
| 4 | David | 3 | 6500 |

**Bảng departments**:
| department_id | department_name |
| ------------- | --------------- |
| 1 | HR |
| 2 | Sales |
| 3 | IT |

**Câu lệnh SQL**:

```sql
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = (
        SELECT department_id
        FROM departments
        WHERE department_name = 'Sales'
    )
);
```

**Kết quả giả định**:
| name | salary |
| ----- | ------ |
| Carol | 7000 |

---

#### Nested Subqueries trong các mệnh đề khác nhau

1. **Trong SELECT**:
   Trả về một giá trị động để thêm vào kết quả.

   **Ví dụ**: Hiển thị nhân viên và tên phòng ban của họ.
   ```sql
   SELECT name, salary,
          (SELECT department_name
           FROM departments
           WHERE departments.department_id = employees.department_id) AS department_name
   FROM employees;
   ```

2. **Trong WHERE**:
   Lọc dữ liệu dựa trên giá trị từ nhiều cấp subqueries.

   **Ví dụ**: Tìm nhân viên có lương cao hơn mức trung bình của phòng ban lớn nhất (nhiều nhân viên nhất).
   ```sql
   SELECT name, salary
   FROM employees
   WHERE salary > (
       SELECT AVG(salary)
       FROM employees
       WHERE department_id = (
           SELECT TOP 1 department_id
           FROM employees
           GROUP BY department_id
           ORDER BY COUNT(*) DESC
       )
   );
   ```

3. **Trong HAVING**:
   Sử dụng để lọc nhóm dữ liệu sau khi áp dụng hàm tổng hợp.

   **Ví dụ**: Tìm các bộ phận có tổng lương cao hơn mức trung bình của toàn công ty.
   ```sql
   SELECT department_id, SUM(salary) AS total_salary
   FROM employees
   GROUP BY department_id
   HAVING SUM(salary) > (
       SELECT AVG(total_salary)
       FROM (
           SELECT SUM(salary) AS total_salary
           FROM employees
           GROUP BY department_id
       ) AS dept_totals
   );
   ```

---

### 3. Ứng dụng của Nested Subqueries

#### Lọc dữ liệu đa cấp

**Ví dụ**: Tìm các sản phẩm có giá cao hơn giá trung bình của loại sản phẩm có nhiều sản phẩm nhất.

```sql
SELECT product_name, price
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
    WHERE category_id = (
        SELECT TOP 1 category_id
        FROM products
        GROUP BY category_id
        ORDER BY COUNT(*) DESC
    )
);
```

---

#### Tìm kiếm giá trị phức tạp

**Ví dụ**: Tìm nhân viên có lương cao nhất trong phòng ban có tổng lương lớn nhất.

```sql
SELECT name, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE department_id = (
        SELECT TOP 1 department_id
        FROM employees
        GROUP BY department_id
        ORDER BY SUM(salary) DESC
    )
);
```

---

#### Kết hợp với các hàm tổng hợp

**Ví dụ**: Tìm tên nhân viên trong các bộ phận có mức lương trung bình lớn hơn toàn công ty.

```sql
SELECT name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING AVG(salary) > (
        SELECT AVG(salary)
        FROM employees
    )
);
```

---

### 4. Hiệu suất và lưu ý khi sử dụng Nested Subqueries

#### Vấn đề hiệu suất

- **Thực thi nhiều lần**: Mỗi cấp subquery có thể được thực thi riêng biệt, dẫn đến hiệu suất giảm.
- **Khó tối ưu hóa**: Các Nested Subqueries phức tạp có thể làm khó cho trình tối ưu hóa truy vấn của SQL Server.
- **Rủi ro lỗi**: Subqueries lồng nhau dễ gây ra lỗi nếu không đảm bảo trả về giá trị duy nhất ở các cấp quan trọng.

#### Các phương án tối ưu hóa

1. **Sử dụng JOIN**:
   Trong nhiều trường hợp, JOIN có thể thay thế Nested Subqueries và cải thiện hiệu suất.
   ```sql
   SELECT e.name, e.salary
   FROM employees e
   JOIN departments d ON e.department_id = d.department_id
   WHERE e.salary > (
       SELECT AVG(salary)
       FROM employees e2
       WHERE e2.department_id = d.department_id
   );
   ```

2. **Dùng WITH (CTE)**:
   Common Table Expressions giúp đơn giản hóa và tái sử dụng kết quả.
   ```sql
   WITH DeptAvgSalary AS (
       SELECT department_id, AVG(salary) AS avg_salary
       FROM employees
       GROUP BY department_id
   )
   SELECT e.name, e.salary
   FROM employees e
   JOIN DeptAvgSalary d ON e.department_id = d.department_id
   WHERE e.salary > d.avg_salary;
   ```

---

### 5. Tổng kết

**Nested Subqueries** là công cụ mạnh mẽ để xử lý các truy vấn phức tạp,

đặc biệt khi cần lọc dữ liệu đa cấp hoặc kết hợp với các phép tính. Tuy nhiên, Nested Subqueries có thể gây ra vấn đề
hiệu suất và khó khăn trong tối ưu hóa. Hãy cân nhắc sử dụng các phương pháp thay thế như JOIN hoặc CTE khi cần thiết để
đảm bảo hiệu suất và tính dễ bảo trì.
