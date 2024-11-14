# Các loại Data Loading trong Entity Framework

## Mục Lục

1. [Tổng quan về Data Loading trong Entity Framework](#1-tổng-quan-về-data-loading-trong-entity-framework)
   - [Các phương pháp Data Loading](#các-phương-pháp-data-loading)
2. [Eager Loading](#2-eager-loading)
   - [Eager Loading là gì?](#eager-loading-là-gì)
   - [Cách sử dụng Eager Loading](#cách-sử-dụng-eager-loading)
3. [Lazy Loading](#3-lazy-loading)
   - [Lazy Loading là gì?](#lazy-loading-là-gì)
   - [Cách sử dụng Lazy Loading](#cách-sử-dụng-lazy-loading)
4. [Explicit Loading](#4-explicit-loading)
   - [Explicit Loading là gì?](#explicit-loading-là-gì)
   - [Cách sử dụng Explicit Loading](#cách-sử-dụng-explicit-loading)
5. [So sánh giữa Eager, Lazy và Explicit Loading](#5-so-sánh-giữa-eager-lazy-và-explicit-loading)
6. [Các lớp Entity trong Entity Framework](#6-các-lớp-entity-trong-entity-framework)
7. [Kết luận](#7-kết-luận)

---

### 1. Tổng quan về Data Loading trong Entity Framework

Trong **Entity Framework (EF)**, **Data Loading** đề cập đến cách thức tải dữ liệu liên quan đến các thực thể (entities) có quan hệ với nhau. Việc tải dữ liệu đúng cách ảnh hưởng trực tiếp đến hiệu suất của ứng dụng, đặc biệt khi làm việc với các bảng có quan hệ phức tạp. EF cung cấp ba phương pháp chính để tải dữ liệu:

- **Eager Loading** (Tải dữ liệu ngay lập tức)
- **Lazy Loading** (Tải dữ liệu khi cần)
- **Explicit Loading** (Tải dữ liệu một cách rõ ràng)

### Các phương pháp Data Loading

| **Phương pháp**      | **Khái niệm**                                                                           | **Ưu điểm**                                                    | **Nhược điểm**                                                               |
| -------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Eager Loading**    | Tải tất cả các dữ liệu liên quan ngay khi truy vấn thực thể chính.                      | Tối ưu hiệu suất khi cần nhiều dữ liệu liên quan ngay lập tức. | Tải quá nhiều dữ liệu không cần thiết, có thể gây giảm hiệu suất.            |
| **Lazy Loading**     | Tải dữ liệu liên quan chỉ khi cần (khi truy cập).                                       | Tải dữ liệu linh hoạt, giảm tải ban đầu.                       | Có thể gây ra nhiều truy vấn, dẫn đến hiệu suất kém nếu không kiểm soát tốt. |
| **Explicit Loading** | Tải dữ liệu liên quan sau khi truy vấn thực thể chính, nhưng phải được yêu cầu rõ ràng. | Tải dữ liệu một cách có kiểm soát, tránh tải thừa.             | Cần viết mã rõ ràng hơn, ít tự động như Eager hoặc Lazy Loading.             |

---

### 2. Eager Loading

#### Eager Loading là gì?

**Eager Loading** là phương pháp tải dữ liệu ngay lập tức khi thực hiện truy vấn. Điều này có nghĩa là khi bạn truy vấn một thực thể, các thực thể liên quan (như các bảng con trong quan hệ 1-n hoặc n-n) sẽ được tải đồng thời với thực thể chính trong cùng một truy vấn.

EF sử dụng `Include` để thực hiện Eager Loading.

#### Cách sử dụng Eager Loading

```csharp
using (var context = new MyDbContext())
{
    var orders = context.Orders
                        .Include(o => o.Customer) // Eager load Customer
                        .Include(o => o.OrderItems) // Eager load OrderItems
                        .ToList();
}
```

Trong ví dụ trên:

- `Include(o => o.Customer)` tải dữ liệu của bảng `Customer` liên quan đến mỗi đơn hàng.
- `Include(o => o.OrderItems)` tải dữ liệu của bảng `OrderItems` liên quan đến đơn hàng.

EF sẽ thực hiện một truy vấn SQL với `JOIN` để lấy tất cả dữ liệu của đơn hàng, khách hàng và các mục đơn hàng trong một lần.

---

### 3. Lazy Loading

#### Lazy Loading là gì?

**Lazy Loading** là phương pháp tải dữ liệu khi cần, tức là khi bạn truy cập một thuộc tính của thực thể mà thuộc tính đó chưa được tải. Điều này giúp giảm bớt khối lượng dữ liệu tải về ban đầu. Tuy nhiên, điều này có thể dẫn đến nhiều truy vấn không cần thiết.

Trong EF, Lazy Loading thường được kích hoạt khi các thuộc tính điều hướng của các thực thể có kiểu `virtual`.

#### Cách sử dụng Lazy Loading

Để sử dụng Lazy Loading trong Entity Framework, bạn cần đảm bảo rằng:

1. Các thuộc tính điều hướng phải có kiểu `virtual`.
2. Phải sử dụng proxy (Entity Framework tự động tạo proxy cho các lớp có thuộc tính `virtual`).

```csharp
using (var context = new MyDbContext())
{
    var order = context.Orders.FirstOrDefault(o => o.Id == 1);

    // Dữ liệu Customer và OrderItems chưa được tải
    var customer = order.Customer; // Lazy load Customer
    var items = order.OrderItems.ToList(); // Lazy load OrderItems
}
```

Trong ví dụ trên, dữ liệu của `Customer` và `OrderItems` chỉ được tải khi chúng được truy cập lần đầu tiên.

#### Nhược điểm của Lazy Loading

- **N+1 Query Problem**: Nếu bạn truy vấn nhiều thực thể, có thể tạo ra nhiều truy vấn con, gây giảm hiệu suất. Ví dụ: Truy vấn tất cả các đơn hàng, sau đó tải khách hàng cho từng đơn hàng, dẫn đến N+1 truy vấn.

---

### 4. Explicit Loading

#### Explicit Loading là gì?

**Explicit Loading** là phương pháp tải dữ liệu liên quan khi bạn yêu cầu rõ ràng. Đây là sự kết hợp giữa Eager Loading và Lazy Loading, cho phép bạn tải dữ liệu theo yêu cầu mà không phải đợi nó tự động được tải khi truy cập vào thuộc tính.

#### Cách sử dụng Explicit Loading

```csharp
using (var context = new MyDbContext())
{
    var order = context.Orders.FirstOrDefault(o => o.Id == 1);

    // Explicit load Customer
    context.Entry(order).Reference(o => o.Customer).Load();

    // Explicit load OrderItems
    context.Entry(order).Collection(o => o.OrderItems).Load();
}
```

Trong ví dụ trên:

- `context.Entry(order).Reference(o => o.Customer).Load();` tải dữ liệu của khách hàng cho đơn hàng.
- `context.Entry(order).Collection(o => o.OrderItems).Load();` tải dữ liệu các mục đơn hàng cho đơn hàng.

Phương pháp này giúp bạn kiểm soát chính xác khi nào và cái gì sẽ được tải, tránh tải dữ liệu không cần thiết.

---

### 5. So sánh giữa Eager, Lazy và Explicit Loading

| **Phương pháp**      | **Ưu điểm**                                                          | **Nhược điểm**                                  | **Khi nào sử dụng**                                     |
| -------------------- | -------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------- |
| **Eager Loading**    | - Tải tất cả dữ liệu cần thiết trong một truy vấn.                   | - Có thể tải quá nhiều dữ liệu không cần thiết. | - Khi bạn cần nhiều dữ liệu liên quan ngay lập tức.     |
| **Lazy Loading**     | - Giảm tải ban đầu, tải dữ liệu khi cần thiết.                       | - Có thể gây ra vấn đề N+1 query.               | - Khi dữ liệu liên quan không cần thiết ngay lập tức.   |
| **Explicit Loading** | - Tải dữ liệu khi cần, có thể kiểm soát tốt hơn so với Lazy Loading. | - Cần phải viết mã rõ ràng để tải dữ liệu.      | - Khi bạn muốn kiểm soát chính xác khi nào tải dữ liệu. |

---

### 6. Các lớp Entity trong Entity Framework

Trong Entity Framework, các thực thể (**entities**) là các lớp đại diện cho các bảng trong cơ sở dữ liệu. Mỗi lớp Entity thường có các thuộc tính tương ứng với các cột trong bảng. Để minh họa các phương pháp **Eager Loading**, **Lazy Loading** và **Explicit Loading**, ta sẽ tạo ra một số lớp Entity cơ bản như sau:

#### Class `Order`

```csharp
public class Order
{
    public int Id { get; set; }
    public string OrderNumber { get; set; }
    public int CustomerId { get; set; }

    // Điều hướng tới thực thể Customer (Eager, Lazy, Explicit Load)
    public virtual Customer Customer { get; set; }

    // Điều hướng tới một danh sách OrderItems
    public virtual ICollection<OrderItem> OrderItems { get; set; }
}
```

#### Class `Customer`

```csharp
public class Customer
{
    public int Id { get; set; }
    public string Name { get; set; }

    // Điều hướng tới danh sách các đơn hàng của khách hàng
    public virtual ICollection<Order> Orders { get; set; }
}
```

#### Class `OrderItem`

```csharp
public class OrderItem
{
    public int Id { get; set; }
    public int OrderId { get; set; }
    public string ProductName { get; set; }
    public int Quantity { get; set; }

    // Điều hướng tới thực thể Order
    public virtual Order Order { get; set; }
}
```

#### Class `MyDbContext`

```csharp
public class MyDbContext : DbContext
{
    public DbSet<Order> Orders { get; set; }
    public DbSet<Customer> Customers { get; set; }
    public DbSet<OrderItem> OrderItems { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Thiết lập các quan hệ giữa các thực thể (nếu cần thiết)
        modelBuilder.Entity<Order>()
            .HasOne(o => o.Customer)
            .WithMany(c => c.Orders)
            .HasForeignKey(o => o.CustomerId);

        modelBuilder.Entity<OrderItem>()
            .HasOne(oi => oi.Order)
            .WithMany(o => o.OrderItems)
            .HasForeignKey(oi => oi.OrderId);
    }
}
```

---

### 7. Kết luận

Các phương pháp Data Loading trong Entity Framework – **Eager Loading**, **Lazy Loading**, và **Explicit Loading** – đều có những ưu điểm và nhược điểm riêng. Việc lựa chọn phương pháp nào phụ thuộc vào yêu cầu ứng dụng và cách bạn muốn kiểm soát việc tải dữ liệu.

- **Eager Loading** phù hợp khi bạn cần tải tất cả dữ liệu liên quan ngay từ đầu và tránh truy vấn nhiều lần.
- **Lazy Loading** hữu ích khi bạn không chắc chắn khi nào sẽ cần dữ liệu liên quan và muốn trì hoãn việc tải dữ liệu.
- **Explicit Loading** là sự kết hợp giữa Eager và Lazy, cho phép bạn tải dữ liệu khi cần thiết mà không làm ảnh hưởng đến hiệu suất quá nhiều.
