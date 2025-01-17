# Configuration Management trong C# .NET

## Mục Lục

1. [Tổng quan về Configuration Management](#1-tổng-quan-về-configuration-management)
    - [Configuration Management là gì?](#configuration-management-là-gì)
    - [Tầm quan trọng của Configuration Management](#tầm-quan-trọng-của-configuration-management)
2. [Các thành phần cấu hình trong ASP.NET Core](#2-các-thành-phần-cấu-hình-trong-aspnet-core)
    - [File `appsettings.json`](#file-appsettingsjson)
    - [Environment Variables](#environment-variables)
    - [User Secrets](#user-secrets)
    - [Command-line Arguments](#command-line-arguments)
3. [Cấu hình và Quản lý môi trường trong ASP.NET Core](#3-cấu-hình-và-quản-lý-môi-trường-trong-aspnet-core)
    - [Thiết lập môi trường](#thiết-lập-môi-trường)
    - [Đọc cấu hình theo môi trường](#đọc-cấu-hình-theo-môi-trường)
4. [Sử dụng Configuration trong ASP.NET Core](#4-sử-dụng-configuration-trong-aspnet-core)
5. [Quản lý cấu hình nhạy cảm và bảo mật](#5-quản-lý-cấu-hình-nhạy-cảm-và-bảo-mật)
    - [Bảo mật cấu hình nhạy cảm](#bảo-mật-cấu-hình-nhạy-cảm)
    - [Sử dụng Azure Key Vault và các giải pháp bảo mật khác](#sử-dụng-azure-key-vault-và-các-giải-pháp-bảo-mật-khác)
6. [Kết luận](#kết-luận)

---

### 1. Tổng quan về Configuration Management

#### Configuration Management là gì?

Configuration Management (Quản lý Cấu hình) là quá trình lưu trữ, quản lý và áp dụng các cấu hình quan trọng của ứng
dụng. Cấu hình này có thể bao gồm các tham số kết nối cơ sở dữ liệu, khóa API, và các thiết lập về môi trường. Điều này
giúp ứng dụng dễ dàng thay đổi hành vi và thông số hoạt động mà không cần sửa đổi mã nguồn.

#### Tầm quan trọng của Configuration Management

- **Dễ dàng tùy chỉnh**: Giúp dễ dàng thay đổi cấu hình theo môi trường (dev, test, production) mà không cần thay đổi
  mã.
- **Bảo mật thông tin nhạy cảm**: Quản lý thông tin nhạy cảm như mật khẩu, khóa API bằng các giải pháp bảo mật.
- **Tăng khả năng kiểm soát và theo dõi**: Cho phép quản lý các thay đổi cấu hình hiệu quả, hỗ trợ gỡ lỗi và khôi phục
  nhanh chóng khi cần.

### 2. Các thành phần cấu hình trong ASP.NET Core

ASP.NET Core cung cấp các thành phần để quản lý cấu hình như file JSON, biến môi trường, và các thông số dòng lệnh, giúp
linh hoạt hóa việc cấu hình ứng dụng.

#### File `appsettings.json`

File `appsettings.json` là nơi lưu trữ các thiết lập cấu hình mặc định của ứng dụng, như chuỗi kết nối cơ sở dữ liệu,
các giá trị cấu hình dịch vụ, và các tùy chọn khác. Khi ứng dụng khởi động, ASP.NET Core sẽ tự động đọc file này và tải
các giá trị vào hệ thống cấu hình.

Ví dụ cấu trúc `appsettings.json`:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=myServer;Database=myDb;User=myUser;Password=myPass;"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Warning"
    }
  },
  "AppSettings": {
    "FeatureToggle": true,
    "MaxItems": 100
  }
}
```

#### Environment Variables

Biến môi trường (Environment Variables) là một cách linh hoạt và bảo mật để cấu hình các tham số đặc biệt khi triển khai
ứng dụng. Chúng có thể được thiết lập từ hệ điều hành hoặc qua các công cụ CI/CD, hữu ích cho cấu hình khác nhau theo
môi trường.

#### User Secrets

User Secrets là công cụ bảo mật cho cấu hình nhạy cảm trong giai đoạn phát triển, không lưu trong source code. Các giá
trị nhạy cảm được lưu trong một file JSON cục bộ và chỉ có thể truy cập từ máy của nhà phát triển.

Thiết lập User Secrets cho một dự án ASP.NET Core:

```bash
dotnet user-secrets init
dotnet user-secrets set "ConnectionStrings:DefaultConnection" "YourSensitiveConnectionString"
```

#### Command-line Arguments

ASP.NET Core hỗ trợ truyền tham số từ dòng lệnh khi chạy ứng dụng, giúp ghi đè các cấu hình khi cần. Các tham số dòng
lệnh hữu ích trong việc kiểm soát hành vi ứng dụng mà không cần thay đổi file cấu hình.

Ví dụ:

```bash
dotnet run --Logging:LogLevel:Default Debug
```

### 3. Cấu hình và Quản lý môi trường trong ASP.NET Core

#### Thiết lập môi trường

ASP.NET Core hỗ trợ nhiều môi trường (Development, Staging, Production). Môi trường mặc định được thiết lập qua biến môi
trường `ASPNETCORE_ENVIRONMENT`.

Ví dụ, thiết lập môi trường cho ứng dụng:

```bash
export ASPNETCORE_ENVIRONMENT=Development
```

#### Đọc cấu hình theo môi trường

ASP.NET Core cho phép tạo file cấu hình riêng biệt theo môi trường, như `appsettings.Development.json` hoặc
`appsettings.Production.json`. Các file này sẽ ghi đè lên `appsettings.json` dựa trên giá trị của
`ASPNETCORE_ENVIRONMENT`.

Cấu trúc ví dụ:

- `appsettings.json`
- `appsettings.Development.json`
- `appsettings.Production.json`

```json
// appsettings.Development.json
{
  "Logging": {
    "LogLevel": {
      "Default": "Debug"
    }
  }
}
```

### 4. Sử dụng Configuration trong ASP.NET Core

ASP.NET Core sử dụng dependency injection (DI) để dễ dàng truy cập cấu hình. `IConfiguration` được sử dụng để đọc các
giá trị cấu hình từ file JSON, biến môi trường, hoặc các nguồn khác.

Ví dụ sử dụng `IConfiguration` trong một dịch vụ:

```csharp
public class SampleService
{
    private readonly IConfiguration _configuration;

    public SampleService(IConfiguration configuration)
    {
        _configuration = configuration;
    }

    public string GetConnectionString()
    {
        return _configuration.GetConnectionString("DefaultConnection");
    }

    public bool IsFeatureEnabled()
    {
        return _configuration.GetValue<bool>("AppSettings:FeatureToggle");
    }
}
```

### 5. Quản lý cấu hình nhạy cảm và bảo mật

#### Bảo mật cấu hình nhạy cảm

Các dữ liệu nhạy cảm như mật khẩu và khóa API không nên lưu trong `appsettings.json`. Thay vào đó, có thể sử dụng:

- **User Secrets**: Trong quá trình phát triển.
- **Environment Variables**: Khi triển khai trên máy chủ.
- **Azure Key Vault**: Đối với các ứng dụng chạy trên đám mây hoặc có yêu cầu bảo mật cao.

#### Sử dụng Azure Key Vault và các giải pháp bảo mật khác

Azure Key Vault cho phép lưu trữ các thông tin nhạy cảm như secret, certificate và các khóa mã hóa một cách bảo mật.
ASP.NET Core có thể tích hợp dễ dàng với Azure Key Vault bằng cách thêm Key Vault provider vào `IConfiguration`.

Ví dụ cấu hình Azure Key Vault:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    var azureServiceTokenProvider = new AzureServiceTokenProvider();
    var keyVaultClient = new KeyVaultClient(
        new KeyVaultClient.AuthenticationCallback(
            azureServiceTokenProvider.KeyVaultTokenCallback));

    builder.AddAzureKeyVault("https://<Your-Key-Vault-Name>.vault.azure.net/", keyVaultClient, new DefaultKeyVaultSecretManager());
}
```

### Kết luận

Quản lý cấu hình là một thành phần quan trọng trong việc đảm bảo hiệu quả, bảo mật và dễ dàng triển khai của ứng dụng.
Sử dụng cấu hình theo môi trường, bảo vệ dữ liệu nhạy cảm và linh hoạt trong việc cấu hình giúp ứng dụng ASP.NET Core
mạnh mẽ, an toàn và dễ bảo trì.
