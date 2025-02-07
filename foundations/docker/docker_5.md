# Chương 5: Dockerfile - " 'Công Thức' " "Tự Động" "Xây Dựng" Docker Images - " 'Làm Chủ' " "Quy Trình" "Đóng Gói" Ứng Dụng - " 'Viết' " "Bản Thiết Kế" Cho " 'Hộp' " Docker

Chào mừng bạn đến với **Chương 5: Dockerfile - " 'Công Thức' " "Tự Động" "Xây Dựng" Docker Images**! Trong chương này,
chúng ta sẽ "khám phá" **Dockerfile**, " 'công thức' " **"vô cùng quan trọng"** để **"tự động hóa"** quá trình **"xây
dựng" Docker Images**. Chúng ta sẽ "học cách" "viết" Dockerfile, "dùng" các **"lệnh"** Dockerfile "cơ bản", và "thực
hành" **"xây dựng" Docker Images** "riêng" cho ứng dụng của bạn. "Dockerfile" là "chìa khóa" để "làm chủ" "quy trình" "
đóng gói" ứng dụng vào Docker Images một cách "chuyên nghiệp" và "linh hoạt".

**Phần 5: Dockerfile - " 'Công Thức' " "Tự Động" "Xây Dựng" Docker Images - " 'Bản Mô Tả' " Các " 'Bước' " "Đóng Gói"**

**5.1. Dockerfile là gì? - " 'Bản Mô Tả' " Các " 'Bước' " "Xây Dựng" Image - " 'Recipe' " Cho " 'Hộp' " Docker**

- **Dockerfile (Dockerfile) - " 'Công Thức' " "Xây Dựng" Docker Image "Tự Động":**

    - **Dockerfile** (Dockerfile) là một **"file văn bản"** (text file) chứa **"danh sách" các **"lệnh"** (instructions)
      ** mà Docker Engine sẽ **"thực hiện"** **"tuần tự"** (sequentially) để **"tự động" "xây dựng"** (build) **Docker
      Image**.
    - Hãy tưởng tượng Dockerfile như một **" 'công thức nấu ăn' " (recipe)**. "Công thức" "mô tả" **"các bước"** (
      instructions) để "nấu" một món ăn (Docker Image). Docker Engine "đọc" "công thức" (Dockerfile) và "thực hiện" "các
      bước" để "tạo ra" món ăn (Docker Image).
    - Dockerfile "cho phép" bạn **"định nghĩa" "môi trường"** và **"cấu hình"** của Docker Image một cách **"chi tiết"**
      và **"tự động hóa"**. "Không cần" phải "xây dựng" Docker Images "thủ công" bằng các lệnh Docker CLI "rời rạc" (mất
      thời gian và dễ "mắc lỗi").
    - Dockerfile giúp **"tái sản xuất"** (reproducible) quá trình "xây dựng" Docker Image một cách **"nhất quán"** và *
      *"tin cậy"**. Bất kỳ ai có Dockerfile và Docker Engine đều có thể "xây dựng" Docker Image **"giống hệt nhau"** từ
      Dockerfile đó.

- **Dockerfile - " 'Code' " Để " 'Xây Dựng' " Docker Images - " 'Infrastructure as Code' " Cho Docker:**

    - Dockerfile được "viết" bằng **"cú pháp" "đơn giản"** và **"dễ đọc"** (Dockerfile syntax). Mỗi dòng trong
      Dockerfile thường là một **"lệnh"** (instruction) Docker và các **"tham số"** (arguments) cho lệnh đó.
    - Dockerfile được xem như là **" 'code' " để " 'xây dựng' " Docker Images** ( "Infrastructure as Code" cho Docker).
      Bạn có thể **"lưu trữ" Dockerfile** trong **"hệ thống quản lý phiên bản"** (version control system) (ví dụ: Git)
      cùng với code ứng dụng, **"theo dõi"** các "thay đổi" Dockerfile, và **"chia sẻ"** Dockerfile với nhóm phát triển
      để "xây dựng" Docker Images "nhất quán" và "dễ quản lý".

- **"Quy Trình" "Xây Dựng" Docker Image Từ Dockerfile - "Docker Build Process":**

    1. **"Tạo" Dockerfile:** "Tạo" một **"file văn bản"** có tên **`Dockerfile`** (không có phần mở rộng file) trong thư
       mục gốc của dự án ứng dụng của bạn. "Viết" các **"lệnh" Dockerfile** để "mô tả" các "bước" "xây dựng" Docker
       Image.
    2. **"Chạy" Lệnh `docker build`:** Mở command line (Terminal, Command Prompt, PowerShell), "di chuyển" đến thư mục
       chứa Dockerfile, và "chạy" lệnh **`docker build`**.
    3. **Docker Engine "đọc" Dockerfile và "thực hiện" các "lệnh" "tuần tự":** Docker Engine "đọc" Dockerfile từ "đầu
       đến cuối" và "thực hiện" **"từng lệnh"** trong Dockerfile theo **"thứ tự"** "khai báo". Mỗi lệnh trong Dockerfile
       thường "tạo ra" một **"lớp Image mới"** (layer) "chồng lên" các lớp Image "trước đó".
    4. **Docker Engine "tạo ra" Docker Image "cuối cùng":** Sau khi "thực hiện" "xong" tất cả các "lệnh" trong
       Dockerfile, Docker Engine sẽ "tạo ra" Docker Image **"cuối cùng"** và "lưu trữ" Image đó trên máy tính "cục bộ"
       của bạn (local Docker image cache). Bạn có thể "dùng" Docker Image "mới xây dựng" để "chạy" Docker Containers.

**5.2. "Cú Pháp" Dockerfile "Cơ Bản" (FROM, COPY, RUN, CMD, EXPOSE, v.v.) - " 'Ngôn Ngữ' " "Hướng Dẫn" Docker "Xây
Image" - " 'Bảng Chữ Cái' " Dockerfile**

- **Dockerfile Instructions (Lệnh Dockerfile) - " 'Từ Vựng' " Của " 'Ngôn Ngữ' " Dockerfile:**

    - **Dockerfile Instructions** (Lệnh Dockerfile) là các **"từ khóa"** (keywords) "đặc biệt" được "dùng" trong
      Dockerfile để "mô tả" **"các bước"** "xây dựng" Docker Image.
    - Dockerfile Instructions thường được "viết" **"chữ hoa"** (uppercase) (theo "quy ước", không bắt buộc, nhưng "
      nên" "tuân thủ" để "dễ đọc" Dockerfile).
    - "Các lệnh" Dockerfile "cơ bản" và "phổ biến" nhất bao gồm:

    - **`FROM <base_image>[:<tag>]` - " 'Chọn' " Base Image - " 'Nền Tảng' " Để " 'Xây' " Image:**
        - **`FROM`** instruction là **"lệnh 'đầu tiên' "** (first instruction) **"bắt buộc"** trong Dockerfile.
        - `FROM` "xác định" **"Base Image"** (Image Nền) cho Docker Image mà bạn muốn "xây dựng". Base Image là Docker
          Image "có sẵn" (thường từ Docker Hub) mà bạn sẽ "dùng" làm **"nền tảng"** để "xây dựng" Docker Image "riêng"
          của mình.
        - **"Ví dụ":** `FROM ubuntu:latest` ( "dùng" Docker Image "ubuntu" phiên bản "latest" làm Base Image),
          `FROM microsoft/dotnet-sdk:7.0` ( "dùng" Docker Image ".NET SDK 7.0" làm Base Image), `FROM nginx:alpine` ( "
          dùng" Docker Image "nginx" phiên bản "alpine" làm Base Image).

    - **`COPY <source> <destination>` - " 'Sao Chép' " File và Thư Mục Từ " 'Máy Host' " Vào Image:**
        - **`COPY`** instruction "sao chép" (copy) **"file"** hoặc **"thư mục"** từ **"máy host"** (máy tính "xây dựng"
          Docker Image) vào **"Docker Image"**.
        - "Dùng" để **"copy" code ứng dụng**, **"file cấu hình"**, **"tài nguyên"** (assets) (ví dụ: hình ảnh, CSS,
          JavaScript, v.v.) từ máy host vào Docker Image.

        - **"Ví dụ":** `COPY . /app` ( "copy" **"thư mục hiện tại"** (`.`) trên máy host vào thư mục `/app` trong Docker
          Image), `COPY app.config /app/config/app.config` ( "copy" file `app.config` trên máy host vào thư mục
          `/app/config` trong Docker Image).

    - **`RUN <command>` - " 'Thực Thi' " Lệnh Trong Image Trong Quá Trình "Xây Dựng":**
        - **`RUN`** instruction "thực thi" một **"lệnh"** (command) **"bên trong" Docker Image** trong quá trình **"xây
          dựng"** Docker Image (docker build).
        - "Dùng" để **"cài đặt" "phần mềm"**, **"thư viện"**, **"dependencies"**, **"cấu hình" "môi trường"**, hoặc "
          thực hiện" các "tác vụ" "xây dựng" khác **"bên trong" Docker Image**.
        - **"Ví dụ":** `RUN apt-get update && apt-get install -y nginx` ( "thực thi" lệnh `apt-get update` và
          `apt-get install -y nginx` để "cài đặt" Nginx web server trong Docker Image (dùng hệ điều hành
          Debian/Ubuntu)), `RUN dotnet restore` ( "thực thi" lệnh `dotnet restore` để "tải về" NuGet packages và "
          restore" dependencies cho ứng dụng .NET trong Docker Image).

    - **`CMD ["executable", "param1", "param2", ...]` - " 'Lệnh' " "Mặc Định" Khi "Chạy" Container:**
        - **`CMD`** instruction "xác định" **"lệnh"** (command) **"mặc định"** sẽ được "thực thi" khi bạn **"chạy"**
          Docker Container từ Docker Image ( `docker run <image_name>` ).
        - "Chỉ có thể" có **"một" `CMD` instruction "duy nhất"** trong Dockerfile. Nếu có "nhiều" `CMD` instructions,
          chỉ `CMD` instruction **"cuối cùng"** sẽ có "hiệu lực".
        - **"Ví dụ":** `CMD ["nginx", "-g", "daemon off;"]` ( "lệnh" "mặc định" để "chạy" Nginx web server trong
          Container), `CMD ["dotnet", "WebAppMvc.dll"]` ( "lệnh" "mặc định" để "chạy" ứng dụng .NET "WebAppMvc.dll"
          trong Container).

    - **`EXPOSE <port> [port/tcp|port/udp]` - " 'Mở Cổng' " Container Để " 'Truy Cập' " Từ Bên Ngoài:**
        - **`EXPOSE`** instruction "khai báo" **"port"** mà Docker Container sẽ **"lắng nghe"** (listen) **"mạng"** bên
          trong Container.
        - `EXPOSE` **"không 'thực sự' " "mở" port** của Container ra "bên ngoài" Container. `EXPOSE` chỉ là **" '
          metadata' " (thông tin)** về port, "cho Docker Engine" và "người dùng" "biết" Container sẽ "lắng nghe" trên
          port nào.
        - Để **" 'mở' " port** của Container ra "bên ngoài" và "cho phép" "truy cập" Container từ "máy host" (hoặc từ
          mạng bên ngoài), bạn cần "dùng" **`-p` hoặc `--publish` "tùy chọn"** của lệnh `docker run` (Port Mapping - Ánh
          Xạ Port - như đã "học" ở Chương 4).
        - **"Ví dụ":** `EXPOSE 80` ( "khai báo" Container sẽ "lắng nghe" trên port 80 (mặc định TCP)),
          `EXPOSE 8080/tcp` ( "khai báo" Container sẽ "lắng nghe" trên port 8080 giao thức TCP), `EXPOSE 53/udp` ( "khai
          báo" Container sẽ "lắng nghe" trên port 53 giao thức UDP).

- **"Các Lệnh" Dockerfile "Khác" (Tùy Chọn):**

    - **`WORKDIR <path>` (Working Directory - Thư Mục Làm Việc):** "Thiết lập" **"thư mục làm việc"** "mặc định" bên
      trong Docker Image. Các lệnh `RUN`, `CMD`, `COPY`, `ADD` "sau" `WORKDIR` sẽ được "thực thi" trong "thư mục làm
      việc" đã "thiết lập". "Tiện lợi" để "tránh" phải "gõ" "đường dẫn" "dài dòng" trong các lệnh Dockerfile.
    - **`ENV <key> <value>` (Environment Variables - Biến Môi Trường):** "Set" **"biến môi trường"** trong Docker Image.
      Biến môi trường có thể được "dùng" để "cấu hình" ứng dụng trong Container (ví dụ: database connection string, API
      keys, v.v.).
    - **`VOLUME <path>` (Volumes - Ổ Đĩa Ảo):** "Tạo" một **"volume"** (ổ đĩa ảo) "anonymous" (vô danh) tại đường dẫn
      `<path>` trong Docker Image. Volumes "dùng" để "lưu trữ" dữ liệu Container **"bên ngoài" Container** (persistent
      data) và "chia sẻ" dữ liệu giữa Container và host. (Thường dùng "tùy chọn" `-v` hoặc `--volume` của lệnh
      `docker run` để "gắn" volumes "rõ ràng" hơn).

**5.3. "Xây Dựng" Docker Image Từ Dockerfile (`docker build`) - " 'Biên Dịch' " Dockerfile Thành Image - " 'Biến' " "
Công Thức" Thành " 'Hộp' " Docker**

- **"Lệnh 'Biên Dịch' " Dockerfile - `docker build` - " 'Biến' " Dockerfile Thành Docker Image "Thực Tế":**

    - **`docker build`** là lệnh Docker CLI "quan trọng" để **"xây dựng" Docker Image** từ **Dockerfile**.
    - Lệnh `docker build` "đọc" Dockerfile, "thực hiện" **"từng lệnh"** trong Dockerfile theo "thứ tự", và "tạo ra"
      Docker Image "cuối cùng".

- **"Cú Pháp" Lệnh `docker build` - " 'Chỉ Định' " "Dockerfile" và " 'Đặt Tên' " Image:**

  ```bash
  docker build [OPTIONS] <path_to_dockerfile>
  ```

    - **`[OPTIONS]`:** Các **"tùy chọn"** (options) để "cấu hình" quá trình "xây dựng" Image. "Phổ biến" nhất là "tùy
      chọn" **`-t` hoặc `--tag`** để **"đặt tên"** và **"tag"** cho Docker Image "mới" "xây dựng".

        - **`-t` hoặc `--tag <image_name>[:<tag>]` (Tag Image - Đặt Tên và Tag Image):** "Đặt tên" và "tag" cho Docker
          Image "mới" "xây dựng". "Nên" "đặt tên" Image (ví dụ: `my-app-image`) và "tag" Image (ví dụ: `v1.0`, `latest`)
          để "dễ dàng" "quản lý" và "phân biệt" các Docker Images "khác nhau". Nếu "không dùng" `-t` hoặc `--tag`
          option, Docker sẽ "tạo" Image "vô danh" (untagged image) (khó "quản lý").

    - **`<path_to_dockerfile>`:** **"Đường dẫn"** đến **"Dockerfile"** hoặc **"thư mục chứa Dockerfile"**. "Bắt buộc"
      phải có.
        - Nếu "đường dẫn" là **"đường dẫn" đến **"file Dockerfile"** "cụ thể"**, "dùng" option **`-f`
          hoặc `--file <path_to_dockerfile>`** để "chỉ định" "đường dẫn" file Dockerfile. (Ví dụ:
          `docker build -f /path/to/my/Dockerfile .`).
        - Nếu "đường dẫn" là **"đường dẫn" đến **"thư mục" chứa Dockerfile** (Dockerfile phải có tên `Dockerfile` và "
          đặt" trong "thư mục" đó), bạn có thể "dùng" **"dấu chấm" `.`** để "biểu thị" "thư mục hiện tại"** là "
          context" "xây dựng" và "chứa" Dockerfile. (Ví dụ: `docker build .`). (Phổ biến nhất - "đơn giản" và "tiện
          lợi").

- **"Context" "Xây Dựng" Docker Image (Build Context) - " 'Vùng' " "Nguyên Liệu" Để " 'Xây' " Image:**

    - **Build Context** (Context "Xây Dựng") là **"tập hợp" các "file" và "thư mục"** trên **"máy host"** mà Docker
      Engine có thể **"truy cập"** trong quá trình "xây dựng" Docker Image (docker build).
    - "Đường dẫn" **`<path_to_dockerfile>`** trong lệnh `docker build` "xác định" **"thư mục 'gốc' " của "build context"
      **. Docker Engine sẽ "coi" thư mục này (và các thư mục "con" của nó) là **" 'vùng' " "nguyên liệu"** (source code,
      thư viện, assets, v.v.) để " 'xây dựng' " Docker Image.
    - Lệnh Dockerfile **`COPY`** và **`ADD`** chỉ có thể "copy" file và thư mục **"từ 'build context' " vào Docker Image
      **. "Không thể" "copy" file và thư mục "từ 'bên ngoài' " "build context". "Đảm bảo" "tính 'đóng gói' " và " 'tái
      sản xuất' " của quá trình "xây dựng" Image.
    - "Quy ước" tốt là "đặt" **Dockerfile** trong **"thư mục gốc"** của dự án ứng dụng của bạn và "dùng" **"dấu
      chấm" `.`** làm "đường dẫn" "build context" trong lệnh `docker build` (ví dụ:
      `docker build -t my-app-image:v1.0 .`). "Thư mục gốc" của dự án ứng dụng sẽ trở thành "build context".

- **"Ví Dụ" "Xây Dựng" Docker Image Từ Dockerfile (Ví dụ: Ứng dụng Web ASP.NET Core MVC):**

    1. **"Tạo" thư mục dự án** (ví dụ: `WebAppMvcDocker`) và "di chuyển" đến thư mục này trong command line (Terminal,
       Command Prompt, PowerShell).
    2. **"Tạo" file `Dockerfile`** trong thư mục dự án (ví dụ: `WebAppMvcDocker/Dockerfile`) và "viết" code Dockerfile "
       sau" (ví dụ: Dockerfile "đơn giản" cho ứng dụng ASP.NET Core MVC):

       ```dockerfile
       FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
       WORKDIR /app

       # Copy csproj and restore as distinct layers
       COPY *.csproj ./
       RUN dotnet restore

       # Copy everything else and build
       COPY . ./
       RUN dotnet publish -c Release -o out

       # Build runtime image
       FROM mcr.microsoft.com/dotnet/aspnet:7.0
       WORKDIR /app
       COPY --from=build-env /app/out .
       ENTRYPOINT ["dotnet", "WebAppMvc.dll"]
       ```

    3. **"Chạy" lệnh `docker build`** trong thư mục dự án (chứa Dockerfile) để "xây dựng" Docker Image:

       ```bash
       docker build -t webappmvc-image:v1.0 . # "Xây dựng" Docker Image, "đặt tên" là "webappmvc-image" và tag là "v1.0", "build context" là thư mục hiện tại (.)
       ```

        - `-t webappmvc-image:v1.0`: "Tùy chọn" `-t` để "đặt tên" Docker Image là `webappmvc-image` và tag là `v1.0`.
        - `.`: "Đường dẫn" "build context" là thư mục hiện tại (thư mục chứa Dockerfile).

    4. **"Chờ" Docker Engine "xây dựng" Docker Image:** Docker Engine sẽ "đọc" Dockerfile, "thực hiện" "từng lệnh" trong
       Dockerfile, "tải về" Base Image (nếu cần), "copy" code ứng dụng, "cài đặt" dependencies, "publish" ứng dụng .NET,
       và "tạo ra" Docker Image "cuối cùng" `webappmvc-image:v1.0`. Quá trình "xây dựng" có thể "mất vài phút" (tùy
       thuộc vào "kích thước" ứng dụng, "tốc độ internet", v.v.).

    5. **"Kiểm tra" Docker Images "đã xây dựng" bằng lệnh `docker images`:**

       ```bash
       docker images
       ```

        - Bạn sẽ thấy Docker Image "mới" `webappmvc-image:v1.0` trong "danh sách" Docker Images "đã tải về" trên máy
          tính của bạn.

**5.4. "Tối Ưu Hóa" Dockerfile Để "Tạo Ra" Images "Nhỏ Gọn" và "Nhanh Chóng" - " 'Nghệ Thuật' " "Xây Image" "Chuyên
Nghiệp" - " 'Đẹp', 'Gọn', 'Nhẹ', và 'Nhanh' "**

- **"Tại Sao" Cần "Tối Ưu Hóa" Dockerfile? - "Images 'Lớn' ", "Build 'Chậm' ", "Triển Khai 'Khó' ":**

    - Docker Images "lớn" (large image size) có thể "gây ra" các "vấn đề" về:
        - **"Dung lượng lưu trữ" "lớn":** "Tốn kém" "dung lượng ổ cứng" để "lưu trữ" Images trên máy tính và Docker
          Registry.
        - **"Thời gian tải về" Images "lâu":** "Chậm" quá trình "triển khai" ứng dụng (vì phải "tải về" Images "lớn" qua
          mạng).
        - **"Băng thông mạng" "tốn kém":** "Tăng" chi phí "băng thông mạng" khi "tải về" Images "lớn" từ Docker
          Registry (đặc biệt khi "mở rộng" ứng dụng trên nhiều máy chủ).
        - **"Bảo mật" "kém hơn":** Docker Images "lớn" có thể "chứa" nhiều "thành phần" "không cần thiết", "tăng" "diện
          tích tấn công" (attack surface) và "nguy cơ" "bảo mật".
        - **"Build time" "lâu":** Dockerfile "không tối ưu" có thể làm quá trình "xây dựng" Docker Image (docker build)
          trở nên **"chậm chạp"**.

- **"Các 'Kỹ Thuật' " "Tối Ưu Hóa" Dockerfile Để "Tạo Ra" Images "Nhỏ Gọn" và "Nhanh Chóng":**

    - **"Sử Dụng" "Base Images 'Nhỏ Gọn' ":** "Chọn" **Base Images "tối giản"** (minimal base images) (ví dụ: Alpine
      Linux, Debian Slim, Distroless Images) thay vì các Base Images "đầy đủ" (full-fledged images) (ví dụ: Ubuntu,
      CentOS, Windows Server Core). Minimal base images "chỉ chứa" **"những thành phần 'cần thiết' " "tối thiểu"** để "
      chạy" ứng dụng, "giảm" "đáng kể" "kích thước" Docker Image "cuối cùng".

    - **"Multi-Stage Builds" (Xây Dựng "Đa Giai Đoạn"):** "Dùng" **"Multi-Stage Builds"** để "chia" quá trình "xây dựng"
      Docker Image thành **"nhiều 'giai đoạn' "** (stages).
        - **"Giai đoạn 'build' " (build stage):** "Tập trung" vào "xây dựng" và "biên dịch" ứng dụng (ví dụ: "cài đặt"
          SDK, "restore" dependencies, "build" code, "chạy" tests). "Dùng" Base Images "lớn" "chứa" các "công cụ" "phát
          triển" (SDK, build tools, v.v.).
        - **"Giai đoạn 'runtime' " (runtime stage):** "Tập trung" vào "chạy" ứng dụng "production". "Dùng" Base Images "
          nhỏ gọn" "chỉ chứa" **"runtime"** "cần thiết" để "chạy" ứng dụng (ví dụ: .NET runtime, Node.js runtime,
          JRE). "Copy" **"artifacts" "cần thiết"** (ứng dụng đã "build", dependencies "runtime") từ "giai đoạn 'build' "
          sang "giai đoạn 'runtime' ". "Không copy" các "công cụ" "phát triển" và "dependencies" "không cần thiết" vào
          Image "cuối cùng".
        - **"Kết quả":** Docker Image "cuối cùng" (từ "giai đoạn 'runtime' ") "chỉ chứa" **"những gì 'thực sự cần' "
          để "chạy" ứng dụng**, "giảm" "đáng kể" "kích thước" Image "cuối cùng".

      ```dockerfile
      # Giai đoạn "build" (build stage)
      FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build-env
      WORKDIR /app
      COPY *.csproj ./
      RUN dotnet restore
      COPY . ./
      RUN dotnet publish -c Release -o out

      # Giai đoạn "runtime" (runtime stage) - "bắt đầu" từ Base Image "nhỏ gọn" "aspnet:7.0"
      FROM mcr.microsoft.com/dotnet/aspnet:7.0
      WORKDIR /app
      COPY --from=build-env /app/out . # "Copy" "artifacts" từ "giai đoạn 'build' " (chỉ copy thư mục "out" chứa ứng dụng đã "publish", không copy SDK, build tools, v.v.)
      ENTRYPOINT ["dotnet", "WebAppMvc.dll"]
      ```

    - **"Layer Caching" và "Tối Ưu Thứ Tự Lệnh" Trong Dockerfile:** Docker Engine "cache" (lưu trữ tạm) "kết quả" của "
      từng lệnh" trong Dockerfile thành các lớp Image. "Tận dụng" **"layer caching"** để "tăng tốc" quá trình "xây dựng"
      Image bằng cách:
        - "Đặt" các lệnh Dockerfile **"ít 'thay đổi' " "lên 'trước' "** và các lệnh **"thay đổi" "thường xuyên" "xuống '
          sau' "** trong Dockerfile. Docker Engine sẽ "tái sử dụng" các lớp Image "đã cache" cho các lệnh "không bị '
          thay đổi' ", "chỉ xây dựng" lại các lớp Image "mới" cho các lệnh "thay đổi" (và các lớp "phụ thuộc" vào các
          lớp "thay đổi").
        - **"Tránh" "thay đổi" các file "nguồn" "không cần thiết"** trong "build context" (ví dụ: "thời gian", "
          metadata") vì có thể làm "vô hiệu hóa" cache layer.
        - "Dùng" **`.dockerignore` file** để "loại trừ" các file và thư mục "không cần thiết" khỏi "build context" (ví
          dụ: `obj`, `bin`, `node_modules`, v.v.). "Giảm" "kích thước" "build context" và "tăng" "hiệu năng" `COPY`
          lệnh.

    - **"Multi-Stage Builds"** (đã nói ở trên) cũng giúp "tận dụng" "layer caching" "hiệu quả" hơn. "Giai đoạn 'build' "
      có thể "thay đổi" "thường xuyên" (code changes, dependency updates), nhưng "giai đoạn 'runtime' " thường **"ổn
      định"** hơn (chỉ "copy" "artifacts" "cuối cùng", "không thay đổi" runtime environment). Docker Engine có thể "tái
      sử dụng" các lớp Image "đã cache" của "giai đoạn 'runtime' " trong các lần "xây dựng" Image "sau".

**Tổng Kết Chương 5:**

- Bạn đã "khám phá" **Dockerfile**, " 'công thức' " "xây dựng" Docker Images "tự động" và " 'bản thiết kế' " ứng dụng "
  đóng gói".
    - "Hiểu" **Dockerfile là gì** ("file văn bản" "mô tả" "các bước" "xây dựng" Image, "Infrastructure as Code" cho
      Docker).
    - "Nắm vững" **"cú pháp" Dockerfile "cơ bản"** (FROM, COPY, RUN, CMD, EXPOSE, v.v.) và "ý nghĩa" của từng "lệnh".
    - Học cách "dùng" lệnh **`docker build`** để "xây dựng" Docker Images từ Dockerfiles.
    - Biết các **"kỹ thuật" "tối ưu hóa" Dockerfile** (Base Images "nhỏ gọn", Multi-Stage Builds, Layer Caching) để "tạo
      ra" Images "nhỏ gọn" và "nhanh chóng".

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 6: Docker Compose - " 'Nhạc Trưởng' " Cho Ứng Dụng "Đa Container"**. Chúng ta sẽ "học
cách" "dùng" **Docker Compose** để "định nghĩa" và "quản lý" các ứng dụng **"đa container"** (multi-container
applications), "điều phối" các Containers "phối hợp" với nhau để "xây dựng" các ứng dụng Docker "phức tạp" hơn.

Bạn có câu hỏi nào về Dockerfile này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành" cùng
bạn trên con đường "chinh phục" Docker.

