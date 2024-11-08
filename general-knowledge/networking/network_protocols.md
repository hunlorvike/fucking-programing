### 1. **TCP (Transmission Control Protocol)**

- **Định nghĩa:** TCP là giao thức **hướng kết nối**, đảm bảo việc truyền tải dữ liệu đáng tin cậy qua mạng. Nó chia nhỏ dữ liệu thành các gói (packets) và sử dụng cơ chế xác nhận (ACKs) để đảm bảo rằng tất cả các gói dữ liệu đều được nhận và không bị mất mát trong quá trình truyền.
- **Cơ chế hoạt động:**
  - **Kết nối**: Trước khi truyền tải dữ liệu, TCP sẽ thiết lập một kết nối ổn định giữa client và server thông qua ba bước bắt tay (three-way handshake).
  - **Xác nhận**: Sau khi dữ liệu được gửi, mỗi gói sẽ được xác nhận. Nếu không nhận được phản hồi, gói dữ liệu sẽ được gửi lại.
  - **Điều chỉnh lưu lượng**: TCP điều chỉnh tốc độ truyền tải để tránh tình trạng tắc nghẽn mạng.
- **Ứng dụng:** Dùng trong các ứng dụng cần đảm bảo độ tin cậy cao, ví dụ: web (HTTP/HTTPS), email (SMTP), truyền tải tệp (FTP).

---

### 2. **UDP (User Datagram Protocol)**

- **Định nghĩa:** UDP là giao thức **không kết nối** và **không đảm bảo**. Dữ liệu được gửi mà không cần xác nhận từ phía người nhận, điều này giúp giảm độ trễ trong quá trình truyền tải.

- **Cơ chế hoạt động:**
  - **Không kết nối**: UDP gửi gói dữ liệu trực tiếp mà không cần thiết lập kết nối trước.
  - **Không đảm bảo**: Không có cơ chế xác nhận hoặc gửi lại gói bị mất.
- **Ứng dụng:** UDP được sử dụng trong các ứng dụng yêu cầu tốc độ truyền tải nhanh và có thể chấp nhận sự mất mát dữ liệu, ví dụ: video streaming, trò chơi trực tuyến, DNS, VoIP.

---

### 3. **HTTP/HTTPS (HyperText Transfer Protocol / Secure)**

- **Định nghĩa:**

  - **HTTP** là giao thức chính để truyền tải dữ liệu web, đặc biệt là cho các trình duyệt web. HTTP hoạt động theo mô hình yêu cầu - phản hồi (request-response).
  - **HTTPS** là phiên bản bảo mật của HTTP, sử dụng **SSL/TLS** để mã hóa dữ liệu truyền tải giữa client và server.

- **Cơ chế hoạt động:**

  - **HTTP**: Client gửi yêu cầu đến server (ví dụ: yêu cầu tải trang web), và server trả về dữ liệu HTML cho trình duyệt.
  - **HTTPS**: Tương tự HTTP nhưng tất cả dữ liệu được mã hóa qua SSL/TLS để bảo vệ khỏi các cuộc tấn công man-in-the-middle.

- **Ứng dụng:** Dùng trong duyệt web, mua sắm trực tuyến, dịch vụ ngân hàng, v.v.

---

### 4. **FTP (File Transfer Protocol)**

- **Định nghĩa:** FTP là giao thức dùng để **truyền tải tệp** giữa client và server. FTP cho phép người dùng tải lên và tải xuống các tệp từ các máy chủ từ xa.

- **Cơ chế hoạt động:**

  - **Kết nối hai kênh**: FTP sử dụng hai kênh: một kênh điều khiển để gửi lệnh và nhận phản hồi, và một kênh dữ liệu để truyền tệp.
  - **Phiên làm việc**: FTP cho phép người dùng tạo phiên làm việc để truyền tải tệp mà không cần kết nối lại mỗi lần.

- **Ứng dụng:** Sử dụng trong việc quản lý tệp từ xa, tải lên hoặc tải xuống tệp từ các server, thường được sử dụng trong các hệ thống lưu trữ dữ liệu hoặc web hosting.

---

### 5. **SMTP/POP3/IMAP (Email Protocols)**

- **SMTP (Simple Mail Transfer Protocol)**:

  - Giao thức chính để **gửi email** từ client đến server. SMTP yêu cầu server nhận và chuyển tiếp email đến các server đích.
  - **Cơ chế hoạt động**: SMTP sử dụng các lệnh như HELO, MAIL FROM, RCPT TO, DATA để gửi và chuyển tiếp email.

- **POP3 (Post Office Protocol)**:

  - Dùng để **lấy email** từ server về client. POP3 chỉ tải xuống email và không giữ lại trên server sau khi tải xong.
  - **Cơ chế hoạt động**: Người dùng kết nối tới server, tải về các email và sau đó xóa khỏi server.

- **IMAP (Internet Message Access Protocol)**:
  - Tương tự POP3 nhưng có khả năng quản lý email trực tiếp trên server mà không cần tải xuống toàn bộ email.
  - **Cơ chế hoạt động**: IMAP cho phép người dùng quản lý thư mục, đánh dấu đã đọc/chưa đọc, và truy cập vào email từ nhiều thiết bị.

---

### 6. **DNS (Domain Name System)**

- **Định nghĩa:** DNS là giao thức cho phép **chuyển đổi tên miền** (ví dụ: `www.google.com`) thành **địa chỉ IP** (ví dụ: `172.217.11.46`), giúp các máy tính và thiết bị trên mạng có thể giao tiếp với nhau.

- **Cơ chế hoạt động:**
  - Người dùng nhập tên miền vào trình duyệt.
  - Trình duyệt gửi yêu cầu DNS đến máy chủ DNS, máy chủ sẽ tìm kiếm địa chỉ IP tương ứng và trả về kết quả cho client.
- **Ứng dụng:** Dùng trong việc phân giải tên miền web, giúp người dùng dễ dàng truy cập vào các website mà không cần nhớ địa chỉ IP.

---

### 7. **SSH (Secure Shell)**

- **Định nghĩa:** SSH là giao thức bảo mật cho phép người dùng **truy cập từ xa** vào máy chủ và thực thi các lệnh. SSH mã hóa kết nối để bảo vệ dữ liệu trong quá trình truyền tải.

- **Cơ chế hoạt động:**

  - SSH sử dụng các thuật toán mã hóa mạnh mẽ (như AES) để bảo vệ thông tin đăng nhập và dữ liệu trao đổi giữa client và server.
  - Các kết nối SSH thường được bảo vệ bằng mật khẩu hoặc khóa công khai/riêng tư.

- **Ứng dụng:** SSH chủ yếu được sử dụng trong quản trị hệ thống, cho phép quản trị viên truy cập và điều khiển các máy chủ từ xa.

---

### 8. **WebSocket**

- **Định nghĩa:** WebSocket là một giao thức **hai chiều**, cho phép **kết nối liên tục** giữa client và server để truyền tải dữ liệu theo thời gian thực.

- **Cơ chế hoạt động:**

  - WebSocket bắt đầu với một yêu cầu HTTP để thiết lập kết nối. Sau đó, giao thức chuyển sang WebSocket và duy trì một kết nối mở để truyền tải dữ liệu.
  - Điều này cho phép server gửi thông tin mới đến client ngay lập tức mà không cần phải chờ yêu cầu từ client.

- **Ứng dụng:** Thường được sử dụng trong các ứng dụng chat, trò chơi trực tuyến, và các ứng dụng cần dữ liệu theo thời gian thực.

---

### 9. **gRPC (Google Remote Procedure Call)**

- **Định nghĩa:** gRPC là một giao thức truyền tải dữ liệu dựa trên **HTTP/2**, cho phép các ứng dụng giao tiếp hiệu quả hơn qua các **lời gọi hàm từ xa** (RPC).

- **Cơ chế hoạt động:**

  - gRPC sử dụng HTTP/2 để hỗ trợ truyền tải song song, mã hóa dữ liệu qua SSL/TLS, và cho phép các hệ thống tương tác qua các lời gọi hàm từ xa.
  - Dữ liệu được gửi dưới dạng **Protocol Buffers (protobuf)**, một định dạng nhị phân hiệu quả và dễ sử dụng.

- **Ứng dụng:** Được sử dụng trong các microservices, nơi có sự giao tiếp giữa các dịch vụ qua mạng.

---

### 10. **RDP (Remote Desktop Protocol)**

- **Định nghĩa:** RDP là giao thức của Microsoft cho phép người dùng **truy cập desktop từ xa** qua một giao diện đồ họa.

- **Cơ chế hoạt động:**

  - Người dùng sẽ kết nối đến máy tính hoặc máy chủ từ xa qua RDP, sử dụng giao diện đồ họa và các lệnh bàn phím chuột để điều khiển hệ thống từ xa.

- **Ứng dụng:** Dùng trong quản trị hệ thống, hỗ trợ người dùng truy cập máy tính của mình từ bất kỳ đâu.
