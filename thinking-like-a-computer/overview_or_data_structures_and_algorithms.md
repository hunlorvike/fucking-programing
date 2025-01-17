## Khái quát về Cấu trúc dữ liệu và Thuật toán

Bài viết này cung cấp một cái nhìn tổng quát về khái niệm Cấu trúc dữ liệu và Thuật toán, giúp độc giả tiếp cận từ góc
độ tổng quát đến chi tiết, từ trừu tượng đến cụ thể khi xem xét về Cấu trúc dữ liệu. Hy vọng thông qua bài viết này,
người đọc có thể có một cái nhìn tổng quan tốt hơn trong việc học và hiểu về Cấu trúc dữ liệu.

***Nếu bạn không có thời gian đọc kỹ, đừng bỏ qua phần thứ tư***

### 1. Cấu trúc dữ liệu đa dạng nhưng đều xuất phát từ gốc rễ chung

Ở mức độ trừu tượng cao nhất, Cấu trúc dữ liệu chỉ có hai loại: mảng (array) và danh sách liên kết (linked list).

Câu này có vẻ hơi bất ngờ, bởi vì chúng ta còn biết đến các cấu trúc dữ liệu khác như bảng băm (hash table), ngăn xếp (
stack), hàng đợi (queue), cây (tree), đồ thị (graph) và nhiều loại khác nữa.

Khi phân tích vấn đề, chúng ta cần có tư duy đệ quy, từ trên xuống dưới, từ trừu tượng đến cụ thể. Những cấu trúc dữ
liệu mà bạn liệt kê thuộc về "kiến trúc nâng cao", trong khi mảng và danh sách liên kết là "nền tảng cơ bản". Bởi vì các
cấu trúc dữ liệu đa dạng kia, xét về nguồn gốc, đều là các thao tác đặc biệt trên danh sách liên kết hoặc mảng, chỉ khác
nhau ở API mà thôi.

**Ví dụ:**

- **Stack** và **Queue** đều có thể được thực hiện bằng mảng hoặc danh sách liên kết.
    - **Mảng**: `Stack` có thể được mô phỏng bằng một mảng, đẩy và lấy phần tử từ cuối mảng. `Queue` có thể được mô
      phỏng bằng mảng, đẩy phần tử vào cuối mảng và lấy phần tử từ đầu mảng.
    - **Danh sách liên kết**: `Stack` và `Queue` có thể được mô phỏng bằng danh sách liên kết, sử dụng thao tác chèn và
      xóa đầu hoặc cuối danh sách.

```python
# Stack sử dụng danh sách liên kết
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

# Queue sử dụng mảng
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
```

- **Graph**: Có thể được biểu diễn bằng danh sách kề (linked list) hoặc ma trận kề (array).
    - **Danh sách kề**: Dùng một danh sách để lưu trữ các nút kết nối với một nút cụ thể.
    - **Ma trận kề**: Dùng một mảng hai chiều để biểu diễn các cạnh của đồ thị.

```python
# Graph sử dụng danh sách kề
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) # Cho đồ thị vô hướng

# Graph sử dụng ma trận kề
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1 # Cho đồ thị vô hướng
```

- **Hash Table**: Sử dụng hàm băm để ánh xạ các khóa vào một mảng lớn. Để giải quyết xung đột băm, có thể sử dụng phương
  pháp chuỗi liên kết (linked list) hoặc thăm dò tuyến tính (linear probing).
    - **Chuỗi liên kết**: Mỗi vị trí trong mảng chứa một danh sách liên kết chứa các phần tử có cùng khóa băm.
    - **Thăm dò tuyến tính**: Nếu vị trí băm đã bị chiếm, tìm vị trí tiếp theo trống trong mảng.

```python
# Hash Table sử dụng chuỗi liên kết
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def __hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.__hash(key)
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def get(self, key):
        index = self.__hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
```

### 2. Các thao tác trên cấu trúc dữ liệu, xoay quanh việc duyệt và truy cập

Duyệt (traverse) và truy cập (access), cụ thể hơn là: thêm (insert), xóa (delete), tìm kiếm (search), sửa đổi (update).

Các loại cấu trúc dữ liệu rất nhiều, nhưng mục đích tồn tại của chúng là để thực hiện thêm, xóa, tìm kiếm, sửa đổi một
cách hiệu quả trong các tình huống ứng dụng khác nhau. Hỏi xem, ngoài những thao tác đó ra, còn gì khác không?

Cách duyệt và truy cập? Chúng ta vẫn xem xét từ mức cao nhất, việc duyệt và truy cập của các loại cấu trúc dữ liệu chỉ
có hai hình thức: tuyến tính (linear) và phi tuyến tính (non-linear).

**Ví dụ:**

- **Duyệt mảng (linear):**

    - **Python:**

  ```python
  arr = [1, 2, 3, 4, 5]
  for i in range(len(arr)):
      print(arr[i])
  ```

    - **Java:**

  ```java
  int[] arr = {1, 2, 3, 4, 5};
  for (int i = 0; i < arr.length; i++) {
      System.out.println(arr[i]);
  }
  ```

- **Duyệt cây nhị phân (non-linear):**

    - **Python:**

  ```python
  class Node:
      def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

  def preorder_traversal(root):
      if root is None:
          return
      print(root.data, end=" ")
      preorder_traversal(root.left)
      preorder_traversal(root.right)

  # Example usage
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)

  preorder_traversal(root) # Output: 1 2 4 5 3
  ```

    - **Java:**

  ```java
  class Node {
      int data;
      Node left;
      Node right;

      public Node(int data) {
          this.data = data;
          this.left = null;
          this.right = null;
      }
  }

  public static void preorderTraversal(Node root) {
      if (root == null) {
          return;
      }
      System.out.print(root.data + " ");
      preorderTraversal(root.left);
      preorderTraversal(root.right);
  }

  // Example usage
  Node root = new Node(1);
  root.left = new Node(2);
  root.right = new Node(3);
  root.left.left = new Node(4);
  root.left.right = new Node(5);

  preorderTraversal(root); // Output: 1 2 4 5 3
  ```

### 3. Tại sao thuật toán luôn xuất hiện cùng cấu trúc dữ liệu

Cấu trúc dữ liệu là công cụ, thuật toán là cách giải quyết vấn đề bằng công cụ thích hợp.

Lấy ví dụ về con người nguyên thủy, khi chúng ta học cấu trúc dữ liệu, giống như con người nguyên thủy sở hữu công cụ
như dao đá, rìu đá. Và tùy vào kỹ thuật chế tạo công cụ khác nhau, dao đá lại chia thành loại dao sắc nhọn và dao răng
cưa, loại trước thích hợp để săn bắn, loại sau thích hợp để cắt gọt; giống như cấu trúc dữ liệu "đồ thị", tùy vào cách
thực hiện khác nhau (danh sách liên kết, mảng), có thể biểu diễn thành danh sách kề và ma trận kề, cái trước thích hợp
xử lý đồ thị thưa, cái sau thích hợp xử lý đồ thị dày.

Người nguyên thủy muốn xây nhà, cần phải lập kế hoạch, dùng rìu đá để chặt cây, dao đá để mài góc,... cũng giống như khi
chúng ta thiết kế thuật toán, phải tận dụng đặc tính của cấu trúc dữ liệu để giải quyết vấn đề thực tế.

**Ví dụ:**

- **Thuật toán tìm kiếm tuyến tính**: Sử dụng mảng để lưu trữ danh sách các phần tử cần tìm kiếm.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [1, 2, 3, 4, 5]
target = 3
index = linear_search(arr, target)
if index != -1:
    print(f"Target {target} found at index {index}")
else:
    print(f"Target {target} not found")
```

- **Thuật toán sắp xếp bọt**: Sử dụng mảng để lưu trữ danh sách các phần tử cần sắp xếp.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
```

### 4. Tóm tắt (quan trọng)

Đối với người mới học thuật toán, điều quan trọng là phải học cách xem xét vấn đề từ góc độ khung, thay vì bận tâm đến
các chi tiết.

Vấn đề chi tiết là gì? Ví dụ như i nên tăng đến n hay n - 1? Kích thước của mảng nên mở rộng n hay n + 1?

Xem xét vấn đề từ góc độ khung là gì? Ví dụ như vấn đề tìm kiếm tiền xu trong lập trình động được đề cập trong phần
trước, nếu bạn chỉ cần nhìn thoáng qua đoạn mã, tự động loại trừ các vấn đề chi tiết, trực tiếp trích xuất khung duyệt
cây N nhánh, thì tư duy khung của bạn đã 到位了 (đạt được).

**Tổng kết:**

Cấu trúc dữ liệu và thuật toán là hai khái niệm không thể tách rời. Cấu trúc dữ liệu cung cấp công cụ, thuật toán sử
dụng công cụ đó để giải quyết vấn đề. Hiểu rõ về cấu trúc dữ liệu và thuật toán giúp chúng ta viết code hiệu quả, giải
quyết các vấn đề một cách logic và dễ dàng.

**Lời khuyên:**

- Hãy tập trung vào việc hiểu rõ các khái niệm cơ bản của cấu trúc dữ liệu và thuật toán.
- Tập trung vào việc học cách giải quyết các vấn đề, thay vì nhớ các đoạn code cụ thể.
- Thực hành nhiều ví dụ để củng cố kiến thức và nâng cao kỹ năng lập trình.
