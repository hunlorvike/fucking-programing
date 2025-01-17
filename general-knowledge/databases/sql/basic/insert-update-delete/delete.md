# DELETE trong SQL Server

## Mục Lục

1. [Tổng quan về câu lệnh DELETE](#1-tổng-quan-về-câu-lệnh-delete)
    - [DELETE là gì?](#delete-là-gì)
    - [Lợi ích của câu lệnh DELETE](#lợi-ích-của-câu-lệnh-delete)
    - [Câu lệnh DELETE hoạt động như thế nào?](#câu-lệnh-delete-hoạt-động-như-thế-nào)
2. [Cú pháp cơ bản của câu lệnh DELETE](#2-cú-pháp-cơ-bản-của-câu-lệnh-delete)
    - [Xóa bản ghi từ một bảng](#xóa-bản-ghi-từ-một-bảng)
    - [Xóa tất cả bản ghi trong bảng](#xóa-tất-cả-bản-ghi-trong-bảng)
3. [Các tùy chọn mở rộng của câu lệnh DELETE](#3-các-tùy-chọn-mở-rộng-của-câu-lệnh-delete)
    - [WHERE](#where)
    - [TOP](#top)
4. [Các ví dụ thực tế với DELETE](#4-các-ví-dụ-thực-tế-với-delete)
5. [Lưu ý và thực hành tốt](#5-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về câu lệnh DELETE

#### DELETE là gì?

Câu lệnh `DELETE` trong SQL Server được sử dụng để xóa một hoặc nhiều bản ghi trong bảng dựa trên điều kiện xác định.
Đây là một câu lệnh quan trọng trong SQL để làm sạch hoặc loại bỏ dữ liệu không còn cần thiết trong cơ sở dữ liệu.

#### Lợi ích của câu lệnh DELETE

- **Quản lý dữ liệu**: Giúp loại bỏ dữ liệu không cần thiết hoặc đã lỗi thời trong bảng.
- **Giảm thiểu sự cồng kềnh**: Xóa các bản ghi giúp duy trì kích thước bảng nhỏ gọn và cải thiện hiệu suất của các truy
  vấn.
- **Bảo mật**: Trong một số trường hợp, xóa dữ liệu không còn cần thiết có thể giúp bảo vệ thông tin nhạy cảm.

#### Câu lệnh DELETE hoạt động như thế nào?

Câu lệnh `DELETE` thực hiện các bước sau:

1. **Lọc dữ liệu cần xóa**: Nếu có điều kiện `WHERE`, SQL Server sẽ tìm các bản ghi thỏa mãn điều kiện đó.
2. **Xóa bản ghi**: Sau khi lọc, các bản ghi phù hợp sẽ bị xóa khỏi bảng.
3. **Cập nhật các chỉ mục và dữ liệu liên quan**: Khi dữ liệu bị xóa, các chỉ mục và các bảng liên quan sẽ được cập
   nhật (nếu có).

---

### 2. Cú pháp cơ bản của câu lệnh DELETE

#### Xóa bản ghi từ một bảng

Câu lệnh `DELETE` có thể được sử dụng để xóa các bản ghi cụ thể từ một bảng, dựa trên một điều kiện xác định.

**Cú pháp**:

```sql
DELETE FROM table_name
WHERE condition;
```

**Ví dụ**:

```sql
DELETE FROM employees
WHERE employee_id = 10;
```

Trong ví dụ này, câu lệnh sẽ xóa bản ghi có `employee_id` bằng 10 từ bảng `employees`.

#### Xóa tất cả bản ghi trong bảng

Nếu không có điều kiện `WHERE`, câu lệnh `DELETE` sẽ xóa tất cả các bản ghi trong bảng. Tuy nhiên, câu lệnh này vẫn giữ
lại cấu trúc bảng và các chỉ mục của bảng.

**Cú pháp**:

```sql
DELETE FROM table_name;
```

**Ví dụ**:

```sql
DELETE FROM employees;
```

Câu lệnh này sẽ xóa tất cả các bản ghi trong bảng `employees`, nhưng bảng vẫn tồn tại và có thể sử dụng cho các thao tác
khác.

---

### 3. Các tùy chọn mở rộng của câu lệnh DELETE

#### WHERE

`WHERE` được sử dụng để xác định điều kiện cho các bản ghi cần xóa. Nếu không có `WHERE`, tất cả các bản ghi trong bảng
sẽ bị xóa.

**Cú pháp**:

```sql
DELETE FROM table_name
WHERE condition;
```

**Ví dụ**:

```sql
DELETE FROM employees
WHERE department = 'HR';
```

Câu lệnh trên sẽ xóa tất cả các bản ghi trong bảng `employees` nơi `department` là `HR`.

#### TOP

Tùy chọn `TOP` có thể được sử dụng trong câu lệnh `DELETE` để giới hạn số lượng bản ghi bị xóa. Điều này rất hữu ích khi
bạn chỉ muốn xóa một số lượng bản ghi nhất định mà không muốn xóa toàn bộ bảng.

**Cú pháp**:

```sql
DELETE TOP (n) FROM table_name
WHERE condition;
```

**Ví dụ**:

```sql
DELETE TOP (5) FROM employees
WHERE department = 'Sales';
```

Câu lệnh này sẽ xóa tối đa 5 bản ghi từ bảng `employees` trong phòng ban `Sales`.

---

### 4. Các ví dụ thực tế với DELETE

#### Xóa một nhân viên dựa trên `employee_id`

**Câu lệnh SQL**:

```sql
DELETE FROM employees
WHERE employee_id = 101;
```

**Giải thích**:

- Câu lệnh này sẽ xóa bản ghi của nhân viên có `employee_id` là 101 từ bảng `employees`.

---

#### Xóa tất cả nhân viên trong phòng ban cụ thể

**Câu lệnh SQL**:

```sql
DELETE FROM employees
WHERE department = 'HR';
```

**Giải thích**:

- Câu lệnh này sẽ xóa tất cả các nhân viên thuộc phòng ban `HR`.

---

#### Xóa 10 bản ghi đầu tiên trong bảng `employees`

**Câu lệnh SQL**:

```sql
DELETE TOP (10) FROM employees;
```

**Giải thích**:

- Câu lệnh này sẽ xóa tối đa 10 bản ghi đầu tiên trong bảng `employees`, tùy theo thứ tự của các bản ghi trong bảng.

---

#### Xóa tất cả các bản ghi trong bảng

**Câu lệnh SQL**:

```sql
DELETE FROM employees;
```

**Giải thích**:

- Câu lệnh này sẽ xóa tất cả các bản ghi trong bảng `employees`, nhưng bảng và cấu trúc của nó vẫn sẽ được giữ lại.

---

### 5. Lưu ý và thực hành tốt

- **Sử dụng điều kiện `WHERE` cẩn thận**: Nếu không có điều kiện `WHERE`, tất cả các bản ghi trong bảng sẽ bị xóa. Vì
  vậy, hãy đảm bảo rằng bạn đã xác định chính xác điều kiện trước khi thực thi câu lệnh.
- **Sử dụng giao dịch (Transactions)**: Khi thực hiện xóa dữ liệu quan trọng, hãy bao bọc trong một giao dịch để đảm bảo
  khả năng khôi phục nếu có sự cố xảy ra.
- **Kiểm tra trước khi xóa**: Để tránh xóa dữ liệu không mong muốn, bạn có thể thực hiện một truy vấn `SELECT` với cùng
  điều kiện `WHERE` trước khi thực hiện câu lệnh `DELETE`.
- **Sao lưu dữ liệu trước khi xóa**: Nếu bạn đang xóa một lượng lớn dữ liệu, hãy đảm bảo có bản sao lưu đầy đủ của cơ sở
  dữ liệu hoặc bảng trước khi xóa.
- **Tối ưu hóa hiệu suất**: Khi xóa dữ liệu từ các bảng có số lượng bản ghi lớn, hãy xem xét việc sử dụng các chỉ mục
  hoặc phân mảnh bảng để cải thiện hiệu suất của các truy vấn `DELETE`.
