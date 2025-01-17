## So sánh Stateless và Stateful

### 1. **Khái Niệm Cơ Bản**

#### a. **Stateless (Không trạng thái)**

- **Định nghĩa**: Mô hình **Stateless** là nơi mỗi yêu cầu (request) từ client (khách hàng) đến server (máy chủ) được xử
  lý độc lập, không phụ thuộc vào bất kỳ yêu cầu trước đó. Tức là, server không giữ lại bất kỳ thông tin nào về trạng
  thái (state) của các phiên làm việc trước đó. Mỗi yêu cầu sẽ mang theo toàn bộ thông tin cần thiết để server có thể
  hiểu và xử lý.

- **Điều này có nghĩa là**: Khi một client gửi yêu cầu đến server, yêu cầu đó sẽ không chứa thông tin về các yêu cầu
  trước đó, và server sẽ không có bất kỳ "ký ức" nào về các yêu cầu trước. Server đơn giản chỉ phản hồi với thông tin
  được yêu cầu mà không quan tâm đến ngữ cảnh của các yêu cầu trước đó.

#### b. **Stateful (Có trạng thái)**

- **Định nghĩa**: Trong mô hình **Stateful**, server duy trì và lưu trữ thông tin về trạng thái của các yêu cầu hoặc
  phiên giao dịch trước đó. Điều này cho phép server nhận biết được tình trạng hiện tại của client và các yêu cầu trước
  đó của họ, từ đó có thể cung cấp những phản hồi liên tục, nhất quán và tương thích với yêu cầu của người dùng.

- **Điều này có nghĩa là**: Khi một client thực hiện một số thao tác với server, thông tin về các thao tác trước đó sẽ
  được server lưu trữ, ví dụ như trạng thái đăng nhập, giỏ hàng hoặc thông tin phiên làm việc (session). Điều này cho
  phép server cung cấp trải nghiệm người dùng liên tục và phản hồi dựa trên trạng thái hiện tại của client.

---

### 2. **Chi Tiết**

#### a. **Stateless (Không trạng thái)**

- **Đặc điểm**:

    - **Độc lập**: Mỗi yêu cầu từ client đến server là độc lập và không ảnh hưởng đến bất kỳ yêu cầu nào trước đó. Không
      có sự phụ thuộc giữa các yêu cầu.
    - **Khả năng mở rộng cao**: Vì không có thông tin trạng thái được lưu trữ trên server, việc mở rộng hệ thống trở nên
      dễ dàng hơn. Bạn có thể dễ dàng thêm nhiều server mà không cần phải đồng bộ hóa dữ liệu trạng thái giữa chúng.
    - **Quản lý đơn giản**: Không cần phải quản lý hoặc lưu trữ trạng thái của các phiên người dùng, vì mỗi yêu cầu đều
      phải chứa đủ thông tin để server xử lý.
    - **Tính chất không bảo mật**: Các thông tin nhạy cảm hoặc thông tin liên quan đến người dùng (như thông tin đăng
      nhập) phải được truyền tải trong mỗi yêu cầu, điều này có thể tạo ra nguy cơ bảo mật nếu không được bảo vệ đúng
      cách.

- **Ví dụ**:

    - **Giao thức HTTP**: Giao thức HTTP (HyperText Transfer Protocol) là một giao thức stateless, nghĩa là mỗi yêu cầu
      HTTP không lưu trạng thái của phiên làm việc trước đó. Khi bạn tải một trang web, server không nhớ được bạn là ai
      hoặc bạn đã thực hiện thao tác gì trước đó. Mỗi lần yêu cầu là một lần khởi tạo hoàn toàn mới.

    - **Dịch vụ RESTful API**: Các dịch vụ RESTful API thường sử dụng mô hình stateless. Mỗi yêu cầu từ client đến
      server chứa đầy đủ thông tin để server có thể xử lý mà không cần phải dựa vào trạng thái của bất kỳ yêu cầu nào
      trước đó. Điều này giúp việc xây dựng và triển khai các API trở nên đơn giản và dễ dàng mở rộng.

- **Ứng dụng**: Mô hình stateless thường được sử dụng trong các ứng dụng web, dịch vụ microservices, và các hệ thống có
  yêu cầu khối lượng lớn các truy vấn độc lập với nhau như các API RESTful.

#### b. **Stateful (Có trạng thái)**

- **Đặc điểm**:

    - **Lưu trữ thông tin**: Server lưu trữ thông tin về các yêu cầu trước đó, có thể là thông tin phiên làm việc (
      session), thông tin người dùng, hoặc trạng thái của các giao dịch. Điều này giúp duy trì một "ngữ cảnh" xuyên suốt
      cho từng người dùng.
    - **Quản lý phức tạp hơn**: Việc lưu trữ và quản lý trạng thái giữa các yêu cầu đòi hỏi hệ thống có các cơ chế đồng
      bộ và lưu trữ thông tin. Điều này có thể dẫn đến việc tăng độ trễ hoặc làm phức tạp quá trình phát triển và triển
      khai.
    - **Tính liên tục**: Trạng thái giữa các yêu cầu có thể được duy trì, điều này giúp tạo ra các trải nghiệm người
      dùng liên tục và mượt mà hơn, ví dụ như trong trường hợp giỏ hàng trực tuyến hoặc các ứng dụng cần theo dõi hành
      vi người dùng.
    - **Phụ thuộc vào phiên làm việc**: Các yêu cầu từ client sẽ phụ thuộc vào các yêu cầu trước đó, do đó server phải
      luôn nhớ thông tin liên quan đến người dùng (như đăng nhập, giỏ hàng, lịch sử tìm kiếm).

- **Ví dụ**:

    - **Ứng dụng Web với Giỏ hàng**: Một ví dụ điển hình của ứng dụng stateful là các hệ thống thương mại điện tử, nơi
      bạn thêm sản phẩm vào giỏ hàng và muốn server ghi nhớ các sản phẩm đó khi bạn tiếp tục duyệt web. Trong trường hợp
      này, server cần phải lưu trữ thông tin về giỏ hàng của bạn trong suốt phiên mua sắm.

    - **Ứng dụng Chat Online**: Các ứng dụng như trò chuyện trực tuyến (ví dụ: WhatsApp, Facebook Messenger) sử dụng mô
      hình stateful để lưu trạng thái cuộc trò chuyện, bạn có thể tiếp tục cuộc trò chuyện từ điểm dừng của lần trước mà
      không bị mất thông tin.

    - **Kết nối WebSocket**: WebSocket là một giao thức kết nối hai chiều cho phép các ứng dụng duy trì một kết nối liên
      tục giữa client và server. Trong một kết nối WebSocket, trạng thái của kết nối (bao gồm dữ liệu đã gửi và nhận)
      được duy trì trong suốt phiên kết nối.

- **Ứng dụng**: Mô hình stateful rất hữu ích trong các ứng dụng cần lưu trữ trạng thái người dùng như các ứng dụng trò
  chơi trực tuyến, các dịch vụ giao dịch tài chính, các hệ thống quản lý người dùng, hoặc các ứng dụng cần trải nghiệm
  người dùng liền mạch.

---

### 3. **Kết Luận**

#### **Stateless**:

- **Ưu điểm**:
    - **Khả năng mở rộng cao**: Dễ dàng mở rộng hệ thống mà không cần đồng bộ hóa trạng thái giữa các server.
    - **Quản lý đơn giản**: Không phải theo dõi trạng thái của các phiên làm việc, giúp giảm độ phức tạp trong quản lý.
    - **Độc lập**: Mỗi yêu cầu được xử lý độc lập, dễ dàng triển khai các hệ thống phân tán.

- **Nhược điểm**:
    - **Khó khăn trong việc duy trì thông tin người dùng**: Vì không có trạng thái lưu trữ, nên việc duy trì thông tin
      liên tục về người dùng là một thách thức.
    - **Độ trễ cao đối với các ứng dụng cần trạng thái**: Nếu yêu cầu phải chứa toàn bộ thông tin trong mỗi lần yêu cầu,
      sẽ có sự tăng độ trễ trong việc xử lý.

#### **Stateful**:

- **Ưu điểm**:
    - **Trải nghiệm người dùng liên tục**: Dễ dàng duy trì trạng thái và tạo ra trải nghiệm người dùng mượt mà và liên
      tục.
    - **Hỗ trợ các ứng dụng phức tạp**: Các ứng dụng yêu cầu thông tin người dùng được lưu trữ, như giỏ hàng hoặc hệ
      thống quản lý người dùng, có thể được triển khai dễ dàng hơn.

- **Nhược điểm**:
    - **Quản lý phức tạp**: Việc duy trì trạng thái và đồng bộ hóa dữ liệu có thể làm phức tạp quá trình triển khai và
      bảo trì hệ thống.
    - **Khả năng mở rộng hạn chế**: Mở rộng hệ thống có thể gặp khó khăn khi cần phải đồng bộ thông tin trạng thái giữa
      nhiều server.
    - **Tăng độ trễ**: Cần phải lưu trữ và truy xuất thông tin trạng thái, điều này có thể làm tăng độ trễ trong một số
      tình huống.

---

Tùy thuộc vào yêu cầu và mục tiêu của hệ thống, việc lựa chọn mô hình **stateless** hay **stateful** sẽ quyết định cách
thức triển khai và quản lý hệ thống.
