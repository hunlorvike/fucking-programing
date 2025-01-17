# ASP.NET Identity: Quản Lý Người Dùng, Vai Trò và Xác Thực

## Mục Lục

1. [Khái niệm về ASP.NET Identity](#khái-niệm-về-aspnet-identity)
2. [Quản lý người dùng và vai trò](#quản-lý-người-dùng-và-vai-trò)
    - [2.1. Quản lý người dùng](#21-quản-lý-người-dùng)
    - [2.2. Quản lý vai trò](#22-quản-lý-vai-trò)
3. [Xác thực và phân quyền người dùng](#xác-thực-và-phân-quyền-người-dùng)
    - [3.1. Đăng nhập và đăng ký người dùng](#31-đăng-nhập-và-đăng-ký-người-dùng)
    - [3.2. Phân quyền người dùng với roles](#32-phân-quyền-người-dùng-với-roles)
4. [Tùy chỉnh bảng Identity](#tùy-chỉnh-bảng-identity)
    - [4.1. Tạo bảng tùy chỉnh](#41-tạo-bảng-tùy-chỉnh)
    - [4.2. Cấu hình bảng tùy chỉnh trong ASP.NET Core](#42-cấu-hình-bảng-tùy-chỉnh-trong-aspnet-core)
5. [Cấu hình xác thực và phân quyền trong ASP.NET Core](#cấu-hình-xác-thực-và-phân-quyền-trong-aspnet-core)
6. [Quản lý mật khẩu và xác thực hai yếu tố](#quản-lý-mật-khẩu-và-xác-thực-hai-yếu-tố)
7. [Tóm tắt](#tóm-tắt)

---

## 1. Khái niệm về ASP.NET Identity

**ASP.NET Identity** là một thư viện trong ASP.NET Core giúp quản lý người dùng, vai trò, và quyền truy cập trong các
ứng dụng web. ASP.NET Identity cung cấp các tính năng như xác thực người dùng (authentication), phân quyền (
authorization), và quản lý các thông tin người dùng (chẳng hạn như email, mật khẩu, vai trò, v.v.). Nó dễ dàng tích hợp
với các hệ thống khác như OAuth, OpenID Connect, và các dịch vụ bên ngoài như Google hoặc Facebook.

ASP.NET Identity hỗ trợ việc quản lý người dùng, bao gồm các tính năng như đăng nhập, đăng ký người dùng, thay đổi mật
khẩu, và xác thực hai yếu tố.

---

## 2. Quản lý người dùng và vai trò

### 2.1. Quản lý người dùng

ASP.NET Identity cung cấp một lớp **UserManager** giúp bạn dễ dàng quản lý người dùng trong hệ thống, bao gồm các chức
năng như đăng ký, đăng nhập, xác thực, và cập nhật thông tin người dùng.

**Ví dụ** về cách sử dụng UserManager để tạo người dùng mới:

```csharp
public class RegisterModel : PageModel
{
    private readonly UserManager<ApplicationUser> _userManager;

    public RegisterModel(UserManager<ApplicationUser> userManager)
    {
        _userManager = userManager;
    }

    public async Task<IActionResult> OnPostAsync(string username, string password)
    {
        var user = new ApplicationUser { UserName = username };
        var result = await _userManager.CreateAsync(user, password);

        if (result.Succeeded)
        {
            // Đăng nhập thành công và chuyển hướng
            return RedirectToPage("/Index");
        }

        // Xử lý lỗi nếu đăng ký không thành công
        return Page();
    }
}
```

### 2.2. Quản lý vai trò

ASP.NET Identity hỗ trợ vai trò (roles) để phân quyền cho người dùng. Bạn có thể sử dụng **RoleManager** để tạo, quản lý
vai trò, và phân quyền cho người dùng.

**Ví dụ** về cách tạo và phân vai trò cho người dùng:

```csharp
public class ApplicationSeeder
{
    public static async Task SeedRoles(RoleManager<IdentityRole> roleManager)
    {
        string[] roleNames = { "Admin", "User", "Manager" };

        foreach (var roleName in roleNames)
        {
            var roleExist = await roleManager.RoleExistsAsync(roleName);
            if (!roleExist)
            {
                await roleManager.CreateAsync(new IdentityRole(roleName));
            }
        }
    }

    public static async Task AssignRole(UserManager<ApplicationUser> userManager, ApplicationUser user)
    {
        if (!await userManager.IsInRoleAsync(user, "Admin"))
        {
            await userManager.AddToRoleAsync(user, "Admin");
        }
    }
}
```

---

## 3. Xác thực và phân quyền người dùng

### 3.1. Đăng nhập và đăng ký người dùng

Xác thực người dùng trong ASP.NET Identity thường được thực hiện thông qua **SignInManager**. Bạn có thể thực hiện đăng
nhập và đăng ký người dùng từ frontend hoặc backend.

**Ví dụ đăng nhập người dùng**:

```csharp
public class LoginModel : PageModel
{
    private readonly SignInManager<ApplicationUser> _signInManager;

    public LoginModel(SignInManager<ApplicationUser> signInManager)
    {
        _signInManager = signInManager;
    }

    public async Task<IActionResult> OnPostAsync(string username, string password)
    {
        var result = await _signInManager.PasswordSignInAsync(username, password, false, false);

        if (result.Succeeded)
        {
            return RedirectToPage("/Index");
        }

        // Xử lý lỗi đăng nhập
        return Page();
    }
}
```

### 3.2. Phân quyền người dùng với roles

ASP.NET Identity cho phép phân quyền cho người dùng dựa trên vai trò của họ. Bạn có thể kiểm tra xem người dùng có vai
trò cụ thể hay không và cấp quyền truy cập cho các phần của ứng dụng dựa trên đó.

**Ví dụ phân quyền dựa trên vai trò**:

```csharp
public class AdminController : Controller
{
    private readonly UserManager<ApplicationUser> _userManager;

    public AdminController(UserManager<ApplicationUser> userManager)
    {
        _userManager = userManager;
    }

    [Authorize(Roles = "Admin")]
    public IActionResult Index()
    {
        return View();
    }
}
```

---

## 4. Tùy chỉnh bảng Identity

### 4.1. Tạo bảng tùy chỉnh

Mặc định, ASP.NET Identity sử dụng các bảng như `AspNetUsers`, `AspNetRoles`, `AspNetUserRoles`, v.v., để lưu trữ thông
tin người dùng và vai trò. Tuy nhiên, nếu bạn muốn lưu trữ thêm thông tin tùy chỉnh hoặc thay đổi cấu trúc các bảng, bạn
có thể tùy chỉnh các bảng này bằng cách tạo các lớp kế thừa từ các lớp mặc định của ASP.NET Identity.

**Ví dụ tạo lớp người dùng tùy chỉnh**:

```csharp
public class ApplicationUser : IdentityUser
{
    public string FullName { get; set; }
    public DateTime DateOfBirth { get; set; }
}
```

### 4.2. Cấu hình bảng tùy chỉnh trong ASP.NET Core

Khi bạn đã tạo các lớp tùy chỉnh, bạn cần cấu hình chúng trong `DbContext` để sử dụng với Entity Framework Core.

```csharp
public class ApplicationDbContext : IdentityDbContext<ApplicationUser>
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options) { }

    protected override void OnModelCreating(ModelBuilder builder)
    {
        base.OnModelCreating(builder);

        // Tùy chỉnh các bảng hoặc mối quan hệ nếu cần
    }
}
```

---

## 5. Cấu hình xác thực và phân quyền trong ASP.NET Core

Trong `Startup.cs` hoặc `Program.cs`, bạn cần cấu hình dịch vụ xác thực và phân quyền cho ASP.NET Identity.

**Ví dụ cấu hình dịch vụ Identity**:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddDbContext<ApplicationDbContext>(options =>
        options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));

    services.AddIdentity<ApplicationUser, IdentityRole>()
        .AddEntityFrameworkStores<ApplicationDbContext>()
        .AddDefaultTokenProviders();

    services.AddAuthorization(options =>
    {
        options.AddPolicy("AdminOnly", policy => policy.RequireRole("Admin"));
    });

    services.AddRazorPages();
}
```

---

## 6. Quản lý mật khẩu và xác thực hai yếu tố

ASP.NET Identity hỗ trợ tính năng **quản lý mật khẩu** và **xác thực hai yếu tố (2FA)** để tăng cường bảo mật.

- **Quản lý mật khẩu**: Bạn có thể cấu hình các chính sách mật khẩu, ví dụ: yêu cầu mật khẩu dài ít nhất 8 ký tự, chứa
  cả chữ hoa, chữ thường, số, và ký tự đặc biệt.
- **Xác thực hai yếu tố**: ASP.NET Identity hỗ trợ xác thực hai yếu tố thông qua SMS hoặc ứng dụng như Google
  Authenticator.

---

## 7. Tóm tắt

ASP.NET Identity là một giải pháp mạnh mẽ để quản lý người dùng và phân quyền trong ứng dụng ASP.NET Core. Nó cung cấp
các chức năng như đăng ký người dùng, đăng nhập, phân quyền với vai trò, và hỗ trợ xác thực hai yếu tố. Bạn có thể tùy
chỉnh bảng Identity để lưu trữ thông tin người dùng theo cách riêng, đồng thời quản lý mật khẩu và quyền truy cập của
người dùng hiệu quả.
