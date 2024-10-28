## Immutable và Mutable trong Lập Trình

Trong lập trình, `immutable` và `mutable` là hai khái niệm cơ bản mô tả khả năng thay đổi nội dung của một đối tượng sau khi nó được tạo ra. Hiểu rõ sự khác biệt giữa hai khái niệm này là rất quan trọng để viết code an toàn, hiệu quả và dễ bảo trì.

### 1. Immutable (Bất biến):

- **Định nghĩa:** Một đối tượng `immutable` là một đối tượng mà nội dung của nó **không thể thay đổi** sau khi được khởi tạo. Bất kỳ thao tác thay đổi nào sẽ tạo ra một đối tượng mới thay vì sửa đổi đối tượng ban đầu.

- **Ví dụ:**

  - **Chuỗi (String):** Trong Python, Java, và nhiều ngôn ngữ khác, chuỗi là bất biến. Khi bạn thực hiện một thao tác sửa đổi chuỗi như nối chuỗi, thay thế ký tự,... thì một chuỗi mới sẽ được tạo ra, và biến ban đầu sẽ trỏ đến chuỗi mới này.

  - **Số (Number):** Các kiểu dữ liệu số như `int`, `float` trong Python và Java cũng là bất biến.

- **Ưu điểm:**

  - **An toàn:** Bảo vệ dữ liệu khỏi bị thay đổi không mong muốn, giúp tránh lỗi.
  - **Dễ dự đoán:** Biết rõ giá trị của đối tượng sẽ luôn giữ nguyên, giúp code dễ đọc và dễ kiểm tra.
  - **Tối ưu hóa:** Dễ dàng lưu trữ trong bộ nhớ cache và chia sẻ giữa các thread (trong lập trình đa luồng).

- **Nhược điểm:**

  - **Tốn bộ nhớ:** Phải tạo đối tượng mới mỗi khi muốn thay đổi giá trị.
  - **Có thể chậm:** Tạo đối tượng mới có thể chậm hơn so với thay đổi đối tượng hiện có.

**Ví dụ minh họa (Python):**

```python
# Ví dụ về chuỗi bất biến trong Python
s = "Hello"
print(id(s))   # In ra địa chỉ ô nhớ của s
s = s + " World"
print(id(s))   # Địa chỉ ô nhớ thay đổi vì s giờ là một object mới
```

### 2. Mutable (Biến đổi):

- **Định nghĩa:** Một đối tượng mutable là một đối tượng mà nội dung của nó **có thể thay đổi** trực tiếp mà không cần tạo ra đối tượng mới.

- **Ví dụ:**

  - **Danh sách (List):** Trong Python, danh sách là có thể thay đổi. Bạn có thể thêm, xóa, sửa đổi các phần tử của danh sách mà không cần tạo danh sách mới.

  - **Từ điển (Dictionary):** Tương tự như danh sách, bạn có thể thêm, xóa, sửa đổi các cặp key-value trong một từ điển.

- **Ưu điểm:**

  - **Hiệu suất tốt hơn:** Thay vì tạo ra một đối tượng mới mỗi khi có thay đổi, mutable object cho phép cập nhật trực tiếp, tiết kiệm bộ nhớ và thời gian xử lý.
  - **Linh hoạt:** Cho phép thay đổi giá trị theo nhu cầu, dễ dàng thao tác dữ liệu.

- **Nhược điểm:**

  - **Nguy cơ lỗi:** Có thể thay đổi giá trị không mong muốn, khó kiểm soát dữ liệu.
  - **Khó dự đoán:** Không thể biết chắc chắn giá trị của đối tượng sẽ thay đổi như thế nào, khó kiểm tra code.
  - **Khó sử dụng trong các hệ thống đa luồng:** Có thể dẫn đến tình trạng xung đột dữ liệu.

**Ví dụ minh họa (Python):**

```python
# Ví dụ về danh sách có thể thay đổi trong Python
my_list = [1, 2, 3]
print(id(my_list))   # In ra địa chỉ ô nhớ của my_list
my_list.append(4)    # Thêm phần tử vào danh sách
print(id(my_list))   # Địa chỉ ô nhớ không thay đổi vì danh sách được thay đổi trực tiếp
```

### 3. So sánh Immutable và Mutable

| Đặc điểm               | Immutable                          | Mutable                           |
| ---------------------- | ---------------------------------- | --------------------------------- |
| Thay đổi nội dung      | Không thể thay đổi nội dung        | Có thể thay đổi nội dung          |
| Ví dụ (Python)         | `str`, `int`, `tuple`, `frozenset` | `list`, `dict`, `set`             |
| An toàn trong đa luồng | Có, vì không thể thay đổi          | Không an toàn nếu không kiểm soát |
| Tiêu tốn bộ nhớ        | Tạo ra đối tượng mới khi thay đổi  | Không cần tạo đối tượng mới       |
| Hiệu suất              | Thường chậm hơn khi thay đổi       | Thường nhanh hơn khi thay đổi     |
| Dễ sử dụng             | Dễ sử dụng, dễ kiểm tra            | Khó sử dụng, khó kiểm tra         |

### 4. Lưu ý khi sử dụng:

- **Ưu tiên Immutable khi có thể:** Nếu bạn có dữ liệu không cần thay đổi, hãy dùng các loại immutable như `tuple` hoặc `str` để tránh các lỗi không mong muốn.
- **Cẩn thận với Mutable khi truyền vào hàm:** Nếu truyền một mutable object vào hàm, bất kỳ thay đổi nào trong hàm sẽ ảnh hưởng trực tiếp đến đối tượng ban đầu.
- **Sử dụng `copy()` để tránh thay đổi đối tượng gốc:** Nếu bạn muốn thay đổi một mutable object mà không ảnh hưởng đến đối tượng gốc, hãy sử dụng `copy()` để tạo một bản sao của đối tượng đó.

**Ví dụ:**

```python
def modify_list(list_to_modify):
  list_to_modify.append(4)

my_list = [1, 2, 3]
modify_list(my_list)  # Thay đổi trực tiếp danh sách my_list
print(my_list)  # Output: [1, 2, 3, 4]

my_list = [1, 2, 3]
new_list = my_list.copy()
modify_list(new_list)  # Thay đổi danh sách new_list
print(my_list)  # Output: [1, 2, 3]
print(new_list)  # Output: [1, 2, 3, 4]
```

### 5. Lưu ý thêm:

- Khái niệm immutable và mutable chủ yếu được áp dụng cho objects trong lập trình. Các biến nguyên thủy (primitive types) như `int`, `float`, `char`, `boolean` thường không có khái niệm mutable hay immutable như vậy.

- **Tại sao?**

  - **Kiểu dữ liệu nguyên thủy**: Các kiểu dữ liệu nguyên thủy thường được lưu trữ trực tiếp trong bộ nhớ. Khi bạn gán một giá trị mới cho một biến nguyên thủy, giá trị đó được ghi đè lên vị trí bộ nhớ đã được cấp phát cho biến đó.

  - **Không có tham chiếu**: Biến nguyên thủy không phải là đối tượng, chúng không có tham chiếu đến một vùng nhớ riêng biệt. Khi bạn thay đổi giá trị của một biến nguyên thủy, bạn thực sự đang thay đổi giá trị tại chính vị trí bộ nhớ đó.

```c
a = 10
b = a  # gán giá trị của a cho b
b = 20  # thay đổi giá trị của b
print(a)  # Output: 10
print(b)  # Output: 20
```

Trong ví dụ trên, `a` và `b` là các biến nguyên thủy kiểu `int`. Khi `b` được gán giá trị `20`, giá trị của `a` không bị ảnh hưởng. Điều này là do `a` và `b` đang lưu trữ hai giá trị riêng biệt trong hai vị trí bộ nhớ riêng biệt.

- **Kết luận:**

  - Khái niệm immutable và mutable chủ yếu liên quan đến đối tượng, nơi các biến trỏ đến vùng nhớ chứa dữ liệu. Các biến nguyên thủy không có tham chiếu đến vùng nhớ riêng biệt, vì vậy chúng không có khái niệm mutable hoặc immutable.

  - Tuy nhiên, trong một số ngôn ngữ lập trình, có thể có các đối tượng bao bọc các biến nguyên thủy, và đối tượng này có thể được thiết kế để có thể thay đổi hoặc không thay đổi. Ví dụ, trong Python, có đối tượng `int` là bất biến, nhưng bạn có thể tạo một đối tượng lớp bao bọc để thay đổi giá trị bên trong.
