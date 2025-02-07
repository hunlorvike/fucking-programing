# Chương 4: Hàm Tổng Hợp và GROUP BY - COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING - " 'Tính Toán' " và " 'Thống Kê' " Dữ Liệu "Theo Nhóm" - " 'Khai Thác' " "Thông Tin" "Giá Trị" Từ " 'Biển' " Dữ Liệu

Chào mừng bạn đến với **Chương 4: Hàm Tổng Hợp và GROUP BY - COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING**! Trong chương
này, chúng ta sẽ "khám phá" **"sức mạnh"** của **"hàm tổng hợp"** (aggregate functions) và mệnh đề **`GROUP BY`** trong
SQL. Chúng ta sẽ "học cách" "dùng" các "hàm tổng hợp" **`COUNT`**, **`SUM`**, **`AVG`**, **`MIN`**, **`MAX`** để "tính
toán" các **"giá trị" "tổng quan"** trên dữ liệu (ví dụ: "đếm" số lượng, "tính tổng", "tính trung bình", "tìm" "giá
trị" "lớn nhất", "nhỏ nhất"). Và "làm chủ" mệnh đề **`GROUP BY`** để **"nhóm"** dữ liệu theo "tiêu chí" và "thực hiện"
các phép "tính toán" "tổng hợp" trên dữ liệu **"theo từng nhóm"**. "Hàm Tổng Hợp" và `GROUP BY` là "công cụ" "đắc lực"
để "khai thác" **"thông tin" "giá trị"** từ "biển" dữ liệu và "biến" dữ liệu "thô" thành **"thống kê"** và **"phân
tích" "chuyên sâu"**.

**Phần 4: Hàm Tổng Hợp và GROUP BY - COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING - " 'Tính Toán' " và " 'Thống Kê' " Dữ
Liệu "Theo Nhóm"**

**4.1. Hàm Tổng Hợp (Aggregate Functions) - " 'Tính Toán' " "Giá Trị" "Tổng Quan" Trên Dữ Liệu - " 'Nhìn' " Dữ Liệu
Từ " 'Góc Độ' " "Thống Kê"**

- **Hàm Tổng Hợp (Aggregate Functions) - " 'Máy Tính' " "Chuyên Nghiệp" Cho Dữ Liệu Database:**

    - **Hàm Tổng Hợp (Aggregate Functions)** là các **"hàm"** "đặc biệt" trong SQL, "dùng" để **"thực hiện" các phép "
      tính toán" "tổng hợp"** (aggregation) trên **"nhiều bản ghi"** (rows) và "trả về" **"một giá trị" "duy nhất"** "
      tổng hợp" (single aggregated value) cho **"tập hợp"** các bản ghi đó.
    - Hàm Tổng Hợp "cho phép" bạn **" 'nhìn' " dữ liệu từ " 'góc độ' " "thống kê"** và "khai thác" các **"thông tin" "
      tổng quan"** về dữ liệu (ví dụ: "tổng số lượng", "giá trị trung bình", "giá trị lớn nhất", "nhỏ nhất", v.v.). "
      Không cần" phải "lấy" và "xử lý" "từng bản ghi" "riêng lẻ" để "tính toán" các "giá trị" "tổng hợp". Database sẽ "
      thực hiện" "tính toán" "hiệu quả" và "trả về" "kết quả" "tổng hợp" "ngay lập tức".

- **"Các Hàm Tổng Hợp" SQL "Phổ Biến" Nhất:**

    - **`COUNT()` - "Đếm" "Số Lượng" Bản Ghi (Rows):**
        - Hàm `COUNT()` "đếm" **"số lượng" "bản ghi"** (rows) trong một **"bảng"** hoặc trong một **"nhóm"** dữ liệu.
        - **`COUNT(*)`:** "Đếm" **"tất cả"** các bản ghi (rows) (bao gồm cả các bản ghi có giá trị `NULL`).
        - **`COUNT(column_name)`:** "Đếm" **"số lượng"** các bản ghi có giá trị **"không NULL"** trong cột
          `column_name`.

        - **"Ví dụ" - " 'Hỏi' " Database: " 'Có Bao Nhiêu' " "Sản Phẩm" Trong Bảng `SanPhams`?**

          ```sql
          SELECT COUNT(*)  -- "Đếm" tất cả các bản ghi (*)
          FROM SanPhams;     -- Từ bảng SanPhams
          ```

            - **"Kết quả"** truy vấn (ví dụ):

              | COUNT(*) |
                              | -------- |
              | 15       |
                - "Kết quả" "trả về" là **`15`** - "tổng số lượng" sản phẩm trong bảng `SanPhams` là 15.

    - **`SUM()` - "Tính Tổng" "Giá Trị" Của Cột Số:**
        - Hàm `SUM()` "tính tổng" **"tổng giá trị"** của một **"cột số"** (numeric column) trong một **"bảng"** hoặc
          trong một **"nhóm"** dữ liệu.
        - "Chỉ áp dụng" cho các cột có kiểu dữ liệu **"số"** (numeric types) (ví dụ: `INT`, `DECIMAL`, `FLOAT`, v.v.). "
          Bỏ qua" các giá trị `NULL` trong cột khi "tính tổng".

        - **"Ví dụ" - " 'Hỏi' " Database: " 'Tổng Giá Trị' " "Tất Cả" "Sản Phẩm" Trong Bảng `SanPhams`?**

          ```sql
          SELECT SUM(Gia)  -- "Tính tổng" giá trị của cột Gia
          FROM SanPhams;    -- Từ bảng SanPhams
          ```

            - **"Kết quả"** truy vấn (ví dụ):

              | SUM(Gia) |
                              | -------- |
              | 12345678 |
                - "Kết quả" "trả về" là **`12345678`** - "tổng giá trị" của "tất cả" sản phẩm trong bảng `SanPhams` là
                  12,345,678 VND.

    - **`AVG()` - "Tính Trung Bình" "Giá Trị" Của Cột Số:**
        - Hàm `AVG()` "tính trung bình" **"giá trị trung bình"** (average value) của một **"cột số"** trong một **"bảng"
          ** hoặc trong một **"nhóm"** dữ liệu.
        - "Chỉ áp dụng" cho các cột có kiểu dữ liệu **"số"**. "Bỏ qua" các giá trị `NULL` trong cột khi "tính trung
          bình".

        - **"Ví dụ" - " 'Hỏi' " Database: " 'Giá Trung Bình' " Của " "Sản Phẩm" Trong Bảng `SanPhams`?**

          ```sql
          SELECT AVG(Gia)  -- "Tính trung bình" giá trị của cột Gia
          FROM SanPhams;    -- Từ bảng SanPhams
          ```

            - **"Kết quả"** truy vấn (ví dụ):

              | AVG(Gia)    |
                              | ----------- |
              | 823045.2    |
                - "Kết quả" "trả về" là **`823045.2`** - "giá trung bình" của "tất cả" sản phẩm trong bảng `SanPhams` là
                  823,045.2 VND.

    - **`MIN()` - "Tìm Giá Trị" "Nhỏ Nhất" Của Cột:**
        - Hàm `MIN()` "tìm" **"giá trị" "nhỏ nhất"** (minimum value) trong một **"cột"** (có thể là cột "số", cột "
          chuỗi", hoặc cột "ngày tháng") trong một **"bảng"** hoặc trong một **"nhóm"** dữ liệu.
        - "Bỏ qua" các giá trị `NULL` trong cột khi "tìm" giá trị "nhỏ nhất".

        - **"Ví dụ" - " 'Hỏi' " Database: " 'Giá' " "Nhỏ Nhất" Của " "Sản Phẩm" Trong Bảng `SanPhams`?**

          ```sql
          SELECT MIN(Gia)  -- "Tìm" giá trị "nhỏ nhất" của cột Gia
          FROM SanPhams;    -- Từ bảng SanPhams
          ```

            - **"Kết quả"** truy vấn (ví dụ):

              | MIN(Gia) |
                              | -------- |
              | 120000  |
                - "Kết quả" "trả về" là **`120000`** - "giá" "nhỏ nhất" của "tất cả" sản phẩm trong bảng `SanPhams` là
                  120,000 VND.

    - **`MAX()` - "Tìm Giá Trị" "Lớn Nhất" Của Cột:**
        - Hàm `MAX()` "tìm" **"giá trị" "lớn nhất"** (maximum value) trong một **"cột"** (có thể là cột "số", cột "
          chuỗi", hoặc cột "ngày tháng") trong một **"bảng"** hoặc trong một **"nhóm"** dữ liệu.
        - "Bỏ qua" các giá trị `NULL` trong cột khi "tìm" giá trị "lớn nhất".

        - **"Ví dụ" - " 'Hỏi' " Database: " 'Giá' " "Lớn Nhất" Của " "Sản Phẩm" Trong Bảng `SanPhams`?**

          ```sql
          SELECT MAX(Gia)  -- "Tìm" giá trị "lớn nhất" của cột Gia
          FROM SanPhams;    -- Từ bảng SanPhams
          ```

            - **"Kết quả"** truy vấn (ví dụ):

              | MAX(Gia)  |
                              | --------- |
              | 3500000   |
                - "Kết quả" "trả về" là **`3500000`** - "giá" "lớn nhất" của "tất cả" sản phẩm trong bảng `SanPhams` là
                  3,500,000 VND.

**4.2. Mệnh Đề `GROUP BY` - " 'Nhóm' " Dữ Liệu Theo " 'Tiêu Chí' " - " 'Chia' " Dữ Liệu Thành " 'Từng Nhóm' " Để " '
Thống Kê' " "Chi Tiết" Hơn**

- **Mệnh Đề `GROUP BY` - " 'Phân Loại' " Dữ Liệu Để " 'Tổng Hợp' " "Theo Nhóm":**

    - **Mệnh Đề `GROUP BY`** là mệnh đề "tùy chọn" (optional) trong câu truy vấn SQL, "dùng" để **"nhóm"** (group) các *
      *"bản ghi"** (rows) trong một **"bảng"** dựa trên **"giá trị"** của **"một hoặc nhiều cột"** (columns) và "thực
      hiện" các phép **"tính toán" "tổng hợp"** (aggregate functions) **"cho từng nhóm"**.
    - `GROUP BY` "cho phép" bạn "phân tích" dữ liệu **"theo từng nhóm"** và "khai thác" các **"thông tin" "thống kê"** "
      chi tiết" hơn (ví dụ: "tổng số lượng sản phẩm" **"theo từng danh mục"**, "giá trung bình sản phẩm" **"theo từng
      nhà sản xuất"**, v.v.).

- **"Cú Pháp" Mệnh Đề `GROUP BY` "Cơ Bản":**

  ```sql
  SELECT column1, column2, ..., aggregate_function(column_to_aggregate) -- "Chọn" các cột "nhóm" và "hàm tổng hợp"
  FROM table_name
  [WHERE condition] -- (tùy chọn)
  GROUP BY column1, column2, ... -- Mệnh đề GROUP BY - "nhóm" dữ liệu theo các cột
  [ORDER BY column_to_sort [ASC|DESC]]; -- (tùy chọn)
  ```

    - **`GROUP BY column1, column2, ...`:** "Liệt kê" **"tên các cột"** (column names) mà bạn muốn **"nhóm"** dữ liệu
      theo, **"cách nhau" bằng dấu phẩy (`,`)**. Các bản ghi có **"cùng giá trị"** ở các cột "nhóm" sẽ được **"gom
      vào" "cùng một nhóm"**.
    - **`SELECT column1, column2, ..., aggregate_function(column_to_aggregate)`:** Trong mệnh đề `SELECT`, bạn cần "
      chọn" **"các cột"** mà bạn "dùng" để **"nhóm"** ( `column1, column2, ...` ) và **"ít nhất một" "hàm tổng hợp"** (
      aggregate function) (ví dụ: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`) để "tính toán" "giá trị" "tổng hợp" cho
      **"mỗi nhóm"**.

- **"Ví Dụ" Mệnh Đề `GROUP BY` - " 'Hỏi' " Database: " 'Số Lượng Sản Phẩm' " Trong " 'Mỗi Danh Mục' " Từ
  Bảng `SanPhams`:**

  ```sql
  SELECT DanhMucSanPham, COUNT(*) AS SoLuongSanPham  -- "Chọn" cột DanhMucSanPham (cột "nhóm") và "tính tổng hợp" COUNT(*) (đếm số lượng sản phẩm)
  FROM SanPhams                                    -- Từ bảng SanPhams
  GROUP BY DanhMucSanPham;                           -- "Nhóm" dữ liệu theo cột DanhMucSanPham
  ```

    - **"Giải thích"**: Câu truy vấn này sẽ "nhóm" các sản phẩm trong bảng `SanPhams` theo "danh mục sản phẩm" (
      `DanhMucSanPham`) và "tính toán" **"số lượng sản phẩm"** (`COUNT(*)`) trong **"mỗi nhóm" "danh mục sản phẩm"**.

    - **"Kết quả"** truy vấn (ví dụ):

      | DanhMucSanPham | SoLuongSanPham |
              | ------------- | ------------- |
      | Điện tử        | 4             |
      | Đồ gia dụng    | 3             |
      | Nội thất       | 2             |
      | Sách           | 6             |
      | ...           | ...           |
        - "Kết quả" "trả về" "số lượng sản phẩm" **"trong từng danh mục"** (ví dụ: "Danh mục 'Điện tử' có 4 sản phẩm", "
          Danh mục 'Sách' có 6 sản phẩm", v.v.).

- **"Tính Toán" "Nhiều Hàm Tổng Hợp" Trong `GROUP BY` - " 'Thống Kê' " "Đa Chiều" và " 'Chi Tiết' " Hơn:** Bạn có thể "
  tính toán" **"nhiều hàm tổng hợp"** "cùng lúc" trong câu truy vấn `GROUP BY` để "khai thác" "thông tin" "thống kê" "đa
  chiều" và "chi tiết" hơn.

    - **"Ví dụ" - " 'Hỏi' " Database: " 'Số Lượng Sản Phẩm' ", " 'Giá Trung Bình' ", " 'Giá Lớn Nhất' ", và " 'Giá Nhỏ
      Nhất' " Trong " 'Mỗi Danh Mục' " Từ Bảng `SanPhams`:**

      ```sql
      SELECT DanhMucSanPham,                              -- "Chọn" cột DanhMucSanPham (cột "nhóm")
             COUNT(*) AS SoLuongSanPham,                 -- "Tính tổng hợp" COUNT(*) (số lượng sản phẩm)
             AVG(Gia) AS GiaTrungBinhSanPham,            -- "Tính tổng hợp" AVG(Gia) (giá trung bình sản phẩm)
             MAX(Gia) AS GiaCaoNhatSanPham,              -- "Tính tổng hợp" MAX(Gia) (giá lớn nhất sản phẩm)
             MIN(Gia) AS GiaNhoNhatSanPham               -- "Tính tổng hợp" MIN(Gia) (giá nhỏ nhất sản phẩm)
      FROM SanPhams                                        -- Từ bảng SanPhams
      GROUP BY DanhMucSanPham;                               -- "Nhóm" dữ liệu theo cột DanhMucSanPham
      ```

        - **"Kết quả"** truy vấn (ví dụ):

          | DanhMucSanPham | SoLuongSanPham | GiaTrungBinhSanPham | GiaCaoNhatSanPham | GiaNhoNhatSanPham |
                      | ------------- | ------------- | ------------------- | ----------------- | ----------------- |
          | Điện tử        | 4             | 1550000             | 3500000           | 250000            |
          | Đồ gia dụng    | 3             | 800000              | 1200000           | 500000            |
          | Nội thất       | 2             | 2500000             | 3000000           | 2000000           |
          | Sách           | 6             | 135000              | 200000            | 120000            |
          | ...           | ...           | ...                 | ...               | ...               |
            - "Kết quả" "trả về" **"thông tin" "thống kê" "đa chiều"** và "chi tiết" hơn **"cho từng danh mục"** (ví
              dụ: "Danh mục 'Điện tử' có 4 sản phẩm, giá trung bình 1.55 triệu, giá cao nhất 3.5 triệu, giá nhỏ nhất 250
              ngàn", v.v.).

**4.3. Mệnh Đề `HAVING` - " 'Lọc' " Các " 'Nhóm' " Dữ Liệu Theo " 'Điều Kiện' " - " 'Lọc Sau' " Khi Đã " 'Nhóm' " Xong**

- **Mệnh Đề `HAVING` - " 'Bộ Lọc' " Cho Các " 'Nhóm' " Dữ Liệu - " 'Lọc' " "Sau Khi Đã Nhóm", "Không Phải" "Lọc Trước
  Khi Nhóm"**:

    - **Mệnh Đề `HAVING`** là mệnh đề "tùy chọn" (optional) trong câu truy vấn SQL `GROUP BY`, "dùng" để **"lọc"** (
      filter) **"các nhóm"** dữ liệu (groups) được "tạo ra" bởi mệnh đề `GROUP BY` dựa trên **"điều kiện"** "tổng hợp" (
      aggregated condition).
    - `HAVING` "giống như" mệnh đề `WHERE`, nhưng `WHERE` "lọc" **"các bản ghi"** (rows) **"trước khi 'nhóm' "**, còn
      `HAVING` "lọc" **"các nhóm"** dữ liệu **"sau khi 'nhóm' " xong**.
    - `HAVING` "ra lệnh" cho database là **" 'chỉ giữ lại' " những " 'nhóm' " dữ liệu** mà **"thỏa mãn' " "điều kiện"
      ** "tổng hợp" đã "chỉ định". "Bỏ qua" các "nhóm" "không thỏa mãn" "điều kiện".
    - `HAVING` thường được "dùng" để "lọc" các "nhóm" dữ liệu dựa trên **"giá trị" "tổng hợp"** (ví dụ: "lọc" các "danh
      mục" có "tổng số lượng sản phẩm" "lớn hơn 5", "lọc" các "nhà sản xuất" có "giá trung bình sản phẩm" "cao hơn 1
      triệu", v.v.).

- **"Cú Pháp" Mệnh Đề `HAVING` "Cơ Bản":**

  ```sql
  SELECT column1, column2, ..., aggregate_function(column_to_aggregate)
  FROM table_name
  [WHERE condition] -- (tùy chọn) - "lọc" bản ghi "trước khi 'nhóm' " (WHERE filter)
  GROUP BY column1, column2, ... -- Mệnh đề GROUP BY - "nhóm" dữ liệu
  HAVING aggregated_condition; -- Mệnh đề HAVING - "lọc" "các nhóm" dữ liệu "sau khi 'nhóm' " (HAVING filter)
  [ORDER BY column_to_sort [ASC|DESC]]; -- (tùy chọn)
  ```

    - **`HAVING aggregated_condition`:** **"Điều kiện"** "tổng hợp" (aggregated condition) để "lọc" "các nhóm" dữ
      liệu. "Điều kiện" `HAVING` thường "dùng" **"hàm tổng hợp"** (aggregate function) (ví dụ: `COUNT(*)`, `SUM()`,
      `AVG()`, `MIN()`, `MAX()`) để "tính toán" "giá trị" "tổng hợp" và "so sánh" giá trị "tổng hợp" đó với một "giá
      trị" "cố định" hoặc một "giá trị" "tổng hợp" khác.

- **"Ví Dụ" Mệnh Đề `HAVING` - " 'Hỏi' " Database: " 'Cho Xem' " "Danh Mục Nào" Có " 'Tổng Số Lượng Sản Phẩm' " "Lớn Hơn
  5" Từ Bảng `SanPhams` (đã "Nhóm" Theo " 'Danh Mục Sản Phẩm' "):**

  ```sql
  SELECT DanhMucSanPham, COUNT(*) AS SoLuongSanPham  -- "Chọn" cột DanhMucSanPham (cột "nhóm") và "tính tổng hợp" COUNT(*) (số lượng sản phẩm)
  FROM SanPhams                                    -- Từ bảng SanPhams
  GROUP BY DanhMucSanPham                           -- "Nhóm" dữ liệu theo cột DanhMucSanPham
  HAVING COUNT(*) > 5;                              -- "Lọc" "các nhóm" "danh mục sản phẩm" có "tổng số lượng sản phẩm" "lớn hơn 5" (điều kiện HAVING)
  ```

    - **"Giải thích"**: Câu truy vấn này sẽ "nhóm" các sản phẩm theo "danh mục sản phẩm", "tính toán" "số lượng sản
      phẩm" trong "mỗi nhóm", và **"chỉ giữ lại"** (lọc) các "nhóm" "danh mục sản phẩm" có **"tổng số lượng sản phẩm"
      ** "lớn hơn 5".

    - **"Kết quả"** truy vấn (ví dụ):

      | DanhMucSanPham | SoLuongSanPham |
              | ------------- | ------------- |
      | Sách           | 6             |
      | ...           | ...           |
        - "Kết quả" "trả về" "chỉ" "danh mục" **"Sách"** (và các danh mục khác nếu có) vì chỉ "danh mục" "Sách" có "tổng
          số lượng sản phẩm" "lớn hơn 5". Các "danh mục" khác có "tổng số lượng sản phẩm" "nhỏ hơn hoặc bằng 5" đã bị "
          lọc" bởi mệnh đề `HAVING COUNT(*) > 5`.

- **" 'Thứ Tự' " Thực Hiện Các Mệnh Đề SQL Trong Câu Truy Vấn `GROUP BY` và `HAVING`:**

    - Khi câu truy vấn SQL có cả mệnh đề `WHERE`, `GROUP BY`, và `HAVING`, **"thứ tự" "thực hiện"** các mệnh đề này là:

        1. **`FROM`**: Database "xác định" "bảng" dữ liệu "đầu vào".
        2. **`WHERE`**: Database "lọc" **"các bản ghi"** (rows) "thỏa mãn" "điều kiện" `WHERE` ( **"lọc 'bản ghi' " "
           trước khi 'nhóm' " **).
        3. **`GROUP BY`**: Database "nhóm" **"các bản ghi"** đã "lọc" (từ bước `WHERE`) theo "các cột" "nhóm" đã "chỉ
           định".
        4. **`HAVING`**: Database "lọc" **"các nhóm"** dữ liệu "thỏa mãn" "điều kiện" `HAVING` ( **"lọc 'nhóm' " "sau
           khi 'nhóm' " **).
        5. **`SELECT`**: Database "chọn" **"các cột"** (cột "nhóm" và cột "tổng hợp") và "tính toán" **"hàm tổng hợp"**
           cho "các nhóm" "đã lọc" (từ bước `HAVING`).
        6. **`ORDER BY`**: Database "sắp xếp" "kết quả truy vấn" (các "nhóm" dữ liệu đã "tổng hợp") theo "thứ tự" "sắp
           xếp" đã "chỉ định".
        7. **`LIMIT` và `OFFSET`**: Database "phân trang" "kết quả truy vấn" (sau khi đã "sắp xếp").

**4.4. "Thực Hành" Hàm Tổng Hợp và GROUP BY - " 'Thống Kê' " và " 'Phân Tích' " Dữ Liệu "Chuyên Sâu" - " 'Khai Thác' " "
Thông Tin" "Giá Trị" Từ Database**

- **"Bài Tập" "Thực Hành" - " 'Luyện Công Phu' " Truy Vấn SQL "Tổng Hợp" và "Nhóm":**

    1. **"Đếm" "tổng số lượng" sản phẩm trong "mỗi danh mục".** (Dùng `COUNT(*)` và `GROUP BY`).
    2. **"Tính tổng" "giá" của sản phẩm trong "mỗi danh mục".** (Dùng `SUM(Gia)` và `GROUP BY`).
    3. **"Tính trung bình" "giá" của sản phẩm trong "mỗi danh mục".** (Dùng `AVG(Gia)` và `GROUP BY`).
    4. **"Tìm" "giá" sản phẩm "cao nhất" và "nhỏ nhất" trong "mỗi danh mục".** (Dùng `MAX(Gia)`, `MIN(Gia)`, và
       `GROUP BY`).
    5. **"Lọc" "các danh mục" có "tổng số lượng sản phẩm" "lớn hơn 3".** (Dùng `GROUP BY`, `HAVING COUNT(*) > 3`).
    6. **"Lọc" "các danh mục" có "giá trung bình sản phẩm" "lớn hơn 1 triệu".** (Dùng `GROUP BY`,
       `HAVING AVG(Gia) > 1000000`).
    7. **"Kết hợp" "lọc" "bản ghi" (WHERE) và "lọc" "nhóm" (HAVING): "Lấy" "các danh mục" (không phải là "Sách") có "giá
       trung bình sản phẩm" "lớn hơn 700 ngàn", "sắp xếp" theo "giá trung bình" "giảm dần".** ( "Bài toán tổng hợp" - "
       thử thách" "kỹ năng" truy vấn SQL của bạn).

- **"Thực Hành" Với SQL Client Tool - " 'Thống Kê' " và " 'Phân Tích' " Dữ Liệu "Thực Tế":**

    - "Mở" SQL client tool.
    - "Kết nối" đến database "mẫu" hoặc database "riêng" của bạn.
    - "Mở" SQL editor và "viết" các câu truy vấn SQL "thực hành" cho từng "bài tập" trên.
    - "Chạy" các câu truy vấn và "xem" "kết quả" truy vấn (các "bảng" "thống kê" dữ liệu "theo nhóm").
    - " 'Sáng tạo' ", " 'thử nghiệm' ", và " 'khám phá' " các "cách" "kết hợp" "linh hoạt" các hàm tổng hợp, mệnh đề
      `GROUP BY`, và mệnh đề `HAVING` để "khai thác" "thông tin" "giá trị" từ database "theo ý muốn" của bạn.

**Tổng Kết Chương 4:**

- Bạn đã "khám phá" **Hàm Tổng Hợp** và mệnh đề **`GROUP BY`**, "công cụ" "mạnh mẽ" để "tính toán" và "thống kê" dữ liệu
  trong SQL.
    - "Nắm vững" các **"hàm tổng hợp" "phổ biến"**: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`.
    - "Hiểu" mệnh đề **`GROUP BY`** và "cách" "nhóm" dữ liệu theo "tiêu chí" và "thực hiện" "tính toán" "tổng hợp"
      trên "từng nhóm".
    - "Làm chủ" mệnh đề **`HAVING`** ("lọc" "các nhóm" dữ liệu).
    - "Thực hành" "viết" và "chạy" các câu truy vấn SQL "tổng hợp" và "nhóm" dữ liệu để "luyện tập" và "khai thác" "
      thông tin" "giá trị" từ database.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 5: Joins - " 'Mối Quan Hệ' " Giữa Các Bảng - " 'Gắn Kết' " Dữ Liệu Từ Nhiều Bảng**.
Chúng ta sẽ "khám phá" **Joins**, "kỹ thuật" "quan trọng" để **"kết hợp"** dữ liệu từ **"nhiều bảng"** "quan hệ" trong
database, "mở rộng" "khả năng" truy vấn SQL và "khai thác" "mối quan hệ" giữa các bảng.

Bạn có câu hỏi nào về Hàm Tổng Hợp và `GROUP BY` này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp"
và "đồng hành" cùng bạn trên con đường "chinh phục" SQL.
