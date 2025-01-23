## **🚀 "GIẢI MÃ" CÁC HÀM NÂNG CAO TRONG SQL SERVER: "VŨ KHÍ" PHÂN TÍCH DỮ LIỆU CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một nhóm hàm cực kỳ quan trọng trong SQL Server: Các
hàm nâng cao (Advanced Functions). Đây là những "chiêu thức" lợi hại giúp bạn làm chủ dữ liệu, giải quyết các bài toán
phức tạp và tạo ra những báo cáo chuyên sâu. Cùng mình "mổ xẻ" chúng nhé!

### **I. HÀM NÂNG CAO LÀ GÌ? (LÀM GÌ ĐƯỢC?)**

- **Hàm nâng cao (Advanced Functions):** Là các hàm trong SQL Server cung cấp các chức năng phức tạp hơn, ngoài các hàm
  cơ bản như `SUM`, `AVG`, `COUNT`.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn có một con dao đa năng: có thể cắt, gọt, bào,... nhiều thứ khác nhau (thay vì chỉ cắt).
- **Quan trọng vì:**
    - **Phân tích dữ liệu:** Giúp bạn phân tích dữ liệu sâu hơn, tạo ra insight (thông tin giá trị).
    - **Tính toán phức tạp:** Thực hiện các tính toán phức tạp hơn trên dữ liệu.
    - **Làm đẹp dữ liệu:** Chuyển đổi, định dạng dữ liệu theo ý muốn.
    - **Tối ưu truy vấn:** Dùng các hàm window để tối ưu các truy vấn phức tạp.

### **II. CÁC HÀM NÂNG CAO PHỔ BIẾN (NHỮNG "CHIÊU" THƯỜNG DÙNG)**

1. **Hàm Window (Window Functions):** Tính toán trên một tập hợp các dòng (window) liên quan đến dòng hiện tại (ví dụ:
   `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`).
2. **Hàm Chuỗi (String Functions):** Thao tác với chuỗi ký tự (`SUBSTRING()`, `LEFT()`, `RIGHT()`, `LEN()`, `UPPER()`,
   `LOWER()`, `REPLACE()`, `TRIM()`).
3. **Hàm Ngày và Giờ (Date and Time Functions):** Thao tác với ngày và giờ (`GETDATE()`, `DATEADD()`, `DATEDIFF()`,
   `DATEPART()`, `FORMAT()`).
4. **Hàm Toán học (Mathematical Functions):** Tính toán số học (`ABS()`, `ROUND()`, `FLOOR()`, `CEILING()`, `POWER()`,
   `SQRT()`, `RAND()`).
5. **Hàm Chuyển đổi (Conversion Functions):** Chuyển đổi giữa các kiểu dữ liệu (`CONVERT()`, `CAST()`).
6. **Hàm Logic (Logical Functions):** Thực hiện các phép logic (`IIF()`, `CASE WHEN`).
7. **Hàm Băm (Hash Functions):** Tạo giá trị băm của dữ liệu (`CHECKSUM()`, `HASHBYTES()`).
8. **Hàm JSON (JSON Functions):** Làm việc với dữ liệu JSON (`JSON_VALUE()`, `JSON_QUERY()`, `FOR JSON`).

### **III. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

#### **1. HÀM WINDOW (WINDOW FUNCTIONS)**

```sql
SELECT
    FirstName,
    LastName,
    Salary,
    RANK() OVER (ORDER BY Salary DESC) AS SalaryRank
FROM Employees;
```

- **Giải thích:** Lấy tên, lương và xếp hạng lương của nhân viên (tính hạng theo lương).
- **`RANK() OVER (ORDER BY Salary DESC)`:** Xếp hạng theo lương từ cao đến thấp.

#### **2. HÀM CHUỖI (STRING FUNCTIONS)**

```sql
SELECT
    FirstName,
    LEFT(FirstName, 3) AS ShortName,
    UPPER(LastName) AS LastNameUpper,
    REPLACE(FirstName, 'John', 'Jon') AS FirstNameReplaced
FROM Employees
WHERE LEN(FirstName) > 3;
```

- **Giải thích:** Lấy tên, rút gọn tên, viết hoa họ và thay thế tên "John" thành "Jon".
- **`LEFT(FirstName, 3)`:** Lấy 3 ký tự đầu của tên.
- **`UPPER(LastName)`:** Viết hoa họ.
- **`REPLACE(FirstName, 'John', 'Jon')`:** Thay thế "John" bằng "Jon".
- **`LEN(FirstName) > 3`:** Lọc các nhân viên có tên dài hơn 3 ký tự.

#### **3. HÀM NGÀY VÀ GIỜ (DATE AND TIME FUNCTIONS)**

```sql
SELECT
    OrderDate,
    DATEADD(day, 7, OrderDate) AS DueDate,
    DATEDIFF(day, OrderDate, GETDATE()) AS DaysSinceOrder,
    FORMAT(OrderDate, 'dd/MM/yyyy') AS FormattedOrderDate
FROM Orders;
```

- **Giải thích:** Lấy ngày đặt hàng, ngày đáo hạn (sau 7 ngày), số ngày từ ngày đặt hàng đến hiện tại, và format lại
  ngày đặt hàng.
- **`DATEADD(day, 7, OrderDate)`:** Cộng 7 ngày vào ngày đặt hàng.
- **`DATEDIFF(day, OrderDate, GETDATE())`:** Tính số ngày từ ngày đặt hàng đến hiện tại.
- **`FORMAT(OrderDate, 'dd/MM/yyyy')`:** Định dạng ngày theo kiểu `dd/MM/yyyy`.

#### **4. HÀM TOÁN HỌC (MATHEMATICAL FUNCTIONS)**

```sql
SELECT
    Salary,
    ROUND(Salary, 0) AS RoundedSalary,
    ABS(Salary - 5000) AS SalaryDiff,
    SQRT(Salary) AS SalarySqrt
FROM Employees
WHERE Department = 'IT';
```

- **Giải thích:** Lấy lương, làm tròn lương, độ lệch lương so với 5000, và căn bậc 2 của lương của nhân viên phòng IT.
- **`ROUND(Salary, 0)`:** Làm tròn lương về số nguyên.
- **`ABS(Salary - 5000)`:** Tính giá trị tuyệt đối của hiệu số lương và 5000.
- **`SQRT(Salary)`:** Tính căn bậc hai của lương.

#### **5. HÀM CHUYỂN ĐỔI (CONVERSION FUNCTIONS)**

```sql
SELECT
    OrderID,
    CONVERT(VARCHAR(10), OrderDate, 103) AS OrderDateStr,
    CAST(Salary AS DECIMAL(10, 2)) AS SalaryDecimal
FROM Orders
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID
WHERE Department = 'Sales';
```

- **Giải thích:** Lấy ID đơn hàng, ngày đặt hàng dạng chuỗi và lương dạng decimal.
- **`CONVERT(VARCHAR(10), OrderDate, 103)`:** Chuyển ngày thành chuỗi theo format `dd/MM/yyyy`.
- **`CAST(Salary AS DECIMAL(10, 2))`:** Chuyển lương thành số decimal với 2 chữ số thập phân.

#### **6. HÀM LOGIC (LOGICAL FUNCTIONS)**

```sql
SELECT
    FirstName,
    LastName,
    Salary,
    IIF(Salary > 7000, 'High Salary', 'Low Salary') AS SalaryLevel,
    CASE
        WHEN Department = 'IT' THEN 'Technical'
        WHEN Department = 'Sales' THEN 'Commercial'
        ELSE 'Other'
    END AS DepartmentType
FROM Employees
WHERE Department IN ('IT', 'Sales', 'HR');
```

- **Giải thích:** Lấy tên, lương, phân loại lương và loại phòng ban.
- **`IIF(Salary > 7000, 'High Salary', 'Low Salary')`:** Nếu lương > 7000 thì 'High Salary', ngược lại thì 'Low Salary'.
- **`CASE WHEN ... THEN ... ELSE ... END`:** Phân loại phòng ban.

#### **7. HÀM BĂM (HASH FUNCTIONS)**

```sql
SELECT
    FirstName,
    LastName,
    HASHBYTES('SHA2_256', FirstName) AS FirstNameHash
FROM Employees
WHERE Department = 'IT';
```

- **Giải thích:** Lấy tên và giá trị băm SHA2_256 của tên.
- **`HASHBYTES('SHA2_256', FirstName)`:** Tạo hash value của tên dùng SHA2_256.

#### **8. HÀM JSON (JSON FUNCTIONS)**

```sql
SELECT
    OrderID,
    OrderDetails
    JSON_VALUE(OrderDetails, '$.items[0].product') AS FirstProduct,
    JSON_QUERY(OrderDetails, '$.items') AS Items
FROM Orders
WHERE OrderID = 100;
```

- **Giải thích:** Lấy ID đơn hàng, details dạng JSON, lấy tên sản phẩm đầu tiên và mảng `items`.
- **`JSON_VALUE(OrderDetails, '$.items[0].product')`:** Lấy giá trị tại path `$.items[0].product`.
- **`JSON_QUERY(OrderDetails, '$.items')`:** Lấy mảng items dạng JSON.
-       **`FOR JSON AUTO`:** Tạo ra một chuỗi JSON từ kết quả truy vấn

```sql
    SELECT
      OrderID,
      OrderDate,
      CustomerID
        FROM Orders
     FOR JSON AUTO;
```

### **VIII. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Hiểu rõ hàm:** Đọc kỹ tài liệu và hiểu rõ cách dùng của từng hàm.
- **Kết hợp:** Kết hợp các hàm để tạo ra các truy vấn phức tạp hơn.
- **Tối ưu:** Dùng hàm đúng cách để tối ưu hiệu suất query.

### **IX. KẾT LUẬN (TỔNG KẾT)**

Các hàm nâng cao trong SQL Server là một công cụ mạnh mẽ giúp bạn phân tích và xử lý dữ liệu một cách hiệu quả. Hãy sử
dụng chúng một cách linh hoạt và sáng tạo để khai thác tối đa tiềm năng của dữ liệu. Chúc các bạn code thành công! 😎
