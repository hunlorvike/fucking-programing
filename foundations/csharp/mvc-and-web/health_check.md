# **Tài Liệu Chi Tiết về Health Checks trong .NET**

**Health Checks** trong .NET là một tính năng tích hợp mạnh mẽ, cho phép bạn giám sát và kiểm tra trạng thái hoạt động
của ứng dụng và các thành phần phụ thuộc. Tính năng này rất hữu ích trong việc duy trì hiệu suất, độ tin cậy, và khắc
phục sự cố của hệ thống.

---

## **Mục Lục**

1. [Health Checks là gì?](#1-health-checks-là-gì)
2. [Cách Tích Hợp Health Checks](#2-cách-tích-hợp-health-checks)
    - 2.1 [Cấu hình cơ bản](#21-cấu-hình-cơ-bản)
    - 2.2 [Kiểm tra các thành phần phụ thuộc](#22-kiểm-tra-các-thành-phần-phụ-thuộc)
3. [Health Check UI](#3-health-check-ui)
4. [Tích Hợp Health Checks với Kubernetes](#4-tích-hợp-health-checks-với-kubernetes)
5. [Các Tình Huống Sử Dụng Thực Tế](#5-các-tình-huống-sử-dụng-thực-tế)
6. [Tổng Kết](#6-tổng-kết)

---

### **1. Health Checks là gì?**

**Health Checks** là cơ chế để xác định trạng thái hiện tại của ứng dụng và các dịch vụ phụ thuộc (như cơ sở dữ liệu,
API bên ngoài, bộ nhớ đệm, v.v.).

Các trạng thái phổ biến:

- **Healthy**: Ứng dụng hoặc thành phần phụ thuộc đang hoạt động bình thường.
- **Unhealthy**: Có sự cố trong ứng dụng hoặc thành phần phụ thuộc.
- **Degraded**: Hệ thống vẫn hoạt động nhưng không đạt hiệu suất tối ưu.

---

### **2. Cách Tích Hợp Health Checks**

#### **2.1 Cấu hình cơ bản**

**Bước 1: Thêm Health Checks vào `Program.cs`:**

Trong .NET, bạn có thể cấu hình Health Checks bằng cách sử dụng phương thức `AddHealthChecks`.

**Ví dụ:**

```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;

var builder = WebApplication.CreateBuilder(args);

// Thêm dịch vụ Health Checks
builder.Services.AddHealthChecks();

var app = builder.Build();

// Map endpoint cho Health Checks
app.MapHealthChecks("/health");

app.Run();
```

**Kết quả:** Truy cập `http://localhost:5000/health` để xem trạng thái Health Check cơ bản.

---

#### **2.2 Kiểm tra các thành phần phụ thuộc**

Bạn có thể thêm các Health Check cho các thành phần cụ thể như cơ sở dữ liệu, Redis, hoặc API bên ngoài.

**Ví dụ kiểm tra kết nối cơ sở dữ liệu:**

```csharp
using Microsoft.Extensions.Diagnostics.HealthChecks;

builder.Services.AddHealthChecks()
    .AddSqlServer(
        connectionString: "Server=localhost;Database=TestDB;User Id=sa;Password=your_password;",
        name: "SQL Server",
        failureStatus: HealthStatus.Unhealthy,
        tags: new[] { "db", "sql" });
```

**Ví dụ kiểm tra Redis:**

```csharp
builder.Services.AddHealthChecks()
    .AddRedis(
        connectionString: "localhost:6379",
        name: "Redis Cache",
        failureStatus: HealthStatus.Unhealthy);
```

**Ví dụ kiểm tra một API bên ngoài:**

```csharp
builder.Services.AddHealthChecks()
    .AddUrlGroup(
        new Uri("https://api.example.com/health"),
        name: "External API",
        failureStatus: HealthStatus.Degraded);
```

**Kết hợp các Health Checks:**

```csharp
builder.Services.AddHealthChecks()
    .AddSqlServer("Server=localhost;Database=TestDB;User Id=sa;Password=your_password;", name: "Database")
    .AddRedis("localhost:6379", name: "Redis")
    .AddUrlGroup(new Uri("https://api.example.com/health"), name: "External API");
```

---

### **3. Health Check UI**

**Health Check UI** cung cấp một giao diện trực quan để giám sát trạng thái của hệ thống.

#### **Cách tích hợp Health Check UI:**

**Bước 1: Cài đặt package:**

```bash
dotnet add package AspNetCore.HealthChecks.UI
```

**Bước 2: Cấu hình Health Check UI:**

```csharp
builder.Services.AddHealthChecksUI(options =>
{
    options.AddHealthCheckEndpoint("Basic Health Check", "/health");
}).AddInMemoryStorage();
```

**Bước 3: Map endpoint cho UI:**

```csharp
app.MapHealthChecksUI();
```

Truy cập **`http://localhost:5000/healthchecks-ui`** để xem giao diện UI.

---

### **4. Tích Hợp Health Checks với Kubernetes**

Health Checks trong .NET rất phù hợp để tích hợp với Kubernetes thông qua các probe:

- **Liveness Probe:** Kiểm tra xem ứng dụng có đang chạy hay không.
- **Readiness Probe:** Kiểm tra xem ứng dụng đã sẵn sàng xử lý request hay chưa.

#### **Ví dụ cấu hình Kubernetes:**

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 80
  initialDelaySeconds: 5
  periodSeconds: 10

readinessProbe:
  httpGet:
    path: /health
    port: 80
  initialDelaySeconds: 5
  periodSeconds: 10
```

---

### **5. Các Tình Huống Sử Dụng Thực Tế**

1. **Giám sát cơ sở dữ liệu:**
    - Kiểm tra trạng thái kết nối tới SQL Server hoặc MongoDB.
2. **Kiểm tra hệ thống cache:**
    - Đảm bảo Redis hoặc Memcached đang hoạt động.
3. **Giám sát API bên ngoài:**
    - Xác minh rằng các dịch vụ bên ngoài mà hệ thống phụ thuộc vẫn hoạt động.
4. **Giám sát microservices:**
    - Tích hợp Health Checks vào từng microservice để theo dõi trạng thái toàn bộ hệ thống.
5. **Tích hợp DevOps:**
    - Sử dụng Health Checks với Kubernetes hoặc các hệ thống CI/CD để tự động giám sát và triển khai.

---

### **6. Tổng Kết**

**Health Checks** là một công cụ mạnh mẽ trong .NET, giúp bạn giám sát trạng thái của ứng dụng và các dịch vụ phụ thuộc
một cách hiệu quả. Khi được tích hợp với các công cụ như **Health Check UI**, **Kubernetes**, hoặc **Prometheus**, nó
trở thành một phần không thể thiếu trong việc duy trì sự ổn định và hiệu suất của hệ thống.
