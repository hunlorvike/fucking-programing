# Scalar Subquery trong SQL Server

## Mục Lục

1. [Tổng quan về Scalar Subquery](#1-tổng-quan-về-scalar-subquery)
    - [Scalar Subquery là gì?](#scalar-subquery-là-gì)
    - [Đặc điểm của Scalar Subquery](#đặc-điểm-của-scalar-subquery)
    - [So sánh Scalar Subquery với Correlated Subquery](#so-sánh-scalar-subquery-với-correlated-subquery)
2. [Cú pháp và cách sử dụng Scalar Subquery](#2-cú-pháp-và-cách-sử-dụng-scalar-subquery)
    - [Ví dụ cơ bản về Scalar Subquery](#ví-dụ-cơ-bản-về-scalar-subquery)
    - [Sử dụng Scalar Subquery trong các mệnh đề khác nhau](#sử-dụng-scalar-subquery-trong-các-mệnh-đề-khác-nhau)
3. [Ứng dụng của Scalar Subquery](#3-ứng-dụng-của-scalar-subquery)
    - [Truy xuất giá trị duy nhất](#truy-xuất-giá-trị-duy-nhất)
    - [Tính toán dựa trên dữ liệu liên quan](#tính-toán-dựa-trên-dữ-liệu-liên-quan)
    - [Kết hợp Scalar Subquery với hàm tổng hợp](#kết-hợp-scalar-subquery-với-hàm-tổng-hợp)
4. [Hiệu suất và lưu ý khi sử dụng](#4-hiệu-suất-và-lưu-ý-khi-sử-dụng)
    - [Vấn đề hiệu suất](#vấn-đề-hiệu-suất)
    - [Các phương án thay thế](#các-phương-án-thay-thế)
5. [Tổng kết](#5-tổng-kết)

---

### 1. Tổng quan về Scalar Subquery

#### Scalar Subquery là gì?

**Scalar Subquery** là một loại subquery (truy vấn con) trả về **một giá trị duy nhất** (một hàng và một cột). Giá trị
này có thể được sử dụng như một biểu thức trong các câu lệnh SQL, tương tự như một giá trị hoặc hàm.

**Ví dụ chung**:

```sql
SELECT employee_id, salary,
       (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;
```

- Subquery `(SELECT AVG(salary) FROM employees)` trả về một giá trị duy nhất, đại diện cho mức lương trung bình của tất
  cả nhân viên.

---

#### Đặc điểm của Scalar Subquery

- **Trả về giá trị duy nhất**: Scalar Subquery chỉ trả về một giá trị (một hàng, một cột). Nếu subquery trả về nhiều hơn
  một giá trị, SQL Server sẽ báo lỗi.
- **Sử dụng như một biểu thức**: Scalar Subquery có thể được dùng trong:
    - Mệnh đề `SELECT` để thêm cột tính toán.
    - Mệnh đề `WHERE` hoặc `HAVING` để so sánh giá trị.
    - Mệnh đề `SET` để gán giá trị cho biến.
- **Độc lập hoặc liên kết**: Scalar Subquery có thể độc lập hoặc phụ thuộc vào truy vấn chính (correlated scalar
  subquery).

---

#### So sánh Scalar Subquery với Correlated Subquery

| **Tiêu chí**       | **Scalar Subquery**                          | **Correlated Subquery**                            |
|--------------------|----------------------------------------------|----------------------------------------------------|
| **Kết quả trả về** | Một giá trị duy nhất (một hàng, một cột).    | Có thể trả về nhiều giá trị nếu không kết hợp hàm. |
| **Sự phụ thuộc**   | Không bắt buộc phụ thuộc vào truy vấn chính. | Phụ thuộc vào dữ liệu từ truy vấn chính.           |
| **Cách sử dụng**   | Được dùng như một biểu thức.                 | Thường dùng để lọc hoặc so sánh dữ liệu liên quan. |

---

### 2. Cú pháp và cách sử dụng Scalar Subquery

#### Ví dụ cơ bản về Scalar Subquery

**Ví dụ**: Tìm thông tin nhân viên cùng với mức lương trung bình của tất cả nhân viên.

**Bảng employees**:
| employee_id | name | salary |
| ----------- | ----- | ------ |
| 1 | Alice | 5000 |
| 2 | Bob | 6000 |
| 3 | Carol | 7000 |

**Câu lệnh SQL**:

```sql
SELECT employee_id, name, salary,
       (SELECT AVG(salary) FROM employees) AS avg_salary
FROM employees;
```

**Kết quả giả định**:
| employee_id | name | salary | avg_salary |
| ----------- | ----- | ------ | ---------- |
| 1 | Alice | 5000 | 6000 |
| 2 | Bob | 6000 | 6000 |
| 3 | Carol | 7000 | 6000 |

---

#### Sử dụng Scalar Subquery trong các mệnh đề khác nhau

1. **Trong SELECT**:
    - Scalar Subquery được dùng để thêm cột tính toán dựa trên kết quả của một truy vấn con.

   **Ví dụ**: Hiển thị tên nhân viên và số lượng nhân viên trong công ty.
   ```sql
   SELECT name,
          (SELECT COUNT(*) FROM employees) AS total_employees
   FROM employees;
   ```

2. **Trong WHERE**:
    - Scalar Subquery có thể được sử dụng để lọc dữ liệu.

   **Ví dụ**: Tìm nhân viên có mức lương lớn hơn mức lương trung bình.
   ```sql
   SELECT name, salary
   FROM employees
   WHERE salary > (SELECT AVG(salary) FROM employees);
   ```

3. **Trong HAVING**:
    - Scalar Subquery có thể được dùng trong mệnh đề `HAVING` để lọc nhóm dữ liệu.

   **Ví dụ**: Tìm các bộ phận có tổng lương lớn hơn mức lương trung bình của toàn công ty.
   ```sql
   SELECT department_id, SUM(salary) AS total_salary
   FROM employees
   GROUP BY department_id
   HAVING SUM(salary) > (SELECT AVG(salary) FROM employees);
   ```

4. **Trong SET**:
    - Scalar Subquery có thể gán giá trị cho một biến.

   **Ví dụ**: Gán mức lương trung bình vào một biến trong SQL Server.
   ```sql
   DECLARE @avg_salary DECIMAL(10, 2);
   SET @avg_salary = (SELECT AVG(salary) FROM employees);
   ```

---

### 3. Ứng dụng của Scalar Subquery

#### Truy xuất giá trị duy nhất

Scalar Subquery có thể được dùng để truy vấn thông tin cụ thể.

**Ví dụ**: Tìm tên nhân viên có mức lương cao nhất.

```sql
SELECT name
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```

---

#### Tính toán dựa trên dữ liệu liên quan

Scalar Subquery thường được dùng để tính toán dựa trên dữ liệu phụ thuộc vào ngữ cảnh.

**Ví dụ**: Tìm thông tin nhân viên và số lượng nhân viên trong cùng bộ phận.

```sql
SELECT employee_id, name, department_id,
       (SELECT COUNT(*)
        FROM employees e2
        WHERE e2.department_id = e1.department_id) AS department_count
FROM employees e1;
```

---

#### Kết hợp Scalar Subquery với hàm tổng hợp

Scalar Subquery thường được kết hợp với các hàm tổng hợp như `AVG`, `MAX`, `MIN` để lấy giá trị liên quan.

**Ví dụ**: Tìm sản phẩm có giá cao hơn giá trung bình của tất cả sản phẩm.

```sql
SELECT product_id, product_name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

---

### 4. Hiệu suất và lưu ý khi sử dụng

#### Vấn đề hiệu suất

- **Tốc độ xử lý**: Vì Scalar Subquery thường được thực thi lặp lại (nhất là khi liên quan đến truy vấn chính), nó có
  thể làm giảm hiệu suất với dữ liệu lớn.
- **Rủi ro trả về nhiều giá trị**: Nếu subquery không được viết cẩn thận (quên sử dụng `TOP 1` hoặc `LIMIT`), có thể xảy
  ra lỗi trả về nhiều giá trị.

#### Các phương án thay thế

- **Dùng JOIN hoặc CTE**:
  Trong nhiều trường hợp, sử dụng `JOIN` hoặc `WITH` (Common Table Expressions) có thể tối ưu hơn Scalar Subquery.

  **Ví dụ**:
  ```sql
  WITH AvgSalary AS (
      SELECT AVG(salary) AS avg_salary
      FROM employees
  )
  SELECT employee_id, name, salary, avg_salary
  FROM employees, AvgSalary;
  ```

- **Tối ưu hóa Scalar Subquery**:
  Thêm chỉ số (index) trên các cột liên quan để cải thiện hiệu suất.

---

### 5. Tổng kết

**Scalar Subquery** là một công cụ mạnh mẽ để tính toán và lấy dữ liệu động trong SQL Server. Với khả năng trả về giá
trị duy nhất, nó rất hữu ích trong nhiều

trường hợp như thêm cột tính toán, lọc dữ liệu và sử dụng trong các mệnh đề khác nhau. Tuy nhiên, để đạt hiệu suất tốt
nhất, bạn cần cân nhắc sử dụng các phương án thay thế như `JOIN` hoặc `WITH` khi làm việc với dữ liệu lớn.
