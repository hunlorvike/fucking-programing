# Chương 4: Authentication và Authorization Trong ASP.NET Core - " 'Vũ Khí' " "Bảo Vệ" Web App .NET - " 'Tích Hợp' ", " 'Cấu Hình' ", " 'Vận Hành' " "Bảo Mật" Trong " 'Lòng' " .NET

Chào mừng bạn đến với **Chương 4: Authentication và Authorization Trong ASP.NET Core - " 'Vũ Khí' " "Bảo Vệ" Web App .NET**! Trong chương này, chúng ta sẽ "tổng kết" lại "kiến thức" về **Authentication** và **Authorization** và "xem xét" cách chúng được **"tích hợp"** và **"hoạt động"** trong **ASP.NET Core**, "tạo ra" " 'lá chắn' " "bảo vệ" ứng dụng web .NET của bạn. Chúng ta sẽ "đi sâu" vào **Authentication Middleware**, **Authorization Middleware**, cách **"cấu hình" Authentication Schemes và Handlers**, và **"cấu hình" Authorization Policies và Handlers** trong ASP.NET Core.

**Phần 4: Authentication và Authorization Trong ASP.NET Core - " 'Vũ Khí' " "Bảo Vệ" Web App .NET**

**4.1. Authentication Middleware Trong ASP.NET Core - " 'Lớp Phòng Thủ' " "Đầu Tiên" Cho Request - " 'Cánh Cửa' " "Xác Thực" Mọi "Lượt Truy Cập"**

-   **Authentication Middleware - " 'Gác Cửa' " "Xác Thực" "Mọi Request" Đến Ứng Dụng:**

    -   **Middleware** trong ASP.NET Core là "thành phần" "phần mềm" được "lắp ghép" vào **"pipeline" "xử lý" HTTP request**. "Mỗi request" HTTP đến ứng dụng web ASP.NET Core sẽ "đi qua" **"pipeline" "middleware"**. Middleware có thể "thực hiện" các "hành động" "trước", "trong", và "sau" khi request được "xử lý" bởi Controller Actions hoặc Razor Pages.
    -   **Authentication Middleware** là một "middleware" **"quan trọng"** trong "pipeline" "middleware". "Nằm ở" **"vị trí" "đầu tiên"** (hoặc gần "đầu tiên") trong "pipeline". "Chịu trách nhiệm" **"xác thực" "danh tính" "người dùng"** cho **"mỗi request"** HTTP đến ứng dụng. "Thiết lập" **`HttpContext.User`** (đối tượng `ClaimsPrincipal`) cho request, "đại diện" cho "danh tính" "người dùng" "đã xác thực" (nếu "xác thực thành công"). Nếu "xác thực thất bại", Authentication Middleware có thể "từ chối" request hoặc "chuyển tiếp" request đến middleware "tiếp theo".

-   **"Cách Hoạt Động" Của Authentication Middleware:**

    1.  **Request Đến Middleware Pipeline:** HTTP request đến ứng dụng web ASP.NET Core và "đi vào" **"middleware pipeline"**.
    2.  **Authentication Middleware Được Gọi:** Authentication Middleware là một trong các middleware trong pipeline, và nó được "gọi" để "xử lý" request.
    3.  **Authentication Schemes và Handlers Được Sử Dụng:** Authentication Middleware được "cấu hình" với **"một hoặc nhiều" "Authentication Schemes"**. "Mỗi Authentication Scheme" "liên kết" với **"một" "Authentication Handler"**. Authentication Middleware "lặp" qua "các Authentication Schemes" và "gọi" **`AuthenticateAsync()`** "của" **"Authentication Handler"** "tương ứng" cho "mỗi scheme".
    4.  **Authentication Handler "Xác Thực" Request:** "Mỗi Authentication Handler" "thực hiện" quá trình **"xác thực"** (authentication) "theo" **"phương thức" Authentication** mà nó "hỗ trợ" (ví dụ: cookies, JWT, OAuth 2.0, v.v.). "Authentication Handler" "kiểm tra" "thông tin" "xác thực" trong request (ví dụ: cookie, JWT token trong header, v.v.) và "xác minh" "danh tính" người dùng.
    5.  **Authentication Result (Kết Quả Xác Thực):** "Authentication Handler" "trả về" **`AuthenticationResult`** (kết quả xác thực). `AuthenticationResult` có thể là:
        -   **`AuthenticationResult.Success(AuthenticationTicket)`:** "Xác thực thành công". `AuthenticationTicket` chứa **`ClaimsPrincipal`** (User Identity) và **`AuthenticationScheme`**. Authentication Middleware "thiết lập" `HttpContext.User = AuthenticationTicket.Principal`.
        -   **`AuthenticationResult.Fail(...)`:** "Xác thực thất bại". Authentication Middleware có thể "tiếp tục" "xử lý" các "Authentication Schemes" khác hoặc "chuyển tiếp" request đến middleware "tiếp theo".
        -   **`AuthenticationResult.NoResult()`:** "Authentication Handler" "không cố gắng" "xác thực" request (ví dụ: không có "thông tin" "xác thực" "phù hợp" trong request). Authentication Middleware "tiếp tục" "xử lý" các "Authentication Schemes" khác.
    6.  **HttpContext.User Được Thiết Lập:** Nếu "có ít nhất một" "Authentication Handler" "trả về" `AuthenticationResult.Success()`, Authentication Middleware sẽ **"thiết lập" `HttpContext.User`** với `ClaimsPrincipal` từ `AuthenticationTicket`. `HttpContext.User` sẽ được "sử dụng" trong các middleware "tiếp theo" và trong Controller Actions/Razor Pages để "truy cập" "thông tin" "người dùng" "đã xác thực".
    7.  **Request Được Chuyển Tiếp Đến Middleware Tiếp Theo:** Authentication Middleware "chuyển tiếp" request đến middleware "tiếp theo" trong "pipeline".

-   **"Đăng Ký" Authentication Middleware Trong `Startup.cs`:**

    ```csharp
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme) // Đăng ký Authentication Service
            .AddJwtBearer(JwtBearerDefaults.AuthenticationScheme, options => { // Cấu hình JWT Bearer Authentication Scheme
                options.Authority = "https://localhost:5001"; // Authority Server (ví dụ: Identity Server)
                options.Audience = "api1"; // Audience (API name)
                options.RequireHttpsMetadata = false;
            });

        // ... các service khác ...
    }

    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        // ... các middleware khác ...

        app.UseAuthentication(); // Thêm Authentication Middleware vào pipeline

        app.UseAuthorization(); // Thêm Authorization Middleware vào pipeline (thường sau Authentication Middleware)

        app.UseEndpoints(endpoints => { ... });
    }
    ```

**4.2. Authorization Middleware Trong ASP.NET Core - " 'Trạm Kiểm Soát' " "Quyền Truy Cập" Tài Nguyên - " 'Phân Quyền' " Sau " 'Xác Thực' "**

-   **Authorization Middleware - " 'Kiểm Soát' " "Quyền Truy Cập" Sau Khi " 'Xác Thực' ":**

    -   **Authorization Middleware** là middleware "tiếp theo" trong "pipeline" "middleware" (thường **"sau" Authentication Middleware**). "Chịu trách nhiệm" **"ủy quyền"** (authorization) - "kiểm tra" xem "người dùng" "đã xác thực" (authenticated user) có **" 'quyền' "** (permission) **"truy cập"** vào "tài nguyên" được "yêu cầu" hay không. "Thực thi" **"Authorization Policies"** (chính sách phân quyền) đã được "định nghĩa" trong ứng dụng. Nếu "ủy quyền thành công", Authorization Middleware "chuyển tiếp" request đến middleware "tiếp theo" (thường là Endpoint Middleware để "xử lý" request bởi Controller Action/Razor Page). Nếu "ủy quyền thất bại", Authorization Middleware "từ chối" request và "trả về" **"lỗi" "ủy quyền"** (ví dụ: HTTP 403 Forbidden).

-   **"Cách Hoạt Động" Của Authorization Middleware:**

    1.  **Request Đến Authorization Middleware:** Sau khi "đi qua" Authentication Middleware (và có thể đã "thiết lập" `HttpContext.User`), request "đi đến" **Authorization Middleware**.
    2.  **Authorization Middleware Được Gọi:** Authorization Middleware được "gọi" để "xử lý" request.
    3.  **Endpoint Routing (Định Tuyến Endpoint):** Authorization Middleware "kiểm tra" **"Endpoint"** của request (thường là Controller Action hoặc Razor Page). "Endpoint" có thể có **"metadata" "ủy quyền"** (ví dụ: `[Authorize]` attribute).
    4.  **Find Authorization Policies (Tìm Chính Sách Phân Quyền):** Authorization Middleware "tìm" **"Authorization Policies"** "áp dụng" cho "Endpoint". "Policies" có thể được "chỉ định" bằng `[Authorize]` attribute (ví dụ: `[Authorize]`, `[Authorize(Policy = "...") ]`, `[Authorize(Roles = "...") ]`, `[Authorize(Claims = "...") ]`). Nếu "không có" `[Authorize]` attribute, Authorization Middleware "cho phép" "truy cập" (mặc định).
    5.  **Authorization Service Được Gọi:** Authorization Middleware "gọi" **`IAuthorizationService.AuthorizeAsync(HttpContext.User, resource, policy)`** để "thực hiện" quá trình **"ủy quyền"**.
        -   **`HttpContext.User`:** "User Identity" (đối tượng `ClaimsPrincipal`) từ `HttpContext`.
        -   **`resource`:** "Tài nguyên" được "truy cập" (tùy chọn). Thường là **"Endpoint"** (Controller Action, Razor Page). Có thể là "dữ liệu" "cụ thể" (ví dụ: "bài viết" cần "sửa" trong "chính sách" "EditOwnArticlePolicy").
        -   **`policy`:** **"Authorization Policy"** được "chỉ định" (ví dụ: "RequireAdminRole").
    6.  **Authorization Service "Đánh Giá" Policies và Requirements:** `IAuthorizationService` (thông qua `AuthorizationPolicyEvaluator`) "đánh giá" **"Authorization Policy"** và **"Authorization Requirements"** trong "policy" bằng cách "gọi" **"Authorization Handlers"**.
    7.  **Authorization Result (Kết Quả Ủy Quyền):** `IAuthorizationService.AuthorizeAsync()` "trả về" **`AuthorizationResult`** (kết quả ủy quyền). `AuthorizationResult` có thể là:
        -   **`AuthorizationResult.Success()`:** "Ủy quyền thành công". Authorization Middleware "chuyển tiếp" request đến middleware "tiếp theo".
        -   **`AuthorizationResult.Failed()`:** "Ủy quyền thất bại". Authorization Middleware "từ chối" request và "trả về" **"lỗi" "ủy quyền"** (HTTP 403 Forbidden).
    8.  **Access Granted/Denied (Truy Cập Được Cho Phép/Từ Chối):** Dựa trên `AuthorizationResult`, Authorization Middleware "cho phép" hoặc "từ chối" "truy cập" vào "tài nguyên".

-   **"Đăng Ký" Authorization Middleware Trong `Startup.cs`:**

    ```csharp
    public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
    {
        // ... các middleware khác ...

        app.UseAuthentication(); // Thêm Authentication Middleware vào pipeline

        app.UseAuthorization(); // Thêm Authorization Middleware vào pipeline (thường sau Authentication Middleware)

        app.UseEndpoints(endpoints => { ... });
    }
    ```

**4.3. "Cấu Hình" Authentication Schemes và Handlers - " 'Chọn 'Chiến Binh' " "Xác Thực" Phù Hợp" - " 'Vũ Trang' " Ứng Dụng Với " 'Phương Thức' " "Xác Thực" Mong Muốn**

-   **Authentication Schemes và Handlers - " 'Bộ Sưu Tập' " "Phương Thức" "Xác Thực":**

    -   **Authentication Schemes** (lược đồ xác thực) là "tên" "định danh" cho **"một 'phương thức' " Authentication** (ví dụ: "Cookies", "JwtBearer", "OAuth", "OpenIdConnect", v.v.). "Mỗi Authentication Scheme" "liên kết" với **"một" "Authentication Handler"** (trình xử lý xác thực).
    -   **Authentication Handlers** (trình xử lý xác thực) là các lớp (classes) **"implement" interface `AuthenticationHandler<TOptions>`**. "Mỗi Authentication Handler" "chịu trách nhiệm" "thực hiện" quá trình **"xác thực"** (authentication) "theo" **"một 'phương thức' " Authentication** "cụ thể" (ví dụ: `CookieAuthenticationHandler` cho Cookies Authentication, `JwtBearerHandler` cho JWT Bearer Authentication, v.v.).

-   **"Cấu Hình" Authentication Schemes và Handlers Trong `Startup.cs`:**

    ```csharp
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddAuthentication(defaultScheme: CookieAuthenticationDefaults.AuthenticationScheme) // Đăng ký Authentication Service, set default scheme
            .AddCookie(CookieAuthenticationDefaults.AuthenticationScheme, options => { // Cấu hình Cookies Authentication Scheme
                options.LoginPath = "/Account/Login"; // Đường dẫn trang đăng nhập
                options.AccessDeniedPath = "/Account/AccessDenied"; // Đường dẫn trang từ chối truy cập
            })
            .AddJwtBearer(JwtBearerDefaults.AuthenticationScheme, options => { // Cấu hình JWT Bearer Authentication Scheme
                options.Authority = "https://localhost:5001"; // Authority Server
                options.Audience = "api1";
                options.RequireHttpsMetadata = false;
            })
            .AddOpenIdConnect("oidc", options => { // Cấu hình OpenID Connect Authentication Scheme
                options.Authority = "https://localhost:5001"; // Authority Server
                options.ClientId = "mvc";
                options.ClientSecret = "secret";
                options.ResponseType = "code";
                options.Scope.Add("openid");
                options.Scope.Add("profile");
                options.SaveTokens = true;
                options.RequireHttpsMetadata = false;
            });

        // ... các service khác ...
    }
    ```

    -   **`services.AddAuthentication(defaultScheme: ...)`:** "Đăng ký" **Authentication Service** vào DI container. "Tham số" `defaultScheme` "chỉ định" **"Authentication Scheme" "mặc định"** được "sử dụng" khi **"không có" "scheme" "cụ thể"** được "chỉ định" (ví dụ: khi "dùng" `[Authorize]` attribute "không tham số"). Nếu không "chỉ định" `defaultScheme`, "scheme" "đầu tiên" được "đăng ký" sẽ được "sử dụng" làm "mặc định".
    -   **`.AddCookie(CookieAuthenticationDefaults.AuthenticationScheme, options => { ... })`:** "Đăng ký" và "cấu hình" **Cookies Authentication Scheme**. `CookieAuthenticationDefaults.AuthenticationScheme` là "tên" "scheme" "chuẩn" cho Cookies Authentication ("Cookies"). `options` là đối tượng `CookieAuthenticationOptions` để "cấu hình" Cookies Authentication Handler (ví dụ: `LoginPath`, `AccessDeniedPath`, `CookieName`, `ExpireTimeSpan`, v.v.).
    -   **`.AddJwtBearer(JwtBearerDefaults.AuthenticationScheme, options => { ... })`:** "Đăng ký" và "cấu hình" **JWT Bearer Authentication Scheme**. `JwtBearerDefaults.AuthenticationScheme` là "tên" "scheme" "chuẩn" cho JWT Bearer Authentication ("Bearer"). `options` là đối tượng `JwtBearerOptions` để "cấu hình" JwtBearerHandler (ví dụ: `Authority`, `Audience`, `TokenValidationParameters`, v.v.).
    -   **`.AddOpenIdConnect("oidc", options => { ... })`:** "Đăng ký" và "cấu hình" **OpenID Connect Authentication Scheme**. "Tên" "scheme" "tùy chỉnh" ("oidc"). `options` là đối tượng `OpenIdConnectOptions` để "cấu hình" OpenIdConnectHandler (ví dụ: `Authority`, `ClientId`, `ClientSecret`, `ResponseType`, `Scope`, v.v.).

-   **"Chọn" Authentication Scheme Trong Code:**

    -   **`[Authorize]` attribute "không tham số"**: "Sử dụng" **"Authentication Scheme" "mặc định"** (được "cấu hình" trong `AddAuthentication(defaultScheme: ...)`).
    -   **`[Authorize(AuthenticationSchemes = "Scheme1,Scheme2")]` attribute**: "Chỉ định" **"danh sách" "Authentication Schemes"** được "sử dụng" cho "ủy quyền". Authentication Middleware sẽ "thử" "xác thực" bằng "tất cả" "schemes" "được chỉ định" và "chọn" "scheme" "thành công" "đầu tiên".
    -   **`HttpContext.SignInAsync(scheme, user, properties)`**: "Đăng nhập" người dùng bằng **"Authentication Scheme" "cụ thể"** (`scheme`). "Sử dụng" trong "code" "đăng nhập" (ví dụ: Controller Action "đăng nhập").
    -   **`HttpContext.AuthenticateAsync(scheme)`**: "Xác thực" request bằng **"Authentication Scheme" "cụ thể"**. "Sử dụng" để "kiểm tra" "xác thực" bằng "scheme" "cụ thể" (ví dụ: trong "Authorization Handlers").
    -   **`HttpContext.ChallengeAsync(scheme)`**: "Gửi" "response 'thử thách' " (challenge response) cho client để "bắt đầu" quá trình "xác thực" bằng **"Authentication Scheme" "cụ thể"**. "Sử dụng" khi "ủy quyền thất bại" và "muốn" "chuyển hướng" người dùng đến trang "đăng nhập" hoặc "bắt đầu" OAuth 2.0 flow, v.v.
    -   **`HttpContext.SignOutAsync(scheme)`**: "Đăng xuất" người dùng bằng **"Authentication Scheme" "cụ thể"**. "Sử dụng" trong "code" "đăng xuất" (ví dụ: Controller Action "đăng xuất").

**4.4. "Cấu Hình" Authorization Policies và Handlers - " 'Xây Dựng' " " 'Hệ Thống Luật Lệ' " "Phân Quyền" - " 'Viết' " "Chính Sách", " 'Tạo' " "Trình Xử Lý", " 'Thiết Lập' " "Quyền Hạn"**

-   **Authorization Policies và Handlers - " 'Nền Tảng' " Của "Policy-Based Authorization":**

    -   **Authorization Policies** (chính sách phân quyền) là " 'luật lệ' " "phân quyền" của ứng dụng. "Được 'định nghĩa' " bằng code, "bao gồm" **"danh sách" "Authorization Requirements"**.
    -   **Authorization Handlers** (trình xử lý ủy quyền) là các lớp (classes) "chịu trách nhiệm" **"đánh giá"** (evaluate) **"Authorization Requirements"** và "quyết định" "ủy quyền".

-   **"Cấu Hình" Authorization Policies và Handlers Trong `Startup.cs`:**

    ```csharp
    public void ConfigureServices(IServiceCollection services)
    {
        services.AddAuthorization(options => { // Đăng ký Authorization Service và cấu hình Policies
            options.AddPolicy("RequireAdminRole", policy => // Định nghĩa Policy "RequireAdminRole"
                policy.RequireRole("Admin")); // Yêu cầu Role "Admin" (sử dụng RolesAuthorizationRequirement)

            options.AddPolicy("EditOwnArticlePolicy", policy => { // Định nghĩa Policy "EditOwnArticlePolicy"
                policy.RequireRole("Editor"); // Yêu cầu Role "Editor"
                policy.AddRequirements(new EditOwnArticleRequirement()); // Thêm Custom Requirement "EditOwnArticleRequirement"
            });

            options.AddPolicy("VIPAccessPolicy", policy => // Định nghĩa Policy "VIPAccessPolicy"
                policy.RequireClaim("level_thanh_vien", "Vàng", "Kim Cương")); // Yêu cầu Claim "level_thanh_vien" có giá trị "Vàng" hoặc "Kim Cương" (sử dụng ClaimsAuthorizationRequirement)

            options.AddPolicy("CustomPolicy", policy => // Định nghĩa Policy "CustomPolicy"
                policy.Requirements.Add(new CustomRequirement("value1", "value2"))); // Thêm Custom Requirement "CustomRequirement" (custom logic)
        });

        services.AddScoped<IAuthorizationHandler, EditOwnArticleHandler>(); // Đăng ký Custom Handler "EditOwnArticleHandler"
        services.AddScoped<IAuthorizationHandler, CustomAuthorizationHandler>(); // Đăng ký Custom Handler "CustomAuthorizationHandler"

        // ... các service khác ...
    }
    ```

    -   **`services.AddAuthorization(options => { ... })`:** "Đăng ký" **Authorization Service** vào DI container và "cấu hình" **Authorization Policies**.
    -   **`options.AddPolicy("PolicyName", policy => { ... })`:** "Định nghĩa" **"Authorization Policy"** với "tên" **"PolicyName"**. "Tham số" `policy` là đối tượng `AuthorizationPolicyBuilder` để "xây dựng" "chính sách".
    -   **`policy.RequireRole("Role1", "Role2", ...)`:** "Thêm" **`RolesAuthorizationRequirement`** vào "chính sách". "Yêu cầu" "người dùng" phải có **"một trong các" "vai trò" "được chỉ định"**.
    -   **`policy.RequireClaim("ClaimType", "ClaimValue1", "ClaimValue2", ...)`:** "Thêm" **`ClaimsAuthorizationRequirement`** vào "chính sách". "Yêu cầu" "người dùng" phải có **"claim" "được chỉ định"** (`ClaimType`) với **"một trong các" "giá trị" "được chỉ định"** (`ClaimValue`).
    -   **`policy.Requirements.Add(new CustomRequirement(...))`:** "Thêm" **"Custom Authorization Requirement"** vào "chính sách". "Yêu cầu" "người dùng" phải "đáp ứng" "Custom Requirement" (được "đánh giá" bởi "Custom Authorization Handler").
    -   **`services.AddScoped<IAuthorizationHandler, HandlerType>();`:** "Đăng ký" **"Authorization Handler"** (`HandlerType`) vào DI container. "Thường" "đăng ký" là **"scoped" service**. "Mỗi Authorization Handler" được "đăng ký" "cho" **"một hoặc nhiều" "Authorization Requirements"**.

-   **"Tạo" Custom Authorization Requirement và Handler:**

    ```csharp
    // Custom Authorization Requirement
    public class EditOwnArticleRequirement : IAuthorizationRequirement
    {
    }

    // Custom Authorization Handler
    public class EditOwnArticleHandler : AuthorizationHandler<EditOwnArticleRequirement>
    {
        protected override Task HandleRequirementAsync(AuthorizationHandlerContext context, EditOwnArticleRequirement requirement)
        {
            if (!context.User.IsInRole("Editor")) // Kiểm tra Role "Editor"
            {
                return Task.CompletedTask; // Không phải Editor, ủy quyền thất bại (mặc định)
            }

            // ... Logic kiểm tra "người dùng" có phải là "tác giả" của "bài viết" hay không ...
            // (ví dụ: lấy "ID bài viết" từ "resource" (context.Resource), "lấy" "UserID" từ "User Identity" (context.User), "kiểm tra" database)

            if (isAuthor) // Nếu là "tác giả"
            {
                context.Succeed(requirement); // Ủy quyền thành công
            }

            return Task.CompletedTask; // Nếu không phải "tác giả", ủy quyền thất bại (mặc định)
        }
    }
    ```

**Tổng Kết Chương 4:**

-   Bạn đã "khám phá" cách Authentication và Authorization được "tích hợp" và "hoạt động" trong ASP.NET Core.
    -   "Hiểu" vai trò của **Authentication Middleware** ("lớp phòng thủ" "đầu tiên" - "xác thực" "mọi request").
    -   "Nắm bắt" chức năng của **Authorization Middleware** ("trạm kiểm soát" "quyền truy cập" - "phân quyền" sau "xác thực").
    -   Biết cách **"cấu hình" Authentication Schemes và Handlers** ("chọn 'chiến binh' " "xác thực" "phù hợp").
    -   "Học" cách **"cấu hình" Authorization Policies và Handlers** ("xây dựng 'hệ thống luật lệ' " "phân quyền").

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 5: "Triển Khai" Authentication và Authorization - " 'Áp Dụng' " "Bảo Mật" Vào Ứng Dụng Thực Tế**. Chúng ta sẽ "đi sâu" vào các "khía cạnh" "thực tế" của việc "triển khai" Authentication và Authorization trong ứng dụng web, bao gồm "lưu trữ" "thông tin người dùng" "an toàn", "xử lý" "lỗ hổng bảo mật", "tích hợp" với "bên thứ ba", và "giám sát" "an ninh" ứng dụng.

Bạn có câu hỏi nào về Authentication và Authorization trong ASP.NET Core này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" "bảo mật" ứng dụng web.
