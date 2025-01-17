# **Tài Liệu Chi Tiết về Globalization & Localization trong .NET**

**Globalization (Toàn cầu hóa)** và **Localization (Địa phương hóa)** trong .NET là hai quy trình quan trọng để xây dựng
ứng dụng đa ngôn ngữ và hỗ trợ nhiều khu vực khác nhau. .NET cung cấp các công cụ mạnh mẽ giúp bạn triển khai cả hai quy
trình này dễ dàng và hiệu quả.

---

## **Mục Lục**

1. [Globalization & Localization là gì?](#1-globalization--localization-là-gì)
2. [Cách Triển Khai Globalization trong .NET](#2-cách-triển-khai-globalization-trong-net)
    - 2.1 [Cấu hình định dạng văn hóa](#21-cấu-hình-định-dạng-văn-hóa)
    - 2.2 [Hỗ trợ Unicode](#22-hỗ-trợ-unicode)
3. [Cách Triển Khai Localization trong .NET](#3-cách-triển-khai-localization-trong-net)
    - 3.1 [Sử dụng tài nguyên `resx`](#31-sử-dụng-tài-nguyên-resx)
    - 3.2 [Dịch văn bản động](#32-dịch-văn-bản-động)
4. [Triển Khai Localization với Razor Pages/MVC](#4-triển-khai-localization-với-razor-pagesmvc)
5. [Tích Hợp với Các Công Cụ Thứ Ba](#5-tích-hợp-với-các-công-cụ-thứ-ba)
6. [Các Tình Huống Sử Dụng Thực Tế](#6-các-tình-huống-sử-dụng-thực-tế)
7. [Tổng Kết](#7-tổng-kết)

---

### **1. Globalization & Localization là gì?**

#### **Globalization (Toàn cầu hóa):**

Globalization là quá trình thiết kế ứng dụng sao cho nó có thể dễ dàng thích nghi với các ngôn ngữ và khu vực khác nhau.
Điều này bao gồm việc hỗ trợ:

- Định dạng ngày giờ.
- Đơn vị tiền tệ.
- Múi giờ.
- Định dạng số và ký tự.

#### **Localization (Địa phương hóa):**

Localization là quá trình tùy chỉnh ứng dụng để phù hợp với một ngôn ngữ hoặc khu vực cụ thể, bao gồm:

- Dịch văn bản giao diện.
- Thay đổi hình ảnh, biểu tượng phù hợp với văn hóa.
- Tuân thủ các quy định địa phương.

---

### **2. Cách Triển Khai Globalization trong .NET**

#### **2.1 Cấu hình định dạng văn hóa**

.NET hỗ trợ cấu hình định dạng văn hóa (Culture) thông qua lớp `CultureInfo` trong namespace `System.Globalization`.

**Cấu hình văn hóa mặc định:**

```csharp
using System.Globalization;
using Microsoft.AspNetCore.Builder;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Cấu hình văn hóa mặc định
var defaultCulture = new CultureInfo("en-US");
CultureInfo.DefaultThreadCurrentCulture = defaultCulture;
CultureInfo.DefaultThreadCurrentUICulture = defaultCulture;

app.Run();
```

**Thay đổi văn hóa theo yêu cầu:**
Bạn có thể thay đổi văn hóa dựa trên request của người dùng bằng middleware:

```csharp
using Microsoft.AspNetCore.Localization;

var supportedCultures = new[] { "en-US", "fr-FR", "vi-VN" };
var localizationOptions = new RequestLocalizationOptions
{
    SupportedCultures = supportedCultures.Select(c => new CultureInfo(c)).ToList(),
    SupportedUICultures = supportedCultures.Select(c => new CultureInfo(c)).ToList(),
    DefaultRequestCulture = new RequestCulture("en-US")
};

app.UseRequestLocalization(localizationOptions);
```

---

#### **2.2 Hỗ trợ Unicode**

Để đảm bảo ứng dụng có thể xử lý đa ngôn ngữ, bạn nên sử dụng mã hóa Unicode (UTF-8).

**Ví dụ cấu hình trong `Program.cs`:**

```csharp
builder.Services.Configure<IISServerOptions>(options =>
{
    options.AutomaticAuthentication = false;
});
builder.Services.Configure<Microsoft.AspNetCore.Server.Kestrel.Core.KestrelServerOptions>(options =>
{
    options.AllowSynchronousIO = true;
});
```

---

### **3. Cách Triển Khai Localization trong .NET**

#### **3.1 Sử dụng tài nguyên `resx`**

.NET hỗ trợ sử dụng các tệp tài nguyên `.resx` để lưu trữ chuỗi được dịch.

**Tạo file tài nguyên:**

1. Tạo một file `Resources.resx` (mặc định) trong thư mục `Resources`.
2. Tạo các file như `Resources.en-US.resx`, `Resources.fr-FR.resx` để chứa bản dịch cho từng ngôn ngữ.

**Sử dụng tài nguyên trong code:**

```csharp
using System.Globalization;
using System.Resources;

var resourceManager = new ResourceManager("YourNamespace.Resources", typeof(Program).Assembly);
Console.WriteLine(resourceManager.GetString("HelloWorld", new CultureInfo("fr-FR")));
```

---

#### **3.2 Dịch văn bản động**

.NET hỗ trợ tiêm `IStringLocalizer` để dịch văn bản động trong ứng dụng.

**Cấu hình dịch vụ `IStringLocalizer`:**

```csharp
builder.Services.AddLocalization(options => options.ResourcesPath = "Resources");

app.UseRequestLocalization(localizationOptions);
```

**Sử dụng trong controller hoặc service:**

```csharp
using Microsoft.Extensions.Localization;

public class HomeController : Controller
{
    private readonly IStringLocalizer<HomeController> _localizer;

    public HomeController(IStringLocalizer<HomeController> localizer)
    {
        _localizer = localizer;
    }

    public IActionResult Index()
    {
        var message = _localizer["WelcomeMessage"];
        return View((object)message);
    }
}
```

---

### **4. Triển Khai Localization với Razor Pages/MVC**

Trong Razor Pages hoặc MVC, bạn có thể dễ dàng tích hợp Localization để dịch giao diện.

**Sử dụng `IViewLocalizer` trong Razor View:**

```html
@inject Microsoft.AspNetCore.Mvc.Localization.IViewLocalizer Localizer

<h1>@Localizer["WelcomeMessage"]</h1>
```

**Tạo file tài nguyên cho View:**

- Tạo file `Views.Shared._Layout.resx` để dịch nội dung trong layout.
- Tạo file `Views.Home.Index.resx` để dịch nội dung của từng trang cụ thể.

---

### **5. Tích Hợp với Các Công Cụ Thứ Ba**

Bạn có thể sử dụng các công cụ quản lý dịch thuật như:

- **Lokalise**.
- **Crowdin**.
- **Google Translate API**.

Các công cụ này giúp bạn dễ dàng quản lý và cập nhật bản dịch mà không cần chỉnh sửa trực tiếp mã nguồn.

---

### **6. Các Tình Huống Sử Dụng Thực Tế**

1. **Website đa ngôn ngữ:**
    - Tạo giao diện người dùng với nhiều ngôn ngữ như tiếng Anh, tiếng Việt, tiếng Nhật.
2. **Ứng dụng thương mại điện tử:**
    - Hiển thị giá tiền, định dạng ngày tháng theo khu vực.
3. **Ứng dụng doanh nghiệp:**
    - Tích hợp hỗ trợ các định dạng văn hóa khác nhau trong báo cáo và tài liệu.
4. **Ứng dụng di động:**
    - Cung cấp nội dung bằng ngôn ngữ phù hợp dựa trên vị trí người dùng.

---

### **7. Tổng Kết**

**Globalization và Localization** trong .NET là những công cụ mạnh mẽ để xây dựng ứng dụng hỗ trợ đa ngôn ngữ và đa khu
vực. Khi được triển khai đúng cách, chúng giúp ứng dụng tiếp cận nhiều đối tượng người dùng hơn, cải thiện trải nghiệm
người dùng và tăng tính cạnh tranh trên thị trường quốc tế.
