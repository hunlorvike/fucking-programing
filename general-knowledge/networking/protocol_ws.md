## Tổng Quan về WebSocket

WebSocket là một giao thức truyền thông hai chiều qua kết nối TCP, cho phép dữ liệu được truyền tải trong thời gian thực giữa máy khách (client) và máy chủ (server). Không giống như giao thức HTTP, WebSocket hỗ trợ truyền thông tin liên tục mà không cần thiết lập kết nối mới mỗi lần trao đổi dữ liệu.

### 1. Định Nghĩa

WebSocket là giao thức được thiết kế để tối ưu hóa cho việc truyền dữ liệu thời gian thực. Nó hoạt động trên cổng TCP 80 hoặc 443 và có thể duy trì kết nối mở liên tục giữa client và server, rất phù hợp cho các ứng dụng như trò chuyện trực tuyến, trò chơi thời gian thực, và các dịch vụ cập nhật dữ liệu liên tục.

### 2. Cấu Trúc URL

WebSocket sử dụng định dạng URL đặc biệt để thiết lập kết nối:

- **ws://**: Sử dụng khi không yêu cầu bảo mật.
- **wss://**: Sử dụng cho kết nối bảo mật, mã hóa dữ liệu bằng SSL/TLS.

Ví dụ:

- `ws://example.com/socket`
- `wss://example.com/socket`

### 3. Chức Năng Chính

WebSocket cho phép trao đổi dữ liệu hai chiều trong thời gian thực. Một khi kết nối được thiết lập, cả client và server đều có thể gửi dữ liệu bất kỳ lúc nào mà không cần yêu cầu hoặc phản hồi liên tục như HTTP.

#### Các Tính Năng Nổi Bật:

- **Hai Chiều (Full Duplex)**: Dữ liệu có thể được truyền tải đồng thời từ cả hai phía.
- **Kết Nối Duy Trì Liên Tục**: Không cần thiết lập lại kết nối sau mỗi lần trao đổi dữ liệu.
- **Tốc Độ Cao**: Truyền dữ liệu nhanh hơn so với HTTP do không cần tải lại trang hoặc thực hiện nhiều yêu cầu.

### 4. Cách WebSocket Hoạt Động

#### Quá Trình Thiết Lập Kết Nối

WebSocket bắt đầu bằng việc thiết lập kết nối từ client đến server qua giao thức HTTP, sau đó chuyển đổi sang WebSocket:

1. **Yêu Cầu Ban Đầu (Handshake)**: Client gửi một yêu cầu kết nối WebSocket dưới dạng HTTP request.
2. **Xác Nhận của Server**: Server đáp lại yêu cầu bằng một mã phản hồi (status code 101 Switching Protocols), cho phép chuyển đổi sang WebSocket.
3. **Chuyển Đổi Giao Thức**: Sau khi xác nhận, kết nối chuyển sang WebSocket và không cần thực hiện yêu cầu HTTP nữa. Kết nối WebSocket liên tục và có thể duy trì cho đến khi client hoặc server chủ động đóng.

#### Truyền Tải Dữ Liệu

Sau khi kết nối thiết lập, cả client và server có thể gửi dữ liệu bất kỳ lúc nào thông qua **khung dữ liệu (data frames)**:

- **Text Frames**: Chứa dữ liệu văn bản, thường là JSON.
- **Binary Frames**: Chứa dữ liệu nhị phân như hình ảnh, file, hoặc dữ liệu mã hóa khác.
- **Ping/Pong Frames**: Kiểm tra trạng thái kết nối và giúp duy trì kết nối lâu dài.

#### Đóng Kết Nối

Kết nối WebSocket có thể được đóng lại khi client hoặc server gửi một **Close Frame**, thường chứa mã trạng thái và thông báo lý do đóng kết nối.

### 5. Ưu và Nhược Điểm của WebSocket

#### Ưu Điểm

- **Phản Hồi Nhanh Chóng**: Truyền tải dữ liệu gần như ngay lập tức, rất hữu ích cho ứng dụng cần phản hồi thời gian thực.
- **Tăng Hiệu Suất**: Không phải thiết lập lại kết nối liên tục như HTTP.
- **Tiết Kiệm Băng Thông**: Giảm độ trễ và chi phí băng thông do không phải truyền tải lại thông tin kết nối.

#### Nhược Điểm

- **Tương Thích Kém với Proxy**: Một số proxy HTTP có thể không hỗ trợ WebSocket.
- **Bảo Mật**: Cần các biện pháp bảo mật bổ sung như mã hóa SSL/TLS (dùng wss://) và kiểm tra xác thực.
- **Khó Khăn trong Kiểm Soát Truy Cập**: Khó thực thi chính sách bảo mật và hạn chế truy cập so với HTTP, có thể dẫn đến các vấn đề về bảo mật.

### 6. So Sánh giữa WebSocket và HTTP

| Tiêu chí      | HTTP                                 | WebSocket                               |
| ------------- | ------------------------------------ | --------------------------------------- |
| **Kết nối**   | Tạo mới mỗi yêu cầu                  | Duy trì liên tục                        |
| **Tốc độ**    | Chậm hơn (cần thiết lập kết nối mới) | Nhanh hơn nhờ kết nối liên tục          |
| **Tương tác** | Đơn chiều                            | Hai chiều                               |
| **Ứng dụng**  | Thích hợp cho tải tài nguyên         | Phù hợp cho dữ liệu thời gian thực      |
| **Bảo mật**   | Hỗ trợ SSL/TLS                       | Cần mã hóa bằng SSL/TLS khi dùng wss:// |

### 7. Ứng Dụng Phổ Biến của WebSocket

WebSocket đặc biệt phù hợp cho các ứng dụng yêu cầu dữ liệu thời gian thực, bao gồm:

- **Trò chuyện Trực Tuyến**: Duy trì trò chuyện đồng bộ giữa người dùng.
- **Trò chơi Trực Tuyến**: Cập nhật thời gian thực các hành động của người chơi.
- **Ứng Dụng Giao Dịch Tài Chính**: Truy cập và cập nhật liên tục giá cổ phiếu, tỷ giá tiền tệ.
- **Cập Nhật Trạng Thái**: Thông báo, trạng thái hệ thống hoặc cập nhật trong các hệ thống giám sát.

### 8. Ví Dụ về Yêu Cầu WebSocket

#### Yêu Cầu Handshake (HTTP Request)

Dưới đây là một ví dụ về yêu cầu WebSocket ban đầu từ client:

```http
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
```

#### Phản Hồi Handshake từ Server

Server xác nhận yêu cầu và chuyển sang giao thức WebSocket:

```http
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: HSmrc0sMlYUkAGmm5OPpG2HaGWk=
Sec-WebSocket-Protocol: chat
```

Sau bước này, kết nối giữa client và server trở thành WebSocket và sẵn sàng cho việc truyền tải dữ liệu hai chiều.

### 9. Kết Luận

WebSocket là một giao thức mạnh mẽ và tối ưu cho các ứng dụng yêu cầu kết nối liên tục và dữ liệu thời gian thực. Với khả năng duy trì kết nối hai chiều mà không cần thiết lập lại mỗi lần trao đổi, WebSocket tăng hiệu suất truyền tải, giảm độ trễ và tiết kiệm băng thông, rất hữu ích trong các ứng dụng hiện đại như trò chuyện trực tuyến, trò chơi thời gian thực, và các hệ thống giám sát.
