## ASP.NET Core Web API - Hướng dẫn Toàn diện (Nâng cấp)

### 1. Giới thiệu về Web API

#### **1.1 API và RESTful API**

##### **1.1.1 API (Application Programming Interface)**

- **Mục đích chính:** Là cầu nối giao tiếp giữa client và server, cho phép các ứng dụng khác nhau tương tác với nhau.
- **Đặc điểm nổi bật:**
    - **Giao thức:** Hỗ trợ nhiều giao thức khác nhau như HTTP, TCP/UDP, SOAP.
    - **Định dạng phản hồi:** Không bị ràng buộc, có thể trả về JSON, XML, text, hoặc binary.
    - **Phương thức:** Không bị ràng buộc bởi HTTP methods (có thể tự định nghĩa cách giao tiếp).
    - **Tài nguyên:** Không tập trung vào việc quản lý tài nguyên thông qua URL.

##### **1.1.2 RESTful API**

- **Mục đích chính:** Là một loại API tuân theo các nguyên tắc của REST (Representational State Transfer).
- **Đặc điểm nổi bật:**
    - **Giao thức:** Sử dụng HTTP làm giao thức chính.
    - **Định dạng phản hồi:** Chủ yếu là JSON hoặc XML.
    - **Phương thức:** Tuân thủ các phương thức chuẩn của HTTP như GET, POST, PUT, DELETE.
    - **Tài nguyên:** Mỗi tài nguyên được định danh bằng một URI, quản lý và thao tác thông qua URL.

##### **1.1.3 So sánh API và RESTful API**

| **Tiêu chí**                  | **API**                               | **RESTful API**                    |
|-------------------------------|---------------------------------------|------------------------------------|
| **Giao thức**                 | HTTP, TCP, UDP, SOAP, v.v.            | HTTP                               |
| **Định dạng phản hồi**        | Không ràng buộc định dạng             | Thường là JSON hoặc XML            |
| **Phương thức**               | Không bị ràng buộc                    | GET, POST, PUT, DELETE             |
| **Tài nguyên**                | Không tập trung vào tài nguyên cụ thể | Dựa trên URL để quản lý tài nguyên |
| **Tuân theo nguyên tắc REST** | Không bắt buộc                        | Phải tuân thủ                      |

---

#### **1.2 Web Application vs Web API**

##### **1.2.1 Web Application (Web App)**

- **Đặc điểm chính:**
    - Trả về giao diện người dùng (HTML, CSS, JavaScript) cho client.
    - Thường dành cho người dùng cuối, tương tác qua giao diện web.
    - Phù hợp cho các ứng dụng truyền thống với giao diện người dùng đầy đủ.
- **Ví dụ:** Website thương mại điện tử, blog, diễn đàn.

- **Quy trình hoạt động:**
    1. Người dùng truy cập website qua trình duyệt.
    2. Server xử lý yêu cầu và trả về HTML, CSS, và JavaScript.
    3. Trình duyệt render nội dung và hiển thị.

##### **1.2.2 Web API**

- **Đặc điểm chính:**
    - Trả về dữ liệu (JSON, XML) thay vì giao diện người dùng.
    - Dùng để giao tiếp giữa các hệ thống hoặc ứng dụng.
    - Phù hợp cho ứng dụng di động, single-page applications (SPA), hoặc tích hợp dữ liệu giữa các hệ thống.
- **Ví dụ:** API cho ứng dụng mobile, API cho ứng dụng React/Angular, API tích hợp ERP.

- **Quy trình hoạt động:**
    1. Một ứng dụng (ví dụ: ứng dụng di động) gửi yêu cầu HTTP tới API.
    2. Server xử lý yêu cầu và trả về dữ liệu dạng JSON/XML.
    3. Ứng dụng sử dụng dữ liệu để hiển thị hoặc thực hiện các tác vụ khác.

| **Tiêu chí**             | **Web App**                        | **Web API**                              |
|--------------------------|------------------------------------|------------------------------------------|
| **Phản hồi**             | HTML, CSS, JavaScript              | JSON, XML                                |
| **Mục tiêu**             | Tương tác trực tiếp với người dùng | Giao tiếp giữa các hệ thống              |
| **Giao diện người dùng** | Có giao diện                       | Không có giao diện                       |
| **Ứng dụng phù hợp**     | Web truyền thống                   | SPA, ứng dụng di động, tích hợp hệ thống |

---

#### **1.3 RESTful API trong ASP.NET Core**

ASP.NET Core là framework mạnh mẽ để phát triển RESTful API, giúp xây dựng các API hiệu quả, dễ mở rộng, và tuân theo
các nguyên tắc REST.

##### **1.3.1 Nguyên tắc REST trong ASP.NET Core**

- **Client-Server:**
    - Kiến trúc RESTful trong ASP.NET Core phân tách rõ ràng giữa client và server.
    - Ví dụ: API `GET /api/products` cho phép client nhận danh sách sản phẩm mà không cần biết cách xử lý dữ liệu bên
      trong server.

- **Stateless (Không trạng thái):**
    - Mỗi yêu cầu từ client phải chứa toàn bộ thông tin cần thiết (bao gồm token xác thực).
    - Thực hiện qua JWT hoặc các token tương tự.
    - Ví dụ: Gọi API `POST /api/orders` để tạo đơn hàng, token xác thực sẽ được gửi qua header
      `Authorization: Bearer <token>`.

- **Cacheable (Có khả năng cache):**
    - ASP.NET Core hỗ trợ cấu hình cache response để giảm tải cho server.
    - Ví dụ: Với API `GET /api/products`, server có thể sử dụng `Cache-Control: public, max-age=3600` để client cache
      trong 1 giờ.

- **Uniform Interface:**
    - Sử dụng các phương thức HTTP chuẩn: `GET`, `POST`, `PUT`, `DELETE`.
    - Tài nguyên được quản lý thông qua URI.
    - Ví dụ các endpoint:
        - `GET /api/products`: Lấy danh sách sản phẩm.
        - `GET /api/products/{id}`: Lấy thông tin chi tiết sản phẩm.
        - `POST /api/products`: Thêm sản phẩm mới.
        - `PUT /api/products/{id}`: Cập nhật sản phẩm.
        - `DELETE /api/products/{id}`: Xóa sản phẩm.

- **Layered System (Hệ thống phân lớp):**
    - Middleware trong ASP.NET Core giúp quản lý logging, xác thực, xử lý lỗi.
    - Các lớp như CDN, load balancer có thể được thêm vào để tối ưu hóa.

##### **1.3.2 Ví dụ RESTful API trong ASP.NET Core**

**Ví dụ chi tiết về một API lấy sản phẩm:**

**Request:**

```http
GET /api/products/1 HTTP/1.1
Host: api.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**Response:**

```json
{
    "id": 1,
    "name": "Laptop Gaming",
    "price": 1499.99,
    "category": "Electronics",
    "specifications": {
        "processor": "Intel i7",
        "ram": "16GB",
        "storage": "512GB SSD"
    },
    "inStock": true,
    "lastUpdated": "2024-03-15T10:30:00Z",
    "_links": {
        "self": { "href": "/api/products/1" },
        "reviews": { "href": "/api/products/1/reviews" },
        "related": { "href": "/api/products/1/related" }
    }
}
```

##### **1.3.3 HTTP Status Codes trong RESTful API**

| **Mã HTTP**                   | **Ý nghĩa**                                      |
|-------------------------------|--------------------------------------------------|
| **200 OK**                    | Yêu cầu thành công                               |
| **201 Created**               | Tạo resource mới thành công                      |
| **204 No Content**            | Yêu cầu thành công nhưng không có dữ liệu trả về |
| **400 Bad Request**           | Yêu cầu không hợp lệ                             |
| **401 Unauthorized**          | Không được phép truy cập                         |
| **404 Not Found**             | Resource không tồn tại                           |
| **409 Conflict**              | Xung đột khi thao tác trên resource              |
| **422 Unprocessable Entity**  | Yêu cầu hợp lệ nhưng không thể xử lý             |
| **500 Internal Server Error** | Lỗi server                                       |

### 2. Controllers cho Web API

#### 2.1. Tạo API Controller

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductService _productService;

    public ProductsController(IProductService productService)
    {
        _productService = productService;
    }

    // Controller actions...
}
```

- **Giải thích:**
    - `[ApiController]` Attribute: Ký hiệu cho controller là một API Controller.
    - `[Route("api/[controller]")]` Attribute: Định nghĩa route cho controller.
        - `[controller]` sẽ được thay thế bằng tên controller (ví dụ: "Products").
    - `IProductService`: Interface đại diện cho dịch vụ xử lý sản phẩm.
    - `_productService`: Biến private để truy cập vào dịch vụ sản phẩm.
    - Constructor: Nhận đối tượng `IProductService` từ Dependency Injection để sử dụng trong controller.

#### 2.2. HTTP Request Methods

##### 2.2.1. GET Request

```csharp
// Lấy danh sách
[HttpGet]
public async Task<ActionResult<IEnumerable<Product>>> GetProducts()
{
    var products = await _productService.GetAllAsync();
    return Ok(products);
}

// Lấy chi tiết theo ID
[HttpGet("{id}")]
public async Task<ActionResult<Product>> GetProduct(int id)
{
    var product = await _productService.GetByIdAsync(id);
    if (product == null)
        return NotFound();

    return Ok(product);
}
```

- **Giải thích:**
    - `[HttpGet]` Attribute: Định nghĩa phương thức này xử lý yêu cầu GET.
    - `GetProducts()`: Hàm xử lý yêu cầu lấy danh sách sản phẩm.
    - `GetProduct(int id)`: Hàm xử lý yêu cầu lấy chi tiết sản phẩm theo ID.
    - `_productService.GetAllAsync()`: Gọi hàm của `IProductService` để lấy danh sách sản phẩm.
    - `_productService.GetByIdAsync(id)`: Gọi hàm của `IProductService` để lấy chi tiết sản phẩm theo ID.
    - `Ok(products)`: Trả về HTTP status code 200 OK và danh sách sản phẩm.
    - `NotFound()`: Trả về HTTP status code 404 Not Found khi sản phẩm không tồn tại.

##### 2.2.2. POST Request

```csharp
[HttpPost]
public async Task<ActionResult<Product>> CreateProduct(ProductCreateDto productDto)
{
    if (!ModelState.IsValid)
        return BadRequest(ModelState);

    var product = await _productService.CreateAsync(productDto);
    return CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product);
}
```

- **Giải thích:**
    - `[HttpPost]` Attribute: Định nghĩa phương thức này xử lý yêu cầu POST.
    - `CreateProduct(ProductCreateDto productDto)`: Hàm xử lý yêu cầu tạo sản phẩm mới.
    - `ProductCreateDto`: DTO (Data Transfer Object) chứa thông tin cần thiết để tạo sản phẩm mới.
    - `ModelState.IsValid`: Kiểm tra xem dữ liệu đầu vào (productDto) có hợp lệ hay không.
    - `BadRequest(ModelState)`: Trả về HTTP status code 400 Bad Request nếu dữ liệu đầu vào không hợp lệ.
    - `_productService.CreateAsync(productDto)`: Gọi hàm của `IProductService` để tạo sản phẩm mới.
    - `CreatedAtAction(nameof(GetProduct), new { id = product.Id }, product)`: Trả về HTTP status code 201 Created và
      thông tin sản phẩm mới được tạo.

##### 2.2.3. PUT Request

```csharp
[HttpPut("{id}")]
public async Task<IActionResult> UpdateProduct(int id, ProductUpdateDto productDto)
{
    if (id != productDto.Id)
        return BadRequest();

    try
    {
        await _productService.UpdateAsync(productDto);
    }
    catch (NotFoundException)
    {
        return NotFound();
    }

    return NoContent();
}
```

- **Giải thích:**
    - `[HttpPut("{id}")]` Attribute: Định nghĩa phương thức này xử lý yêu cầu PUT.
    - `UpdateProduct(int id, ProductUpdateDto productDto)`: Hàm xử lý yêu cầu cập nhật sản phẩm.
    - `ProductUpdateDto`: DTO chứa thông tin cần thiết để cập nhật sản phẩm.
    - `id != productDto.Id`: Kiểm tra xem ID trong route và ID trong DTO có khớp nhau hay không.
    - `BadRequest()`: Trả về HTTP status code 400 Bad Request nếu ID không khớp.
    - `_productService.UpdateAsync(productDto)`: Gọi hàm của `IProductService` để cập nhật sản phẩm.
    - `NotFoundException`: Ngoại lệ được ném ra khi sản phẩm không tồn tại.
    - `NotFound()`: Trả về HTTP status code 404 Not Found nếu sản phẩm không tồn tại.
    - `NoContent()`: Trả về HTTP status code 204 No Content khi cập nhật sản phẩm thành công.

##### 2.2.4. DELETE Request

```csharp
[HttpDelete("{id}")]
public async Task<IActionResult> DeleteProduct(int id)
{
    try
    {
        await _productService.DeleteAsync(id);
    }
    catch (NotFoundException)
    {
        return NotFound();
    }

    return NoContent();
}
```

- **Giải thích:**
    - `[HttpDelete("{id}")]` Attribute: Định nghĩa phương thức này xử lý yêu cầu DELETE.
    - `DeleteProduct(int id)`: Hàm xử lý yêu cầu xóa sản phẩm.
    - `_productService.DeleteAsync(id)`: Gọi hàm của `IProductService` để xóa sản phẩm.
    - `NotFoundException`: Ngoại lệ được ném ra khi sản phẩm không tồn tại.
    - `NotFound()`: Trả về HTTP status code 404 Not Found nếu sản phẩm không tồn tại.
    - `NoContent()`: Trả về HTTP status code 204 No Content khi xóa sản phẩm thành công.

### 3. Model Binding và Validation

#### 3.1. Model Binding

- **Binding từ Query String:**

```csharp
[HttpGet]
public IActionResult Get([FromQuery] ProductFilterDto filter)
```

- **Giải thích:**

    - `[FromQuery]` Attribute: Chỉ định rằng dữ liệu được lấy từ query string của URL.
    - `ProductFilterDto`: DTO chứa các thông tin lọc sản phẩm (ví dụ: name, price).
    - **Ví dụ URL:** `/api/products?name=Sản phẩm A&price=100000`

- **Binding từ Request Body:**

```csharp
[HttpPost]
public IActionResult Create([FromBody] ProductCreateDto product)
```

- **Giải thích:**

    - `[FromBody]` Attribute: Chỉ định rằng dữ liệu được lấy từ body của request.
    - `ProductCreateDto`: DTO chứa thông tin sản phẩm mới.
    - **Ví dụ Request Body:**

  ```json
  {
    "name": "Sản phẩm D",
    "price": 400000
  }
  ```

- **Binding từ Route:**

```csharp
[HttpGet("{id}")]
public IActionResult GetById([FromRoute] int id)
```

- **Giải thích:**

    - `[FromRoute]` Attribute: Chỉ định rằng dữ liệu được lấy từ route parameter.
    - `id`: Biến int nhận giá trị ID từ route parameter.
    - **Ví dụ URL:** `/api/products/123`

- **Binding từ Form:**

```csharp
[HttpPost]
public IActionResult Upload([FromForm] ProductImageDto imageData)
```

- **Giải thích:**

    - `[FromForm]` Attribute: Chỉ định rằng dữ liệu được lấy từ form data.
    - `ProductImageDto`: DTO chứa thông tin file ảnh (ví dụ: file, fileName).
    - **Ví dụ Request Body (multipart/form-data):**

  ```
  --boundary
  Content-Disposition: form-data; name="file"; filename="image.jpg"
  Content-Type: image/jpeg

  (Nội dung file image.jpg)
  --boundary--
  ```

#### 3.2. Data Annotations

```csharp
public class ProductCreateDto
{
    [Required(ErrorMessage = "Tên sản phẩm là bắt buộc")]
    [StringLength(100)]
    public string Name { get; set; }

    [Range(0, double.MaxValue)]
    public decimal Price { get; set; }

    [Required]
    [MinLength(10)]
    public string Description { get; set; }

    [EmailAddress]
    public string ContactEmail { get; set; }
}
```

- **Giải thích:**
    - **Data Annotations:** Các attribute được sử dụng để xác định quy tắc validate cho thuộc tính của DTO.
    - `[Required]` Attribute: Yêu cầu trường phải có giá trị.
    - `[StringLength]` Attribute: Giới hạn độ dài của chuỗi.
    - `[Range]` Attribute: Giới hạn phạm vi giá trị.
    - `[MinLength]` Attribute: Yêu cầu độ dài tối thiểu của chuỗi.
    - `[EmailAddress]` Attribute: Kiểm tra xem giá trị có hợp lệ là địa chỉ email hay không.

#### 3.3. Custom Validation

```csharp
public class CustomValidationAttribute : ValidationAttribute
{
    protected override ValidationResult IsValid(object value, ValidationContext validationContext)
    {
        // Custom validation logic
        if (/* _ validation condition _ */)
        {
            return ValidationResult.Success;
        }

        return new ValidationResult("Custom error message");
    }
}
```

- **Giải thích:**
    - Tạo một attribute class kế thừa từ `ValidationAttribute`.
    - Override phương thức `IsValid()` để thực hiện logic validate.
    - `ValidationResult.Success`: Trả về giá trị thành công nếu dữ liệu hợp lệ.
    - `new ValidationResult("Custom error message")`: Trả về giá trị lỗi với thông điệp lỗi.

### 4. Authentication và Authorization

#### 4.1. JWT Configuration

```csharp
// Startup.cs
public void ConfigureServices(IServiceCollection services)
{
    services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidateAudience = true,
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            ValidIssuer = Configuration["Jwt:Issuer"],
            ValidAudience = Configuration["Jwt:Audience"],
            IssuerSigningKey = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(Configuration["Jwt:Key"]))
        };
    });
}
```

- **Giải thích:**
    - `AddAuthentication(JwtBearerDefaults.AuthenticationScheme)`: Cấu hình Authentication middleware sử dụng JWT.
    - `AddJwtBearer(options => ...)`: Cấu hình các tham số cho JWT.
        - `ValidateIssuer`: Kiểm tra issuer của token.
        - `ValidateAudience`: Kiểm tra audience của token.
        - `ValidateLifetime`: Kiểm tra thời hạn của token.
        - `ValidateIssuerSigningKey`: Kiểm tra key được sử dụng để ký token.
        - `ValidIssuer`, `ValidAudience`, `IssuerSigningKey`: Các giá trị được lấy từ `Configuration` (file
          appsettings.json).

#### 4.2. JWT Token Generation

```csharp
public class AuthService
{
    public string GenerateJwtToken(User user)
    {
        var claims = new[]
        {
            new Claim(ClaimTypes.NameIdentifier, user.Id.ToString()),
            new Claim(ClaimTypes.Name, user.Username),
            new Claim(ClaimTypes.Role, user.Role)
        };

        var key = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_configuration["Jwt:Key"]));
        var credentials = new SigningCredentials(key, SecurityAlgorithms.HmacSha256);

        var token = new JwtSecurityToken(
            issuer: _configuration["Jwt:Issuer"],
            audience: _configuration["Jwt:Audience"],
            claims: claims,
            expires: DateTime.Now.AddHours(3),
            signingCredentials: credentials
        );

        return new JwtSecurityTokenHandler().WriteToken(token);
    }
}
```

- **Giải thích:**
    - `GenerateJwtToken(User user)`: Hàm tạo JWT token.
    - `claims`: Mảng các claims chứa thông tin về người dùng.
    - `key`: Key được sử dụng để ký token.
    - `credentials`: Chứa thông tin về key và algorithm được sử dụng để ký token.
    - `token`: Đối tượng JwtSecurityToken chứa thông tin về token.
    - `WriteToken()`: Hàm của `JwtSecurityTokenHandler` để tạo chuỗi token.

#### 4.3. Protecting API Endpoints

```csharp
[Authorize]
[ApiController]
[Route("api/[controller]")]
public class SecureController : ControllerBase
{
    [Authorize(Roles = "Admin")]
    [HttpGet("admin-only")]
    public IActionResult AdminOnlyEndpoint()
    {
        return Ok("You are an admin!");
    }

    [Authorize(Policy = "RequireManagerRole")]
    [HttpGet("manager-only")]
    public IActionResult ManagerOnlyEndpoint()
    {
        return Ok("You are a manager!");
    }
}
```

- **Giải thích:**
    - `[Authorize]` Attribute: Yêu cầu người dùng phải được xác thực (authentication) trước khi truy cập vào controller.
    - `[Authorize(Roles = "Admin")]` Attribute: Yêu cầu người dùng phải có vai trò "Admin" để truy cập vào endpoint.
    - `[Authorize(Policy = "RequireManagerRole")]` Attribute: Yêu cầu người dùng phải đáp ứng chính sách "
      RequireManagerRole" để truy cập vào endpoint.

#### 4.4. Policy-based Authorization

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddAuthorization(options =>
    {
        options.AddPolicy("RequireManagerRole", policy =>
            policy.RequireRole("Manager", "Admin"));

        options.AddPolicy("RequireUserDepartment", policy =>
            policy.RequireClaim("Department", "IT", "HR"));
    });
}
```

- **Giải thích:**
    - `AddAuthorization(options => ...)`: Cấu hình Authorization middleware.
    - `AddPolicy()`: Định nghĩa một Authorization Policy.
        - `RequireRole()`: Yêu cầu người dùng phải có vai trò cụ thể.
        - `RequireClaim()`: Yêu cầu người dùng phải có claim cụ thể.

### 5. Error Handling và Middleware

#### 5.1. Global Exception Handler

```csharp
public class GlobalExceptionMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<GlobalExceptionMiddleware> _logger;

    public GlobalExceptionMiddleware(RequestDelegate next,
        ILogger<GlobalExceptionMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        try
        {
            await _next(context);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "An unhandled exception occurred.");
            await HandleExceptionAsync(context, ex);
        }
    }

    private static Task HandleExceptionAsync(HttpContext context, Exception exception)
    {
        context.Response.ContentType = "application/json";
        context.Response.StatusCode = exception switch
        {
            NotFoundException => StatusCodes.Status404NotFound,
            ValidationException => StatusCodes.Status400BadRequest,
            UnauthorizedAccessException => StatusCodes.Status401Unauthorized,
            _ => StatusCodes.Status500InternalServerError
        };

        return context.Response.WriteAsync(new ErrorResponse
        {
            StatusCode = context.Response.StatusCode,
            Message = exception.Message
        }.ToString());
    }
}
```

- **Giải thích:**
    - `GlobalExceptionMiddleware`: Middleware xử lý các ngoại lệ (exception) không được xử lý bởi các middleware khác.
    - `InvokeAsync(HttpContext context)`: Phương thức xử lý request.
    - `try...catch`: Bắt các ngoại lệ trong quá trình xử lý request.
    - `_logger.LogError(ex, "An unhandled exception occurred.")`: Ghi log lỗi.
    - `HandleExceptionAsync(HttpContext context, Exception exception)`: Hàm xử lý ngoại lệ, trả về mã lỗi và thông điệp
      lỗi cho client.

### 6. API Versioning

#### 6.1. Configuration

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddApiVersioning(options =>
    {
        options.DefaultApiVersion = new ApiVersion(1, 0);
        options.AssumeDefaultVersionWhenUnspecified = true;
        options.ReportApiVersions = true;
    });
}
```

- **Giải thích:**
    - `AddApiVersioning(options => ...)`: Cấu hình API Versioning middleware.
    - `DefaultApiVersion`: Phiên bản API mặc định.
    - `AssumeDefaultVersionWhenUnspecified`: Giả sử phiên bản API mặc định khi client không cung cấp phiên bản.
    - `ReportApiVersions`: Trả về thông tin về các phiên bản API trong response.

#### 6.2. Versioned Controllers

```csharp
[ApiController]
[ApiVersion("1.0")]
[Route("api/v{version:apiVersion}/[controller]")]
public class ProductsV1Controller : ControllerBase
{
    // V1 implementation
}

[ApiController]
[ApiVersion("2.0")]
[Route("api/v{version:apiVersion}/[controller]")]
public class ProductsV2Controller : ControllerBase
{
    // V2 implementation
}
```

- **Giải thích:**
    - `[ApiVersion("1.0")]`, `[ApiVersion("2.0")]`: Định nghĩa phiên bản cho từng controller.
    - `Route("api/v{version:apiVersion}/[controller]")]`: Định nghĩa route cho controller, bao gồm phiên bản API trong
      URL.
    - **Ví dụ URL:**
        - `/api/v1/products`: Truy cập phiên bản 1.0 của API.
        - `/api/v2/products`: Truy cập phiên bản 2.0 của API.

### 7. API Documentation

#### 7.1. Swagger Configuration

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddSwaggerGen(c =>
    {
        c.SwaggerDoc("v1", new OpenApiInfo
        {
            Title = "My API",
            Version = "v1"
        });

        // Add JWT Authentication
        c.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
        {
            Description = "JWT Authorization header using the Bearer scheme.",
            Name = "Authorization",
            In = ParameterLocation.Header,
            Type = SecuritySchemeType.ApiKey,
            Scheme = "Bearer"
        });

        c.AddSecurityRequirement(new OpenApiSecurityRequirement
        {
            {
                new OpenApiSecurityScheme
                {
                    Reference = new OpenApiReference
                    {
                        Type = ReferenceType.SecurityScheme,
                        Id = "Bearer"
                    }
                },
                Array.Empty<string>()
            }
        });
    });
}
```

- **Giải thích:**
    - `AddSwaggerGen(c => ...)`: Cấu hình Swagger middleware.
    - `SwaggerDoc("v1", new OpenApiInfo {...})`: Định nghĩa thông tin cho API documentation.
    - `AddSecurityDefinition()`: Định nghĩa schema cho JWT authentication.
    - `AddSecurityRequirement()`: Yêu cầu client phải cung cấp JWT token để truy cập vào API.

#### 7.2. XML Comments

```csharp
/// <summary>
/// Retrieves a specific product by its ID.
/// </summary>
/// <param name="id">The ID of the product to retrieve</param>
/// <returns>The requested product</returns>
/// <response code="200">Returns the requested product</response>
/// <response code="404">If the product is not found</response>
[HttpGet("{id}")]
[ProducesResponseType(typeof(Product), StatusCodes.Status200OK)]
[ProducesResponseType(StatusCodes.Status404NotFound)]
public async Task<ActionResult<Product>> GetProduct(int id)
{
    var product = await _productService.GetByIdAsync(id);
    if (product == null)
        return NotFound();

    return Ok(product);
}
```

- **Giải thích:**
    - **XML Comments:** Các comment được viết trong code để tạo tài liệu cho API.
    - `/// <summary> ... </summary>`: Mô tả chung của action.
    - `/// <param name="id"> ... </param>`: Mô tả tham số của action.
    - `/// <returns> ... </returns>`: Mô tả giá trị trả về của action.
    - `/// <response code="200"> ... </response>`: Mô tả HTTP status code trả về.
    - `[ProducesResponseType(typeof(Product), StatusCodes.Status200OK)]`: Chỉ định type dữ liệu trả về cho HTTP status
      code 200 OK.
    - `[ProducesResponseType(StatusCodes.Status404NotFound)]`: Chỉ định HTTP status code 404 NotFound khi sản phẩm không
      tồn tại.

### 8. Testing

#### 8.1. Unit Testing Controllers

```csharp
public class ProductsControllerTests
{
    private readonly Mock<IProductService> _mockService;
    private readonly ProductsController _controller;

    public ProductsControllerTests()
    {
        _mockService = new Mock<IProductService>();
        _controller = new ProductsController(_mockService.Object);
    }

    [Fact]
    public async Task GetProduct_WithValidId_ReturnsProduct()
    {
        // Arrange
        var productId = 1;
        var expectedProduct = new Product { Id = productId, Name = "Test Product" };
        _mockService.Setup(s => s.GetByIdAsync(productId))
            .ReturnsAsync(expectedProduct);

        // Act
        var result = await _controller.GetProduct(productId);

        // Assert
        var okResult = Assert.IsType<OkObjectResult>(result.Result);
        var returnedProduct = Assert.IsType<Product>(okResult.Value);
        Assert.Equal(expectedProduct.Id, returnedProduct.Id);
        Assert.Equal(expectedProduct.Name, returnedProduct.Name);
    }
}
```

- **Giải thích:**
    - `ProductsControllerTests`: Class test cho `ProductsController`.
    - `Mock<IProductService>`: Mô phỏng `IProductService` để sử dụng trong test.
    - `Setup(s => s.GetByIdAsync(productId)) .ReturnsAsync(expectedProduct)`: Cấu hình mock để trả về giá trị mong đợi
      khi gọi hàm `GetByIdAsync()`.
    - `Assert.IsType<>()`: Kiểm tra type của kết quả trả về.
    - `Assert.Equal()`: Kiểm tra xem kết quả trả về có khớp với giá trị mong đợi hay không.

#### 8.2. Integration Testing

```csharp
public class ProductsApiIntegrationTests : IClassFixture<WebApplicationFactory<Startup>>
{
    private readonly WebApplicationFactory<Startup> _factory;
    private readonly HttpClient _client;

    public ProductsApiIntegrationTests(WebApplicationFactory<Startup> factory)
    {
        _factory = factory;
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task GetProducts_ReturnsSuccessStatusCode()
    {
        // Arrange
        var url = "/api/products";

        // Act
        var response = await _client.GetAsync(url);

        // Assert
        response.EnsureSuccessStatusCode();
        Assert.Equal("application/json", response.Content.Headers.ContentType.MediaType);
    }
}
```

- **Giải thích:**
    - `ProductsApiIntegrationTests`: Class test tích hợp cho API.
    - `WebApplicationFactory<Startup>`: Khởi tạo một web application để sử dụng trong test.
    - `HttpClient`: Client để gửi yêu cầu tới API.
    - `EnsureSuccessStatusCode()`: Kiểm tra xem response có mã lỗi thành công (2xx) hay không.
    - `Assert.Equal()`: Kiểm tra xem type của response có phù hợp hay không.

### 9. Performance Optimization

#### 9.1. Response Caching

```csharp
[HttpGet]
[ResponseCache(Duration = 60)] // Cache for 1 minute
public async Task<ActionResult<IEnumerable<Product>>> GetProducts()
{
    var products = await _productService.GetAllAsync();
    return Ok(products);
}
```

- **Giải thích:**
    - `[ResponseCache]` Attribute: Cấu hình caching cho response.
    - `Duration`: Thời gian cache (tính bằng giây).
    - **Hoạt động:** Khi client gửi yêu cầu lần đầu tiên, response sẽ được cache trong 60 giây. Các yêu cầu tiếp theo
      trong vòng 60 giây sẽ được lấy từ cache.

#### 9.2. Compression

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddResponseCompression(options =>
    {
        options.Providers.Add<GzipCompressionProvider>();
        options.Providers.Add<BrotliCompressionProvider>();
        options.EnableForHttps = true;
    });
}
```

- **Giải thích:**
    - `AddResponseCompression(options => ...)`: Cấu hình Response Compression middleware.
    - `Providers.Add<GzipCompressionProvider>()`, `Providers.Add<BrotliCompressionProvider>()`: Thêm các provider để nén
      response.
    - `EnableForHttps`: Bật nén cho kết nối HTTPS.
    - **Hoạt động:** Middleware sẽ nén response trước khi gửi cho client. Việc nén giúp giảm dung lượng dữ liệu truyền
      tải, cải thiện hiệu năng.

### 10. Best Practices

#### 10.1. API Design Guidelines

- **Sử dụng danh từ số nhiều cho tên resources:** `api/products`, `api/customers`.
- **Sử dụng HTTP methods đúng mục đích:** `GET` cho lấy dữ liệu, `POST` cho tạo mới, `PUT` cho cập nhật, `DELETE` cho
  xóa.
- **Trả về đúng HTTP status codes:** 200, 201, 400, 401, 404, 500.
- **Implement paging cho collections lớn:** Tránh trả về toàn bộ danh sách sản phẩm, chỉ trả về một số lượng nhỏ, có thể
  phân trang.
- **Sử dụng versioning cho API:** Giúp quản lý các phiên bản API và tránh xung đột.
- **Implement HATEOAS khi cần thiết:** Thêm thông tin liên kết (link) để client dễ dàng tìm hiểu cách tương tác với API.
- **Xử lý lỗi một cách nhất quán:** Trả về các mã lỗi và thông điệp rõ ràng để client xử lý lỗi.
- **Validate input data:** Kiểm tra dữ liệu đầu vào để đảm bảo tính hợp lệ.
- **Sử dụng DTOs để kiểm soát data exposure:** Tránh lộ toàn bộ thông tin từ model, chỉ trả về các thuộc tính cần thiết.

#### 10.2. Security Best Practices

- **Sử dụng HTTPS:** Bảo mật kết nối giữa client và server.
- **Implement Rate Limiting:** Giới hạn số lượng yêu cầu từ một IP address để chống DDos.
- **Secure Headers Middleware:** Bảo mật các header của response (X-Frame-Options, X-Content-Type-Options,
  X-XSS-Protection).

### 11. Advanced Features

#### 11.1. Real-time Communication với SignalR

- **Hub Definition:**

```csharp
public class NotificationHub : Hub
{
    public async Task SendMessage(string user, string message)
    {
        await Clients.All.SendAsync("ReceiveMessage", user, message);
    }
}
```

- **Giải thích:**

    - `NotificationHub`: Class Hub của SignalR.
    - `SendMessage(string user, string message)`: Phương thức gửi thông báo đến tất cả các client kết nối.
    - `Clients.All`: Biểu thị tất cả các client kết nối.
    - `SendAsync("ReceiveMessage", user, message)`: Gửi thông báo đến client với tên method "ReceiveMessage" và dữ liệu
      là `user` và `message`.

- **Startup Configuration:**

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddSignalR();
}

public void Configure(IApplicationBuilder app)
{
    app.UseEndpoints(endpoints =>
    {
        endpoints.MapHub<NotificationHub>("/notificationHub");
    });
}
```

- **Giải thích:**
    - `services.AddSignalR()`: Cấu hình SignalR middleware.
    - `endpoints.MapHub<NotificationHub>("/notificationHub")`: Mapping Hub `NotificationHub` với endpoint
      `/notificationHub`.

#### 11.2. Background Tasks

```csharp
public class BackgroundWorkerService : BackgroundService
{
    private readonly ILogger<BackgroundWorkerService> _logger;

    public BackgroundWorkerService(ILogger<BackgroundWorkerService> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            _logger.LogInformation("Worker running at: {time}", DateTimeOffset.Now);
            await Task.Delay(1000, stoppingToken);
        }
    }
}
```

- **Giải thích:**
    - `BackgroundWorkerService`: Class thực hiện background tasks.
    - `ExecuteAsync(CancellationToken stoppingToken)`: Phương thức chính của background tasks.
    - `while (!stoppingToken.IsCancellationRequested)`: Vòng lặp chạy liên tục cho đến khi `stoppingToken` được hủy.
    - `Task.Delay(1000, stoppingToken)`: Chờ 1 giây (1000 mili giây) trước khi thực hiện lại vòng lặp.

#### 11.3. File Upload/Download

```csharp
[ApiController]
[Route("api/[controller]")]
public class FilesController : ControllerBase
{
    private readonly IFileService _fileService;

    [HttpPost("upload")]
    public async Task<IActionResult> Upload(IFormFile file)
    {
        if (file == null || file.Length == 0)
            return BadRequest("File is empty");

        var fileName = await _fileService.SaveFileAsync(file);
        return Ok(new { fileName });
    }

    [HttpGet("download/{fileName}")]
    public async Task<IActionResult> Download(string fileName)
    {
        var fileStream = await _fileService.GetFileStreamAsync(fileName);
        if (fileStream == null)
            return NotFound();

        return File(fileStream, "application/octet-stream", fileName);
    }
}
```

- **Giải thích:**
    - `FilesController`: Controller xử lý chức năng upload và download file.
    - `IFileService`: Interface đại diện cho dịch vụ xử lý file.
    - `_fileService`: Biến private để truy cập vào dịch vụ file.
    - `Upload(IFormFile file)`: Hàm xử lý yêu cầu upload file.
        - `IFormFile`: Đối tượng đại diện cho file được upload.
        - `SaveFileAsync(file)`: Gọi hàm của `IFileService` để lưu file vào server.
        - `Ok(new { fileName })`: Trả về HTTP status code 200 OK và tên file đã lưu.
    - `Download(string fileName)`: Hàm xử lý yêu cầu download file.
        - `GetFileStreamAsync(fileName)`: Gọi hàm của `IFileService` để lấy stream của file.
        - `NotFound()`: Trả về HTTP status code 404 Not Found nếu file không tồn tại.
        - `File(fileStream, "application/octet-stream", fileName)`: Trả về response là stream của file, cùng với header
          Content-Type là "application/octet-stream" và tên file để client download.

### 12. Logging và Monitoring

#### 12.1. Structured Logging

```csharp
public class ProductsController : ControllerBase
{
    private readonly ILogger<ProductsController> _logger;

    public ProductsController(ILogger<ProductsController> logger)
    {
        _logger = logger;
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<Product>> GetProduct(int id)
    {
        _logger.LogInformation(
            "Getting product with ID: {ProductId} at {RequestTime}",
            id,
            DateTime.UtcNow);

        try
        {
            var product = await _productService.GetByIdAsync(id);
            if (product == null)
            {
                _logger.LogWarning("Product not found: {ProductId}", id);
                return NotFound();
            }

            return Ok(product);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error getting product {ProductId}", id);
            throw;
        }
    }
}
```

- **Giải thích:**
    - `ILogger<ProductsController>`: Interface đại diện cho logger, được inject vào controller.
    - `_logger`: Biến private để truy cập vào logger.
    - `LogInformation()`, `LogWarning()`, `LogError()`: Các phương thức của logger để ghi log thông tin, cảnh báo, lỗi.
    - **Hoạt động:**
        - Khi controller xử lý request, logger sẽ ghi log thông tin về request, thời gian xử lý, và các ngoại lệ xảy ra.
        - Các thông tin log có thể được lưu vào file, database hoặc console để tiện theo dõi và gỡ lỗi.

#### 12.2. Health Checks

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddHealthChecks()
    .AddDbContextCheck<ApplicationDbContext>()
    .AddUrlGroup(new Uri("https://external-api.com/health"), "External API")
    .AddCheck("Disk Space", () =>
    {
        var freeSpace = GetFreeDiskSpace();
        return freeSpace > 500_000_000
            ? HealthCheckResult.Healthy()
            : HealthCheckResult.Degraded();
    });
}

public void Configure(IApplicationBuilder app)
{
    app.UseEndpoints(endpoints =>
    {
        endpoints.MapHealthChecks("/health", new HealthCheckOptions
        {
            ResponseWriter = async (context, report) =>
            {
                context.Response.ContentType = "application/json";
                var result = JsonSerializer.Serialize(new
                {
                    status = report.Status.ToString(),
                    checks = report.Entries.Select(e => new
                    {
                        name = e.Key,
                        status = e.Value.Status.ToString(),
                        description = e.Value.Description
                    })
                });
                await context.Response.WriteAsync(result);
            }
        });
    });
}
```

- **Giải thích:**
    - `AddHealthChecks()`: Cấu hình Health Checks middleware.
    - `AddDbContextCheck()`: Kiểm tra kết nối đến database.
    - `AddUrlGroup()`: Kiểm tra kết nối đến một URL (external API).
    - `AddCheck()`: Thêm một Health Check tùy chỉnh.
    - **Hoạt động:**
        - Middleware sẽ kiểm tra trạng thái sức khỏe của các service và trả về response với thông tin về trạng thái của
          từng service.
        - Endpoint `/health` có thể được sử dụng để giám sát trạng thái sức khỏe của API.

### 13. Dependency Injection và Service Lifetime

#### 13.1. Service Registration

```csharp
public void ConfigureServices(IServiceCollection services)
{
    // Transient: Tạo mới mỗi lần request
    services.AddTransient<ITransientService, TransientService>();

    // Scoped: Tạo mới mỗi HTTP request
    services.AddScoped<IScopedService, ScopedService>();

    // Singleton: Tạo một lần duy nhất
    services.AddSingleton<ISingletonService, SingletonService>();

    // Factory Pattern
    services.AddTransient<IProductService>(provider =>
    {
        var dbContext = provider.GetRequiredService<ApplicationDbContext>();
        var logger = provider.GetRequiredService<ILogger<ProductService>>();
        return new ProductService(dbContext, logger);
    });
}
```

- **Giải thích:**
    - `services.AddTransient()`, `services.AddScoped()`, `services.AddSingleton()`: Các phương thức để đăng ký service.
    - **Transient:** Service sẽ được tạo mới mỗi lần request.
    - **Scoped:** Service sẽ được tạo mới mỗi HTTP request.
    - **Singleton:** Service sẽ được tạo một lần duy nhất cho toàn bộ application.
    - **Factory Pattern:** Sử dụng factory để tạo service.
    - **Hoạt động:**
        - Khi controller cần sử dụng service, Dependency Injection sẽ inject service vào controller.
        - Vòng đời của service được quản lý bởi Dependency Injection dựa trên loại đăng ký (transient, scoped,
          singleton).

#### 13.2. Service Consumption

```csharp
public class ProductsController : ControllerBase
{
    private readonly IProductService _productService;
    private readonly ILogger<ProductsController> _logger;
    private readonly IConfiguration _configuration;

    public ProductsController(
        IProductService productService,
        ILogger<ProductsController> logger,
        IConfiguration configuration)
    {
        _productService = productService;
        _logger = logger;
        _configuration = configuration;
    }
}
```

- **Giải thích:**
    - Các service (`IProductService`, `ILogger<ProductsController>`, `IConfiguration`) được inject vào constructor của
      controller.
    - Dependency Injection tự động tạo instance của các service và inject vào controller.

### 14. API Documentation và Client Generation

#### 14.1. Swagger UI Customization

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddSwaggerGen(c =>
    {
        c.SwaggerDoc("v1", new OpenApiInfo
        {
            Title = "My API",
            Version = "v1",
            Description = "A simple example ASP.NET Core Web API",
            Contact = new OpenApiContact
            {
                Name = "Your Name",
                Email = "your.email@example.com",
                Url = new Uri("https://example.com")
            },
            License = new OpenApiLicense
            {
                Name = "Use under MIT",
                Url = new Uri("https://opensource.org/licenses/MIT")
            }
        });

        // Include XML comments
        var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
        var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
        c.IncludeXmlComments(xmlPath);
    });
}
```

- **Giải thích:**
    - `SwaggerDoc()`: Cấu hình thông tin cho API documentation trong Swagger.
    - `Contact`, `License`: Cấu hình thông tin liên hệ và giấy phép.
    - `IncludeXmlComments()`: Bao gồm các XML comments vào API documentation.

#### 14.2. Client Code Generation

- **Sử dụng NSwag để generate TypeScript client:**

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddOpenApiDocument(config =>
    {
        config.PostProcess = document =>
        {
            document.Info.Version = "v1";
            document.Info.Title = "My API";
            document.Info.Description = "ASP.NET Core Web API";
        };

        config.GenerateEnumMappingDescription = true;
        config.GenerateExamples = true;
    });
}
```

- **Giải thích:**
    - `AddOpenApiDocument()`: Cấu hình NSwag middleware để generate API documentation và client code.
    - `PostProcess()`: Cấu hình thông tin cho API documentation.
    - `GenerateEnumMappingDescription`, `GenerateExamples`: Cấu hình thêm các tùy chọn cho client code generation.

### 15. Performance Tips

#### 15.1. Async/Await Best Practices

```csharp
// Good Practice
public async Task<IActionResult> GetProducts()
{
    var products = await _context.Products
        .AsNoTracking() // Improve performance for read-only
        .ToListAsync();
    return Ok(products);
}

// Avoid Blocking Calls
public async Task<IActionResult> BadExample()
{
    // Bad: Blocking call
    var result = Task.Run(async () => await _service.GetDataAsync()).Result;

    // Good: Async all the way
    var result = await _service.GetDataAsync();
    return Ok(result);
}
```

- **Giải thích:**
    - **Good Practice:** Sử dụng `async` và `await` một cách hợp lý trong các hàm để tránh blocking thread.
    - **Avoid Blocking Calls:** Tránh sử dụng `Task.Run()` và `Result` để tránh blocking thread.

#### 15.2. Caching Strategies

```csharp
public class ProductsController : ControllerBase
{
    private readonly IMemoryCache _cache;
    private readonly IProductService _productService;

    [HttpGet("{id}")]
    public async Task<ActionResult<Product>> GetProduct(int id)
    {
        var cacheKey = $"product-{id}";

        if (!_cache.TryGetValue(cacheKey, out Product product))
        {
            product = await _productService.GetByIdAsync(id);

            var cacheEntryOptions = new MemoryCacheEntryOptions()
                .SetSlidingExpiration(TimeSpan.FromMinutes(5))
                .SetAbsoluteExpiration(TimeSpan.FromHours(1));

            _cache.Set(cacheKey, product, cacheEntryOptions);
        }

        return Ok(product);
    }
}
```

- **Giải thích:**
    - `IMemoryCache`: Interface đại diện cho in-memory cache.
    - `_cache`: Biến private để truy cập vào cache.
    - **Hoạt động:**
        - Kiểm tra xem dữ liệu đã có trong cache hay chưa.
        - Nếu chưa, lấy dữ liệu từ service và lưu vào cache.
        - Nếu đã có, lấy dữ liệu từ cache.

### 16. Deployment và CI/CD

#### 16.1. Docker Support

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["MyApi.csproj", "./"]
RUN dotnet restore "MyApi.csproj"
COPY . .
RUN dotnet build "MyApi.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MyApi.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MyApi.dll"]
```

- **Giải thích:**
    - Dockerfile: Định nghĩa cách tạo image Docker cho API.
    - `FROM mcr.microsoft.com/dotnet/aspnet:7.0`: Sử dụng image ASP.NET Core 7.0 làm base image.
    - `WORKDIR /app`: Thiết lập thư mục làm việc.
    - `EXPOSE 80`, `EXPOSE 443`: Mở các port 80 và 443 cho API.
    - `COPY`, `RUN`: Các lệnh để build và publish API trong Docker.
    - **Hoạt động:**
        - Dockerfile được sử dụng để tạo image Docker cho API.
        - Image Docker có thể được deploy vào các nền tảng cloud như Azure, AWS, Google Cloud hoặc các server tự quản
          lý.

#### 16.2. Azure DevOps Pipeline

```yaml
trigger:
  - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'

steps:
  - task: DotNetCoreCLI@2
    inputs:
      command: 'restore'
      projects: '\*_/_.csproj'

  - task: DotNetCoreCLI@2
    inputs:
      command: 'build'
      projects: '\*_/_.csproj'
      arguments: '--configuration $(buildConfiguration)'

  - task: DotNetCoreCLI@2
    inputs:
      command: 'test'
      projects: '\**/*Tests/\*.csproj'
      arguments: '--configuration $(buildConfiguration)'

  - task: DotNetCoreCLI@2
    inputs:
      command: 'publish'
      publishWebProjects: true
      arguments: '--configuration $(BuildConfiguration) --output $(Build.ArtifactStagingDirectory)'

  - task: PublishBuildArtifacts@1
    inputs:
      pathtoPublish: '$(Build.ArtifactStagingDirectory)'
      artifactName: 'webapp'
```

- **Giải thích:**
    - Azure DevOps Pipeline: Định nghĩa các bước để build, test và deploy API vào Azure.
    - `trigger: - main`: Pipeline được trigger khi có commit mới vào branch `main`.
    - `pool: vmImage: 'ubuntu-latest'`: Sử dụng virtual machine Ubuntu làm agent để chạy pipeline.
    - `variables: buildConfiguration: 'Release'`: Khai báo biến `buildConfiguration` để sử dụng trong các bước của
      pipeline.
    - **Hoạt động:**
        - Pipeline sẽ chạy các bước build, test, publish và deploy API vào Azure khi có commit mới vào branch `main`.
        - Pipeline có thể được tùy chỉnh để phù hợp với quy trình CI/CD của từng dự án.

### 17. Mở rộng và Maintenance

#### 17.1. Modular Architecture

```csharp
public class Startup
{
    public void ConfigureServices(IServiceCollection services)
    {
        // Register modules
        services.AddModule<AuthenticationModule>();
        services.AddModule<LoggingModule>();
        services.AddModule<SwaggerModule>();
    }
}

public interface IModule
{
    void RegisterServices(IServiceCollection services);
    void Configure(IApplicationBuilder app);
}

public class AuthenticationModule : IModule
{
    public void RegisterServices(IServiceCollection services)
    {
        // Register authentication services
    }

    public void Configure(IApplicationBuilder app)
    {
        // Configure authentication middleware
    }
}
```

- **Giải thích:**
    - `IModule`: Interface định nghĩa các phương thức cần thiết cho một module.
    - `RegisterServices()`: Phương thức để đăng ký các service của module.
    - `Configure()`: Phương thức để cấu hình middleware của module.
    - **Hoạt động:**
        - Sử dụng module để chia nhỏ code thành các phần độc lập, dễ quản lý và bảo trì.
        - Mỗi module có thể xử lý một chức năng cụ thể như authentication, logging, hoặc API documentation.

#### 17.2. Feature Flags

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddFeatureManagement()
        .AddFeatureFilter<PercentageFilter>();
}

[HttpGet]
public async Task<IActionResult> GetProducts(
    [FromServices] IFeatureManager featureManager)
{
    if (await featureManager.IsEnabledAsync("BetaFeatures"))
    {
        // Return new version
        return Ok(await _productService.GetProductsV2Async());
    }

    // Return old version
    return Ok(await _productService.GetProductsAsync());
}
```

- **Giải thích:**
    - `AddFeatureManagement()`: Cấu hình Feature Management middleware.
    - `AddFeatureFilter<PercentageFilter>()`: Cấu hình filter để điều khiển việc bật/tắt feature dựa trên tỷ lệ phần
      trăm.
    - `IsEnabledAsync("BetaFeatures")`: Kiểm tra xem feature "BetaFeatures" có được bật hay không.
    - **Hoạt động:**
        - Sử dụng feature flags để bật/tắt các tính năng mới hoặc experimental features trong API.
        - Việc bật/tắt feature có thể được thực hiện thông qua một dashboard hoặc API.

### 18. Hướng dẫn sử dụng

**Bước 1:** Tạo một dự án ASP.NET Core Web API mới.

**Bước 2:** Thêm các package cần thiết:

```bash
dotnet add package Microsoft.AspNetCore.Mvc.NewtonsoftJson
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer
dotnet add package Microsoft.AspNetCore.Authorization
dotnet add package Swashbuckle.AspNetCore
dotnet add package NSwag.AspNetCore
dotnet add package Microsoft.Extensions.Caching.Memory
```

**Bước 3:** Cấu hình các service trong Startup.cs:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddDbContext<ApplicationDbContext>(options =>
        options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));

    services.AddControllers()
        .AddNewtonsoftJson();

    services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
        .AddJwtBearer(options =>
        {
            // Cấu hình JWT ở đây
        });

    services.AddAuthorization(options =>
    {
        // Cấu hình Authorization Policy ở đây
    });

    services.AddSwaggerGen(c =>
    {
        // Cấu hình Swagger ở đây
    });

    // Cấu hình các service khác
}
```

**Bước 4:** Tạo Controllers và Actions:

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    private readonly IProductService _productService;

    public ProductsController(IProductService productService)
    {
        _productService = productService;
    }

    // Các Actions cho API
}
```

**Bước 5:** Cấu hình Middleware trong Startup.cs:

```csharp
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }

    app.UseHttpsRedirection();

    app.UseRouting();

    app.UseAuthentication();
    app.UseAuthorization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapControllers();
    });

    // Cấu hình Swagger
    app.UseSwagger();
    app.UseSwaggerUI(c =>
    {
        c.SwaggerEndpoint("/swagger/v1/swagger.json", "My API V1");
    });
}
```

**Bước 6:** Chạy ứng dụng:

```bash
dotnet run
```

**Lưu ý:** Hướng dẫn này chỉ là một bản tóm tắt cơ bản. Để triển khai một API Web ASP.NET Core hoàn chỉnh, bạn sẽ cần
tìm hiểu thêm về các khía cạnh nâng cao như bảo mật, quản lý lỗi, caching, testing, deployment và các kiến thức liên
quan.

### 19. Kết luận

ASP.NET Core Web API là một framework mạnh mẽ và linh hoạt cho phép bạn phát triển các API web hiệu quả và an toàn.
Hướng dẫn này cung cấp cho bạn kiến thức cơ bản để bắt đầu với ASP.NET Core Web API và xây dựng các ứng dụng API web của
riêng bạn.
