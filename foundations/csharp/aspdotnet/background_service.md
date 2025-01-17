# Tìm Hiểu về `Background Service` trong .NET

`Background Service` trong .NET là một thành phần được sử dụng để thực thi các công việc chạy nền mà không ảnh hưởng đến luồng chính của ứng dụng. Các công việc này có thể bao gồm xử lý dữ liệu, gửi email, lập lịch tác vụ, hoặc xử lý hàng đợi.

Dưới đây là tài liệu chi tiết về `Background Service`, bao gồm các khái niệm, cách sử dụng, và ví dụ thực tiễn.

## Mục Lục

1. [Background Service là gì?](#1-background-service-là-gì)
2. [Phân Loại Background Service](#2-phân-loại-background-service)
   - 2.1 [IHostedService](#21-ihostedservice)
   - 2.2 [BackgroundService](#22-backgroundservice)
3. [Cách Tạo Background Service](#3-cách-tạo-background-service)
4. [Cách Đăng Ký Background Service](#4-cách-đăng-ký-background-service)
5. [Sử Dụng Hosted Service với Dependency Injection](#5-sử-dụng-hosted-service-với-dependency-injection)
6. [Quartz.NET cho Các Tác Vụ Định Kỳ](#6-quartznet-cho-các-tác-vụ-định-kỳ)
7. [Các Tình Huống Sử Dụng Thực Tế](#7-các-tình-huống-sử-dụng-thực-tế)
8. [Tổng Kết](#8-tổng-kết)

---

### 1. Background Service là gì?

`Background Service` là một cơ chế trong .NET được sử dụng để xử lý các tác vụ nền trong suốt vòng đời của ứng dụng. Những tác vụ này có thể chạy liên tục hoặc được lập lịch để thực hiện vào các thời điểm cụ thể.

---

### 2. Phân Loại Background Service

#### 2.1. **IHostedService**
`IHostedService` là giao diện cơ bản nhất để triển khai các công việc nền trong .NET. Nó định nghĩa hai phương thức chính:
- `StartAsync(CancellationToken)`: Được gọi khi dịch vụ khởi động.
- `StopAsync(CancellationToken)`: Được gọi khi dịch vụ dừng lại.

**Ví dụ**:
```csharp
using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;

public class MyHostedService : IHostedService
{
    public Task StartAsync(CancellationToken cancellationToken)
    {
        Console.WriteLine("Service is starting...");
        return Task.CompletedTask;
    }

    public Task StopAsync(CancellationToken cancellationToken)
    {
        Console.WriteLine("Service is stopping...");
        return Task.CompletedTask;
    }
}
```

#### 2.2. **BackgroundService**
`BackgroundService` là lớp cơ sở trừu tượng triển khai sẵn `IHostedService`. Bạn chỉ cần override phương thức `ExecuteAsync(CancellationToken)` để thực hiện logic xử lý nền.

**Ví dụ**:
```csharp
using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;

public class MyBackgroundService : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            Console.WriteLine("Background task is running...");
            await Task.Delay(1000, stoppingToken);
        }
    }
}
```

---

### 3. Cách Tạo Background Service

Dưới đây là quy trình chi tiết để tạo một `Background Service`:

#### Bước 1: Tạo lớp kế thừa `BackgroundService`
```csharp
using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;

public class LoggingService : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            Console.WriteLine($"Logging at {DateTime.Now}");
            await Task.Delay(5000, stoppingToken); // Log mỗi 5 giây
        }
    }
}
```

---

### 4. Cách Đăng Ký Background Service

Background Service cần được đăng ký vào Dependency Injection container để .NET quản lý.

**Cách đăng ký trong `Program.cs`:**
```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

// Đăng ký Background Service
builder.Services.AddHostedService<LoggingService>();

var app = builder.Build();
app.Run();
```

---

### 5. Sử Dụng Hosted Service với Dependency Injection

Bạn có thể sử dụng **Dependency Injection (DI)** để inject các dịch vụ cần thiết vào Background Service.

**Ví dụ**:
```csharp
using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

public class MyBackgroundService : BackgroundService
{
    private readonly ILogger<MyBackgroundService> _logger;

    public MyBackgroundService(ILogger<MyBackgroundService> logger)
    {
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            _logger.LogInformation("Background service is running...");
            await Task.Delay(2000, stoppingToken);
        }
    }
}
```

---

### 6. Quartz.NET cho Các Tác Vụ Định Kỳ

Nếu bạn cần lập lịch các tác vụ định kỳ, hãy sử dụng **Quartz.NET**.

**Cài đặt:**
```bash
Install-Package Quartz
Install-Package Quartz.Extensions.Hosting
```

**Triển khai Job với Quartz.NET:**
```csharp
using Quartz;
using System;
using System.Threading.Tasks;

public class SampleJob : IJob
{
    public Task Execute(IJobExecutionContext context)
    {
        Console.WriteLine($"Sample job executed at {DateTime.Now}");
        return Task.CompletedTask;
    }
}
```

**Đăng ký Quartz.NET trong `Program.cs`:**
```csharp
builder.Services.AddQuartz(q =>
{
    q.UseMicrosoftDependencyInjectionJobFactory();

    q.AddJob<SampleJob>(opts => opts.WithIdentity("SampleJob"));
    q.AddTrigger(opts => opts
        .ForJob("SampleJob")
        .WithIdentity("SampleJobTrigger")
        .WithCronSchedule("0/5 * * * * ?")); // Mỗi 5 giây
});

builder.Services.AddQuartzHostedService(q => q.WaitForJobsToComplete = true);
```

---

### 7. Các Tình Huống Sử Dụng Thực Tế

1. **Xử lý hàng đợi email:**
   - Lấy email từ hàng đợi và gửi chúng định kỳ.
2. **Đồng bộ hóa dữ liệu với API bên thứ ba:**
   - Lấy dữ liệu từ API và cập nhật cơ sở dữ liệu mỗi giờ.
3. **Lập lịch báo cáo:**
   - Tạo và gửi báo cáo hàng ngày hoặc hàng tuần.
4. **Dọn dẹp dữ liệu cũ:**
   - Xóa các bản ghi không còn cần thiết trong cơ sở dữ liệu.

---

### 8. Tổng Kết

`Background Service` là một công cụ mạnh mẽ trong .NET, giúp xử lý các công việc nền một cách hiệu quả. Với sự kết hợp của `Hosted Service` và các thư viện như **Quartz.NET**, bạn có thể dễ dàng triển khai các tác vụ nền phức tạp và định kỳ trong ứng dụng của mình.