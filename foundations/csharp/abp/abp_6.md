# Chương 6: Application Services - " 'Cầu Nối' " Giữa " 'Ngoại Vi' " và " 'Nội Tại' " - " 'Xử Lý' " Các Use Cases - " 'Hiện Thực Hóa' " "Tính Năng" Ứng Dụng

Chào mừng bạn đến với **Chương 6: Application Services - " 'Cầu Nối' " Giữa " 'Ngoại Vi' " và " 'Nội Tại' "**! Trong
chương này, chúng ta sẽ "đi sâu" vào **Application Services** (Dịch vụ ứng dụng), một "thành phần" **"quan trọng"**
trong **Application Layer** của kiến trúc ABP Framework. Chúng ta sẽ "tìm hiểu" **Application Services là gì**, **"vai
trò"** của Application Services, **"cách" Application Services "tương tác"** với các "thành phần" khác trong ứng dụng,
và **"cách" "tạo" và "sử dụng" Application Services** để "triển khai" các **"use cases"** (trường hợp sử dụng) của ứng
dụng. Application Services "đóng vai trò" như **" 'cầu nối' " "liên kết"** giữa **Presentation Layer** (tầng trình bày -
ví dụ: Web API controllers) và **Domain Layer** (tầng nghiệp vụ), "giúp" bạn "xây dựng" các ứng dụng **"có tổ chức"**,
**"dễ bảo trì"**, và **"dễ kiểm thử"**.

**Phần 6: Application Services - " 'Cầu Nối' " Giữa " 'Ngoại Vi' " và " 'Nội Tại' " - " 'Xử Lý' " Các Use Cases**

- **Application Services (Dịch Vụ Ứng Dụng) - " 'Hiện Thực Hóa' " Các "Tính Năng" Ứng Dụng:**

    - **Application Services** (Dịch vụ ứng dụng) là các **"lớp"** (classes) **"triển khai"** các **"use cases"** (
      trường hợp sử dụng) của ứng dụng. Use cases là các **"tác vụ"** (tasks) hoặc **"hành động"** (actions) mà người
      dùng (hoặc ứng dụng khác) có thể "thực hiện" trên ứng dụng (ví dụ: "tạo sản phẩm mới", "xem danh sách sản phẩm", "
      cập nhật thông tin sản phẩm", "xóa sản phẩm", "đặt hàng", "thanh toán", v.v.).
    - Application Services "đóng vai trò" **"trung gian"** giữa **Presentation Layer** (tầng trình bày - ví dụ: Web API
      controllers) và **Domain Layer** (tầng nghiệp vụ).
        *   **Presentation Layer "gọi"** các phương thức của Application Services để "thực hiện" các "use cases".
        *   Application Services **"gọi"** các Domain Services (trong Domain Layer) và Repositories (trong
            Infrastructure Layer) để "thực hiện" các "tác vụ" "cụ thể" và "truy cập" dữ liệu.
        *   Application Services **"trả về" "kết quả"** cho Presentation Layer (thường thông qua các Data Transfer
            Objects - DTOs).
    - Application Services **"không chứa" "logic nghiệp vụ" "phức tạp"**. Logic nghiệp vụ "phức tạp" phải được "đặt"
      trong **Domain Layer** (trong các Domain Services, Entities, hoặc Value Objects). Application Services "chủ yếu"
      **"điều phối"** các hoạt động, "gọi" các Domain Services và Repositories, "xử lý" các "tác vụ" "ở mức cao", và "
      chuyển đổi" dữ liệu giữa Presentation Layer và Domain Layer (sử dụng DTOs).

- **"Tại Sao" Cần Application Services? - " 'Tách Biệt' " "Mối Quan Tâm", " 'Tăng' " "Tính 'Tái Sử Dụng' ", và " 'Dễ
  Kiểm Thử' "**:

    - **Separation of Concerns (Tách biệt các mối quan tâm):** Application Services "giúp" "tách biệt" **"giao diện"**
      (UI) và **"logic trình bày"** (presentation logic) (trong Presentation Layer) khỏi **"logic nghiệp vụ"** (
      business logic) (trong Domain Layer). "Giúp" code **"sạch sẽ"** hơn, **"dễ hiểu"** hơn, và **"dễ bảo trì"** hơn.
    * **Tránh trùng lặp code:**
    - **Reusability (Khả năng tái sử dụng):** Application Services "có thể" được **"tái sử dụng"** bởi **"nhiều"** "giao
      diện người dùng" (UI) hoặc "điểm gọi" (entry points) khác nhau (ví dụ: Web API, Razor Pages, Blazor, gRPC,
      console application, v.v.). Bạn "không cần" phải "viết lại" code "xử lý" use cases cho "mỗi" giao diện người
      dùng.
    - **Testability (Khả năng kiểm thử):** Application Services "dễ dàng" được **"kiểm thử"** (unit testing) vì chúng
      **"không phụ thuộc"** vào các "thành phần" UI hoặc các "công nghệ" "giao tiếp" "cụ thể" (ví dụ: HTTP,
      WebSockets). Bạn có thể "mock" (giả lập) các Domain Services và Repositories được "sử dụng" bởi Application
      Services để "kiểm thử" logic của Application Services một cách "cô lập".

- **"Cách" ABP Framework "Hỗ Trợ" Application Services - " 'Đơn Giản Hóa' " Việc "Tạo" và "Sử Dụng" Application
  Services:**

    - ABP Framework "cung cấp" các **"lớp cơ sở"** (base classes) và **"giao diện"** (interfaces) để bạn **"dễ dàng" "
      tạo"** Application Services.
    - ABP Framework "tự động" **"đăng ký"** (register) Application Services vào hệ thống **Dependency Injection (DI)**
      , "giúp" bạn **"dễ dàng" "sử dụng"** Application Services trong các "thành phần" khác của ứng dụng (ví dụ:
      controllers, Razor Pages, Blazor components).
    - ABP Framework "cung cấp" các **"tính năng" "tích hợp"** (built-in features) để "xử lý" các "tác vụ" "phổ biến"
      trong Application Services (ví dụ: data validation, authorization, exception handling, auditing, v.v.).

**6.1. Tạo Application Service - " 'Hiện Thực Hóa' " Các "Tính Năng" Ứng Dụng - " 'Xây Dựng' " "Cầu Nối"**

- **"Các Bước" "Tạo" Application Service Trong ABP Framework:**

    1.  **"Tạo" Interface (Giao diện) cho Application Service (trong `.Application.Contracts` project):**
        *   "Tạo" một **"interface"** (giao diện) trong dự án **`.Application.Contracts`** để "định nghĩa" các **"
            phương thức"** (methods) của Application Service. "Đặt tên" interface theo "quy ước" (ví dụ:
            `IProductAppService`, `IOrderAppService`).
        *   Interface "thường" "kế thừa" từ interface **`IApplicationService`** (hoặc các interface "con" của nó như
            `ICrudAppService`, `IReadOnlyAppService`) của ABP Framework.
        *   "Định nghĩa" các **"phương thức"** của Application Service trong interface. Mỗi phương thức "thường" "đại
            diện" cho một **"use case"** của ứng dụng.
        *   **"Ví dụ":**

            ```csharp
            // Application.Contracts/Products/IProductAppService.cs (Application Service Interface)

            using System;
            using System.Collections.Generic;
            using System.Threading.Tasks;
            using Volo.Abp.Application.Dtos;
            using Volo.Abp.Application.Services;

            namespace MyProject.Products
            {
                public interface IProductAppService : IApplicationService // Kế thừa từ IApplicationService
                {
                    Task<ProductDto> GetAsync(Guid id); // Lấy sản phẩm theo ID

                    Task<PagedResultDto<ProductDto>> GetListAsync(PagedAndSortedResultRequestDto input); // Lấy danh sách sản phẩm (có phân trang và sắp xếp)

                    Task<ProductDto> CreateAsync(CreateUpdateProductDto input); // Tạo sản phẩm mới

                    Task<ProductDto> UpdateAsync(Guid id, CreateUpdateProductDto input); // Cập nhật sản phẩm

                    Task DeleteAsync(Guid id); // Xóa sản phẩm
                }
            }
            ```

    2.  **"Tạo" Lớp (Class) "Triển Khai" (Implementation) Application Service (trong `.Application` project):**
        *   "Tạo" một **"lớp"** (class) trong dự án **`.Application`** để **"triển khai"** (implement) **"giao diện"**
            Application Service bạn đã "tạo" ở bước 1. "Đặt tên" lớp theo "quy ước" (ví dụ: `ProductAppService`, `
            OrderAppService`).
        *   Lớp Application Service "thường" "kế thừa" từ lớp **`ApplicationService`** (hoặc các lớp "con" của nó
            như `CrudAppService`, `ReadOnlyAppService`) của ABP Framework.
        *   **"Triển khai"** (implement) các **"phương thức"** của Application Service trong lớp. "Viết" code để "thực
            hiện" các "use cases" của ứng dụng (bằng cách "gọi" các Domain Services, Repositories, và các "thành phần"
            khác).
        *   **"Sử dụng" Dependency Injection (DI)** để **"tiêm"** (inject) các **dependencies** (ví dụ: Repositories,
            Domain Services) vào Application Service thông qua **constructor** (constructor injection).
        *   **"Ví dụ":**

            ```csharp
            // Application/Products/ProductAppService.cs (Application Service Implementation)

            using System;
            using System.Collections.Generic;
            using System.Threading.Tasks;
            using Microsoft.AspNetCore.Authorization;
            using Volo.Abp.Application.Dtos;
            using Volo.Abp.Application.Services;
            using Volo.Abp.Domain.Repositories;

            namespace MyProject.Products
            {
                [Authorize] // Áp dụng authorization (phân quyền) cho toàn bộ Application Service (tùy chọn)
                public class ProductAppService :
                    CrudAppService< // Kế thừa từ CrudAppService (cung cấp sẵn các phương thức CRUD cơ bản)
                        Product, // Entity
                        ProductDto, // DTO
                        Guid, // Primary Key Type
                        PagedAndSortedResultRequestDto, // Input DTO cho phân trang và sắp xếp
                        CreateUpdateProductDto>, // Input DTO cho tạo và cập nhật
                    IProductAppService // Triển khai interface IProductAppService
                {
                    public ProductAppService(IRepository<Product, Guid> repository)
                        : base(repository)
                    {
                    }

                    // Có thể "ghi đè" (override) các phương thức từ CrudAppService hoặc "thêm" các phương thức "tùy chỉnh" (nếu cần)
                }
            }
            ```

        *   **`[Authorize]` attribute:** (Tùy chọn) "Áp dụng" **authorization** (phân quyền) cho toàn bộ Application
            Service hoặc cho các "phương thức" cụ thể trong Application Service.
        *   **`CrudAppService`:** Lớp "cơ sở" (base class) "cung cấp" sẵn các **"phương thức" CRUD "cơ bản"** (Create,
            Read, Update, Delete) cho Application Service. Bạn có thể "kế thừa" từ `CrudAppService` để "tiết kiệm"
            thời gian "viết" code CRUD "lặp đi lặp lại". (Nếu bạn "không cần" các phương thức CRUD "mặc định", bạn có
            thể "kế thừa" từ lớp `ApplicationService` "cơ bản".)

    3.  **ABP Framework "Tự Động" "Đăng Ký" Application Services:** ABP Framework "sử dụng" **"quy ước"** (convention)
        để **"tự động" "đăng ký"** (register) Application Services vào hệ thống **Dependency Injection (DI)**. Bạn
        **"không cần" "phải 'đăng ký' " Application Services "thủ công"**.
        *   ABP Framework "tự động" "quét" (scan) các lớp "kế thừa" từ `ApplicationService` (hoặc các lớp "con" của
            nó) hoặc "triển khai" interface `IApplicationService` (hoặc các interface "con" của nó) và "đăng ký" chúng
            vào DI container.
        *   Bạn có thể "sử dụng" Application Services trong các "thành phần" khác của ứng dụng (ví dụ: controllers,
            Razor Pages, Blazor components) thông qua **Dependency Injection (DI)** (constructor injection).

**6.2. Data Transfer Objects (DTOs) - " 'Vận Chuyển' " Dữ Liệu - " 'Đóng Gói' " Dữ Liệu Để "Trao Đổi"**

- **Data Transfer Objects (DTOs) - " 'Hộp' " "Chứa" Dữ Liệu Để "Truyền" Giữa Các Tầng:**

    - **Data Transfer Objects (DTOs)** là các **"đối tượng" "đơn giản"** (simple objects) **"chỉ chứa" dữ liệu**, **"
      không chứa" "logic nghiệp vụ"**. DTOs được "dùng" để **"truyền" dữ liệu** giữa **Presentation Layer** và **
      Application Layer**.
    - DTOs "đóng vai trò" như các **" 'hộp' " (containers)** để **"đóng gói" dữ liệu** cần thiết để "truyền" giữa các
      tầng của ứng dụng. DTOs "giúp" **"tách biệt"** (decouple) Presentation Layer và Domain Layer, "giảm thiểu" "sự
      phụ thuộc" giữa các tầng, và "tối ưu hóa" việc "truyền" dữ liệu.

- **"Các Loại" DTOs "Phổ Biến" Trong ABP Framework:**

    - **Input DTOs:**
        *   "Dùng" để **"nhận" dữ liệu** từ Presentation Layer (ví dụ: từ HTTP request body).
        *   "Thường" được "dùng" làm **"tham số"** (parameters) cho các phương thức của Application Services (ví dụ:
            `CreateProductDto`, `UpdateProductDto`).
        *   **"Ví dụ":**

            ```csharp
            // Products/CreateUpdateProductDto.cs (Input DTO)

            using System.ComponentModel.DataAnnotations;

            namespace MyProject.Products
            {
                public class CreateUpdateProductDto // DTO để tạo và cập nhật sản phẩm
                {
                    [Required] // Data annotation để validate (bắt buộc phải nhập)
                    [StringLength(128)] // Data annotation để validate (giới hạn độ dài chuỗi)
                    public string Name { get; set; }

                    [Required]
                    public decimal Price { get; set; }

                    public string Description {get; set;}
                }
            }
            ```

    - **Output DTOs:**
        *   "Dùng" để **"trả về" dữ liệu** cho Presentation Layer (ví dụ: trả về HTTP response body).
        *   "Thường" được "trả về" bởi các phương thức của Application Services (ví dụ: `ProductDto`).
        *   **"Ví dụ":**

            ```csharp
            // Products/ProductDto.cs (Output DTO)

            using System;
            using Volo.Abp.Application.Dtos;

            namespace MyProject.Products
            {
                public class ProductDto : AuditedEntityDto<Guid> // Kế thừa từ AuditedEntityDto (cung cấp các thuộc tính như Id, CreationTime, CreatorId, v.v.)
                {
                    public string Name { get; set; }
                    public decimal Price { get; set; }
                    public string Description {get; set;}
                }
            }
            ```

    - **List DTOs:**
        *   "Dùng" để "trả về" **"danh sách"** (list) các đối tượng (ví dụ: `List<ProductDto>`).
        *   "Thường" được "kết hợp" với **"phân trang"** (pagination) và **"sắp xếp"** (sorting).
        *   **"Ví dụ":** ABP Framework "cung cấp" sẵn các DTOs cho phân trang và sắp xếp (ví dụ:
            `PagedAndSortedResultRequestDto`, `PagedResultDto<T>`).

            ```csharp
                // Sử dụng PagedResultDto để trả về danh sách sản phẩm có phân trang
                public async Task<PagedResultDto<ProductDto>> GetListAsync(PagedAndSortedResultRequestDto input)
                {
                    // ...
                }
            ```

- **"Ánh Xạ" (Mapping) Giữa Entities và DTOs - " 'Chuyển Đổi' " Dữ Liệu:**

    - Bạn cần **"ánh xạ"** (map) dữ liệu giữa **Entities** (trong Domain Layer) và **DTOs** (trong Application Layer).
    - **"Cách 'ánh xạ' " Entities và DTOs:**
        *   **"Thủ công" (Manual Mapping):** "Viết" code để "gán" giá trị từ các thuộc tính của Entity sang các thuộc
            tính của DTO (và ngược lại).
        *   **"Sử dụng" thư viện "AutoMapper" (khuyên dùng):** **AutoMapper** là một thư viện .NET "phổ biến" để **"tự
            động hóa"** quá trình "ánh xạ" giữa các đối tượng. AutoMapper "giúp" bạn "giảm thiểu" "code 'lặp đi lặp lại'
            " và "làm cho" code "ánh xạ" "gọn gàng" hơn.
            *   ABP Framework **"tích hợp"** sẵn **AutoMapper**. Bạn có thể "sử dụng" AutoMapper một cách "dễ dàng"
                trong các Application Services.
            *   **"Ví dụ" (sử dụng AutoMapper):**

                ```csharp
                // Trong Application Service
                public async Task<ProductDto> CreateAsync(CreateUpdateProductDto input)
                {
                    // ...

                    // Ánh xạ (map) từ CreateUpdateProductDto sang Product (Entity)
                    var product = ObjectMapper.Map<CreateUpdateProductDto, Product>(input); // Sử dụng ObjectMapper (AutoMapper)

                    // Lưu Product vào database
                    await _productRepository.InsertAsync(product);

                    // Ánh xạ (map) từ Product (Entity) sang ProductDto
                    return ObjectMapper.Map<Product, ProductDto>(product); // Trả về ProductDto
                }
                ```

                * Bạn cần "định nghĩa" **"mapping profiles"** (AutoMapper profiles) để "chỉ định" "cách" AutoMapper "ánh
                  xạ" giữa các đối tượng.

                  ```csharp
                  // Tạo 1 class kế thừa từ Profile:
                  public class MyProjectApplicationAutoMapperProfile : Profile
                  {
                      public MyProjectApplicationAutoMapperProfile()
                      {
                          CreateMap<Product, ProductDto>();
                          CreateMap<CreateUpdateProductDto, Product>();
                      }
                  }
                  ```

**6.3. Input Validation (Kiểm Tra Đầu Vào) - " 'Bảo Vệ' " Ứng Dụng Khỏi Dữ Liệu " 'Xấu' "**

- **Input Validation - " 'Chốt Chặn' " "Đầu Tiên" Để "Đảm Bảo" "An Toàn" và "Chính Xác" Dữ Liệu:**

    - **Input Validation** (Kiểm tra đầu vào) là quá trình **"kiểm tra"** xem dữ liệu **"đầu vào"** (input data) từ
      Presentation Layer (ví dụ: từ HTTP request body, từ form data) có **"hợp lệ"** (valid) hay không **"trước khi"** "
      xử lý" dữ liệu đó trong Application Layer hoặc Domain Layer.
    - Input Validation "giúp":
        *   **"Đảm bảo" "an toàn"** cho ứng dụng: "Ngăn chặn" các **"tấn công"** dựa trên dữ liệu "đầu vào" "độc hại" (
            ví dụ: SQL injection, Cross-Site Scripting (XSS), v.v.).
        *   **"Đảm bảo" "chính xác"** dữ liệu: "Đảm bảo" dữ liệu "đầu vào" "tuân thủ" các **"quy tắc"** và **"ràng
            buộc"** của ứng dụng (ví dụ: "bắt buộc" nhập một số trường, "giới hạn" độ dài chuỗi, "kiểm tra" định dạng
            email, v.v.).
        *   **"Cải thiện" "trải nghiệm" người dùng:** "Cung cấp" **"phản hồi" "sớm"** và **"rõ ràng"** cho người dùng về
            các "lỗi" dữ liệu "đầu vào", "giúp" người dùng "nhập" dữ liệu "đúng" và "nhanh chóng" hơn.

- **"Các Kỹ Thuật" Input Validation Trong ABP Framework:**

    *   **Data Annotations (Chú thích dữ liệu):**
        *   **"Cách 'dễ nhất' " và "phổ biến nhất"** để "kiểm tra" dữ liệu "đầu vào" trong ABP Framework.
        *   "Sử dụng" các **"attributes"** (chú thích) (ví dụ: `[Required]`, `[StringLength]`, `[EmailAddress]`, `[
            Range]`, `[RegularExpression]`, v.v.) để "định nghĩa" các **"quy tắc" "kiểm tra"** (validation rules) cho
            các **"thuộc tính"** của **DTOs** (Data Transfer Objects).
        *   ABP Framework "tự động" "thực hiện" "kiểm tra" dữ liệu "đầu vào" dựa trên các Data Annotations khi bạn "
            gọi" các Application Services.
        *   **"Ví dụ":**

            ```csharp
            // Products/CreateUpdateProductDto.cs (Input DTO)

            using System.ComponentModel.DataAnnotations;

            namespace MyProject.Products
            {
                public class CreateUpdateProductDto // DTO để tạo và cập nhật sản phẩm
                {
                    [Required] // Bắt buộc phải nhập
                    [StringLength(128)] // Giới hạn độ dài chuỗi tối đa là 128 ký tự
                    public string Name { get; set; }

                    [Required]
                    [Range(0, 1000000)] // Giá trị phải nằm trong khoảng từ 0 đến 1000000
                    public decimal Price { get; set; }
                    public string Description {get; set;}
                }
            }
            ```

    *   **Fluent Validation:**
        *   **"Thư viện" "mạnh mẽ"** và **"linh hoạt"** để "kiểm tra" dữ liệu "đầu vào" trong .NET.
        *   "Cho phép" bạn "định nghĩa" các "quy tắc" "kiểm tra" **"phức tạp"** hơn Data Annotations bằng cách "sử
            dụng" **"fluent interface"** (giao diện "trôi chảy").
        *   ABP Framework "tích hợp" sẵn **Fluent Validation**. Bạn có thể "dễ dàng" "sử dụng" Fluent Validation trong
            các Application Services.

    *   **Custom Validation (Kiểm tra tùy chỉnh):**
        *   Nếu bạn cần "thực hiện" các "quy tắc" "kiểm tra" **"phức tạp"** mà Data Annotations và Fluent Validation "
            không hỗ trợ", bạn có thể "tự mình" "viết" code "kiểm tra" trong Application Services (hoặc trong Domain
            Services).

- **"Xử Lý" Lỗi Validation Trong ABP Framework:**

    *   Khi dữ liệu "đầu vào" **"không hợp lệ"**, ABP Framework sẽ **"tự động" "ném ra"** (throw) một **`
        AbpValidationException`**.
    *   `AbpValidationException` "chứa" thông tin chi tiết về các "lỗi" validation (ví dụ: trường nào bị lỗi, thông
        báo lỗi là gì).
    *   ABP Framework "tự động" "xử lý" `AbpValidationException` và **"trả về"** một **HTTP response** với **status
        code 400 (Bad Request)** và **"thông báo lỗi"** "chi tiết" cho client (ví dụ: dưới dạng JSON).
    *   Bạn có thể "tùy chỉnh" "cách" ABP Framework "xử lý" lỗi validation bằng cách "ghi đè" (override) phương thức `
        NormalizeException` trong lớp `AbpExceptionFilter`.

**6.4. Authorization (Phân Quyền) - " 'Kiểm Soát' " "Quyền Truy Cập" - " 'Ai' " "Được Làm Gì"**

- **Authorization (Phân Quyền) - " 'Xác Định' " "Ai" "Được Phép" "Làm Gì" Trong Ứng Dụng:**

    - **Authorization** (Phân quyền) là quá trình **"xác định"** xem một **"người dùng"** (user) (hoặc một **"ứng
      dụng"**) đã được **"xác thực"** (authenticated) có **"quyền"** (permission) để **"thực hiện"** một **"hành
      động"** (action) cụ thể hoặc **"truy cập"** vào một **"tài nguyên"** (resource) cụ thể trong ứng dụng hay không.
    - Authorization "thường" được "thực hiện" **"sau khi"** người dùng đã được **"xác thực"** (authenticated) (tức là
      sau khi đã "xác minh" "danh tính" của người dùng).
    - Authorization "giúp" **"bảo vệ"** ứng dụng khỏi các **"truy cập" "trái phép"** và **"đảm bảo"** rằng người dùng
      chỉ có thể "thực hiện" các "hành động" mà họ được "phép".

- **"Các Cơ Chế" Authorization (Phân Quyền) "Phổ Biến" Trong ABP Framework:**

    - **Role-Based Authorization (Phân quyền dựa trên vai trò):**
        *   **"Cơ chế" "phân quyền" "phổ biến" và "dễ hiểu" nhất**.
        *   "Gán" người dùng vào các **"vai trò"** (roles) (ví dụ: "Admin", "User", "Editor", "Manager", v.v.).
        *   "Định nghĩa" **"quyền"** (permissions) cho từng "vai trò".
        *   "Kiểm tra" xem người dùng có "vai trò" "cần thiết" để "thực hiện" một "hành động" hoặc "truy cập" vào một "
            tài nguyên" hay không.
        *   **"Ví dụ":**
            *   Chỉ người dùng có role "Admin" mới có quyền "xóa" sản phẩm.
            *   Người dùng có role "Editor" có quyền "sửa" bài viết, nhưng không có quyền "xóa" bài viết.

    - **Permission-Based Authorization (Phân quyền dựa trên quyền):**
        *   **"Cơ chế" "phân quyền" "linh hoạt"** và **"mạnh mẽ"** hơn Role-Based Authorization.
        *   "Định nghĩa" các **"quyền"** (permissions) **"cụ thể"** trong ứng dụng (ví dụ: `Products.Create`, `
            Products.Edit`, `Products.Delete`, `Orders.View`, `Orders.Ship`, v.v.).
        *   "Gán" các "quyền" cho người dùng hoặc vai trò.
        *   "Kiểm tra" xem người dùng có "quyền" "cần thiết" để "thực hiện" một "hành động" hoặc "truy cập" vào một "
            tài nguyên" hay không.
        *   **"Ví dụ":**
            *   Quyền `Products.Create` cho phép người dùng "tạo" sản phẩm mới.
            *   Quyền `Orders.Ship` cho phép người dùng "xác nhận" đơn hàng đã được "vận chuyển".

    - **Policy-Based Authorization (Phân quyền dựa trên chính sách):**
        *   **"Cơ chế" "phân quyền" "linh hoạt" và "mở rộng" nhất**.
        *   "Định nghĩa" các **"chính sách"** (policies) "phân quyền" bằng cách "kết hợp" các "điều kiện" (conditions)
            và "quy tắc" (rules) "phức tạp".
        *   "Kiểm tra" xem người dùng có "đáp ứng" các "điều kiện" của "chính sách" hay không để "quyết định" xem người
            dùng có "quyền" "thực hiện" một "hành động" hoặc "truy cập" vào một "tài nguyên" hay không.
        *   **"Ví dụ":**
            *   "Chính sách" "Order.EditPolicy" có thể "quy định" rằng người dùng chỉ có thể "sửa" đơn hàng nếu đơn
                hàng ở trạng thái "Pending" và người dùng là "chủ sở hữu" của đơn hàng đó hoặc có role "Admin".

- **"Cách" ABP Framework "Hỗ Trợ" Authorization (Phân Quyền):**

    - ABP Framework "tích hợp" sẵn các **"cơ chế" "phân quyền"** (Role-Based, Permission-Based, Policy-Based) và "cung
      cấp" các **"API"** và **"attributes"** để bạn **"dễ dàng" "triển khai"** authorization trong ứng dụng của mình.
    - **"Các Thành Phần" "Chính" Cho Authorization Trong ABP Framework:**
        *   **`IPermissionChecker` (Interface):** "Giao diện" "cốt lõi" để "kiểm tra" quyền (permissions). Cung cấp
            các phương thức như `IsGrantedAsync` để "kiểm tra" xem người dùng có "quyền" cụ thể hay không.
        *   **`[Authorize]` Attribute:** "Attribute" (chú thích) để "áp dụng" authorization cho các **Application
            Services** (hoặc các phương thức cụ thể trong Application Services), **Web API Controllers** (hoặc các
            actions cụ thể trong controllers), **Razor Pages**, hoặc **Blazor Components**.
            *   `[Authorize]`: "Kiểm tra" xem người dùng đã được **"xác thực"** (authenticated) hay chưa.
            *   `[Authorize(Roles = "Admin,Manager")]`: "Kiểm tra" xem người dùng có **"vai trò"** (role) "Admin"
                hoặc "Manager" hay không.
            *   `[Authorize(Permissions = "Products.Create")]`: "Kiểm tra" xem người dùng có **"quyền"** (permission)
                `Products.Create` hay không.
            *   `[Authorize(Policy = "Order.EditPolicy")]`: "Kiểm tra" xem người dùng có "đáp ứng" **"chính sách"**
                (policy) `Order.EditPolicy` hay không.
        *   **Permission Management Module:** ABP Framework "cung cấp" **Permission Management Module** để bạn "định
            nghĩa" và "quản lý" các "quyền" (permissions) trong ứng dụng.
        *   **Authorization Middleware:** ABP Framework "tự động" "thêm" **Authorization Middleware** vào pipeline của
            ứng dụng ASP.NET Core để "thực hiện" "kiểm tra" authorization dựa trên các `[Authorize]` attributes.

    - **"Ví Dụ" Authorization Trong Application Service (Sử Dụng `[Authorize]` Attribute):**

      ```csharp
      // Application/Products/ProductAppService.cs (Application Service)

      using Microsoft.AspNetCore.Authorization;
      using Volo.Abp.Application.Services;

      namespace MyProject.Products
      {
          [Authorize(Permissions = "Products.Manage")] // Yêu cầu người dùng phải có quyền "Products.Manage" để truy cập vào Application Service này
          public class ProductAppService : ApplicationService, IProductAppService
          {
              // ...

              [Authorize(Permissions = "Products.Create")] // Yêu cầu người dùng phải có quyền "Products.Create" để gọi phương thức này
              public async Task<ProductDto> CreateAsync(CreateUpdateProductDto input)
              {
                  // ...
              }

              [Authorize(Roles = "Admin")] // Yêu cầu người dùng phải có role "Admin" để gọi phương thức này
              public async Task DeleteAsync(Guid id)
              {
                  // ...
              }
          }
      }
      ```

**Tổng Kết Chương 6:**

-   Bạn đã "tìm hiểu" về **Application Services** (Dịch vụ ứng dụng), " 'cầu nối' " giữa Presentation Layer và Domain
    Layer trong kiến trúc ABP Framework.
    -   "Hiểu" **Application Services là gì** ("lớp" "triển khai" các "use cases", "điều phối" các "tác vụ", "giao
        tiếp" với Presentation Layer và Domain Layer).
    -   "Biết" **vai trò" của Application Services** ("tách biệt" "mối quan tâm", "tăng" "tính 'tái sử dụng' ", "dễ
        kiểm thử").
    -   "Học cách" **"tạo" Application Services** trong ABP Framework (kế thừa từ `ApplicationService` hoặc `
        CrudAppService`, "triển khai" interface, "sử dụng" Dependency Injection).
    -   "Nắm vững" **Data Transfer Objects (DTOs)** và "cách" "sử dụng" DTOs để "truyền" dữ liệu giữa Presentation
        Layer và Application Layer.
    -   "Tìm hiểu" về **Input Validation** (Data Annotations, Fluent Validation, Custom Validation) và "cách" ABP
        Framework "xử lý" lỗi validation.
    -   "Khám phá" các **"cơ chế" Authorization** (phân quyền) trong ABP Framework (Role-Based, Permission-Based,
        Policy-Based) và "cách" "sử dụng" `[Authorize]` attribute để "bảo vệ" Application Services.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 7: Data Access (Truy Cập Dữ Liệu) - " 'Kết Nối' " Với " 'Kho Tàng' " Dữ Liệu**. Chúng
ta sẽ "tìm hiểu" cách ABP Framework "tích hợp" với **Entity Framework Core** (và các ORM khác), "khám phá" **
Repositories** (kho chứa) và **Unit of Work pattern**, và "học cách" "truy vấn" và "thao tác" dữ liệu trong ứng dụng
ABP Framework.

Bạn có câu hỏi nào về Application Services, DTOs, Input Validation, hoặc Authorization trong ABP Framework không? Hãy
cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" ABP Framework.