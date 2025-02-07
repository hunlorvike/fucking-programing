# Chương 8: "Ứng Dụng Thực Tế Của MVC" và "Bước Tiếp Theo" - "MVC Đi Muôn Nơi" - " 'Xây Dựng' " Web App MVC "Hoàn Chỉnh" và " 'Vươn Tới' " "Đỉnh Cao" MVC

Chào mừng bạn đến với **Chương 8: "Ứng Dụng Thực Tế Của MVC" và "Bước Tiếp Theo"**, chương "kết thúc" hành trình "khám
phá" MVC trong .NET! Trong chương này, chúng ta sẽ **"lắp ghép"** tất cả các **"kiến thức" MVC "cốt lõi"** đã học từ
Chương 1 đến Chương 7 và **"xây dựng"** một **"ứng dụng web MVC" "ví dụ" "hoàn chỉnh"** để **"thấy"** MVC "ứng dụng"
trong **"thực tế"**. Sau đó, chúng ta sẽ "nhìn lại" "hành trình" MVC và "vạch ra" **" 'bước tiếp theo' "** để bạn "tiếp
tục" "nâng cao" kỹ năng MVC và "trở thành" "cao thủ" MVC.

**Phần 8: "Ứng Dụng Thực Tế Của MVC" và "Bước Tiếp Theo" - "MVC Đi Muôn Nơi"**

**8.1. Ví dụ ứng dụng web ASP.NET Core MVC đơn giản - Ứng Dụng Web MVC "Vỡ Lòng" - " 'Xây Dựng' " Web App MVC "Bước Đầu"
**

- **"Ứng Dụng" Ví Dụ - Web App "Quản Lý Sản Phẩm" (Product Management Web App):**

    - Chúng ta sẽ "xây dựng" một ứng dụng web ASP.NET Core MVC "đơn giản" để "quản lý" **"danh sách sản phẩm"**. Ứng
      dụng sẽ có các "chức năng" CRUD (Create, Read, Update, Delete) "cơ bản" cho "Sản Phẩm":
        1. "Xem" "danh sách" sản phẩm (Index page).
        2. "Xem" "chi tiết" sản phẩm (Details page).
        3. "Thêm" sản phẩm mới (Create page).
        4. "Sửa" thông tin sản phẩm (Edit page).
        5. "Xóa" sản phẩm (Delete page).

- **"Các 'Thành Phần' " MVC "Cần Thiết" Cho Ứng Dụng "Quản Lý Sản Phẩm":**

    - **Model:**
        - **`SanPham` Class (Data Model):** (File: `Models/SanPham.cs`) - "Đại diện" cho "dữ liệu" "Sản Phẩm" (
          SanPhamId, TenSanPham, Gia, DanhMucSanPham). (Đã "xây dựng" ở các chương trước).
    - **View:**
        - **`Index.cshtml` (View "Danh Sách Sản Phẩm"):** (File: `Views/SanPham/Index.cshtml`) - "Hiển thị" "danh sách"
          sản phẩm (dùng Model `List<SanPham>`).
        - **`Details.cshtml` (View "Chi Tiết Sản Phẩm"):** (File: `Views/SanPham/Details.cshtml`) - "Hiển thị" "thông
          tin chi tiết" của một sản phẩm (dùng Model `SanPham`).
        - **`Create.cshtml` (View "Thêm Sản Phẩm"):** (File: `Views/SanPham/Create.cshtml`) - "Hiển thị" form để "thêm"
          sản phẩm mới (dùng Model `SanPham`).
        - **`Edit.cshtml` (View "Sửa Sản Phẩm"):** (File: `Views/SanPham/Edit.cshtml`) - "Hiển thị" form để "sửa" thông
          tin sản phẩm (dùng Model `SanPham`).
        - **`Delete.cshtml` (View "Xóa Sản Phẩm"):** (File: `Views/SanPham/Delete.cshtml`) - "Hiển thị" form "xác nhận
          xóa" sản phẩm (dùng Model `SanPham`).
        - **`_Layout.cshtml` (Layout View):** (File: `Views/Shared/_Layout.cshtml`) - "Khung sườn" "chung" cho các trang
          web. (Dùng lại Layout "mặc định" của ASP.NET Core MVC template).
    - **Controller:**
        - **`SanPhamController` Class (Controller "Sản Phẩm"):** (File: `Controllers/SanPhamController.cs`) - "Xử lý"
          các request "liên quan" đến "Sản Phẩm" (xem danh sách, xem chi tiết, thêm, sửa, xóa).
        - **Action Methods:** `Index()`, `Details(int id)`, `Create()`, `Create(SanPham sanPham)`, `Edit(int id)`,
          `Edit(int id, SanPham sanPham)`, `Delete(int id)`, `DeleteConfirmed(int id)`. (Các Action Methods CRUD "cơ
          bản" - như ví dụ ở Chương 4, 5, 6).
    - **Data Access (Truy Cập Dữ Liệu):**
        - **`MyDbContext` Class (Data Context):** (File: `Data/MyDbContext.cs`) - "Quản lý" "kết nối" database và "truy
          cập" database bằng EF Core. (Dùng lại `MyDbContext` "đơn giản" với `DbSet<SanPham>` - như ví dụ ở Chương 2, 3,
          4).
        - **In-Memory Database (Database "Trong Bộ Nhớ"):** "Dùng" In-Memory Database của EF Core để "đơn giản hóa" ví
          dụ và "không cần" "cài đặt" database server "thực tế". (Bạn có thể "chuyển sang" "kết nối" database server "
          thực tế" - ví dụ: SQL Server LocalDB - sau khi "hiểu" ví dụ "cơ bản").

- **"Code Ứng Dụng Web MVC" "Quản Lý Sản Phẩm" (Code "Hoàn Chỉnh"):**

  **(File: `Models/SanPham.cs` - Data Model `SanPham`):**

  ```csharp
  // (Code Class SanPham.cs - "giữ nguyên" như ví dụ ở Chương 6 về Model Binding và Validation)
  public class SanPham
  {
      public int SanPhamId { get; set; }

      [Required(ErrorMessage = "Tên sản phẩm là bắt buộc.")]
      [StringLength(255, ErrorMessage = "Tên sản phẩm không được vượt quá 255 ký tự.")]
      public string TenSanPham { get; set; }

      [Required(ErrorMessage = "Giá là bắt buộc.")]
      [Range(0.01, 1000000, ErrorMessage = "Giá phải lớn hơn 0.")]
      public decimal Gia { get; set; }

      public string DanhMucSanPham { get; set; }
  }
  ```

  **(File: `Data/MyDbContext.cs` - Data Context `MyDbContext`):**

  ```csharp
  using Microsoft.EntityFrameworkCore;

  public class MyDbContext : DbContext // Data Context "kế thừa" từ DbContext
  {
      public MyDbContext(DbContextOptions<MyDbContext> options) : base(options) // Constructor - "nhận" options từ Dependency Injection
      {
      }

      public DbSet<SanPham> SanPhams { get; set; } // DbSet<SanPham> property - "ánh xạ" bảng SanPhams
  }
  ```

  **(File: `Controllers/SanPhamController.cs` - Controller `SanPhamController`):**

  ```csharp
  using Microsoft.AspNetCore.Mvc;
  using Microsoft.EntityFrameworkCore;
  using WebAppMvc.Models; // "Nhập" namespace Models

  public class SanPhamController : Controller // Class "SanPhamController" "kế thừa" từ Controller base class
  {
      private readonly MyDbContext _context; // "Dependency Injection" - "Inject" DbContext

      public SanPhamController(MyDbContext context) // Constructor Injection
      {
          _context = context;
      }

      // Action Method "Index" - "Xem danh sách sản phẩm"
      public async Task<IActionResult> Index()
      {
          return View(await _context.SanPhams.ToListAsync()); // "Lấy" danh sách sản phẩm từ database bằng EF Core và "truyền" cho View "Index"
      }

      // Action Method "Details" - "Xem chi tiết sản phẩm"
      public async Task<IActionResult> Details(int? id)
      {
          if (id == null)
          {
              return NotFound(); // "Trả về" HTTP 404 Not Found nếu ID không có
          }

          var sanPham = await _context.SanPhams
              .FirstOrDefaultAsync(m => m.SanPhamId == id); // "Lấy" sản phẩm theo ID từ database bằng EF Core
          if (sanPham == null)
          {
              return NotFound(); // "Trả về" HTTP 404 Not Found nếu không "tìm" thấy sản phẩm
          }

          return View(sanPham); // "Truyền" sản phẩm cho View "Details"
      }

      // Action Method "Create" - "Hiển thị form 'thêm sản phẩm' " (GET request)
      public IActionResult Create()
      {
          return View(); // "Trả về" View "Create" (form "thêm sản phẩm")
      }

      // Action Method "Create" - "Xử lý form 'thêm sản phẩm' " (POST request)
      [HttpPost]
      [ValidateAntiForgeryToken] // "Bảo vệ" chống CSRF attack
      public async Task<IActionResult> Create([Bind("SanPhamId,TenSanPham,Gia,DanhMucSanPham")] SanPham sanPham) // Model Binding - "Ràng buộc" form data vào đối tượng "SanPham"
      {
          if (ModelState.IsValid) // "Validation" Model
          {
              _context.Add(sanPham); // "Thêm" sản phẩm vào DbSet<SanPham> (EF Core)
              await _context.SaveChangesAsync(); // "Lưu" thay đổi vào database (EF Core)
              return RedirectToAction(nameof(Index)); // "Chuyển hướng" đến Action "Index" (xem danh sách sản phẩm)
          }
          return View(sanPham); // Nếu Model "không hợp lệ", "trả về" lại View "Create" (form) và "hiển thị" "lỗi validation"
      }

      // Action Method "Edit" - "Hiển thị form 'sửa sản phẩm' " (GET request)
      public async Task<IActionResult> Edit(int? id)
      {
          if (id == null)
          {
              return NotFound(); // "Trả về" HTTP 404 Not Found nếu ID không có
          }

          var sanPham = await _context.SanPhams.FindAsync(id); // "Lấy" sản phẩm theo ID từ database bằng EF Core
          if (sanPham == null)
          {
              return NotFound(); // "Trả về" HTTP 404 Not Found nếu không "tìm" thấy sản phẩm
          }
          return View(sanPham); // "Truyền" sản phẩm cho View "Edit" (form "sửa sản phẩm")
      }

      // Action Method "Edit" - "Xử lý form 'sửa sản phẩm' " (POST request)
      [HttpPost]
      [ValidateAntiForgeryToken] // "Bảo vệ" chống CSRF attack
      public async Task<IActionResult> Edit(int id, [Bind("SanPhamId,TenSanPham,Gia,DanhMucSanPham")] SanPham sanPham) // Model Binding - "Ràng buộc" form data vào đối tượng "SanPham", Bind attribute - "chỉ bind" các properties "chỉ định"
      {
          if (id != sanPham.SanPhamId)
          {
              return NotFound(); // "Trả về" HTTP 404 Not Found nếu ID không "khớp"
          }

          if (ModelState.IsValid) // "Validation" Model
          {
              try
              {
                  _context.Update(sanPham); // "Cập nhật" sản phẩm trong DbSet<SanPham> (EF Core)
                  await _context.SaveChangesAsync(); // "Lưu" thay đổi vào database (EF Core)
              }
              catch (DbUpdateConcurrencyException) // "Xử lý" lỗi "đụng độ" (concurrency) khi "cập nhật"
              {
                  if (!SanPhamExists(sanPham.SanPhamId))
                  {
                      return NotFound(); // "Trả về" HTTP 404 Not Found nếu sản phẩm "không còn tồn tại"
                  }
                  else
                  {
                      throw; // "Ném lại" exception nếu lỗi không phải do "sản phẩm không còn tồn tại"
                  }
              }
              return RedirectToAction(nameof(Index)); // "Chuyển hướng" đến Action "Index" (xem danh sách sản phẩm)
          }
          return View(sanPham); // Nếu Model "không hợp lệ", "trả về" lại View "Edit" (form) và "hiển thị" "lỗi validation"
      }

      // Action Method "Delete" - "Hiển thị form 'xác nhận xóa sản phẩm' " (GET request)
      public async Task<IActionResult> Delete(int? id)
      {
          if (id == null)
          {
              return NotFound(); // "Trả về" HTTP 404 Not Found nếu ID không có
          }

          var sanPham = await _context.SanPhams
              .FirstOrDefaultAsync(m => m.SanPhamId == id); // "Lấy" sản phẩm theo ID từ database bằng EF Core
          if (sanPham == null)
          {
              return NotFound(); // "Trả về" HTTP 404 Not Found nếu không "tìm" thấy sản phẩm
          }

          return View(sanPham); // "Truyền" sản phẩm cho View "Delete" (form "xác nhận xóa")
      }

      // Action Method "DeleteConfirmed" - "Xử lý xóa sản phẩm" (POST request - sau khi người dùng "xác nhận" xóa)
      [HttpPost, ActionName("Delete")] // "Đánh dấu" Action Method này là Action "Delete" và chỉ "xử lý" request POST
      [ValidateAntiForgeryToken] // "Bảo vệ" chống CSRF attack
      public async Task<IActionResult> DeleteConfirmed(int id) // "Tham số" "id" - ID sản phẩm cần "xóa"
      {
          var sanPham = await _context.SanPhams.FindAsync(id); // "Lấy" sản phẩm theo ID từ database bằng EF Core
          if (sanPham != null) // "Kiểm tra" xem có "tìm" thấy sản phẩm không
          {
              _context.SanPhams.Remove(sanPham); // "Xóa" sản phẩm khỏi DbSet<SanPham> (EF Core)
              await _context.SaveChangesAsync(); // "Lưu" thay đổi vào database (EF Core)
          }
          return RedirectToAction(nameof(Index)); // "Chuyển hướng" đến Action "Index" (xem danh sách sản phẩm)
      }

      private bool SanPhamExists(int id) // "Phương thức" "kiểm tra" sản phẩm có "tồn tại" trong database không (dùng cho mục đích "kiểm tra" concurrency)
      {
          return _context.SanPhams.Any(e => e.SanPhamId == id); // "Kiểm tra" bằng EF Core Any()
      }
  }
  ```

  **(File: `Views/SanPham/Index.cshtml` - View "Danh Sách Sản Phẩm"):**

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
          @foreach (var item in Model)
          {
              <tr>
                  <td>
                      @Html.DisplayFor(modelItem => item.SanPhamId)
                  </td>
                  <td>
                      @Html.DisplayFor(modelItem => item.TenSanPham)
                  </td>
                  <td>
                      @Html.DisplayFor(modelItem => item.Gia)
                  </td>
                  <td>
                      @Html.DisplayFor(modelItem => item.DanhMucSanPham)
                  </td>
                  <td>
                      <a asp-action="Edit" asp-route-id="@item.SanPhamId">Sửa</a> |
                      <a asp-action="Details" asp-route-id="@item.SanPhamId">Chi tiết</a> |
                      <a asp-action="Delete" asp-route-id="@item.SanPhamId">Xóa</a>
                  </td>
              </tr>
          }
      </tbody>
  </table>
  ```

  **(File: `Views/SanPham/Details.cshtml` - View "Chi Tiết Sản Phẩm"):**

  ```cshtml
  @model WebAppMvc.Models.SanPham

  @{
      ViewData["Title"] = "Chi tiết Sản Phẩm";
  }

  <h1>@ViewData["Title"]</h1>

  <div>
      <h4>SanPham</h4>
      <hr />
      <dl class="row">
          <dt class = "col-sm-2">
              @Html.DisplayNameFor(model => model.SanPhamId)
          </dt>
          <dd class = "col-sm-10">
              @Html.DisplayFor(model => model.SanPhamId)
          </dd>
          <dt class = "col-sm-2">
              @Html.DisplayNameFor(model => model.TenSanPham)
          </dt>
          <dd class = "col-sm-10">
              @Html.DisplayFor(model => model.TenSanPham)
          </dd>
          <dt class = "col-sm-2">
              @Html.DisplayNameFor(model => model.Gia)
          </dt>
          <dd class = "col-sm-10">
              @Html.DisplayFor(model => model.Gia)
          </dd>
          <dt class = "col-sm-2">
              @Html.DisplayNameFor(model => model.DanhMucSanPham)
          </dt>
          <dd class = "col-sm-10">
              @Html.DisplayFor(model => model.DanhMucSanPham)
          </dd>
      </dl>
  </div>
  <div>
      <a asp-action="Edit" asp-route-id="@Model?.SanPhamId">Sửa</a> |
      <a asp-action="Index">Quay lại danh sách</a>
  </div>
  ```

  **(File: `Views/SanPham/Create.cshtml` - View "Thêm Sản Phẩm"):**

  ```cshtml
  @model WebAppMvc.Models.SanPham

  @{
      ViewData["Title"] = "Thêm Sản Phẩm Mới";
  }

  <h1>@ViewData["Title"]</h1>

  <h4>SanPham</h4>
  <hr />
  <div class="row">
      <div class="col-md-4">
          <form asp-action="Create">
              <div asp-validation-summary="ModelOnly" class="text-danger"></div>
              <div class="form-group">
                  <label asp-for="TenSanPham" class="control-label"></label>
                  <input asp-for="TenSanPham" class="form-control" />
                  <span asp-validation-for="TenSanPham" class="text-danger"></span>
              </div>
              <div class="form-group">
                  <label asp-for="Gia" class="control-label"></label>
                  <input asp-for="Gia" class="form-control" />
                  <span asp-validation-for="Gia" class="text-danger"></span>
              </div>
              <div class="form-group">
                  <label asp-for="DanhMucSanPham" class="control-label"></label>
                  <input asp-for="DanhMucSanPham" class="form-control" />
                  <span asp-validation-for="DanhMucSanPham" class="text-danger"></span>
              </div>
              <div class="form-group">
                  <input type="submit" value="Create" class="btn btn-primary" />
              </div>
          </form>
      </div>
  </div>

  <div>
      <a asp-action="Index">Quay lại danh sách</a>
  </div>

  @section Scripts {
      @{await Html.RenderPartialAsync("_ValidationScriptsPartial");}
  }
  ```

  **(File: `Views/SanPham/Edit.cshtml` - View "Sửa Sản Phẩm"):**

  ```cshtml
  @model WebAppMvc.Models.SanPham

  @{
      ViewData["Title"] = "Sửa Sản Phẩm";
  }

  <h1>@ViewData["Title"]</h1>

  <h4>SanPham</h4>
  <hr />
  <div class="row">
      <div class="col-md-4">
          <form asp-action="Edit">
              <div asp-validation-summary="ModelOnly" class="text-danger"></div>
              <input type="hidden" asp-for="SanPhamId" />
              <div class="form-group">
                  <label asp-for="TenSanPham" class="control-label"></label>
                  <input asp-for="TenSanPham" class="form-control" />
                  <span asp-validation-for="TenSanPham" class="text-danger"></span>
              </div>
              <div class="form-group">
                  <label asp-for="Gia" class="control-label"></label>
                  <input asp-for="Gia" class="form-control" />
                  <span asp-validation-for="Gia" class="text-danger"></span>
              </div>
              <div class="form-group">
                  <label asp-for="DanhMucSanPham" class="control-label"></label>
                  <input asp-for="DanhMucSanPham" class="form-control" />
                  <span asp-validation-for="DanhMucSanPham" class="text-danger"></span>
              </div>
              <div class="form-group">
                  <input type="submit" value="Save" class="btn btn-primary" />
              </div>
          </form>
      </div>
  </div>

  <div>
      <a asp-action="Index">Quay lại danh sách</a>
  </div>

  @section Scripts {
      @{await Html.RenderPartialAsync("_ValidationScriptsPartial");}
  }
  ```

  **(File: `Views/SanPham/Delete.cshtml` - View "Xóa Sản Phẩm"):**

  ```cshtml
  @model WebAppMvc.Models.SanPham

  @{
      ViewData["Title"] = "Xóa Sản Phẩm";
  }

  <h1>@ViewData["Title"]</h1>

  <h3>Bạn có chắc chắn muốn xóa sản phẩm này?</h3>
  <div>
      <h4>SanPham</h4>
      <hr />
      <dl class="row">
          <dt class = "col-sm-2">
              @Html.DisplayNameFor(model => model.SanPhamId)
          </dt>
          <dd class = "col-sm-10">
              @Html.DisplayFor(model => model.SanPhamId)
          </dd>
          <dt class = "col-sm-2">
              @Html.DisplayNameFor(model => model.TenSanPham)
          </dt>
          <dd class = "col-sm-10">
              @Html.DisplayFor(model => model.TenSanPham)
          </dd>
          <dt class = "col-sm-2">
              @Html.DisplayNameFor(model => model.Gia)
          </dt>
          <dd class = "col-sm-10">
              @Html.DisplayFor(model => model.Gia)
          </dd>
          <dt class = "col-sm-2">
              @Html.DisplayNameFor(model => model.DanhMucSanPham)
          </dt>
          <dd class = "col-sm-10">
              @Html.DisplayFor(model => model.DanhMucSanPham)
          </dd>
      </dl>

      <form asp-action="Delete">
          <input type="hidden" asp-for="SanPhamId" />
          <input type="submit" value="Delete" class="btn btn-danger" /> |
          <a asp-action="Index">Quay lại danh sách</a>
      </form>
  </div>
  ```

**(File: `Views/Shared/_ValidationScriptsPartial.cshtml` - Partial View "Validation Scripts") - COMPLETED CODE:**

```cshtml
@* Partial View "Validation Scripts" - "chứa" JavaScript validation scripts (jQuery Validation, jQuery Validation Unobtrusive) - được "dùng chung" cho các Views cần client-side validation *@
<environment include="Development">
    <script src="~/lib/jquery-validation/dist/jquery.validate.js"></script>
    <script src="~/lib/jquery-validation-unobtrusive/jquery.validate.unobtrusive.js"></script>
</environment>
<environment exclude="Development">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.17.0/jquery.validate.min.js"
            asp-fallback-src="~/lib/jquery-validation/dist/jquery.validate.min.js"
            asp-fallback-test="window.jQuery && window.jQuery.validator"
            crossorigin="anonymous"
            integrity="sha384-rZfj/ogBloos6mSA2zWY8/aqSDdxZVZxIUgY0ilBZg+g8kKxCsvVtBndlN27c/RhfzESg==">
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validation-unobtrusive/3.2.9/jquery.validate.unobtrusive.min.js"
            asp-fallback-src="~/lib/jquery-validation-unobtrusive/jquery.validate.unobtrusive.min.js"
            asp-fallback-test="window.jQuery && window.jQuery.validator && window.jQuery.validator.unobtrusive"
            crossorigin="anonymous"
            integrity="sha384-if2liw8ho3US5pDxNNtjClrneTqhUT3maw9vFGMEcunvTyhiuZ/CkfBXcPixKks8H">
    </script>
</environment>
```

**Cách Chạy Ứng Dụng Web MVC "Quản Lý Sản Phẩm":**

1. **Tạo Dự Án ASP.NET Core MVC Mới (Nếu Cần):** Nếu bạn chưa có dự án ASP.NET Core MVC, hãy tạo một dự án mới trong
   Visual Studio hoặc bằng .NET CLI:
    - **Visual Studio:** `Create a new project` -> `ASP.NET Core Web App (Model-View-Controller)` -> `Next` ->
      `Configure your new project` -> `Create`.
    - **.NET CLI:** Chạy lệnh `dotnet new mvc -o WebAppMvc` trong command line.

2. **Thêm Code Files Vào Dự Án:** "Thêm" các code files ( `SanPham.cs`, `MyDbContext.cs`, `SanPhamController.cs`,
   `Index.cshtml`, `Details.cshtml`, `Create.cshtml`, `Edit.cshtml`, `Delete.cshtml`,
   `_ValidationScriptsPartial.cshtml`) vào các thư mục "tương ứng" trong dự án của bạn (nếu chưa có, hãy "tạo" các thư
   mục `Models`, `Data`, `Controllers`, `Views/SanPham`, `Views/Shared`). "Copy" code từ các ví dụ trên vào các file
   này.

3. **Cấu Hình Database In-Memory (Trong Bộ Nhớ):** Trong `Program.cs` (hoặc `Startup.cs`), "đảm bảo" bạn đã "cấu hình" *
   *In-Memory Database** cho EF Core (như ví dụ ở Chương 2):

   ```csharp
   // Program.cs (hoặc Startup.cs - ConfigureServices method)
   builder.Services.AddDbContext<MyDbContext>(options =>
       options.UseInMemoryDatabase("WebAppMvcDatabase")); // "Cấu hình" In-Memory Database với tên "WebAppMvcDatabase"
   ```

4. **Chạy Ứng Dụng:**
    - **Visual Studio:** Bấm nút "Run" (biểu tượng Play) hoặc bấm `Ctrl+F5` (Start without debugging).
    - **.NET CLI:** "Di chuyển" đến thư mục dự án trong command line và chạy lệnh `dotnet run`.

5. **Truy Cập Ứng Dụng Trên Trình Duyệt Web:** Ứng dụng web sẽ "chạy" trên URL (thường là `https://localhost:xxxx` hoặc
   `http://localhost:xxxx` - cổng port `xxxx` có thể khác nhau tùy theo cấu hình). "Mở" trình duyệt web và "truy cập"
   URL này để "thử nghiệm" ứng dụng "Quản Lý Sản Phẩm".

6. **"Thử Nghiệm" Các Chức Năng CRUD:**
    - **Xem danh sách sản phẩm:** Truy cập URL trang chủ hoặc URL `/SanPham/Index` để "xem" "danh sách" sản phẩm (ban
      đầu có thể "trống" nếu chưa có dữ liệu).
    - **Thêm sản phẩm mới:** Bấm link "Thêm Sản Phẩm Mới" để "mở" trang "thêm sản phẩm", "nhập" thông tin sản phẩm, và
      bấm nút "Create" để "thêm" sản phẩm vào thư viện.
    - **Xem chi tiết sản phẩm:** Bấm link "Chi tiết" (Details) ở mỗi hàng sản phẩm để "xem" "thông tin chi tiết" của sản
      phẩm đó.
    - **Sửa sản phẩm:** Bấm link "Sửa" (Edit) ở mỗi hàng sản phẩm để "mở" trang "sửa sản phẩm", "sửa đổi" thông tin sản
      phẩm, và bấm nút "Save" để "lưu" thay đổi.
    - **Xóa sản phẩm:** Bấm link "Xóa" (Delete) ở mỗi hàng sản phẩm để "mở" trang "xác nhận xóa", "xem lại" thông tin
      sản phẩm cần xóa, và bấm nút "Delete" để "xóa" sản phẩm khỏi thư viện.

**8.2. "Phân Tích" Ví Dụ MVC - " 'Mổ Xẻ' " Code MVC "Thực Tế" - " 'Hiểu Sâu' " "Sức Mạnh" MVC**

- **"Phân Tách" "Rõ Ràng" "3 Thành Phần" MVC:** Ứng dụng "Quản Lý Sản Phẩm" "ví dụ" "minh họa" rõ ràng "cấu trúc" MVC "3
  tầng":
    - **Model (`SanPham.cs`):** "Chứa" Data Model class `SanPham` - "khuôn mẫu" cho dữ liệu sản phẩm.
    - **View (thư mục `Views/SanPham/`):** "Chứa" các Razor Views (`Index.cshtml`, `Details.cshtml`, `Create.cshtml`,
      `Edit.cshtml`, `Delete.cshtml`) - "giao diện người dùng" để "hiển thị" dữ liệu sản phẩm và "tương tác" với người
      dùng.
    - **Controller (`SanPhamController.cs`):** "Điều phối" "luồng" ứng dụng, "tương tác" với Model (DbContext) để "lấy"
      và "lưu" dữ liệu sản phẩm, "chọn" View phù hợp, và "truyền" dữ liệu Model cho View.

- **"CRUD Operations" "Hoàn Chỉnh" Với MVC:** Ứng dụng "ví dụ" "hiện thực hóa" các thao tác CRUD "cơ bản" (Create, Read,
  Update, Delete) cho "Sản Phẩm" bằng kiến trúc MVC:
    - **Create:** Action Methods `Create()` (GET và POST) và View `Create.cshtml` để "thêm" sản phẩm mới.
    - **Read:** Action Methods `Index()` và `Details()` và Views `Index.cshtml` và `Details.cshtml` để "xem" danh sách
      và "chi tiết" sản phẩm.
    - **Update:** Action Methods `Edit()` (GET và POST) và View `Edit.cshtml` để "sửa" thông tin sản phẩm.
    - **Delete:** Action Methods `Delete()` và `DeleteConfirmed()` và View `Delete.cshtml` để "xóa" sản phẩm.

- **"Ứng Dụng" Các "Kiến Thức" MVC "Đã Học":** Ví dụ "ứng dụng" "tổng hợp" các "kiến thức" MVC "đã học" trong các chương
  trước:
    - **Model Binding:** Action Methods `Create(SanPham sanPham)` và `Edit(int id, SanPham sanPham)` "dùng" Model
      Binding để "biến" dữ liệu form thành đối tượng `SanPham`.
    - **Model Validation:** Data Annotations (`[Required]`, `[StringLength]`, `[Range]`) trong Data Model `SanPham` và
      `ModelState.IsValid` trong Controller Actions để "kiểm tra" "tính hợp lệ" dữ liệu "đầu vào" từ form.
    - **ViewData:** View `Index.cshtml` và các Views khác "dùng" `ViewData["Title"]` để "thiết lập" và "hiển thị" "tiêu
      đề trang".
    - **Tag Helpers và HTML Helpers:** Các Views "dùng" Tag Helpers (`<a asp-action>`, `<form asp-action>`,
      `<input asp-for>`, `<label asp-for>`, `<ValidationSummary>`, `<ValidationMessage>`) và HTML Helpers (
      `@Html.DisplayNameFor()`, `@Html.DisplayFor()`) để "tạo ra" "giao diện người dùng" và "tương tác" với Model và
      Controller.
    - **Routing:** Routing "mặc định" (Convention-Based Routing) "ánh xạ" URLs đến Controller Actions (ví dụ:
      `/SanPham/Index`, `/SanPham/Details/123`, `/SanPham/Create`, `/SanPham/Edit/456`, `/SanPham/Delete/789`).

**8.3. "Lời Khuyên" "Chân Thành" Để "Trở Thành" "Cao Thủ" MVC - " 'Bước Tiếp Theo' " Trên Con Đường MVC**

- **" 'Thực Hành' " "Nhiều Hơn Nữa":** "Ứng dụng" "Quản Lý Sản Phẩm" chỉ là "bước khởi đầu". Hãy **"thực hành" "xây
  dựng" thêm "nhiều" ứng dụng web MVC "khác nhau"**, từ "đơn giản" đến "phức tạp", để "rèn luyện" "kỹ năng" MVC và "làm
  chủ" MVC "thực sự".
- **" "Khám Phá' " Các " 'Tính Năng' " "Nâng Cao" Của MVC:** ASP.NET Core MVC còn rất nhiều "tính năng" "nâng cao"
  khác (ví dụ: View Components, Areas, Filters, Model Binders "tùy chỉnh", Tag Helpers "tùy chỉnh", API Controllers,
  Razor Pages, v.v.). Hãy "tiếp tục" "tìm hiểu" và "khám phá" để "nâng cao" "trình độ" MVC của bạn lên "đỉnh cao".
- **" "Học Tập' " "Thiết Kế" Ứng Dụng Web MVC "Chuyên Nghiệp":** "Nghiên cứu" các "nguyên tắc" "thiết kế" ứng dụng web
  MVC "tốt" (ví dụ: **SOLID principles**, **Design Patterns**, **Clean Architecture**, **Domain-Driven Design - DDD**,
  v.v.). "Học cách" "thiết kế" "kiến trúc" MVC "linh hoạt", "mạnh mẽ", và "dễ bảo trì" cho các ứng dụng web "quy mô
  lớn".
- **" "Xây Dựng' " Ứng Dụng Web MVC "Thực Tế":** "Tham gia" vào các dự án "thực tế" (real-world projects) (ví dụ: dự
  án "mã nguồn mở", dự án "cá nhân", dự án "công ty") để "ứng dụng" kiến thức MVC đã học và "học hỏi" "kinh nghiệm" "
  thực tế" từ các lập trình viên "khác".
- **" "Theo Dõi' " "Xu Hướng" MVC "Mới Nhất":** ASP.NET Core MVC (và .NET nói chung) "luôn" "phát triển" và "cập nhật"
  các "tính năng" mới, "công nghệ" mới, và "best practices" mới. "Theo dõi" "blog" Microsoft .NET, "tài liệu" "chính
  thức", và "cộng đồng" .NET để "cập nhật" "kiến thức" MVC và "không ngừng" "tiến bộ".

**8.4. "Tài Nguyên" "Bổ Ích" Để "Học Sâu" Về MVC - " 'Kho Tàng' " "Kiến Thức" MVC "Bao La"**

- **"Tài Liệu 'Chính Chủ' " Của Microsoft:**
    - **ASP.NET Core MVC documentation:
      ** [https://learn.microsoft.com/en-us/aspnet/core/mvc/overview](https://learn.microsoft.com/en-us/aspnet/core/mvc/overview) (
      Tài liệu "đầy đủ" và "chính xác" nhất về ASP.NET Core MVC).
    - **ASP.NET Core tutorials:
      ** [https://learn.microsoft.com/en-us/aspnet/core/tutorials/](https://learn.microsoft.com/en-us/aspnet/core/tutorials/) (
      Các tutorials "thực hành" "từng bước" để "học" ASP.NET Core MVC).
    - **.NET API Browser:** [https://apisof.net/](https://apisof.net/) (Tra cứu API documentation cho các classes và
      methods của ASP.NET Core MVC framework).

- **"Sách" Về ASP.NET Core MVC:**
    - **"Pro ASP.NET Core MVC"** by Adam Freeman (Sách "kinh điển" và "toàn diện" về ASP.NET Core MVC).
    - **"ASP.NET Core in Action"** by Andrew Lock (Sách "thực tế" và "chú trọng" "thực hành" về ASP.NET Core MVC).
    - **"The ASP.NET Core MVC Tutorial"** by Valerij Leschenko (Sách "miễn phí" online, "dành cho người mới bắt đầu" về
      ASP.NET Core MVC).

- **"Trang Web" và "Blog" Về ASP.NET Core MVC:**
    - **Microsoft .NET Blog:** [https://devblogs.microsoft.com/dotnet/](https://devblogs.microsoft.com/dotnet/) (Blog
      chính thức của Microsoft .NET, "cập nhật" các "tin tức", "tính năng" mới, và "best practices" về ASP.NET Core và
      MVC).
    - **ASP.NET Community Standup:** [https://www.youtube.com/dotnet](https://www.youtube.com/dotnet) (YouTube channel
      của .NET team, có các buổi live stream về ASP.NET Core và MVC).
    - **Stack Overflow:
      ** [https://stackoverflow.com/questions/tagged/asp.net-mvc-core](https://stackoverflow.com/questions/tagged/asp.net-mvc-core) (
      Trang hỏi đáp Stack Overflow, tìm kiếm và đặt câu hỏi về ASP.NET Core MVC).

- **"Khóa Học Online" Về ASP.NET Core MVC:**
    - **Microsoft Learn:** [https://learn.microsoft.com/en-us/](https://learn.microsoft.com/en-us/) (Tìm kiếm các
      modules và learning paths về "ASP.NET Core", "MVC", "Web Development").
    - **Udemy, Coursera, Pluralsight, v.v.:** Các nền tảng học trực tuyến có "vô số" khóa học về ASP.NET Core MVC từ "cơ
      bản" đến "nâng cao". "Chọn" khóa học "phù hợp" với "trình độ" và "mục tiêu" của bạn.

**8.5. "Lời Chúc" "Kết Thúc Hành Trình MVC" - " 'Chúc Bạn Thành Công Trên Con Đường Web Dev MVC' "**

Chúc mừng bạn đã "hoàn thành" "hành trình" "khám phá" MVC trong .NET từ "A đến Z" (cơ bản đến nâng cao)!

Bạn đã "bước qua" một "chặng đường" "dài hơi", từ những "khái niệm" "vỡ lòng" về MVC, "các thành phần" MVC, Routing,
Model Binding, Form Handling, đến "ứng dụng" MVC trong "thực tế". Hy vọng rằng bạn đã có được một "hành trang" "vững
chắc" để "chinh phục" thế giới phát triển ứng dụng web MVC và "xây dựng" các ứng dụng web .NET "tuyệt vời"!

**"Lời khuyên" "chân thành" "khép lại":**

- **"MVC là 'kiến trúc' " "mạnh mẽ"**, nhưng cũng cần **"học tập"** và **"thực hành"** "không ngừng nghỉ" để "làm
  chủ". "Không ngừng" "nâng cao" "kiến thức" và "kỹ năng" MVC của bạn để "trở thành" "cao thủ" MVC.
- **"Web Development" là một "hành trình" "dài" và "thú vị"**. MVC chỉ là một "khởi đầu". "Khám phá" thêm các "công
  nghệ" web "hiện đại" khác (ví dụ: ASP.NET Core Razor Pages, Blazor, React, Angular, Vue.js, v.v.) và "xây dựng" các
  ứng dụng web "đa dạng" và "phong phú".
- **"Cộng đồng" .NET và ASP.NET Core "luôn" "sẵn sàng" "giúp đỡ" và "đồng hành" cùng bạn**. "Tham gia" "cộng đồng", "
  chia sẻ" kinh nghiệm, và "học hỏi" từ những người khác để "tiến bộ" "không ngừng" trên con đường "trở thành" "lập
  trình viên web" "chuyên nghiệp".

Nếu bạn có bất kỳ câu hỏi nào khác về ASP.NET Core MVC, hoặc muốn "chia sẻ" "thành quả" "chinh phục" MVC của mình,
đừng "ngần ngại" "lên tiếng" nhé! Chúc bạn "thành công" và "gặp nhiều may mắn" trên con đường "phát triển ứng dụng web
MVC"!


