# Correlated Subquery trong SQL Server

## Mục Lục

1. [Tổng quan về Correlated Subquery](#1-tổng-quan-về-correlated-subquery)
   - [Correlated Subquery là gì?](#correlated-subquery-là-gì)
   - [So sánh Subquery thông thường và Correlated Subquery](#so-sánh-subquery-thông-thường-và-correlated-subquery)
2. [Cú pháp và cách sử dụng Correlated Subquery](#2-cú-pháp-và-cách-sử-dụng-correlated-subquery)
   - [Ví dụ cơ bản về Correlated Subquery](#ví-dụ-cơ-bản-về-correlated-subquery)
   - [Sử dụng với các mệnh đề khác](#sử-dụng-với-các-mệnh-đề-khác)
3. [Ứng dụng của Correlated Subquery](#3-ứng-dụng-của-correlated-subquery)
   - [Lọc dữ liệu theo điều kiện](#lọc-dữ-liệu-theo-điều-kiện)
   - [So sánh từng hàng](#so-sánh-từng-hàng)
   - [Tìm giá trị lớn nhất hoặc nhỏ nhất](#tìm-giá-trị-lớn-nhất-hoặc-nhỏ-nhất)
4. [Hiệu suất và lưu ý khi sử dụng](#4-hiệu-suất-và-lưu-ý-khi-sử-dụng)
   - [Vấn đề hiệu suất](#vấn-đề-hiệu-suất)
   - [Các phương án thay thế](#các-phương-án-thay-thế)
5. [Tổng kết](#5-tổng-kết)

---

### 1. Tổng quan về Correlated Subquery

#### Correlated Subquery là gì?

**Correlated Subquery** (truy vấn con có liên kết) là một loại subquery mà mỗi lần thực thi sẽ phụ thuộc vào dữ liệu từ truy vấn chính. Điều này có nghĩa là subquery không thể thực hiện một cách độc lập vì nó tham chiếu đến cột trong truy vấn chính. 

Trong Correlated Subquery:
- Mỗi hàng trong truy vấn chính sẽ kích hoạt việc thực thi subquery.
- Kết quả của subquery thay đổi dựa trên hàng hiện tại của truy vấn chính.

**Ví dụ chung**:
```sql
SELECT e1.employee_id, e1.salary
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```
Trong ví dụ này, subquery phụ thuộc vào `e1.department_id` từ truy vấn chính.

---

#### So sánh Subquery thông thường và Correlated Subquery

| **Tiêu chí**         | **Subquery thông thường**                             | **Correlated Subquery**                                 |
|-----------------------|------------------------------------------------------|--------------------------------------------------------|
| **Cách hoạt động**    | Thực thi một lần và kết quả được sử dụng nhiều lần.   | Thực thi nhiều lần, mỗi lần cho một hàng từ truy vấn chính. |
| **Sự phụ thuộc**      | Không phụ thuộc vào truy vấn chính.                   | Phụ thuộc vào dữ liệu từ truy vấn chính.               |
| **Hiệu suất**         | Hiệu suất cao hơn vì không phải thực thi nhiều lần.   | Hiệu suất thấp hơn do subquery được thực thi lặp lại.  |

---

### 2. Cú pháp và cách sử dụng Correlated Subquery

#### Ví dụ cơ bản về Correlated Subquery

**Ví dụ 1**: Tìm những nhân viên có mức lương cao hơn mức lương trung bình của bộ phận mà họ làm việc.

**Bảng employees**:

| employee_id | name  | department_id | salary |
| ----------- | ----- | ------------- | ------ |
| 1           | Alice | 1             | 5000   |
| 2           | Bob   | 1             | 6000   |
| 3           | Carol | 2             | 7000   |
| 4           | David | 2             | 6500   |

**Câu lệnh SQL**:
```sql
SELECT e1.name, e1.salary
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```

**Kết quả giả định**:
| name  | salary |
| ----- | ------ |
| Bob   | 6000   |
| Carol | 7000   |

Trong ví dụ này:
- Truy vấn chính duyệt qua từng hàng trong bảng `employees`.
- Subquery tính mức lương trung bình (`AVG`) cho từng bộ phận dựa trên `e1.department_id`.

---

#### Sử dụng với các mệnh đề khác

1. **Correlated Subquery trong SELECT**:
   Subquery trả về dữ liệu tính toán cho từng hàng trong kết quả của truy vấn chính.

   **Ví dụ**: Tìm mức lương và số lượng nhân viên trong cùng bộ phận.
   ```sql
   SELECT e1.name, e1.salary, 
       (SELECT COUNT(*) 
        FROM employees e2 
        WHERE e2.department_id = e1.department_id) AS num_employees
   FROM employees e1;
   ```

2. **Correlated Subquery trong WHERE**:
   Lọc các hàng dựa trên điều kiện phụ thuộc vào dữ liệu của truy vấn chính.

   **Ví dụ**: Tìm các sản phẩm có giá cao hơn giá trung bình trong cùng loại.
   ```sql
   SELECT p1.product_name, p1.price
   FROM products p1
   WHERE p1.price > (
       SELECT AVG(p2.price)
       FROM products p2
       WHERE p2.category_id = p1.category_id
   );
   ```

---

### 3. Ứng dụng của Correlated Subquery

#### Lọc dữ liệu theo điều kiện

Correlated Subquery thường được sử dụng để lọc dữ liệu mà điều kiện phụ thuộc vào giá trị cụ thể từ truy vấn chính.

**Ví dụ**: Tìm nhân viên trẻ tuổi nhất trong mỗi bộ phận.
```sql
SELECT e1.name, e1.age
FROM employees e1
WHERE e1.age = (
    SELECT MIN(e2.age)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```

---

#### So sánh từng hàng

Correlated Subquery có thể so sánh từng hàng với một tập hợp dữ liệu liên quan.

**Ví dụ**: Tìm những đơn hàng có tổng giá trị cao hơn giá trị trung bình của tất cả các đơn hàng.
```sql
SELECT o1.order_id, o1.total_amount
FROM orders o1
WHERE o1.total_amount > (
    SELECT AVG(o2.total_amount)
    FROM orders o2
    WHERE o2.customer_id = o1.customer_id
);
```

---

#### Tìm giá trị lớn nhất hoặc nhỏ nhất

Sử dụng Correlated Subquery để tìm các hàng có giá trị cực trị trong tập hợp.

**Ví dụ**: Tìm nhân viên có mức lương cao nhất trong mỗi bộ phận.
```sql
SELECT e1.name, e1.salary
FROM employees e1
WHERE e1.salary = (
    SELECT MAX(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```

---

### 4. Hiệu suất và lưu ý khi sử dụng

#### Vấn đề hiệu suất

- **Thực thi nhiều lần**: Subquery được thực thi lặp lại cho mỗi hàng trong truy vấn chính, dẫn đến thời gian xử lý tăng lên đáng kể với các bảng lớn.
- **Tối ưu hóa kém**: Các Correlated Subquery phức tạp có thể khó tối ưu hóa, gây ảnh hưởng đến hiệu suất tổng thể của hệ thống.

#### Các phương án thay thế

- **Sử dụng JOIN**:
  Thay thế Correlated Subquery bằng `JOIN` trong nhiều trường hợp có thể cải thiện hiệu suất đáng kể.

  **Ví dụ**:
  ```sql
  SELECT e1.name, e1.salary
  FROM employees e1
  JOIN (
      SELECT department_id, AVG(salary) AS avg_salary
      FROM employees
      GROUP BY department_id
  ) AS subquery
  ON e1.department_id = subquery.department_id
  WHERE e1.salary > subquery.avg_salary;
  ```

- **Sử dụng WITH (Common Table Expressions - CTE)**:
  Dùng CTE để tính trước kết quả và cải thiện hiệu suất.

  **Ví dụ**:
  ```sql
  WITH AvgSalaryPerDept AS (
      SELECT department_id, AVG(salary) AS avg_salary
      FROM employees
      GROUP BY department_id
  )
  SELECT e1.name, e1.salary
  FROM employees e1
  JOIN AvgSalaryPerDept d
  ON e1.department_id = d.department_id
  WHERE e1.salary > d.avg_salary;
  ```

---

### 5. Tổng kết

**Correlated Subquery** là một công cụ mạnh mẽ giúp thực hiện các truy vấn phức tạp bằng cách liên kết dữ liệu từ truy vấn chính với subquery. Tuy nhiên, nó cũng có nhược điểm về hiệu suất, đặc biệt khi làm việc với dữ liệu lớn. Khi sử dụng, bạn nên cân nhắc các phương án thay thế như `JOIN`