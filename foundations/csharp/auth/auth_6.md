# Chương 6: "Tuyệt Chiêu" Authentication và Authorization Nâng Cao - " 'Luyện Công Phu' " "Bảo Mật" Ứng Dụng - " 'Nâng Tầm' " "Kỹ Năng", " 'Mở Rộng' " "Giới Hạn", " 'Chinh Phục' " "Đỉnh Cao" "Bảo Mật"

Chào mừng bạn đến với **Chương 6: "Tuyệt Chiêu" Authentication và Authorization Nâng Cao - " 'Luyện Công Phu' " "Bảo Mật" Ứng Dụng**! Sau khi đã "xây dựng" "nền tảng" "vững chắc" về Authentication và Authorization "cơ bản" và "thực tế", chúng ta sẽ "bước lên" **"tầm cao mới"**, "khám phá" các **"kỹ thuật" Authentication và Authorization "nâng cao"** để **" 'nâng cấp' " "hệ thống" "bảo mật"** của bạn "lên một 'đẳng cấp' " "khác biệt". Chúng ta sẽ "đi sâu" vào **Role-Based Authorization "Nâng Cao"**, **Policy-Based Authorization "Nâng Cao"**, **Claims Transformation**, và **Custom Authorization Handlers**.

**Phần 6: "Tuyệt Chiêu" Authentication và Authorization Nâng Cao - " 'Luyện Công Phu' " "Bảo Mật" Ứng Dụng**

**6.1. Role-Based Authorization "Nâng Cao" - " 'Phân Quyền' " "Chi Tiết" và " 'Linh Hoạt' " Hơn - " 'Vượt Xa' " "Giới Hạn" "Vai Trò" "Cứng Nhắc"**

-   **Role-Based Authorization "Nâng Cao" - " 'Mở Rộng' " "Khả Năng" "Phân Quyền" "Vai Trò":**

    -   **Role-Based Authorization (RBAC) "cơ bản"** (chương 3) "phân quyền" "dựa trên" **"vai trò"** "cứng nhắc" (static roles). "Mỗi người dùng" được "gán" vào **"một hoặc nhiều" "vai trò"** (ví dụ: "Admin", "Editor", "Viewer", v.v.). "Quyền truy cập" được "quyết định" bởi **"vai trò"**. RBAC "cơ bản" "đơn giản" và "dễ hiểu", nhưng có thể **"kém 'linh hoạt' "** khi "yêu cầu" "phân quyền" trở nên **"phức tạp"** và **"chi tiết"** hơn.
    -   **Role-Based Authorization "nâng cao"** "mở rộng" "khả năng" "phân quyền" "vai trò" bằng cách "thêm" **"ngữ cảnh"** (context) và **"điều kiện"** (conditions) vào "quy tắc" "phân quyền" "vai trò". "Cho phép" "phân quyền" "chi tiết" hơn và "linh hoạt" hơn, "dựa trên" **"vai trò" "kết hợp" với "các 'tiêu chí' " khác**.

-   **"Các 'Kỹ Thuật' " Role-Based Authorization "Nâng Cao":**

    -   **"Role Hierarchy" (Phân Cấp Vai Trò):** "Tổ chức" "vai trò" thành **"cây phân cấp"** (hierarchy). "Vai trò" "cao hơn" trong "cây phân cấp" "thừa kế" "quyền hạn" của "vai trò" "thấp hơn". "Ví dụ": "vai trò" "SuperAdmin" "thừa kế" "quyền hạn" của "vai trò" "Admin", "Editor", "Viewer", v.v. "Giảm" "sự trùng lặp" "quyền hạn" giữa các "vai trò" và "dễ dàng" "quản lý" "vai trò" "phức tạp".
    -   **"Scoped Roles" (Vai Trò Phạm Vi):** "Gán" "vai trò" cho "người dùng" trong **"phạm vi"** (scope) "cụ thể" (ví dụ: "vai trò" "Admin" **"cho 'dự án' " X**, "vai trò" "Editor" **"cho 'danh mục' " Y**, v.v.). "Phân quyền" "chi tiết" hơn "dựa trên" "ngữ cảnh" "tài nguyên". "Ví dụ": "người dùng" A có "vai trò" "Admin" **"trong 'dự án' " "ProjectA"**, nhưng chỉ có "vai trò" "Viewer" **"trong 'dự án' " "ProjectB"**. "Quyền hạn" của "vai trò" "Admin" chỉ "áp dụng" trong "phạm vi" "ProjectA".
    -   **"Dynamic Roles" (Vai Trò Động):** "Xác định" "vai trò" của "người dùng" **"một cách 'động' "** (dynamically) **"dựa trên" "ngữ cảnh"** (context) "hiện tại" (ví dụ: "thời gian", "địa điểm", "trạng thái" "tài nguyên", "thuộc tính" "người dùng", v.v.). "Vai trò" "không còn" là "tĩnh" và "cứng nhắc", mà "thay đổi" "dựa trên" "điều kiện" "cụ thể". "Ví dụ": "người dùng" có "vai trò" "Approver" (người phê duyệt) **"trong 'phiên' " "phê duyệt" "đơn hàng"**, nhưng không có "vai trò" "Approver" "ngoài" "phiên" "phê duyệt" "đơn hàng".
    -   **"Conditional Roles" (Vai Trò Có Điều Kiện):** "Gán" "vai trò" cho "người dùng" **"dựa trên" "điều kiện"** (condition) "cụ thể". "Vai trò" chỉ "có hiệu lực" khi "điều kiện" "được thỏa mãn". "Ví dụ": "vai trò" "VIP Member" chỉ "được gán" cho "người dùng" có **`level_thành_viên >= "Vàng"`** và "thời gian" "gia nhập" "hệ thống" **`> 1 năm`**. "Quyền hạn" của "vai trò" "VIP Member" chỉ "áp dụng" khi "người dùng" "đáp ứng" "cả hai" "điều kiện".
    -   **"Role-Based Access Control with Attributes" (RBAC với Thuộc Tính):** "Kết hợp" RBAC với **Attribute-Based Access Control (ABAC)**. "Phân quyền" "dựa trên" **"vai trò" "kết hợp" với "thuộc tính"** (attributes) của "người dùng", "tài nguyên", "hành động", và "môi trường". "Ví dụ": "cho phép" "Editor" "sửa bài viết" **"của chính mình"** (vai trò "Editor" + thuộc tính "người tạo bài viết" = "người dùng hiện tại"). "Tăng" "độ chi tiết" và "tính 'linh hoạt' " của "phân quyền" "vai trò".

-   **"Triển Khai" Role-Based Authorization "Nâng Cao" Trong ASP.NET Core:**

    -   **"Role Hierarchy":** "Tự" "quản lý" "cây phân cấp" "vai trò" trong database hoặc cấu hình. "Viết" "logic" "kiểm tra" "vai trò" "thừa kế" trong "Authorization Handlers" hoặc "custom authorization logic". ASP.NET Core Authorization System "không 'hỗ trợ' " "trực tiếp" "role hierarchy".
    -   **"Scoped Roles":** "Lưu trữ" "vai trò" và "phạm vi" (scope) trong database. "Viết" "logic" "kiểm tra" "vai trò" và "phạm vi" trong "Authorization Handlers" hoặc "custom authorization logic".
    -   **"Dynamic Roles":** "Viết" "logic" "xác định" "vai trò" "động" trong "Authorization Handlers" hoặc "custom authorization logic", "dựa trên" `AuthorizationHandlerContext` (ngữ cảnh trình xử lý ủy quyền) và các "nguồn" "thông tin" "khác" (database, cấu hình, APIs, v.v.).
    -   **"Conditional Roles":** "Viết" "logic" "kiểm tra" "điều kiện" "gán" "vai trò" trong "Authorization Handlers" hoặc "custom authorization logic".
    -   **"RBAC with Attributes":** "Sử dụng" **Policy-Based Authorization** (chương 3) để "kết hợp" "vai trò" và "thuộc tính" trong "chính sách" "phân quyền". "Ví dụ": "chính sách" "EditOwnArticlePolicy" (chương 3) là một "ví dụ" của RBAC with Attributes (vai trò "Editor" + điều kiện "là tác giả bài viết").

**6.2. Policy-Based Authorization "Nâng Cao" - " 'Luật Lệ' " "Phức Tạp" và " 'Tùy Biến' " Cao - " 'Vượt Qua' " "Giới Hạn" "Chính Sách" "Đơn Giản"**

-   **Policy-Based Authorization "Nâng Cao" - " 'Giải Phóng' " "Sức Mạnh" "Tùy Biến" "Phân Quyền":**

    -   **Policy-Based Authorization "cơ bản"** (chương 3) "cho phép" "định nghĩa" "Authorization Policies" (chính sách phân quyền) "tùy chỉnh" bằng code, "dựa trên" "Authorization Requirements" (yêu cầu ủy quyền) và "Authorization Handlers" (trình xử lý ủy quyền). Policy-Based Authorization "cơ bản" "linh hoạt" hơn RBAC và Claims-Based Authorization, nhưng vẫn có thể **"bị 'giới hạn' "** khi "yêu cầu" "phân quyền" trở nên **"cực kỳ" "phức tạp"** và **"tùy biến" "cao"**.
    -   **Policy-Based Authorization "nâng cao"** "mở rộng" "khả năng" "tùy biến" "chính sách" bằng cách "thêm" **"tính 'mô-đun' "**, **"tính 'tái sử dụng' "**, và **"tính 'mở rộng' "** vào "chính sách" "phân quyền". "Cho phép" "xây dựng" các "chính sách" "phân quyền" **"phức tạp"**, **"tùy biến"**, và **"dễ 'quản lý' "** hơn.

-   **"Các 'Kỹ Thuật' " Policy-Based Authorization "Nâng Cao":**

    -   **"Policy Composition" (Kết Hợp Chính Sách):** "Kết hợp" **"nhiều" "Authorization Policies"** lại với nhau để "tạo ra" **"chính sách" "phức tạp" hơn**. "Ví dụ": "chính sách" "RequireAdminOrEditorRole" = "chính sách" "RequireAdminRole" **"OR"** "chính sách" "RequireEditorRole". "Tái sử dụng" "chính sách" "nhỏ" và "đơn giản" để "xây dựng" "chính sách" "lớn" và "phức tạp".
    -   **"Policy Inheritance" (Kế Thừa Chính Sách):** "Tạo" **"chính sách" "con"** (child policy) "thừa kế" **"chính sách" "cha"** (parent policy) và "thêm" "yêu cầu" "phân quyền" "riêng" cho "chính sách" "con". "Ví dụ": "chính sách" "AdminPanelPolicy" "thừa kế" "chính sách" "RequireAuthenticatedUserPolicy" (yêu cầu "xác thực") và "thêm" "yêu cầu" "vai trò" "Admin". "Giảm" "sự trùng lặp" "định nghĩa" "chính sách" và "tăng" "tính 'tái sử dụng' ".
    -   **"Policy Providers" "Tùy Chỉnh" (Custom Policy Providers):** "Implement" **`IAuthorizationPolicyProvider` interface** (chương 4) để **"cung cấp" "Authorization Policies" một cách "động"** và **"tùy biến"**. "Lấy" "chính sách" từ database, cấu hình, "tạo" "chính sách" "dựa trên" "ngữ cảnh", v.v. "Giải quyết" "vấn đề" "quản lý" "chính sách" "số lượng lớn" và "thay đổi" "thường xuyên".
    -   **"Policy Factories" (Nhà Máy Chính Sách):** "Tạo" **"factory classes"** (lớp nhà máy) để **"tạo ra" "Authorization Policies" "dựa trên" "tham số"** (parameters). "Ví dụ": `ArticlePolicyFactory.CreatePolicy(ArticleAction action)` "tạo ra" "Authorization Policy" cho "hành động" `action` trên "bài viết" (ví dụ: "ReadArticlePolicy", "EditArticlePolicy", "DeleteArticlePolicy"). "Tăng" "tính 'mô-đun' " và "tính 'tái sử dụng' " của "định nghĩa" "chính sách".
    -   **"Policy-Based Authorization with Attributes" (Policy-Based Authorization với Thuộc Tính):** "Kết hợp" Policy-Based Authorization với **Attribute-Based Access Control (ABAC)** (chương 3). "Định nghĩa" **"Authorization Policies" "dựa trên" "thuộc tính"** (attributes) của "người dùng", "tài nguyên", "hành động", và "môi trường". "Tận dụng" "sức mạnh" "linh hoạt" và "tùy biến" của ABAC trong "khuôn khổ" Policy-Based Authorization.

-   **"Triển Khai" Policy-Based Authorization "Nâng Cao" Trong ASP.NET Core:**

    -   **"Policy Composition":** "Sử dụng" **`policyBuilder.Combine(otherPolicy)`** (trong `AuthorizationPolicyBuilder`) để "kết hợp" "chính sách". "Hoặc" "định nghĩa" "Custom Authorization Requirement" và "Handler" để "thực hiện" "logic" "kết hợp" "chính sách".
    -   **"Policy Inheritance":** "Tạo" "chính sách" "con" "dựa trên" "chính sách" "cha" bằng cách "sao chép" "Authorization Requirements" từ "chính sách" "cha" và "thêm" "yêu cầu" "mới". "Hoặc" "sử dụng" "Policy Composition" để "kết hợp" "chính sách" "cha" và "chính sách" "con".
    -   **"Policy Providers" "Tùy Chỉnh":** "Implement" `IAuthorizationPolicyProvider` interface (chương 4) và "đăng ký" trong DI container.
    -   **"Policy Factories":** "Tạo" "factory classes" với "phương thức" `CreatePolicy(parameters)` trả về `AuthorizationPolicy`. "Gọi" "factory methods" để "lấy" "Authorization Policies" trong code (ví dụ: trong Controller Actions, Services, v.v.).
    -   **"Policy-Based Authorization with Attributes":** "Định nghĩa" "Custom Authorization Requirements" và "Handlers" để "kiểm tra" "thuộc tính" (attributes) trong `AuthorizationHandlerContext` (ngữ cảnh trình xử lý ủy quyền), `HttpContext`, hoặc "lấy" "thuộc tính" từ "resource" (ví dụ: "bài viết" cần "sửa"). "Xây dựng" "Authorization Policies" "dựa trên" "Custom Requirements".

**6.3. Claims Transformation - " 'Biến Hình' " Claims Để " 'Phù Hợp' " Với " 'Nhu Cầu' " Ứng Dụng - " 'Tùy Biến' " "Hồ Sơ" "Danh Tính"**

-   **Claims Transformation - " 'Biến Đổi' " "Claims" "Linh Hoạt" và " 'Tùy Chỉnh' ":**

    -   **Claims Transformation** (biến đổi claims) là quá trình **"thay đổi"**, **"bổ sung"**, hoặc **"xóa" "Claims"** trong **`ClaimsPrincipal`** (User Identity) của "người dùng" **"sau khi" "xác thực" (authentication) và "trước khi" "ủy quyền" (authorization)**. "Cho phép" **" 'tùy biến' " "hồ sơ" "danh tính"** của người dùng để "phù hợp" với **"nhu cầu" "phân quyền"** của ứng dụng.
    -   Claims Transformation "giúp" **"chuẩn hóa" "claims"**, **"enrich claims"** (bổ sung "thông tin" "mới" vào "claims"), và **"filter claims"** (loại bỏ "claims" "không cần thiết"). "Tăng" "tính 'linh hoạt' " và "tính 'mô-đun' " của "hệ thống" "claims-based authentication" và "authorization".

-   **"Các 'Kịch Bản' " Claims Transformation:**

    -   **"Claim Normalization" (Chuẩn Hóa Claims):** "Chuẩn hóa" "Claim Types" và "Claim Values" để "đảm bảo" "tính "nhất quán' " và "tính 'tương thích' " giữa các "Identity Providers" (IdPs) "khác nhau". "Ví dụ": "chuẩn hóa" "Claim Type" "emailaddress" (SAML) thành `ClaimTypes.Email` (.NET), "chuẩn hóa" "Claim Value" "User" (string) thành "User" (enum).
    -   **"Claim Enrichment" (Bổ Sung Claims):** "Bổ sung" "claims" "mới" vào "User Identity" "dựa trên" "thông tin" "có sẵn" (ví dụ: "lấy" "thông tin" "vai trò" từ database "dựa trên" "User ID" trong "claims", "tính toán" "level thành viên" "dựa trên" "thời gian" "gia nhập" và "số lượng" "đơn hàng"). "Làm giàu" "hồ sơ" "danh tính" người dùng với "thông tin" "phân quyền" "cần thiết".
    -   **"Claim Filtering" (Lọc Claims):** "Loại bỏ" "claims" "không cần thiết" hoặc "nhạy cảm" khỏi "User Identity" "trước khi" "truyền" đến ứng dụng. "Giảm thiểu" "lượng dữ liệu" "truyền tải" và "tăng cường" "bảo mật" ( "giảm" "nguy cơ" "lộ lọt" "dữ liệu").
    -   **"Claim Transformation Based on Context" (Biến Đổi Claims Dựa Trên Ngữ Cảnh):** "Biến đổi" "claims" **"dựa trên" "ngữ cảnh"** "hiện tại" (ví dụ: "thời gian", "địa điểm", "ứng dụng" "yêu cầu" "claims", v.v.). "Ví dụ": "thêm" "claim" `is_vip_customer = true` vào "User Identity" **"chỉ khi"** "người dùng" "truy cập" vào "ứng dụng" "VIP customer portal". "Phân quyền" "theo ngữ cảnh" "linh hoạt".

-   **"Triển Khai" Claims Transformation Trong ASP.NET Core:**

    -   **"Implement" `IClaimsTransformation` interface**. `IClaimsTransformation` interface có "phương thức" `TransformAsync(ClaimsPrincipal principal)`. "Phương thức" này được "gọi" bởi Authentication Middleware **"sau khi" "xác thực" "thành công"** và **"trước khi" `HttpContext.User` được "thiết lập"**. Bạn "viết code" trong `TransformAsync()` để **"thay đổi"**, **"bổ sung"**, hoặc **"xóa" "claims"** trong `principal` (đối tượng `ClaimsPrincipal` "đầu vào"). "Phương thức" `TransformAsync()` phải "trả về" `Task<ClaimsPrincipal>` ( `ClaimsPrincipal` "đã được biến đổi").
    -   **"Đăng ký" "implementation" của `IClaimsTransformation`** trong DI container (thường là "scoped" service).

    ```csharp
    public class AppClaimsTransformer : IClaimsTransformation
    {
        private readonly IUserRepository _userRepository; // Ví dụ: UserRepository để lấy thông tin người dùng từ database

        public AppClaimsTransformer(IUserRepository userRepository)
        {
            _userRepository = userRepository;
        }

        public async Task<ClaimsPrincipal> TransformAsync(ClaimsPrincipal principal)
        {
            if (!principal.Identity.IsAuthenticated) // Chỉ biến đổi claims cho người dùng "đã xác thực"
            {
                return principal;
            }

            var identity = principal.Identities.FirstOrDefault(); // Lấy ClaimsIdentity
            if (identity == null)
            {
                return principal;
            }

            var userIdClaim = identity.FindFirst(ClaimTypes.NameIdentifier); // Tìm Claim "User ID"
            if (userIdClaim == null || string.IsNullOrEmpty(userIdClaim.Value))
            {
                return principal;
            }

            var userId = userIdClaim.Value;

            var user = await _userRepository.GetUserByIdAsync(userId); // Lấy thông tin người dùng từ database

            if (user != null)
            {
                // Bổ sung Claim "level_thanh_vien" (ví dụ: lấy từ User Profile trong database)
                if (!string.IsNullOrEmpty(user.LevelThanhVien))
                {
                    identity.AddClaim(new Claim("level_thanh_vien", user.LevelThanhVien));
                }

                // Bổ sung Claim "phong_ban" (ví dụ: lấy từ User Profile trong database)
                if (!string.IsNullOrEmpty(user.PhongBan))
                {
                    identity.AddClaim(new Claim("phong_ban", user.PhongBan));
                }

                // ... bổ sung các Claims khác ...
            }

            return principal; // Trả về ClaimsPrincipal đã được biến đổi
        }
    }

    public void ConfigureServices(IServiceCollection services)
    {
        services.AddScoped<IClaimsTransformation, AppClaimsTransformer>(); // Đăng ký ClaimsTransformer vào DI container

        // ... các service khác ...
    }
    ```

**6.4. Custom Authorization Handlers - " 'Viết' " " 'Bộ Kiểm Soát' " "Quyền Truy Cập" "Riêng" - " 'Tự Do' " "Thiết Kế" "Logic" "Phân Quyền" "Phức Tạp"**

-   **Custom Authorization Handlers - " 'Công Cụ' " "Tối Thượng" Để "Tùy Biến" "Logic" "Phân Quyền":**

    -   **Custom Authorization Handlers** (trình xử lý ủy quyền tùy chỉnh) là "công cụ" **"mạnh mẽ"** và **"linh hoạt"** nhất trong ASP.NET Core Authorization System để **"tùy biến" "logic" "phân quyền" "phức tạp"** và **"đặc thù"** của ứng dụng. "Cho phép" bạn **"viết code" "riêng"** để **"kiểm tra" "quyền truy cập"** "dựa trên" **"bất kỳ" "điều kiện"** nào, "không bị" "giới hạn" bởi các "Authorization Requirements" "chuẩn" ( `RolesAuthorizationRequirement`, `ClaimsAuthorizationRequirement`, v.v.).
-   Custom Authorization Handlers "mở ra" **"khả năng" "phân quyền" "không giới hạn"**, "đáp ứng" các **"yêu cầu" "phân quyền" "khó khăn" nhất**.

-   **"Khi Nào Cần Dùng" Custom Authorization Handlers?**

    -   Khi **"Authorization Policies" "chuẩn"** (dựa trên `RequireRole`, `RequireClaim`, v.v.) **"không đủ"** để "thể hiện" "logic" "phân quyền" "cần thiết".
    -   Khi "logic" "phân quyền" **"phụ thuộc" vào "dữ liệu" "bên ngoài"** (ví dụ: database, APIs, external services).
    -   Khi "logic" "phân quyền" **"rất" "phức tạp"** và **"tùy biến"**, "yêu cầu" code "logic" "riêng".
    -   Khi bạn muốn **"tái sử dụng" "logic" "phân quyền"** trong "nhiều" "Authorization Policies" khác nhau.
    -   Khi bạn muốn **"tách biệt" "logic" "phân quyền"** khỏi "Controller Actions" và "Razor Pages" để "tăng" "tính 'mô-đun' " và "tính 'bảo trì' ".

-   **"Cách Tạo" Custom Authorization Handlers:**

    1.  **"Tạo" Custom Authorization Requirement:** (Nếu chưa có) "Tạo" một lớp (class) "implement" interface `IAuthorizationRequirement` (như đã thấy ở chương 3 và 4). Custom Authorization Requirement "đại diện" cho **"yêu cầu" "phân quyền" "tùy chỉnh"** mà bạn muốn "thực hiện".
    2.  **"Tạo" Custom Authorization Handler:** "Tạo" một lớp (class) "implement" lớp trừu tượng `AuthorizationHandler<TRequirement>`, với `TRequirement` là "loại" Custom Authorization Requirement mà "handler" này "xử lý".
    3.  **"Viết Code" "Logic" "Phân Quyền" Trong `HandleRequirementAsync()`:** "Override" phương thức `HandleRequirementAsync(AuthorizationHandlerContext context, TRequirement requirement)` trong Custom Authorization Handler. "Phương thức" này được "gọi" bởi Authorization Middleware khi "đánh giá" "Authorization Policy" có chứa Custom Authorization Requirement `TRequirement`.
        -   **`AuthorizationHandlerContext context`:** "Ngữ cảnh" trình xử lý ủy quyền. Chứa "thông tin" về:
            -   **`context.User`:** `ClaimsPrincipal` (User Identity) của "người dùng" "hiện tại".
            -   **`context.Resource`:** "Tài nguyên" được "truy cập" (tùy chọn). Có thể là `null` nếu "phân quyền" "không 'dựa trên' " "tài nguyên" "cụ thể". Nếu "phân quyền" "dựa trên" "tài nguyên" (resource-based authorization), `context.Resource` sẽ chứa "tài nguyên" (ví dụ: đối tượng "bài viết", "đơn hàng", v.v.).
            -   **`context.Requirements`:** "Danh sách" "Authorization Requirements" trong "Authorization Policy" đang được "đánh giá".
            -   **`context.Succeed(requirement)`:** "Gọi" "phương thức" này để **"báo hiệu" "ủy quyền" "thành công"** cho "Authorization Requirement" `requirement`.
            -   **`context.Fail(requirement)`:** "Gọi" "phương thức" này để **"báo hiệu" "ủy quyền" "thất bại"** cho "Authorization Requirement" `requirement`. (Mặc định, nếu không gọi `Succeed()` cho "requirement", "ủy quyền" sẽ "thất bại").
        -   **`TRequirement requirement`:** "Instance" của Custom Authorization Requirement đang được "xử lý". Chứa "thông tin" "cấu hình" "Requirement" (nếu có).
        -   **"Viết code" "logic" "phân quyền"** trong `HandleRequirementAsync()`. "Kiểm tra" `context.User`, `context.Resource`, `requirement`, và các "nguồn" "thông tin" "khác" (database, APIs, v.v.) để "quyết định" xem "người dùng" có **"đáp ứng" "Authorization Requirement"** hay không. "Gọi" `context.Succeed(requirement)` nếu "đáp ứng", hoặc "không gọi" `context.Succeed()` (hoặc "gọi" `context.Fail()`) nếu "không đáp ứng".
    4.  **"Đăng ký" Custom Authorization Handler** trong DI container (thường là "scoped" service).
    5.  **"Định nghĩa" "Authorization Policy"** "sử dụng" Custom Authorization Requirement (như đã thấy ở chương 4).

-   **"Ví Dụ" Custom Authorization Handlers:**

    -   **"Data Ownership Check" (Kiểm Tra Quyền Sở Hữu Dữ Liệu):** "Chỉ cho phép" "người dùng" "sửa" hoặc "xóa" **"dữ liệu" "của chính mình"**.

        ```csharp
        // Custom Requirement: Yêu cầu người dùng phải là "chủ sở hữu" của "tài nguyên"
        public class OwnsResourceRequirement : IAuthorizationRequirement
        {
            public string ResourceIdPropertyName { get; } // Tên property chứa "ID tài nguyên" trong "route data"

            public OwnsResourceRequirement(string resourceIdPropertyName)
            {
                ResourceIdPropertyName = resourceIdPropertyName;
            }
        }

        // Custom Handler: Kiểm tra xem người dùng có phải là "chủ sở hữu" của "tài nguyên" hay không
        public class OwnsResourceHandler : AuthorizationHandler<OwnsResourceRequirement>
        {
            private readonly IDataContext _dbContext; // Ví dụ: DataContext để truy cập database
            private readonly IHttpContextAccessor _httpContextAccessor; // Để truy cập HttpContext

            public OwnsResourceHandler(IDataContext dbContext, IHttpContextAccessor httpContextAccessor)
            {
                _dbContext = dbContext;
                _httpContextAccessor = httpContextAccessor;
            }

            protected override async Task HandleRequirementAsync(AuthorizationHandlerContext context, OwnsResourceRequirement requirement)
            {
                if (!context.User.Identity.IsAuthenticated) // Yêu cầu "xác thực"
                {
                    return; // Không xác thực, ủy quyền thất bại (mặc định)
                }

                var userId = context.User.FindFirstValue(ClaimTypes.NameIdentifier); // Lấy User ID từ Claims
                if (string.IsNullOrEmpty(userId))
                {
                    return; // Không có User ID, ủy quyền thất bại (mặc định)
                }

                var httpContext = _httpContextAccessor.HttpContext;
                if (httpContext == null)
                {
                    return; // Không có HttpContext, ủy quyền thất bại (mặc định)
                }

                var resourceIdRouteValue = httpContext.GetRouteValue(requirement.ResourceIdPropertyName)?.ToString(); // Lấy "ID tài nguyên" từ route data
                if (string.IsNullOrEmpty(resourceIdRouteValue) || !int.TryParse(resourceIdRouteValue, out int resourceId))
                {
                    return; // Không tìm thấy "ID tài nguyên" hợp lệ trong route data, ủy quyền thất bại (mặc định)
                }

                // Ví dụ: Kiểm tra trong database xem "người dùng" có phải là "chủ sở hữu" của "tài nguyên" có "ID" là `resourceId` hay không
                var isOwner = await _dbContext.CheckResourceOwnershipAsync(resourceId, userId); // Giả sử có phương thức CheckResourceOwnershipAsync() trong DataContext

                if (isOwner)
                {
                    context.Succeed(requirement); // Là "chủ sở hữu", ủy quyền thành công
                }

                return; // Không phải "chủ sở hữu", ủy quyền thất bại (mặc định)
            }
        }

        public void ConfigureServices(IServiceCollection services)
        {
            services.AddScoped<IAuthorizationHandler, OwnsResourceHandler>(); // Đăng ký Custom Handler

            services.AddAuthorization(options => {
                options.AddPolicy("OwnsArticlePolicy", policy => // Định nghĩa Policy "OwnsArticlePolicy"
                    policy.Requirements.Add(new OwnsResourceRequirement("id"))); // Sử dụng Custom Requirement "OwnsResourceRequirement", "id" là "tên property" chứa "ID bài viết" trong route data
            });

            // ... các service khác ...
        }

        // Sử dụng trong Controller Action:
        [Authorize(Policy = "OwnsArticlePolicy")] // Yêu cầu Policy "OwnsArticlePolicy"
        public IActionResult Edit(int id) // "id" là "ID bài viết", sẽ được "truyền" vào "OwnsResourceRequirement"
        {
            // ... code "sửa bài viết" ...
        }
        ```

    -   **"Business Logic Based Authorization" (Phân Quyền Dựa Trên Logic Nghiệp Vụ):** "Phân quyền" "dựa trên" **"quy tắc" "nghiệp vụ" "phức tạp"**, "không chỉ" "dựa vào" "vai trò" hoặc "claims". "Ví dụ": "chỉ cho phép" "người dùng" "đặt hàng" nếu "tổng giá trị" "đơn hàng" **"nhỏ hơn" "hạn mức tín dụng"** của "người dùng".

        ```csharp
        // Custom Requirement: Yêu cầu "tổng giá trị" "đơn hàng" phải "nhỏ hơn" "hạn mức tín dụng" của "người dùng"
        public class CreditLimitRequirement : IAuthorizationRequirement
        {
            public decimal MaxOrderValue { get; } // "Hạn mức" "tối đa" cho "đơn hàng"

            public CreditLimitRequirement(decimal maxOrderValue)
            {
                MaxOrderValue = maxOrderValue;
            }
        }

        // Custom Handler: Kiểm tra xem "tổng giá trị" "đơn hàng" có "nhỏ hơn" "hạn mức tín dụng" của "người dùng" hay không
        public class CreditLimitHandler : AuthorizationHandler<CreditLimitRequirement>
        {
            private readonly ICreditService _creditService; // Ví dụ: CreditService để lấy "hạn mức tín dụng" của "người dùng"

            public CreditLimitHandler(ICreditService creditService)
            {
                _creditService = creditService;
            }

            protected override async Task HandleRequirementAsync(AuthorizationHandlerContext context, CreditLimitRequirement requirement)
            {
                if (!context.User.Identity.IsAuthenticated) // Yêu cầu "xác thực"
                {
                    return; // Không xác thực, ủy quyền thất bại (mặc định)
                }

                var userId = context.User.FindFirstValue(ClaimTypes.NameIdentifier); // Lấy User ID từ Claims
                if (string.IsNullOrEmpty(userId))
                {
                    return; // Không có User ID, ủy quyền thất bại (mặc định)
                }

                var orderValue = GetOrderValueFromResource(context.Resource); // Giả sử có phương thức GetOrderValueFromResource() để lấy "tổng giá trị" "đơn hàng" từ "resource" (context.Resource)

                if (orderValue > requirement.MaxOrderValue) // "Tổng giá trị" "đơn hàng" "vượt quá" "hạn mức" "tối đa"
                {
                    return; // Ủy quyền thất bại (mặc định)
                }

                var creditLimit = await _creditService.GetCreditLimitAsync(userId); // Lấy "hạn mức tín dụng" của "người dùng" từ CreditService

                if (orderValue <= creditLimit) // "Tổng giá trị" "đơn hàng" "nhỏ hơn" hoặc "bằng" "hạn mức tín dụng"
                {
                    context.Succeed(requirement); // Ủy quyền thành công
                }

                return; // "Tổng giá trị" "đơn hàng" "vượt quá" "hạn mức tín dụng", ủy quyền thất bại (mặc định)
            }

            private decimal GetOrderValueFromResource(object resource) // Ví dụ: Lấy "tổng giá trị" "đơn hàng" từ "resource"
            {
                if (resource is Order order)
                {
                    return order.TotalValue; // Giả sử "resource" là đối tượng "Order" có property "TotalValue"
                }
                return 0; // Không phải "Order", hoặc không lấy được "tổng giá trị", trả về 0 (hoặc xử lý lỗi khác)
            }
        }

        public void ConfigureServices(IServiceCollection services)
        {
            services.AddScoped<IAuthorizationHandler, CreditLimitHandler>(); // Đăng ký Custom Handler

            services.AddAuthorization(options => {
                options.AddPolicy("OrderWithinCreditLimitPolicy", policy => // Định nghĩa Policy "OrderWithinCreditLimitPolicy"
                    policy.Requirements.Add(new CreditLimitRequirement(1000))); // Sử dụng Custom Requirement "CreditLimitRequirement", "hạn mức" "tối đa" là 1000
            });

            // ... các service khác ...
        }

        // Sử dụng trong Controller Action:
        [Authorize(Policy = "OrderWithinCreditLimitPolicy")] // Yêu cầu Policy "OrderWithinCreditLimitPolicy"
        public IActionResult PlaceOrder(Order order) // "Order" là "resource", sẽ được "truyền" vào "CreditLimitHandler" qua context.Resource
        {
            // ... code "đặt hàng" ...
        }
        ```

-   **"Lợi Ích" Của Custom Authorization Handlers:**

    -   **"Flexibility" (Linh Hoạt) "tối đa"**: "Viết code" "logic" "phân quyền" "tùy chỉnh" "hoàn toàn" để "đáp ứng" "mọi" "yêu cầu" "phân quyền" "phức tạp" nhất.
    -   **"Control" (Kiểm Soát) "hoàn toàn"**: "Kiểm soát" "toàn bộ" quá trình "đánh giá" "quyền truy cập". "Tùy biến" "mọi khía cạnh" của "logic" "phân quyền".
    -   **"Extensibility" (Khả Năng Mở Rộng)**: "Dễ dàng" "mở rộng" "hệ thống" "phân quyền" bằng cách "thêm" "Custom Authorization Requirements" và "Handlers" "mới".
    -   **"Maintainability" (Tính Bảo Trì)**: "Tách biệt" "logic" "phân quyền" khỏi "Controller Actions" và "Razor Pages", "tăng" "tính 'mô-đun' " và "tính 'bảo trì' " của code. "Tái sử dụng" "logic" "phân quyền" trong "nhiều" "Authorization Policies".

**Tổng Kết Chương 6:**

-   Bạn đã "nắm vững" các "tuyệt chiêu" Authentication và Authorization "nâng cao" để " 'luyện công phu' " "bảo mật" ứng dụng.
    -   "Hiểu" **Role-Based Authorization "Nâng Cao"** ("phân quyền" "vai trò" "chi tiết" và "linh hoạt" hơn).
    -   "Khám phá" **Policy-Based Authorization "Nâng Cao"** ("luật lệ" "phân quyền" "phức tạp" và "tùy biến" cao).
    -   Biết cách "sử dụng" **Claims Transformation** ("biến hình" "claims" để "phù hợp" với "nhu cầu" ứng dụng).
    -   "Làm chủ" **Custom Authorization Handlers** ("viết 'bộ kiểm soát' " "quyền truy cập" "riêng" - "tùy biến" "tối đa").

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 7: "Ứng Dụng Thực Tế Của Authentication và Authorization" - "AuthN/AuthZ Đi Muôn Nơi"**. Chúng ta sẽ "xem xét" các "ví dụ" "ứng dụng thực tế" của Authentication và Authorization trong ứng dụng web ASP.NET Core MVC, "phân tích" code "bảo mật" "thực tế", và "mở rộng" "ví dụ" để "nâng cấp" "bảo mật" ứng dụng "lên tầm cao mới".

Bạn có câu hỏi nào về Authentication và Authorization "nâng cao" này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" "bảo mật" ứng dụng web.
