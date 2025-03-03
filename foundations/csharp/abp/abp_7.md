# Chương 7: Data Access (Truy Cập Dữ Liệu) - " 'Kết Nối' " Với " 'Kho Tàng' " Dữ Liệu - " 'Lấy', 'Thêm', 'Sửa', 'Xóa' " Dữ Liệu

Chào mừng bạn đến với **Chương 7: Data Access (Truy Cập Dữ Liệu)**! Trong chương này, chúng ta sẽ "khám phá" cách ABP
Framework **"xử lý" "truy cập dữ liệu"** (data access), "tìm hiểu" cách ABP Framework **"tích hợp"** với **Entity
Framework Core** (ORM phổ biến nhất trong .NET), "khám phá" **Repositories** (kho chứa) và **Unit of Work pattern**, và "
học cách" **"truy vấn"**, **"thêm"**, **"sửa"**, và **"xóa"** dữ liệu trong ứng dụng ABP Framework. "Truy cập dữ liệu" là
một "phần" **"không thể thiếu"** của "hầu hết" các ứng dụng, và ABP Framework "cung cấp" một **"cơ chế" "mạnh mẽ"** và
**"linh hoạt"** để "thực hiện" việc này.

**Phần 7: Data Access (Truy Cập Dữ Liệu) - " 'Kết Nối' " Với " 'Kho Tàng' " Dữ Liệu**

- **Data Access (Truy Cập Dữ Liệu) Trong ABP Framework - " 'Linh Hoạt' ", " 'Trừu Tượng' ", và " 'Dễ Kiểm Thử' "**:

    - ABP Framework "cung cấp" một **"lớp 'trừu tượng' " (abstraction layer)** cho việc **"truy cập dữ liệu"**, "giúp"
      bạn **"dễ dàng" "thay đổi" "công nghệ" "truy cập" dữ liệu** (ví dụ: "chuyển" từ Entity Framework Core sang Dapper
      hoặc MongoDB) mà **"không ảnh hưởng"** đến các "phần còn lại" của ứng dụng (Domain Layer, Application Layer).
    - ABP Framework "khuyến khích" việc "sử dụng" **Repositories** (kho chứa) để "truy cập" dữ liệu. Repositories "cung
      cấp" một **"giao diện" "thống nhất"** và **"hướng đối tượng"** để "thao tác" với dữ liệu, "ẩn" các "chi tiết" "kỹ
      thuật" của việc "truy cập" dữ liệu (ví dụ: SQL queries, database connection) khỏi các "lớp" "cao hơn" (Application
      Services, Domain Services).
    - ABP Framework "tích hợp" sẵn **Unit of Work pattern** để **"quản lý" "giao dịch"** (transactions) một cách **"
      tự động"**, "đảm bảo" **"tính 'nhất quán' "** của dữ liệu khi "thực hiện" "nhiều thao tác" trên database trong
      cùng một "giao dịch".

- **"Các Thành Phần" "Chính" Trong Data Access Của ABP Framework:**

    *   **Repositories (Kho chứa):**
        *   "Định nghĩa" (nhắc lại): Repositories là các "lớp" (classes) "cung cấp" một "lớp 'trừu tượng' " để "truy
            cập" dữ liệu.
        *   **`IRepository<TEntity, TKey>`:** "Giao diện" (interface) **"cốt lõi"** để "định nghĩa" Repositories trong
            ABP Framework.
            *   `TEntity`: "Kiểu" (type) của **Entity** (thực thể) mà Repository sẽ "quản lý" (ví dụ: `Product`, `
                Order`).
            *   `TKey`: "Kiểu" (type) của **"khóa chính"** (primary key) của Entity (ví dụ: `Guid`, `int`).
            *   `IRepository` "cung cấp" các **"phương thức" "cơ bản"** để "thao tác" với dữ liệu (ví dụ: `GetAsync`, `
                GetAllAsync`, `InsertAsync`, `UpdateAsync`, `DeleteAsync`).
        *   **"Triển khai" Repositories:** ABP Framework "cung cấp" các **"triển khai" "mặc định"** của `IRepository`
            cho **Entity Framework Core** và **MongoDB**. Bạn có thể "sử dụng" các "triển khai" "mặc định" này hoặc "
            tự mình" "triển khai" `IRepository` cho các "công nghệ" "truy cập" dữ liệu khác.
        *   **Custom Repositories:** Bạn có thể "tạo" các **"custom repositories"** (repositories "tùy chỉnh") bằng
            cách "kế thừa" từ `IRepository` và "thêm" các "phương thức" "riêng" để "thực hiện" các "truy vấn" dữ liệu "
            phức tạp" hoặc "thao tác" dữ liệu "đặc biệt".
        *   **Repository Pattern:** Là một design pattern phổ biến
    *   **Unit of Work (Đơn vị công việc):**
        *   **"Định nghĩa":** Unit of Work là một **"design pattern"** (mẫu thiết kế) "quản lý" một **"giao dịch"** (
            transaction) trên database và "đảm bảo" **"tính 'nhất quán' "** của dữ liệu khi "thực hiện" "nhiều thao
            tác" trên database trong cùng một "giao dịch".
        *   **ABP Framework:** ABP Framework "tích hợp" sẵn Unit of Work pattern. Bạn **"không cần" "phải 'quản lý' "
            giao dịch" "thủ công"**. ABP Framework sẽ "tự động" "tạo" và "quản lý" Unit of Work cho bạn.
        *   **`IUnitOfWork` (Interface):** "Giao diện" để "làm việc" với Unit of Work.
        *   **`[UnitOfWork]` Attribute:** "Attribute" (chú thích) để "đánh dấu" một phương thức (ví dụ: phương thức
            trong Application Service) là một **"đơn vị công việc"**. ABP Framework sẽ "tự động" "tạo" một Unit of
            Work khi phương thức này được "gọi" và "commit" (hoặc "rollback") giao dịch khi phương thức "kết thúc".
            *   `[UnitOfWork(IsDisabled = true)]`: Vô hiệu hóa UoW
            *   `[UnitOfWork(TransactionScopeOption = TransactionScopeOption.RequiresNew)]`: Luôn tạo transaction
                mới.
    *   **`DbContext` (Database Context) (Entity Framework Core):**
        *   **"Định nghĩa":** `DbContext` là một lớp của **Entity Framework Core** "đại diện" cho **"phiên làm việc"**
            (session) với database. `DbContext` "chứa" các **`DbSet` properties** để "truy cập" các **"bảng"** (
            tables) trong database.
        *   **ABP Framework:** ABP Framework "tích hợp" sẵn với Entity Framework Core. Bạn có thể "dễ dàng" "sử dụng"
            Entity Framework Core để "truy cập" dữ liệu trong ứng dụng ABP Framework.
        *   **`AbpDbContext`:** Lớp cơ sở, kế thừa từ `DbContext`

**7.1. Entity Framework Core Integration (Tích Hợp EF Core) - " 'Sức Mạnh' " ORM "Hàng Đầu" Cho .NET**

- **Entity Framework Core (EF Core) - " 'Cầu Nối' " Giữa .NET và Database:**

    - **Entity Framework Core (EF Core)** là một **Object-Relational Mapper (ORM)** "mã nguồn mở", "đa nền tảng", và "
      linh hoạt" cho .NET. EF Core "cho phép" bạn **"làm việc" với database** bằng **"code C#"** và **"đối tượng"** (
      objects) thay vì phải "viết" các câu truy vấn **SQL** "trực tiếp".
    - EF Core "đơn giản hóa" quá trình "truy cập" dữ liệu, "giúp" bạn **"tăng" "năng suất"** lập trình và **"giảm" "
      lỗi"**.

- **ABP Framework và Entity Framework Core - " 'Kết Hợp' " "Hoàn Hảo":**

    - ABP Framework **"tích hợp"** sẵn với **Entity Framework Core**. Bạn có thể "dễ dàng" "sử dụng" EF Core để "
      truy cập" dữ liệu trong ứng dụng ABP Framework.
    - ABP Framework "cung cấp" các **"lớp cơ sở"** (base classes) và **"tiện ích"** (utilities) để "đơn giản hóa" việc
      "sử dụng" EF Core trong ứng dụng ABP Framework (ví dụ: `AbpDbContext`, `EfCoreRepository`, v.v.).

- **"Các Bước" "Sử Dụng" Entity Framework Core Trong Ứng Dụng ABP Framework:**

    1.  **"Cài Đặt" NuGet Packages:**
        *   **`Volo.Abp.EntityFrameworkCore`:** Package "cốt lõi" để "tích hợp" EF Core với ABP Framework.
        *   **`Volo.Abp.EntityFrameworkCore.SqlServer`** (hoặc package cho database provider khác - ví dụ:
            `Volo.Abp.EntityFrameworkCore.PostgreSql`, `Volo.Abp.EntityFrameworkCore.MySql`,
            `Volo.Abp.EntityFrameworkCore.Oracle`, v.v.): Package "cung cấp" **"triển khai"** của ABP Framework cho EF
            Core với **database provider** "cụ thể" (ví dụ: SQL Server, PostgreSQL, MySQL, Oracle, v.v.).
        *   **`Microsoft.EntityFrameworkCore.Tools`:** Package "chứa" các **"công cụ"** để "thực hiện" **database
            migrations** (tạo bảng, thêm cột, v.v.).
        *   "Cài đặt" các NuGet packages này vào dự án **`.EntityFrameworkCore`** trong solution của bạn.

    2.  **"Tạo" `DbContext` (Database Context):**
        *   "Tạo" một lớp (class) trong dự án `.EntityFrameworkCore`, **"kế thừa"** từ lớp **`AbpDbContext`** của ABP
            Framework.
        *   **"Định nghĩa"** các **`DbSet<TEntity>` properties** cho các **Entities** (thực thể) mà bạn muốn "quản lý"
            bằng EF Core. Mỗi `DbSet` property "đại diện" cho một **"bảng"** (table) trong database.
        *   **"Ghi đè"** (override) phương thức **`OnModelCreating`** để **"cấu hình"** mapping giữa Entities và database
            tables (ví dụ: "đặt tên" bảng, "định nghĩa" các "quan hệ" (relationships) giữa các Entities, "thiết lập"
            các "ràng buộc" (constraints), v.v.).
        *   **"Ví dụ":**

            ```csharp
            // EntityFrameworkCore/MyProjectDbContext.cs (DbContext)

            using Microsoft.EntityFrameworkCore;
            using MyProject.Products; // Tham chiếu đến Domain Layer (Entities)
            using Volo.Abp.Data;
            using Volo.Abp.EntityFrameworkCore;

            namespace MyProject.EntityFrameworkCore
            {
                [ConnectionStringName("Default")] // Sử dụng connection string có tên "Default" (được định nghĩa trong appsettings.json)
                public class MyProjectDbContext : AbpDbContext<MyProjectDbContext> // Kế thừa từ AbpDbContext
                {
                    // Định nghĩa các DbSet properties cho các Entities
                    public DbSet<Product> Products { get; set; } // DbSet cho Entity Product (tương ứng với bảng Products trong database)

                    // ... (Các DbSet properties khác)

                    public MyProjectDbContext(DbContextOptions<MyProjectDbContext> options)
                        : base(options)
                    {
                    }

                    protected override void OnModelCreating(ModelBuilder builder)
                    {
                        base.OnModelCreating(builder);

                        // Cấu hình mapping giữa Entities và database tables (ví dụ)
                        builder.Entity<Product>(b =>
                        {
                            b.ToTable("Products"); // Đặt tên bảng là "Products"
                            b.ConfigureByConvention(); // Áp dụng các quy ước cấu hình của ABP Framework
                            b.Property(x => x.Name).IsRequired().HasMaxLength(128); // Cấu hình thuộc tính Name (bắt buộc, độ dài tối đa 128)
                            // ... (Các cấu hình khác)
                        });

                        // ... (Cấu hình mapping cho các Entities khác)
                    }
                }
            }
            ```

    3.  **"Cấu Hình" Connection String:**
        *   "Cấu hình" **connection string** (chuỗi kết nối) đến database trong file **`appsettings.json`** của dự án
            **`.Web`** (hoặc `.HttpApi.Host`).
        *   **"Ví dụ" (SQL Server):**

            ```json
            // appsettings.json
            {
              "ConnectionStrings": {
                "Default": "Server=localhost;Database=MyProjectDb;Trusted_Connection=True;MultipleActiveResultSets=true" // Connection string cho SQL Server
              },
              // ...
            }
            ```

    4.  **"Tạo" và "Áp Dụng" Database Migrations:**
        *   **Database Migrations** là một "cơ chế" của EF Core để **"quản lý" "schema"** (cấu trúc) của database một
            cách **"có hệ thống"** và **"theo phiên bản"**.
        *   **"Các Bước" "Thực Hiện" Database Migrations:**
            1.  **"Mở" Package Manager Console** (trong Visual Studio) hoặc **Terminal** (trong VS Code).
            2.  **"Chọn"** dự án **`.EntityFrameworkCore`** làm **"Default project"** (trong Package Manager Console)
                hoặc **"di chuyển"** đến thư mục của dự án `.EntityFrameworkCore` (trong Terminal).
            3.  **"Chạy"** lệnh **`Add-Migration <MigrationName>`** để **"tạo"** một **migration** mới. `<MigrationName>`
                là "tên" của migration (ví dụ: `InitialCreate`, `AddProductNameIndex`, v.v.). EF Core sẽ "so sánh"
                "trạng thái" "hiện tại" của Entities (trong code) với "trạng thái" "hiện tại" của database (dựa trên
                các migrations đã "áp dụng" trước đó) và "tạo ra" code C# (migration file) để "cập nhật" database schema
                cho "khớp" với Entities.
            4.  **"Chạy"** lệnh **`Update-Database`** để **"áp dụng"** migration mới lên database. EF Core sẽ "thực thi"
                code C# trong migration file để "tạo" bảng, "thêm" cột, "thay đổi" kiểu dữ liệu, v.v. trong database.
        *   **"Ví dụ":**

            ```bash
            # Trong Package Manager Console (Visual Studio) hoặc Terminal (VS Code) (trong thư mục của dự án .EntityFrameworkCore)

            Add-Migration InitialCreate # Tạo migration mới có tên "InitialCreate"
            Update-Database            # Áp dụng migration lên database
            ```

    5.  **"Sử Dụng" Repositories (trong Application Services) để "Truy Cập" Dữ Liệu:**
        *   **"Inject"** (tiêm) các **Repositories** (ví dụ: `IProductRepository`) vào **Application Services** thông
            qua **constructor**.
        *   **"Sử dụng"** các phương thức của Repositories (ví dụ: `GetAsync`, `GetAllAsync`, `InsertAsync`, `
            UpdateAsync`, `DeleteAsync`) để "truy vấn" và "thao tác" dữ liệu.
        *   ABP Framework sẽ "tự động" "sử dụng" **triển khai** của Repository (ví dụ: `ProductRepository`) "sử dụng"
            Entity Framework Core để "thực hiện" các thao tác trên database.

            ```csharp
            // Application/Products/ProductAppService.cs (Application Service)

            using System;
            using System.Threading.Tasks;
            using Volo.Abp.Application.Services;
            using Volo.Abp.Domain.Repositories;

            namespace MyProject.Products
            {
                public class ProductAppService : ApplicationService, IProductAppService
                {
                    private readonly IProductRepository _productRepository; // Inject IProductRepository

                    public ProductAppService(IProductRepository productRepository)
                    {
                        _productRepository = productRepository;
                    }

                    public async Task<ProductDto> GetAsync(Guid id)
                    {
                        var product = await _productRepository.GetAsync(id); // Sử dụng Repository để lấy Product theo ID
                        return ObjectMapper.Map<Product, ProductDto>(product); // Ánh xạ Product sang ProductDto
                    }

                    // ... (Các phương thức khác)
                }
            }
            ```

**7.2. Repositories (Kho Chứa) - " 'Truy Vấn' " Dữ Liệu "Dễ Dàng" - " 'Giao Diện' " "Thống Nhất" Để "Làm Việc" Với Dữ
Liệu**

- **Repositories - " 'Cầu Nối' " Giữa " 'Logic Nghiệp Vụ' " và " 'Dữ Liệu' "**:

    - **Repositories** (Kho chứa) là các **"lớp"** (classes) "cung cấp" một **"lớp 'trừu tượng' " (abstraction layer)**
      để **"truy cập" dữ liệu** (thường là từ database).
    - Repositories **"ẩn"** các **"chi tiết" "kỹ thuật"** của việc "truy cập" dữ liệu (ví dụ: SQL queries, database
      connection) khỏi các "lớp" "cao hơn" (Application Services, Domain Services). "Giúp" code **"sạch sẽ"** hơn, **"
      dễ bảo trì"** hơn, và **"dễ kiểm thử"** hơn.
    - Repositories "cung cấp" một **"giao diện" "thống nhất"** và **"hướng đối tượng"** để "thao tác" với dữ liệu. Bạn "
      làm việc" với các **"đối tượng"** (objects) (Entities) thay vì phải "viết" các câu truy vấn **SQL** "trực tiếp".

- **`IRepository<TEntity, TKey>` - " 'Giao Diện' " "Chính" Của Repository Trong ABP Framework:**

    - ABP Framework "cung cấp" **"giao diện" `IRepository<TEntity, TKey>`** (và các biến thể của nó) để bạn "định
      nghĩa" các Repositories cho các Entities của bạn.
        *   `TEntity`: "Kiểu" (type) của **Entity** (thực thể) mà Repository sẽ "quản lý" (ví dụ: `Product`, `Order`).
        *   `TKey`: "Kiểu" (type) của **"khóa chính"** (primary key) của Entity (ví dụ: `Guid`, `int`).
    - `IRepository` "cung cấp" các **"phương thức" "cơ bản"** để "thao tác" với dữ liệu:

        *   **`GetAsync(TKey id)`:** Lấy một Entity theo ID.
        *   **`GetAllAsync()`:** Lấy danh sách tất cả các Entities.
        *   **`FirstOrDefaultAsync(...)`:**
        *   **`AnyAsync(...)`:**
        *   **`FindAsync(TKey id)`:** Tìm một entity theo ID
        *   **`InsertAsync(TEntity entity)`:** Thêm một Entity mới.
        *   **`UpdateAsync(TEntity entity)`:** Cập nhật một Entity hiện có.
        *   **`DeleteAsync(TEntity entity)`:** Xóa một Entity.
        *   **`DeleteAsync(TKey id)`:** Xóa theo ID
        *   **`GetListAsync(...)`:** Lấy danh sách có điều kiện.
        *   **`GetCountAsync()`:**
        *   ... (và nhiều phương thức khác - xem tài liệu ABP Framework để biết thêm chi tiết).
    - Ngoài ra có thể dùng `IQueryable`

- **"Sử Dụng" Repositories Trong Application Services:**

    - Bạn **"inject"** (tiêm) các Repositories vào **Application Services** thông qua **constructor**.
    - Bạn "gọi" các phương thức của Repositories để "truy vấn" và "thao tác" dữ liệu trong Application Services.

      ```csharp
      // Application/Products/ProductAppService.cs (Application Service)
      public class ProductAppService : ApplicationService, IProductAppService
      {
          private readonly IProductRepository _productRepository; // Inject IProductRepository

          public ProductAppService(IProductRepository productRepository)
          {
              _productRepository = productRepository;
          }

          public async Task<ProductDto> GetAsync(Guid id)
          {
              var product = await _productRepository.GetAsync(id); // Sử dụng Repository để lấy Product theo ID
              return ObjectMapper.Map<Product, ProductDto>(product); // Ánh xạ Product sang ProductDto
          }
          //...
      }
      ```

**7.3. Unit of Work (Đơn Vị Công Việc) - " 'Đảm Bảo' " "Tính 'Nhất Quán' " Dữ Liệu - " 'Tất Cả' " Hoặc " 'Không Gì Cả'
"**

- **Unit of Work Pattern - " 'Quản Lý' " "Giao Dịch" (Transactions) "Một Cách 'Thông Minh' "**:

    - **Unit of Work** là một **"design pattern"** (mẫu thiết kế) "quản lý" một **"giao dịch"** (transaction) trên
      database và "đảm bảo" **"tính 'nhất quán' "** của dữ liệu khi "thực hiện" "nhiều thao tác" trên database trong
      cùng một "giao dịch".
    - Unit of Work "theo dõi" (track) các "thay đổi" trên các đối tượng (Entities) trong "bộ nhớ" (in-memory) và "áp
      dụng" (apply) tất cả các "thay đổi" này lên database **"cùng một lúc"** khi bạn "gọi" phương thức **"Commit"** (
      hoặc tương tự).
    - Unit of Work "đảm bảo" rằng **"tất cả" các "thay đổi"** được "thực hiện" **"thành công"** hoặc **"không có" "thay
      đổi" nào** được "thực hiện" ( **"all or nothing"** ). Nếu có bất kỳ "lỗi" nào xảy ra trong quá trình "thực hiện"
      các "thay đổi", Unit of Work sẽ **"rollback"** (hủy bỏ) "toàn bộ" "giao dịch", "đảm bảo" dữ liệu "không bị 'mâu
      thuẫn' ".

- **ABP Framework và Unit of Work - " 'Tự Động' " "Quản Lý" Giao Dịch Cho Bạn:**

    - ABP Framework **"tích hợp"** sẵn **Unit of Work pattern**. Bạn **"không cần" "phải 'quản lý' " giao dịch" "
      thủ công"** (bắt đầu giao dịch, commit giao dịch, rollback giao dịch). ABP Framework sẽ **"tự động" "tạo"** và **"
      quản lý"** Unit of Work cho bạn.
    - ABP Framework "sử dụng" **`IUnitOfWork` interface** và **`[UnitOfWork]` attribute** để "đánh dấu" các phương
      thức (ví dụ: phương thức trong Application Service) là một **"đơn vị công việc"**.
        *   **`IUnitOfWork` (Interface):** "Giao diện" để "làm việc" với Unit of Work (thường "không cần" "sử dụng"
            trực tiếp trong code ứng dụng).
        *   **`[UnitOfWork]` Attribute:** "Attribute" (chú thích) để "đánh dấu" một phương thức (ví dụ: phương thức
            trong Application Service) là một **"đơn vị công việc"**. ABP Framework sẽ "tự động" "tạo" một Unit of
            Work khi phương thức này được "gọi" và "commit" (hoặc "rollback") giao dịch khi phương thức "kết thúc".
            *   `[UnitOfWork(IsDisabled = true)]`: Vô hiệu hóa UoW
            *   `[UnitOfWork(TransactionScopeOption = TransactionScopeOption.RequiresNew)]`: Luôn tạo transaction
                mới.
        * **Không cần attribute:** Các phương thức của Application Service mặc định đã được coi là 1 unit of work.

    - **"Ví dụ" (Unit of Work "Tự Động" Trong Application Service):**

      ```csharp
      // Application/Products/ProductAppService.cs (Application Service)

      using System;
      using System.Threading.Tasks;
      using Volo.Abp.Application.Services;
      using Volo.Abp.Domain.Repositories;
      using Volo.Abp.Uow; // Thêm namespace Volo.Abp.Uow

      namespace MyProject.Products
      {
          //[UnitOfWork] // Áp dụng Unit of Work cho toàn bộ Application Service (tùy chọn - ABP Framework "mặc định" coi các phương thức Application Service là Unit of Work)
          public class ProductAppService : ApplicationService, IProductAppService
          {
              private readonly IProductRepository _productRepository;

              public ProductAppService(IProductRepository productRepository)
              {
                  _productRepository = productRepository;
              }

              // Phương thức CreateAsync được "bao bọc" trong một Unit of Work "tự động"
              public async Task<ProductDto> CreateAsync(CreateUpdateProductDto input)
              {
                  // Tạo Product mới
                  var product = new Product(Guid.NewGuid(), input.Name, input.Price);

                  // Lưu Product vào database thông qua Repository
                  await _productRepository.InsertAsync(product);

                  // (Nếu có bất kỳ lỗi nào xảy ra trong quá trình "thực hiện" phương thức này,
                  //  Unit of Work sẽ "tự động" "rollback" giao dịch và "hủy bỏ" các thay đổi trên database)

                  // Ánh xạ Product sang ProductDto và trả về
                  return ObjectMapper.Map<Product, ProductDto>(product);
              }

              // ... (Các phương thức khác)
          }
      }
      ```

        *   Trong ví dụ trên, phương thức `CreateAsync` của `ProductAppService` được "bao bọc" trong một **Unit of
            Work "tự động"**. Khi `CreateAsync` được "gọi", ABP Framework sẽ "tự động" "tạo" một Unit of Work (và một
            database transaction) trước khi "thực hiện" code trong `CreateAsync`. Nếu **"không có" "lỗi"** nào xảy
            ra, Unit of Work sẽ **"tự động" "commit"** giao dịch (lưu các thay đổi vào database) khi `CreateAsync` "
            kết thúc". Nếu **"có" "lỗi"** xảy ra (ví dụ: `Product` không hợp lệ, database bị lỗi, v.v.), Unit of Work sẽ
            **"tự động" "rollback"** giao dịch (hủy bỏ các thay đổi trên database), "đảm bảo" **"tính 'nhất quán' "**
            của dữ liệu.

**Tổng Kết Chương 7:**

-   Bạn đã "khám phá" cách ABP Framework **"xử lý" "truy cập dữ liệu"** (data access), "tích hợp" với **Entity
    Framework Core**, và "sử dụng" **Repositories** và **Unit of Work pattern**.
    -   "Hiểu" **Data Access trong ABP Framework** là gì ("lớp 'trừu tượng' ", "dễ thay đổi" "công nghệ", "sử dụng"
        Repositories và Unit of Work).
    -   "Nắm vững" **Entity Framework Core (EF Core)** và cách ABP Framework **"tích hợp"** với EF Core.
    -   "Biết" cách **"tạo" `DbContext`**, "định nghĩa" **Entities**, "cấu hình" **mapping**, và "thực hiện" **database
        migrations**.
    -   "Hiểu" **Repositories** (kho chứa) là gì, "vai trò" của Repositories, và "cách" "sử dụng" **`IRepository`
        interface** trong ABP Framework.
    -   "Nắm vững" **Unit of Work pattern** và cách ABP Framework **"tự động" "quản lý"** giao dịch (transactions)
        bằng Unit of Work.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 8: Các "Tính Năng" "Xịn Xò" Của ABP Framework**. Chúng ta sẽ "khám phá" các "tính
năng" "nâng cao" và "hữu ích" khác của ABP Framework (Dependency Injection, Localization, Event Bus, Background Jobs,
Caching, v.v.) để "tận dụng" "tối đa" "sức mạnh" của ABP Framework trong ứng dụng của bạn.

Bạn có câu hỏi nào về Data Access, Repositories, Unit of Work, hoặc Entity Framework Core trong ABP Framework không?
Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" ABP
Framework.

