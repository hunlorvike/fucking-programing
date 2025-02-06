# Chương 3: Sắp Xếp và Lọc Dữ Liệu Nâng Cao - ORDER BY, LIMIT, OFFSET, AND, OR, NOT - " 'Tinh Chỉnh' " "Truy Vấn" Để " 'Lấy Đúng' " "Dữ Liệu Cần" - " 'Lọc Sâu' " và " 'Sắp Xếp' " Kết Quả Truy Vấn

Chào mừng bạn đến với **Chương 3: Sắp Xếp và Lọc Dữ Liệu Nâng Cao - ORDER BY, LIMIT, OFFSET, AND, OR, NOT**! Trong chương này, chúng ta sẽ "nâng cấp" "kỹ năng" truy vấn SQL của bạn lên một "bước mới" bằng cách "học cách" **"sắp xếp"** kết quả truy vấn, **"phân trang"** kết quả, và **"lọc"** dữ liệu theo các **"điều kiện"** "phức tạp" hơn. Chúng ta sẽ "làm chủ" các mệnh đề **`ORDER BY`**, **`LIMIT`**, **`OFFSET`**, và các toán tử **`AND`**, **`OR`**, **`NOT`** - "những 'vũ khí' " "mạnh mẽ" để " 'tinh chỉnh' " "truy vấn" và " 'lấy đúng' " "dữ liệu" mà bạn "cần".

**Phần 3: Sắp Xếp và Lọc Dữ Liệu Nâng Cao - ORDER BY, LIMIT, OFFSET, AND, OR, NOT - " 'Tinh Chỉnh' " "Truy Vấn" Để " 'Lấy Đúng' " "Dữ Liệu Cần"**

**3.1. Mệnh Đề `ORDER BY` - " 'Sắp Xếp' " Kết Quả Truy Vấn - " 'Ngăn Nắp' " Hóa Dữ Liệu "Đầu Ra"**

-   **Mệnh Đề `ORDER BY` - " 'Sắp Xếp' " Dữ Liệu Theo " 'Trật Tự' " Mong Muốn:**

    -   **Mệnh Đề `ORDER BY`** là mệnh đề "tùy chọn" (optional) trong câu truy vấn SQL, "dùng" để **"sắp xếp"** (sort) các **"bản ghi"** (rows) trong **"kết quả truy vấn"** theo **"một hoặc nhiều cột"** (columns) theo **"thứ tự"** "tăng dần" (ascending) hoặc "giảm dần" (descending).
    -   `ORDER BY` giúp bạn **"ngăn nắp" hóa** dữ liệu "đầu ra" (output) của truy vấn, "dễ dàng" "xem", "phân tích", và "hiểu" dữ liệu hơn.

-   **"Cú Pháp" Mệnh Đề `ORDER BY` "Cơ Bản":**

    ```sql
    SELECT column1, column2, ...
    FROM table_name
    ORDER BY column_to_sort [ASC|DESC]; -- Mệnh đề ORDER BY - "sắp xếp" kết quả truy vấn
    ```

    -   **`ORDER BY column_to_sort`:** "Chỉ định" **"tên cột"** (column name) mà bạn muốn "sắp xếp" kết quả truy vấn theo.
    -   **`[ASC|DESC]`:** "Chỉ định" **"thứ tự" "sắp xếp"**:
        -   **`ASC` (Ascending):** "Sắp xếp" theo **"thứ tự" "tăng dần"** (từ nhỏ đến lớn, từ A đến Z, từ cũ đến mới). **"Mặc định"** nếu bạn "không chỉ định" `ASC` hoặc `DESC`.
        -   **`DESC` (Descending):** "Sắp xếp" theo **"thứ tự" "giảm dần"** (từ lớn đến nhỏ, từ Z đến A, từ mới đến cũ).

-   **"Ví Dụ" Mệnh Đề `ORDER BY` - " 'Hỏi' " Database: " 'Cho Xem' " "Sản Phẩm" Từ Bảng `SanPhams`, " 'Sắp Xếp' " Theo " 'Giá' " "Giảm Dần":**

    ```sql
    SELECT TenSanPham, Gia  -- "Chọn" cột TenSanPham và cột Gia
    FROM SanPhams         -- Từ bảng SanPhams
    ORDER BY Gia DESC;    -- "Sắp xếp" kết quả theo cột Gia "giảm dần" (DESC - Descending)
    ```

    -   **"Kết quả"** truy vấn (ví dụ):

        | TenSanPham         | Gia     |
        | ------------------ | ------- |
        | Màn hình LCD        | 3500000 |
        | Bàn phím cơ         | 1500000 |
        | Tai nghe Bluetooth   | 750000  |
        | Chuột không dây      | 250000  |
        | Sách "Lập trình C#" | 150000  |
        | Sách "OOP"          | 120000  |
        | ...                | ...     |

-   **"Sắp Xếp" Theo "Nhiều Cột" (Multi-Column Sorting):** Bạn có thể "sắp xếp" kết quả truy vấn theo **"nhiều cột"** bằng cách "liệt kê" **"tên các cột"** trong mệnh đề `ORDER BY`, **"cách nhau" bằng dấu phẩy (`,`)**. "Thứ tự" các cột "liệt kê" sẽ là **"thứ tự ưu tiên"** "sắp xếp".

    -   **"Ví dụ" - " 'Sắp Xếp' " "Sản Phẩm" Theo " 'Danh Mục' " "Tăng Dần", Sau Đó Theo " 'Giá' " "Giảm Dần":**

        ```sql
        SELECT TenSanPham, DanhMucSanPham, Gia  -- "Chọn" cột TenSanPham, DanhMucSanPham, và cột Gia
        FROM SanPhams                         -- Từ bảng SanPhams
        ORDER BY DanhMucSanPham ASC, Gia DESC; -- "Sắp xếp" theo cột DanhMucSanPham "tăng dần" (ASC), sau đó theo cột Gia "giảm dần" (DESC)
        ```

        -   Kết quả sẽ được "sắp xếp" theo cột `DanhMucSanPham` **"tăng dần"** trước. Trong mỗi "nhóm" "danh mục sản phẩm" (có cùng giá trị `DanhMucSanPham`), các sản phẩm sẽ được "sắp xếp" theo cột `Gia` **"giảm dần"**.

**3.2. Mệnh Đề `LIMIT` và `OFFSET` - " 'Phân Trang' " Kết Quả Truy Vấn - " 'Chia Nhỏ' " "Danh Sách Dài Dằng Dặc" Thành " 'Từng Trang' " "Dễ Xem"**

-   **Mệnh Đề `LIMIT` và `OFFSET` - " 'Phân Trang' " Dữ Liệu "Đầu Ra":**

    -   **Mệnh Đề `LIMIT`** và **`OFFSET`** là các mệnh đề "tùy chọn" (optional) trong câu truy vấn SQL, "dùng" để **"phân trang"** (paginate) **"kết quả truy vấn"**. "Chia nhỏ" "danh sách" kết quả "dài dằng dặc" thành **"từng trang"** (page) "nhỏ hơn", "dễ xem" và "quản lý" hơn (ví dụ: trong ứng dụng web "hiển thị" "danh sách" dữ liệu "phân trang").

    -   **Mệnh Đề `LIMIT`:** "Giới hạn" **"số lượng"** "bản ghi" (rows) "tối đa" được "trả về" trong kết quả truy vấn. "Lấy" **"tối đa" "N" bản ghi** "đầu tiên" từ kết quả truy vấn.

    -   **Mệnh Đề `OFFSET`:** "Bỏ qua" **"M" bản ghi** "đầu tiên" trong kết quả truy vấn và "bắt đầu" "lấy" dữ liệu từ bản ghi thứ **"M+1"**. "Dùng" để "bỏ qua" các bản ghi ở "các trang 'trước' " khi "phân trang".

-   **"Cú Pháp" Mệnh Đề `LIMIT` và `OFFSET` "Cơ Bản":**

    ```sql
    SELECT column1, column2, ...
    FROM table_name
    [WHERE condition] -- (tùy chọn)
    [ORDER BY column_to_sort [ASC|DESC]] -- (tùy chọn)
    LIMIT number_of_rows -- Mệnh đề LIMIT - "giới hạn" "số lượng" bản ghi
    [OFFSET number_of_rows_to_skip]; -- Mệnh đề OFFSET - "bỏ qua" "số lượng" bản ghi (tùy chọn)
    ```

    -   **`LIMIT number_of_rows`:** "Chỉ định" **"số lượng"** "bản ghi" (rows) "tối đa" muốn "lấy" (ví dụ: `LIMIT 10` - "lấy" tối đa 10 bản ghi).
    -   **`OFFSET number_of_rows_to_skip`:** "Chỉ định" **"số lượng"** "bản ghi" (rows) muốn "bỏ qua" (ví dụ: `OFFSET 20` - "bỏ qua" 20 bản ghi "đầu tiên"). Mệnh đề `OFFSET` thường được "dùng" "kèm" với mệnh đề `LIMIT` để "phân trang".

-   **"Ví Dụ" Mệnh Đề `LIMIT` và `OFFSET` - " 'Hỏi' " Database: " 'Cho Xem' " "Trang 2" Của "Danh Sách Sản Phẩm" Từ Bảng `SanPhams` (mỗi trang 10 sản phẩm), " 'Sắp Xếp' " Theo " 'Tên Sản Phẩm' " "Tăng Dần":**

    -   Giả sử bạn muốn "phân trang" "danh sách sản phẩm" từ bảng `SanPhams`, mỗi trang "hiển thị" **10 sản phẩm**, và bạn muốn "xem" **"trang thứ 2"**.
    -   Để "lấy" "trang thứ 2" (page 2), bạn cần "bỏ qua" (skip) **10 sản phẩm** (page 1) "đầu tiên" và "lấy" **10 sản phẩm** "tiếp theo" (page 2).
    -   Câu truy vấn SQL:

        ```sql
        SELECT TenSanPham, Gia  -- "Chọn" cột TenSanPham và cột Gia
        FROM SanPhams         -- Từ bảng SanPhams
        ORDER BY TenSanPham ASC -- "Sắp xếp" theo cột TenSanPham "tăng dần" (ASC)
        LIMIT 10              -- "Giới hạn" "số lượng" bản ghi "mỗi trang" là 10 (LIMIT 10)
        OFFSET 10;             -- "Bỏ qua" 10 bản ghi "đầu tiên" (OFFSET 10) - "lấy" "trang thứ 2"

        -- "Giải thích":
        -- "Trang 1": LIMIT 10 OFFSET 0 (bỏ qua 0 bản ghi, lấy 10 bản ghi đầu tiên)
        -- "Trang 2": LIMIT 10 OFFSET 10 (bỏ qua 10 bản ghi, lấy 10 bản ghi tiếp theo - từ bản ghi thứ 11 đến bản ghi thứ 20)
        -- "Trang 3": LIMIT 10 OFFSET 20 (bỏ qua 20 bản ghi, lấy 10 bản ghi tiếp theo - từ bản ghi thứ 21 đến bản ghi thứ 30)
        -- ... và cứ tiếp tục như vậy
        ```

    -   **"Kết quả"** truy vấn (ví dụ) - "trang thứ 2" của "danh sách sản phẩm" (10 sản phẩm từ bản ghi thứ 11 đến bản ghi thứ 20 sau khi "sắp xếp" theo "tên sản phẩm"):

        | TenSanPham             | Gia     |
        | ---------------------- | ------- |
        | Laptop Dell XPS 13      | 45000000|
        | Màn hình ASUS ProArt    | 12000000|
        | Màn hình LCD           | 3500000 |
        | Máy in laser Canon     | 3000000 |
        | Ổ cứng SSD Samsung 980 | 2800000 |
        | Tai nghe Bluetooth      | 750000  |
        | Tai nghe chụp tai Sony  | 1200000 |
        | ...                    | ...     |

-   **"Lưu Ý" Về Mệnh Đề `LIMIT` và `OFFSET` - "Phương Ngữ SQL" (SQL Dialects):**

    -   "Cú pháp" mệnh đề `LIMIT` và `OFFSET` có thể **"khác nhau"** giữa các **SQL Dialects** (phương ngữ SQL) của các RDBMSs "khác nhau":
        -   **MySQL, PostgreSQL, SQLite:** "Dùng" `LIMIT number_of_rows OFFSET number_of_rows_to_skip` (như ví dụ trên).
        -   **SQL Server:** "Dùng" mệnh đề `TOP number_of_rows` để "giới hạn" "số lượng" bản ghi và mệnh đề `OFFSET number_of_rows_to_skip ROWS FETCH NEXT number_of_rows ROWS ONLY` để "phân trang".
        -   **Oracle:** "Dùng" mệnh đề `ROWNUM <= number_of_rows` để "giới hạn" và mệnh đề `OFFSET number_of_rows_to_skip ROWS FETCH NEXT number_of_rows ROWS ONLY` (từ Oracle 12c trở lên) hoặc các "phương pháp" "phân trang" "phức tạp" hơn (ví dụ: dùng subqueries, row_number() function) cho các phiên bản Oracle "cũ hơn".
        -   **"Kiểm tra" "tài liệu SQL"** của RDBMS mà bạn đang "dùng" để "biết" "cú pháp" `LIMIT` và `OFFSET` "chính xác" cho DBMS đó.

**3.3. Toán Tử `AND`, `OR`, `NOT` - " 'Kết Hợp' " "Điều Kiện Lọc" "Phức Tạp" - " 'Lọc Nhiều Tầng' " Để " 'Lấy Đúng' " "Dữ Liệu 'Khó Tính' "**

-   **Toán Tử `AND`, `OR`, `NOT` - " 'Vũ Khí' " "Lọc Dữ Liệu" " 'Siêu Đẳng' ":**

    -   **Toán Tử `AND`**, **`OR`**, và **`NOT`** là các **"toán tử 'logic' "** (logical operators) trong SQL, "dùng" để **"kết hợp"** **"nhiều 'điều kiện' " "lọc"** (conditions) trong mệnh đề `WHERE` thành các **"điều kiện" "phức tạp" hơn**.
    -   Toán Tử `AND`, `OR`, `NOT` "cho phép" bạn "xây dựng" các câu truy vấn SQL "lọc" dữ liệu **"đa dạng"** và **"mạnh mẽ"** hơn, "lấy" **"đúng"** "dữ liệu" "khó tính" mà bạn "thực sự" "cần".

-   **"Các Toán Tử" `AND`, `OR`, `NOT` và " 'Bảng Chân Lý' " (Truth Table):**

    -   **`AND` (Và):** "Kết hợp" hai "điều kiện" bằng toán tử `AND`. "Điều kiện" "kết hợp" chỉ "trả về" **`TRUE`** nếu **"cả hai" "điều kiện" "thành phần"** đều "trả về" **`TRUE`**. Nếu "một trong hai" "điều kiện" hoặc "cả hai" "điều kiện" đều "trả về" `FALSE`, "điều kiện" "kết hợp" sẽ "trả về" `FALSE`.

        | Điều kiện 1 | Toán tử | Điều kiện 2 | Kết quả (Điều kiện 1 AND Điều kiện 2) |
        | ---------- | -------- | ---------- | -------------------------------------- |
        | TRUE       | AND      | TRUE       | TRUE                                   |
        | TRUE       | AND      | FALSE      | FALSE                                  |
        | FALSE      | AND      | TRUE       | FALSE                                  |
        | FALSE      | AND      | FALSE      | FALSE                                  |

    -   **`OR` (Hoặc):** "Kết hợp" hai "điều kiện" bằng toán tử `OR`. "Điều kiện" "kết hợp" "trả về" **`TRUE`** nếu **"một trong hai" "điều kiện"** hoặc **"cả hai" "điều kiện"** đều "trả về" **`TRUE`**. "Điều kiện" "kết hợp" chỉ "trả về" `FALSE` nếu **"cả hai" "điều kiện" "thành phần"** đều "trả về" `FALSE`.

        | Điều kiện 1 | Toán tử | Điều kiện 2 | Kết quả (Điều kiện 1 OR Điều kiện 2) |
        | ---------- | -------- | ---------- | ------------------------------------- |
        | TRUE       | OR       | TRUE       | TRUE                                  |
        | TRUE       | OR       | FALSE      | TRUE                                  |
        | FALSE      | OR       | TRUE       | TRUE                                  |
        | FALSE      | OR       | FALSE      | FALSE                                 |

    -   **`NOT` (Phủ Định):** "Phủ định" (negate) một "điều kiện" bằng toán tử `NOT`. "Điều kiện" `NOT` "trả về" **`TRUE`** nếu "điều kiện" "thành phần" "trả về" **`FALSE`**, và "trả về" `FALSE` nếu "điều kiện" "thành phần" "trả về" `TRUE`.

        | Điều kiện | Toán tử | Kết quả (NOT Điều kiện) |
        | -------- | -------- | ----------------------- |
        | TRUE     | NOT      | FALSE                     |
        | FALSE    | NOT      | TRUE                      |

-   **"Cú Pháp" "Kết Hợp" "Điều Kiện Lọc" Với `AND`, `OR`, `NOT`:**

    ```sql
    SELECT ...
    FROM table_name
    WHERE condition1 [AND|OR] condition2 [AND|OR] ... [AND|OR] conditionN  -- "Kết hợp" nhiều "điều kiện" bằng AND, OR
      [AND NOT condition] -- "Phủ định" "điều kiện" bằng NOT
      [OR NOT condition]; -- "Phủ định" "điều kiện" bằng NOT
    ```

    -   Bạn có thể "kết hợp" **"nhiều"** "điều kiện" "lọc" bằng cách "dùng" toán tử `AND` và `OR` "lặp đi lặp lại".
    -   Bạn có thể "phủ định" "điều kiện" bằng cách "dùng" toán tử `NOT` "trước" "điều kiện" đó.
    -   "Dùng" **dấu ngoặc đơn `()`** để "nhóm" các "điều kiện" và "điều khiển" **"thứ tự" "thực hiện"** các toán tử `AND`, `OR`, `NOT` (ưu tiên toán tử). Toán tử `NOT` được "thực hiện" "trước" `AND`, và toán tử `AND` được "thực hiện" "trước" `OR` (theo "thứ tự ưu tiên toán tử" "mặc định"). Nhưng "dùng" dấu ngoặc đơn `()` để "làm rõ" "thứ tự" "thực hiện" và "tăng" "tính 'dễ đọc' " của câu truy vấn.

-   **"Ví Dụ" Toán Tử `AND`, `OR`, `NOT` - " 'Hỏi' " Database: " 'Cho Xem' " "Sản Phẩm Nào" Có " 'Danh Mục' " Là " 'Điện Tử' " "VÀ" " 'Giá' " "Lớn Hơn 1 Triệu" "HOẶC" " 'Sản Phẩm Nào' " "Không Thuộc" " 'Danh Mục' " "Sách"**:

    ```sql
    SELECT TenSanPham, DanhMucSanPham, Gia  -- "Chọn" cột TenSanPham, DanhMucSanPham, và cột Gia
    FROM SanPhams                         -- Từ bảng SanPhams
    WHERE (DanhMucSanPham = 'Điện tử' AND Gia > 1000000) -- "Điều kiện 1": "Danh mục" là "Điện tử" "VÀ" "Giá" > 1 triệu (AND)
       OR NOT DanhMucSanPham = 'Sách';                  -- "HOẶC" "Điều kiện 2": "Không thuộc" "danh mục" "Sách" (OR NOT)
    ```

    -   Câu truy vấn này sẽ "lấy" các sản phẩm "thỏa mãn" **"một trong hai" "điều kiện"**:
        1.  Sản phẩm thuộc "danh mục" "Điện tử" **"VÀ"** có "giá" "lớn hơn 1 triệu".
        2.  **"HOẶC"** (OR) sản phẩm **"không thuộc"** "danh mục" "Sách".

    -   **"Kết quả"** truy vấn sẽ là "tập hợp" các sản phẩm "thỏa mãn" "một trong hai" "điều kiện" trên.

**3.4. "Thực Hành" Lọc và Sắp Xếp Dữ Liệu Nâng Cao - " 'Truy Vấn' " "Chính Xác" và " 'Hiệu Quả' " Hơn - " 'Làm Chủ' " "Bộ Lọc" và " 'Sắp Xếp' " Của SQL**

-   **"Bài Tập" "Thực Hành" - " 'Luyện Công Phu' " Truy Vấn SQL "Nâng Cao":**

    1.  **"Sắp xếp" "danh sách sản phẩm" theo "tên sản phẩm" "ngược thứ tự bảng chữ cái" (Z-A).** (Dùng `ORDER BY` với `DESC`).
    2.  **"Lấy" "3 sản phẩm" có "giá" "cao nhất".** (Dùng `ORDER BY` với `DESC` và `LIMIT 3`).
    3.  **"Phân trang" "danh sách sản phẩm" (mỗi trang 5 sản phẩm) và "lấy" "trang thứ 3".** (Dùng `LIMIT 5 OFFSET 10`).
    4.  **"Lọc" "sản phẩm" có "giá" nằm trong "khoảng" từ 500 ngàn đến 2 triệu (bao gồm cả 500 ngàn và 2 triệu).** (Dùng `WHERE` với `BETWEEN ... AND ...`).
    5.  **"Lọc" "sản phẩm" có "tên sản phẩm" "chứa" từ khóa "màn hình".** (Dùng `WHERE` với `LIKE '%màn hình%'`).
    6.  **"Lọc" "sản phẩm" có "danh mục" là "Điện tử" "HOẶC" "Sách".** (Dùng `WHERE` với `OR` và `IN (...)`).
    7.  **"Lọc" "sản phẩm" có "giá" "lớn hơn 1 triệu" "VÀ" "không thuộc" "danh mục" "Đồ gia dụng".** (Dùng `WHERE` với `AND` và `NOT`).
    8.  **"Kết hợp" "sắp xếp" và "lọc" "phức tạp": "Lấy" "trang thứ 1" (5 sản phẩm mỗi trang) của "danh sách sản phẩm" có "giá" "lớn hơn 500 ngàn" và "thuộc" "danh mục" "Điện tử" "HOẶC" "Sách", "sắp xếp" theo "tên sản phẩm" "tăng dần".** ( "Bài toán tổng hợp" - "thử thách" "kỹ năng" truy vấn SQL của bạn).

-   **"Thực Hành" Với SQL Client Tool - " 'Gõ Lệnh' " và " 'Xem Kết Quả' " "Ngay Tức Thì":**

    -   "Mở" SQL client tool (ví dụ: Dbeaver, SSMS, pgAdmin, MySQL Workbench, SQLiteStudio).
    -   "Kết nối" đến database "mẫu" hoặc database "riêng" của bạn.
    -   "Mở" SQL editor và "viết" các câu truy vấn SQL "thực hành" cho từng "bài tập" trên.
    -   "Chạy" các câu truy vấn và "xem" "kết quả" truy vấn trong "bảng" "kết quả".
    -   " 'Mày mò' ", " 'thử nghiệm' ", và " 'chinh phục' " các "bài tập" để "làm chủ" các mệnh đề `ORDER BY`, `LIMIT`, `OFFSET`, và các toán tử `AND`, `OR`, `NOT`.

**Tổng Kết Chương 3:**

-   Bạn đã "nâng cấp" "kỹ năng" truy vấn SQL lên một "tầm cao mới" bằng cách "học cách" "sắp xếp" và "lọc" dữ liệu "nâng cao".
    -   "Nắm vững" mệnh đề **`ORDER BY`** ("sắp xếp" kết quả truy vấn).
    -   "Hiểu" mệnh đề **`LIMIT`** và **`OFFSET`** ("phân trang" kết quả truy vấn).
    -   "Làm chủ" các toán tử **`AND`**, **`OR`**, **`NOT`** ("kết hợp" "điều kiện" "lọc" "phức tạp").
    -   "Thực hành" "viết" và "chạy" các câu truy vấn SQL "lọc" và "sắp xếp" dữ liệu "nâng cao" để "luyện tập" và "củng cố" "kỹ năng".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: Hàm Tổng Hợp và GROUP BY - COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING**. Chúng ta sẽ "khám phá" các **"hàm tổng hợp"** (aggregate functions) để "tính toán" "giá trị" "tổng quan" trên dữ liệu và mệnh đề **`GROUP BY`** để "nhóm" dữ liệu và "thực hiện" "tính toán" "tổng hợp" trên dữ liệu "theo nhóm".

Bạn có câu hỏi nào về "lọc" và "sắp xếp" dữ liệu "nâng cao" này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" SQL.
