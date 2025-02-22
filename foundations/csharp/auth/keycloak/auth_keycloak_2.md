**1. Người dùng truy cập ứng dụng.**

*   Đây là điểm khởi đầu, khi người dùng muốn sử dụng ứng dụng của bạn. Ứng dụng nhận ra rằng người dùng chưa được xác thực hoặc cần quyền truy cập vào tài nguyên được bảo vệ.

**2. Ứng dụng redirect đến Keycloak để đăng nhập:**

```bash
GET http://localhost:8080/realms/myrealm/protocol/openid-connect/auth?client_id=myclient&redirect_uri=http://localhost:3000/callback&response_type=code
```

*   **Authorization Request**: Ứng dụng tạo một yêu cầu ủy quyền (Authorization Request) và chuyển hướng trình duyệt của người dùng đến Authorization Endpoint của Keycloak (thường là `/auth`).
*   **Các tham số quan trọng**:
    *   `client_id`:  Định danh duy nhất của ứng dụng (Client) đã được đăng ký trong Keycloak.
    *   `redirect_uri`: URI mà Keycloak sẽ chuyển hướng trình duyệt người dùng trở lại ứng dụng sau khi xác thực và ủy quyền thành công. URI này phải khớp với một trong các Redirect URI đã được cấu hình cho Client trong Keycloak.
    *   `response_type=code`:  Chỉ định rằng ứng dụng muốn sử dụng Authorization Code Grant flow. Keycloak sẽ trả về Authorization Code.
*   **Keycloak Authorization Endpoint**:  URL này là điểm mà ứng dụng gửi yêu cầu ủy quyền đến Keycloak. Nó bao gồm realm (`myrealm`) và giao thức (`openid-connect`).

**3. Sau khi đăng nhập, Keycloak redirect về ứng dụng kèm theo code.**

*   **Xác thực và Ủy quyền tại Keycloak**:  Keycloak sẽ hiển thị trang đăng nhập cho người dùng (nếu chưa đăng nhập). Sau khi người dùng đăng nhập thành công (xác thực), Keycloak sẽ hiển thị trang "consent" (đồng ý) nếu ứng dụng yêu cầu phạm vi (scopes) truy cập dữ liệu người dùng.
*   **Authorization Code Callback**: Nếu người dùng đồng ý ủy quyền, Keycloak sẽ chuyển hướng trình duyệt người dùng trở lại `redirect_uri` mà ứng dụng đã cung cấp.
*   **`code` parameter**:  Quan trọng nhất, Keycloak sẽ đính kèm **Authorization Code** vào URL callback dưới dạng query parameter: `http://localhost:3000/callback?code=<CODE_NHAN_DUOC>`.  Authorization Code này là "vé" tạm thời để ứng dụng đổi lấy Access Token.

**4. Ứng dụng gọi API lấy Access Token:**

```sh
POST http://localhost:8080/realms/myrealm/protocol/openid-connect/token
Content-Type: application/x-www-form-urlencoded
---
client_id=myclient
client_secret=mysecret
grant_type=authorization_code
code=<CODE_NHAN_DUOC>
redirect_uri=http://localhost:3000/callback
```

*   **Token Request**: Ứng dụng thực hiện một yêu cầu POST **back-channel** (server-to-server) trực tiếp đến Token Endpoint của Keycloak (thường là `/token`). **Lưu ý**:  Yêu cầu này **không thông qua trình duyệt web** của người dùng.
*   **Content-Type**: `application/x-www-form-urlencoded` là định dạng chuẩn cho Token Request.
*   **Các tham số quan trọng trong body**:
    *   `client_id` và `client_secret`:  Thông tin xác thực của ứng dụng (Client Credentials). `client_secret` cần được giữ bí mật và chỉ sử dụng ở backend server của ứng dụng, **không bao giờ ở frontend client-side code**.
    *   `grant_type=authorization_code`:  Chỉ định rằng ứng dụng đang sử dụng Authorization Code Grant flow và muốn đổi Authorization Code lấy tokens.
    *   `code=<CODE_NHAN_DUOC>`:  Authorization Code mà ứng dụng đã nhận được từ bước 3.
    *   `redirect_uri=http://localhost:3000/callback`:  `redirect_uri` phải khớp với `redirect_uri` đã sử dụng trong Authorization Request ở bước 2. Điều này giúp Keycloak xác minh tính hợp lệ của yêu cầu.
*   **Keycloak Token Endpoint**: URL này là điểm mà ứng dụng gửi Authorization Code và Client Credentials để đổi lấy tokens.

**5. Nhận được Access Token, ứng dụng dùng nó để gọi API:**

```sh
GET http://localhost:8080/realms/myrealm/protocol/openid-connect/userinfo
Authorization: Bearer <ACCESS_TOKEN>
```

*   **Protected Resource Access**: Ứng dụng đã nhận được **Access Token** từ bước 4. Bây giờ ứng dụng có thể sử dụng Access Token này để truy cập các tài nguyên được bảo vệ (ví dụ: APIs, dữ liệu người dùng) trên Resource Server (trong trường hợp này, `userinfo` endpoint của Keycloak có thể được xem như Resource Server cung cấp thông tin người dùng).
*   **Authorization Header**:  Access Token thường được gửi trong header `Authorization` với lược đồ `Bearer`.  Đây là cách phổ biến nhất để truyền Access Token trong các yêu cầu HTTP API.
*   **Resource Server Validation**: Khi Resource Server nhận được yêu cầu API kèm Access Token, nó sẽ **xác minh tính hợp lệ** của Access Token (ví dụ: chữ ký, thời gian hết hạn, issuer) với Authorization Server (Keycloak) hoặc bằng cách kiểm tra JWT Access Token cục bộ (nếu cấu hình). Nếu Access Token hợp lệ và có đủ quyền hạn (scopes), Resource Server sẽ cho phép truy cập tài nguyên.
*   **`userinfo` Endpoint**: Trong ví dụ của bạn, bạn sử dụng `userinfo` endpoint. Đây là một endpoint chuẩn của OpenID Connect, cung cấp thông tin về người dùng đã xác thực (claims).

**Điểm Nhấn Quan Trọng:**

*   **Authorization Code Grant Flow**:  Đây là luồng được **khuyến nghị** cho ứng dụng web server-side vì tính bảo mật cao.
*   **Back-channel vs. Front-channel**:  Bước 4 (Token Request) là **back-channel** (server-to-server), không thông qua trình duyệt, giúp bảo mật `client_secret`. Các bước 1-3 (Authorization Request và Callback) là **front-channel** (thông qua trình duyệt).
*   **Client Secret Security**:  Việc bảo mật `client_secret` là **vô cùng quan trọng**. Không bao giờ để lộ `client_secret` ở client-side code.
*   **Access Token and Resource Access**: Access Token là "vé" tạm thời để ứng dụng truy cập tài nguyên. Ứng dụng phải gửi Access Token trong mỗi yêu cầu đến Resource Server để chứng minh quyền truy cập.

