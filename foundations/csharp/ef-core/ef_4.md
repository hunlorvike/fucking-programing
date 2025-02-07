# Chương 4: "Mối Quan Hệ" Giữa Các Bảng (Relationships) - "Gắn Kết" Dữ Liệu - "Mạng Lưới" Dữ Liệu "Rộng Lớn"

Chào mừng bạn đến với **Chương 4: "Mối Quan Hệ" Giữa Các Bảng (Relationships)**! Trong chương này, chúng ta sẽ "khám
phá" một trong những "khía cạnh" "quan trọng" nhất của cơ sở dữ liệu quan hệ và EF Core - **"mối quan hệ"** giữa các
bảng. "Mối quan hệ" giúp bạn "gắn kết" dữ liệu từ nhiều bảng lại với nhau, tạo nên một "mạng lưới" dữ liệu "rộng lớn"
và "phong phú".

**Phần 4: "Mối Quan Hệ" Giữa Các Bảng (Relationships) - "Gắn Kết" Dữ Liệu**

**4.1. Các Loại "Quan Hệ" Phổ Biến: Một-Một, Một-Nhiều, Nhiều-Nhiều - "Bản Đồ" "Liên Kết" Dữ Liệu (Giải thích "dễ nuốt")
**

Trong cơ sở dữ liệu quan hệ, các bảng thường không "đứng riêng lẻ", mà "liên kết" với nhau thông qua các **"mối quan hệ"
**. Các loại "quan hệ" phổ biến nhất bao gồm:

- **Quan hệ Một-Một (One-to-One):**

    - Mỗi bản ghi (row) trong bảng **A** chỉ "liên kết" với **tối đa một** bản ghi trong bảng **B**, và ngược lại.
    - Ví dụ: Một `NguoiDung` (bảng A) chỉ có **một** `HoSoNguoiDung` (bảng B) duy nhất, và mỗi `HoSoNguoiDung` cũng
      chỉ "thuộc về" **một** `NguoiDung`.
    - Trong EF Core, quan hệ một-một thường được "định nghĩa" bằng cách "chia sẻ" "khóa chính" (primary key sharing)
      hoặc dùng "khóa ngoại duy nhất" (unique foreign key).

- **Quan hệ Một-Nhiều (One-to-Many):**

    - Một bản ghi (row) trong bảng **A** có thể "liên kết" với **không, một, hoặc nhiều** bản ghi trong bảng **B**,
      nhưng mỗi bản ghi trong bảng **B** chỉ "liên kết" với **tối đa một** bản ghi trong bảng **A**.
    - Ví dụ: Một `DanhMuc` (bảng A) có thể "chứa" **nhiều** `SanPham` (bảng B), nhưng mỗi `SanPham` chỉ "thuộc về" **một
      ** `DanhMuc` duy nhất.
    - Trong EF Core, quan hệ một-nhiều được "định nghĩa" bằng cách dùng **khóa ngoại** (foreign key) ở bảng **B** "tham
      chiếu" đến "khóa chính" của bảng **A**.

- **Quan hệ Nhiều-Nhiều (Many-to-Many):**

    - Nhiều bản ghi (rows) trong bảng **A** có thể "liên kết" với **nhiều** bản ghi trong bảng **B**, và ngược lại.
    - Ví dụ: Một `SinhVien` (bảng A) có thể "đăng ký" **nhiều** `KhoaHoc` (bảng B), và một `KhoaHoc` cũng có thể được "
      đăng ký" bởi **nhiều** `SinhVien`.
    - Trong cơ sở dữ liệu quan hệ, quan hệ nhiều-nhiều thường được "hiện thực hóa" thông qua một **"bảng liên kết"** (
      junction table) hoặc **"bảng trung gian"** (join table) (ví dụ: `SinhVienKhoaHoc`), bảng này chứa "khóa ngoại" "
      tham chiếu" đến "khóa chính" của cả bảng **A** và bảng **B**.
    - Trong EF Core, quan hệ nhiều-nhiều có thể được "định nghĩa" một cách "trực tiếp" (với EF Core 5.0 trở lên) hoặc "
      gián tiếp" (thông qua "bảng liên kết" - cách truyền thống).

**4.2. "Định Nghĩa" "Quan Hệ" Trong EF Core (Fluent API và Data Annotations) - "Vẽ" "Sơ Đồ" Quan Hệ Trong Code**

Để EF Core "hiểu" và "quản lý" các "mối quan hệ" giữa các Entities (classes "ánh xạ" bảng), bạn cần "định nghĩa" các "
quan hệ" này trong code của bạn. Có hai cách chính để "định nghĩa" "quan hệ" trong EF Core:

- **Fluent API (Phong Cách "Mượt Mà"):**

    - "Dùng" các "phương thức" "mượt mà" (fluent methods) trong phương thức **`OnModelCreating`** của Data Context (
      `DbContext`) để "cấu hình" "quan hệ".
    - "Linh hoạt" hơn Data Annotations, cho phép "cấu hình" các "quan hệ" "phức tạp" và "tùy biến" cao.
    - Code "cấu hình" "quan hệ" được "tập trung" ở một nơi (trong `OnModelCreating`), giúp code "gọn gàng" và "dễ quản
      lý" hơn.

- **Data Annotations (Phong Cách "Trang Trí" Dữ Liệu):**

    - "Dùng" các **attributes** (ví dụ: `[ForeignKey]`, `[Required]`, `[MaxLength]`, v.v.) để "trang trí" các properties
      trong Entity classes.
    - "Đơn giản" và "dễ dùng" cho các "quan hệ" "cơ bản".
    - Code "cấu hình" "quan hệ" được "rải rác" trong các Entity classes, có thể làm code "khó theo dõi" hơn khi "quan
      hệ" trở nên "phức tạp".

**Ví dụ "định nghĩa" quan hệ Một-Nhiều giữa `DanhMuc` và `SanPham` bằng **Fluent API**:

```csharp
public class DanhMuc
{
    public int DanhMucId { get; set; }
    public string TenDanhMuc { get; set; }

    public ICollection<SanPham> SanPhams { get; set; } // Navigation property - "danh sách" các sản phẩm thuộc danh mục này
}

public class SanPham
{
    public int SanPhamId { get; set; }
    public string TenSanPham { get; set; }
    public decimal Gia { get; set; }
    public string DanhMucSanPham { get; set; }

    public int DanhMucId { get; set; } // Foreign key - "khóa ngoại" liên kết đến bảng DanhMucs
    public DanhMuc DanhMuc { get; set; } // Navigation property - "tham chiếu" đến đối tượng DanhMuc cha
}

public class MyDbContext : DbContext
{
    public DbSet<DanhMuc> DanhMucs { get; set; }
    public DbSet<SanPham> SanPhams { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // "Cấu hình" quan hệ Một-Nhiều giữa DanhMuc và SanPham bằng Fluent API
        modelBuilder.Entity<DanhMuc>() // "Chọn" Entity DanhMuc
            .HasMany(dm => dm.SanPhams) // "DanhMuc" có "nhiều" "món đồ" "con" là SanPhams (HasMany)
            .WithOne(sp => sp.DanhMuc) // Mỗi "món đồ" "con" SanPham "thuộc về" "một" "món đồ" "cha" DanhMuc (WithOne)
            .HasForeignKey(sp => sp.DanhMucId); // "Khóa ngoại" để "liên kết" là DanhMucId trong bảng SanPhams (HasForeignKey)
    }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer("Server=(localdb)\\mssqllocaldb;Database=MyDatabase;Trusted_Connection=True;");
    }
}
```

**"Giải mã" code "định nghĩa" quan hệ Một-Nhiều (Fluent API):**

- **Navigation Properties:**
    - `DanhMuc.SanPhams`: Property kiểu `ICollection<SanPham>` trong class `DanhMuc` là **navigation property** - "danh
      sách" các `SanPham` "liên quan" đến `DanhMuc` (quan hệ 1-nhiều).
    - `SanPham.DanhMuc`: Property kiểu `DanhMuc` trong class `SanPham` cũng là navigation property - "tham chiếu" đến
      `DanhMuc` "cha" (quan hệ nhiều-1).
- **Foreign Key Property:**
    - `SanPham.DanhMucId`: Property kiểu `int` và có tên kết thúc bằng `Id` (theo convention) trong class `SanPham` được
      EF Core "nhận diện" là **foreign key property** - "khóa ngoại" để "liên kết" đến bảng `DanhMucs`.
- **Fluent API Configuration (trong `OnModelCreating`):**
  -
  `modelBuilder.Entity<DanhMuc>().HasMany(dm => dm.SanPhams).WithOne(sp => sp.DanhMuc).HasForeignKey(sp => sp.DanhMucId);`:
  Dòng code "mấu chốt" để "định nghĩa" quan hệ một-nhiều.
  - `.HasMany(dm => dm.SanPhams)`: "Báo" rằng Entity `DanhMuc` có quan hệ **"nhiều"** với Entity `SanPham` (một
  `DanhMuc` có nhiều `SanPham`).
  - `.WithOne(sp => sp.DanhMuc)`: "Báo" rằng mỗi Entity `SanPham` có quan hệ **"một"** với Entity `DanhMuc` (mỗi
  `SanPham` thuộc về một `DanhMuc`).
  - `.HasForeignKey(sp => sp.DanhMucId)`: "Chỉ định" property `DanhMucId` trong Entity `SanPham` là **"khóa ngoại"
  ** để "liên kết" đến bảng `DanhMucs`.

**4.3. "Truy Vấn" Dữ Liệu "Liên Quan" (Eager Loading, Lazy Loading) - "Đi Xuyên Qua" Các "Bảng Biểu" - "Khám Phá" "Mạng
Lưới" Dữ Liệu**

- Khi các bảng trong database có "quan hệ" với nhau, bạn thường muốn "truy vấn" dữ liệu **"liên quan"** từ nhiều bảng *
  *"cùng một lúc"**. EF Core cung cấp hai "chiêu" chính để "tải" dữ liệu "liên quan": **Eager Loading** và **Lazy
  Loading** (chúng ta đã "lướt qua" ở Chương 5 về LINQ to Entities, và giờ sẽ "đi sâu" hơn).

- **Eager Loading (Tải Dữ Liệu "Háo Hức"):**

    - "Tải" dữ liệu **"chính"** và dữ liệu **"liên quan"** **"cùng một lúc"** trong **"một truy vấn duy nhất"**.
    - "Dùng" "chiêu" **`.Include(navigationProperty)`** (và `.ThenInclude()` cho quan hệ "nhiều tầng") trong LINQ
      queries để "chỉ định" các navigation properties cần "tải" "háo hức".
    - **"Ưu điểm":** "Giảm" số lượng truy vấn database (tránh N+1 query problem), "tăng" "hiệu năng" khi bạn "biết"
      trước là mình sẽ cần dữ liệu "liên quan".
    - **"Nhược điểm":** Có thể "tải" nhiều dữ liệu hơn "cần thiết" nếu không phải lúc nào cũng "dùng" dữ liệu "liên
      quan", có thể làm truy vấn ban đầu "phức tạp" hơn.

- **Lazy Loading (Tải Dữ Liệu "Lười Biếng"):**

    - "Chỉ tải" dữ liệu **"chính"** khi bạn "truy vấn". Dữ liệu **"liên quan"** chỉ được "tải" **"sau"**, khi bạn **"
      truy cập"** vào navigation properties của đối tượng "chính" lần đầu tiên.
    - EF Core sẽ "tự động" "phát sinh" các truy vấn "riêng biệt" để "tải" dữ liệu "liên quan" khi cần.
    - **"Ưu điểm":** "Tải" dữ liệu khi "cần", có thể "tiết kiệm" "tài nguyên" nếu không phải lúc nào cũng cần dữ liệu "
      liên quan".
    - **"Nhược điểm":** Có thể "gây ra" N+1 query problem (nếu không "cẩn thận"), có thể làm "chậm" ứng dụng nếu "tải"
      dữ liệu "liên quan" quá nhiều lần.
    - **Lazy Loading "không bật" mặc định trong EF Core**. Bạn cần "kích hoạt" nó bằng cách cài đặt NuGet package
      `Microsoft.EntityFrameworkCore.Proxies` và "cấu hình" trong `DbContextOptionsBuilder`.

- **Ví dụ "truy vấn" dữ liệu "liên quan" (DanhMuc và SanPham) bằng Eager Loading:**

  ```csharp
  using (var dbContext = new MyDbContext()) // "Mở" "trạm trung chuyển" Data Context
  {
      // Eager Loading: "Tải" DanhMuc "cùng lúc" với SanPhams (danh sách sản phẩm thuộc danh mục)
      var danhMuc_DienTu = dbContext.DanhMucs // "Bắt đầu" từ DbSet<DanhMuc>
                                      .Include(dm => dm.SanPhams) // "Ra lệnh" Eager Loading: "tải" luôn navigation property SanPhams
                                      .FirstOrDefault(dm => dm.TenDanhMuc == "Điện tử"); // "Lọc" "danh mục" "Điện tử" và "lấy" "món đồ" "đầu tiên" (hoặc "không có gì")

      if (danhMuc_DienTu != null) // "Kiểm tra" xem có "tìm" thấy "danh mục" "Điện tử" không
      {
          Console.WriteLine($"Danh mục: {danhMuc_DienTu.TenDanhMuc}"); // In ra "tên" "danh mục"
          Console.WriteLine("--- Sản phẩm thuộc danh mục ---");
          foreach (var sp in danhMuc_DienTu.SanPhams) // Duyệt qua "danh sách" SanPhams (đã được Eager Loading, không cần truy vấn database thêm)
          {
              Console.WriteLine($"- {sp.TenSanPham}, Giá: {sp.Gia:#,##0}"); // In ra "tên" và "giá" "sản phẩm"
          }
      }
  }
  ```

- **"Giải mã" code Eager Loading:**

    - `.Include(dm => dm.SanPhams)`: "Chiêu" `Include` "ra lệnh" cho EF Core là "hãy 'tải' luôn" navigation property
      `SanPhams` (danh sách sản phẩm) của Entity `DanhMuc` trong **cùng một truy vấn database**. Nhờ đó, khi bạn "truy
      cập" vào `danhMuc_DienTu.SanPhams` trong code, dữ liệu `SanPhams` đã được "tải sẵn" và không cần EF Core phải "
      phát sinh" thêm truy vấn database "lẻ tẻ" nào nữa.

**Tổng Kết Chương 4:**

- Bạn đã "khám phá" các loại "quan hệ" phổ biến trong cơ sở dữ liệu (Một-Một, Một-Nhiều, Nhiều-Nhiều) và "hiểu" cách
  chúng "gắn kết" dữ liệu.
    - Học cách "định nghĩa" "quan hệ" Một-Nhiều trong EF Core bằng Fluent API (trong `OnModelCreating`).
    - "Nắm vững" hai "chiêu" "truy vấn" dữ liệu "liên quan": Eager Loading (`Include`) và Lazy Loading.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 5: Migrations - "Quản Lý" "Thay Đổi" Cấu Trúc Database**. Chúng ta sẽ học cách "dùng"
Migrations để "quản lý" các "thay đổi" cấu trúc database một cách "thông minh" và "chuyên nghiệp", giúp bạn "nâng cấp"
database một cách "dễ dàng" khi "mô hình dữ liệu" của ứng dụng "thay đổi".

Bạn có câu hỏi nào về "mối quan hệ" giữa các bảng và cách "truy vấn" dữ liệu "liên quan" này không? Hãy cứ "hỏi tự
nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "cùng bạn" "làm chủ" EF Core "mạng lưới" dữ liệu.

