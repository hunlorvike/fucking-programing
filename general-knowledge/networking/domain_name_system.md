## **🚀 "GIẢI MÃ" DNS: "TỪ ĐIỂN" CỦA INTERNET CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" về một hệ thống cực kỳ quan trọng trong mạng Internet:
Domain Name System (DNS). Nghe có vẻ "lý thuyết" nhưng thực ra nó là "người phiên dịch" giúp chúng ta dễ dàng truy cập
website mà không cần nhớ những dãy số IP phức tạp. Cùng mình "mổ xẻ" nó nhé!

![DNS](/assets/images/dns-4-1.jpg)

### **I. DOMAIN NAME SYSTEM (DNS) LÀ GÌ? (NHƯ "TỪ ĐIỂN" CỦA INTERNET)**

- **DNS (Domain Name System):** Là hệ thống _phân giải_ tên miền (domain name - ví dụ: `google.com`) thành địa chỉ IP (
  ví dụ: `172.217.160.142`).
- **Nó hoạt động như thế nào?**
    - Giống như khi bạn tra từ điển: bạn dùng từ (tên miền) để tìm nghĩa (địa chỉ IP).
- **Quan trọng vì:**
    - **Dễ dùng:** Giúp người dùng nhớ tên dễ hơn địa chỉ IP.
    - **Linh hoạt:** Cho phép website thay đổi IP mà không ảnh hưởng đến người dùng.
    - **Internet:** Là một phần không thể thiếu của Internet.

### **II. CÁCH DNS HOẠT ĐỘNG (CÁCH "TỪ ĐIỂN" TRA CỨU)**

1. **Bạn gõ tên miền:** (ví dụ: `google.com`) vào trình duyệt.
2. **Trình duyệt hỏi DNS resolver:** Trình duyệt sẽ gửi yêu cầu tới DNS resolver (thường là của ISP).
3. **DNS resolver tìm địa chỉ IP:**
    - Nếu có trong cache: Trả về IP ngay.
    - Nếu không: Tìm kiếm ở các DNS server khác (root, TLD, authoritative).
4. **Trả về IP:** DNS resolver trả IP cho trình duyệt.
5. **Trình duyệt kết nối:** Trình duyệt dùng IP để kết nối với web server.
6. **Hiển thị web:** Web server trả về dữ liệu cho trình duyệt.

### **III. CÁC LOẠI DNS SERVER (CÁC "NGƯỜI TRA TỪ ĐIỂN")**

1. **DNS Resolver:**
    - Thường là DNS server của ISP (Internet Service Provider) của bạn.
    - Làm nhiệm vụ tìm kiếm địa chỉ IP.
    - Có cache (bộ nhớ đệm) để trả lời nhanh hơn.
2. **Root DNS Server:**
    - Nằm ở "gốc" của hệ thống DNS (chứa thông tin của các TLD DNS server).
    - **13 Root DNS Server chính**.
    - Không trực tiếp trả về IP cho bạn, mà chỉ hướng dẫn đến TLD DNS server.
3. **TLD DNS Server (Top-Level Domain DNS Server):**
    - Quản lý các tên miền cấp cao nhất (ví dụ: .com, .org, .vn).
    - Hướng dẫn đến authoritative DNS server.
4. **Authoritative DNS Server:**
    - Chứa thông tin IP chính thức của tên miền.
    - Trả về địa chỉ IP cho DNS resolver.

### **IV. CÁC LOẠI BẢN GHI DNS (CÁC LOẠI "TRANG" TRONG TỪ ĐIỂN)**

1. **A Record:** Trỏ tên miền tới địa chỉ IPv4.
    - **Ví dụ:** `google.com` -> `172.217.160.142`.
2. **AAAA Record:** Trỏ tên miền tới địa chỉ IPv6.
    - **Ví dụ:** `google.com` -> `2001:0db8:85a3:0000:0000:8a2e:0370:7334`.
3. **CNAME Record:** Tạo bí danh (alias) cho một tên miền khác.
    - **Ví dụ:** `www.example.com` -> `example.com`.
4. **MX Record:** Chỉ định mail server để nhận email.
    - **Ví dụ:** `gmail.com` -> `gmail-smtp-in.l.google.com`.
5. **NS Record:** Chỉ định nameserver của domain.
    - **Ví dụ:** `example.com` -> `ns1.example.com`, `ns2.example.com`.
6. **TXT Record:** Lưu trữ text tùy ý, thường dùng để xác thực, SPF,...
    - **Ví dụ:** Dùng để xác minh quyền sở hữu domain.

### **V. CÁCH THIẾT LẬP DNS (CÁCH "VIẾT" "TỪ ĐIỂN")**

1. **Cấu hình trên domain registrar:** (ví dụ: GoDaddy, Namecheap, ...)
    - Để trỏ tên miền đến server của bạn.
2. **Cấu hình DNS server:** (ví dụ: Cloudflare, AWS Route 53, Google Cloud DNS)
    - Tạo các bản ghi (A, CNAME, MX, TXT, ...).
3. **Cấu hình máy chủ:** (ví dụ: Cấu hình host trên server web)
    - Khi cấu hình máy chủ web cũng cần trỏ tên miền đó vào địa chỉ máy chủ.

### **VI. VÍ DỤ MINH HỌA (XEM "THỰC HÀNH")**

1. **Tra cứu DNS dùng `nslookup` (Windows):**

```
nslookup google.com
```

- **Kết quả:** Trả về địa chỉ IP của `google.com`.

2. **Tra cứu DNS dùng `dig` (Linux/MacOS):**

```
dig google.com
```

- **Kết quả:** Trả về thông tin chi tiết về các bản ghi DNS.

### **VII. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **DNS cache:** Trình duyệt, hệ điều hành, DNS resolver đều có cache để tăng tốc độ truy vấn.
- **Propagation:** DNS có thể mất chút thời gian để cập nhật trên toàn thế giới.
- **DNS record:** Hiểu rõ các loại record và cách dùng chúng.
- **DNS server:** Chọn DNS server uy tín để có tốc độ truy vấn nhanh và ổn định.

### **VIII. ỨNG DỤNG (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Truy cập website:** Phân giải tên miền khi bạn gõ địa chỉ web.
- **Gửi email:** Tìm mail server để gửi/nhận email.
- **API:** Dùng DNS để tìm địa chỉ API server.
- **Load balancing:** Phân phối traffic đến nhiều server dựa trên DNS.

### **IX. KẾT LUẬN (TỔNG KẾT)**

DNS là một hệ thống "thầm lặng" nhưng cực kỳ quan trọng, giúp Internet hoạt động một cách trơn tru và dễ dàng sử dụng.
Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào công việc hàng ngày của mình. Chúc các bạn
code thành công! 😎
