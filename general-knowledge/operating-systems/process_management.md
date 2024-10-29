## Quản lý tiến trình (Process Management)

### 1. Giới thiệu

Quản lý tiến trình là một trong những chức năng cốt lõi của hệ điều hành, chịu trách nhiệm quản lý việc tạo, hủy, và điều phối thực thi các tiến trình trong hệ thống. Một **tiến trình** là một chương trình đang chạy, bao gồm mã chương trình, dữ liệu, và ngữ cảnh thực thi. Hệ điều hành cần quản lý tiến trình để đảm bảo hiệu suất, tránh xung đột tài nguyên, và duy trì sự ổn định của hệ thống.

### 2. Khái niệm cơ bản

- **Tiến trình (Process):** Là một chương trình đang chạy, bao gồm một hoặc nhiều luồng thực thi.
- **Luồng (Thread):** Là đơn vị thực thi nhỏ hơn tiến trình, chia sẻ tài nguyên như bộ nhớ với các luồng khác trong cùng tiến trình, nhưng có ngữ cảnh riêng biệt.
- **Bảng quản lý tiến trình (Process Control Block - PCB):** Là cấu trúc dữ liệu hệ điều hành sử dụng để theo dõi thông tin về mỗi tiến trình, bao gồm ID, trạng thái, địa chỉ bộ nhớ, và thông tin về CPU.

### 3. Trạng thái của tiến trình

Tiến trình có thể tồn tại trong một số trạng thái chính sau:

- **New (Mới):** Tiến trình đang được tạo.
- **Ready (Sẵn sàng):** Tiến trình đã sẵn sàng thực thi nhưng chưa được cấp CPU.
- **Running (Đang chạy):** Tiến trình đang được CPU xử lý.
- **Waiting (Chờ):** Tiến trình đang chờ một tài nguyên hoặc sự kiện để tiếp tục.
- **Terminated (Kết thúc):** Tiến trình đã hoàn thành và đang được hệ điều hành giải phóng tài nguyên.

### 4. Các thành phần chính của quản lý tiến trình

#### 4.1. Khởi tạo và hủy tiến trình

- **Khởi tạo:**
  - Hệ điều hành cấp phát tài nguyên cho tiến trình mới, bao gồm bộ nhớ, thông tin CPU, và tạo một PCB.
  - Đưa tiến trình vào trạng thái Ready để chờ được cấp CPU.
- **Hủy tiến trình:**
  - Hệ điều hành giải phóng tất cả tài nguyên liên quan đến tiến trình đã kết thúc, bao gồm bộ nhớ và PCB.

#### 4.2. Định thời tiến trình (Process Scheduling)

- **Mục tiêu:** Đảm bảo rằng CPU được sử dụng hiệu quả bằng cách chuyển đổi giữa các tiến trình sẵn sàng.
- **Loại định thời:**
  - **Định thời sơ cấp (Long-term scheduling):** Quyết định tiến trình nào sẽ được tải vào bộ nhớ để sẵn sàng thực thi.
  - **Định thời trung cấp (Medium-term scheduling):** Chọn tiến trình để chuyển sang trạng thái chờ khi có quá nhiều tiến trình trong bộ nhớ.
  - **Định thời ngắn hạn (Short-term scheduling):** Quyết định tiến trình nào sẽ được CPU thực thi tiếp theo, thông qua thuật toán định thời.
- **Thuật toán định thời:**
  - **FCFS (First Come, First Serve):** Tiến trình đến trước sẽ được xử lý trước.
  - **SJF (Shortest Job First):** Tiến trình có thời gian ngắn nhất sẽ được ưu tiên.
  - **Round Robin (RR):** Mỗi tiến trình được cấp một thời gian nhất định để chạy, luân phiên giữa các tiến trình.
  - **Priority Scheduling:** Mỗi tiến trình có một mức độ ưu tiên. Tiến trình có ưu tiên cao sẽ được xử lý trước.
  - **Multilevel Feedback Queue:** Sử dụng nhiều hàng đợi với các mức độ ưu tiên khác nhau, cho phép thay đổi ưu tiên của tiến trình dựa trên hành vi của nó.

#### 4.3. Đồng bộ hóa và giao tiếp liên tiến trình (Inter-Process Communication - IPC)

- **Đồng bộ hóa:** Đảm bảo rằng các tiến trình không truy cập vào tài nguyên chung cùng lúc, tránh xung đột dữ liệu.
  - **Semaphore:** Một biến nguyên dùng để quản lý quyền truy cập vào tài nguyên chung.
  - **Mutex (Mutual Exclusion):** Một khóa dùng để đảm bảo chỉ một tiến trình có thể truy cập tài nguyên tại một thời điểm.
  - **Condition variable:** Cho phép các tiến trình chờ một điều kiện cụ thể xảy ra.
- **Giao tiếp:** Cho phép các tiến trình trao đổi thông tin với nhau.
  - **Pipes:** Kênh liên lạc cho phép dữ liệu truyền từ một tiến trình này sang tiến trình khác.
  - **Message Queue:** Hàng đợi tin nhắn lưu trữ thông điệp để các tiến trình giao tiếp với nhau.
  - **Shared Memory:** Một vùng bộ nhớ chung cho phép các tiến trình cùng đọc và ghi.
  - **Sockets:** Cho phép giao tiếp mạng giữa các tiến trình trên các máy tính khác nhau.

#### 4.4. Xử lý và phòng ngừa bế tắc (Deadlock)

- **Bế tắc:** Xảy ra khi một nhóm tiến trình bị khóa chờ tài nguyên của nhau, không tiến trình nào có thể tiếp tục.
- **Các điều kiện để xảy ra bế tắc:**
  - **Mutual Exclusion:** Mỗi tài nguyên chỉ được một tiến trình sử dụng.
  - **Hold and Wait:** Tiến trình giữ tài nguyên này và chờ tài nguyên khác.
  - **No Preemption:** Không có tiến trình nào có thể lấy tài nguyên từ tiến trình khác.
  - **Circular Wait:** Có một chuỗi tiến trình, mỗi tiến trình chờ tài nguyên từ tiến trình khác trong chuỗi.
- **Phòng ngừa và xử lý bế tắc:**
  - **Phòng ngừa bế tắc:** Hệ điều hành áp dụng chính sách để tránh một trong bốn điều kiện trên.
  - **Tránh bế tắc:** Áp dụng thuật toán Banker’s của Dijkstra để xác định tài nguyên có thể cấp cho tiến trình mà không gây bế tắc.
  - **Phát hiện và giải quyết bế tắc:** Hệ điều hành thường xuyên kiểm tra và phá vỡ bế tắc bằng cách dừng hoặc tái phân bổ tài nguyên.

### 5. Các cơ chế quản lý tiến trình khác

#### 5.1. Ngắt (Interrupt)

- **Ngắt:** Tín hiệu từ phần cứng hoặc phần mềm gửi đến CPU để báo hiệu một sự kiện.
- **Ngắt phần cứng:** Khi một thiết bị (như bàn phím) yêu cầu CPU xử lý.
- **Ngắt phần mềm:** Khi một chương trình cần sự hỗ trợ từ hệ điều hành.
- **Xử lý ngắt:** CPU tạm dừng tiến trình đang thực hiện để xử lý ngắt và sau đó quay lại tiến trình.

#### 5.2. Chuyển ngữ cảnh (Context Switching)

- **Chuyển ngữ cảnh:** Khi hệ điều hành quyết định chuyển từ tiến trình này sang tiến trình khác, nó phải lưu trạng thái của tiến trình hiện tại vào PCB và tải trạng thái của tiến trình tiếp theo.
- **Thời gian chuyển ngữ cảnh:** Thời gian hệ điều hành cần để hoàn tất việc chuyển đổi giữa hai tiến trình, ảnh hưởng đến hiệu suất hệ thống.

### 6. Ý nghĩa của quản lý tiến trình

- **Tối ưu hóa hiệu suất CPU:** Đảm bảo rằng CPU không bị nhàn rỗi và tiến trình nào cũng có cơ hội thực thi.
- **Bảo vệ tài nguyên:** Ngăn chặn các tiến trình xâm phạm tài nguyên của nhau, tránh xung đột dữ liệu.
- **Tăng cường khả năng đáp ứng:** Giảm thời gian chờ đợi cho tiến trình, cải thiện trải nghiệm người dùng.
- **Tăng tính ổn định và tin cậy của hệ thống:** Giúp hệ thống xử lý tốt hơn trong môi trường nhiều tiến trình.

### 7. Kết luận

Quản lý tiến trình là một phần quan trọng trong hệ điều hành, bao gồm các cơ chế khởi tạo, hủy, định thời, đồng bộ, và quản lý bế tắc. Tất cả các cơ chế này phối hợp với nhau để đảm bảo hệ thống hoạt động ổn định và hiệu quả, giúp hệ điều hành điều phối tài nguyên và đảm bảo tính toàn vẹn dữ liệu giữa các tiến trình.
