## Tổng Quan về Giao Thức FTP (File Transfer Protocol)

FTP (File Transfer Protocol) là một giao thức tiêu chuẩn được sử dụng để truyền tải tệp tin giữa client và server trên mạng TCP/IP, đặc biệt là Internet. FTP cho phép người dùng đăng nhập vào một máy chủ từ xa để tải lên, tải xuống, và quản lý tệp tin.

### 1. Định Nghĩa

FTP là một giao thức ứng dụng, được định nghĩa bởi giao thức TCP, cho phép client kết nối đến server và truyền tải các tệp tin với độ tin cậy cao. FTP được sử dụng rộng rãi để chia sẻ tệp tin trong môi trường mạng công cộng và nội bộ, hỗ trợ cả truyền tải dữ liệu dạng văn bản và nhị phân.

### 2. Cấu Trúc URL

FTP sử dụng URL có dạng:

- `ftp://` hoặc `ftps://` khi sử dụng FTP với kết nối bảo mật (FTP Secure).

Ví dụ:

- `ftp://example.com/folder/file.txt`
- `ftps://example.com/folder/file.txt` (sử dụng SSL/TLS)

### 3. Chức Năng Chính

FTP cho phép thực hiện các thao tác cơ bản với tệp tin trên máy chủ từ xa như:

- **Tải xuống (Download)**: Lấy dữ liệu từ server về máy tính client.
- **Tải lên (Upload)**: Gửi dữ liệu từ máy tính client lên server.
- **Quản lý thư mục và tệp tin**: Tạo, xóa thư mục và tệp tin, thay đổi quyền truy cập tệp tin, di chuyển tệp tin.

### 4. Cách FTP Hoạt Động

FTP hoạt động theo mô hình client-server, nghĩa là client khởi tạo yêu cầu và server sẽ đáp ứng lại yêu cầu đó. Có hai chế độ kết nối chính trong FTP:

#### Chế Độ Kết Nối

1. **Active Mode**: Server khởi tạo kết nối ngược lại đến client để truyền dữ liệu. Trong chế độ này, server sử dụng cổng mặc định là 21 cho điều khiển và một cổng động để truyền dữ liệu.

2. **Passive Mode**: Client chịu trách nhiệm mở kết nối dữ liệu đến server. Server chỉ mở cổng để đợi kết nối từ client thay vì chủ động kết nối lại, giúp vượt qua các hạn chế của tường lửa hoặc NAT trên client.

#### Cấu Trúc Kết Nối FTP

FTP sử dụng hai kết nối TCP riêng biệt:

- **Kết nối điều khiển**: Kết nối quản lý các lệnh và phản hồi của server qua cổng TCP 21 (mặc định).
- **Kết nối dữ liệu**: Dùng để truyền dữ liệu, được mở khi cần truyền tệp và đóng lại sau khi hoàn tất.

#### Các Lệnh FTP Thường Dùng

FTP sử dụng các lệnh để thực hiện thao tác với tệp tin và thư mục, như:

- **USER** và **PASS**: Đăng nhập với tên người dùng và mật khẩu.
- **LIST**: Liệt kê các tệp và thư mục.
- **RETR**: Tải xuống tệp từ server.
- **STOR**: Tải lên tệp từ client đến server.
- **DELE**: Xóa tệp trên server.
- **MKD** và **RMD**: Tạo hoặc xóa thư mục trên server.

#### Các Bước Truyền Tải Tệp Tin

1. **Khởi Tạo Kết Nối**: Client kết nối đến server qua cổng TCP 21 để bắt đầu phiên FTP.
2. **Xác Thực Người Dùng**: Server yêu cầu client cung cấp tên người dùng và mật khẩu (hoặc sử dụng chế độ ẩn danh).
3. **Chuyển Dữ Liệu**: Client gửi lệnh để tải lên hoặc tải xuống tệp tin. Server phản hồi và thực hiện quá trình truyền tải thông qua kết nối dữ liệu.
4. **Đóng Kết Nối**: Sau khi truyền tải hoàn tất, kết nối dữ liệu sẽ được đóng. Phiên điều khiển cũng đóng khi client thoát khỏi server.

### 5. Bảo Mật trong FTP

#### FTP Ẩn Danh (Anonymous FTP)

FTP hỗ trợ chế độ ẩn danh, cho phép người dùng kết nối và truy cập một số tệp tin công khai mà không cần đăng nhập bằng tên người dùng và mật khẩu.

#### FTPS và SFTP

Vì FTP ban đầu không có mã hóa, nó dễ bị tấn công trong mạng công cộng. Có hai giải pháp tăng cường bảo mật:

- **FTPS (FTP Secure)**: Sử dụng SSL/TLS để mã hóa kết nối FTP, bảo vệ dữ liệu khỏi bị đánh cắp.
- **SFTP (SSH File Transfer Protocol)**: Chạy qua giao thức SSH, cung cấp mã hóa và các tính năng bảo mật mạnh mẽ, được sử dụng rộng rãi hơn trong truyền tải dữ liệu an toàn.

### 6. Ưu và Nhược Điểm của FTP

#### Ưu Điểm

- **Đơn Giản và Hiệu Quả**: Dễ triển khai và truyền tải tệp tin nhanh chóng qua kết nối TCP.
- **Hỗ Trợ Tệp Tin Lớn**: Có khả năng truyền tải các tệp có kích thước lớn, không giới hạn dung lượng.
- **Tương Thích Nhiều Hệ Thống**: FTP có thể hoạt động trên hầu hết các hệ điều hành, từ Windows đến UNIX/Linux.

#### Nhược Điểm

- **Bảo Mật Kém**: FTP nguyên bản không mã hóa dữ liệu, bao gồm cả tên người dùng và mật khẩu.
- **Thiếu Linh Hoạt với Tường Lửa**: Chế độ Active FTP gặp khó khăn khi hoạt động qua các thiết bị NAT hoặc tường lửa.
- **Bị Thay Thế Bởi Các Giao Thức An Toàn Hơn**: Với sự phát triển của các giao thức bảo mật hơn như SFTP và FTPS, FTP ngày càng ít được sử dụng cho các ứng dụng yêu cầu bảo mật cao.

### 7. So Sánh giữa FTP, FTPS và SFTP

| Tiêu chí                 | FTP                             | FTPS                            | SFTP                                  |
| ------------------------ | ------------------------------- | ------------------------------- | ------------------------------------- |
| **Bảo mật**              | Không mã hóa                    | Mã hóa bằng SSL/TLS             | Mã hóa thông qua SSH                  |
| **Cổng mặc định**        | 21 (điều khiển), 20 (dữ liệu)   | 21 hoặc 990                     | 22                                    |
| **Khả năng tương thích** | Nhiều hệ điều hành              | Nhiều hệ điều hành              | Nhiều hệ điều hành                    |
| **Truyền tải dữ liệu**   | Truyền theo hai kênh riêng biệt | Truyền theo hai kênh riêng biệt | Truyền trên một kênh duy nhất qua SSH |
| **Ứng dụng**             | Thích hợp chia sẻ tệp công khai | Sử dụng cho dữ liệu cần mã hóa  | Thích hợp cho dữ liệu cần bảo mật cao |

### 8. Ứng Dụng Phổ Biến của FTP

FTP thường được dùng cho các mục đích sau:

- **Lưu Trữ và Chia Sẻ Tệp Công Khai**: Tải lên và tải xuống các tệp tin từ máy chủ công cộng.
- **Quản Lý Nội Dung Website**: Dùng để cập nhật, tải lên tệp HTML, hình ảnh hoặc các nội dung khác cho trang web.
- **Sao Lưu Dữ Liệu**: Được dùng trong việc lưu trữ và truyền tải bản sao lưu giữa các hệ thống.

### 9. Ví Dụ về Kết Nối và Giao Thức FTP

#### Yêu Cầu Kết Nối và Đăng Nhập

```plaintext
USER username
PASS password
```

#### Liệt Kê Tệp và Tải Xuống Tệp

```plaintext
LIST
RETR example.txt
```

#### Tải Lên Tệp và Đóng Kết Nối

```plaintext
STOR uploadfile.txt
QUIT
```

### 10. Kết Luận

FTP là giao thức truyền tải tệp tin phổ biến và tiện dụng, đặc biệt khi cần di chuyển các tệp lớn và không yêu cầu bảo mật cao. Tuy nhiên, với sự phát triển của các giao thức an toàn như FTPS và SFTP, FTP dần ít được sử dụng cho các ứng dụng yêu cầu bảo mật. Đối với các ứng dụng cần mã hóa dữ liệu, việc sử dụng FTPS hoặc SFTP sẽ phù hợp hơn, trong khi FTP vẫn hữu ích cho các trường hợp truyền tải tệp công khai hoặc nội bộ không đòi hỏi độ bảo mật cao.
