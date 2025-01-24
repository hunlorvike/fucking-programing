## **🚀 TỔNG QUAN VỀ NETWORKING: "BẢN ĐỒ" KẾT NỐI THẾ GIỚI SỐ 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau khám phá về Networking (Mạng máy tính), một lĩnh vực nền tảng và
cực kỳ quan trọng trong thế giới công nghệ. Đây là "bản đồ" giúp chúng ta hiểu cách các thiết bị kết nối và giao tiếp
với nhau, từ máy tính cá nhân đến Internet toàn cầu. Let's go!

![NET WORKING](/assets/images/Networking.jpg)

### **I. NETWORKING LÀ GÌ? (KẾT NỐI MỌI THỨ)**

- **Networking (Mạng máy tính):** Là tập hợp các thiết bị, giao thức, và phần mềm cho phép các máy tính giao tiếp và
  chia sẻ thông tin với nhau.
- **Nó hoạt động như thế nào?**
    - Giống như một hệ thống giao thông: các thiết bị (xe) di chuyển theo các quy tắc (giao thức) trên các "con đường" (
      kết nối) để đến đích (trao đổi thông tin).
- **Quan trọng vì:**
    - **Kết nối:** Cho phép các máy tính "nói chuyện" được với nhau.
    - **Chia sẻ:** Cho phép chia sẻ dữ liệu, tài nguyên.
    - **Internet:** Nền tảng của Internet và các dịch vụ trực tuyến.
    - **Ứng dụng:** Rất nhiều ứng dụng (web, app, game online, IoT, ...) đều dựa vào mạng.

### **II. CÁC THÀNH PHẦN CHÍNH CỦA MẠNG (NHỮNG "MẢNH GHÉP" CỦA MẠNG)**

1. **Thiết bị (Devices):**
    - Máy tính, điện thoại, server, router, switch, modem, ...
    - Mỗi thiết bị có địa chỉ IP để nhận biết và liên lạc với nhau.
2. **Kết nối (Connections):**
    - Cáp mạng (Ethernet), Wi-Fi, Bluetooth, sóng radio,...
    - Các phương tiện để dữ liệu có thể truyền tải qua lại.
3. **Giao thức (Protocols):**
    - Các quy tắc giao tiếp, đảm bảo các thiết bị "hiểu" nhau (TCP, UDP, IP, HTTP, ...).
    - Giống như các "luật lệ" giao thông, giúp các thiết bị giao tiếp một cách trật tự.

### **III. CÁC MÔ HÌNH MẠNG CƠ BẢN (CÁCH CHIA "TẦNG" CỦA MẠNG)**

1. **Mô hình OSI (7 lớp):**
    - **Application:** Giao diện với người dùng (HTTP, FTP, DNS,...).
    - **Presentation:** Mã hóa, giải mã, nén dữ liệu.
    - **Session:** Quản lý phiên làm việc.
    - **Transport:** Truyền dữ liệu tin cậy (TCP) hoặc không tin cậy (UDP).
    - **Network:** Định tuyến (IP).
    - **Data Link:** Truyền dữ liệu trong cùng mạng (Ethernet, Wi-Fi).
    - **Physical:** Truyền tín hiệu (cáp, sóng radio).
2. **Mô hình TCP/IP (4 lớp):**
    - **Application:** (HTTP, FTP, DNS, ...).
    - **Transport:** (TCP, UDP).
    - **Internet:** (IP).
    - **Network Access:** (Ethernet, Wi-Fi).

### **IV. ĐỊA CHỈ IP (IP ADDRESS) - "SỐ NHÀ" TRONG MẠNG**

- **Địa chỉ IP (IP Address):** Là địa chỉ logic của một thiết bị trong mạng.
- **IPv4:** Dạng `192.168.1.1` (32 bit, sắp cạn).
- **IPv6:** Dạng `2001:0db8:85a3:0000:0000:8a2e:0370:7334` (128 bit, thay thế IPv4).
- **Subnet Mask:** Dùng để chia mạng thành các mạng con.

### **V. GIAO THỨC TCP VÀ UDP (CÁCH "NÓI CHUYỆN" TRONG MẠNG)**

- **TCP (Transmission Control Protocol):**
    - **Tin cậy:** Đảm bảo dữ liệu đến nơi đầy đủ, đúng thứ tự.
    - **Chậm hơn:** Có cơ chế kiểm tra và phục hồi lỗi.
    - **Dùng trong:** Web, email, ...
- **UDP (User Datagram Protocol):**
    - **Không tin cậy:** Không đảm bảo dữ liệu đến nơi.
    - **Nhanh hơn:** Không có cơ chế kiểm tra.
    - **Dùng trong:** Game, video call, ...

### **VI. DOMAIN NAME SYSTEM (DNS) - "TỪ ĐIỂN" INTERNET**

- **DNS (Domain Name System):** Chuyển tên miền (ví dụ: `google.com`) thành địa chỉ IP (ví dụ: `172.217.160.142`).

### **VII. HTTP VÀ HTTPS (CÁCH "GIAO TIẾP" TRÊN WEB)**

- **HTTP:** Giao thức truyền dữ liệu trên web (không mã hóa).
- **HTTPS:** HTTP bảo mật (dùng SSL/TLS để mã hóa).

### **VIII. BẢO MẬT MẠNG (BẢO VỆ DỮ LIỆU TRÊN MẠNG)**

- **Tường lửa (Firewall):** Chặn các truy cập trái phép.
- **IDS (Intrusion Detection System):** Phát hiện các hành vi xâm nhập.
- **IPS (Intrusion Prevention System):** Ngăn chặn các hành vi xâm nhập.
- **VPN (Virtual Private Network):** Tạo kết nối an toàn.
- **Tấn công mạng:** DoS, DDoS, Man-in-the-Middle, ...

### **IX. CÁC THIẾT BỊ MẠNG (NHỮNG "MẢNH GHÉP" TRONG HỆ THỐNG)**

- **Router:** Định tuyến gói tin giữa các mạng.
- **Switch:** Kết nối các thiết bị trong mạng LAN.
- **Hub:** Chia sẻ băng thông (ít dùng ngày nay).
- **Modem:** Kết nối mạng với Internet.
- **Access Point:** Cho phép thiết bị kết nối Wi-Fi.

### **X. MẠNG LAN VÀ WAN (HAI LOẠI "MÔ HÌNH" MẠNG)**

- **LAN (Local Area Network):** Mạng cục bộ (trong nhà, văn phòng).
- **WAN (Wide Area Network):** Mạng diện rộng (Internet).

### **XI. CLOUD COMPUTING (MẠNG ĐỂ "THUÊ" SỨC MẠNH)**

- **Điện toán đám mây:** Dùng tài nguyên máy tính trên internet (IaaS, PaaS, SaaS).

### **XII. CÁC GIAO THỨC ỨNG DỤNG (CÁCH APP "NÓI CHUYỆN")**

- **SMTP:** Gửi email.
- **FTP:** Truyền file.
- **SSH:** Truy cập từ xa an toàn.
- **Telnet:** Truy cập từ xa (không an toàn).

### **XIII. LOAD BALANCING (CÂN BẰNG TẢI) - (ĐẢM BẢO "GIAO THÔNG" THÔNG SUỐT)**

- **Cân bằng tải:** Phân phối traffic đến nhiều server để tránh bị quá tải và tăng hiệu suất.

### **XIV. KẾT LUẬN (TỔNG KẾT)**

Networking là một lĩnh vực rộng lớn và rất quan trọng trong thế giới công nghệ. Hy vọng qua bài viết này, các bạn đã có
một cái nhìn tổng quan và hữu ích về nó. Chúc các bạn học tập thành công! 😎
