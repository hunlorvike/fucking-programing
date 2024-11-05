# Entity Framework trong C# .NET

## Mục Lục

1. [Tổng Quan về Entity Framework](#1-tổng-quan-về-entity-framework)

   - [Mục Đích](#mục-đích)
   - [Các Phiên Bản](#các-phiên-bản)

2. [Kiến Trúc](#2-kiến-trúc)

3. [Cài Đặt Entity Framework](#3-cài-đặt-entity-framework)

4. [Tạo Mô Hình Dữ Liệu](#4-tạo-mô-hình-dữ-liệu)

5. [Tạo DbContext](#5-tạo-dbcontext)

6. [Các Hoạt Động Cơ Bản với Entity Framework](#6-các-hoạt-động-cơ-bản-với-entity-framework)

   - [a. Thêm Dữ Liệu](#a-thêm-dữ-liệu)
   - [b. Truy Vấn Dữ Liệu](#b-truy-vấn-dữ-liệu)
   - [c. Cập Nhật Dữ Liệu](#c-cập-nhật-dữ-liệu)
   - [d. Xóa Dữ Liệu](#d-xóa-dữ-liệu)

7. [Quản Lý Mối Quan Hệ](#7-quản-lý-mối-quan-hệ)

   - [Mối Quan Hệ Một - Nhiều](#mối-quan-hệ-một---nhiều)
   - [Cấu Hình Mối Quan Hệ](#cấu-hình-mối-quan-hệ)

8. [Migration](#8-migration)

   - [a. Tạo Migration](#a-tạo-migration)
   - [b. Áp Dụng Migration](#b-áp-dụng-migration)

9. [Tóm Tắt](#9-tóm-tắt)

---

### 1. Tổng Quan về Entity Framework

**Entity Framework (EF)** là một framework ORM (Object-Relational Mapping) được phát triển bởi Microsoft, giúp lập trình viên .NET làm việc với cơ sở dữ liệu mà không cần viết nhiều câu lệnh SQL phức tạp. Thay vào đó, lập trình viên có thể thao tác với dữ liệu bằng cách sử dụng các đối tượng trong ứng dụng.

#### Mục Đích

- **Giảm thiểu code SQL**: Thay vì phải viết các câu lệnh SQL thủ công, lập trình viên có thể làm việc với dữ liệu dưới dạng đối tượng.
- **Quản lý dữ liệu**: EF cung cấp các phương thức để dễ dàng thêm, sửa, xóa và truy vấn dữ liệu.

#### Các Phiên Bản

- **Entity Framework 6 (EF6)**: Là phiên bản ổn định, dễ sử dụng, phù hợp cho nhiều ứng dụng doanh nghiệp nhưng không còn được cập nhật thường xuyên.
- **Entity Framework Core (EF Core)**: Là phiên bản mới, nhẹ hơn, hỗ trợ nhiều nền tảng (Windows, Linux, macOS), có hiệu suất tốt hơn và nhiều tính năng mới.

### 2. Kiến Trúc

Entity Framework hoạt động dựa trên mô hình 3 lớp:

- **Model**: Định nghĩa các thực thể (entities) và các mối quan hệ giữa chúng. Đây là nơi bạn sẽ xác định các lớp biểu diễn các bảng trong cơ sở dữ liệu.
- **DbContext**: Lớp trung gian chịu trách nhiệm quản lý các đối tượng thực thể và giao tiếp với cơ sở dữ liệu. `DbContext` là lớp chính mà bạn sẽ sử dụng khi làm việc với EF.
- **Database**: Nơi lưu trữ dữ liệu thực tế. EF giúp bạn thực hiện các thao tác CRUD (Create, Read, Update, Delete) trên cơ sở dữ liệu thông qua các đối tượng.

### 3. Cài Đặt Entity Framework

Để sử dụng Entity Framework trong ứng dụng .NET, bạn cần cài đặt các gói NuGet tương ứng:

- **Đối với EF6**:

  ```bash
  Install-Package EntityFramework
  ```

- **Đối với EF Core**:

  ```bash
  Install-Package Microsoft.EntityFrameworkCore
  Install-Package Microsoft.EntityFrameworkCore.SqlServer  // Nếu bạn sử dụng SQL Server
  ```

### 4. Tạo Mô Hình Dữ Liệu

Mô hình dữ liệu trong EF được tạo ra từ các lớp thực thể, với mỗi lớp tương ứng với một bảng trong cơ sở dữ liệu.

```csharp
public class Product
{
    public int ProductId { get; set; } // Khóa chính
    public string Name { get; set; }    // Tên sản phẩm
    public decimal Price { get; set; }  // Giá sản phẩm
}
```

### 5. Tạo DbContext

`DbContext` quản lý các thực thể và các kết nối đến cơ sở dữ liệu.

```csharp
public class AppDbContext : DbContext
{
    public DbSet<Product> Products { get; set; } // Tập hợp các sản phẩm

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseSqlServer("Your_Connection_String"); // Đường dẫn kết nối đến cơ sở dữ liệu
    }
}
```

### 6. Các Hoạt Động Cơ Bản với Entity Framework

#### a. Thêm Dữ Liệu

Thêm một sản phẩm mới vào cơ sở dữ liệu.

```csharp
using (var context = new AppDbContext())
{
    var product = new Product { Name = "Apple", Price = 1.20m };
    context.Products.Add(product); // Thêm sản phẩm vào DbSet
    context.SaveChanges(); // Lưu thay đổi vào cơ sở dữ liệu
}
```

#### b. Truy Vấn Dữ Liệu

Truy vấn để lấy dữ liệu từ cơ sở dữ liệu.

```csharp
using (var context = new AppDbContext())
{
    var products = context.Products.ToList(); // Lấy tất cả sản phẩm
    var product = context.Products.FirstOrDefault(p => p.ProductId == 1); // Lấy sản phẩm theo ID
}
```

#### c. Cập Nhật Dữ Liệu

Cập nhật thông tin của một sản phẩm đã có trong cơ sở dữ liệu.

```csharp
using (var context = new AppDbContext())
{
    var product = context.Products.First(p => p.ProductId == 1); // Lấy sản phẩm
    product.Price = 1.50m; // Cập nhật giá
    context.SaveChanges(); // Lưu thay đổi vào cơ sở dữ liệu
}
```

#### d. Xóa Dữ Liệu

Xóa một sản phẩm khỏi cơ sở dữ liệu.

```csharp
using (var context = new AppDbContext())
{
    var product = context.Products.First(p => p.ProductId == 1); // Lấy sản phẩm
    context.Products.Remove(product); // Xóa sản phẩm
    context.SaveChanges(); // Lưu thay đổi vào cơ sở dữ liệu
}
```

### 7. Quản Lý Mối Quan Hệ

Entity Framework hỗ trợ quản lý các mối quan hệ giữa các thực thể:

- **Một - Nhiều**: Ví dụ, một danh mục có nhiều sản phẩm.
- **Nhiều - Nhiều**: Ví dụ, một sản phẩm có thể thuộc nhiều danh mục và ngược lại.

#### Mối Quan Hệ Một - Nhiều

```csharp
public class Category
{
    public int CategoryId { get; set; } // Khóa chính
    public string Name { get; set; } // Tên danh mục
    public ICollection<Product> Products { get; set; } // Danh sách sản phẩm
}
```

#### Cấu Hình Mối Quan Hệ

Bạn có thể cấu hình mối quan hệ trong phương thức `OnModelCreating` của `DbContext`.

```csharp
protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.Entity<Product>()
        .HasOne<Category>() // Một sản phẩm thuộc một danh mục
        .WithMany(c => c.Products); // Một danh mục có nhiều sản phẩm
}
```

### 8. Migration

Migration trong Entity Framework giúp bạn quản lý và áp dụng các thay đổi đối với cấu trúc cơ sở dữ liệu theo thời gian.

#### a. Tạo Migration

Khi bạn thực hiện thay đổi trong mô hình dữ liệu, bạn có thể tạo migration mới:

```bash
Add-Migration InitialCreate
```

#### b. Áp Dụng Migration

Để áp dụng các migration đã tạo vào cơ sở dữ liệu:

```bash
Update-Database
```

### 9. Tóm Tắt

Entity Framework là một công cụ mạnh mẽ cho việc tương tác với cơ sở dữ liệu trong .NET. Việc sử dụng EF giúp lập trình viên giảm thiểu khối lượng công việc liên quan đến SQL và tăng cường hiệu suất phát triển ứng dụng.

**Các điểm chính:**

- **Sử dụng Đối Tượng**: Làm việc với dữ liệu dưới dạng các đối tượng.
- **CRUD**: Hỗ trợ các thao tác CRUD dễ dàng.
- **Quản Lý Mối Quan Hệ**: Hỗ trợ các loại mối quan hệ giữa các thực thể.
- **Migration**: Giúp theo dõi và áp dụng thay đổi trong

cơ sở dữ liệu.
