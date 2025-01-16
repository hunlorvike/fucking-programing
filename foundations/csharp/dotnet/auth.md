# Authentication & Authorization: Tổng Quan và Hướng Dẫn

## Mục Lục

1. [Khái niệm về Authentication & Authorization](#khái-niệm-về-authentication--authorization)
2. [Authentication: Chứng thực người dùng](#authentication-chứng-thực-người-dùng)
   - [2.1. OAuth2](#21-oauth2)
   - [2.2. OpenID Connect](#22-openid-connect)
   - [2.3. IdentityServer](#23-identityserver)
3. [Authorization: Phân quyền người dùng](#authorization-phân-quyền-người-dùng)
   - [3.1. Role-based Authorization](#31-role-based-authorization)
   - [3.2. Policy-based Authorization](#32-policy-based-authorization)
4. [Cách tích hợp trong ASP.NET Core](#cách-tích-hợp-trong-aspnet-core)
   - [4.1. Authentication Middleware](#41-authentication-middleware)
   - [4.2. Authorization Middleware](#42-authorization-middleware)
5. [Kiểm thử Authentication & Authorization](#kiểm-thử-authentication--authorization)
6. [Thực hành tốt nhất với Authentication & Authorization](#thực-hành-tốt-nhất-với-authentication--authorization)
7. [Tóm tắt](#tóm-tắt)

---

## 1. Khái niệm về Authentication & Authorization

- **Authentication (Chứng thực)**: Quá trình xác định danh tính của người dùng. Nó đảm bảo rằng người dùng là ai họ tuyên bố.
- **Authorization (Phân quyền)**: Quá trình xác định quyền truy cập của người dùng vào tài nguyên cụ thể, dựa trên vai trò (roles) hoặc chính sách (policies).

### Sự khác biệt:
- **Authentication** trả lời câu hỏi: *"Bạn là ai?"*
- **Authorization** trả lời câu hỏi: *"Bạn có quyền làm gì?"*

---

## 2. Authentication: Chứng thực người dùng

Authentication trong ứng dụng hiện đại thường dựa trên các tiêu chuẩn bảo mật, như **OAuth2** và **OpenID Connect**, để đảm bảo sự an toàn và tính di động.

### 2.1. OAuth2

- **Mục đích**: Cho phép ứng dụng bên thứ ba truy cập tài nguyên của người dùng trên một dịch vụ khác một cách an toàn, mà không cần cung cấp mật khẩu.
- **Các thành phần chính**:
  - **Resource Owner**: Người dùng sở hữu tài nguyên.
  - **Client**: Ứng dụng muốn truy cập tài nguyên.
  - **Authorization Server**: Máy chủ chứng thực và cung cấp token.
  - **Resource Server**: Máy chủ chứa tài nguyên, xác thực token.

**Luồng hoạt động chính**:
1. Người dùng ủy quyền ứng dụng.
2. Ứng dụng nhận **Access Token** từ Authorization Server.
3. Sử dụng **Access Token** để truy cập tài nguyên.

**Ví dụ**:

```plaintext
Ứng dụng sử dụng OAuth2 để truy cập API của Google, như lấy danh sách email của người dùng.
```

### 2.2. OpenID Connect

- **Mục đích**: Mở rộng OAuth2 để cung cấp khả năng *chứng thực* (Authentication) bên cạnh *ủy quyền* (Authorization).
- **Thành phần bổ sung**:
  - **ID Token**: Chứa thông tin về người dùng (như tên, email), sử dụng để xác thực.
  
**Ưu điểm**:
- Phù hợp cho các ứng dụng cần chứng thực người dùng (Single Sign-On - SSO).
- Dễ dàng tích hợp với nhiều nền tảng.

### 2.3. IdentityServer

- **Mục đích**: Một công cụ mã nguồn mở giúp triển khai OAuth2 và OpenID Connect.
- **Ứng dụng**: Được sử dụng để thiết lập Identity Provider (IdP), hỗ trợ quản lý người dùng và quyền truy cập trong ứng dụng ASP.NET Core.

**Tính năng chính**:
- Quản lý người dùng và thông tin xác thực.
- Hỗ trợ đa nền tảng và đa loại ứng dụng (SPA, Mobile, API).

---

## 3. Authorization: Phân quyền người dùng

Authorization trong ASP.NET Core dựa trên hai mô hình chính: **Role-based** và **Policy-based**.

### 3.1. Role-based Authorization

- **Định nghĩa**: Người dùng được gán một hoặc nhiều vai trò (roles), mỗi vai trò xác định quyền truy cập tài nguyên.
- **Cách cấu hình**:
  - Gán vai trò cho người dùng.
  - Sử dụng thuộc tính `[Authorize(Roles = "Admin")]` để giới hạn quyền truy cập.

**Ví dụ**:

```csharp
[Authorize(Roles = "Admin")]
public IActionResult ManageUsers()
{
    return View();
}
```

### 3.2. Policy-based Authorization

- **Định nghĩa**: Phân quyền dựa trên các chính sách (policies), cho phép kiểm tra các điều kiện phức tạp hơn.
- **Cách cấu hình**:
  1. Định nghĩa chính sách trong `Startup.cs` hoặc `Program.cs`.
  2. Áp dụng chính sách trong controller hoặc action.

**Ví dụ**:

Định nghĩa chính sách yêu cầu người dùng phải trên 18 tuổi:
```csharp
services.AddAuthorization(options =>
{
    options.AddPolicy("Over18", policy =>
        policy.RequireClaim("Age", "18"));
});
```

Áp dụng chính sách:
```csharp
[Authorize(Policy = "Over18")]
public IActionResult AccessRestrictedContent()
{
    return View();
}
```

---

## 4. Cách tích hợp trong ASP.NET Core

### 4.1. Authentication Middleware

- Cấu hình trong `Program.cs`:

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddAuthentication("CookieAuth")
    .AddCookie("CookieAuth", options =>
    {
        options.LoginPath = "/Account/Login";
    });

var app = builder.Build();

app.UseAuthentication();
```

### 4.2. Authorization Middleware

- Kích hoạt authorization sau authentication:
```csharp
app.UseAuthorization();
```

- Kết hợp `[Authorize]` để kiểm soát quyền truy cập.

---

## 5. Kiểm thử Authentication & Authorization

### Authentication
- Sử dụng các token giả (mock token) để kiểm tra logic đăng nhập và xác thực.

### Authorization
- Thực hiện kiểm tra các roles và policies bằng cách tạo người dùng với quyền cụ thể.
  
**Ví dụ kiểm thử với xUnit**:
```csharp
[Fact]
public async Task AdminRole_ShouldAccess_AdminPage()
{
    var user = new ClaimsPrincipal(new ClaimsIdentity(new[]
    {
        new Claim(ClaimTypes.Role, "Admin")
    }, "mock"));

    var controller = new AdminController
    {
        ControllerContext = new ControllerContext
        {
            HttpContext = new DefaultHttpContext { User = user }
        }
    };

    var result = await controller.ManageUsers();
    Assert.IsType<ViewResult>(result);
}
```

---

## 6. Thực hành tốt nhất với Authentication & Authorization

1. **Sử dụng HTTPS**: Bảo vệ dữ liệu trong quá trình truyền.
2. **Token Expiration**: Thiết lập thời gian hết hạn token để giảm nguy cơ bị lạm dụng.
3. **Quản lý Claims cẩn thận**: Chỉ thêm các thông tin cần thiết vào Claims.
4. **Cập nhật Framework thường xuyên**: Đảm bảo hệ thống bảo mật được cập nhật.
5. **Không lạm dụng quyền Admin**: Giới hạn quyền truy cập với vai trò Admin chỉ khi thực sự cần thiết.

---

## 7. Tóm tắt

**Authentication & Authorization** là hai thành phần quan trọng trong bảo mật ứng dụng. Chứng thực xác định danh tính người dùng, còn phân quyền đảm bảo họ chỉ truy cập được các tài nguyên được phép. Sử dụng các tiêu chuẩn như OAuth2 và OpenID Connect giúp xây dựng hệ thống bảo mật mạnh mẽ, trong khi tích hợp ASP.NET Core với các middleware giúp triển khai nhanh chóng và hiệu quả.