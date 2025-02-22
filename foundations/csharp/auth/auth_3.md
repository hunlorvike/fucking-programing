# Chương 3: Authorization - " 'Phân Quyền' " Truy Cập Tài Nguyên - " 'Được Phép Làm Gì' " Khi " 'Đã Xác Thực' "?" - " 'Bản Đồ' " "Phân Quyền", " 'Đi' " Theo " 'Lối' " Nào Để " 'Bảo Mật' " và " 'Linh Hoạt' "?

Chào mừng bạn đến với **Chương 3: Authorization - " 'Phân Quyền' " Truy Cập Tài Nguyên"**! Sau khi đã "vượt qua" "cửa ải" **Authentication** ( " 'Xác Minh' " Danh Tính - " 'Ai' " "đang gõ cửa"?), chúng ta sẽ "bước vào" thế giới **Authorization** ( " 'Phân Quyền' " Truy Cập - " 'Được Phép Làm Gì' " khi " 'đã vào' "?). Trong chương này, chúng ta sẽ "khám phá" các **"mô hình" Authorization "phổ biến"** nhất (Role-Based Access Control - RBAC, Attribute-Based Access Control - ABAC, Policy-Based Authorization) và "học cách" **"chọn"** "mô hình" Authorization **"phù hợp"** để "xây dựng" " 'bản đồ' " "phân quyền" "hiệu quả" và "linh hoạt" cho ứng dụng của bạn.

**Phần 3: Authorization - " 'Phân Quyền' " Truy Cập Tài Nguyên - " 'Được Phép Làm Gì' " Khi " 'Đã Xác Thực' "?"**

**3.1. Các "mô hình" Authorization "phổ biến" (Role-Based Access Control - RBAC, Attribute-Based Access Control - ABAC, Policy-Based Authorization) - " 'Bản Đồ' " "Phân Quyền" - " 'Chọn' " "Lối Đi" Nào Cho " 'Ứng Dụng' "?**

-   **" 'Bản Đồ' " "Phân Quyền" - " 'Muôn Nẻo Đường' ", " 'Chọn' " "Lối" Nào Cho " 'Phù Hợp' "?"**:

    -   **Authorization** (Ủy Quyền) là "nghệ thuật" **" 'phân quyền' "** truy cập tài nguyên, "kiểm soát" **"ai"** (người dùng "đã xác thực") được **" 'phép làm gì' "** (what actions are allowed) đối với **"tài nguyên"** nào (which resources). "Lựa chọn" "mô hình" Authorization "phù hợp" "quyết định" **" 'bản đồ' " "phân quyền"** của ứng dụng, "ảnh hưởng" đến "tính 'bảo mật' ", "tính 'linh hoạt' ", và "khả năng 'quản lý' " của hệ thống.
    -   "Không có" "mô hình" Authorization nào là **" 'vạn năng' "**. "Mỗi 'mô hình' " có "ưu điểm", "nhược điểm" riêng. "Cần" "hiểu rõ" "bản chất" của từng "mô hình" và "chọn" "mô hình" "phù hợp nhất" với "yêu cầu" và "đặc điểm" của ứng dụng của bạn.

-   **"Các 'Mô Hình' " Authorization "Phổ Biến" Nhất:**

    -   **Role-Based Access Control (RBAC) - " 'Phân Quyền' " Dựa Trên " 'Vai Trò' " - " 'Chức Danh' " "Quyền Lực"**:
        -   **"Mô tả":** "Mô hình" Authorization **"phổ biến"** và **"đơn giản"** nhất. "Phân quyền" truy cập tài nguyên dựa trên **"vai trò"** (role) của người dùng trong ứng dụng. "Vai trò" là **" 'nhóm quyền hạn' "** (collection of permissions) được "gán" cho người dùng (ví dụ: "Admin", "Editor", "Viewer", "User", "Guest", v.v.). "Người dùng" được "gán" vào **"một hoặc nhiều" "vai trò"**. "Quyền truy cập" vào tài nguyên được "quyết định" bởi **"vai trò"** của người dùng.
        -   **"Ví dụ RBAC":**
            -   "Người dùng" có **"vai trò" "Admin"** có "quyền" "truy cập" **"mọi chức năng"** (ví dụ: "quản lý người dùng", "quản lý sản phẩm", "quản lý đơn hàng", v.v.).
            -   "Người dùng" có **"vai trò" "Editor"** có "quyền" "truy cập" **"chức năng" "biên tập nội dung"** (ví dụ: "tạo bài viết", "sửa bài viết", "xóa bài viết").
            -   "Người dùng" có **"vai trò" "Viewer"** có "quyền" "truy cập" **"chức năng" "xem nội dung"** (ví dụ: "đọc bài viết", "xem sản phẩm").
            -   "Người dùng" có **"vai trò" "User"** có "quyền" "truy cập" **"chức năng" "cá nhân"** (ví dụ: "xem profile", "sửa profile", "đặt hàng").
            -   "Người dùng" có **"vai trò" "Guest"** (khách) có "quyền" "truy cập" **"chức năng" "công cộng"** (ví dụ: "xem trang chủ", "xem danh sách sản phẩm").

        -   **"Ưu điểm RBAC":**
            -   **"Đơn giản" và "dễ hiểu"**: "Dễ dàng" "thiết kế", "triển khai", và "quản lý". "Phù hợp" cho các ứng dụng có "cấu trúc" "phân quyền" **"tĩnh"** và **"rõ ràng"**.
            -   **"Quản lý" "vai trò" "tập trung"**: "Dễ dàng" "quản lý" "quyền hạn" bằng cách "quản lý" **"vai trò"**. "Thay đổi" "quyền hạn" của "vai trò" sẽ "ảnh hưởng" đến "tất cả" "người dùng" "thuộc" "vai trò" đó.
            -   **"Hiệu quả" cho "phần lớn" ứng dụng web**: RBAC đáp ứng được "yêu cầu" "phân quyền" của "nhiều" ứng dụng web thông thường.

        -   **"Nhược điểm RBAC":**
            -   **"Kém 'linh hoạt' " trong "phân quyền" "chi tiết"**: RBAC "khó" "xử lý" các "yêu cầu" "phân quyền" "phức tạp" và "tùy biến" cao, "dựa trên" **"nhiều 'tiêu chí' "** "khác nhau" (không chỉ "vai trò"). Ví dụ: "chỉ cho phép" "Editor" "sửa bài viết" **"của chính mình"**, "không cho phép" "sửa bài viết" "của người khác". RBAC "khó" "thể hiện" "quy tắc" "phân quyền" "dạng này" một cách "trực tiếp".
            -   **"Khó 'mở rộng' " khi "số lượng" "vai trò" và "quyền hạn" "tăng lên"**: Khi ứng dụng "phát triển" và "số lượng" "vai trò" và "quyền hạn" "tăng lên", "ma trận" "phân quyền" (role-permission matrix) trở nên **"cồng kềnh"** và **"khó 'quản lý' "**.
            -   **"Không 'phù hợp' " cho "phân quyền" "động" và "theo ngữ cảnh"**: RBAC "khó" "xử lý" các "yêu cầu" "phân quyền" "thay đổi" "dựa trên" **"ngữ cảnh"** (context) "hiện tại" (ví dụ: "thời gian", "địa điểm", "trạng thái" "tài nguyên", v.v.).

    -   **Attribute-Based Access Control (ABAC) - " 'Phân Quyền' " Dựa Trên " 'Thuộc Tính' " - " 'Đặc Điểm' " "Quyết Định" "Quyền Hạn"**:
        -   **"Mô tả":** "Mô hình" Authorization **"linh hoạt"** và **"mạnh mẽ"** hơn RBAC. "Phân quyền" truy cập tài nguyên dựa trên **"thuộc tính"** (attribute) của **"người dùng"**, **"tài nguyên"**, **"hành động"**, và **"môi trường"** (context). "Thuộc tính" là **" 'đặc điểm' "**, **" 'tính chất' "**, hoặc **" 'thông tin' "** "mô tả" các "thành phần" "tham gia" vào quá trình "phân quyền". "Quyền truy cập" được "quyết định" bởi **"các 'quy tắc' " "phân quyền"** (authorization rules) được "định nghĩa" **"dựa trên" "các 'thuộc tính' "**.
        -   **"Các 'Loại' " "Thuộc Tính" Trong ABAC:**
            -   **User Attributes (Thuộc tính người dùng):** "Thuộc tính" "mô tả" "đặc điểm" của "người dùng" (ví dụ: "vai trò" (role), "chức vụ", "phòng ban", "tuổi", "giới tính", "địa chỉ", "level thành viên", "quyền hạn" "đặc biệt", "thời gian làm việc", v.v.).
            -   **Resource Attributes (Thuộc tính tài nguyên):** "Thuộc tính" "mô tả" "đặc điểm" của "tài nguyên" được "truy cập" (ví dụ: "loại tài liệu", "tính bảo mật" (confidentiality level), "chủ sở hữu", "người tạo", "thời gian tạo", "trạng thái" (draft, published), "vị trí địa lý", v.v.).
            -   **Action Attributes (Thuộc tính hành động):** "Thuộc tính" "mô tả" "hành động" mà "người dùng" muốn "thực hiện" trên "tài nguyên" (ví dụ: "đọc" (read), "ghi" (write), "sửa" (edit), "xóa" (delete), "tải xuống" (download), "in" (print), v.v.).
            -   **Environment Attributes (Thuộc tính môi trường):** "Thuộc tính" "mô tả" "ngữ cảnh" (context) "xung quanh" "yêu cầu" "truy cập" (ví dụ: "thời gian" (time of day), "địa điểm" (location), "mạng" (network), "thiết bị" (device), "IP address", "mức độ rủi ro" (risk level), v.v.).

        -   **"Ví dụ ABAC":**
            -   **"Quy tắc" 1:** "Cho phép" "người dùng" có **`vai_trò = "Admin"`** "thực hiện" **"mọi hành động"** trên **"mọi tài nguyên"**.
            -   **"Quy tắc" 2:** "Cho phép" "người dùng" có **`vai_trò = "Editor"`** "thực hiện" **"hành động" `sửa`** trên **"tài nguyên"** có **`loại = "Bài viết"`** **"nếu"** **`người_tạo_bài_viết = người_dùng_hiện_tại`** (chỉ "sửa bài viết" "của chính mình").
            -   **"Quy tắc" 3:** "Cho phép" "người dùng" có **`level_thành_viên >= "Vàng"`** "truy cập" **"tài nguyên"** có **`tính_bảo_mật = "Bình thường"`** **"trong khoảng thời gian"** **`8h00 - 17h00`** **"từ thứ 2 đến thứ 6"**.
            -   **"Quy tắc" 4:** "Từ chối" "mọi hành động" "ghi" (write) trên "tài nguyên" có `loại = "Dữ liệu nhạy cảm"` **"nếu"** "người dùng" "truy cập" từ "mạng" **`mạng_công_cộng = true`**.

        -   **"Ưu điểm ABAC":**
            -   **"Linh hoạt" và "tùy biến" "cao nhất":** "Cho phép" "định nghĩa" các "quy tắc" "phân quyền" **"phức tạp"** và **"tùy biến"** "cao", "dựa trên" **"nhiều 'tiêu chí' "** "khác nhau" ( "thuộc tính" của "người dùng", "tài nguyên", "hành động", "môi trường"). "Đáp ứng" "mọi" "yêu cầu" "phân quyền" "phức tạp" nhất.
            -   **"Quản lý" "quy tắc" "tập trung"**: "Dễ dàng" "quản lý" "quyền hạn" bằng cách "quản lý" **"các 'quy tắc' " "phân quyền"**. "Thay đổi" "quy tắc" sẽ "ảnh hưởng" đến "tất cả" "yêu cầu" "truy cập" "tuân theo" "quy tắc" đó.
            -   **"Phù hợp" cho "phân quyền" "động" và "theo ngữ cảnh"**: ABAC "dễ dàng" "xử lý" các "yêu cầu" "phân quyền" "thay đổi" "dựa trên" **"ngữ cảnh"** (context) "hiện tại".
            -   **"Mở rộng" "tốt"**: ABAC "dễ dàng" "mở rộng" khi "số lượng" "thuộc tính" và "quy tắc" "tăng lên".

        -   **"Nhược điểm ABAC":**
            -   **"Phức tạp" và "khó hiểu" hơn RBAC**: "Thiết kế", "triển khai", và "quản lý" ABAC **"phức tạp"** hơn RBAC. "Yêu cầu" "hiểu biết" "sâu sắc" về "các 'thuộc tính' " và " 'quy tắc' " "phân quyền".
            -   **"Hiệu suất" có thể "kém hơn" RBAC**: "Đánh giá" "quy tắc" ABAC (policy evaluation) có thể "tốn kém" "tài nguyên" hơn so với "kiểm tra" "vai trò" RBAC, đặc biệt khi có "nhiều" "thuộc tính" và "quy tắc" "phức tạp". "Cần" "tối ưu hóa" "hiệu suất" "đánh giá" "quy tắc" ABAC.
            -   **"Khó 'quản lý' " khi "số lượng" "quy tắc" "tăng lên"**: Mặc dù "quản lý" "quy tắc" "tập trung", nhưng khi "số lượng" "quy tắc" ABAC "tăng lên" "quá nhiều", việc "quản lý" và "duy trì" các "quy tắc" trở nên **"khó khăn"**. "Cần" "công cụ" và "quy trình" "quản lý" "quy tắc" "hiệu quả".

    -   **Policy-Based Authorization - " 'Phân Quyền' " Dựa Trên " 'Chính Sách' " - " 'Luật Lệ' " "Tùy Chỉnh"**:
        -   **"Mô tả":** "Mô hình" Authorization **"tổng quát"** và **"linh hoạt"**, "bao gồm" cả RBAC và ABAC (và các "mô hình" Authorization khác) như là "trường hợp" "đặc biệt". "Phân quyền" truy cập tài nguyên dựa trên **"chính sách"** (policy) - các **" 'luật lệ' "** "được 'định nghĩa' " bằng code (hoặc cấu hình) để "quyết định" "quyền truy cập". "Chính sách" có thể "dựa trên" **"vai trò"** (RBAC), **"thuộc tính"** (ABAC), hoặc **"kết hợp"** cả hai (hoặc "các 'tiêu chí' " khác).
        -   **"Policy-Based Authorization Trong ASP.NET Core":** ASP.NET Core Authorization System "cung cấp" **"Policy-Based Authorization"** làm "cơ chế" "chính" để "phân quyền". "Cho phép" "định nghĩa" **"authorization policies"** (chính sách phân quyền) "tùy chỉnh" bằng code, "kết hợp" "linh hoạt" các "yếu tố" "phân quyền" (roles, claims, attributes, custom logic, v.v.).
        -   **"Ví dụ Policy-Based Authorization":**
            -   **"Policy" "RequireAdminRole":** "Yêu cầu" "người dùng" phải có **"vai trò" "Admin"** để được "ủy quyền". (RBAC Policy)
            -   **"Policy" "EditOwnArticlePolicy":** "Yêu cầu" "người dùng" có **"vai trò" "Editor"** và **"là 'tác giả' " của "bài viết"** để được "ủy quyền" "sửa bài viết". (ABAC-like Policy - "kết hợp" "vai trò" và "thuộc tính").
            -   **"Policy" "VIPAccessPolicy":** "Yêu cầu" "người dùng" có **`level_thành_viên >= "Vàng"`** và "truy cập" **"trong giờ làm việc"** (8h00 - 17h00, thứ 2 - thứ 6) để được "ủy quyền" "truy cập" "khu vực VIP". (ABAC Policy - "dựa trên" "thuộc tính" và "ngữ cảnh").
            -   **"Policy" "CustomPolicy":** "Chính sách" "phân quyền" "tùy chỉnh" "phức tạp", "được 'định nghĩa' " bằng code, "kết hợp" "nhiều" "điều kiện" "khác nhau" (ví dụ: "kiểm tra" "vai trò", "claims", "thuộc tính", "ngữ cảnh", "dữ liệu" từ database, "gọi" "API bên ngoài", v.v.).

        -   **"Ưu điểm Policy-Based Authorization":**
            -   **"Linh hoạt" và "tùy biến" "cao nhất":** "Cho phép" "xây dựng" các "chính sách" "phân quyền" **"phức tạp"** và **"tùy biến"** "cao", "đáp ứng" "mọi" "yêu cầu" "nghiệp vụ" "đặc thù" của ứng dụng. "Bao gồm" cả RBAC và ABAC (và các "mô hình" khác) như "trường hợp" "đặc biệt".
            -   **"Mã hóa" "quy tắc" "phân quyền" bằng code**: "Chính sách" "phân quyền" được "định nghĩa" bằng code (C# trong ASP.NET Core), "dễ dàng" "kiểm soát phiên bản" (version control), "tái sử dụng", và "mở rộng".
            -   **"Tách biệt" "logic" "phân quyền" khỏi "code" "nghiệp vụ"**: "Chính sách" "phân quyền" được "định nghĩa" "riêng biệt" (trong Authorization Policies and Handlers), "không 'trộn lẫn' " với "code" "nghiệp vụ" (Controller Actions, Services, v.v.). "Tăng" "tính 'mô-đun' " và "tính 'bảo trì' " của code.

        -   **"Nhược điểm Policy-Based Authorization":**
            -   **"Phức tạp" và "khó học" ban đầu**: "Học" và "làm chủ" Policy-Based Authorization "yêu cầu" "thời gian" và "nỗ lực" hơn so với RBAC. "Cần" "hiểu rõ" các khái niệm **Authorization Policies**, **Authorization Handlers**, **Authorization Requirements**, v.v. trong ASP.NET Core.
            -   **"Khó 'quản lý' " khi "số lượng" "chính sách" "tăng lên"**: Khi "số lượng" "chính sách" "phân quyền" "tăng lên" "quá nhiều", việc "quản lý" và "duy trì" các "chính sách" trở nên **"khó khăn"**. "Cần" "cấu trúc" và "tổ chức" "chính sách" "hợp lý" để "đảm bảo" "tính 'quản lý' " và "tính 'bảo trì' ".
            -   **"Hiệu suất" có thể "ảnh hưởng" nếu "chính sách" "quá phức tạp"**: "Đánh giá" "chính sách" "phân quyền" "quá phức tạp" (ví dụ: "chính sách" "gọi" "database", "gọi" "API bên ngoài", "thực hiện" "tính toán" "phức tạp", v.v.) có thể "ảnh hưởng" đến "hiệu suất" ứng dụng. "Cần" "thiết kế" "chính sách" "hiệu quả" và "tối ưu hóa" "hiệu suất" "đánh giá" "chính sách".

**3.2. Claims-Based Authorization - " 'Phân Quyền' " Dựa Trên " 'Đặc Điểm' " Người Dùng (Claims) - " 'Hồ Sơ' " "Quyền Hạn" "Linh Hoạt"**

-   **Claims-Based Authorization - " 'Linh Hồn' " Của "Phân Quyền" "Hiện Đại":**

    -   **Claims-Based Authorization** là một "cách tiếp cận" **"hiện đại"** và **"linh hoạt"** để "phân quyền" truy cập tài nguyên, "dựa trên" **"claims"** (tuyên bố) của người dùng. **"Claims"** là các **"mảnh thông tin"** (pieces of information) hoặc **"thuộc tính"** (attributes) "mô tả" **"đặc điểm"** của người dùng (ví dụ: "vai trò" (role), "tên", "email", "quyền hạn" "đặc biệt", "level thành viên", "phòng ban", "địa chỉ", "tuổi", "giới tính", v.v.). "Claims" được "cung cấp" bởi **"Identity Provider" (IdP)** (nhà cung cấp danh tính) sau khi người dùng "được 'xác thực' " (authenticated).
    -   Claims-Based Authorization "cho phép" "phân quyền" truy cập tài nguyên **"dựa trên" "bất kỳ" "thông tin"** nào có thể được "biểu diễn" dưới dạng **"claims"**. "Linh hoạt" hơn RBAC (chỉ "dựa trên" "vai trò") và "mở đường" cho ABAC ( "thuộc tính" trong ABAC thường được "biểu diễn" dưới dạng "claims").

-   **"Claims" - " 'Hồ Sơ' " "Danh Tính" và " 'Quyền Hạn' " Của Người Dùng:**

    -   **"Claim Type" (Loại Claim):** "Tên" của "claim", "định danh" "loại" "thông tin" được "tuyên bố" (ví dụ: `ClaimTypes.Role` (vai trò), `ClaimTypes.Name` (tên), `ClaimTypes.Email` (email), `ClaimTypes.DateOfBirth` (ngày sinh), `ClaimTypes.Country` (quốc gia), v.v.). ASP.NET Core "định nghĩa" một số **"Claim Types" "chuẩn"** trong lớp `ClaimTypes`. Bạn cũng có thể "định nghĩa" **"Claim Types" "tùy chỉnh"**.
    -   **"Claim Value" (Giá Trị Claim):** "Giá trị" của "claim", "dữ liệu" "thực tế" được "tuyên bố" (ví dụ: "Admin" (vai trò), "John Doe" (tên), "john.doe@example.com" (email), "1990-01-01" (ngày sinh), "USA" (quốc gia), v.v.). "Giá trị Claim" là một chuỗi (string).

    -   **"Ví Dụ Claims":**

        ```
        Claim: Type="http://schemas.microsoft.com/ws/2008/06/identity/claims/role", Value="Admin"
        Claim: Type="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name", Value="John Doe"
        Claim: Type="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress", Value="john.doe@example.com"
        Claim: Type="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/dateofbirth", Value="1990-01-01"
        Claim: Type="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/country", Value="USA"
        Claim: Type="http://example.com/claims/level_thanh_vien", Value="Vàng"  // Custom Claim Type
        Claim: Type="http://example.com/claims/phong_ban", Value="Kinh Doanh" // Custom Claim Type
        ```

-   **"Claims-Based Authorization Process":**

    1.  **Authentication (Xác Thực):** Người dùng "đăng nhập" và "được 'xác thực' " bởi Identity Provider (IdP).
    2.  **Issue Claims (Phát Hành Claims):** IdP "phát hành" **"Claims"** cho người dùng "đã xác thực". "Claims" được "lưu trữ" trong **"User Identity"** (đối tượng `ClaimsPrincipal` trong .NET) của người dùng. "User Identity" thường được "truyền" đến ứng dụng web thông qua **Authentication Cookie** (session-based authentication) hoặc **JWT Access Token** (token-based authentication).
    3.  **Authorization (Ủy Quyền):** Ứng dụng web "kiểm tra" **"Claims"** trong **"User Identity"** của người dùng để "quyết định" "quyền truy cập" vào tài nguyên. "Kiểm tra" "claims" bằng cách "định nghĩa" **"authorization policies"** (chính sách phân quyền) "dựa trên" **"claims"**.
    4.  **Access Granted/Denied (Truy Cập Được Cho Phép/Từ Chối):** Dựa trên kết quả "kiểm tra" "claims", ứng dụng web "cho phép" hoặc "từ chối" "truy cập" vào tài nguyên.

-   **"Ưu điểm Claims-Based Authorization":**
    -   **"Linh hoạt" và "mở rộng"**: "Phân quyền" "dựa trên" **"bất kỳ" "thông tin"** nào có thể được "biểu diễn" dưới dạng "claims". "Dễ dàng" "mở rộng" "hệ thống" "phân quyền" bằng cách "thêm" "claims" "mới".
    -   **"Decoupled" (Tách Biệt) Authorization Logic khỏi User Store**: "Logic" "phân quyền" (authorization policies) "dựa trên" **"claims"**, "không 'phụ thuộc' " vào "cấu trúc" "user store" (database người dùng) "cụ thể". "Ứng dụng" "không cần" phải "biết" "cách" "lưu trữ" "vai trò" hoặc "quyền hạn" trong database. "Chỉ cần" "kiểm tra" "claims" trong "User Identity".
    -   **"Interoperability" (Khả năng tương tác) "cao"**: "Claims" là một "tiêu chuẩn" "mở" (open standard), được "hỗ trợ" "rộng rãi" trong các hệ thống "xác thực" và "ủy quyền" "hiện đại" (ví dụ: OAuth 2.0, OpenID Connect, SAML). "Dễ dàng" "tích hợp" Claims-Based Authorization với các "hệ thống" "bên ngoài".
    -   **"Fine-grained" (Chi tiết) và "context-aware" (nhận biết ngữ cảnh) Authorization**: "Claims" có thể "chứa" "thông tin" "chi tiết" về "người dùng" và "ngữ cảnh", "cho phép" "phân quyền" "chi tiết" và "theo ngữ cảnh".

-   **"Nhược điểm Claims-Based Authorization":**
    -   **"Quản lý" "claims" "phức tạp" hơn**: "Quản lý" "claims" (định nghĩa "Claim Types", "phát hành" "Claims", "cập nhật" "Claims", v.v.) có thể "phức tạp" hơn so với "quản lý" "vai trò" trong RBAC.
    -   **"Security Risks" nếu "claims" "không được 'bảo vệ' "**: Nếu "claims" bị "sửa đổi" hoặc "giả mạo", "hệ thống" "phân quyền" có thể bị "vô hiệu". "Cần" "đảm bảo" "tính 'toàn vẹn' " và "tính 'xác thực' " của "claims" (ví dụ: bằng cách "ký" "claims" bằng "chữ ký số" - digital signature trong JWT).
    -   **"Policy Evaluation" có thể "tốn kém" "hiệu suất"**: "Đánh giá" "chính sách" "phân quyền" "dựa trên" "claims" "phức tạp" (ví dụ: "chính sách" "kiểm tra" "nhiều" "claims", "claims" có "giá trị" "lớn", v.v.) có thể "tốn kém" "hiệu suất". "Cần" "tối ưu hóa" "hiệu suất" "đánh giá" "chính sách".

**3.3. Policy-Based Authorization Trong ASP.NET Core - " 'Luật Lệ' " "Tùy Chỉnh" Cho "Phân Quyền" - " 'Viết' " "Chính Sách", " 'Xây Dựng' " "Hệ Thống Luật"**

-   **Policy-Based Authorization Trong ASP.NET Core - " 'Sức Mạnh' " "Tùy Biến" "Phân Quyền":**

    -   ASP.NET Core Authorization System "cung cấp" **"Policy-Based Authorization"** làm "cơ chế" "chính" để "phân quyền". "Cho phép" bạn **"định nghĩa" "authorization policies"** (chính sách phân quyền) **"tùy chỉnh"** bằng code, "để" "kiểm soát" "quyền truy cập" vào tài nguyên. "Chính sách" là " 'luật lệ' " "phân quyền" của ứng dụng.
    -   "Chính sách" Authorization trong ASP.NET Core được "xây dựng" từ **"Authorization Requirements"** (yêu cầu ủy quyền) và **"Authorization Handlers"** (trình xử lý ủy quyền).

-   **Authorization Policy (Chính Sách Phân Quyền):**

    -   **"Định nghĩa" "tên" "chính sách"**: "Đặt tên" cho "chính sách" (ví dụ: "RequireAdminRole", "EditOwnArticlePolicy", "VIPAccessPolicy", v.v.). "Tên" "chính sách" được "dùng" để "tham chiếu" đến "chính sách" trong code (ví dụ: trong `[Authorize]` attribute).
    -   **"Định nghĩa" "danh sách" "Authorization Requirements"**: "Chính sách" "bao gồm" **"một hoặc nhiều" "Authorization Requirements"**. "Authorization Requirement" là một **"yêu cầu" "cụ thể"** mà "người dùng" phải "đáp ứng" để được "ủy quyền".

-   **Authorization Requirement (Yêu Cầu Ủy Quyền):**

    -   "Đại diện" cho **"một 'điều kiện' " "phân quyền"** "cụ thể" (ví dụ: "yêu cầu" "người dùng" phải có "vai trò" "Admin", "yêu cầu" "người dùng" phải có "claim" `level_thành_viên` với "giá trị" >= "Vàng", "yêu cầu" "thời gian" "truy cập" phải "trong giờ làm việc", v.v.).
    -   "Authorization Requirement" là một lớp (class) **"implement" interface `IAuthorizationRequirement`**. Bạn có thể "tạo" **"Authorization Requirements" "tùy chỉnh"** của riêng bạn bằng cách "implement" interface `IAuthorizationRequirement`.
    -   "Ví dụ Authorization Requirements "chuẩn" trong ASP.NET Core":
        -   `RolesAuthorizationRequirement`: "Yêu cầu" "người dùng" phải có **"một trong các" "vai trò" "được chỉ định"** (RBAC).
        -   `ClaimsAuthorizationRequirement`: "Yêu cầu" "người dùng" phải có **"claim" "được chỉ định"** (Claim-Based Authorization).
        -   `AssertionRequirement`: "Yêu cầu" "người dùng" phải "đáp ứng" một **"biểu thức" "logic" "tùy chỉnh"** (custom assertion).

-   **Authorization Handler (Trình Xử Lý Ủy Quyền):**

    -   "Chịu trách nhiệm" **"đánh giá"** (evaluate) **"Authorization Requirement"** và "quyết định" xem "người dùng" có **"đáp ứng"** "Authorization Requirement" đó hay không.
    -   "Authorization Handler" là một lớp (class) **"implement" interface `AuthorizationHandler<TRequirement>`**, với `TRequirement` là "loại" "Authorization Requirement" mà "handler" này "xử lý". Bạn cần "tạo" **"Authorization Handlers" "tùy chỉnh"** để "xử lý" "Authorization Requirements" "tùy chỉnh" của bạn.
    -   Mỗi `AuthorizationHandler` "nhận" vào **`AuthorizationHandlerContext`** (ngữ cảnh trình xử lý ủy quyền), chứa "thông tin" về **"người dùng"**, **"Authorization Requirement"**, và **"tài nguyên"** (resource) (tùy chọn).
    -   Trong `AuthorizationHandler`, bạn "viết code" để **"kiểm tra" "Authorization Requirement"** và "gọi" `context.Succeed(requirement)` nếu "người dùng" "đáp ứng" "requirement", hoặc `context.Fail(requirement)` nếu "người dùng" "không đáp ứng" "requirement".

-   **"Luồng" Policy-Based Authorization Trong ASP.NET Core:**

    1.  **Request Authorization (Yêu Cầu Ủy Quyền):** Khi một request "truy cập" vào một "tài nguyên" được "bảo vệ" (ví dụ: Controller Action có attribute `[Authorize(Policy = "...") ]`), ASP.NET Core Authorization Middleware "bắt" request.
    2.  **Find Policy (Tìm Chính Sách):** Authorization Middleware "tìm" **"Authorization Policy"** được "chỉ định" (ví dụ: "RequireAdminRole").
    3.  **Get Requirements (Lấy Yêu Cầu):** Authorization Middleware "lấy" **"danh sách" "Authorization Requirements"** từ "Authorization Policy".
    4.  **Find Handlers (Tìm Trình Xử Lý):** Authorization Middleware "tìm" **"Authorization Handlers"** "tương ứng" với "mỗi" "Authorization Requirement".
    5.  **Execute Handlers (Thực Thi Trình Xử Lý):** Authorization Middleware "thực thi" **"tất cả" "Authorization Handlers"** "tìm thấy", "truyền" **`AuthorizationHandlerContext`** vào "mỗi" "handler".
    6.  **Check Results (Kiểm Tra Kết Quả):** Authorization Middleware "kiểm tra" **"kết quả"** từ "tất cả" "Authorization Handlers".
        -   **"Authorization Success (Ủy Quyền Thành Công):** Nếu **"tất cả"** "Authorization Requirements" trong "Policy" được "đáp ứng" (ít nhất một `AuthorizationHandler` gọi `context.Succeed(requirement)` cho "mỗi" "requirement"), "ủy quyền" thành công.
        -   **"Authorization Failure (Ủy Quyền Thất Bại):** Nếu **"có 'bất kỳ' " "Authorization Requirement"** nào **"không được" "đáp ứng"** (không có `AuthorizationHandler` nào gọi `context.Succeed(requirement)` cho "requirement" đó), "ủy quyền" thất bại.
    7.  **Access Granted/Denied (Truy Cập Được Cho Phép/Từ Chối):** Dựa trên kết quả "ủy quyền", ASP.NET Core "cho phép" hoặc "từ chối" "truy cập" vào tài nguyên.

**3.4. "Thực Thi" Authorization Trong Code - Attributes `[Authorize]`, `IAuthorizationPolicyProvider`, `IAuthorizationHandler` - " 'Code' " "Quyền Lực" "Phân Quyền"**

-   **"Thực Thi" Authorization Trong ASP.NET Core - " 'Vũ Khí' " "Phân Quyền" Trong Tay "Lập Trình Viên":**

    -   ASP.NET Core "cung cấp" nhiều "công cụ" để "thực thi" Authorization trong code, "kiểm soát" "quyền truy cập" tài nguyên ở các "mức độ" "khác nhau": Controller Actions, Razor Pages, View Components, Services, v.v.

-   **`[Authorize]` Attribute - " 'Lá Chắn' " "Bảo Vệ" Controller Actions và Razor Pages:**

    -   `[Authorize]` attribute là "cách" **"đơn giản"** và **"phổ biến"** nhất để "yêu cầu" **"ủy quyền"** cho **Controller Actions** và **Razor Pages**.
    -   **"Áp dụng" `[Authorize]` attribute lên Controller Class hoặc Controller Action:**

        ```csharp
        [Authorize] // Yêu cầu người dùng phải "được xác thực" (authenticated)
        public class HomeController : Controller
        {
            public IActionResult Index() { ... } // Yêu cầu "xác thực"

            [Authorize] // Yêu cầu "xác thực" (thừa kế từ class, nhưng có thể ghi đè)
            public IActionResult Privacy() { ... }

            [AllowAnonymous] // Cho phép "truy cập" "vô danh" (anonymous access) - ghi đè [Authorize] ở class
            public IActionResult Contact() { ... }
        }
        ```

    -   **"Chỉ định" "Authorization Policy" trong `[Authorize]` attribute:**

        ```csharp
        [Authorize(Policy = "RequireAdminRole")] // Yêu cầu "chính sách" "RequireAdminRole"
        public IActionResult AdminPanel() { ... }

        [Authorize(Policy = "EditOwnArticlePolicy")] // Yêu cầu "chính sách" "EditOwnArticlePolicy"
        public IActionResult EditArticle(int id) { ... }
        ```

    -   **"Chỉ định" "Roles" (Vai Trò) trong `[Authorize]` attribute (RBAC Shortcut):**

        ```csharp
        [Authorize(Roles = "Admin,SuperAdmin")] // Yêu cầu người dùng phải có "vai trò" "Admin" hoặc "SuperAdmin"
        public IActionResult AdminPanel() { ... }
        ```

    -   **"Chỉ định" "Claims" trong `[Authorize]` attribute (Claims-Based Authorization Shortcut):**

        ```csharp
        [Authorize(Policy = "RequireClaim_LevelThanhVien_Vang")] // Policy "tùy chỉnh" "dựa trên" claim
        public IActionResult VIPArea() { ... }

        // Cách "inline" - ít dùng vì "khó 'bảo trì' "
        [Authorize(Policy = "RequireVangLevel")] // Policy "được định nghĩa" trong Startup.cs
        public IActionResult VIPArea() { ... }

        // Policy "RequireVangLevel" được định nghĩa" trong Startup.cs
        services.AddAuthorization(options =>
        {
            options.AddPolicy("RequireVangLevel", policy =>
                  policy.RequireClaim("level_thanh_vien", "Vàng", "Kim Cương")); // Yêu cầu claim "level_thanh_vien" có giá trị "Vàng" hoặc "Kim Cương"
        });
        ```

-   **`IAuthorizationPolicyProvider` Interface - " 'Nhà Cung Cấp' " "Chính Sách" "Tùy Biến":**

    -   `IAuthorizationPolicyProvider` interface "cho phép" bạn **"cung cấp" "Authorization Policies" một cách "động"** và **"tùy biến"**. "Thay vì" "đăng ký" "chính sách" "cứng" trong `Startup.cs`, bạn có thể "lấy" "chính sách" từ database, cấu hình, hoặc "tạo" "chính sách" "dựa trên" "ngữ cảnh" (context).
    -   "Implement" interface `IAuthorizationPolicyProvider` và "đăng ký" "implementation" của bạn trong DI container (Dependency Injection container).
    -   "Phương thức" `GetPolicyAsync(string policyName)` trong `IAuthorizationPolicyProvider` được gọi khi `[Authorize(Policy = "{policyName}")]` attribute được "sử dụng". Bạn "viết code" trong `GetPolicyAsync` để "trả về" `AuthorizationPolicy` "tương ứng" với `policyName`.

-   **`IAuthorizationHandler` Interface - " 'Trình Xử Lý' " "Yêu Cầu" "Phân Quyền" "Tùy Biến":**

    -   `IAuthorizationHandler` interface "cho phép" bạn **"viết" "Authorization Handlers" "tùy chỉnh"** để "xử lý" **"Authorization Requirements" "tùy chỉnh"** của bạn.
    -   "Implement" interface `IAuthorizationHandler<TRequirement>` (với `TRequirement` là "loại" "Authorization Requirement" mà "handler" này "xử lý").
    -   "Phương thức" `HandleAsync(AuthorizationHandlerContext context)` trong `IAuthorizationHandler` được gọi khi Authorization Middleware "thực thi" "handler". Bạn "viết code" trong `HandleAsync` để **"kiểm tra" "Authorization Requirement"** và "gọi" `context.Succeed(requirement)` hoặc `context.Fail(requirement)`.
    -   "Đăng ký" "Authorization Handlers" trong DI container (thường là "scoped" service).

**Tổng Kết Chương 3:**

-   Bạn đã "khám phá" các "mô hình" Authorization "phổ biến" nhất và "hiểu" "ưu điểm", "nhược điểm" của từng "mô hình".
    -   "Nắm vững" **Role-Based Access Control (RBAC)** ("phân quyền" dựa trên "vai trò" - "đơn giản" và "phổ biến").
    -   "Tìm hiểu" **Attribute-Based Access Control (ABAC)** ("phân quyền" dựa trên "thuộc tính" - "linh hoạt" và "mạnh mẽ").
    -   Biết về **Policy-Based Authorization** ("phân quyền" dựa trên "chính sách" - "tùy biến" "cao nhất" - "cơ chế" "chính" trong ASP.NET Core).
    -   "Hiểu" **Claims-Based Authorization** ("phân quyền" dựa trên "claims" - "linh hoạt" và "hiện đại").
    -   "Nắm bắt" cách " "thực thi' " Authorization trong ASP.NET Core bằng **`[Authorize]` attribute**, **`IAuthorizationPolicyProvider`**, và **`IAuthorizationHandler`**.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: Authentication và Authorization Trong ASP.NET Core - " 'Vũ Khí' " "Bảo Vệ" Web App .NET**. Chúng ta sẽ "tổng kết" lại "kiến thức" về Authentication và Authorization và "xem xét" cách chúng được "tích hợp" và "hoạt động" trong ASP.NET Core, "tạo ra" " 'lá chắn' " "bảo vệ" ứng dụng web .NET của bạn.

Bạn có câu hỏi nào về Authorization này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" "bảo mật" ứng dụng web.



