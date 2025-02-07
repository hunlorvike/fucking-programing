# Chương 4: Docker Containers - " 'Thực Thể' " Ứng Dụng "Đang Chạy" - " 'Phiên Bản' " "Sống Động" Của Image - " 'Hộp' " Ứng Dụng "Hoạt Động"

Chào mừng bạn đến với **Chương 4: Docker Containers - " 'Thực Thể' " Ứng Dụng "Đang Chạy"**! Trong chương này, chúng ta
sẽ "đi sâu" vào **Docker Containers**, "khái niệm" **"trung tâm"** của Docker, "hiểu" **Container là gì** và "khác biệt"
với Images, "học cách" **"chạy" Docker Containers** từ Docker Images, và **"quản lý" "vòng đời"** của Docker
Containers (start, stop, restart, remove). "Docker Containers" là "nơi" ứng dụng "thực sự" "chạy" và "thể hiện" "sức
mạnh" của Docker.

**Phần 4: Docker Containers - " 'Thực Thể' " Ứng Dụng "Đang Chạy" - " 'Phiên Bản' " "Sống Động" Của Image**

**4.1. Docker Containers là gì? - " 'Phiên Bản' " "Hoạt Động" Của Docker Image - " 'Thực Thể' " Sờ 'Được', 'Chạy' '
Được' "**

- **Docker Container (Docker Container) - " 'Thực Thể' " Ứng Dụng "Đang Sống" Trong Docker:**

    - **Docker Container** (Docker Container) là một **"phiên bản" "đang chạy"** (running instance) của một **Docker
      Image**. Container là **" 'thực thể' " "sờ 'được' ", "chạy 'được' "** của Docker Image.
    - Hãy tưởng tượng Docker Container như một **" 'ngôi nhà' " "thực tế"** được "xây dựng" dựa trên **" 'bản thiết
      kế' " Docker Image**. Docker Image là "bản thiết kế", Docker Container là "ngôi nhà" "thực tế" "đang tồn tại" và "
      có thể 'ở' được".
    - Docker Container "chứa" **"ứng dụng"** của bạn và **"mọi thứ" "cần thiết"** để "chạy" ứng dụng (code, thư viện,
      dependencies, runtime, settings, v.v.) (giống như Docker Image), nhưng Container **"khác"** với Image ở chỗ
      Container là **" 'writable' " (có thể ghi)** và **" 'đang chạy' " (running)**.

- **" 'Khác Biệt' " Giữa Docker Image và Docker Container - " 'Bản Thiết Kế' " vs. " 'Ngôi Nhà' ", " 'Chỉ Đọc' " vs. " '
  Ghi Đọc' ", " 'Tĩnh' " vs. " 'Động' "**:

  | Tính Năng           | Docker Image                                    | Docker Container                                  |
        | --------------------- | ----------------------------------------------- | ------------------------------------------------- |
  | **"Bản Chất"**         | " 'Bản Thiết Kế' ", " 'Khuôn Mẫu' " Ứng Dụng      | " 'Thực Thể' ", " 'Phiên Bản' " "Đang Chạy" Ứng Dụng |
  | **"Tính Chất"**        | " 'Chỉ Đọc' " (Read-Only)                         | " 'Ghi Đọc' " (Read-Write)                           |
  | **"Trạng Thái"**       | " 'Tĩnh' " (Static)                               | " 'Động' " (Dynamic), " 'Đang Sống' " (Running)        |
  | **"Bộ Nhớ"**          | "Không Chiếm Bộ Nhớ" (Chỉ File "Bản Thiết Kế")   | "Chiếm Bộ Nhớ" (RAM) Khi "Đang Chạy"                |
  | **"Mục Đích"**         | " 'Làm Khuôn Mẫu' " Để " 'Tạo' " Containers       | " 'Chạy' " Ứng Dụng, " 'Thực Thi' " Code             |
  | **"Số Lượng"**        | "Một Image" Có Thể "Tạo Ra" "Nhiều Containers"   | "Mỗi Container" "Thuộc Về" "Một Image" Duy Nhất      |
  | **"Thay Đổi"**         | "Không Thể Thay Đổi" (Immutable)                 | "Có Thể Thay Đổi" (Writable Layer)                  |
  | **"Lưu Trữ Dữ Liệu"** | "Không Lưu Trữ Dữ Liệu" (Chỉ "Bản Thiết Kế")     | "Lưu Trữ Dữ Liệu" Trong "Writable Layer" (Tạm Thời)   |
  | **"Vòng Đời"**        | "Tồn Tại" "Vĩnh Viễn" (Cho Đến Khi Bị "Xóa")      | "Tồn Tại" "Trong Thời Gian Chạy" (Tạm Thời)           |

- **Docker Container - " 'Môi Trường' " Chạy Ứng Dụng "Cô Lập" và "Nhất Quán":**

    - Docker Container "cung cấp" một **"môi trường" "chạy ứng dụng" "cô lập"** (isolated environment). Container "cô
      lập" ứng dụng khỏi **"hệ điều hành" "host"** (máy chủ) và khỏi **"các containers khác"** trên cùng một máy chủ.
    - **"Cô Lập" Hệ Thống (System Isolation):** Container "chạy" trong một **"không gian tên" "riêng biệt"** (namespace)
      của Linux kernel. Container có **"process ID tree" "riêng"**, **"network interface" "riêng"**, **"mount points" "
      riêng"**, **"user IDs" và "group IDs" "riêng"**, và **"hostname" "riêng"**. "Giống như" một **"máy ảo" "nhẹ"** (
      lightweight virtual machine), nhưng **"nhẹ hơn"** và **"nhanh hơn"** VM rất nhiều (vì Container "chia sẻ" kernel
      của hệ điều hành host, không cần "ảo hóa" phần cứng "toàn bộ").
    - **"Cô Lập" Tài Nguyên (Resource Isolation):** Container "bị 'giới hạn' " (limited) về **"tài nguyên"** (CPU, bộ
      nhớ RAM, disk I/O, network bandwidth) mà nó có thể "sử dụng" thông qua **Control Groups (cgroups)** của Linux
      kernel. "Đảm bảo" **"công bằng"** và **"ổn định"** khi "chạy" nhiều Containers trên cùng một máy chủ. "Ngăn chặn"
      một Container "ngốn hết" tài nguyên và "ảnh hưởng" đến các Containers khác.
    - **"Nhất Quán" Môi Trường (Environment Consistency):** Docker Container "đảm bảo" **"tính 'nhất quán' " của "môi
      trường" "chạy ứng dụng"** ở **"mọi nơi"** mà Container được "chạy". "Không lo" về "khác biệt môi trường" (
      environment differences) giữa các môi trường phát triển, kiểm thử, staging, và production. " 'Chạy tốt trên
      Docker, chạy tốt ở mọi nơi' ".

**4.2. "Chạy" Docker Container Từ Image (`docker run`) - " 'Thổi Hồn' " Vào Image - " 'Biến' " "Bản Thiết Kế" Thành " '
Ngôi Nhà' " "Sống Động"**

- **"Lệnh 'Thần Thánh' " `docker run <image_name>` - " 'Khởi Động' " Container "Từ Image":**

    - **`docker run <image_name>`** là lệnh Docker CLI **"quan trọng nhất"** và **"phổ biến nhất"**. "Dùng" để **"tạo
      ra"** và **"chạy"** một Docker Container từ Docker Image có tên `<image_name>`.
    - Lệnh `docker run` "thực hiện" **"hai công việc"** "chính" "cùng một lúc":
        1. **"Tạo" Docker Container Mới:** Docker Engine "dùng" Docker Image `<image_name>` làm **"khuôn mẫu"** để "tạo
           ra" một Docker Container **"mới"**. Container mới sẽ là một **"phiên bản" "đang chạy"** của Docker Image.
        2. **"Khởi Động" Docker Container:** Docker Engine **"khởi động"** Docker Container vừa "tạo ra" và "bắt đầu" "
           chạy" ứng dụng được "đóng gói" trong Docker Image.

- **"Cú Pháp" Lệnh `docker run` - " 'Muôn Hình Vạn Trạng' " "Tùy Biến" Container:**

  ```bash
  docker run [OPTIONS] <image_name>[:<tag>] [COMMAND] [ARG...]
  ```

    - **`[OPTIONS]`:** Các **"tùy chọn"** (options) để **"cấu hình"** Docker Container khi "chạy". Có rất nhiều "tùy
      chọn" khác nhau để "tùy biến" Container (ví dụ: "đặt tên" container, "map ports", "mount volumes", "set
      environment variables", "giới hạn" tài nguyên, v.v.). "Tùy chọn" là **"tùy chọn"** (optional), nếu "không có" "tùy
      chọn" nào, Docker sẽ "dùng" các "giá trị 'mặc định' ".

        - **"Một Số 'Tùy Chọn' " `docker run` "Phổ Biến":**
            - **`-d` hoặc `--detach` (Detached Mode): "Chạy" Container ở chế độ **"detached"** (nền) (background).
              Container sẽ "chạy" "ngầm" và Docker CLI sẽ "trả về" command prompt "ngay lập tức" sau khi Container đã "
              khởi động". "Phù hợp" cho "chạy" ứng dụng server hoặc các ứng dụng "chạy" "liên tục" (long-running
              applications).
            - **`-p` hoặc `--publish` (Port Mapping - Ánh Xạ Port): "Ánh xạ"** (map) **"port"** của Container vào **"
              port"** của **"host"** (máy chủ). "Cho phép" "truy cập" ứng dụng trong Container từ "bên ngoài"
              Container (ví dụ: từ trình duyệt web trên máy host). Cú pháp: `-p <host_port>:<container_port>`. (Ví dụ:
              `-p 8080:80` - "ánh xạ" port 80 của container vào port 8080 của host).
            - **`--name <container_name>` (Container Name - Tên Container): "Đặt tên"** cho Docker Container. "Dùng"
              để "dễ dàng" "quản lý" Container bằng "tên" thay vì "Container ID" "dài dòng". (Ví dụ:
              `--name my-web-app`).
            - **`-v` hoặc `--volume` (Volume Mounting - Gắn Volume): "Gắn"** (mount) một **"volume"** (ổ đĩa ảo) từ **"
              host"** vào **"container"**. "Cho phép" "chia sẻ" dữ liệu giữa host và container, "lưu trữ" dữ liệu
              Container "bên ngoài" Container (persistent data), và "mount" code ứng dụng từ host vào container để "phát
              triển" ứng dụng "nhanh chóng" (code changes trên host "tự động" "cập nhật" trong container). Cú pháp:
              `-v <host_path>:<container_path>`. (Ví dụ: `-v /app/data:/container/data` - "gắn" thư mục `/app/data` trên
              host vào thư mục `/container/data` trong container).
            - **`-e` hoặc `--env` (Environment Variables - Biến Môi Trường): "Set" "biến môi trường"** cho Container. "
              Dùng" để "cấu hình" ứng dụng trong Container bằng "biến môi trường". (Ví dụ:
              `-e "DATABASE_URL=localhost:5432"`, `-e "API_KEY=your_api_key"`).
            - **`--rm` (Remove on Exit - Xóa Khi Dừng):** "Ra lệnh" Docker "tự động" **"xóa" Container** sau khi
              Container **"dừng lại"** (exit). "Tiện lợi" cho các Container "chạy một lần" (one-off containers) hoặc các
              Container "không cần" "lưu trữ" dữ liệu "sau khi dừng".

    - **`<image_name>[:<tag>]`:** **"Tên" Docker Image** và **"tag"** (phiên bản) (giống lệnh `docker pull`). "Bắt buộc"
      phải có. Docker Engine sẽ "dùng" Docker Image này để "tạo ra" và "chạy" Container.

    - **`[COMMAND]` và `[ARG...]`:** **"Lệnh"** (command) và **"tham số"** (arguments) để "ghi đè" **"command 'mặc
      định' "** được "định nghĩa" trong Docker Image. **"Tùy chọn"**. "Dùng" để "thay đổi" "hành vi" "chạy" ứng dụng
      trong Container hoặc "truyền" "tham số" cho ứng dụng.

- **"Ví Dụ" Lệnh `docker run` "Tùy Biến" Container:**

  ```bash
  docker run -d -p 8080:80 --name my-nginx-web-server nginx:latest # "Chạy" Container "nginx" ở chế độ "detached" (-d), "map port" 8080 của host vào port 80 của container (-p 8080:80), và "đặt tên" container là "my-nginx-web-server" (--name my-nginx-web-server)
  docker run -it --rm ubuntu:latest /bin/bash  # "Chạy" Container "ubuntu" ở chế độ "interactive" và "TTY" (-it), "xóa" container "tự động" khi "exit" (--rm), và "ghi đè" command "mặc định" bằng command "/bin/bash" (mở shell bash trong container)
  docker run -d -e "DATABASE_URL=localhost:5432" my-app-image:v1.0 # "Chạy" Container "my-app-image" ở chế độ "detached" (-d) và "set" biến môi trường "DATABASE_URL" cho container (-e "DATABASE_URL=localhost:5432")
  ```

**4.3. "Quản Lý" Vòng Đời Container (Start, Stop, Restart,
Remove - `docker start`, `docker stop`, `docker restart`, `docker rm`) - " 'Điều Khiển' " Container "Theo Ý Muốn" - " '
Sinh', 'Tồn Tại', và 'Diệt' " Container**

- **Vòng Đời Docker Container - " 'Sinh Ra' ", " 'Tồn Tại' ", và " 'Diệt Đi' " (Create, Run, Stop, Remove):**

    - Docker Container có **"vòng đời"** (lifecycle) **"tóm gọn"** và **"dễ quản lý"**. Bạn có thể **"điều khiển"** "
      vòng đời" của Container bằng các "lệnh" Docker CLI:
        1. **Create (Tạo Container):** Lệnh `docker create` (ít dùng trực tiếp, thường `docker run` "tự động" "tạo" và "
           chạy" container). "Tạo" Container từ Docker Image, nhưng **"chưa 'khởi động' " Container** (Container ở trạng
           thái "created").
        2. **Run (Chạy Container):** Lệnh `docker run` (phổ biến nhất) hoặc `docker start`. "Khởi động" Container và "
           chạy" ứng dụng bên trong Container. Container chuyển sang trạng thái **"running"** (đang chạy).
        3. **Stop (Dừng Container):** Lệnh `docker stop`. "Dừng" Container "đang chạy". Container chuyển sang trạng thái
           **"stopped"** (đã dừng). Container "vẫn 'tồn tại' " trên máy tính của bạn (vẫn "chiếm" dung lượng ổ cứng),
           nhưng **"không còn 'chạy' "** và **"không 'tiêu thụ' " tài nguyên** (CPU, bộ nhớ RAM). Bạn có thể "khởi động
           lại" Container "đã dừng" "sau này".
        4. **Restart (Khởi Động Lại Container):** Lệnh `docker restart`. "Khởi động lại" Container "đang chạy" hoặc "đã
           dừng". Container "dừng lại" (nếu đang chạy), sau đó "khởi động lại" và chuyển sang trạng thái **"running"**.
        5. **Remove (Xóa Container):** Lệnh `docker rm`. "Xóa" Container **"đã dừng"**. Container **"bị 'xóa hoàn
           toàn' "** khỏi máy tính của bạn (giải phóng bộ nhớ và dung lượng ổ cứng mà Container "chiếm giữ"). **"Không
           thể" "xóa" Container "đang chạy"**. Cần "dừng" Container trước khi "xóa".

- **"Các Lệnh" Docker CLI "Quản Lý" Vòng Đời Container:**

    - **`docker start <container_id>` - "Khởi Động" Docker Container "Đã Dừng":** "Khởi động" một Docker Container **"đã
      dừng"** có ID `<container_id>`. Container chuyển từ trạng thái "stopped" sang **"running"**.

      ```bash
      docker start <container_id> # "Khởi động" container có ID "<container_id>" (thay "<container_id>" bằng Container ID "thực tế" từ `docker ps -a`)
      docker start my-web-app     # "Khởi động" container có tên "my-web-app" (nếu bạn đã "đặt tên" container khi chạy bằng `--name`)
      ```

    - **`docker stop <container_id>` - "Dừng" Docker Container "Đang Chạy":** (Đã "giới thiệu" ở phần 2.2).

    - **`docker restart <container_id>` - "Khởi Động Lại" Docker Container:** "Khởi động lại" một Docker Container có ID
      `<container_id>`. Container "dừng lại" (nếu đang chạy), sau đó "khởi động lại" và chuyển sang trạng thái **"
      running"**. "Tương tự" như "tắt" và "bật lại" máy tính. "Dùng" để "khởi động lại" ứng dụng trong Container (ví dụ:
      sau khi "thay đổi" cấu hình).

      ```bash
      docker restart <container_id> # "Khởi động lại" container có ID "<container_id>" (thay "<container_id>" bằng Container ID "thực tế" từ `docker ps`)
      docker restart my-web-app     # "Khởi động lại" container có tên "my-web-app" (nếu bạn đã "đặt tên" container khi chạy bằng `--name`)
      ```

    - **`docker rm <container_id>` - "Xóa" Docker Container "Đã Dừng":** (Đã "giới thiệu" ở phần 2.2).

- **"Liệt Kê" Containers Để "Quản Lý" ( `docker ps` ):**

    - Để "quản lý" Docker Containers (start, stop, restart, remove), bạn cần "biết" **"Container ID"** hoặc **"Container
      Name"** của Container mà bạn muốn "thao tác".
    - Lệnh **`docker ps`** (và `docker ps -a`) là "công cụ" "quan trọng" để **"liệt kê" "danh sách" Docker Containers**
      trên máy tính của bạn và "xem" **"Container ID"**, **"Container Name"**, **"trạng thái"** (status) (running,
      stopped, exited), và các "thông tin" khác về Containers.
    - "Dùng" "Container ID" hoặc "Container Name" từ "kết quả" lệnh `docker ps` (hoặc `docker ps -a`) để "truyền" vào
      các lệnh "quản lý" Container (ví dụ: `docker stop`, `docker rm`, `docker restart`, `docker exec`, v.v.).

**4.4. "Truy Cập" Vào Container Đang Chạy (`docker exec`) - " 'Khám Phá' " "Thế Giới Bên Trong" Container - " 'Chui
Vào' " "Hộp Docker" Để " 'Xem Xét' "**

- **`docker exec` - " 'Cánh Cửa' " Vào " 'Thế Giới Bên Trong' " Container:**

    - **`docker exec`** là lệnh Docker CLI "cho phép" bạn **"thực thi" "lệnh"** (command) **"bên trong"** một Docker
      Container **"đang chạy"**.
    - `docker exec` "cho phép" bạn **"truy cập"** vào "môi trường" "bên trong" Container, "xem xét" **"cấu trúc file"**,
      **"chạy" các "lệnh"** (ví dụ: `ls`, `cd`, `cat`, `ps`, `top`, v.v.), **"debug" ứng dụng**, hoặc "thực hiện" các "
      tác vụ" "quản trị" Container.
    - `docker exec` "giống như" việc **" 'chui vào' " "hộp container"** để " 'xem xét' " "bên trong" "hộp" có gì.

- **"Cú Pháp" Lệnh `docker exec` - " 'Chỉ Định' " "Container" và " 'Lệnh' " "Thực Thi":**

  ```bash
  docker exec [OPTIONS] <container_id> <command> [ARG...]
  ```

    - **`[OPTIONS]`:** Các **"tùy chọn"** (options) để "cấu hình" lệnh `docker exec`. "Phổ biến" nhất là các "tùy chọn"
      **"interactive"** và **"TTY"** (`-it`) để "mở" **"interactive shell"** (ví dụ: bash, sh) bên trong Container.

        - **`-i` hoặc `--interactive` (Interactive): "Giữ" STDIN "mở"** (keep STDIN open) "ngay cả khi" "không 'gắn
          kèm' " (not attached). "Cho phép" bạn **"tương tác"** với process trong Container thông qua **standard input
          ** (bàn phím).
        - **`-t` hoặc `--tty` (Allocate a pseudo-TTY): "Cấp phát" một **"pseudo-TTY"** (terminal). "Cho phép" các ứng
          dụng console bên trong Container "hiển thị" "giao diện" "console" "đầy đủ" (ví dụ: màu sắc, cursor, v.v.).

    - **`<container_id>`:** **"Container ID"** hoặc **"Container Name"** của Container bạn muốn "truy cập". "Bắt buộc"
      phải có.

    - **`<command>`:** **"Lệnh"** bạn muốn "thực thi" bên trong Container. "Bắt buộc" phải có. Thường dùng các lệnh **"
      shell"** (ví dụ: `/bin/bash`, `/bin/sh`, `cmd.exe`) để "mở" "interactive shell" trong Container.

    - **`[ARG...]`:** **"Tham số"** (arguments) cho "lệnh" (command). "Tùy chọn".

- **"Ví Dụ" Lệnh `docker exec` - " 'Mở' " "Shell Bash" Bên Trong Container `nginx` và "Chạy Lệnh" `ls`:**

    1. **"Chạy" Docker Container `nginx` (ví dụ):** (Nếu bạn chưa có container `nginx` đang chạy, hãy "chạy" container
       `nginx` bằng lệnh `docker run -d -p 8080:80 --name my-nginx-web-server nginx:latest`).

    2. **"Mở" "shell bash" bên trong Container `nginx` bằng lệnh `docker exec -it <container_id> /bin/bash`:**

       ```bash
       docker exec -it my-nginx-web-server /bin/bash # "Mở" "shell bash" trong container "my-nginx-web-server" (-it: interactive và TTY, /bin/bash: lệnh shell bash)
       ```

        - Thay `<container_id>` bằng **"Container ID"** của Container `nginx` (bạn có thể "lấy" Container ID từ lệnh
          `docker ps`) hoặc "dùng" **"Container Name"** `"my-nginx-web-server"` (nếu bạn đã "đặt tên" container khi chạy
          bằng `--name`).
        - Lệnh `docker exec -it my-nginx-web-server /bin/bash` sẽ "mở" một **"interactive shell bash"** (command prompt)
          **"bên trong" Docker Container `nginx`**. Command prompt sẽ "thay đổi" (thường có dạng
          `root@<container_id>:/#`) để "biểu thị" rằng bạn đang "làm việc" bên trong Container.

    3. **"Chạy" các lệnh Linux bên trong Container Shell Bash:** "Trong" Container Shell Bash, bạn có thể "chạy" các **"
       lệnh Linux"** (ví dụ: `ls`, `cd`, `pwd`, `cat`, `mkdir`, `rm`, `ps`, `top`, v.v.) để "khám phá" "cấu trúc file"
       Container, "xem" các "process" "đang chạy" trong Container, "kiểm tra" "cấu hình" Container, v.v.

       ```bash
       ls / # "Liệt kê" thư mục gốc (root directory) của Container
       cd /etc/nginx # "Di chuyển" đến thư mục "/etc/nginx" của Container
       ls # "Liệt kê" file trong thư mục "/etc/nginx"
       cat nginx.conf # "Xem nội dung" file "nginx.conf" (file cấu hình Nginx)
       exit # "Thoát" khỏi Container Shell Bash và "trở về" command prompt của máy host
       ```

    4. **"Chạy" lệnh `ls /usr/share/nginx/html` "trực tiếp" bằng `docker exec` (không cần mở shell bash):**

       ```bash
       docker exec my-nginx-web-server ls /usr/share/nginx/html # "Chạy" lệnh "ls /usr/share/nginx/html" bên trong container "my-nginx-web-server" và "hiển thị" kết quả trên command prompt của máy host
       ```

        - Lệnh `docker exec my-nginx-web-server ls /usr/share/nginx/html` sẽ "chạy" lệnh `ls /usr/share/nginx/html` **"
          một lần duy nhất"** bên trong Container `nginx` và "hiển thị" **"kết quả"** của lệnh đó trên command prompt
          của máy host. Sau khi lệnh "chạy" xong, bạn sẽ "trở về" command prompt của máy host (không "mở" shell bash "
          tương tác" trong Container).

**Tổng Kết Chương 4:**

- Bạn đã "khám phá" **Docker Containers**, " 'thực thể' " ứng dụng "đang chạy" và " 'phiên bản' " "sống động" của Docker
  Images.
    - "Hiểu" **Docker Container là gì** ("phiên bản" "đang chạy" của Docker Image, "môi trường" chạy ứng dụng "cô lập"
      và "nhất quán").
    - "Nắm vững" lệnh **`docker run`** và "cách" "dùng" lệnh `docker run` để "tạo ra" và "chạy" Docker Containers từ
      Docker Images, và "cấu hình" Container bằng các "tùy chọn" khác nhau.
    - Biết cách "quản lý" **"vòng đời" Docker Containers** (start, stop, restart, remove) bằng các lệnh Docker CLI (
      `docker start`, `docker stop`, `docker restart`, `docker rm`).
    - Học cách "dùng" lệnh **`docker exec`** để "truy cập" vào "môi trường" "bên trong" Docker Container "đang chạy"
      và "thực thi" các "lệnh" bên trong Container.

**Bước Tiếp Theo:**

Chúng ta sẽ chuyển sang **Chương 5: Dockerfile - " 'Công Thức' " "Tự Động" "Xây Dựng" Docker Images**. Chúng ta sẽ "học
cách" "viết" **Dockerfile**, "file" "công thức" để Docker **"tự động" "xây dựng" Docker Images** cho ứng dụng của bạn, "
làm chủ" "quy trình" "đóng gói" ứng dụng vào Docker Images.

Bạn có câu hỏi nào về Docker Containers này không? Hãy cứ "hỏi tự nhiên" nhé! Mình luôn sẵn sàng "giải đáp" và "đồng
hành" cùng bạn trên con đường "chinh phục" Docker.

