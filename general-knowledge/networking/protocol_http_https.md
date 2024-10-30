## Tổng Quan về HTTP và HTTPS: Nắm Vững Kiến Thức Về Giao Thức Web

**Giới thiệu**

HTTP (HyperText Transfer Protocol) và HTTPS (HTTP Secure) là hai giao thức nền tảng của Internet, đóng vai trò trọng yếu trong việc truyền tải dữ liệu giữa máy khách (client) và máy chủ (server). Cùng khám phá chi tiết về hai giao thức này để hiểu rõ vai trò và sự khác biệt của chúng.

**1. HTTP (HyperText Transfer Protocol)**

**1.1 Định Nghĩa:**

HTTP là một giao thức ứng dụng tầng cao, hoạt động theo mô hình client-server, được sử dụng để truyền tải dữ liệu trên World Wide Web. HTTP được thiết kế để giao tiếp giữa máy khách và máy chủ bằng cách sử dụng các yêu cầu và phản hồi theo dạng văn bản.

**1.2 Cấu Trúc URL:**

URL (Uniform Resource Locator) là địa chỉ duy nhất của mỗi tài nguyên trên web, theo định dạng:
`http://www.example.com/path/to/resource`

- **http://**: là phần biểu thị giao thức HTTP
- **www.example.com**: là tên miền của website
- **path/to/resource**: là đường dẫn đến tài nguyên cụ thể trên máy chủ.

**1.3 Chức Năng:**

HTTP cho phép máy khách gửi yêu cầu đến máy chủ và nhận phản hồi. Các phương thức phổ biến gồm:

- **GET**: Lấy dữ liệu từ máy chủ.
  - Ví dụ: Truy cập vào một trang web, tải xuống hình ảnh.
- **POST**: Gửi dữ liệu lên máy chủ.
  - Ví dụ: Gửi thông tin đăng nhập, đăng ký tài khoản, gửi biểu mẫu.
- **PUT**: Cập nhật dữ liệu hiện có trên máy chủ.
- **DELETE**: Xóa dữ liệu trên máy chủ.

**1.4 Ưu Điểm:**

- Đơn giản, dễ dàng triển khai và sử dụng.
- Tốc độ nhanh do không có quá trình mã hóa dữ liệu.
- Hỗ trợ nhiều loại tài liệu, bao gồm văn bản, hình ảnh, video, âm thanh, v.v.

**1.5 Nhược Điểm:**

- Không bảo mật, thông tin truyền tải có thể bị đánh cắp hoặc giả mạo trong quá trình truyền tải.
- Không phù hợp với các giao dịch trực tuyến, truyền tải thông tin nhạy cảm.

**2. HTTPS (HTTP Secure)**

**2.1 Định Nghĩa:**

HTTPS là phiên bản bảo mật của HTTP, sử dụng giao thức mã hóa SSL (Secure Sockets Layer) hoặc TLS (Transport Layer Security) để bảo vệ thông tin trao đổi giữa máy khách và máy chủ.

**2.2 Cấu Trúc URL:**

URL của HTTPS có định dạng:
`https://www.example.com/path/to/resource`

- **https://**: biểu thị giao thức HTTPS sử dụng mã hóa SSL/TLS.

**2.3 Chức Năng:**

HTTPS mã hóa và bảo mật dữ liệu, giúp bảo vệ thông tin khỏi bị chặn hoặc giả mạo trong quá trình truyền tải, đặc biệt quan trọng cho:

- Các giao dịch trực tuyến như thanh toán, mua hàng, đăng nhập tài khoản.
- Trao đổi thông tin nhạy cảm như mật khẩu, số thẻ tín dụng, thông tin cá nhân.

**2.4 Ưu Điểm:**

- **Bảo mật**: Thông tin được mã hóa, bảo vệ khỏi truy cập trái phép.
- **Tăng độ tin cậy**: Người dùng tin tưởng vào các trang web HTTPS.
- **Bảo vệ dữ liệu khỏi bị giả mạo**: Ngăn chặn việc đánh cắp thông tin, tạo cảm giác an toàn cho người dùng.

**2.5 Nhược Điểm:**

- **Tốc độ**: Có thể chậm hơn một chút do quá trình mã hóa.
- **Chi phí**: Yêu cầu chứng chỉ SSL/TLS, có thể tốn chi phí cho doanh nghiệp nhỏ.

**3. So Sánh giữa HTTP và HTTPS:**

| Tiêu chí          | HTTP                                   | HTTPS                                       |
| ----------------- | -------------------------------------- | ------------------------------------------- |
| **Bảo mật**       | Không mã hóa dữ liệu                   | Dữ liệu được mã hóa                         |
| **Cổng mặc định** | 80                                     | 443                                         |
| **Chứng thực**    | Không có                               | Sử dụng chứng chỉ SSL/TLS                   |
| **Hiệu suất**     | Nhanh hơn do không mã hóa              | Có thể chậm hơn một chút vì mã hóa          |
| **Ứng dụng**      | Thích hợp cho thông tin không nhạy cảm | Phù hợp với giao dịch và thông tin nhạy cảm |

**4. Cách thức hoạt động của HTTP và HTTPS:**

**4.1 HTTP:**

- **Kết nối**: Máy khách gửi yêu cầu kết nối đến máy chủ.
- **Gửi yêu cầu**: Máy khách gửi yêu cầu HTTP với các phương thức (GET, POST, PUT, DELETE).
- **Nhận phản hồi**: Máy chủ xử lý yêu cầu và trả về dữ liệu, thường là mã HTML.

**Ví dụ về yêu cầu HTTP:**

```http
GET /index.html HTTP/1.1
Host: www.example.com
```

**4.2 HTTPS:**

- **Kết nối an toàn**: Máy khách và máy chủ thiết lập kết nối an toàn thông qua trao đổi chứng chỉ SSL/TLS.
- **Mã hóa dữ liệu**: Dữ liệu được mã hóa trước khi gửi.
- **Gửi và nhận dữ liệu**: Dữ liệu trao đổi được bảo vệ bằng kết nối mã hóa.

**Ví dụ về yêu cầu HTTPS:**

```http
GET /index.html HTTP/1.1
Host: www.example.com
```

**5. Chi Tiết về Cách HTTP và HTTPS Gửi Dữ Liệu và Bảo Mật:**

**5.1 HTTP:**

- **Gửi yêu cầu**: Máy khách gửi yêu cầu HTTP với các thành phần:
  - Phương thức (GET, POST, PUT, DELETE)
  - Đường dẫn đến tài nguyên.
  - Headers bổ sung thông tin yêu cầu.
  - Thân yêu cầu (Body) (chỉ với một số phương thức như POST hoặc PUT).

**Ví dụ về yêu cầu POST:**

```http
POST /api/user HTTP/1.1
Host: www.example.com
Content-Type: application/json

{
    "name": "John",
    "age": 30
}
```

- **Xử lý yêu cầu**: Máy chủ nhận, xử lý yêu cầu và trả về kết quả.
- **Gửi phản hồi**: Máy chủ gửi lại phản hồi với:
  - Mã trạng thái (200 OK, 404 Not Found).
  - Headers bổ sung thông tin.
  - Thân phản hồi (Body) chứa dữ liệu.

**Ví dụ về phản hồi:**

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "User created successfully"
}
```

**5.2 HTTPS:**

- **SSL/TLS Handshake**:

  - **Xác thực máy chủ**: Máy chủ gửi chứng chỉ SSL/TLS để máy khách xác thực.
  - **Trao đổi khóa**: Máy khách và máy chủ tạo khóa bí mật (session key) để mã hóa dữ liệu.

- **Mã hóa dữ liệu**: Sau khi kết nối an toàn, dữ liệu truyền tải được mã hóa, giúp bảo mật thông tin khỏi truy cập trái phép.

**6. Handshake trong HTTPS:**

- **Handshake**: là quá trình thiết lập kết nối an toàn giữa máy khách và máy chủ trong HTTPS. Quá trình này đảm bảo cả hai đồng ý về các thông số mã hóa, và máy khách có thể xác thực danh tính của máy chủ.

**Các Bước trong TLS/SSL Handshake:**

1. **Máy khách gửi yêu cầu kết nối**:

   - Gửi yêu cầu ClientHello, gồm thông tin:
     - Phiên bản SSL/TLS hỗ trợ.
     - Các bộ mã hóa (cipher suites) khả dụng.
     - Một số ngẫu nhiên hỗ trợ mã hóa.

2. **Máy chủ phản hồi**:

   - Gửi lại phản hồi ServerHello:
     - Chọn phiên bản SSL/TLS và bộ mã hóa.
     - Gửi chứng chỉ số để xác thực danh tính.
     - Gửi một số ngẫu nhiên khác hỗ trợ mã hóa.

3. **Xác thực chứng chỉ máy chủ**:

   - Máy khách kiểm tra chứng chỉ máy chủ.
   - Nếu chứng chỉ hợp lệ, quá trình Handshake tiếp tục; nếu không, kết nối bị hủy.

4. **Tạo khóa phiên (Session Key)**:

   - Máy khách tạo khóa phiên dùng cho mã hóa dữ liệu trao đổi trong phiên.

5. **Hoàn tất Handshake**:
   - Máy khách và máy chủ gửi thông báo hoàn tất Handshake. Từ đây, dữ liệu trao đổi đều được mã hóa.

**7. Kết Luận:**

HTTP và HTTPS là hai giao thức quan trọng trong hoạt động của World Wide Web. Mặc dù HTTP đơn giản và nhanh, nhưng nó không bảo mật, trong khi HTTPS mang đến bảo mật cao cho dữ liệu nhạy cảm. Việc lựa chọn giữa HTTP và HTTPS phụ thuộc vào nhu cầu bảo mật và tính nhạy cảm của dữ liệu được truyền tải.
