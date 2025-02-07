# Chương 4: Caching Trong ASP.NET Core - "Web Cũng Cần 'Nước Ngọt' " - "Cache 'Tận Răng' Cho Ứng Dụng Web"

Chào mừng bạn đến với **Chương 4: Caching Trong ASP.NET Core**! Trong chương này, chúng ta sẽ "tập trung" vào việc "ứng
dụng" **Caching** vào các ứng dụng **ASP.NET Core**. Ứng dụng web thường "đối mặt" với "lượng truy cập" "cao" và "yêu
cầu" "hiệu năng" "khắt khe". Caching là một "vũ khí" "lợi hại" để "tăng tốc" ứng dụng web ASP.NET Core của bạn.

**Phần 4: Caching Trong ASP.NET Core - "Web Cũng Cần 'Nước Ngọt' "**

**4.1. Middleware Caching "Ngay Trong Bộ Nhớ" (In-Memory Caching Middleware) - "Cache 'Tự Động' Cho Ứng Dụng Web" - "
Thêm 'Lớp Áo Giáp' Cache 'Tức Thì' Cho Web"**

- **Middleware Caching - "Cache 'Tự Động' " "Không Cần 'Code Nhiều' ":**

    - Trong ASP.NET Core, **Middleware** là các "thành phần" "phần mềm" được "xếp lớp" trong **"pipeline xử lý request"
      **. Middleware có thể "thực hiện" các "tác vụ" "trước" và "sau" khi request được "xử lý" bởi controller action.
    - **Caching Middleware** là một loại middleware "đặc biệt" được "thiết kế" để "thêm" "chức năng" **Caching** vào ứng
      dụng web một cách **"tự động"** và **"trong suốt"**.
    - Với Caching Middleware, bạn có thể "cache" **"toàn bộ"** hoặc **"một phần"** **"phản hồi"** HTTP (HTTP response)
      của ứng dụng web (ví dụ: trang HTML, dữ liệu JSON, hình ảnh, v.v.) vào **In-Memory Cache** hoặc **Distributed
      Cache**. Khi có request "tương tự" trong tương lai, Caching Middleware sẽ **"tự động" "phục vụ"** "phản hồi" từ
      cache, **"không cần"** "ứng dụng phải 'xử lý' lại request" và "tạo lại" "phản hồi".

- **In-Memory Caching Middleware - "Cache 'Ngay Trong Web Server' ":**

    - **In-Memory Caching Middleware** "lưu trữ" dữ liệu cache **"ngay trong bộ nhớ"** (RAM) của **"web server"** đang
      chạy ứng dụng ASP.NET Core.
    - "Sử dụng" **`IMemoryCache`** interface (đã được "giới thiệu" ở Chương 2) để "tương tác" với In-Memory Cache.
      ASP.NET Core đã **"đăng ký" sẵn** `IMemoryCache` vào **Dependency Injection (DI) container**, bạn có thể "inject"
      nó vào middleware hoặc controller của bạn.

- **"Cách 'kích hoạt' " In-Memory Caching Middleware trong ASP.NET Core:**

    1. **"Đăng ký" dịch vụ `IMemoryCache`** vào DI container (thường đã được "đăng ký" mặc định trong `Program.cs` hoặc
       `Startup.cs`):

       ```csharp
       // Program.cs (hoặc Startup.cs - ConfigureServices method)
       builder.Services.AddMemoryCache(); // "Đăng ký" dịch vụ IMemoryCache
       ```

    2. **"Thêm" In-Memory Caching Middleware vào "pipeline" request** trong `Program.cs` hoặc `Startup.cs` (thường trong
       `Configure` method):

       ```csharp
       // Program.cs (hoặc Startup.cs - Configure method)
       app.UseStaticFiles(); // (Thường có sẵn) Middleware phục vụ file tĩnh (ví dụ: CSS, JS, hình ảnh)

       app.UseResponseCaching(); // "Thêm" Response Caching Middleware (In-Memory Caching Middleware) - **đặt trước MVC middleware**

       app.UseRouting(); // (Thường có sẵn) Middleware routing (định tuyến request đến controller action)

       app.UseAuthorization(); // (Thường có sẵn) Middleware authorization (kiểm tra quyền truy cập)

       app.UseEndpoints(endpoints => // (Thường có sẵn) Middleware endpoints (map endpoints cho controller actions)
       {
           endpoints.MapControllerRoute(
               name: "default",
               pattern: "{controller=Home}/{action=Index}/{id?}");
       });
       ```

    3. **"Cấu hình" "caching" cho controller actions hoặc endpoints** (bằng cách dùng **`[ResponseCache]` attribute**
       hoặc **"cấu hình" middleware "tùy chỉnh"** - xem phần sau).

- **"Cấu hình" Caching cho Controller Actions với `[ResponseCache]` Attribute:**

    - **`[ResponseCache]` attribute** là một attribute "có sẵn" trong ASP.NET Core MVC, cho phép bạn **"cấu hình" "chính
      sách" caching** cho **"phản hồi"** của một controller action.
    - "Các thuộc tính" "quan trọng" của `[ResponseCache]` attribute:

        - `Duration`: **"Thời gian" (giây)** mà "phản hồi" được "cache" (time-to-live). **"Bắt buộc"** phải "cài đặt"
          giá trị này để "bật" caching.
        - `Location`: **"Vị trí"** "cache" (ví dụ: `ResponseCacheLocation.Any`, `ResponseCacheLocation.Client`,
          `ResponseCacheLocation.None`, `ResponseCacheLocation.Server`). Mặc định là `ResponseCacheLocation.Any` (cache
          ở cả server và client). `ResponseCacheLocation.Server` chỉ cache ở server (In-Memory Cache Middleware).
        - `VaryByHeader`: **"Danh sách" HTTP headers** mà cache sẽ **"phân biệt"** (vary by). Nếu giá trị của các
          headers này "thay đổi", cache sẽ được xem là "khác nhau". Ví dụ: `VaryByHeader = "Accept-Encoding"` (cache "
          riêng biệt" cho các loại encoding khác nhau).
        - `VaryByQueryKeys`: **"Danh sách" query string keys** mà cache sẽ **"phân biệt"**. Ví dụ:
          `VaryByQueryKeys = new[] { "categoryId", "page" }` (cache "riêng biệt" cho các category và page khác nhau).
        - `NoStore`: `bool` - "Xác định" xem "phản hồi" có được "lưu trữ" trong **"bất kỳ cache nào"** hay không (bao
          gồm cả client cache và server cache). `NoStore = true` "vô hiệu hóa" caching hoàn toàn.
        - `CacheProfileName`: "Tên" của **"cache profile"** được "định nghĩa" trong `Startup.cs` (hoặc `Program.cs`).
          Cho phép "dùng lại" "cấu hình" cache cho nhiều actions.

    - **Ví dụ "cấu hình" caching cho action `Index` của `HomeController`:**

      ```csharp
      using Microsoft.AspNetCore.Mvc;
      using System.Diagnostics;

      public class HomeController : Controller
      {
          private readonly ILogger<HomeController> _logger;

          public HomeController(ILogger<HomeController> logger)
          {
              _logger = logger;
          }

          [ResponseCache(Duration = 60, Location = ResponseCacheLocation.Server, VaryByQueryKeys = new[] { "page" })] // "Bật" In-Memory Caching cho action Index: cache 60 giây, chỉ cache ở server, phân biệt theo query string "page"
          public IActionResult Index(int page = 1) // Action Index với tham số "page"
          {
              ViewData["Page"] = page; // "Truyền" giá trị "page" vào ViewData
              return View(); // "Trả về" View Index.cshtml
          }

          public IActionResult Privacy()
          {
              return View();
          }

          [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)] // "Tắt" caching cho action Error (ví dụ)
          public IActionResult Error()
          {
              return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
          }
      }
      ```

        -
      `[ResponseCache(Duration = 60, Location = ResponseCacheLocation.Server, VaryByQueryKeys = new[] { "page" })]`: "
      Ra lệnh" cho ASP.NET Core "cache" "phản hồi" của action `Index` trong **60 giây**, "chỉ cache" ở **server-side
      ** (In-Memory Caching Middleware), và "phân biệt" cache theo **query string parameter `page`**.
        - Khi người dùng "truy cập" action `Index` với cùng giá trị `page` trong vòng 60 giây, In-Memory Caching
          Middleware sẽ **"tự động" "phục vụ" "phản hồi" từ cache**, "không cần" action `Index` phải "chạy" lại.
        - Nếu giá trị `page` "thay đổi", hoặc sau 60 giây, cache sẽ "hết hạn" (hoặc không có cache cho giá trị `page`
          đó), action `Index` sẽ "chạy" và "tạo ra" "phản hồi" mới (và "phản hồi" mới sẽ được "lưu" vào cache).

- **"Cấu hình" Cache Profiles trong `Program.cs` hoặc `Startup.cs`:**

    - Thay vì "lặp lại" "cấu hình" `[ResponseCache]` attribute ở nhiều actions, bạn có thể "định nghĩa" **"Cache
      Profiles"** trong `Program.cs` hoặc `Startup.cs` và "dùng lại" chúng bằng thuộc tính `CacheProfileName` trong
      `[ResponseCache]` attribute.

      ```csharp
      // Program.cs (hoặc Startup.cs - ConfigureServices method)
      builder.Services.AddControllersWithViews(options =>
      {
          options.CacheProfiles.Add("Default", new CacheProfile() // "Định nghĩa" Cache Profile "Default"
          {
              Duration = 30, // Cache 30 giây
              Location = ResponseCacheLocation.Server // Chỉ cache ở server
          });

          options.CacheProfiles.Add("NoCache", new CacheProfile() // "Định nghĩa" Cache Profile "NoCache"
          {
              NoStore = true, // "Tắt" caching hoàn toàn
              Location = ResponseCacheLocation.None // "Vô hiệu hóa" cache ở mọi nơi
          });
      });
      ```

      ```csharp
      // HomeController.cs
      public class HomeController : Controller
      {
          // ...

          [ResponseCache(CacheProfileName = "Default", VaryByQueryKeys = new[] { "page" })] // "Dùng" Cache Profile "Default" và "thêm" VaryByQueryKeys
          public IActionResult Index(int page = 1)
          {
              // ...
          }

          [ResponseCache(CacheProfileName = "NoCache")] // "Dùng" Cache Profile "NoCache" - "tắt" caching
          public IActionResult Error()
          {
              // ...
          }
      }
      ```

**4.2. Caching "Phân Tán" Trong ASP.NET Core (`IDistributedCache`) - "Mở Rộng 'Bể Nước' Cho Web" - "Cache 'Chia Sẻ' Cho
Web 'Đa Máy Chủ' "**

- **`IDistributedCache` - "Interface" "Trừu Tượng" Cho Cache "Phân Tán":**

    - **`IDistributedCache`** là một interface trong ASP.NET Core (namespace
      `Microsoft.Extensions.Caching.Distributed`) "định nghĩa" **"hợp đồng"** (contract) cho các "hệ thống" *
      *Distributed Cache**.
    - `IDistributedCache` cung cấp các "phương thức" "cơ bản" để "thao tác" với Distributed Cache (ví dụ: `Get`, `Set`,
      `Remove`, `Refresh`, v.v.).
    - ASP.NET Core "không cung cấp" "triển khai" `IDistributedCache` "mặc định". Bạn cần "chọn" và "đăng ký" một "triển
      khai" cụ thể của `IDistributedCache` (ví dụ: Redis, Memcached, SQL Server Distributed Cache, v.v.) vào DI
      container.

- **"Triển Khai" `IDistributedCache` Với Redis (Ví Dụ: StackExchange.Redis):**

    1. **"Cài đặt" NuGet Package StackExchange.Redis** (nếu chưa cài đặt - như đã "hướng dẫn" ở Chương 3).

    2. **"Đăng ký" Redis Cache "phân tán" (Distributed Redis Cache) vào DI container** trong `Program.cs` hoặc
       `Startup.cs` (ConfigureServices method):

       ```csharp
       // Program.cs (hoặc Startup.cs - ConfigureServices method)
       builder.Services.AddStackExchangeRedisCache(options => // "Đăng ký" Distributed Redis Cache
       {
           options.Configuration = builder.Configuration.GetConnectionString("RedisConnection"); // "Lấy" chuỗi kết nối Redis từ configuration (appsettings.json)
           // Hoặc "cấu hình" trực tiếp:
           // options.Configuration = "localhost:6379,password=your_redis_password";
           options.InstanceName = "SampleInstance"; // "Tên instance" Redis (tùy chọn)
       });
       ```

        - `AddStackExchangeRedisCache()` là một extension method "thuận tiện" để "đăng ký" `IDistributedCache` "triển
          khai" bằng Redis (sử dụng StackExchange.Redis).
        - `options.Configuration`: "Chuỗi kết nối" Redis server. Bạn có thể "lấy" từ configuration (appsettings.json)
          hoặc "cấu hình" trực tiếp.
        - `options.InstanceName`: "Tên instance" Redis (tùy chọn). "Dùng" để "phân biệt" cache của các ứng dụng khác
          nhau trên cùng Redis server.

    3. **"Inject" `IDistributedCache` vào controller hoặc service** của bạn:

       ```csharp
       using Microsoft.AspNetCore.Mvc;
       using Microsoft.Extensions.Caching.Distributed;
       using System.Text;
       using System.Text.Json;
       using System.Threading.Tasks;

       public class DistributedCacheController : Controller
       {
           private readonly IDistributedCache _distributedCache; // "Inject" IDistributedCache

           public DistributedCacheController(IDistributedCache distributedCache) // Constructor injection
           {
               _distributedCache = distributedCache;
           }

           public async Task<IActionResult> Index() // Action Index
           {
               string cacheKey = "SanPham_DistributedCache_1"; // "Khóa" cache

               // "Lấy" dữ liệu từ Distributed Cache
               byte[] cachedSanPhamBytes = await _distributedCache.GetAsync(cacheKey);
               SanPham sanPham_Cached = null;

               if (cachedSanPhamBytes != null) // "Cache hit"
               {
                   string cachedSanPhamString = Encoding.UTF8.GetString(cachedSanPhamBytes); // "Chuyển đổi" byte array về string (UTF8)
                   sanPham_Cached = JsonSerializer.Deserialize<SanPham>(cachedSanPhamString); // "Deserialize" JSON string về đối tượng SanPham
                   ViewBag.Message = "Lấy sản phẩm từ Distributed Cache (Redis)!"; // Thông báo "cache hit"
               }
               else // "Cache miss"
               {
                   // "Lấy" dữ liệu từ "nguồn gốc" (ví dụ: database - bỏ qua trong ví dụ này)
                   SanPham sanPham_FromSource = new SanPham { SanPhamId = 1, TenSanPham = "Tai nghe Bluetooth", Gia = 750000 }; // "Tạo" đối tượng SanPham "mẫu"

                   // "Serialize" đối tượng SanPham về JSON string
                   string sanPhamString = JsonSerializer.Serialize(sanPham_FromSource);
                   byte[] sanPhamBytes = Encoding.UTF8.GetBytes(sanPhamString); // "Chuyển đổi" JSON string về byte array (UTF8)

                   // "Cấu hình" DistributedCacheEntryOptions (tùy chọn cache)
                   var cacheOptions = new DistributedCacheEntryOptions()
                                           .SetAbsoluteExpiration(TimeSpan.FromSeconds(60)); // "Đặt" Absolute Expiration là 60 giây

                   // "Lưu" dữ liệu vào Distributed Cache
                   await _distributedCache.SetAsync(cacheKey, sanPhamBytes, cacheOptions); // "Lưu" byte array vào Distributed Cache

                   sanPham_Cached = sanPham_FromSource; // "Gán" dữ liệu từ "nguồn gốc" để hiển thị
                   ViewBag.Message = "Không tìm thấy trong cache. Lấy từ nguồn gốc và lưu vào Distributed Cache (Redis)!"; // Thông báo "cache miss"
               }

               return View(sanPham_Cached); // "Trả về" View, "gửi" kèm theo đối tượng SanPham
           }
       }
       ```

        - "Inject" `IDistributedCache` vào controller constructor.
        - `_distributedCache.GetAsync(cacheKey)`: "Lấy" dữ liệu cache theo "khóa" từ Distributed Cache. "Trả về"
          `byte[]` (vì Distributed Cache thường "lưu trữ" dữ liệu dưới dạng byte array).
        - `_distributedCache.SetAsync(cacheKey, sanPhamBytes, cacheOptions)`: "Lưu" dữ liệu vào Distributed Cache. "
          Nhận" vào `byte[]` dữ liệu, và `DistributedCacheEntryOptions` để "cấu hình" cache (ví dụ: expiration).
        - `DistributedCacheEntryOptions`: "Tương tự" như `CacheItemPolicy` của `MemoryCache`, dùng để "cấu hình" các "
          tùy chọn" cache (ví dụ: AbsoluteExpiration, SlidingExpiration).

- **"Triển Khai" `IDistributedCache` Với Memcached (Ví Dụ: EnyimMemcachedCore):**

    - Tương tự như Redis, bạn cần "cài đặt" NuGet package cho Memcached (ví dụ: **`EnyimMemcachedCore`**) và "đăng ký"
      Memcached Distributed Cache vào DI container bằng extension method tương ứng (ví dụ: `AddEnyimMemcached()` từ
      EnyimMemcachedCore).

**4.3. Middleware Caching Phản Hồi (Response Caching Middleware) - "Cache 'Toàn Trang' " "Siêu Tốc" - "Cache 'HTTP
Level' Cho Web"**

- **Response Caching Middleware - "Cache 'Toàn Bộ' Phản Hồi HTTP - "Nhanh Gọn Lẹ" ":**

    - **Response Caching Middleware** là một middleware "có sẵn" trong ASP.NET Core, "cho phép" bạn "cache" **"toàn bộ"
      ** **"phản hồi"** HTTP (HTTP response) của ứng dụng web (bao gồm cả HTTP headers và HTTP body).
    - Response Caching Middleware "hoạt động" ở **"tầng HTTP"**, **"trước"** khi request được "xử lý" bởi MVC middleware
      và controller actions.
    - Khi có request, Response Caching Middleware sẽ **"kiểm tra"** xem "phản hồi" cho request này đã được **"cache"**
      chưa.
        - **Nếu có trong cache (cache hit):** Response Caching Middleware sẽ **"trực tiếp" "phục vụ" "phản hồi" từ cache
          ** (HTTP response đã cache), **"bỏ qua"** các middleware và controller actions "phía sau". "Ứng dụng web" hầu
          như **"không cần"** "xử lý" request, "tăng tốc" "hiệu năng" một cách "đáng kể".
        - **Nếu không có trong cache (cache miss):** Request sẽ được "chuyển" đến các middleware và controller actions "
          phía sau" để "xử lý" bình thường. Sau khi "phản hồi" được "tạo ra", Response Caching Middleware sẽ **"lưu" "
          phản hồi" vào cache** để "phục vụ" cho các request tiếp theo.

- **"Cách 'kích hoạt' " Response Caching Middleware trong ASP.NET Core:**

    1. **"Thêm" Response Caching Middleware vào "pipeline" request** trong `Program.cs` hoặc `Startup.cs` (thường trong
       `Configure` method) - **"đặt trước" MVC middleware** (như đã "thấy" ở phần 4.1):

       ```csharp
       // Program.cs (hoặc Startup.cs - Configure method)
       app.UseResponseCaching(); // "Thêm" Response Caching Middleware - **đặt trước MVC middleware**
       ```

    2. **"Cấu hình" "caching" cho controller actions hoặc endpoints** (bằng cách dùng **`[ResponseCache]` attribute**
       hoặc **"cấu hình" middleware "tùy chỉnh"** - xem phần sau).

- **"Cấu hình" Caching cho Controller Actions với `[ResponseCache]` Attribute (tương tự như In-Memory Caching
  Middleware - phần 4.1):**

    - Bạn có thể "dùng" **`[ResponseCache]` attribute** (đã "giới thiệu" ở phần 4.1) để "cấu hình" "chính sách" caching
      cho Response Caching Middleware.
    - "Các thuộc tính" của `[ResponseCache]` attribute (ví dụ: `Duration`, `Location`, `VaryByHeader`,
      `VaryByQueryKeys`, v.v.) vẫn có "ý nghĩa" tương tự khi dùng với Response Caching Middleware.
    - **"Lưu ý quan trọng"**: Khi dùng Response Caching Middleware, `Location = ResponseCacheLocation.Any` (mặc định)
      sẽ "cache" "phản hồi" ở **"cả server-side cache" (Response Caching Middleware) và "client-side cache" (browser
      cache, proxy cache)**. Nếu bạn muốn **"chỉ cache"** ở **"server-side"** (In-Memory Caching Middleware), bạn cần "
      dùng" `Location = ResponseCacheLocation.Server`.

- **"Cấu hình" Response Caching Middleware "Toàn Cục" trong `appsettings.json` hoặc `Program.cs`:**

    - Bạn có thể "cấu hình" các "tùy chọn" "toàn cục" cho Response Caching Middleware trong `appsettings.json` hoặc
      `Program.cs` (Configure method):

      ```json
      // appsettings.json
      {
          "ResponseCaching": {
              // "Section" cấu hình ResponseCaching
              "MaximumBodySize": 102400, // "Kích thước body" tối đa được cache (bytes) - mặc định 100KB
              "UseCaseSensitivePaths": false // "Phân biệt chữ hoa chữ thường" trong URL path khi cache (mặc định false - không phân biệt)
          }
          // ...
      }
      ```

      ```csharp
      // Program.cs (hoặc Startup.cs - Configure method)
      builder.Services.Configure<ResponseCachingOptions>(options => // "Cấu hình" ResponseCachingOptions
      {
          options.MaximumBodySize = 102400; // "Kích thước body" tối đa được cache (bytes)
          options.UseCaseSensitivePaths = false; // "Phân biệt chữ hoa chữ thường" trong URL path
      });
      ```

- **"Lưu ý quan trọng" khi dùng Response Caching Middleware:**

    - **"Chỉ cache" "phản hồi" HTTP GET và HEAD:** Response Caching Middleware chỉ "cache" "phản hồi" cho các request
      HTTP methods **`GET` và `HEAD`**. Các methods khác (POST, PUT, DELETE, v.v.) thường "không được cache".
    - **"Tuân thủ" HTTP caching headers:** Response Caching Middleware "tuân thủ" các HTTP caching headers (ví dụ:
      `Cache-Control`, `Expires`, `Pragma`) trong request và response để "xác định" xem "phản hồi" có được "cache" hay
      không và "cách cache". "Đảm bảo" bạn "cài đặt" HTTP caching headers "chính xác" để Response Caching Middleware "
      hoạt động" "đúng ý".
    - **"Cẩn thận" với dữ liệu "động" và "cá nhân hóa":** Response Caching Middleware "cache" "toàn bộ" "phản hồi" HTTP,
      bao gồm cả dữ liệu "động" và "cá nhân hóa" (ví dụ: thông tin người dùng, session data). "Đảm bảo" bạn **"không
      cache"** các "phản hồi" chứa dữ liệu "nhạy cảm" hoặc "cá nhân hóa" mà "không muốn" "chia sẻ" cho người dùng
      khác. "Dùng" `VaryByHeader`, `VaryByQueryKeys`, hoặc "middleware 'tùy chỉnh' " để "kiểm soát" "cách cache" dữ
      liệu "động" và "cá nhân hóa".

**4.4. Tag Helpers Cho Caching - "Cache 'Từng Phần' " "Linh Hoạt" Trong View - "Cache 'Mảnh Ghép' UI"**

- **Cache Tag Helper (`<cache>` tag helper) - "Cache 'Từng Đoạn' HTML Trong View":**

    - **Cache Tag Helper (`<cache>` tag helper)** là một tag helper "có sẵn" trong ASP.NET Core MVC, cho phép bạn **"
      cache" "từng phần"** (fragments) **HTML** trong **Razor Views** của bạn (`.cshtml` files).
    - Cache Tag Helper "cho phép" bạn "cache" **"một phần"** View (ví dụ: một partial view, một section, một đoạn HTML
      code) mà **"không cần"** phải "cache" "toàn bộ" trang.
    - Cache Tag Helper "dùng" **In-Memory Cache** để "lưu trữ" dữ liệu cache.

- **"Cách 'sử dụng' " Cache Tag Helper:**

    - "Đặt" đoạn HTML code bạn muốn "cache" **"bên trong"** tag **`<cache>`** trong View (`.cshtml` file).
    - "Cấu hình" các **"thuộc tính"** của tag `<cache>` để "định nghĩa" "chính sách" caching (ví dụ: `expires-after`,
      `expires-sliding`, `vary-by-query`, `vary-by-cookie`, `vary-by-header`, v.v.).

  ```cshtml
  @* Index.cshtml *@
  @page
  @model IndexModel
  @{
      ViewData["Title"] = "Home page";
  }

  <div class="text-center">
      <h1 class="display-4">Welcome</h1>
      <p>Learn about <a href="https://docs.microsoft.com/aspnet/core">building Web apps with ASP.NET Core</a>.</p>

      @* Cache Tag Helper - "Cache" đoạn HTML code này trong 60 giây *@
      <cache expires-after="@TimeSpan.FromSeconds(60)">
          <p>Thời gian hiện tại (lần đầu hiển thị, sau đó sẽ cache): @DateTime.Now</p>
      </cache>

      @* Cache Tag Helper - "Cache" đoạn HTML code này, "phân biệt" theo query string "culture" *@
      <cache vary-by-query="culture">
          <p>Ngôn ngữ hiện tại (phân biệt theo query string "culture"): @System.Globalization.CultureInfo.CurrentCulture.DisplayName</p>
      </cache>
  </div>
  ```

    - `<cache expires-after="@TimeSpan.FromSeconds(60)">`: "Cache" đoạn HTML code bên trong tag `<cache>` trong **60
      giây** (Absolute Expiration).
    - `<cache vary-by-query="culture">`: "Cache" đoạn HTML code bên trong tag `<cache>`, và **"phân biệt"** cache theo *
      *query string parameter `culture`**. Nếu giá trị `culture` "thay đổi", cache sẽ được xem là "khác nhau".

- **"Các thuộc tính" "quan trọng" của Cache Tag Helper:**

    - **Expiration (Hết Hạn Cache):**

        - `expires-after`: `TimeSpan` - "Thời gian" "hết hạn tuyệt đối" (Absolute Expiration) sau lần đầu tiên "cache".
        - `expires-sliding`: `TimeSpan` - "Thời gian" "hết hạn trượt" (Sliding Expiration) sau lần "truy cập" "cuối
          cùng".
        - `expires-on`: `DateTimeOffset` - "Thời điểm" "hết hạn tuyệt đối" (Absolute Expiration) "cụ thể".

    - **Vary By (Phân Biệt Cache):**

        - `vary-by-query`: `string` - "Query string key" hoặc "danh sách query string keys" mà cache sẽ "phân biệt".
        - `vary-by-cookie`: `string` - "Cookie name" hoặc "danh sách cookie names" mà cache sẽ "phân biệt".
        - `vary-by-header`: `string` - "HTTP header name" hoặc "danh sách HTTP header names" mà cache sẽ "phân biệt".
        - `vary-by-user`: `bool` - "Phân biệt" cache theo "người dùng" đã đăng nhập (authentication).
        - `vary-by-route`: `string` - "Route data name" hoặc "danh sách route data names" mà cache sẽ "phân biệt".
        - `vary-by`: `object` - "Biểu thức C#" "tùy chỉnh" để "phân biệt" cache (linh hoạt nhất).

    - **Priority (Độ Ưu Tiên Cache):**

        - `priority`: `CacheItemPriority` enum - "Độ ưu tiên" của dữ liệu cache khi bộ nhớ cache "đầy" (ví dụ: `Low`,
          `Normal`, `High`, `NeverRemove`). "Dùng" để "kiểm soát" "chính sách 'loại bỏ' cache" (eviction policy).

    - **Enabled (Bật/Tắt Cache):**
        - `enabled`: `bool` - "Bật" hoặc "tắt" caching cho tag helper `<cache>`. "Dùng" để "tạm thời" "vô hiệu hóa"
          caching trong quá trình phát triển hoặc debug.

- **Distributed Cache Tag Helper (`<distributed-cache>` tag helper) - "Cache 'Từng Phần' HTML Vào Distributed Cache":**

    - **Distributed Cache Tag Helper (`<distributed-cache>` tag helper)** (namespace
      `Microsoft.AspNetCore.Mvc.TagHelpers`) "tương tự" như Cache Tag Helper, nhưng "cho phép" bạn "cache" "từng phần"
      HTML vào **Distributed Cache** (thay vì In-Memory Cache).
    - Để "sử dụng" Distributed Cache Tag Helper, bạn cần "cài đặt" NuGet package **`Microsoft.AspNetCore.Mvc.TagHelpers`
      ** (thường đã được "cài đặt" mặc định trong dự án ASP.NET Core MVC) và "đăng ký" tag helpers trong
      `_ViewImports.cshtml`:

      ```csharp
      @addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
      ```

    - "Cách 'sử dụng' " Distributed Cache Tag Helper và "các thuộc tính" "tương tự" như Cache Tag Helper.

**Tổng Kết Chương 4:**

- Bạn đã "khám phá" các "chiêu thức" Caching "đa dạng" trong ASP.NET Core để "tối ưu hóa" "hiệu năng" ứng dụng web của
  bạn.
    - "Sử dụng" **In-Memory Caching Middleware** và **`[ResponseCache]` attribute** để "cache 'tự động' " "phản hồi"
      controller actions "vào bộ nhớ" web server.
    - "Vận dụng" **`IDistributedCache`** để "caching 'phân tán' " dữ liệu trong ứng dụng web "đa máy chủ" (ví dụ: với
      Redis).
    - "Dùng" **Response Caching Middleware** để "cache 'toàn trang' " "phản hồi" HTTP ở "tầng HTTP" cho "tốc độ" "siêu
      nhanh".
    - "Tận dụng" **Cache Tag Helper** và **Distributed Cache Tag Helper** để "cache 'từng phần' " HTML trong Razor
      Views, "tăng" "tính linh hoạt" caching UI.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 5: "Tuyệt Chiêu" Caching Nâng Cao - "Luyện 'Công Phu' Caching"**. Chúng ta sẽ "khám
phá" các "kỹ thuật" Caching "nâng cao" hơn như Cache Invalidation, Cache Stampede Prevention, Cache Partitioning, Lazy
Loading and Caching, v.v. để "nâng cao" "trình độ" Caching của bạn lên một "tầm cao mới".

Bạn có câu hỏi nào về Caching trong ASP.NET Core này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp"
và "đồng hành" cùng bạn trên con đường "chinh phục" Caching.
