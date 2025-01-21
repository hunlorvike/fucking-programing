## **🚀 "GIẢI MÃ" STATELESS VÀ STATEFUL: "NHỚ" HAY "QUÊN" TRONG ỨNG DỤNG CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai khái niệm quan trọng trong kiến trúc ứng dụng:
Stateless (Không trạng thái) và Stateful (Có trạng thái). Nghe có vẻ "lý thuyết" nhưng thực ra rất gần gũi và ảnh hưởng
đến cách bạn xây dựng ứng dụng web, API, ... Cùng mình "mổ xẻ" nó nhé!

### **I. STATELESS VÀ STATEFUL LÀ GÌ? (ỨNG DỤNG "NHỚ" HAY "QUÊN"?)**

- **Stateless (Không trạng thái):** Là khi mỗi yêu cầu (request) từ client đến server là _độc lập_, không liên quan gì
  đến các yêu cầu trước đó.
    - Giống như khi bạn gọi taxi: mỗi lần bạn gọi thì tài xế coi bạn là khách mới.
- **Stateful (Có trạng thái):** Là khi server _ghi nhớ_ thông tin về các yêu cầu trước đó của client.
    - Giống như khi bạn nói chuyện với bạn: bạn có thể tiếp tục câu chuyện từ lần trước mà không cần nhắc lại.
- **Tóm lại:**
    - **Stateless:** "Quên" mọi thứ sau mỗi request.
    - **Stateful:** "Nhớ" các request trước đó.

### **II. STATELESS (KHÔNG TRẠNG THÁI) - "KHÁCH LẠ" MỖI LẦN**

#### **2.1. ĐẶC ĐIỂM (CÓ GÌ HAY?)**

- **Độc lập:** Mỗi request là độc lập, không phụ thuộc vào các request trước.
- **Dễ mở rộng:** Dễ thêm server mà không cần đồng bộ trạng thái.
- **Quản lý đơn giản:** Không cần quản lý trạng thái của người dùng.
- **Thông tin trong request:** Các request đều phải chứa đầy đủ thông tin để server xử lý.

#### **2.2. VÍ DỤ**

- **HTTP:** Mỗi request HTTP là độc lập, server không nhớ bạn là ai.
- **RESTful API:** Mỗi request API chứa thông tin cần thiết để server trả về kết quả.

#### **2.3. ỨNG DỤNG (THƯỜNG DÙNG Ở ĐÂU?)**

- Ứng dụng web, API.
- Các dịch vụ microservices.
- Hệ thống có nhiều request độc lập.

### **III. STATEFUL (CÓ TRẠNG THÁI) - "BẠN CŨ" MỖI LẦN**

#### **3.1. ĐẶC ĐIỂM (CÓ GÌ HAY?)**

- **Lưu trữ thông tin:** Server lưu thông tin về các request trước đó (session, thông tin user).
- **Liên tục:** Tạo trải nghiệm mượt mà, liền mạch cho người dùng.
- **Phụ thuộc vào phiên làm việc:** Các request phụ thuộc vào các request trước đó.

#### **3.2. VÍ DỤ**

- **Giỏ hàng:** Server nhớ các sản phẩm bạn đã thêm vào giỏ.
- **Chat online:** Server nhớ trạng thái cuộc trò chuyện.
- **WebSocket:** Duy trì kết nối liên tục giữa client và server.

#### **3.3. ỨNG DỤNG (THƯỜNG DÙNG Ở ĐÂU?)**

- Ứng dụng web cần lưu trạng thái người dùng.
- Game online.
- Ứng dụng giao dịch tài chính.

### **IV. SO SÁNH STATELESS VÀ STATEFUL (ĐỂ THẤY RÕ SỰ KHÁC BIỆT)**

| Tính chất          | Stateless           | Stateful                         |
|--------------------|---------------------|----------------------------------|
| **Nhớ trạng thái** | Không               | Có                               |
| **Độc lập**        | Các request độc lập | Các request liên quan đến nhau   |
| **Mở rộng**        | Dễ                  | Khó hơn                          |
| **Quản lý**        | Đơn giản            | Phức tạp hơn                     |
| **Tính liên tục**  | Không               | Có                               |
| **Ví dụ**          | HTTP, REST API      | Giỏ hàng, Chat online, WebSocket |

### **V. KHI NÀO NÊN CHỌN CÁI NÀO? (CHỌN "VŨ KHÍ" PHÙ HỢP)**

- **Stateless:**
    - Khi cần dễ mở rộng.
    - Khi không cần lưu thông tin giữa các request.
    - Ví dụ: API, microservices.
- **Stateful:**
    - Khi cần trải nghiệm liền mạch, mượt mà.
    - Khi cần lưu thông tin người dùng (giỏ hàng, ...).
    - Ví dụ: Web app, game online.

### **VI. KẾT LUẬN (TỔNG KẾT)**

- **Stateless:** "Quên" mọi thứ, dễ mở rộng.
- **Stateful:** "Nhớ" thông tin, tạo trải nghiệm tốt hơn.
- **Chọn đúng:** Dựa vào yêu cầu của ứng dụng để chọn cho phù hợp.

Hy vọng qua bài viết này, các bạn đã hiểu rõ hơn về stateless và stateful, và có thể áp dụng vào các dự án của mình.
Chúc các bạn code thành công! 😎
