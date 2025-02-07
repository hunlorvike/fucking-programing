# Chương 6: Docker Compose - " 'Nhạc Trưởng' " Cho Ứng Dụng "Đa Container" - " 'Điều Phối' " Các Containers "Phối Hợp" - " 'Xây Dựng' " Ứng Dụng Docker "Phức Tạp" "Dễ Dàng"

Chào mừng bạn đến với **Chương 6: Docker Compose - " 'Nhạc Trưởng' " Cho Ứng Dụng "Đa Container"**! Trong chương này,
chúng ta sẽ "khám phá" **Docker Compose**, "công cụ" **"không thể thiếu"** để "quản lý" các ứng dụng **"đa container"
** (multi-container applications). Chúng ta sẽ "học cách" "dùng" Docker Compose để "định nghĩa" ứng dụng "đa container"
bằng file **`docker-compose.yml`**, và "điều phối" các Containers "phối hợp" với nhau một cách "dễ dàng" và "hiệu
quả". "Docker Compose" là "nhạc trưởng" "điều khiển" "dàn nhạc" Docker Containers, giúp bạn "xây dựng" ứng dụng Docker "
phức tạp" như "chơi Lego".

**Phần 6: Docker Compose - " 'Nhạc Trưởng' " Cho Ứng Dụng "Đa Container" - " 'Điều Phối' " Các Containers "Phối Hợp"**

**6.1. Docker Compose là gì? - " 'Công Cụ' " "Quản Lý" Ứng Dụng "Đa Container" - " 'Chỉ Huy' " "Dàn Nhạc" Containers "
Phức Tạp"**

- **Docker Compose (Docker Compose) - " 'Đạo Diễn' " Cho " 'Vở Kịch' " Ứng Dụng "Đa Container":**

    - **Docker Compose** (Docker Compose) là một **"công cụ"** của Docker để **"định nghĩa"** và **"quản lý"** các ứng
      dụng **"đa container"** (multi-container applications).
    - Ứng dụng "đa container" là ứng dụng được "xây dựng" từ **"nhiều" Docker Containers "phối hợp"** với nhau để "thực
      hiện" các "chức năng" "hoàn chỉnh" của ứng dụng. (Ví dụ: ứng dụng web "hiện đại" thường bao gồm web server
      container, application server container, database server container, cache server container, message queue
      container, v.v.).
    - Docker Compose "cho phép" bạn **"định nghĩa" "toàn bộ" "cấu hình"** của ứng dụng "đa container" (danh sách
      containers, networking, volumes, dependencies, v.v.) trong một **"file duy nhất"** ( `docker-compose.yml` file) và
      **"quản lý"** ứng dụng "đa container" như một **"thể thống nhất"**.
    - Hãy tưởng tượng Docker Compose như một **" 'đạo diễn' "** của một **" 'vở kịch' " ứng dụng "đa container"**. "Đạo
      diễn" (Docker Compose) "chỉ huy" **"dàn diễn viên"** (Docker Containers) "diễn xuất" "phối hợp" với nhau để "dựng
      nên" một "vở kịch" "hoàn chỉnh" (ứng dụng "đa container" "hoạt động" "nhịp nhàng").

- **"Khi Nào" Cần "Dùng" Docker Compose? - "Khi Ứng Dụng "Lớn" và "Phức Tạp", "Gồm Nhiều Containers":**

    - **Ứng dụng web "hiện đại"** (modern web applications) thường được "xây dựng" theo kiến trúc **"microservices"**
      hoặc kiến trúc **"đa tầng"** (multi-tier architecture), "gồm" **"nhiều" Docker Containers "phối hợp"** với nhau. (
      Ví dụ: web app với front-end container, back-end API container, database container, cache container, v.v.).
    - Khi bạn muốn **"quản lý"** và **"vận hành"** các ứng dụng "đa container" một cách **"dễ dàng"** và **"hiệu quả"
      **. "Khởi động", "dừng", "khởi động lại", "mở rộng", và "xóa" **"toàn bộ" ứng dụng "đa container"** chỉ với **"một
      lệnh duy nhất"**.
    - Khi bạn muốn **"định nghĩa"** và **"cấu hình" "mối quan hệ"** giữa các Containers (ví dụ: "networking" - mạng, "
      volumes" - ổ đĩa ảo, "dependencies" - phụ thuộc, v.v.).
    - Khi bạn muốn **"phát triển"**, **"kiểm thử"**, và **"triển khai"** ứng dụng "đa container" một cách **"nhất quán"
      ** và **"dễ dàng"** giữa các môi trường khác nhau (development, testing, staging, production).

- **"Docker Compose 'Không Phải' " Là "Orchestration Tool" "Cho Production" "Quy Mô Lớn":**

    - Docker Compose **"chủ yếu"** được "dùng" cho **"phát triển"** (development), **"kiểm thử"** (testing), và **"
      staging"** environments. "Không được 'thiết kế' " để "quản lý" ứng dụng "đa container" **"production"** "quy mô
      lớn" (large-scale production environments) "yêu cầu" **"khả năng mở rộng"**, **"độ tin cậy"**, và **"tính sẵn sàng
      cao"**.
    - Cho ứng dụng "production" "quy mô lớn", bạn nên "dùng" các **"Docker Orchestration Tools"** "mạnh mẽ" hơn (ví dụ:
      **Kubernetes**, Docker Swarm). Docker Orchestration Tools "cung cấp" các "tính năng" "nâng cao" để "quản lý"
      Containers "quy mô lớn" (load balancing, auto-scaling, auto-healing, rolling updates, service discovery, v.v.).

**6.2. `docker-compose.yml` File - " 'Bản Nhạc' " Cho Ứng Dụng "Đa Container" - " 'Kịch Bản' " "Điều Phối" Containers**

- **`docker-compose.yml` File - " 'Trung Tâm' " "Cấu Hình" Ứng Dụng "Đa Container":**

    - **`docker-compose.yml`** là một file **YAML** (YAML Ain't Markup Language) được "dùng" bởi Docker Compose để **"
      định nghĩa" "cấu hình"** của ứng dụng **"đa container"**.
    - `docker-compose.yml` file "mô tả" **"dàn nhạc" Containers** của bạn - **"danh sách"** các Containers, **"Images"**
      mà các Containers sẽ "dùng", **"networking"** (mạng) giữa các Containers, **"volumes"** (ổ đĩa ảo) để "lưu trữ" dữ
      liệu, **"ports"** để "expose" Containers ra "bên ngoài", **"environment variables"** để "cấu hình" Containers, **"
      dependencies"** (phụ thuộc) giữa các Containers, v.v.
    - `docker-compose.yml` file là **" 'bản nhạc' "** (score) hoặc **" 'kịch bản' "** (script) để Docker Compose "dựa
      vào" đó để **" 'điều phối' "** và **" 'quản lý' "** ứng dụng "đa container".

- **"Cấu Trúc" "Cơ Bản" Của `docker-compose.yml` File:**

    - **`version: '3.8'` (hoặc phiên bản khác):** "Phiên bản" Docker Compose file format. "Xác định" "phiên bản" Docker
      Compose file format mà bạn đang "dùng". "Nên" "dùng" phiên bản "mới nhất" "ổn định" (ví dụ: `'3.8'`, `'3.9'`,
      `'3.x'`).

    - **`services:`:** "Section" **"bắt buộc"** để "định nghĩa" **"danh sách" Docker Containers** (services) của ứng
      dụng. Mỗi "service" (container) được "định nghĩa" bằng một **"block"** (khối) "con" dưới section `services:`. "
      Tên" của "block" "con" (ví dụ: `web`, `api`, `database`, `redis`) là **"tên service"** (container name).

        - **"Cấu hình" "cho từng service" (container):** Bên trong mỗi "block" service, bạn "định nghĩa" các "tùy
          chọn" "cấu hình" cho service đó:
            - **`image:`:** "Tên" Docker Image mà service sẽ "dùng" (ví dụ: `nginx:latest`, `mysql:8.0`,
              `my-app-image:v1.0`).
            - **`build:`:** "Đường dẫn" đến **"thư mục chứa Dockerfile"** để Docker Compose "tự động" "xây dựng" Docker
              Image cho service (thay vì "dùng" Image "có sẵn" từ Docker Hub).
                - `context: .` ( "thư mục hiện tại" là "context" "xây dựng").
                - `dockerfile: Dockerfile-dev` ( "tên file Dockerfile" là `Dockerfile-dev`).
            - **`ports:`:** "Port mappings" (ánh xạ port) - "ánh xạ" port của Container vào port của host (ví dụ:
              `- "8080:80"` - "ánh xạ" port 80 của container vào port 8080 của host).
            - **`volumes:`:** "Volume mappings" (gắn volume) - "gắn" volume từ host vào container (ví dụ:
              `- ./data:/var/lib/mysql` - "gắn" thư mục `./data` trên host vào thư mục `/var/lib/mysql` trong
              container).
            - **`environment:`:** "Environment variables" (biến môi trường) - "set" biến môi trường cho container (ví
              dụ: `DATABASE_URL: mysql://user:password@host:port/database`).
            - **`depends_on:`:** "Dependencies" (phụ thuộc) - "xác định" **"thứ tự" "khởi động"** các services (ví dụ:
              service `web` "phụ thuộc" vào service `database`, `database` phải được "khởi động" "trước" `web`).
            - **`networks:`:** "Networks" (mạng) - "kết nối" service vào một hoặc nhiều Docker Networks.
            - **`restart:`:** "Restart policy" - "quy định" **"cách" Docker Compose "khởi động lại" Container** khi
              Container bị "lỗi" hoặc "dừng lại" (ví dụ: `always` - "luôn luôn" "khởi động lại", `on-failure` - "khởi
              động lại" khi "lỗi", `no` - "không" "khởi động lại").
            - ... (và nhiều "tùy chọn" "cấu hình" khác - tham khảo tài liệu Docker Compose để biết thêm chi tiết).

    - **`networks:` (tùy chọn):** "Section" "tùy chọn" để "định nghĩa" **Docker Networks** "riêng" cho ứng dụng "đa
      container". Docker Networks "cho phép" các Containers trong cùng một network "giao tiếp" với nhau qua "tên
      service" (service name) (service discovery).

    - **`volumes:` (tùy chọn):** "Section" "tùy chọn" để "định nghĩa" **Docker Volumes** "đặt tên" (named volumes) "dùng
      chung" cho ứng dụng "đa container". Named Volumes "giúp" "quản lý" volumes "dễ dàng" hơn và "chia sẻ" volumes giữa
      các services.

- **"Ví Dụ" `docker-compose.yml` File - Ứng Dụng Web ASP.NET Core MVC Với Database MySQL:**

  ```yaml
  version: '3.8' # Phiên bản Docker Compose file format

  services: # Section "services" - "định nghĩa" "danh sách" containers (services)

    web: # Service "web" - Container "chạy" ứng dụng web ASP.NET Core MVC
      image: my-webapp-image:v1.0 # "Dùng" Docker Image "my-webapp-image:v1.0" (đã "xây dựng" ở Chương 5)
      ports: # "Port mappings" - "ánh xạ" port
        - "8080:80" # "Ánh xạ" port 80 của container vào port 8080 của host
      depends_on: # "Dependencies" - service "web" "phụ thuộc" vào service "database"
        - database
      environment: # "Environment variables" - "set" biến môi trường cho container "web"
        - ASPNETCORE_ENVIRONMENT=Development # "Set" ASPNETCORE_ENVIRONMENT=Development (chạy ứng dụng ở môi trường Development)
        - ConnectionStrings__DefaultConnection=Server=database;Database=WebAppMvcDb;User=root;Password=your_mysql_root_password; # "Set" connection string database

    database: # Service "database" - Container "chạy" database server MySQL
      image: mysql:8.0 # "Dùng" Docker Image "mysql:8.0" từ Docker Hub
      ports: # "Port mappings" - "ánh xạ" port
        - "3306:3306" # "Ánh xạ" port 3306 của container vào port 3306 của host
      environment: # "Environment variables" - "set" biến môi trường cho container "database"
        - MYSQL_ROOT_PASSWORD=your_mysql_root_password # "Set" mật khẩu root MySQL
        - MYSQL_DATABASE=WebAppMvcDb # "Set" tên database MySQL

  networks: # Section "networks" - "định nghĩa" Docker Networks "riêng" cho ứng dụng
    app-network: # Network "app-network"
      driver: bridge # "Driver" network là "bridge" (Docker bridge network)
  ```

**6.3. "Khởi Động" Ứng Dụng "Đa Container" Với Docker Compose (`docker-compose up`) - " 'Chỉ Huy' " "Dàn Nhạc"
Containers - " 'Bấm Nút Play', Ứng Dụng "Chạy" "**

- **"Lệnh 'Thần Kỳ' " `docker-compose up` - " 'Khởi Động' " "Toàn Bộ" Ứng Dụng "Đa Container" Chỉ Với "Một Lệnh":**

    - **`docker-compose up`** là lệnh Docker Compose **"quan trọng nhất"** và **"phổ biến nhất"**. "Dùng" để **"khởi
      động"** và **"chạy" "toàn bộ" ứng dụng "đa container"** được "định nghĩa" trong file `docker-compose.yml`.
    - Lệnh `docker-compose up` "thực hiện" **"nhiều công việc"** "phức tạp" "tự động":
        1. **"Đọc" file `docker-compose.yml`:** Docker Compose "đọc" file `docker-compose.yml` để "hiểu" "cấu hình" ứng
           dụng "đa container" (danh sách services, networking, volumes, v.v.).
        2. **"Xây dựng" Docker Images (nếu cần):** Nếu trong `docker-compose.yml` file có "định nghĩa" `build:` cho một
           service, Docker Compose sẽ "tự động" "xây dựng" Docker Image cho service đó (dùng Dockerfile "chỉ định" trong
           `build: context:`).
        3. **"Tải về" Docker Images (nếu cần):** Nếu Docker Images "chỉ định" trong `image:` "chưa có" trên máy tính "
           cục bộ", Docker Compose sẽ "tự động" "tải về" Docker Images đó từ Docker Hub (hoặc registry khác).
        4. **"Tạo" Docker Networks (nếu có):** Docker Compose "tạo" Docker Networks được "định nghĩa" trong section
           `networks:` (nếu chưa có).
        5. **"Tạo" Docker Volumes (nếu có):** Docker Compose "tạo" Docker Volumes được "định nghĩa" trong section
           `volumes:` (nếu chưa có).
        6. **"Tạo" và "Khởi động" Docker Containers:** Docker Compose "tạo ra" và "khởi động" Docker Containers cho **"
           tất cả" các services** được "định nghĩa" trong section `services:`. Docker Compose sẽ "đảm bảo" các
           Containers được "khởi động" theo **"thứ tự" "phụ thuộc"** (dependencies) đã "định nghĩa" trong `depends_on:`.
           Docker Compose cũng sẽ "kết nối" các Containers vào các Docker Networks và "gắn" Volumes theo "cấu hình" đã "
           định nghĩa".
        7. **"Hiển thị" "logs" (logs) của Containers (nếu "chạy" ở chế độ "foreground"):** Nếu bạn "chạy" lệnh
           `docker-compose up` **"không có" `-d` hoặc `--detach` option** (chế độ "foreground" - mặc định), Docker
           Compose sẽ "hiển thị" **"logs"** (output) của **"tất cả" các Containers** "trên console" "theo thời gian
           thực". "Tiện lợi" để "theo dõi" quá trình "khởi động" và "hoạt động" của ứng dụng "đa container" trong quá
           trình "phát triển" và "debug".

- **"Cách 'Khởi Động' " Ứng Dụng "Đa Container" Với `docker-compose up`:**

    1. Mở command line (Terminal, Command Prompt, PowerShell).
    2. "Di chuyển" đến **"thư mục chứa file `docker-compose.yml`"** của ứng dụng "đa container" (ví dụ: thư mục gốc của
       dự án ứng dụng).
    3. "Chạy" lệnh **`docker-compose up`** (để "khởi động" ứng dụng ở chế độ "foreground" và "xem" logs trên console)
       hoặc **`docker-compose up -d`** (để "khởi động" ứng dụng ở chế độ "detached" (nền) và "chạy" "ngầm").
    4. Bấm **Enter** và "chờ" Docker Compose "khởi động" ứng dụng "đa container". Docker Compose sẽ "hiển thị" "tiến
       trình" "khởi động" các services và "thông báo" khi ứng dụng đã "khởi động" "thành công".

- **"Truy Cập" Ứng Dụng Web "Đa Container" Trên Trình Duyệt Web:**

    - Sau khi ứng dụng "đa container" đã "khởi động" "thành công" với `docker-compose up`, bạn có thể "truy cập" ứng
      dụng web trên trình duyệt web bằng cách "dùng" URL **`http://localhost:<host_port>`**, với `<host_port>` là **"
      port" "ánh xạ"** (port mapping) "đã định nghĩa" trong section `ports:` của service `web` (hoặc service "chứa" ứng
      dụng web) trong file `docker-compose.yml`. (Ví dụ: nếu bạn "ánh xạ" port `8080:80`, URL sẽ là
      `http://localhost:8080`).

**6.4. "Quản Lý" Ứng Dụng "Đa Container" Với Docker Compose (`docker-compose down`, `docker-compose logs`, v.v.) - " '
Điều Hành' " "Ứng Dụng Phức Tạp" - " 'Tắt', 'Xem Logs', 'Xóa', v.v.**

- **"Các Lệnh" Docker Compose "Quản Lý" Ứng Dụng "Đa Container":**

    - **`docker-compose down` - "Dừng" và "Xóa" Ứng Dụng "Đa Container":** "Dừng" **"tất cả" các Containers** của ứng
      dụng "đa container" và **"xóa"** các Containers, Networks, Volumes đã được "tạo ra" bởi `docker-compose up`. "
      Dùng" để **"dọn dẹp"** ứng dụng "đa container" sau khi "dùng" xong hoặc khi muốn "khởi động lại" ứng dụng "từ
      đầu".

      ```bash
      docker-compose down # "Dừng" và "xóa" ứng dụng "đa container"
      ```

    - **`docker-compose stop` - "Dừng" Ứng Dụng "Đa Container" (Không Xóa):** "Dừng" **"tất cả" các Containers** của ứng
      dụng "đa container" "đang chạy", nhưng **"không 'xóa' "** các Containers, Networks, Volumes. Containers "chuyển
      sang" trạng thái **"stopped"**. Bạn có thể "khởi động lại" ứng dụng "sau này" bằng lệnh `docker-compose start`.

      ```bash
      docker-compose stop # "Dừng" ứng dụng "đa container" (không xóa containers)
      ```

    - **`docker-compose start` - "Khởi Động Lại" Ứng Dụng "Đa Container" "Đã Dừng":** "Khởi động lại" ứng dụng "đa
      container" **"đã dừng"**. "Khởi động" **"tất cả" các Containers** "đã được" "tạo ra" bởi `docker-compose up` và
      đang ở trạng thái "stopped". Ứng dụng "chuyển sang" trạng thái **"running"**.

      ```bash
      docker-compose start # "Khởi động lại" ứng dụng "đa container" "đã dừng"
      ```

    - **`docker-compose restart` - "Khởi Động Lại" Ứng Dụng "Đa Container" (Restart):** "Khởi động lại" ứng dụng "đa
      container". "Dừng" và sau đó "khởi động lại" **"tất cả" các Containers** của ứng dụng. "Tương tự" như "restart
      server".

      ```bash
      docker-compose restart # "Khởi động lại" ứng dụng "đa container" (restart containers)
      ```

    - **`docker-compose logs <service_name>` - "Xem Logs" Của Container:** "Hiển thị" **"logs"** (output) của một **"
      service" (container)** cụ thể có tên `<service_name>`. "Dùng" để "theo dõi" **"quá trình" "khởi động"** và **"hoạt
      động"** của Container, "debug" ứng dụng, hoặc "xem" "thông tin" logging.

      ```bash
      docker-compose logs web # "Xem logs" của service "web" (container "web")
      docker-compose logs -f web # "Xem logs" của service "web" "theo thời gian thực" (follow logs - giống lệnh `tail -f` trong Linux)
      docker-compose logs -t web # "Xem logs" của service "web" và "thêm" "timestamp" vào mỗi dòng log (-t: timestamps)
      ```

    - **`docker-compose ps` - "Liệt Kê" Containers Của Ứng Dụng "Đa Container":** "Hiển thị" **"danh sách"** các
      Containers "thuộc về" ứng dụng "đa container" hiện tại và "xem" **"trạng thái"** của các Containers (running,
      stopped, exited), "ports" "ánh xạ", "volumes" "gắn", v.v. "Tương tự" lệnh `docker ps`, nhưng chỉ "hiển thị"
      Containers "thuộc về" ứng dụng Docker Compose hiện tại.

      ```bash
      docker-compose ps # "Liệt kê" containers của ứng dụng "đa container" hiện tại
      ```

**Tổng Kết Chương 6:**

- Bạn đã "khám phá" **Docker Compose**, " 'nhạc trưởng' " "điều phối" ứng dụng "đa container", và "học cách" "dùng"
  Docker Compose để "quản lý" ứng dụng "đa container" một cách "dễ dàng" và "hiệu quả".
    - "Hiểu" **Docker Compose là gì** ("công cụ" "quản lý" ứng dụng "đa container", " 'bản nhạc' " cho containers).
    - "Nắm vững" **`docker-compose.yml` file** và "cách" "định nghĩa" "cấu hình" ứng dụng "đa container" trong file
      `docker-compose.yml`.
    - Học cách "dùng" lệnh **`docker-compose up`** để "khởi động" ứng dụng "đa container" chỉ với "một lệnh duy nhất".
    - Biết cách "dùng" các lệnh Docker Compose "quản lý" vòng đời ứng dụng "đa container" (`docker-compose down`,
      `docker-compose stop`, `docker-compose start`, `docker-compose restart`, `docker-compose logs`,
      `docker-compose ps`).

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 7: "Ứng Dụng Thực Tế Của Docker" và "Bước Tiếp Theo" - "Docker Đi Muôn Nơi"**. Chúng ta
sẽ "khám phá" các "ví dụ" "ứng dụng" Docker trong "thực tế", từ Docker cho "phát triển", "kiểm thử", "triển khai" ứng
dụng, đến Docker trong "kiến trúc microservices".

Bạn có câu hỏi nào về Docker Compose này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng hành"
cùng bạn trên con đường "chinh phục" Docker.

