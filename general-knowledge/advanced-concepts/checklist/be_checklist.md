# **Danh Sách Kiểm Tra Code Back-End (ASP.NET)**

## **Nó là gì? Tại sao quan trọng?**

**Danh sách kiểm tra Code Back-End (ASP.NET)** là công cụ giúp các nhà phát triển ASP.NET kiểm tra chất lượng mã nguồn,
bảo mật, hiệu suất, và khả năng mở rộng trong quá trình phát triển ứng dụng web. Danh sách này phù hợp với các dự án
ASP.NET Core và ASP.NET Framework, đảm bảo mã nguồn tuân thủ các tiêu chuẩn tốt nhất.

---

## **Back-End (ASP.NET)**

### **Bảo mật**

- [ ] Các API và endpoint đã được bảo vệ bằng **xác thực và phân quyền** (e.g., ASP.NET Identity, JWT, hoặc OAuth) chưa?
- [ ] Bạn có sử dụng các **middleware** để kiểm tra đầu vào của người dùng và phòng ngừa **SQL Injection**, **XSS**,
  hoặc các cuộc tấn công khác không?
- [ ] **AppSettings.json** có ẩn thông tin nhạy cảm (e.g., connection strings, API keys) không? Sử dụng **User Secrets**
  hoặc **Azure Key Vault** để quản lý chúng.
- [ ] Dữ liệu nhạy cảm có được mã hóa hoặc băm (e.g., mật khẩu bằng **ASP.NET Identity với BCrypt**) trước khi lưu trữ
  không?
- [ ] CORS có được cấu hình chính xác để kiểm soát nguồn gốc của yêu cầu không?
- [ ] Các API có sử dụng **rate limiting** (e.g., **AspNetCoreRateLimit**) để ngăn ngừa brute force không?
- [ ] Bạn đã kiểm tra và cập nhật các **NuGet package** để vá lỗ hổng bảo mật chưa?
- [ ] Có cơ chế bảo vệ chống lại **CSRF** không (e.g., `AntiForgeryToken` trong Razor Pages hoặc MVC)?
- [ ] JSON Web Token (JWT) có được triển khai với thời gian hết hạn và bảo vệ chống **JWT hijacking** (e.g., Refresh
  Token) không?
- [ ] Các thư mục và file nhạy cảm (e.g., wwwroot, logs) đã được bảo vệ bằng cấu hình **IIS hoặc Kestrel** chưa?

---

### **Hiệu suất**

- [ ] Bạn có sử dụng **Response Caching** hoặc **Distributed Caching** (e.g., Redis) cho dữ liệu thường xuyên được truy
  cập không?
- [ ] Các truy vấn cơ sở dữ liệu (e.g., Entity Framework Core) có được tối ưu hóa bằng **AsNoTracking**, **projection**,
  hoặc **caching** chưa?
- [ ] Có sử dụng **connection pooling** với cơ sở dữ liệu chưa?
- [ ] Ứng dụng có hỗ trợ **scale-out** (e.g., **Azure App Service Scale**, **Kubernetes**) không?
- [ ] Bạn đã bật **Response Compression Middleware** (e.g., Gzip hoặc Brotli) chưa?
- [ ] Có sử dụng **IAsyncEnumerable** hoặc **IQueryable** để tối ưu hóa xử lý dữ liệu lớn không?
- [ ] Các công việc dài hạn (e.g., gửi email, xử lý video) đã được chuyển sang **Background Services** hoặc **Queues** (
  e.g., Hangfire, Azure Queue) chưa?
- [ ] Bạn đã sử dụng công cụ như **Application Insights** hoặc **Serilog** để giám sát hiệu suất chưa?

---

## **Chất lượng mã nguồn**

- [ ] Mã nguồn có tuân thủ các tiêu chuẩn **Microsoft Coding Guidelines** không?
- [ ] Các controller/service có tuân thủ nguyên tắc **Single Responsibility Principle (SRP)** không?
- [ ] Bạn có tuân thủ nguyên tắc **DRY (Don't Repeat Yourself)** trong các service hoặc controller không?
- [ ] Tên phương thức và biến có rõ ràng, dễ hiểu không?
- [ ] Tất cả các log (`Console.WriteLine`, `Debug.WriteLine`) không cần thiết đã được loại bỏ chưa?
- [ ] Code có được tổ chức rõ ràng với các tầng riêng biệt (e.g., **Controllers**, **Services**, **Repositories**)
  không?
- [ ] Bạn có sử dụng **linters** (e.g., **SonarQube**, **StyleCop**, hoặc **Resharper**) để kiểm tra code chưa?
- [ ] Bạn đã xử lý các tình huống lỗi và các điều kiện biên trong toàn bộ ứng dụng chưa?
- [ ] Thông báo lỗi có cung cấp đủ thông tin để debug mà không tiết lộ dữ liệu nhạy cảm không?
- [ ] Ứng dụng có kiểm tra và xử lý **memory leaks** chưa (e.g., sử dụng đúng **IDisposable**, **using blocks**)?

---

## **Tài liệu**

- [ ] Tất cả các endpoint API đã được mô tả rõ ràng bằng **Swagger (Swashbuckle)** hoặc **NSwag** chưa?
- [ ] Bạn có viết tài liệu giải thích cấu trúc project và cách cấu hình không?
- [ ] Các đoạn code phức tạp có được chú thích đủ để giải thích logic không?
- [ ] Có hướng dẫn chi tiết về cách chạy ứng dụng (e.g., cài đặt môi trường, kết nối DB) không?
- [ ] Tài liệu có liệt kê các tình huống lỗi hoặc giới hạn của ứng dụng không?
- [ ] Bạn có liệt kê đầy đủ các **dependency** trong file `README` hoặc tương tự không?

---

## **Kiểm thử**

### **Kiểm thử chức năng**

- [ ] Các API có trả về đúng **status code** (e.g., 200, 400, 401, 404, 500) và thông báo không?
- [ ] Đầu vào từ người dùng có được xác thực đầy đủ bằng **Data Annotations** hoặc **Fluent Validation** không?
- [ ] Các tình huống lỗi đã được xử lý đúng cách chưa?
- [ ] Ứng dụng đã được kiểm thử trong các môi trường khác nhau (e.g., Development, Staging, Production) chưa?
- [ ] Bạn đã viết **unit test** và **integration test** với **xUnit**, **MSTest**, hoặc **NUnit** chưa?
- [ ] Độ bao phủ code (code coverage) có đạt mức mong muốn không (e.g., ≥80%)?

### **Kiểm thử hiệu suất**

- [ ] Bạn đã sử dụng các công cụ như **Apache JMeter**, **k6**, hoặc **Visual Studio Load Test** để kiểm tra tải chưa?
- [ ] Bạn đã kiểm tra hiệu suất hệ thống trong điều kiện stress cao chưa?
- [ ] Hệ thống có thể phục hồi nhanh chóng từ lỗi hiệu suất (e.g., database timeout) không?

### **Kiểm thử bảo mật**

- [ ] Bạn đã sử dụng các công cụ kiểm thử bảo mật (e.g., OWASP ZAP, Burp Suite) chưa?
- [ ] Bạn đã mô phỏng các cuộc tấn công (e.g., SQL Injection, XSS, Brute Force) để kiểm tra ứng dụng chưa?
- [ ] Dữ liệu nhạy cảm trong **logs** có được ẩn hoặc mã hóa trước khi lưu không?

---

## **Quản lý tài nguyên**

### **Cơ sở dữ liệu**

- [ ] Database có được thiết kế tối ưu (e.g., chuẩn hóa hoặc khử chuẩn hóa khi cần thiết) không?
- [ ] Các bảng cơ sở dữ liệu có sử dụng index phù hợp không?
- [ ] Các thao tác truy vấn có được kiểm tra hiệu suất và tối ưu hóa không?
- [ ] Dữ liệu có được sao lưu định kỳ và phục hồi (backup & restore) không?

### **Logging và giám sát**

- [ ] Bạn đã triển khai logging với công cụ như **Serilog**, **NLog**, hoặc **Application Insights** chưa?
- [ ] Logs có sử dụng định dạng chuẩn (e.g., JSON) để dễ phân tích không?
- [ ] Bạn đã triển khai các công cụ giám sát (e.g., **ELK stack**, **Prometheus**, **Grafana**) chưa?
- [ ] Hệ thống có cảnh báo (alerts) khi có sự cố hoặc lỗi nghiêm trọng không?

### **Triển khai**

- [ ] Ứng dụng có hỗ trợ CI/CD (e.g., GitHub Actions, Azure Pipelines) không?
- [ ] Bạn có kiểm tra đầy đủ trước và sau khi triển khai không?
- [ ] Có cơ chế rollback nếu bản triển khai mới gặp lỗi không?
- [ ] Biến môi trường và cấu hình đã được tách biệt khỏi mã nguồn không?

---

## **Đóng góp**

- [ ] Code có tuân thủ nguyên tắc **SOLID principles** không?
- [ ] Tài liệu onboarding cho nhà phát triển mới có rõ ràng không?
- [ ] Có quy trình rõ ràng cho **pull request**, **code review**, và **branching** không?
- [ ] Các bài kiểm thử tối thiểu có được yêu cầu trước khi merge không?

Danh sách kiểm tra này dành riêng cho ứng dụng ASP.NET, đảm bảo mã nguồn và hệ thống đáp ứng yêu cầu chất lượng, bảo
mật, và hiệu suất cao.
