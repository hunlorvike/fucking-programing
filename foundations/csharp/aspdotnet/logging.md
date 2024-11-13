# Logging trong C# .NET

## Mục Lục

1. [Tổng quan về Logging](#1-tổng-quan-về-logging)
   - [Logging là gì?](#logging-là-gì)
   - [Các mức độ Logging](#các-mức-độ-logging)
   - [Logging hoạt động như thế nào?](#logging-hoạt-động-như-thế-nào)
2. [Cấu hình Logging trong C# .NET](#2-cấu-hình-logging-trong-c-net)
   - [Cấu hình Logging trong `appsettings.json`](#a-cấu-hình-logging-trong-appsettingsjson)
   - [Sử dụng Logging trong các dịch vụ](#b-sử-dụng-logging-trong-các-dịch-vụ)
3. [Logging Provider trong ASP.NET Core](#3-logging-provider-trong-aspnet-core)
   - [Console Logger](#console-logger)
   - [File Logger (3rd Party)](#file-logger-3rd-party)
   - [Debug Logger](#debug-logger)
   - [EventLog Logger](#eventlog-logger)
4. [Logging định dạng và cấu trúc](#4-logging-định-dạng-và-cấu-trúc)
5. [Logging hiệu suất và bảo mật](#5-logging-hiệu-suất-và-bảo-mật)
   - [Độ chi tiết và hiệu suất của Logging](#độ-chi-tiết-và-hiệu-suất-của-logging)
   - [Logging thông tin nhạy cảm](#logging-thông-tin-nhạy-cảm)
6. [Logging trong Môi trường Production](#6-logging-trong-môi-trường-production)
7. [Kết luận](#kết-luận)

---

### 1. Tổng quan về Logging

#### Logging là gì?

Logging là quá trình ghi lại các sự kiện, trạng thái, và thông báo từ ứng dụng vào các tệp log hoặc hệ thống giám sát, giúp các nhà phát triển và quản trị hệ thống theo dõi, phân tích và khắc phục sự cố trong ứng dụng.

#### Các mức độ Logging

C# .NET hỗ trợ nhiều mức độ logging để phân loại độ quan trọng và độ chi tiết của thông tin log:

- **Trace**: Mức thấp nhất, log mọi thông tin chi tiết nhất trong ứng dụng.
- **Debug**: Thông tin chi tiết để kiểm tra và phát triển ứng dụng.
- **Information**: Các thông tin có ích về các sự kiện thông thường.
- **Warning**: Cảnh báo về các sự kiện bất thường nhưng chưa gây lỗi nghiêm trọng.
- **Error**: Thông báo về các lỗi không mong muốn xảy ra trong ứng dụng.
- **Critical**: Thông báo về các lỗi nghiêm trọng, ảnh hưởng đến sự hoạt động của hệ thống.

#### Logging hoạt động như thế nào?

1. Khi ứng dụng gặp sự kiện cần log, nó gọi phương thức log ở mức độ phù hợp (e.g., `LogInformation`, `LogError`).
2. Thông báo log được gửi đến các **Logging Providers** được cấu hình (e.g., Console, File, EventLog).
3. Logging Providers lưu trữ hoặc hiển thị log theo cấu hình (e.g., chỉ log từ mức `Warning` trở lên).

### 2. Cấu hình Logging trong C# .NET

#### a. Cấu hình Logging trong `appsettings.json`

ASP.NET Core hỗ trợ cấu hình logging trực tiếp trong file `appsettings.json` để dễ dàng tùy chỉnh. Ví dụ cấu hình cơ bản:

```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
    }
  }
}
```

Trong cấu hình này:

- **Default**: Thiết lập mức độ log mặc định cho toàn bộ ứng dụng.
- **Microsoft**: Giới hạn các log từ thư viện Microsoft ở mức `Warning` trở lên để giảm độ chi tiết.
- **Microsoft.Hosting.Lifetime**: Log thông tin về thời gian sống của ứng dụng (quá trình khởi động và tắt ứng dụng).

#### b. Sử dụng Logging trong các dịch vụ

ASP.NET Core sử dụng Dependency Injection để quản lý logging, cho phép bạn dễ dàng lấy đối tượng logger trong các dịch vụ của ứng dụng:

```csharp
public class SampleService
{
    private readonly ILogger<SampleService> _logger;

    public SampleService(ILogger<SampleService> logger)
    {
        _logger = logger;
    }

    public void Process()
    {
        _logger.LogInformation("Bắt đầu xử lý trong SampleService.");

        try
        {
            // Xử lý công việc
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Đã xảy ra lỗi trong quá trình xử lý.");
        }
    }
}
```

### 3. Logging Provider trong ASP.NET Core

ASP.NET Core cung cấp nhiều **Logging Providers** khác nhau để lưu trữ và hiển thị log.

#### Console Logger

Console Logger ghi log ra **console**, thường sử dụng cho việc phát triển và kiểm thử.

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddLogging(config =>
    {
        config.AddConsole(); // Kích hoạt Console Logger
    });
}
```

#### File Logger (3rd Party)

ASP.NET Core không có File Logger mặc định, nhưng có thể tích hợp thư viện **Serilog** để ghi log vào file:

```csharp
public class Program
{
    public static void Main(string[] args)
    {
        Log.Logger = new LoggerConfiguration()
            .WriteTo.File("logs/logfile.txt", rollingInterval: RollingInterval.Day)
            .CreateLogger();

        var host = CreateHostBuilder(args).Build();
        host.Run();
    }

    public static IHostBuilder CreateHostBuilder(string[] args) =>
        Host.CreateDefaultBuilder(args)
            .UseSerilog() // Sử dụng Serilog
            .ConfigureWebHostDefaults(webBuilder =>
            {
                webBuilder.UseStartup<Startup>();
            });
}
```

#### Debug Logger

Debug Logger ghi log vào **Debug Output Window** trong IDE, phù hợp để phát triển và kiểm thử.

```csharp
services.AddLogging(config =>
{
    config.AddDebug(); // Kích hoạt Debug Logger
});
```

#### EventLog Logger

EventLog Logger ghi log vào **Windows Event Log** (chỉ khả dụng trên Windows).

```csharp
services.AddLogging(config =>
{
    config.AddEventLog(eventLogSettings => {
        eventLogSettings.LogName = "Application";
        eventLogSettings.SourceName = "MyApp";
    });
});
```

### 4. Logging định dạng và cấu trúc

Để ghi các thông điệp log có định dạng rõ ràng và dễ hiểu, ASP.NET Core hỗ trợ các placeholders trong thông điệp log. Điều này giúp các hệ thống phân tích log xử lý tốt hơn.

```csharp
_logger.LogInformation("User {UserId} đã đăng nhập vào lúc {Time}", userId, DateTime.UtcNow);
```

Kết quả log mẫu sẽ là:

```
User 123 đã đăng nhập vào lúc 11/13/2024 02:30:00
```

### 5. Logging hiệu suất và bảo mật

#### Độ chi tiết và hiệu suất của Logging

- Sử dụng log ở mức **Debug** và **Trace** chỉ khi cần thiết vì chúng tạo ra nhiều thông tin chi tiết, ảnh hưởng đến hiệu suất.
- Hạn chế log ở mức cao như **Information**, **Warning** trong môi trường Production trừ khi có sự cố.

#### Logging thông tin nhạy cảm

- Tránh log các thông tin nhạy cảm như mật khẩu, mã xác thực, thông tin cá nhân.
- Mã hóa các log chứa thông tin nhạy cảm nếu cần thiết.

### 6. Logging trong Môi trường Production

Trong môi trường Production, chỉ nên ghi các log cần thiết (ví dụ: từ `Warning` trở lên) để tránh log quá nhiều và ảnh hưởng đến hiệu suất của ứng dụng. Có thể sử dụng các giải pháp quản lý log như **Application Insights**, **Seq**, **Splunk**, hoặc **Elasticsearch** để thu thập và phân tích log hiệu quả.

### Kết luận

Logging là một thành phần quan trọng trong việc giám sát và xử lý sự cố của ứng dụng. Trong C# .NET, có nhiều lựa chọn và cấu hình linh hoạt để ghi log, cho phép tích hợp với các hệ thống lưu trữ log khác nhau. Việc quản lý các mức độ log và bảo mật log là rất quan trọng để đảm bảo hiệu suất và an toàn của ứng dụng.
