## **🚀 "GIẢI MÃ" TCP VÀ UDP: HAI "PHƯƠNG THỨC" TRUYỀN DỮ LIỆU TRÊN INTERNET CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" về hai giao thức cốt lõi trong mạng Internet: TCP và
UDP. Đây là hai "cách nói chuyện" khác nhau giữa các máy tính, mỗi giao thức có ưu điểm và nhược điểm riêng. Cùng mình "
mổ xẻ" chúng nhé!

![TCP vs UDP](/assets/images/TCP-vs-UDP.webp)

### **I. TCP VÀ UDP LÀ GÌ? (CÁCH THIẾT BỊ "NÓI CHUYỆN" VỚI NHAU)**

- **TCP (Transmission Control Protocol):** Là giao thức _tin cậy_, có thứ tự, dùng để truyền dữ liệu giữa các ứng dụng.
- **UDP (User Datagram Protocol):** Là giao thức _không tin cậy_, nhanh hơn, dùng cho các ứng dụng cần tốc độ.
- **Tóm lại:**
    - **TCP:** Giống như gửi thư bảo đảm, đến nơi đầy đủ và đúng thứ tự.
    - **UDP:** Giống như gọi điện, có thể mất tiếng nhưng nhanh.

### **II. TCP (TRANSMISSION CONTROL PROTOCOL): "GỬI THƯ BẢO ĐẢM"**

#### **2.1. ĐẶC ĐIỂM (CÓ GÌ HAY?)**

- **Kết nối tin cậy:** Đảm bảo dữ liệu đến nơi đầy đủ và đúng thứ tự.
- **Có cơ chế kiểm soát lỗi:** Nếu mất gói tin, sẽ tự động gửi lại.
- **Có bắt tay 3 bước (3-way handshake):** Xác định kết nối trước khi truyền dữ liệu.
- **Có kiểm soát tắc nghẽn:** Tránh làm nghẽn mạng.
- **Chậm hơn:** Vì có nhiều cơ chế đảm bảo.
- **Ví dụ:** HTTP (web), email, file transfer.

#### **2.2. CƠ CHẾ HOẠT ĐỘNG (CÁCH TRUYỀN DỮ LIỆU)**

1. **3-way handshake:**
    - **SYN (synchronize):** Client gửi yêu cầu kết nối (SYN).
    - **SYN-ACK (synchronize-acknowledge):** Server gửi xác nhận và yêu cầu đồng bộ (SYN-ACK).
    - **ACK (acknowledge):** Client gửi xác nhận cuối cùng (ACK).
2. **Truyền dữ liệu:** Dữ liệu được chia thành các gói (segment), mỗi gói có số thứ tự.
3. **Kiểm tra và gửi lại:** Nếu mất gói tin, server sẽ yêu cầu gửi lại.
4. **Sắp xếp:** Dữ liệu được sắp xếp lại đúng thứ tự khi đến đích.

#### **2.3. ƯU ĐIỂM (ĐIỂM "ĐÁNG YÊU")**

- **Tin cậy:** Dữ liệu đến nơi đầy đủ và đúng thứ tự.
- **Đảm bảo:** Không lo mất mát, sai thứ tự dữ liệu.

#### **2.4. NHƯỢC ĐIỂM (ĐIỂM "KHÓ CHỊU")**

- **Chậm hơn:** Do có nhiều cơ chế kiểm tra, có thể chậm hơn UDP.
- **Overhead:** Có thêm nhiều thông tin (header) trong mỗi gói tin.

### **III. UDP (USER DATAGRAM PROTOCOL): "GỌI ĐIỆN THOẠI"**

#### **3.1. ĐẶC ĐIỂM (CÓ GÌ HAY?)**

- **Không tin cậy:** Không đảm bảo dữ liệu đến nơi (có thể bị mất).
- **Không có thứ tự:** Không đảm bảo thứ tự các gói tin đến.
- **Không kết nối:** Không cần thiết lập kết nối trước khi truyền dữ liệu.
- **Nhanh hơn:** Vì không có cơ chế kiểm tra và gửi lại.
- **Ít overhead:** Gói tin UDP đơn giản hơn TCP.
- **Ví dụ:** Game online, video call, streaming.

#### **3.2. CƠ CHẾ HOẠT ĐỘNG (CÁCH TRUYỀN DỮ LIỆU)**

1. **Gửi:** Dữ liệu được chia thành các gói (datagram).
2. **Không đảm bảo:** UDP không đảm bảo dữ liệu sẽ đến nơi (có thể bị mất hoặc đến không đúng thứ tự).
3. **Nhanh:** Vì không cần kiểm tra, không cần thiết lập kết nối.

#### **3.3. ƯU ĐIỂM (ĐIỂM "ĐÁNG YÊU")**

- **Nhanh:** Truyền dữ liệu nhanh hơn TCP.
- **Overhead thấp:** Tiết kiệm băng thông.
- **Thích hợp cho streaming, game:** Vì có thể mất gói tin nhưng vẫn chạy được.

#### **3.4. NHƯỢC ĐIỂM (ĐIỂM "KHÓ CHỊU")**

- **Không tin cậy:** Có thể mất gói tin, dữ liệu đến không đúng thứ tự.
- **Không đảm bảo:** Không có cơ chế kiểm tra và gửi lại nếu có lỗi.

### **IV. SO SÁNH TCP VÀ UDP (AI "NGON" HƠN?)**

| Tính chất    | TCP                                     | UDP                              |
|--------------|-----------------------------------------|----------------------------------|
| **Tin cậy**  | Có (đảm bảo)                            | Không (có thể mất)               |
| **Thứ tự**   | Có (đảm bảo đúng thứ tự)                | Không (có thể không đúng thứ tự) |
| **Kết nối**  | Cần thiết lập kết nối (3-way handshake) | Không cần                        |
| **Tốc độ**   | Chậm hơn                                | Nhanh hơn                        |
| **Overhead** | Cao hơn (nhiều header)                  | Thấp hơn                         |
| **Ứng dụng** | Web, email, file transfer, ...          | Game, video call, streaming, ... |

### **V. KHI NÀO NÊN DÙNG TCP VÀ UDP (CHỌN ĐÚNG "VŨ KHÍ")**

- **TCP:**
    - Khi cần độ tin cậy cao (dữ liệu phải đến nơi đầy đủ, đúng thứ tự).
    - **Ví dụ:** Web browsing, email, download file.
- **UDP:**
    - Khi cần tốc độ cao, có thể chấp nhận mất gói tin.
    - **Ví dụ:** Game online, video call, streaming, DNS, ...

### **VI. LƯU Ý QUAN TRỌNG (ĐỂ KHÔNG BỊ "SAI SÓT")**

- **Hiểu rõ mục đích:** Dùng TCP khi cần tin cậy, UDP khi cần nhanh.
- **Không có cái nào "tuyệt đối" hơn:** Mỗi giao thức có ưu và nhược điểm riêng.
- **TCP chậm hơn nhưng tin cậy hơn:** UDP nhanh hơn nhưng không đảm bảo.

### **VII. KẾT LUẬN (TỔNG KẾT)**

TCP và UDP là hai giao thức quan trọng trong mạng máy tính, mỗi giao thức có vai trò và ứng dụng riêng. Hy vọng qua bài
viết này, các bạn đã hiểu rõ hơn về chúng và có thể lựa chọn giao thức phù hợp cho ứng dụng của mình. Chúc các bạn code
thành công! 😎
