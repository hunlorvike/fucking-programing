# Tìm Hiểu về `HttpContext` trong ASP.NET Core

`HttpContext` là một lớp trong ASP.NET Core cung cấp quyền truy cập vào thông tin về yêu cầu HTTP, phản hồi, người dùng,
cookies, và các thông tin về kết nối. Dưới đây là một số phương thức và thuộc tính quan trọng trong `HttpContext`, cùng
với mô tả và ví dụ sử dụng.

## Mục Lục

1. [HttpContext.Request](#1-httpcontextrequest)
2. [HttpContext.Response](#2-httpcontextresponse)
3. [HttpContext.User](#3-httpcontextuser)
4. [HttpContext.Session](#4-httpcontextsession)
5. [HttpContext.Connection](#5-httpcontextconnection)
6. [HttpContext.Items](#6-httpcontextitems)
7. [HttpContext.Features](#7-httpcontextfeatures)
8. [HttpContext.TraceIdentifier](#8-httpcontexttraceidentifier)
9. [HttpContext.Abort()](#9-httpcontextabort)
10. [Tổng Kết](#tổng-kết)

---

### 1. `HttpContext.Request`

`HttpContext.Request` chứa thông tin về yêu cầu HTTP hiện tại từ client.

- **Phương thức và Thuộc tính quan trọng**:

    - `Request.Path`: Đường dẫn của yêu cầu.
    - `Request.Query`: Tham số query trong URL.
    - `Request.Method`: Phương thức HTTP (GET, POST, PUT, DELETE).
    - `Request.Cookies`: Đọc cookie từ yêu cầu.
    - `Request.Headers`: Truy cập header của yêu cầu.
    - `Request.Body`: Nội dung của body yêu cầu, thường dùng để đọc dữ liệu trong POST, PUT.

- **Ví dụ**:

  ```csharp
  public IActionResult Example()
  {
      string path = HttpContext.Request.Path;
      string method = HttpContext.Request.Method;
      var query = HttpContext.Request.Query["param"];

      return Ok($"Path: {path}, Method: {method}, Query Param: {query}");
  }
  ```

---

### 2. `HttpContext.Response`

`HttpContext.Response` chứa các phương thức và thuộc tính để thiết lập phản hồi trả về cho client.

- **Phương thức và Thuộc tính quan trọng**:

    - `Response.StatusCode`: Thiết lập mã trạng thái HTTP của phản hồi.
    - `Response.Headers`: Thiết lập các header cho phản hồi.
    - `Response.Cookies`: Thiết lập cookie cho phản hồi.
    - `Response.Body`: Ghi nội dung phản hồi trực tiếp vào body.

- **Ví dụ**:

  ```csharp
  public IActionResult SetCookie()
  {
      HttpContext.Response.StatusCode = 200;
      HttpContext.Response.Cookies.Append("SampleCookie", "CookieValue", new CookieOptions
      {
          HttpOnly = true,
          Expires = DateTime.Now.AddHours(1)
      });

      return Ok("Cookie được đặt thành công.");
  }
  ```

---

### 3. `HttpContext.User`

Đại diện cho người dùng hiện tại. `HttpContext.User` cung cấp thông tin về danh tính người dùng thông qua các claims.

- **Phương thức và Thuộc tính quan trọng**:

    - `User.Identity.IsAuthenticated`: Kiểm tra xem người dùng đã xác thực hay chưa.
    - `User.Identity.Name`: Lấy tên người dùng đã xác thực.
    - `User.Claims`: Truy cập các claims liên quan đến người dùng.

- **Ví dụ**:

  ```csharp
  public IActionResult GetUserInfo()
  {
      if (HttpContext.User.Identity.IsAuthenticated)
      {
          var userName = HttpContext.User.Identity.Name;
          return Ok($"Tên người dùng: {userName}");
      }
      return Unauthorized("Người dùng chưa đăng nhập.");
  }
  ```

---

### 4. `HttpContext.Session`

`HttpContext.Session` là đối tượng cung cấp khả năng lưu trữ dữ liệu session giữa các yêu cầu của người dùng.

- **Phương thức và Thuộc tính quan trọng**:

    - `Session.SetString(string key, string value)`: Lưu trữ một chuỗi vào session.
    - `Session.GetString(string key)`: Lấy một chuỗi từ session.
    - `Session.SetInt32(string key, int value)`: Lưu trữ một số nguyên vào session.
    - `Session.GetInt32(string key)`: Lấy một số nguyên từ session.

- **Ví dụ**:

  ```csharp
  public IActionResult SetSessionData()
  {
      HttpContext.Session.SetString("Username", "AdminUser");
      return Ok("Session data set successfully.");
  }

  public IActionResult GetSessionData()
  {
      var username = HttpContext.Session.GetString("Username");
      return Ok($"Username in session: {username}");
  }
  ```

---

### 5. `HttpContext.Connection`

Cung cấp thông tin về kết nối của yêu cầu hiện tại.

- **Phương thức và Thuộc tính quan trọng**:

    - `Connection.RemoteIpAddress`: Địa chỉ IP của client gửi yêu cầu.
    - `Connection.LocalIpAddress`: Địa chỉ IP của server nhận yêu cầu.
    - `Connection.ClientCertificate`: Chứng chỉ của client (nếu có).

- **Ví dụ**:

  ```csharp
  public IActionResult GetClientIp()
  {
      var clientIp = HttpContext.Connection.RemoteIpAddress?.ToString();
      return Ok($"Client IP: {clientIp}");
  }
  ```

---

### 6. `HttpContext.Items`

`HttpContext.Items` là một từ điển có thể được sử dụng để lưu trữ dữ liệu tạm thời trong suốt vòng đời của yêu cầu hiện
tại. Dữ liệu trong `Items` chỉ có hiệu lực trong yêu cầu hiện tại và sẽ bị xóa sau khi phản hồi được gửi đi.

- **Ví dụ**:

  ```csharp
  public IActionResult SetItems()
  {
      HttpContext.Items["RequestID"] = Guid.NewGuid().ToString();
      return Ok("RequestID set in HttpContext.Items.");
  }

  public IActionResult GetItems()
  {
      var requestId = HttpContext.Items["RequestID"]?.ToString();
      return Ok($"Request ID: {requestId}");
  }
  ```

---

### 7. `HttpContext.Features`

`HttpContext.Features` cho phép truy cập đến các tính năng (features) của HTTP được thêm vào quá trình xử lý yêu cầu.
Các tính năng này có thể bao gồm `IHttpConnectionFeature`, `IHttpRequestFeature`, `IHttpResponseFeature`,… tùy thuộc vào
các dịch vụ HTTP đã đăng ký.

- **Ví dụ**:

  ```csharp
  public IActionResult GetHttpProtocol()
  {
      var requestFeature = HttpContext.Features.Get<IHttpRequestFeature>();
      return Ok($"HTTP Protocol: {requestFeature.Protocol}");
  }
  ```

---

### 8. `HttpContext.TraceIdentifier`

Một ID duy nhất được tạo ra cho mỗi yêu cầu, giúp theo dõi và ghi nhận các lỗi trong ứng dụng.

- **Ví dụ**:

  ```csharp
  public IActionResult GetTraceIdentifier()
  {
      var traceId = HttpContext.TraceIdentifier;
      return Ok($"Trace Identifier: {traceId}");
  }
  ```

---

### 9. `HttpContext.Abort()`

`Abort` dừng yêu cầu HTTP hiện tại và đóng kết nối. Phương thức này thường được sử dụng để ngắt kết nối khi có lỗi
nghiêm trọng hoặc yêu cầu không hợp lệ.

- **Ví dụ**:

  ```csharp
  public IActionResult TerminateRequest()
  {
      HttpContext.Abort();
      return StatusCode(500, "Request terminated.");
  }
  ```

---

### 10. Tổng Kết

`HttpContext` là một công cụ mạnh mẽ trong ASP.NET Core, cho phép quản lý thông tin và xử lý các yêu cầu và phản hồi
HTTP. Thông qua `HttpContext`, ta có thể truy cập các dữ liệu quan trọng về phiên làm việc của người dùng, kết nối HTTP,
lưu trữ session và cookies, cũng như các tính năng HTTP cụ thể của yêu cầu.
