# Chương 5: Routing - " 'Bản Đồ' " URL Của Ứng Dụng Web - " 'Nâng Cấp' " "Kỹ Năng" "Định Tuyến" URL - " 'Làm Chủ' " "Đường Đi Nước Bước" Của Request

Chào mừng bạn đến với **Chương 5: Routing - " 'Bản Đồ' " URL Của Ứng Dụng Web"**! Trong chương này, chúng ta sẽ **"nâng cấp"** "kỹ năng" **Routing** của bạn lên một "tầm cao mới". Chúng ta sẽ "đi sâu" vào **Route Templates**, **Route Parameters**, **Convention-Based Routing**, **Attribute Routing**, và "học cách" **"thiết kế"** "hệ thống Routing" **"linh hoạt"**, **"mạnh mẽ"**, và **"tối ưu hóa" SEO** cho ứng dụng web MVC của bạn. "Routing" là "xương sống" "dẫn dắt" request trong ứng dụng web, "làm chủ" Routing là "làm chủ" "vận mệnh" của ứng dụng web MVC.

**Phần 5: Routing - " 'Bản Đồ' " URL Của Ứng Dụng Web - " 'Dẫn Đường' " Request Đến Đúng Nơi**

**5.1. Routing là gì? - " 'Kết Nối' " URL Với Code Ứng Dụng - " 'Bí Mật' " Đằng Sau " 'Đường Dẫn' " Web**

-   **Routing (Định Tuyến) - " 'Bắc Cầu' " Giữa URL và Controller Actions:**

    -   **Routing** (Định Tuyến) là một "cơ chế" "nền tảng" trong ứng dụng web MVC, "chịu trách nhiệm" **"ánh xạ"** (map) **"request URLs"** (địa chỉ web mà người dùng "gõ" vào trình duyệt) đến **"Controller Actions"** (phương thức action trong Controller) "tương ứng" để "xử lý" request đó.
    -   Routing "hoạt động" như một **" 'bản đồ' " URL** của ứng dụng web, "xác định" **" 'đường đi' "** của mỗi request, "dẫn đường" request từ URL đến **" 'đúng 'đích' "** (Controller Action) để "xử lý" và "tạo ra" "phản hồi".
    -   Routing "cho phép" bạn **"thiết kế" "cấu trúc URL" "thân thiện"** với người dùng và SEO (search engine optimization), "dễ nhớ", "dễ chia sẻ", và "dễ 'index' " bởi các công cụ tìm kiếm.

-   **"Ví Dụ 'Minh Họa' " - Routing "Dẫn Đường" Request Đến Controller Actions:**

    -   Khi người dùng "truy cập" URL **`/products`** (xem danh sách sản phẩm), Routing sẽ "dẫn đường" request này đến **Action Method `Index()`** trong **Controller `SanPhamController`** (ProductController) để "hiển thị" trang "danh sách sản phẩm".
    -   Khi người dùng "truy cập" URL **`/products/details/123`** (xem chi tiết sản phẩm có ID là 123), Routing sẽ "dẫn đường" request này đến **Action Method `Details(int id)`** trong **Controller `SanPhamController`** và "truyền" giá trị `123` từ URL segment `{id}` vào **tham số `id`** của Action Method.
    -   Khi người dùng "gửi" form "thêm sản phẩm mới" đến URL **`/products/create`** (HTTP POST request), Routing sẽ "dẫn đường" request này đến **Action Method `Create(SanPham sanPham)`** (phiên bản HTTP POST) trong **Controller `SanPhamController`** để "xử lý" form data và "lưu" sản phẩm mới vào database.

-   **Routing " 'Ẩn' " "Chi Tiết" "Bên Trong" URL - " 'Trừu Tượng Hóa' " "Đường Dẫn" Web:**

    -   Routing "giúp" "ẩn" "chi tiết" "thực hiện" "bên trong" ứng dụng web "khỏi" URL. URL trở nên **" 'trừu tượng' "** hơn, **"không 'phản ánh' " "cấu trúc thư mục"** "vật lý" của ứng dụng trên server, hoặc "tên file" code.
    -   URL "tập trung" vào **" 'tài nguyên' "** (resource) và **" 'hành động' "** (action) mà người dùng muốn "truy cập" hoặc "thực hiện" trên ứng dụng web (ví dụ: "tài nguyên" `products`, "hành động" `details`, `create`, `edit`, `delete`).
    -   "Thay đổi" "cấu trúc thư mục" code, "đổi tên file" code, hoặc "tái cấu trúc" code "bên trong" ứng dụng **"không ảnh hưởng"** đến **"URL 'công khai' "** mà người dùng "truy cập", miễn là bạn "giữ nguyên" "cấu hình" Routing. "Tăng" **"tính 'linh hoạt' " và " 'dễ bảo trì' "** của ứng dụng web.

**5.2. Route Templates (Mẫu Route) - " 'Cách' " "Định Nghĩa" "Đường Dẫn" URL - " 'Công Thức' " Tạo Ra " 'Bản Đồ' " URL**

-   **Route Templates (Mẫu Route) - " 'Khuôn Mẫu' " URL - " 'Công Thức' " "Định Tuyến" Request:**

    -   **Route Templates** (Mẫu Route) là các **"chuỗi"** (strings) "được 'dùng' " để **"định nghĩa" "cấu trúc"** của **"đường dẫn" URL** (URL path) và **"ánh xạ"** URL segments (phần URL) đến **Controller**, **Action Method**, và **Route Parameters**.
    -   Route Templates "hoạt động" như **" 'công thức' "** để Routing Middleware "dùng" để **"đối sánh"** (match) request URLs và "xác định" **"Route Data"** (dữ liệu route) và **Controller Action** "tương ứng".

-   **"Các 'Thành Phần' " Của Route Template:**

    -   **Literal Segments (Phần Cố Định):** "Chuỗi" "cố định" (literals) trong Route Template, phải **"khớp chính xác"** với URL segment "tương ứng" để Route Template được "đối sánh". (Ví dụ: `"products"`, `"details"`, `"create"`, `"edit"`, `"delete"`).

    -   **Parameter Segments (Phần Tham Số):** "Được bao quanh" bởi dấu **`{` và `}`** (ví dụ: `{controller}`, `{action}`, `{id}`). "Đại diện" cho các **"tham số" "động"** trong URL. Routing Middleware sẽ "trích xuất" **"giá trị"** của URL segment "tương ứng" và "gán" cho **"tham số"** có tên trong Parameter Segment.

        -   **Required Parameter Segments (Phần Tham Số "Bắt Buộc"):** (Ví dụ: `{id}`). Tham số **"bắt buộc"** phải có trong URL để Route Template được "đối sánh". Nếu "thiếu" Parameter Segment "bắt buộc" trong URL, Route Template sẽ "không" được "đối sánh".

        -   **Optional Parameter Segments (Phần Tham Số "Tùy Chọn"):** (Ví dụ: `{id?}`). Tham số **"tùy chọn"** có thể **"có"** hoặc **"không có"** trong URL. Dấu **`?`** "biểu thị" tham số là "tùy chọn". Nếu "không có" Parameter Segment "tùy chọn" trong URL, tham số sẽ "nhận" **"giá trị 'mặc định' "** (nếu được "định nghĩa" trong Route Template) hoặc **`null`**.

        -   **Default Values (Giá Trị "Mặc Định"):** Bạn có thể "định nghĩa" **"giá trị 'mặc định' "** cho Parameter Segments bằng cách "dùng" dấu **`=`** sau tên tham số (ví dụ: `{controller=Home}`, `{action=Index}`). Nếu "không có" URL segment "tương ứng" cho Parameter Segment có "giá trị 'mặc định' ", tham số sẽ "nhận" "giá trị 'mặc định' " đã "định nghĩa".

        -   **Constraints (Ràng Buộc):** Bạn có thể "thêm" **"ràng buộc"** (constraints) cho Parameter Segments để "giới hạn" **"kiểu dữ liệu"** hoặc **"định dạng"** của giá trị tham số (ví dụ: `{id:int}`, `{page:int:min(1)}`, `{slug:regex(^[a-z0-9-]+$)}`). Constraints giúp Routing Middleware "chọn" **"Route Template" "phù hợp nhất"** khi có "nhiều" Route Templates có thể "đối sánh" với cùng một URL.

-   **"Ví Dụ" Route Templates:**

    -   `"products"`: Route Template "chỉ đối sánh" URL `/products` (Literal Segment "products").
    -   `"products/details/{id}"`: Route Template "đối sánh" URL bắt đầu bằng `/products/details/` và có thêm một URL segment "bắt buộc" ở cuối (Parameter Segment `{id}` - Required Parameter Segment). Ví dụ: `/products/details/123`, `/products/details/abc`.
    -   `"products/edit/{id?}"`: Route Template "đối sánh" URL bắt đầu bằng `/products/edit/` và có thêm một URL segment "tùy chọn" ở cuối (Parameter Segment `{id?}` - Optional Parameter Segment). Ví dụ: `/products/edit`, `/products/edit/456`.
    -   `"categories/{categoryId:int}/products/{productId:int}"`: Route Template "đối sánh" URL có "cấu trúc" "phức tạp" hơn, có nhiều Literal Segments và Parameter Segments với "ràng buộc" "kiểu dữ liệu" (constraints). Ví dụ: `/categories/10/products/200`.
    -   `"{controller=Home}/{action=Index}/{id?}"`: Route Template "mặc định" (default route template) - "linh hoạt" hơn, "đối sánh" nhiều loại URLs khác nhau.

**5.3. Route Parameters (Tham Số Route) - " 'Biến' " Trong URL - " 'Truyền' " Dữ Liệu Từ URL Đến Action Methods**

-   **Route Parameters (Tham Số Route) - " 'Biến' " "Động" Trong URL:**

    -   **Route Parameters** (Tham Số Route) là các **"biến" "động"** trong **URL** được "định nghĩa" trong **Parameter Segments** của **Route Templates** (ví dụ: `{controller}`, `{action}`, `{id}`, `{categoryId}`, `{productId}`, v.v.).
    -   Route Parameters "cho phép" bạn **"truyền" "dữ liệu"** từ **URL** (URL segments) đến **Controller Actions**. Routing Middleware sẽ "trích xuất" **"giá trị"** của URL segments "tương ứng" và "gán" cho **"tham số"** của Action Methods có **"cùng tên"** với Route Parameters.
    -   Route Parameters giúp "tạo ra" **URLs "động"** và **"thân thiện"** với người dùng và SEO, "mô tả" **"tài nguyên"** (resource) và **"hành động"** mà người dùng muốn "truy cập" hoặc "thực hiện" trên ứng dụng web.

-   **"Cách 'Truyền' " Dữ Liệu Từ Route Parameters Đến Action Methods - " 'Ràng Buộc Model' " Tự Động:**

    -   ASP.NET Core MVC "tự động" **"bind"** (ràng buộc) **"giá trị"** của **Route Parameters** từ URL vào **"tham số"** (parameters) của **Action Methods** có **"cùng tên"** thông qua **Model Binding** (chúng ta sẽ "học" sâu hơn về Model Binding ở Chương 7).
    -   Để "nhận" giá trị Route Parameter trong Action Method, bạn chỉ cần "khai báo" một **"tham số"** trong Action Method có **"cùng tên"** với **Parameter Segment** trong Route Template.

    -   **"Ví Dụ" "Truyền" Dữ Liệu Route Parameter `id` Đến Action Method `Details(int id)`:**

        **Route Template (Attribute Routing):**

        ```csharp
        [Route("products/details/{id}")] // Route Template có Parameter Segment "{id}"
        public IActionResult Details(int id) // Action Method "Details" có tham số "id" (cùng tên với Parameter Segment)
        {
            // ... (code "xử lý" sản phẩm theo ID) ...
        }
        ```

        **URL Request:**

        ```
        https://localhost:5001/products/details/123 // URL request có URL segment "123" cho Parameter Segment "{id}"
        ```

        **Model Binding "Tự Động":**

        -   Routing Middleware "trích xuất" giá trị URL segment `"123"` cho Parameter Segment `{id}`.
        -   Model Binding "tự động" "chuyển đổi" giá trị `"123"` thành kiểu `int` và "gán" cho **tham số `id`** của Action Method `Details(int id)`.
        -   Trong Action Method `Details(int id)`, bạn có thể "dùng" **tham số `id`** để "truy cập" giá trị `"123"` từ URL segment `{id}`.

-   **"Các Loại" Route Parameters:**

    -   **Required Route Parameters (Tham Số Route "Bắt Buộc"):** (Ví dụ: `{id}`). Tham số "bắt buộc" phải có trong URL để Route Template được "đối sánh" và Action Method được "gọi".

    -   **Optional Route Parameters (Tham Số Route "Tùy Chọn"):** (Ví dụ: `{page?}`). Tham số "tùy chọn" có thể "có" hoặc "không có" trong URL. Action Method vẫn được "gọi" ngay cả khi "không có" giá trị cho tham số "tùy chọn" trong URL.

    -   **Default Values For Optional Route Parameters (Giá Trị "Mặc Định" Cho Tham Số Route "Tùy Chọn"):** (Ví dụ: `{page=1}`). Nếu "không có" giá trị cho tham số "tùy chọn" trong URL, tham số sẽ "nhận" "giá trị 'mặc định' " đã "định nghĩa" trong Route Template.

    -   **Constraints On Route Parameters (Ràng Buộc Cho Tham Số Route):** (Ví dụ: `{id:int}`, `{page:int:min(1)}`, `{slug:regex(^[a-z0-9-]+$)}`). "Giới hạn" "kiểu dữ liệu" hoặc "định dạng" của giá trị tham số. "Đảm bảo" dữ liệu "đầu vào" từ URL "hợp lệ" và "an toàn".

**5.4. Attribute Routing (Định Tuyến Bằng Attribute) vs. Convention-Based Routing (Định Tuyến Dựa Trên Quy Ước) - "Chọn 'Đường Đi' Nào?" - " 'Linh Hoạt' " vs. " 'Đơn Giản' "**

-   **Attribute Routing (Định Tuyến Bằng Attribute) - " 'Định Nghĩa' " Route "Ngay Trong Code" Controller:**

    -   **Attribute Routing** (Định Tuyến Bằng Attribute) là "cách" "định nghĩa" **Route Templates** **"trực tiếp"** trên **Controller classes** và **Action Methods** bằng cách "dùng" các **"attributes"** (ví dụ: `[Route]`, `[HttpGet]`, `[HttpPost]`, `[HttpPut]`, `[HttpDelete]`, `[HttpPatch]`, `[HttpHead]`, `[HttpOptions]`).
    -   Attribute Routing "cho phép" bạn "tạo ra" **"route" "tùy chỉnh"** và "phức tạp" hơn, "không bị 'ràng buộc' " bởi "quy ước" của Convention-Based Routing. "Linh hoạt" hơn và "mạnh mẽ" hơn Convention-Based Routing.
    -   Attribute Routing là "lựa chọn" **"phổ biến"** và **"được 'khuyến khích' "** cho các ứng dụng web MVC "hiện đại" và Web APIs, đặc biệt là khi "xây dựng" **RESTful APIs**.

    -   **"Các Attributes" "Phổ Biến" Của Attribute Routing:**
        -   `[Route("template")]`: "Attribute" "cơ bản" để "định nghĩa" **"Route Template"** cho Controller class hoặc Action Method. (Ví dụ: `[Route("products")]`, `[Route("products/details/{id}")]`).
        -   `[HttpGet("template")]`, `[HttpPost("template")]`, `[HttpPut("template")]`, `[HttpDelete("template")]`, `[HttpPatch("template")]`, `[HttpHead("template")]`, `[HttpOptions("template")]`: **"Verb-specific Routing Attributes"** (Attributes "định tuyến" theo HTTP verb). "Kết hợp" "định nghĩa" **"Route Template"** và **"HTTP verb"** (method) mà Action Method sẽ "xử lý". "Dùng" để "xây dựng" **RESTful APIs**. (Ví dụ: `[HttpGet("products")]` - Action Method "xử lý" HTTP GET request đến URL `/products`, `[HttpPost("products")]` - Action Method "xử lý" HTTP POST request đến URL `/products`).

        -   **"Ví Dụ" Attribute Routing Trong `SanPhamController`:**

            ```csharp
            [Route("api/[controller]")] // "Route Attribute" "trên Controller class" - "base route" cho tất cả Action Methods trong Controller (ví dụ: "/api/SanPham")
            [ApiController] // "Attribute" "báo hiệu" Controller này là API controller (tự động validation, binding, v.v.)
            public class SanPhamApiController : ControllerBase
            {
                // ... (Dependency Injection, Constructor) ...

                [HttpGet] // "HttpGet Attribute" - "Route Template" "kết hợp" với HTTP GET verb - "ánh xạ" HTTP GET request đến URL "/api/SanPham" đến Action Method "Index"
                public async Task<ActionResult<IEnumerable<SanPham>>> Index()
                {
                    // ... (code "lấy" danh sách sản phẩm) ...
                }

                [HttpGet("{id}")] // "HttpGet Attribute" - "Route Template" "kết hợp" với HTTP GET verb và Parameter Segment "{id}" - "ánh xạ" HTTP GET request đến URL "/api/SanPham/{id}" đến Action Method "GetSanPham"
                public async Task<ActionResult<SanPham>> GetSanPham(int id)
                {
                    // ... (code "lấy" sản phẩm theo ID) ...
                }

                [HttpPost] // "HttpPost Attribute" - "Route Template" "kết hợp" với HTTP POST verb - "ánh xạ" HTTP POST request đến URL "/api/SanPham" đến Action Method "CreateSanPham"
                public async Task<ActionResult<SanPham>> CreateSanPham(SanPham sanPham)
                {
                    // ... (code "thêm" sản phẩm mới) ...
                }

                // ... (các Action Methods khác: Put, Delete, v.v. với các Route Attributes tương ứng) ...
            }
            ```

-   **Convention-Based Routing (Định Tuyến Dựa Trên Quy Ước) - " 'Đường Đi' " "Mặc Định" "Đơn Giản" và "Tiện Lợi":**

    -   **Convention-Based Routing** (Định Tuyến Dựa Trên Quy Ước) "dựa vào" **"quy ước"** và **"Route Template 'mặc định' "** (default route template) để "ánh xạ" URL đến Controller Actions. "Không cần" "định nghĩa" Route Templates "trực tiếp" trên Controller classes và Action Methods.
    -   Convention-Based Routing "đơn giản" và "dễ dùng" cho các ứng dụng web **"cơ bản"** và **"truyền thống"** (ví dụ: ứng dụng web MVC "dạng website", "không phải" Web API).

    -   **"Cách 'Đăng Ký' " Convention-Based Routing Trong `Program.cs` (hoặc `Startup.cs`):**

        ```csharp
        endpoints.MapControllerRoute(
            name: "default", // "Tên route"
            pattern: "{controller=Home}/{action=Index}/{id?}"); // "Route Template" "mặc định"
        ```

    -   **"Ưu Điểm" và "Nhược Điểm" Của Attribute Routing vs. Convention-Based Routing:**

        | Tính Năng        | Attribute Routing                                  | Convention-Based Routing                                    |
        | ---------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
        | **"Độ Linh Hoạt"** | Rất linh hoạt, "tùy biến" cao, "định nghĩa" route "phức tạp" | "Ít linh hoạt" hơn, "dựa vào" "quy ước" và "Route Template 'mặc định' " |
        | **"Độ Rõ Ràng"**   | Route Templates "được 'định nghĩa' " "ngay trong code" Controller, "dễ theo dõi" và "quản lý" routes | Route Templates "được 'định nghĩa' " "tập trung" ở "một nơi" (Startup.cs/Program.cs), có thể "khó theo dõi" hơn khi ứng dụng có nhiều routes |
        | **"RESTful APIs"** | "Phù hợp" "tuyệt vời" để "xây dựng" RESTful APIs, "hỗ trợ" Verb-specific Routing Attributes | "Kém 'linh hoạt' " hơn cho RESTful APIs, "khó" "định nghĩa" routes RESTful "phức tạp" |
        | **"Độ Phức Tạp"**  | "Phức tạp" hơn một chút để "bắt đầu", nhưng "dễ quản lý" hơn khi ứng dụng "lớn" và "phức tạp" | "Đơn giản" hơn để "bắt đầu", nhưng có thể "khó quản lý" hơn khi ứng dụng "lớn" và "phức tạp" |
        | **"Best Practice"** | "Được 'khuyến khích' " cho các ứng dụng web MVC "hiện đại" và Web APIs | "Phù hợp" cho các ứng dụng web MVC "cơ bản" hoặc "truyền thống" |

    -   **" 'Lời Khuyên' " - "Chọn 'Đường Đi' Nào?":**

        -   **Cho ứng dụng web MVC "mới" và Web APIs:** **"Ưu tiên" "dùng" Attribute Routing**. "Linh hoạt" hơn, "mạnh mẽ" hơn, và "phù hợp" với "xu hướng" phát triển ứng dụng web hiện đại.
        -   **Cho ứng dụng web MVC "cơ bản" hoặc "truyền thống":** Có thể "bắt đầu" với **Convention-Based Routing** để "đơn giản" và "nhanh chóng". Sau đó, có thể "chuyển đổi" dần sang Attribute Routing khi ứng dụng "phát triển" "phức tạp" hơn.
        -   **"Kết hợp" cả hai?** Trong một số trường hợp, bạn có thể **"kết hợp"** cả Attribute Routing và Convention-Based Routing trong cùng một ứng dụng. "Dùng" Attribute Routing cho các Controller và Actions "chính" "yêu cầu" "route" "tùy biến" và "phức tạp". "Dùng" Convention-Based Routing cho các Controller và Actions "phụ trợ" hoặc các routes "đơn giản" "theo quy ước".

**Tổng Kết Chương 5:**

-   Bạn đã "nâng cấp" "kỹ năng" **Routing** lên "chuyên nghiệp" hơn và "hiểu" được "sức mạnh" của Routing trong việc "điều khiển" "đường đi nước bước" của request trong ứng dụng web MVC.
    -   "Hiểu" **Routing là gì** ("bản đồ" URL, "kết nối" URL với code ứng dụng).
    -   "Nắm vững" **Route Templates** và "cách" "định nghĩa" "cấu trúc" URL.
    -   Biết cách "dùng" **Route Parameters** để "truyền" dữ liệu từ URL đến Action Methods.
    -   "Phân biệt" **Attribute Routing** và **Convention-Based Routing** và "hiểu" "ưu điểm", "nhược điểm" của từng loại để "chọn" "phương pháp" Routing "phù hợp" cho ứng dụng của bạn.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 6: ViewData, ViewBag, và ViewContext - " 'Cầu Nối' " Dữ Liệu Từ Controller Đến View**. Chúng ta sẽ "khám phá" các "cơ chế" và "kỹ thuật" để **"truyền" "dữ liệu"** từ **Controller Actions** sang **Views** để View có thể "hiển thị" "dữ liệu Model" cho người dùng.

Bạn có câu hỏi nào về Routing này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" MVC.
