## **🚀 "GIẢI MÃ" PIVOT VÀ UNPIVOT TRONG SQL SERVER: XOAY CHUYỂN DỮ LIỆU CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai câu lệnh đặc biệt trong SQL Server: `PIVOT` và `UNPIVOT`. Đây là những "chiêu thức" lợi hại giúp bạn biến đổi cấu trúc dữ liệu, làm cho dữ liệu dễ đọc, dễ phân tích hơn. Cùng mình "mổ xẻ" chúng nhé!

### **I. PIVOT VÀ UNPIVOT LÀ GÌ? (XOAY DỮ LIỆU KIỂU GÌ?)**

-   **`PIVOT`:** Là câu lệnh dùng để _xoay_ dữ liệu từ dạng hàng (rows) sang dạng cột (columns).
    -   Giống như khi bạn biến một bảng dọc thành một bảng ngang để dễ nhìn hơn.
-   **`UNPIVOT`:** Là câu lệnh ngược lại, dùng để _xoay_ dữ liệu từ dạng cột sang dạng hàng.
    -   Giống như khi bạn biến bảng ngang thành bảng dọc.
-   **Quan trọng vì:**
    -   **Biến đổi dữ liệu:** Thay đổi cấu trúc dữ liệu (hàng thành cột, cột thành hàng).
    -   **Báo cáo:** Dùng để tạo báo cáo dễ đọc hơn.
    -   **Phân tích:** Giúp phân tích dữ liệu dễ dàng hơn.

### **II. CÚ PHÁP CƠ BẢN (CÁCH DÙNG PIVOT VÀ UNPIVOT)**

#### **2.1. `PIVOT` (XOAY DỮ LIỆU TỪ HÀNG THÀNH CỘT)**

```sql
SELECT column1, [value1], [value2], ...
FROM (
    SELECT column1, column2, value_column
    FROM table_name
) AS source_table
PIVOT (
    aggregate_function(value_column)
    FOR column2 IN ([value1], [value2], ...)
) AS pivot_table;
```

-   **`SELECT column1, [value1], [value2], ...`:** Chọn các cột và các giá trị cần xoay thành cột.
-   **`FROM ( SELECT ... FROM table_name) AS source_table`:** Tạo một bảng tạm (subquery) chứa dữ liệu cần xoay.
-   **`PIVOT (aggregate_function(value_column) FOR column2 IN ([value1], [value2], ...))`:** Thực hiện phép xoay.
    -   `aggregate_function()`: Hàm tổng hợp (COUNT, SUM, AVG, ...).
    -   `value_column`: Cột chứa giá trị cần tính tổng.
    -   `column2`: Cột chứa các giá trị cần chuyển thành tên cột.
    -   `[value1], [value2], ...`: Các giá trị cột 2 sẽ chuyển thành cột.

#### **2.2. `UNPIVOT` (XOAY DỮ LIỆU TỪ CỘT THÀNH HÀNG)**

```sql
SELECT column1, column2, value_column
FROM (
    SELECT column1, [value1], [value2], ...
    FROM table_name
) AS unpivot_table
UNPIVOT (
    value_column FOR column2 IN ([value1], [value2], ...)
) AS unpivot_result;
```

-   **`SELECT column1, column2, value_column`:** Chọn các cột cần lấy sau khi xoay.
-   **`FROM ( SELECT ... FROM table_name) AS unpivot_table`:** Tạo bảng tạm (subquery) chứa dữ liệu cần xoay.
-   **`UNPIVOT (value_column FOR column2 IN ([value1], [value2], ...))`:** Thực hiện phép xoay.
    -   `value_column`: Cột mới chứa các giá trị từ các cột cũ.
    -   `column2`: Cột mới chứa tên của các cột cũ.
    -   `[value1], [value2], ...`: Các cột cần chuyển thành hàng.

### **IV. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

Giả sử ta có bảng:

-   **`Sales`:** (Year, Quarter, Product, Revenue)

#### **1. `PIVOT` (LẤY DOANH THU THEO NĂM):**

```sql
SELECT Product, [Q1], [Q2], [Q3], [Q4]
FROM (
    SELECT Year, Quarter, Product, Revenue
    FROM Sales
) AS SourceTable
PIVOT (
    SUM(Revenue)
    FOR Quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS PivotTable
ORDER BY Product;
```

-   **Giải thích:**
    -   Lấy doanh thu theo từng sản phẩm và quý (từ dạng hàng sang cột).
    -   `SUM(Revenue)`: Tính tổng doanh thu.
    -   `FOR Quarter IN ([Q1], [Q2], [Q3], [Q4])`: Chuyển các giá trị `Q1`, `Q2`, `Q3`, `Q4` thành cột.
-   **Output:**

| Product | Q1   | Q2   | Q3   | Q4   |
| ------- | ---- | ---- | ---- | ---- |
| Laptop  | 1000 | 1200 | 1500 | 1300 |
| Phone   | 800  | 900  | 1100 | 1000 |
| Tablet  | 500  | 600  | 700  | 800  |

#### **2. `UNPIVOT` (BIẾN DỮ LIỆU THEO NĂM THÀNH DẠNG HÀNG):**

```sql
SELECT Product, Quarter, Revenue
FROM (
  SELECT Product, Q1, Q2, Q3, Q4
  FROM (
    SELECT Product, SUM(Revenue) AS Q1, SUM(Revenue) AS Q2, SUM(Revenue) AS Q3, SUM(Revenue) AS Q4
     FROM Sales
    GROUP BY Product
   ) AS P
  ) AS SourceTable
UNPIVOT (
    Revenue FOR Quarter IN ([Q1], [Q2], [Q3], [Q4])
) AS UnpivotTable
ORDER BY Product;
```

-   **Giải thích:**
    -   Chuyển dữ liệu doanh thu theo quý (từ cột thành hàng).
    -   `Revenue FOR Quarter IN ([Q1], [Q2], [Q3], [Q4])`: Chuyển các cột `Q1`, `Q2`, `Q3`, `Q4` thành hàng.
-   **Output:**

| Product | Quarter | Revenue |
| ------- | ------- | ------- |
| Laptop  | Q1      | 1000    |
| Laptop  | Q2      | 1200    |
| Laptop  | Q3      | 1500    |
| Laptop  | Q4      | 1300    |
| Phone   | Q1      | 800     |
| Phone   | Q2      | 900     |
| Phone   | Q3      | 1100    |
| Phone   | Q4      | 1000    |
| Tablet  | Q1      | 500     |
| Tablet  | Q2      | 600     |
| Tablet  | Q3      | 700     |
| Tablet  | Q4      | 800     |

### **V. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

-   **Dùng khi cần thiết:** Chỉ nên dùng `PIVOT` và `UNPIVOT` khi cần thay đổi cấu trúc dữ liệu, không nên dùng quá nhiều.
-   **Kiểm tra dữ liệu:** Cần hiểu rõ cấu trúc dữ liệu trước và sau khi xoay.
-   **Chú ý hàm tổng hợp:** Dùng đúng hàm tổng hợp với dữ liệu cần xoay (SUM, AVG, ...).
-   **Số lượng cột/hàng:** Biết rõ số lượng cột và hàng trước khi thực hiện.
-   **Hiệu suất:** Nếu bảng lớn, có thể ảnh hưởng đến hiệu suất.

### **VI. KẾT LUẬN (TỔNG KẾT)**

`PIVOT` và `UNPIVOT` là hai công cụ rất hữu ích để biến đổi dữ liệu trong SQL Server. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về chúng và có thể áp dụng vào các báo cáo, phân tích của mình. Chúc các bạn code thành công! 😎
