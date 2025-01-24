## **🚀 "GIẢI MÃ" MÔ HÌNH OSI: "BẢN THIẾT KẾ" CHO MẠNG MÁY TÍNH CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "mổ xẻ" một chủ đề cực kỳ quan trọng trong Networking: Mô hình
OSI (Open Systems Interconnection). Đây là một "bản thiết kế" giúp chúng ta hiểu rõ cách dữ liệu được truyền tải qua
mạng, và nó cũng là nền tảng cho nhiều công nghệ mạng hiện đại. Cùng mình "khám phá" nó nhé!

![OSI Model](/assets/images/OSI_model_LAN.webp)

### **I. MÔ HÌNH OSI LÀ GÌ? (NHƯ "BẢN VẼ" CỦA MẠNG)**

- **Mô hình OSI (Open Systems Interconnection):** Là một mô hình trừu tượng, chia quá trình truyền thông mạng thành 7
  lớp (layer) riêng biệt.
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn viết thư: bạn viết nội dung (application layer), bạn cho vào phong bì (presentation layer), bạn
      gửi qua bưu điện (các layer bên dưới), ...
- **Quan trọng vì:**
    - **Chuẩn hóa:** Giúp các thiết bị từ các nhà sản xuất khác nhau có thể giao tiếp được với nhau.
    - **Dễ hiểu:** Chia nhỏ quy trình truyền thông thành các lớp dễ quản lý.
    - **Gỡ lỗi:** Giúp dễ dàng tìm ra lỗi khi có sự cố trong mạng.
    - **Phân tầng**: Giúp dễ dàng nghiên cứu, phát triển các giao thức mạng phức tạp.

### **II. 7 LỚP CỦA MÔ HÌNH OSI (NHƯ "CẦU THANG" CỦA MẠNG)**

#### **1. Physical Layer (Lớp Vật lý) - "SỰ SỐNG" CỦA MẠNG**

- **Chức năng:** Truyền tín hiệu điện, quang, sóng radio,... (các tín hiệu vật lý).
- **Nó làm gì?** Chuyển dữ liệu thành các tín hiệu điện, ánh sáng, sóng radio để truyền đi.
- **Thiết bị:**
    - Cáp Ethernet (đồng, quang).
    - Bộ thu phát sóng Wi-Fi.
    - Bộ phát sóng Bluetooth, ...
- **Giao thức:**
    - Ethernet, Wi-Fi, Bluetooth, ...
- **Lưu ý:** Quan tâm đến tốc độ, khoảng cách, loại cáp,...
- **Ví dụ:** Bạn gửi một bức ảnh qua wifi, lớp physical sẽ chuyển dữ liệu của ảnh này thành các tín hiệu điện từ để
  truyền đi.
- **Chủ đề chi tiết:**
    - Các loại cáp mạng (cáp đồng, cáp quang).
    - Các chuẩn kết nối (Ethernet, Wi-Fi, Bluetooth).
    - Mã hóa tín hiệu, điều chế, giải điều chế.
    - Tốc độ truyền dẫn và khoảng cách.

#### **2. Data Link Layer (Lớp Liên kết Dữ liệu) - "ĐÓNG GÓI" DỮ LIỆU TRONG MẠNG**

- **Chức năng:** Đóng gói dữ liệu thành các frame, truyền dữ liệu giữa 2 thiết bị trên cùng một mạng (LAN).
- **Nó làm gì?** Đảm bảo dữ liệu đến đúng địa chỉ MAC, phát hiện và sửa lỗi khi truyền.
- **Thiết bị:**
    - Switch (chuyển mạch).
    - Card mạng (NIC).
- **Giao thức:**
    - Ethernet, Wi-Fi, PPP,...
    - MAC address (địa chỉ vật lý).
- **Lưu ý**: Quan tâm đến giao thức nào được dùng để truyền dữ liệu trên một môi trường cụ thể (ví dụ: Ethernet trong
  mạng LAN hoặc Wi-fi trong mạng không dây)
- **Ví dụ:** Bạn gửi một gói tin trên mạng LAN, lớp data link sẽ đóng gói gói tin này thành Ethernet frame để truyền đi,
  đảm bảo đến đúng máy đích.
- **Chủ đề chi tiết:**
    - MAC address và cách hoạt động.
    - Các giao thức truyền dữ liệu (Ethernet, Wi-Fi, ...).
    - CSMA/CD (Carrier Sense Multiple Access with Collision Detection) và CSMA/CA (Carrier Sense Multiple Access with
      Collision Avoidance).
    - VLAN (Virtual LAN).

#### **3. Network Layer (Lớp Mạng) - "ĐỊNH TUYẾN" TRONG MẠNG LỚN**

- **Chức năng:** Định tuyến (routing) các gói tin trên mạng (từ mạng này đến mạng khác).
- **Nó làm gì?** Tìm đường đi tốt nhất để gói tin đến đích.
- **Thiết bị:**
    - Router.
- **Giao thức:**
    - IP (Internet Protocol) - địa chỉ IP.
    - Các giao thức định tuyến (RIP, OSPF, BGP,...).
- **Lưu ý:** Quan tâm đến subnet mask, routing table, ...
- **Ví dụ:** Gói tin từ máy tính của bạn (trong mạng LAN) đi đến server Google (trên Internet) phải qua nhiều router,
  lớp network sẽ đảm bảo gói tin đến đúng nơi.
- **Chủ đề chi tiết:**
    - IP address (IPv4, IPv6) và subnetting.
    - Giao thức định tuyến (RIP, OSPF, BGP).
    - NAT (Network Address Translation).
    - ICMP (Internet Control Message Protocol).

#### **4. Transport Layer (Lớp Giao Vận) - "VẬN CHUYỂN" DỮ LIỆU TIN CẬY HOẶC KHÔNG TIN CẬY**

- **Chức năng:** Truyền dữ liệu giữa các ứng dụng, đảm bảo độ tin cậy và thứ tự (hoặc không tin cậy).
- **Nó làm gì?** Chuyển dữ liệu từ ứng dụng này sang ứng dụng khác, có cơ chế kiểm soát lỗi và thứ tự (nếu cần).
- **Giao thức:**
    - TCP (Transmission Control Protocol): Tin cậy, có thứ tự, dùng trong web, email.
    - UDP (User Datagram Protocol): Không tin cậy, nhanh hơn, dùng trong game, video call.
- **Lưu ý:** Quan tâm đến cơ chế bắt tay (handshake) của TCP, độ tin cậy, port.
- **Ví dụ:** Khi bạn tải một trang web, TCP sẽ đảm bảo dữ liệu không bị mất và đến đúng thứ tự. Còn khi bạn chơi game
  online, UDP được sử dụng vì cần truyền dữ liệu nhanh, không cần quá tin cậy.
- **Chủ đề chi tiết:**
    - TCP và cơ chế bắt tay (3-way handshake).
    - UDP và truyền thông không tin cậy.
    - Port number.
    - Flow control, congestion control.

#### **5. Session Layer (Lớp Phiên) - "QUẢN LÝ" PHIÊN LÀM VIỆC**

- **Chức năng:** Quản lý kết nối (phiên làm việc) giữa hai ứng dụng.
- **Nó làm gì?** Thiết lập, duy trì, và kết thúc kết nối giữa các ứng dụng.
- **Ví dụ:**
    - Quản lý phiên đăng nhập vào một website.
    - Quản lý phiên kết nối TCP.
- **Giao thức:**

    - Nhiều giao thức như SSL/TLS handshake, NetBIOS, ...

- **Lưu ý:** Lớp này không phải lúc nào cũng dùng rõ ràng trong các ứng dụng thực tế, thường được tích hợp vào các lớp
  khác.
- **Chủ đề chi tiết:**
    - Các giao thức session layer (SSL/TLS handshake,...).
    - Session management trong web application.

#### **6. Presentation Layer (Lớp Trình Bày) - "ĐỊNH DẠNG" VÀ "MÃ HÓA" DỮ LIỆU**

- **Chức năng:** Định dạng, mã hóa, nén dữ liệu.
- **Nó làm gì?** Chuyển đổi dữ liệu thành định dạng phù hợp và bảo mật dữ liệu khi cần.
- **Ví dụ:**
    - Mã hóa SSL/TLS.
    - Nén dữ liệu dùng Gzip hoặc Brotli.
    - Định dạng JSON, XML.
- **Lưu ý:** Chú ý đến các phương pháp mã hóa, nén dữ liệu.
- **Chủ đề chi tiết:**
    - Mã hóa và giải mã dữ liệu (encryption, decryption).
    - Nén dữ liệu (compression).
    - Các định dạng dữ liệu (JSON, XML, ...).

#### **7. Application Layer (Lớp Ứng Dụng) - "GIAO DIỆN" VỚI NGƯỜI DÙNG**

- **Chức năng:** Cung cấp các dịch vụ mạng cho ứng dụng.
- **Nó làm gì?** Là giao diện để ứng dụng có thể gửi/nhận dữ liệu qua mạng.
- **Ví dụ:**
    - HTTP (web).
    - FTP (truyền file).
    - SMTP (gửi email).
    - DNS (phân giải tên miền).
- **Lưu ý:** Các giao thức ở tầng này thường do ứng dụng tự định nghĩa.
- **Chủ đề chi tiết:**
    - Các giao thức ứng dụng (HTTP, FTP, SMTP, DNS, SSH, ...).
    - API (Application Programming Interface).
    - Web service, microservices.

### **III. TÓM LƯỢC**

| Layer        | Chức năng chính                             | Ví dụ                        |
|--------------|---------------------------------------------|------------------------------|
| Physical     | Truyền tín hiệu vật lý                      | Cáp Ethernet, Wi-Fi          |
| Data Link    | Đóng gói dữ liệu trong mạng LAN             | Ethernet, Wi-Fi, MAC Address |
| Network      | Định tuyến gói tin giữa các mạng            | IP address, Router           |
| Transport    | Truyền dữ liệu tin cậy (hoặc không tin cậy) | TCP, UDP                     |
| Session      | Quản lý các phiên kết nối                   | SSL/TLS handshake            |
| Presentation | Định dạng, mã hóa dữ liệu                   | JSON, XML, HTTPS             |
| Application  | Cung cấp dịch vụ mạng cho ứng dụng          | HTTP, FTP, SMTP, DNS         |

### **IV. SƠ ĐỒ HOẠT ĐỘNG (CÁCH DỮ LIỆU "ĐI" QUA CÁC LỚP)**

1. **Ứng dụng gửi dữ liệu:** Dữ liệu từ ứng dụng sẽ đi xuống các lớp từ 7 đến 1.
    - Mỗi lớp sẽ thêm các header (thông tin điều khiển) vào dữ liệu.
2. **Dữ liệu được truyền đi:** Dữ liệu sẽ được truyền tải qua mạng (ở lớp vật lý).
3. **Ứng dụng nhận dữ liệu:** Dữ liệu từ mạng sẽ đi lên các lớp từ 1 đến 7.
    - Mỗi lớp sẽ loại bỏ header của lớp tương ứng.
    - Dữ liệu sẽ được đưa đến ứng dụng ở lớp 7.

### **V. VÍ DỤ THỰC TẾ (MỘT GÓI TIN "ĐI" TRONG MẠNG)**

Giả sử bạn mở trang web Google (dùng HTTP):

1. **Application Layer (Lớp ứng dụng):**
    - Trình duyệt tạo request HTTP để lấy trang web.
2. **Presentation Layer (Lớp trình bày):**
    - Mã hóa dữ liệu (nếu dùng HTTPS).
3. **Session Layer (Lớp phiên):**
    - Thiết lập phiên kết nối với server.
4. **Transport Layer (Lớp giao vận):**
    - Dùng TCP để đảm bảo dữ liệu được truyền đầy đủ, đúng thứ tự.
5. **Network Layer (Lớp mạng):**
    - Thêm địa chỉ IP của bạn và địa chỉ IP của Google vào gói tin.
6. **Data Link Layer (Lớp liên kết dữ liệu):**
    - Đóng gói gói tin vào frame (ethernet frame).
7. **Physical Layer (Lớp vật lý):**
    - Truyền tín hiệu qua cáp hoặc Wi-Fi.

Sau đó, các gói tin sẽ đi ngược lại qua các lớp ở máy chủ Google, và trả kết quả về cho bạn.

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Mô hình trừu tượng:** OSI là mô hình lý thuyết, không phải lúc nào cũng có sự tương ứng 1-1 với thực tế.
- **Mỗi lớp có chức năng riêng:** Mỗi lớp có chức năng và giao thức riêng biệt.
- **Hiểu rõ từng lớp:** Để gỡ lỗi mạng, cần hiểu rõ từng lớp.
- **Không cứng nhắc:** Đôi khi các lớp có thể kết hợp với nhau trong thực tế.
- **Layer 4/7:** Layer 4 (Transport Layer) và Layer 7 (Application Layer) là những layer quan trọng nhất cần chú ý.

### **VII. ỨNG DỤNG CỦA MÔ HÌNH OSI (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Học mạng:** Nắm vững kiến thức cơ bản về mạng máy tính.
- **Gỡ lỗi mạng:** Giúp tìm ra lỗi khi có sự cố mạng.
- **Thiết kế mạng:** Giúp thiết kế các giao thức, các ứng dụng mạng.
- **An ninh mạng:** Giúp hiểu cách bảo mật thông tin trên mạng.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

Mô hình OSI là một công cụ quan trọng giúp chúng ta hiểu rõ về cách hoạt động của mạng máy tính. Nắm vững mô hình OSI sẽ
giúp các bạn trở thành những chuyên gia mạng thực thụ! Chúc các bạn học tập thành công! 😎
