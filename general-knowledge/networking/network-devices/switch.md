## **🚀 "GIẢI MÃ" THIẾT BỊ MẠNG: SWITCH - "NGƯỜI PHÂN PHỐI" DỮ LIỆU TRONG MẠNG LAN 🚀**

Yo các bạn sinh viên IT! Hôm nay, chúng ta sẽ tiếp tục "khám phá" một thiết bị mạng không thể thiếu trong bất kỳ mạng
LAN nào: Switch. Nếu Router là "người điều phối giao thông" giữa các mạng, thì Switch là "người phân phối" dữ liệu trong
một mạng LAN cụ thể. Cùng mình tìm hiểu xem Switch hoạt động như thế nào và tại sao nó lại quan trọng nhé!

### **I. SWITCH LÀ GÌ? (NHƯ "BƯU ĐIỆN" TRONG MẠNG LAN)**

- **Switch:** Là một thiết bị mạng, có nhiệm vụ **chuyển mạch** (switching) các khung dữ liệu (data frames) giữa các
  thiết bị trong cùng một mạng LAN.
- **Nó hoạt động như thế nào?**
    - Giống như "bưu điện": Switch nhận khung dữ liệu từ một thiết bị và gửi nó đến đúng thiết bị nhận.
    - Switch hoạt động ở lớp liên kết dữ liệu (Data Link Layer) trong mô hình OSI.
- **Đặc điểm:**
    - Kết nối các thiết bị trong cùng một mạng LAN (ví dụ: máy tính, máy in, server).
    - Gửi dữ liệu trực tiếp đến thiết bị đích (không gửi broadcast như hub).
    - Học địa chỉ MAC (Media Access Control) của các thiết bị để chuyển mạch dữ liệu hiệu quả.
    - Cải thiện hiệu suất mạng so với hub.

### **II. SO SÁNH SWITCH VÀ HUB (ĐỂ THẤY RÕ SỰ KHÁC BIỆT)**

| Tính chất           | Hub                            | Switch                                    |
|---------------------|--------------------------------|-------------------------------------------|
| **Chuyển dữ liệu**  | Broadcast (gửi cho tất cả)     | Unicast (gửi trực tiếp cho thiết bị đích) |
| **Địa chỉ sử dụng** | Không quan tâm địa chỉ         | Địa chỉ MAC                               |
| **Hiệu suất**       | Thấp, dễ gây xung đột          | Cao, ít xung đột                          |
| **Lớp hoạt động**   | Lớp vật lý (Physical Layer)    | Lớp liên kết dữ liệu (Data Link Layer)    |
| **Thông minh**      | Không có tính năng học địa chỉ | Có khả năng học địa chỉ MAC               |
| **Ứng dụng**        | Ít sử dụng trong mạng hiện đại | Sử dụng rộng rãi trong mạng LAN           |

### **III. CÁCH SWITCH HOẠT ĐỘNG (CƠ CHẾ "HỌC" VÀ "CHUYỂN")**

1. **Nhận khung dữ liệu:** Switch nhận khung dữ liệu từ một thiết bị kết nối.
2. **Kiểm tra địa chỉ MAC nguồn:** Switch ghi lại địa chỉ MAC nguồn (MAC address của thiết bị gửi) vào bảng địa chỉ
   MAC (MAC Address Table).
3. **Kiểm tra địa chỉ MAC đích:**
    - Nếu địa chỉ MAC đích có trong bảng: Switch chuyển khung dữ liệu đến cổng kết nối với thiết bị đích.
    - Nếu địa chỉ MAC đích không có trong bảng: Switch gửi broadcast (gửi cho tất cả các cổng, trừ cổng nhận) để tìm
      thiết bị đích.
4. **Cập nhật bảng địa chỉ MAC:** Khi thiết bị đích trả lời, Switch sẽ ghi lại địa chỉ MAC đích vào bảng.
5. **Chuyển dữ liệu:** Từ đó về sau, Switch sẽ gửi trực tiếp dữ liệu đến thiết bị đích.
6. **Lặp lại:** Quá trình này tiếp tục diễn ra khi có các khung dữ liệu mới.

### **IV. BẢNG ĐỊA CHỈ MAC (MAC ADDRESS TABLE) LÀ GÌ? (NHƯ "DANH BẠ ĐIỆN THOẠI")**

- **Bảng địa chỉ MAC:** Là một bảng ghi lại thông tin về địa chỉ MAC của các thiết bị kết nối và cổng kết nối tương ứng.
- **Nó chứa:**
    - **Địa chỉ MAC (MAC Address):** Địa chỉ vật lý của thiết bị.
    - **Cổng (Port):** Cổng kết nối mà thiết bị đó được kết nối.
- **Mục đích:** Giúp Switch biết được thiết bị nào đang kết nối vào cổng nào để chuyển dữ liệu trực tiếp đến đích.

### **V. CÁC LOẠI SWITCH (MỖI LOẠI MỘT "ĐẲNG CẤP")**

1. **Switch không quản lý (Unmanaged Switch):**

    - **Đặc điểm:** Đơn giản, dễ sử dụng, cắm là chạy (plug-and-play).
    - **Ứng dụng:** Mạng gia đình, văn phòng nhỏ.

2. **Switch có quản lý (Managed Switch):**

    - **Đặc điểm:** Nhiều tính năng nâng cao, có thể cấu hình, quản lý và giám sát.
    - **Ứng dụng:** Mạng doanh nghiệp, trung tâm dữ liệu.
    - **Các tính năng:**
        - VLAN (Virtual LAN): Chia mạng thành các mạng con.
        - QoS (Quality of Service): Ưu tiên băng thông cho các ứng dụng quan trọng.
        - Port Mirroring: Sao chép lưu lượng mạng để phân tích.
        - Spanning Tree Protocol (STP): Ngăn chặn loop mạng.

3. **Switch lớp 3 (Layer 3 Switch):**
    - **Đặc điểm:** Có khả năng định tuyến như router, hoạt động ở cả lớp liên kết dữ liệu và lớp mạng.
    - **Ứng dụng:** Mạng lớn, cần hiệu suất cao, cần chia VLAN và định tuyến.

### **VI. SWITCH TRONG MÔ HÌNH OSI (NÓ "ĐỨNG" Ở ĐÂU?)**

- **Lớp liên kết dữ liệu (Data Link Layer):** Switch hoạt động ở lớp liên kết dữ liệu, sử dụng địa chỉ MAC để chuyển
  mạch dữ liệu.
- **Chuyển khung dữ liệu:** Nhận khung dữ liệu từ lớp dưới (Physical Layer) và chuyển tiếp đến lớp trên (Network Layer)
  hoặc đến thiết bị đích.

### **VII. CÁC LỖI THƯỜNG GẶP (CẦN LƯU Ý)**

- **Broadcast Storm:** Xung đột broadcast, do loop mạng.
- **Switch Loop:** Lỗi mạng do kết nối dự phòng mà không có STP.

### **VIII. KẾT LUẬN (TỔNG KẾT)**

- **Switch:** Là thiết bị mạng quan trọng, giúp chuyển mạch dữ liệu trong mạng LAN.
- **"Bưu điện" trong LAN:** Gửi dữ liệu trực tiếp đến thiết bị đích.
- **Bảng địa chỉ MAC:** "Danh bạ" mà Switch dùng để tìm thiết bị.
- **Các loại Switch:** Không quản lý, có quản lý, lớp 3.
- **Lớp liên kết dữ liệu:** Hoạt động ở lớp liên kết dữ liệu trong mô hình OSI.
- **Cần chú ý:** Tránh broadcast storm, switch loop.

Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về switch và cách nó hoạt động trong mạng máy tính. Chúc các bạn
code thành công! 😎
