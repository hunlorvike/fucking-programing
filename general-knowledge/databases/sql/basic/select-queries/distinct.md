# **DISTINCT trong SQL Server**

## Mục Lục

1. [Tổng quan về DISTINCT](#1-tổng-quan-về-distinct)
2. [Cú pháp cơ bản của DISTINCT](#2-cú-pháp-cơ-bản-của-distinct)
3. [Cách sử dụng DISTINCT](#3-cách-sử-dụng-distinct)
    - [Lọc giá trị duy nhất trong một cột](#lọc-giá-trị-duy-nhất-trong-một-cột)
    - [Lọc giá trị duy nhất trong nhiều cột](#lọc-giá-trị-duy-nhất-trong-nhiều-cột)
4. [Ví dụ về DISTINCT](#4-ví-dụ-về-distinct)
    - [Ví dụ 1: Sử dụng DISTINCT trên một cột](#ví-dụ-1-sử-dụng-distinct-trên-một-cột)
    - [Ví dụ 2: Sử dụng DISTINCT trên nhiều cột](#ví-dụ-2-sử-dụng-distinct-trên-nhiều-cột)
5. [Lưu ý khi sử dụng DISTINCT](#5-lưu-ý-khi-sử-dụng-distinct)
6. [Kết luận](#6-kết-luận)

---

### 1. Tổng quan về DISTINCT

Trong SQL, từ khóa `DISTINCT` được sử dụng để loại bỏ các giá trị trùng lặp trong kết quả truy vấn và chỉ trả về các giá
trị duy nhất. Điều này rất hữu ích khi bạn cần tìm ra các giá trị không trùng lặp từ một hoặc nhiều cột trong bảng.

Ví dụ, nếu bạn muốn tìm tất cả các giá trị khác nhau trong một cột (ví dụ: tên khách hàng, thành phố, hoặc mã sản phẩm),
`DISTINCT` sẽ giúp bạn chỉ lấy các giá trị duy nhất mà không có bản sao.

### 2. Cú pháp cơ bản của DISTINCT

Cú pháp cơ bản của `DISTINCT` trong SQL là:

```sql
SELECT DISTINCT column_name
FROM table_name;
```

Hoặc khi bạn cần sử dụng `DISTINCT` cho nhiều cột:

```sql
SELECT DISTINCT column1, column2
FROM table_name;
```

### 3. Cách sử dụng DISTINCT

#### Lọc giá trị duy nhất trong một cột

Khi bạn sử dụng `DISTINCT` trên một cột, SQL sẽ trả về tất cả các giá trị duy nhất có trong cột đó.

**Cú pháp**:

```sql
SELECT DISTINCT column_name
FROM table_name;
```

**Ví dụ**:
Giả sử có bảng `Customers` với cột `City`:

```sql
SELECT DISTINCT City
FROM Customers;
```

Kết quả sẽ trả về danh sách tất cả các thành phố mà khách hàng đang sống, với mỗi thành phố chỉ xuất hiện một lần, dù có
bao nhiêu khách hàng từ thành phố đó.

#### Lọc giá trị duy nhất trong nhiều cột

`DISTINCT` cũng có thể được sử dụng để lọc các giá trị duy nhất từ nhiều cột. Khi sử dụng `DISTINCT` với nhiều cột, SQL
sẽ trả về các kết hợp duy nhất của các giá trị trong các cột đó.

**Cú pháp**:

```sql
SELECT DISTINCT column1, column2
FROM table_name;
```

**Ví dụ**:
Giả sử có bảng `Orders` với cột `ProductID` và `CustomerID`:

```sql
SELECT DISTINCT ProductID, CustomerID
FROM Orders;
```

Kết quả sẽ trả về tất cả các kết hợp duy nhất của `ProductID` và `CustomerID`, nghĩa là nếu một khách hàng đã mua cùng
một sản phẩm nhiều lần, kết quả sẽ chỉ xuất hiện một lần cho mỗi kết hợp `ProductID` và `CustomerID`.

### 4. Ví dụ về DISTINCT

#### Ví dụ 1: Sử dụng DISTINCT trên một cột

Giả sử có bảng `Employees` với cột `Department` và bạn muốn tìm tất cả các phòng ban mà các nhân viên đang làm việc (
không bị trùng lặp):

```sql
SELECT DISTINCT Department
FROM Employees;
```

Kết quả có thể là:

| Department |
|------------|
| HR         |
| IT         |
| Sales      |
| Marketing  |

Mặc dù có thể có nhiều nhân viên trong mỗi phòng ban, nhưng chỉ có các giá trị phòng ban duy nhất sẽ được trả về.

#### Ví dụ 2: Sử dụng DISTINCT trên nhiều cột

Giả sử có bảng `Sales` với cột `ProductID` và `CustomerID`, bạn muốn tìm tất cả các kết hợp duy nhất của sản phẩm và
khách hàng:

```sql
SELECT DISTINCT ProductID, CustomerID
FROM Sales;
```

Kết quả có thể là:

| ProductID | CustomerID |
|-----------|------------|
| 101       | 5001       |
| 102       | 5002       |
| 103       | 5003       |
| 104       | 5001       |

Kết quả này sẽ loại bỏ bất kỳ bản ghi trùng lặp nào, chỉ trả về các kết hợp duy nhất của `ProductID` và `CustomerID`.

### 5. Lưu ý khi sử dụng DISTINCT

- **Hiệu suất**: Mặc dù `DISTINCT` rất hữu ích để loại bỏ các giá trị trùng lặp, nhưng nó có thể làm giảm hiệu suất truy
  vấn nếu bạn đang làm việc với một tập dữ liệu rất lớn, vì SQL phải thực hiện việc kiểm tra các giá trị trùng lặp.
- **Sử dụng với nhiều cột**: Khi sử dụng `DISTINCT` với nhiều cột, SQL sẽ kiểm tra sự duy nhất của tất cả các kết hợp
  giữa các cột. Điều này có thể dẫn đến các kết quả không như mong muốn nếu không kiểm soát tốt các cột.
- **Từ khóa DISTINCT có thể không cần thiết**: Nếu dữ liệu của bạn đã được kiểm soát để không có giá trị trùng lặp (
  chẳng hạn, nếu bảng đã có ràng buộc khóa chính hoặc duy nhất), việc sử dụng `DISTINCT` có thể không cần thiết.

### 6. Kết luận

Từ khóa `DISTINCT` trong SQL Server giúp loại bỏ các bản sao và chỉ trả về các giá trị duy nhất trong kết quả truy vấn.
Đây là một công cụ mạnh mẽ khi bạn cần làm sạch dữ liệu hoặc muốn lấy các giá trị độc nhất từ bảng. Tuy nhiên, khi sử
dụng `DISTINCT`, bạn cần lưu ý về hiệu suất và các tình huống sử dụng để đảm bảo rằng kết quả truy vấn đáp ứng yêu cầu
của bạn mà không làm giảm hiệu quả của hệ thống.
