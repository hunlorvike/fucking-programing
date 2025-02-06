# Chương 7: Form Handling và Model Binding - " 'Thu Thập' " Dữ Liệu Từ Người Dùng - " 'Biến Form Thành Model' " - " 'Giao Tiếp' " Hai Chiều Với User

Chào mừng bạn đến với **Chương 7: Form Handling và Model Binding**! Trong chương này, chúng ta sẽ "khám phá" cách ứng dụng web MVC **"tương tác"** với **"người dùng"** thông qua **HTML Forms**. Chúng ta sẽ "học cách" **"xử lý"** **Form Submission** (gửi form), **"thu thập"** **"dữ liệu"** từ người dùng "nhập" vào form, và "vận dụng" **Model Binding** để **"biến"** dữ liệu form thành **"đối tượng C#"** (Model) một cách "tự động" và "thuận tiện". "Form Handling" và "Model Binding" là "cầu nối" "quan trọng" để "xây dựng" các ứng dụng web MVC "tương tác" và "dữ liệu-driven".

**Phần 7: Form Handling và Model Binding - " 'Thu Thập' " Dữ Liệu Từ Người Dùng**

**7.1. HTML Forms Trong MVC Views - " 'Cánh Cửa' " "Tương Tác" Với Người Dùng - " 'Nơi' " Người Dùng " 'Giao Tiếp' " Với Web App**

-   **HTML Forms (Biểu Mẫu HTML) - " 'Công Cụ' " "Tương Tác" "Cơ Bản" Trên Web:**

    -   **HTML Forms** (Biểu Mẫu HTML) là một "thành phần" **"cơ bản"** và **"quan trọng"** của **HTML** (HyperText Markup Language) để "tạo ra" **"giao diện" "tương tác"** với người dùng trên web.
    -   HTML Forms "cho phép" người dùng **"nhập" "dữ liệu"** (input) thông qua các **"phần tử" "form"** (form elements) (ví dụ: textbox, textarea, password field, checkbox, radio button, dropdown list, v.v.) và **"gửi"** dữ liệu đã "nhập" về **server** để "xử lý" (form submission).
    -   HTML Forms là **" 'cánh cửa' " "tương tác"** "chính" giữa **"người dùng"** và **"ứng dụng web"**. Hầu hết các ứng dụng web "tương tác" đều "dùng" HTML Forms để "thu thập" "dữ liệu" từ người dùng (ví dụ: form "đăng ký", form "đăng nhập", form "liên hệ", form "tìm kiếm", form "đặt hàng", v.v.).

-   **"Các 'Thành Phần' " Chính Của HTML Form:**

    -   **`<form>` tag:** "Thẻ" HTML **"bao bọc"** "toàn bộ" "form". Các attributes "quan trọng" của `<form>` tag:
        -   **`action` attribute:** "URL" mà form data sẽ được "gửi" đến khi form được "submit". Thường là URL của một **Controller Action Method** trong ứng dụng MVC.
        -   **`method` attribute:** **HTTP method** được "dùng" để "gửi" form data. "Phổ biến" nhất là **`GET`** (gửi dữ liệu qua URL query string) và **`POST`** (gửi dữ liệu trong HTTP request body). "Chọn" HTTP method "phù hợp" với "mục đích" của form (GET cho "lấy dữ liệu", POST cho "thay đổi dữ liệu", v.v.).

    -   **Form Elements (Phần Tử Form):** Các "phần tử" HTML "bên trong" `<form>` tag để "người dùng" "nhập" "dữ liệu" (ví dụ: `<input>`, `<textarea>`, `<select>`, v.v.). Các attributes "quan trọng" của form elements:
        -   **`type` attribute (`<input>` tag):** "Xác định" **"loại"** "phần tử" input (ví dụ: `text`, `password`, `email`, `checkbox`, `radio`, `submit`, `hidden`, v.v.).
        -   **`name` attribute:** **"Tên"** của "phần tử" input. **"Quan trọng nhất"** attribute trong form elements. `name` attribute "xác định" **"key"** (tên) của dữ liệu khi form data được "gửi" về server. Server sẽ "dùng" `name` attribute để "nhận diện" và "xử lý" dữ liệu form.

    -   **Submit Button (`<button type="submit">` hoặc `<input type="submit">`):** "Button" để "người dùng" "submit" form (gửi form data về server).

-   **"Ví Dụ" HTML Form Trong MVC View (Trang "Thêm Sản Phẩm Mới" - `Create.cshtml`):**

    ```cshtml
    @model WebAppMvc.Models.SanPham // "Khai báo" Model cho View - SanPham

    @{
        ViewData["Title"] = "Thêm Sản Phẩm Mới"; // "Tiêu đề trang"
    }

    <h1>@ViewData["Title"]</h1> // "Hiển thị" tiêu đề trang

    <h4>SanPham</h4> // Tiêu đề form
    <hr />
    <div class="row"> // Container row
        <div class="col-md-4"> // Column form
            <form asp-action="Create"> // <form> tag - "bắt đầu" form, asp-action="Create" - "gửi form" đến Action Method "Create"
                <div asp-validation-summary="ModelOnly" class="text-danger"></div> // Tag Helper "<ValidationSummary>" - "Hiển thị" "tổng hợp" lỗi validation
                <div class="form-group"> // Form group - container cho label và input
                    <label asp-for="TenSanPham" class="control-label"></label> // Tag Helper "<label>" - "label" cho property "TenSanPham"
                    <input asp-for="TenSanPham" class="form-control" />       // Tag Helper "<input>" - "input" textbox cho property "TenSanPham"
                    <span asp-validation-for="TenSanPham" class="text-danger"></span> // Tag Helper "<ValidationMessage>" - "hiển thị" lỗi validation cho property "TenSanPham"
                </div>
                <div class="form-group"> // Form group
                    <label asp-for="Gia" class="control-label"></label> // Tag Helper "<label>" - "label" cho property "Gia"
                    <input asp-for="Gia" class="form-control" />       // Tag Helper "<input>" - "input" textbox cho property "Gia"
                    <span asp-validation-for="Gia" class="text-danger"></span> // Tag Helper "<ValidationMessage>" - "hiển thị" lỗi validation cho property "Gia"
                </div>
                <div class="form-group"> // Form group
                    <label asp-for="DanhMucSanPham" class="control-label"></label> // Tag Helper "<label>" - "label" cho property "DanhMucSanPham"
                    <input asp-for="DanhMucSanPham" class="form-control" />       // Tag Helper "<input>" - "input" textbox cho property "DanhMucSanPham"
                    <span asp-validation-for="DanhMucSanPham" class="text-danger"></span> // Tag Helper "<ValidationMessage>" - "hiển thị" lỗi validation cho property "DanhMucSanPham"
                </div>
                <div class="form-group"> // Form group - button "Submit"
                    <input type="submit" value="Create" class="btn btn-primary" /> // <input type="submit"> - Button "Submit", type="submit" - "kích hoạt" form submission
                </div>
            </form>
        </div>
    </div>

    <div>
        <a asp-action="Index">Quay lại danh sách</a> // Tag Helper "<a>" - "link" "Quay lại danh sách"
    </div>

    @section Scripts { // Section "Scripts" - "chèn" JavaScript validation
        @{await Html.RenderPartialAsync("_ValidationScriptsPartial");} // Partial View "_ValidationScriptsPartial" chứa JavaScript validation scripts
    }
    ```

-   **"Giải Thích" Code HTML Form `Create.cshtml`:**

    -   `<form asp-action="Create">`: **`<form>` tag** - "bắt đầu" form. `asp-action="Create"` attribute (Tag Helper) "xác định" form data sẽ được "gửi" đến **Action Method `Create`** (phiên bản HTTP POST) trong Controller hiện tại (Controller "Sản Phẩm" - SanPhamController). HTTP method "mặc định" cho form là **POST**.
    -   `<div asp-validation-summary="ModelOnly" class="text-danger"></div>`: **Tag Helper `<ValidationSummary>`** để "hiển thị" **"tổng hợp" "lỗi validation"** Model (nếu có) ở "đầu form".
    -   `<label asp-for="TenSanPham" class="control-label"></label>`: **Tag Helper `<label>`** để "tạo label" HTML `<label>`. `asp-for="TenSanPham"` attribute "liên kết" label này với **property `TenSanPham`** của Model (DataAnnotations).
    -   `<input asp-for="TenSanPham" class="form-control" />`: **Tag Helper `<input>`** để "tạo input" textbox HTML `<input type="text">`. `asp-for="TenSanPham"` attribute "liên kết" input này với **property `TenSanPham`** của Model. **`name` attribute** của input sẽ được "tạo tự động" là `"TenSanPham"` (dựa trên tên property Model).
    -   `<span asp-validation-for="TenSanPham" class="text-danger"></span>`: **Tag Helper `<ValidationMessage>`** để "hiển thị" **"thông báo lỗi validation"** (nếu có) cho property `TenSanPham` **"ngay bên cạnh"** input textbox.
    -   `<input type="submit" value="Create" class="btn btn-primary" />`: **`<input type="submit">`** - button "Submit" để "submit" form.

**7.2. Form Submission (Gửi Form) - " 'Hành Trình' " Dữ Liệu Từ Browser Đến Server - " 'Dữ Liệu Form 'Đi Đâu Về Đâu' "?"**

-   **Form Submission (Gửi Form) - " 'Gửi' " Dữ Liệu Từ Client Đến Server:**

    -   **Form Submission** (Gửi Form) là quá trình **"người dùng" "gửi" "dữ liệu"** đã "nhập" vào HTML Form (form data) từ **"trình duyệt web" (client)** về **"ứng dụng web MVC" (server)** để "xử lý".
    -   Form Submission được "kích hoạt" khi người dùng **"bấm" "submit button"** trong HTML Form.

-   **"Các Bước" "Hành Trình" Form Submission:**

    1.  **User Input Data (Người Dùng Nhập Dữ Liệu):** Người dùng "nhập" dữ liệu vào các "phần tử" form (textbox, checkbox, v.v.) trong HTML Form trên trình duyệt web.

    2.  **Form Data Encoding (Mã Hóa Dữ Liệu Form):** Khi người dùng "bấm" "submit button", trình duyệt web sẽ **"mã hóa"** (encode) dữ liệu form thành một **"chuỗi"** (string) theo một trong các **"định dạng" "mã hóa" form data** (form data encoding):
        -   **`application/x-www-form-urlencoded` (mặc định cho HTTP GET và POST):** Mã hóa dữ liệu form thành chuỗi **"key=value&key=value&..."**. "Key" là giá trị của `name` attribute của form element. "Value" là dữ liệu người dùng "nhập" vào form element. Các ký tự "đặc biệt" (ví dụ: space, &, =) được "mã hóa" (URL encoding). "Gửi" dữ liệu form trong **URL query string** (cho HTTP GET) hoặc trong **HTTP request body** (cho HTTP POST). "Phù hợp" với dữ liệu form "nhỏ" và "đơn giản".
        -   **`multipart/form-data` (dành cho upload files - tải file lên server):** Mã hóa dữ liệu form thành **"nhiều phần"** (multipart), mỗi phần chứa dữ liệu của một form element, có thể bao gồm cả **"file"**. "Gửi" dữ liệu form trong **HTTP request body**. "Phù hợp" với form có **"upload files"** hoặc dữ liệu form "lớn".
        -   **`text/plain` (ít dùng):** Mã hóa dữ liệu form thành chuỗi "văn bản thuần túy" (plain text). "Không hỗ trợ" mã hóa ký tự "đặc biệt". "Ít dùng" trong ứng dụng web "thực tế".

    3.  **HTTP Request (Request HTTP):** Trình duyệt web "tạo ra" một **HTTP request** (HTTP GET hoặc HTTP POST) và **"gửi"** request đó đến **"server"** (ứng dụng web MVC). HTTP request sẽ "chứa" **"form data"** đã được "mã hóa" (form data encoding) (trong URL query string hoặc HTTP request body). URL của request được "xác định" bởi `action` attribute của `<form>` tag. HTTP method (GET hoặc POST) được "xác định" bởi `method` attribute của `<form>` tag (hoặc "mặc định" là GET nếu không có `method` attribute).

    4.  **Server Receives Request (Server Nhận Request):** Ứng dụng web MVC (server) "nhận" HTTP request từ trình duyệt web.

    5.  **Routing (Định Tuyến):** ASP.NET Core Routing Middleware "phân tích" URL của request và "dẫn đường" request đến **Controller Action Method** "phù hợp" để "xử lý" request (dựa trên routing rules và URL).

    6.  **Model Binding (Ràng Buộc Model):** ASP.NET Core Model Binding "tự động" **"lấy" "form data"** từ HTTP request (từ URL query string hoặc HTTP request body), **"chuyển đổi"** dữ liệu form thành các **"kiểu dữ liệu C#"** (dựa trên `name` attributes của form elements và "kiểu dữ liệu" của tham số Action Method), và **"gán"** dữ liệu đã "chuyển đổi" cho **"tham số"** của **Controller Action Method**. "Biến" dữ liệu form thành **"đối tượng C#"** (Model) để Action Method có thể "dễ dàng" "sử dụng" dữ liệu form. (Chúng ta sẽ "khám phá" Model Binding "chi tiết" hơn ở phần 7.3).

    7.  **Controller Action Executes (Action Method Thực Thi):** Controller Action Method "chứa" code "xử lý" request. Action Method "dùng" dữ liệu form (đã được Model Binding "gán" vào tham số) để "thực hiện" các "tác vụ" "nghiệp vụ" (ví dụ: "validation" dữ liệu, "lưu" dữ liệu vào database, v.v.).

    8.  **Response (Phản Hồi):** Controller Action Method "tạo ra" và "trả về" **"phản hồi"** (response) cho trình duyệt web (ví dụ: View, Redirect, JSON data, v.v.).

    9.  **Browser Receives Response (Trình Duyệt Nhận Phản Hồi):** Trình duyệt web "nhận" "phản hồi" từ server và "hiển thị" "phản hồi" đó cho người dùng (ví dụ: "hiển thị" trang web mới, "tải xuống" file, v.v.).

**7.3. Model Binding - " 'Phép Màu' " "Biến Dữ Liệu Form Thành Đối Tượng C#" - " 'Giải Mã' " Dữ Liệu Form và " 'Gán' " Vào Model**

-   **Model Binding (Ràng Buộc Model) - " 'Trợ Lý' " "Đắc Lực" "Chuyển Đổi" Dữ Liệu Form:**

    -   **Model Binding** (Ràng Buộc Model) là một "tính năng" **"mạnh mẽ"** và **"tiện lợi"** của ASP.NET Core MVC, "tự động" **"lấy" "dữ liệu form"** từ HTTP request, **"chuyển đổi"** dữ liệu form thành các **"kiểu dữ liệu C#"**, và **"gán"** dữ liệu đã "chuyển đổi" cho **"tham số"** của **Controller Action Methods**.
    -   Model Binding "giải phóng" lập trình viên khỏi việc "viết code" "thủ công" để "lấy" và "chuyển đổi" dữ liệu form "một cách 'lặp đi lặp lại' " trong Controller Actions. "Tăng" "năng suất" và "giảm" code "rườm rà".
    -   Model Binding "hoạt động" như một **" 'trợ lý' " "đắc lực"** giúp bạn **"biến"** dữ liệu form "thô" (string, string array) thành các **"đối tượng C#"** (Model objects) "quen thuộc" và "dễ dàng" "sử dụng" trong code C# của bạn.

-   **"Cách Model Binding 'Hoạt Động' " - " 'Từ Form Data Đến Tham Số Action Method' ":**

    1.  **Request Đến Controller Action:** Trình duyệt web "gửi" HTTP request chứa **"form data"** về server. Request được "định tuyến" đến **Controller Action Method**.
    2.  **Model Binding Intervenes (Model Binding "Can Thiệp"):** ASP.NET Core Model Binding **"can thiệp"** vào quá trình "gọi" Action Method.
    3.  **"Lấy" Form Data Từ Request:** Model Binding "lấy" **"form data"** từ HTTP request. Form data có thể được "gửi" trong **URL query string** (cho HTTP GET) hoặc trong **HTTP request body** (cho HTTP POST). Model Binding "hỗ trợ" các "định dạng" "mã hóa" form data "phổ biến" (`application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain`).
    4.  **"Chuyển Đổi" Form Data Sang "Kiểu Dữ Liệu C#":** Model Binding "chuyển đổi" **"giá trị" form data** (dạng strings) thành các **"kiểu dữ liệu C#"** "tương ứng" với **"kiểu" "tham số"** của Action Method. "Tự động" "chuyển đổi" string sang `int`, `decimal`, `DateTime`, `bool`, enum, custom types, v.v.
    5.  **"Gán" Dữ Liệu Đã "Chuyển Đổi" Cho Tham Số Action Method:** Model Binding "gán" dữ liệu form đã "chuyển đổi" cho **"tham số"** của **Action Method**. "Tham số" Action Method sẽ "nhận" "giá trị" từ form data "tương ứng" (dựa trên `name` attribute của form elements và "tên" tham số Action Method).
    6.  **Action Method Executes (Action Method Thực Thi):** Action Method được "gọi" và "thực thi" với các **"tham số"** đã được **Model Binding "gán"** giá trị từ form data. Action Method có thể "dễ dàng" "sử dụng" dữ liệu form thông qua các "tham số" này.

-   **"Ví Dụ" Model Binding - "Biến Form Data Thành Object `SanPham` Trong Action Method `Create(SanPham sanPham)`:**

    **(View `Create.cshtml` - HTML Form):**

    ```cshtml
    <form asp-action="Create"> 
        // ... (các form fields với name attributes: TenSanPham, Gia, DanhMucSanPham) ...
    </form>
    ```

    **(Controller `SanPhamController.cs` - Action Method `Create(SanPham sanPham)`):**

    ```csharp
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Create(SanPham sanPham) // Action Method "Create" "nhận" tham số kiểu "SanPham"
    {
        if (ModelState.IsValid) // "Validation" Model (dữ liệu form "đã được" Model Binding)
        {
            await _sanPhamService.ThemSanPhamMoi(sanPham); // "Dùng" đối tượng "sanPham" (đã được Model Binding) để "thêm" sản phẩm mới
            return RedirectToAction(nameof(Index));
        }
        return View(sanPham);
    }
    ```

    -   Khi người dùng "submit" form `Create.cshtml`, trình duyệt web sẽ "gửi" form data về Action Method `Create(SanPham sanPham)`.
    -   **Model Binding "tự động" "lấy" form data** (ví dụ: `TenSanPham=Chuột không dây&Gia=250000&DanhMucSanPham=Điện tử`) và **"biến"** form data đó thành một **"đối tượng `SanPham`"**.
    -   **Property `TenSanPham`** của đối tượng `SanPham` sẽ được "gán" giá trị từ form data field có `name="TenSanPham"`.
    -   **Property `Gia`** của đối tượng `SanPham` sẽ được "gán" giá trị từ form data field có `name="Gia"`.
    -   **Property `DanhMucSanPham`** của đối tượng `SanPham` sẽ được "gán" giá trị từ form data field có `name="DanhMucSanPham"`.
    -   **Action Method `Create(SanPham sanPham)` "nhận" tham số `sanPham`** - một đối tượng `SanPham` đã được **Model Binding "gán" "dữ liệu form"**. Bạn có thể "dễ dàng" "sử dụng" đối tượng `sanPham` trong Action Method để "xử lý" dữ liệu form (ví dụ: "validation" dữ liệu, "lưu" vào database).

-   **"Các 'Nguồn' " Dữ Liệu Mà Model Binding "Có Thể Lấy":**

    -   **Form Data (Dữ Liệu Form):** Dữ liệu "gửi" từ HTML Forms (từ URL query string hoặc HTTP request body). (Phổ biến nhất).
    -   **Route Data (Dữ Liệu Route):** Giá trị của **Route Parameters** trong URL (ví dụ: `/products/details/{id}` - Route Parameter `{id}`).
    -   **Query String (Chuỗi Truy Vấn):** Các **Query String Parameters** trong URL (ví dụ: `?page=1&pageSize=10`).
    -   **HTTP Headers (Headers HTTP):** Giá trị của **HTTP Request Headers**.
    -   **Request Body (Body Request):** Nội dung của HTTP Request Body (ví dụ: JSON, XML, text). (Thường dùng cho Web APIs).
    -   **Files (Files):** Files "upload" qua form (dùng encoding `multipart/form-data`).

**7.4. Model Validation (Kiểm Tra Dữ Liệu Model) - " 'Bộ Lọc' " Dữ Liệu "Đầu Vào" "Chính Xác" - " 'Ngăn Chặn' " Dữ Liệu " 'Rác' " Vào Ứng Dụng**

-   **Model Validation (Kiểm Tra Dữ Liệu Model) - " 'Đảm Bảo' " Dữ Liệu " 'Hợp Lệ' " Trước Khi " 'Xử Lý' ":**

    -   **Model Validation** (Kiểm Tra Dữ Liệu Model) là quá trình **"kiểm tra"** **"tính hợp lệ"** và **"tính nhất quán"** của **"dữ liệu Model"** (Data Models) **"trước khi 'xử lý' "** dữ liệu đó trong ứng dụng (ví dụ: "trước khi 'lưu' " dữ liệu vào database, "trước khi 'thực hiện' " "logic nghiệp vụ").
    -   Model Validation "đảm bảo" rằng dữ liệu "đầu vào" (input data) từ người dùng (thông qua HTML Forms, APIs, v.v.) là **" 'hợp lệ' "**, **"đúng định dạng"**, **"đáp ứng"** các **"quy tắc nghiệp vụ"** (business rules) của ứng dụng, và **"tránh"** việc "xử lý" dữ liệu **"không hợp lệ"** hoặc **"dữ liệu 'rác' "** (garbage data) có thể "gây ra" "lỗi" và "vấn đề" cho ứng dụng.

-   **"Các 'Loại' " Validation Phổ Biến:**

    -   **Data Type Validation (Kiểm Tra Kiểu Dữ Liệu):** "Đảm bảo" dữ liệu có **"kiểu dữ liệu" "đúng"** (ví dụ: "tuổi" phải là số nguyên, "email" phải là chuỗi).
    -   **Required Field Validation (Kiểm Tra Trường "Bắt Buộc"):** "Đảm bảo" các trường "bắt buộc" **"không bị 'bỏ trống' "** (not null or empty).
    -   **Range Validation (Kiểm Tra "Khoảng Giá Trị"):** "Đảm bảo" dữ liệu nằm trong **"khoảng giá trị" "cho phép"** (ví dụ: "giá" sản phẩm phải lớn hơn 0, "tuổi" phải từ 18 đến 100).
    -   **String Length Validation (Kiểm Tra "Độ Dài Chuỗi"):** "Đảm bảo" "độ dài" của chuỗi **"không vượt quá"** "giới hạn" (ví dụ: "tên sản phẩm" không quá 255 ký tự, "mật khẩu" phải dài ít nhất 8 ký tự).
    -   **Regular Expression Validation (Kiểm Tra "Định Dạng" Chuỗi):** "Đảm bảo" chuỗi "phù hợp" với **"định dạng" "xác định"** (ví dụ: "email" phải có định dạng email hợp lệ, "số điện thoại" phải có định dạng số điện thoại hợp lệ).
    -   **Custom Validation (Kiểm Tra "Tùy Chỉnh"):** "Thực hiện" các **"quy tắc nghiệp vụ" "phức tạp"** hơn để "kiểm tra" dữ liệu (ví dụ: "kiểm tra" "tên người dùng" "đã tồn tại" trong database chưa, "kiểm tra" "mật khẩu" và "xác nhận mật khẩu" có "khớp nhau" không).

-   **"Các 'Cách' " "Thực Hiện" Model Validation Trong ASP.NET Core MVC:**

    -   **Data Annotations (Attributes "Trang Trí" Dữ Liệu):** "Dùng" các **"attributes"** trong namespace `System.ComponentModel.DataAnnotations` để **"trang trí"** các properties trong Data Model classes và "định nghĩa" các "quy tắc" validation (ví dụ: `[Required]`, `[StringLength]`, `[Range]`, `[EmailAddress]`, `[RegularExpression]`, v.v.). **"Đơn giản"** và "dễ dùng" cho các "quy tắc" validation "cơ bản".

        ```csharp
        public class SanPham // Class "Sản Phẩm" - Data Model với Data Annotations Validation
        {
            public int SanPhamId { get; set; }

            [Required(ErrorMessage = "Tên sản phẩm là bắt buộc.")] // Data Annotation "[Required]" - "Trường 'Tên sản phẩm' là bắt buộc"
            [StringLength(255, ErrorMessage = "Tên sản phẩm không được vượt quá 255 ký tự.")] // Data Annotation "[StringLength]" - "Độ dài tối đa 255 ký tự"
            public string TenSanPham { get; set; }

            [Required(ErrorMessage = "Giá là bắt buộc.")] // Data Annotation "[Required]" - "Trường 'Giá' là bắt buộc"
            [Range(0.01, 1000000, ErrorMessage = "Giá phải lớn hơn 0.")] // Data Annotation "[Range]" - "Giá trị trong khoảng từ 0.01 đến 1000000"
            public decimal Gia { get; set; }

            public string DanhMucSanPham { get; set; }
        }
        ```

    -   **FluentValidation (Fluent Validation Library):** "Dùng" thư viện **FluentValidation** (NuGet package) để "định nghĩa" các **"quy tắc" validation "phức tạp"** hơn bằng code **C# "fluent API"**. "Mạnh mẽ" và "linh hoạt" hơn Data Annotations, "phù hợp" với các ứng dụng "yêu cầu" "validation" "nâng cao".

        ```csharp
        // Cài đặt NuGet package: FluentValidation.AspNetCore

        public class SanPhamValidator : AbstractValidator<SanPham> // Class Validator cho Data Model "SanPham" - "kế thừa" từ AbstractValidator<SanPham>
        {
            public SanPhamValidator() // Constructor
            {
                RuleFor(sp => sp.TenSanPham) // "Quy tắc" validation cho property "TenSanPham"
                    .NotEmpty().WithMessage("Tên sản phẩm là bắt buộc.") // "Bắt buộc" không được "bỏ trống"
                    .MaximumLength(255).WithMessage("Tên sản phẩm không được vượt quá 255 ký tự."); // "Độ dài tối đa" 255 ký tự

                RuleFor(sp => sp.Gia) // "Quy tắc" validation cho property "Gia"
                    .NotEmpty().WithMessage("Giá là bắt buộc.") // "Bắt buộc" không được "bỏ trống"
                    .GreaterThan(0).WithMessage("Giá phải lớn hơn 0."); // "Phải lớn hơn" 0
            }
        }
        ```

-   **"Cách 'Kích Hoạt' " Model Validation Trong MVC:**

    1.  **"Áp dụng" Data Annotations** (attributes) lên các properties Data Model classes **"hoặc"** "tạo" **Validator classes** (FluentValidation).
    2.  Trong **Controller Action Methods**, "kiểm tra" **`ModelState.IsValid` property**. `ModelState.IsValid` sẽ là `true` nếu Model **"hợp lệ"** (vượt qua tất cả các quy tắc validation), `false` nếu Model **"không hợp lệ"** (có lỗi validation).
    3.  Nếu `ModelState.IsValid` là `false`, "trả về" **View** và **"hiển thị" "lỗi validation"** cho người dùng (ví dụ: dùng Tag Helper `<ValidationSummary>`, `<ValidationMessage>`).

**Tổng Kết Chương 7:**

-   Bạn đã "khám phá" **Form Handling** và **Model Binding**, các "công cụ" "quan trọng" để "thu thập" "dữ liệu" từ người dùng và "tạo ra" ứng dụng web MVC "tương tác".
    -   "Hiểu" **HTML Forms** và "vai trò" của Forms trong "tương tác" người dùng trên web.
    -   "Nắm vững" **Form Submission** và "hành trình" dữ liệu từ browser đến server.
    -   Học cách "vận dụng" **Model Binding** để "biến" dữ liệu form thành "đối tượng C#" "dễ dàng".
    -   Biết cách "thực hiện" **Model Validation** bằng Data Annotations và FluentValidation để "kiểm tra" "tính hợp lệ" dữ liệu "đầu vào" từ người dùng.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 8: "Ứng Dụng Thực Tế Của MVC" và "Bước Tiếp Theo" - "MVC Đi Muôn Nơi"**. Chúng ta sẽ "xây dựng" một **"ứng dụng web MVC" "ví dụ" "hoàn chỉnh"** để "lắp ghép" tất cả các "kiến thức" MVC đã học và "thấy" MVC "ứng dụng" trong "thực tế".

Bạn có câu hỏi nào về Form Handling và Model Binding này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" MVC.
