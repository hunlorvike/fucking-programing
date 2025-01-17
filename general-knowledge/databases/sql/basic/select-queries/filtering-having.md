# Filtering với HAVING trong SQL Server

## Mục Lục

1. [Tổng quan về Filtering với HAVING](#1-tổng-quan-về-filtering-với-having)
    - [HAVING là gì?](#having-là-gì)
    - [Lợi ích của HAVING](#lợi-ích-của-having)
    - [HAVING hoạt động như thế nào?](#having-hoạt-động-như-thế-nào)
2. [Cú pháp của HAVING](#2-cú-pháp-của-having)
    - [Kết hợp với GROUP BY](#kết-hợp-với-group-by)
    - [Kết hợp với SELECT](#kết-hợp-với-select)
3. [Sử dụng HAVING với các hàm tổng hợp](#3-sử-dụng-having-với-các-hàm-tổng-hợp)
    - [HAVING và COUNT](#having-và-count)
    - [HAVING và SUM](#having-và-sum)
    - [HAVING và AVG](#having-và-avg)
4. [Ví dụ thực tế với HAVING](#4-ví-dụ-thực-tế-với-having)
5. [Lưu ý và thực hành tốt](#5-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Filtering với HAVING

#### HAVING là gì?

Mệnh đề `HAVING` trong SQL Server được sử dụng để lọc các nhóm kết quả sau khi nhóm dữ liệu bằng mệnh đề `GROUP BY`. Mặc
dù `WHERE` lọc dữ liệu trước khi nhóm, `HAVING` lọc các nhóm sau khi dữ liệu đã được nhóm lại. Điều này có nghĩa là bạn
có thể áp dụng điều kiện vào kết quả của các hàm tổng hợp như `COUNT()`, `SUM()`, `AVG()`, v.v.

#### Lợi ích của HAVING

- **Lọc nhóm dữ liệu**: Mệnh đề `HAVING` cho phép bạn lọc dữ liệu sau khi nhóm các bản ghi, điều này rất hữu ích khi bạn
  muốn làm việc với các kết quả tổng hợp.
- **Sử dụng với hàm tổng hợp**: `HAVING` thường được sử dụng để lọc kết quả của các hàm tổng hợp (ví dụ: `COUNT()`,
  `SUM()`, `AVG()`), điều mà `WHERE` không thể thực hiện.
- **Tăng khả năng phân tích dữ liệu**: Mệnh đề `HAVING` giúp bạn phân tích các nhóm dữ liệu theo các tiêu chí phức tạp.

#### HAVING hoạt động như thế nào?

1. **Nhóm dữ liệu**: Trước tiên, SQL Server sẽ nhóm các bản ghi theo các cột mà bạn chỉ định trong mệnh đề `GROUP BY`.
2. **Áp dụng hàm tổng hợp**: Sau khi nhóm dữ liệu, SQL Server sẽ tính toán các hàm tổng hợp cho mỗi nhóm.
3. **Lọc nhóm dữ liệu**: Sau đó, mệnh đề `HAVING` được áp dụng để lọc các nhóm dữ liệu dựa trên điều kiện mà bạn chỉ
   định.
4. **Trả về kết quả**: SQL Server sẽ trả về các nhóm dữ liệu thỏa mãn điều kiện trong `HAVING`.

---

### 2. Cú pháp của HAVING

#### Kết hợp với GROUP BY

Mệnh đề `HAVING` phải được sử dụng với mệnh đề `GROUP BY`. Cú pháp chung khi kết hợp `HAVING` với `GROUP BY` như sau:

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

**Ví dụ**:

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

Trong ví dụ này, câu lệnh sẽ trả về các phòng ban có số lượng nhân viên lớn hơn 10.

#### Kết hợp với SELECT

Mệnh đề `HAVING` có thể được kết hợp với mệnh đề `SELECT` khi bạn muốn lọc kết quả nhóm theo các hàm tổng hợp.

**Ví dụ**:

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 5000;
```

Câu lệnh này sẽ trả về các phòng ban có mức lương trung bình lớn hơn 5000.

---

### 3. Sử dụng HAVING với các hàm tổng hợp

Mệnh đề `HAVING` đặc biệt hữu ích khi bạn muốn lọc các nhóm dựa trên các kết quả tổng hợp như `COUNT()`, `SUM()`,
`AVG()`, v.v.

#### HAVING và COUNT

`COUNT()` là hàm tổng hợp được sử dụng để đếm số lượng bản ghi trong mỗi nhóm.

**Ví dụ**:

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
```

Câu lệnh này sẽ trả về các phòng ban có hơn 10 nhân viên.

#### HAVING và SUM

`SUM()` là hàm tổng hợp được sử dụng để tính tổng giá trị trong một nhóm.

**Ví dụ**:

```sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department
HAVING SUM(salary) > 50000;
```

Câu lệnh trên sẽ trả về các phòng ban có tổng lương vượt quá 50000.

#### HAVING và AVG

`AVG()` là hàm tổng hợp được sử dụng để tính giá trị trung bình của một cột trong một nhóm.

**Ví dụ**:

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 5000;
```

Câu lệnh này sẽ trả về các phòng ban có mức lương trung bình lớn hơn 5000.

---

Dưới đây là phần bổ sung ví dụ kèm kết quả cho tài liệu về **Filtering với HAVING** trong SQL Server, giúp người đọc dễ
dàng hình dung hơn.

---

### 4. Ví dụ thực tế với HAVING

#### Lọc phòng ban có số nhân viên lớn hơn 5

**Câu lệnh SQL**:

```sql
SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

**Giải thích**:

- Truy vấn này sẽ nhóm các nhân viên theo phòng ban và trả về các phòng ban có số nhân viên lớn hơn 5.

**Kết quả có thể xảy ra**:

| department | num_employees |
|------------|---------------|
| HR         | 8             |
| IT         | 12            |
| Sales      | 6             |

---

#### Lọc phòng ban có tổng lương vượt quá 100000

**Câu lệnh SQL**:

```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department
HAVING SUM(salary) > 100000;
```

**Giải thích**:

- Truy vấn này sẽ tính tổng lương của nhân viên trong từng phòng ban và trả về các phòng ban có tổng lương vượt quá
    100000.

**Kết quả có thể xảy ra**:

| department | total_salary |
|------------|--------------|
| IT         | 150000       |
| Sales      | 120000       |

---

#### Lọc các phòng ban có mức lương trung bình lớn hơn 4000

**Câu lệnh SQL**:

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 4000;
```

**Giải thích**:

- Truy vấn này sẽ tính mức lương trung bình trong từng phòng ban và chỉ trả về các phòng ban có mức lương trung bình lớn
  hơn 4000.

**Kết quả có thể xảy ra**:

| department | avg_salary |
|------------|------------|
| IT         | 5500       |
| Sales      | 4600       |

---

#### Lọc các phòng ban có số nhân viên hơn 10 và mức lương trung bình trên 5000

**Câu lệnh SQL**:

```sql
SELECT department, COUNT(*) AS num_employees, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 10 AND AVG(salary) > 5000;
```

**Giải thích**:

- Truy vấn này sẽ lọc các phòng ban có số nhân viên lớn hơn 10 và mức lương trung bình lớn hơn 5000.

**Kết quả có thể xảy ra**:

| department | num_employees | avg_salary |
|------------|---------------|------------|
| IT         | 12            | 6000       |

---

#### Lọc phòng ban có mức lương trung bình thấp hơn 4000 và có số nhân viên lớn hơn 5

**Câu lệnh SQL**:

```sql
SELECT department, COUNT(*) AS num_employees, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) < 4000 AND COUNT(*) > 5;
```

**Giải thích**:

- Truy vấn này sẽ lọc các phòng ban có mức lương trung bình thấp hơn 4000 và có số nhân viên lớn hơn 5.

**Kết quả có thể xảy ra**:

| department | num_employees | avg_salary |
|------------|---------------|------------|
| HR         | 8             | 3500       |

---

#### Lọc phòng ban có tổng lương lớn hơn 50000 và số nhân viên ít nhất là 3

**Câu lệnh SQL**:

```sql
SELECT department, SUM(salary) AS total_salary, COUNT(*) AS num_employees
FROM employees
GROUP BY department
HAVING SUM(salary) > 50000 AND COUNT(*) >= 3;
```

**Giải thích**:

- Truy vấn này sẽ trả về các phòng ban có tổng lương lớn hơn 50000 và số nhân viên ít nhất là 3.

**Kết quả có thể xảy ra**:

| department | total_salary | num_employees |
|------------|--------------|---------------|
| IT         | 75000        | 10            |
| Sales      | 55000        | 6             |

---

### 5. Lưu ý và thực hành tốt

- **Sử dụng HAVING sau GROUP BY**: `HAVING` luôn được sử dụng sau khi nhóm dữ liệu với `GROUP BY`. Điều này có nghĩa là
  bạn không thể sử dụng `HAVING` mà không có `GROUP BY`.
- **Lọc sau khi nhóm**: `HAVING` là để lọc các nhóm, trong khi `WHERE` được sử dụng để lọc dữ liệu trước khi nhóm. Nếu
  bạn muốn lọc các bản ghi trước khi nhóm, hãy sử dụng `WHERE`.
- **Tối ưu hóa truy vấn**: Cần lưu ý rằng mệnh đề `HAVING` có thể làm chậm truy vấn nếu nhóm dữ liệu quá lớn hoặc nếu
  bạn sử dụng các hàm tổng hợp phức tạp. Hãy tối ưu hóa truy vấn của bạn bằng cách sử dụng điều kiện lọc hợp lý.
- **Kết hợp WHERE và HAVING**: Trong một số trường hợp, bạn có thể cần kết hợp `WHERE` và `HAVING` để lọc dữ liệu trước
  khi nhóm và sau khi nhóm. Hãy chắc chắn sử dụng `WHERE` cho các điều kiện không liên quan đến hàm tổng hợp.
