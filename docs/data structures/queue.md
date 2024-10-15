## Hàng đợi (Queue)

**Đặc điểm:**

- Là một cấu trúc dữ liệu tuyến tính, tức là các phần tử được sắp xếp theo một thứ tự tuyến tính.
- Tuân theo nguyên tắc FIFO (First In, First Out): Phần tử được thêm vào đầu tiên sẽ được lấy ra đầu tiên.
- Có hai thao tác chính:
  - **Enqueue:** Thêm một phần tử vào cuối hàng đợi.
  - **Dequeue:** Lấy ra phần tử ở đầu hàng đợi.
- Ngoài ra, còn có các thao tác khác như:
  - **Peek:** Xem phần tử ở đầu hàng đợi mà không lấy nó ra.
  - **IsEmpty:** Kiểm tra xem hàng đợi có rỗng hay không.

**Ưu điểm:**

- **Xử lý dữ liệu theo thứ tự:** Hàng đợi rất hiệu quả khi xử lý dữ liệu theo thứ tự đến trước, chẳng hạn như:
  - Lập lịch CPU: Các tiến trình được thêm vào hàng đợi và xử lý theo thứ tự đến.
  - Quản lý yêu cầu trong hệ thống mạng: Các yêu cầu được thêm vào hàng đợi và xử lý theo thứ tự đến.
- **Dễ triển khai:** Hàng đợi có thể được triển khai một cách đơn giản bằng mảng hoặc danh sách liên kết.

**Nhược điểm:**

- **Truy cập hạn chế:** Chỉ có thể thao tác với phần tử ở đầu và cuối hàng đợi. Việc truy cập các phần tử khác trong hàng đợi yêu cầu dequeue các phần tử ở trên.
- **Khó tìm kiếm:** Việc tìm kiếm một phần tử cụ thể trong hàng đợi có độ phức tạp thời gian O(n) (n là số lượng phần tử).

**Ứng dụng:**

- **Lập lịch CPU:** Các tiến trình được thêm vào hàng đợi và xử lý theo thứ tự đến.
- **Quản lý yêu cầu trong hệ thống mạng:** Các yêu cầu được thêm vào hàng đợi và xử lý theo thứ tự đến.
- **Xử lý dữ liệu trong trò chơi:** Hàng đợi được sử dụng để lưu trữ các sự kiện xảy ra trong trò chơi và xử lý chúng theo thứ tự.
- **Hệ thống in ấn:** Các công việc in được thêm vào hàng đợi và xử lý theo thứ tự đến.

**Ví dụ:**

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Tạo một hàng đợi
my_queue = Queue()

# Thêm các phần tử vào hàng đợi
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# Lấy ra phần tử ở đầu hàng đợi
print(my_queue.dequeue())  # Output: 1

# Xem phần tử ở đầu hàng đợi
print(my_queue.peek())  # Output: 2
```

**Bổ sung:**

- Hàng đợi là một cấu trúc dữ liệu rất quan trọng trong lập trình, được sử dụng trong nhiều thuật toán và cấu trúc dữ liệu khác.
- Hàng đợi có thể được triển khai bằng mảng hoặc danh sách liên kết, nhưng việc triển khai bằng danh sách liên kết thường hiệu quả hơn, đặc biệt khi cần chèn/xóa các phần tử ở đầu hàng đợi.
