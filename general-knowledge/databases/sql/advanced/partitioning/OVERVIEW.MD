## **🚀 "GIẢI MÃ" PHÂN VÙNG (PARTITIONING): CHIA NHỎ DỮ LIỆU LỚN TRONG SQL SERVER CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một kỹ thuật cực kỳ quan trọng khi làm việc với
database lớn: Partitioning (Phân vùng). Đây là một "chiêu thức" giúp bạn "cưa nhỏ" dữ liệu khổng lồ, để dễ quản lý và
truy vấn hơn. Cùng mình "mổ xẻ" nó nhé!

### **I. PHÂN VÙNG (PARTITIONING) LÀ GÌ? (CHIA NHỎ "KHO" DỮ LIỆU)**

- **Partitioning (Phân vùng):** Là kỹ thuật chia một bảng lớn thành các phần nhỏ hơn (partition) để:
    - Quản lý dữ liệu dễ hơn.
    - Tăng tốc độ truy vấn.
    - Giảm tải cho database.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn chia đồ trong tủ: bạn chia theo loại (quần áo, sách, đồ chơi, ...) để dễ tìm, dễ quản lý.
- **Quan trọng vì:**
    - **Hiệu suất:** Truy vấn nhanh hơn (vì chỉ cần tìm trong 1 partition).
    - **Quản lý:** Quản lý dữ liệu lớn dễ dàng hơn.
    - **Linh hoạt:** Có thể phân vùng theo nhiều cách khác nhau.

### **II. CÁC LOẠI PHÂN VÙNG (CÁCH CHIA "KHO")**

1. **Phân vùng ngang (Horizontal Partitioning):**
    - Chia bảng theo hàng (dòng dữ liệu).
    - Thường dùng khi có cột thời gian, vùng, ...
    - **Ví dụ:** Chia bảng `Orders` theo năm.
2. **Phân vùng dọc (Vertical Partitioning):**
    - Chia bảng theo cột (chia thành nhiều bảng con, mỗi bảng con có một số cột).
    - Thường dùng khi có một số cột ít dùng.
    - **Ví dụ:** Tách các cột ít dùng (hình ảnh, note, ...) sang bảng khác.

### **III. CÁCH PHÂN VÙNG BẢNG (CÁCH CHIA "TỦ")**

#### **3.1. RANGE PARTITIONING (PHÂN VÙNG THEO KHOẢNG)**

- Chia theo khoảng giá trị của một cột.
- **Ví dụ:** Chia theo năm, theo tháng, theo vùng,...
- **Code:**

```sql
CREATE PARTITION FUNCTION partition_by_year (datetime)
AS RANGE RIGHT FOR VALUES ('2020-01-01', '2021-01-01', '2022-01-01');

CREATE PARTITION SCHEME partition_scheme_by_year
AS PARTITION partition_by_year
TO ([PRIMARY], [SECONDARY], [TERTIARY], [QUATERNARY]);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderDate DATETIME,
    CustomerID INT
)
ON partition_scheme_by_year (OrderDate);
```

**Giải thích:**

- Tạo function `partition_by_year` để định nghĩa các khoảng.
- Tạo scheme `partition_scheme_by_year` để xác định partition sẽ lưu ở filegroup nào.
- Tạo bảng `Orders` với partition function và scheme.

#### **3.2. LIST PARTITIONING (PHÂN VÙNG THEO DANH SÁCH)**

- Chia theo danh sách các giá trị.
- **Ví dụ:** Chia theo vùng (region), theo loại sản phẩm,...

```sql
CREATE PARTITION FUNCTION partition_by_region (VARCHAR(20))
AS LIST ( 'North', 'South', 'East', 'West');

CREATE PARTITION SCHEME partition_scheme_by_region
AS PARTITION partition_by_region
TO ([PRIMARY], [SECONDARY], [TERTIARY], [QUATERNARY]);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Region VARCHAR(20),
    CustomerName VARCHAR(100)
)
ON partition_scheme_by_region (Region);
```

**Giải thích:**

- Tạo function `partition_by_region` để định nghĩa các vùng.
- Tạo scheme `partition_scheme_by_region` để xác định partition sẽ lưu ở filegroup nào.
- Tạo bảng `Customers` với partition function và scheme.

#### **3.3. HASH PARTITIONING (PHÂN VÙNG THEO HASH)**

- Chia dựa trên giá trị băm của một cột (phân phối đều dữ liệu).
- **Ví dụ:** Chia dựa trên ID của người dùng (CustomerID).

```sql
CREATE PARTITION FUNCTION partition_by_customer_id(INT)
AS RANGE RIGHT FOR VALUES (100, 200, 300)

CREATE PARTITION SCHEME partition_scheme_by_customer_id
AS PARTITION partition_by_customer_id
TO ([PRIMARY], [SECONDARY], [TERTIARY], [QUATERNARY]);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    CustomerID INT
)
ON partition_scheme_by_customer_id(CustomerID);
```

**Giải thích:**

- Tạo function `partition_by_customer_id` để định nghĩa cách phân chia dựa theo ID khách hàng.
- Tạo scheme `partition_scheme_by_customer_id` để xác định partition sẽ lưu ở filegroup nào.
- Tạo bảng `Products` với partition function và scheme.

### **IV. LỢI ÍCH CỦA PHÂN VÙNG (TẠI SAO NÊN CHIA "TỦ")**

- **Hiệu suất:** Giúp query nhanh hơn (chỉ cần tìm trong một partition).
- **Quản lý:** Dễ quản lý dữ liệu lớn (backup, restore, ... dễ hơn).
- **Tính khả dụng:** Tăng tính sẵn sàng (không bị sập hết nếu một partition bị lỗi).

### **V. NHƯỢC ĐIỂM CỦA PHÂN VÙNG (CẨN THẬN KHI CHIA "TỦ")**

- **Phức tạp:** Cần phải có kiến thức về database, chọn cột phân vùng hợp lý.
- **Cấu hình phức tạp:** Cấu hình partition scheme, partition function.
- **Tốn bộ nhớ:** Có thể tốn bộ nhớ để lưu trữ metadata về partition.

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Chọn cột phân vùng:** Chọn cột phân vùng cẩn thận để dữ liệu phân bố đều, tránh bị lệch.
- **Test kỹ:** Kiểm tra kỹ trước khi áp dụng vào production (để tránh bị mất dữ liệu).
- **Quản lý:** Nên có kế hoạch quản lý partition thường xuyên.

### **VII. KẾT LUẬN (TỔNG KẾT)**

Partitioning là một kỹ thuật rất mạnh mẽ, giúp bạn quản lý và truy vấn dữ liệu lớn một cách hiệu quả hơn. Hy vọng qua
bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào dự án của mình. Chúc các bạn code thành công! 😎
