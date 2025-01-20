## Cấu trúc dữ liệu tuyến tính

Cấu trúc dữ liệu tuyến tính là những cấu trúc dữ liệu mà các phần tử được sắp xếp theo một thứ tự tuần tự. Nói cách
khác, chúng ta có thể truy cập trực tiếp đến mỗi phần tử dựa trên vị trí của nó trong chuỗi.

**Đặc điểm chính:**

- **Thứ tự tuyến tính:** Các phần tử được sắp xếp theo một thứ tự nhất định, có thể là từ trái sang phải hoặc từ trên
  xuống dưới.
- **Truy cập trực tiếp:** Chúng ta có thể truy cập trực tiếp đến một phần tử bất kỳ bằng cách sử dụng chỉ số (index) của
  nó.
- **Lưu trữ tuyến tính:** Các phần tử được lưu trữ theo thứ tự tuyến tính trong bộ nhớ.

**Các loại cấu trúc dữ liệu tuyến tính phổ biến:**

### 1. Mảng (Array)

- Một tập hợp các phần tử có cùng kiểu dữ liệu, được lưu trữ liên tiếp trong bộ nhớ.
- Truy cập nhanh đến các phần tử bằng chỉ số (index).
- Ví dụ: `[1, 2, 3, 4, 5]`

**Ưu điểm:**

- Hiệu quả trong việc truy cập trực tiếp.

**Nhược điểm:**

- Kích thước cố định, cần thêm bộ nhớ khi cần thêm phần tử.

### 2. Danh sách liên kết (Linked List)

- Các phần tử được lưu trữ dưới dạng các node, mỗi node chứa dữ liệu và con trỏ trỏ đến node tiếp theo.
- Không có kích thước cố định, dễ dàng chèn và xóa phần tử.

**Ưu điểm:**

- Linh hoạt, dễ dàng chèn và xóa.

**Nhược điểm:**

- Truy cập chậm hơn mảng, cần thêm bộ nhớ cho các con trỏ.

### 3. Ngăn xếp (Stack)

- Cấu trúc dữ liệu LIFO (Last-In First-Out) - phần tử được thêm vào cuối cùng sẽ được lấy ra đầu tiên.
- Triển khai bằng mảng hoặc danh sách liên kết.
- Ví dụ: Thêm đĩa vào một cọc đĩa (phần tử cuối cùng được thêm vào sẽ được lấy ra đầu tiên)

**Ưu điểm:**

- Sử dụng trong nhiều bài toán đệ quy và quản lý bộ nhớ.

**Nhược điểm:**

- Chỉ có thể truy cập đến phần tử ở đỉnh.

### 4. Hàng đợi (Queue)

- Cấu trúc dữ liệu FIFO (First-In First-Out) - phần tử được thêm vào đầu tiên sẽ được lấy ra đầu tiên.
- Triển khai bằng mảng hoặc danh sách liên kết.
- Ví dụ: Hành khách đợi lên xe buýt (người đến trước sẽ được lên trước).

**Ưu điểm:**

- Sử dụng trong các hệ thống xử lý sự kiện, quản lý các tác vụ.

**Nhược điểm:**

- Chỉ có thể thêm vào cuối và lấy ra đầu.

**Ưu điểm của cấu trúc dữ liệu tuyến tính:**

- Dễ hiểu và triển khai.
- Hiệu quả cho các thao tác cơ bản như chèn, xóa và tìm kiếm.
- Thích hợp cho việc lưu trữ các dữ liệu có thứ tự tuyến tính.

**Nhược điểm của cấu trúc dữ liệu tuyến tính:**

- Khó khăn trong việc thực hiện các thao tác phức tạp.
- Không hiệu quả khi cần lưu trữ dữ liệu có cấu trúc phức tạp.

**Ví dụ minh họa:**

- **Mảng:** Bạn có thể hình dung một mảng như một dãy các ngăn xếp đồ chơi, mỗi ngăn chứa một món đồ chơi. Bạn có thể dễ
  dàng lấy ra món đồ chơi thứ ba bằng cách biết chỉ số của nó (trong trường hợp này là 2, vì chỉ số bắt đầu từ 0).

- **Danh sách liên kết:** Hay một danh sách liên kết giống như một chuỗi các xe lửa, mỗi toa chứa một vật phẩm. Bạn có
  thể thêm hoặc gỡ bỏ một toa xe bất kỳ mà không cần phải di chuyển các toa khác.

**Kết luận:**

Cấu trúc dữ liệu tuyến tính đơn giản và hiệu quả cho các thao tác cơ bản, nhưng có thể không phù hợp cho các bài toán có
cấu trúc phức tạp.

Cấu trúc dữ liệu phi tuyến tính, như cây và đồ thị, cung cấp nhiều tính năng nâng cao và thường được sử dụng cho các bài
toán phức tạp hơn. Tuy nhiên, chúng cũng phức tạp hơn để triển khai và hiểu.

## Cấu trúc dữ liệu phi tuyến tính

Cấu trúc dữ liệu phi tuyến tính là những cấu trúc dữ liệu mà các phần tử không được sắp xếp theo một thứ tự tuần tự.
Thay vào đó, chúng được liên kết với nhau thông qua các mối quan hệ phức tạp hơn, thường được biểu diễn bằng các con trỏ
hoặc các liên kết.

**Đặc điểm chính:**

- **Không có thứ tự tuyến tính:** Các phần tử không được sắp xếp theo một thứ tự nhất định, chúng có thể được liên kết
  với nhau theo nhiều cách khác nhau.
- **Truy cập gián tiếp:** Chúng ta không thể truy cập trực tiếp đến một phần tử bằng cách sử dụng chỉ số (index) như
  trong mảng. Thay vào đó, chúng ta phải sử dụng các con trỏ hoặc các liên kết để tìm đến phần tử đó.
- **Lưu trữ không tuyến tính:** Các phần tử được lưu trữ theo cấu trúc liên kết, không nhất thiết theo thứ tự tuyến tính
  trong bộ nhớ.

**Các loại cấu trúc dữ liệu phi tuyến tính phổ biến:**

### 1. Cây (Tree)

- Một cấu trúc dữ liệu dạng cây, bao gồm các node được kết nối với nhau theo một cấu trúc phân cấp.
- Mỗi node có thể có một hoặc nhiều node con, ngoại trừ node gốc (root).
- Ví dụ: Cây thư mục trên máy tính, cây tìm kiếm nhị phân (BST), cây AVL, cây Red-Black.

**Ưu điểm:**

- Hiệu quả trong việc tìm kiếm, sắp xếp, và truy vấn dữ liệu theo cấu trúc phân cấp.

**Nhược điểm:**

- Khó triển khai hơn so với các cấu trúc tuyến tính.

### 2. Đồ thị (Graph)

- Một tập hợp các node (đỉnh) và các cạnh (cạnh) kết nối các node với nhau.
- Mỗi cạnh có thể được định hướng (có hướng) hoặc không định hướng (không hướng).
- Ví dụ: Bản đồ đường đi, mạng xã hội, mạng máy tính.

**Ưu điểm:**

- Phù hợp để biểu diễn các mối quan hệ phức tạp giữa các đối tượng.

**Nhược điểm:**

- Phức tạp hơn để triển khai và thao tác.

### 3. Bảng băm (Hash Table)

- Một cấu trúc dữ liệu sử dụng hàm băm (hash function) để ánh xạ khóa (key) vào một vị trí trong mảng.
- Cho phép tìm kiếm nhanh các phần tử bằng khóa.
- Ví dụ: Tìm kiếm một từ trong từ điển, lưu trữ các giá trị trong bộ nhớ cache.

**Ưu điểm:**

- Hiệu quả trong việc tìm kiếm và chèn phần tử.

**Nhược điểm:**

- Có thể xảy ra va chạm (collision) khi hai khóa khác nhau được ánh xạ vào cùng một vị trí trong mảng.

**Ưu điểm của cấu trúc dữ liệu phi tuyến tính:**

- Hiệu quả hơn trong việc thực hiện các thao tác phức tạp.
- Thích hợp cho việc lưu trữ dữ liệu có cấu trúc phức tạp.
- Cho phép truy cập dữ liệu theo nhiều cách khác nhau.

**Nhược điểm của cấu trúc dữ liệu phi tuyến tính:**

- Khó triển khai và hiểu.
- Yêu cầu bộ nhớ lớn hơn để lưu trữ các liên kết (con trỏ).

**Ví dụ minh họa:**

- **Cây thư mục trên máy tính:** Mỗi thư mục là một node, thư mục con của nó là node con.
- **Bản đồ đường đi:** Mỗi thành phố là một node, các con đường nối các thành phố là các cạnh.
- **Tìm kiếm từ trong từ điển:** Từ điển được lưu trữ trong bảng băm, mỗi từ được ánh xạ vào một vị trí trong mảng.

**Kết luận:**

Cấu trúc dữ liệu phi tuyến tính cung cấp những lợi ích lớn trong việc lưu trữ và thao tác dữ liệu có cấu trúc phức tạp.
Tuy nhiên, chúng cũng phức tạp hơn để triển khai và hiểu so với các cấu trúc dữ liệu tuyến tính. Lựa chọn loại cấu trúc
dữ liệu phù hợp phụ thuộc vào nhu cầu của bài toán.

## So sánh Cấu trúc Dữ liệu Tuyến tính và Phi tuyến tính

| Tiêu chí                         | Kiểu dữ liệu tuyến tính (Linear Data Structures)                                                                                               | Kiểu dữ liệu phi tuyến tính (Non-linear Data Structures)                                                                    |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Cấu trúc                         | Các phần tử được sắp xếp tuần tự, theo một trình tự nhất định.                                                                                 | Các phần tử không được sắp xếp tuần tự, có thể có nhiều quan hệ phức tạp giữa các phần tử.                                  |
| Mối quan hệ giữa các phần tử     | Mỗi phần tử chỉ liên kết với một phần tử trước và sau nó (ngoại trừ đầu và cuối).                                                              | Mỗi phần tử có thể liên kết với nhiều phần tử khác theo nhiều hướng (đồ thị) hoặc cấu trúc phân cấp (cây).                  |
| Truy cập phần tử                 | Dễ dàng truy cập phần tử theo thứ tự tuyến tính. Truy cập phần tử thường theo trình tự từ đầu đến cuối hoặc thông qua chỉ số.                  | Truy cập phần tử phức tạp hơn, thường thông qua các thuật toán tìm kiếm đặc biệt. Không có thứ tự rõ ràng giữa các phần tử. |
| Ví dụ                            | - Mảng (Array) <br> - Danh sách liên kết (Linked List) <br> - Ngăn xếp (Stack) <br> - Hàng đợi (Queue)                                         | - Cây (Tree) <br> - Đồ thị (Graph) <br> - Cây nhị phân tìm kiếm (Binary Search Tree)                                        |
| Tính tuần tự                     | Phần tử được tổ chức theo một hàng duy nhất, nghĩa là có thể duyệt lần lượt qua các phần tử một cách dễ dàng.                                  | Không có hàng duy nhất, có thể tồn tại nhiều đường đi để duyệt qua các phần tử khác nhau.                                   |
| Kích thước cố định hay linh hoạt | Một số cấu trúc tuyến tính (như mảng) có kích thước cố định, không dễ thay đổi kích thước. Một số khác (như danh sách liên kết) linh hoạt hơn. | Kích thước thường rất linh hoạt, có thể thêm/bớt phần tử dễ dàng mà không cần biết trước kích thước ban đầu.                |
| Phạm vi ứng dụng                 | Thường được dùng trong các bài toán đơn giản hoặc khi dữ liệu có mối quan hệ tuyến tính rõ ràng.                                               | Dùng cho các bài toán phức tạp hơn, nơi dữ liệu có mối quan hệ phân cấp hoặc không có thứ tự cố định.                       |
| Độ phức tạp thao tác             | Các thao tác như thêm, xóa, truy cập phần tử thường có độ phức tạp thấp (thường là O(1) hoặc O(n)).                                            | Các thao tác trên cây và đồ thị thường phức tạp hơn và có độ phức tạp cao hơn (có thể là O(log n) đến O(n²) hoặc cao hơn).  |

**Lưu ý:** Bảng này cung cấp một cái nhìn tổng quan về sự khác biệt giữa cấu trúc dữ liệu tuyến tính và phi tuyến tính.

**Cấu trúc dữ liệu tuyến tính và phi tuyến tính** đều có ưu điểm và nhược điểm riêng, và lựa chọn loại cấu trúc dữ liệu
phù hợp phụ thuộc vào nhu cầu của bài toán.

