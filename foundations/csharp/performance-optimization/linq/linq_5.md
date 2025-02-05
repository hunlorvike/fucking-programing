## **Chương 5: LINQ to SQL/Entities - Kết Nối Với Cơ Sở Dữ Liệu - "Nói Chuyện" Với Database Bằng LINQ**

Chào mừng bạn đến với **Chương 5: LINQ to SQL/Entities**! Trong chương này, chúng ta sẽ "bước vào" thế giới cơ sở dữ
liệu và học cách dùng LINQ để "bắt nhịp" với chúng, "nói chuyện" với cơ sở dữ liệu bằng ngôn ngữ LINQ "thân thiện" thay
vì SQL "khô khan".

**Phần 5: LINQ to SQL/Entities (LINQ to Database) - "Bắt Nhịp" Với Cơ Sở Dữ Liệu**

**5.1. Giới thiệu LINQ to SQL và Entity Framework (EF Core) - "Cầu Nối" LINQ Và Database**

- **LINQ to SQL (Dự án "tiền bối"):** Là "người mở đường" cho LINQ trong việc "truy vấn" cơ sở dữ liệu, ban đầu được
  thiết kế để "hợp tác" với cơ sở dữ liệu SQL Server. Nó giúp bạn viết các câu truy vấn LINQ và "dịch" chúng thành SQL
  để "chạy" trên SQL Server. Tuy nhiên, LINQ to SQL giờ đã "về hưu" - **không còn được "chăm sóc"** nữa và chỉ "biết"
  mỗi SQL Server.

- **Entity Framework (EF) và Entity Framework Core (EF Core):** Là những "chiến binh" ORM (Object-Relational Mapper) "
  mạnh mẽ" và "linh hoạt" của Microsoft, "kế thừa" và "phát triển" ý tưởng từ LINQ to SQL.
    - **ORM (Object-Relational Mapper):** Nghe "lạ tai" nhỉ? Nhưng nó chỉ là một "kỹ thuật" giúp bạn "bắc cầu" giữa **"
      thế giới đối tượng"** trong code C# của bạn (các class, đối tượng) và **"thế giới quan hệ"** trong cơ sở dữ liệu (
      bảng, cột...). ORM giúp bạn "làm việc" với cơ sở dữ liệu bằng các đối tượng C# "quen thuộc" thay vì viết SQL "lằng
      nhằng", giúp code "dễ thở", "dễ bảo trì" và "an toàn" về kiểu dữ liệu.
    - **EF Core** là phiên bản **"hiện đại"**, **"mã nguồn mở"**, **"đa nền tảng"** (chạy được trên nhiều hệ điều hành)
      của Entity Framework, đang được Microsoft và cộng đồng "chăm sóc" "tận răng". Nó "hỗ trợ" nhiều loại cơ sở dữ liệu
      khác nhau (SQL Server, MySQL, PostgreSQL, SQLite, v.v.).

**Vì sao nên "bắt tay" với LINQ to Database (qua EF Core)?**

- **"Truy vấn" dữ liệu bằng LINQ:** Dùng cú pháp LINQ "quen thuộc" để "hỏi han" dữ liệu từ cơ sở dữ liệu, thay vì viết
  SQL "dài dằng dặc".
- **"An toàn" kiểu dữ liệu và "bắt lỗi" sớm:** Truy vấn LINQ được "kiểm tra" kiểu dữ liệu ngay khi bạn viết code (lúc
  biên dịch), giúp "tóm" lỗi sớm và giảm "tai nạn" khi chương trình "lăn bánh" (runtime).
- **Code "dễ đọc", "dễ thở" và "dễ bảo trì":** Code truy vấn LINQ thường "gọn gàng", "dễ hiểu" hơn SQL "khô khan", đặc
  biệt là các truy vấn "phức tạp".
- **"Trừu tượng hóa" việc "nói chuyện" với database:** ORM giúp bạn "giấu nhẹm" đi những "rắc rối" khi "giao tiếp" với
  cơ sở dữ liệu. Bạn chỉ cần "làm việc" với các đối tượng C# và LINQ, còn EF Core sẽ "lo liệu" phần "dịch" sang SQL, "
  quản lý" kết nối, "giao dịch" (transactions), v.v.
- **"Chiều" nhiều loại database:** EF Core "hợp tác" với nhiều hệ quản trị cơ sở dữ liệu (DBMS), giúp bạn "dễ dàng" "
  chuyển nhà" giữa các DBMS nếu "đổi ý" (dù vẫn có thể có những "khác biệt nhỏ" về "ngôn ngữ SQL địa phương").

**Trong chương này, chúng ta sẽ "tập trung" vào sử dụng LINQ với **Entity Framework Core (EF Core)**, "chiến binh" ORM "
đỉnh cao" hiện nay.**

**5.2. Thiết lập kết nối cơ sở dữ liệu và tạo Data Context - "Chuẩn Bị Sân Khấu" Cho LINQ Và Database**

Để "bắt đầu" dùng EF Core, bạn cần "chuẩn bị" một số thứ:

1. **"Rinh về" NuGet Packages:** Cài đặt các "gói" NuGet cần thiết cho EF Core và "nhà cung cấp" cơ sở dữ liệu mà bạn
   muốn "kết nối" (ví dụ: SQL Server, MySQL). Ví dụ, cho SQL Server:

   ```bash
   Install-Package Microsoft.EntityFrameworkCore.SqlServer
   Install-Package Microsoft.EntityFrameworkCore.Tools
   ```

2. **"Vẽ" Entities (Classes "ánh xạ" bảng):** Tạo các class C# để "đại diện" cho các bảng trong cơ sở dữ liệu của bạn.
   Các class này thường được gọi là **Entities**. Mỗi "thuộc tính" (property) trong class sẽ "ứng với" một "cột" (
   column) trong bảng.

   ```csharp
   public class SanPham // Class "đại diện" cho bảng SanPham
   {
       public int SanPhamId { get; set; } // "Khóa chính" (tên theo "luật": <ClassName>Id hoặc Id) - "cột" SanPhamId trong bảng
       public string TenSanPham { get; set; } // "Cột" TenSanPham trong bảng
       public decimal Gia { get; set; }      // "Cột" Gia trong bảng
       public string DanhMucSanPham { get; set; } // "Cột" DanhMucSanPham trong bảng
   }

   public class DonHang // Class "đại diện" cho bảng DonHang
   {
       public int DonHangId { get; set; } // "Khóa chính" - "cột" DonHangId
       public DateTime NgayDatHang { get; set; } // "Cột" NgayDatHang
       // ... các thuộc tính khác tương ứng với các cột khác trong bảng DonHang

       // "Quan hệ" 1-n với SanPham (mỗi DonHang có nhiều DonHangChiTiet)
       public ICollection<DonHangChiTiet> DonHangChiTiets { get; set; } // Danh sách DonHangChiTiet liên quan đến DonHang này
   }

   public class DonHangChiTiet // Class "đại diện" cho bảng DonHangChiTiet (bảng "chi tiết" của DonHang)
   {
       public int DonHangChiTietId { get; set; } // "Khóa chính" - "cột" DonHangChiTietId
       public int DonHangId { get; set; }      // "Khóa ngoại" - "cột" DonHangId (liên kết đến bảng DonHang)
       public int SanPhamId { get; set; }      // "Khóa ngoại" - "cột" SanPhamId (liên kết đến bảng SanPham)
       public int SoLuong { get; set; }        // "Cột" SoLuong

       // Navigation properties (để "đi lại" giữa các đối tượng liên quan)
       public DonHang DonHang { get; set; }       // Đối tượng DonHang liên quan
       public SanPham SanPham { get; set; }       // Đối tượng SanPham liên quan
   }
   ```

3. **"Dựng" Data Context (DbContext):** Tạo một class "kế thừa" từ `DbContext`. `DbContext` là "trái tim" của EF Core,
   đóng vai trò như một **"trạm trung chuyển"** giữa code của bạn và cơ sở dữ liệu, và cũng là một **"kho chứa"** các
   entities của bạn. Trong `DbContext`, bạn sẽ "khai báo" các `DbSet<TEntity>` properties, mỗi `DbSet` "đại diện" cho
   một bảng trong cơ sở dữ liệu.

   ```csharp
   using Microsoft.EntityFrameworkCore; // "Nhập" không gian tên của EF Core

   public class CuaHangDbContext : DbContext // Class Data Context "kế thừa" từ DbContext
   {
       public DbSet<SanPham> SanPhams { get; set; } // DbSet "đại diện" cho bảng SanPham
       public DbSet<DonHang> DonHangs { get; set; }   // DbSet "đại diện" cho bảng DonHang
       public DbSet<DonHangChiTiet> DonHangChiTiets { get; set; } // DbSet "đại diện" cho bảng DonHangChiTiet

       protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder) // "Cấu hình" kết nối database
       {
           // "Cài đặt" connection string và "nhà cung cấp" cơ sở dữ liệu
           optionsBuilder.UseSqlServer("Server=.\\SQLEXPRESS;Database=CuaHangDB;Trusted_Connection=True;"); // Ví dụ cho SQL Server LocalDB - "chỉ đường" đến database của bạn
       }

       // (Tùy chọn) Có thể "cấu hình" thêm về "mối quan hệ" giữa các bảng (Fluent API) trong OnModelCreating
       protected override void OnModelCreating(ModelBuilder modelBuilder)
       {
           // Ví dụ: "Cấu hình" "khóa chính" cho DonHangChiTiet là "khóa kép" (DonHangId, SanPhamId)
           modelBuilder.Entity<DonHangChiTiet>()
               .HasKey(dhct => new { dhct.DonHangId, dhct.SanPhamId }); // "Khóa kép" gồm 2 cột

           // ... có thể "cấu hình" thêm các "mối quan hệ", "ràng buộc", v.v. giữa các bảng ở đây
       }
   }
   ```

**"Giải mã" code:**

- **`DbContext`:** Class "chính" để "giao tiếp" với cơ sở dữ liệu.
    - **`DbSet<SanPham> SanPhams`:** `DbSet<T>` là một "cổng giao tiếp" kiểu `IQueryable<T>` (họ hàng với
      `IEnumerable<T>`), "đại diện" cho một bảng trong cơ sở dữ liệu. `SanPhams` "đại diện" cho bảng `SanPhams`. Bạn
      sẽ "dùng" `SanPhams` để viết các câu truy vấn LINQ.
    - **`OnConfiguring(DbContextOptionsBuilder optionsBuilder)`:** "Phương thức" này dùng để "cài đặt" kết nối cơ sở dữ
      liệu.
        - `optionsBuilder.UseSqlServer(...)`: "Ra lệnh" cho EF Core là "hãy dùng SQL Server" làm "nhà cung cấp" cơ sở dữ
          liệu và "cung cấp" connection string (đường dẫn đến database). "Thay"
          `".\\SQLEXPRESS;Database=CuaHangDB;Trusted_Connection=True;"` bằng connection string "thật" của bạn.
    - **`OnModelCreating(ModelBuilder modelBuilder)` (tùy chọn):** "Phương thức" này dùng để "cấu hình" thêm về "mối
      quan hệ" giữa các bảng (ví dụ: "định nghĩa" "khóa chính" "khóa kép", "quan hệ" một-nhiều, "ràng buộc" dữ liệu,
      v.v.) bằng Fluent API (một cách viết code "mượt mà"). Nếu bạn không "cấu hình" gì thêm, EF Core sẽ "tự động" "
      đoán" cấu hình dựa trên "luật lệ" (conventions).

**5.3. Truy vấn dữ liệu từ cơ sở dữ liệu bằng LINQ - "Hỏi Han" Database Với LINQ**

Sau khi có `DbContext` và các `DbSet` properties, bạn có thể "tung hoành" với LINQ queries trực tiếp trên các `DbSet`
để "hỏi han" dữ liệu từ cơ sở dữ liệu.

```csharp
using (var dbContext = new CuaHangDbContext()) // Tạo "trạm trung chuyển" DbContext (using để đảm bảo "dọn dẹp" sau khi dùng xong)
{
    // 1. "Lấy" danh sách "tất cả" sản phẩm (LINQ Query Syntax) - "Hỏi" database: "Cho tôi xem hết sản phẩm đi!"
    var danhSachSanPham_Query = from sp in dbContext.SanPhams // "Từ" "kho" sản phẩm (DbSet<SanPham> - bảng SanPhams trong database)
                                 select sp; // "Chọn" hết sản phẩm

    foreach (var sp in danhSachSanPham_Query) // Duyệt qua kết quả "hỏi han"
    {
        Console.WriteLine($"Tên SP: {sp.TenSanPham}, Giá: {sp.Gia}"); // In ra thông tin sản phẩm
    }

    // 2. "Lấy" danh sách sản phẩm có "giá" "cao hơn" 1000 (LINQ Method Syntax) - "Hỏi" database: "Sản phẩm nào giá 'chát' hơn 1000?"
    var sanPhamGiaHon1000_Method = dbContext.SanPhams // "Kho" sản phẩm
                                        .Where(sp => sp.Gia > 1000) // "Lọc": chỉ lấy sản phẩm có "giá" > 1000
                                        .OrderByDescending(sp => sp.Gia) // "Sắp xếp": theo "giá" giảm dần (đắt nhất lên đầu)
                                        .ToList(); // "Ép" truy vấn "chạy" và "đổ" kết quả vào List<SanPham> ("lấy" kết quả "ngay và luôn" - Immediate Execution)

    Console.WriteLine("\nSản phẩm giá > 1000 (Method Syntax):");
    foreach (var sp in sanPhamGiaHon1000_Method) // Duyệt qua kết quả "hỏi han"
    {
        Console.WriteLine($"Tên SP: {sp.TenSanPham}, Giá: {sp.Gia}"); // In ra thông tin sản phẩm "đắt tiền"
    }

    // 3. "Lấy" "tổng số lượng" sản phẩm trong "danh mục" "Điện tử" - "Hỏi" database: "Điện tử có bao nhiêu 'món'?"
    int soLuongSP_DienTu = dbContext.SanPhams // "Kho" sản phẩm
                                    .Where(sp => sp.DanhMucSanPham == "Điện tử") // "Lọc": chỉ lấy sản phẩm "danh mục" "Điện tử"
                                    .Count(); // "Đếm": số lượng sản phẩm đã "lọc" ("lấy" kết quả "đếm" - Immediate Execution)

    Console.WriteLine($"\nSố lượng sản phẩm 'Điện tử': {soLuongSP_DienTu}"); // In ra "số lượng"

    // 4. "Lấy" sản phẩm "đầu tiên" có "giá" "rẻ nhất" - "Hỏi" database: "Sản phẩm nào 'kinh tế' nhất?"
    SanPham sanPhamReNhat = dbContext.SanPhams // "Kho" sản phẩm
                                     .OrderBy(sp => sp.Gia) // "Sắp xếp": theo "giá" tăng dần (rẻ nhất lên đầu)
                                     .FirstOrDefault(); // "Lấy" "món đồ" "đầu tiên" (rẻ nhất), hoặc "không có gì" nếu "kho" rỗng ("lấy" kết quả "đầu tiên" - Immediate Execution)

    if (sanPhamReNhat != null) // Kiểm tra xem có "món đồ" nào không
    {
        Console.WriteLine($"\nSản phẩm rẻ nhất: {sanPhamReNhat.TenSanPham}, Giá: {sanPhamReNhat.Gia}"); // In ra thông tin sản phẩm "rẻ nhất"
    }
}
```

**"Lưu ý" quan trọng:**

- **`using (var dbContext = new CuaHangDbContext()) { ... }`:** Luôn "gói gọn" việc dùng `DbContext` trong khối `using`.
  Khi khối `using` "kết thúc", `dbContext.Dispose()` sẽ được "gọi" tự động, giúp "dọn dẹp" các "kết nối" cơ sở dữ liệu,
  tránh "rò rỉ" tài nguyên.
- **`dbContext.SanPhams`:** "Truy cập" `DbSet<SanPham>` để "bắt đầu" "hỏi han" bảng `SanPhams`.
- **`.ToList()`:** Là một "chiêu" **thực thi ngay lập tức (immediate execution)**. Khi bạn "triệu hồi" `.ToList()`, truy
  vấn LINQ sẽ được **"dịch" thành câu lệnh SQL và "gửi" đến cơ sở dữ liệu để "thực thi"**. Kết quả "trả về" là một
  `List<SanPham>` chứa các đối tượng `SanPham` được "lấy" từ database.
- **Deferred Execution (vẫn "hiện diện"):** Các "chiêu" như `Where`, `OrderBy`, `Select`... vẫn là **thực thi trì hoãn
  **. Truy vấn chỉ thực sự được "giao phó" cho database khi bạn "triệu hồi" các "chiêu" **thực thi ngay lập tức** như
  `ToList()`, `ToArray()`, `Count()`, `FirstOrDefault()`, v.v., hoặc khi bạn "bắt đầu" "xem" kết quả bằng `foreach`.
- **SQL Translation ("Dịch Thuật" Sang SQL):** EF Core sẽ **"tự động" "dịch" các câu truy vấn LINQ thành các câu lệnh
  SQL** "chuẩn chỉnh" với DBMS (hệ quản trị cơ sở dữ liệu) mà bạn đang dùng. Bạn không cần phải "động tay động chân"
  viết SQL trực tiếp.

**5.4. Thêm, sửa, xóa dữ liệu trong cơ sở dữ liệu bằng LINQ - "Thay Đổi" Database Với LINQ**

**5.4.1. Thêm dữ liệu - "Gửi Gắm" "Món Đồ" Mới Vào Database:**

- "Tạo ra" một "món đồ" mới (instance) của entity class (ví dụ: `SanPham`).
- "Gán" giá trị cho các "đặc điểm" (properties) của "món đồ" đó.
- Dùng `dbContext.Add(entity)` hoặc `dbContext.Set<TEntity>().Add(entity)` để "đưa" "món đồ" vào "trạm trung chuyển"
  `DbContext`.
- "Gọi" `dbContext.SaveChanges()` để "lưu" các "thay đổi" vào cơ sở dữ liệu.

```csharp
using (var dbContext = new CuaHangDbContext()) // "Trạm trung chuyển" DbContext
{
    // "Tạo ra" một sản phẩm mới
    var sanPhamMoi = new SanPham // "Món đồ" SanPham mới
    {
        TenSanPham = "Bàn phím cơ",
        Gia = 800,
        DanhMucSanPham = "Máy tính"
    };

    dbContext.SanPhams.Add(sanPhamMoi); // "Đưa" "món đồ" vào "trạm trung chuyển" DbSet<SanPham> (chưa "lưu" vào database)
    dbContext.SaveChanges();          // "Lệnh" "trạm trung chuyển" "lưu" thay đổi vào database (lúc này INSERT statement mới "chạy")

    Console.WriteLine($"\nĐã thêm sản phẩm mới: {sanPhamMoi.TenSanPham}, ID: {sanPhamMoi.SanPhamId}"); // SanPhamId "tự động" có giá trị sau SaveChanges (do database "tự sinh" khóa chính)
}
```

**5.4.2. Sửa dữ liệu - "Chỉnh Sửa" "Món Đồ" Đã Có Trong Database:**

- "Tìm" "món đồ" cần "chỉnh sửa" từ cơ sở dữ liệu (ví dụ: bằng `dbContext.SanPhams.Find(id)` hoặc dùng "chiêu" LINQ
  `Where().FirstOrDefault()`).
- "Thay đổi" giá trị của các "đặc điểm" (properties) của "món đồ" đã "tìm" thấy.
- "Gọi" `dbContext.SaveChanges()` để "lưu" các "thay đổi" vào cơ sở dữ liệu. EF Core sẽ "tự động" "nhận ra" các "thay
  đổi" và "phát lệnh" `UPDATE` statement.

```csharp
using (var dbContext = new CuaHangDbContext()) // "Trạm trung chuyển" DbContext
{
    // "Tìm" sản phẩm cần "chỉnh sửa" (ví dụ: theo SanPhamId = 1)
    var sanPhamCanSua = dbContext.SanPhams.Find(1); // "Tìm" theo "khóa chính" (SanPhamId = 1) - hoặc dùng LINQ Where().FirstOrDefault()

    if (sanPhamCanSua != null) // Nếu "tìm" thấy
    {
        sanPhamCanSua.Gia = 900; // "Chỉnh" "giá" mới
        sanPhamCanSua.DanhMucSanPham = "Phụ kiện máy tính"; // "Chỉnh" "danh mục" mới

        dbContext.SaveChanges(); // "Lưu" thay đổi vào database (lúc này UPDATE statement mới "ra đời")
        Console.WriteLine($"\nĐã sửa sản phẩm: {sanPhamCanSua.TenSanPham}, Giá mới: {sanPhamCanSua.Gia}"); // Thông báo "đã sửa"
    }
    else
    {
        Console.WriteLine("\nKhông tìm thấy sản phẩm để sửa."); // Thông báo nếu không "tìm" thấy
    }
}
```

**5.4.3. Xóa dữ liệu - "Dọn Dẹp" "Món Đồ" Khỏi Database:**

- "Tìm" "món đồ" cần "xóa sổ" khỏi cơ sở dữ liệu.
- Dùng `dbContext.Remove(entity)` hoặc `dbContext.Set<TEntity>().Remove(entity)` để "đánh dấu" "món đồ" cần "xóa".
- "Gọi" `dbContext.SaveChanges()` để "lưu" thay đổi vào cơ sở dữ liệu. EF Core sẽ "phát lệnh" `DELETE` statement.

```csharp
using (var dbContext = new CuaHangDbContext()) // "Trạm trung chuyển" DbContext
{
    // "Tìm" sản phẩm cần "xóa sổ" (ví dụ: theo SanPhamId = 2)
    var sanPhamCanXoa = dbContext.SanPhams.Find(2); // "Tìm" theo "khóa chính" (SanPhamId = 2) - hoặc dùng LINQ Where().FirstOrDefault()

    if (sanPhamCanXoa != null) // Nếu "tìm" thấy
    {
        dbContext.SanPhams.Remove(sanPhamCanXoa); // "Đánh dấu" "món đồ" cần "xóa" (chưa "xóa" khỏi database)
        dbContext.SaveChanges();                // "Lệnh" "trạm trung chuyển" "xóa" thay đổi vào database (lúc này DELETE statement mới "xuất hiện")
        Console.WriteLine($"\nĐã xóa sản phẩm: {sanPhamCanXoa.TenSanPham}"); // Thông báo "đã xóa"
    }
    else
    {
        Console.WriteLine("\nKhông tìm thấy sản phẩm để xóa."); // Thông báo nếu không "tìm" thấy
    }
}
```

**"Lưu ý" "ngàn vàng" về `SaveChanges()`:**

- `SaveChanges()` là "chiêu" **thực thi ngay lập tức (immediate execution)** các "thay đổi" (INSERT, UPDATE, DELETE) đã
  được "đánh dấu" trong `DbContext` và "gửi" chúng đến cơ sở dữ liệu trong một **"giao dịch" (transaction)**.
    - Nếu có "sự cố" xảy ra khi "lưu" (ví dụ: "vi phạm" "luật lệ" database), `SaveChanges()` sẽ **"quay xe"** (rollback
      transaction) và "nổi giận" (ném ra lỗi - exception).
    - `SaveChanges()` "trả về" "số lượng" "món đồ" bị "tác động" bởi các "thao tác" (số "hàng" được "thêm", "sửa", "
      xóa").

**5.5. Lazy Loading và Eager Loading trong LINQ to Entities - "Chọn Cách Tải Dữ Liệu Liên Quan"**

Khi "làm việc" với các "mối quan hệ" giữa các bảng trong cơ sở dữ liệu (ví dụ: một-nhiều, nhiều-nhiều), EF Core "mách
bạn" hai "bí kíp" để "tải" dữ liệu "liên quan":

- **Lazy Loading (Tải Dữ Liệu "Lười Biếng"):**

    - Khi bạn "hỏi han" một "món đồ" (entity), **chỉ các "đặc điểm" (properties) của "món đồ" đó được "tải" về**. Các *
      *navigation properties** (những "đặc điểm" "chỉ" đến các "món đồ" khác, thể hiện "quan hệ") **chưa được "tải" ngay
      ** (chúng có giá trị `null` hoặc "mặc định").
    - **Khi bạn "tò mò" "xem" một navigation property lần đầu tiên**, EF Core sẽ **"tự động" "gọi" một truy vấn riêng
      biệt** để "tải" dữ liệu "liên quan" (nếu dữ liệu đó chưa được "tải" trước đó).
    - **"Điểm cộng":** "Tải" dữ liệu khi "cần đến", có thể "tiết kiệm" "tài nguyên" nếu không phải lúc nào cũng cần dữ
      liệu "liên quan".
    - **"Điểm trừ":** Có thể "gây họa" **N+1 query problem**: nếu bạn "duyệt" qua một "danh sách" các "món đồ" và "tò
      mò" "xem" navigation property của **từng** "món đồ", có thể "sinh ra" N+1 truy vấn (1 truy vấn ban đầu để "lấy"
      danh sách "món đồ", và N truy vấn "lẻ tẻ" để "tải" dữ liệu "liên quan" cho **từng** "món đồ"). Điều này có thể
      làm "chậm chân" ứng dụng, nhất là khi có nhiều "món đồ".
    - **Lazy Loading "tắt máy" mặc định trong EF Core**. Bạn cần "bật công tắc" để "kích hoạt" (thường bằng cách "rinh
      về" NuGet package `Microsoft.EntityFrameworkCore.Proxies` và "bật" trong `DbContextOptionsBuilder`).

- **Eager Loading (Tải Dữ Liệu "Hăng Hái"):**
    - Khi bạn "hỏi han" một "món đồ" (entity), bạn có thể **"dặn trước"** là muốn "tải" luôn các **navigation properties
      ** mà bạn sẽ "cần dùng", tất cả **trong một truy vấn duy nhất**.
    - Dùng "chiêu" **`.Include(navigationProperty)`** (và `.ThenInclude()` cho "quan hệ" "nhiều tầng") để "chỉ mặt điểm
      tên" các navigation properties cần "tải" "hăng hái".
    - **"Điểm cộng":** "Tránh" được "tai họa" N+1 query problem, "chạy nhanh" hơn khi bạn "biết tỏng" là mình sẽ cần dữ
      liệu "liên quan".
    - **"Điểm trừ":** Có thể "tải" "hơi nhiều" dữ liệu hơn "cần thiết" nếu không phải lúc nào cũng "đụng" đến dữ liệu "
      liên quan", có thể làm truy vấn ban đầu "phức tạp" hơn.

**Ví dụ Eager Loading (giả sử "món đồ" `DonHang` có navigation property `DonHangChiTiets` và `DonHangChiTiet` có
navigation property `SanPham`):**

```csharp
using (var dbContext = new CuaHangDbContext()) // "Trạm trung chuyển" DbContext
{
    // Eager loading: "Tải" DonHang "cùng lúc" với DonHangChiTiets và SanPham của mỗi DonHangChiTiet ("tải" một lèo cho "đỡ lằng nhằng")
    var donHangsEagerLoad = dbContext.DonHangs // "Kho" DonHang
                                    .Include(dh => dh.DonHangChiTiets) // "Dặn": "tải" luôn DonHangChiTiets (danh sách chi tiết đơn hàng)
                                        .ThenInclude(dhct => dhct.SanPham) // "Dặn thêm": "tải" luôn SanPham (sản phẩm của từng chi tiết đơn hàng)
                                    .ToList(); // "Ép" truy vấn "chạy" và "đổ" kết quả vào List<DonHang>

    Console.WriteLine("\nĐơn hàng (Eager Loading):");
    foreach (var dh in donHangsEagerLoad) // Duyệt qua các đơn hàng đã "tải"
    {
        Console.WriteLine($"Mã ĐH: {dh.DonHangId}, Ngày: {dh.NgayDatHang}"); // In thông tin đơn hàng
        foreach (var dhct in dh.DonHangChiTiets) // Duyệt qua "chi tiết đơn hàng" của từng đơn hàng
        {
            Console.WriteLine($"  - Sản phẩm: {dhct.SanPham.TenSanPham}, Số lượng: {dhct.SoLuong}"); // In thông tin sản phẩm và số lượng trong chi tiết đơn hàng
        }
    }
}
```

**Khi nào nên "chọn" Lazy Loading và Eager Loading?**

- **Eager Loading:** Nên "dùng" khi bạn **"biết chắc"** là mình sẽ cần dữ liệu "liên quan", và muốn **"tối ưu" "tốc độ"
  ** bằng cách giảm số lần "hỏi han" database. Thường "hợp" khi bạn "trình bày" dữ liệu "chi tiết", làm báo cáo, hoặc "
  xử lý" dữ liệu "liên quan" trong code nghiệp vụ.
- **Lazy Loading:** Có thể "có ích" trong các trường hợp:
    - Bạn **"không chắc"** là có cần dữ liệu "liên quan" hay không.
    - Bạn muốn **"tải" dữ liệu "liên quan" chỉ khi "thực sự cần"** để "nhẹ gánh" ban đầu.
    - Trong các ứng dụng "nhỏ xinh", hoặc khi "tốc độ" không phải là "ưu tiên số 1".
    - **Cần "cẩn thận" để "né" N+1 query problem** khi dùng Lazy Loading.

**5.6. Transactions và Unit of Work với LINQ to Entities - "Đảm Bảo" Dữ Liệu "Đúng Chuẩn"**

- **Transactions (Giao Dịch):** Là một "chuỗi" các "thao tác" cơ sở dữ liệu (ví dụ: "thêm", "sửa", "xóa") được "gom" lại
  thành một **"gói công việc" duy nhất**. Transactions "đảm bảo" 4 chữ vàng **ACID**:

    - **Nguyên tử (Atomicity):** Hoặc **tất cả** các "thao tác" trong transaction "thành công" ("commit" - "chốt sổ"),
      hoặc **tất cả** "thất bại" ("rollback" - "quay đầu"). Không có chuyện "dở dở ương ương".
    - **Nhất quán (Consistency):** Transaction phải "đưa" cơ sở dữ liệu từ một "trạng thái hợp lệ" sang một "trạng thái
      hợp lệ" khác. Không được "phá vỡ" các "luật lệ" (ràng buộc) dữ liệu.
    - **Cô lập (Isolation):** Các transaction "chạy" đồng thời không được "chen chân" vào nhau. Mỗi transaction phải "
      cảm thấy" như thể nó là transaction "duy nhất" đang "hoạt động".
    - **Bền vững (Durability):** Sau khi transaction "chốt sổ" thành công, các "thay đổi" phải được "ghi nhớ" "vĩnh
      viễn" và "không bị mất" dù có "sự cố" xảy ra.

- **Unit of Work (Đơn Vị Công Việc):** Là một "mẫu thiết kế" phần mềm, "định nghĩa" một "gói công việc" "logic" trong
  ứng dụng. Trong thế giới ORM, `DbContext` trong EF Core thường được "xem" là một Unit of Work. Nó "theo dõi" các "thay
  đổi" của entities và "quản lý" transaction khi bạn "gọi" `SaveChanges()`.

**EF Core và Transactions - "Quản Lý" Giao Dịch Trong EF Core:**

- **Implicit Transactions (Transaction "Ngầm Định"):** Khi bạn "gọi" `dbContext.SaveChanges()`, EF Core sẽ **"tự động" "
  bắt đầu" một transaction**, "thực hiện" tất cả các "thay đổi" ("thêm", "sửa", "xóa") trong transaction này, và **"chốt
  sổ"** (commit transaction) nếu "xuôi chèo mát mái", hoặc **"quay đầu"** (rollback transaction) nếu có "sóng gió" (
  lỗi). Đây là "chế độ" transaction "mặc định" và thường "đủ dùng" cho nhiều trường hợp.

- **Explicit Transactions (Transaction "Rõ Ràng"):** Trong một số "tình huống" "đặc biệt", bạn có thể cần "kiểm soát"
  transaction một cách "chặt chẽ" hơn, ví dụ:

    - Muốn "gói" nhiều lần "gọi" `SaveChanges()` vào chung một transaction ("không khuyến khích", nên cố gắng "gom"
      các "thay đổi" vào một lần `SaveChanges()` duy nhất).
    - Muốn "thêm" các "thao tác" cơ sở dữ liệu không phải EF Core (ví dụ: "gọi" stored procedure, raw SQL) vào chung một
      transaction với các "thao tác" EF Core.
    - Muốn "điều khiển" "điểm bắt đầu" và "điểm kết thúc" transaction một cách "chính xác" (ví dụ: "bắt đầu" transaction
      ở chỗ này, nhưng "chốt sổ"/"quay đầu" ở chỗ khác).

  Để dùng explicit transactions, bạn có thể "triệu hồi" `dbContext.Database.BeginTransaction()`, `transaction.Commit()`,
  `transaction.Rollback()`.

  ```csharp
  using (var dbContext = new CuaHangDbContext()) // "Trạm trung chuyển" DbContext
  {
      using (var transaction = dbContext.Database.BeginTransaction()) // "Bắt đầu" explicit transaction (mở "cánh cửa" transaction)
      {
          try // "Bắt đầu" "thử" làm một loạt "thao tác"
          {
              // "Thêm" sản phẩm 1
              var sp1 = new SanPham { TenSanPham = "SP Transaction 1", Gia = 100 };
              dbContext.SanPhams.Add(sp1);
              dbContext.SaveChanges(); // "Lưu" thay đổi lần 1 (vẫn nằm trong transaction)

              // "Thêm" sản phẩm 2
              var sp2 = new SanPham { TenSanPham = "SP Transaction 2", Gia = 200 };
              dbContext.SanPhams.Add(sp2);
              dbContext.SaveChanges(); // "Lưu" thay đổi lần 2 (vẫn nằm trong transaction)

              // "Chốt sổ" transaction nếu mọi thứ "xuôi chèo mát mái"
              transaction.Commit(); // "Đóng dấu" "thành công" cho transaction
              Console.WriteLine("\nTransaction Commit thành công."); // Thông báo "thành công"
          }
          catch (Exception ex) // Nếu có "sóng gió" (lỗi)
          {
              // "Quay đầu" transaction (hủy bỏ mọi "thay đổi" trong transaction)
              transaction.Rollback(); // "Lệnh" transaction "quay đầu"
              Console.WriteLine($"\nTransaction Rollback do lỗi: {ex.Message}"); // Thông báo "lỗi"
          }
      } // transaction.Dispose() sẽ tự động "quay đầu" transaction nếu bạn "quên" "chốt sổ" (commit)
  }
  ```

**Tổng Kết Chương 5:**

- Bạn đã được "giới thiệu" về LINQ to SQL và Entity Framework Core (EF Core).
    - Học cách "thiết lập" kết nối cơ sở dữ liệu và "dựng" `DbContext`.
    - "Nắm chắc" cách "truy vấn" dữ liệu từ database bằng LINQ queries.
    - Biết cách "thêm", "sửa", "xóa" dữ liệu trong database bằng EF Core.
    - "Phân biệt" Lazy Loading và Eager Loading và cách dùng `.Include()` để "tải" dữ liệu "hăng hái".
    - "Hiểu" về Transactions và Unit of Work, và cách EF Core "quản lý" transactions.

LINQ to Entities (qua EF Core) là một "vũ khí" "lợi hại" để "xây dựng" các ứng dụng .NET "tương tác" với cơ sở dữ liệu.
Nó giúp bạn viết code "hỏi han" dữ liệu "an toàn", "dễ đọc", và "chạy nhanh".

**Bài Tập "Database":**

1. "Dựng" một cơ sở dữ liệu "nhỏ xinh" (ví dụ: dùng SQL Server LocalDB) với các bảng `SanPham`, `DanhMuc`, `NhaCungCap`,
   có "quan hệ" giữa các bảng.
2. "Vẽ" các Entity classes "ứng với" các bảng trong database.
3. "Dựng" `DbContext` và "cài đặt" kết nối đến database.
4. Sử dụng LINQ queries để:
    - "Lấy" danh sách "tất cả" sản phẩm thuộc một "danh mục" cụ thể, "sắp xếp" theo "giá" giảm dần.
    - "Lấy" danh sách "tên sản phẩm" và "tên nhà cung cấp" của tất cả sản phẩm có "giá" trong một "khoảng" nào đó do bạn
      chọn.
    - "Tính tổng" "số lượng" sản phẩm theo từng "danh mục".
    - "Lấy" sản phẩm có "giá" "cao nhất" trong **từng** "danh mục".
5. "Thêm" một vài sản phẩm mới vào database.
6. "Chỉnh sửa" "thông tin" của một sản phẩm.
7. "Xóa sổ" một sản phẩm (chú ý đến các "ràng buộc" "quan hệ" nếu có).
8. "Thử nghiệm" với Eager Loading và Lazy Loading để "thấy" sự "khác biệt".
9. Sử dụng explicit transaction để "thực hiện" một "chuỗi" các "thao tác" "thêm/sửa/xóa" dữ liệu, và "xử lý" "quay
   đầu" (rollback) khi có "sự cố".

**Bước Tiếp Theo:**

Chúng ta sẽ "phiêu lưu" đến **Chương 6: Parallel LINQ (PLINQ) - "Bơm Ga" Cho Truy Vấn**. Chúng ta sẽ "khám phá" cách
dùng PLINQ để "song song hóa" các truy vấn LINQ và "tăng tốc" "xử lý" dữ liệu bằng "sức mạnh" của bộ vi xử lý "đa nhân".

Bạn có câu hỏi nào về LINQ to SQL/Entities này không? Hãy cứ "hỏi han" nhé!
