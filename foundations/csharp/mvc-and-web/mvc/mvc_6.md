# Chương 6: ViewData, ViewBag, và ViewContext - " 'Cầu Nối' " Dữ Liệu Từ Controller Đến View - " 'Gửi Gắm' " Thông Tin Cho View - " 'Bí Quyết' " "Chia Sẻ" Dữ Liệu MVC

Chào mừng bạn đến với **Chương 6: ViewData, ViewBag, và ViewContext**! Trong chương này, chúng ta sẽ "khám phá" các **"
cơ chế"** và **"kỹ thuật"** trong ASP.NET Core MVC để **"truyền" "dữ liệu"** (thường là **Model**) từ **Controller
Actions** sang **Views** để View có thể "dùng" dữ liệu đó "hiển thị" "giao diện người dùng". "Truyền dữ liệu" từ
Controller đến View là "cầu nối" "quan trọng" để "kết nối" "logic nghiệp vụ" (Controller, Model) với "giao diện người
dùng" (View) trong ứng dụng MVC.

**Phần 6: ViewData, ViewBag, và ViewContext - " 'Cầu Nối' " Dữ Liệu Từ Controller Đến View**

**6.1. ViewData - " 'Từ Điển' " Dữ Liệu "Truyền Thống" - " 'Hộp Đựng' " Dữ Liệu "Kiểu Cũ" Nhưng " 'Ổn Định' "**

- **ViewData - " 'Từ Điển' " (Dictionary) Để " 'Chia Sẻ' " Dữ Liệu:**

    - **ViewData** là một **`ViewDataDictionary` object**, được "cung cấp" bởi **Controller base class** và **View base
      class** trong ASP.NET Core MVC.
    - ViewData "hoạt động" như một **" 'từ điển' " (dictionary) "khóa-giá trị"** (key-value dictionary) để **"truyền" "
      dữ liệu"** từ **Controller Action** sang **View**.
    - Controller Action có thể **"lưu" "dữ liệu"** vào **ViewData** bằng cách "gán" giá trị cho các **"keys"** (chuỗi
      strings) trong `ViewData` dictionary.
    - View có thể **"lấy" "dữ liệu"** từ **ViewData** bằng cách "truy cập" các **"keys"** "tương ứng" trong `ViewData`
      dictionary.
    - ViewData là "cách" "truyền dữ liệu" **"truyền thống"** và **"cơ bản"** nhất trong ASP.NET MVC.

- **"Cách 'Dùng' " ViewData - " 'Gán' " và " 'Lấy' " Dữ Liệu Qua " 'Khóa' " (Key):**

    - **Trong Controller Action ( " 'Gán' " Dữ Liệu Vào ViewData):** "Dùng" property **`ViewData`** của Controller base
      class (kiểu `ViewDataDictionary`) để "lưu" dữ liệu.

      ```csharp
      public class HomeController : Controller
      {
          public IActionResult Index() // Action Method "Index"
          {
              ViewData["Message"] = "Chào mừng đến với ứng dụng MVC!"; // "Lưu" string vào ViewData với key "Message"
              ViewData["SanPham"] = new SanPham { TenSanPham = "Chuột không dây", Gia = 250000 }; // "Lưu" Object vào ViewData với key "SanPham"
              ViewData["DanhSachDanhMuc"] = new List<string> { "Điện tử", "Văn phòng phẩm", "Sách" }; // "Lưu" List vào ViewData với key "DanhSachDanhMuc"
              return View(); // "Trả về" View "Index"
          }
      }
      ```

    - **Trong View (.cshtml file) ( " 'Lấy' " Dữ Liệu Từ ViewData):** "Dùng" property **`ViewData`** của View base
      class (kiểu `ViewDataDictionary`) để "lấy" dữ liệu. "Ép kiểu" (cast) giá trị lấy ra từ `ViewData` về kiểu dữ
      liệu "thực tế" (vì `ViewData` lưu trữ giá trị kiểu `object`).

      ```cshtml
      @* Index.cshtml *@
      @{
          ViewData["Title"] = "Trang chủ"; // "Thiết lập" ViewData["Title"] trong View (thường dùng trong Layout - _Layout.cshtml)
      }

      <h1>@ViewData["Message"]</h1> // "Lấy" và "hiển thị" string từ ViewData["Message"]

      <h2>Sản phẩm</h2>
      <p>Tên sản phẩm: @(((WebAppMvc.Models.SanPham)ViewData["SanPham"]).TenSanPham)</p> // "Lấy", "ép kiểu", và "hiển thị" property của Object từ ViewData["SanPham"]
      <p>Giá: @(((WebAppMvc.Models.SanPham)ViewData["SanPham"]).Gia)</p>

      <h2>Danh mục sản phẩm</h2>
      <ul>
          @foreach (string danhMuc in (List<string>)ViewData["DanhSachDanhMuc"]) // "Lấy", "ép kiểu", và "duyệt qua" List từ ViewData["DanhSachDanhMuc"]
          {
              <li>@danhMuc</li>
          }
      </ul>
      ```

- **"Ưu Điểm" Của ViewData:**

    - **"Đơn giản" và "dễ dùng":** API của ViewData rất "trực quan" và "dễ học" (dictionary "khóa-giá trị").
    - **"Truyền dữ liệu" "cơ bản":** "Phù hợp" để "truyền" dữ liệu "đơn giản" (ví dụ: string, int, bool, object) từ
      Controller sang View.
    - **"Dynamic" (Kiểu Động):** ViewData là `ViewDataDictionary` (dictionary), "cho phép" bạn "thêm" và "lấy" dữ liệu "
      kiểu động" (dynamic) mà "không cần" "định nghĩa" "kiểu dữ liệu" "rõ ràng" trước.

- **"Nhược Điểm" Của ViewData:**

    - **"Type-Unsafe" (Không An Toàn Kiểu Dữ Liệu):** ViewData lưu trữ giá trị kiểu `object`, bạn cần **"ép kiểu"** (
      cast) giá trị lấy ra từ ViewData về kiểu dữ liệu "thực tế" trong View. "Dễ gây ra" **"lỗi 'ép kiểu' " runtime** (
      runtime casting errors) nếu "ép kiểu" không đúng. "Không được" "kiểm tra" "kiểu dữ liệu" tại thời điểm compile (
      compile-time type checking).
    - **"Khó 'bảo trì' " code View:** Code View "dùng" ViewData có thể trở nên "khó đọc" và "khó bảo trì" hơn khi có quá
      nhiều "ép kiểu" và "key" strings "rải rác" trong View.
    - **"Không 'IntelliSense' " Trong View:** Visual Studio IntelliSense (tính năng "gợi ý code") **"không hoạt động"
      ** "tốt" với ViewData trong Razor Views. "Khó" "khám phá" các "keys" và "kiểu dữ liệu" có sẵn trong ViewData khi
      viết code View.

**6.2. ViewBag - " 'Túi Động' " Dữ Liệu "Tiện Lợi" - " 'Gọn Gàng' " Hơn ViewData, Nhưng Vẫn " 'Kiểu Động' "**

- **ViewBag - " 'Wrapper' " "Tiện Lợi" Hơn Cho ViewData:**

    - **ViewBag** là một property **`dynamic`** (kiểu động) được "cung cấp" bởi **Controller base class** và **View base
      class** trong ASP.NET Core MVC.
    - ViewBag "thực chất" là một **" 'wrapper' "** (lớp bao bọc) "xung quanh" **ViewData**. ViewBag "dùng" ViewData "bên
      dưới" để "lưu trữ" dữ liệu, nhưng "cung cấp" **"cú pháp" "truy cập" dữ liệu "tiện lợi" hơn** (dùng **"dynamic
      properties"** thay vì "key" strings).
    - ViewBag "giúp" code "gọn gàng" hơn so với ViewData, nhưng vẫn **"kế thừa" "nhược điểm" "type-unsafe"** (không an
      toàn kiểu dữ liệu) của ViewData vì ViewBag là `dynamic`.

- **"Cách 'Dùng' " ViewBag - " 'Gán' " và " 'Lấy' " Dữ Liệu Qua " 'Dynamic Properties' " (Properties "Động"):**

    - **Trong Controller Action ( " 'Gán' " Dữ Liệu Vào ViewBag):** "Dùng" property **`ViewBag`** của Controller base
      class (kiểu `dynamic`) để "lưu" dữ liệu. "Gán" giá trị cho các **"dynamic properties"** (tên property "tùy ý" -
      không cần "khai báo" trước).

      ```csharp
      public class HomeController : Controller
      {
          public IActionResult Index() // Action Method "Index"
          {
              ViewBag.Message = "Chào mừng đến với ứng dụng MVC!"; // "Lưu" string vào ViewBag với dynamic property "Message"
              ViewBag.SanPham = new SanPham { TenSanPham = "Chuột không dây", Gia = 250000 }; // "Lưu" Object vào ViewBag với dynamic property "SanPham"
              ViewBag.DanhSachDanhMuc = new List<string> { "Điện tử", "Văn phòng phẩm", "Sách" }; // "Lưu" List vào ViewBag với dynamic property "DanhSachDanhMuc"
              return View(); // "Trả về" View "Index"
          }
      }
      ```

    - **Trong View (.cshtml file) ( " 'Lấy' " Dữ Liệu Từ ViewBag):** "Dùng" property **`ViewBag`** của View base class (
      kiểu `dynamic`) để "lấy" dữ liệu. "Truy cập" dữ liệu thông qua các **"dynamic properties"** (tên property "trùng"
      với tên dynamic property đã "gán" trong Controller). **"Không cần" "ép kiểu"** (cast) khi "lấy" dữ liệu từ
      ViewBag (vì ViewBag là `dynamic`).

      ```cshtml
      @* Index.cshtml *@
      @{
          ViewData["Title"] = "Trang chủ"; // Vẫn dùng ViewData["Title"] (ví dụ)
      }

      <h1>@ViewBag.Message</h1> // "Lấy" và "hiển thị" string từ ViewBag.Message (dynamic property)

      <h2>Sản phẩm</h2>
      <p>Tên sản phẩm: @ViewBag.SanPham.TenSanPham</p> // "Lấy" và "hiển thị" property của Object từ ViewBag.SanPham (dynamic property)
      <p>Giá: @ViewBag.SanPham.Gia</p>

      <h2>Danh mục sản phẩm</h2>
      <ul>
          @foreach (string danhMuc in ViewBag.DanhSachDanhMuc) // "Lấy" và "duyệt qua" List từ ViewBag.DanhSachDanhMuc (dynamic property)
          {
              <li>@danhMuc</li>
          }
      </ul>
      ```

- **"Ưu Điểm" Của ViewBag:**

    - **"Cú Pháp" "Gọn Gàng" Hơn ViewData:** "Truy cập" dữ liệu qua **"dynamic properties"** "dễ đọc" và "dễ viết" hơn
      so với "key" strings của ViewData. "Code View" trở nên "gọn gàng" hơn.
    - **"Dynamic" (Kiểu Động):** Giống ViewData, ViewBag là `dynamic`, "cho phép" "truyền" dữ liệu "kiểu động" mà "không
      cần" "định nghĩa" "kiểu dữ liệu" "rõ ràng" trước.

- **"Nhược Điểm" Của ViewBag:**

    - **"Type-Unsafe" (Không An Toàn Kiểu Dữ Liệu):** Vẫn **"kế thừa" "nhược điểm" "type-unsafe"** của ViewData vì
      ViewBag cũng là `dynamic`. "Dễ gây ra" **"lỗi runtime"** nếu "truy cập" dynamic properties "không tồn tại" hoặc "
      không đúng kiểu". "Không được" "kiểm tra" "kiểu dữ liệu" tại thời điểm compile.
    - **"Khó 'bảo trì' " (ít hơn ViewData, nhưng vẫn còn):** Code View "dùng" ViewBag vẫn có thể trở nên "khó bảo trì"
      hơn khi có quá nhiều dynamic properties "rải rác" trong View.
    - **"Không 'IntelliSense' " Trong View:** Visual Studio IntelliSense **"không hoạt động"** "với dynamic properties"
      của ViewBag trong Razor Views. "Khó" "khám phá" các dynamic properties có sẵn trong ViewBag khi viết code View.

**6.3. ViewContext - " 'Thông Tin Ngữ Cảnh' " View - " 'Toàn Cảnh' " "Môi Trường" View**

- **ViewContext - " 'Bức Tranh Toàn Cảnh' " View - " 'Thông Tin' " "Bao Quanh" View:**

    - **ViewContext** là một property **`ViewContext` object** được "cung cấp" bởi **View base class** trong ASP.NET
      Core MVC.
    - ViewContext "chứa" **"thông tin 'ngữ cảnh' "** (contextual information) về **"View hiện tại"** và **"môi trường"
      ** "thực thi" View. "Không dùng" để "truyền" dữ liệu Model "chính" từ Controller sang View.
    - ViewContext "cung cấp" "quyền truy cập" đến các **"thông tin"** "quan trọng" về View, Controller, HTTP request,
      HTTP response, routing, validation, v.v. trong "phạm vi" của View.

- **"Các 'Thông Tin' " "Hữu Ích" Trong ViewContext:**

    - **`ViewContext.HttpContext`:** "Trả về" **`HttpContext` object** của request hiện tại. `HttpContext` "cung cấp" "
      quyền truy cập" đến **"toàn bộ" "thông tin" HTTP request và response** (headers, cookies, session, user
      authentication, v.v.).

      ```cshtml
      @* View - Truy cập HttpContext thông qua ViewContext.HttpContext *@

      @{
          var request = ViewContext.HttpContext.Request; // "Lấy" HttpRequest object
          var response = ViewContext.HttpContext.Response; // "Lấy" HttpResponse object
          var user = ViewContext.HttpContext.User;       // "Lấy" ClaimsPrincipal (thông tin người dùng đã xác thực)
      }

      <p>Request Path: @ViewContext.HttpContext.Request.Path</p> // "Hiển thị" Request Path
      <p>User Name: @ViewContext.HttpContext.User.Identity.Name</p> // "Hiển thị" User Name (nếu có)
  ```

  -   **`ViewContext.RouteData`:** "Trả về" **`RouteData` object** của request hiện tại. `RouteData` "chứa" **"thông tin" "routing"** (Controller name, Action name, Route Parameters, v.v.) được "trích xuất" từ URL.

      ```cshtml
      @* View - Truy cập RouteData thông qua ViewContext.RouteData *@

      @{
          var routeData = ViewContext.RouteData; // "Lấy" RouteData object
      }

      <p>Controller Name: @ViewContext.RouteData.Values["controller"]</p> // "Hiển thị" Controller Name từ RouteData
      <p>Action Name: @ViewContext.RouteData.Values["action"]</p>       // "Hiển thị" Action Name từ RouteData
      <p>Route Parameter "id": @ViewContext.RouteData.Values["id"]</p>   // "Hiển thị" Route Parameter "id" từ RouteData
  ```

    - **`ViewContext.ModelState`:** "Trả về" **`ModelStateDictionary` object** "chứa" **"trạng thái" "validation"** (
      kiểm tra dữ liệu) của Model. "Dùng" để "hiển thị" **"lỗi validation"** trong View (ví dụ: dùng Tag Helper
      `<ValidationSummary>`, `<ValidationMessage>`).

      ```cshtml
      @* View - Truy cập ModelState thông qua ViewContext.ModelState *@

      @model WebAppMvc.Models.SanPham // "Khai báo" Model cho View

      <form asp-action="Create">
          <div asp-validation-summary="ModelOnly" class="text-danger"></div> // Tag Helper "<ValidationSummary>" - "Hiển thị" "tổng hợp" lỗi validation
          <div class="form-group">
              <label asp-for="TenSanPham" class="control-label"></label> // Tag Helper "<label>"
              <input asp-for="TenSanPham" class="form-control" />       // Tag Helper "<input>"
              <span asp-validation-for="TenSanPham" class="text-danger"></span> // Tag Helper "<ValidationMessage>" - "Hiển thị" lỗi validation cho property "TenSanPham"
          </div>
          // ... (các form fields khác) ...
          <div class="form-group">
              <input type="submit" value="Create" class="btn btn-primary" /> // Button "Submit"
          </div>
      </form>
      ```

    - **`ViewContext.Controller`:** "Trả về" **ControllerContext** object "chứa" **"thông tin" về **Controller** "hiện
      tại" đang "xử lý" request.

    - **`ViewContext.ViewData` và `ViewContext.ViewBag`:** "Trả về" **`ViewDataDictionary`** và **`dynamic` `ViewBag`**
      object "tương ứng" với View hiện tại (chính là ViewData và ViewBag mà chúng ta đã "khám phá" ở trên).

- **"Khi Nào" "Dùng" ViewContext? - "Khi 'Cần' " "Thông Tin 'Ngữ Cảnh' ", Không Phải " 'Truyền' " Dữ Liệu Model:**

    - ViewContext **"không dùng"** để **"truyền" "dữ liệu Model" "chính"** từ Controller sang View (dùng ViewData,
      ViewBag, hoặc ViewModel - xem Chương 7).
    - ViewContext **"dùng"** khi bạn **"cần" "truy cập" "thông tin 'ngữ cảnh' "** (contextual information) về **"View
      hiện tại"** và **"môi trường"** "thực thi" View, ví dụ:
        - "Lấy" "thông tin" HTTP request và response (headers, cookies, session, user authentication, v.v.) -
          `ViewContext.HttpContext`.
        - "Lấy" "thông tin" "routing" (Controller name, Action name, Route Parameters) - `ViewContext.RouteData`.
        - "Hiển thị" "lỗi validation" Model - `ViewContext.ModelState`.
        - "Truy cập" ViewData và ViewBag - `ViewContext.ViewData`, `ViewContext.ViewBag`.

**6.4. "Chọn" "Chiêu Thức" "Truyền Dữ Liệu" Nào? - ViewData vs ViewBag vs ViewContext - " 'Chọn Đúng' " "Công Cụ" Cho "
Đúng 'Việc' "**

- **"So Sánh" ViewData, ViewBag, và ViewContext - " 'Điểm Mạnh', 'Điểm Yếu', và 'Ứng Dụng' ":**

  | Tính Năng               | ViewData                                    | ViewBag                                      | ViewContext                                       |
        | ------------------------- | ------------------------------------------- | --------------------------------------------- | ------------------------------------------------- |
  | **"Kiểu Dữ Liệu"**        | `ViewDataDictionary` (Dictionary)           | `dynamic` (Dynamic Object)                    | `ViewContext` (ViewContext Object)                |
  | **"Type Safety"**         | "Type-Unsafe" (Không an toàn kiểu dữ liệu)   | "Type-Unsafe" (Không an toàn kiểu dữ liệu)     | "Type-Safe" (An toàn kiểu dữ liệu)                  |
  | **"Cú Pháp" "Truy Cập"**  | Dictionary "Keys" (Chuỗi Strings)          | Dynamic Properties (Properties "Động")         | Properties "Chính Chủ" (Properties "Cụ Thể")      |
  | **"IntelliSense"**        | "Không Hỗ Trợ" (Ít IntelliSense)            | "Không Hỗ Trợ" (Không IntelliSense)             | "Hỗ Trợ Tốt" (IntelliSense Đầy Đủ)                 |
  | **"Mục Đích" "Sử Dụng"**  | "Truyền Dữ Liệu" "Cơ Bản" Từ Controller Sang View | "Truyền Dữ Liệu" "Tiện Lợi" (Nhưng Vẫn "Cơ Bản") | "Truy Cập" "Thông Tin 'Ngữ Cảnh' " View và "Môi Trường" |
  | **"Code 'Gọn Gàng' "**     | "Kém Gọn Gàng" (Nhiều "Ép Kiểu", "Key Strings") | "Gọn Gàng Hơn ViewData" (Dynamic Properties)   | "Không Dùng" Để "Truyền Dữ Liệu" Model "Chính"      |
  | **"Code 'Bảo Trì' "**    | "Khó Bảo Trì Hơn" (Type-Unsafe, Key Strings) | "Khó Bảo Trì Hơn" (Type-Unsafe, Dynamic Props) | "Dễ Bảo Trì Hơn" (Type-Safe, Properties "Cụ Thể") |
  | **"Best Practice"**       | "Ít Dùng" Trong Ứng Dụng "Hiện Đại"           | "Ít Dùng" Trong Ứng Dụng "Hiện Đại"             | "Dùng Khi Cần" "Thông Tin 'Ngữ Cảnh' " View        |

- **" 'Lời Khuyên' " - "Chọn Đúng 'Công Cụ' Cho 'Đúng Việc' ":**

    - **ViewData và ViewBag:** "Dùng" cho các trường hợp **"truyền" dữ liệu "đơn giản"** (ví dụ: "thông báo", "tiêu đề
      trang", "dữ liệu 'nhỏ' "). Nhưng **"hạn chế" "sử dụng"** trong ứng dụng "lớn" và "phức tạp" vì "nhược điểm" "
      type-unsafe" và "khó bảo trì".
    - **ViewContext:** "Dùng" khi **"cần" "truy cập" "thông tin 'ngữ cảnh' " View** (HttpContext, RouteData, ModelState,
      v.v.). **"Không dùng"** để **"truyền" dữ liệu Model "chính"** từ Controller sang View.
    - **ViewModel (View Model) (sẽ "học" ở Chương 7):** **" 'Lựa Chọn' " "Tốt Nhất"** và **" 'Được Khuyến Khích' "** để
      **"truyền" "dữ liệu Model" "chính"** từ Controller sang View trong ứng dụng MVC "hiện đại". ViewModel là **"
      Type-Safe"**, **"dễ bảo trì"**, **"IntelliSense" "tốt"**, và "đáp ứng" tốt các "nguyên tắc" thiết kế OOP và MVC.

**Tổng Kết Chương 6:**

- Bạn đã "khám phá" **ViewData**, **ViewBag**, và **ViewContext**, các "cơ chế" và "kỹ thuật" "truyền" dữ liệu từ
  Controller đến View trong ASP.NET Core MVC.
    - "Hiểu" **ViewData là gì** ("từ điển" dữ liệu "truyền thống") và "ưu điểm", "nhược điểm" của ViewData.
    - "Nắm vững" **ViewBag** ("túi động" dữ liệu "tiện lợi") và "hiểu" "cú pháp" "gọn gàng" hơn của ViewBag, nhưng vẫn "
      kế thừa" "nhược điểm" "type-unsafe" của ViewData.
    - "Khám phá" **ViewContext** ("thông tin ngữ cảnh" View) và "biết" cách "dùng" ViewContext để "truy cập" "thông tin"
      View, Controller, HTTP request, v.v.
    - "So sánh" ViewData, ViewBag, ViewContext và "biết" cách **"chọn" "chiêu thức" "truyền dữ liệu" "phù hợp"** cho
      từng "tình huống".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 7: Form Handling và Model Binding - " 'Thu Thập' " Dữ Liệu Từ Người Dùng**. Chúng ta
sẽ "học cách" "xử lý" **HTML Forms** trong MVC Views, "thu thập" **"dữ liệu"** từ người dùng thông qua form submission,
và "vận dụng" **Model Binding** để "biến" dữ liệu form thành **"đối tượng C#"** (Model) "dễ dàng" và "thuận tiện".

Bạn có câu hỏi nào về ViewData, ViewBag, ViewContext này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp"
và "đồng hành" cùng bạn trên con đường "chinh phục" MVC.

