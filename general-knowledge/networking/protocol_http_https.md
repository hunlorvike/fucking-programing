# HTTP và HTTPS: Giao thức truyền tải siêu văn bản

## Mục lục

1. [Tổng quan về HTTP và HTTPS](#1-tổng-quan-về-http-và-https)  
2. [HTTP: Giao thức truyền tải siêu văn bản](#2-http-giao-thức-truyền-tải-siêu-văn-bản)  
   - [2.1. Khái niệm và lịch sử phát triển](#21-khái-niệm-và-lịch-sử-phát-triển)  
   - [2.2. Phương thức HTTP](#22-phương-thức-http)  
   - [2.3. HTTP/1.1, HTTP/2, và HTTP/3](#23-http11-http2-và-http3)  
3. [HTTPS: HTTP bảo mật](#3-https-http-bảo-mật)  
   - [3.1. Sự khác biệt giữa HTTP và HTTPS](#31-sự-khác-biệt-giữa-http-và-https)  
   - [3.2. SSL/TLS: Nền tảng của HTTPS](#32-ssltls-nền-tảng-của-https)  
4. [So sánh HTTP và HTTPS](#4-so-sánh-http-và-https)  
5. [Ứng dụng thực tiễn của HTTP và HTTPS](#5-ứng-dụng-thực-tiễn-của-http-và-https)  
6. [Bảo mật trong HTTPS](#6-bảo-mật-trong-https)  
7. [Kết luận](#7-kết-luận)

---

## 1. Tổng quan về HTTP và HTTPS

HTTP (Hypertext Transfer Protocol) và HTTPS (Hypertext Transfer Protocol Secure) là hai giao thức quan trọng trong việc truyền tải dữ liệu trên web. HTTP cung cấp cơ chế trao đổi dữ liệu không bảo mật, trong khi HTTPS tăng cường an toàn bằng cách mã hóa dữ liệu giữa máy khách và máy chủ.

---

## 2. HTTP: Giao thức truyền tải siêu văn bản

### 2.1. **Khái niệm và lịch sử phát triển:**
- **HTTP:** Là giao thức giao tiếp giữa máy khách (web browser) và máy chủ (web server), ra đời năm 1991 bởi Tim Berners-Lee.  
- **Nguyên lý hoạt động:** Máy khách gửi yêu cầu (request) đến máy chủ, máy chủ phản hồi (response) với nội dung hoặc thông báo trạng thái.  
- **Không trạng thái (stateless):** Mỗi yêu cầu HTTP độc lập, không lưu trữ trạng thái giữa các lần kết nối.

### 2.2. **Phương thức HTTP:**
HTTP sử dụng các phương thức để thực hiện các hành động trên tài nguyên web:
- **GET:** Lấy dữ liệu từ máy chủ (truy cập trang web).  
- **POST:** Gửi dữ liệu lên máy chủ (đăng nhập, gửi form).  
- **PUT:** Cập nhật hoặc thay thế tài nguyên.  
- **DELETE:** Xóa tài nguyên trên máy chủ.  
- **HEAD:** Lấy thông tin header mà không cần tải nội dung.  
- **PATCH:** Thay đổi một phần tài nguyên.  
- **OPTIONS:** Kiểm tra các phương thức hỗ trợ trên máy chủ.

### 2.3. **HTTP/1.1, HTTP/2, và HTTP/3:**
#### **HTTP/1.1:**
- Ra mắt năm 1997.  
- Hỗ trợ kết nối lâu dài (**persistent connection**).  
- Cải thiện hiệu suất bằng cách sử dụng **chunked transfer encoding**.  

#### **HTTP/2:**
- Ra mắt năm 2015.  
- Sử dụng nén header để giảm dữ liệu truyền tải.  
- Cho phép truyền tải đồng thời (multiplexing), tăng tốc độ tải trang.  

#### **HTTP/3:**
- Dựa trên giao thức QUIC (Quick UDP Internet Connections).  
- Cải thiện tốc độ và giảm độ trễ so với HTTP/2.  

---

## 3. HTTPS: HTTP bảo mật

### 3.1. **Sự khác biệt giữa HTTP và HTTPS:**
HTTPS là phiên bản bảo mật của HTTP, sử dụng mã hóa để bảo vệ dữ liệu.
- **HTTP:** Gửi dữ liệu dưới dạng văn bản thuần, dễ bị tấn công.  
- **HTTPS:** Mã hóa dữ liệu để tránh bị chặn hoặc đánh cắp.

### 3.2. **SSL/TLS: Nền tảng của HTTPS**
- **SSL (Secure Sockets Layer):** Giao thức bảo mật ban đầu, hiện đã lỗi thời.  
- **TLS (Transport Layer Security):** Phiên bản nâng cao của SSL, đảm bảo tính toàn vẹn và bí mật của dữ liệu.  
#### **Quá trình hoạt động của HTTPS:**
1. **Bắt tay SSL/TLS (Handshake):**  
   - Xác thực danh tính của máy chủ qua chứng chỉ số (SSL certificate).  
   - Thỏa thuận khóa mã hóa phiên (session key).  
2. **Mã hóa dữ liệu:** Dữ liệu được mã hóa trước khi truyền tải.  
3. **Xác thực:** Đảm bảo dữ liệu không bị thay đổi trong quá trình truyền.

---

## 4. So sánh HTTP và HTTPS

| **Đặc điểm**           | **HTTP**                          | **HTTPS**                         |
|-------------------------|------------------------------------|------------------------------------|
| **Bảo mật dữ liệu**     | Không                             | Có                                |
| **Mã hóa**             | Không                             | Dữ liệu được mã hóa               |
| **Cổng mặc định**       | 80                               | 443                               |
| **Tốc độ**             | Nhanh hơn (không mã hóa)          | Chậm hơn (do mã hóa và xác thực)  |
| **Tin cậy**            | Không                             | Cao                               |
| **Ứng dụng**           | Trang web không yêu cầu bảo mật   | Giao dịch tài chính, đăng nhập,...|

---

## 5. Ứng dụng thực tiễn của HTTP và HTTPS

### **HTTP:**
- Trang web công khai không yêu cầu bảo mật (như blog cá nhân, trang tin tức).  
- Tải tài nguyên công khai (ảnh, video).  

### **HTTPS:**
- Giao dịch trực tuyến (thanh toán, ngân hàng).  
- Mạng xã hội, email, dịch vụ đăng nhập.  
- API, dịch vụ IoT cần bảo mật.

---

## 6. Bảo mật trong HTTPS

### **Lợi ích của HTTPS:**
1. **Bảo vệ thông tin người dùng:** Ngăn chặn tấn công kiểu **man-in-the-middle**.  
2. **Xác thực:** Đảm bảo người dùng truy cập đúng trang web chính thống.  
3. **SEO:** Các công cụ tìm kiếm ưu tiên xếp hạng cho các trang HTTPS.  
4. **Tăng độ tin cậy:** Biểu tượng khóa trên trình duyệt làm tăng uy tín của trang web.

### **Hạn chế của HTTPS:**
- Yêu cầu chi phí mua chứng chỉ SSL/TLS.  
- Tăng tải xử lý trên máy chủ.  

---

## 7. Kết luận

HTTP và HTTPS đóng vai trò không thể thiếu trong việc truy cập và bảo mật thông tin trên Internet. Trong khi HTTP phù hợp cho các ứng dụng không yêu cầu bảo mật cao, HTTPS đã trở thành tiêu chuẩn mới cho việc xây dựng các trang web và dịch vụ an toàn. Hiểu rõ cả hai giao thức sẽ giúp cải thiện khả năng thiết kế, bảo trì và tối ưu hóa hệ thống web trong môi trường mạng hiện đại.