# Giới hạn kết quả trong SQL Server

## Mục Lục

1. [Tổng quan về Giới hạn kết quả](#1-tổng-quan-về-giới-hạn-kết-quả)
   - [Giới hạn kết quả là gì?](#giới-hạn-kết-quả-là-gì)
   - [Lợi ích của Giới hạn kết quả](#lợi-ích-của-giới-hạn-kết-quả)
   - [Giới hạn kết quả hoạt động như thế nào?](#giới-hạn-kết-quả-hoạt-động-như-thế-nào)
2. [Các cách giới hạn kết quả trong SQL Server](#2-các-cách-giới-hạn-kết-quả-trong-sql-server)
   - [Sử dụng TOP](#sử-dụng-top)
   - [Sử dụng OFFSET-FETCH](#sử-dụng-offset-fetch)
3. [Ví dụ thực tế](#3-ví-dụ-thực-tế)
4. [Lưu ý và thực hành tốt](#4-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Giới hạn kết quả

#### Giới hạn kết quả là gì?

Giới hạn kết quả trong SQL Server là một kỹ thuật giúp bạn kiểm soát số lượng bản ghi được trả về từ một truy vấn. Điều này rất hữu ích khi bạn chỉ cần một phần nhỏ dữ liệu thay vì toàn bộ tập dữ liệu. Các mệnh đề và kỹ thuật khác nhau có thể được sử dụng để giới hạn kết quả, chẳng hạn như `TOP`, `OFFSET-FETCH`, hoặc các điều kiện lọc kết hợp với mệnh đề `WHERE`.

#### Lợi ích của Giới hạn kết quả

- **Tiết kiệm tài nguyên**: Giới hạn số lượng bản ghi trả về giúp giảm tải cho hệ thống và tiết kiệm bộ nhớ.
- **Cải thiện hiệu suất**: Giới hạn kết quả giúp giảm thiểu thời gian xử lý khi làm việc với bảng lớn hoặc dữ liệu phức tạp.
- **Dễ dàng phân trang dữ liệu**: Khi xây dựng các ứng dụng web hoặc API, việc giới hạn kết quả giúp phân trang dữ liệu, chỉ hiển thị một phần của dữ liệu tại một thời điểm.

#### Giới hạn kết quả hoạt động như thế nào?

1. **TOP**: Giới hạn số lượng bản ghi trả về, thường được sử dụng trong các truy vấn cần lấy một số lượng bản ghi nhất định từ đầu danh sách.
2. **OFFSET-FETCH**: Cho phép bạn phân trang dữ liệu, nghĩa là lấy một phần kết quả dựa trên chỉ mục và số lượng bản ghi yêu cầu.

---

### 2. Các cách giới hạn kết quả trong SQL Server

#### Sử dụng TOP

Mệnh đề `TOP` trong SQL Server cho phép bạn chỉ định số lượng bản ghi bạn muốn lấy từ kết quả truy vấn.

**Cú pháp:**

```sql
SELECT TOP (n) column1, column2, ...
FROM table_name
WHERE condition
ORDER BY column1;
```

Trong đó:

- `n`: Số lượng bản ghi mà bạn muốn lấy.
- `column1, column2, ...`: Các cột bạn muốn truy xuất.
- `WHERE condition`: Điều kiện lọc (tuỳ chọn).
- `ORDER BY`: Sắp xếp dữ liệu (tuỳ chọn nhưng nên được sử dụng để đảm bảo tính nhất quán).

**Ví dụ**:

```sql
SELECT TOP 5 employee_id, first_name, salary
FROM employees
ORDER BY salary DESC;
```

Câu lệnh trên sẽ trả về 5 nhân viên có lương cao nhất.

**Lưu ý**:

- Nếu không có mệnh đề `ORDER BY`, SQL Server sẽ trả về bất kỳ bản ghi nào mà không có thứ tự xác định.
- `TOP` có thể được sử dụng với hoặc không có `ORDER BY` tùy thuộc vào nhu cầu sắp xếp.

#### Sử dụng OFFSET-FETCH

Mệnh đề `OFFSET-FETCH` được sử dụng trong SQL Server để phân trang kết quả truy vấn. Bạn có thể chỉ định số lượng bản ghi bắt đầu từ một chỉ mục nhất định, rất hữu ích trong các ứng dụng web hoặc API khi bạn muốn chia nhỏ kết quả thành các trang.

**Cú pháp**:

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1
OFFSET (n) ROWS
FETCH NEXT (m) ROWS ONLY;
```

Trong đó:

- `n`: Số lượng bản ghi bạn muốn bỏ qua (OFFSET).
- `m`: Số lượng bản ghi bạn muốn lấy sau khi bỏ qua (FETCH NEXT).
- `ORDER BY`: Cần thiết để chỉ định cách sắp xếp các bản ghi trước khi áp dụng `OFFSET` và `FETCH`.

**Ví dụ**:

```sql
SELECT employee_id, first_name, salary
FROM employees
ORDER BY salary DESC
OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY;
```

Câu lệnh trên sẽ bỏ qua 10 nhân viên đầu tiên và trả về 5 nhân viên tiếp theo có lương cao nhất.

- **OFFSET 10 ROWS**: Bỏ qua 10 bản ghi đầu tiên.
- **FETCH NEXT 5 ROWS ONLY**: Lấy 5 bản ghi tiếp theo sau khi bỏ qua.

**Lưu ý**:

- Mệnh đề `OFFSET-FETCH` yêu cầu mệnh đề `ORDER BY` để đảm bảo kết quả có thể phân trang chính xác.
- Phân trang với `OFFSET-FETCH` rất hữu ích khi xây dựng các ứng dụng web hoặc API có chức năng phân trang.

---

Dưới đây là các ví dụ thực tế với kết quả minh họa cho việc giới hạn kết quả trong SQL Server, giúp bạn dễ dàng hình dung cách các kỹ thuật này hoạt động.

---

### 3. Ví dụ thực tế

#### 1. **Lấy 10 bản ghi đầu tiên từ bảng sản phẩm (TOP)**

**Câu lệnh SQL**:

```sql
SELECT TOP 10 product_name, price
FROM products
ORDER BY price DESC;
```

**Kết quả giả định**:

| product_name | price |
| ------------ | ----- |
| Laptop A     | 2000  |
| Laptop B     | 1900  |
| Laptop C     | 1800  |
| Phone X      | 1500  |
| Phone Y      | 1400  |
| Tablet Z     | 1200  |
| Headphones X | 1100  |
| Headphones Y | 1000  |
| Smartwatch A | 900   |
| Smartwatch B | 850   |

Trong ví dụ trên, câu lệnh sẽ trả về 10 sản phẩm có giá cao nhất từ bảng `products`, được sắp xếp theo thứ tự giảm dần của giá (`ORDER BY price DESC`).

---

#### 2. **Lấy 5 bản ghi tiếp theo sau khi bỏ qua 10 bản ghi đầu tiên (phân trang sử dụng OFFSET-FETCH)**

**Câu lệnh SQL**:

```sql
SELECT product_name, price
FROM products
ORDER BY price DESC
OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY;
```

**Kết quả giả định**:

| product_name | price |
| ------------ | ----- |
| Tablet A     | 800   |
| Tablet B     | 750   |
| Headphones Z | 700   |
| Smartwatch C | 650   |
| Smartwatch D | 600   |

Trong ví dụ này, câu lệnh sẽ bỏ qua 10 sản phẩm đầu tiên và lấy 5 sản phẩm tiếp theo có giá giảm dần. Đây là một kỹ thuật phân trang, rất hữu ích trong các ứng dụng web khi bạn cần hiển thị dữ liệu theo trang.

---

#### 3. **Lấy 10 nhân viên có lương cao nhất (TOP)**

**Câu lệnh SQL**:

```sql
SELECT TOP 10 employee_id, first_name, salary
FROM employees
ORDER BY salary DESC;
```

**Kết quả giả định**:

| employee_id | first_name | salary |
| ----------- | ---------- | ------ |
| 1           | John       | 8000   |
| 2           | Mary       | 7500   |
| 3           | James      | 7000   |
| 4           | Anna       | 6800   |
| 5           | Peter      | 6700   |
| 6           | Sam        | 6500   |
| 7           | Linda      | 6300   |
| 8           | David      | 6200   |
| 9           | Sarah      | 6000   |
| 10          | Bob        | 5800   |

Câu lệnh trên sẽ trả về danh sách 10 nhân viên có mức lương cao nhất từ bảng `employees`.

---

#### 4. **Phân trang kết quả nhân viên (Lấy từ bản ghi thứ 11 đến thứ 20)**

**Câu lệnh SQL**:

```sql
SELECT employee_id, first_name, salary
FROM employees
ORDER BY salary DESC
OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
```

**Kết quả giả định**:

| employee_id | first_name | salary |
| ----------- | ---------- | ------ |
| 11          | Helen      | 5700   |
| 12          | Tom        | 5600   |
| 13          | Nancy      | 5500   |
| 14          | Emma       | 5400   |
| 15          | Jacob      | 5300   |
| 16          | Peter      | 5200   |
| 17          | Hannah     | 5100   |
| 18          | Jack       | 5000   |
| 19          | Lily       | 4900   |
| 20          | Sophia     | 4800   |

Trong ví dụ này, câu lệnh sẽ bỏ qua 10 nhân viên đầu tiên và lấy 10 nhân viên tiếp theo có mức lương cao, từ bản ghi thứ 11 đến thứ 20. Đây là cách phân trang dữ liệu trong các ứng dụng cần xử lý lượng dữ liệu lớn.

---

### 4. Lưu ý và thực hành tốt

- **Hiệu suất**: Việc sử dụng `TOP` để lấy một số lượng bản ghi nhất định giúp cải thiện hiệu suất khi làm việc với các bảng dữ liệu lớn. Mặc dù vậy, nếu không sử dụng mệnh đề `ORDER BY` trong câu lệnh `TOP`, kết quả có thể không nhất quán.
- **Phân trang dữ liệu**: Khi sử dụng `OFFSET-FETCH` trong các ứng dụng web hoặc API, bạn có thể dễ dàng phân trang dữ liệu, giúp giảm tải cho hệ thống và cải thiện trải nghiệm người dùng. Đảm bảo rằng bạn luôn sử dụng `ORDER BY` để có kết quả phân trang chính xác.

- **Lựa chọn kỹ thuật phù hợp**:

  - Dùng `TOP` khi bạn chỉ cần một số lượng bản ghi cụ thể (ví dụ: 10 bản ghi đầu tiên).
  - Dùng `OFFSET-FETCH` khi bạn cần phân trang dữ liệu, ví dụ: để lấy dữ liệu từ một trang nhất định trong một ứng dụng web.

- **Cẩn thận với thứ tự**: Đối với mệnh đề `OFFSET-FETCH`, luôn sử dụng `ORDER BY` để đảm bảo thứ tự chính xác của kết quả truy vấn. Nếu không, bạn có thể nhận được kết quả không mong muốn do các bản ghi được lấy theo thứ tự ngẫu nhiên.
