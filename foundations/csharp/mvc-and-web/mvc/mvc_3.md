# Chương 3: View - " 'Mặt Tiền' " Xinh Đẹp Của Ứng Dụng MVC - " 'Sân Khấu' " Cho Dữ Liệu và " 'Ấn Tượng' " Đầu Tiên Với Người Dùng

Chào mừng bạn đến với **Chương 3: View - " 'Mặt Tiền' " Xinh Đẹp Của Ứng Dụng MVC"**! Trong chương này, chúng ta sẽ "khám phá" **View**, "thành phần" **"giao diện người dùng"** (user interface - UI) của ứng dụng MVC, đóng vai trò như **" 'mặt tiền' " "xinh đẹp"** "hiển thị" **"dữ liệu"** (Model) và "tạo ra" **"ấn tượng" "đầu tiên"** với người dùng web. "View" là nơi "người dùng" **"thực sự 'nhìn thấy' "** và **"tương tác"** với ứng dụng MVC.

**Phần 3: View - " 'Mặt Tiền' " Xinh Đẹp Của Ứng Dụng MVC**

**3.1. View là gì? - " 'Giao Diện' " Người Dùng - " 'Nơi' " Dữ Liệu " 'Hóa Thân' " Thành " 'Trang Web' "**

-   **View (View) - " 'Lớp' " "Hiển Thị" và " 'Tương Tác' " Người Dùng:**

    -   **View** (View) trong kiến trúc MVC là "thành phần" **"chịu trách nhiệm"** "tạo ra" **"giao diện người dùng"** (user interface - UI) để **"hiển thị"** **"dữ liệu"** (Model) cho người dùng và **"cung cấp" "cơ chế"** để người dùng **"tương tác"** với ứng dụng web.
    -   Hãy tưởng tượng View như **" 'mặt tiền' " "xinh đẹp"** của một "cửa hàng" hoặc một "ngôi nhà". "Mặt tiền" "thu hút" "ánh nhìn" của "khách hàng" hoặc "người qua đường" và "tạo ra" **"ấn tượng" "đầu tiên"**. View "tạo ra" **"ấn tượng" "đầu tiên"** cho người dùng về ứng dụng web của bạn.
    -   View **"nhận" "dữ liệu"** từ **Controller** (dữ liệu Model) và "dùng" dữ liệu đó để **"tạo ra" "phản hồi"** (response) "hiển thị" cho người dùng (thường là trang HTML). View **"không chứa" "logic nghiệp vụ"** (business logic) và **"không 'tương tác' " "trực tiếp"** với **Model**. View **"thụ động"**, chỉ "nhận" "lệnh" và "dữ liệu" từ Controller và "hiển thị".

-   **" 'Nhiệm Vụ' " Chính Của View - "Hiển Thị" và "Tương Tác":**

    -   **"Hiển Thị" Dữ Liệu Model:** "Chuyển đổi" **"dữ liệu" Model** (thường là các đối tượng C#) thành **"giao diện người dùng"** (thường là trang HTML) để **"người dùng" "dễ dàng" "xem"** và **"hiểu"** dữ liệu. "Trình bày" dữ liệu một cách **"trực quan"**, **"hấp dẫn"**, và **"thân thiện"** với người dùng.
    -   **"Cung Cấp" "Giao Diện" "Tương Tác":** "Cung cấp" các **"phần tử" "giao diện"** (UI elements) (ví dụ: form, button, link, textbox, dropdown list, checkbox, radio button, v.v.) để **"người dùng" "nhập" "dữ liệu"** (input) và **"thực hiện" "hành động"** (actions) trên ứng dụng web (ví dụ: "gửi form", "bấm nút", "click link").

-   **View "Không Chứa" Business Logic - " 'Chỉ Tập Trung' " Vào " 'Giao Diện' ", Không " 'Xử Lý' " Nghiệp Vụ":**

    -   View **"không nên" "chứa" "bất kỳ" "logic nghiệp vụ" nào**. View "chỉ" "tập trung" vào **"trình bày" "dữ liệu"** và **"cung cấp" "giao diện" "tương tác"**.
    -   "Logic nghiệp vụ" (ví dụ: "tính toán giá", "xác thực dữ liệu", "truy vấn database") thuộc về **Model** và **Controller**, **"không nên" "đặt" trong View**.
    -   **"Tách biệt" "logic nghiệp vụ" khỏi View** giúp "View" trở nên **"đơn giản"**, **"dễ bảo trì"**, và **"dễ thay đổi" "giao diện"** (ví dụ: thay đổi layout, style, theme) mà **"không làm 'ảnh hưởng' "** đến "logic nghiệp vụ" của ứng dụng.

**3.2. Razor Views (.cshtml files) - " 'Ngôn Ngữ' " Tạo View Trong ASP.NET Core MVC - " 'Vẽ' " "Mặt Tiền" Web Với C# và HTML**

-   **Razor Views (.cshtml files) - " 'Bản Vẽ' " "Mặt Tiền" Web Bằng C# và HTML:**

    -   **Razor Views** là "công nghệ" **"view engine"** (bộ máy view) mặc định trong ASP.NET Core MVC để **"tạo ra"** **Views**.
    -   Razor Views được "viết" bằng **"Razor syntax"**, một "sự kết hợp" giữa **HTML** (HyperText Markup Language) và **C# code**.
    -   Razor Views được "lưu trữ" trong các file có phần mở rộng **`.cshtml`** (C# HTML).

-   **"Cấu Trúc" Của Razor View (.cshtml file):**

    -   **HTML Markup:** "Phần lớn" Razor View là **HTML code** "tiêu chuẩn" để "xác định" "cấu trúc" và "nội dung" của trang web (ví dụ: `<p>`, `<div>`, `<span>`, `<table>`, `<img>`, `<a>`, `<form>`, v.v.).
    -   **Razor Code Blocks (`@{ ... }`):** "Khối code" C# được "nhúng" vào HTML bằng cú pháp **`@{ ... }`**. "Dùng" để "viết" code C# "thực hiện" các "tác vụ" "xử lý" "logic" "nhỏ" trong View (ví dụ: "khai báo" biến, "thực hiện" vòng lặp, "điều kiện", v.v.). **"Hạn chế" "logic nghiệp vụ" "phức tạp"** trong Razor Code Blocks.
    -   **Razor Expressions (`@(...)` hoặc `@property`):** "Hiển thị" **"giá trị"** của **"biến C#"**, **"property C#"**, hoặc **"kết quả"** của **"biểu thức C#"** "ngay trong HTML" bằng cú pháp **`@(...)`** hoặc **`@property`**. "Dùng" để "hiển thị" **"dữ liệu Model"** trong View.
    -   **Tag Helpers (`<tag-helper>`) và HTML Helpers (`@Html.HelperName(...)`):** "Cung cấp" các **"thành phần" "giao diện" "mạnh mẽ"** và **"tiện lợi"** để "tạo ra" các phần tử HTML "phức tạp" (ví dụ: form, label, input, validation, link, v.v.) và "thực hiện" các "tác vụ" "thường dùng" trong View (ví dụ: "tạo URL", "hiển thị HTML encoded text", v.v.).

-   **"Ví Dụ" Razor View - `Index.cshtml` (Trang "Danh Sách Sản Phẩm"):**

    ```cshtml
    @model List<WebAppMvc.Models.SanPham> // "Khai báo" Model cho View - List<SanPham>

    @{
        ViewData["Title"] = "Danh sách Sản Phẩm"; // "Thiết lập" ViewData["Title"] (tiêu đề trang)
    }

    <h1>@ViewData["Title"]</h1> // "Hiển thị" ViewData["Title"] (tiêu đề trang)

    <p>
        <a asp-action="Create">Thêm Sản Phẩm Mới</a> // Tag Helper "<a>" - "tạo link" đến action "Create"
    </p>
    <table class="table"> // Bảng HTML
        <thead> // Header bảng
            <tr> // Hàng header
                <th>
                    @Html.DisplayNameFor(model => model.SanPhamId) // HTML Helper "DisplayNameFor" - "Hiển thị" "tên hiển thị" của property "SanPhamId"
                </th>
                <th>
                    @Html.DisplayNameFor(model => model.TenSanPham) // HTML Helper "DisplayNameFor" - "Hiển thị" "tên hiển thị" của property "TenSanPham"
                </th>
                <th>
                    @Html.DisplayNameFor(model => model.Gia) // HTML Helper "DisplayNameFor" - "Hiển thị" "tên hiển thị" của property "Gia"
                </th>
                <th>
                    @Html.DisplayNameFor(model => model.DanhMucSanPham) // HTML Helper "DisplayNameFor" - "Hiển thị" "tên hiển thị" của property "DanhMucSanPham"
                </th>
                <th></th> // Cột "Actions" (Hành động)
            </tr>
        </thead>
        <tbody> // Body bảng
            @foreach (var item in Model) // Razor Code Block - Vòng lặp "foreach" để duyệt qua Model (danh sách sản phẩm)
            {
                <tr> // Hàng dữ liệu sản phẩm
                    <td>
                        @Html.DisplayFor(modelItem => item.SanPhamId) // HTML Helper "DisplayFor" - "Hiển thị" giá trị của property "SanPhamId"
                    </td>
                    <td>
                        @Html.DisplayFor(modelItem => item.TenSanPham) // HTML Helper "DisplayFor" - "Hiển thị" giá trị của property "TenSanPham"
                    </td>
                    <td>
                        @Html.DisplayFor(modelItem => item.Gia) // HTML Helper "DisplayFor" - "Hiển thị" giá trị của property "Gia"
                    </td>
                    <td>
                        @Html.DisplayFor(modelItem => item.DanhMucSanPham) // HTML Helper "DisplayFor" - "Hiển thị" giá trị của property "DanhMucSanPham"
                    </td>
                    <td> // Cột "Actions" (Hành động) - các link "Edit", "Details", "Delete"
                        <a asp-action="Edit" asp-route-id="@item.SanPhamId">Sửa</a> | // Tag Helper "<a>" - "tạo link" đến action "Edit" với route parameter "id"
                        <a asp-action="Details" asp-route-id="@item.SanPhamId">Chi tiết</a> | // Tag Helper "<a>" - "tạo link" đến action "Details" với route parameter "id"
                        <a asp-action="Delete" asp-route-id="@item.SanPhamId">Xóa</a> // Tag Helper "<a>" - "tạo link" đến action "Delete" với route parameter "id"
                    </td>
                </tr>
            }
        </tbody>
    </table>
    ```

-   **"Giải Thích" Code Razor View `Index.cshtml`:**

    -   `@model List<WebAppMvc.Models.SanPham>`: **"Khai báo" Model** cho View là một `List<SanPham>`. View sẽ "nhận" một danh sách các đối tượng `SanPham` từ Controller và "dùng" danh sách này để "hiển thị" dữ liệu.
    -   `@{ ViewData["Title"] = "Danh sách Sản Phẩm"; }`: **Razor Code Block** để "thiết lập" giá trị cho `ViewData["Title"]` (tiêu đề trang).
    -   `<h1>@ViewData["Title"]</h1>`: **Razor Expression** `@ViewData["Title"]` để "hiển thị" giá trị của `ViewData["Title"]` trong thẻ `<h1>`.
    -   `<a asp-action="Create">Thêm Sản Phẩm Mới</a>`: **Tag Helper `<a>`** để "tạo link" HTML `<a>` (anchor tag). `asp-action="Create"` attribute "chỉ định" link này sẽ "dẫn đến" action `Create` trong Controller hiện tại.
    -   `@Html.DisplayNameFor(model => model.SanPhamId)`: **HTML Helper `Html.DisplayNameFor()`** để "hiển thị" **"tên hiển thị"** (display name) được "định nghĩa" cho property `SanPhamId` trong Data Model `SanPham` (có thể "định nghĩa" display name bằng Data Annotations).
    -   `@foreach (var item in Model) { ... }`: **Razor Code Block** - vòng lặp `foreach` để "duyệt qua" **`Model`** (danh sách sản phẩm) và "tạo ra" **"hàng"** (row) HTML `<tr>` cho **mỗi sản phẩm**.
    -   `@Html.DisplayFor(modelItem => item.SanPhamId)`: **HTML Helper `Html.DisplayFor()`** để "hiển thị" **"giá trị"** của property `SanPhamId` của **`modelItem`** (mỗi sản phẩm trong vòng lặp).
    -   `<a asp-action="Edit" asp-route-id="@item.SanPhamId">Sửa</a>`: **Tag Helper `<a>`** để "tạo link" "Sửa" sản phẩm. `asp-action="Edit"` attribute "chỉ định" link này sẽ "dẫn đến" action `Edit`. `asp-route-id="@item.SanPhamId"` attribute "truyền" giá trị của property `SanPhamId` làm **"route parameter"** có tên `id` cho action `Edit`.

**3.3. View Layouts (_Layout.cshtml) - " 'Khung Sườn' " Chung Cho Các Trang Web - " 'Giao Diện' " "Nhất Quán" Cho Toàn Ứng Dụng**

-   **View Layouts (_Layout.cshtml) - " 'Mẫu Trang' " "Chung" - " 'Bộ Xương' " Của Trang Web:**

    -   **View Layouts** (Layout Views) trong ASP.NET Core MVC là các **Razor Views (.cshtml files)** được "dùng" làm **"khung sườn" "chung"** (shared layout) cho **"nhiều Views"** khác trong ứng dụng web.
    -   View Layouts "chứa" **"cấu trúc HTML" "chung"** của trang web (ví dụ: `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`, `<header>`, `<footer>`, `<script>` tags, v.v.) và các **"vùng nội dung" "động"** (dynamic content placeholders) nơi "nội dung" "riêng biệt" của từng View sẽ được "chèn vào".
    -   View Layouts giúp **"tạo ra" "giao diện" "nhất quán"** cho **"toàn bộ" ứng dụng web**. "Tránh" "lặp đi lặp lại" code HTML "chung" ở nhiều Views. "Đơn giản hóa" việc "bảo trì" và "cập nhật" "giao diện" "chung" của ứng dụng.

-   **"File" Layout "Mặc Định" - `_Layout.cshtml` (Thường Nằm Trong Thư Mục `Views/Shared/`):**

    -   Trong dự án ASP.NET Core MVC, View Layout "mặc định" thường được "đặt" trong file **`_Layout.cshtml`** trong thư mục **`Views/Shared/`**.
    -   File `_Layout.cshtml` "được" **"dùng mặc định"** bởi **"tất cả" các Views** trong ứng dụng (trừ khi bạn "chỉ định" Layout khác cho View).

-   **"Các 'Thành Phần' " Quan Trọng Trong `_Layout.cshtml`:**

    -   **`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>` tags:** "Cấu trúc HTML" "cơ bản" của trang web.
    -   **`<head>` section:** Chứa các meta tags, title, CSS links, JavaScript links "chung" cho toàn bộ trang web.
        -   **`<title>@ViewData["Title"] - WebAppMvc</title>`:** **Razor Expression** để "hiển thị" **"tiêu đề trang"** (thường được "thiết lập" trong từng View và "truyền" qua `ViewData["Title"]`).
        -   **`<link rel="stylesheet" href="~/css/site.css" />`:** Tag Helper `<link>` để "nhúng" CSS file "site.css" (style "chung" cho toàn bộ trang web).
    -   **`<body>` section:** Chứa "nội dung" "chính" của trang web.
        -   **`<header>`:** Header "chung" của trang web (ví dụ: logo, menu điều hướng).
        -   **`<div class="container">`:** Container "chứa" "nội dung" "thay đổi" của từng View (nội dung "riêng biệt" của từng trang).
            -   **`@RenderBody()`:** **Razor Method `RenderBody()`** - **"Placeholder"** (vị trí "chèn") **"quan trọng nhất"** trong Layout. **"Nội dung" "riêng biệt"** của **"từng View"** sẽ được **"chèn vào" "vị trí" `@RenderBody()`** này khi trang web được "hiển thị".
        -   **`<footer>`:** Footer "chung" của trang web (ví dụ: thông tin bản quyền, liên hệ).
        -   **`<script src="~/js/site.js"></script>`:** Tag Helper `<script>` để "nhúng" JavaScript file "site.js" (script "chung" cho toàn bộ trang web).
        -   **`@await RenderSectionAsync("Scripts", required: false)`:** **Razor Method `RenderSectionAsync()`** - "Placeholder" để "chèn" **"sections" "JavaScript"** "tùy chọn" (optional) từ các Views "con".

-   **"Cách Dùng" View Layouts - " 'Chèn' " "Nội Dung View Vào 'Khung Sườn' " Layout:**

    -   **"Mặc định"**, **"tất cả"** các Views trong ứng dụng MVC sẽ **"dùng"** View Layout **`_Layout.cshtml`** (nếu file `_ViewStart.cshtml` không "chỉ định" Layout khác).
    -   Khi View được "hiển thị", **"nội dung" "riêng biệt"** của View sẽ được **"chèn vào" "vị trí" `@RenderBody()`** trong Layout. "Layout" "cung cấp" "khung sườn" "chung", View "cung cấp" "nội dung" "riêng biệt".
    -   Bạn có thể "tạo" **"nhiều" View Layouts** khác nhau (ví dụ: layout cho trang "admin", layout cho trang "user", layout cho trang "landing page", v.v.) và "chọn" Layout "phù hợp" cho từng View bằng cách "thiết lập" property `Layout` trong View hoặc trong `_ViewStart.cshtml`.

-   **"Ví Dụ" File Layout `_Layout.cshtml` "Mặc Định" (trong ASP.NET Core MVC template):**

    ```cshtml
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>@ViewData["Title"] - WebAppMvc</title> // Razor Expression - "Tiêu đề trang"
        <link rel="stylesheet" href="~/lib/bootstrap/dist/css/bootstrap.min.css" /> // Bootstrap CSS
        <link rel="stylesheet" href="~/css/site.css" asp-append-version="true" /> // Site CSS
        <link rel="stylesheet" href="~/WebAppMvc.styles.css" asp-append-version="true" /> // Ứng dụng CSS
    </head>
    <body>
        <header> // Header "chung"
            <nav class="navbar navbar-expand-sm navbar-toggleable-sm navbar-light bg-white border-bottom box-shadow mb-3">
                <div class="container-fluid">
                    <a class="navbar-brand" asp-area="" asp-controller="Home" asp-action="Index">WebAppMvc</a> // Logo/Brand - Tag Helper "<a>"
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target=".navbar-collapse" aria-controls="navbarSupportedContent"
                            aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="navbar-collapse collapse d-sm-inline-flex justify-content-between">
                        <ul class="navbar-nav flex-grow-1">
                            <li class="nav-item">
                                <a class="nav-link text-dark" asp-area="" asp-controller="Home" asp-action="Index">Home</a> // Menu item "Home" - Tag Helper "<a>"
                            </li>
                            <li class="nav-item">
                                <a class="nav-link text-dark" asp-area="" asp-controller="Home" asp-action="Privacy">Privacy</a> // Menu item "Privacy" - Tag Helper "<a>"
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
        <div class="container"> // Container "chứa" "nội dung" View
            <main role="main" class="pb-3">
                @RenderBody() // Razor Method "RenderBody()" - Placeholder cho "nội dung" View
            </main>
        </div>

        <footer class="border-top footer text-muted"> // Footer "chung"
            <div class="container">
                &copy; 2023 - WebAppMvc - <a asp-area="" asp-controller="Home" asp-action="Privacy">Privacy</a> // Footer text - Tag Helper "<a>"
            </div>
        </footer>
        <script src="~/lib/jquery/dist/jquery.min.js"></script> // jQuery script
        <script src="~/lib/bootstrap/dist/js/bootstrap.bundle.min.js"></script> // Bootstrap JavaScript
        <script src="~/js/site.js" asp-append-version="true"></script> // Site JavaScript

        @await RenderSectionAsync("Scripts", required: false) // Razor Method "RenderSectionAsync()" - Placeholder cho "sections" "JavaScript" "tùy chọn"
    </body>
    </html>
    ```

**3.4. Partial Views (_PartialView.cshtml) - " 'Mảnh Ghép' " View "Tái Sử Dụng" - " 'View Con' " Trong View "Lớn"**

-   **Partial Views (_PartialView.cshtml) - " 'View Con' " "Nhỏ Bé" và "Tái Sử Dụng":**

    -   **Partial Views** (View "Từng Phần") là các **Razor Views (.cshtml files)** được "dùng" làm **"mảnh ghép" "nhỏ"** (reusable fragments) của **Views "lớn"** hơn.
    -   Partial Views "cho phép" bạn **"chia nhỏ"** View "phức tạp" thành các **"View con" "nhỏ hơn"**, "dễ quản lý" hơn, và **"tái sử dụng"** các "mảnh ghép" View "này" ở **"nhiều Views"** khác nhau trong ứng dụng.
    -   Partial Views thường được "dùng" để "tái sử dụng" các **"phần" "giao diện" "chung"** (ví dụ: header, footer, sidebar, form fields, list items, v.v.) ở nhiều trang web khác nhau.

-   **"Cách Tạo" Partial View:**

    -   "Tạo" một Razor View file mới với phần mở rộng **`.cshtml`**, và **"đặt tên"** file **"bắt đầu bằng" dấu `_`** (gạch dưới) (ví dụ: `_SanPhamItem.cshtml`, `_DanhMucForm.cshtml`, `_Footer.cshtml`). "Quy ước" đặt tên file Partial View bắt đầu bằng `_` để "phân biệt" với View "thông thường".
    -   "Đặt" Partial View files trong thư mục **`Views/Shared/Components/YourComponentName/Default.cshtml`** (cho View Components) hoặc trong thư mục **`Views/ControllerName/`** (cho Partial View "cục bộ" của Controller) hoặc thư mục **`Views/Shared/`** (Partial View "dùng chung" cho toàn ứng dụng).

-   **"Cách 'Sử Dụng' " Partial View Trong View "Cha":**

    -   "Dùng" **Tag Helper `<partial>`** hoặc **HTML Helper `Html.Partial()`** hoặc **`Html.PartialAsync()`** trong View "cha" để **"render"** (hiển thị) Partial View.
    -   "Truyền" **Model** (dữ liệu) cho Partial View (nếu cần) thông qua `model` attribute (Tag Helper) hoặc tham số `model` (HTML Helpers).

    -   **Ví dụ "sử dụng" Partial View `_SanPhamItem.cshtml` để "hiển thị" thông tin sản phẩm trong View `Index.cshtml`:**

        **(File: `Views/SanPham/_SanPhamItem.cshtml` - Partial View `_SanPhamItem`):**

        ```cshtml
        @model WebAppMvc.Models.SanPham // "Khai báo" Model cho Partial View - SanPham

        <tr> // Hàng dữ liệu sản phẩm (HTML - "mã HTML" cho "mỗi sản phẩm")
            <td>
                @Html.DisplayFor(model => model.SanPhamId)
            </td>
            <td>
                @Html.DisplayFor(model => model.TenSanPham)
            </td>
            <td>
                @Html.DisplayFor(model => model.Gia)
            </td>
            <td>
                @Html.DisplayFor(model => model.DanhMucSanPham)
            </td>
            <td>
                <a asp-action="Edit" asp-route-id="@Model.SanPhamId">Sửa</a> |
                <a asp-action="Details" asp-route-id="@Model.SanPhamId">Chi tiết</a> |
                <a asp-action="Delete" asp-route-id="@Model.SanPhamId">Xóa</a>
            </td>
        </tr>
        ```

        **(File: `Views/SanPham/Index.cshtml` - View `Index` "sử dụng" Partial View `_SanPhamItem`):**

        ```cshtml
        @model List<WebAppMvc.Models.SanPham>

        @{
            ViewData["Title"] = "Danh sách Sản Phẩm";
        }

        <h1>@ViewData["Title"]</h1>

        <p>
            <a asp-action="Create">Thêm Sản Phẩm Mới</a>
        </p>
        <table class="table">
            <thead>
                <tr>
                    <th>
                        @Html.DisplayNameFor(model => model.SanPhamId)
                    </th>
                    <th>
                        @Html.DisplayNameFor(model => model.TenSanPham)
                    </th>
                    <th>
                        @Html.DisplayNameFor(model => model.Gia)
                    </th>
                    <th>
                        @Html.DisplayNameFor(model => model.DanhMucSanPham)
                    </th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                @foreach (var item in Model) // Vòng lặp "foreach" duyệt qua danh sách sản phẩm
                {
                    <partial name="_SanPhamItem" model="item" /> // Tag Helper "<partial>" - "render" Partial View "_SanPhamItem" và "truyền" Model "item" cho Partial View
                }
            </tbody>
        </table>
        ```

-   **"Lợi Ích" Của Partial Views - " 'Tái Sử Dụng' ", " 'Gọn Gàng' ", và " 'Dễ Quản Lý' " Views:**

    -   **"Tái Sử Dụng" Code View (View Reusability):** "Tái sử dụng" các "mảnh ghép" View "chung" ở "nhiều Views" khác nhau, "giảm" code "lặp đi lặp lại" và "tăng" "năng suất" phát triển View.
    -   **"Code View 'Gọn Gàng' " (View Simplicity):** "Chia nhỏ" View "phức tạp" thành các Partial Views "nhỏ hơn", "dễ quản lý" hơn, và "dễ đọc" hơn. "View cha" trở nên "gọn gàng" hơn vì "bớt" đi "code HTML" "chi tiết" của các "mảnh ghép".
    -   **"Code View 'Dễ Bảo Trì' " (View Maintainability):** "Sửa đổi" một Partial View sẽ "tự động" "cập nhật" "tất cả" các Views "cha" đang "sử dụng" Partial View đó. "Đơn giản hóa" việc "bảo trì" và "cập nhật" các "phần" "giao diện" "chung" của ứng dụng.

**Tổng Kết Chương 3:**

-   Bạn đã "khám phá" **View**, " 'mặt tiền' " xinh đẹp của ứng dụng MVC, và "hiểu" được "vai trò" của View trong "hiển thị" "giao diện người dùng" và "tạo ra" "trải nghiệm" cho người dùng web.
    -   "Hiểu" **View là gì** ("giao diện người dùng", "nơi" dữ liệu "hóa thân" thành "trang web").
    -   "Nắm vững" **Razor Views (.cshtml files)** và "cách" "dùng" Razor syntax (HTML, C# Code Blocks, Razor Expressions, Tag Helpers, HTML Helpers) để "tạo ra" Views.
    -   Biết cách "sử dụng" **View Layouts (_Layout.cshtml)** để "tạo ra" "khung sườn" "chung" và "giao diện" "nhất quán" cho toàn ứng dụng web.
    -   Học cách "dùng" **Partial Views (_PartialView.cshtml)** để "tái sử dụng" "mảnh ghép" View và "tổ chức" View code "gọn gàng" hơn.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: Controller - " 'Nhạc Trưởng' " Điều Phối Ứng Dụng MVC**. Chúng ta sẽ "khám phá" **Controller**, "thành phần" MVC "chịu trách nhiệm" "điều khiển" "luồng" ứng dụng và "điều phối" "tương tác" giữa Model và View, "đảm bảo" ứng dụng MVC "hoạt động" "nhịp nhàng" và "trơn tru".

Bạn có câu hỏi nào về View này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" MVC.

