# Chương 7: Tối Ưu Hiệu Năng EF Core - "Chạy Nhanh Như Chớp" Với Database - "Bí Kíp" "Gia Tốc" Ứng Dụng EF Core

Chào mừng bạn đến với **Chương 7: Tối Ưu Hiệu Năng EF Core**! Trong chương này, chúng ta sẽ "khám phá" các "bí quyết" và "chiến lược" để **"tăng tốc"** ứng dụng EF Core của bạn, giúp ứng dụng "chạy nhanh", "mượt mà", và "tiết kiệm" tài nguyên database. "Hiệu năng" là một yếu tố "quan trọng" để "đánh giá" chất lượng của bất kỳ ứng dụng nào, và EF Core cũng không ngoại lệ.

**Phần 7: Tối Ưu Hiệu Năng EF Core - "Chạy Nhanh Như Chớp" Với Database**

**7.1. "Tránh" Truy Vấn "Thừa Thãi" (Select N+1 Problem) - "Tối Ưu" Cách "Tải" Dữ Liệu Liên Quan - "Không 'Tham Lam' "**

-   **"Vấn đề" N+1 Query Problem - "Truy Vấn 'Vòng Lặp' ", "Chậm Chạp" và "Tốn Kém":**

    -   **N+1 Query Problem** là một "vấn đề" "hiệu năng" "phổ biến" trong ORM (như EF Core) khi bạn "truy vấn" dữ liệu **"liên quan"** (ví dụ: quan hệ Một-Nhiều).
    -   "Tình huống" "xảy ra" khi bạn:
        1.  "Truy vấn" một "danh sách" các đối tượng "chính" (ví dụ: "lấy" danh sách `DanhMucs`).
        2.  Sau đó, trong vòng lặp, bạn "truy cập" vào navigation property của **từng** đối tượng "chính" để "lấy" dữ liệu **"liên quan"** (ví dụ: `danhMuc.SanPhams` để "lấy" danh sách `SanPhams` thuộc `DanhMuc` đó).
        3.  EF Core sẽ "phát sinh" **1 truy vấn database ban đầu** để "lấy" danh sách đối tượng "chính", và sau đó **"thêm N truy vấn database 'lẻ tẻ' "** để "tải" dữ liệu "liên quan" cho **từng** đối tượng "chính" (với N là số lượng đối tượng "chính").
        4.  Tổng cộng, bạn sẽ có **N+1 truy vấn database** (1 truy vấn "chính" và N truy vấn "phụ"), thay vì chỉ **1 truy vấn** "duy nhất" nếu "tải" dữ liệu "liên quan" một cách "hiệu quả".
        5.   N+1 Query Problem làm **"chậm" ứng dụng**, "tăng" tải cho database server, và "lãng phí" tài nguyên.

-   **"Giải pháp" "tránh" N+1 Query Problem - "Tải Dữ Liệu Liên Quan" "Hợp Lý":**

    -   **Eager Loading (`Include` và `ThenInclude`) - "Tải Dữ Liệu 'Háo Hức' " (như đã "học" ở Chương 4):**

        -   "Dùng" "chiêu" `Include` (và `ThenInclude` cho quan hệ "nhiều tầng") trong LINQ queries để "ra lệnh" cho EF Core **"tải" dữ liệu "chính" và dữ liệu "liên quan" "cùng một lúc" trong **một truy vấn duy nhất**.
        -   "Tránh" được N+1 query problem, "tăng" "hiệu năng" khi bạn "biết" trước là mình sẽ cần dữ liệu "liên quan".

        ```csharp
        // Eager Loading: "Tải" DanhMucs "cùng lúc" với SanPhams (tránh N+1 query problem)
        var danhSachDanhMuc_EagerLoading = dbContext.DanhMucs
                                                .Include(dm => dm.SanPhams) // "Ra lệnh" Eager Loading: "tải" luôn SanPhams
                                                .ToList(); // "Lấy" danh sách DanhMucs và SanPhams "liên quan" trong **1 truy vấn**

        foreach (var dm in danhSachDanhMuc_EagerLoading) // Duyệt qua danh sách DanhMucs
        {
            Console.WriteLine($"Danh mục: {dm.TenDanhMuc}");
            foreach (var sp in dm.SanPhams) // "Truy cập" SanPhams "liên quan" - dữ liệu đã được "tải sẵn", không có truy vấn database "lẻ tẻ" nào nữa
            {
                Console.WriteLine($"- {sp.TenSanPham}");
            }
        }
        ```

    -   **Explicit Loading (Tải Dữ Liệu "Rõ Ràng"):**

        -   "Tải" dữ liệu "liên quan" một cách **"rõ ràng"** và **"linh hoạt"** khi bạn **"thực sự"** "cần" chúng, bằng cách dùng các "chiêu" `DbContext.Entry(entity).Collection(navigationProperty).Load()` (cho quan hệ 1-nhiều) hoặc `DbContext.Entry(entity).Reference(navigationProperty).Load()` (cho quan hệ 1-1).
        -   "Phù hợp" khi bạn muốn "tải" dữ liệu "liên quan" **"có điều kiện"** hoặc **"theo yêu cầu"** (ví dụ: chỉ "tải" dữ liệu "liên quan" khi người dùng "bấm" vào một button "Xem chi tiết").

        ```csharp
        // Explicit Loading: "Tải" SanPhams "liên quan" đến DanhMuc "một cách rõ ràng" (khi cần)
        var danhMuc_DienTu = dbContext.DanhMucs.FirstOrDefault(dm => dm.TenDanhMuc == "Điện tử"); // "Lấy" "danh mục" "Điện tử" (chỉ tải dữ liệu DanhMuc, chưa tải SanPhams)

        if (danhMuc_DienTu != null) // "Kiểm tra" xem có "tìm" thấy DanhMuc không
        {
            Console.WriteLine($"Danh mục: {danhMuc_DienTu.TenDanhMuc}");

            // "Tải" SanPhams "liên quan" đến DanhMuc "Điện tử" "một cách rõ ràng" (Explicit Loading)
            dbContext.Entry(danhMuc_DienTu) // "Lấy" Entry của đối tượng danhMuc_DienTu trong Change Tracker
                       .Collection(dm => dm.SanPhams) // "Chọn" navigation property Collection SanPhams (quan hệ 1-nhiều)
                       .Load(); // "Ra lệnh" Explicit Loading: "tải" dữ liệu "liên quan" ngay bây giờ

            Console.WriteLine("--- Sản phẩm thuộc danh mục (Explicit Loading) ---");
            foreach (var sp in danhMuc_DienTu.SanPhams) // "Truy cập" SanPhams "liên quan" - dữ liệu đã được Explicit Loading, không có truy vấn database "lẻ tẻ"
            {
                Console.WriteLine($"- {sp.TenSanPham}");
            }
        }
        ```

    -   **Lazy Loading (Tải Dữ Liệu "Lười Biếng"):**

        -   Để EF Core "tự động" "tải" dữ liệu "liên quan" khi bạn "truy cập" vào navigation properties (nhưng cần "kích hoạt" Lazy Loading và "cẩn thận" N+1 query problem - như đã "bàn" ở Chương 5 về LINQ to Entities).

**7.2. "Sử Dụng" Indexing - "Tăng Tốc" Truy Vấn Database - "Đường Cao Tốc" Cho Dữ Liệu**

-   **"Vấn đề": Truy Vấn Chậm Chạp Trên Bảng Lớn - "Tìm Kim Đáy Bể" Khi Không Có Index:**

    -   Khi bạn "truy vấn" dữ liệu trên các bảng database có **"hàng triệu"** hoặc **"hàng tỷ"** bản ghi, các truy vấn có thể trở nên **"chậm chạp"** "kinh khủng" nếu database phải "lục tung" **"toàn bộ"** bảng để "tìm kiếm" dữ liệu (full table scan).
    -   Tưởng tượng như bạn đang "tìm kim đáy bể" trong một "đống rơm khổng lồ" mà không có "bản đồ" hay "chỉ dẫn" nào.

-   **Indexing - "Giải Pháp" "Tăng Tốc" Truy Vấn - "Bản Đồ" "Chỉ Đường" Cho Database:**

    -   **Indexing** (chỉ mục) trong database là một "kỹ thuật" giúp **"tăng tốc"** "hiệu năng" truy vấn bằng cách "tạo ra" một **"cấu trúc dữ liệu" "đặc biệt"** (index) cho một hoặc nhiều cột trong bảng.
    -   Index giống như một **"bản đồ"** hoặc **"mục lục"** giúp database "nhanh chóng" "tìm" đến các bản ghi "thỏa mãn" "điều kiện" truy vấn, **"không cần"** "quét" "toàn bộ" bảng.

-   **"Khi nào" nên "sử dụng" Indexing? - "Nhắm Trúng" "Điểm Yếu" "Hiệu Năng":**

    -   **"Xác định" các cột thường xuyên được "dùng" trong mệnh đề `WHERE` (điều kiện lọc), `ORDER BY` (sắp xếp), `JOIN` (kết hợp bảng) của các truy vấn LINQ (hoặc SQL).**
    -   **"Tạo" index cho các cột đó trong database.**
    -   **"Theo dõi" "hiệu năng" truy vấn** sau khi "tạo" index để "đánh giá" "lợi ích" mà index mang lại.

-   **"Cách tạo" Index trong database (ví dụ SQL Server):**

    -   **SQL Server Management Studio (SSMS) - "Giao Diện" "Trực Quan":**
        1.  "Kết nối" đến database server bằng SSMS.
        2.  "Mở rộng" database, "Tables", "chọn" bảng bạn muốn "tạo" index.
        3.  "Chuột phải" vào "Indexes", chọn "New Index", chọn "Non-Clustered Index..." (thường dùng index non-clustered).
        4.  Trong hộp thoại "New Index", "đặt tên" index, "chọn" các cột bạn muốn "đưa" vào index (Index key columns), và "cấu hình" các "tùy chọn" index khác (nếu cần).
        5.  Bấm "OK" để "tạo" index.

    -   **Tạo Migration trong EF Core (Code-First Approach) - "Tạo Index" "Bằng Code":**

        ```csharp
        using Microsoft.EntityFrameworkCore;

        public class MyDbContext : DbContext
        {
            public DbSet<SanPham> SanPhams { get; set; }
            public DbSet<DanhMuc> DanhMucs { get; set; }

            protected override void OnModelCreating(ModelBuilder modelBuilder)
            {
                // ... (cấu hình quan hệ) ...

                // "Tạo" index cho cột "DanhMucSanPham" trong bảng "SanPhams" bằng Fluent API
                modelBuilder.Entity<SanPham>()
                    .HasIndex(sp => sp.DanhMucSanPham); // "Ra lệnh" EF Core "tạo" index cho cột DanhMucSanPham

                // "Tạo" index "kết hợp" (composite index) cho cột "TenSanPham" và "Gia" trong bảng "SanPhams"
                modelBuilder.Entity<SanPham>()
                    .HasIndex(sp => new { sp.TenSanPham, sp.Gia }); // "Ra lệnh" EF Core "tạo" composite index cho 2 cột TenSanPham và Gia
            }

            protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
            {
                optionsBuilder.UseSqlServer("Server=(localdb)\\mssqllocaldb;Database=MyDatabase;Trusted_Connection=True;");
            }
        }
        ```

        Sau khi "thêm" code "tạo index" vào `OnModelCreating`, bạn cần **"tạo" và "áp dụng" Migration mới** để EF Core "tạo" index trong database:

        ```powershell
        Add-Migration AddSanPhamIndexes
        Update-Database
        ```

-   **"Lưu ý" khi "sử dụng" Indexing:**

    -   **"Không phải cứ 'thêm' index là 'tốt' ":** Index giúp "tăng tốc" "truy vấn" `SELECT`, nhưng có thể làm **"chậm"** các thao tác **"thay đổi" dữ liệu** (INSERT, UPDATE, DELETE), vì database phải "cập nhật" index mỗi khi dữ liệu thay đổi.
    -   **"Chọn lọc" cột để index:** Chỉ "tạo" index cho các cột **thực sự** cần thiết (thường xuyên được "dùng" để "lọc", "sắp xếp", "kết hợp"). "Tránh" "tạo" index "vô tội vạ" cho "tất cả" các cột.
    -   **"Theo dõi" "hiệu năng" truy vấn** để "đánh giá" "lợi ích" của index và "tinh chỉnh" index khi cần.

**7.3. AsNoTracking - "Đọc Dữ Liệu" "Siêu Nhanh" (Khi Không Cần "Theo Dõi" Thay Đổi) - "Đọc Nhanh, Không 'Vướng Bận' "**

-   **"Vấn đề": Change Tracking (Theo Dõi Thay Đổi) - "Gánh Nặng" Khi "Chỉ Đọc" Dữ Liệu:**

    -   EF Core có một cơ chế gọi là **Change Tracking (Theo Dõi Thay Đổi)**, giúp nó "theo dõi" các "thay đổi" (thêm, sửa, xóa) của các Entities mà bạn đã "lấy" từ database. Khi bạn gọi `SaveChanges()`, EF Core sẽ "dựa vào" Change Tracking để "biết" những "thay đổi" nào cần "lưu" vào database.
    -   Change Tracking là một "tính năng" **"hữu ích"** khi bạn muốn **"sửa đổi"** dữ liệu và "lưu" lại vào database.
    -   Tuy nhiên, khi bạn **"chỉ" "đọc" dữ liệu** từ database (ví dụ: để "hiển thị" dữ liệu lên giao diện người dùng, "báo cáo", "thống kê" - các truy vấn **"read-only"**), **Change Tracking trở thành một "gánh nặng" "không cần thiết"**. EF Core vẫn phải "tốn công" "theo dõi" các Entities đã "lấy" về, dù bạn không có ý định "sửa đổi" chúng. Điều này có thể làm "chậm" "hiệu năng" truy vấn, đặc biệt khi "lấy" "lượng dữ liệu lớn".

-   **`AsNoTracking()` - "Giải Phóng" Khỏi "Gánh Nặng" Change Tracking - "Đọc Nhanh Như Gió":**

    -   **`AsNoTracking()`** là một "chiêu" LINQ trong EF Core, "ra lệnh" cho EF Core là **"hãy 'quên' Change Tracking đi"** trong truy vấn này. Khi bạn "dùng" `AsNoTracking()`, EF Core sẽ **"không" "theo dõi"** các Entities mà bạn "lấy" về từ database.
    -   `AsNoTracking()` giúp **"tăng tốc"** "hiệu năng" truy vấn **"chỉ đọc"** dữ liệu một cách "đáng kể", vì EF Core không cần "tốn công" "theo dõi" các Entities.

-   **"Cách dùng" `AsNoTracking()`:** "Thêm" "chiêu" `.AsNoTracking()` vào "đuôi" truy vấn LINQ của bạn (trước các "chiêu" "thực thi" như `ToList()`, `FirstOrDefault()`, v.v.).

    ```csharp
    // "Truy vấn" sản phẩm và "tắt" Change Tracking bằng AsNoTracking() - "đọc nhanh" hơn
    var danhSachSanPham_AsNoTracking = dbContext.SanPhams // "Bắt đầu" truy vấn
                                                 .AsNoTracking() // "Ra lệnh" "tắt" Change Tracking
                                                 .ToList(); // "Lấy" kết quả dạng List<SanPham> - "nhanh hơn" vì không có Change Tracking

    Console.WriteLine("\n--- Sản phẩm (AsNoTracking) ---");
    foreach (var sp in danhSachSanPham_AsNoTracking) // Duyệt qua danh sách sản phẩm
    {
        Console.WriteLine($"- {sp.TenSanPham}, Giá: {sp.Gia:#,##0}"); // In ra thông tin sản phẩm
    }
    ```

-   **"Khi nào" nên "dùng" `AsNoTracking()`? - "Khi 'Chỉ Đọc' Dữ Liệu" và "Ưu Tiên" "Tốc Độ":**

    -   **"Ưu tiên" "dùng" `AsNoTracking()` cho các truy vấn "chỉ đọc" dữ liệu** (read-only queries) khi bạn **"không có ý định" "sửa đổi"** các Entities "lấy" về và "lưu" lại vào database. Ví dụ:
        -   "Hiển thị" dữ liệu lên giao diện người dùng.
        -   "Báo cáo", "thống kê", "phân tích" dữ liệu.
        -   "Export" dữ liệu ra file.

    -   **"Không dùng" `AsNoTracking()` khi bạn muốn "sửa đổi" dữ liệu** sau khi "lấy" về (vì EF Core sẽ không "theo dõi" "thay đổi" của các Entities `AsNoTracking`).

**7.4. "Xem Xét Sử Dụng" PLINQ Khi Phù Hợp (như đã "bàn" ở Chương 6 về PLINQ) - "Tăng Tốc" Truy Vấn Với "Đa Luồng"**

-   **Parallel LINQ (PLINQ) - "Chiến Binh" "Tăng Tốc" Truy Vấn "Đa Luồng":**

    -   Như đã "khám phá" ở Chương 6 về PLINQ, **Parallel LINQ (PLINQ)** có thể giúp **"tăng tốc"** các truy vấn LINQ bằng cách "chạy" chúng **"song song"** trên nhiều luồng (threads), "tận dụng" "sức mạnh" của bộ vi xử lý "đa nhân".
    -   PLINQ có thể "hữu ích" để "tăng tốc" các truy vấn EF Core **"phức tạp"** và **"ngốn CPU"**, đặc biệt khi "xử lý" "lượng dữ liệu lớn".

-   **"Cách dùng" PLINQ với EF Core:** "Thêm" "chiêu" `.AsParallel()` vào "giữa" hoặc "đầu" truy vấn LINQ của bạn.

    ```csharp
    // "Truy vấn" sản phẩm và "tăng tốc" bằng PLINQ - "chạy song song" "nếu có thể"
    var danhSachSanPham_PLINQ = dbContext.SanPhams // "Bắt đầu" truy vấn
                                             .AsParallel() // "Bật chế độ" PLINQ - "chạy song song"
                                             .Where(sp => sp.Gia > 500) // "Lọc" sản phẩm giá > 500
                                             .OrderByDescending(sp => sp.TenSanPham) // "Sắp xếp" theo "tên sản phẩm" giảm dần
                                             .ToList(); // "Lấy" kết quả

    Console.WriteLine("\n--- Sản phẩm giá > 500 (PLINQ) ---");
    foreach (var sp in danhSachSanPham_PLINQ) // Duyệt qua kết quả
    {
        Console.WriteLine($"- {sp.TenSanPham}, Giá: {sp.Gia:#,##0}");
    }
    ```

-   **"Lưu ý" khi "dùng" PLINQ với EF Core (tương tự như "lưu ý" về PLINQ ở Chương 6):**

    -   **"Không phải lúc nào" PLINQ cũng "tăng tốc":** PLINQ có thể "giảm" "hiệu năng" nếu truy vấn quá "nhanh" hoặc "nghẽn cổ chai" I/O (ví dụ: database server "chậm"). "Benchmark" (đo "tốc độ") để "kiểm chứng" "lợi ích" của PLINQ trong từng trường hợp cụ thể.
    -   **"Cẩn thận" với "tác dụng phụ" và "thứ tự":** "Tránh" "tác dụng phụ" trong lambda expressions của PLINQ. "Thứ tự" kết quả có thể "không được đảm bảo" (trừ khi dùng `.AsOrdered()`, nhưng có thể "giảm" "hiệu năng" song song).

**Tổng Kết Chương 7:**

-   Bạn đã "bỏ túi" các "bí kíp" và "chiến lược" "tối ưu hóa" "hiệu năng" EF Core:
    -   "Tránh" N+1 Query Problem bằng Eager Loading và Explicit Loading - "tải dữ liệu 'liên quan' " "thông minh".
    -   "Sử dụng" Indexing trong database - "tạo 'đường cao tốc' " cho truy vấn.
    -   "Dùng" `AsNoTracking()` cho truy vấn "chỉ đọc" - "đọc nhanh" hơn, "nhẹ gánh" Change Tracking.
    -   "Xem xét" "bật chế độ" PLINQ (`AsParallel()`) khi "phù hợp" để "tăng tốc" truy vấn "đa luồng".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 8: Ứng Dụng Thực Tế Của Entity Framework Core - "EF Core Đi Muôn Nơi"**. Chúng ta sẽ "thấy" EF Core "tung hoành" trong các "ứng dụng" "thực tế", từ ứng dụng console "đơn giản" đến ứng dụng web và desktop "hoành tráng" hơn.

Bạn có câu hỏi nào về "tối ưu hiệu năng" EF Core này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "cùng bạn" "trở thành" "chuyên gia" EF Core "hiệu năng cao".

