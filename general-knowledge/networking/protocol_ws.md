### 1. Cách WebSocket Sử Dụng TCP

WebSocket sử dụng kết nối **TCP** để truyền tải dữ liệu giữa client và server. Cụ thể, quá trình truyền tải WebSocket được xây dựng trên nền tảng TCP/IP, vì vậy nó đảm bảo tính ổn định và đáng tin cậy khi truyền dữ liệu, đặc biệt là khi cần duy trì kết nối lâu dài trong các ứng dụng yêu cầu trao đổi dữ liệu liên tục.

#### Quá Trình Sử Dụng TCP trong WebSocket:

1. **Kết nối TCP**: Khi client muốn kết nối đến WebSocket server, đầu tiên một kết nối TCP sẽ được thiết lập. WebSocket sử dụng cổng mặc định là **80 (ws)** cho các kết nối không bảo mật và **443 (wss)** cho các kết nối bảo mật.

2. **Handshake HTTP**: Trước khi chuyển sang WebSocket, client gửi yêu cầu "Upgrade" HTTP (HandShake) đến server. Trong yêu cầu này, client thông báo server rằng nó muốn nâng cấp kết nối HTTP hiện tại sang WebSocket. Đây là bước đầu tiên để WebSocket sử dụng TCP làm phương tiện truyền tải.

3. **Chuyển đổi giao thức**: Sau khi server nhận yêu cầu và đồng ý, kết nối HTTP ban đầu sẽ chuyển thành kết nối WebSocket. Lúc này, một kênh truyền thông hai chiều thông qua TCP được duy trì mở, giúp client và server có thể giao tiếp mà không cần phải thiết lập lại kết nối mỗi lần.

4. **Truyền tải dữ liệu qua TCP**: Sau khi quá trình Handshake thành công, WebSocket sử dụng các khung dữ liệu (frames) để truyền tải thông tin hai chiều giữa client và server, thông qua kết nối TCP hiện tại. WebSocket cho phép gửi dữ liệu ở cả định dạng văn bản (text) và nhị phân (binary), cũng như thực hiện các kiểm tra trạng thái với các khung Ping/Pong.

5. **Kết thúc kết nối**: Khi không còn nhu cầu truyền tải dữ liệu nữa, kết nối WebSocket có thể được đóng lại bằng cách gửi một khung Close, sau đó kết nối TCP sẽ được đóng.

### 2. Cấu Trúc Dữ Liệu WebSocket

Khi một kết nối WebSocket đã được thiết lập, dữ liệu được truyền tải thông qua các **frames** (khung dữ liệu). Mỗi frame này có thể chứa dữ liệu văn bản hoặc nhị phân và được phân thành các phần nhỏ để có thể truyền tải hiệu quả qua mạng.

#### Các Loại WebSocket Frames:

1. **Text Frame**: Dữ liệu trong khung này là văn bản (thường là JSON, nhưng có thể là bất kỳ dữ liệu văn bản nào). WebSocket sử dụng mã hóa UTF-8 để truyền tải văn bản.
2. **Binary Frame**: Dữ liệu trong khung này là dạng nhị phân, có thể là hình ảnh, video, hoặc các tệp dữ liệu khác. WebSocket hỗ trợ hai định dạng nhị phân chính:

   - **Blob**: Dữ liệu lớn, không cần phải chuyển đổi thành mã ký tự.
   - **ArrayBuffer**: Một bộ nhớ được phân bổ trực tiếp trong trình duyệt, hỗ trợ thao tác trực tiếp với dữ liệu nhị phân.

3. **Ping/Pong Frame**: Đây là khung dữ liệu được dùng để kiểm tra trạng thái kết nối. Khung Ping được gửi từ client hoặc server, và khung Pong là phản hồi từ đối phương, đảm bảo kết nối không bị gián đoạn.

4. **Close Frame**: Khi một bên (client hoặc server) muốn kết thúc kết nối, họ sẽ gửi một khung Close. Khung này có thể chứa mã trạng thái, cho biết lý do đóng kết nối.

#### Cấu trúc khung WebSocket:

- **Fin (1 bit)**: Cho biết liệu đây có phải là frame cuối cùng không.
- **RSV1, RSV2, RSV3 (1 bit mỗi)**: Dùng cho các mở rộng (extensions).
- **Opcode (4 bit)**: Xác định loại frame (ví dụ: văn bản, nhị phân, Ping/Pong, Close).
- **Payload length (7 bits hoặc 7-64 bit)**: Kích thước của dữ liệu trong frame.
- **Mask (1 bit)**: Xác định liệu dữ liệu có bị mã hóa (mask) không.
- **Payload Data**: Dữ liệu thực tế được truyền tải.

### 3. Các Ưu Điểm và Hạn Chế Khác

#### Ưu Điểm:

- **Hiệu quả trong truyền thông thời gian thực**: Nhờ tính năng duy trì kết nối và truyền tải dữ liệu không đồng bộ, WebSocket rất phù hợp cho các ứng dụng như trò chuyện trực tuyến, chơi game, các dịch vụ tài chính cần cập nhật nhanh chóng.
- **Giảm độ trễ**: Do không phải liên tục thiết lập kết nối mới như HTTP, WebSocket giúp giảm độ trễ trong giao tiếp giữa client và server.
- **Tiết kiệm tài nguyên mạng**: WebSocket chỉ cần một kết nối duy nhất để truyền tải tất cả các dữ liệu mà không phải thực hiện các yêu cầu và phản hồi HTTP liên tục.

#### Hạn Chế:

- **Quản lý kết nối phức tạp hơn**: Vì WebSocket giữ kết nối mở, việc quản lý nhiều kết nối đồng thời có thể trở nên phức tạp đối với các server với khối lượng người dùng lớn.
- **Tính tương thích của proxy và firewall**: Một số proxy và firewall không hỗ trợ WebSocket hoặc có thể chặn các kết nối WebSocket không bảo mật. Điều này đòi hỏi việc cấu hình lại để hỗ trợ.
- **Khó khăn trong bảo mật**: WebSocket cần mã hóa bằng SSL/TLS (wss://) để đảm bảo bảo mật. Tuy nhiên, việc sử dụng WebSocket qua các mạng không bảo mật vẫn là một mối lo ngại lớn.

### 4. WebSocket và Các Giao Thức Liên Quan

#### WebSocket và HTTP:

WebSocket được thiết kế để khắc phục các hạn chế của HTTP khi cần giao tiếp hai chiều và duy trì kết nối mở lâu dài. HTTP, mặc dù rất mạnh mẽ trong việc truy xuất tài nguyên tĩnh (như trang web, hình ảnh, CSS), lại không thích hợp cho các ứng dụng yêu cầu trao đổi dữ liệu liên tục, như trò chuyện trực tuyến hoặc cập nhật thông tin thời gian thực.

#### WebSocket và MQTT:

WebSocket và MQTT đều là các giao thức truyền thông thời gian thực, nhưng MQTT được tối ưu hóa cho các ứng dụng IoT và các hệ thống nhúng có băng thông thấp hoặc yêu cầu truyền tải dữ liệu trong điều kiện mạng không ổn định. WebSocket, ngược lại, được sử dụng chủ yếu trong môi trường web và các ứng dụng yêu cầu độ trễ thấp và truyền tải dữ liệu lớn.

#### WebSocket và WebRTC:

WebSocket và WebRTC đều hỗ trợ giao tiếp thời gian thực, nhưng WebRTC chủ yếu được sử dụng cho truyền thông video và âm thanh trực tiếp giữa các client mà không cần phải qua server, trong khi WebSocket chủ yếu xử lý việc truyền tải dữ liệu giữa client và server.

### 5. Kết Luận

WebSocket là một giao thức cực kỳ mạnh mẽ và linh hoạt, được tối ưu hóa cho các ứng dụng cần dữ liệu thời gian thực và kết nối lâu dài giữa client và server. Với khả năng truyền tải dữ liệu hai chiều liên tục qua kết nối TCP, WebSocket đang ngày càng trở thành lựa chọn hàng đầu trong các ứng dụng web hiện đại, như trò chuyện trực tuyến, các trò chơi trực tuyến, và các ứng dụng giám sát.

Tuy nhiên, cũng cần lưu ý rằng việc triển khai WebSocket đòi hỏi phải quản lý các kết nối tốt hơn và bảo mật thông qua SSL/TLS để bảo vệ dữ liệu truyền tải. Do đó, các nhà phát triển cần phải xem xét đầy đủ các yếu tố về bảo mật, tài nguyên mạng, và hiệu suất khi sử dụng WebSocket trong ứng dụng của mình.
