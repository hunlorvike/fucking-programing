## Deep Copy và Shallow Copy

Trong lập trình, copy (sao chép) dữ liệu là một hoạt động phổ biến. Tuy nhiên, tùy thuộc vào cách dữ liệu được sao chép,
chúng ta có hai loại copy: shallow copy (sao chép nông) và deep copy (sao chép sâu). Hiểu rõ sự khác biệt giữa hai loại
này là điều cần thiết để tránh lỗi và đảm bảo mã của bạn hoạt động như mong đợi.

### 1. Shallow Copy (Sao chép nông)

- **Định nghĩa:** Shallow copy tạo ra một bản sao mới của đối tượng gốc, nhưng chỉ sao chép địa chỉ bộ nhớ của các thành
  phần con, chứ không sao chép nội dung của chúng. Nói cách khác, shallow copy tạo ra một bản sao chứa cùng một dữ liệu
  với đối tượng gốc, nhưng dữ liệu này được lưu trữ ở một vị trí bộ nhớ khác.

- **Ví dụ:**

```python
import copy

class MyClass:
    def __init__(self, data):
        self.data = data

original = MyClass([1, 2, 3])
shallow_copy = copy.copy(original)

original.data.append(4)
print(original.data)  # Output: [1, 2, 3, 4]
print(shallow_copy.data)  # Output: [1, 2, 3, 4]
```

Trong ví dụ này, thay đổi giá trị `original.data` sẽ ảnh hưởng đến `shallow_copy.data` vì cả hai đều tham chiếu đến cùng
một danh sách.

- **Ưu điểm:**

    - Nhanh hơn deep copy vì chỉ sao chép các tham chiếu.
    - Tiết kiệm tài nguyên bộ nhớ.

- **Nhược điểm:**

    - Thay đổi dữ liệu trong bản sao shallow sẽ ảnh hưởng đến dữ liệu trong đối tượng gốc.
    - Không phù hợp khi làm việc với các cấu trúc dữ liệu phức tạp có chứa tham chiếu lồng nhau.

- **Ứng dụng:**
    - Sao chép đối tượng đơn giản, không cần thay đổi dữ liệu gốc.
    - Tạo một bản sao nhanh chóng để thao tác tạm thời.

### 2. Deep Copy (Sao chép sâu)

- **Định nghĩa:** Deep copy tạo ra một bản sao mới của đối tượng gốc, bao gồm cả việc sao chép nội dung của các thành
  phần con (thường là các đối tượng khác). Nói cách khác, deep copy tạo ra một bản sao hoàn toàn độc lập với đối tượng
  gốc, không chia sẻ bất kỳ dữ liệu nào với đối tượng gốc.

- **Ví dụ:**

```python
import copy

class MyClass:
    def __init__(self, data):
        self.data = data

original = MyClass([1, 2, 3])
deep_copy = copy.deepcopy(original)

original.data.append(4)
print(original.data)  # Output: [1, 2, 3, 4]
print(deep_copy.data)  # Output: [1, 2, 3]
```

Trong ví dụ này, thay đổi giá trị `original.data` sẽ không ảnh hưởng đến `deep_copy.data` vì `deep_copy` đã tạo ra một
bản sao độc lập của `original.data`.

- **Ưu điểm:**

    - Đảm bảo bản sao độc lập, thay đổi dữ liệu trong bản sao không ảnh hưởng đến đối tượng gốc.
    - An toàn hơn khi làm việc với các cấu trúc dữ liệu phức tạp.

- **Nhược điểm:**

    - Chậm hơn shallow copy vì phải sao chép nội dung của tất cả các thành phần con.
    - Tốn nhiều tài nguyên bộ nhớ hơn.

- **Ứng dụng:**
    - Sao chép đối tượng phức tạp, cần thay đổi dữ liệu trong bản sao mà không ảnh hưởng đến đối tượng gốc.
    - Bảo vệ dữ liệu gốc khỏi thay đổi không mong muốn.

### 3. Khi nào nên dùng Shallow Copy và Deep Copy?

- **Shallow copy:** Thích hợp khi làm việc với các cấu trúc dữ liệu đơn giản hoặc khi không cần tạo bản sao độc lập hoàn
  toàn của các phần tử con.

- **Deep copy:** Cần thiết khi làm việc với các cấu trúc dữ liệu phức tạp, hoặc khi muốn tạo ra một bản sao hoàn toàn
  độc lập để tránh thay đổi không mong muốn.

### 4. Lưu ý khi sử dụng Deep Copy:

- Deep copy có thể trở nên phức tạp khi đối tượng gốc có cấu trúc phức tạp, ví dụ như chứa các danh sách lồng nhau.
- Deep copy có thể tốn nhiều thời gian và tài nguyên hơn shallow copy, do đó hãy cân nhắc kỹ trước khi sử dụng.

### 5. Ví dụ minh họa:

```python
import copy

# Shallow copy
original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)

original_list[2].append(5)
print(original_list) # Output: [1, 2, [3, 4, 5]]
print(shallow_copied_list) # Output: [1, 2, [3, 4, 5]]

# Deep copy
original_list = [1, 2, [3, 4]]
deep_copied_list = copy.deepcopy(original_list)

original_list[2].append(5)
print(original_list) # Output: [1, 2, [3, 4, 5]]
print(deep_copied_list) # Output: [1, 2, [3, 4]]
```

Trong ví dụ này, shallow copy tạo ra một bản sao chia sẻ cùng một danh sách bên trong với `original_list`. Do đó, khi
thêm phần tử vào danh sách bên trong `original_list`, `shallow_copied_list` cũng bị ảnh hưởng. Ngược lại, deep copy tạo
ra một bản sao độc lập, do đó thay đổi `original_list` không ảnh hưởng đến `deep_copied_list`.

### 6. Kết luận:

Hiểu rõ sự khác biệt giữa shallow copy và deep copy là rất quan trọng để viết mã hiệu quả và tránh những lỗi không mong
muốn. Nên chọn loại copy phù hợp với nhu cầu của bạn để đảm bảo tính chính xác và hiệu quả của mã.
