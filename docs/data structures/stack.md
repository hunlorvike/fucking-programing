## Ngăn xếp (Stack)

**Đặc điểm:**

- Là một cấu trúc dữ liệu tuyến tính, tức là các phần tử được sắp xếp theo một thứ tự tuyến tính.
- Tuân theo nguyên tắc LIFO (Last In, First Out): Phần tử được thêm vào cuối cùng sẽ được lấy ra đầu tiên.
- Có hai thao tác chính:
  - **Push:** Thêm một phần tử vào đỉnh ngăn xếp.
  - **Pop:** Lấy ra phần tử ở đỉnh ngăn xếp.
- Ngoài ra, còn có các thao tác khác như:
  - **Peek:** Xem phần tử ở đỉnh ngăn xếp mà không lấy nó ra.
  - **IsEmpty:** Kiểm tra xem ngăn xếp có rỗng hay không.

**Ưu điểm:**

- **Quản lý lịch sử hiệu quả:** Ngăn xếp thích hợp để quản lý lịch sử các thao tác, chẳng hạn như:
  - Undo/Redo trong các phần mềm chỉnh sửa văn bản, hình ảnh.
  - Điều hướng lịch sử trong trình duyệt web.
- **Dễ triển khai:** Ngăn xếp có thể được triển khai một cách đơn giản bằng mảng hoặc danh sách liên kết.
- **Kiểm soát luồng chương trình:** Ngăn xếp được sử dụng trong các ngôn ngữ lập trình để quản lý bộ nhớ và kiểm soát luồng thực thi của chương trình.

**Nhược điểm:**

- **Truy cập hạn chế:** Chỉ có thể thao tác với phần tử ở đỉnh ngăn xếp. Việc truy cập các phần tử khác trong ngăn xếp yêu cầu pop các phần tử ở trên.
- **Khó tìm kiếm:** Việc tìm kiếm một phần tử cụ thể trong ngăn xếp có độ phức tạp thời gian O(n) (n là số lượng phần tử).

**Ứng dụng:**

- **Quản lý bộ nhớ:** Ngăn xếp được sử dụng trong các ngôn ngữ lập trình để quản lý bộ nhớ.
- **Kiểm tra biểu thức:** Kiểm tra tính hợp lệ của biểu thức chứa các dấu ngoặc, chẳng hạn như biểu thức toán học, biểu thức chính quy.
- **Giải thuật quay lui (backtracking):** Ngăn xếp được sử dụng để lưu trữ các lựa chọn đã thực hiện trong quá trình tìm kiếm lùi.
- **Lập trình hướng đối tượng:** Ngăn xếp được sử dụng để quản lý các đối tượng được tạo trong quá trình thực thi chương trình.

**Ví dụ:**

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

# Tạo một ngăn xếp
my_stack = Stack()

# Thêm các phần tử vào ngăn xếp
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Lấy ra phần tử ở đỉnh ngăn xếp
print(my_stack.pop())  # Output: 3

# Xem phần tử ở đỉnh ngăn xếp
print(my_stack.peek())  # Output: 2
```

**Bổ sung:**

- Ngăn xếp là một cấu trúc dữ liệu rất quan trọng trong lập trình, được sử dụng trong nhiều thuật toán và cấu trúc dữ liệu khác.
- Ngăn xếp có thể được triển khai bằng mảng hoặc danh sách liên kết, nhưng việc triển khai bằng danh sách liên kết thường hiệu quả hơn.
