# Chương 4: ABP Modules - " 'Viên Gạch' " "Xây Dựng" Ứng Dụng - " 'Sức Mạnh' " Của Tính Mô-đun - " 'Lắp Ráp' " Ứng Dụng Từ Các Modules

Chào mừng bạn đến với **Chương 4: ABP Modules - " 'Viên Gạch' " "Xây Dựng" Ứng Dụng**! Trong chương này, chúng ta
sẽ "khám phá" **hệ thống mô-đun** (module system) của ABP Framework, **" 'linh hồn' "** của kiến trúc ABP Framework,
"tìm hiểu" **Module là gì**, "lợi ích" của việc "sử dụng" modules, "khám phá" các **"pre-built modules"** (mô-đun "
có sẵn") "quan trọng" mà ABP Framework "cung cấp", và "học cách" **"tạo" custom modules** (mô-đun "tự tạo") để "đóng
gói" và "tái sử dụng" các "tính năng" trong ứng dụng của bạn. "ABP Modules" là các **" 'viên gạch' " "lắp ráp"** nên
ứng dụng ABP Framework, "giúp" bạn "xây dựng" ứng dụng **"nhanh chóng"**, **"dễ dàng"**, và **"có tổ chức"**.

**Phần 4: ABP Modules - " 'Viên Gạch' " "Xây Dựng" Ứng Dụng - " 'Sức Mạnh' " Của Tính Mô-đun**

**4.1. Module System (Hệ Thống Mô-đun) - " 'Linh Hồn' " Của ABP Framework - " 'Chia Nhỏ' " Ứng Dụng Để " 'Dễ Quản Lý'
"**

- **Module (Mô-đun) - " 'Đơn Vị' " "Độc Lập" và "Tái Sử Dụng" Trong ABP Framework:**

    - Trong ABP Framework, **Module** (Mô-đun) là một **"đơn vị" "độc lập"**, **"tự đóng gói"** (self-contained), và **"
      có thể 'tái sử dụng' "**, "chứa" **"tất cả" các "thành phần"** (entities, services, controllers, views,
      localization resources, v.v.) "liên quan" đến một **"chức năng" "cụ thể"** của ứng dụng.
    - Hãy tưởng tượng Module như một **" 'viên gạch Lego' "** trong **" 'bộ Lego' " ABP Framework**. Mỗi "viên gạch" (
      module) có "hình dạng", "kích thước", và "chức năng" "riêng", nhưng có thể được **"lắp ráp"** với các "viên gạch" "
      khác" để "tạo ra" các "công trình" "phức tạp" hơn (ứng dụng).
    - Module là **" 'trái tim' " và " 'linh hồn' " của kiến trúc ABP Framework**. ABP Framework "được thiết kế" theo
      kiến trúc **"hướng mô-đun"** (module-oriented architecture) từ "gốc". "Mọi thứ" trong ABP Framework đều là **"
      module"** (hoặc "thuộc về" một module).
    - ABP Framework "cung cấp" **"nhiều" "pre-built modules"** (mô-đun "có sẵn") để "giải quyết" các **"bài toán" "
      phổ biến"** trong phát triển ứng dụng (ví dụ: Identity Module, Tenant Management Module, Setting Management
      Module, Audit Logging Module, v.v.). Bạn có thể **"tái sử dụng"** các "pre-built modules" này trong ứng dụng
      của mình để **"tiết kiệm" "thời gian"** và **"công sức"**.
    - Bạn cũng có thể **"tạo" custom modules** (mô-đun "tự tạo") để "đóng gói" các **"tính năng" "riêng"** của ứng
      dụng hoặc để "tái sử dụng" các "tính năng" trong "nhiều dự án" khác nhau.

- **"Lợi Ích" Của Việc "Sử Dụng" Modules Trong ABP Framework - " 'Chia Để Trị' ", " 'Tái Sử Dụng' ", và " 'Mở Rộng' "
  Dễ Dàng:**

    - **"Tổ Chức" Code "Gọn Gàng" và "Dễ Quản Lý" (Code Organization and Maintainability):** Modules "giúp" bạn **"
      chia" ứng dụng "lớn"** thành các **"phần nhỏ" "dễ quản lý"** hơn. Mỗi module "chứa" các "thành phần" "liên
      quan" đến một "chức năng" "cụ thể", "giúp" code **"gọn gàng"**, **"dễ hiểu"**, và **"dễ bảo trì"** hơn.
    * **" cô lập logic", dễ tìm kiếm và sửa chữa**
    - **"Tăng" "Tính 'Tái Sử Dụng' " Code (Code Reusability):**
        *   Bạn có thể **"tái sử dụng"** các **"pre-built modules"** (mô-đun "có sẵn") của ABP Framework trong **"nhiều
            dự án"** khác nhau. "Tiết kiệm" thời gian và công sức "viết lại" code cho các "tính năng" "chung" (ví dụ:
            quản lý người dùng, phân quyền, đa ngôn ngữ, v.v.).
        *   Bạn có thể **"tạo" custom modules** (mô-đun "tự tạo") để "đóng gói" các **"tính năng" "riêng"** của ứng
            dụng hoặc các **"thành phần" "có thể 'tái sử dụng' "** và "sử dụng lại" các modules này trong **"nhiều dự
            án"** khác nhau.
    - **"Giảm" "Coupling" (Sự Phụ Thuộc) Giữa Các "Thành Phần" Ứng Dụng (Loose Coupling):** Modules "được thiết kế" để
      **"độc lập"** với nhau. Các modules "giao tiếp" với nhau thông qua các **"giao diện"** (interfaces) và **"sự
      kiện"** (events), **"không phụ thuộc"** vào các "triển khai" (implementations) "cụ thể" của nhau. "Giảm thiểu" "
      sự phụ thuộc" (coupling) giữa các "thành phần" ứng dụng, "giúp" ứng dụng **"dễ bảo trì"**, **"dễ nâng cấp"**, và **"
      dễ kiểm thử"** hơn.
    - **"Dễ Dàng" "Thêm" Hoặc "Xóa" "Tính Năng" (Easy Feature Management):** Modules "cho phép" bạn **"dễ dàng" "thêm"
      ** hoặc **"xóa" "tính năng"** của ứng dụng bằng cách **"thêm"** hoặc **"xóa"** các modules "tương ứng". "Không cần"
      phải "sửa đổi" code của các "thành phần" "khác" trong ứng dụng (nếu modules được thiết kế "đúng cách").
    - **"Hỗ Trợ" "Kiến Trúc Microservices" (Microservices Support):** Modules "có thể" được "triển khai" như các **
      microservices "độc lập"** (nếu cần). Mỗi microservice có thể là một module ABP Framework "riêng biệt". "Giúp" bạn
      "xây dựng" các ứng dụng **"microservices"** một cách **"dễ dàng"** và **"hiệu quả"**.
    - **"Dễ dàng" "phân chia" "công việc" trong "nhóm phát triển" (Team Collaboration):** Modules "giúp" **"phân chia" "
      công việc"** trong "nhóm phát triển" một cách "dễ dàng". Mỗi thành viên (hoặc nhóm con) có thể "phụ trách" "phát
      triển" và "bảo trì" một hoặc nhiều modules "riêng biệt".

- **"Định Nghĩa" Module Trong ABP Framework - " 'Khai Báo' " Module Class:**

    - Trong ABP Framework, mỗi module được "đại diện" bởi một **"lớp"** (class) **"kế thừa"** từ lớp **`AbpModule`** (
      lớp "cơ sở" cho tất cả các modules trong ABP Framework).
    - Lớp module (module class) "chứa" các **"thông tin" "khai báo"** về module (ví dụ: tên module, phiên bản,
      dependencies) và **"cấu hình"** module (ví dụ: đăng ký services, cấu hình database, v.v.).
    - **"Ví dụ" "Định Nghĩa" Module Class (C#):**

      ```csharp
      // MyModule.cs (Module Class)

      using Volo.Abp.Modularity;

      namespace MyProject.MyModule // Namespace của module
      {
          [DependsOn( // "Khai báo" các module "phụ thuộc" (dependencies) (nếu có)
              typeof(AbpIdentityModule), // Module "phụ thuộc" vào AbpIdentityModule (module quản lý danh tính)
              typeof(AbpTenantManagementModule) // Module "phụ thuộc" vào AbpTenantManagementModule (module quản lý đa người thuê)
          )]
          public class MyModule : AbpModule // Kế thừa từ AbpModule
          {
              // "Override" các phương thức của AbpModule để "cấu hình" module (nếu cần)
              // Ví dụ:
              public override void ConfigureServices(ServiceConfigurationContext context)
              {
                  // "Đăng ký" các services của module vào hệ thống Dependency Injection (DI)
                  // context.Services.AddTransient<IMyService, MyService>();

                  // "Cấu hình" các options của module (nếu có)
                  // Configure<MyModuleOptions>(options => { ... });
              }

              public override void OnApplicationInitialization(ApplicationInitializationContext context)
              {
                  // "Thực hiện" các "tác vụ" "khởi tạo" module khi ứng dụng "khởi động" (nếu cần)
                  // Ví dụ: "seed" dữ liệu vào database
              }
          }
      }
      ```

        *   **`[DependsOn(...)]` (Attribute):** "Khai báo" các **"module 'phụ thuộc' "** (dependencies) của module.
            Module của bạn có thể "phụ thuộc" vào các "pre-built modules" của ABP Framework hoặc các custom modules
            "khác". ABP Framework sẽ "đảm bảo" các module "phụ thuộc" được **"khởi tạo" "trước"** module của bạn.
        *   **`ConfigureServices` (Method):** "Phương thức" "quan trọng nhất" trong module class. "Dùng" để **"đăng
            ký"** các **services** của module vào hệ thống **Dependency Injection (DI)** của ABP Framework và **"cấu
            hình"** các **options** của module.
        *   **`OnApplicationInitialization` (Method):** "Phương thức" "tùy chọn" để "thực hiện" các **"tác vụ" "khởi
            tạo"** module khi ứng dụng **"khởi động"** (ví dụ: "seed" dữ liệu vào database, "đăng ký" các event
            handlers, v.v.).

**4.2. Các "Pre-built Modules" (Mô-đun "Có Sẵn") "Quan Trọng" - " 'Gia Vị' " Cho Ứng Dụng - " 'Thư Viện' " Modules "
Phong Phú"**

- **ABP Framework - " 'Kho Tàng' " Modules "Có Sẵn" (Pre-built Modules) - " 'Tiết Kiệm' " "Thời Gian" và "Công Sức"**:

    - ABP Framework "cung cấp" một **" 'thư viện' " "phong phú"** các **"pre-built modules"** (mô-đun "có sẵn") để "
      giải quyết" các **"bài toán" "phổ biến"** trong phát triển ứng dụng.
    - Bạn có thể **"tái sử dụng"** các "pre-built modules" này trong ứng dụng của mình **"một cách 'dễ dàng' "** bằng
      cách **"thêm"** các module vào **"dependencies"** của module class (sử dụng attribute `[DependsOn(...)]`).
    - "Sử dụng" các "pre-built modules" giúp bạn **"tiết kiệm" "đáng kể" "thời gian"** và **"công sức"** "phát triển"
      ứng dụng, "không cần" phải "viết lại" code cho các "tính năng" "chung" (ví dụ: quản lý người dùng, phân quyền, đa
      ngôn ngữ, v.v.).

- **"Một Số" "Pre-built Modules" "Quan Trọng" và "Phổ Biến" Của ABP Framework:**

    - **4.2.1. Identity Module (`Volo.Abp.Identity.AspNetCore`):**
        * **Chức năng**: Cung cấp các tính năng **quản lý người dùng** (users), **vai trò** (roles), và **xác thực**
          (authentication).
        * Tính năng:
            * Đăng ký/đăng nhập
            * Quản lý mật khẩu
            * Quản lý thông tin
            * Phân quyền (vai trò)
            * Xác thực 2 yếu tố
            * Tích hợp social login
            * ...
        * Các package liên quan: `Volo.Abp.Account.Web`
    - **4.2.2. Tenant Management Module (`Volo.Abp.TenantManagement.AspNetCore`):**
        * **Chức năng:** Cung cấp các tính năng **quản lý "đa người thuê"** (multi-tenancy) cho ứng dụng SaaS (Software as
          a Service).
        * Tính năng:
            * Quản lý tenant (tạo, sửa, xóa).
            * Phân tách dữ liệu.
        * **Lưu ý:** Multi-tenancy cần được "bật" trong cấu hình ứng dụng.

    - **4.2.3. Setting Management Module (`Volo.Abp.SettingManagement.AspNetCore`):**
        *   **Chức năng:** Cung cấp các tính năng **quản lý "cài đặt"** (settings) của ứng dụng. Cho phép "lưu trữ" và "
            truy xuất" các "cài đặt" ở các "mức" khác nhau (global, tenant, user).
        * Tính năng:
            * Định nghĩa setting.
            * Lấy/gán giá trị setting.
            * Nhiều provider khác nhau.

    - **4.2.4. Audit Logging Module (`Volo.Abp.AuditLogging.AspNetCore`):**
        *   **Chức năng:** Cung cấp các tính năng **ghi nhật ký kiểm toán** (audit logging). "Tự động" "ghi lại" các "
            hành động" của người dùng và hệ thống (ví dụ: đăng nhập, đăng xuất, tạo, sửa, xóa dữ liệu, v.v.).
        * Tính năng:
            * Ghi log các thay đổi của entity.
            * Ghi log các hành động của user.

    - **4.2.5. Permission Management Module (`Volo.Abp.PermissionManagement.AspNetCore`):**
        * Chức năng: định nghĩa và quản lý các quyền trong hệ thống

    - **4.2.6. Feature Management Module (`Volo.Abp.FeatureManagement.AspNetCore`):**
        * Chức năng: Quản lý các tính năng.

    - **4.2.7. Blob Storing Module (`Volo.Abp.BlobStoring`):**
        *   **Chức năng:** Cung cấp một **"hệ thống 'trừu tượng' "** để **"lưu trữ"** và **"quản lý"** các **"đối tượng
            nhị phân"** (binary objects) (ví dụ: file, ảnh, video, v.v.).
        *   **Hỗ trợ nhiều "providers" khác nhau:** FileSystem, Azure Blob Storage, AWS S3, v.v.

    - **4.2.8. Emailing Module (`Volo.Abp.Emailing`):**
        *   **Chức năng:** Cung cấp các API để **"gửi email"**.
        *   **Hỗ trợ nhiều "providers" khác nhau:** SMTP, SendGrid, MailKit, v.v.

    - **4.2.9. Text Templating Module (`Volo.Abp.TextTemplating`):**

        *   **Chức năng:** Cung cấp một hệ thống để **"tạo"** các **"văn bản"** (text) dựa trên các **"mẫu"** (
            templates) và **"dữ liệu"** đầu vào.
    - **4.2.10 Background Jobs Module (`Volo.Abp.BackgroundJobs`):**
        * Chức năng: Hỗ trợ thực hiện các tác vụ nền.
    - ... (và **"rất nhiều"** pre-built modules "khác" - xem tài liệu ABP Framework để biết thêm chi tiết).

- **"Cách 'Dùng' " Pre-built Modules - " 'Thêm' " Module Vào "Dependencies":**

    1.  **"Cài đặt" NuGet Package:** "Cài đặt" **NuGet package** của module mà bạn muốn "dùng" vào các dự án "tương
        ứng" trong solution của bạn (thường là các dự án `.Domain.Shared`, `.Application`, `.Web`, v.v.).
    2.  **"Thêm" Module Vào "Dependencies":** "Thêm" module vào **"dependencies"** của module class (trong file `.cs`
        của module) bằng cách "sử dụng" attribute **`[DependsOn(...)]`**.

        ```csharp
        // MyModule.cs (Module Class)

        using Volo.Abp.Identity; // Namespace của Identity Module
        using Volo.Abp.Modularity;
        using Volo.Abp.TenantManagement;

        [DependsOn(
            typeof(AbpIdentityModule), // "Thêm" AbpIdentityModule vào dependencies
            typeof(AbpTenantManagementModule) // Thêm 1 module khác
        )]
        public class MyModule : AbpModule
        {
            // ...
        }
        ```

    3.  **"Cấu hình" Module (nếu cần):** Một số modules có thể "yêu cầu" bạn "thực hiện" các bước "cấu hình" "bổ sung"
        (ví dụ: "thêm" các "dòng code" vào file `Startup.cs` hoặc file module class, "cấu hình" các "options" của
        module, v.v.). "Tham khảo" **tài liệu** của module để biết thêm chi tiết.

**4.3. "Tạo" Custom Module (Mô-đun "Tự Tạo") - " 'Nặn' " "Viên Gạch" "Theo Ý Muốn" - " 'Đóng Gói' " "Tính Năng" "
Riêng"**

- **Custom Module (Mô-đun "Tự Tạo") - " 'Mở Rộng' " "Sức Mạnh" ABP Framework:**

    - Ngoài việc "sử dụng" các "pre-built modules" của ABP Framework, bạn có thể **"tạo" custom modules** (mô-đun "tự
      tạo") để **"đóng gói"** các **"tính năng" "riêng"** của ứng dụng hoặc để **"tái sử dụng"** các "thành phần" trong
      **"nhiều dự án"** khác nhau.
    - Custom modules "giúp" bạn **"tổ chức" code** một cách **"gọn gàng"**, **"dễ quản lý"**, và **"tăng" "tính 'tái sử
      dụng' "** code.

- **"Các Bước" "Tạo" Custom Module Trong ABP Framework:**

    1.  **"Tạo" Dự Án Class Library (.NET):** "Tạo" một dự án **Class Library (.NET)** mới trong solution của bạn. "Đặt
        tên" dự án theo "quy ước" của ABP Framework (ví dụ: `YourProjectName.YourModuleName`).
    2.  **"Cài Đặt" NuGet Packages:** "Cài đặt" các **NuGet packages** cần thiết cho module của bạn (ví dụ:
        `Volo.Abp.Module`, các pre-built modules mà module của bạn "phụ thuộc").
    3.  **"Tạo" Module Class:** "Tạo" một **"lớp"** (class) trong dự án Class Library, "kế thừa" từ lớp **`AbpModule`** và
        "đặt tên" lớp theo "quy ước" (ví dụ: `YourModuleNameModule`).
    4.  **"Định Nghĩa" Module Dependencies:** "Sử dụng" attribute **`[DependsOn(...)]`** để "khai báo" các modules mà
        module của bạn "phụ thuộc" (nếu có).
    5.  **"Cấu Hình" Module:** "Ghi đè" (override) các "phương thức" của lớp `AbpModule` (ví dụ: `ConfigureServices`,
        `OnApplicationInitialization`) để "đăng ký" các services của module, "cấu hình" các options, và "thực hiện"
        các "tác vụ" "khởi tạo" module (nếu cần).
    6.  **"Thêm" Các "Thành Phần" Của Module:** "Thêm" các "thành phần" của module (ví dụ: entities, domain services,
        application services, DTOs, controllers, views, localization resources, v.v.) vào các thư mục "tương ứng"
        trong dự án Class Library.
    7. **"Tham Chiếu" (Reference) Module:** "Thêm" "tham chiếu" (project reference) đến dự án Class Library của module
       vào các dự án "khác" trong solution mà bạn muốn "sử dụng" module (ví dụ: `.Web`, `.Application`, `.HttpApi`,
       v.v.).
    8. **"Sử Dụng" Module:** "Sử dụng" các "thành phần" của module (ví dụ: services, entities) trong các dự án "khác"
       như bình thường.

- **"Ví Dụ" "Tạo" Custom Module (C#):**
    *   **Tạo project**: Tạo project class library, ví dụ: `MyProject.MyModule`
    *   **Cài các nuget packages**:
        ```
        Volo.Abp.Module
        ```
    *   **Tạo class kế thừa `AbpModule`:**

    ```csharp
    // MyModule.cs (Module Class)

    using Volo.Abp.Modularity;

    namespace MyProject.MyModule
    {
        [DependsOn(
            typeof(AbpIdentityModule) // Ví dụ: phụ thuộc vào AbpIdentityModule
        )]
        public class MyModule : AbpModule
        {
            public override void ConfigureServices(ServiceConfigurationContext context)
            {
                // Đăng ký các services của module vào DI container
                // context.Services.AddTransient<IMyService, MyService>();
            }
        }
    }
    ```

    *   **Thêm các thành phần vào module** (entities, services,...)
    *   **Tham chiếu và sử dụng module** trong các project khác.

**Tổng Kết Chương 4:**

-   Bạn đã "khám phá" **hệ thống mô-đun** (module system) của ABP Framework, " 'linh hồn' " của kiến trúc ABP Framework.
    -   "Hiểu" **Module là gì** ("đơn vị" "độc lập", "tự đóng gói", "tái sử dụng", "chứa" các "thành phần" "liên quan"
        đến một "chức năng" "cụ thể").
    -   "Nắm vững" các **"lợi ích"** của việc "sử dụng" modules (tổ chức code, tái sử dụng code, giảm coupling, dễ
        thêm/xóa tính năng, hỗ trợ microservices, dễ phân chia công việc).
    -   "Khám phá" các **"pre-built modules"** (mô-đun "có sẵn") "quan trọng" của ABP Framework (Identity Module,
        Tenant Management Module, Setting Management Module, Audit Logging Module, v.v.) và "cách" "sử dụng" chúng.
    -   "Học cách" **"tạo" custom modules** (mô-đun "tự tạo") để "đóng gói" các "tính năng" "riêng" của ứng dụng hoặc "
        tái sử dụng" các "thành phần" trong "nhiều dự án".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 5: Domain-Driven Design (DDD) Với ABP Framework**. Chúng ta sẽ "tìm hiểu" các "khái
niệm" "cốt lõi" của **Domain-Driven Design (DDD)** và "cách" ABP Framework "hỗ trợ" "triển khai" DDD trong ứng dụng
của bạn.

Bạn có câu hỏi nào về ABP Modules này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành"
cùng bạn trên con đường "chinh phục" ABP Framework.

