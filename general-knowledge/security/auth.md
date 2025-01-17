# Authentication và Authorization trong C# .NET ASP.NET

## Mục Lục

1. [Tổng quan về Authentication và Authorization](#1-tổng-quan-về-authentication-và-authorization)
    - [Authentication là gì?](#authentication-là-gì)
    - [Authorization là gì?](#authorization-là-gì)
    - [Lợi ích của Authentication và Authorization](#lợi-ích-của-authentication-và-authorization)
2. [Các loại Authentication trong C# .NET](#2-các-loại-authentication-trong-c-net)
    - [Cookie Authentication](#cookie-authentication)
    - [JWT Authentication](#jwt-authentication)
    - [OAuth2 Authentication](#oauth2-authentication)
    - [OpenID Connect Authentication](#openid-connect-authentication)
3. [Cấu hình và sử dụng Authentication trong ASP.NET Core](#3-cấu-hình-và-sử-dụng-authentication-trong-aspnet-core)
    - [Cấu hình Cookie Authentication](#cấu-hình-cookie-authentication)
    - [Cấu hình JWT Authentication](#cấu-hình-jwt-authentication)
    - [Cấu hình OAuth2 Authentication](#cấu-hình-oauth2-authentication)
    - [Cấu hình OpenID Connect Authentication](#cấu-hình-openid-connect-authentication)
4. [Sử dụng Authorization trong ASP.NET Core](#4-sử-dụng-authorization-trong-aspnet-core)
    - [Cấu hình Authorization Policy](#cấu-hình-authorization-policy)
    - [Role-Based Authorization](#role-based-authorization)
    - [Claims-Based Authorization](#claims-based-authorization)
5. [Bảo mật và hiệu suất trong Authentication và Authorization](#5-bảo-mật-và-hiệu-suất-trong-authentication-và-authorization)
6. [Công cụ hỗ trợ trong môi trường Production](#6-công-cụ-hỗ-trợ-trong-môi-trường-production)
7. [Quy trình giao tiếp giữa Client và Server trong Authentication và cách lưu trữ](#7-quy-trình-giao-tiếp-giữa-client-và-server-trong-authentication-và-cách-lưu-trữ)
8. [Kết luận](#kết-luận)

---

### 1. Tổng quan về Authentication và Authorization

#### Authentication là gì?

Authentication (xác thực) là quá trình xác minh danh tính người dùng. Mục tiêu của Authentication là xác định xem người
dùng là ai, thông qua các phương thức như tên người dùng/mật khẩu, mã token, hoặc thông qua xác thực bên thứ ba (Google,
Facebook, v.v.).

#### Authorization là gì?

Authorization (ủy quyền) là quá trình kiểm tra quyền truy cập của người dùng đã được xác thực. Sau khi người dùng được
xác thực, hệ thống sẽ xác định xem họ có quyền truy cập vào các tài nguyên hoặc thực hiện các hành động nhất định hay
không.

#### Lợi ích của Authentication và Authorization

- **Bảo mật**: Đảm bảo rằng chỉ những người dùng được phép mới có thể truy cập vào tài nguyên bảo mật.
- **Quản lý quyền truy cập**: Giúp quản lý và phân quyền cho các nhóm người dùng khác nhau (quản trị viên, người dùng
  thường, v.v.).
- **Dễ dàng tích hợp**: Cung cấp khả năng tích hợp với các dịch vụ xác thực và ủy quyền bên ngoài (OAuth, OpenID
  Connect, v.v.).

### 2. Các loại Authentication trong C# .NET

#### Cookie Authentication

Cookie Authentication sử dụng cookie HTTP để lưu trữ thông tin xác thực. Thông tin này thường chứa một mã thông báo
phiên làm việc, giúp hệ thống nhận diện người dùng trong các lần truy cập sau.

- **Ưu điểm**: Dễ triển khai và sử dụng, không cần phải gửi thông tin xác thực trong mỗi yêu cầu.
- **Nhược điểm**: Cookie có thể bị tấn công nếu không bảo vệ đúng cách (ví dụ: thông qua CSRF hoặc XSS).

#### JWT Authentication

JSON Web Tokens (JWT) là một tiêu chuẩn mở để truyền tải thông tin xác thực dưới dạng JSON. JWT thường được sử dụng
trong các ứng dụng API hoặc ứng dụng phân tán, nơi người dùng được xác thực qua token thay vì cookie.

- **Ưu điểm**: Không cần lưu trữ trạng thái, dễ dàng sử dụng trong các ứng dụng phân tán hoặc mobile.
- **Nhược điểm**: Nếu không được bảo vệ, token có thể bị tấn công hoặc đánh cắp.

#### OAuth2 Authentication

OAuth2 là một giao thức ủy quyền phổ biến cho phép các ứng dụng truy cập tài nguyên của người dùng trên các dịch vụ bên
ngoài (như Google, Facebook) mà không cần phải biết thông tin đăng nhập của người dùng. OAuth2 phân tách rõ ràng giữa
xác thực (Authentication) và ủy quyền (Authorization).

- **Ưu điểm**: An toàn, bảo mật, có thể sử dụng với các dịch vụ bên ngoài.
- **Nhược điểm**: Cấu hình phức tạp và cần có các máy chủ ủy quyền.

#### OpenID Connect Authentication

OpenID Connect (OIDC) là một lớp mở rộng của OAuth2, bổ sung thêm khả năng xác thực người dùng. OIDC cho phép ứng dụng
xác thực người dùng thông qua các dịch vụ bên ngoài như Google, Microsoft, v.v.

- **Ưu điểm**: Được sử dụng phổ biến cho các ứng dụng web và mobile, hỗ trợ xác thực người dùng qua các nhà cung cấp
  dịch vụ.
- **Nhược điểm**: Cần cấu hình máy chủ ủy quyền và phụ thuộc vào các dịch vụ bên ngoài.

### 3. Cấu hình và sử dụng Authentication trong ASP.NET Core

#### Cấu hình Cookie Authentication

Để sử dụng Cookie Authentication trong ASP.NET Core, ta cần cấu hình dịch vụ trong `Startup.cs`:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddAuthentication(CookieAuthenticationDefaults.AuthenticationScheme)
            .AddCookie(options =>
            {
                options.LoginPath = "/Account/Login"; // Địa chỉ trang đăng nhập
                options.LogoutPath = "/Account/Logout"; // Địa chỉ trang đăng xuất
            });
}
```

#### Cấu hình JWT Authentication

Để sử dụng JWT Authentication trong ASP.NET Core, ta cần cấu hình dịch vụ JWT Bearer Authentication trong `Startup.cs`:

1. **Cài đặt package JWT**:

   ```bash
   dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer
   ```

2. **Cấu hình JWT Bearer Authentication**:

   ```csharp
   public void ConfigureServices(IServiceCollection services)
   {
       services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
               .AddJwtBearer(options =>
               {
                   options.RequireHttpsMetadata = false;
                   options.TokenValidationParameters = new TokenValidationParameters
                   {
                       ValidateIssuer = true,
                       ValidateAudience = true,
                       ValidateLifetime = true,
                       ValidIssuer = "YourIssuer",
                       ValidAudience = "YourAudience",
                       IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes("YourSecretKey"))
                   };
               });
   }
   ```

#### Cấu hình OAuth2 Authentication

Để cấu hình OAuth2 Authentication trong ASP.NET Core, ta có thể sử dụng một dịch vụ bên ngoài như Google, Facebook, v.v.
Ví dụ cấu hình Google OAuth2:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddAuthentication(options =>
    {
        options.DefaultScheme = CookieAuthenticationDefaults.AuthenticationScheme;
        options.DefaultChallengeScheme = GoogleDefaults.AuthenticationScheme;
    })
    .AddCookie()
    .AddGoogle(options =>
    {
        options.ClientId = "your-client-id";
        options.ClientSecret = "your-client-secret";
    });
}
```

#### Cấu hình OpenID Connect Authentication

Để cấu hình OpenID Connect trong ASP.NET Core, ta có thể sử dụng dịch vụ như Microsoft Identity:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddAuthentication(options =>
    {
        options.DefaultScheme = CookieAuthenticationDefaults.AuthenticationScheme;
        options.DefaultChallengeScheme = OpenIdConnectDefaults.AuthenticationScheme;
    })
    .AddCookie()
    .AddOpenIdConnect(options =>
    {
        options.Authority = "https://your-identity-provider";
        options.ClientId = "your-client-id";
        options.ClientSecret = "your-client-secret";
        options.ResponseType = "code";
    });
}
```

### 4. Sử dụng Authorization trong ASP.NET Core

#### Cấu hình Authorization Policy

Authorization Policy trong ASP.NET Core cho phép bạn xác định các điều kiện quyền truy cập. Ví dụ, bạn có thể tạo một
policy yêu cầu người dùng phải có quyền admin:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddAuthorization(options =>
    {
        options.AddPolicy("AdminPolicy", policy =>
            policy.RequireRole("Admin"));
    });
}
```

#### Role-Based Authorization

Role-Based Authorization yêu cầu người dùng phải có một hoặc nhiều vai trò để truy cập vào các tài nguyên nhất định.

```csharp
[Authorize(Roles = "Admin")]
public IActionResult AdminDashboard()
{
    return View();
}
```

#### Claims-Based Authorization

Claims-Based Authorization cho phép kiểm tra quyền truy cập dựa trên các claim của người dùng (ví dụ: tên, email, quyền
truy cập đặc biệt).

```csharp
[Authorize(Policy = "AdminPolicy")]
public IActionResult AdminOnlyAction()
{
    return View();
}
```

### 5. Bảo mật và hiệu suất trong Authentication và Authorization

- **Bảo mật thông tin xác thực**: Luôn sử dụng HTTPS để bảo vệ thông tin xác thực, đặc biệt là trong các giao dịch mạng.
- **Bảo vệ chống lại tấn công CSRF**: Sử dụng token chống CSRF để bảo vệ ứng dụng khỏi các cuộc tấn công

.

- **Hiệu suất**: Sử dụng các token có thời gian sống ngắn để giảm thiểu nguy cơ tấn công, đồng thời tránh lưu trữ quá
  nhiều thông tin trong các cookie hoặc token.

### 6. Công cụ hỗ trợ trong môi trường Production

- **IdentityServer4**: Một framework mã nguồn mở cho việc xác thực và ủy quyền dựa trên OpenID Connect và OAuth2.
- **Azure AD B2C**: Cung cấp giải pháp xác thực người dùng dựa trên các dịch vụ đám mây.
- **Auth0**: Dịch vụ bên ngoài hỗ trợ xác thực người dùng và ủy quyền với các tính năng như bảo mật cao và dễ dàng tích
  hợp.

### 7. Quy trình giao tiếp giữa Client và Server trong Authentication và cách lưu trữ

Quy trình giao tiếp giữa **Client** và **Server** trong các cơ chế Authentication (Xác thực) như **Cookie Authentication
**, **JWT Authentication**, **OAuth2**, và **OpenID Connect** sẽ có sự khác biệt về cách thức trao đổi và lưu trữ thông
tin xác thực. Dưới đây là chi tiết về quy trình giao tiếp và cách thức lưu trữ cho từng cơ chế:

---

#### **1. Cookie Authentication**

##### Quy trình giao tiếp giữa Client và Server:

1. **Client gửi yêu cầu đăng nhập**:

    - Người dùng nhập thông tin đăng nhập (ví dụ: tên người dùng và mật khẩu) trên giao diện của client (trình duyệt
      hoặc ứng dụng).
    - Client gửi yêu cầu POST chứa thông tin đăng nhập đến server (thường là `/login` hoặc một API endpoint tương ứng).

2. **Server xác thực và trả về Cookie**:

    - Server kiểm tra thông tin đăng nhập, nếu hợp lệ, tạo một **cookie** chứa thông tin phiên (session) của người dùng
      và gửi cookie này trong **header HTTP response** dưới dạng `Set-Cookie`.
    - Cookie này có thể chứa một **session ID** hoặc một **JWT** mã hóa các thông tin người dùng (tùy vào cấu hình của
      server).

3. **Client lưu trữ Cookie**:

    - Trình duyệt (client) nhận cookie và lưu trữ nó trong bộ nhớ hoặc trên ổ đĩa (tùy thuộc vào thời gian sống của
      cookie).
    - Cookie sẽ được lưu trữ tự động trong trình duyệt với các thuộc tính như `HttpOnly`, `Secure`, và `SameSite` để bảo
      mật.

4. **Client gửi cookie trong các yêu cầu tiếp theo**:
    - Trong các yêu cầu tiếp theo, trình duyệt sẽ tự động gửi cookie chứa thông tin phiên qua header `Cookie`.
    - Server sẽ nhận cookie, giải mã hoặc kiểm tra session, xác thực người dùng và xử lý yêu cầu tiếp theo.

##### Lưu trữ:

- **Trình duyệt (Client)** lưu cookie vào bộ nhớ trong hoặc bộ nhớ đĩa của trình duyệt.
- Các cookie có thể có thời gian sống ngắn hạn hoặc dài hạn tùy vào thông số `Expires` hoặc `Max-Age` được thiết lập.

---

#### **2. JWT Authentication**

##### Quy trình giao tiếp giữa Client và Server:

1. **Client gửi yêu cầu đăng nhập**:

    - Client gửi yêu cầu POST chứa thông tin đăng nhập (ví dụ: tên người dùng và mật khẩu) đến server (thường là một API
      endpoint xác thực, ví dụ: `/auth/login`).

2. **Server xác thực và trả về JWT**:

    - Server xác minh thông tin người dùng và, nếu hợp lệ, tạo một **JSON Web Token (JWT)** chứa các thông tin xác
      thực (như user ID, quyền truy cập) và gửi lại trong **HTTP response**.

3. **Client lưu trữ JWT**:

    - Client nhận JWT và lưu trữ nó. Thông thường, JWT được lưu trữ trong:
        - **LocalStorage** hoặc **SessionStorage**: Phổ biến trong ứng dụng web JavaScript, tuy nhiên cần chú ý tới các
          nguy cơ bảo mật như tấn công XSS.
        - **Cookie**: JWT có thể được lưu trữ trong cookie với thuộc tính `HttpOnly` để bảo vệ khỏi các tấn công XSS.

4. **Client gửi JWT trong các yêu cầu tiếp theo**:
    - Trong các yêu cầu API tiếp theo, Client sẽ gửi JWT trong **header** của yêu cầu HTTP dưới dạng:
      ```http
      Authorization: Bearer <JWT>
      ```
    - Server sẽ giải mã JWT, kiểm tra tính hợp lệ của token (ví dụ: kiểm tra chữ ký, ngày hết hạn) và xác thực người
      dùng.

##### Lưu trữ:

- **LocalStorage** hoặc **SessionStorage**: Lưu trữ JWT trong trình duyệt. Tuy nhiên, không nên lưu trữ JWT trong *
  *localStorage** nếu có thể bị tấn công XSS.
- **Cookie**: Lưu JWT trong cookie với thuộc tính `HttpOnly` và `Secure` để ngăn ngừa tấn công XSS và CSRF.

---

#### **3. OAuth2 Authentication**

##### Quy trình giao tiếp giữa Client và Server:

1. **Client yêu cầu ủy quyền (authorization request)**:

    - Client (ví dụ: ứng dụng web hoặc di động) chuyển hướng người dùng đến server của nhà cung cấp OAuth2 (ví dụ:
      Google, Facebook) để người dùng ủy quyền cho ứng dụng truy cập vào tài nguyên của họ.
    - Quá trình này bao gồm yêu cầu từ client tới OAuth2 provider với các tham số như `client_id`, `redirect_uri`, và
      `response_type=code`.

2. **User cấp phép và Provider trả mã ủy quyền (Authorization Code)**:

    - Nếu người dùng đồng ý, OAuth2 provider sẽ chuyển hướng lại người dùng về **redirect URI** của client và cung cấp *
      *authorization code**.

3. **Client lấy Access Token**:

    - Client gửi yêu cầu POST đến OAuth2 provider để trao đổi **authorization code** lấy **access token** và **refresh
      token**.
    - Thông tin này sẽ được trả về dưới dạng JSON, ví dụ:
      ```json
      {
        "access_token": "access_token_value",
        "expires_in": 3600,
        "refresh_token": "refresh_token_value"
      }
      ```

4. **Client gửi Access Token trong các yêu cầu tiếp theo**:
    - Client sử dụng **access token** để gửi yêu cầu truy cập tài nguyên từ server của OAuth2 provider.
    - Access token sẽ được gửi trong header của HTTP request dưới dạng:
      ```http
      Authorization: Bearer <access_token>
      ```

##### Lưu trữ:

- **Client (ứng dụng web, mobile)** lưu trữ access token trong **localStorage**, **sessionStorage**, hoặc **cookie**.
- **Refresh Token** (nếu có) thường được lưu trữ an toàn trong **secure cookie** hoặc **server-side session** vì nó cần
  phải được bảo vệ kỹ càng để tránh bị đánh cắp.

---

#### **4. OpenID Connect Authentication**

##### Quy trình giao tiếp giữa Client và Server:

1. **Client gửi yêu cầu đăng nhập**:

    - Giống như OAuth2, client sẽ chuyển hướng người dùng đến OpenID Connect provider (ví dụ: Google, Microsoft) để đăng
      nhập và xác thực.

2. **User xác thực và Provider trả về Authorization Code**:

    - Sau khi người dùng đăng nhập thành công, OpenID Connect provider sẽ trả về **authorization code** cho client.

3. **Client trao đổi Authorization Code lấy Access Token và ID Token**:

    - Client gửi yêu cầu POST để trao đổi authorization code lấy **ID Token** (xác thực người dùng) và **Access Token
      ** (truy cập tài nguyên).

4. **Client sử dụng Access Token và ID Token**:
    - **Access Token** sẽ được dùng để truy cập tài nguyên từ OpenID Connect provider.
    - **ID Token** sẽ được sử dụng để xác thực người dùng (thường là một JWT).

##### Lưu trữ:

- **ID Token và Access Token** có thể được lưu trữ trong **localStorage**, **sessionStorage**, hoặc **cookie**.
- Để bảo mật, **ID Token** và **Access Token** nên được lưu trong **secure cookie** với `HttpOnly` flag để giảm nguy cơ
  bị tấn công XSS.

---

#### **Tóm lại quy trình giao tiếp và lưu trữ Authentication**:

- **Cookie Authentication**: Server gửi cookie xác thực trong header `Set-Cookie`, và client tự động gửi lại cookie
  trong các yêu cầu tiếp theo.
- **JWT Authentication**: Server trả JWT, client lưu trữ trong **localStorage**, **sessionStorage** hoặc **cookie**, và
  gửi JWT trong header `Authorization: Bearer <JWT>` trong các yêu cầu tiếp theo.
- **OAuth2 Authentication**: Client yêu cầu mã ủy quyền, nhận token từ OAuth2 provider, và sử dụng Access Token trong
  các yêu cầu truy cập tài nguyên.
- **OpenID Connect**: Quy trình tương tự OAuth2, nhưng bao gồm cả ID Token để xác thực người dùng.

Trong mọi trường hợp, việc lưu trữ và bảo mật token hoặc cookie rất quan trọng để bảo vệ ứng dụng khỏi các tấn công như
**XSS** và **CSRF**.

### 8. Kết luận

Authentication và Authorization là hai thành phần quan trọng trong bảo mật ứng dụng web. ASP.NET Core cung cấp các giải
pháp linh hoạt để cấu hình và triển khai xác thực và ủy quyền với các phương thức như Cookie, JWT, OAuth2 và OpenID
Connect. Việc bảo mật và tối ưu hóa hiệu suất là điều quan trọng khi triển khai các phương pháp này để đảm bảo sự an
toàn và hiệu quả cho hệ thống.
