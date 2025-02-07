# Chương 5: Joins - " 'Gắn Kết' " Dữ Liệu Từ Nhiều Bảng - " 'Mạng Lưới' " Dữ Liệu "Quan Hệ" - " 'Vượt Qua' " "Giới Hạn" Một Bảng Để " 'Khám Phá' " "Toàn Cảnh" Dữ Liệu

Chào mừng bạn đến với **Chương 5: Joins - " 'Mối Quan Hệ' " Giữa Các Bảng**! Trong chương này, chúng ta sẽ "khám phá" *
*Joins**, một "kỹ thuật" **"vô cùng quan trọng"** và **"mạnh mẽ"** trong SQL, "cho phép" bạn **"kết hợp"** dữ liệu từ *
*"nhiều bảng"** "quan hệ" trong database thành **"một tập kết quả" "duy nhất"**. Joins giúp bạn **"vượt qua"** "giới
hạn" "một bảng" và "khai thác" **"mối quan hệ"** giữa các bảng để "lấy" **"dữ liệu" "đa dạng"** và **"phong phú"**
hơn, " 'khám phá' " "toàn cảnh" dữ liệu trong database "quan hệ".

**Phần 5: Joins - " 'Mối Quan Hệ' " Giữa Các Bảng - " 'Gắn Kết' " Dữ Liệu Từ Nhiều Bảng**

**5.1. Joins (Phép Kết Nối) - " 'Gắn Kết' " Dữ Liệu Từ "Nhiều Bảng" "Quan Hệ" - " 'Mở Rộng' " "Góc Nhìn" Dữ Liệu**

- **Joins (Phép Kết Nối) - " 'Kết Hợp' " Dữ Liệu " 'Vượt Qua' " "Ranh Giới" "Bảng Biểu":**

    - **Joins** (Phép Kết Nối) trong SQL là một "kỹ thuật" "cho phép" bạn **"kết hợp"** (combine) **"các bản ghi"** (
      rows) từ **"hai hoặc nhiều bảng"** trong database thành **"một tập kết quả"** (result set) dựa trên **"mối quan
      hệ"** giữa các bảng.
    - Trong cơ sở dữ liệu "quan hệ" (Relational Database), dữ liệu thường được "phân chia" và "lưu trữ" ở **"nhiều
      bảng" "liên quan"** với nhau (ví dụ: bảng `SanPhams` (Products) và bảng `DanhMucs` (Categories) có "quan hệ"
      Một-Nhiều). Để "lấy" dữ liệu "liên quan" từ nhiều bảng, bạn cần "dùng" **Joins**.
    - Joins "cho phép" bạn **" 'vượt qua' " "ranh giới" "bảng biểu"** và **" 'mở rộng' " "góc nhìn" dữ liệu** từ "một
      bảng" "riêng lẻ" sang **" 'toàn cảnh' " "mạng lưới" dữ liệu "quan hệ"** giữa các bảng.

- **" 'Mục Đích' " Của Joins - " 'Khai Thác' " "Mối Quan Hệ" Giữa Các Bảng:**

    - **"Lấy" Dữ Liệu "Liên Quan" Từ "Nhiều Bảng":** "Kết hợp" dữ liệu từ các bảng "khác nhau" có "mối quan hệ" để "
      lấy" "thông tin" "hoàn chỉnh" và "đa dạng" hơn. (Ví dụ: "lấy" "tên sản phẩm" từ bảng `SanPhams` và "tên danh mục"
      từ bảng `DanhMucs` để "hiển thị" "danh sách sản phẩm" kèm theo "danh mục" của chúng).
    - **"Phân Tích" Dữ Liệu "Đa Chiều":** "Phân tích" dữ liệu "theo nhiều chiều" bằng cách "kết hợp" dữ liệu từ các
      bảng "khác nhau" và "thực hiện" các phép "tính toán" "tổng hợp" (aggregate functions) trên dữ liệu "đã kết hợp". (
      Ví dụ: "tính tổng" "doanh thu" "theo từng danh mục sản phẩm", "tính trung bình" "đánh giá" sản phẩm "theo từng nhà
      sản xuất", v.v.).
    - **"Tạo Báo Cáo" "Phức Tạp":** "Tạo" các "báo cáo" dữ liệu "phức tạp" "dựa trên" dữ liệu từ "nhiều bảng" "liên
      quan". (Ví dụ: "báo cáo" "đơn hàng" "chi tiết" "bao gồm" "thông tin" "đơn hàng", "thông tin" "khách hàng", và "
      danh sách" "sản phẩm" trong đơn hàng).

- **"Các 'Loại' " Joins SQL "Phổ Biến":**

    - **`INNER JOIN` (Kết Nối Trong):** "Lấy" các bản ghi (rows) **"khớp nhau"** (matching rows) từ **"cả hai bảng"**
      dựa trên "điều kiện" "kết nối" (join condition). "Chỉ trả về" các bản ghi có "khóa" "khớp nhau" ở "cả hai bảng".

    - **`LEFT JOIN` (Kết Nối Trái) (hoặc `LEFT OUTER JOIN`):** "Lấy" **"tất cả" các bản ghi** (rows) từ **"bảng bên
      trái"** (left table) và các bản ghi **"khớp nhau"** (matching rows) từ **"bảng bên phải"** (right table) dựa
      trên "điều kiện" "kết nối". Nếu "không có" bản ghi "khớp nhau" ở "bảng bên phải", các cột của "bảng bên phải"
      trong kết quả sẽ có giá trị `NULL`.

    - **`RIGHT JOIN` (Kết Nối Phải) (hoặc `RIGHT OUTER JOIN`):** "Tương tự" `LEFT JOIN`, nhưng "ngược lại". "Lấy" **"tất
      cả" các bản ghi** (rows) từ **"bảng bên phải"** (right table) và các bản ghi **"khớp nhau"** (matching rows) từ *
      *"bảng bên trái"** (left table). Nếu "không có" bản ghi "khớp nhau" ở "bảng bên trái", các cột của "bảng bên trái"
      trong kết quả sẽ có giá trị `NULL`.

    - **`FULL OUTER JOIN` (Kết Nối Ngoài Toàn Phần):** "Lấy" **"tất cả" các bản ghi** (rows) từ **"cả hai bảng"** (bảng
      bên trái và bảng bên phải) - **"bao gồm"** cả các bản ghi **"khớp nhau"** và các bản ghi **"không khớp nhau"**.
      Nếu "không có" bản ghi "khớp nhau" ở "bảng còn lại", các cột của "bảng còn lại" trong kết quả sẽ có giá trị
      `NULL`.

    - **`CROSS JOIN` (Kết Nối Tích Đề Các):** "Kết hợp" **"mọi bản ghi"** (every row) từ **"bảng bên trái"** với **"mọi
      bản ghi"** (every row) từ **"bảng bên phải"** (Cartesian product). "Không dùng" "điều kiện" "kết nối". "Trả về" *
      *"tích đề các"** (Cartesian product) của "hai bảng" - "số lượng" bản ghi kết quả thường rất "lớn" (tích của "số
      lượng" bản ghi của "hai bảng"). "Ít dùng" trong thực tế, thường "dùng" trong các trường hợp "đặc biệt" hoặc khi "
      kết hợp" với các mệnh đề "lọc" khác để "tạo ra" "tập dữ liệu" "đặc biệt".

**5.2. `INNER JOIN` - " 'Lấy' " Dữ Liệu "Khớp Nhau" Từ "Cả Hai Bảng" - " 'Giao Điểm' " Dữ Liệu "Quan Hệ"**

- **`INNER JOIN` (Kết Nối Trong) - " 'Chỉ Lấy' " "Phần Chung" Của "Hai Bảng":**

    - **`INNER JOIN`** là loại Join **"phổ biến"** và **"thường dùng"** nhất trong SQL.
    - `INNER JOIN` "lấy" các bản ghi (rows) **"khớp nhau"** (matching rows) từ **"cả hai bảng"** dựa trên **"điều
      kiện" "kết nối"** (join condition) đã "chỉ định". "Chỉ trả về" các bản ghi có **"khóa" "khớp nhau"** ở **"cả hai
      bảng"**. Các bản ghi "không khớp nhau" (không có "khóa" "tương ứng" ở "bảng còn lại") sẽ bị **"loại bỏ"** khỏi kết
      quả truy vấn.
    - `INNER JOIN` "tạo ra" **"giao điểm"** (intersection) của dữ liệu từ "hai bảng" - "chỉ lấy" "phần chung" của "hai
      bảng" dựa trên "mối quan hệ".

- **"Cú Pháp" `INNER JOIN` "Cơ Bản":**

  ```sql
  SELECT column_list  -- "Chọn" các cột từ "bảng 1" và "bảng 2" (tùy ý)
  FROM table1         -- Bảng "bên trái" (left table)
  INNER JOIN table2   -- Lệnh INNER JOIN - "kết nối" với bảng "bên phải" (right table)
      ON table1.join_column = table2.join_column; -- Mệnh đề ON - "điều kiện" "kết nối" (join condition)
  ```

    - **`INNER JOIN table2 ON table1.join_column = table2.join_column`:** "Cú pháp" "mấu chốt" của `INNER JOIN`.
        - **`INNER JOIN table2`:** "Chỉ định" **"bảng bên phải"** (right table) là `table2` để "kết nối" với bảng "bên
          trái" `table1`.
        - **`ON table1.join_column = table2.join_column`:** "Mệnh đề" **`ON`** "chỉ định" **"điều kiện" "kết nối"** (
          join condition). "Điều kiện" "kết nối" thường là **"so sánh" "bằng"** (equal) giữa **"khóa chính"** (primary
          key) của "bảng bên trái" (`table1.join_column`) và **"khóa ngoại"** (foreign key) của "bảng bên phải" (
          `table2.join_column`) (hoặc ngược lại). "Khóa chính" và "khóa ngoại" "thiết lập" **"mối quan hệ"** giữa "hai
          bảng".

- **"Ví Dụ" `INNER JOIN` - " 'Hỏi' " Database: " 'Cho Xem' " "Tên Sản Phẩm" và " 'Tên Danh Mục' " Của " "Tất Cả" "Sản
  Phẩm" (chỉ sản phẩm có "danh mục" - quan hệ Một-Nhiều giữa `DanhMucs` và `SanPhams`, bảng `SanPhams` có
  cột `DanhMucId` là khóa ngoại "tham chiếu" đến bảng `DanhMucs`):**

  ```sql
  SELECT SanPhams.TenSanPham, DanhMucs.TenDanhMuc  -- "Chọn" cột TenSanPham từ bảng SanPhams và cột TenDanhMuc từ bảng DanhMucs
  FROM SanPhams                                    -- Bảng "bên trái" (left table) - SanPhams
  INNER JOIN DanhMucs                                -- INNER JOIN với bảng "bên phải" (right table) - DanhMucs
      ON SanPhams.DanhMucId = DanhMucs.DanhMucId;    -- Mệnh đề ON - "điều kiện" "kết nối": cột DanhMucId của bảng SanPhams "bằng" cột DanhMucId của bảng DanhMucs
  ```

    - **"Giải thích"**: Câu truy vấn này sẽ "kết nối" bảng `SanPhams` và bảng `DanhMucs` dựa trên "mối quan hệ" "khóa
      ngoại" `DanhMucId` (cột `DanhMucId` trong bảng `SanPhams` "tham chiếu" đến cột `DanhMucId` trong bảng `DanhMucs`).
      `INNER JOIN` sẽ "lấy" các bản ghi "khớp nhau" từ **"cả hai bảng"** (chỉ "lấy" các sản phẩm có `DanhMucId` "tồn
      tại" trong bảng `DanhMucs` và "chỉ lấy" các danh mục có `DanhMucId` "được 'tham chiếu' " bởi ít nhất một sản phẩm
      trong bảng `SanPhams` - trong trường hợp quan hệ Một-Nhiều).

    - **"Kết quả"** truy vấn (ví dụ):

      | TenSanPham         | TenDanhMuc    |
              | ------------------ | ------------- |
      | Chuột không dây      | Điện tử       |
      | Bàn phím cơ         | Điện tử       |
      | Màn hình LCD        | Điện tử       |
      | Tai nghe Bluetooth   | Điện tử       |
      | Sách "Lập trình C#" | Sách         |
      | Sách "OOP"          | Sách         |
      | ...                | ...         |
        - "Kết quả" "trả về" "danh sách" các sản phẩm, mỗi sản phẩm "kèm theo" "tên danh mục" "tương ứng". "Chỉ" các sản
          phẩm có "danh mục" (có `DanhMucId` "khớp" với `DanhMucId` trong bảng `DanhMucs`) mới được "lấy" vào kết quả.

**5.3. `LEFT JOIN` (và `RIGHT JOIN`) - " 'Lấy' " "Tất Cả" Dữ Liệu Từ "Một Bảng" và Dữ Liệu "Khớp Nhau" Từ "Bảng Còn
Lại" - " 'Không Bỏ Sót' " Dữ Liệu Từ "Bảng 'Chính' "**

- **`LEFT JOIN` (Kết Nối Trái) - " 'Giữ Lại' " "Toàn Bộ" Dữ Liệu "Bảng Bên Trái" (Left Table) Dù Có "Khớp" Hay Không:**

    - **`LEFT JOIN`** (Kết Nối Trái), còn gọi là **`LEFT OUTER JOIN`**, là loại Join "mở rộng" hơn `INNER JOIN`.
    - `LEFT JOIN` "lấy" **"tất cả" các bản ghi** (rows) từ **"bảng bên trái"** (left table) (bảng được "chỉ định" trong
      mệnh đề `FROM`).
    - `LEFT JOIN` "kết hợp" với các bản ghi **"khớp nhau"** (matching rows) từ **"bảng bên phải"** (right table) dựa
      trên "điều kiện" "kết nối" (join condition).
    - **"Điểm 'khác biệt' " với `INNER JOIN`**: Nếu "không có" bản ghi **"khớp nhau"** (no matching row) ở **"bảng bên
      phải"** cho một bản ghi ở "bảng bên trái", `LEFT JOIN` vẫn **"giữ lại"** bản ghi đó từ "bảng bên trái" trong kết
      quả truy vấn, nhưng các cột của **"bảng bên phải"** trong bản ghi kết quả sẽ có giá trị **`NULL`**. `INNER JOIN`
      sẽ "loại bỏ" các bản ghi "không khớp nhau" từ "cả hai bảng".
    - `LEFT JOIN` "đảm bảo" **"không 'bỏ sót' " "dữ liệu" từ "bảng bên trái"** (left table) - "bảng 'chính' " mà bạn
      muốn "lấy" "toàn bộ" dữ liệu.

- **`RIGHT JOIN` (Kết Nối Phải) - " 'Đối Xứng' " Với `LEFT JOIN` - " 'Giữ Lại' " "Toàn Bộ" Dữ Liệu "Bảng Bên Phải" (
  Right Table) Dù Có "Khớp" Hay Không:**

    - **`RIGHT JOIN`** (Kết Nối Phải), còn gọi là **`RIGHT OUTER JOIN`**, là loại Join **"đối xứng"** với `LEFT JOIN`.
    - `RIGHT JOIN` "lấy" **"tất cả" các bản ghi** (rows) từ **"bảng bên phải"** (right table) (bảng được "chỉ định" sau
      `RIGHT JOIN`).
    - `RIGHT JOIN` "kết hợp" với các bản ghi **"khớp nhau"** (matching rows) từ **"bảng bên trái"** (left table) dựa
      trên "điều kiện" "kết nối" (join condition).
    - Nếu "không có" bản ghi **"khớp nhau"** (no matching row) ở **"bảng bên trái"**, `RIGHT JOIN` vẫn **"giữ lại"** bản
      ghi đó từ "bảng bên phải" trong kết quả truy vấn, nhưng các cột của **"bảng bên trái"** trong bản ghi kết quả sẽ
      có giá trị **`NULL`**.
    - `RIGHT JOIN` "đảm bảo" **"không 'bỏ sót' " "dữ liệu" từ "bảng bên phải"** (right table) - "bảng 'chính' " mà bạn
      muốn "lấy" "toàn bộ" dữ liệu.
    - `RIGHT JOIN` "ít 'phổ biến' " hơn `LEFT JOIN` trong thực tế. Hầu hết các bài toán "dùng" `RIGHT JOIN` đều có thể
      được "giải quyết" bằng `LEFT JOIN` bằng cách "đổi chỗ" "bảng bên trái" và "bảng bên phải".

- **"Cú Pháp" `LEFT JOIN` và `RIGHT JOIN` "Cơ Bản":**

  ```sql
  SELECT column_list  -- "Chọn" các cột từ "bảng bên trái" và "bảng bên phải" (tùy ý)
  FROM table1         -- Bảng "bên trái" (left table)
  LEFT JOIN table2    -- Lệnh LEFT JOIN - "kết nối" với bảng "bên phải" (right table)
      ON table1.join_column = table2.join_column; -- Mệnh đề ON - "điều kiện" "kết nối"

  SELECT column_list  -- "Chọn" các cột từ "bảng bên trái" và "bảng bên phải" (tùy ý)
  FROM table1         -- Bảng "bên trái" (left table)
  RIGHT JOIN table2   -- Lệnh RIGHT JOIN - "kết nối" với bảng "bên phải" (right table)
      ON table1.join_column = table2.join_column; -- Mệnh đề ON - "điều kiện" "kết nối"
  ```

    - Cú pháp `LEFT JOIN` và `RIGHT JOIN` "tương tự" `INNER JOIN`, chỉ "thay đổi" từ khóa `INNER JOIN` thành `LEFT JOIN`
      hoặc `RIGHT JOIN`.
    - **`LEFT JOIN table2`**: "Chỉ định" `LEFT JOIN` với bảng "bên phải" `table2`. Bảng `table1` là **"bảng bên trái"**.
    - **`RIGHT JOIN table2`**: "Chỉ định" `RIGHT JOIN` với bảng "bên phải" `table2`. Bảng `table1` là **"bảng bên trái"
      **.

- **"Ví Dụ" `LEFT JOIN` - " 'Hỏi' " Database: " 'Cho Xem' " "Tất Cả" "Danh Mục" (kể cả "danh mục" "chưa có" "sản phẩm"
  nào) và " 'Tên Sản Phẩm' " "Tương Ứng" (nếu có) Từ Bảng `DanhMucs` và `SanPhams` (quan hệ Một-Nhiều, `DanhMucId` là
  khóa ngoại trong `SanPhams`):**

  ```sql
  SELECT DanhMucs.TenDanhMuc, SanPhams.TenSanPham  -- "Chọn" cột TenDanhMuc từ bảng DanhMucs và cột TenSanPham từ bảng SanPhams
  FROM DanhMucs                                    -- Bảng "bên trái" (left table) - DanhMucs
  LEFT JOIN SanPhams                                -- LEFT JOIN với bảng "bên phải" (right table) - SanPhams
      ON DanhMucs.DanhMucId = SanPhams.DanhMucId;    -- Mệnh đề ON - "điều kiện" "kết nối": cột DanhMucId của bảng DanhMucs "bằng" cột DanhMucId của bảng SanPhams
  ```

    - **"Giải thích"**: Câu truy vấn này sẽ `LEFT JOIN` bảng `DanhMucs` (bảng "bên trái") và bảng `SanPhams` (bảng "bên
      phải") dựa trên "mối quan hệ" "khóa ngoại" `DanhMucId`. `LEFT JOIN` sẽ "lấy" **"tất cả" các bản ghi** từ **"
      bảng `DanhMucs`"** (danh mục), **"kể cả"** các danh mục **"chưa có" "sản phẩm"** nào trong bảng `SanPhams`. Với
      mỗi danh mục, `LEFT JOIN` sẽ "tìm" các sản phẩm **"khớp nhau"** (matching products) trong bảng `SanPhams` (có cùng
      `DanhMucId`) và "kết hợp" dữ liệu. Nếu một danh mục **"không có" "sản phẩm" "khớp nhau"**, các cột của **"
      bảng `SanPhams`"** trong kết quả sẽ có giá trị **`NULL`** (ví dụ: `TenSanPham` sẽ là `NULL` cho các danh mục "
      không có" sản phẩm).

    - **"Kết quả"** truy vấn (ví dụ):

      | TenDanhMuc    | TenSanPham         |
              | ------------- | ------------------ |
      | Điện tử       | Chuột không dây      |
      | Điện tử       | Bàn phím cơ         |
      | Điện tử       | Màn hình LCD        |
      | Điện tử       | Tai nghe Bluetooth   |
      | Đồ gia dụng   | Nồi cơm điện       |
      | Đồ gia dụng   | Máy hút bụi        |
      | Đồ gia dụng   | Bàn ủi hơi nước    |
      | Nội thất      | Giường ngủ         |
      | Nội thất      | Bàn làm việc       |
      | Thời trang    | NULL               | -- Danh mục "Thời trang" "không có" sản phẩm nào trong bảng SanPhams, TenSanPham = NULL
      | Sách         | Sách "Lập trình C#" |
      | Sách         | Sách "OOP"          |
      | ...           | ...                |
        - "Kết quả" "trả về" **"tất cả" "danh mục"** (từ bảng `DanhMucs`), "kể cả" các danh mục "chưa có" sản phẩm nào (
          ví dụ: "Thời trang"). Với các danh mục "có" sản phẩm, kết quả "hiển thị" "tên danh mục" và "tên sản phẩm" "
          tương ứng". Với các danh mục "không có" sản phẩm, `TenSanPham` sẽ là `NULL`.

**5.4. `FULL OUTER JOIN` - " 'Lấy' " "Tất Cả" Dữ Liệu Từ "Cả Hai Bảng" (Khớp Nhau và Không Khớp Nhau) - " 'Không Bỏ
Quên' " "Ai Hết" - " 'Trọn Vẹn' " Dữ Liệu "Hai Bảng"**

- **`FULL OUTER JOIN` (Kết Nối Ngoài Toàn Phần) - " 'Lấy Hết' " "Mọi Thứ" Từ "Cả Hai Bảng":**

    - **`FULL OUTER JOIN`** (Kết Nối Ngoài Toàn Phần), còn gọi là **`FULL JOIN`**, là loại Join **" 'bao quát' " nhất**.
    - `FULL OUTER JOIN` "lấy" **"tất cả" các bản ghi** (rows) từ **"cả hai bảng"** (bảng bên trái và bảng bên phải) - *
      *"bao gồm"** cả các bản ghi **"khớp nhau"** (matching rows) và các bản ghi **"không khớp nhau"** (non-matching
      rows).
    - Nếu "không có" bản ghi **"khớp nhau"** (no matching row) ở **"bảng còn lại"**, các cột của **"bảng còn lại"**
      trong bản ghi kết quả sẽ có giá trị **`NULL`**.
    - `FULL OUTER JOIN` "tạo ra" **"hợp nhất"** (union) của dữ liệu từ "hai bảng" - "lấy" **"trọn vẹn"** dữ liệu từ "cả
      hai bảng", "không 'bỏ quên' " "ai hết".

- **"Cú Pháp" `FULL OUTER JOIN` "Cơ Bản":**

  ```sql
  SELECT column_list  -- "Chọn" các cột từ "bảng bên trái" và "bảng bên phải" (tùy ý)
  FROM table1         -- Bảng "bên trái" (left table)
  FULL OUTER JOIN table2 -- Lệnh FULL OUTER JOIN - "kết nối" với bảng "bên phải" (right table)
      ON table1.join_column = table2.join_column; -- Mệnh đề ON - "điều kiện" "kết nối"
  ```

    - Cú pháp `FULL OUTER JOIN` "tương tự" `INNER JOIN`, `LEFT JOIN`, và `RIGHT JOIN`, chỉ "thay đổi" từ khóa Join thành
      `FULL OUTER JOIN`.

- **"Ví Dụ" `FULL OUTER JOIN` - " 'Hỏi' " Database: " 'Cho Xem' " "Tất Cả" "Danh Mục" và "Tất Cả" "Sản Phẩm", " 'Kết
  Hợp' " "Thông Tin" (nếu có "quan hệ") Từ Bảng `DanhMucs` và `SanPhams` (quan hệ Một-Nhiều, `DanhMucId` là khóa ngoại
  trong `SanPhams`):**

  ```sql
  SELECT DanhMucs.TenDanhMuc, SanPhams.TenSanPham  -- "Chọn" cột TenDanhMuc từ bảng DanhMucs và cột TenSanPham từ bảng SanPhams
  FROM DanhMucs                                    -- Bảng "bên trái" (left table) - DanhMucs
  FULL OUTER JOIN SanPhams                            -- FULL OUTER JOIN với bảng "bên phải" (right table) - SanPhams
      ON DanhMucs.DanhMucId = SanPhams.DanhMucId;    -- Mệnh đề ON - "điều kiện" "kết nối": cột DanhMucId của bảng DanhMucs "bằng" cột DanhMucId của bảng SanPhams
  ```

    - **"Giải thích"**: Câu truy vấn này sẽ `FULL OUTER JOIN` bảng `DanhMucs` và bảng `SanPhams` dựa trên "mối quan
      hệ" "khóa ngoại" `DanhMucId`. `FULL OUTER JOIN` sẽ "lấy" **"tất cả" các bản ghi** từ **"cả hai bảng"** (danh mục
      và sản phẩm) - "bao gồm" cả các danh mục "chưa có" sản phẩm nào và các sản phẩm "không thuộc" danh mục nào (nếu có
      trường hợp sản phẩm "không có" `DanhMucId` hợp lệ).

    - **"Kết quả"** truy vấn (ví dụ):

      | TenDanhMuc    | TenSanPham         |
              | ------------- | ------------------ |
      | Điện tử       | Chuột không dây      |
      | Điện tử       | Bàn phím cơ         |
      | Điện tử       | Màn hình LCD        |
      | Điện tử       | Tai nghe Bluetooth   |
      | Đồ gia dụng   | Nồi cơm điện       |
      | Đồ gia dụng   | Máy hút bụi        |
      | Đồ gia dụng   | Bàn ủi hơi nước    |
      | Nội thất      | Giường ngủ         |
      | Nội thất      | Bàn làm việc       |
      | Thời trang    | NULL               | -- Danh mục "Thời trang" "không có" sản phẩm nào, TenSanPham = NULL
      | Sách         | Sách "Lập trình C#" |
      | Sách         | Sách "OOP"          |
      | NULL          | Sản phẩm "Lẻ Loi"    | -- Sản phẩm "Lẻ Loi" "không thuộc" danh mục nào, TenDanhMuc = NULL
      | ...           | ...                |
        - "Kết quả" "trả về" **"tất cả" "danh mục"** (từ bảng `DanhMucs`) và **"tất cả" "sản phẩm"** (từ bảng
          `SanPhams`). Với các danh mục và sản phẩm "có 'quan hệ' " (khớp nhau `DanhMucId`), kết quả "hiển thị" "tên
          danh mục" và "tên sản phẩm" "tương ứng". Với các danh mục "không có" sản phẩm nào, `TenSanPham` sẽ là `NULL`.
          Với các sản phẩm "không thuộc" danh mục nào, `TenDanhMuc` sẽ là `NULL`.

**5.5. "Thực Hành" Joins - " 'Khám Phá' " "Mối Quan Hệ" Giữa Các Bảng - " 'Gắn Kết' " Dữ Liệu "Thực Tế"**

- **"Bài Tập" "Thực Hành" - " 'Luyện Công Phu' " Joins Để " 'Khai Thác' " Dữ Liệu "Đa Bảng":**

    1. **"Lấy" "danh sách" "tất cả" "sản phẩm" và "danh mục" "tương ứng" của chúng (nếu có danh mục).** (Dùng
       `INNER JOIN` hoặc `LEFT JOIN` giữa `SanPhams` và `DanhMucs`).
    2. **"Lấy" "danh sách" "tất cả" "danh mục" và "số lượng sản phẩm" "thuộc mỗi danh mục".** (Dùng `LEFT JOIN`,
       `GROUP BY`, và `COUNT()` - "kết hợp" Joins với "kiến thức" Chương 4).
    3. **"Lấy" "danh sách" "sản phẩm" có "giá" "lớn hơn 1 triệu" và "thuộc" "danh mục" "Điện tử", "kèm theo" "tên danh
       mục" và "tên nhà cung cấp" (nếu có bảng `NhaCungCaps` (Suppliers) và "quan hệ" với `SanPhams`).** ( "Bài toán
       tổng hợp" - "thử thách" "kỹ năng" Joins và "lọc" "phức tạp").
    4. **"Tìm hiểu" và "thực hành" các loại Joins "khác" (ví dụ: `SELF JOIN` - kết nối bảng với chính nó, `CROSS JOIN` -
       kết nối tích đề các, `UNION JOIN` - kết hợp kết quả từ nhiều truy vấn).** ( "Nâng cao" "kiến thức" Joins "vượt
       xa" "cơ bản").

- **"Thực Hành" Với SQL Client Tool - " 'Gắn Kết' " Dữ Liệu và " 'Thấy' " "Sức Mạnh" Joins:**

    - "Mở" SQL client tool.
    - "Kết nối" đến database "mẫu" hoặc database "riêng" của bạn có "nhiều bảng" "quan hệ" (ví dụ: database "thương mại
      điện tử", database "quản lý bán hàng", v.v.).
    - "Mở" SQL editor và "viết" các câu truy vấn SQL "thực hành" cho từng "bài tập" trên, "dùng" các loại Joins khác
      nhau (`INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`).
    - "Chạy" các câu truy vấn và "xem" "kết quả" truy vấn (các "bảng" "kết hợp" dữ liệu từ "nhiều bảng", "khám phá" "mối
      quan hệ" giữa các bảng).
    - " 'Sáng tạo' ", " 'thử nghiệm' ", và " 'khám phá' " các "cách" "kết hợp" Joins với các mệnh đề SQL khác (`WHERE`,
      `ORDER BY`, `GROUP BY`, `HAVING`, v.v.) để "khai thác" "dữ liệu" "đa dạng" và "phong phú" từ database "quan hệ".

**Tổng Kết Chương 5:**

- Bạn đã "khám phá" **Joins**, " 'vũ khí' " "mạnh mẽ" để "kết hợp" dữ liệu từ "nhiều bảng" "quan hệ" trong SQL.
    - "Hiểu" **Joins là gì** ("phép kết nối" bảng, "gắn kết" dữ liệu "đa bảng").
    - "Nắm vững" các **"loại" Joins SQL "phổ biến"**: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN` và "
      khác biệt" giữa chúng.
    - Học cách "dùng" Joins để "lấy" dữ liệu "liên quan" từ "nhiều bảng" và "khai thác" "mối quan hệ" giữa các bảng.
    - "Thực hành" "viết" và "chạy" các câu truy vấn SQL "dùng" Joins để "luyện tập" và "khám phá" "sức mạnh" Joins
      trong "thực tế".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 6: Thao Tác Dữ Liệu (DML) - INSERT, UPDATE, DELETE - " 'Làm Chủ' " "Bảng Biểu" - " '
Thay Đổi' ", " 'Thêm' ", " 'Xóa' " Dữ Liệu**. Chúng ta sẽ "học cách" "dùng" các lệnh SQL **"Data Manipulation Language (
DML)"** (`INSERT`, `UPDATE`, `DELETE`) để **"thao tác"** với dữ liệu trong database - "thêm" dữ liệu mới, "sửa đổi" dữ
liệu đã có, và "xóa" dữ liệu "không cần thiết".

Bạn có câu hỏi nào về Joins này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn
trên con đường "chinh phục" SQL.
