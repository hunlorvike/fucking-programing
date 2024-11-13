# Sorting với ORDER BY trong SQL Server

## Mục Lục

1. [Tổng quan về Sorting với ORDER BY](#1-tổng-quan-về-sorting-với-order-by)
   - [ORDER BY là gì?](#order-by-là-gì)
   - [Lợi ích của ORDER BY](#lợi-ích-của-order-by)
   - [ORDER BY hoạt động như thế nào?](#order-by-hoạt-động-như-thế-nào)
2. [Cú pháp của ORDER BY](#2-cú-pháp-của-order-by)
   - [Sắp xếp theo một cột](#sắp-xếp-theo-một-cột)
   - [Sắp xếp theo nhiều cột](#sắp-xếp-theo-nhiều-cột)
   - [Sắp xếp theo thứ tự tăng dần và giảm dần](#sắp-xếp-theo-thứ-tự-tăng-dần-và-giảm-dần)
3. [Sử dụng ORDER BY với các kiểu dữ liệu](#3-sử-dụng-order-by-với-các-kiểu-dữ-liệu)
   - [Sắp xếp với kiểu số](#sắp-xếp-với-kiểu-số)
   - [Sắp xếp với kiểu chuỗi](#sắp-xếp-với-kiểu-chuỗi)
   - [Sắp xếp với kiểu ngày giờ](#sắp-xếp-với-kiểu-ngày-giờ)
4. [Ví dụ thực tế với ORDER BY](#4-ví-dụ-thực-tế-với-order-by)
5. [Lưu ý và thực hành tốt](#5-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Sorting với ORDER BY

#### ORDER BY là gì?

Mệnh đề `ORDER BY` trong SQL Server được sử dụng để sắp xếp các bản ghi trong kết quả truy vấn theo một hoặc nhiều cột. Mệnh đề này có thể được sử dụng để sắp xếp dữ liệu theo thứ tự tăng dần (ASC) hoặc giảm dần (DESC). Đây là công cụ quan trọng để tổ chức và trình bày dữ liệu dễ dàng hơn trong kết quả truy vấn.

#### Lợi ích của ORDER BY

- **Sắp xếp kết quả**: `ORDER BY` giúp sắp xếp dữ liệu theo một hoặc nhiều cột, giúp bạn có cái nhìn rõ ràng hơn về dữ liệu.
- **Dễ dàng phân tích**: Sắp xếp dữ liệu giúp việc phân tích và ra quyết định trở nên dễ dàng hơn, ví dụ như tìm ra giá trị lớn nhất, nhỏ nhất, hoặc các nhóm dữ liệu theo thứ tự.
- **Hiển thị báo cáo**: Khi tạo báo cáo hoặc xuất dữ liệu, việc sắp xếp là rất quan trọng để kết quả có thể đọc và hiểu được một cách hợp lý.

#### ORDER BY hoạt động như thế nào?

1. **Xác định cột sắp xếp**: Trước tiên, bạn phải chỉ định một hoặc nhiều cột mà bạn muốn sắp xếp.
2. **Chọn thứ tự sắp xếp**: Sau khi xác định các cột sắp xếp, bạn có thể chọn thứ tự sắp xếp (tăng dần hoặc giảm dần).
3. **Trả về kết quả**: SQL Server sẽ trả về kết quả của truy vấn theo thứ tự mà bạn đã chỉ định trong mệnh đề `ORDER BY`.

---

### 2. Cú pháp của ORDER BY

#### Sắp xếp theo một cột

Cú pháp đơn giản để sắp xếp theo một cột trong SQL Server là:

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC];
```

**Ví dụ**:

```sql
SELECT employee_id, first_name, salary
FROM employees
ORDER BY salary ASC;
```

Câu lệnh trên sẽ trả về danh sách nhân viên được sắp xếp theo lương từ thấp đến cao (tăng dần).

#### Sắp xếp theo nhiều cột

Bạn cũng có thể sắp xếp dữ liệu theo nhiều cột bằng cách chỉ định nhiều cột trong mệnh đề `ORDER BY`. Kết quả sẽ được sắp xếp theo thứ tự ưu tiên từ trái qua phải.

Cú pháp:

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

**Ví dụ**:

```sql
SELECT employee_id, first_name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;
```

Câu lệnh trên sẽ trả về danh sách nhân viên, trước tiên sắp xếp theo phòng ban (tăng dần), sau đó sắp xếp theo lương (giảm dần) trong mỗi phòng ban.

#### Sắp xếp theo thứ tự tăng dần và giảm dần

- **Tăng dần (ASC)**: Đây là thứ tự mặc định của `ORDER BY`, tức là các giá trị sẽ được sắp xếp từ nhỏ nhất đến lớn nhất.
- **Giảm dần (DESC)**: Sắp xếp theo thứ tự giảm dần, tức là các giá trị sẽ được sắp xếp từ lớn nhất đến nhỏ nhất.

**Ví dụ**:

```sql
SELECT first_name, hire_date
FROM employees
ORDER BY hire_date DESC;
```

Câu lệnh trên sẽ trả về danh sách nhân viên được sắp xếp theo ngày nhận việc, từ ngày gần nhất đến ngày xa nhất (giảm dần).

---

### 3. Sử dụng ORDER BY với các kiểu dữ liệu

#### Sắp xếp với kiểu số

Đối với các cột có kiểu dữ liệu số (INT, FLOAT, DOUBLE, v.v.), `ORDER BY` sẽ sắp xếp theo giá trị số học.

**Ví dụ**:

```sql
SELECT employee_id, salary
FROM employees
ORDER BY salary DESC;
```

Câu lệnh trên sẽ sắp xếp nhân viên theo lương từ cao xuống thấp.

#### Sắp xếp với kiểu chuỗi

Với các cột kiểu chuỗi (VARCHAR, CHAR, TEXT, v.v.), `ORDER BY` sẽ sắp xếp dữ liệu theo bảng chữ cái.

**Ví dụ**:

```sql
SELECT employee_id, first_name
FROM employees
ORDER BY first_name ASC;
```

Câu lệnh trên sẽ sắp xếp nhân viên theo tên từ A đến Z.

#### Sắp xếp với kiểu ngày giờ

Khi làm việc với kiểu dữ liệu ngày giờ (DATE, DATETIME, TIMESTAMP, v.v.), `ORDER BY` sẽ sắp xếp theo ngày tháng và giờ.

**Ví dụ**:

```sql
SELECT employee_id, hire_date
FROM employees
ORDER BY hire_date ASC;
```

Câu lệnh trên sẽ sắp xếp nhân viên theo ngày nhận việc từ sớm đến muộn.

---

### 4. Ví dụ thực tế với ORDER BY (tiếp theo)

- **Sắp xếp nhân viên theo lương từ cao đến thấp**:

```sql
SELECT employee_id, first_name, salary
FROM employees
ORDER BY salary DESC;
```

**Kết quả:**

| employee_id | first_name | salary |
| ----------- | ---------- | ------ |
| 1           | John       | 9000   |
| 3           | Sarah      | 8500   |
| 5           | Mike       | 8000   |
| 2           | Alice      | 7500   |
| 4           | Bob        | 7000   |

Trong ví dụ này, danh sách nhân viên sẽ được sắp xếp theo lương từ cao nhất đến thấp nhất.

- **Sắp xếp nhân viên theo phòng ban và lương**:

```sql
SELECT employee_id, first_name, department, salary
FROM employees
ORDER BY department ASC, salary DESC;
```

**Kết quả:**

| employee_id | first_name | department | salary |
| ----------- | ---------- | ---------- | ------ |
| 2           | Alice      | HR         | 7500   |
| 1           | John       | HR         | 9000   |
| 4           | Bob        | IT         | 7000   |
| 3           | Sarah      | IT         | 8500   |
| 5           | Mike       | Sales      | 8000   |

Kết quả được sắp xếp theo phòng ban (tăng dần) và sau đó theo lương (giảm dần) trong từng phòng ban.

- **Sắp xếp các sản phẩm theo giá**:

```sql
SELECT product_name, price
FROM products
ORDER BY price ASC;
```

**Kết quả:**

| product_name | price |
| ------------ | ----- |
| Product A    | 100   |
| Product B    | 200   |
| Product C    | 300   |
| Product D    | 500   |
| Product E    | 800   |

Kết quả này sẽ hiển thị các sản phẩm được sắp xếp từ giá thấp nhất đến cao nhất.

- **Sắp xếp các đơn hàng theo ngày đặt hàng**:

```sql
SELECT order_id, order_date
FROM orders
ORDER BY order_date DESC;
```

**Kết quả:**

| order_id | order_date |
| -------- | ---------- |
| 1005     | 2024-11-10 |
| 1004     | 2024-11-05 |
| 1003     | 2024-10-25 |
| 1002     | 2024-10-15 |
| 1001     | 2024-10-01 |

Dữ liệu sẽ được sắp xếp theo ngày đặt hàng từ gần nhất đến xa nhất.

---

### 5. Lưu ý và thực hành tốt

- **Thứ tự ưu tiên**: Khi sử dụng nhiều cột trong `ORDER BY`, các cột sẽ được sắp xếp theo thứ tự từ trái qua phải. Đảm bảo rằng bạn chỉ định đúng thứ tự ưu tiên của các cột.

  **Ví dụ**:

  ```sql
  SELECT first_name, last_name, hire_date
  FROM employees
  ORDER BY last_name ASC, first_name ASC, hire_date DESC;
  ```

  Kết quả sẽ sắp xếp theo **last_name** (tăng dần), sau đó theo **first_name** (tăng dần), và nếu có nhân viên trùng tên, họ sẽ được sắp xếp theo **hire_date** (giảm dần).

- **Sắp xếp theo mặc định**: Nếu bạn không chỉ định `ASC` hoặc `DESC`, SQL Server sẽ sắp xếp theo mặc định là **tăng dần (ASC)**.

  ```sql
  SELECT first_name, salary
  FROM employees
  ORDER BY salary;
  ```

  Câu lệnh trên sẽ sắp xếp theo lương từ thấp đến cao.

- **Hiệu suất**: Việc sắp xếp dữ liệu có thể ảnh hưởng đến hiệu suất của truy vấn, đặc biệt là khi làm việc với các bảng có nhiều dữ liệu. Hãy đảm bảo rằng các cột bạn sắp xếp đã được chỉ mục (index) nếu cần thiết. Điều này giúp tối ưu hóa tốc độ truy vấn.

- **NULLs và sắp xếp**: Trong SQL Server, `NULL` được coi là giá trị nhỏ nhất khi sắp xếp theo thứ tự tăng dần và là giá trị lớn nhất khi sắp xếp theo thứ tự giảm dần. Điều này có thể ảnh hưởng đến kết quả của truy vấn.

  **Ví dụ**:

  ```sql
  SELECT first_name, salary
  FROM employees
  ORDER BY salary ASC;
  ```

  Trong trường hợp này, các bản ghi có giá trị `NULL` sẽ xuất hiện đầu tiên. Nếu bạn muốn thay đổi hành vi này, bạn có thể sử dụng `IS NULL` để xử lý các giá trị `NULL`.

  **Ví dụ xử lý NULL**:

  ```sql
  SELECT first_name, salary
  FROM employees
  ORDER BY salary ASC NULLS LAST;
  ```

  Điều này đảm bảo rằng các giá trị `NULL` sẽ xuất hiện cuối cùng trong danh sách sắp xếp.
