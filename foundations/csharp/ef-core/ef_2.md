# Chương 2: "Bắt Tay" Với Entity Framework Core - "Chuẩn Bị Sân Khấu" - "Setup" Môi Trường Để "Vọc Vạch" EF Core

Chào mừng bạn trở lại với hành trình Entity Framework! Trong chương này, chúng ta sẽ "bắt tay" vào việc "chuẩn bị sân khấu" để "vọc vạch" **Entity Framework Core (EF Core)** - phiên bản "hiện đại" và "mã nguồn mở" của Entity Framework.

**Phần 2: "Bắt Tay" Với Entity Framework Core - "Chuẩn Bị Sân Khấu"**

**2.1. Chọn phiên bản Entity Framework: EF 6 vs EF Core - "Nên 'Chọn' Ai?" - "Quyết Định" Khôn Ngoan**

-   **Entity Framework 6 (EF 6) - "Anh Cả Làng" "Ổn Định" Nhưng "Hơi 'Già' ":**

    -   **"Đàn anh"** đi trước, ra đời từ lâu, đã được "kiểm chứng" qua nhiều năm tháng và nhiều dự án thực tế.
    -   **"Ổn định"** và **"trưởng thành"**, có nhiều "tính năng" và "công cụ" "phong phú".
    -   Chỉ "hỗ trợ" **.NET Framework** (không chạy được trên .NET Core hoặc .NET 5+).
    -   **"Không còn được phát triển"** tích cực nữa, chủ yếu chỉ nhận các bản vá lỗi nhỏ.

-   **Entity Framework Core (EF Core) - "Em Út" "Năng Động" và "Đa Nền Tảng":**

    -   **"Hậu duệ"** "hiện đại", được "xây dựng lại từ đầu" với nhiều "cải tiến" về "hiệu năng", "mở rộng", và "linh hoạt".
    -   **"Mã nguồn mở"** và **"đa nền tảng"** (cross-platform), chạy được trên **.NET Framework, .NET Core, .NET 5+**, và nhiều hệ điều hành (Windows, macOS, Linux).
    -   Được **"phát triển"** tích cực bởi Microsoft và cộng đồng, liên tục "cập nhật" các "tính năng" mới và "cải tiến" "hiệu năng".
    -   "Thiếu" một số "tính năng" "nâng cao" so với EF 6 (ở thời điểm hiện tại), nhưng đang dần được "bổ sung" trong các phiên bản mới.

-   **"Nên 'chọn' ai?" - "Lời Khuyên" "Sáng Suốt":**

    -   **Cho dự án mới:** **"Ưu tiên"** **Entity Framework Core (EF Core)**. Vì EF Core là tương lai của Entity Framework, "đa nền tảng", "hiệu năng tốt", và được "hỗ trợ" lâu dài.
    -   **Cho dự án "bảo trì" hoặc "nâng cấp" từ .NET Framework cũ:** Nếu dự án của bạn đang dùng .NET Framework và EF 6, việc "chuyển đổi" sang EF Core có thể tốn nhiều công sức. Bạn có thể **"tiếp tục"** dùng EF 6 nếu dự án không có yêu cầu "đặc biệt" về "đa nền tảng" hoặc "hiệu năng". Nhưng nếu có thể, hãy **"xem xét"** "nâng cấp" lên EF Core để "tận hưởng" các "lợi ích" "hiện đại" của nó.

**Trong loạt tài liệu này, chúng ta sẽ tập trung vào **Entity Framework Core (EF Core)** - "người bạn đồng hành" "tốt nhất" cho các dự án .NET hiện đại.**

**2.2. Cài đặt NuGet Packages - "Rinh Về" "Đồ Nghề" EF Core - "Sắm Đồ" Để "Chiến Đấu"**

Để "bắt đầu" dùng EF Core trong dự án C# của bạn, bạn cần "rinh về" các **NuGet packages** cần thiết. NuGet là "trợ lý" đắc lực giúp bạn "quản lý" các thư viện bên ngoài (packages) trong dự án .NET.

-   **Các NuGet packages "cốt yếu" của EF Core:**

    -   **`Microsoft.EntityFrameworkCore`:** "Gói" "cốt lõi" của EF Core, chứa các "thành phần" "cơ bản" nhất (DbContext, DbSet, LINQ provider, v.v.).
    -   **`Microsoft.EntityFrameworkCore.Relational`:** "Gói" "mở rộng" "nền tảng" cho các cơ sở dữ liệu **quan hệ** (Relational Databases) - loại database mà EF Core "chuyên trị".
    -   **`Microsoft.EntityFrameworkCore.Tools`:** "Gói" "công cụ" dòng lệnh (command-line tools) của EF Core, giúp bạn "thực hiện" các "lệnh" EF Core (ví dụ: tạo migrations, cập nhật database) từ command line hoặc Package Manager Console.
    -   **"Nhà cung cấp" (Provider) cơ sở dữ liệu:** Bạn cần "chọn" và "cài đặt" thêm "gói" **"nhà cung cấp"** (provider) "tương ứng" với loại cơ sở dữ liệu mà bạn muốn "kết nối" (ví dụ: SQL Server, MySQL, PostgreSQL, SQLite, v.v.). Ví dụ:
        -   **SQL Server:** `Microsoft.EntityFrameworkCore.SqlServer`
        -   **MySQL:** `MySql.EntityFrameworkCore` (từ bên thứ ba, Oracle) hoặc `Pomelo.EntityFrameworkCore.MySql` (từ cộng đồng, phổ biến hơn)
        -   **PostgreSQL:** `Npgsql.EntityFrameworkCore.PostgreSQL`
        -   **SQLite:** `Microsoft.EntityFrameworkCore.Sqlite`

-   **"Cách cài đặt" NuGet packages:**

    -   **Visual Studio - Package Manager Console (dành cho dân "pro" thích "gõ lệnh"):**

        1.  Mở **Package Manager Console** (Tools -> NuGet Package Manager -> Package Manager Console).
        2.  "Gõ" lệnh `Install-Package <PackageName>` (thay `<PackageName>` bằng tên package bạn muốn cài, ví dụ: `Install-Package Microsoft.EntityFrameworkCore.SqlServer`).
        3.  Bấm Enter và "chờ" NuGet "tải" và "cài đặt" package vào dự án của bạn.

    -   **Visual Studio - NuGet Package Manager UI (dành cho người "mới bắt đầu" thích "giao diện"):**
        1.  Mở **NuGet Package Manager** (Project -> Manage NuGet Packages...).
        2.  Chọn tab **Browse**.
        3.  "Tìm kiếm" package bạn muốn cài (ví dụ: "Microsoft.EntityFrameworkCore.SqlServer").
        4.  Chọn package, chọn phiên bản (thường chọn phiên bản mới nhất "ổn định"), chọn dự án của bạn, và bấm **Install**.
        5.  "Chờ" NuGet "tải" và "cài đặt" package.

**Ví dụ: Cài đặt các NuGet packages cần thiết cho EF Core và SQL Server (dùng Package Manager Console):**

```powershell
Install-Package Microsoft.EntityFrameworkCore.SqlServer
Install-Package Microsoft.EntityFrameworkCore.Tools
```

**2.3. Tạo Data Context (DbContext) - "Trái Tim" Của EF Core - "Trung Tâm Điều Hành" Database**

-   **Data Context (DbContext) là gì?**

    -   `DbContext` là một class **"đặc biệt"** trong EF Core, đóng vai trò như **"trái tim"** của EF Core trong ứng dụng của bạn. Hãy tưởng tượng `DbContext` như **"trạm trung chuyển"** giữa code C# và cơ sở dữ liệu.
    -   `DbContext` "quản lý" **kết nối** đến database, "theo dõi" các **thay đổi** của dữ liệu, và "cung cấp" các **phương thức** để bạn "truy vấn", "thêm", "sửa", "xóa" dữ liệu trong database.
    -   Bạn cần **tạo một class "kế thừa" từ `DbContext`** và "cấu hình" nó để EF Core "biết" cách "kết nối" đến database và "quản lý" dữ liệu.

-   **"Cách tạo" Data Context (DbContext):**

    1.  Tạo một class C# mới trong dự án của bạn (ví dụ: `MyDbContext.cs`).
    2.  "Kế thừa" class này từ class `DbContext` (trong namespace `Microsoft.EntityFrameworkCore`).
    3.  "Cấu hình" kết nối database trong phương thức `OnConfiguring` (override method này trong class của bạn).
    4.  "Khai báo" các `DbSet<TEntity>` properties để "ánh xạ" các bảng database (chúng ta sẽ nói về `DbSet<TEntity>` ở phần sau).

-   **Ví dụ code Data Context (DbContext) cho SQL Server LocalDB:**

    ```csharp
    using Microsoft.EntityFrameworkCore; // "Nhập" namespace EF Core

    public class MyDbContext : DbContext // Class Data Context "kế thừa" từ DbContext
    {
        // (Khai báo DbSet<TEntity> properties ở đây - xem phần sau)

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder) // Override method OnConfiguring để "cấu hình" kết nối database
        {
            // "Cấu hình" kết nối SQL Server LocalDB
            optionsBuilder.UseSqlServer("Server=(localdb)\\mssqllocaldb;Database=MyDatabase;Trusted_Connection=True;"); // Thay "MyDatabase" bằng tên database của bạn
        }
    }
    ```

-   **"Giải thích" code Data Context:**

    -   `public class MyDbContext : DbContext`: Tạo class `MyDbContext` "kế thừa" từ `DbContext`.
    -   `protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)`: Override method `OnConfiguring` để "cấu hình" kết nối database.
        -   `optionsBuilder.UseSqlServer("...")`: "Chiêu" `UseSqlServer` "ra lệnh" cho EF Core là "hãy dùng SQL Server" làm "nhà cung cấp" database.
        -   `"Server=(localdb)\\mssqllocaldb;Database=MyDatabase;Trusted_Connection=True;"`: Đây là **connection string** - "chuỗi" "thông tin" để EF Core "biết" cách "kết nối" đến database SQL Server LocalDB. Bạn cần **"thay" `"MyDatabase"` bằng "tên database"** mà bạn muốn "làm việc".

**2.4. Định nghĩa Entities (Classes "Ánh Xạ" Bảng) - "Vẽ" "Bản Thiết Kế" Dữ Liệu - "Khuôn Mẫu" Cho Dữ Liệu**

-   **Entities (Thực Thể) là gì?**

    -   **Entities** là các class C# "đơn giản" (Plain Old CLR Objects - POCOs) mà bạn "tạo ra" để "đại diện" cho các **"bảng"** trong cơ sở dữ liệu của bạn.
    -   Mỗi Entity class sẽ "ánh xạ" tới một bảng database.
    -   Các properties trong Entity class sẽ "ánh xạ" tới các cột trong bảng.
    -   Entities là "cầu nối" giữa thế giới "đối tượng" C# và thế giới "quan hệ" database.

-   **"Cách định nghĩa" Entities:**

    1.  Tạo các class C# mới trong dự án của bạn (ví dụ: `SanPham.cs`, `DanhMuc.cs`, `KhachHang.cs`).
    2.  "Đặt tên" class "trùng" với tên bảng database (hoặc "tên" "gần giống", bạn có thể "tùy chỉnh" "ánh xạ" tên sau).
    3.  "Thêm" các properties vào class để "đại diện" cho các cột trong bảng.
    4.  "Quy ước" đặt tên property "khóa chính" (primary key): thường dùng `<ClassName>Id` hoặc `Id` (ví dụ: `SanPhamId`, `Id`). EF Core sẽ "tự động" "nhận ra" property này là "khóa chính" (convention).

-   **Ví dụ code Entities (SanPham, DanhMuc):**

    ```csharp
    // SanPham.cs - Entity class "đại diện" cho bảng SanPhams
    public class SanPham // Class "ánh xạ" bảng SanPhams
    {
        public int SanPhamId { get; set; } // Property "ánh xạ" cột SanPhamId (khóa chính)
        public string TenSanPham { get; set; } // Property "ánh xạ" cột TenSanPham
        public decimal Gia { get; set; }      // Property "ánh xạ" cột Gia
        public string DanhMucSanPham { get; set; } // Property "ánh xạ" cột DanhMucSanPham
    }

    // DanhMuc.cs - Entity class "đại diện" cho bảng DanhMucs
    public class DanhMuc // Class "ánh xạ" bảng DanhMucs
    {
        public int DanhMucId { get; set; } // Property "ánh xạ" cột DanhMucId (khóa chính)
        public string TenDanhMuc { get; set; } // Property "ánh xạ" cột TenDanhMuc
    }
    ```

-   **"Khai báo" `DbSet<TEntity>` properties trong Data Context:**

    -   Sau khi "định nghĩa" Entities, bạn cần "khai báo" các `DbSet<TEntity>` properties trong Data Context (`DbContext`) để EF Core "biết" về các Entities này và "ánh xạ" chúng với các bảng database.
    -   "Thêm" các properties kiểu `DbSet<TEntity>` vào class `DbContext` của bạn, với `TEntity` là kiểu Entity class (ví dụ: `DbSet<SanPham>`, `DbSet<DanhMuc>`).
    -   "Tên" property `DbSet<TEntity>` thường được đặt **số nhiều** của tên Entity class (ví dụ: `SanPhams`, `DanhMucs`) - đây là "quy ước" tốt.

-   **Ví dụ "cập nhật" Data Context (MyDbContext.cs) để "khai báo" `DbSet<SanPham>` và `DbSet<DanhMuc>`:**

    ```csharp
    using Microsoft.EntityFrameworkCore;

    public class MyDbContext : DbContext
    {
        // "Khai báo" DbSet<SanPham> property - "ánh xạ" bảng SanPhams
        public DbSet<SanPham> SanPhams { get; set; }

        // "Khai báo" DbSet<DanhMuc> property - "ánh xạ" bảng DanhMucs
        public DbSet<DanhMuc> DanhMucs { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseSqlServer("Server=(localdb)\\mssqllocaldb;Database=MyDatabase;Trusted_Connection=True;");
        }
    }
    ```

**Tổng Kết Chương 2:**

-   Bạn đã "chuẩn bị" "xong xuôi" "sân khấu" để "bắt đầu" "vọc vạch" EF Core:
    -   "Chọn" phiên bản EF Core (phiên bản "hiện đại" và "đa nền tảng").
    -   "Cài đặt" các NuGet packages "cần thiết" (EF Core, Tools, Provider).
    -   "Tạo" Data Context (`DbContext`) - "trái tim" của EF Core.
    -   "Định nghĩa" Entities (classes "ánh xạ" bảng) - "khuôn mẫu" cho dữ liệu.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 3: "Thao Tác" Dữ Liệu Cơ Bản (CRUD Operations) - "Làm Chủ" "Bảng Biểu"**. Chúng ta sẽ học cách "thực hiện" các thao tác CRUD (Create, Read, Update, Delete) - "thêm", "đọc", "sửa", "xóa" dữ liệu trong database thông qua EF Core và LINQ queries.

Bạn có câu hỏi nào về "thiết lập" EF Core này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" EF Core.

