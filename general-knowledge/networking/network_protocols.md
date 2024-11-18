# **Giao thức Mạng Máy tính: Tổng quan và Ứng dụng**

## **Mục lục**

1. [Tổng quan Giao thức Mạng](#1-tổng-quan-giao-thức-mạng)
2. [Mô hình OSI và TCP/IP](#2-mô-hình-osi-và-tcpip)
3. [Giao thức quan trọng và ứng dụng](#3-giao-thức-quan-trọng-và-ứng-dụng)
    - [3.1. Lớp ứng dụng](#31-lớp-ứng-dụng)
    - [3.2. Lớp vận chuyển](#32-lớp-vận-chuyển)
    - [3.3. Lớp mạng](#33-lớp-mạng)
    - [3.4. Lớp liên kết dữ liệu và vật lý](#34-lớp-liên-kết-dữ-liệu-và-vật-lý)
4. [Bảo mật trong mạng](#4-bảo-mật-trong-mạng)
    - [4.1. SSL/TLS](#41-ssltls)
    - [4.2. IPSec](#42-ipsec)
    - [4.3. Firewall và NAT](#43-firewall-và-nat)
5. [Các giao thức mới: HTTP/3 và QUIC](#5-các-giao-thức-mới-http3-và-quic)
6. [Ứng dụng thực tiễn](#6-ứng-dụng-thực-tiễn)
    - [Quản lý DNS và DHCP](#quản-lý-dns-và-dhcp)
    - [Bảo mật trong doanh nghiệp](#bảo-mật-trong-doanh-nghiệp)
    - [Tối ưu mạng gia đình](#tối-ưu-mạng-gia-đình)

---

## **1. Tổng quan Giao thức Mạng**

### **Định nghĩa và vai trò của giao thức mạng**
Giao thức mạng là tập hợp các quy tắc, tiêu chuẩn và thủ tục được định nghĩa để quản lý cách các thiết bị truyền tải, nhận và xử lý dữ liệu trong mạng máy tính. Đây là cơ sở để đảm bảo các thiết bị có thể giao tiếp hiệu quả và chính xác.

Các chức năng chính của giao thức mạng bao gồm:

- **Đồng bộ hóa (Synchronization):** Đảm bảo các thiết bị bắt đầu và dừng giao tiếp một cách chính xác.
- **Phát hiện lỗi (Error Detection):** Xác định và sửa lỗi dữ liệu trong quá trình truyền.
- **Tối ưu hóa truyền tải:** Kiểm soát tốc độ truyền để giảm thiểu tắc nghẽn và tối ưu hiệu suất.

---

## **2. Mô hình OSI và TCP/IP**

### **2.1 Mô hình OSI**
Mô hình OSI gồm 7 lớp, được thiết kế như một tham chiếu lý thuyết. Mỗi lớp đảm nhận một nhiệm vụ riêng biệt:

#### **Phân tích chi tiết 7 lớp:**
1. **Lớp vật lý (Physical Layer):** 
   - Truyền tín hiệu qua môi trường vật lý (cáp đồng, cáp quang, sóng không dây).
   - Ví dụ: Chuẩn Ethernet 10Base-T, 100Base-TX.
   
2. **Lớp liên kết dữ liệu (Data Link Layer):** 
   - Đảm bảo truyền dữ liệu tin cậy giữa các thiết bị liền kề.
   - Gồm hai lớp con: LLC (Logical Link Control) và MAC (Media Access Control).

3. **Lớp mạng (Network Layer):** 
   - Định tuyến dữ liệu giữa các mạng khác nhau.
   - Ví dụ: IPv4, IPv6, OSPF.

4. **Lớp vận chuyển (Transport Layer):** 
   - Quản lý kết nối và truyền tải dữ liệu giữa các ứng dụng.
   - Ví dụ: TCP (đảm bảo tin cậy), UDP (không đảm bảo tin cậy).

5. **Lớp phiên (Session Layer):** 
   - Quản lý các phiên giao tiếp, thiết lập và hủy kết nối giữa các ứng dụng.

6. **Lớp trình bày (Presentation Layer):** 
   - Mã hóa, giải mã và nén dữ liệu (ví dụ: chuyển đổi ASCII sang Unicode).

7. **Lớp ứng dụng (Application Layer):** 
   - Giao diện giữa người dùng và hệ thống mạng.
   - Ví dụ: HTTP, FTP, DNS.

---

### **2.2 Mô hình TCP/IP**
Mô hình TCP/IP, đơn giản hơn OSI, gồm 4 lớp. Đây là mô hình thực tế sử dụng rộng rãi trong Internet.

- **Lớp ứng dụng:** Tương ứng với ba lớp trên cùng của OSI. Ví dụ: HTTP, FTP, DNS.
- **Lớp vận chuyển:** Đảm bảo giao tiếp giữa các ứng dụng. Ví dụ: TCP, UDP.
- **Lớp Internet:** Định tuyến dữ liệu. Ví dụ: IPv4, IPv6.
- **Lớp liên kết:** Kết nối thiết bị trong cùng mạng cục bộ.

| **Lớp OSI** | **Lớp TCP/IP** | **Ví dụ giao thức** |
|-------------|----------------|---------------------|
| Ứng dụng    | Ứng dụng       | HTTP, DNS, FTP      |
| Vận chuyển  | Vận chuyển     | TCP, UDP            |
| Mạng        | Internet       | IP, ICMP            |
| Liên kết    | Liên kết       | Ethernet, Wi-Fi     |

---

## **3. Giao thức quan trọng và ứng dụng**

### **3.1. Lớp ứng dụng**
- **HTTP/HTTPS:** Dùng để truy cập trang web. HTTPS sử dụng SSL/TLS để mã hóa.
- **FTP/SFTP:** Truyền tải tệp tin. SFTP (Secure FTP) bảo mật hơn nhờ SSH.
- **DNS:** Chuyển đổi tên miền thành địa chỉ IP.
- **DHCP:** Tự động cấp phát IP.
- **SNMP:** Quản lý và giám sát mạng.

### **3.2. Lớp vận chuyển**
- **TCP:** Đảm bảo dữ liệu được truyền đúng thứ tự và không mất mát.
- **UDP:** Nhanh hơn TCP nhưng không đảm bảo tin cậy, phù hợp cho streaming video.

### **3.3. Lớp mạng**
- **IPv4/IPv6:** Địa chỉ hóa thiết bị.
- **OSPF, RIP, BGP:** Định tuyến gói tin qua các mạng khác nhau.

### **3.4. Lớp liên kết dữ liệu và vật lý**
- **Ethernet:** Sử dụng CSMA/CD để tránh va chạm.
- **Wi-Fi:** Chuẩn 802.11, hỗ trợ kết nối không dây.

---

## **4. Bảo mật trong mạng**

### **4.1 SSL/TLS**
- Mã hóa dữ liệu trên các giao thức như HTTPS, bảo vệ thông tin người dùng.

### **4.2 IPSec**
- Bảo mật ở lớp mạng, hỗ trợ VPN và các kết nối mã hóa.

### **4.3 Firewall và NAT**
- Firewall bảo vệ khỏi các truy cập trái phép.
- NAT tiết kiệm địa chỉ IP công cộng và tăng cường bảo mật.

---

## **5. Các giao thức mới: HTTP/3 và QUIC**

- **HTTP/3:** Phiên bản cải tiến của HTTP/2, sử dụng QUIC thay TCP.
- **QUIC:** Nhanh hơn, mã hóa toàn diện, phù hợp cho streaming và ứng dụng đòi hỏi độ trễ thấp.

---

## **6. Ứng dụng thực tiễn**

### **Quản lý DNS và DHCP**
- Cấu hình DNS công cộng (Google DNS, Cloudflare) để tăng tốc Internet.
- Dùng DHCP để quản lý IP trong mạng nội bộ.

### **Bảo mật trong doanh nghiệp**
- Sử dụng VPN để bảo mật truy cập từ xa.
- Kết hợp Firewall và IPSec để bảo vệ dữ liệu nhạy cảm.

### **Tối ưu mạng gia đình**
- Sử dụng router Wi-Fi 6, đặt mật khẩu mạnh và sử dụng WPA3 để bảo mật.

