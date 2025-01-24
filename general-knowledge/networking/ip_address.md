## **🚀 "GIẢI MÃ" ĐỊA CHỈ IP: "SỐ NHÀ" TRÊN MẠNG 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "mổ xẻ" một trong những khái niệm cơ bản nhất của mạng máy tính:
Địa chỉ IP (IP Address). Nghe có vẻ "hàn lâm" nhưng thực ra rất quen thuộc và cần thiết để các thiết bị "tìm thấy" nhau
trên mạng. Cùng mình "khám phá" nó nhé!

![IP ADDRESS](/assets/images/ip-address.webp)

### **I. ĐỊA CHỈ IP (IP ADDRESS) LÀ GÌ? (NHƯ "SỐ NHÀ" TRÊN MẠNG)**

- **Địa chỉ IP (IP Address):** Là một địa chỉ _logic_ dùng để định danh các thiết bị trên mạng (Internet hoặc LAN).
- **Nó hoạt động như thế nào?**
    - Giống như "số nhà" của bạn: địa chỉ IP giúp các thiết bị tìm thấy nhau và trao đổi dữ liệu.
- **Quan trọng vì:**
    - **Định danh:** Giúp các thiết bị xác định nhau trên mạng.
    - **Định tuyến:** Giúp dữ liệu đi đúng đường đến đích.
    - **Giao tiếp:** Giúp các thiết bị trao đổi thông tin.

### **II. HAI LOẠI ĐỊA CHỈ IP (HAI "ĐỊA CHỈ" KHÁC NHAU)**

1. **IPv4 (Internet Protocol version 4):**
    - Dạng: `192.168.1.1` (4 số, mỗi số từ 0 đến 255).
    - 32 bit (khá ít, gần như cạn kiệt).
    - **Ví dụ:** `172.217.160.142` (địa chỉ của `google.com`).
2. **IPv6 (Internet Protocol version 6):**
    - Dạng: `2001:0db8:85a3:0000:0000:8a2e:0370:7334` (8 nhóm số, mỗi nhóm 4 chữ số hex).
    - 128 bit (rất nhiều địa chỉ, đủ cho tương lai).
    - **Ví dụ:** `2401:4900:1132:9c62:7132:687a:978d:3596`
    - **Thường được rút gọn:** `2001:db8::8a2e:370:7334` (bỏ bớt số 0).

### **III. CÁC THÀNH PHẦN CỦA ĐỊA CHỈ IP (CÁI GÌ TRONG "SỐ NHÀ"?)**

1. **Network ID:** Phần định danh mạng (giống như tên đường).
2. **Host ID:** Phần định danh thiết bị trong mạng (giống như số nhà).
3. **Subnet Mask:** Dùng để phân biệt phần network ID và host ID.

### **IV. CÁC LỚP MẠNG IP (NHƯ CÁC "KHU VỰC" TRONG MẠNG)**

- **Lớp A:** Mạng lớn (ít mạng, nhiều máy), `0.0.0.0` đến `127.255.255.255`.
- **Lớp B:** Mạng vừa (vừa vừa), `128.0.0.0` đến `191.255.255.255`.
- **Lớp C:** Mạng nhỏ (nhiều mạng, ít máy), `192.0.0.0` đến `223.255.255.255`.
- **Lớp D:** Dùng cho multicast (gửi 1 gói tin đến nhiều máy).
- **Lớp E:** Dùng cho mục đích nghiên cứu.

### **V. SUBNET MASK ( "BẢN ĐỒ" PHÂN CHIA MẠNG)**

- **Subnet Mask:** Dùng để chia mạng lớn thành các mạng nhỏ hơn (subnet).
- **Ví dụ:**
    - `255.255.255.0` (`/24`): 24 bit đầu là network ID, 8 bit cuối là host ID.
    - `255.255.0.0` (`/16`): 16 bit đầu là network ID, 16 bit cuối là host ID.
- **CIDR (Classless Inter-Domain Routing):** Dùng `/n` để biểu diễn subnet mask (ví dụ: `/24`, `/16`).

### **VI. ĐỊA CHỈ IP PRIVATE VÀ PUBLIC (HAI LOẠI "SỐ NHÀ" KHÁC NHAU)**

- **IP Private:** Dùng trong mạng LAN, không ra được internet.
    - Ví dụ: `192.168.1.1`, `10.0.0.1`.
- **IP Public:** Dùng để kết nối vào Internet, có thể truy cập từ bên ngoài.
    - Ví dụ: Địa chỉ IP của `google.com`.

### **VII. NAT (NETWORK ADDRESS TRANSLATION) - "CHUNG SỐ NHÀ"**

- **NAT (Network Address Translation):** Chuyển đổi địa chỉ IP private sang public để các thiết bị trong mạng LAN có thể
  ra internet.
- Giúp tiết kiệm địa chỉ IP public (vì IP private không ra internet được).
- **Ví dụ:** Nhiều máy tính ở nhà có cùng IP private (ví dụ `192.168.1.x`) có thể cùng ra internet thông qua một IP
  public của router.

### **VIII. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

1. **IPv4:** `192.168.1.100` (mạng lớp C, địa chỉ private).
2. **IPv6:** `2001:0db8:85a3:0000:0000:8a2e:0370:7334` (128 bit, địa chỉ public).
3. **Địa chỉ mạng:**
    - IP: `192.168.1.100` , Subnet Mask: `255.255.255.0`, thì `192.168.1.0` là địa chỉ mạng.
4. **Subnetting:** Mạng `192.168.1.0/24` có 254 host.
5. **NAT:** Máy tính trong mạng LAN có IP private, NAT sẽ chuyển thành IP public khi ra Internet.

### **IX. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **IP private vs public:** Hiểu rõ sự khác biệt giữa IP private (LAN) và public (Internet).
- **Subnet mask:** Hiểu rõ cách chia mạng con.
- **IPv4 vs IPv6:** Biết cả hai loại địa chỉ (IPv6 đang thay thế IPv4).
- **NAT:** Hiểu về NAT, giúp nhiều thiết bị ra internet dùng 1 IP public.
- **Dynamic vs static IP:** Hiểu sự khác biệt của hai kiểu cấp IP

### **X. KẾT LUẬN (TỔNG KẾT)**

Địa chỉ IP là một khái niệm cơ bản nhưng rất quan trọng trong mạng máy tính, giúp các thiết bị giao tiếp và trao đổi dữ
liệu với nhau. Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày. Chúc
các bạn code thành công! 😎
