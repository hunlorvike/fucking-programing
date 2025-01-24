## **🚀 TỔNG QUAN VỀ MÔ HÌNH TCP/IP: "BẢN ĐỒ" GIAO TIẾP TRÊN INTERNET 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau khám phá về mô hình TCP/IP, một mô hình "kinh điển" giúp chúng ta
hiểu rõ cách Internet hoạt động. Đây là "bản đồ" giúp các thiết bị giao tiếp và trao đổi dữ liệu với nhau trên toàn cầu.
Let's go!

![TCP IP](/assets/images/ClouDNS-TCPIP-5-7.png)

### **I. MÔ HÌNH TCP/IP LÀ GÌ? (CÁCH THIẾT BỊ "NÓI CHUYỆN")**

- **Mô hình TCP/IP:** Là một mô hình _trừu tượng_ mô tả cách các giao thức mạng hoạt động, chia quá trình giao tiếp
  thành 4 lớp (layer).
- **Nó hoạt động như thế nào?**
    - Giống như một quy trình gửi thư: bạn viết thư (application layer), bỏ vào phong bì (transport layer), ghi địa
      chỉ (internet layer), và gửi qua bưu điện (network access layer).
- **Quan trọng vì:**
    - **Nền tảng của Internet:** Là mô hình cơ bản cho mọi giao tiếp trên Internet.
    - **Chuẩn hóa:** Giúp các thiết bị từ các hãng khác nhau giao tiếp được với nhau.
    - **Dễ hiểu:** Chia nhỏ quy trình giao tiếp thành các lớp dễ quản lý.
    - **Gỡ lỗi:** Giúp tìm ra lỗi khi có sự cố mạng.

### **II. 4 LỚP CỦA MÔ HÌNH TCP/IP (CÁC "BƯỚC" GIAO TIẾP)**

#### **1. Application Layer (Lớp Ứng Dụng) - "GIAO DIỆN" VỚI NGƯỜI DÙNG**

- **Chức năng:** Cung cấp các dịch vụ mạng cho ứng dụng (như web browser, email client, ...).
- **Nó làm gì?**
    - Xử lý yêu cầu của ứng dụng, hiển thị dữ liệu cho người dùng.
    - Dùng các giao thức như HTTP, FTP, SMTP, DNS, ...
- **Giao thức phổ biến:**
    - **HTTP (Hypertext Transfer Protocol):** Dùng để truyền dữ liệu web (HTML, CSS, JavaScript,...).
        - **Ví dụ:** Khi bạn truy cập `google.com`, trình duyệt của bạn dùng HTTP (hoặc HTTPS) để lấy trang web.
    - **FTP (File Transfer Protocol):** Dùng để truyền file.
        - **Ví dụ:** Khi bạn tải file lên server hoặc từ server về máy.
    - **SMTP (Simple Mail Transfer Protocol):** Dùng để gửi email.
        - **Ví dụ:** Khi bạn dùng Gmail, Yahoo Mail,... để gửi email.
    - **DNS (Domain Name System):** Phân giải tên miền thành địa chỉ IP.
        - **Ví dụ:** Khi bạn gõ `google.com`, DNS sẽ giúp bạn tìm ra địa chỉ IP của server Google.
    - **SSH (Secure Shell):** Truy cập máy tính từ xa (có mã hóa).
        - **Ví dụ:** Truy cập vào server Linux từ xa.
    - **Telnet:** Truy cập máy tính từ xa (không mã hóa).
    - **SNMP:** Quản lý các thiết bị trong mạng.
- **Ví dụ hoạt động:**
    - Khi bạn mở trang web, trình duyệt sẽ dùng HTTP để lấy dữ liệu từ web server.
    - Khi bạn gửi email, ứng dụng email sẽ dùng SMTP để gửi email.
    - Khi bạn tải file, trình download dùng FTP để truyền file.
- **Mẹo nhỏ:** Các giao thức tầng này thường do ứng dụng định nghĩa, không quá phức tạp.
- **Chủ đề chi tiết:**
    - Cấu trúc header và payload của các giao thức HTTP, SMTP, FTP, DNS, ...
    - Cách ứng dụng sử dụng API để kết nối với mạng.
    - Các phương pháp mã hóa dữ liệu tại application layer (ví dụ: end-to-end encryption).

#### **2. Transport Layer (Lớp Giao Vận) - "VẬN CHUYỂN" DỮ LIỆU**

- **Chức năng:** Truyền dữ liệu giữa các ứng dụng, đảm bảo độ tin cậy hoặc tốc độ.
- **Nó làm gì?**
    - Chuyển dữ liệu từ ứng dụng này đến ứng dụng khác một cách tin cậy (hoặc không tin cậy).
    - Chia dữ liệu thành các gói nhỏ hơn để truyền đi (segmentation).
    - Thêm port number để xác định ứng dụng nào đang dùng (giống như số phòng trong tòa nhà).
- **Giao thức phổ biến:**
    - **TCP (Transmission Control Protocol):**
        - **Tin cậy:** Đảm bảo dữ liệu đến nơi đầy đủ, đúng thứ tự.
        - **Có cơ chế kiểm soát lỗi:** Gửi lại nếu mất gói tin.
        - **Dùng trong:** Web, email, file transfer (những ứng dụng cần độ tin cậy cao).
        - **Ví dụ:** Khi bạn tải một file lớn, TCP sẽ đảm bảo file được tải về đầy đủ và đúng thứ tự.
        - **Cơ chế hoạt động**: 3-way handshake, đảm bảo kết nối trước khi truyền dữ liệu, và các cơ chế flow control và
          congestion control để tối ưu hiệu suất.
    - **UDP (User Datagram Protocol):**
        - **Không tin cậy:** Không đảm bảo dữ liệu đến nơi, có thể bị mất gói tin.
        - **Nhanh hơn:** Không có cơ chế kiểm tra lỗi, ít overhead (thông tin thừa).
        - **Dùng trong:** Game, video call, streaming (những ứng dụng cần tốc độ).
        - **Ví dụ:** Khi bạn chơi game online, nếu mất một gói tin thì game vẫn tiếp tục chạy (dù có thể giật lag 1
          chút).
- **Ví dụ hoạt động:**
    - HTTP dùng TCP để truyền tải dữ liệu (vì web cần tin cậy).
    - Video call dùng UDP để truyền dữ liệu (vì cần nhanh hơn, ít delay).
- **Lưu ý:** Port number (số cổng) để xác định ứng dụng nào đang dùng (ví dụ: HTTP dùng port 80, HTTPS dùng port 443).
- **Chủ đề chi tiết:**
    - TCP: 3-way handshake, sequence number, acknowledgment, flow control, congestion control.
    - UDP: Không kết nối, datagram.
    - Port number.

#### **3. Internet Layer (Lớp Mạng) - "ĐỊNH TUYẾN" DỮ LIỆU TRONG INTERNET**

- **Chức năng:** Định tuyến (routing) các gói tin trên Internet.
- **Nó làm gì?**
    - Thêm địa chỉ IP (source IP, destination IP) vào gói tin.
    - Tìm đường đi tốt nhất để gói tin đến đích.
- **Giao thức chính:**
    - **IP (Internet Protocol):**
        - **IPv4:** Dạng `192.168.1.1` (32 bit).
        - **IPv6:** Dạng `2001:0db8:85a3:0000:0000:8a2e:0370:7334` (128 bit, thế hệ mới).
    - Các giao thức định tuyến (Routing Protocols) như RIP, OSPF, BGP, ...
- **Ví dụ hoạt động:**
    - Khi bạn truy cập `google.com`, lớp Internet sẽ biết địa chỉ IP của máy bạn và địa chỉ IP của server Google, sau đó
      tìm đường đi ngắn nhất để gói tin đến đích.
- **Mẹo nhỏ:** Tìm hiểu về subnet mask (mặt nạ mạng), giúp chia mạng con, và NAT (Network Address Translation) để "giấu"
  địa chỉ IP thật.
- **Chủ đề chi tiết:**
    - IPv4, IPv6, subnetting, CIDR.
    - Giao thức định tuyến (RIP, OSPF, BGP).
    - NAT (Network Address Translation).
    - ICMP (Internet Control Message Protocol).

#### **4. Network Access Layer (Lớp Truy Cập Mạng) - "TRUYỀN TẢI" DỮ LIỆU TRONG MẠNG CỤC BỘ**

- **Chức năng:** Truyền dữ liệu trên mạng cục bộ (LAN).
- **Nó làm gì?**
    - Đóng gói dữ liệu vào các frame (ví dụ: Ethernet frame).
    - Truyền frame qua các phương tiện truyền dẫn (cáp, Wi-Fi).
- **Giao thức phổ biến:**
    - **Ethernet:** Dùng trong mạng có dây (dùng cáp RJ45).
        - **MAC address:** Địa chỉ vật lý của thiết bị.
    - **Wi-Fi:** Dùng trong mạng không dây.
        - **Access point:** Thiết bị phát sóng Wi-Fi.
- **Thiết bị:**
    - Card mạng (NIC - Network Interface Card).
    - Switch.
- **Ví dụ hoạt động:**
    - Khi máy tính của bạn kết nối Wi-Fi, lớp Network Access sẽ đóng gói gói tin vào frame Wi-Fi, rồi gửi lên access
      point.
- **Mẹo nhỏ:** Tìm hiểu về Ethernet frame, Wi-Fi frame, và cách các thiết bị mạng gửi dữ liệu cho nhau.
- **Chủ đề chi tiết:**
    - Ethernet frame format (MAC address, EtherType, ...).
    - Wi-Fi (802.11) protocol.
    - Switch, hub, bridge, ...
    - ARP (Address Resolution Protocol).

### **III. TÓM LƯỢC**

| Layer          | Chức năng chính                    | Giao thức/Ví dụ                        |
|----------------|------------------------------------|----------------------------------------|
| Application    | Cung cấp dịch vụ mạng cho ứng dụng | HTTP, FTP, SMTP, DNS, SSH, Telnet, ... |
| Transport      | Truyền dữ liệu giữa các ứng dụng   | TCP (tin cậy), UDP (không tin cậy)     |
| Internet       | Định tuyến gói tin trên mạng       | IP (IPv4, IPv6), ICMP                  |
| Network Access | Truyền dữ liệu trên mạng cục bộ    | Ethernet, Wi-Fi, MAC Address           |

### **IV. SƠ ĐỒ HOẠT ĐỘNG (CÁCH DỮ LIỆU "ĐI" QUA CÁC LỚP)**

1. **Ứng dụng gửi dữ liệu:** Dữ liệu sẽ đi từ lớp application xuống các lớp dưới.
    - Mỗi lớp sẽ thêm header (thông tin điều khiển) vào dữ liệu.
2. **Dữ liệu được truyền đi:** Dữ liệu được truyền tải qua mạng (lớp network access).
3. **Ứng dụng nhận dữ liệu:** Dữ liệu sẽ đi từ lớp network access lên các lớp trên.
    - Mỗi lớp sẽ loại bỏ header tương ứng.
    - Dữ liệu được đưa đến ứng dụng.

### **V. VÍ DỤ THỰC TẾ (MỘT GÓI TIN "ĐI" TRÊN INTERNET)**

Giả sử bạn mở trang web Google (dùng HTTP):

1. **Application Layer:**
    - Trình duyệt tạo request HTTP để lấy trang web.
2. **Transport Layer:**
    - Dùng TCP để đảm bảo dữ liệu được truyền đầy đủ, đúng thứ tự.
3. **Internet Layer:**
    - Thêm địa chỉ IP của bạn và địa chỉ IP của Google vào gói tin.
4. **Network Access Layer:**
    - Truyền gói tin qua Wi-Fi, Ethernet, ...

Sau đó, các gói tin sẽ đi ngược lại qua các lớp ở máy chủ Google, và trả kết quả về cho bạn.

### **VI. SO SÁNH VỚI MÔ HÌNH OSI (TCP/IP VS OSI - "ĐẤU" VỚI NHAU)**

- **OSI:** 7 lớp, chi tiết, đầy đủ.
- **TCP/IP:** 4 lớp, đơn giản, thực tế.
- **Mối liên hệ:**
    - Application layer (TCP/IP) ≈ Application, Presentation, Session (OSI).
    - Transport layer (TCP/IP) ≈ Transport (OSI).
    - Internet layer (TCP/IP) ≈ Network (OSI).
    - Network Access layer (TCP/IP) ≈ Data Link, Physical (OSI).

### **VII. CÁC GIAO THỨC CHÍNH (CÁC "NGÔN NGỮ" CỦA MẠNG)**

- **TCP (Transmission Control Protocol):**
    - Tin cậy, có thứ tự, dùng trong web, email.
- **UDP (User Datagram Protocol):**
    - Không tin cậy, nhanh hơn, dùng trong game, video call.
- **IP (Internet Protocol):**
    - Giao thức định tuyến, địa chỉ IP.
- **HTTP (Hypertext Transfer Protocol):**
    - Truyền tải dữ liệu web (HTML, CSS, JavaScript).
- **DNS (Domain Name System):**
    - Phân giải tên miền (google.com) thành địa chỉ IP.

### **VIII. CÁC THIẾT BỊ MẠNG (NHỮNG "MẢNH GHÉP" CỦA MẠNG)**

- **Router:** Định tuyến gói tin giữa các mạng.
- **Switch:** Kết nối các thiết bị trong mạng LAN.
- **Hub:** Chia sẻ băng thông (ít dùng ngày nay).
- **Modem:** Kết nối mạng với Internet.
- **Access Point:** Cho phép thiết bị kết nối Wi-Fi.

### **IX. BẢO MẬT MẠNG (BẢO VỆ "CON ĐƯỜNG" TRUYỀN DỮ LIỆU)**

- **Tường lửa (Firewall):** Chặn các truy cập trái phép.
- **IDS (Intrusion Detection System):** Phát hiện các hành vi xâm nhập.
- **IPS (Intrusion Prevention System):** Ngăn chặn các hành vi xâm nhập.
- **VPN (Virtual Private Network):** Tạo kết nối an toàn.
- **Tấn công mạng:** DoS, DDoS, Man-in-the-Middle,...

### **X. TÓM LƯỢC**

- **Mô hình TCP/IP:** Chia mạng thành 4 lớp đơn giản, dễ hiểu.
- **TCP/UDP:** Hai giao thức truyền tải dữ liệu chính.
- **IP:** Giao thức định tuyến, địa chỉ IP.
- **HTTP, DNS, ...:** Các giao thức lớp ứng dụng.
- **Bảo mật:** Quan trọng để bảo vệ thông tin trên mạng.

### **XI. KẾT LUẬN (TỔNG KẾT)**

Mô hình TCP/IP là "bản đồ" quan trọng để hiểu cách Internet hoạt động. Nắm vững kiến thức về nó sẽ giúp bạn xây dựng các
ứng dụng mạng hiệu quả hơn. Chúc các bạn học tập thành công! 😎
