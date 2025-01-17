# Cross Join trong SQL Server

## Mục Lục

1. [Tổng quan về Cross Join](#1-tổng-quan-về-cross-join)
    - [Cross Join là gì?](#cross-join-là-gì)
    - [Lợi ích và ứng dụng của Cross Join](#lợi-ích-và-ứng-dụng-của-cross-join)
    - [Cách hoạt động của Cross Join](#cách-hoạt-động-của-cross-join)
2. [Cú pháp và cách sử dụng Cross Join](#2-cú-pháp-và-cách-sử-dụng-cross-join)
    - [Cú pháp Cross Join cơ bản](#cú-pháp-cross-join-cơ-bản)
    - [Ví dụ thực tế sử dụng Cross Join](#ví-dụ-thực-tế-sử-dụng-cross-join)
3. [Kết hợp với các mệnh đề khác](#3-kết-hợp-với-các-mệnh-đề-khác)
    - [Cross Join với WHERE](#cross-join-với-where)
    - [Cross Join với ORDER BY](#cross-join-với-order-by)
4. [Lưu ý và thực hành tốt](#4-lưu-ý-và-thực-hành-tốt)

---

### 1. Tổng quan về Cross Join

#### Cross Join là gì?

Trong SQL Server, **Cross Join** là một loại phép kết nối giữa hai bảng mà không yêu cầu bất kỳ điều kiện kết nối nào (
không có mối quan hệ giữa các bảng). Khi thực hiện một **Cross Join**, mỗi bản ghi trong bảng đầu tiên sẽ kết hợp với
mỗi bản ghi trong bảng thứ hai, tạo thành một tập hợp các kết quả gọi là **Cartesian Product** (tích Cartesian).

Với một bảng có `m` bản ghi và một bảng có `n` bản ghi, kết quả của phép **Cross Join** sẽ là một bảng có `m * n` bản
ghi.

![Cross join](/assets/images/sql-joins-venn-diagrams-cross-join-1.png)

#### Lợi ích và ứng Vdụng của Cross Join

- **Tạo dữ liệu mẫu**: Cross Join có thể được sử dụng để tạo dữ liệu giả định hoặc mô phỏng các trường hợp với tất cả
  các kết hợp có thể giữa các tập hợp dữ liệu.
- **Tạo kết hợp giữa nhiều yếu tố**: Được dùng trong các trường hợp cần tạo ra mọi kết hợp có thể giữa các tập hợp (ví
  dụ: kết hợp mọi sản phẩm với mọi màu sắc, kích thước, v.v.).
- **Ứng dụng trong phân tích**: Có thể sử dụng để phân tích các kết hợp giữa các yếu tố mà không có mối quan hệ cụ thể
  giữa chúng.

#### Cách hoạt động của Cross Join

Cross Join kết hợp mỗi bản ghi của bảng đầu tiên với mỗi bản ghi của bảng thứ hai mà không cần điều kiện kết nối. Điều
này tạo ra một số lượng kết quả rất lớn nếu hai bảng có số lượng bản ghi lớn.

Ví dụ, nếu bảng A có 3 bản ghi và bảng B có 4 bản ghi, kết quả của Cross Join sẽ có 3 * 4 = 12 bản ghi.

---

### 2. Cú pháp và cách sử dụng Cross Join

#### Cú pháp Cross Join cơ bản

Cú pháp cơ bản của **Cross Join** như sau:

```sql
SELECT column1, column2, ...
FROM table1
CROSS JOIN table2;
```

Trong đó:

- `table1` và `table2` là tên của các bảng mà bạn muốn kết hợp.
- `column1, column2, ...` là các cột bạn muốn lấy từ kết quả kết hợp.

**Lưu ý**: Cross Join không yêu cầu điều kiện kết nối (khác với các kiểu JOIN khác như INNER JOIN, LEFT JOIN, v.v.).

#### Ví dụ thực tế sử dụng Cross Join

Giả sử bạn có hai bảng: `products` và `colors`. Bảng `products` có các sản phẩm, và bảng `colors` có các màu sắc.

**Bảng products**:

| product_id | product_name |
|------------|--------------|
| 1          | Laptop       |
| 2          | Phone        |
| 3          | Tablet       |

**Bảng colors**:

| color_id | color_name |
|----------|------------|
| 1        | Red        |
| 2        | Blue       |
| 3        | Green      |

**Câu lệnh SQL**:

```sql
SELECT p.product_name, c.color_name
FROM products p
CROSS JOIN colors c;
```

**Kết quả giả định**:

| product_name | color_name |
|--------------|------------|
| Laptop       | Red        |
| Laptop       | Blue       |
| Laptop       | Green      |
| Phone        | Red        |
| Phone        | Blue       |
| Phone        | Green      |
| Tablet       | Red        |
| Tablet       | Blue       |
| Tablet       | Green      |

Trong ví dụ trên, mỗi sản phẩm được kết hợp với mỗi màu sắc, tạo thành tất cả các kết hợp có thể.

---

### 3. Kết hợp với các mệnh đề khác

#### Cross Join với WHERE

Mặc dù Cross Join không yêu cầu điều kiện kết nối, bạn có thể kết hợp nó với mệnh đề `WHERE` để lọc kết quả sau khi kết
hợp. Điều này có thể giúp bạn chỉ lấy những kết hợp thỏa mãn điều kiện nhất định.

**Ví dụ**:

```sql
SELECT p.product_name, c.color_name
FROM products p
CROSS JOIN colors c
WHERE c.color_name = 'Red';
```

**Kết quả giả định**:

| product_name | color_name |
|--------------|------------|
| Laptop       | Red        |
| Phone        | Red        |
| Tablet       | Red        |

Trong ví dụ trên, kết quả chỉ bao gồm các kết hợp mà màu sắc là 'Red'.

#### Cross Join với ORDER BY

Kết quả của Cross Join có thể được sắp xếp bằng cách sử dụng mệnh đề `ORDER BY` nếu bạn muốn kết quả hiển thị theo một
thứ tự cụ thể.

**Ví dụ**:

```sql
SELECT p.product_name, c.color_name
FROM products p
CROSS JOIN colors c
ORDER BY p.product_name, c.color_name;
```

**Kết quả giả định**:

| product_name | color_name |
|--------------|------------|
| Laptop       | Blue       |
| Laptop       | Green      |
| Laptop       | Red        |
| Phone        | Blue       |
| Phone        | Green      |
| Phone        | Red        |
| Tablet       | Blue       |
| Tablet       | Green      |
| Tablet       | Red        |

Trong ví dụ này, kết quả được sắp xếp theo tên sản phẩm và tên màu sắc.

---

### 4. Lưu ý và thực hành tốt

- **Hiệu suất**: Cross Join có thể tạo ra một số lượng bản ghi rất lớn, đặc biệt khi các bảng có số lượng bản ghi lớn.
  Cần thận trọng khi sử dụng để tránh làm giảm hiệu suất hệ thống.
- **Dữ liệu kết quả**: Vì Cross Join tạo ra tất cả các kết hợp có thể giữa các bảng, nên kết quả có thể rất lớn. Hãy cân
  nhắc sử dụng các điều kiện lọc (mệnh đề `WHERE`) để hạn chế số lượng kết quả trả về khi cần thiết.
- **Tránh sử dụng với bảng lớn**: Nếu bạn đang làm việc với các bảng lớn, hãy tránh sử dụng Cross Join nếu không có mục
  đích cụ thể. Việc kết hợp các bảng lớn có thể tạo ra một lượng dữ liệu khổng lồ, gây ảnh hưởng đến hiệu suất.
- **Kết hợp với các mệnh đề khác**: Cross Join có thể kết hợp với các mệnh đề như `WHERE`, `ORDER BY`, hoặc `LIMIT` để
  tùy chỉnh kết quả trả về theo nhu cầu cụ thể.

---

### Tổng kết

Cross Join là một kỹ thuật mạnh mẽ trong SQL Server cho phép bạn kết hợp hai bảng mà không cần điều kiện kết nối. Nó có
thể hữu ích trong việc tạo các kết hợp giữa các yếu tố hoặc tạo dữ liệu giả định. Tuy nhiên, do tính chất của nó tạo ra
tất cả các kết hợp có thể, việc sử dụng Cross Join cần được thực hiện cẩn thận, đặc biệt khi làm việc với các bảng lớn.
