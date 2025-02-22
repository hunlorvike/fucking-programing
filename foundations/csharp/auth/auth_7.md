# Chương 7: "Ứng Dụng Thực Tế Của Authentication và Authorization" - "AuthN/AuthZ Đi Muôn Nơi" - " 'Chứng Kiến' " "Bảo Mật" "Hành Động", " 'Học Hỏi' " Từ " 'Kinh Nghiệm' " "Thực Chiến"

Chào mừng bạn đến với **Chương 7: "Ứng Dụng Thực Tế Của Authentication và Authorization" - "AuthN/AuthZ Đi Muôn Nơi"**! Trong chương này, chúng ta sẽ **" 'bước ra' " khỏi "lý thuyết"** và **" 'chứng kiến' " Authentication và Authorization " 'hành động' "** trong một **"ví dụ" ứng dụng web ASP.NET Core MVC "đơn giản"**. Chúng ta sẽ **" 'mổ xẻ' " code "bảo mật" "thực tế"**, "phân tích" cách Authentication và Authorization được **"triển khai"**, và **"mở rộng" "ví dụ"** để **" 'nâng cấp' " "bảo mật"** ứng dụng "lên một 'tầm cao mới' ". "AuthN/AuthZ" không chỉ là "khái niệm", mà là " 'vũ khí' " "bảo vệ" ứng dụng "đi muôn nơi" trong thế giới web "đầy rẫy" "nguy cơ".

**Phần 7: "Ứng Dụng Thực Tế Của Authentication và Authorization" - "AuthN/AuthZ Đi Muôn Nơi"**

**7.1. Ví dụ ứng dụng web ASP.NET Core MVC đơn giản với Authentication và Authorization - Ứng Dụng Web "Bảo Mật" "Vỡ Lòng" - " 'Bắt Đầu' " Từ " 'Nền Tảng' ", " 'Xây Dựng' " "Ngôi Nhà" "Bảo Mật"**

-   **"Ứng Dụng Web 'Quản Lý Công Việc' " - " 'Hello World' " Của "Bảo Mật":**

    -   Chúng ta sẽ "xây dựng" một ứng dụng web ASP.NET Core MVC "cực kỳ" **"đơn giản"** để "quản lý" **"danh sách công việc" (to-do list)**. Ứng dụng này sẽ "minh họa" các "khái niệm" Authentication và Authorization "cơ bản" nhất.
    -   **"Chức năng" ứng dụng:**
        -   **"Đăng ký" và "Đăng nhập"**: Người dùng có thể "tạo" "tài khoản" và "đăng nhập" để "truy cập" các "chức năng" "bảo mật".
        -   **"Xem danh sách công việc"**: "Người dùng" "đã đăng nhập" có thể "xem" "danh sách công việc" "cá nhân".
        -   **"Thêm công việc mới"**: "Người dùng" "đã đăng nhập" có thể "thêm" "công việc mới" vào "danh sách" của mình.
        -   **"Sửa công việc"**: "Người dùng" "đã đăng nhập" có thể "sửa" "công việc" "của mình".
        -   **"Xóa công việc"**: "Người dùng" "đã đăng nhập" có thể "xóa" "công việc" "của mình".
        -   **"Trang Admin" (chỉ "Admin" "mới được" "truy cập")**: "Trang" "quản trị" "đơn giản" (ví dụ: "hiển thị" "thống kê" "ứng dụng") - "minh họa" **Role-Based Authorization**.

-   **"Cấu Trúc" Ứng Dụng (ASP.NET Core MVC):**

    -   **"Models"**:
        -   `TodoItem.cs`: Model "công việc" (ID, Title, Description, IsCompleted, UserId).
        -   `ApplicationUser.cs`: "Mở rộng" `IdentityUser` (từ ASP.NET Core Identity) - "không cần" "mở rộng" gì thêm trong "ví dụ" này.
    -   **"Controllers"**:
        -   `HomeController.cs`: Controller "trang chủ" và "trang công cộng".
        -   `TodoController.cs`: Controller "quản lý" "công việc" (CRUD operations).
        -   `AdminController.cs`: Controller "trang quản trị" (chỉ "Admin" "mới được" "truy cập").
        -   `AccountController.cs`: Controller "quản lý" "tài khoản" (Đăng ký, Đăng nhập, Đăng xuất).
    -   **"Views"**:
        -   `Home`: Views cho `HomeController` (Index, Privacy, Contact).
        -   `Todo`: Views cho `TodoController` (Index, Create, Edit, Delete).
        -   `Admin`: Views cho `AdminController` (Index).
        -   `Account`: Views cho `AccountController` (Login, Register, AccessDenied).
        -   `Shared`: Layout, _LoginPartial (partial view "hiển thị" "trạng thái" "đăng nhập").
    -   **"Data"**:
        -   `ApplicationDbContext.cs`: `DbContext` (sử dụng Entity Framework Core) - "kết nối" với database (In-Memory Database cho "ví dụ" "đơn giản").
    -   **"Services"**: (Không có service "riêng" trong "ví dụ" "đơn giản" này - "logic" "nghiệp vụ" "đơn giản" được "thực hiện" trực tiếp trong Controllers).

-   **"Code" "Ví Dụ" (Code "chính" "liên quan" đến Authentication và Authorization - "code đầy đủ" có thể được "tải về" từ repository ví dụ):**

    -   **`Startup.cs` (Cấu Hình Authentication và Authorization):**

        ```csharp
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddDbContext<ApplicationDbContext>(options =>
                options.UseInMemoryDatabase("TodoAppDb")); // Sử dụng In-Memory Database cho ví dụ

            services.AddDefaultIdentity<ApplicationUser>(options => options.SignIn.RequireConfirmedAccount = false) // Đăng ký ASP.NET Core Identity
                .AddRoles<IdentityRole>() // Thêm hỗ trợ Roles
                .AddEntityFrameworkStores<ApplicationDbContext>();

            services.Configure<IdentityOptions>(options =>
            {
                // Password settings.
                options.Password.RequireDigit = true;
                options.Password.RequireLowercase = true;
                options.Password.RequireNonAlphanumeric = true;
                options.Password.RequireUppercase = true;
                options.Password.RequiredLength = 6;
                options.Password.RequiredUniqueChars = 1;

                // Lockout settings.
                options.Lockout.DefaultLockoutTimeSpan = TimeSpan.FromMinutes(5);
                options.Lockout.MaxFailedAccessAttempts = 5;
                options.Lockout.AllowedForNewUsers = true;

                // User settings.
                options.User.AllowedUserNameCharacters =
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._@+";
                options.User.RequireUniqueEmail = false;
            });

            services.ConfigureApplicationCookie(options =>
            {
                // Cookie settings
                options.Cookie.HttpOnly = true;
                options.ExpireTimeSpan = TimeSpan.FromMinutes(20);

                options.LoginPath = "/Account/Login";
                options.AccessDeniedPath = "/Account/AccessDenied";
                options.SlidingExpiration = true;
            });

            services.AddControllersWithViews();
            services.AddRazorPages();

            services.AddAuthorization(options => // Cấu hình Authorization Policies
            {
                options.AddPolicy("RequireAdminRole", policy => // Policy "RequireAdminRole"
                    policy.RequireRole("Admin")); // Yêu cầu Role "Admin"
            });
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
                app.UseMigrationsEndPoint();
            }
            else
            {
                app.UseExceptionHandler("/Home/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }
            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthentication(); // Thêm Authentication Middleware
            app.UseAuthorization(); // Thêm Authorization Middleware

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
                endpoints.MapRazorPages();
            });

            // Tạo "vai trò" "Admin" và "người dùng" "Admin" "mặc định" (cho ví dụ)
            CreateDefaultUserRoles(app).Wait();
        }

        private async Task CreateDefaultUserRoles(IApplicationBuilder app)
        {
            using (var serviceScope = app.ApplicationServices.CreateScope())
            {
                var roleManager = serviceScope.ServiceProvider.GetRequiredService<RoleManager<IdentityRole>>();
                var userManager = serviceScope.ServiceProvider.GetRequiredService<UserManager<ApplicationUser>>();

                // Tạo Role "Admin" nếu chưa tồn tại
                if (!await roleManager.RoleExistsAsync("Admin"))
                {
                    await roleManager.CreateAsync(new IdentityRole("Admin"));
                }

                // Tạo người dùng "admin@example.com" nếu chưa tồn tại và gán Role "Admin"
                var adminUser = await userManager.FindByEmailAsync("admin@example.com");
                if (adminUser == null)
                {
                    adminUser = new ApplicationUser { UserName = "admin@example.com", Email = "admin@example.com" };
                    await userManager.CreateAsync(adminUser, "P@$$wOrd123"); // Mật khẩu "mạnh" cho ví dụ
                    await userManager.AddToRoleAsync(adminUser, "Admin");
                }
            }
        }
        ```

    -   **`AccountController.cs` (Đăng ký, Đăng nhập, Đăng xuất, Từ chối truy cập):**

        ```csharp
        public class AccountController : Controller
        {
            private readonly UserManager<ApplicationUser> _userManager;
            private readonly SignInManager<ApplicationUser> _signInManager;

            public AccountController(UserManager<ApplicationUser> userManager, SignInManager<ApplicationUser> signInManager)
            {
                _userManager = userManager;
                _signInManager = signInManager;
            }

            [HttpGet]
            [AllowAnonymous]
            public IActionResult Register()
            {
                return View();
            }

            [HttpPost]
            [AllowAnonymous]
            [ValidateAntiForgeryToken]
            public async Task<IActionResult> Register(RegisterViewModel model)
            {
                if (ModelState.IsValid)
                {
                    var user = new ApplicationUser { UserName = model.Email, Email = model.Email };
                    var result = await _userManager.CreateAsync(user, model.Password);
                    if (result.Succeeded)
                    {
                        await _signInManager.SignInAsync(user, isPersistent: false);
                        return RedirectToAction("Index", "Home");
                    }
                    foreach (var error in result.Errors)
                    {
                        ModelState.AddModelError(string.Empty, error.Description);
                    }
                }

                return View(model);
            }

            [HttpGet]
            [AllowAnonymous]
            public IActionResult Login(string returnUrl = null)
            {
                ViewData["ReturnUrl"] = returnUrl;
                return View();
            }

            [HttpPost]
            [AllowAnonymous]
            [ValidateAntiForgeryToken]
            public async Task<IActionResult> Login(LoginViewModel model, string returnUrl = null)
            {
                ViewData["ReturnUrl"] = returnUrl;
                if (ModelState.IsValid)
                {
                    var result = await _signInManager.PasswordSignInAsync(model.Email, model.Password, model.RememberMe, lockoutOnFailure: false);
                    if (result.Succeeded)
                    {
                        return RedirectToLocal(returnUrl);
                    }
                    if (result.IsLockedOut)
                    {
                        return View("Lockout");
                    }
                    else
                    {
                        ModelState.AddModelError(string.Empty, "Invalid login attempt.");
                        return View(model);
                    }
                }
                return View(model);
            }

            [HttpPost]
            [ValidateAntiForgeryToken]
            public async Task<IActionResult> Logout()
            {
                await _signInManager.SignOutAsync();
                return RedirectToAction("Index", "Home");
            }

            [HttpGet]
            public IActionResult AccessDenied()
            {
                return View();
            }

            private IActionResult RedirectToLocal(string returnUrl)
            {
                if (Url.IsLocalUrl(returnUrl))
                {
                    return Redirect(returnUrl);
                }
                else
                {
                    return RedirectToAction("Index", "Home");
                }
            }
        }
        ```

    -   **`TodoController.cs` (CRUD Operations - "bảo vệ" bằng `[Authorize]`):**

        ```csharp
        [Authorize] // Yêu cầu "xác thực" cho "toàn bộ" TodoController
        public class TodoController : Controller
        {
            private readonly ApplicationDbContext _context;
            private readonly UserManager<ApplicationUser> _userManager;

            public TodoController(ApplicationDbContext context, UserManager<ApplicationUser> userManager)
            {
                _context = context;
                _userManager = userManager;
            }

            // GET: Todo
            public async Task<IActionResult> Index()
            {
                var user = await _userManager.GetUserAsync(User); // Lấy "người dùng" "hiện tại"
                if (user == null)
                {
                    return Challenge(); // Nếu "không xác thực", "thử thách" "xác thực" (redirect to login)
                }
                var todoItems = await _context.TodoItems
                    .Where(t => t.UserId == user.Id) // Chỉ "lấy" "công việc" của "người dùng" "hiện tại"
                    .ToListAsync();
                return View(todoItems);
            }

            // GET: Todo/Create
            public IActionResult Create()
            {
                return View();
            }

            // POST: Todo/Create
            [HttpPost]
            [ValidateAntiForgeryToken]
            public async Task<IActionResult> Create([Bind("Id,Title,Description,IsCompleted")] TodoItem todoItem)
            {
                if (ModelState.IsValid)
                {
                    var user = await _userManager.GetUserAsync(User); // Lấy "người dùng" "hiện tại"
                    if (user == null)
                    {
                        return Challenge(); // Nếu "không xác thực", "thử thách" "xác thực"
                    }
                    todoItem.UserId = user.Id; // "Gán" "User ID" cho "công việc"
                    _context.Add(todoItem);
                    await _context.SaveChangesAsync();
                    return RedirectToAction(nameof(Index));
                }
                return View(todoItem);
            }

            // GET: Todo/Edit/5
            public async Task<IActionResult> Edit(int? id)
            {
                if (id == null)
                {
                    return NotFound();
                }

                var todoItem = await _context.TodoItems.FindAsync(id);
                if (todoItem == null)
                {
                    return NotFound();
                }

                var user = await _userManager.GetUserAsync(User); // Lấy "người dùng" "hiện tại"
                if (user == null || todoItem.UserId != user.Id) // "Kiểm tra" "quyền sở hữu" "công việc"
                {
                    return Forbid(); // Nếu "không phải" "chủ sở hữu", "từ chối" "truy cập" (HTTP 403 Forbidden)
                }

                return View(todoItem);
            }

            // POST: Todo/Edit/5
            [HttpPost]
            [ValidateAntiForgeryToken]
            public async Task<IActionResult> Edit(int id, [Bind("Id,Title,Description,IsCompleted")] TodoItem todoItem)
            {
                if (id != idItem)
                {
                    return NotFound();
                }

                if (ModelState.IsValid)
                {
                    try
                    {
                        var user = await _userManager.GetUserAsync(User); // Lấy "người dùng" "hiện tại"
                        if (user == null || todoItem.UserId != user.Id) // "Kiểm tra" "quyền sở hữu" "công việc"
                        {
                            return Forbid(); // Nếu "không phải" "chủ sở hữu", "từ chối" "truy cập" (HTTP 403 Forbidden)
                        }

                        _context.Update(todoItem);
                        await _context.SaveChangesAsync();
                    }
                    catch (DbUpdateConcurrencyException)
                    {
                        if (!TodoItemExists(todoItem.Id))
                        {
                            return NotFound();
                        }
                        else
                        {
                            throw;
                        }
                    }
                    return RedirectToAction(nameof(Index));
                }
                return View(todoItem);
            }

            // GET: Todo/Delete/5
            public async Task<IActionResult> Delete(int? id)
            {
                if (id == null)
                {
                    return NotFound();
                }

                var todoItem = await _context.TodoItems
                    .FirstOrDefaultAsync(m => m.Id == id);
                if (todoItem == null)
                {
                    return NotFound();
                }

                var user = await _userManager.GetUserAsync(User); // Lấy "người dùng" "hiện tại"
                if (user == null || todoItem.UserId != user.Id) // "Kiểm tra" "quyền sở hữu" "công việc"
                {
                    return Forbid(); // Nếu "không phải" "chủ sở hữu", "từ chối" "truy cập" (HTTP 403 Forbidden)
                }

                return View(todoItem);
            }

            // POST: Todo/Delete/5
            [HttpPost, ActionName("Delete")]
            [ValidateAntiForgeryToken]
            public async Task<IActionResult> DeleteConfirmed(int id)
            {
                var todoItem = await _context.TodoItems.FindAsync(id);
                if (todoItem == null)
                {
                    return NotFound();
                }
                 var user = await _userManager.GetUserAsync(User); // Lấy "người dùng" "hiện tại"
                if (user == null || todoItem.UserId != user.Id)  // "Kiểm tra" "quyền sở hữu" "công việc"
                {
                    return Forbid(); // Nếu "không phải" "chủ sở hữu", "từ chối" "truy cập" (HTTP 403 Forbidden)
                }

                _context.TodoItems.Remove(todoItem);
                await _context.SaveChangesAsync();
                return RedirectToAction(nameof(Index));
            }

            private bool TodoItemExists(int id)
            {
                return _context.TodoItems.Any(e => e.Id == id);
            }
        }
        ```

    -   **`AdminController.cs` (Trang Admin - "bảo vệ" bằng Policy `RequireAdminRole`):**

        ```csharp
        [Authorize(Policy = "RequireAdminRole")] // Yêu cầu Policy "RequireAdminRole" (chỉ "Admin" "mới được" "truy cập")
        public class AdminController : Controller
        {
            public IActionResult Index()
            {
                return View();
            }
        }
        ```

    -   **`_LoginPartial.cshtml` (Partial View "hiển thị" "trạng thái" "đăng nhập"):**

        ```cshtml
        @using Microsoft.AspNetCore.Identity
        @inject SignInManager<ApplicationUser> SignInManager
        @inject UserManager<ApplicationUser> UserManager

        <ul class="navbar-nav">
        @if (SignInManager.IsSignedIn(User))
        {
            <li class="nav-item">
                <a  class="nav-link text-dark" asp-area="Identity" asp-page="/Account/Manage/Index" title="Manage">Hello @User.Identity?.Name!</a>
            </li>
            <li class="nav-item">
                <form class="form-inline" asp-area="Identity" asp-page="/Account/Logout" asp-route-returnUrl="@Url.Action("Index", "Home", new { area = "" })" method="post" >
                    <button  type="submit" class="nav-link btn btn-link text-dark">Logout</button>
                </form>
            </li>
        }
        else
        {
            <li class="nav-item">
                <a class="nav-link text-dark" asp-area="Identity" asp-page="/Account/Register">Register</a>
            </li>
            <li class="nav-item">
                <a class="nav-link text-dark" asp-area="Identity" asp-page="/Account/Login">Login</a>
            </li>
        }
        </ul>
        ```

**7.2. "Phân Tích" Ví Dụ AuthN/AuthZ - " 'Mổ Xẻ' " Code "Bảo Mật" "Thực Tế" - " 'Đi Sâu' " Vào " 'Ngóc Ngách' ", " 'Hiểu Rõ' " "Cơ Chế" "Bảo Vệ"**

-   **"Phân Tích" Code "Startup.cs":**

    -   **`services.AddDbContext<ApplicationDbContext>(...)`**: "Cấu hình" `DbContext` và "sử dụng" **In-Memory Database** (cho "ví dụ" "đơn giản"). Trong ứng dụng "thực tế", bạn sẽ "sử dụng" database server "thực sự" (SQL Server, PostgreSQL, MySQL, v.v.).
    -   **`services.AddDefaultIdentity<ApplicationUser>(...)`**: **"Đăng ký" ASP.NET Core Identity Service**. `AddDefaultIdentity()` "cấu hình" Identity với "thiết lập" "mặc định" (Cookies Authentication, UserManager, SignInManager, v.v.). `AddRoles<IdentityRole>()` "thêm" **hỗ trợ Roles** vào Identity. `AddEntityFrameworkStores<ApplicationDbContext>()` "kết nối" Identity với `ApplicationDbContext` để "lưu trữ" "dữ liệu" "người dùng" và "vai trò" trong database.
    -   **`services.Configure<IdentityOptions>(...)`**: **"Cấu hình" `IdentityOptions`** để "thiết lập" các "quy tắc" về **"mật khẩu"** (Password Complexity Requirements), **"khóa tài khoản"** (Lockout Settings), và **"tên người dùng"** (User Settings). "Đảm bảo" "mật khẩu" "mạnh" và "tài khoản" được "bảo vệ" khỏi "tấn công" "brute-force".
    -   **`services.ConfigureApplicationCookie(options => { ... })`**: **"Cấu hình" Cookies Authentication Cookie**. `Cookie.HttpOnly = true` và `Cookie.SecurePolicy = CookieSecurePolicy.Always` (trong production) "tăng cường" "bảo mật" cookie. `ExpireTimeSpan` "thiết lập" **"thời gian hết hạn" "cookie"** (session timeout). `LoginPath` và `AccessDeniedPath` "chỉ định" **"đường dẫn" "trang đăng nhập"** và **"trang từ chối truy cập"**.
    -   **`services.AddAuthorization(options => { ... })`**: **"Cấu hình" Authorization Service** và **"định nghĩa" "Authorization Policy" `RequireAdminRole`**. Policy này "yêu cầu" "người dùng" phải có **"vai trò" "Admin"** (sử dụng `RequireRole("Admin")`).
    -   **`app.UseAuthentication()`**: **"Thêm" Authentication Middleware** vào "middleware pipeline". Middleware này "xác thực" "danh tính" "người dùng" cho "mỗi request".
    -   **`app.UseAuthorization()`**: **"Thêm" Authorization Middleware** vào "middleware pipeline" (sau Authentication Middleware). Middleware này "ủy quyền" "truy cập" "tài nguyên" "dựa trên" "Authorization Policies".
    -   **`CreateDefaultUserRoles(app).Wait()`**: "Phương thức" "tạo" **"vai trò" "Admin"** và **"người dùng" "Admin" "mặc định"** khi ứng dụng "khởi động" (chỉ cho "ví dụ" "đơn giản"). Trong ứng dụng "thực tế", bạn sẽ có "cơ chế" "quản lý" "vai trò" và "người dùng" "admin" "chuyên nghiệp" hơn (ví dụ: trang "quản trị" "người dùng" và "vai trò").

-   **"Phân Tích" Code "AccountController.cs":**

    -   **`UserManager<ApplicationUser>` và `SignInManager<ApplicationUser>`**: "Dependency Injection" (DI) của `UserManager` và `SignInManager` - "công cụ" "chính" của ASP.NET Core Identity để "quản lý" "người dùng" và "đăng nhập".
    -   **`[AllowAnonymous]` attribute**: "Áp dụng" cho các Actions `Register` và `Login` để **"cho phép" "truy cập" "vô danh"** (anonymous access) - "ai cũng có thể" "truy cập" trang "đăng ký" và "đăng nhập".
    -   **`[ValidateAntiForgeryToken]` attribute**: **"Bảo vệ" chống lại "tấn công" CSRF** (Cross-Site Request Forgery) cho các Actions `Register`, `Login`, và `Logout` (POST requests).
    -   **`_userManager.CreateAsync(user, model.Password)`**: "Tạo" "người dùng" "mới" bằng `UserManager`. `CreateAsync()` **"tự động" "băm" "mật khẩu"** (password hashing) "an toàn" bằng `PasswordHasher`.
    -   **`_signInManager.PasswordSignInAsync(model.Email, model.Password, model.RememberMe, lockoutOnFailure: false)`**: **"Đăng nhập" "người dùng"** bằng `SignInManager`. `PasswordSignInAsync()` "xác minh" "mật khẩu" (so sánh "hash value" mật khẩu "nhập vào" với "hash value" "đã lưu trữ") và "tạo" **"Authentication Cookie"** (session-based authentication) nếu "xác thực thành công".
    -   **`_signInManager.SignOutAsync()`**: **"Đăng xuất" "người dùng"**. "Xóa" "Authentication Cookie" để "kết thúc" "phiên" "đăng nhập".
    -   **`[HttpGet] AccessDenied()`**: Action "trang từ chối truy cập". "Hiển thị" View "AccessDenied.cshtml" khi "ủy quyền thất bại".
    -   **`RedirectToLocal(returnUrl)`**: "Phương thức" "hỗ trợ" "chuyển hướng" "an toàn" sau "đăng nhập" (chỉ "chuyển hướng" đến "URL nội bộ" của ứng dụng - "ngăn chặn" "tấn công" "chuyển hướng" "mở").

-   **"Phân Tích" Code "TodoController.cs":**

    -   **`[Authorize]` attribute**: "Áp dụng" cho **"toàn bộ" `TodoController`**. **"Yêu cầu" "xác thực"** cho "mọi Action" trong `TodoController`. "Người dùng" phải "đăng nhập" để "truy cập" các "chức năng" "quản lý" "công việc".
    -   **`_userManager.GetUserAsync(User)`**: "Lấy" **`ApplicationUser` "hiện tại"** từ `HttpContext.User` (User Identity) bằng `UserManager`. `User` property trong `ControllerBase` là "shortcut" để "truy cập" `HttpContext.User`.
    -   **`return Challenge()`**: "Trả về" `ChallengeResult` khi `GetUserAsync(User)` "trả về" `null` (người dùng "chưa xác thực"). `ChallengeResult` "kích hoạt" Authentication Middleware để **"thử thách" "xác thực"** (thường "chuyển hướng" đến "trang đăng nhập").
    -   **`_context.TodoItems.Where(t => t.UserId == user.Id).ToListAsync()`**: **"Lọc" "danh sách công việc"** chỉ **"cho" "người dùng" "hiện tại"**. "Đảm bảo" "người dùng" chỉ "xem" được "công việc" "cá nhân" (data isolation).
    -   **`todoItem.UserId = user.Id`**: **"Gán" `UserId`** cho `TodoItem` khi "tạo" "công việc" "mới". "Liên kết" "công việc" với "người dùng" "tạo ra" nó.
    -   **"Kiểm tra" "quyền sở hữu" "công việc" trong `Edit()` và `Delete()` Actions**: "Kiểm tra" xem **"người dùng" "hiện tại" có phải là "chủ sở hữu"** của "công việc" "đang sửa" hoặc "xóa" hay không (`todoItem.UserId != user.Id`). Nếu "không phải" "chủ sở hữu", **`return Forbid()`** - "trả về" `ForbidResult` (HTTP 403 Forbidden) - **"từ chối" "truy cập"** (Authorization failure). "Thực hiện" **"resource-based authorization"** (phân quyền "dựa trên" "tài nguyên").

-   **"Phân Tích" Code "AdminController.cs":**

    -   **`[Authorize(Policy = "RequireAdminRole")]` attribute**: "Áp dụng" **`[Authorize]` attribute với "policy" `RequireAdminRole`** cho `AdminController`. **"Yêu cầu" "Authorization Policy" `RequireAdminRole`** để "truy cập" "toàn bộ" `AdminController`. Chỉ "người dùng" "có" "vai trò" "Admin" "mới được" "phép" "truy cập" trang "quản trị". "Thực hiện" **Role-Based Authorization**.

-   **"Phân Tích" Code `_LoginPartial.cshtml`:**

    -   **`@inject SignInManager<ApplicationUser> SignInManager` và `@inject UserManager<ApplicationUser> UserManager`**: "Dependency Injection" (DI) của `SignInManager` và `UserManager` trong Razor Partial View.
    -   **`@if (SignInManager.IsSignedIn(User)) { ... } else { ... }`**: **"Kiểm tra" "trạng thái" "đăng nhập"** bằng `SignInManager.IsSignedIn(User)`. "Hiển thị" "giao diện" "khác nhau" "dựa trên" "trạng thái" "đăng nhập" ( "Xin chào, [Tên người dùng]!" và nút "Đăng xuất" khi "đã đăng nhập", "Đăng ký" và "Đăng nhập" links khi "chưa đăng nhập").
    -   **`asp-area="Identity" asp-page="/Account/Manage/Index"`**: "Liên kết" đến trang "quản lý" "tài khoản" (ASP.NET Core Identity Razor Pages).
    -   **`asp-area="Identity" asp-page="/Account/Logout"`**: "Form" "đăng xuất" (POST request đến "trang đăng xuất" của ASP.NET Core Identity Razor Pages).
    -   **`@User.Identity?.Name`**: "Hiển thị" **"tên người dùng"** (username) "đã đăng nhập" từ `User.Identity?.Name`.

**7.3. "Mở Rộng" Ví Dụ AuthN/AuthZ - " 'Nâng Cấp' " "Bảo Mật" Ứng Dụng "Lên Tầm Cao Mới" - " 'Thêm' " "Vũ Khí", " 'Củng Cố' " "Thành Trì", " 'Vươn Tới' " "Đỉnh Cao"**

-   **"Nâng Cấp" "Bảo Mật" Ứng Dụng "Quản Lý Công Việc" - " 'Mở Rộng' " "Chức Năng", " 'Tăng Cường' " "An Ninh":**

    -   **"Thêm" Social Login (Đăng Nhập Mạng Xã Hội):** "Tích hợp" **Social Login** (Google, Facebook, v.v.) để "cung cấp" "phương thức" "đăng nhập" "tiện lợi" và "hiện đại" hơn cho người dùng. "Sử dụng" các NuGet packages `Microsoft.AspNetCore.Authentication.Google`, `Microsoft.AspNetCore.Authentication.Facebook`, v.v. và "cấu hình" trong `Startup.cs`.
    -   **"Triển khai" Multi-Factor Authentication (MFA - Xác Thực Đa Yếu Tố):** "Tăng cường" "bảo mật" "tài khoản" bằng cách "yêu cầu" người dùng "cung cấp" **"mã OTP"** (one-time password) "ngoài" "mật khẩu". "Sử dụng" ASP.NET Core Identity MFA features ( `services.AddDefaultIdentity<ApplicationUser>().AddDefaultTokenProviders()` và "thêm" "code" MFA vào "trang đăng nhập" và "trang quản lý tài khoản").
    -   **"Áp dụng" Policy-Based Authorization "Chi Tiết" Hơn:** "Thay vì" chỉ "kiểm tra" "quyền sở hữu" "công việc" trong code (trong `Edit()` và `Delete()` Actions), "tạo" **"Custom Authorization Requirement" `OwnsTodoItemRequirement`** và **"Custom Authorization Handler" `OwnsTodoItemHandler`** để "đóng gói" "logic" "kiểm tra" "quyền sở hữu" "công việc". "Định nghĩa" **"Authorization Policy" `OwnsTodoItemPolicy`** "sử dụng" `OwnsTodoItemRequirement`. "Sử dụng" `[Authorize(Policy = "OwnsTodoItemPolicy")]` attribute cho các Actions `Edit()` và `Delete()`. "Tăng" "tính 'mô-đun' " và "tính 'tái sử dụng' " của "logic" "phân quyền".
    -   **"Thêm" Role-Based Authorization "Chi Tiết" Hơn:** "Thêm" "các "vai trò" "khác"** (ví dụ: "Editor", "Viewer") ngoài "vai trò" "Admin". "Định nghĩa" "Authorization Policies" "khác nhau" cho các "vai trò" "khác nhau". "Ví dụ": "Policy" `RequireEditorRole` (yêu cầu "vai trò" "Editor"), "Policy" `RequireViewerRole` (yêu cầu "vai trò" "Viewer"). "Sử dụng" các "policies" này trong `[Authorize]` attributes cho các Controller Actions "khác nhau" để "phân quyền" "chi tiết" hơn "dựa trên" "vai trò".
    -   **"Triển khai" Claims-Based Authorization:** "Thay vì" "dựa vào" "vai trò", "phân quyền" "dựa trên" **"claims"** của "người dùng". "Ví dụ": "thêm" "claim" `level_thanh_vien` (level thành viên) cho "người dùng". "Định nghĩa" "Authorization Policies" "dựa trên" "claims" `level_thanh_vien` (ví dụ: "Policy" `RequireVangLevel` - yêu cầu "claim" `level_thanh_vien` có giá trị >= "Vàng"). "Sử dụng" các "policies" này trong `[Authorize]` attributes.
    -   **"Giám sát" và "Kiểm Toán" Authentication và Authorization:** "Thêm" **"logging"** cho "hoạt động" "đăng nhập", "đăng xuất", "lỗi" "xác thực", "lỗi" "ủy quyền". "Sử dụng" **Application Insights** hoặc **Serilog** để "ghi log" "tập trung" và "phân tích" "log data". "Thiết lập" **"cảnh báo"** khi "phát hiện" "hoạt động" "bất thường" hoặc "tấn công" "bảo mật".

**Tổng Kết Chương 7:**

-   Bạn đã " 'chứng kiến' " Authentication và Authorization " 'vận hành' "** trong một "ví dụ" ứng dụng web ASP.NET Core MVC "thực tế".
    -   "Thấy" cách **ASP.NET Core Identity** "giúp" "triển khai" Authentication và Authorization "dễ dàng" và "nhanh chóng".
    -   "Hiểu" cách **`[Authorize]` attribute** "bảo vệ" Controller Actions và Razor Pages.
    -   "Nắm bắt" cách **Authorization Policies** và **Role-Based Authorization** "phân quyền" "truy cập" "tài nguyên".
    -   "Biết cách" **"mở rộng"** và **"nâng cấp"** "bảo mật" ứng dụng bằng cách "thêm" các "tính năng" Authentication và Authorization "nâng cao".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 8: "Tổng Kết Hành Trình AuthN/AuthZ" và "Bước Tiếp Theo" - "Trở Thành 'Bậc Thầy' Bảo Mật Ứng Dụng"**. Chúng ta sẽ "ôn lại" "kiến thức" AuthN/AuthZ "cốt lõi", "nhận" "lời khuyên" "chân thành" để "tiếp tục" "nâng cao" kỹ năng, và "khám phá" các "tài nguyên" "bổ ích" để "học sâu" hơn về Authentication và Authorization trong .NET.

Bạn có câu hỏi nào về "ứng dụng thực tế" của Authentication và Authorization này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" "bảo mật" ứng dụng web.