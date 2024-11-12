# **Cấu Trúc Thư Mục của Dự Án ASP.NET Core**

## Mục Lục

1. [Giới thiệu về ASP.NET Core](#gioi-thieu-ve-asp-net-core)
2. [Cấu Trúc Thư Mục Chuẩn cho Dự Án ASP.NET Core](#cau-truc-thu-muc-chuan-cho-du-an-asp-net-core)
   - 2.1 [Thư mục Controllers](#thu-muc-controllers)
   - 2.2 [Thư mục Models](#thu-muc-models)
   - 2.3 [Thư mục Views](#thu-muc-views)
   - 2.4 [Thư mục wwwroot](#thu-muc-wwwroot)
   - 2.5 [Thư mục Services](#thu-muc-services)
   - 2.6 [Thư mục Data](#thu-muc-data)
   - 2.7 [Thư mục Properties](#thu-muc-properties)
3. [Các Tệp Cấu Hình Chính](#cac-tep-cau-hinh-chinh)
4. [Cấu Trúc trong ASP.NET Framework](#cau-truc-trong-asp-net-framework)
5. [Tổng Kết](#tong-ket)

## 1. Giới thiệu về ASP.NET Core <a name="gioi-thieu-ve-asp-net-core"></a>

**ASP.NET Core** là một nền tảng phát triển ứng dụng web đa nền tảng (cross-platform), mã nguồn mở của Microsoft. Nó hỗ trợ việc xây dựng các ứng dụng web hiện đại, API mạnh mẽ, và có thể triển khai dễ dàng trên các hệ điều hành Windows, Linux và macOS. Cấu trúc của một dự án ASP.NET Core thường bao gồm các thư mục và tệp theo chuẩn MVC (Model-View-Controller) hoặc Web API.

## 2. Cấu Trúc Thư Mục Chuẩn cho Dự Án ASP.NET Core <a name="cau-truc-thu-muc-chuan-cho-du-an-asp-net-core"></a>

Một dự án ASP.NET Core thường có cấu trúc thư mục cơ bản như sau:

```
MyAspNetApp/
│
├── Controllers/
├── Models/
├── Views/
├── wwwroot/
├── Services/
├── Data/
├── Properties/
├── appsettings.json
├── Program.cs
├── Startup.cs
└── MyAspNetApp.csproj
```

### 2.1 Thư mục Controllers <a name="thu-muc-controllers"></a>

- **Chứa các lớp Controller** trong mô hình MVC, chịu trách nhiệm xử lý các yêu cầu HTTP từ người dùng và trả về kết quả dưới dạng Views hoặc dữ liệu (thường là JSON cho Web API).
- **Ví dụ**:
  - `HomeController.cs`: Quản lý các yêu cầu liên quan đến giao diện chính.
  - `ProductController.cs`: Xử lý các yêu cầu liên quan đến sản phẩm trong ứng dụng.

```plaintext
├── Controllers/
│   ├── HomeController.cs
│   └── ProductController.cs
```

### 2.2 Thư mục Models <a name="thu-muc-models"></a>

- **Chứa các lớp Model** biểu diễn dữ liệu và logic nghiệp vụ.
- **Model** thường bao gồm các lớp đại diện cho cấu trúc dữ liệu của ứng dụng, kết nối với cơ sở dữ liệu thông qua **Entity Framework** hoặc các dịch vụ dữ liệu khác.
- **Ví dụ**:
  - `Product.cs`: Lớp biểu diễn thông tin sản phẩm.
  - `User.cs`: Lớp biểu diễn thông tin người dùng.

```plaintext
├── Models/
│   ├── Product.cs
│   └── User.cs
```

### 2.3 Thư mục Views (chỉ có trong dự án MVC) <a name="thu-muc-views"></a>

- **Chứa các tệp Razor Views (.cshtml)** dùng để hiển thị giao diện người dùng.
- **Views** được tổ chức theo từng Controller, và có thể sử dụng các tệp dùng chung (Shared) như layout.
- **Ví dụ**:
  - `Index.cshtml`: Giao diện trang chủ.
  - `_Layout.cshtml`: Template dùng chung cho các trang.

```plaintext
├── Views/
│   ├── Home/
│   │   ├── Index.cshtml
│   │   └── About.cshtml
│   └── Shared/
│       └── _Layout.cshtml
```

### 2.4 Thư mục wwwroot <a name="thu-muc-wwwroot"></a>

- **Thư mục chứa các tệp tĩnh** như CSS, JavaScript, hình ảnh mà người dùng có thể truy cập từ trình duyệt.
- **wwwroot** là thư mục gốc mà tất cả các tệp tĩnh sẽ được phục vụ từ đó.

```plaintext
├── wwwroot/
│   ├── css/
│   ├── js/
│   └── images/
```

### 2.5 Thư mục Services <a name="thu-muc-services"></a>

- **Chứa các lớp dịch vụ** cung cấp logic nghiệp vụ cho ứng dụng.
- **Services** giúp chia nhỏ các tác vụ xử lý cụ thể để tái sử dụng và dễ quản lý, ví dụ như xác thực, quản lý sản phẩm, hoặc kết nối dữ liệu.
- **Ví dụ**:
  - `ProductService.cs`: Xử lý các nghiệp vụ liên quan đến sản phẩm.
  - `UserService.cs`: Xử lý nghiệp vụ liên quan đến người dùng.

```plaintext
├── Services/
│   ├── ProductService.cs
│   └── UserService.cs
```

### 2.6 Thư mục Data <a name="thu-muc-data"></a>

- **Chứa các lớp liên quan đến cơ sở dữ liệu** như lớp `DbContext` trong Entity Framework Core và các migration cho cơ sở dữ liệu.
- **Data** thường bao gồm lớp `ApplicationDbContext` và các tệp dùng để khởi tạo dữ liệu.

```plaintext
├── Data/
│   ├── ApplicationDbContext.cs
│   └── SeedData.cs
```

### 2.7 Thư mục Properties <a name="thu-muc-properties"></a>

- Chứa các tệp cấu hình, bao gồm **launchSettings.json**, dùng để thiết lập môi trường chạy cho ứng dụng trong quá trình phát triển.

```plaintext
├── Properties/
│   └── launchSettings.json
```

## 3. Các Tệp Cấu Hình Chính <a name="cac-tep-cau-hinh-chinh"></a>

- **appsettings.json**: Chứa cấu hình chính của ứng dụng, bao gồm chuỗi kết nối cơ sở dữ liệu, cài đặt bảo mật, và các cấu hình tùy chỉnh khác.
- **Program.cs**: Điểm bắt đầu của ứng dụng, nơi thiết lập cấu hình cơ bản và chạy ứng dụng.
- **Startup.cs**: Chứa các cấu hình dịch vụ và middleware cho ứng dụng (trong các phiên bản ASP.NET Core 3.x trở xuống).

## 4. Cấu Trúc trong ASP.NET Framework <a name="cau-truc-trong-asp-net-framework"></a>

### Ví dụ cấu trúc thư mục của một dự án ASP.NET MVC (không phải Core):

```
MyAspNetApp/
├── Controllers/
├── Models/
├── Views/
│   ├── Home/
│   └── Shared/
├── Scripts/
├── Content/
├── App_Data/
├── Global.asax
├── Web.config
└── MyAspNetApp.csproj
```

- **Scripts**: Chứa các tệp JavaScript.
- **Content**: Chứa các tệp CSS và tài nguyên tĩnh khác.
- **App_Data**: Thư mục chứa các dữ liệu tạm thời hoặc cơ sở dữ liệu file (.mdf).
- **Global.asax**: Điểm khởi đầu của ứng dụng trong ASP.NET Framework.
- **Web.config**: Tệp cấu hình của ứng dụng.

## 5. Tổng Kết <a name="tong-ket"></a>

Cấu trúc thư mục của các dự án **ASP.NET** và **ASP.NET Core** giúp phân tách rõ ràng giữa các thành phần, hỗ trợ tổ chức mã nguồn hợp lý và tối ưu hóa quy trình phát triển. Việc hiểu và nắm vững cấu trúc thư mục giúp dễ dàng quản lý các thành phần ứng dụng như controller, model, view, các dịch vụ và cấu hình.
