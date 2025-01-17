# TCP/IP: Kiến trúc mạng và giao thức truyền dẫn (Nâng cao)

## Mục lục

1. [Tổng quan về TCP/IP](#1-tổng-quan-về-tcpip)
2. [Kiến trúc TCP/IP](#2-kiến-trúc-tcpip)
3. [Giao thức IP (Internet Protocol)](#3-giao-thức-ip-internet-protocol)
    - [3.1. IPv4](#31-ipv4)
    - [3.2. IPv6](#32-ipv6)
    - [3.3. Địa chỉ IP, Subnet Mask và CIDR](#33-địa-chỉ-ip-subnet-mask-và-cidr)
    - [3.4. NAT (Network Address Translation)](#34-nat-network-address-translation)
4. [Giao thức ICMP (Internet Control Message Protocol)](#4-giao-thức-icmp-internet-control-message-protocol)
    - [4.1. Chức năng của ICMP](#41-chức-năng-của-icmp)
    - [4.2. Ứng dụng thực tế](#42-ứng-dụng-thực-tế)
5. [Giao thức TCP (Transmission Control Protocol)](#5-giao-thức-tcp-transmission-control-protocol)
    - [5.1. Kết nối ba chiều (Three-Way Handshake)](#51-kết-nối-ba-chiều-three-way-handshake)
    - [5.2. Ngắt kết nối bốn bước (Four-Way Handshake)](#52-ngắt-kết-nối-bốn-bước-four-way-handshake)
    - [5.3. Kiểm soát luồng, lỗi và tắc nghẽn](#53-kiểm-soát-luồng-lỗi-và-tắc-nghẽn)
6. [Giao thức UDP (User Datagram Protocol)](#6-giao-thức-udp-user-datagram-protocol)
7. [So sánh TCP và UDP](#7-so-sánh-tcp-và-udp)
8. [Các giao thức khác trong TCP/IP](#8-các-giao-thức-khác-trong-tcpip)
    - [8.1. ARP và RARP](#81-arp-và-rarp)
    - [8.2. Giao thức định tuyến: RIP, OSPF, và BGP](#82-giao-thức-định-tuyến-rip-ospf-và-bgp)
9. [Ứng dụng thực tiễn](#9-ứng-dụng-thực-tiễn)
10. [Kết luận](#10-kết-luận)

---

## 1. Tổng quan về TCP/IP

TCP/IP (Transmission Control Protocol/Internet Protocol) là bộ giao thức chuẩn tạo nền tảng cho Internet và các mạng máy
tính hiện đại. Được phát triển từ những năm 1970, TCP/IP trở thành mô hình giao tiếp chuẩn trong việc truyền tải dữ
liệu, đảm bảo tính tương thích giữa các hệ thống khác nhau.

### **Đặc điểm chính:**

- **Hướng mô-đun:** Các giao thức được tổ chức thành các lớp độc lập, mỗi lớp thực hiện chức năng cụ thể.
- **Độc lập phần cứng:** Hỗ trợ hoạt động trên nhiều loại mạng và thiết bị khác nhau.
- **Khả năng mở rộng:** Được thiết kế để hỗ trợ các mạng từ nhỏ đến lớn, kể cả mạng toàn cầu.

---

## 2. Kiến trúc TCP/IP

### **Cấu trúc 4 lớp của TCP/IP:**

1. **Lớp ứng dụng (Application Layer):** Tương tác trực tiếp với người dùng và cung cấp các giao thức cấp cao như HTTP,
   FTP, SMTP, DNS, DHCP, SNMP.
2. **Lớp vận chuyển (Transport Layer):** Đảm bảo truyền dữ liệu đáng tin cậy qua mạng với hai giao thức chính:
    - **TCP:** Đáng tin cậy, kiểm soát lỗi, định hướng kết nối.
    - **UDP:** Nhanh, không định hướng kết nối.
3. **Lớp mạng (Internet Layer):** Quản lý định tuyến, định địa chỉ IP và phân phối dữ liệu giữa các mạng.
    - Các giao thức chính: IP, ICMP, ARP.
4. **Lớp liên kết dữ liệu/vật lý (Link Layer):** Giao tiếp với phần cứng và truyền dữ liệu qua các kết nối vật lý như
   Ethernet, Wi-Fi.

---

## 3. Giao thức IP (Internet Protocol)

IP là giao thức chính trong TCP/IP, đảm nhận việc định tuyến và truyền tải dữ liệu qua mạng.

### 3.1. **IPv4:**

- **Cấu trúc địa chỉ:** 32 bit, chia thành 4 octet (dạng `192.168.0.1`).
- **Hạn chế:** Không gian địa chỉ hạn chế (~4,3 tỷ địa chỉ) dẫn đến tình trạng thiếu hụt.
- **Header IPv4:** Bao gồm các trường như **Version, Header Length, Source IP, Destination IP, Time To Live (TTL)**.

### 3.2. **IPv6:**

- **Cấu trúc địa chỉ:** 128 bit, hỗ trợ 3,4×10³⁸ địa chỉ.
- **Ưu điểm:** Không gian địa chỉ lớn, hỗ trợ tự động cấu hình và tích hợp bảo mật (IPSec).
- **Biểu diễn:** Địa chỉ được viết dưới dạng hexadecimal (ví dụ: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`).

### 3.3. **Địa chỉ IP, Subnet Mask và CIDR:**

- **Subnet Mask:** Xác định phần mạng và phần host trong một địa chỉ IP (ví dụ: `255.255.255.0`).
- **CIDR (Classless Inter-Domain Routing):** Cách viết ngắn gọn cho subnet mask (ví dụ: `192.168.1.0/24`).

### 3.4. **NAT (Network Address Translation):**

- **Chức năng:** Biến đổi địa chỉ IP riêng (private) thành địa chỉ IP công cộng (public) và ngược lại.
- **Lợi ích:**
    - Tiết kiệm địa chỉ IP công cộng.
    - Tăng cường bảo mật bằng cách che giấu địa chỉ IP nội bộ.

---

## 4. Giao thức ICMP (Internet Control Message Protocol)

### 4.1. **Chức năng của ICMP:**

- Báo cáo lỗi mạng (ví dụ: **Destination Unreachable**).
- Kiểm tra kết nối và độ trễ (dùng lệnh **ping**).
- Xác định đường đi của gói tin (lệnh **traceroute**).

### 4.2. **Ứng dụng thực tế:**

- **Giám sát mạng:** Phát hiện lỗi và định vị các vấn đề.
- **Đánh giá hiệu suất:** Kiểm tra độ trễ và tổn thất gói tin.

---

## 5. Giao thức TCP (Transmission Control Protocol)

TCP đảm bảo truyền dữ liệu đáng tin cậy giữa các thiết bị trên mạng.

### 5.1. **Kết nối ba chiều (Three-Way Handshake):**

1. Máy gửi (Client) gửi gói **SYN** để yêu cầu kết nối.
2. Máy nhận (Server) phản hồi bằng gói **SYN-ACK**.
3. Máy gửi gửi **ACK**, hoàn tất quá trình thiết lập kết nối.

### 5.2. **Ngắt kết nối bốn bước (Four-Way Handshake):**

1. Máy gửi gửi **FIN** để yêu cầu ngắt kết nối.
2. Máy nhận phản hồi **ACK**.
3. Máy nhận gửi **FIN** để xác nhận ngắt kết nối.
4. Máy gửi phản hồi **ACK**, hoàn tất.

### 5.3. **Kiểm soát luồng, lỗi và tắc nghẽn:**

- **Sliding Window:** Điều chỉnh tốc độ truyền dữ liệu.
- **Congestion Control:** Các thuật toán như **Slow Start**, **Congestion Avoidance** giúp giảm tắc nghẽn.

---

## 6. Giao thức UDP (User Datagram Protocol)

UDP nhanh hơn TCP nhưng không đảm bảo độ tin cậy. Phù hợp với các ứng dụng như:

- Streaming video/audio.
- Dịch vụ DNS và DHCP.
- Trò chơi trực tuyến.

---

## 7. So sánh TCP và UDP

| **Tính năng**      | **TCP**                               | **UDP**                     |
|--------------------|---------------------------------------|-----------------------------|
| Định hướng kết nối | Có                                    | Không                       |
| Độ tin cậy         | Cao (xác nhận gói tin, kiểm soát lỗi) | Thấp                        |
| Tốc độ truyền      | Thấp hơn do kiểm soát tắc nghẽn       | Cao hơn                     |
| Ứng dụng phổ biến  | HTTP, FTP, Email, SSH                 | Streaming, DNS, Game online |

---

## 8. Các giao thức khác trong TCP/IP

### 8.1. **ARP và RARP:**

- **ARP (Address Resolution Protocol):** Chuyển đổi địa chỉ IP

thành địa chỉ MAC.

- **RARP (Reverse ARP):** Chuyển đổi địa chỉ MAC thành địa chỉ IP.

### 8.2. **Giao thức định tuyến:**

- **RIP (Routing Information Protocol):** Sử dụng thuật toán khoảng cách (Distance Vector).
- **OSPF (Open Shortest Path First):** Giao thức trạng thái liên kết (Link-State), tối ưu hóa đường đi.
- **BGP (Border Gateway Protocol):** Giao thức định tuyến giữa các mạng lớn trên Internet.

---

## 9. Ứng dụng thực tiễn

- **Mạng doanh nghiệp:** Đảm bảo kết nối an toàn và quản lý lưu lượng.
- **IoT (Internet of Things):** Truyền dữ liệu giữa các thiết bị thông minh.
- **Truyền phát trực tiếp:** Hỗ trợ truyền dữ liệu nhanh, hiệu quả.

---

## 10. Kết luận

TCP/IP không chỉ là nền tảng của Internet mà còn là trụ cột trong mọi hệ thống mạng. Việc nắm vững TCP/IP sẽ giúp bạn
hiểu sâu về cách mạng hoạt động, từ thiết kế hệ thống đến giải quyết các vấn đề kỹ thuật.
