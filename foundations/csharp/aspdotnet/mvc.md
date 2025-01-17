## 1. Tổng quan về ASP.NET Core MVC

### 1.1 Kiến trúc MVC

ASP.NET Core MVC là một framework cho phép phát triển ứng dụng web sử dụng mô hình MVC:

- **Model**: Chứa các lớp đại diện cho dữ liệu và business logic của ứng dụng. Model tương tác với cơ sở dữ liệu và thực
  hiện các xử lý liên quan đến dữ liệu.
- **View**: Thành phần hiển thị giao diện người dùng. View lấy dữ liệu từ Model và hiển thị chúng cho người dùng.
- **Controller**: Điều phối giữa Model và View, nhận các yêu cầu từ người dùng, xử lý và trả về dữ liệu cần thiết.

### 1.2 Cấu hình cơ bản

```csharp
// Program.cs
var builder = WebApplication.CreateBuilder(args);

// Thêm dịch vụ MVC vào ứng dụng
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Cấu hình middleware
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthorization();

// Định tuyến mặc định
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
```

## 2. Cấu trúc Project

Cấu trúc thư mục của dự án ASP.NET Core MVC thường bao gồm các thư mục chính sau:

```plaintext
MyProject/
├── Controllers/           # Chứa các controller (xử lý yêu cầu)
│   ├── HomeController.cs
│   └── AccountController.cs
├── Models/                # Chứa các model (dữ liệu và logic nghiệp vụ)
│   ├── ErrorViewModel.cs
│   └── User.cs
├── Views/                 # Chứa các view (giao diện người dùng)
│   ├── Home/
│   │   ├── Index.cshtml
│   │   └── Privacy.cshtml
│   ├── Shared/
│   │   ├── _Layout.cshtml
│   │   └── Error.cshtml
│   └── _ViewImports.cshtml
├── wwwroot/               # Chứa tài nguyên tĩnh (CSS, JS, hình ảnh)
│   ├── css/
│   ├── js/
│   └── lib/
├── Program.cs             # Điểm vào của ứng dụng
└── appsettings.json       # File cấu hình cho các thiết lập ứng dụng
```

## 3. Controllers

### 3.1 Tạo Controller Cơ Bản

Một Controller là một lớp kế thừa từ `Controller` và chứa các phương thức để xử lý yêu cầu.

```csharp
public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;

    public HomeController(ILogger<HomeController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        return View();
    }

    public IActionResult Privacy()
    {
        return View();
    }
}
```

### 3.2 Các Action Method và Kết quả Trả về

Các Action Method là các phương thức công khai (`public`) trong controller, có nhiệm vụ nhận yêu cầu từ người dùng và
trả về các kiểu kết quả (`ActionResult`).

- `ViewResult`: Trả về một View
- `JsonResult`: Trả về JSON
- `ContentResult`: Trả về nội dung thuần (như text hoặc HTML)
- `FileResult`: Trả về file
- `RedirectResult`: Điều hướng đến một URL khác
- `StatusCodeResult`: Trả về mã trạng thái HTTP

Ví dụ:

```csharp
public class ProductController : Controller
{
    // Trả về View
    public IActionResult Index()
    {
        var products = _productService.GetAll();
        return View(products);
    }

    // Trả về JSON
    public IActionResult GetProductData()
    {
        var product = new { Name = "Sample", Price = 100 };
        return Json(product);
    }

    // Trả về File
    public IActionResult DownloadFile()
    {
        byte[] fileBytes = System.IO.File.ReadAllBytes("path_to_file");
        return File(fileBytes, "application/pdf", "file.pdf");
    }

    // Điều hướng
    public IActionResult RedirectExample()
    {
        return RedirectToAction("Index", "Home");
    }
}
```

## 4. Models

### 4.1 Tạo Model và Định nghĩa Thuộc tính

Model là các lớp đại diện cho dữ liệu và logic nghiệp vụ của ứng dụng.

```csharp
public class Product
{
    public int Id { get; set; }

    [Required(ErrorMessage = "Name is required")]
    [StringLength(100)]
    public string Name { get; set; }

    [Range(0, 1000000)]
    public decimal Price { get; set; }

    [DataType(DataType.MultilineText)]
    public string Description { get; set; }
}
```

### 4.2 View Models

View Model là các lớp đặc biệt dùng để truyền dữ liệu từ Controller tới View. Chúng được tối ưu hóa để hiển thị dữ liệu
mà không liên quan đến cấu trúc dữ liệu trong cơ sở dữ liệu.

```csharp
public class ProductViewModel
{
    public int Id { get; set; }

    [Required]
    public string Name { get; set; }

    [Range(1, 1000)]
    public decimal Price { get; set; }

    public List<SelectListItem> Categories { get; set; }
}
```

## 5. Views

### 5.1 Razor Syntax

ASP.NET Core MVC sử dụng Razor để tạo các trang .cshtml. Razor cho phép nhúng mã C# vào HTML.

```cshtml
@model ProductViewModel

<h2>@Model.Name</h2>
<p>Price: $@Model.Price</p>
<p>Description: @Model.Description</p>
```

### 5.2 Sử dụng Layouts

Layout là file chứa phần chung của các trang. File Layout thường nằm ở thư mục `Views/Shared/_Layout.cshtml`.

```cshtml
<!DOCTYPE html>
<html>
<head>
    <title>@ViewData["Title"] - MyApp</title>
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
        </nav>
    </header>

    <main role="main">
        @RenderBody()
    </main>

    <footer>Footer content here</footer>
</body>
</html>
```

### 5.3 Partial Views

Partial View là các thành phần giao diện nhỏ được tái sử dụng trong các view khác nhau. Chúng có thể được tạo trong
`Views/Shared`.

```cshtml
<!-- Partial view: _ProductCard.cshtml -->
@model Product

<div class="product-card">
    <h3>@Model.Name</h3>
    <p>Price: $@Model.Price</p>
</div>

<!-- Sử dụng partial view -->
<div class="products">
    @foreach (var product in Model.Products)
    {
        <partial name="_ProductCard" model="product" />
    }
</div>
```

## 6. Routing

### 6.1 Định tuyến Mặc định

```csharp
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");
```

### 6.2 Định tuyến với Attribute

```csharp
[Route("api/[controller]")]
public class ProductsController : Controller
{
    [HttpGet("{id}")]
    public IActionResult Get(int id)
    {
        // Trả về thông tin sản phẩm
    }
}
```

## 7. Validation

ASP.NET Core MVC hỗ trợ kiểm tra tính hợp lệ bằng cách sử dụng các thuộc tính Data Annotation như `[Required]`,
`[StringLength]`, `[Range]`,...

```csharp
public class RegisterViewModel
{
    [Required]
    [EmailAddress]
    public string Email { get; set; }

    [Required]
    [StringLength(100, MinimumLength = 6)]
    [DataType(DataType.Password)]
    public string Password { get; set; }

    [DataType(DataType.Password)]
    [Compare("Password", ErrorMessage = "Passwords do not match.")]
    public string ConfirmPassword { get; set; }
}
```

## 8. Dependency Injection (DI)

ASP.NET Core MVC hỗ trợ Dependency Injection để giúp quản lý sự phụ thuộc.

```csharp
// Đăng ký dịch vụ
builder.Services.AddScoped<IProductService, ProductService>();

// Sử dụng trong controller
public class ProductController : Controller
{
    private readonly IProductService _productService;

    public ProductController(IProductService productService)
    {
        _productService = productService;
    }
}
```

## 9. Middleware

Middleware là các thành phần xử lý yêu cầu và phản hồi trong ASP.NET Core.

```csharp
public class RequestLoggingMiddleware
{
    private readonly RequestDelegate _next;

    public RequestLoggingMiddleware(RequestDelegate next)
    {
        _next = next;
    }

    public async Task

 Invoke(HttpContext context)
    {
        Console.WriteLine("Request: " + context.Request.Path);
        await _next(context);
    }
}
```
