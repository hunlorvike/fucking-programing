## Quản lý bộ nhớ (Memory Management)

### 1. Giới thiệu

Quản lý bộ nhớ là một trong những chức năng quan trọng nhất của hệ điều hành. Nó đảm nhận vai trò phân bổ, quản lý và bảo vệ bộ nhớ cho các tiến trình đang chạy trên hệ thống. Mục tiêu chính của quản lý bộ nhớ là tối ưu hóa việc sử dụng bộ nhớ, đảm bảo tính toàn vẹn của dữ liệu và cho phép nhiều tiến trình chạy đồng thời một cách hiệu quả và an toàn.

### 2. Mục tiêu và vai trò của quản lý bộ nhớ

- **Cấp phát bộ nhớ:** Phân phối bộ nhớ cho các tiến trình theo yêu cầu của chúng.
- **Thu hồi bộ nhớ:** Giải phóng bộ nhớ khi tiến trình kết thúc hoặc không còn sử dụng nữa.
- **Bảo vệ bộ nhớ:** Ngăn chặn các tiến trình truy cập trái phép vào bộ nhớ của tiến trình khác, bảo vệ tính toàn vẹn của dữ liệu.
- **Tăng hiệu quả sử dụng bộ nhớ:** Tối ưu hóa việc sử dụng bộ nhớ vật lý, giảm thiểu lãng phí và phân mảnh bộ nhớ.

### 3. Khái niệm cơ bản

- **Bộ nhớ vật lý:** Không gian bộ nhớ thực tế trên hệ thống, thường là RAM.
- **Bộ nhớ ảo:** Một lớp trừu tượng được cung cấp bởi hệ điều hành, cho phép các tiến trình sử dụng một không gian bộ nhớ lớn hơn bộ nhớ vật lý bằng cách sử dụng ổ đĩa cứng làm bộ nhớ bổ sung.
- **Không gian địa chỉ:** Phạm vi địa chỉ mà tiến trình có thể truy cập, bao gồm địa chỉ ảo và địa chỉ vật lý.
- **Trang (Page):** Một đơn vị bộ nhớ có kích thước cố định được sử dụng trong kỹ thuật phân trang.
- **Khung trang (Page frame):** Một đơn vị bộ nhớ trong bộ nhớ vật lý có cùng kích thước với trang.
- **Phân đoạn (Segment):** Một đơn vị bộ nhớ có kích thước thay đổi, thường đại diện cho một phần của chương trình (ví dụ: mã lệnh, dữ liệu).
- **Bảng trang (Page table):** Lưu trữ thông tin ánh xạ giữa địa chỉ ảo và địa chỉ vật lý cho từng trang của tiến trình.
- **Bảng phân đoạn (Segment table):** Lưu trữ thông tin ánh xạ giữa địa chỉ ảo và địa chỉ vật lý cho từng phân đoạn của tiến trình.

### 4. Các kỹ thuật quản lý bộ nhớ

#### 4.1. Quản lý bộ nhớ đơn giản

- **Phân đoạn tĩnh:** Chia bộ nhớ vật lý thành các phân đoạn cố định có kích thước xác định trước.
  - **Ưu điểm:** Dễ quản lý, hiệu quả trong trường hợp các tiến trình có kích thước tương đương với các phân đoạn.
  - **Nhược điểm:** Gây lãng phí bộ nhớ nếu kích thước tiến trình không phù hợp với kích thước phân đoạn.
- **Phân đoạn động:** Phân bổ bộ nhớ cho tiến trình theo nhu cầu của chúng.
  - **Ưu điểm:** Giảm lãng phí bộ nhớ, phù hợp với các tiến trình có kích thước thay đổi.
  - **Nhược điểm:** Dễ gây phân mảnh bộ nhớ (tình trạng nhiều vùng trống nhỏ không liên tục), khó quản lý.

#### 4.2. Phân trang (Paging)

- **Khái niệm:** Chia bộ nhớ vật lý và bộ nhớ ảo thành các trang có kích thước bằng nhau. Khi tiến trình yêu cầu bộ nhớ, các trang của nó được lưu trữ vào các khung trang có sẵn trong bộ nhớ vật lý.
- **Ưu điểm:**
  - Giảm thiểu phân mảnh ngoài.
  - Hỗ trợ bộ nhớ ảo.
  - Dễ dàng quản lý bộ nhớ.
- **Nhược điểm:**
  - Cần bảng trang để ánh xạ địa chỉ, có thể làm giảm hiệu suất nếu bảng trang quá lớn.
- **Bảng trang:** Lưu trữ thông tin ánh xạ giữa địa chỉ ảo và địa chỉ vật lý cho từng trang của tiến trình.

#### 4.3. Phân đoạn (Segmentation)

- **Khái niệm:** Chia bộ nhớ ảo thành các phân đoạn có kích thước thay đổi, mỗi phân đoạn đại diện cho một phần của chương trình (ví dụ: mã lệnh, dữ liệu, ngăn xếp).
- **Ưu điểm:**
  - Cung cấp cấu trúc cho bộ nhớ.
  - Dễ dàng thực thi các cơ chế bảo vệ bộ nhớ.
  - Phù hợp với các chương trình có cấu trúc logic rõ ràng.
- **Nhược điểm:**
  - Cần bảng phân đoạn để ánh xạ địa chỉ, có thể làm giảm hiệu suất.
- **Bảng phân đoạn:** Lưu trữ thông tin ánh xạ giữa địa chỉ ảo và địa chỉ vật lý cho từng phân đoạn của tiến trình.

#### 4.4. Bộ nhớ ảo (Virtual Memory)

- **Khái niệm:** Cho phép các tiến trình sử dụng một không gian bộ nhớ lớn hơn bộ nhớ vật lý bằng cách sử dụng ổ đĩa cứng làm bộ nhớ bổ sung.
- **Swap và Paging:**
  - **Swap:** Di chuyển các trang ít được sử dụng từ bộ nhớ vật lý ra ổ đĩa cứng.
  - **Paging:** Phân chia bộ nhớ ảo thành các trang và ánh xạ chúng vào các khung trang trong bộ nhớ vật lý.
- **Ưu điểm:**
  - Hỗ trợ nhiều tiến trình chạy đồng thời trên bộ nhớ vật lý hạn chế.
  - Nâng cao khả năng mở rộng của hệ thống.
- **Nhược điểm:**
  - Tốc độ truy cập bộ nhớ chậm hơn so với bộ nhớ vật lý.
  - Có thể gây ra tình trạng "thắt cổ chai" nếu quá trình swap diễn ra thường xuyên.

### 5. Thuật toán thay thế trang (Page Replacement Algorithms)

- **Khái niệm:** Khi bộ nhớ vật lý đầy, hệ điều hành phải chọn trang nào sẽ được thay thế bằng một trang mới.
- **Các thuật toán phổ biến:**
  - **FIFO (First-In-First-Out):** Thay thế trang được đưa vào bộ nhớ sớm nhất.
  - **LRU (Least Recently Used):** Thay thế trang ít được sử dụng gần đây nhất.
  - **Optimal:** Thay thế trang sẽ không được sử dụng lâu nhất trong tương lai (thuật toán lý tưởng, không thực hiện được trong thực tế).
  - **Clock:** Cải tiến từ LRU, theo dõi trạng thái của các trang bằng một vòng xoay.

### 6. Vấn đề phân mảnh bộ nhớ

- **Phân mảnh ngoài (External Fragmentation):** Xảy ra khi có nhiều vùng trống trong bộ nhớ nhưng không liên tục, không thể cấp phát cho tiến trình có kích thước lớn.
- **Phân mảnh trong (Internal Fragmentation):** Xảy ra khi bộ nhớ được cấp phát cho tiến trình lớn hơn dung lượng tiến trình cần, phần dư thừa bị lãng phí.
- **Các kỹ thuật giảm phân mảnh:**
  - **Kỹ thuật phân trang:** Giảm phân mảnh ngoài bằng cách chia bộ nhớ thành các trang có kích thước bằng nhau.
  - **Gộp bộ nhớ (Memory Compaction):** Di chuyển các tiến trình trong bộ nhớ để tạo ra các vùng trống liên tục.
  - **Phân vùng động:** Cấp phát bộ nhớ theo đúng kích thước tiến trình yêu cầu, giảm phân mảnh trong.

### 7. Bộ quản lý bộ nhớ (Memory Management Unit - MMU)

- **MMU:** Là một thành phần phần cứng hoặc phần mềm có nhiệm vụ chuyển đổi địa chỉ ảo sang địa chỉ vật lý.
- **Chuyển đổi địa chỉ (Address Translation):** MMU sử dụng bảng trang hoặc bảng phân đoạn để tìm địa chỉ vật lý tương ứng với địa chỉ ảo mà tiến trình yêu cầu.
- **Bộ đệm dịch địa chỉ (Translation Lookaside Buffer - TLB):** Bộ nhớ đệm lưu trữ các ánh xạ trang gần đây, giúp tăng tốc độ chuyển đổi địa chỉ.

### 8. Bảo vệ và an toàn bộ nhớ

- **Bảo vệ bộ nhớ:** Ngăn chặn các tiến trình truy cập trái phép vào bộ nhớ của tiến trình khác.
- **Bit bảo vệ:** Mỗi trang hoặc phân đoạn có một bit bảo vệ, cho phép hoặc cấm quyền truy cập (đọc, ghi, thực thi) của tiến trình.
- **Cơ chế ngoại lệ:** Hệ điều hành sẽ tạo ra một ngoại lệ khi tiến trình cố gắng truy cập trái phép vào bộ nhớ.

### 9. Ý nghĩa của quản lý bộ nhớ

- **Tối ưu hóa tài nguyên:** Đảm bảo sử dụng hiệu quả bộ nhớ vật lý, giảm lãng phí và phân mảnh.
- **Tăng hiệu năng hệ thống:** Tăng tốc độ truy xuất bộ nhớ, giảm thời gian xử lý của tiến trình.
- **Hỗ trợ đa nhiệm:** Cho phép nhiều tiến trình chạy đồng thời trên bộ nhớ vật lý hạn chế.
- **Tăng tính bảo mật:** Ngăn chặn truy cập trái phép, bảo vệ dữ liệu và ngăn ngừa lỗi không mong muốn.

### 10. Kết luận

Quản lý bộ nhớ là một phần thiết yếu của hệ điều hành, đảm bảo hiệu suất và an toàn cho hệ thống. Các kỹ thuật quản lý bộ nhớ như phân trang, phân đoạn và bộ nhớ ảo đã được phát triển để tối ưu hóa việc sử dụng bộ nhớ, hỗ trợ đa nhiệm và bảo vệ dữ liệu.
