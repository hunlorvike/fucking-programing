# Configuration Management

**Configuration Management** là tập hợp các kỹ thuật được sử dụng để quản lý và xử lý các cấu hình ứng dụng một cách
hiệu quả. Việc tổ chức cấu hình hợp lý giúp ứng dụng dễ dàng thích nghi với các môi trường khác nhau như **Development
**, **Staging**, và **Production**, đồng thời tăng tính linh hoạt và bảo mật. Trong bài viết này, chúng ta sẽ tìm hiểu
các kỹ thuật phổ biến như **Sử dụng JSON**, **XML**, và **Secrets Manager** trong .NET.

---

## **1. Giới Thiệu**

**Configuration Management** là quá trình quản lý các thiết lập và thông tin cấu hình của ứng dụng để:

- **Dễ dàng triển khai** trên nhiều môi trường.
- **Tăng tính bảo mật** bằng cách quản lý các thông tin nhạy cảm (như API Keys, chuỗi kết nối).
- **Giảm thiểu lỗi cấu hình** nhờ tổ chức cấu hình rõ ràng và tách biệt.

Trong .NET, bạn có thể sử dụng các công cụ và phương pháp như:

- **Tệp cấu hình dạng JSON hoặc XML**.
- **Secrets Manager** để bảo vệ thông tin nhạy cảm.
- **Hỗ trợ cấu hình môi trường linh hoạt** thông qua các tệp riêng biệt.

---

## **2. Sử Dụng JSON để Quản Lý Cấu Hình**

### **2.1 JSON là gì?**

- JSON (JavaScript Object Notation) là định dạng phổ biến để lưu trữ cấu hình nhờ tính dễ đọc và dễ mở rộng.
- Trong .NET, tệp `appsettings.json` là tệp chính để quản lý cấu hình.

### **2.2 Cách Cấu Hình JSON**

.NET cho phép tổ chức cấu hình theo từng môi trường bằng cách sử dụng các tệp riêng biệt, ví dụ:

- **appsettings.json**: Tệp cấu hình chung.
- **appsettings.Development.json**: Cấu hình dành riêng cho môi trường phát triển.
- **appsettings.Production.json**: Cấu hình dành riêng cho môi trường sản xuất.

**Ví dụ:**

```json
// appsettings.json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information"
    }
  },
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=MyApp;User Id=dev_user;Password=dev_pass;"
  }
}

// appsettings.Production.json
{
  "Logging": {
    "LogLevel": {
      "Default": "Error"
    }
  },
  "ConnectionStrings": {
    "DefaultConnection": "Server=prod-server;Database=MyApp;User Id=prod_user;Password=prod_pass;"
  }
}
```

### **2.3 Tích Hợp JSON Vào Ứng Dụng**

```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Configuration
    .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
    .AddJsonFile($"appsettings.{builder.Environment.EnvironmentName}.json", optional: true, reloadOnChange: true)
    .AddEnvironmentVariables(); // Đọc thêm cấu hình từ biến môi trường

var app = builder.Build();
```

### **2.4 Ưu Điểm và Nhược Điểm**

- **Ưu Điểm:**
    - Dễ đọc, dễ viết, và dễ quản lý.
    - Hỗ trợ tự động tải cấu hình theo môi trường.
- **Nhược Điểm:**
    - Không phù hợp để lưu trữ thông tin nhạy cảm như mật khẩu hoặc khóa API.

---

## **3. Secrets Manager**

### **3.1 Secrets Manager là gì?**

**Secrets Manager** trong .NET là một công cụ để quản lý các thông tin nhạy cảm như:

- Chuỗi kết nối cơ sở dữ liệu.
- Khóa API hoặc mã thông báo.

### **3.2 Cách Sử Dụng Secrets Manager**

1. **Kích Hoạt Secrets Manager**:

   ```bash
   dotnet user-secrets init
   ```

2. **Thêm Secrets**:

   ```bash
   dotnet user-secrets set "ConnectionStrings:DefaultConnection" "Server=secure-server;Database=SecureDB;User Id=secure_user;Password=secure_pass;"
   ```

3. **Đăng Ký Secrets Manager Trong Ứng Dụng**:

   ```csharp
   builder.Configuration.AddUserSecrets<Program>();
   ```

4. **Sử Dụng Secrets Trong Mã Nguồn**:
   ```csharp
   var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
   ```

### **3.3 Ưu Điểm và Nhược Điểm**

- **Ưu Điểm:**
    - Bảo vệ thông tin nhạy cảm không bị lưu trong mã nguồn.
    - Hỗ trợ quản lý secrets cục bộ theo từng developer.
- **Nhược Điểm:**
    - Chỉ hoạt động tốt trong môi trường phát triển. Với môi trường sản xuất, cần tích hợp các công cụ khác như **Azure
      Key Vault**.

---

## **4. Sử Dụng XML để Quản Lý Cấu Hình**

### **4.1 XML là gì?**

- XML (Extensible Markup Language) là một định dạng cấu hình được sử dụng phổ biến trong các ứng dụng .NET Framework cũ
  hoặc khi cần lưu trữ dữ liệu cấu hình phức tạp.

### **4.2 Ví Dụ Cấu Hình XML**

```xml
<configuration>
  <appSettings>
    <add key="ApplicationName" value="MyApp" />
    <add key="Environment" value="Production" />
  </appSettings>
</configuration>
```

### **4.3 Tích Hợp XML Vào Ứng Dụng**

```csharp
builder.Configuration.AddXmlFile("config.xml", optional: true, reloadOnChange: true);
```

### **4.4 Ưu Điểm và Nhược Điểm**

- **Ưu Điểm:**
    - Phù hợp với các cấu hình phức tạp, có tính phân cấp.
- **Nhược Điểm:**
    - Dài dòng, khó đọc hơn so với JSON.
    - Không còn phổ biến trong các dự án hiện đại.

---

## **5. Kết Hợp Nhiều Nguồn Cấu Hình**

.NET cho phép bạn kết hợp nhiều nguồn cấu hình (JSON, XML, Secrets Manager, Biến Môi Trường, v.v.). Cấu hình sau sẽ ghi
đè cấu hình trước nếu có xung đột.

**Ví dụ:**

```csharp
builder.Configuration
    .AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)
    .AddJsonFile($"appsettings.{builder.Environment.EnvironmentName}.json", optional: true, reloadOnChange: true)
    .AddXmlFile("config.xml", optional: true, reloadOnChange: true)
    .AddUserSecrets<Program>() // Secrets Manager
    .AddEnvironmentVariables(); // Biến môi trường
```

---

## **6. Các Tình Huống Sử Dụng Thực Tế**

1. **JSON Configuration**:
    - Quản lý cấu hình chung cho ứng dụng web hoặc API.
    - Tự động thay đổi cấu hình theo môi trường.
2. **Secrets Manager**:
    - Bảo vệ các thông tin nhạy cảm trong quá trình phát triển.
3. **XML Configuration**:
    - Tích hợp với các hệ thống cũ hoặc khi cần cấu hình phức tạp.
4. **Kết hợp nhiều nguồn cấu hình**:
    - Phù hợp cho các ứng dụng lớn, cần khả năng mở rộng và quản lý cấu hình phức tạp.

---

## **7. Tổng Kết**

**Configuration Management** là một phần không thể thiếu trong việc xây dựng các ứng dụng hiện đại. Với .NET, việc sử
dụng các công cụ như JSON, XML, và Secrets Manager giúp bạn:

- Tăng tính linh hoạt trong quản lý cấu hình.
- Bảo vệ thông tin nhạy cảm.
- Dễ dàng triển khai ứng dụng trên nhiều môi trường.

Việc áp dụng hiệu quả **Configuration Management** sẽ giúp ứng dụng của bạn vận hành ổn định và dễ bảo trì hơn trong dài
hạn.
