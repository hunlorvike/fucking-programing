# Chương 9: "Thực Hành" Xây Dựng Ứng Dụng ABP Framework - " 'Vào Bếp' " "Nấu" Ứng Dụng "Thực Tế"

Chào mừng bạn đến với **Chương 9: "Thực Hành" Xây Dựng Ứng Dụng ABP Framework**! Trong chương này, chúng ta sẽ **"thực
hành"** "xây dựng" các ứng dụng ABP Framework **"thực tế"** để "củng cố" các "kiến thức" đã học và "rèn luyện" "kỹ
năng" "lập trình" với ABP Framework. Chúng ta sẽ "bắt đầu" với một ứng dụng **CRUD** (Create, Read, Update, Delete) "
đơn giản", sau đó "mở rộng" ứng dụng để "thêm" các "tính năng" "phức tạp" hơn (ví dụ: quản lý người dùng, phân quyền, đa
ngôn ngữ, multi-tenancy, v.v.). "Thực hành" là "cách tốt nhất" để "nắm vững" ABP Framework và "biến" "lý thuyết" thành "
kỹ năng" "thực tế".

**Phần 9: "Thực Hành" Xây Dựng Ứng Dụng ABP Framework - " 'Vào Bếp' " "Nấu" Ứng Dụng "Thực Tế"**

**9.1. Xây Dựng Ứng Dụng CRUD (Create, Read, Update, Delete) Đơn Giản - " 'Bài Tập' " "Vỡ Lòng" Với ABP Framework**

- **"Mục Tiêu" Của Ứng Dụng CRUD "Đơn Giản":**

    -   "Xây dựng" một ứng dụng web **"đơn giản"** cho phép người dùng thực hiện các thao tác **CRUD** (Create, Read,
        Update, Delete) trên một **"thực thể"** (entity) duy nhất (ví dụ: **`Product`** - Sản phẩm).
    -   "Áp dụng" các **"khái niệm" "cơ bản"** của ABP Framework đã học (Modules, Application Services, DTOs,
        Repositories, Entities, v.v.) để "xây dựng" ứng dụng.
    -   "Làm quen" với **"quy trình" "phát triển"** ứng dụng ABP Framework "từ đầu đến cuối".

- **"Các Bước" "Xây Dựng" Ứng Dụng CRUD "Đơn Giản" Với ABP Framework:**

    1.  **"Tạo" Dự Án ABP Framework Mới:**
        *   Sử dụng **ABP CLI** để "tạo" dự án mới với template **`app`** và UI framework là **`mvc`** (hoặc `blazor`
            nếu bạn thích).
            ```bash
            abp new MyCrudApp -t app --ui mvc # Hoặc --ui blazor
            ```
        *   Chọn database provider (ví dụ: EF Core).

    2.  **"Tạo" Entity `Product` (Thực Thể Sản Phẩm):**
        *   "Tạo" một lớp (class) `Product` trong thư mục `Entities` của dự án `.Domain`.
        *   "Kế thừa" từ lớp `AggregateRoot<Guid>` (hoặc `Entity<Guid>`).
        *   "Định nghĩa" các "thuộc tính" (properties) của `Product` (ví dụ: `Name`, `Price`, `Description`,
            `CategoryId` (nếu có quan hệ với Category), v.v.).
        * "Ví dụ":

          ```csharp
          // Domain/Products/Product.cs (Entity)
          using System;
          using Volo.Abp.Domain.Entities.Auditing;

          namespace MyCrudApp.Products
          {
              public class Product : AuditedAggregateRoot<Guid> // Kế thừa từ AuditedAggregateRoot (thêm các thuộc tính auditing như CreationTime, CreatorId, v.v.)
              {
                  public string Name { get; set; }
                  public decimal Price { get; set; }
                  public string Description {get; set;}
              }
          }
          ```

    3.  **"Tạo" DTOs cho `Product`:**
        *   "Tạo" các DTOs (Data Transfer Objects) để "truyền" dữ liệu giữa Presentation Layer và Application Layer.
            *   `ProductDto`: DTO để "hiển thị" thông tin sản phẩm.
            *   `CreateUpdateProductDto`: DTO để "tạo" và "cập nhật" sản phẩm.
        *   "Đặt" các DTOs trong thư mục `Products` của dự án `.Application.Contracts`.
        *   "Ví dụ":

            ```csharp
            // Application.Contracts/Products/ProductDto.cs (Output DTO)

            using System;
            using Volo.Abp.Application.Dtos;

            namespace MyCrudApp.Products
            {
                public class ProductDto : AuditedEntityDto<Guid>
                {
                    public string Name { get; set; }
                    public decimal Price { get; set; }
                    public string Description {get; set;}
                }
            }
            ```

            ```csharp
            // Application.Contracts/Products/CreateUpdateProductDto.cs (Input DTO)

            using System.ComponentModel.DataAnnotations;

            namespace MyCrudApp.Products
            {
                public class CreateUpdateProductDto
                {
                    [Required]
                    [StringLength(128)]
                    public string Name { get; set; }

                    [Required]
                    [Range(0, 1000000)]
                    public decimal Price { get; set; }
                    public string Description {get; set;}
                }
            }
            ```

    4.  **"Tạo" Application Service `ProductAppService`:**
        *   "Tạo" interface `IProductAppService` trong dự án `.Application.Contracts`.
        *   "Tạo" lớp `ProductAppService` trong dự án `.Application`, "kế thừa" từ `CrudAppService` và "triển khai"
            `IProductAppService`.
        * "Ví dụ":

          ```csharp
          // Application.Contracts/Products/IProductAppService.cs (Application Service Interface)
          using System;
          using System.Threading.Tasks;
          using Volo.Abp.Application.Dtos;
          using Volo.Abp.Application.Services;

          namespace MyCrudApp.Products
          {
              public interface IProductAppService :
                  ICrudAppService< // Kế thừa từ ICrudAppService (cung cấp các phương thức CRUD)
                      ProductDto, // DTO
                      Guid, // Primary Key Type
                      PagedAndSortedResultRequestDto, // Input DTO cho phân trang và sắp xếp
                      CreateUpdateProductDto> // Input DTO cho tạo và cập nhật
              {
              }
          }
          ```

          ```csharp
          // Application/Products/ProductAppService.cs (Application Service Implementation)

          using System;
          using System.Threading.Tasks;
          using Volo.Abp.Application.Dtos;
          using Volo.Abp.Application.Services;
          using Volo.Abp.Domain.Repositories;

          namespace MyCrudApp.Products
          {
              public class ProductAppService :
                  CrudAppService< // Kế thừa từ CrudAppService
                      Product, // Entity
                      ProductDto, // DTO
                      Guid, // Primary Key Type
                      PagedAndSortedResultRequestDto, // Input DTO cho phân trang và sắp xếp
                      CreateUpdateProductDto>, // Input DTO cho tạo và cập nhật
                  IProductAppService // Triển khai IProductAppService
              {
                  public ProductAppService(IRepository<Product, Guid> repository)
                      : base(repository)
                  {
                  }
              }
          }
          ```

    5.  **"Tạo" Controller (nếu dùng Web API) hoặc Razor Page/Blazor Component (nếu dùng MVC/Blazor):**
        *   **Web API:** "Tạo" `ProductsController` trong dự án `.Web` (hoặc `.HttpApi`), "kế thừa" từ `
            AbpApiController`.
        *   **MVC/Razor Pages:** "Tạo" `Index.cshtml` và `Index.cshtml.cs` trong thư mục `Pages/Products`.
        *   **Blazor:** "Tạo" `ProductList.razor` trong thư mục `Pages`.
        *   **"Inject"** (tiêm) `IProductAppService` vào controller/page/component thông qua constructor.
        *   **"Gọi"** các phương thức của `IProductAppService` để "thực hiện" các thao tác CRUD.
        * **Ví dụ (Web API Controller):**
            ```csharp
            using Microsoft.AspNetCore.Mvc;
            using MyCrudApp.Products;
            using System;
            using System.Threading.Tasks;
            using Volo.Abp;
            using Volo.Abp.AspNetCore.Mvc;

            namespace MyCrudApp.Controllers
            {
                [Route("api/products")]
                public class ProductsController : AbpController
                {
                    private readonly IProductAppService _productAppService;

                    public ProductsController(IProductAppService productAppService)
                    {
                        _productAppService = productAppService;
                    }

                    [HttpGet]
                    public async Task<IActionResult> GetListAsync()
                    {
                        var products = await _productAppService.GetListAsync(new PagedAndSortedResultRequestDto());
                        return Ok(products);
                    }

                    [HttpGet("{id}")]
                    public async Task<IActionResult> GetAsync(Guid id)
                    {
                        try
                        {
                            var product = await _productAppService.GetAsync(id);
                            return Ok(product);
                        }
                        catch (EntityNotFoundException)
                        {
                            return NotFound();
                        }
                    }

                    [HttpPost]
                    public async Task<IActionResult> CreateAsync([FromBody] CreateUpdateProductDto input)
                    {
                        var product = await _productAppService.CreateAsync(input);
                        return CreatedAtAction(nameof(GetAsync), new { id = product.Id }, product);
                    }

                    [HttpPut("{id}")]
                    public async Task<IActionResult> UpdateAsync(Guid id, [FromBody] CreateUpdateProductDto input)
                    {
                        try
                        {
                            var product = await _productAppService.UpdateAsync(id, input);
                            return Ok(product);
                        }
                        catch (EntityNotFoundException)
                        {
                            return NotFound();
                        }
                    }

                    [HttpDelete("{id}")]
                    public async Task<IActionResult> DeleteAsync(Guid id)
                    {
                        try
                        {
                            await _productAppService.DeleteAsync(id);
                            return NoContent();
                        }
                        catch (EntityNotFoundException)
                        {
                            return NotFound();
                        }
                    }
                }
            }

            ```

    6.  **"Cấu Hình" Database:**
        *   "Cấu hình" connection string trong file `appsettings.json` của dự án `.Web` (hoặc `.HttpApi.Host`).
        *   "Chạy" database migrations để "tạo" bảng `Products` trong database. (xem lại chương 2 và 7)

    7.  **"Chạy" và "Kiểm Thử" Ứng Dụng:**
        *   "Chạy" ứng dụng (nhấn F5 trong Visual Studio hoặc dùng lệnh `dotnet run` trong Terminal).
        *   "Sử dụng" **Postman** (hoặc công cụ tương tự) để "gửi" các HTTP requests (GET, POST, PUT, DELETE) đến các
            API endpoints của `ProductsController` để "kiểm thử" các tính năng CRUD.
        *   "Sử dụng" trình duyệt web để "truy cập" giao diện Razor Pages/Blazor Components (nếu có) và "kiểm thử" các
            tính năng CRUD.

**9.2. Xây Dựng Ứng Dụng Quản Lý Người Dùng - " 'Mở Rộng' " Ứng Dụng CRUD Với "Tính Năng" "Xác Thực" và "Phân
Quyền"**
    * Sử dụng các module có sẵn.
    * Tự custom các tính năng.

**9.3. Xây Dựng Ứng Dụng Multi-tenant**

*   **"Mở Rộng" Ứng Dụng CRUD Để "Hỗ Trợ" Multi-tenancy:** "Thêm" tính năng **multi-tenancy** (đa người thuê) vào
    ứng dụng CRUD "đơn giản" để "phục vụ" "nhiều khách hàng" (tenants) trên "cùng một" codebase và "cùng một"
    database.

**Tổng Kết Chương 9:**

-   Bạn đã **"thực hành" "xây dựng"** các ứng dụng ABP Framework **"thực tế"**, "áp dụng" các "kiến thức" đã học từ các
    chương trước.
    -   "Xây dựng" ứng dụng **CRUD "đơn giản"** (Create, Read, Update, Delete) cho một "thực thể" (entity) duy nhất (ví
        dụ: `Product`).
    -   "Mở rộng" ứng dụng CRUD để "thêm" các "tính năng" "phức tạp" hơn (ví dụ: quản lý người dùng, multi-tenancy).
    -   "Áp dụng" các **"khái niệm" "cốt lõi"** của ABP Framework (Modules, Application Services, DTOs, Repositories,
        Entities, v.v.) vào "thực tế".
    -   "Làm quen" với **"quy trình" "phát triển"** ứng dụng ABP Framework "từ đầu đến cuối".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 10: "Triển Khai" Ứng Dụng ABP Framework**. Chúng ta sẽ "học cách" "triển khai" ứng
dụng ABP Framework lên các "môi trường" khác nhau (ví dụ: máy chủ IIS, Docker containers, cloud platforms).

Bạn có câu hỏi nào về "thực hành" xây dựng ứng dụng ABP Framework này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn
sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" ABP Framework.
