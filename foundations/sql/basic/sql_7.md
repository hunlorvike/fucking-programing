# Chương 7: Định Nghĩa Dữ Liệu (DDL) - CREATE, ALTER, DROP (TABLE, DATABASE) - " 'Xây Dựng' " và " 'Quản Lý' " Cấu Trúc Database - " 'Quyền Năng' " "Kiến Tạo" và " 'Biến Đổi' " "Hình Hài" Database

Chào mừng bạn đến với **Chương 7: Định Nghĩa Dữ Liệu (DDL) - CREATE, ALTER, DROP (TABLE, DATABASE)**! Trong chương này,
chúng ta sẽ "khám phá" các lệnh SQL **"Data Definition Language (DDL)"**, "bộ ba" lệnh **`CREATE`**, **`ALTER`**, và *
*`DROP`**, "cho phép" bạn **"định nghĩa"** và **"quản lý"** **"cấu trúc" database** - "tạo" database mới, "tạo" bảng
mới, "sửa đổi" cấu trúc bảng, và "xóa" bảng "không cần thiết". "DDL" trao cho bạn **"quyền năng"** "tối thượng" để **"
kiến tạo"** và **"biến đổi" "hình hài" database**, "xây dựng" "nền móng" vững chắc cho ứng dụng dữ liệu của bạn.

**Phần 7: Định Nghĩa Dữ Liệu (DDL) - CREATE, ALTER, DROP (TABLE, DATABASE) - " 'Xây Dựng' " và " 'Quản Lý' " Cấu Trúc
Database**

**7.1. Lệnh `CREATE TABLE` - " 'Tạo' " Bảng Mới Trong Database - " 'Đặt Viên Gạch Đầu Tiên' " Cho " 'Ngôi Nhà' " Dữ Liệu
**

- **Lệnh `CREATE TABLE` - " 'Sinh Ra' " "Bảng Mới" Trong Database:**

    - **Lệnh `CREATE TABLE`** là lệnh SQL "dùng" để **"tạo"** (create) một **"bảng"** (table) **"mới"** trong database.
    - `CREATE TABLE` "cho phép" bạn **" 'vẽ' " "bản thiết kế"** (schema) cho bảng - "xác định" **"tên bảng"**, **"danh
      sách các cột"**, **"kiểu dữ liệu"** của từng cột, và **"các ràng buộc"** (constraints) cho các cột và bảng. "Đặt
      viên gạch đầu tiên" để "xây dựng" "ngôi nhà" dữ liệu của bạn.

- **"Cú Pháp" Lệnh `CREATE TABLE` "Cơ Bản":**

  ```sql
  CREATE TABLE table_name ( -- "Ra lệnh" "tạo" bảng mới có tên "table_name"
      column1 datatype1 [column_constraint1], -- "Định nghĩa" cột 1: tên cột, kiểu dữ liệu, và ràng buộc (tùy chọn)
      column2 datatype2 [column_constraint2], -- "Định nghĩa" cột 2: tên cột, kiểu dữ liệu, và ràng buộc (tùy chọn)
      ...,
      columnN datatypeN [column_constraintN], -- "Định nghĩa" cột N: tên cột, kiểu dữ liệu, và ràng buộc (tùy chọn)
      [table_constraint1],                    -- "Định nghĩa" ràng buộc "bảng" (tùy chọn)
      [table_constraint2],                    -- "Định nghĩa" ràng buộc "bảng" (tùy chọn)
      ...
      [table_constraintM]                     -- "Định nghĩa" ràng buộc "bảng" (tùy chọn)
  );
  ```

    - **`CREATE TABLE table_name`:** "Ra lệnh" cho database là "hãy 'tạo' một bảng mới" có **"tên bảng"** (table name)
      là `table_name`. "Tên bảng" phải **"duy nhất"** trong database.
    - **`(column1 datatype1 [column_constraint1], ...)`:** "Định nghĩa" **"cấu trúc"** của bảng - **"danh sách các cột"
      ** (column list) và các "thuộc tính" của từng cột:
        - **`column1`, `column2`, ..., `columnN`:** "Tên cột" (column names) - "đặt tên" cho từng cột trong bảng. "Tên
          cột" phải **"duy nhất"** trong bảng.
        - **`datatype1`, `datatype2`, ..., `datatypeN`:** **"Kiểu dữ liệu"** (data type) của từng cột. "Xác định" "loại
          dữ liệu" mà cột sẽ "lưu trữ" (ví dụ: `INT` - số nguyên, `VARCHAR(255)` - chuỗi ký tự có độ dài tối đa 255,
          `DECIMAL(10, 2)` - số thập phân có độ chính xác 10 chữ số và 2 chữ số thập phân, `DATE` - ngày tháng,
          `BOOLEAN` - boolean, v.v.). "Chọn" "kiểu dữ liệu" "phù hợp" với "loại dữ liệu" mà bạn muốn "lưu trữ" trong
          cột. Các RDBMSs "khác nhau" có thể "hỗ trợ" các "kiểu dữ liệu" "khác nhau" (SQL Dialects - Chương 1).
        - **`[column_constraint1]`, `[column_constraint2]`, ..., `[column_constraintN]`:** **"Ràng buộc" cột** (column
          constraints) (tùy chọn) - "quy định" **"ràng buộc"** và **"quy tắc"** cho dữ liệu trong cột đó (ví dụ:
          `NOT NULL` - "không cho phép" giá trị `NULL`, `UNIQUE` - "đảm bảo" giá trị "duy nhất", `PRIMARY KEY` - "xác
          định" cột là "khóa chính", `FOREIGN KEY` - "xác định" cột là "khóa ngoại", `CHECK (condition)` - "kiểm tra" "
          điều kiện" "tùy chỉnh", v.v.). "Đảm bảo" **"tính 'toàn vẹn' " (integrity)** và **"tính 'chính xác' " (
          accuracy)** của dữ liệu trong cột.

    - **`[table_constraint1]`, `[table_constraint2]`, ..., `[table_constraintM]`:** **"Ràng buộc" bảng** (table
      constraints) (tùy chọn) - "quy định" **"ràng buộc"** và **"quy tắc"** cho **"toàn bộ" bảng** (ví dụ:
      `PRIMARY KEY (column1, column2, ...)` - "xác định" "khóa chính" "kết hợp" (composite primary key) gồm nhiều cột,
      `FOREIGN KEY (column_name) REFERENCES another_table(another_column)` - "xác định" "khóa ngoại" "tham chiếu" đến
      bảng khác, `UNIQUE (column1, column2, ...)` - "đảm bảo" "tổ hợp" giá trị của nhiều cột là "duy nhất",
      `CHECK (condition)` - "kiểm tra" "điều kiện" "tùy chỉnh" cho "toàn bộ" bảng, v.v.). "Đảm bảo" **"tính 'toàn
      vẹn' " (integrity)** và **"mối quan hệ"** giữa các cột trong bảng.

- **"Ví Dụ" Lệnh `CREATE TABLE` - " 'Tạo' " Bảng `DanhMucs` (Categories) Trong Database "Mẫu":**

  ```sql
  CREATE TABLE DanhMucs (  -- "Tạo" bảng mới có tên "DanhMucs"
      DanhMucId INT PRIMARY KEY AUTO_INCREMENT, -- Cột "DanhMucId": kiểu INT, Khóa Chính (PRIMARY KEY), Tự Động Tăng (AUTO_INCREMENT) (MySQL syntax)
      TenDanhMuc VARCHAR(255) NOT NULL UNIQUE     -- Cột "TenDanhMuc": kiểu VARCHAR(255) (chuỗi ký tự tối đa 255), Bắt Buộc Nhập (NOT NULL), Giá Trị Duy Nhất (UNIQUE)
  );
  ```

    - **"Giải thích"**: Câu lệnh này sẽ "tạo" một bảng mới tên là **`DanhMucs`** (Categories) với "hai cột":
        - **`DanhMucId`**:
            - "Tên cột": `DanhMucId` (Category ID)
            - "Kiểu dữ liệu": `INT` (số nguyên)
            - "Ràng buộc cột":
                - `PRIMARY KEY`: "Xác định" cột `DanhMucId` là **"khóa chính"** của bảng `DanhMucs`. "Khóa chính" "đảm
                  bảo" mỗi bản ghi trong bảng có một "ID" "duy nhất" và "không NULL".
                - `AUTO_INCREMENT` (MySQL syntax): "Tự động" "tăng" giá trị "khóa chính" khi "thêm" bản ghi mới (
                  database sẽ "tự động" "gán" giá trị ID "mới" cho bản ghi "mới"). (Syntax "tự động" "tăng" có thể "khác
                  nhau" giữa các RDBMSs - ví dụ: `IDENTITY` trong SQL Server, `SERIAL` trong PostgreSQL, `AUTOINCREMENT`
                  trong SQLite).
        - **`TenDanhMuc`**:
            - "Tên cột": `TenDanhMuc` (Category Name)
            - "Kiểu dữ liệu": `VARCHAR(255)` (chuỗi ký tự có độ dài tối đa 255)
            - "Ràng buộc cột":
                - `NOT NULL`: "Bắt buộc" phải "nhập" giá trị cho cột `TenDanhMuc` khi "thêm" hoặc "cập nhật" bản ghi. "
                  Không cho phép" giá trị `NULL`.
                - `UNIQUE`: "Đảm bảo" các giá trị trong cột `TenDanhMuc` là **"duy nhất"** trong bảng. "Không cho
                  phép" "trùng lặp" giá trị `TenDanhMuc` giữa các bản ghi.

**7.2. Lệnh `ALTER TABLE` - " 'Sửa Đổi' " Cấu Trúc Bảng Đã Có - " 'Nâng Cấp' " "Bản Thiết Kế" "Sau Khi 'Xây Nhà' "**

- **Lệnh `ALTER TABLE` - " 'Biến Đổi' " "Hình Dạng" "Bảng Đã Tồn Tại":**

    - **Lệnh `ALTER TABLE`** là lệnh SQL "dùng" để **"sửa đổi"** (alter) **"cấu trúc"** của một **"bảng"** (table) **"đã
      có"** trong database.
    - `ALTER TABLE` "cho phép" bạn **" 'nâng cấp' " "bản thiết kế"** của bảng "sau khi 'xây nhà' " xong - "thay đổi" "
      hình dạng" "bảng biểu" một cách "linh hoạt" (ví dụ: "thêm cột mới", "xóa cột", "sửa đổi" kiểu dữ liệu cột, "
      thêm/xóa/sửa đổi" ràng buộc, v.v.).

- **"Các 'Thao Tác' " `ALTER TABLE` "Phổ Biến":**

    - **`ADD COLUMN column_definition` - " 'Thêm' " Cột Mới Vào Bảng:** "Thêm" một **"cột mới"** vào bảng. Bạn cần "chỉ
      định" **"tên cột"** và **"kiểu dữ liệu"** của cột mới.

        - **"Cú Pháp":**

          ```sql
          ALTER TABLE table_name
          ADD COLUMN column_name datatype [column_constraint]; -- "Thêm" cột mới
          ```

        - **"Ví Dụ" - " 'Thêm' " Cột `MoTa` (Description) Kiểu `VARCHAR(255)` Vào Bảng `SanPhams`:**

          ```sql
          ALTER TABLE SanPhams
          ADD COLUMN MoTa VARCHAR(255); -- "Thêm" cột mới "MoTa" kiểu VARCHAR(255) vào bảng SanPhams
          ```

    - **`DROP COLUMN column_name` - " 'Xóa' " Cột "Không Cần Thiết" Khỏi Bảng:** "Xóa" một **"cột"** "đã có" khỏi bảng.
      **"Cẩn thận"** khi "xóa" cột - dữ liệu trong cột sẽ **"bị mất" "vĩnh viễn"**.

        - **"Cú Pháp":**

          ```sql
          ALTER TABLE table_name
          DROP COLUMN column_name; -- "Xóa" cột "column_name"
          ```

        - **"Ví Dụ" - " 'Xóa' " Cột `DanhMucSanPham` Khỏi Bảng `SanPhams`:**

          ```sql
          ALTER TABLE SanPhams
          DROP COLUMN DanhMucSanPham; -- "Xóa" cột "DanhMucSanPham" khỏi bảng SanPhams
          ```

    - **`MODIFY COLUMN column_definition` (MySQL, SQLite) / `ALTER COLUMN column_definition` (SQL Server,
      PostgreSQL) - " 'Sửa Đổi' " "Định Nghĩa" Cột (Kiểu Dữ Liệu, Ràng Buộc, v.v.):** "Sửa đổi" **"định nghĩa"** (
      definition) của một **"cột"** "đã có" trong bảng (ví dụ: "thay đổi" "kiểu dữ liệu" cột, "thêm" hoặc "xóa" "ràng
      buộc" cột). "Cú pháp" có thể "khác nhau" giữa các SQL Dialects (MySQL, PostgreSQL, SQL Server, SQLite, v.v.).

        - **"Cú Pháp" (Tổng Quát - Cần "Tham Khảo" "Tài Liệu" DBMS Cụ Thể Để Biết "Cú Pháp" "Chính Xác"):**

          ```sql
          ALTER TABLE table_name
          MODIFY COLUMN column_name new_datatype [new_column_constraint]; -- "Sửa đổi" "định nghĩa" cột "column_name" (MySQL, SQLite)

          ALTER TABLE table_name
          ALTER COLUMN column_name new_datatype [new_column_constraint]; -- "Sửa đổi" "định nghĩa" cột "column_name" (SQL Server, PostgreSQL)
          ```

        - **"Ví Dụ" - " 'Sửa Đổi' " "Kiểu Dữ Liệu" Cột `Gia` Từ `INT` Sang `DECIMAL(10, 2)` Trong Bảng `SanPhams` (ví
          dụ - Cú pháp MySQL):**

          ```sql
          ALTER TABLE SanPhams
          MODIFY COLUMN Gia DECIMAL(10, 2); -- "Sửa đổi" cột Gia - "kiểu dữ liệu" mới DECIMAL(10, 2) (MySQL syntax)
          ```

    - **`ADD CONSTRAINT constraint_definition` - " 'Thêm' " "Ràng Buộc" Mới Vào Bảng (hoặc Cột):** "Thêm" một **"ràng
      buộc"** (constraint) **"mới"** vào bảng (table constraint) hoặc vào một **"cột"** (column constraint) "đã có". (Ví
      dụ: "thêm" ràng buộc `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`, `NOT NULL`, v.v.).

        - **"Cú Pháp":**

          ```sql
          ALTER TABLE table_name
          ADD CONSTRAINT constraint_name constraint_definition; -- "Thêm" ràng buộc mới
          ```

        - **"Ví Dụ" - " 'Thêm' " "Khóa Ngoại" (FOREIGN KEY) "Ràng Buộc" Cho Cột `DanhMucId` Trong Bảng `SanPhams` "Tham
          Chiếu" Đến Bảng `DanhMucs`:**

          ```sql
          ALTER TABLE SanPhams
          ADD CONSTRAINT FK_SanPham_DanhMuc -- "Thêm" ràng buộc mới có tên "FK_SanPham_DanhMuc"
          FOREIGN KEY (DanhMucId)          -- "Ràng buộc" FOREIGN KEY trên cột DanhMucId
          REFERENCES DanhMucs(DanhMucId);     -- "Tham chiếu" đến bảng DanhMucs và cột DanhMucId
          ```

    - **`DROP CONSTRAINT constraint_name` - " 'Xóa' " "Ràng Buộc" "Không Cần Thiết" Khỏi Bảng:** "Xóa" một **"ràng buộc"
      ** (constraint) "đã có" khỏi bảng (table constraint) hoặc khỏi một "cột" (column constraint).

        - **"Cú Pháp":**

          ```sql
          ALTER TABLE table_name
          DROP CONSTRAINT constraint_name; -- "Xóa" ràng buộc "constraint_name"
          ```

        - **"Ví Dụ" - " 'Xóa' " "Khóa Ngoại" "Ràng Buộc" `FK_SanPham_DanhMuc` Khỏi Bảng `SanPhams`:**

          ```sql
          ALTER TABLE SanPhams
          DROP CONSTRAINT FK_SanPham_DanhMuc; -- "Xóa" ràng buộc "FK_SanPham_DanhMuc" khỏi bảng SanPhams
          ```

**7.3. Lệnh `DROP TABLE` - " 'Xóa' " Bảng "Không Cần Thiết" Khỏi Database - " 'Phá Bỏ' " "Ngôi Nhà" Dữ Liệu "Cũ"**

- **Lệnh `DROP TABLE` - " 'Xóa Sổ' " "Bảng" Khỏi Database - " 'Không Còn Gì' "**:

    - **Lệnh `DROP TABLE`** là lệnh SQL "dùng" để **"xóa"** (drop) một **"bảng"** (table) **"không cần thiết"** hoặc **"
      không còn dùng"** nữa khỏi database.
    - `DROP TABLE` "xóa" **"toàn bộ" "cấu trúc"** và **"dữ liệu"** của bảng ( **"vĩnh viễn"** - permanent deletion). **"
      Cực kỳ 'nguy hiểm' " - "cẩn thận" khi "dùng" lệnh `DROP TABLE`**.
    - `DROP TABLE` "giống như" việc **" 'phá bỏ' " "ngôi nhà" dữ liệu "cũ"** - "xóa sổ" bảng khỏi database, "không còn
      gì" "tồn tại" sau khi "xóa".

- **"Cú Pháp" Lệnh `DROP TABLE` "Cơ Bản":**

  ```sql
  DROP TABLE table_name; -- "Ra lệnh" "xóa" bảng có tên "table_name"
  ```

    - **`DROP TABLE table_name`:** "Ra lệnh" cho database là "hãy 'xóa' bảng" có **"tên bảng"** (table name) là
      `table_name`. "Tên bảng" phải **"tồn tại"** trong database.

- **"Ví Dụ" Lệnh `DROP TABLE` - " 'Xóa' " Bảng `Tam` Khỏi Database:**

  ```sql
  DROP TABLE Tam; -- "Xóa" bảng "Tam" khỏi database
  ```

- **"Lưu Ý" Quan Trọng Khi Dùng Lệnh `DROP TABLE`:**

    - **"Xóa Bảng Là "Hành Động" "Vĩnh Viễn" (Permanent Action):** Lệnh `DROP TABLE` **"xóa"** bảng và **"toàn bộ" "dữ
      liệu"** trong bảng **"vĩnh viễn"** khỏi database. **"Không thể" "khôi phục"** bảng và dữ liệu đã "xóa" bằng lệnh
      `DROP TABLE` (trừ khi bạn có "backup" database). **"Cực kỳ 'nguy hiểm' " - "cẩn thận" khi "dùng" lệnh `DROP TABLE`
      **. **"Chỉ 'xóa' bảng khi bạn 'chắc chắn' " là mình "không còn cần" bảng đó nữa**.
    - **"Ràng Buộc" (Constraints) "Tham Chiếu" Đến Bảng:** Nếu có các bảng khác có **"khóa ngoại"** (foreign key) "tham
      chiếu" đến bảng bạn muốn "xóa", bạn có thể gặp **"lỗi" "ràng buộc"** (foreign key constraint violation) khi "xóa"
      bảng. "Cần" "xóa" các ràng buộc "khóa ngoại" "trước" hoặc "xóa" các bảng "tham chiếu" "trước" khi "xóa" bảng "
      cha".
    - **"Transactions" (Giao Dịch):** Lệnh `DROP TABLE` thường được "thực thi" trong một **"transaction"** (giao dịch).
      Nếu có "lỗi" trong quá trình `DROP TABLE`, transaction có thể được **"rollback"** (hoàn tác) để "đảm bảo"
      database "không bị" "thay đổi" "không nhất quán". (Chúng ta sẽ "học" về Transactions ở Chương 8).

**7.4. Lệnh `CREATE DATABASE`, `DROP DATABASE`, `ALTER DATABASE` - " 'Quản Lý' " Database "Tổng Thể" - " 'Sinh
Ra' ", " 'Hủy Diệt' ", và " 'Biến Đổi' " "Kho Dữ Liệu"**

- **Lệnh `CREATE DATABASE` - " 'Tạo' " Database Mới - " 'Khai Sinh' " "Kho Dữ Liệu" "Mới Tinh"**:

    - **Lệnh `CREATE DATABASE`** là lệnh SQL "dùng" để **"tạo"** (create) một **"database"** **"mới"** trong hệ quản trị
      cơ sở dữ liệu (RDBMS).
    - `CREATE DATABASE` "cho phép" bạn **" 'khai sinh' " "kho dữ liệu" "mới tinh"** để "lưu trữ" dữ liệu ứng dụng của
      bạn.

    - **"Cú Pháp" Lệnh `CREATE DATABASE` "Cơ Bản":**

      ```sql
      CREATE DATABASE database_name; -- "Ra lệnh" "tạo" database mới có tên "database_name"
      ```

        - **`CREATE DATABASE database_name`:** "Ra lệnh" cho RDBMS là "hãy 'tạo' một database mới" có **"tên database"
          ** (database name) là `database_name`. "Tên database" phải **"duy nhất"** trong RDBMS server.

    - **"Ví Dụ" Lệnh `CREATE DATABASE` - " 'Tạo' " Database Mới Tên `MyWebAppDB`:**

      ```sql
      CREATE DATABASE MyWebAppDB; -- "Tạo" database mới có tên "MyWebAppDB"
      ```

- **Lệnh `DROP DATABASE` - " 'Xóa' " Database "Không Cần Thiết" - " 'Hủy Diệt' " "Kho Dữ Liệu" "Cũ"**:

    - **Lệnh `DROP DATABASE`** là lệnh SQL "dùng" để **"xóa"** (drop) một **"database"** **"không cần thiết"** hoặc **"
      không còn dùng"** nữa khỏi RDBMS server.
    - `DROP DATABASE` "xóa" **"toàn bộ" "cấu trúc"**, **"dữ liệu"**, và **"đối tượng"** (tables, views, indexes, stored
      procedures, v.v.) **"bên trong" database** ( **"vĩnh viễn"** - permanent deletion). **"Cực kỳ 'nguy hiểm' " - "cẩn
      thận" khi "dùng" lệnh `DROP DATABASE`**.
    - `DROP DATABASE` "giống như" việc **" 'hủy diệt' " "kho dữ liệu" "cũ"** - "xóa sổ" database khỏi RDBMS server, "
      không còn gì" "tồn tại" sau khi "xóa".

    - **"Cú Pháp" Lệnh `DROP DATABASE` "Cơ Bản":**

      ```sql
      DROP DATABASE database_name; -- "Ra lệnh" "xóa" database có tên "database_name"
      ```

        - **`DROP DATABASE database_name`:** "Ra lệnh" cho RDBMS là "hãy 'xóa' database" có **"tên database"** (database
          name) là `database_name`. "Tên database" phải **"tồn tại"** trong RDBMS server.

    - **"Ví Dụ" Lệnh `DROP DATABASE` - " 'Xóa' " Database `MyOldWebAppDB` Khỏi Server:**

      ```sql
      DROP DATABASE MyOldWebAppDB; -- "Xóa" database "MyOldWebAppDB" khỏi server
      ```

    - **"Lưu Ý" Quan Trọng Khi Dùng Lệnh `DROP DATABASE`:**

        - **"Xóa Database Là "Hành Động" "Vĩnh Viễn" (Permanent Action):** Lệnh `DROP DATABASE` **"xóa"** database và *
          *"toàn bộ" "dữ liệu"**, **"bảng"**, **"đối tượng"** bên trong database **"vĩnh viễn"** khỏi RDBMS server. **"
          Không thể" "khôi phục"** database và dữ liệu đã "xóa" bằng lệnh `DROP DATABASE` (trừ khi bạn có "backup"
          database). **"Cực kỳ 'nguy hiểm' " - "cẩn thận" khi "dùng" lệnh `DROP DATABASE`**. **"Chỉ 'xóa' database khi
          bạn 'chắc chắn' " là mình "không còn cần" database đó nữa**.
        - **"Cần 'Quyền Admin' " (Admin Privileges):** Bạn cần **"quyền admin"** (administrator privileges) trên RDBMS
          server để "thực hiện" lệnh `DROP DATABASE`.
        - **"Đóng" "Kết Nối" Đến Database Trước Khi "Xóa":** "Đảm bảo" **"không có" "kết nối" nào** (connections) đến
          database mà bạn muốn "xóa" trước khi "thực hiện" lệnh `DROP DATABASE`. Nếu có "kết nối" "đang mở", database có
          thể "từ chối" "xóa" database.

- **Lệnh `ALTER DATABASE` - " 'Sửa Đổi' " Database "Tổng Thể" (Ít Dùng Hơn `CREATE TABLE` và `DROP TABLE`):**

    - **Lệnh `ALTER DATABASE`** là lệnh SQL "dùng" để **"sửa đổi"** (alter) một số "thuộc tính" "tổng thể" của **"
      database"** "đã có" (ví dụ: "đổi tên" database, "thay đổi" character set, "thay đổi" collation, v.v.).
    - `ALTER DATABASE` "ít 'phổ biến' " hơn lệnh `CREATE TABLE` và `DROP TABLE`. Thường "dùng" khi "cần" "thay đổi" "cấu
      hình" "database "tổng thể" (ví dụ: sau khi "cài đặt" database server hoặc khi "nâng cấp" database server lên phiên
      bản mới).

    - **"Cú Pháp" Lệnh `ALTER DATABASE` "Cơ Bản" (Cú Pháp "Có Thể Khác Nhau" Giữa Các RDBMSs - "Tham Khảo" "Tài Liệu"
      DBMS Cụ Thể):**

      ```sql
      ALTER DATABASE database_name
      [MODIFY <database_property> = new_value] -- "Sửa đổi" một "thuộc tính" database (tùy chọn)
      [SET <database_option> = new_value]      -- "Set" một "tùy chọn" database (tùy chọn)
      ...
      ;
      ```

        - Cú pháp `ALTER DATABASE` có thể **"khác nhau"** giữa các **SQL Dialects** (phương ngữ SQL) của các RDBMSs "
          khác nhau". "Tham khảo" **"tài liệu"** của RDBMS mà bạn đang "dùng" để "biết" "cú pháp" "chính xác" và các "
          tùy chọn" "sửa đổi" database "được hỗ trợ".

        - **"Ví Dụ" Lệnh `ALTER DATABASE` - " 'Đổi Tên' " Database `MyWebAppDB` Thành `WebAppDB_V2` (ví dụ - Cú pháp
          MySQL - "không hỗ trợ" "đổi tên" database trực tiếp bằng `ALTER DATABASE`, cần "tạo" database mới và "
          rename"):**

          (Trong MySQL, "đổi tên" database thường được thực hiện bằng cách "tạo" database mới với tên mới và "rename"
          database cũ thành tên mới, hoặc dùng các công cụ "quản lý" database GUI. Lệnh `ALTER DATABASE` trong MySQL chủ
          yếu "dùng" để "thay đổi" "character set" và "collation" của database).

**7.5. "Thực Hành" Định Nghĩa Dữ Liệu (DDL) - " 'Thiết Kế' " và " 'Biến Đổi' " Cấu Trúc Database - " 'Làm Chủ' " "Nghệ
Thuật" "Xây Database"**

- **"Bài Tập" "Thực Hành" - " 'Luyện Công Phu' " DDL Để " 'Xây Dựng' " và " 'Biến Đổi' " Database:**

    1. **"Tạo" một database "mới" tên `QuanLyBanHangDB` (Sales Management Database).** (Dùng `CREATE DATABASE`).
    2. **"Tạo" bảng `KhachHangs` (Customers) trong database `QuanLyBanHangDB` với các cột: `KhachHangId` (INT, PRIMARY
       KEY, AUTO_INCREMENT), `TenKhachHang` (VARCHAR(255), NOT NULL), `DiaChi` (VARCHAR(255)), `Email` (VARCHAR(255),
       UNIQUE).** (Dùng `CREATE TABLE` và các "ràng buộc" cột).
    3. **"Tạo" bảng `DonHangs` (Orders) trong database `QuanLyBanHangDB` với các cột: `DonHangId` (INT, PRIMARY KEY,
       AUTO_INCREMENT), `KhachHangId` (INT, FOREIGN KEY "tham chiếu" đến bảng `KhachHangs`), `NgayDatHang` (DATE, NOT
       NULL), `TongTien` (DECIMAL(10, 2), NOT NULL).** (Dùng `CREATE TABLE` và "ràng buộc" cột và "ràng buộc" bảng
       `FOREIGN KEY`).
    4. **"Thêm" cột `SoDienThoai` (PhoneNumber) kiểu `VARCHAR(20)` vào bảng `KhachHangs`.** (Dùng
       `ALTER TABLE ADD COLUMN`).
    5. **"Sửa đổi" kiểu dữ liệu cột `DiaChi` trong bảng `KhachHangs` từ `VARCHAR(255)` sang `TEXT`.** (Dùng
       `ALTER TABLE MODIFY COLUMN` hoặc `ALTER TABLE ALTER COLUMN` - tùy theo SQL Dialect).
    6. **"Thêm" ràng buộc `UNIQUE` cho "tổ hợp" cột `TenKhachHang` và `SoDienThoai` trong bảng `KhachHangs`.** (Dùng
       `ALTER TABLE ADD CONSTRAINT UNIQUE (column1, column2, ...)`).
    7. **"Xóa" bảng `Tam` (nếu có) khỏi database `QuanLyBanHangDB`.** (Dùng `DROP TABLE`).
    8. **"Xóa" database `MyOldWebAppDB` (nếu có) khỏi server.** (Dùng `DROP DATABASE` - **"cẩn thận"** khi "xóa"
       database).

- **"Thực Hành" Với SQL Client Tool - " 'Kiến Tạo' " và " 'Biến Đổi' " Database "Theo Ý Muốn":**

    - "Mở" SQL client tool.
    - "Kết nối" đến RDBMS server (ví dụ: MySQL Server, PostgreSQL Server, SQL Server, SQLite).
    - "Mở" SQL editor và "viết" các câu lệnh DDL "thực hành" cho từng "bài tập" trên.
    - "Chạy" các câu lệnh DDL để "tạo", "sửa đổi", và "xóa" cấu trúc database.
    - " 'Sáng tạo' ", " 'thử nghiệm' ", và " 'khám phá' " các "cách" "kết hợp" các lệnh DDL để "thiết kế" và "biến đổi"
      cấu trúc database "theo ý muốn" của bạn. **"Làm chủ" "nghệ thuật" "xây database"**.

**Tổng Kết Chương 7:**

- Bạn đã "khám phá" các lệnh SQL **Data Definition Language (DDL)** để "định nghĩa" và "quản lý" "cấu trúc" database.
    - "Nắm vững" lệnh **`CREATE TABLE`** ("tạo" bảng mới).
    - "Hiểu" lệnh **`ALTER TABLE`** ("sửa đổi" cấu trúc bảng đã có).
    - "Làm chủ" lệnh **`DROP TABLE`** ("xóa" bảng "không cần thiết").
    - Biết cách "dùng" lệnh **`CREATE DATABASE`**, **`DROP DATABASE`**, và **`ALTER DATABASE`** để "quản lý" database "
      tổng thể".
    - "Thực hành" "viết" và "chạy" các câu lệnh DDL để "luyện tập" và "xây dựng" và "biến đổi" cấu trúc database "thực
      tế".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 8: "Tuyệt Chiêu" SQL Nâng Cao và "Bước Tiếp Theo" - " 'Luyện Công Phu' " SQL Để " 'Trở
Thành' " "Cao Thủ"**. Chúng ta sẽ "nâng cấp" "kỹ năng" SQL của bạn lên "đỉnh cao" với các "tuyệt chiêu" SQL "nâng cao"
như Subqueries, CTEs, Indexes, Transactions, và "best practices" SQL để "viết code SQL" "chuyên nghiệp" và "hiệu quả"
hơn.

Bạn có câu hỏi nào về các lệnh định nghĩa dữ liệu (DDL) này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải
đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" SQL.
