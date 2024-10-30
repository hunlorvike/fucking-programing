## Giao Thức Mạng

### 1. Giao thức HTTP/HTTPS

- **HTTP (HyperText Transfer Protocol)**: Là giao thức chính cho truyền tải dữ liệu trên web. Nó hoạt động theo mô hình request-response.
- **HTTPS (HTTP Secure)**: Là phiên bản bảo mật của HTTP, sử dụng SSL/TLS để mã hóa dữ liệu trong quá trình truyền tải.

### 2. Giao thức FTP

- **FTP (File Transfer Protocol)**: Dùng để truyền tải tệp giữa client và server. Nó cho phép người dùng tải lên và tải xuống tệp từ server.

### 3. Giao thức SMTP/POP3/IMAP

- **SMTP (Simple Mail Transfer Protocol)**: Dùng để gửi email từ client đến server email.
- **POP3 (Post Office Protocol)**: Dùng để lấy email từ server về client. Thường lưu trữ email trên server cho đến khi người dùng tải về.
- **IMAP (Internet Message Access Protocol)**: Cung cấp khả năng quản lý email trực tiếp trên server mà không cần tải về toàn bộ email.

### 4. Giao thức WebSocket

- **WebSocket**: Cung cấp kết nối liên tục giữa client và server, cho phép truyền tải dữ liệu hai chiều theo thời gian thực. Thích hợp cho các ứng dụng như trò chuyện trực tuyến hoặc thông báo thời gian thực.

### 5. Giao thức gRPC

- **gRPC**: Là một giao thức truyền tải dữ liệu dựa trên HTTP/2, cho phép các ứng dụng giao tiếp với nhau một cách hiệu quả hơn thông qua các lời gọi hàm từ xa (remote procedure calls).

### 6. Giao thức SOAP

- **SOAP (Simple Object Access Protocol)**: Một giao thức truyền tải thông điệp XML qua HTTP/HTTPS. Thường được sử dụng trong các dịch vụ web doanh nghiệp.

### 7. Giao thức DNS

- **DNS (Domain Name System)**: Chuyển đổi tên miền thành địa chỉ IP, cho phép client tìm được server mà nó muốn kết nối.

### 8. Giao thức SSH

- **SSH (Secure Shell)**: Cung cấp một phương pháp bảo mật để truy cập vào máy chủ từ xa và thực hiện các lệnh.

### 9. Giao thức RDP

- **RDP (Remote Desktop Protocol)**: Cho phép người dùng truy cập và quản lý máy tính từ xa qua một giao diện đồ họa.

### 10. Giao thức MQTT

- **MQTT (Message Queuing Telemetry Transport)**: Một giao thức nhắn tin nhẹ, thích hợp cho các ứng dụng IoT, cho phép gửi và nhận tin nhắn giữa các thiết bị và server.

### 11. Giao thức TCP/UDP

- **TCP (Transmission Control Protocol)**: Giao thức truyền tải hướng kết nối, đảm bảo dữ liệu được truyền tải chính xác và đầy đủ. Sử dụng kết nối TCP để đảm bảo dữ liệu được truyền tải an toàn và đáng tin cậy.
- **UDP (User Datagram Protocol)**: Giao thức truyền tải không hướng kết nối, nhanh hơn TCP nhưng không đảm bảo tính chính xác và đầy đủ của dữ liệu. Thích hợp cho các ứng dụng yêu cầu tốc độ cao như trò chơi trực tuyến hoặc truyền phát video.

### 12. Giao thức ICMP/IGMP

- **ICMP (Internet Control Message Protocol)**: Giao thức để trao đổi thông tin quản lý mạng giữa các máy tính, chẳng hạn như thông báo lỗi hoặc thông báo kết nối.
- **IGMP (Internet Group Management Protocol)**: Giao thức cho phép máy chủ đa điểm (multicast) truyền dữ liệu đến một nhóm máy khách, thay vì truyền riêng lẻ đến từng máy khách.

### 13. Giao thức DHCP/RIP/OSPF/BGP

- **DHCP (Dynamic Host Configuration Protocol)**: Giao thức tự động cấp phát địa chỉ IP cho các thiết bị mạng, giúp quản lý địa chỉ IP một cách hiệu quả.
- **RIP (Routing Information Protocol)**: Giao thức định tuyến đơn giản, được sử dụng để chia sẻ thông tin định tuyến giữa các bộ định tuyến trong một mạng nhỏ.
- **OSPF (Open Shortest Path First)**: Giao thức định tuyến phức tạp hơn RIP, sử dụng thuật toán Dijkstra để tính toán đường dẫn ngắn nhất cho dữ liệu.
- **BGP (Border Gateway Protocol)**: Giao thức định tuyến sử dụng cho Internet, cho phép kết nối giữa các mạng khác nhau và trao đổi thông tin định tuyến.
