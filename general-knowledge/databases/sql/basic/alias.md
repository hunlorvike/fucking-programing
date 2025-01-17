# **ALIAS trong SQL Server**

## Mục Lục

1. [Tổng quan về ALIAS](#1-tổng-quan-về-alias)
2. [Cú pháp cơ bản của ALIAS](#2-cú-pháp-cơ-bản-của-alias)
3. [Cách sử dụng ALIAS](#3-cách-sử-dụng-alias)
    - [Alias cho bảng](#alias-cho-bảng)
    - [Alias cho cột](#alias-cho-cột)
4. [Ví dụ về ALIAS](#4-ví-dụ-về-alias)
    - [Ví dụ 1: Alias cho bảng](#ví-dụ-1-alias-cho-bảng)
    - [Ví dụ 2: Alias cho cột](#ví-dụ-2-alias-cho-cột)
5. [Lưu ý khi sử dụng ALIAS](#5-lưu-ý-khi-sử-dụng-alias)
6. [Kết luận](#6-kết-luận)

---

### 1. Tổng quan về ALIAS

Trong SQL, `ALIAS` là một tên tạm thời được gán cho bảng hoặc cột trong truy vấn, giúp đơn giản hóa cú pháp và làm cho
câu lệnh dễ đọc hơn. Alias được sử dụng đặc biệt khi bạn muốn thay thế tên dài hoặc phức tạp của bảng/cột bằng một tên
ngắn gọn hơn, hoặc khi sử dụng các phép toán hoặc hàm trong câu truy vấn.

`ALIAS` chỉ có hiệu lực trong phạm vi câu lệnh SQL đang được thực thi và không thay đổi tên thực tế của bảng hoặc cột
trong cơ sở dữ liệu.

### 2. Cú pháp cơ bản của ALIAS

#### Alias cho bảng:

```sql
SELECT column1, column2
FROM table_name AS alias_name;
```

#### Alias cho cột:

```sql
SELECT column_name AS alias_name
FROM table_name;
```

### 3. Cách sử dụng ALIAS

#### Alias cho bảng

Khi bạn làm việc với bảng có tên dài hoặc phức tạp, bạn có thể sử dụng alias để thay thế tên bảng đó trong câu truy vấn.
Điều này giúp câu truy vấn ngắn gọn và dễ hiểu hơn.

**Cú pháp**:

```sql
SELECT column1, column2
FROM table_name AS alias_name;
```

**Ví dụ**:
Giả sử bạn có bảng `Customers` với các cột `CustomerID` và `CustomerName`. Bạn có thể sử dụng alias cho bảng `Customers`
để câu truy vấn ngắn gọn hơn:

```sql
SELECT c.CustomerID, c.CustomerName
FROM Customers AS c;
```

Trong ví dụ này, `c` là alias của bảng `Customers`. Thay vì phải viết `Customers.CustomerID` hoặc
`Customers.CustomerName` mỗi lần, bạn có thể sử dụng alias `c` để tham chiếu đến bảng này.

#### Alias cho cột

Alias có thể được sử dụng để đổi tên cột trong kết quả truy vấn. Điều này rất hữu ích khi bạn sử dụng các phép toán hoặc
hàm trong câu truy vấn và muốn đặt tên dễ hiểu cho các kết quả trả về.

**Cú pháp**:

```sql
SELECT column_name AS alias_name
FROM table_name;
```

**Ví dụ**:
Giả sử bạn có bảng `Orders` với cột `OrderAmount`, bạn muốn tính tổng số tiền đơn hàng và đặt alias cho cột tính toán
này:

```sql
SELECT SUM(OrderAmount) AS TotalAmount
FROM Orders;
```

Trong ví dụ này, `TotalAmount` là alias cho kết quả tính tổng của cột `OrderAmount`. Kết quả trả về sẽ có cột với tên
`TotalAmount` thay vì tên mặc định `SUM(OrderAmount)`.

### 4. Ví dụ về ALIAS

#### Ví dụ 1: Alias cho bảng

Giả sử bạn có bảng `Employees` với cột `EmployeeID`, `FirstName` và `LastName`, bạn có thể sử dụng alias cho bảng
`Employees` để làm cho câu truy vấn dễ đọc hơn:

```sql
SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employees AS e;
```

Trong ví dụ này, `e` là alias cho bảng `Employees`. Bạn có thể sử dụng `e.EmployeeID`, `e.FirstName`, và `e.LastName`
thay vì viết `Employees.EmployeeID`, `Employees.FirstName`, và `Employees.LastName` mỗi lần.

#### Ví dụ 2: Alias cho cột

Giả sử bạn có bảng `Products` với cột `Price` và bạn muốn tính giá trị trung bình của các sản phẩm, bạn có thể sử dụng
alias cho cột này:

```sql
SELECT AVG(Price) AS AveragePrice
FROM Products;
```

Ở đây, `AveragePrice` là alias cho kết quả tính toán của hàm `AVG(Price)`. Thay vì trả về tên hàm `AVG(Price)`, kết quả
trả về sẽ là `AveragePrice`.

### 5. Lưu ý khi sử dụng ALIAS

- **Alias không thay đổi tên thực tế của bảng/cột**: Alias chỉ có tác dụng trong phạm vi truy vấn và không thay đổi tên
  thực tế của bảng hoặc cột trong cơ sở dữ liệu.
- **Alias có thể không cần dùng từ khóa `AS`**: Từ khóa `AS` là tùy chọn và có thể bỏ qua, bạn có thể trực tiếp sử dụng
  alias mà không cần từ khóa `AS`. Tuy nhiên, sử dụng `AS` làm cho câu truy vấn dễ đọc hơn.

  Ví dụ:

  ```sql
  SELECT FirstName AS FN, LastName AS LN
  FROM Employees;
  ```

  Hoặc bạn có thể viết ngắn gọn:

  ```sql
  SELECT FirstName FN, LastName LN
  FROM Employees;
  ```

- **Alias giúp cải thiện khả năng đọc hiểu**: Alias rất hữu ích khi làm việc với các phép toán phức tạp hoặc các bảng có
  tên dài. Nó giúp cho câu truy vấn trở nên dễ đọc và dễ hiểu hơn.

### 6. Kết luận

Từ khóa `ALIAS` trong SQL Server giúp bạn đơn giản hóa và cải thiện khả năng đọc hiểu câu truy vấn bằng cách gán tên tạm
thời cho bảng và cột. Việc sử dụng alias không chỉ giúp mã SQL ngắn gọn hơn mà còn giúp bạn dễ dàng làm việc với các
phép toán và hàm trong câu truy vấn. Tuy nhiên, bạn cần nhớ rằng alias chỉ có tác dụng trong phạm vi câu truy vấn và
không thay đổi tên thực tế của bảng hoặc cột trong cơ sở dữ liệu.
