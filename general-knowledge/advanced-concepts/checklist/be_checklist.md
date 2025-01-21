## **🚀 DANH SÁCH KIỂM TRA CODE BACK-END ASP.NET: "CHECKLIST" ĐỈNH CAO CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay mình sẽ chia sẻ một "checklist" cực kỳ quan trọng cho dân code backend ASP.NET: **Danh
sách kiểm tra code (Code Checklist)**. Đây là một công cụ giúp bạn kiểm tra lại code của mình, đảm bảo chất lượng, bảo
mật, hiệu suất và dễ bảo trì. Cùng mình khám phá nhé!

### **I. TẠI SAO CẦN CHECKLIST? (VÌ "CẨN TẮC VÔ ƯU")**

- **Checklist:** Là danh sách các việc cần làm để kiểm tra code trước khi chạy thật.
- **Quan trọng vì:**
    - **Chất lượng:** Đảm bảo code chạy đúng, không có lỗi.
    - **Bảo mật:** Ngăn chặn hacker tấn công.
    - **Hiệu suất:** Giúp ứng dụng chạy nhanh, mượt mà.
    - **Dễ bảo trì:** Code dễ đọc, dễ sửa chữa sau này.

### **II. CHECKLIST CHI TIẾT CHO BACK-END ASP.NET**

#### **1. BẢO MẬT (SECURITY) - "KHÓA CỬA" CẨN THẬN**

-   [ ] **Xác thực/Ủy quyền (Authentication/Authorization):**

    - Dùng **ASP.NET Identity**, **JWT** hoặc **OAuth2** để bảo vệ API (như bài trước chúng ta đã nói).
    - **Kiểm tra:** Các API/endpoint đã được bảo vệ chưa?

-   [ ] **Kiểm tra đầu vào (Input Validation):**

    - Dùng **middleware** để kiểm tra dữ liệu đầu vào, tránh **SQL Injection**, **XSS**, ...
    - **Kiểm tra:** Dữ liệu người dùng nhập vào có hợp lệ không?

-   [ ] **Thông tin nhạy cảm:**

    - Ẩn connection string, API keys trong `appsettings.json`.
    - Dùng **User Secrets** hoặc **Azure Key Vault** (như đã nói ở bài về cryptography).
    - **Kiểm tra:** Thông tin nhạy cảm có bị lộ không?

-   [ ] **Mật khẩu:**

    - Dùng **ASP.NET Identity với BCrypt** để mã hóa mật khẩu.
    - **Kiểm tra:** Mật khẩu có được băm/mã hóa chưa?

-   [ ] **CORS (Cross-Origin Resource Sharing):**

    - Cấu hình CORS để chỉ cho phép các domain được phép truy cập (bài về API).
    - **Kiểm tra:** Chỉ cho domain nào truy cập API?

-   [ ] **Rate Limiting:**

    - Dùng **AspNetCoreRateLimit** để chặn brute force (như đã nói ở bài về API).
    - **Kiểm tra:** Có giới hạn số lần gọi API không?

-   [ ] **NuGet Packages:**

    - Cập nhật các package để vá lỗi bảo mật.
    - **Kiểm tra:** Package có lỗi bảo mật không?

-   [ ] **CSRF (Cross-Site Request Forgery):**

    - Dùng `AntiForgeryToken` trong Razor Pages hoặc MVC để chống CSRF.
    - **Kiểm tra:** Có dùng CSRF token không?

-   [ ] **JWT (JSON Web Token):**

    - Có hết hạn (expire), có bảo vệ chống JWT Hijacking không?
    - **Kiểm tra:** JWT có an toàn không?

-   [ ] **Thư mục nhạy cảm:**
    - Bảo vệ các thư mục như `wwwroot`, `logs` bằng IIS hoặc Kestrel.
    - **Kiểm tra:** Có ai truy cập file nhạy cảm không?

#### **2. HIỆU SUẤT (PERFORMANCE) - "CHẠY NHANH NHƯ CHỚP"**

-   [ ] **Caching:**
    - Dùng **Response Caching** hoặc **Distributed Caching (Redis)** cho dữ liệu thường dùng.
    - **Kiểm tra:** Có cache dữ liệu không?
-   [ ] **Tối ưu database:**
    - Dùng **AsNoTracking**, **projection**, **caching** với Entity Framework Core.
    - **Kiểm tra:** Database có tối ưu không?
-   [ ] **Connection Pooling:**
    - Có dùng connection pooling với database không?
    - **Kiểm tra:** Có tái sử dụng connection không?
-   [ ] **Scale-out:**
    - Hỗ trợ scale-out (Azure App Service Scale, Kubernetes).
    - **Kiểm tra:** Có dễ mở rộng hệ thống không?
-   [ ] **Response Compression:**
    - Dùng Gzip hoặc Brotli để nén response.
    - **Kiểm tra:** Có nén dữ liệu không?
-   [ ] **IAsyncEnumerable/IQueryable:**
    - Dùng để tối ưu khi xử lý dữ liệu lớn (bài về cơ sở dữ liệu).
    - **Kiểm tra:** Có dùng đúng kiểu dữ liệu khi làm việc với data lớn không?
-   [ ] **Background Services/Queues:**
    - Chuyển công việc nặng sang **Background Services** (Hangfire, Azure Queue).
    - **Kiểm tra:** Có task nào chạy quá lâu không?
-   [ ] **Giám sát:**
    - Dùng **Application Insights** hoặc **Serilog** để theo dõi hiệu suất.
    - **Kiểm tra:** Có theo dõi hiệu suất không?

#### **3. CHẤT LƯỢNG MÃ NGUỒN (CODE "GỌN GÀNG" VÀ DỄ HIỂU)**

-   [ ] **Coding Guidelines:** Tuân thủ **Microsoft Coding Guidelines**.
-   [ ] **SRP (Single Responsibility Principle):** Các controller/service chỉ làm 1 việc.
-   [ ] **DRY (Don't Repeat Yourself):** Không copy code, dùng chung hàm, class.
-   [ ] **Tên rõ ràng:** Tên biến, hàm, class dễ hiểu.
-   [ ] **Loại bỏ log:** Xóa các log không cần thiết (`Console.WriteLine`, `Debug.WriteLine`).
-   [ ] **Cấu trúc code:** Code được chia thành các tầng riêng (Controllers, Services, Repositories).
-   [ ] **Linters:** Dùng **SonarQube**, **StyleCop**, hoặc **Resharper** để kiểm tra code.
-   [ ] **Xử lý lỗi:** Xử lý các tình huống lỗi, điều kiện biên.
-   [ ] **Thông báo lỗi:** Thông báo lỗi dễ hiểu, không tiết lộ thông tin nhạy cảm.
-   [ ] **Memory leak:** Xử lý memory leak, dùng `IDisposable`, `using` blocks (như đã nói ở bài quản lý bộ nhớ).

#### **4. TÀI LIỆU (DOCUMENTATION) - "HƯỚNG DẪN" ĐẦY ĐỦ**

-   [ ] **Swagger:** Mô tả các API bằng Swagger (Swashbuckle), NSwag.
-   [ ] **Cấu trúc dự án:** Tài liệu giải thích cấu trúc project, cách cấu hình.
-   [ ] **Chú thích:** Chú thích code phức tạp để dễ hiểu.
-   [ ] **Hướng dẫn chạy:** Hướng dẫn cài đặt, kết nối database, ...
-   [ ] **Giới hạn/lỗi:** Tài liệu liệt kê các lỗi và giới hạn của ứng dụng.
-   [ ] **Dependency:** Liệt kê các package trong `README` (hoặc file tương tự).

#### **5. KIỂM THỬ (TESTING) - "THỬ NGHIỆM" CẨN THẬN**

1. **Kiểm thử chức năng (Functional Test):**
    - **Status code:** Các API trả về đúng status code (200, 400, 401, 404, 500).
    - **Xác thực đầu vào:** Xác thực dữ liệu đầu vào bằng **Data Annotations** hoặc **Fluent Validation**.
    - **Xử lý lỗi:** Kiểm tra các tình huống lỗi đã xử lý đúng cách.
    - **Môi trường:** Kiểm thử trên các môi trường (dev, staging, prod).
    - **Unit test/Integration test:** Viết unit test và integration test bằng xUnit, MSTest, NUnit, ...
    - **Code Coverage:** Độ bao phủ code phải đạt mức mong muốn (≥80%).
2. **Kiểm thử hiệu suất (Performance Test):**
    - Dùng **Apache JMeter**, **k6**, **Visual Studio Load Test** để kiểm tra tải.
    - Kiểm tra hệ thống khi có tải lớn (stress test).
    - Kiểm tra khả năng phục hồi khi có lỗi hiệu suất (ví dụ: database timeout).
3. **Kiểm thử bảo mật (Security Test):**
    - Dùng **OWASP ZAP**, **Burp Suite** để kiểm tra bảo mật.
    - Mô phỏng các cuộc tấn công (SQL Injection, XSS, Brute Force).
    - Dữ liệu nhạy cảm trong log đã được ẩn/mã hóa chưa?

#### **6. QUẢN LÝ TÀI NGUYÊN (KHÔNG LÃNG PHÍ)**

1. **Cơ sở dữ liệu:**
    - Database có thiết kế tối ưu (chuẩn hóa, khử chuẩn hóa).
    - Có index cho các cột hay tìm kiếm.
    - Truy vấn được kiểm tra và tối ưu.
    - Dữ liệu được backup thường xuyên.
2. **Logging & Giám sát:**
    - Dùng **Serilog**, **NLog**, **Application Insights** để ghi log.
    - Logs có định dạng chuẩn (JSON) để dễ phân tích.
    - Có các công cụ giám sát (ELK stack, Prometheus, Grafana).
    - Có cảnh báo khi có lỗi nghiêm trọng.
3. **Triển khai:**
    - Hỗ trợ CI/CD (GitHub Actions, Azure Pipelines).
    - Kiểm tra trước/sau khi deploy.
    - Có cơ chế rollback khi có lỗi.
    - Tách biệt biến môi trường/cấu hình ra khỏi code.

#### **7. ĐÓNG GÓP (LÀM VIỆC "NHÓM" THẬT TỐT)**

- **SOLID Principles:** Code có tuân thủ SOLID không?
- **Tài liệu onboarding:** Tài liệu cho người mới rõ ràng.
- **Pull request/Code review:** Có quy trình rõ ràng cho pull request, code review, branching.
- **Kiểm thử trước khi merge:** Yêu cầu các bài kiểm thử phải pass trước khi merge.

### **VII. KẾT LUẬN (TỔNG KẾT)**

Checklist này sẽ giúp các bạn kiểm tra code một cách cẩn thận, đảm bảo chất lượng, bảo mật, hiệu suất và dễ bảo trì cho
ứng dụng ASP.NET. Nhớ rằng, code tốt là code vừa chạy đúng, vừa an toàn, nhanh và dễ hiểu. Chúc các bạn code thành công!
😎
