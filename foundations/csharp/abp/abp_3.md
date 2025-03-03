# Chương 3: Kiến Trúc Ứng Dụng ABP Framework - " 'Bộ Khung' " "Vững Chắc" Cho Ứng Dụng - " 'Sơ Đồ' " "Tổ Chức" Code

Chào mừng bạn đến với **Chương 3: Kiến Trúc Ứng Dụng ABP Framework**! Trong chương này, chúng ta sẽ "khám phá" **kiến
trúc** (architecture) của ứng dụng ABP Framework, "tìm hiểu" **"các tầng"** (layers) trong kiến trúc, **"vai trò"**
của từng tầng, và **"cách" các tầng "tương tác"** với nhau. "Nắm vững" kiến trúc ứng dụng ABP Framework là "nền tảng"
quan trọng để bạn "xây dựng" các ứng dụng **"chất lượng cao"**, **"dễ bảo trì"**, và **"dễ mở rộng"**.

**Phần 3: Kiến Trúc Ứng Dụng ABP Framework - " 'Bộ Khung' " "Vững Chắc" Cho Ứng Dụng**

- **Kiến Trúc "Đa Tầng" (Layered Architecture) - " 'Kim Chỉ Nam' " Cho "Tổ Chức" Code:**

    - ABP Framework "áp dụng" kiến trúc **"đa tầng"** (layered architecture) (còn gọi là kiến trúc **"n-tier"**). Kiến
      trúc "đa tầng" **"chia" ứng dụng** thành các **"tầng" (layers) "độc lập"**, mỗi tầng có **"trách nhiệm" "riêng"**
      và **"giao tiếp"** với các tầng "khác" theo các **"quy tắc" "rõ ràng"**.
    - Kiến trúc "đa tầng" "mang lại" nhiều "lợi ích":
        *   **"Tổ chức" code "gọn gàng" và "dễ hiểu":** "Phân chia" code thành các tầng "riêng biệt" giúp "giảm thiểu" "
            độ phức tạp" của ứng dụng và "làm cho" code "dễ đọc", "dễ hiểu", và "dễ quản lý" hơn.
        *   **"Tăng" "tính 'tái sử dụng' " code:** Các tầng "có thể" được "tái sử dụng" trong các "phần khác" của ứng
            dụng hoặc trong các ứng dụng "khác".
        *   **"Dễ dàng" "bảo trì" và "nâng cấp":** "Thay đổi" code trong một tầng **"không ảnh hưởng"** (hoặc "ít ảnh
            hưởng") đến các tầng "khác" (nếu "tuân thủ" các "nguyên tắc" "thiết kế" tốt). "Dễ dàng" "thêm" tính năng
            "mới", "sửa lỗi", hoặc "nâng cấp" ứng dụng.
        *   **"Dễ dàng" "kiểm thử" (testable):** Các tầng "độc lập" "có thể" được **"kiểm thử" "riêng lẻ"** (unit
            testing).
        *   **"Tăng cường" "bảo mật":** "Phân chia" ứng dụng thành các tầng "giúp" "kiểm soát" "luồng dữ liệu" và "
            quyền truy cập" giữa các tầng, "tăng cường" "bảo mật" ứng dụng.
        *   **"Hỗ trợ" "nhiều mô hình" "triển khai":** Các tầng "có thể" được "triển khai" trên các **"máy chủ" "khác
            nhau"** (ví dụ: web server, application server, database server) để "tăng" "hiệu suất" và "khả năng mở
            rộng".

- **"Các Tầng" (Layers) "Chính" Trong Kiến Trúc Ứng Dụng ABP Framework:**

    - ABP Framework "áp dụng" kiến trúc "đa tầng" với các tầng "chính" sau:

        1.  **Presentation Layer (Tầng Trình Bày):** "Giao diện" với người dùng hoặc các ứng dụng khác.
        2.  **Application Layer (Tầng Ứng Dụng):** "Triển khai" các "use cases" (trường hợp sử dụng) của ứng dụng.
        3.  **Domain Layer (Tầng Nghiệp Vụ):** "Trái tim" của ứng dụng, chứa "logic nghiệp vụ" (business logic).
        4.  **Infrastructure Layer (Tầng Cơ Sở Hạ Tầng):** "Cung cấp" các "triển khai" "cụ thể" cho các "giao diện"
            (interfaces) được "định nghĩa" ở các tầng "trên" (ví dụ: kết nối database, gửi email, gọi API bên ngoài).

    - **"Mối Quan Hệ" Giữa Các Tầng:**

        *   **Presentation Layer** "phụ thuộc" vào **Application Layer**.
        *   **Application Layer** "phụ thuộc" vào **Domain Layer** và **Infrastructure Layer**.
        *   **Domain Layer** "không phụ thuộc" vào bất kỳ tầng nào khác ("độc lập").
        *   **Infrastructure Layer** "phụ thuộc" vào **Domain Layer**.

    - **"Sơ Đồ" Kiến Trúc "Đa Tầng" (Layered Architecture) Của ABP Framework:** (Hình ảnh minh họa)

      ```
      +---------------------+     +---------------------+     +---------------------+     +---------------------+
      | Presentation Layer  |---->| Application Layer   |---->|    Domain Layer     |     | Infrastructure Layer|
      | (Web API, MVC,      |     | (Application        |     | (Entities, Value    |<----| (EF Core, MongoDB,  |
      |  Blazor, etc.)      |     |  Services, DTOs)    |     |  Objects, Domain    |     |  Repositories,      |
      |                     |     |                     |     |  Services,          |     |  External Services) |
      |                     |     |                     |     |  Repositories  (I)) |     |                     |
      +---------------------+     +---------------------+     +---------------------+     +---------------------+
             ^                                                                                      |
             |                                                                                      |
             +---------------------------------------<----------------------------------------------+
                                    Data Flow (Luồng Dữ Liệu)
      ```

**3.1. Presentation Layer (Tầng Trình Bày) - " 'Giao Tiếp' " Với "Thế Giới Bên Ngoài" - " 'Mặt Tiền' " Của Ứng Dụng**

- **Presentation Layer - " 'Cánh Cửa' " Để "Tương Tác" Với Ứng Dụng:**

    - **Presentation Layer** (Tầng Trình Bày) là **"tầng 'ngoài cùng' "** của ứng dụng, "chịu trách nhiệm" **"giao
      tiếp"** với **"người dùng"** (users) hoặc **"các ứng dụng khác"** (other applications).
    - Presentation Layer "cung cấp" **"giao diện"** (interface) để người dùng (hoặc ứng dụng khác) **"tương tác"** với
      ứng dụng, "gửi" "yêu cầu" (requests) đến ứng dụng và "nhận" "phản hồi" (responses) từ ứng dụng.

- **"Các Thành Phần" "Chính" Trong Presentation Layer:**

    - **Web API Controllers (ASP.NET Core Web API):**
        *   **"Phổ biến nhất"** trong các ứng dụng ABP Framework.
        *   **"Xử lý"** các **HTTP requests** (GET, POST, PUT, DELETE) từ client (ví dụ: trình duyệt web, ứng dụng
            mobile, ứng dụng desktop).
        *   **"Gọi"** các **Application Services** (trong Application Layer) để "thực hiện" các "tác vụ" và "trả về"
            dữ liệu cho client dưới dạng **JSON** hoặc **XML**.
        *   **"Sử dụng" Data Transfer Objects (DTOs)** để "nhận" dữ liệu từ client và "trả về" dữ liệu cho client.
        *   **"Định tuyến" (routing):** "Định nghĩa" các **"URL endpoints"** (ví dụ: `/api/products`, `/api/orders`) để
            client có thể "gọi" đến.
        *   **"Xác thực" (authentication) và "phân quyền" (authorization):** "Kiểm tra" "danh tính" của người dùng (
            authentication) và "xác minh" xem người dùng có "quyền" truy cập vào API endpoint hay không (authorization)
            .
        *   **"Ví dụ":**

            ```csharp
            // Controllers/ProductsController.cs (ASP.NET Core Web API)

            using Microsoft.AspNetCore.Mvc;
            using MyProject.Products;
            using System.Threading.Tasks;

            namespace MyProject.Controllers
            {
                [Route("api/[controller]")] // Định tuyến (routing) - URL endpoint: /api/products
                [ApiController]
                public class ProductsController : ControllerBase // Kế thừa từ ControllerBase
                {
                    private readonly IProductAppService _productAppService; // Inject IProductAppService

                    public ProductsController(IProductAppService productAppService) // Constructor injection
                    {
                        _productAppService = productAppService;
                    }

                    [HttpGet] // HTTP GET method
                    public async Task<List<ProductDto>> GetListAsync() // Lấy danh sách sản phẩm
                    {
                        return await _productAppService.GetListAsync(); // Gọi Application Service
                    }

                    [HttpGet("{id}")] // HTTP GET method với parameter "id"
                    public async Task<ProductDto> GetAsync(Guid id) // Lấy sản phẩm theo ID
                    {
                        return await _productAppService.GetAsync(id); // Gọi Application Service
                    }

                    [HttpPost] // HTTP POST method
                    public async Task<ProductDto> CreateAsync(CreateProductDto input) // Tạo sản phẩm mới
                    {
                        return await _productAppService.CreateAsync(input); // Gọi Application Service
                    }

                    // ... (Các actions khác: Update, Delete)
                }
            }
            ```

    - **Razor Pages (ASP.NET Core MVC/Razor Pages):**
        *   "Dùng" để "xây dựng" các ứng dụng web **"server-side rendering"** (render HTML trên server và gửi HTML đến
            trình duyệt).
        *   **"Kết hợp"** code C# (server-side code) và HTML (client-side code) trong cùng một file (`.cshtml`).
        *   **"Model-View-ViewModel (MVVM)" pattern:** Razor Pages "thường" sử dụng mô hình MVVM.
            *   **Model:** Đại diện cho dữ liệu.
            *   **View:** Đại diện cho giao diện người dùng (HTML).
            *   **ViewModel:** Lớp trung gian giữa Model và View, chứa dữ liệu và logic để "xử lý" tương tác của người
                dùng.
        *   **"Ví dụ":**

            ```csharp
            // Pages/Products/Index.cshtml.cs (Razor Page)

            using Microsoft.AspNetCore.Mvc.RazorPages;
            using MyProject.Products;
            using System.Collections.Generic;
            using System.Threading.Tasks;

            namespace MyProject.Pages.Products
            {
                public class IndexModel : PageModel // Kế thừa từ PageModel
                {
                    private readonly IProductAppService _productAppService; // Inject IProductAppService

                    public IndexModel(IProductAppService productAppService)
                    {
                        _productAppService = productAppService;
                    }

                    public List<ProductDto> Products { get; set; } // ViewModel - chứa danh sách sản phẩm

                    public async Task OnGetAsync() // Xử lý HTTP GET request
                    {
                        Products = await _productAppService.GetListAsync(); // Gọi Application Service để lấy danh sách sản phẩm
                    }
                }
            }
            ```

            ```html
            @* Pages/Products/Index.cshtml (Razor Page View) *@
            @page
            @model MyProject.Pages.Products.IndexModel

            <h1>Products</h1>

            <ul>
                @foreach (var product in Model.Products)
                {
                    <li>@product.Name - @product.Price</li>
                }
            </ul>
            ```

    - **Blazor Components (Blazor Server/Blazor WebAssembly):**
        *   "Dùng" để "xây dựng" các ứng dụng web **"client-side rendering"** (Blazor WebAssembly) hoặc **"
            server-side rendering"** (Blazor Server) bằng **C#** thay vì JavaScript.
        *   **"Component-based" architecture:** Blazor "sử dụng" mô hình "component-based" để "xây dựng" giao diện
            người dùng. Mỗi "component" là một "khối" UI "có thể 'tái sử dụng' ".
        *   **"Ví dụ":**

            ```csharp
            // Components/ProductList.razor (Blazor Component)

            @using MyProject.Products
            @inject IProductAppService ProductAppService

            <h3>Products</h3>

            @if (products == null)
            {
                <p><em>Loading...</em></p>
            }
            else
            {
                <ul>
                    @foreach (var product in products)
                    {
                        <li>@product.Name - @product.Price</li>
                    }
                </ul>
            }

            @code {
                private List<ProductDto> products;

                protected override async Task OnInitializedAsync()
                {
                    products = await ProductAppService.GetListAsync();
                }
            }
            ```

    - **GraphQL APIs:**
        * Ngoài ra, Presentation Layer có thể triển khai theo dạng GraphQL API

    - **gRPC Services:**
        * Presentation Layer cũng có thể là các gRPC Service

- **"Đặc Điểm" Của Presentation Layer:**

    *   **"Phụ thuộc" vào Application Layer:** Presentation Layer **"gọi"** các Application Services (trong
        Application Layer) để "thực hiện" các "tác vụ" và "lấy" dữ liệu.
    *   **"Không chứa" "logic nghiệp vụ" (business logic):** Presentation Layer **"chỉ"** "chịu trách nhiệm" về "hiển
        thị" dữ liệu và "tương tác" với người dùng (hoặc ứng dụng khác), **"không chứa" "logic nghiệp vụ" "phức tạp"**.
        Logic nghiệp vụ "phức tạp" phải được "đặt" trong Domain Layer.
    *   **"Có thể thay đổi" "linh hoạt":** Bạn có thể "thay đổi" Presentation Layer (ví dụ: "thay đổi" UI framework, "
        chuyển" từ Web API sang Razor Pages) mà **"không ảnh hưởng"** đến các tầng "khác" của ứng dụng (nếu "tuân thủ"
        các "nguyên tắc" "thiết kế" tốt).

**3.2. Application Layer (Tầng Ứng Dụng) - " 'Triển Khai' " Các "Use Cases" - " 'Cầu Nối' " Giữa " 'Presentation' " và
" 'Domain' "**

- **Application Layer - " 'Điều Phối' " Các "Tác Vụ" Ứng Dụng:**

    - **Application Layer** (Tầng Ứng Dụng) là "tầng" **"trung gian"** giữa **Presentation Layer** (tầng trình bày) và
      **Domain Layer** (tầng nghiệp vụ).
    - Application Layer "chịu trách nhiệm" **"triển khai"** các **"use cases"** (trường hợp sử dụng) của ứng dụng. Use
      cases là các **"tác vụ"** (tasks) hoặc **"hành động"** (actions) mà người dùng (hoặc ứng dụng khác) có thể "thực
      hiện" trên ứng dụng (ví dụ: "tạo sản phẩm mới", "xem danh sách sản phẩm", "cập nhật thông tin sản phẩm", "xóa sản
      phẩm", "đặt hàng", "thanh toán", v.v.).
    - Application Layer **"không chứa" "logic nghiệp vụ" "phức tạp"**. Logic nghiệp vụ "phức tạp" phải được "đặt" trong
      **Domain Layer**. Application Layer "chủ yếu" "điều phối" các hoạt động, "gọi" các Domain Services (trong Domain
      Layer) và Repositories (trong Infrastructure Layer) để "thực hiện" các "tác vụ" "cụ thể".

- **"Thành Phần" "Chính" Trong Application Layer:**

    - **Application Services (Dịch vụ ứng dụng):**
        *   **"Trái tim"** của Application Layer.
        *   Các "lớp" (classes) "triển khai" các **"use cases"** của ứng dụng.
        *   Mỗi Application Service thường "xử lý" **"một" hoặc "vài" "use cases" "liên quan"**.
        *   Application Services "nhận" "yêu cầu" (requests) từ Presentation Layer (thường thông qua các DTOs), "thực
            hiện" các "tác vụ" (bằng cách "gọi" các Domain Services và Repositories), và "trả về" "kết quả" (thường
            thông qua các DTOs) cho Presentation Layer.
        *   **"Ví dụ":**

            ```csharp
            // Application/Products/ProductAppService.cs (Application Service)

            using System;
            using System.Collections.Generic;
            using System.Threading.Tasks;
            using Volo.Abp.Application.Dtos;
            using Volo.Abp.Application.Services;
            using Volo.Abp.Domain.Repositories;

            namespace MyProject.Products
            {
                public class ProductAppService :
                    CrudAppService< // Kế thừa từ CrudAppService (cung cấp sẵn các phương thức CRUD)
                        Product, // Entity (Thực thể)
                        ProductDto, // DTO (Data Transfer Object)
                        Guid, // Primary Key Type (Kiểu dữ liệu của khóa chính)
                        PagedAndSortedResultRequestDto, // DTO cho phân trang và sắp xếp
                        CreateUpdateProductDto>, // DTO cho tạo và cập nhật sản phẩm
                    IProductAppService // Interface (Giao diện) của Application Service
                {
                    public ProductAppService(IRepository<Product, Guid> repository)
                        : base(repository)
                    {
                    }

                    // Có thể "thêm" các phương thức "tùy chỉnh" cho các use cases "khác" (nếu cần)
                    // Ví dụ:
                    // public async Task<List<ProductDto>> GetListByCategoryIdAsync(Guid categoryId) { ... }
                }
            }
            ```

    - **Data Transfer Objects (DTOs):** (Đã "giới thiệu" ở Chương 1).
        *   **"Đặc điểm" (nhắc lại):**
            *   **"Đơn giản" và "dễ hiểu"**: DTOs "chỉ chứa" các "thuộc tính" dữ liệu cần thiết, "không chứa" các "
                phương thức" "phức tạp".
            *   **"Giảm" "coupling" (sự phụ thuộc) giữa Presentation Layer và Domain Layer:** Presentation Layer "chỉ
                làm việc" với DTOs, "không biết" gì về Entities hoặc các đối tượng khác trong Domain Layer.
            *   **"Tối ưu hóa" "truyền" dữ liệu:** DTOs "chỉ chứa" các "trường" dữ liệu "cần thiết" cho một "use case"
                cụ thể, "tránh" "truyền" các "dữ liệu 'thừa' " qua mạng.
            *   **"Thường" "được 'ánh xạ' " (mapped) từ/đến Entities** bằng các công cụ như **AutoMapper**.

- **"Đặc Điểm" Của Application Layer:**

    *   **"Phụ thuộc" vào Domain Layer và Infrastructure Layer:** Application Layer "gọi" các Domain Services (trong
        Domain Layer) để "thực hiện" các "tác vụ" "nghiệp vụ" "phức tạp" và "gọi" các Repositories (trong
        Infrastructure Layer) để "truy cập" dữ liệu.
    *   **"Không chứa" "logic nghiệp vụ" "phức tạp"**: Logic nghiệp vụ "phức tạp" phải được "đặt" trong Domain Layer.
        Application Layer "chủ yếu" "điều phối" các hoạt động và "xử lý" các "tác vụ" "ở mức cao".
    *   **"Được 'gọi' " từ Presentation Layer:** Presentation Layer "gọi" các Application Services để "thực hiện" các "
        use cases" của ứng dụng.
    *   **"Sử dụng" Dependency Injection (DI):** Application Services "thường" được "đăng ký" trong hệ thống
        Dependency Injection (DI) của ABP Framework và được "tiêm" (injected) vào các "thành phần" khác (ví dụ:
        controllers trong Presentation Layer) thông qua "constructor injection".

**3.3. Domain Layer (Tầng Nghiệp Vụ) - " 'Trái Tim' " Của Ứng Dụng - " 'Nơi' " "Logic Nghiệp Vụ" "Ngự Trị"**

- **Domain Layer - " 'Trung Tâm' " "Xử Lý" "Nghiệp Vụ" - " 'Bộ Não' " Của Ứng Dụng:**

    *   **Domain Layer** (Tầng Nghiệp Vụ) là **"tầng 'quan trọng nhất' "** của ứng dụng, "chứa" **"toàn bộ" "logic
        nghiệp vụ"** (business logic) và **"quy tắc nghiệp vụ"** (business rules) của ứng dụng.
    *   Domain Layer **"không phụ thuộc"** vào bất kỳ tầng nào khác. Domain Layer "tập trung" vào **"miền nghiệp vụ"** (
        business domain) của ứng dụng và "không quan tâm" đến các "vấn đề" "kỹ thuật" (ví dụ: giao diện người dùng, cơ
        sở dữ liệu, giao thức mạng, v.v.).
    *   Domain Layer là **" 'trái tim' " và " 'bộ não' " của ứng dụng**. "Xây dựng" Domain Layer "vững chắc" là "nền
        tảng" để "xây dựng" các ứng dụng **"chất lượng cao"**, **"dễ bảo trì"**, và **"dễ mở rộng"**.

- **"Các Thành Phần" "Chính" Trong Domain Layer:**

    - **Entities (Thực thể):** (Đã "giới thiệu" ở Chương 1).
    - **Value Objects (Đối tượng giá trị):** (Đã "giới thiệu" ở Chương 1).
    - **Domain Services (Dịch vụ nghiệp vụ):** (Đã "giới thiệu" ở Chương 1).
    - **Repositories (Kho chứa) (Interfaces):**
        *   **"Lưu ý" quan trọng:** Trong Domain Layer, bạn **"chỉ 'định nghĩa' " "giao diện" (interfaces) của
            Repositories**, **"không 'triển khai' " (implement)** Repositories trong Domain Layer.
        *   **"Ví dụ":** `IProductRepository` (giao diện repository cho sản phẩm) - "định nghĩa" các "phương thức" để "
            truy cập" dữ liệu sản phẩm (ví dụ: `GetByIdAsync`, `GetAllAsync`, `InsertAsync`, `UpdateAsync`, `
            DeleteAsync`), nhưng **"không 'viết' " code** để "thực hiện" các phương thức này (ví dụ: "không viết" SQL
            queries).
        *   **"Triển khai"** (implementations) của Repositories (ví dụ: `ProductRepository` sử dụng Entity Framework
            Core để "truy cập" database) sẽ được "đặt" trong **Infrastructure Layer** (sẽ "học" ở phần sau).
        *   **"Lý do":** "Tách biệt" **"giao diện"** (interface) của Repository khỏi **"triển khai"** (implementation)
            giúp **"giảm thiểu" "sự phụ thuộc"** của Domain Layer vào các **"công nghệ" "cụ thể"** (ví dụ: database,
            ORM framework). Domain Layer "chỉ cần" "biết" về "giao diện" Repository, "không cần" "biết" về "cách"
            Repository được "triển khai". "Dễ dàng" "thay đổi" "công nghệ" "truy cập" dữ liệu (ví dụ: "chuyển" từ
            Entity Framework Core sang Dapper) mà **"không ảnh hưởng"** đến Domain Layer.
    - **Aggregates (Tập hợp) và Aggregate Roots:**
        *   **Aggregates (Tập hợp):** Là **"nhóm"** các **Entities** và **Value Objects** "liên quan" "chặt chẽ" với nhau
            và được "quản lý" như một **"đơn vị" "duy nhất"**. Aggregates "đảm bảo" **"tính 'nhất quán' " (consistency)
            ** và **"tính 'toàn vẹn' " (integrity)** của dữ liệu trong "miền nghiệp vụ".
        *   **Aggregate Root:** Là một **Entity "đặc biệt"** trong Aggregate, "đóng vai trò" là **"điểm truy cập" "
            duy nhất"** vào Aggregate. "Mọi thao tác" trên Aggregate phải được "thực hiện" thông qua Aggregate Root.
        *   **"Ví dụ":**
            *   **`Order` (Đơn hàng) là một Aggregate Root.** `Order` có thể "chứa" các Entities và Value Objects "con"
                như:
                *   `OrderItem` (Chi tiết đơn hàng) (Entity)
                *   `Address` (Địa chỉ giao hàng) (Value Object)
                *   `PaymentMethod` (Phương thức thanh toán) (Value Object)
            *   Bạn "không thể" "truy cập" trực tiếp vào `OrderItem` từ "bên ngoài" Aggregate `Order`. Bạn phải "truy
                cập" `OrderItem` thông qua `Order` (Aggregate Root). (Ví dụ: `order.AddOrderItem(product, quantity)`)

    - **Domain Events (Sự kiện nghiệp vụ):**
        *   **Domain Events** (Sự kiện nghiệp vụ) là các **"sự kiện" "xảy ra"** trong **Domain Layer**, "biểu thị" **"
            điều gì đó" "quan trọng"** đã "xảy ra" trong "miền nghiệp vụ".
        *   **"Ví dụ":**
            *   `OrderCreatedEvent` (Sự kiện "Đơn hàng đã được tạo").
            *   `ProductStockDecreasedEvent` (Sự kiện "Số lượng sản phẩm trong kho đã giảm").
            *   `UserRegisteredEvent` (Sự kiện "Người dùng đã đăng ký").
        *   **"Mục đích":**
            *   **"Thông báo"** cho các "thành phần" "khác" trong hệ thống về các "sự kiện" "quan trọng" đã "xảy ra"
                trong Domain Layer.
            *   **"Tách biệt"** (decouple) các "thành phần" trong hệ thống. Các "thành phần" "không cần" "biết" về nhau
                một cách "trực tiếp", chúng chỉ cần "lắng nghe" (subscribe) các "sự kiện" mà chúng "quan tâm".
            *   **"Hỗ trợ"** các **"kiến trúc" "hướng sự kiện"** (event-driven architectures).

- **"Đặc Điểm" Của Domain Layer:**

    *   **"Không phụ thuộc"** vào bất kỳ tầng nào khác ("độc lập").
    *   **"Tập trung"** vào **"miền nghiệp vụ"** (business domain) của ứng dụng, "không quan tâm" đến các "vấn đề" "kỹ
        thuật".
    *   **"Chứa" "toàn bộ" "logic nghiệp vụ"** và **"quy tắc nghiệp vụ"** của ứng dụng.
    *   **"Tuân thủ"** các nguyên tắc của **Domain-Driven Design (DDD)**.

**3.4. Infrastructure Layer (Tầng Cơ Sở Hạ Tầng) - " 'Kết Nối' " Với "Thế Giới Bên Ngoài" - " 'Hiện Thực Hóa' " Các "
Giao Tiếp" Kỹ Thuật**

- **Infrastructure Layer - " 'Cây Cầu' " "Kết Nối" Ứng Dụng Với "Hệ Thống" Bên Ngoài:**

    - **Infrastructure Layer** (Tầng Cơ Sở Hạ Tầng) "chịu trách nhiệm" **"giao tiếp"** với các **"hệ thống" "bên
      ngoài"** ứng dụng (ví dụ: database, file system, email server, message queue, external APIs, v.v.) và "cung cấp"
      các **"triển khai" "cụ thể"** cho các **"giao diện"** (interfaces) được "định nghĩa" ở các tầng "trên" (Domain
      Layer, Application Layer).
    *   Infrastructure Layer **"ẩn"** các **"chi tiết" "kỹ thuật"** của việc "giao tiếp" với các "hệ thống" "bên
        ngoài" khỏi các tầng "lõi" của ứng dụng (Domain Layer, Application Layer). "Giúp" code **"sạch sẽ"** hơn, **"dễ
        bảo trì"** hơn, và **"dễ thay đổi"** "công nghệ" "bên dưới" mà **"không ảnh hưởng"** đến các tầng "lõi".

- **"Các Thành Phần" "Chính" Trong Infrastructure Layer:**

    - **Repository Implementations (Triển khai của Repositories):**
        *   **"Thành phần" "quan trọng nhất"** trong Infrastructure Layer.
        *   Các **"lớp"** (classes) **"triển khai"** (implement) các **"giao diện" Repository** (được "định nghĩa" trong
            Domain Layer) bằng cách "sử dụng" các **"công nghệ" "cụ thể"** để **"truy cập" dữ liệu** (ví dụ: Entity
            Framework Core, Dapper, MongoDB driver).
        *   **"Ví dụ":**
            *   `ProductRepository` (triển khai `IProductRepository` sử dụng Entity Framework Core để truy cập database
                SQL Server).
            *   `MongoDbOrderRepository` (triển khai `IOrderRepository` sử dụng MongoDB driver để truy cập database
                MongoDB).

            ```csharp
            // Infrastructure/Data/Repositories/ProductRepository.cs (Repository Implementation)

            using System;
            using System.Collections.Generic;
            using System.Threading.Tasks;
            using Microsoft.EntityFrameworkCore;
            using MyProject.Domain.Products; // Tham chiếu đến Domain Layer (Entities, Repository Interfaces)
            using Volo.Abp.Domain.Repositories.EntityFrameworkCore;
            using Volo.Abp.EntityFrameworkCore;

            namespace MyProject.Infrastructure.Data.Repositories
            {
                public class ProductRepository : EfCoreRepository<MyProjectDbContext, Product, Guid>, IProductRepository // Kế thừa từ EfCoreRepository (cung cấp các phương thức CRUD cơ bản), triển khai IProductRepository
                {
                    public ProductRepository(IDbContextProvider<MyProjectDbContext> dbContextProvider)
                        : base(dbContextProvider)
                    {
                    }

                    // Có thể "ghi đè" (override) các phương thức từ EfCoreRepository hoặc "thêm" các phương thức "tùy chỉnh" (nếu cần)
                    // Ví dụ:
                    // public async Task<List<Product>> GetListByCategoryIdAsync(Guid categoryId) { ... }
                }
            }
            ```

    - **`DbContext` (Database Context) (Nếu Dùng Entity Framework Core):**
        *   Lớp `DbContext` (ví dụ: `MyProjectDbContext`) "đại diện" cho **"phiên làm việc"** (session) với database, "
            chứa" các `DbSet` properties để "truy cập" các "bảng" (tables) trong database.
        *   `DbContext` được "cấu hình" để "kết nối" với database (connection string) và "ánh xạ" (map) các Entities
            thành các tables trong database.

    - **Email Sending Service (Dịch vụ gửi email):**
        *   Các "lớp" (classes) để "gửi email" (ví dụ: sử dụng SMTP, SendGrid, MailKit, v.v.).
        *   Thường "triển khai" một "giao diện" (interface) được "định nghĩa" trong Application Layer hoặc Domain
            Layer (ví dụ: `IEmailSender`).

    - **SMS Sending Service (Dịch vụ gửi tin nhắn SMS):**
        *   Các "lớp" (classes) để "gửi tin nhắn SMS" (ví dụ: sử dụng Twilio, Nexmo, v.v.).
        *   Thường "triển khai" một "giao diện" (interface) được "định nghĩa" trong Application Layer hoặc Domain
            Layer.

    - **External API Clients (Các Clients Gọi API Bên Ngoài):**
        *   Các "lớp" (classes) để "gọi" các **"API bên ngoài"** (external APIs) (ví dụ: API của Google Maps, API của
            Facebook, API của một hệ thống khác).
        *   Thường "sử dụng" `HttpClient` hoặc các thư viện HTTP client khác.
        *   Thường "triển khai" một "giao diện" (interface) được "định nghĩa" trong Application Layer hoặc Domain
            Layer.

    - **Logging (Ghi Log):**
        *   "Triển khai" "cấu hình" logging (ví dụ: sử dụng Serilog, NLog) để "ghi log" các "sự kiện" trong ứng dụng (
            ví dụ: lỗi, cảnh báo, thông tin debug, v.v.).

    - **Caching (Bộ Nhớ Đệm):**
        *   "Triển khai" "cấu hình" caching (ví dụ: sử dụng in-memory cache, distributed cache - Redis, Memcached) để "
            caching" dữ liệu "thường xuyên" "truy cập" và "tăng" "hiệu suất" ứng dụng.

    - **... (và các "thành phần" "kỹ thuật" khác):** Tùy thuộc vào "nhu cầu" của ứng dụng, Infrastructure Layer có thể "
        chứa" các "thành phần" "kỹ thuật" khác (ví dụ: message queue clients, file storage services, v.v.).

- **"Đặc Điểm" Của Infrastructure Layer:**

    *   **"Phụ thuộc" vào Domain Layer:** Infrastructure Layer "tham chiếu" (reference) đến Domain Layer để "truy
        cập" các **Entities**, **Value Objects**, và **Repository Interfaces**.
*   **"Cung cấp" "triển khai" "cụ thể"** cho các "giao diện" (interfaces) được "định nghĩa" ở các tầng "trên" (Domain
        Layer, Application Layer).
    *   **"Ẩn" "chi tiết" "kỹ thuật"** khỏi các tầng "lõi" của ứng dụng: Các tầng "lõi" (Domain Layer, Application
        Layer) "không cần" "biết" Infrastructure Layer "sử dụng" "công nghệ" "cụ thể" nào để "thực hiện" các "tác vụ" (
        ví dụ: "không cần" "biết" đang "dùng" database SQL Server hay MongoDB, "không cần" "biết" đang "dùng" thư viện
        gửi email nào).
    *   **"Dễ dàng" "thay đổi" "công nghệ" "bên dưới":** Bạn có thể "dễ dàng" "thay đổi" "công nghệ" được "sử dụng"
        trong Infrastructure Layer (ví dụ: "chuyển" từ Entity Framework Core sang Dapper, "chuyển" từ SQL Server sang
        PostgreSQL, "chuyển" từ SMTP sang SendGrid) mà **"không ảnh hưởng"** đến các tầng "lõi" của ứng dụng (nếu bạn
        "tuân thủ" các "nguyên tắc" "thiết kế" tốt và "sử dụng" các "giao diện" (interfaces) để "giao tiếp" giữa các
        tầng).

**Tổng Kết Chương 3:**

-   Bạn đã "khám phá" **kiến trúc "đa tầng"** (layered architecture) của ứng dụng ABP Framework, "nền tảng" "vững
    chắc" để "xây dựng" các ứng dụng .NET "chất lượng cao".
    *   "Hiểu" **kiến trúc "đa tầng" là gì** và "lợi ích" của việc "áp dụng" kiến trúc "đa tầng".
    *   "Nắm vững" **"các tầng" (layers) "chính"** trong kiến trúc ứng dụng ABP Framework:
        *   **Presentation Layer:** "Giao tiếp" với người dùng hoặc các ứng dụng khác (Web API controllers, Razor
            Pages, Blazor components, v.v.).
        *   **Application Layer:** "Triển khai" các "use cases" của ứng dụng (Application Services, DTOs).
        *   **Domain Layer:** "Trái tim" của ứng dụng, "chứa" "logic nghiệp vụ" (Entities, Value Objects, Domain
            Services, Repository Interfaces).
        *   **Infrastructure Layer:** "Cung cấp" các "triển khai" "cụ thể" cho các "giao diện" (ví dụ: Repository
            Implementations, Email Sending Service, External API Clients, v.v.).
    *   "Hiểu" **"mối quan hệ"** giữa các tầng và **"luồng dữ liệu"** (data flow) trong ứng dụng.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: ABP Modules - " 'Viên Gạch' " "Xây Dựng" Ứng Dụng**. Chúng ta sẽ "đi sâu" vào **
hệ thống mô-đun** (module system) của ABP Framework, "khám phá" các **"pre-built modules"** (mô-đun "có sẵn") "quan
trọng", và "học cách" **"tạo" custom modules** (mô-đun "tự tạo") để "mở rộng" "chức năng" của ứng dụng.

Bạn có câu hỏi nào về kiến trúc ứng dụng ABP Framework này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải
đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" ABP Framework.

