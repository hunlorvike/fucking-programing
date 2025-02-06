# Chương 3: Docker Images - " 'Bản Thiết Kế' " Ứng Dụng Đóng Gói - " 'Khuôn Mẫu' " Cho Container - " 'Bí Mật' " Bên Trong " 'Hộp' " Docker

Chào mừng bạn đến với **Chương 3: Docker Images - " 'Bản Thiết Kế' " Ứng Dụng Đóng Gói"**! Trong chương này, chúng ta sẽ "đi sâu" vào **Docker Images**, "khái niệm" **"nền tảng"** và **"quan trọng"** nhất của Docker. Chúng ta sẽ "mở hộp" Docker Images, "khám phá" **"bản chất"** của Docker Images, "cách" Docker Images được **"lưu trữ"** và **"quản lý"**, và "học cách" **"tìm kiếm"** và **"tải về"** Docker Images "có sẵn" từ **Docker Hub**. "Docker Images" là " 'khuôn mẫu' " để "tạo ra" Docker Containers, "hiểu rõ" Docker Images là "hiểu rõ" " 'linh hồn' " của Docker.

**Phần 3: Docker Images - " 'Bản Thiết Kế' " Ứng Dụng Đóng Gói - " 'Khuôn Mẫu' " Cho Container**

**3.1. Docker Images là gì? - " 'Ảnh Chụp' " Ứng Dụng và Môi Trường Chạy - " 'Bản Sao' " "Hoàn Hảo" Để " 'Vận Chuyển' "**

-   **Docker Image (Docker Image) - " 'Ảnh Chụp' " "Toàn Diện" Ứng Dụng:**

    -   **Docker Image** (Docker Image) là một **"file" "chỉ đọc"** (read-only template) chứa **"toàn bộ"** "mọi thứ" mà ứng dụng "cần" để "chạy" (code ứng dụng, thư viện, dependencies, runtime, system tools, settings, v.v.).
    -   Hãy tưởng tượng Docker Image như một **" 'ảnh chụp' " (snapshot)** của ứng dụng và **"môi trường" "chạy"** ứng dụng tại một **"thời điểm" "cụ thể"**. "Ảnh chụp" này **"đóng băng"** trạng thái của ứng dụng và môi trường, "đảm bảo" ứng dụng sẽ **"chạy" "nhất quán"** ở **"mọi nơi"** mà Docker Container được "chạy" từ Image đó.
    -   Docker Image là **" 'bản sao' " "hoàn hảo"** để **"vận chuyển"** ứng dụng. Bạn có thể "vận chuyển" Docker Image "dễ dàng" giữa các môi trường khác nhau (máy tính cá nhân, máy chủ, cloud, v.v.) và "chạy" ứng dụng "nhất quán" ở "mọi nơi" từ Image đó.

-   **" 'Cấu Tạo' " Bên Trong Docker Image - " 'Tầng Tầng Lớp Lớp' " "Xây Dựng" Nên Image:**

    -   Docker Image được "xây dựng" từ **"nhiều lớp"** (layers) **"chỉ đọc"** (read-only layers) **"chồng lên nhau"** (layered filesystem). Mỗi lớp "đại diện" cho một **"thay đổi"** (change) trong Dockerfile (file "công thức" "xây dựng" Image - Chương 5).
    -   **Base Image (Image Nền):** Lớp **"đầu tiên"** (base layer) của Docker Image là **"Base Image"**. Base Image thường là một Docker Image "có sẵn" trên Docker Hub "chứa" **"hệ điều hành 'tối giản' "** (minimal OS) (ví dụ: Alpine Linux, Ubuntu Minimal, Debian Slim) hoặc **"runtime"** (ví dụ: .NET runtime, Node.js runtime, Java runtime). Base Image "cung cấp" **"nền tảng"** để "xây dựng" ứng dụng.
    -   **Application Layers (Các Lớp Ứng Dụng):** Các lớp **"tiếp theo"** (application layers) "chứa" **"code ứng dụng"**, **"thư viện"**, **"dependencies"**, **"settings"**, v.v. Các lớp này được "tạo ra" bằng cách "thực hiện" các "lệnh" trong Dockerfile (ví dụ: `COPY`, `RUN`). Mỗi lệnh trong Dockerfile thường "tạo ra" một lớp Image mới.
    -   **Read-Only Layers (Các Lớp "Chỉ Đọc"):** **"Tất cả"** các lớp của Docker Image đều là **"chỉ đọc"** (read-only). Dữ liệu trong các lớp Image **"không thể" "bị 'thay đổi' "** sau khi Image đã được "xây dựng". "Đảm bảo" **"tính 'bất biến' " (immutability)** và **"tính 'nhất quán' " (consistency)** của Docker Image.
    -   **Writable Layer (Lớp "Ghi"):** Khi bạn "chạy" Docker Container từ Docker Image, Docker Engine sẽ "thêm" một **"lớp 'ghi' " "phía trên"** các lớp Image "chỉ đọc". Lớp "ghi" (container layer) là **"nơi" Docker Container "ghi" "dữ liệu"** (ví dụ: file log, dữ liệu database, v.v.) trong quá trình "chạy". Dữ liệu "ghi" trong lớp "ghi" **"không bị 'mất' "** khi Container "dừng lại", nhưng sẽ **"bị 'mất' "** khi Container **"bị 'xóa' "**.

-   **"Lợi Ích" Của "Kiến Trúc" Layered Filesystem - " 'Tiết Kiệm' ", " 'Nhanh Chóng' ", và " 'Tái Sử Dụng' " Images:**

    -   **"Tiết Kiệm" "Dung Lượng Lưu Trữ" (Storage Efficiency):** Các lớp Image "chỉ đọc" được **"chia sẻ"** (shared) giữa **"nhiều Containers"** và **"nhiều Images"** khác nhau. Nếu nhiều Containers "dùng chung" một Base Image hoặc các lớp Image "chung", Docker Engine chỉ cần "lưu trữ" các lớp "chung" **"một lần duy nhất"** trên ổ cứng, "tiết kiệm" "đáng kể" "dung lượng lưu trữ" (disk space).
    -   **"Tải Về" Images "Nhanh Chóng" (Faster Image Pulls):** Khi bạn "tải về" Docker Image từ Docker Hub, Docker Engine chỉ cần "tải về" **"các lớp Image 'mới' "** hoặc **"các lớp Image 'thay đổi' "**, **"không cần" "tải về" "toàn bộ" Image** nếu các lớp Image "chung" đã "có sẵn" trên máy tính của bạn. "Tăng tốc" quá trình "tải về" Images.
    -   **"Xây Dựng" Images "Nhanh Chóng" (Faster Image Builds):** Khi bạn "xây dựng" Docker Image từ Dockerfile, Docker Engine **"cache"** (lưu trữ tạm) **"kết quả"** của **"từng lệnh"** trong Dockerfile thành các lớp Image. Nếu bạn "sửa đổi" Dockerfile và "xây dựng" lại Image, Docker Engine sẽ **"tái sử dụng"** các lớp Image "đã cache" **"không bị 'thay đổi' "** và chỉ "xây dựng" lại **"các lớp Image 'mới' "** hoặc **"các lớp Image 'phụ thuộc' "** vào các lớp "thay đổi". "Tăng tốc" quá trình "xây dựng" Images.
    -   **"Tái Sử Dụng" Images (Image Reusability):** Docker Images "có sẵn" trên Docker Hub (Base Images, ứng dụng "đóng gói" "hoàn chỉnh", v.v.) có thể được **"tái sử dụng"** trong nhiều dự án khác nhau, "tiết kiệm" thời gian và công sức "xây dựng" Images "từ đầu".

**3.2. Docker Hub và "Kho Lưu Trữ" Images "Công Cộng" và "Riêng Tư" - " 'Siêu Thị' " Images - " 'Nơi' " "Tìm Kiếm", "Tải Về", và " 'Chia Sẻ' " Images**

-   **Docker Hub (Docker Hub) - " 'Chợ' " Docker Images "Lớn Nhất Hành Tinh":**

    -   **Docker Hub** (hub.docker.com) là một **"registry" "trực tuyến"** (online registry) "công cộng" và "riêng tư" để **"lưu trữ"**, **"chia sẻ"**, và **"quản lý"** Docker Images.
    -   Docker Hub là **"registry" Docker "mặc định"**. Khi bạn "dùng" lệnh `docker pull <image_name>` hoặc `docker run <image_name>` mà "không chỉ định" registry, Docker CLI sẽ "tự động" "tìm kiếm" và "tải về" Docker Images từ Docker Hub.
    -   Docker Hub "cung cấp" **"hai loại" "kho lưu trữ" (repositories) Docker Images:**

        -   **Public Repositories (Kho Lưu Trữ "Công Cộng"):** **"Miễn phí"** cho mọi người "sử dụng". Docker Images trong "public repositories" có thể được **"tìm kiếm"**, **"tải về"**, và **"sử dụng"** bởi **"bất kỳ ai"** trên internet ( "Public" - "ai cũng thấy được"). "Phù hợp" để "chia sẻ" Docker Images "mã nguồn mở" (open-source images), "ứng dụng 'nền tảng' " (base images), hoặc các Docker Images "công cộng" khác.
        -   **Private Repositories (Kho Lưu Trữ "Riêng Tư"):** **"Trả phí"** (có các gói "miễn phí giới hạn" và các gói "trả phí" "nhiều tính năng" hơn). Docker Images trong "private repositories" chỉ có thể được **"truy cập"** và "tải về" bởi **"người dùng" "được phép"** (thường là "thành viên" của tổ chức hoặc nhóm "chủ sở hữu" repository) ( "Private" - "chỉ người được phép mới thấy được"). "Phù hợp" để "lưu trữ" Docker Images "riêng tư" của doanh nghiệp, ứng dụng "proprietary" (độc quyền), hoặc dữ liệu "nhạy cảm".

-   **"Các 'Tính Năng' " "Chính" Của Docker Hub:**

    -   **"Kho Lưu Trữ" Docker Images "Khổng Lồ":** "Chứa" **"hàng triệu" Docker Images** "từ khắp nơi trên thế giới". "Tìm" được Docker Images cho "hầu hết" các "nhu cầu" ứng dụng của bạn.
    -   **"Tìm Kiếm" Docker Images (Image Search):** "Cho phép" bạn **"tìm kiếm"** Docker Images "dễ dàng" bằng "từ khóa" (ví dụ: "nginx", "mysql", "dotnet", "ubuntu", v.v.) thông qua website Docker Hub hoặc lệnh `docker search` trên Docker CLI.
    -   **"Tải Về" Docker Images (Image Pull):** "Cho phép" bạn **"tải về"** Docker Images từ Docker Hub về máy tính của mình bằng lệnh `docker pull`.
    -   **"Tải Lên" Docker Images (Image Push):** "Cho phép" bạn **"tải lên"** Docker Images "riêng" của bạn lên Docker Hub để "lưu trữ" và "chia sẻ" với người khác (cần "tạo tài khoản" và "đăng nhập" Docker Hub).
    -   **"Quản Lý" Docker Images (Image Management):** "Cung cấp" các "công cụ" để "quản lý" Docker Images (ví dụ: "tạo" repositories, "quản lý" tags (phiên bản), "xóa" images, "phân quyền" truy cập, v.v.).
    -   **"Tự Động Hóa" "Xây Dựng" Images (Automated Builds):** "Cho phép" bạn **"tự động hóa"** quá trình "xây dựng" Docker Images từ **GitHub** hoặc **Bitbucket** repositories. Mỗi khi code trong repository "thay đổi", Docker Hub sẽ "tự động" "xây dựng" Docker Image mới và "cập nhật" Image trên Docker Hub. "Tiện lợi" cho **CI/CD (Continuous Integration/Continuous Delivery)** workflows.
    -   **"Tổ Chức" và "Nhóm" (Organizations and Teams):** "Cho phép" các **"tổ chức"** (organizations) và **"nhóm"** (teams) "làm việc chung" trên Docker Hub, "chia sẻ" Docker Images, và "quản lý" "quyền truy cập" Images.

**3.3. "Tìm Kiếm" và "Tải Về" Docker Images Từ Docker Hub (`docker pull`, `docker search`) - " 'Rinh Về' " Images "Có Sẵn" - " 'Lạc Giữa' " "Biển Images" và " 'Chọn' " "Đúng' " Image "Cần"**

-   **"Tìm Kiếm" Docker Images Trên Docker Hub - " 'Lạc Giữa' " "Biển Images" và " 'Tìm' " "Ngọc Trai' " Ứng Dụng:**

    -   Docker Hub "chứa" **"hàng triệu" Docker Images**. "Tìm kiếm" Docker Image "phù hợp" với "nhu cầu" của bạn có thể "giống như" "lạc giữa" một **"biển" Docker Images**.
    -   "Kỹ năng" **"tìm kiếm"** Docker Images "hiệu quả" trên Docker Hub là "quan trọng" để bạn **"nhanh chóng" "tìm"** được Docker Images **"chất lượng"**, **"an toàn"**, và **"phù hợp"** với "mục đích" của mình.

-   **"Các 'Chiêu' " "Tìm Kiếm" Docker Images "Hiệu Quả" Trên Docker Hub:**

    -   **"Từ Khóa" Tìm Kiếm "Chính Xác":** "Dùng" **"từ khóa"** "mô tả" **"chính xác"** "ứng dụng" hoặc "công nghệ" bạn muốn "tìm" Docker Image. (Ví dụ: "nginx", "mysql", "dotnet", "ubuntu", "wordpress", "redis", v.v.). "Từ khóa" càng "chính xác", "kết quả" tìm kiếm càng "chính xác" hơn.

    -   **"Lọc" Theo "Bộ Lọc" (Filters) Trên Website Docker Hub:** "Dùng" các **"bộ lọc"** (filters) trên website Docker Hub (https://hub.docker.com/search) để "thu hẹp" "phạm vi" tìm kiếm và "lọc" "kết quả" theo các "tiêu chí" "khác nhau":
        -   **"Images" vs. "Organizations" vs. "Repositories":** "Chọn" loại "kết quả" tìm kiếm (Images - chỉ tìm Images, Organizations - chỉ tìm Organizations, Repositories - tìm cả Images và Repositories).
        -   **"Official Images" (Images "Chính Thức"):** "Lọc" chỉ "hiển thị" các Docker Images **"chính thức"** được "cung cấp" bởi Docker Verified Publishers (thường là các hãng phần mềm lớn hoặc các tổ chức uy tín). Docker Official Images thường được "đánh dấu" bằng **"huy hiệu màu xanh" "Verified Publisher"**. "Ưu tiên" dùng Official Images vì thường **"chất lượng"**, **"an toàn"**, và **"được 'hỗ trợ' " tốt** hơn.
        -   **"Star Count" (Số Sao):** "Sắp xếp" kết quả tìm kiếm theo **"số sao"** (stars) (độ "phổ biến" và "uy tín" của Docker Image). Docker Images có "số sao" "cao" thường được "cộng đồng" Docker "tin dùng" hơn.
        -   **"Pull Count" (Số Lượt Tải Về):** "Sắp xếp" kết quả tìm kiếm theo **"số lượt tải về"** (pulls) (mức độ "sử dụng" của Docker Image). Docker Images có "số lượt tải về" "cao" thường "phổ biến" và "được 'kiểm chứng' " qua "thực tế" hơn.
        -   **"Automated Builds" (Tự Động Xây Dựng):** "Lọc" chỉ "hiển thị" các Docker Images được **"tự động" "xây dựng"** từ **GitHub** hoặc **Bitbucket** repositories. "Đảm bảo" Docker Image được "cập nhật" "thường xuyên" theo code "mới nhất" trong repository "nguồn".

    -   **"Dùng" Lệnh `docker search` Với "Bộ Lọc" (Filters) và "Sắp Xếp" (Sorting) (Docker CLI):** Lệnh `docker search` trên Docker CLI cũng "hỗ trợ" một số "tùy chọn" để "lọc" và "sắp xếp" "kết quả" tìm kiếm (tham khảo tài liệu `docker search --help` để biết thêm chi tiết).

        ```bash
        docker search --filter is-official=true nginx  # "Tìm kiếm" Docker Images "chính thức" của "nginx"
        docker search --filter stars=5 nginx         # "Tìm kiếm" Docker Images "nginx" có "ít nhất" 5 sao
        docker search --sort stars nginx           # "Tìm kiếm" Docker Images "nginx" và "sắp xếp" theo "số sao" (giảm dần)
        ```

-   **" 'Đọc Kỹ' " "Thông Tin" Docker Image Trước Khi "Tải Về" và "Dùng":**

    -   Trước khi "tải về" (pull) và "dùng" bất kỳ Docker Image nào từ Docker Hub (đặc biệt là Docker Images "không chính thức" - non-official images), hãy **"dành thời gian" "đọc kỹ" "thông tin"** về Docker Image đó trên trang Docker Hub repository:
        -   **"Mô Tả" (Description):** "Đọc" "mô tả" Docker Image để "hiểu" **"mục đích"** và **"chức năng"** của Image, **"các thành phần"** "chứa" trong Image, và **"cách 'sử dụng' " Image**.
        -   **"Tags" (Phiên Bản):** "Xem" các **"tags"** (phiên bản) "có sẵn" của Image và "chọn" tag **"phù hợp"** với "nhu cầu" của bạn. "Tag" `latest` thường là "phiên bản" "mới nhất" (nhưng có thể "không ổn định"). "Ưu tiên" "dùng" các tags **"phiên bản" "cụ thể"** (ví dụ: `1.21.3`, `7.0-sdk`, `alpine-3.16`) để "đảm bảo" **"tính 'ổn định' "** và **"tính 'tái sản xuất' "** của ứng dụng.
        -   **"Dockerfile" (nếu có):** "Xem" Dockerfile (nếu "nhà cung cấp" Image "cung cấp" Dockerfile trên GitHub hoặc Docker Hub) để "hiểu" **"cách" Docker Image được "xây dựng"**. "Kiểm tra" Dockerfile để "đánh giá" **"tính 'an toàn' "** và **"tính 'tin cậy' "** của Image (ví dụ: "có chứa" "mã độc hại" không, "có 'tuân thủ' " "best practices" Dockerfile không).
        -   **"Hướng Dẫn Sử Dụng" (Usage Instructions):** "Đọc" "hướng dẫn sử dụng" (thường có trong phần "Overview" hoặc "Readme" của Docker Hub repository) để "biết" **"cách 'chạy' " Container** từ Image, **"cấu hình" Container**, **"truy cập" ứng dụng** trong Container, và **"các 'tùy chọn' " "nâng cao"** khác.
        -   **"Đánh Giá" và "Bình Luận" (Stars and Comments):** "Xem" **"số sao"** (stars) và **"bình luận"** (comments) của "cộng đồng" Docker về Docker Image để "đánh giá" **"chất lượng"** và **"độ tin cậy"** của Image.

-   **"Tải Về" Docker Image (`docker pull <image_name>`) - " 'Rinh Về' " Image "Đã Chọn" Để " 'Dùng' "**:

    -   Sau khi đã "tìm kiếm" và "chọn" được Docker Image "phù hợp" trên Docker Hub, bạn có thể **"tải về"** Docker Image đó về máy tính của mình bằng lệnh **`docker pull <image_name>`**.
    -   **"Cú pháp" lệnh `docker pull`:**

        ```bash
        docker pull <image_name>[:<tag>] # "Tải về" Docker Image có tên "<image_name>" và tag "<tag>" (nếu có tag). Nếu "không có" tag, "mặc định" "tải về" tag "latest".
        ```

        -   **`<image_name>`:** **"Tên" Docker Image** (ví dụ: `nginx`, `mysql`, `microsoft/dotnet-sdk`). "Bắt buộc" phải có.
        -   **`[:<tag>]`:** **"Tag" Docker Image** (phiên bản Image) (ví dụ: `:latest`, `:stable`, `:alpine-3.16`, `:7.0-sdk`). **"Tùy chọn"**. Nếu "không chỉ định" tag, Docker CLI sẽ "mặc định" "tải về" tag **`latest`** (phiên bản "mới nhất" - nhưng có thể "không ổn định"). "Nên" "chọn" tag **"phiên bản" "cụ thể"** (ví dụ: `nginx:1.21.3`, `microsoft/dotnet-sdk:7.0`) để "đảm bảo" **"tính 'ổn định' "** và **"tính 'tái sản xuất' "** của ứng dụng.

    -   **"Ví Dụ" Lệnh `docker pull`:**

        ```bash
        docker pull nginx:latest   # "Tải về" Docker Image "nginx" với tag "latest" (phiên bản mới nhất)
        docker pull mysql:8.0      # "Tải về" Docker Image "mysql" với tag "8.0" (phiên bản 8.0)
        docker pull ubuntu:20.04   # "Tải về" Docker Image "ubuntu" với tag "20.04" (phiên bản Ubuntu 20.04)
        docker pull microsoft/dotnet-sdk:7.0 # "Tải về" Docker Image "microsoft/dotnet-sdk" với tag "7.0" (phiên bản .NET SDK 7.0)
        ```

    -   Sau khi "chạy" lệnh `docker pull`, Docker CLI sẽ "hiển thị" "tiến trình" "tải về" các lớp Image và "thông báo" **"Download complete"** (Tải về hoàn tất) khi Image đã được "tải về" thành công.

**Tổng Kết Chương 3:**

-   Bạn đã "khám phá" **Docker Images**, " 'bản thiết kế' " ứng dụng "đóng gói" và " 'khuôn mẫu' " cho Docker Containers.
    -   "Hiểu" **Docker Image là gì** ("ảnh chụp" ứng dụng và môi trường chạy, "bản sao" "hoàn hảo" để "vận chuyển").
    -   "Nắm vững" **"cấu tạo"** bên trong Docker Image (layered filesystem, Base Image, Application Layers, Read-Only Layers, Writable Layer) và "lợi ích" của "kiến trúc" layered filesystem.
    -   "Khám phá" **Docker Hub** - " 'chợ ứng dụng' " Docker "khổng lồ" và "cách" "tìm kiếm", "lọc", và "đánh giá" Docker Images trên Docker Hub.
    -   Học cách "dùng" lệnh **`docker pull`** để "tải về" Docker Images "có sẵn" từ Docker Hub về máy tính của bạn.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 4: Docker Containers - " 'Thực Thể' " Ứng Dụng "Đang Chạy"**. Chúng ta sẽ "đi sâu" vào **Docker Containers**, "hiểu" **Container là gì** và "khác biệt" với Images, "học cách" **"chạy" Docker Containers** từ Docker Images, và **"quản lý" "vòng đời"** của Docker Containers (start, stop, restart, remove).

Bạn có câu hỏi nào về Docker Images này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng bạn trên con đường "chinh phục" Docker.

