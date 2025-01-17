# **Hàm Tổng Hợp (Aggregate Functions) trong SQL Server**

## Mục Lục

1. [Tổng quan về Hàm Tổng Hợp](#1-tổng-quan-về-hàm-tổng-hợp)
2. [Các Hàm Tổng Hợp trong SQL Server](#2-các-hàm-tổng-hợp-trong-sql-server)
    - [COUNT](#count)
    - [SUM](#sum)
    - [AVG](#avg)
    - [MIN](#min)
    - [MAX](#max)
    - [GROUP_CONCAT](#group_concat)
3. [Sử dụng Hàm Tổng Hợp với GROUP BY](#3-sử-dụng-hàm-tổng-hợp-với-group-by)
4. [Sử dụng Hàm Tổng Hợp với HAVING](#4-sử-dụng-hàm-tổng-hợp-với-having)
5. [Ví dụ về Hàm Tổng Hợp](#5-ví-dụ-về-hàm-tổng-hợp)
6. [Lưu ý khi sử dụng Hàm Tổng Hợp](#6-lưu-ý-khi-sử-dụng-hàm-tổng-hợp)
7. [Kết luận](#7-kết-luận)

---

### 1. Tổng quan về Hàm Tổng Hợp

Hàm tổng hợp (aggregate functions) trong SQL Server là các hàm đặc biệt được sử dụng để tính toán hoặc tóm tắt dữ liệu
trong bảng. Những hàm này giúp bạn thực hiện các phép toán trên một nhóm các bản ghi và trả về một giá trị duy nhất. Các
hàm tổng hợp phổ biến trong SQL Server bao gồm `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, và một số hàm khác.

Các hàm này thường được sử dụng kết hợp với câu lệnh `GROUP BY` để nhóm dữ liệu và tính toán giá trị cho từng nhóm.

---

### 2. Các Hàm Tổng Hợp trong SQL Server

#### COUNT

Hàm `COUNT` trả về số lượng các bản ghi trong một nhóm, hoặc số lượng giá trị không NULL trong một cột.

**Cú pháp**:

```sql
COUNT(column_name)
```

**Ví dụ**:

Để đếm số lượng nhân viên trong bảng `employees`:

```sql
SELECT COUNT(*) AS TotalEmployees
FROM employees;
```

Câu truy vấn trên sẽ trả về tổng số lượng bản ghi trong bảng `employees`.

---

#### SUM

Hàm `SUM` tính tổng của các giá trị trong một cột số.

**Cú pháp**:

```sql
SUM(column_name)
```

**Ví dụ**:

Để tính tổng lương của tất cả nhân viên trong bảng `employees`:

```sql
SELECT SUM(salary) AS TotalSalary
FROM employees;
```

Câu truy vấn trên sẽ trả về tổng giá trị của cột `salary` trong bảng `employees`.

---

#### AVG

Hàm `AVG` tính giá trị trung bình của một cột số.

**Cú pháp**:

```sql
AVG(column_name)
```

**Ví dụ**:

Để tính lương trung bình của tất cả nhân viên trong bảng `employees`:

```sql
SELECT AVG(salary) AS AverageSalary
FROM employees;
```

Câu truy vấn trên sẽ trả về giá trị trung bình của cột `salary`.

---

#### MIN

Hàm `MIN` trả về giá trị nhỏ nhất trong một cột.

**Cú pháp**:

```sql
MIN(column_name)
```

**Ví dụ**:

Để tìm lương thấp nhất trong bảng `employees`:

```sql
SELECT MIN(salary) AS MinSalary
FROM employees;
```

Câu truy vấn trên sẽ trả về giá trị nhỏ nhất trong cột `salary`.

---

#### MAX

Hàm `MAX` trả về giá trị lớn nhất trong một cột.

**Cú pháp**:

```sql
MAX(column_name)
```

**Ví dụ**:

Để tìm lương cao nhất trong bảng `employees`:

```sql
SELECT MAX(salary) AS MaxSalary
FROM employees;
```

Câu truy vấn trên sẽ trả về giá trị lớn nhất trong cột `salary`.

---

#### GROUP_CONCAT (chỉ có trong một số phiên bản SQL Server)

Hàm `GROUP_CONCAT` được sử dụng để nối các giá trị trong một cột thành một chuỗi duy nhất, phân cách bởi một ký tự nhất
định.

**Cú pháp**:

```sql
GROUP_CONCAT(column_name)
```

**Ví dụ**:

Để nối tên tất cả nhân viên trong một chuỗi, phân cách bằng dấu phẩy:

```sql
SELECT GROUP_CONCAT(name) AS EmployeeNames
FROM employees;
```

Lưu ý: Trong SQL Server, bạn cần sử dụng `STRING_AGG` thay vì `GROUP_CONCAT`.

---

### 3. Sử dụng Hàm Tổng Hợp với GROUP BY

Hàm tổng hợp thường được sử dụng cùng với câu lệnh `GROUP BY` để nhóm các bản ghi theo một hoặc nhiều cột và tính toán
giá trị cho từng nhóm.

**Cú pháp**:

```sql
SELECT column_name, AGGREGATE_FUNCTION(column_name)
FROM table_name
GROUP BY column_name;
```

**Ví dụ**:

Để tính tổng lương theo từng phòng ban trong bảng `employees`, bạn có thể sử dụng câu lệnh sau:

```sql
SELECT department, SUM(salary) AS TotalSalary
FROM employees
GROUP BY department;
```

Câu truy vấn trên sẽ trả về tổng lương cho mỗi phòng ban.

---

### 4. Sử dụng Hàm Tổng Hợp với HAVING

Khi bạn sử dụng `GROUP BY` với các hàm tổng hợp, bạn có thể sử dụng `HAVING` để lọc các nhóm dữ liệu sau khi đã áp dụng
hàm tổng hợp. `HAVING` khác với `WHERE` vì `WHERE` áp dụng trước khi nhóm dữ liệu, còn `HAVING` áp dụng sau khi dữ liệu
đã được nhóm.

**Cú pháp**:

```sql
SELECT column_name, AGGREGATE_FUNCTION(column_name)
FROM table_name
GROUP BY column_name
HAVING AGGREGATE_FUNCTION(column_name) condition;
```

**Ví dụ**:

Để lấy những phòng ban có tổng lương lớn hơn 50000:

```sql
SELECT department, SUM(salary) AS TotalSalary
FROM employees
GROUP BY department
HAVING SUM(salary) > 50000;
```

Câu truy vấn trên sẽ chỉ trả về các phòng ban có tổng lương lớn hơn 50000.

---

### 5. Ví dụ về Hàm Tổng Hợp

#### Ví dụ 1: COUNT

Để đếm số lượng đơn hàng trong bảng `orders`:

```sql
SELECT COUNT(*) AS TotalOrders
FROM orders;
```

#### Ví dụ 2: SUM

Để tính tổng số tiền của các đơn hàng trong bảng `orders`:

```sql
SELECT SUM(order_amount) AS TotalAmount
FROM orders;
```

#### Ví dụ 3: AVG

Để tính giá trị trung bình của các đơn hàng trong bảng `orders`:

```sql
SELECT AVG(order_amount) AS AverageAmount
FROM orders;
```

#### Ví dụ 4: GROUP BY và HAVING

Để tính tổng lương theo phòng ban và chỉ lấy những phòng ban có tổng lương lớn hơn 100,000:

```sql
SELECT department, SUM(salary) AS TotalSalary
FROM employees
GROUP BY department
HAVING SUM(salary) > 100000;
```

---

### 6. Lưu ý khi sử dụng Hàm Tổng Hợp

- **NULL và Hàm Tổng Hợp**: Các giá trị NULL thường không được tính trong các hàm `SUM`, `AVG`, `MIN`, `MAX`. Tuy nhiên,
  `COUNT` chỉ đếm các giá trị không NULL trong một cột.
- **Nhóm dữ liệu đúng cách**: Khi sử dụng `GROUP BY`, hãy đảm bảo rằng bạn chỉ nhóm các cột mà bạn thực sự muốn tính
  toán hoặc hiển thị.
- **Sử dụng `HAVING` để lọc nhóm**: Khi bạn cần lọc dữ liệu sau khi đã nhóm và tính toán, hãy sử dụng `HAVING` thay vì
  `WHERE`.

---

### 7. Kết luận

Hàm tổng hợp trong SQL Server là công cụ mạnh mẽ để xử lý và phân tích dữ liệu. Chúng cho phép bạn tính toán tổng số,
giá trị trung bình, giá trị nhỏ nhất, giá trị lớn nhất và nhiều phép toán khác trên dữ liệu nhóm. Kết hợp với `GROUP BY`
và `HAVING`, bạn có thể phân tích dữ liệu một cách linh hoạt và hiệu quả.
