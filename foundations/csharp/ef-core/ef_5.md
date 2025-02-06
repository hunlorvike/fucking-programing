# Chương 5: Migrations - "Quản Lý" "Thay Đổi" Cấu Trúc Database - "Nâng Cấp" Database "Thông Minh" - "Biến Hóa" Database Theo Code

Chào mừng bạn đến với **Chương 5: Migrations - "Quản Lý" "Thay Đổi" Cấu Trúc Database**! Trong chương này, chúng ta sẽ "khám phá" một "tính năng" "vô cùng quan trọng" của EF Core - **Migrations**. Migrations giúp bạn "quản lý" các "thay đổi" cấu trúc database một cách "thông minh" và "chuyên nghiệp", "giải quyết" bài toán "đau đầu" về việc "cập nhật" database khi "mô hình dữ liệu" của ứng dụng "thay đổi".

**Phần 5: Migrations - "Quản Lý" "Thay Đổi" Cấu Trúc Database**

**5.1. Migrations Là Gì? Tại Sao Cần Migrations? - "Vấn Đề" "Đồng Bộ" Cấu Trúc Database và "Giải Pháp" Migrations**

-   **"Vấn Đề": "Làm Sao 'Đồng Bộ' Cấu Trúc Database Với Code?" - "Bài Toán Khó"**

    -   Trong quá trình phát triển ứng dụng, **"mô hình dữ liệu"** của bạn (Entities, Data Context) có thể **"thay đổi"** theo thời gian. Ví dụ: bạn "thêm" một property mới vào Entity class, "đổi tên" property, "thêm" hoặc "xóa" một Entity class, "thay đổi" "quan hệ" giữa các Entities, v.v.
    -   Những "thay đổi" này trong code **"cần phải được 'ánh xạ' "** (đồng bộ hóa) vào **"cấu trúc database"** (bảng, cột, khóa, quan hệ) để ứng dụng có thể "làm việc" với database một cách "nhịp nhàng".
    -   Nếu bạn "quản lý" "thay đổi" cấu trúc database bằng tay (ví dụ: viết và "chạy" các script SQL "thủ công"), sẽ rất **"vất vả"**, **"dễ mắc lỗi"**, và **"khó theo dõi"** "lịch sử" các "thay đổi".

-   **Migrations - "Giải Pháp" "Tự Động" "Quản Lý" "Thay Đổi" Cấu Trúc Database:**

    -   **Migrations** trong EF Core là một "công cụ" giúp bạn **"tự động hóa"** quá trình **"quản lý"** và **"áp dụng"** các "thay đổi" cấu trúc database dựa trên những "thay đổi" trong "mô hình dữ liệu" (Entities, Data Context) của bạn.
    -   Migrations "hoạt động" theo cơ chế **"ghi lại"** các "thay đổi" cấu trúc database thành các **"file migration"** (file code C#). Mỗi "file migration" đại diện cho một "phiên bản" "thay đổi" cấu trúc database.
    -   Bạn có thể "dùng" các "lệnh" EF Core Migrations để:
        -   **"Tạo" Migration Mới:** "Ghi lại" các "thay đổi" trong "mô hình dữ liệu" thành một "file migration" mới.
        -   **"Áp Dụng" Migrations Vào Database:** "Cập nhật" cấu trúc database lên phiên bản mới nhất (hoặc một phiên bản cụ thể) bằng cách "chạy" các "file migration" đã được tạo.
        -   **"Hoàn Tác" Migrations (Rollback):** "Quay về" phiên bản cấu trúc database cũ hơn bằng cách "hoàn tác" các "file migration" đã "áp dụng".

**5.2. "Tạo" Migration Mới - "Ghi Lại" "Thay Đổi" Cấu Trúc - "Chụp Ảnh" "Thay Đổi"**

-   **"Mục tiêu":** "Ghi lại" các "thay đổi" trong "mô hình dữ liệu" (Entities, Data Context) thành một **"file migration"** mới.
-   **"Cách thực hiện" - "Dùng" EF Core Tools (command-line tools):**

    1.  Mở **Package Manager Console** (trong Visual Studio) hoặc **Command Line Interface (CLI)** (ví dụ: Command Prompt, Terminal).
    2.  "Di chuyển" đến **thư mục dự án** chứa Data Context của bạn.
    3.  "Chạy" lệnh **`Add-Migration <MigrationName>`** (trong Package Manager Console) hoặc **`dotnet ef migrations add <MigrationName>`** (trong CLI). Thay `<MigrationName>` bằng **"tên"** bạn muốn đặt cho migration (ví dụ: `AddDanhMucEntity`, `UpdateSanPhamGia`, `AddQuanHeDanhMucSanPham`, v.v.) - tên migration nên "mô tả" "ý nghĩa" của "thay đổi" cấu trúc database.
    4.  EF Core Tools sẽ "so sánh" "mô hình dữ liệu" hiện tại của bạn với "snapshot" (ảnh chụp) "mô hình dữ liệu" của migration trước đó (hoặc "mô hình dữ liệu" ban đầu nếu chưa có migrations nào).
    5.  Nếu có "thay đổi", EF Core Tools sẽ "tự động" "tạo ra" một **"thư mục Migrations"** (nếu chưa có) và một **"file migration"** mới (file code C#) bên trong thư mục này. "File migration" này sẽ chứa code C# để "mô tả" các "thay đổi" cấu trúc database (ví dụ: "thêm bảng", "thêm cột", "thêm khóa ngoại", v.v.) cần "áp dụng" vào database.

-   **Ví dụ "tạo" migration mới (ví dụ: "thêm" Entity `DanhMuc` và quan hệ với `SanPham`):**

    1.  Đảm bảo bạn đã "định nghĩa" Entity `DanhMuc`, Entity `SanPham` và Data Context `MyDbContext` có "quan hệ" Một-Nhiều giữa `DanhMuc` và `SanPham` (như ví dụ ở Chương 4).
    2.  Mở Package Manager Console.
    3.  "Gõ" lệnh: `Add-Migration AddDanhMucAndSanPhamRelationship` (đặt tên migration là `AddDanhMucAndSanPhamRelationship`).
    4.  Bấm Enter và "chờ" EF Core Tools "tạo" migration.

-   **"Kết quả" sau khi "tạo" migration:**

    -   Một **"thư mục Migrations"** được "tạo ra" (nếu chưa có) trong dự án của bạn.
    -   Bên trong thư mục `Migrations`, một **"file migration" C# mới** được "sinh ra" (ví dụ: `20231027103045_AddDanhMucAndSanPhamRelationship.cs`). "File migration" này thường có **hai phương thức quan trọng**:
        -   **`Up(MigrationBuilder migrationBuilder)`:** Chứa code C# để **"cập nhật"** cấu trúc database (ví dụ: "thêm bảng", "thêm cột", v.v.) khi "áp dụng" migration này.
        -   **`Down(MigrationBuilder migrationBuilder)`:** Chứa code C# để **"hoàn tác"** (rollback) các "thay đổi" cấu trúc database (ví dụ: "xóa bảng", "xóa cột", v.v.) khi "hoàn tác" migration này.

**5.3. "Áp Dụng" Migrations Vào Database - "Cập Nhật" Cấu Trúc Database Theo Code - "Biến Hình" Database**

-   **"Mục tiêu":** "Cập nhật" cấu trúc database hiện tại lên phiên bản mới nhất (hoặc một phiên bản cụ thể) bằng cách "chạy" các "file migration" đã được "tạo".
-   **"Cách thực hiện" - "Dùng" EF Core Tools (command-line tools):**

    -   **"Cập nhật" database lên phiên bản mới nhất (áp dụng tất cả các migrations "chưa áp dụng"):**
        1.  Mở **Package Manager Console** hoặc **CLI**.
        2.  "Di chuyển" đến **thư mục dự án** chứa Data Context của bạn.
        3.  "Chạy" lệnh **`Update-Database`** (trong Package Manager Console) hoặc **`dotnet ef database update`** (trong CLI).
        4.  EF Core Tools sẽ "tìm kiếm" các "file migration" **"chưa được áp dụng"** vào database.
        5.  "Chạy" lần lượt các phương thức **`Up()`** trong các "file migration" "chưa áp dụng" để "cập nhật" cấu trúc database.
        6.  "Ghi lại" vào database là các migrations đã được "áp dụng".

    -   **"Cập nhật" database lên một phiên bản cụ thể (áp dụng migrations đến một migration cụ thể):**
        1.  "Chạy" lệnh **`Update-Database <MigrationName>`** (trong Package Manager Console) hoặc **`dotnet ef database update <MigrationName>`** (trong CLI). Thay `<MigrationName>` bằng **"tên"** của migration mà bạn muốn "cập nhật" đến (ví dụ: `AddDanhMucAndSanPhamRelationship`).
        2.  EF Core Tools sẽ "chạy" các phương thức `Up()` trong các "file migration" **từ đầu đến migration có tên `<MigrationName>`** (nếu migration có tên `<MigrationName>` "chưa được áp dụng").

-   **Ví dụ "áp dụng" migrations vào database (cập nhật lên phiên bản mới nhất):**

    1.  Mở Package Manager Console.
    2.  "Gõ" lệnh: `Update-Database` (không có tham số).
    3.  Bấm Enter và "chờ" EF Core Tools "cập nhật" database.

-   **"Kết quả" sau khi "áp dụng" migrations:**

    -   Cấu trúc database sẽ được **"cập nhật"** theo các "thay đổi" được "mô tả" trong các "file migration" đã được "áp dụng". Ví dụ: bảng mới được "thêm", cột mới được "thêm", khóa ngoại được "tạo", v.v.
    -   Một bảng lịch sử migrations **`__EFMigrationsHistory`** (hoặc tên khác tùy theo database provider) sẽ được "tạo ra" trong database để EF Core "theo dõi" các migrations đã được "áp dụng" vào database.

**5.4. "Hoàn Tác" Migrations (Rollback) - "Quay Về" Phiên Bản Cấu Trúc Cũ - "Cỗ Máy Thời Gian" Cho Database**

-   **"Mục tiêu":** "Hoàn tác" (rollback) các "thay đổi" cấu trúc database, "quay về" phiên bản cấu trúc database cũ hơn.
-   **"Cách thực hiện" - "Dùng" EF Core Tools (command-line tools):**

    -   **"Hoàn tác" về migration "trước đó" (rollback một bước):**
        1.  Mở **Package Manager Console** hoặc **CLI**.
        2.  "Di chuyển" đến **thư mục dự án** chứa Data Context của bạn.
        3.  "Chạy" lệnh **`Update-Database 0`** (trong Package Manager Console) hoặc **`dotnet ef database update 0`** (trong CLI).
        4.  EF Core Tools sẽ "tìm" migration **"cuối cùng"** đã được "áp dụng" vào database.
        5.  "Chạy" phương thức **`Down()`** trong "file migration" "cuối cùng" đó để "hoàn tác" các "thay đổi" cấu trúc database.

    -   **"Hoàn tác" về một migration cụ thể (rollback về phiên bản bất kỳ):**
        1.  "Chạy" lệnh **`Update-Database <MigrationName>`** (trong Package Manager Console) hoặc **`dotnet ef database update <MigrationName>`** (trong CLI). Thay `<MigrationName>` bằng **"tên"** của migration mà bạn muốn "hoàn tác" về (ví dụ: `AddDanhMucAndSanPhamRelationship`).
        2.  EF Core Tools sẽ "chạy" các phương thức `Down()` trong các "file migration" **từ migration "cuối cùng" đến migration có tên `<MigrationName>`** (và migration `<MigrationName>` nếu nó đã được "áp dụng").

-   **Ví dụ "hoàn tác" migration (rollback về migration "trước đó"):**

    1.  Mở Package Manager Console.
    2.  "Gõ" lệnh: `Update-Database 0` (hoặc `Update-Database -1` cũng tương tự).
    3.  Bấm Enter và "chờ" EF Core Tools "hoàn tác" migration.

-   **"Kết quả" sau khi "hoàn tác" migration:**

    -   Cấu trúc database sẽ được "quay về" phiên bản cũ hơn, "đảo ngược" các "thay đổi" được "mô tả" trong các "file migration" đã "hoàn tác". Ví dụ: bảng bị "xóa", cột bị "xóa", khóa ngoại bị "xóa", v.v.
    -   Bảng lịch sử migrations `__EFMigrationsHistory` sẽ được "cập nhật" để "phản ánh" các migrations đã được "hoàn tác".

**Tổng Kết Chương 5:**

-   Bạn đã "khám phá" "sức mạnh" của Migrations trong EF Core để "quản lý" "thay đổi" cấu trúc database một cách "thông minh" và "tự động hóa".
    -   "Hiểu" được "vấn đề" "đồng bộ" cấu trúc database và "giải pháp" Migrations.
    -   Học cách "tạo" Migration mới (`Add-Migration`) để "ghi lại" "thay đổi" cấu trúc.
    -   Biết cách "áp dụng" Migrations vào database (`Update-Database`) để "cập nhật" cấu trúc database theo code.
    -   Học cách "hoàn tác" Migrations (`Update-Database 0` hoặc `Update-Database <MigrationName>`) để "quay về" phiên bản cấu trúc cũ.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 6: Truy Vấn Nâng Cao Với LINQ - "Hỏi Han" Database "Chuyên Nghiệp"**. Chúng ta sẽ "nâng cấp" "kỹ năng" truy vấn LINQ của bạn lên một "tầm cao mới" với các "chiêu thức" "truy vấn" "cao cấp" hơn như Projections, Filtering, Aggregation, và Raw SQL Queries.

Bạn có câu hỏi nào về Migrations này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" EF Core.

