Session, Cookies, và JWT (JSON Web Token) là ba phương thức phổ biến để quản lý thông tin và trạng thái người dùng trong các ứng dụng web. Mỗi phương pháp có cách tiếp cận riêng để lưu trữ và xác thực, phù hợp với các yêu cầu và kịch bản sử dụng khác nhau.

- **Session và Cookie** là **stateful** vì chúng yêu cầu lưu trữ trạng thái:

  - **Session**: Server lưu trữ thông tin phiên cho từng người dùng, mỗi lần người dùng thực hiện yêu cầu, server kiểm tra session ID và dựa vào đó để truy xuất dữ liệu trạng thái từ bộ nhớ hoặc cơ sở dữ liệu.
  - **Cookie**: Là stateful khi nó lưu trữ trạng thái đăng nhập hoặc các thông tin người dùng cần giữ qua các yêu cầu khác nhau.

- **JWT** là **stateless**:

  - JWT chứa tất cả thông tin người dùng cần thiết trong chính token và server chỉ cần xác thực token đó mà không cần lưu trữ thông tin phiên (state) liên quan đến người dùng. Điều này giúp JWT thích hợp cho các hệ thống phân tán và không trạng thái.

Dưới đây là so sánh chi tiết về cách thức hoạt động, ưu và nhược điểm của từng phương pháp:

| **Tiêu chí**                    | **Session**                                                                                                          | **Cookies**                                                                                                | **JWT (JSON Web Token)**                                                                                    |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Vị trí lưu trữ**              | Lưu trữ trên **server**; chỉ lưu **Session ID** trên client.                                                         | Lưu trữ trực tiếp trên **client** (trong trình duyệt).                                                     | Lưu trữ **token** trên client, thường là trong localStorage hoặc sessionStorage.                            |
| **Cách thức hoạt động**         | Tạo **Session ID** duy nhất cho mỗi phiên người dùng, lưu trên server, và client gửi kèm ID trong cookie.            | Dữ liệu được lưu trực tiếp dưới dạng key-value trong cookie và gửi kèm với mọi yêu cầu HTTP.               | Token bao gồm thông tin người dùng và xác thực, client gửi kèm token với mỗi yêu cầu HTTP.                  |
| **Kiểm tra tính toàn vẹn**      | Không có kiểm tra tự động từ server, nếu session ID bị đánh cắp thì nguy cơ mất thông tin cao.                       | Cookie có thể được mã hóa nhưng nếu không bảo vệ tốt, dễ bị đánh cắp.                                      | JWT sử dụng chữ ký số để đảm bảo tính toàn vẹn của token (Signature).                                       |
| **Tính trạng thái**             | **Có trạng thái**; cần lưu trữ dữ liệu người dùng trên server cho mỗi session.                                       | **Có trạng thái**, nhưng dữ liệu chỉ lưu trên client và được gửi kèm trong mọi yêu cầu.                    | **Không trạng thái**; server không cần lưu trữ dữ liệu người dùng, giảm gánh nặng quản lý trạng thái.       |
| **Quản lý thời gian sống**      | Thời gian sống của session có thể được điều chỉnh trên server; tự động hủy sau một khoảng thời gian không hoạt động. | Có thể thiết lập thời gian sống của cookie (expires) hoặc cookie phiên (tồn tại đến khi đóng trình duyệt). | Có thể đặt thời gian hết hạn trong JWT và sử dụng Refresh Token để lấy JWT mới khi cần.                     |
| **Bảo mật**                     | Tương đối an toàn vì session ID được lưu trên server.                                                                | Cần thiết lập `HttpOnly`, `Secure`, và `SameSite` để bảo mật khỏi các cuộc tấn công XSS và CSRF.           | Bảo mật cao hơn nếu được lưu trữ an toàn và có thể kết hợp với Refresh Token để tránh lộ JWT cũ.            |
| **Khả năng mở rộng**            | Kém linh hoạt trong các hệ thống phân tán (cần lưu session trên nhiều server hoặc trong database).                   | Không thích hợp để lưu dữ liệu nhạy cảm lâu dài, chủ yếu dùng để lưu thông tin phiên người dùng.           | **Thích hợp cho các hệ thống phân tán**; có thể xác thực trên nhiều server mà không cần chia sẻ trạng thái. |
| **Dễ sử dụng trong lập trình**  | Đơn giản để thiết lập và sử dụng, phù hợp với các ứng dụng cần lưu trữ tạm thời.                                     | Dễ thiết lập và tích hợp, phù hợp cho việc lưu trữ trạng thái nhỏ hoặc các tùy chọn của người dùng.        | Phức tạp hơn trong cấu hình ban đầu; phù hợp với các hệ thống RESTful và microservices.                     |
| **Lưu trữ và quản lý dữ liệu**  | Lưu trữ trên server, có thể lưu dữ liệu lớn và phức tạp.                                                             | Lưu trữ trên client, không phù hợp cho dữ liệu lớn hoặc nhạy cảm.                                          | Đóng gói dữ liệu trong JWT; dung lượng nhỏ để dễ truyền tải nhưng khó cập nhật sau khi phát hành.           |
| **Trường hợp sử dụng phổ biến** | Ứng dụng cần lưu trạng thái phức tạp hoặc thông tin nhạy cảm trên server, chẳng hạn như giỏ hàng.                    | Lưu trữ trạng thái đăng nhập ngắn hạn, các tùy chọn người dùng, hoặc thông tin không nhạy cảm khác.        | Xác thực người dùng cho các API RESTful, ứng dụng web/mobile không trạng thái, hệ thống phân tán.           |

### So sánh chi tiết

1. **Session**:

   - **Ưu điểm**: Bảo mật cao hơn vì dữ liệu lưu trên server, dễ quản lý dữ liệu người dùng.
   - **Nhược điểm**: Không phù hợp với các hệ thống phân tán hoặc hệ thống có lượng truy cập lớn, vì cần lưu session trên server.

2. **Cookies**:

   - **Ưu điểm**: Đơn giản để sử dụng và thiết lập. Có thể lưu trữ trạng thái nhẹ và duy trì qua các lần truy cập.
   - **Nhược điểm**: Bảo mật thấp nếu không được cấu hình đúng. Dễ bị lộ nếu không sử dụng `HttpOnly`, `Secure`, và `SameSite` để bảo vệ khỏi XSS, CSRF.

3. **JWT**:
   - **Ưu điểm**: Tính chất không trạng thái, cho phép xác thực nhanh và hiệu quả trong các ứng dụng phân tán. Bảo mật tốt khi sử dụng signature.
   - **Nhược điểm**: Khó thu hồi hoặc vô hiệu hóa token khi bị đánh cắp. Thường cần triển khai thêm cơ chế Refresh Token để gia hạn.
