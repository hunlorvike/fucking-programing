# Routing trong ASP.NET Core: Tổng Quan và Hướng Dẫn

## Mục Lục

1. [Khái niệm về Routing](#khái-niệm-về-routing)
2. [Attribute Routing](#attribute-routing)
    - [2.1. Cách thức hoạt động](#21-cách-thức-hoạt-động)
    - [2.2. Ví dụ với Attribute Routing](#22-ví-dụ-với-attribute-routing)
3. [Endpoint Routing](#endpoint-routing)
    - [3.1. Cách thức hoạt động](#31-cách-thức-hoạt-động)
    - [3.2. Ví dụ với Endpoint Routing](#32-ví-dụ-với-endpoint-routing)
4. [Cấu hình Routing trong ASP.NET Core](#cấu-hình-routing-trong-aspnet-core)
    - [4.1. Đăng ký Routes](#41-đăng-ký-routes)
    - [4.2. Sử dụng Routes trong Controller](#42-sử-dụng-routes-trong-controller)
5. [So sánh Attribute Routing và Endpoint Routing](#so-sánh-attribute-routing-và-endpoint-routing)
6. [Kiểm thử với Routing](#kiểm-thử-với-routing)
7. [Thực hành tốt nhất với Routing](#thực-hành-tốt-nhất-với-routing)
8. [Tóm tắt](#tóm-tắt)

---

## 1. Khái niệm về Routing

**Routing** là cơ chế trong ASP.NET Core giúp ứng dụng ánh xạ các yêu cầu HTTP đến các hành động cụ thể của controller.
Routing quyết định URL nào sẽ được sử dụng để truy cập các tài nguyên và hành động trong ứng dụng.

Routing trong ASP.NET Core có thể được cấu hình theo hai cách chính: **Attribute Routing** và **Endpoint Routing**.

---

## 2. Attribute Routing

**Attribute Routing** cho phép định nghĩa các route trực tiếp trong các hành động (action) của controller thông qua các
thuộc tính (attribute). Đây là một cách tiếp cận mạnh mẽ và linh hoạt, giúp mã nguồn trở nên rõ ràng và dễ quản lý hơn.

### 2.1. Cách thức hoạt động

- **Attribute Routing** hoạt động bằng cách thêm các thuộc tính `[Route]`, `[HttpGet]`, `[HttpPost]`, v.v. vào các
  phương thức trong controller.
- Các route sẽ được ánh xạ trực tiếp từ các attribute này và có thể chứa các tham số động.

**Ví dụ**:

```csharp
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    [HttpGet]
    public IActionResult GetAllProducts()
    {
        return Ok(new string[] { "Product1", "Product2" });
    }

    [HttpGet("{id}")]
    public IActionResult GetProductById(int id)
    {
        return Ok($"Product {id}");
    }
}
```

### 2.2. Ví dụ với Attribute Routing

Dưới đây là một ví dụ về cách sử dụng **Attribute Routing** trong một controller:

```csharp
[Route("api/[controller]")]
public class ProductController : ControllerBase
{
    // Route: GET /api/product
    [HttpGet]
    public IActionResult GetAllProducts()
    {
        return Ok(new { message = "All products" });
    }

    // Route: GET /api/product/{id}
    [HttpGet("{id}")]
    public IActionResult GetProduct(int id)
    {
        return Ok(new { message = $"Product with ID {id}" });
    }

    // Route: POST /api/product
    [HttpPost]
    public IActionResult CreateProduct([FromBody] string productName)
    {
        return Ok(new { message = $"Created product {productName}" });
    }
}
```

Trong ví dụ trên, mỗi action được ánh xạ trực tiếp với các route khác nhau thông qua các thuộc tính `[Route]` và
`[HttpGet]`, `[HttpPost]`.

---

## 3. Endpoint Routing

**Endpoint Routing** là một mô hình mới được giới thiệu trong ASP.NET Core 3.0 và sử dụng trong ASP.NET Core 5.0 trở đi.
Endpoint Routing giúp tách biệt logic định tuyến ra khỏi controller và tập trung vào việc xử lý các yêu cầu HTTP trong
ứng dụng. Nó cung cấp khả năng linh hoạt và mở rộng hơn so với các kỹ thuật routing trước đó.

### 3.1. Cách thức hoạt động

- **Endpoint Routing** hoạt động thông qua cấu hình trong `Startup.cs` hoặc `Program.cs`, nơi các route được đăng ký tại
  thời điểm ứng dụng khởi chạy.
- Các route được đăng ký trực tiếp trong các phương thức cấu hình middleware như `MapGet`, `MapPost`, v.v.

**Ví dụ**:

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Đăng ký các endpoints cho các phương thức HTTP GET, POST
app.MapGet("/api/products", () => new string[] { "Product1", "Product2" });
app.MapGet("/api/products/{id}", (int id) => $"Product {id}");
app.MapPost("/api/products", (string product) => $"Created product {product}");

app.Run();
```

### 3.2. Ví dụ với Endpoint Routing

Trong **Endpoint Routing**, bạn có thể định nghĩa các route ngay trong phương thức `Program.cs`:

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Định nghĩa Endpoint cho HTTP GET và POST
app.MapGet("/api/products", () => new string[] { "Product1", "Product2" });
app.MapGet("/api/products/{id}", (int id) => $"Product with ID {id}");
app.MapPost("/api/products", (string productName) => $"Created product {productName}");

app.Run();
```

Các route không cần phải được đặt trong controller mà có thể trực tiếp ở bất kỳ đâu trong ứng dụng, mang lại sự linh
hoạt hơn trong việc cấu hình và mở rộng.

---

## 4. Cấu hình Routing trong ASP.NET Core

### 4.1. Đăng ký Routes

Trong ASP.NET Core, các route có thể được đăng ký thông qua middleware trong `Program.cs` hoặc `Startup.cs`.

```csharp
public void Configure(IApplicationBuilder app)
{
    app.UseRouting();  // Kích hoạt routing

    app.UseEndpoints(endpoints =>
    {
        // Đăng ký route cho các API
        endpoints.MapControllerRoute(
            name: "default",
            pattern: "{controller=Home}/{action=Index}/{id?}");
    });
}
```

### 4.2. Sử dụng Routes trong Controller

Sử dụng **Attribute Routing** để xác định các route trong controller.

```csharp
[Route("api/[controller]")]
public class ProductController : ControllerBase
{
    [HttpGet]
    public IActionResult GetProducts() => Ok(new[] { "Product1", "Product2" });

    [HttpGet("{id}")]
    public IActionResult GetProduct(int id) => Ok($"Product {id}");
}
```

---

## 5. So sánh Attribute Routing và Endpoint Routing

| **Điểm**               | **Attribute Routing**                        | **Endpoint Routing**                                       |
|------------------------|----------------------------------------------|------------------------------------------------------------|
| **Đăng ký Routes**     | Được đăng ký trực tiếp trong controller      | Được đăng ký trong `Program.cs` hoặc `Startup.cs`          |
| **Linh hoạt**          | Cần phải chỉ định rõ ràng trong từng action  | Linh hoạt hơn, có thể đăng ký tại một nơi chung            |
| **Kết nối Controller** | Phụ thuộc vào controller và hành động        | Không cần controller, có thể định nghĩa endpoint trực tiếp |
| **Khả năng mở rộng**   | Tốt nhưng có thể bị ràng buộc vào controller | Dễ dàng mở rộng và có thể hoạt động ngoài controller       |

---

## 6. Kiểm thử với Routing

### Kiểm thử Attribute Routing

Bạn có thể kiểm thử các route được xác định trong controller bằng cách tạo các unit test và kiểm tra các route của các
hành động.

```csharp
[Fact]
public void Test_GetProductById()
{
    var controller = new ProductController();
    var result = controller.GetProduct(1);
    Assert.IsType<OkObjectResult>(result);
}
```

### Kiểm thử Endpoint Routing

Với Endpoint Routing, bạn có thể sử dụng các công cụ kiểm thử HTTP để kiểm tra các endpoint đã đăng ký.

```csharp
[Fact]
public void Test_Endpoint_GetProducts()
{
    var client = new TestServer(new WebHostBuilder().UseStartup<Startup>()).CreateClient();
    var response = client.GetAsync("/api/products").Result;
    Assert.Equal(HttpStatusCode.OK, response.StatusCode);
}
```

---

## 7. Thực hành tốt nhất với Routing

- **Sử dụng Attribute Routing cho các API RESTful**: Attribute Routing giúp rõ ràng và dễ quản lý cho các API.
- **Sử dụng Endpoint Routing cho các ứng dụng nhẹ và microservices**: Endpoint Routing linh hoạt và dễ mở rộng, đặc biệt
  khi không cần controller.
- **Tách biệt Routes theo các nhóm**: Chia các routes theo vùng (area) hoặc module để dễ dàng quản lý.
- **Đảm bảo rõ ràng trong cách tổ chức Routes**: Giúp dễ dàng duy trì và phát triển ứng dụng.

---

## 8. Tóm tắt

**Routing** là một yếu tố quan trọng trong việc xây dựng các ứng dụng web với ASP.NET Core. **Attribute Routing** cung
cấp sự rõ ràng và dễ dàng khi ánh xạ các route đến các hành động của controller, trong khi **Endpoint Routing** cung cấp
một cách tiếp cận linh hoạt và có thể tách rời hoàn toàn khỏi controller. Việc lựa chọn giữa chúng phụ thuộc vào yêu cầu
cụ thể của ứng dụng, với cả hai đều hỗ trợ mạnh mẽ cho việc phát triển các ứng dụng web hiện đại.
