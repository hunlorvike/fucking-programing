## **🚀 "MỔ XẺ" HTTP & HTTPS: "CẶP ĐÔI" GIAO TIẾP TRÊN WEB CHO DÂN CODE 🚀**

Yo các bạn developer! Hôm nay chúng ta sẽ cùng nhau khám phá về hai "người bạn" không thể thiếu trong thế giới web: HTTP
và HTTPS. Đây là hai giao thức đóng vai trò "trung gian" cho mọi hoạt động trao đổi thông tin giữa trình duyệt của bạn
và server. Cùng mình đi sâu vào chi tiết nhé!

![HTTP vs HTTPS](/assets/images/Difference-Between-HTTP-and-HTTPS.webp)

### **I. HTTP (HYPERTEXT TRANSFER PROTOCOL) LÀ GÌ? (NGÔN NGỮ GIAO TIẾP CƠ BẢN)**

- **HTTP (Hypertext Transfer Protocol):** Là giao thức _ứng dụng_ (application-layer protocol) cho phép trình duyệt web
  và máy chủ web _giao tiếp_ với nhau.
- **Nó hoạt động như thế nào?**
    - Giống như việc bạn gửi thư: bạn có địa chỉ (URL), nội dung (request/response) và người nhận/gửi (client/server).
- **Quan trọng vì:**
    - **Cơ bản:** Là nền tảng của web, mọi website đều sử dụng HTTP.
    - **Đơn giản:** Dễ hiểu và dễ triển khai.
    - **Linh hoạt:** Cho phép truyền tải nhiều loại dữ liệu (HTML, CSS, JS, ảnh,...).

### **II. HTTPS (HTTP SECURE) LÀ GÌ? (HTTP "MẶC GIÁP")**

- **HTTPS (HTTP Secure):** Là phiên bản _bảo mật_ của HTTP, sử dụng _mã hóa_ để bảo vệ thông tin.
- **Nó hoạt động như thế nào?**
    - Giống như gửi thư có phong bì niêm phong: thông tin được mã hóa, chỉ người nhận mới đọc được.
- **Quan trọng vì:**
    - **Bảo mật:** Chống lại các cuộc tấn công "nghe lén", giả mạo.
    - **Tin cậy:** Tăng độ tin cậy của website trong mắt người dùng.
    - **SEO:** Google ưu tiên website dùng HTTPS.

### **III. CÁCH HTTP/HTTPS HOẠT ĐỘNG (QUÁ TRÌNH GỬI/NHẬN DỮ LIỆU)**

1. **Trình duyệt gửi request:** Trình duyệt gửi yêu cầu (request) đến server (ví dụ: GET `/index.html`).
2. **Server xử lý request:** Server nhận request, xử lý và chuẩn bị dữ liệu trả về (response).
3. **Server gửi response:** Server gửi trả lại response (ví dụ: HTML, status code `200 OK`, header).
4. **Trình duyệt nhận response:** Trình duyệt nhận response và hiển thị nội dung cho người dùng.
5. **(HTTPS) Quá trình bắt tay TLS:** Nếu là HTTPS, trước khi trao đổi dữ liệu, trình duyệt và server thực hiện quá
   trình bắt tay TLS để thiết lập kết nối an toàn.

### **IV. REQUEST & RESPONSE (CÁC "THÔNG ĐIỆP" GIAO TIẾP)**

- **Request (Yêu cầu):**
    - **Method (Phương thức):** GET, POST, PUT, DELETE, ...
    - **URL (Đường dẫn):** `/index.html`, `/api/users`, ...
    - **Headers (Tiêu đề):** Thông tin thêm về request (ví dụ: `User-Agent`, `Content-Type`).
    - **Body (Nội dung):** (thường có trong POST, PUT) Dữ liệu gửi kèm theo.
- **Response (Phản hồi):**
    - **Status Code (Mã trạng thái):** 200 OK, 404 Not Found, 500 Internal Server Error, ...
    - **Headers (Tiêu đề):** Thông tin thêm về response (ví dụ: `Content-Type`, `Server`).
    - **Body (Nội dung):** Dữ liệu trả về (HTML, JSON, ảnh, ...).

### **V. MÃ TRẠNG THÁI HTTP (CÁC "TÍN HIỆU" BÁO LỖI/THÀNH CÔNG)**

- **1xx: Thông tin (Informational):** Request đang được xử lý.
- **2xx: Thành công (Success):** Request đã thành công. (200 OK, 201 Created)
- **3xx: Chuyển hướng (Redirection):** Request cần được chuyển hướng. (301 Moved Permanently, 302 Found)
- **4xx: Lỗi Client (Client Error):** Lỗi do phía client. (400 Bad Request, 404 Not Found)
- **5xx: Lỗi Server (Server Error):** Lỗi do phía server. (500 Internal Server Error, 502 Bad Gateway)

### **VI. BẢO MẬT HTTPS (CÁCH "MẶC GIÁP" CHO DỮ LIỆU)**

1. **TLS/SSL (Transport Layer Security/Secure Sockets Layer):** Là giao thức mã hóa, sử dụng _chứng chỉ số_ (SSL/TLS
   certificate).
2. **Quá trình bắt tay TLS:**
    - Trình duyệt và server xác thực lẫn nhau bằng chứng chỉ.
    - Hai bên trao đổi khóa mã hóa bí mật.
    - Dữ liệu được mã hóa trước khi truyền tải.
3. **Mã hóa:** Ngăn chặn người khác đọc được thông tin truyền tải.

### **VII. CÁCH KIỂM TRA HTTP/HTTPS (XEM "THỰC HÀNH")**

1. **Trình duyệt:** Xem URL (có `https://` hay `http://`). Có biểu tượng khóa (https).
2. **Công cụ DevTools (trình duyệt):**
    - Tab Network: Xem các request/response, header, status code.
3. **`curl` (terminal):**

```bash
curl -v http://example.com
curl -v https://google.com
```

- `-v`: Hiển thị thông tin chi tiết.

### **VIII. LƯU Ý QUAN TRỌNG (ĐỂ TRÁNH "SAI SÓT")**

- **HTTP:** Dễ bị tấn công, không nên dùng cho các trang web chứa thông tin nhạy cảm.
- **HTTPS:** Bắt buộc cho các website có thông tin người dùng, tài khoản, thanh toán,...
- **Caching:** Sử dụng cache để tăng tốc độ website.
- **Headers:** Hiểu rõ các header (ví dụ: `Content-Type`, `Cache-Control`, `Set-Cookie`)
- **Status code:** Hiểu rõ ý nghĩa của các mã trạng thái để debug khi có lỗi.

### **IX. ỨNG DỤNG (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Truy cập website:** Tất cả các trang web đều sử dụng HTTP/HTTPS.
- **API:** Giao tiếp giữa các server với nhau.
- **Ứng dụng di động:** Trao đổi dữ liệu với server.
- **Internet of Things:** Giao tiếp giữa các thiết bị thông minh.

### **X. KẾT LUẬN (TỔNG KẾT)**

HTTP và HTTPS là hai giao thức cốt lõi của web. Hiểu rõ về chúng giúp bạn xây dựng web an toàn, hiệu quả và mượt mà hơn.
Hy vọng qua bài viết này, các bạn đã có cái nhìn sâu hơn về "cặp đôi" này và có thể áp dụng vào công việc hàng ngày.
Chúc các bạn code thật "bá đạo"! 😎
