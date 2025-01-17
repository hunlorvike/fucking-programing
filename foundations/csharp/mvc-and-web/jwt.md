# Hướng Dẫn Sử Dụng JWT Trong C# .NET: Tổng Quan, Triển Khai và Các Yếu Tố Bảo Mật

**JSON Web Token (JWT)** là một chuẩn mã hóa dùng để truyền tải thông tin giữa các bên một cách an toàn và không cần
trạng thái (stateless). Với đặc tính “không trạng thái,” JWT trở thành lựa chọn hàng đầu trong việc xác thực và phân
quyền cho các ứng dụng RESTful API, giúp đơn giản hóa quá trình xác thực trên các hệ thống phân tán hoặc các ứng dụng có
yêu cầu về bảo mật.

## Mục Lục

1. [Tổng Quan về JWT](#1-tổng-quan-về-jwt)
    - [JWT là gì?](#jwt-là-gì)
    - [JWT hoạt động như thế nào?](#jwt-hoạt-động-như-thế-nào)
    - [Cấu trúc của JWT](#cấu-trúc-của-jwt)
2. [Sử Dụng JWT trong C# .NET](#2-sử-dụng-jwt-trong-c-net)

    - [Thiết lập JWT trong ASP.NET Core](#a-thiết-lập-jwt-trong-aspnet-core)
    - [Tạo JWT trong Controller](#b-tạo-jwt-trong-controller)

3. [Xác Thực và Phân Quyền trong Các API Khác](#3-xác-thực-và-phân-quyền-trong-các-api-khác)

4. [Các Thành Phần Quan Trọng của JWT](#4-các-thành-phần-quan-trọng-của-jwt)

5. [Bảo Mật JWT](#5-bảo-mật-jwt)

6. [Kết Luận](#kết-luận)

---

## 1. Tổng Quan về JWT

### JWT là gì?

JWT là một chuỗi token chứa thông tin xác thực người dùng và các quyền liên quan. JWT gồm ba phần chính, được ngăn cách
bằng dấu chấm (`.`):

- **Header**: Chứa loại token và thuật toán mã hóa.
- **Payload**: Chứa các claims (dữ liệu) liên quan đến người dùng hoặc phiên làm việc.
- **Signature**: Được tạo từ Header và Payload bằng một khóa bí mật để xác thực tính toàn vẹn của token.

Ví dụ về JWT:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

### JWT hoạt động như thế nào?

1. Khi người dùng đăng nhập, hệ thống xác thực thông tin đăng nhập và tạo một JWT chứa thông tin người dùng.
2. JWT này được gửi về client, lưu trữ ở phía client (trong `localStorage`, `sessionStorage`, hoặc `httpOnly cookies`).
3. Trong các yêu cầu tới server, client gửi JWT qua HTTP header (Authorization: Bearer `JWT`) để server xác minh và cấp
   quyền truy cập tài nguyên mà không cần lưu trạng thái.

### Cấu trúc của JWT

1. **Header**: Chứa thông tin mã hóa, ví dụ `{"alg": "HS256", "typ": "JWT"}`.
2. **Payload**: Chứa các claims (dữ liệu), như `userId`, `roles`, hoặc thông tin liên quan đến phiên làm việc, ví dụ:
   ```json
   {
     "sub": "1234567890",
     "name": "John Doe",
     "iat": 1516239022
   }
   ```
3. **Signature**: Được tạo từ header, payload và khóa bí mật của server, giúp xác minh tính toàn vẹn của token.

---

## 2. Sử Dụng JWT trong C# .NET

Trong ASP.NET Core, việc sử dụng JWT thường kết hợp với **ASP.NET Core Identity** hoặc các hệ thống xác thực không trạng
thái (stateless authentication) cho các API.

### a. Thiết lập JWT trong ASP.NET Core

1. **Cài đặt các thư viện cần thiết**:

    - Cài đặt thư viện `Microsoft.AspNetCore.Authentication.JwtBearer` qua **NuGet Package Manager**:
      ```shell
      Install-Package Microsoft.AspNetCore.Authentication.JwtBearer
      ```

2. **Cấu hình JWT trong `Startup.cs`**:

    - Đầu tiên, thêm cấu hình cho JWT trong `ConfigureServices` của `Startup.cs` để ASP.NET biết cách xác thực yêu cầu
      từ client.

   ```csharp
   public void ConfigureServices(IServiceCollection services)
   {
       services.AddAuthentication(options =>
       {
           options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
           options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
       })
       .AddJwtBearer(options =>
       {
           options.TokenValidationParameters = new TokenValidationParameters
           {
               ValidateIssuer = true,
               ValidateAudience = true,
               ValidateLifetime = true,
               ValidateIssuerSigningKey = true,
               ValidIssuer = Configuration["Jwt:Issuer"],
               ValidAudience = Configuration["Jwt:Audience"],
               IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(Configuration["Jwt:Key"]))
           };
       });

       services.AddControllers();
   }

   public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
   {
       app.UseRouting();
       app.UseAuthentication();
       app.UseAuthorization();
       app.UseEndpoints(endpoints => endpoints.MapControllers());
   }
   ```

3. **Cấu hình `appsettings.json`**:

    - Các giá trị như `Issuer`, `Audience`, và `Key` có thể được thêm vào `appsettings.json` để dễ dàng quản lý và chỉnh
      sửa.

   ```json
   {
     "Jwt": {
       "Key": "YourSecureSecretKeyHere",
       "Issuer": "YourIssuer",
       "Audience": "YourAudience"
     }
   }
   ```

### b. Tạo JWT trong Controller

Trong các API xác thực (ví dụ: `AuthController`), bạn có thể tạo JWT sau khi người dùng đăng nhập thành công.

```csharp
using System;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;

[Route("api/[controller]")]
[ApiController]
public class AuthController : ControllerBase
{
    private readonly IConfiguration _config;

    public AuthController(IConfiguration config)
    {
        _config = config;
    }

    [HttpPost("login")]
    public IActionResult Login([FromBody] UserLogin login)
    {
        // Giả sử ValidateUser là phương thức kiểm tra thông tin đăng nhập của người dùng
        if (ValidateUser(login))
        {
            var tokenString = GenerateJwtToken();
            return Ok(new { token = tokenString });
        }
        return Unauthorized();
    }

    private string GenerateJwtToken()
    {
        var securityKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(_config["Jwt:Key"]));
        var credentials = new SigningCredentials(securityKey, SecurityAlgorithms.HmacSha256);

        var claims = new[]
        {
            new Claim(JwtRegisteredClaimNames.Sub, "UserIdentifier"),
            new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString())
        };

        var token = new JwtSecurityToken(
            issuer: _config["Jwt:Issuer"],
            audience: _config["Jwt:Audience"],
            claims: claims,
            expires: DateTime.Now.AddMinutes(30),
            signingCredentials: credentials);

        return new JwtSecurityTokenHandler().WriteToken(token);
    }
}
```

---

## 3. Xác Thực và Phân Quyền trong Các API Khác

Khi có JWT, client sẽ gửi JWT trong header `Authorization` của các yêu cầu tiếp theo với format `Bearer <token>`.
ASP.NET sẽ tự động kiểm tra và cấp quyền nếu JWT hợp lệ.

- **Ví dụ Header**:

  ```http
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
  ```

- **Kiểm tra quyền truy cập trong Controller**:

    - Để hạn chế quyền truy cập vào các endpoint, sử dụng `[Authorize]` trong Controller hoặc các phương thức riêng lẻ.

      ```csharp
      [Authorize]
      [Route("api/[controller]")]
      [ApiController]
      public class SampleController : ControllerBase
      {
          [HttpGet("secure-data")]
          public IActionResult GetSecureData()
          {
              return Ok(new { data = "This is secured data" });
          }
      }
      ```

---

## 4. Các Thành Phần Quan Trọng của JWT

- **Claims**: Các thông tin liên quan tới người dùng (như `userId`, `roles`, `permissions`).
- **Issuer và Audience**: Xác định ai tạo JWT và ai là người nhận JWT, được cấu hình trong `appsettings.json`.
- **Signature**: Đảm bảo tính toàn vẹn của JWT, ngăn chặn việc giả mạo hoặc thay đổi dữ liệu bên trong token.

---

## 5. Bảo Mật JWT

- **Thời Gian Sống của JWT (Expiration)**:

- Để hạn chế rủi ro bảo mật, nên thiết lập thời gian sống ngắn cho JWT và sử dụng **Refresh Tokens** để cấp mới JWT khi
  hết hạn.
- **Refresh Tokens**:

    - Là mã có thời gian sống dài hơn, thường dùng để lấy JWT mới mà không cần yêu cầu đăng nhập lại.

- **Lưu trữ JWT an toàn**:

    - Tránh lưu trữ JWT trong các cookie hoặc storage không bảo mật.
    - Sử dụng **HTTP-only cookies** hoặc **Secure storage** để ngăn ngừa truy cập từ JavaScript.

- **Xử lý JWT bị đánh cắp**:
    - Sử dụng danh sách đen (blacklist) trên server để thu hồi các JWT không hợp lệ hoặc đã bị đánh cắp.

---

## 6. Kết Luận

**JWT** là một giải pháp mạnh mẽ và hiệu quả cho các ứng dụng không trạng thái. Tuy nhiên, khi triển khai JWT trong C#
.NET, cần phải chú trọng đến các cơ chế bảo mật như refresh token, danh sách đen và cách lưu trữ an toàn để đảm bảo tính
bảo mật cho ứng dụng.
