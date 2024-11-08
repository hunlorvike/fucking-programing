### 1. **Giao thức HTTP/HTTPS và TCP/IP**

HTTP (Hypertext Transfer Protocol) và HTTPS (Hypertext Transfer Protocol Secure) đều là các giao thức ứng dụng hoạt động ở tầng 7 của mô hình OSI (Open Systems Interconnection), tức là chúng là giao thức dùng để trao đổi dữ liệu giữa các ứng dụng (máy khách và máy chủ) trong hệ thống mạng. Tuy nhiên, HTTP và HTTPS cần một giao thức tầng thấp hơn để thực hiện kết nối và truyền tải dữ liệu giữa các máy tính. Đó chính là **TCP** (Transmission Control Protocol).

#### **TCP/IP** – Giao thức nền tảng

TCP/IP (Transmission Control Protocol/Internet Protocol) là bộ giao thức được sử dụng rộng rãi để trao đổi dữ liệu trên Internet. TCP cung cấp một kết nối đáng tin cậy, điều này có nghĩa là dữ liệu được truyền tải sẽ được xác minh, tái truyền nếu bị mất và đảm bảo đúng thứ tự.

- **IP** (Internet Protocol): Là giao thức tầng mạng, có chức năng xác định và truyền tải các gói dữ liệu từ nguồn đến đích qua địa chỉ IP.
- **TCP**: Là giao thức vận chuyển, cung cấp các chức năng như xác nhận (acknowledgement) dữ liệu đã được nhận và đảm bảo không có dữ liệu nào bị mất trong quá trình truyền.

#### **Cách HTTP và HTTPS sử dụng TCP/IP để truyền tải dữ liệu**

Khi một máy khách (browser) muốn truy cập một trang web, quá trình sử dụng HTTP hoặc HTTPS diễn ra qua nhiều bước, bắt đầu từ giao thức **TCP/IP**.

### 2. **Quy Trình Truyền Tải Dữ Liệu HTTP/HTTPS qua TCP/IP**

Dưới đây là quy trình chi tiết khi một máy khách yêu cầu một trang web qua HTTP hoặc HTTPS, từ khi gửi yêu cầu cho đến khi nhận được phản hồi:

#### **2.1 HTTP (Không Bảo Mật)**

1. **Máy khách gửi yêu cầu TCP:**

   - Máy khách mở một kết nối TCP đến máy chủ web thông qua cổng TCP 80 (cổng mặc định cho HTTP).
   - Quy trình bắt đầu với **Bước bắt tay TCP** (TCP Handshake), nơi máy khách và máy chủ xác nhận và thiết lập một kết nối đáng tin cậy.

   Bước bắt tay TCP diễn ra qua ba giai đoạn:

   - **SYN**: Máy khách gửi yêu cầu SYN (synchronize) tới máy chủ, yêu cầu thiết lập kết nối.
   - **SYN-ACK**: Máy chủ nhận yêu cầu và trả lời bằng gói SYN-ACK, xác nhận kết nối.
   - **ACK**: Máy khách trả lời với gói ACK, xác nhận rằng kết nối đã sẵn sàng.

2. **Máy khách gửi yêu cầu HTTP:**
   - Sau khi kết nối TCP được thiết lập, máy khách gửi yêu cầu HTTP (thường là phương thức GET hoặc POST) đến máy chủ. Ví dụ:
     ```http
     GET /index.html HTTP/1.1
     Host: www.example.com
     ```
3. **Máy chủ xử lý và phản hồi:**

   - Máy chủ nhận yêu cầu HTTP, xử lý và trả về một phản hồi HTTP. Phản hồi này sẽ có mã trạng thái HTTP (200 OK, 404 Not Found, v.v.) và nội dung (HTML, hình ảnh, v.v.). Ví dụ:

     ```http
     HTTP/1.1 200 OK
     Content-Type: text/html

     <html>
     <head><title>Example</title></head>
     <body><h1>Welcome</h1></body>
     </html>
     ```

4. **Đóng kết nối TCP:**
   - Sau khi dữ liệu được truyền tải xong, máy khách và máy chủ sẽ đóng kết nối TCP bằng một quy trình gọi là **TCP teardown**. Máy khách sẽ gửi gói FIN để yêu cầu đóng kết nối, và máy chủ sẽ đáp lại với gói ACK.

#### **2.2 HTTPS (Bảo Mật)**

Quy trình với HTTPS rất tương tự với HTTP, nhưng có thêm một bước quan trọng là mã hóa và xác thực SSL/TLS, giúp bảo mật dữ liệu trong suốt quá trình trao đổi.

1. **Bắt tay TCP:**

   - Quy trình bắt tay TCP giống như trong HTTP, nơi máy khách và máy chủ thiết lập một kết nối TCP qua cổng 443 (cổng mặc định của HTTPS).

2. **Bắt tay SSL/TLS (SSL/TLS Handshake):**

   - Sau khi kết nối TCP được thiết lập, máy khách và máy chủ bắt đầu quy trình **SSL/TLS handshake** để thiết lập một kết nối an toàn.
     Quá trình này bao gồm các bước:
   - **ClientHello**: Máy khách gửi yêu cầu với thông tin về các thuật toán mã hóa, phiên bản SSL/TLS mà nó hỗ trợ, và một giá trị ngẫu nhiên.
   - **ServerHello**: Máy chủ trả lời với bộ mã hóa mà nó chọn và gửi chứng chỉ SSL/TLS của mình để chứng minh danh tính.
   - **Kiểm tra chứng chỉ**: Máy khách xác minh tính hợp lệ của chứng chỉ máy chủ. Nếu hợp lệ, máy khách tạo khóa phiên (session key) để mã hóa dữ liệu và gửi cho máy chủ.
   - **Kết thúc Handshake**: Sau khi tạo khóa mã hóa, máy khách và máy chủ gửi thông báo hoàn tất Handshake. Từ đây, tất cả dữ liệu truyền tải sẽ được mã hóa bằng khóa phiên.

3. **Gửi yêu cầu HTTP qua kết nối an toàn (SSL/TLS):**
   - Máy khách gửi yêu cầu HTTP (GET, POST, v.v.) qua kết nối bảo mật SSL/TLS.
4. **Máy chủ phản hồi HTTP qua SSL/TLS:**

   - Máy chủ xử lý yêu cầu và trả về phản hồi được mã hóa bằng SSL/TLS.

5. **Đóng kết nối bảo mật và TCP:**
   - Sau khi hoàn thành trao đổi dữ liệu, kết nối SSL/TLS được đóng trước khi kết nối TCP bị đóng.

### 3. **Sự Khác Biệt Chính Giữa HTTP và HTTPS trong Quá Trình Truyền Tải Dữ Liệu**

| **Tiêu Chí**                         | **HTTP**                               | **HTTPS**                                    |
| ------------------------------------ | -------------------------------------- | -------------------------------------------- |
| **Cổng Mặc Định**                    | 80                                     | 443                                          |
| **Mã Hóa Dữ Liệu**                   | Không mã hóa                           | Dữ liệu được mã hóa bằng SSL/TLS             |
| **Đảm Bảo Bảo Mật**                  | Không đảm bảo bảo mật                  | Mã hóa và xác thực chứng chỉ đảm bảo bảo mật |
| **Hiệu Suất**                        | Tốc độ nhanh hơn vì không có mã hóa    | Có thể chậm hơn vì mã hóa SSL/TLS            |
| **Sử Dụng trong Giao Dịch Nhạy Cảm** | Không thích hợp cho giao dịch nhạy cảm | Phù hợp cho giao dịch và thông tin nhạy cảm  |

### 4. **Kết Luận**

HTTP và HTTPS đều sử dụng giao thức **TCP/IP** để truyền tải dữ liệu, nhưng HTTPS bổ sung thêm các biện pháp bảo mật quan trọng như mã hóa SSL/TLS để bảo vệ thông tin khỏi sự truy cập trái phép trong quá trình trao đổi giữa máy khách và máy chủ. Khi sử dụng HTTP, thông tin có thể bị dễ dàng xâm phạm trong quá trình truyền tải, trong khi với HTTPS, dữ liệu luôn được mã hóa và bảo vệ, làm tăng độ tin cậy và bảo mật, đặc biệt là đối với các giao dịch trực tuyến.
