# Chương 3: "Thao Tác" Dữ Liệu Cơ Bản (CRUD Operations) - "Làm Chủ" "Bảng Biểu" - "Nắm Vững" "Bốn Chiêu Thức" "Cơ Bản" Với Database

Chào mừng bạn trở lại với hành trình Entity Framework! Trong chương này, chúng ta sẽ "học cách" "thao tác" dữ liệu **"cơ bản"** nhất với cơ sở dữ liệu thông qua EF Core - các thao tác **CRUD Operations**. CRUD là viết tắt của **Create, Read, Update, Delete** - "bốn chiêu thức" "võ công" "nền tảng" mà bạn cần "nắm vững" để "làm chủ" bất kỳ hệ thống quản lý dữ liệu nào.

**Phần 3: "Thao Tác" Dữ Liệu Cơ Bản (CRUD Operations) - "Làm Chủ" "Bảng Biểu"**

**3.1. "Thêm" Dữ Liệu Mới (Create) - "Gieo Mầm" Bản Ghi Mới - "Sinh Ra" Dữ Liệu**

-   **"Mục tiêu":** "Thêm" một bản ghi (row) mới vào một bảng (table) trong cơ sở dữ liệu.
-   **"Cách thực hiện" với EF Core:**

    1.  **"Tạo" một "món đồ" mới (instance) của Entity class** mà bạn muốn "thêm" vào database (ví dụ: tạo một đối tượng `SanPham` mới).
    2.  **"Gán" giá trị** cho các "đặc điểm" (properties) của "món đồ" mới này (ví dụ: `TenSanPham`, `Gia`, `DanhMucSanPham`).
    3.  **"Thêm" "món đồ" vào `DbSet<TEntity>`** tương ứng trong Data Context (ví dụ: `dbContext.SanPhams.Add(sanPhamMoi)`). `DbSet<TEntity>` là "đại diện" cho bảng database mà bạn muốn "thêm" dữ liệu vào.
    4.  "Gọi" phương thức **`dbContext.SaveChanges()`** để **"lưu"** các "thay đổi" (thao tác "thêm") vào cơ sở dữ liệu. EF Core sẽ "tự động" "phát lệnh" `INSERT` statement để "thêm" bản ghi mới vào bảng.

-   **Ví dụ code "thêm" sản phẩm mới vào database:**

    ```csharp
    using (var dbContext = new MyDbContext()) // "Mở" "trạm trung chuyển" Data Context (using để đảm bảo "đóng cửa" sau khi dùng xong)
    {
        // 1. "Tạo" "món đồ" SanPham mới
        var sanPhamMoi = new SanPham // Tạo instance của class SanPham
        {
            TenSanPham = "Chuột không dây", // "Gán" "tên sản phẩm"
            Gia = 250000,                // "Gán" "giá"
            DanhMucSanPham = "Điện tử"    // "Gán" "danh mục sản phẩm"
        };

        // 2. "Thêm" "món đồ" SanPham vào DbSet<SanPham> (bảng SanPhams)
        dbContext.SanPhams.Add(sanPhamMoi); // "Thêm" 'sanPhamMoi' vào "rổ" SanPhams (DbSet<SanPham>) - chưa "lưu" vào database

        // 3. "Lưu" thay đổi vào database (thực thi INSERT statement)
        dbContext.SaveChanges(); // "Lệnh" EF Core "lưu" các "thay đổi" vào database - INSERT statement được "gửi" đến database

        Console.WriteLine($"Đã thêm sản phẩm mới: {sanPhamMoi.TenSanPham}, ID: {sanPhamMoi.SanPhamId}"); // Thông báo "thêm thành công" và "in ra" ID sản phẩm (ID được database "tự động" tạo ra)
    }
    ```

-   **"Giải mã" code "thêm" dữ liệu:**

    -   `using (var dbContext = new MyDbContext())`: "Mở" Data Context - "cửa ngõ" để "tương tác" với database.
    -   `var sanPhamMoi = new SanPham { ... }`: "Tạo" một đối tượng `SanPham` mới và "gán" giá trị cho các properties.
    -   `dbContext.SanPhams.Add(sanPhamMoi)`: "Thêm" đối tượng `SanPham` vào `DbSet<SanPham>`. Lúc này, EF Core **"theo dõi"** đối tượng `sanPhamMoi` và "biết" rằng bạn muốn "thêm" nó vào bảng `SanPhams`. Nhưng **chưa có gì được "ghi" vào database** cả.
    -   `dbContext.SaveChanges()`: "Lệnh" EF Core "thực sự" "lưu" các "thay đổi" vào database. EF Core sẽ "phân tích" các "thay đổi" đã được "theo dõi" (trong trường hợp này là thao tác "thêm" `sanPhamMoi`) và "phát lệnh" câu lệnh `INSERT` SQL để "thêm" bản ghi mới vào bảng `SanPhams`. Sau khi `SaveChanges()` "chạy" xong, bản ghi mới sẽ được "thêm" vào database, và property `SanPhamId` của đối tượng `sanPhamMoi` sẽ được "cập nhật" với giá trị ID do database "tự động" tạo ra (nếu `SanPhamId` là cột identity - tự tăng).

**3.2. "Đọc" Dữ Liệu (Read) - "Hỏi Han" Database Bằng LINQ - "Tìm Kiếm" và "Lấy Ra" Dữ Liệu**

-   **"Mục tiêu":** "Lấy" dữ liệu (một hoặc nhiều bản ghi) từ một hoặc nhiều bảng trong cơ sở dữ liệu.
-   **"Cách thực hiện" với EF Core - "Sức mạnh" của LINQ queries:**

    -   EF Core "cho phép" bạn "truy vấn" dữ liệu từ database bằng các câu truy vấn **LINQ (Language Integrated Query)** "quen thuộc" của C#.
    -   Bạn "bắt đầu" truy vấn từ `DbSet<TEntity>` properties trong Data Context (ví dụ: `dbContext.SanPhams`, `dbContext.DanhMucs`).
    -   "Dùng" các "chiêu" LINQ như `Where`, `OrderBy`, `Select`, `Join`, `Include`, `FirstOrDefault`, `ToList`, `Count`, `Sum`, v.v. để "xây dựng" câu truy vấn theo ý muốn.
    -   EF Core sẽ "tự động" "dịch" LINQ queries của bạn thành các câu lệnh **SQL** "tương ứng" và "thực thi" chúng trên database.
    -   Kết quả truy vấn sẽ được EF Core "chuyển đổi" thành các **đối tượng C#** (Entities) "quen thuộc".

-   **Ví dụ code "đọc" dữ liệu sản phẩm từ database bằng LINQ queries:**

    ```csharp
    using (var dbContext = new MyDbContext()) // "Mở" "trạm trung chuyển" Data Context
    {
        // 1. "Lấy" "tất cả" sản phẩm từ bảng SanPhams (LINQ Method Syntax) - "Hỏi" database: "Cho xem hết sản phẩm đi!"
        var danhSachSanPham_TatCa = dbContext.SanPhams // "Bắt đầu" từ DbSet<SanPham> (bảng SanPhams)
                                            .ToList(); // "Ép" truy vấn "chạy" và "lấy" kết quả dạng List<SanPham> - Immediate Execution

        Console.WriteLine("--- Tất cả sản phẩm ---");
        foreach (var sp in danhSachSanPham_TatCa) // Duyệt qua danh sách sản phẩm
        {
            Console.WriteLine($"- {sp.TenSanPham}, Giá: {sp.Gia:#,##0}"); // In ra "tên" và "giá" sản phẩm
        }

        // 2. "Lọc" sản phẩm theo "danh mục" "Điện tử" (LINQ Query Syntax) - "Hỏi" database: "Sản phẩm nào thuộc danh mục 'Điện tử'?"
        var danhSachSanPham_DienTu = from sp in dbContext.SanPhams // "Từ" DbSet<SanPham>
                                     where sp.DanhMucSanPham == "Điện tử" // "Lọc" theo "danh mục" "Điện tử"
                                     orderby sp.Gia descending // "Sắp xếp" theo "giá" giảm dần
                                     select sp; // "Chọn" sản phẩm

        Console.WriteLine("\n--- Sản phẩm danh mục 'Điện tử' (giá giảm dần) ---");
        foreach (var sp in danhSachSanPham_DienTu) // Duyệt qua danh sách sản phẩm đã "lọc"
        {
            Console.WriteLine($"- {sp.TenSanPham}, Giá: {sp.Gia:#,##0}"); // In ra "tên" và "giá" sản phẩm
        }

        // 3. "Tìm" sản phẩm theo "ID" (FirstOrDefault) - "Hỏi" database: "Sản phẩm nào có ID là 1?"
        var sanPham_ID_1 = dbContext.SanPhams.FirstOrDefault(sp => sp.SanPhamId == 1); // "Tìm" sản phẩm "đầu tiên" (hoặc "không có gì" nếu không tìm thấy) có SanPhamId == 1

        if (sanPham_ID_1 != null) // "Kiểm tra" xem có "tìm" thấy sản phẩm không
        {
            Console.WriteLine($"\n--- Sản phẩm có ID = 1 ---");
            Console.WriteLine($"- Tên: {sanPham_ID_1.TenSanPham}, Giá: {sanPham_ID_1.Gia:#,##0}"); // In ra "tên" và "giá" sản phẩm "tìm" thấy
        }
        else
        {
            Console.WriteLine("\nKhông tìm thấy sản phẩm có ID = 1."); // Thông báo "không tìm thấy"
        }
    }
    ```

-   **"Giải mã" code "đọc" dữ liệu:**

    -   `dbContext.SanPhams`: "Bắt đầu" truy vấn từ `DbSet<SanPham>` - "đại diện" cho bảng `SanPhams`.
    -   `.ToList()`: "Ép" truy vấn "thực thi ngay lập tức" và "lấy" kết quả dạng `List<SanPham>`.
    -   `from sp in dbContext.SanPhams where ... orderby ... select sp`: Ví dụ về **Query Syntax** của LINQ - cú pháp "giống SQL" giúp viết truy vấn "dễ đọc".
    -   `.Where(sp => sp.DanhMucSanPham == "Điện tử")`: "Chiêu" `Where` của LINQ để "lọc" dữ liệu theo "điều kiện".
    -   `.OrderByDescending(sp => sp.Gia)`: "Chiêu" `OrderByDescending` của LINQ để "sắp xếp" dữ liệu theo "giá" giảm dần.
    -   `.FirstOrDefault(sp => sp.SanPhamId == 1)`: "Chiêu" `FirstOrDefault` của LINQ để "tìm" "món đồ" "đầu tiên" (hoặc "không có gì" nếu không tìm thấy) "thỏa mãn" "điều kiện".

**3.3. "Sửa" Dữ Liệu (Update) - "Chỉnh Sửa" Bản Ghi Đã Có - "Thay Áo Mới" Cho Dữ Liệu**

-   **"Mục tiêu":** "Cập nhật" (sửa đổi) một bản ghi (row) đã có trong một bảng (table) trong cơ sở dữ liệu.
-   **"Cách thực hiện" với EF Core:**

    1.  **"Tìm" "món đồ" (Entity) cần "sửa"** từ database (ví dụ: bằng `dbContext.SanPhams.Find(id)` hoặc dùng LINQ queries như `Where().FirstOrDefault()`).
    2.  **"Thay đổi" giá trị** của các "đặc điểm" (properties) của "món đồ" đã "tìm" thấy (ví dụ: `sanPhamCanSua.Gia = 300000;`).
    3.  "Gọi" phương thức **`dbContext.SaveChanges()`** để **"lưu"** các "thay đổi" (thao tác "sửa") vào cơ sở dữ liệu. EF Core sẽ "tự động" "phát lệnh" `UPDATE` statement để "cập nhật" bản ghi trong bảng.

-   **Ví dụ code "sửa" thông tin sản phẩm trong database:**

    ```csharp
    using (var dbContext = new MyDbContext()) // "Mở" "trạm trung chuyển" Data Context
    {
        // 1. "Tìm" sản phẩm cần "sửa" (ví dụ: theo SanPhamId = 3)
        var sanPhamCanSua = dbContext.SanPhams.Find(3); // "Tìm" sản phẩm có SanPhamId == 3 - dùng Find (chỉ tìm theo khóa chính)

        if (sanPhamCanSua != null) // "Kiểm tra" xem có "tìm" thấy sản phẩm không
        {
            // 2. "Thay đổi" giá trị các properties của sản phẩm
            sanPhamCanSua.Gia = 300000;                // "Sửa" "giá" sản phẩm
            sanPhamCanSua.DanhMucSanPham = "Linh kiện"; // "Sửa" "danh mục sản phẩm"

            // (Không cần gọi Add hay Update gì cả - EF Core đã "theo dõi" 'sanPhamCanSua' và "biết" là bạn muốn "sửa" nó)

            // 3. "Lưu" thay đổi vào database (thực thi UPDATE statement)
            dbContext.SaveChanges(); // "Lệnh" EF Core "lưu" các "thay đổi" vào database - UPDATE statement được "gửi" đi

            Console.WriteLine($"Đã sửa sản phẩm: {sanPhamCanSua.TenSanPham}, Giá mới: {sanPhamCanSua.Gia:#,##0}, Danh mục mới: {sanPhamCanSua.DanhMucSanPham}"); // Thông báo "sửa thành công"
        }
        else
        {
            Console.WriteLine("Không tìm thấy sản phẩm có ID = 3 để sửa."); // Thông báo "không tìm thấy" sản phẩm để sửa
        }
    }
    ```

-   **"Giải mã" code "sửa" dữ liệu:**

    -   `var sanPhamCanSua = dbContext.SanPhams.Find(3);`: "Tìm" đối tượng `SanPham` cần "sửa" bằng `Find(3)` (tìm theo "khóa chính" `SanPhamId` = 3).
    -   `sanPhamCanSua.Gia = 300000;` và `sanPhamCanSua.DanhMucSanPham = "Linh kiện";`: "Thay đổi" giá trị của các properties `Gia` và `DanhMucSanPham` của đối tượng `sanPhamCanSua`. EF Core sẽ **"tự động" "theo dõi"** các "thay đổi" này.
    -   `dbContext.SaveChanges()`: "Lệnh" EF Core "lưu" các "thay đổi" vào database. EF Core sẽ "phát hiện" các "thay đổi" của đối tượng `sanPhamCanSua` và "phát lệnh" câu lệnh `UPDATE` SQL để "cập nhật" bản ghi tương ứng trong bảng `SanPhams`.

**3.4. "Xóa" Dữ Liệu (Delete) - "Dọn Dẹp" Bản Ghi Không Cần Thiết - "Khử" Dữ Liệu**

-   **"Mục tiêu":** "Xóa" một bản ghi (row) khỏi một bảng (table) trong cơ sở dữ liệu.
-   **"Cách thực hiện" với EF Core:**

    1.  **"Tìm" "món đồ" (Entity) cần "xóa"** từ database (ví dụ: bằng `dbContext.SanPhams.Find(id)` hoặc LINQ queries).
    2.  **"Xóa" "món đồ" khỏi `DbSet<TEntity>`** tương ứng (ví dụ: `dbContext.SanPhams.Remove(sanPhamCanXoa)`). "Chiêu" `Remove()` sẽ "đánh dấu" đối tượng `sanPhamCanXoa` là cần "xóa".
    3.  "Gọi" phương thức **`dbContext.SaveChanges()`** để **"lưu"** các "thay đổi" (thao tác "xóa") vào cơ sở dữ liệu. EF Core sẽ "tự động" "phát lệnh" `DELETE` statement để "xóa" bản ghi khỏi bảng.

-   **Ví dụ code "xóa" sản phẩm khỏi database:**

    ```csharp
    using (var dbContext = new MyDbContext()) // "Mở" "trạm trung chuyển" Data Context
    {
        // 1. "Tìm" sản phẩm cần "xóa" (ví dụ: theo SanPhamId = 4)
        var sanPhamCanXoa = dbContext.SanPhams.Find(4); // "Tìm" sản phẩm có SanPhamId == 4

        if (sanPhamCanXoa != null) // "Kiểm tra" xem có "tìm" thấy sản phẩm không
        {
            // 2. "Xóa" "món đồ" SanPham khỏi DbSet<SanPham> (bảng SanPhams)
            dbContext.SanPhams.Remove(sanPhamCanXoa); // "Đánh dấu" 'sanPhamCanXoa' là cần "xóa" - chưa "xóa" khỏi database

            // 3. "Lưu" thay đổi vào database (thực thi DELETE statement)
            dbContext.SaveChanges(); // "Lệnh" EF Core "lưu" các "thay đổi" vào database - DELETE statement được "gửi" đi

            Console.WriteLine($"Đã xóa sản phẩm: {sanPhamCanXoa.TenSanPham}"); // Thông báo "xóa thành công"
        }
        else
        {
            Console.WriteLine("Không tìm thấy sản phẩm có ID = 4 để xóa."); // Thông báo "không tìm thấy" sản phẩm để xóa
        }
    }
    ```

-   **"Giải mã" code "xóa" dữ liệu:**

    -   `var sanPhamCanXoa = dbContext.SanPhams.Find(4);`: "Tìm" đối tượng `SanPham` cần "xóa" bằng `Find(4)`.
    -   `dbContext.SanPhams.Remove(sanPhamCanXoa)`: "Xóa" đối tượng `sanPhamCanXoa` khỏi `DbSet<SanPham>`. Lúc này, EF Core **"đánh dấu"** đối tượng `sanPhamCanXoa` là cần **"xóa"**, nhưng **chưa "xóa" khỏi database** ngay.
    -   `dbContext.SaveChanges()`: "Lệnh" EF Core "thực sự" "xóa" các "thay đổi" vào database. EF Core sẽ "phát hiện" thao tác "xóa" và "phát lệnh" câu lệnh `DELETE` SQL để "xóa" bản ghi tương ứng khỏi bảng `SanPhams`.

**Tổng Kết Chương 3:**

-   Bạn đã "nắm vững" các "chiêu thức" **CRUD Operations** "cơ bản" nhất để "thao tác" dữ liệu với EF Core:
    -   **Create (Thêm):** `dbContext.SanPhams.Add()`, `dbContext.SaveChanges()`
    -   **Read (Đọc):** `dbContext.SanPhams.ToList()`, `dbContext.SanPhams.Where()...`, `dbContext.SanPhams.FirstOrDefault()...` (LINQ queries)
    -   **Update (Sửa):** `dbContext.SanPhams.Find()`, "thay đổi" properties, `dbContext.SaveChanges()`
    -   **Delete (Xóa):** `dbContext.SanPhams.Find()`, `dbContext.SanPhams.Remove()`, `dbContext.SaveChanges()`

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: "Mối Quan Hệ" Giữa Các Bảng (Relationships) - "Gắn Kết" Dữ Liệu**. Chúng ta sẽ "khám phá" cách EF Core "quản lý" các "mối quan hệ" phổ biến giữa các bảng trong database (một-một, một-nhiều, nhiều-nhiều) và cách "truy vấn" dữ liệu "liên quan" một cách "hiệu quả".

Bạn có câu hỏi nào về các thao tác CRUD "cơ bản" này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "cùng bạn" "làm chủ" EF Core.
