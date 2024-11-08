### FTP và Cách Nó Sử Dụng TCP/IP Để Truyền Tải Dữ Liệu

FTP (File Transfer Protocol) là một giao thức truyền tải tệp tin được thiết kế để truyền dữ liệu giữa client và server trong môi trường mạng TCP/IP, đặc biệt là trên Internet. Giao thức này hoạt động trên nguyên lý của mô hình client-server, trong đó client gửi yêu cầu đến server và server đáp ứng các yêu cầu đó, chủ yếu là việc truyền tải các tệp tin.

Để hiểu rõ hơn về cách FTP sử dụng TCP/IP để truyền tải dữ liệu, chúng ta cần phân tích chi tiết các yếu tố sau: **cấu trúc giao thức**, **các kết nối TCP/IP** và **các bước truyền tải dữ liệu**.

### 1. **Cấu Trúc FTP trên TCP/IP**

FTP hoạt động trên tầng ứng dụng của mô hình OSI và sử dụng giao thức TCP (Transmission Control Protocol) để thiết lập kết nối đáng tin cậy giữa client và server. TCP là một giao thức kết nối có bảo đảm, đảm bảo rằng các gói dữ liệu được gửi đi sẽ đến đích một cách chính xác và theo đúng thứ tự.

Khi FTP được sử dụng để truyền tải dữ liệu, nó tận dụng hai kết nối TCP riêng biệt:

- **Kết nối điều khiển (Control Connection)**: Đây là kết nối được sử dụng để gửi các lệnh FTP giữa client và server, chẳng hạn như yêu cầu đăng nhập, liệt kê tệp tin, hoặc tải lên/tải xuống tệp. Kết nối này sử dụng cổng TCP 21 (cổng mặc định).
- **Kết nối dữ liệu (Data Connection)**: Khi cần truyền tải tệp tin hoặc thông tin cụ thể (như danh sách tệp), FTP mở một kết nối dữ liệu riêng biệt. Cổng được sử dụng cho kết nối này có thể thay đổi tùy thuộc vào chế độ kết nối (Active Mode hoặc Passive Mode).

### 2. **Các Chế Độ Kết Nối trong FTP**

FTP có hai chế độ kết nối chính, cả hai đều sử dụng TCP/IP nhưng có sự khác biệt trong cách thức mở kết nối dữ liệu:

#### **Chế Độ Active (Active Mode)**

- **Kết nối điều khiển**: Client kết nối tới server qua cổng TCP 21.
- **Kết nối dữ liệu**: Sau khi nhận được yêu cầu từ client, server sẽ mở một kết nối ngược lại tới client để truyền tải dữ liệu, thường qua một cổng ngẫu nhiên được chọn từ khoảng 1024 đến 65535.

**Lưu ý về Active Mode**: Khi FTP hoạt động ở chế độ Active, client phải cho phép server mở kết nối ngược lại, điều này có thể gặp khó khăn khi có tường lửa hoặc NAT (Network Address Translation) trên client, bởi vì các kết nối ngược lại có thể bị chặn.

#### **Chế Độ Passive (Passive Mode)**

- **Kết nối điều khiển**: Vẫn sử dụng cổng TCP 21 để thiết lập kết nối điều khiển.
- **Kết nối dữ liệu**: Thay vì server chủ động mở kết nối ngược lại, trong chế độ Passive, client sẽ yêu cầu server mở một cổng dữ liệu, và client sẽ chủ động kết nối tới cổng đó để truyền tải dữ liệu.

**Lưu ý về Passive Mode**: Passive Mode rất hữu ích khi client nằm sau tường lửa hoặc NAT, vì nó giúp client kiểm soát kết nối dữ liệu thay vì phải chấp nhận kết nối từ server.

### 3. **Cấu Trúc Kết Nối trong FTP**

FTP sử dụng hai kết nối TCP độc lập:

1. **Kết nối điều khiển (Control Connection)**:

   - Kết nối này được mở khi client kết nối tới server qua cổng TCP 21.
   - Kết nối điều khiển duy trì trong suốt phiên làm việc và chỉ được đóng khi client kết thúc phiên làm việc (ví dụ, khi thực hiện lệnh `QUIT`).
   - Các lệnh FTP (như `USER`, `PASS`, `LIST`, `RETR`, `STOR`, `DELE`, v.v.) đều được gửi qua kết nối này.

2. **Kết nối dữ liệu (Data Connection)**:
   - Kết nối này được mở khi cần truyền tải tệp tin hoặc dữ liệu (như danh sách tệp).
   - Trong chế độ Active, server sẽ chủ động mở kết nối này tới client.
   - Trong chế độ Passive, client sẽ kết nối tới server để truyền tải dữ liệu.
   - Sau khi truyền tải dữ liệu hoàn tất, kết nối dữ liệu sẽ được đóng.

### 4. **Quy Trình Truyền Tải Dữ Liệu qua FTP**

Khi một client kết nối đến một FTP server để tải lên hoặc tải xuống tệp tin, các bước giao tiếp giữa client và server diễn ra theo quy trình sau:

#### **Bước 1: Khởi Tạo Kết Nối**

- Client mở kết nối TCP tới cổng 21 của server.
- Server phản hồi với thông báo chào mừng (ví dụ: `220 Welcome to FTP Server`).

#### **Bước 2: Đăng Nhập**

- Client gửi lệnh `USER` và `PASS` để đăng nhập vào server, cung cấp tên người dùng và mật khẩu (hoặc sử dụng chế độ ẩn danh).
- Server kiểm tra thông tin đăng nhập và phản hồi (ví dụ: `230 User logged in, proceed`).

#### **Bước 3: Chuyển Dữ Liệu**

- Sau khi đăng nhập thành công, client có thể yêu cầu các thao tác như liệt kê thư mục (`LIST`), tải xuống tệp (`RETR`) hoặc tải lên tệp (`STOR`).
- Mỗi yêu cầu này sẽ được gửi qua kết nối điều khiển.
- Khi cần truyền tải tệp tin, kết nối dữ liệu sẽ được mở. Client hoặc server (tùy chế độ) sẽ tạo kết nối này để truyền tải tệp.
- Sau khi truyền tải hoàn tất, kết nối dữ liệu sẽ được đóng.

#### **Bước 4: Đóng Kết Nối**

- Khi quá trình truyền tải tệp tin hoặc các thao tác FTP khác hoàn tất, client sẽ gửi lệnh `QUIT` để kết thúc phiên làm việc.
- Kết nối điều khiển và dữ liệu sẽ được đóng, kết thúc phiên FTP.

### 5. **Lệnh FTP và Sử Dụng TCP/IP**

Các lệnh FTP cơ bản mà client và server sử dụng đều được gửi qua kết nối điều khiển TCP (cổng 21). Dưới đây là một số lệnh và các tương tác cơ bản:

- **USER <username>**: Gửi tên người dùng cho server.
- **PASS <password>**: Gửi mật khẩu cho server.
- **LIST**: Liệt kê các thư mục và tệp tin trong thư mục hiện tại.
- **RETR <filename>**: Tải xuống tệp từ server.
- **STOR <filename>**: Tải lên tệp từ client tới server.
- **DELE <filename>**: Xóa tệp trên server.
- **QUIT**: Kết thúc phiên làm việc FTP.

### 6. **Bảo Mật trong FTP**

FTP không mã hóa dữ liệu, vì vậy thông tin như mật khẩu và dữ liệu truyền tải đều có thể bị nghe lén nếu không sử dụng các cơ chế bảo mật bổ sung. Một số giao thức mở rộng bảo mật cho FTP bao gồm:

- **FTPS (FTP Secure)**: Sử dụng SSL/TLS để mã hóa kết nối FTP, bảo vệ dữ liệu trong quá trình truyền tải.
- **SFTP (SSH File Transfer Protocol)**: Không phải là FTP thực sự, nhưng sử dụng giao thức SSH để bảo mật kết nối và mã hóa dữ liệu.

### Kết luận

FTP là một giao thức mạnh mẽ và hiệu quả cho việc truyền tải tệp tin, hoạt động trên nền tảng TCP/IP với kết nối điều khiển và dữ liệu riêng biệt. Mặc dù có những hạn chế về bảo mật, FTP vẫn là một công cụ quan trọng cho việc chia sẻ và quản lý tệp tin, đặc biệt khi không yêu cầu mã hóa cao. Tuy nhiên, khi bảo mật là ưu tiên, các giao thức thay thế như FTPS hoặc SFTP sẽ được ưu tiên sử dụng.
