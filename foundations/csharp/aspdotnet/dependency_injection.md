# Dependency Injection trong .NET: Tổng Quan và Hướng Dẫn

## Mục Lục

1. [Khái niệm về Dependency Injection](#khái-niệm-về-dependency-injection)
2. [Tại sao cần Dependency Injection?](#tại-sao-cần-dependency-injection)
3. [Các phương thức Dependency Injection](#các-phương-thức-dependency-injection)
    - [3.1. Constructor Injection](#31-constructor-injection)
    - [3.2. Property Injection](#32-property-injection)
    - [3.3. Method Injection](#33-method-injection)
4. [Cấu hình Dependency Injection trong ASP.NET Core](#cấu-hình-dependency-injection-trong-aspnet-core)
    - [4.1. Đăng ký dịch vụ](#41-đăng-ký-dịch-vụ)
    - [4.2. Sử dụng dịch vụ](#42-sử-dụng-dịch-vụ)
5. [Quản lý vòng đời của dịch vụ](#quản-lý-vòng-đời-của-dịch-vụ)
    - [5.1. Singleton](#51-singleton)
    - [5.2. Scoped](#52-scoped)
    - [5.3. Transient](#53-transient)
6. [Kiểm thử với Dependency Injection](#kiểm-thử-với-dependency-injection)
7. [Mẫu thực hành tốt nhất với Dependency Injection](#mẫu-thực-hành-tốt-nhất-với-dependency-injection)
8. [Tóm tắt](#tóm-tắt)

---

## 1. Khái niệm về Dependency Injection

**Dependency Injection (DI)** là một mẫu thiết kế quan trọng trong lập trình, cho phép tách biệt các lớp và đối tượng,
từ đó quản lý các phụ thuộc một cách hiệu quả hơn. DI thực hiện nguyên tắc **Inversion of Control (IoC)**, trong đó việc
khởi tạo và quản lý các đối tượng không nằm trong các lớp sử dụng chúng. Thay vào đó, các đối tượng này được "tiêm" vào
lớp cần sử dụng, giúp tăng tính linh hoạt và khả năng bảo trì của ứng dụng.

## 2. Tại sao cần Dependency Injection?

Sử dụng DI mang lại nhiều lợi ích cho phát triển ứng dụng:

- **Giảm kết nối chặt chẽ (Tight Coupling)**: Mã nguồn dễ bảo trì và mở rộng hơn khi các lớp không phụ thuộc trực tiếp
  vào nhau.
- **Dễ dàng kiểm thử (Testability)**: Cho phép thay thế các dependencies bằng các mock hoặc stub, giúp kiểm thử đơn vị
  trở nên dễ dàng hơn.
- **Quản lý vòng đời (Lifecycle Management)**: DI Container giúp kiểm soát và tái sử dụng các đối tượng một cách dễ
  dàng.

## 3. Các phương thức Dependency Injection

Trong .NET, có ba phương pháp chính để thực hiện DI:

1. **Constructor Injection**: Dependency được truyền qua constructor của lớp.
2. **Property Injection**: Dependency được gán qua các thuộc tính.
3. **Method Injection**: Dependency được truyền vào một phương thức cụ thể.

### 3.1. Constructor Injection

Đây là phương pháp phổ biến nhất và được khuyến khích. Dependency được truyền qua constructor, đảm bảo rằng đối tượng
không thể tồn tại nếu không có các phụ thuộc cần thiết.

**Ví dụ**:

```csharp
public interface ILogger
{
    void Log(string message);
}

public class ConsoleLogger : ILogger
{
    public void Log(string message) => Console.WriteLine(message);
}

public class MyService
{
    private readonly ILogger _logger;

    public MyService(ILogger logger) => _logger = logger ?? throw new ArgumentNullException(nameof(logger));

    public void Execute() => _logger.Log("Executing MyService...");
}
```

### 3.2. Property Injection

Phương pháp này cho phép gán dependencies qua các thuộc tính, thường được sử dụng khi dependency không cần thiết ngay
lập tức.

**Ví dụ**:

```csharp
public class MyService
{
    public ILogger Logger { get; set; }

    public void Execute() => Logger?.Log("Executing MyService...");
}
```

### 3.3. Method Injection

Phương pháp này cho phép truyền dependency vào một phương thức cụ thể.

**Ví dụ**:

```csharp
public class MyService
{
    public void Execute(ILogger logger) => logger.Log("Executing MyService...");
}
```

## 4. Cấu hình Dependency Injection trong ASP.NET Core

ASP.NET Core cung cấp DI container tích hợp, cho phép đăng ký dịch vụ trong phương thức `ConfigureServices` trong file
`Startup.cs`.

### 4.1. Đăng ký dịch vụ

Bạn có thể đăng ký các dịch vụ với ba phương thức chính:

- **AddSingleton**: Tạo một thể hiện duy nhất cho toàn bộ ứng dụng.
- **AddScoped**: Tạo một thể hiện mới cho mỗi yêu cầu HTTP.
- **AddTransient**: Tạo một thể hiện mới mỗi khi dịch vụ được yêu cầu.

**Ví dụ**:

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddSingleton<ILogger, ConsoleLogger>(); // Singleton
    services.AddScoped<MyService>(); // Scoped
    services.AddTransient<AnotherService>(); // Transient
}
```

### 4.2. Sử dụng dịch vụ

Để sử dụng các dịch vụ đã đăng ký, bạn tiêm chúng vào constructor của lớp (thường là controller hoặc service).

**Ví dụ**:

```csharp
public class MyController : ControllerBase
{
    private readonly MyService _myService;

    public MyController(MyService myService) => _myService = myService;

    public IActionResult Get()
    {
        _myService.Execute();
        return Ok();
    }
}
```

## 5. Quản lý vòng đời của dịch vụ

Trong DI của .NET, có ba cách chính để quản lý vòng đời dịch vụ: **Singleton**, **Scoped**, và **Transient**.

### 5.1. Singleton

- **Định nghĩa**: Khởi tạo một lần duy nhất trong toàn bộ ứng dụng.
- **Tình huống sử dụng**: Chia sẻ trạng thái toàn cục, như cấu hình hoặc logging.
- **Ưu điểm**: Giảm chi phí tạo đối tượng.
- **Nhược điểm**: Có thể dẫn đến vấn đề đồng bộ hóa.

**Đăng ký**:

```csharp
services.AddSingleton<IMyService, MyService>();
```

### 5.2. Scoped

- **Định nghĩa**: Tạo mới cho mỗi yêu cầu HTTP.
- **Tình huống sử dụng**: Lưu trữ trạng thái giữa các phương thức trong cùng một yêu cầu.
- **Ưu điểm**: Tránh các vấn đề về trạng thái toàn cục.
- **Nhược điểm**: Không chia sẻ trạng thái giữa các yêu cầu khác nhau.

**Đăng ký**:

```csharp
services.AddScoped<IMyService, MyService>();
```

### 5.3. Transient

- **Định nghĩa**: Tạo mới mỗi khi dịch vụ được yêu cầu.
- **Tình huống sử dụng**: Các dịch vụ nhẹ không cần trạng thái.
- **Ưu điểm**: Quản lý các đối tượng ngắn hạn dễ dàng.
- **Nhược điểm**: Chi phí tạo đối tượng mới có thể ảnh hưởng đến hiệu suất.

**Đăng ký**:

```csharp
services.AddTransient<IMyService, MyService>();
```

## 6. Kiểm thử với Dependency Injection

DI giúp đơn giản hóa việc kiểm thử bằng cách cho phép bạn thay thế các dependency bằng các mock hoặc stub.

**Ví dụ với xUnit và Moq**:

```csharp
public class MyServiceTests
{
    [Fact]
    public void Execute_ShouldLogMessage()
    {
        var mockLogger = new Mock<ILogger>();
        var service = new MyService(mockLogger.Object);

        service.Execute();

        mockLogger.Verify(logger => logger.Log("Executing MyService..."), Times.Once);
    }
}
```

## 7. Mẫu thực hành tốt nhất với Dependency Injection

- **Tránh sử dụng Service Locator**: Giảm việc gọi DI container trong các lớp để giữ tính tách biệt.
- **Sử dụng Interface**: Đăng ký interfaces thay vì các lớp cụ thể để dễ dàng thay thế trong tương lai.
- **Giữ cho DI container gọn gàng**: Chỉ đăng ký các dịch vụ cần thiết, tránh những dịch vụ không sử dụng.

## 8. Tóm tắt

Dependency Injection trong .NET là công cụ mạnh mẽ giúp tách biệt các phần của ứng dụng, cải thiện khả năng kiểm thử, và
giảm độ phức tạp trong việc quản lý các đối tượng. Sử dụng DI giúp xây dựng ứng dụng dễ bảo trì, mở rộng và kiểm thử,
nâng cao chất lượng tổng thể của mã nguồn.
