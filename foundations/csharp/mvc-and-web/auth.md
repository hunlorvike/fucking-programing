## **🚀 "GIẢI MÃ" AUTHENTICATION VÀ AUTHORIZATION: BẢO MẬT ỨNG DỤNG WEB CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai khái niệm cực kỳ quan trọng trong bảo mật ứng dụng
web: Authentication (Xác thực) và Authorization (Ủy quyền). Nghe có vẻ "hóc búa" nhưng thực ra rất gần gũi và cần thiết
cho dân code chúng mình đấy. Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình
dung nhé! Let's go!

### **I. AUTHENTICATION VÀ AUTHORIZATION LÀ GÌ? (NHƯ "CHỨNG MINH THƯ" VÀ "VÉ VÀO CỬA")**

* **Authentication (Xác thực):** Là quá trình *xác minh danh tính* người dùng (kiểm tra xem bạn là ai).
* **Authorization (Ủy quyền):** Là quá trình *kiểm tra quyền truy cập* của người dùng (kiểm tra xem bạn được làm gì).
* **Tóm lại:**
    * **Authentication:** "Chứng minh thư" - xác nhận bạn là ai.
    * **Authorization:** "Vé vào cửa" - xác nhận bạn được làm gì.

### **II. CÁC LOẠI AUTHENTICATION PHỔ BIẾN (CÁC "CÁCH" XÁC MINH)**

1. **Cookie Authentication:** Dùng cookie để lưu thông tin phiên, giúp server nhận ra người dùng ở các lần truy cập sau.
    * **Ưu:** Dễ dùng, không cần gửi thông tin xác thực mỗi lần.
    * **Nhược:** Cookie có thể bị tấn công (CSRF, XSS), cần bảo vệ cẩn thận.
2. **JWT (JSON Web Token) Authentication:** Dùng token để xác thực, thường dùng cho API, ứng dụng phân tán.
    * **Ưu:** Không cần lưu trạng thái, dễ dùng trong mobile/app.
    * **Nhược:** Token có thể bị đánh cắp nếu không bảo vệ.
3. **OAuth2 Authentication:** Cho phép ứng dụng truy cập tài nguyên của người dùng trên các dịch vụ khác (Google,
   Facebook) mà không cần mật khẩu.
    * **Ưu:** An toàn, tiện lợi, dùng với các dịch vụ bên ngoài.
    * **Nhược:** Cấu hình phức tạp, cần có server ủy quyền.
4. **OpenID Connect Authentication:** Mở rộng từ OAuth2, thêm khả năng xác thực người dùng.
    * **Ưu:** Phổ biến, dùng cho web/mobile, xác thực qua các nhà cung cấp.
    * **Nhược:** Cần có server ủy quyền.

### **III. CẤU HÌNH AUTHENTICATION TRONG ASP.NET CORE (CÁCH "CÀI ĐẶT" XÁC THỰC)**

#### **1. Cookie Authentication:**

```csharp
    using Microsoft.AspNetCore.Authentication.Cookies;

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

#### **2. JWT Authentication:**

```csharp
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.IdentityModel.Tokens;
using System.Text;

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

#### **3. OAuth2 Authentication (Google):**

```csharp
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authentication.Google;

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

#### **4. OpenID Connect (Microsoft Identity):**

```csharp
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authentication.OpenIdConnect;

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

### **IV. AUTHORIZATION TRONG ASP.NET CORE (CÁCH "CẤP QUYỀN")**

#### **1. Authorization Policy:**

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

#### **2. Role-Based Authorization:**

```csharp
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

[Authorize(Roles = "Admin")]
public class AdminController : ControllerBase
{
    [HttpGet]
    public IActionResult AdminDashboard()
    {
        return Ok("Welcome to Admin dashboard");
    }
}
```

#### **3. Claims-Based Authorization:**

```csharp
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

[Authorize(Policy = "AdminPolicy")]
public class AdminOnlyController : ControllerBase
{
    [HttpGet]
    public IActionResult AdminOnlyAction()
    {
        return Ok("Welcome to Admin Area");
    }
}
```

### **V. BẢO MẬT VÀ HIỆU SUẤT (KHÔNG CHỈ BẢO VỆ, MÀ CÒN CHẠY NHANH)**

* **HTTPS:** Bắt buộc dùng HTTPS để bảo vệ thông tin xác thực.
* **CSRF:** Dùng token chống CSRF.
* **Token ngắn hạn:** Dùng token có thời gian sống ngắn để giảm rủi ro.
* **Lưu trữ:** Tránh lưu quá nhiều thông tin trong cookie/token.

### **VI. CÔNG CỤ HỖ TRỢ (NHỮNG "TRỢ THỦ" ĐẮC LỰC)**

* **IdentityServer4:** Framework cho xác thực/ủy quyền dựa trên OAuth2/OpenID Connect.
* **Azure AD B2C:** Dịch vụ xác thực người dùng trên đám mây.
* **Auth0:** Dịch vụ xác thực bên ngoài (có nhiều tính năng bảo mật).

### **VII. GIAO TIẾP CLIENT - SERVER VÀ LƯU TRỮ (CÁCH "NÓI CHUYỆN" VÀ LƯU THÔNG TIN)**

1. **Cookie:**
    * Server gửi cookie cho client (trong header `Set-Cookie`).
    * Client tự động gửi cookie trong các request sau (header `Cookie`).
    * Lưu trong bộ nhớ hoặc file của trình duyệt.
2. **JWT:**
    * Server trả JWT.
    * Client lưu JWT (trong localStorage, sessionStorage, hoặc cookie).
    * Client gửi JWT trong header: `Authorization: Bearer <JWT>`.
3. **OAuth2:**
    * Client xin code ủy quyền (authorization code).
    * Client dùng code ủy quyền lấy token.
    * Client dùng access token để truy cập tài nguyên.
    * Lưu token trong localStorage, sessionStorage hoặc cookie.
4. **OpenID Connect:**
    * Giống OAuth2, nhưng có thêm ID Token để xác thực người dùng.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Authentication và Authorization là hai khái niệm rất quan trọng trong bảo mật web. Hy vọng qua bài viết này, các bạn đã
hiểu rõ hơn về chúng và có thể áp dụng vào các ứng dụng của mình. Chúc các bạn code thành công và luôn bảo mật! 😎
