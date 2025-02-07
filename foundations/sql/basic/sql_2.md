# Chương 2: Truy Vấn SQL Cơ Bản - SELECT, FROM, WHERE - " 'Bắt Đầu' " "Hỏi Han" Database - " 'Lệnh' " "Nhập Môn" Để " 'Lấy Dữ Liệu' " Từ " 'Bảng Biểu' "

Chào mừng bạn đến với **Chương 2: Truy Vấn SQL Cơ Bản - SELECT, FROM, WHERE**! Trong chương này, chúng ta sẽ "bắt đầu" "
hành trình" "khám phá" SQL bằng cách "học cách" "viết" các câu truy vấn SQL **"cơ bản"** nhất để **"lấy"** dữ liệu từ
database. Chúng ta sẽ "làm quen" với **"bộ ba" "quyền lực"** của SQL queries: **`SELECT`**, **`FROM`**, và **`WHERE`
**, "ba 'lệnh' " "nhập môn" mà bạn cần "nắm vững" để "bắt đầu" "hỏi han" database và "khai thác" "kho tàng" dữ liệu.

**Phần 2: Truy Vấn SQL Cơ Bản - SELECT, FROM, WHERE - " 'Bắt Đầu' " "Hỏi Han" Database**

**2.1. Lệnh `SELECT` - " 'Chọn' " Dữ Liệu Muốn "Xem" - " 'Ra Lệnh' " Cho Database: " 'Cho Xem' " ...**

- **Lệnh `SELECT` - " 'Chiếu Sáng' " Vào " 'Cột' " Dữ Liệu:**

    - **Lệnh `SELECT`** là lệnh SQL **"cơ bản nhất"** và **"quan trọng nhất"** để **"truy vấn"** (query) dữ liệu từ
      database.
    - `SELECT` "ra lệnh" cho database là **"hãy 'chọn' "** và **" 'trả về' "** (select and retrieve) **"dữ liệu"** mà
      bạn muốn "xem" từ database.
    - `SELECT` "chỉ định" **"các cột"** (columns) dữ liệu mà bạn muốn "lấy" từ bảng (table).

- **"Cú Pháp" Lệnh `SELECT` "Cơ Bản":**

  ```sql
  SELECT column1, column2, ..., columnN
  FROM table_name;
  ```

    - **`SELECT column1, column2, ..., columnN`:** "Liệt kê" **"tên các cột"** (column names) mà bạn muốn "lấy" từ bảng,
      **"cách nhau" bằng dấu phẩy (`,`)**. "Thứ tự" các cột "liệt kê" sẽ là "thứ tự" các cột "hiển thị" trong kết quả
      truy vấn.
    - **`FROM table_name`:** "Chỉ định" **"tên bảng"** (table name) mà bạn muốn "lấy" dữ liệu từ.

- **"Ví Dụ" Lệnh `SELECT` "Cơ Bản" - " 'Hỏi' " Database: " 'Cho Xem' " "Tên Sản Phẩm" và " 'Giá' " Từ Bảng `SanPhams`:**

    - Giả sử bạn có một bảng database tên là **`SanPhams`** (Products) chứa thông tin về sản phẩm, và bảng này có các
      cột sau: `SanPhamId` (ProductID), `TenSanPham` (ProductName), `Gia` (Price), `DanhMucSanPham` (Category).
    - Bạn muốn "lấy" **"tên sản phẩm"** (`TenSanPham`) và **"giá"** (`Gia`) của **"tất cả"** sản phẩm trong bảng
      `SanPhams`.
    - Câu truy vấn SQL:

      ```sql
      SELECT TenSanPham, Gia  -- "Chọn" cột TenSanPham và cột Gia
      FROM SanPhams;         -- Từ bảng SanPhams
      ```

    - **"Kết quả"** truy vấn (ví dụ):

      | TenSanPham         | Gia     |
              | ------------------ | ------- |
      | Chuột không dây      | 250000  |
      | Bàn phím cơ         | 1500000 |
      | Màn hình LCD        | 3500000 |
      | Tai nghe Bluetooth   | 750000  |
      | ...                | ...     |

- **`SELECT *` - " 'Chọn' " "Tất Cả" Các Cột - " 'Cho Xem' " "Hết Mọi Thứ" Trong Bảng:**

    - **`SELECT *`** là một "cú pháp" "đặc biệt" của lệnh `SELECT`, "dùng" để **"chọn" "tất cả" các cột** (all columns)
      từ bảng.
    - `SELECT *` "ra lệnh" cho database là **"hãy 'chọn' " và " 'trả về' " "tất cả" các cột** của bảng.
    - "Tiện lợi" khi bạn muốn "xem nhanh" "toàn bộ" dữ liệu trong bảng hoặc khi bạn "thực sự" cần "tất cả" các cột dữ
      liệu. Nhưng **"không nên" "lạm dụng" `SELECT *`** trong ứng dụng "production" (vì có thể làm "chậm" "hiệu năng"
      truy vấn và "lãng phí" băng thông mạng khi "lấy" "quá nhiều cột" "không cần thiết" - chúng ta sẽ nói về "tối ưu
      hóa" truy vấn SQL ở các chương sau).

    - **"Ví dụ" `SELECT *` - " 'Hỏi' " Database: " 'Cho Xem' " "Tất Cả" "Sản Phẩm" Từ Bảng `SanPhams`:**

      ```sql
      SELECT *        -- "Chọn" tất cả các cột (*)
      FROM SanPhams;   -- Từ bảng SanPhams
      ```

    - **"Kết quả"** truy vấn (ví dụ):

      | SanPhamId | TenSanPham         | Gia     | DanhMucSanPham |
              | --------- | ------------------ | ------- | ------------- |
      | 1         | Chuột không dây      | 250000  | Điện tử        |
      | 2         | Bàn phím cơ         | 1500000 | Điện tử        |
      | 3         | Màn hình LCD        | 3500000 | Điện tử        |
      | 4         | Tai nghe Bluetooth   | 750000  | Điện tử        |
      | 5         | Sách "Lập trình C#" | 150000  | Sách           |
      | 6         | Sách "OOP"          | 120000  | Sách           |
      | ...       | ...                | ...     | ...           |

**2.2. Mệnh Đề `FROM` - " 'Chỉ Định' " "Bảng" Dữ Liệu - " 'Nói' " Với Database: " 'Dữ Liệu Ở' " "Bảng" Nào?**

- **Mệnh Đề `FROM` - " 'Gốc Rễ' " Của Truy Vấn - " 'Bắt Đầu' " Từ " 'Bảng' " Nào:**

    - **Mệnh Đề `FROM`** là mệnh đề **"bắt buộc"** trong hầu hết các câu truy vấn SQL (trừ một số trường hợp "đặc
      biệt" - ví dụ: truy vấn "tính toán" "đơn giản" "không cần" "bảng").
    - `FROM` "chỉ định" **"tên bảng"** (table name) mà bạn muốn **"lấy" dữ liệu** từ. `FROM` là " 'gốc rễ' " của truy
      vấn - " 'bắt đầu' " từ " 'bảng' " dữ liệu nào.
    - Bạn có thể "chỉ định" **"một"** hoặc **"nhiều" "bảng"** trong mệnh đề `FROM` (khi "kết hợp" dữ liệu từ nhiều bảng
      bằng **Joins** - chúng ta sẽ "học" ở Chương 5 về Joins).

- **"Cú Pháp" Mệnh Đề `FROM` "Cơ Bản":**

  ```sql
  SELECT ...
  FROM table_name;  -- Mệnh đề FROM - "chỉ định" "bảng" dữ liệu
  ```

    - **`table_name`:** "Tên bảng" (table name) mà bạn muốn "truy vấn". "Tên bảng" phải **"tồn tại"** trong database mà
      bạn đang "truy vấn".

- **"Ví Dụ" Mệnh Đề `FROM` - " 'Hỏi' " Database: " 'Dữ Liệu Từ' " "Bảng" `DanhMucs`:**

    - Giả sử bạn có một bảng database tên là **`DanhMucs`** (Categories) chứa thông tin về danh mục sản phẩm, và bảng
      này có các cột sau: `DanhMucId` (CategoryID), `TenDanhMuc` (CategoryName).
    - Bạn muốn "lấy" **"tất cả" các cột** từ bảng `DanhMucs`.
    - Câu truy vấn SQL:

      ```sql
      SELECT *        -- "Chọn" tất cả các cột (*)
      FROM DanhMucs;   -- Từ bảng DanhMucs
      ```

    - **"Kết quả"** truy vấn (ví dụ):

      | DanhMucId | TenDanhMuc    |
              | --------- | ------------- |
      | 1         | Điện tử       |
      | 2         | Đồ gia dụng   |
      | 3         | Nội thất      |
      | 4         | Thời trang    |
      | 5         | Sách         |
      | ...       | ...         |

**2.3. Mệnh Đề `WHERE` - " 'Lọc' " Dữ Liệu Theo " 'Điều Kiện' " - " 'Hỏi' " Database: " 'Chỉ Cho Xem' " "Sản Phẩm Nào" "
Thỏa Mãn' " "Điều Kiện" ...**

- **Mệnh Đề `WHERE` - " 'Bộ Lọc' " Dữ Liệu "Mạnh Mẽ":**

    - **Mệnh Đề `WHERE`** là mệnh đề "tùy chọn" (optional) trong câu truy vấn SQL, "dùng" để **"lọc"** (filter) dữ liệu
      từ bảng dựa trên **"một hoặc nhiều 'điều kiện' "** (conditions).
    - `WHERE` "ra lệnh" cho database là **" 'chỉ trả về' " những bản ghi (rows) trong bảng** mà **"thỏa mãn' " "điều
      kiện"** "lọc" đã "chỉ định". "Bỏ qua" các bản ghi "không thỏa mãn" "điều kiện".
    - `WHERE` giúp bạn **"thu hẹp"** "phạm vi" dữ liệu "truy vấn" và "lấy" **"đúng"** "dữ liệu" mà bạn **"thực sự" "cần"
      **.

- **"Cú Pháp" Mệnh Đề `WHERE` "Cơ Bản":**

  ```sql
  SELECT ...
  FROM table_name
  WHERE condition; -- Mệnh đề WHERE - "điều kiện" "lọc" dữ liệu
  ```

    - **`condition`:** **"Điều kiện"** "lọc" dữ liệu. "Điều kiện" thường là một **"biểu thức 'logic' "** (logical
      expression) "trả về" **`TRUE`** hoặc **`FALSE`** cho mỗi bản ghi (row) trong bảng. "Chỉ" những bản ghi mà "điều
      kiện" "trả về" **`TRUE`** mới được "lấy" vào kết quả truy vấn.

- **"Các 'Toán Tử So Sánh' " (Comparison Operators) "Phổ Biến" Trong Mệnh Đề `WHERE`:**

    - **`=` (Equal):** "Bằng". (Ví dụ: `Gia = 250000` - "Giá bằng 250000").
    - **`>` (Greater Than):** "Lớn hơn". (Ví dụ: `Gia > 1000000` - "Giá lớn hơn 1 triệu").
    - **`<` (Less Than):** "Nhỏ hơn". (Ví dụ: `Gia < 500000` - "Giá nhỏ hơn 500 ngàn").
    - **`>=` (Greater Than or Equal To):** "Lớn hơn hoặc bằng". (Ví dụ: `Gia >= 1000000` - "Giá lớn hơn hoặc bằng 1
      triệu").
    - **`<=` (Less Than or Equal To):** "Nhỏ hơn hoặc bằng". (Ví dụ: `Gia <= 500000` - "Giá nhỏ hơn hoặc bằng 500
      ngàn").
    - **`<>` hoặc `!=` (Not Equal):** "Không bằng". (Ví dụ: `DanhMucSanPham <> 'Điện tử'` - "Danh mục sản phẩm không
      phải là 'Điện tử' ").
    - **`LIKE` (Pattern Matching - So Khớp Mẫu):** "So khớp" chuỗi với **"mẫu"** (pattern). "Dùng" các **"wildcard
      characters"** (ký tự đại diện) để "xây dựng" "mẫu".
        - **`%` (Percent Sign):** "Đại diện" cho **"không, một, hoặc nhiều ký tự bất kỳ"**. (Ví dụ:
          `TenSanPham LIKE 'Sách %'` - "Tên sản phẩm bắt đầu bằng 'Sách ' " (có thể có thêm ký tự bất kỳ "sau")).
        - **`_` (Underscore):** "Đại diện" cho **"một ký tự bất kỳ"**. (Ví dụ: `TenSanPham LIKE 'Sách _ _ _'` - "Tên sản
          phẩm bắt đầu bằng 'Sách ' " và có thêm "ba ký tự bất kỳ" "sau").

    - **`BETWEEN ... AND ...` (Range - Khoảng Giá Trị):** "Kiểm tra" giá trị có nằm trong **"khoảng giá trị"** "cho
      trước" không (bao gồm cả giá trị "đầu" và giá trị "cuối" của "khoảng"). (Ví dụ:
      `Gia BETWEEN 500000 AND 1500000` - "Giá nằm trong khoảng từ 500 ngàn đến 1.5 triệu").
    - **`IN (...)` (List - Danh Sách Giá Trị):** "Kiểm tra" giá trị có nằm trong **"danh sách"** các giá trị "cho trước"
      không. (Ví dụ: `DanhMucSanPham IN ('Điện tử', 'Sách', 'Thời trang')` - "Danh mục sản phẩm thuộc một trong các danh
      mục: 'Điện tử', 'Sách', 'Thời trang' ").
    - **`IS NULL` và `IS NOT NULL` (Null Value - Giá Trị NULL):** "Kiểm tra" giá trị có phải là **`NULL`** (giá trị "
      rỗng", "không có giá trị") hay không. (Ví dụ: `MoTa IS NULL` - "Mô tả sản phẩm là NULL", `MoTa IS NOT NULL` - "Mô
      tả sản phẩm không phải là NULL").

- **"Ví Dụ" Mệnh Đề `WHERE` - " 'Hỏi' " Database: " 'Cho Xem' " "Sản Phẩm Nào" Có " 'Giá' " "Nhỏ Hơn 500 Ngàn" Từ
  Bảng `SanPhams`:**

  ```sql
  SELECT *        -- "Chọn" tất cả các cột (*)
  FROM SanPhams   -- Từ bảng SanPhams
  WHERE Gia < 500000; -- "Lọc" sản phẩm có "Giá" "nhỏ hơn 500 ngàn" (điều kiện WHERE)
  ```

    - **"Kết quả"** truy vấn (ví dụ):

      | SanPhamId | TenSanPham         | Gia     | DanhMucSanPham |
              | --------- | ------------------ | ------- | ------------- |
      | 1         | Chuột không dây      | 250000  | Điện tử        |
      | 5         | Sách "Lập trình C#" | 150000  | Sách           |
      | 6         | Sách "OOP"          | 120000  | Sách           |
      | ...       | ...                | ...     | ...           |

**2.4. "Thực Hành" Truy Vấn SQL Cơ Bản - " 'Viết' " và " 'Chạy' " Các Câu Truy Vấn "Đầu Tiên" - " 'Cảm Nhận' " "Sức
Mạnh" SQL Trong " 'Thực Tế' "**

- **"Công Cụ" "Thực Hành" SQL - "SQL Client Tools":**

    - Để "thực hành" "viết" và "chạy" các câu truy vấn SQL, bạn cần "dùng" một **"SQL client tool"** (công cụ client
      SQL) "tương ứng" với RDBMS mà bạn đang "học" SQL.
    - "Các SQL client tools" "phổ biến":
        - **SQL Server Management Studio (SSMS):** "Dành cho" **SQL Server**. "Giao diện" GUI "mạnh mẽ" để "quản lý"
          và "truy vấn" SQL Server databases. (Windows only).
        - **pgAdmin:** "Dành cho" **PostgreSQL**. "Giao diện" GUI "đa nền tảng" (cross-platform) (Windows, macOS, Linux)
          để "quản lý" và "truy vấn" PostgreSQL databases.
        - **MySQL Workbench:** "Dành cho" **MySQL**. "Giao diện" GUI "đa nền tảng" để "quản lý" và "truy vấn" MySQL
          databases.
        - **Dbeaver:** "Công cụ" SQL client **"đa năng"** (universal database tool) "hỗ trợ" **"nhiều loại" databases
          khác nhau** (MySQL, PostgreSQL, SQL Server, Oracle, SQLite, v.v.). "Giao diện" GUI "đa nền tảng". "Lựa chọn"
          tốt nếu bạn muốn "làm việc" với "nhiều loại" databases.
        - **SQLiteStudio:** "Dành cho" **SQLite**. "Công cụ" GUI "nhẹ nhàng" và "dễ dùng" để "quản lý" và "truy vấn"
          SQLite databases.
        - **Command Line Interface (CLI) Clients:** Các RDBMSs cũng thường "cung cấp" các **"command line interface (
          CLI) clients"** (ví dụ: `mysql` client cho MySQL, `psql` client cho PostgreSQL, `sqlcmd` client cho SQL
          Server, `sqlite3` client cho SQLite). "Dành cho" dân "pro" thích "gõ lệnh" và "làm việc" trên command line.

- **"Các Bước" "Thực Hành" Truy Vấn SQL Cơ Bản Với SQL Client Tool (ví dụ: Dbeaver):**

    1. **"Cài đặt" và "khởi động" SQL Client Tool** (ví dụ: Dbeaver).
    2. **"Kết nối" đến database** mà bạn muốn "thực hành" SQL (ví dụ: database "mẫu" hoặc database "riêng" của bạn).
    3. **"Mở" một "SQL editor"** (trình soạn thảo SQL) trong SQL Client Tool.
    4. **"Viết" câu truy vấn SQL** (ví dụ: các câu truy vấn ví dụ ở trên - `SELECT TenSanPham, Gia FROM SanPhams;`,
       `SELECT * FROM DanhMucs;`, `SELECT * FROM SanPhams WHERE Gia < 500000;`).
    5. **"Chạy" câu truy vấn SQL** (thường bằng cách bấm nút "Execute" hoặc "Run SQL" trong SQL Client Tool).
    6. **"Xem" "kết quả" truy vấn** (dữ liệu được "trả về" từ database) trong "bảng" "kết quả" (result grid) của SQL
       Client Tool.
    7. **"Thử nghiệm"** "sửa đổi" câu truy vấn SQL (ví dụ: "thay đổi" "tên cột", "thêm" "điều kiện" `WHERE`, "thay
       đổi" "toán tử so sánh", v.v.) và "chạy" lại truy vấn để "thấy" "kết quả" "thay đổi" như thế nào. **"Thực hành" "
       thử nghiệm" "không ngừng nghỉ"** để "làm quen" với "cú pháp" SQL và "hiểu" "cách" SQL queries "hoạt động".

**Tổng Kết Chương 2:**

- Bạn đã "bắt đầu" "hành trình" SQL bằng cách "học cách" "viết" các câu truy vấn SQL "cơ bản" nhất để "lấy" dữ liệu từ
  database.
    - "Nắm vững" lệnh **`SELECT`** ("chọn" cột dữ liệu).
    - "Hiểu" mệnh đề **`FROM`** ("chỉ định" bảng dữ liệu).
    - "Làm chủ" mệnh đề **`WHERE`** ("lọc" dữ liệu theo "điều kiện").
    - Học cách "dùng" **SQL client tools** để "thực hành" "viết" và "chạy" các câu truy vấn SQL "cơ bản" và "xem" "kết
      quả" truy vấn "thực tế".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 3: Sắp Xếp và Lọc Dữ Liệu Nâng Cao - ORDER BY, LIMIT, OFFSET, AND, OR, NOT**. Chúng ta
sẽ "nâng cấp" "kỹ năng" truy vấn SQL của bạn lên một "tầm cao mới" bằng cách "học cách" "sắp xếp" kết quả truy vấn, "
phân trang" kết quả, và "lọc" dữ liệu theo các "điều kiện" "phức tạp" hơn bằng các mệnh đề **`ORDER BY`**, **`LIMIT`**,
**`OFFSET`**, và các toán tử **`AND`**, **`OR`**, **`NOT`**.

Bạn có câu hỏi nào về truy vấn SQL "cơ bản" này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng
hành" cùng bạn trên con đường "chinh phục" SQL.

