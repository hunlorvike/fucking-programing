# Chương 6: Thao Tác Dữ Liệu (DML) - INSERT, UPDATE, DELETE - " 'Làm Chủ' " "Bảng Biểu" - " 'Thay Đổi' ", " 'Thêm' ", " 'Xóa' " Dữ Liệu - " 'Quyền Năng' " "Biến Đổi" "Nội Dung" Database

Chào mừng bạn đến với **Chương 6: Thao Tác Dữ Liệu (DML) - INSERT, UPDATE, DELETE**! Trong chương này, chúng ta sẽ "khám
phá" các lệnh SQL **"Data Manipulation Language (DML)"**, "bộ ba" lệnh **`INSERT`**, **`UPDATE`**, và **`DELETE`**, "cho
phép" bạn **"thao tác"** trực tiếp với **"dữ liệu"** trong database - "thêm" dữ liệu mới, "sửa đổi" dữ liệu đã có, và "
xóa" dữ liệu "không cần thiết". "DML" trao cho bạn **"quyền năng"** "thực sự" **"biến đổi" "nội dung" database**, "làm
chủ" "bảng biểu" và "dữ liệu" của mình.

**Phần 6: Thao Tác Dữ Liệu (DML) - INSERT, UPDATE, DELETE - " 'Làm Chủ' " "Bảng Biểu"**

**6.1. Lệnh `INSERT` - " 'Thêm' " Dữ Liệu Mới Vào Bảng - " 'Gieo Mầm' " Bản Ghi Mới Vào " 'Vườn' " Database**

- **Lệnh `INSERT` - " 'Sinh Ra' " Dữ Liệu Mới Trong Bảng:**

    - **Lệnh `INSERT`** là lệnh SQL "dùng" để **"thêm"** (insert) **"một hoặc nhiều bản ghi"** (rows) **"mới"** vào một
      **"bảng"** (table) trong database.
    - `INSERT` "cho phép" bạn **"bổ sung"** thêm dữ liệu vào database, " 'gieo mầm' " các bản ghi "mới" vào " 'vườn' "
      database của bạn.

- **"Cú Pháp" Lệnh `INSERT` "Cơ Bản" - "Thêm Một Bản Ghi":**

  ```sql
  INSERT INTO table_name (column1, column2, ..., columnN) -- "Chỉ định" "bảng" và "các cột" muốn "thêm" dữ liệu
  VALUES (value1, value2, ..., valueN);                  -- "Chỉ định" "giá trị" cho "từng cột"
  ```

    - **`INSERT INTO table_name (column1, column2, ..., columnN)`:** "Chỉ định" **"tên bảng"** (table name) mà bạn
      muốn "thêm" dữ liệu vào (`table_name`) và **"danh sách các cột"** (column list) mà bạn muốn "thêm" dữ liệu (
      `column1, column2, ..., columnN` ). "Thứ tự" các cột "liệt kê" phải "tương ứng" với "thứ tự" các giá trị trong
      mệnh đề `VALUES`. Nếu bạn muốn "thêm" dữ liệu vào **"tất cả" các cột** của bảng (theo "thứ tự" các cột trong
      bảng), bạn có thể "bỏ qua" "danh sách các cột" ( `INSERT INTO table_name VALUES (...)` - xem ví dụ sau).
    - **`VALUES (value1, value2, ..., valueN)`:** "Chỉ định" **"danh sách các giá trị"** (value list) cho **"từng cột"**
      đã "liệt kê" trong mệnh đề `INSERT INTO (...)`. "Thứ tự" các giá trị phải "tương ứng" với "thứ tự" các cột đã "
      liệt kê". "Kiểu dữ liệu" của các giá trị phải "tương thích" với "kiểu dữ liệu" của các cột "tương ứng".

- **"Ví Dụ" Lệnh `INSERT` - " 'Thêm' " "Sản Phẩm Mới" Vào Bảng `SanPhams`:**

  ```sql
  INSERT INTO SanPhams (TenSanPham, Gia, DanhMucSanPham)  -- "Thêm" dữ liệu vào bảng SanPhams, "chỉ định" các cột TenSanPham, Gia, DanhMucSanPham
  VALUES ('Màn hình cong Samsung', 8500000, 'Điện tử');   -- "Giá trị" cho từng cột: TenSanPham = 'Màn hình cong Samsung', Gia = 8500000, DanhMucSanPham = 'Điện tử'
  ```

    - Câu lệnh này sẽ "thêm" một **"bản ghi" "mới"** vào bảng `SanPhams` với các giá trị:
        - `TenSanPham`: "Màn hình cong Samsung"
        - `Gia`: 8500000
        - `DanhMucSanPham`: "Điện tử"
        - Giá trị cho cột `SanPhamId` (khóa chính) sẽ được database "tự động" "tạo ra" (nếu cột `SanPhamId` được "cấu
          hình" là `AUTO_INCREMENT` hoặc `IDENTITY`).

- **"Cú Pháp" Lệnh `INSERT` - "Thêm Nhiều Bản Ghi Cùng Lúc":**

  ```sql
  INSERT INTO table_name (column1, column2, ..., columnN) -- "Chỉ định" "bảng" và "các cột"
  VALUES (value1_row1, value2_row1, ..., valueN_row1),  -- "Giá trị" cho bản ghi thứ nhất
         (value1_row2, value2_row2, ..., valueN_row2),  -- "Giá trị" cho bản ghi thứ hai
         ...
         (value1_rowM, value2_rowM, ..., valueN_rowM);  -- "Giá trị" cho bản ghi thứ M
  ```

    - Bạn có thể "thêm" **"nhiều bản ghi"** (rows) "cùng lúc" bằng cách "liệt kê" **"nhiều mệnh đề" `VALUES`**, **"cách
      nhau" bằng dấu phẩy (`,`)**. "Tiết kiệm" "hiệu năng" khi "thêm" "lượng lớn" dữ liệu vào database.

    - **"Ví dụ" - " 'Thêm' " "Ba Sản Phẩm Mới" Vào Bảng `SanPhams` "Cùng Lúc":**

      ```sql
      INSERT INTO SanPhams (TenSanPham, Gia, DanhMucSanPham)  -- "Thêm" dữ liệu vào bảng SanPhams, "chỉ định" các cột TenSanPham, Gia, DanhMucSanPham
      VALUES ('Máy tính bảng iPad Pro', 25000000, 'Điện tử'),  -- "Giá trị" cho bản ghi thứ nhất (sản phẩm 1)
             ('Máy hút bụi thông minh', 1200000, 'Đồ gia dụng'), -- "Giá trị" cho bản ghi thứ hai (sản phẩm 2)
             ('Bàn trà gỗ tự nhiên', 5000000, 'Nội thất');    -- "Giá trị" cho bản ghi thứ ba (sản phẩm 3)
      ```

- **"Cú Pháp" Lệnh `INSERT` - "Thêm Dữ Liệu Vào "Tất Cả" Các Cột (theo "Thứ Tự" Cột Trong Bảng)":**

  ```sql
  INSERT INTO table_name  -- "Chỉ định" "bảng" (không "chỉ định" "danh sách các cột")
  VALUES (value1, value2, ..., valueN); -- "Chỉ định" "giá trị" cho "tất cả" các cột (theo "thứ tự" cột trong bảng)
  ```

    - Nếu bạn muốn "thêm" dữ liệu vào **"tất cả" các cột** của bảng (và theo "thứ tự" các cột được "định nghĩa" trong
      bảng), bạn có thể "bỏ qua" "danh sách các cột" trong mệnh đề `INSERT INTO (...)` và "chỉ" "chỉ định" **"danh sách
      các giá trị"** trong mệnh đề `VALUES (...)`.
    - **"Lưu Ý"**: "Thứ tự" các giá trị trong `VALUES (...)` phải **"tuyệt đối" "chính xác"** "tương ứng" với "thứ tự"
      các cột trong bảng. "Dễ gây lỗi" nếu "không cẩn thận" hoặc khi bảng có "nhiều cột". "Nên" "dùng" cú pháp
      `INSERT INTO table_name (column1, column2, ..., columnN) VALUES (...)` (có "chỉ định" "danh sách các cột") để "
      code" SQL "rõ ràng" hơn và "tránh" "nhầm lẫn".

    - **"Ví dụ" - " 'Thêm' " "Sản Phẩm Mới" Vào Bảng `SanPhams` - "Thêm Dữ Liệu Vào "Tất Cả" Các Cột (theo "Thứ Tự" Cột
      Trong Bảng):**

      ```sql
      INSERT INTO SanPhams  -- "Thêm" dữ liệu vào bảng SanPhams (không "chỉ định" "danh sách các cột")
      VALUES (7, 'Máy hút ẩm Sharp', 4500000, 'Đồ gia dụng'); -- "Giá trị" cho "tất cả" các cột (theo "thứ tự" cột trong bảng SanPhams: SanPhamId, TenSanPham, Gia, DanhMucSanPham)
      ```

- **"Lưu Ý" Quan Trọng Khi Dùng Lệnh `INSERT`:**

    - **"Kiểu Dữ Liệu" "Tương Thích":** "Kiểu dữ liệu" của các **"giá trị"** trong mệnh đề `VALUES (...)` phải **"tương
      thích"** với "kiểu dữ liệu" của các **"cột"** "tương ứng" trong mệnh đề `INSERT INTO (...)`. Nếu "không tương
      thích", database sẽ "báo lỗi".
    - **"Ràng Buộc" (Constraints) Cột:** "Tuân thủ" các **"ràng buộc"** (constraints) được "định nghĩa" trên các cột (ví
      dụ: `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`, v.v.). Nếu "vi phạm" các "ràng buộc", database sẽ "từ chối" "
      thêm" bản ghi và "báo lỗi". (Ví dụ: "không thể" "thêm" bản ghi nếu cột `TenSanPham` được "định nghĩa" `NOT NULL`
      và bạn "không cung cấp" giá trị cho cột `TenSanPham`).
    - **"Khóa Chính" (Primary Key) "Tự Động" "Tăng" (Auto-Increment/Identity):** Nếu cột "khóa chính" (primary key) của
      bảng được "cấu hình" là **`AUTO_INCREMENT`** (MySQL, SQLite) hoặc **`IDENTITY`** (SQL Server, PostgreSQL), bạn **"
      không cần"** (và "không nên") "cung cấp" giá trị cho cột "khóa chính" khi "thêm" bản ghi. Database sẽ **"tự
      động" "tạo ra"** giá trị "khóa chính" "mới" cho bản ghi "mới" (thường là "tự động" "tăng" giá trị "khóa chính" "
      lớn nhất" hiện tại lên 1). Nếu bạn "cố tình" "cung cấp" giá trị cho cột "khóa chính" "tự động" "tăng", database có
      thể "báo lỗi" hoặc "ghi đè" giá trị "tự động" (tùy theo DBMS và cấu hình).
    - **"Transactions" (Giao Dịch):** Lệnh `INSERT` thường được "thực thi" trong một **"transaction"** (giao dịch) để "
      đảm bảo" "tính 'toàn vẹn' " dữ liệu (ACID properties). Nếu có "lỗi" trong quá trình `INSERT`, transaction có thể
      được **"rollback"** (hoàn tác) để "đảm bảo" database "không bị" "thay đổi" "không nhất quán". (Chúng ta sẽ "học"
      về Transactions ở Chương 8).

**6.2. Lệnh `UPDATE` - " 'Cập Nhật' " Dữ Liệu "Đã Có" Trong Bảng - " 'Chỉnh Sửa' " Bản Ghi "Đã Tồn Tại"**

- **Lệnh `UPDATE` - " 'Thay Đổi' " Dữ Liệu "Đã "Cũ" " Thành Dữ Liệu " "Mới" ":**

    - **Lệnh `UPDATE`** là lệnh SQL "dùng" để **"cập nhật"** (update) (sửa đổi) **"dữ liệu"** của **"một hoặc nhiều bản
      ghi"** (rows) **"đã có"** trong một **"bảng"** (table) trong database.
    - `UPDATE` "cho phép" bạn **" 'chỉnh sửa' "** các bản ghi "đã tồn tại" trong database, " 'thay áo mới' " cho dữ
      liệu "đã 'cũ' " thành dữ liệu " 'mới' " "cập nhật".

- **"Cú Pháp" Lệnh `UPDATE` "Cơ Bản":**

  ```sql
  UPDATE table_name          -- "Chỉ định" "bảng" muốn "cập nhật"
  SET column1 = new_value1,   -- "Set" giá trị "mới" cho cột 1
      column2 = new_value2,   -- "Set" giá trị "mới" cho cột 2
      ...,
      columnN = new_valueN     -- "Set" giá trị "mới" cho cột N
  WHERE condition;          -- Mệnh đề WHERE - "điều kiện" "lọc" bản ghi muốn "cập nhật"
  ```

    - **`UPDATE table_name`:** "Chỉ định" **"tên bảng"** (table name) mà bạn muốn "cập nhật" dữ liệu trong đó.
    - **`SET column1 = new_value1, column2 = new_value2, ..., columnN = new_valueN`:** "Chỉ định" **"danh sách các cột"
      ** (column list) mà bạn muốn "cập nhật" giá trị và **"giá trị" "mới"** (new values) cho từng cột. "Cột" và "giá
      trị" được "phân tách" bằng dấu bằng (`=`) và các cặp "cột = giá trị" được "cách nhau" bằng dấu phẩy (`,`).
    - **`WHERE condition`:** Mệnh đề **`WHERE`** (tùy chọn) để **"lọc"** (filter) **"các bản ghi"** (rows) mà bạn muốn *
      *"cập nhật"**. "Chỉ" những bản ghi mà "điều kiện" `WHERE` "trả về" `TRUE` mới được "cập nhật". Nếu bạn **"bỏ qua"
      ** mệnh đề `WHERE`, lệnh `UPDATE` sẽ "cập nhật" **"tất cả"** các bản ghi trong bảng ( **"cực kỳ 'nguy hiểm' " - "
      cẩn thận" khi "bỏ qua" mệnh đề `WHERE`**).

- **"Ví Dụ" Lệnh `UPDATE` - " 'Cập Nhật' " "Giá" Của " "Sản Phẩm" Có " 'SanPhamId' " Là 1 Trong Bảng `SanPhams`:**

  ```sql
  UPDATE SanPhams          -- "Cập nhật" bảng SanPhams
  SET Gia = 300000         -- "Set" cột Gia = 300000 (giá mới)
  WHERE SanPhamId = 1;      -- "Lọc" bản ghi có SanPhamId = 1 (chỉ "cập nhật" sản phẩm có ID là 1)
  ```

    - Câu lệnh này sẽ "cập nhật" **"cột `Gia`"** của bản ghi có `SanPhamId` là `1` trong bảng `SanPhams` thành giá trị *
      *`300000`**. Các cột khác của bản ghi này sẽ **"không bị" "thay đổi"**.

- **"Cập Nhật" "Nhiều Cột" Cùng Lúc:** Bạn có thể "cập nhật" **"nhiều cột"** "cùng lúc" trong một lệnh `UPDATE` bằng
  cách "liệt kê" **"nhiều cặp" `column = new_value`** trong mệnh đề `SET`, **"cách nhau" bằng dấu phẩy (`,`)**.

    - **"Ví dụ" - " 'Cập Nhật' " "Giá" và " 'Danh Mục Sản Phẩm' " Của " "Sản Phẩm" Có " 'SanPhamId' " Là 2 Trong
      Bảng `SanPhams`:**

      ```sql
      UPDATE SanPhams          -- "Cập nhật" bảng SanPhams
      SET Gia = 1600000,      -- "Set" cột Gia = 1600000 (giá mới)
          DanhMucSanPham = 'Điện thoại' -- "Set" cột DanhMucSanPham = 'Điện thoại' (danh mục mới)
      WHERE SanPhamId = 2;      -- "Lọc" bản ghi có SanPhamId = 2 (chỉ "cập nhật" sản phẩm có ID là 2)
      ```

- **"Lưu Ý" Quan Trọng Khi Dùng Lệnh `UPDATE`:**

    - **Mệnh Đề `WHERE` "Cực Kỳ Quan Trọng":** **"Luôn 'dùng' " mệnh đề `WHERE`** để "lọc" "các bản ghi" muốn "cập nhật"
      khi "thực hiện" lệnh `UPDATE`. Nếu bạn **"bỏ qua"** mệnh đề `WHERE`, lệnh `UPDATE` sẽ "cập nhật" **"tất cả" các
      bản ghi** trong bảng ( **"cực kỳ 'nguy hiểm' " - "dữ liệu có thể bị 'cập nhật' " "ngoài ý muốn"**).
    - **"Kiểu Dữ Liệu" "Tương Thích":** "Kiểu dữ liệu" của **"giá trị" "mới"** trong mệnh đề `SET` phải **"tương thích"
      ** với "kiểu dữ liệu" của **"cột"** "tương ứng". Nếu "không tương thích", database sẽ "báo lỗi".
    - **"Ràng Buộc" (Constraints) Cột:** "Tuân thủ" các **"ràng buộc"** (constraints) được "định nghĩa" trên các cột (ví
      dụ: `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`, v.v.) khi "cập nhật" dữ liệu. Nếu "vi phạm" các "ràng buộc",
      database sẽ "từ chối" "cập nhật" bản ghi và "báo lỗi". (Ví dụ: "không thể" "cập nhật" cột `TenSanPham` thành
      `NULL` nếu cột `TenSanPham` được "định nghĩa" `NOT NULL`).
    - **"Transactions" (Giao Dịch):** Lệnh `UPDATE` thường được "thực thi" trong một **"transaction"** (giao dịch) để "
      đảm bảo" "tính 'toàn vẹn' " dữ liệu (ACID properties). Nếu có "lỗi" trong quá trình `UPDATE`, transaction có thể
      được **"rollback"** (hoàn tác) để "đảm bảo" database "không bị" "thay đổi" "không nhất quán". (Chúng ta sẽ "học"
      về Transactions ở Chương 8).

**6.3. Lệnh `DELETE` - " 'Xóa' " Dữ Liệu Không Cần Thiết Khỏi Bảng - " 'Dọn Dẹp' " "Rác" Dữ Liệu Trong Database**

- **Lệnh `DELETE` - " 'Khử' " Dữ Liệu "Không Mong Muốn" - " 'Dọn Dẹp' " "Vườn' " Database:**

    - **Lệnh `DELETE`** là lệnh SQL "dùng" để **"xóa"** (delete) **"một hoặc nhiều bản ghi"** (rows) **"không cần thiết"
      ** hoặc **"không mong muốn"** khỏi một **"bảng"** (table) trong database.
    - `DELETE` "cho phép" bạn **" 'dọn dẹp' " "rác" dữ liệu** trong database, "giữ" database "gọn gàng", "sạch sẽ", và "
      tối ưu" "hiệu năng".

- **"Cú Pháp" Lệnh `DELETE` "Cơ Bản":**

  ```sql
  DELETE FROM table_name  -- "Chỉ định" "bảng" muốn "xóa" dữ liệu
  WHERE condition;          -- Mệnh đề WHERE - "điều kiện" "lọc" bản ghi muốn "xóa"
  ```

    - **`DELETE FROM table_name`:** "Chỉ định" **"tên bảng"** (table name) mà bạn muốn "xóa" dữ liệu khỏi đó.
    - **`WHERE condition`:** Mệnh đề **`WHERE`** (tùy chọn) để **"lọc"** (filter) **"các bản ghi"** (rows) mà bạn muốn *
      *"xóa"**. "Chỉ" những bản ghi mà "điều kiện" `WHERE` "trả về" `TRUE` mới bị "xóa". Nếu bạn **"bỏ qua"** mệnh đề
      `WHERE`, lệnh `DELETE` sẽ **"xóa" "tất cả" các bản ghi** trong bảng ( **"cực kỳ 'nguy hiểm' " - "dữ liệu có thể
      bị 'xóa sạch' " "ngoài ý muốn"**).

- **"Ví Dụ" Lệnh `DELETE` - " 'Xóa' " "Sản Phẩm" Có " 'SanPhamId' " Là 7 Khỏi Bảng `SanPhams`:**

  ```sql
  DELETE FROM SanPhams  -- "Xóa" dữ liệu khỏi bảng SanPhams
  WHERE SanPhamId = 7;      -- "Lọc" bản ghi có SanPhamId = 7 (chỉ "xóa" sản phẩm có ID là 7)
  ```

    - Câu lệnh này sẽ "xóa" **"bản ghi"** có `SanPhamId` là `7` khỏi bảng `SanPhams`. Các bản ghi khác trong bảng
      `SanPhams` sẽ **"không bị" "ảnh hưởng"**.

- **"Xóa" "Tất Cả" Bản Ghi Trong Bảng ( " 'Dọn Sạch' " Bảng):** Để "xóa" **"tất cả" các bản ghi** (all rows) trong một
  bảng ( "dọn sạch" bảng), bạn có thể "dùng" lệnh `DELETE` **"không có" mệnh đề `WHERE`** ( **"cực kỳ 'nguy hiểm' " - "
  cẩn thận" khi "xóa" "toàn bộ" bảng**):

  ```sql
  DELETE FROM table_name; -- "Xóa" dữ liệu khỏi bảng (không có mệnh đề WHERE - "xóa" "tất cả" bản ghi)
  ```

    - **"Ví dụ" - " 'Xóa Sạch' " "Tất Cả" "Sản Phẩm" Trong Bảng `SanPhams`:**

      ```sql
      DELETE FROM SanPhams; -- "Xóa" dữ liệu khỏi bảng SanPhams (không có mệnh đề WHERE - "xóa" "tất cả" bản ghi)
      ```

- **"Lưu Ý" Quan Trọng Khi Dùng Lệnh `DELETE`:**

    - **Mệnh Đề `WHERE` "Cực Kỳ Quan Trọng":** **"Luôn 'dùng' " mệnh đề `WHERE`** để "lọc" "các bản ghi" muốn "xóa"
      khi "thực hiện" lệnh `DELETE`. Nếu bạn **"bỏ qua"** mệnh đề `WHERE`, lệnh `DELETE` sẽ **"xóa" "tất cả" các bản ghi
      ** trong bảng ( **"cực kỳ 'nguy hiểm' " - "dữ liệu có thể bị 'xóa sạch' " "vĩnh viễn"**). **"Không có 'undo' " cho
      lệnh `DELETE` "không có" `WHERE` clause**.
    - **"Xóa Dữ Liệu Là "Hành Động" "Vĩnh Viễn" (Permanent Action):** Lệnh `DELETE` **"xóa"** dữ liệu **"vĩnh viễn"**
      khỏi database (trừ khi bạn "rollback" transaction - xem phần sau). **"Không thể" "khôi phục"** dữ liệu đã "xóa"
      bằng lệnh `DELETE` (trừ khi bạn có "backup" database). **"Cẩn thận"** khi "dùng" lệnh `DELETE` và **"kiểm tra" "
      kỹ" "điều kiện" `WHERE`** trước khi "chạy" lệnh.
    - **"Khóa Ngoại" (Foreign Key) "Ràng Buộc" (Constraints):** Nếu bảng bạn muốn "xóa" dữ liệu có **"khóa ngoại"** (
      foreign key) "tham chiếu" đến bảng khác, bạn có thể gặp **"lỗi" "ràng buộc"** (foreign key constraint violation)
      nếu bạn "xóa" bản ghi ở bảng "cha" mà vẫn còn các bản ghi "con" "tham chiếu" đến bản ghi đó. "Cần" "xóa" các bản
      ghi "con" "trước" hoặc "thiết lập" **`ON DELETE CASCADE`** "ràng buộc" khóa ngoại (để database "tự động" "xóa" các
      bản ghi "con" khi "xóa" bản ghi "cha").
    - **"Transactions" (Giao Dịch):** Lệnh `DELETE` thường được "thực thi" trong một **"transaction"** (giao dịch) để "
      đảm bảo" "tính 'toàn vẹn' " dữ liệu (ACID properties). Nếu có "lỗi" trong quá trình `DELETE`, transaction có thể
      được **"rollback"** (hoàn tác) để "đảm bảo" database "không bị" "thay đổi" "không nhất quán". (Chúng ta sẽ "học"
      về Transactions ở Chương 8).

**Tổng Kết Chương 6:**

- Bạn đã "làm chủ" các lệnh SQL **Data Manipulation Language (DML)** để "thao tác" dữ liệu trong database:
    - "Nắm vững" lệnh **`INSERT`** ("thêm" dữ liệu mới).
    - "Hiểu" lệnh **`UPDATE`** ("cập nhật" dữ liệu đã có).
    - "Làm chủ" lệnh **`DELETE`** ("xóa" dữ liệu "không cần thiết").
    - "Lưu ý" các "điểm quan trọng" khi "dùng" các lệnh DML (mệnh đề `WHERE` "cẩn thận", "kiểu dữ liệu", "ràng buộc", "
      transactions").

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 7: Định Nghĩa Dữ Liệu (DDL) - CREATE, ALTER, DROP (TABLE, DATABASE) - " 'Xây Dựng' "
và " 'Quản Lý' " Cấu Trúc Database**. Chúng ta sẽ "khám phá" các lệnh SQL **Data Definition Language (DDL)** (`CREATE`,
`ALTER`, `DROP`) để **"định nghĩa"** và **"quản lý"** "cấu trúc" database - "tạo" database, "tạo" bảng, "sửa đổi" bảng,
và "xóa" bảng.

Bạn có câu hỏi nào về các lệnh thao tác dữ liệu (DML) này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải
đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" SQL.
