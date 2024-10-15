## Cấu trúc dữ liệu cây (Tree) trong Python

Cây là một cấu trúc dữ liệu phi tuyến tính, được tổ chức theo dạng phân cấp. Nó gồm các nút (node) được liên kết với nhau theo một trật tự nhất định. Mỗi nút chứa dữ liệu và có thể có các nút con, ngoại trừ nút gốc (root) không có nút cha.

**1. Khái niệm cơ bản:**

- **Nút (Node):** Mỗi phần tử trong cây, chứa dữ liệu và các liên kết đến các nút con.
- **Nút gốc (Root):** Nút đầu tiên và duy nhất không có nút cha.
- **Nút con (Child):** Nút được nối với một nút cha.
- **Nút cha (Parent):** Nút có liên kết đến một hoặc nhiều nút con.
- **Nút lá (Leaf):** Nút không có nút con.
- **Độ cao (Height):** Số cạnh từ nút gốc đến nút lá xa nhất.
- **Độ sâu (Depth):** Số cạnh từ nút gốc đến một nút bất kỳ.

**2. Triển khai cây trong Python:**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

- **Node:** Là lớp đại diện cho một nút trong cây.
- **data:** Dữ liệu được lưu trữ trong nút.
- **left:** Liên kết đến nút con bên trái.
- **right:** Liên kết đến nút con bên phải.

**3. Duyệt cây (Tree Traversal):**

- **Duyệt theo thứ tự trước (Preorder):** Duyệt nút gốc, sau đó duyệt con trái, sau đó duyệt con phải.

  ```python
  def preorder(node):
      if node:
          print(node.data, end=" ")
          preorder(node.left)
          preorder(node.right)
  ```

- **Duyệt theo thứ tự giữa (Inorder):** Duyệt con trái, sau đó duyệt nút gốc, sau đó duyệt con phải.

  ```python
  def inorder(node):
      if node:
          inorder(node.left)
          print(node.data, end=" ")
          inorder(node.right)
  ```

- **Duyệt theo thứ tự sau (Postorder):** Duyệt con trái, sau đó duyệt con phải, sau đó duyệt nút gốc.
  ```python
  def postorder(node):
      if node:
          postorder(node.left)
          postorder(node.right)
          print(node.data, end=" ")
  ```

**4. Ví dụ:**

Tạo một cây nhị phân đơn giản:

```python
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
```

Duyệt cây theo thứ tự trước:

```python
preorder(root)  # Output: 1 2 4 5 3
```

**5. Các loại cây:**

- **Cây nhị phân (Binary Tree):** Mỗi nút có tối đa hai nút con.
- **Cây tìm kiếm nhị phân (Binary Search Tree):** Cây nhị phân thỏa mãn điều kiện:
  - Giá trị của nút con trái nhỏ hơn giá trị của nút cha.
  - Giá trị của nút con phải lớn hơn giá trị của nút cha.
- **Cây AVL:** Cây tìm kiếm nhị phân cân bằng tự động, đảm bảo độ cao của hai nhánh con của mỗi nút chênh lệch tối đa là 1.
- **Cây Red-Black:** Cây tìm kiếm nhị phân cân bằng tự động khác, sử dụng màu sắc (đỏ hoặc đen) để quản lý độ cao của các nút.

**6. Ứng dụng của cây:**

- **Lưu trữ dữ liệu:** Cây tìm kiếm nhị phân được sử dụng để lưu trữ dữ liệu hiệu quả, cho phép tìm kiếm, chèn, xóa nhanh chóng.
- **Tìm kiếm:** Cây tìm kiếm nhị phân, cây AVL, cây Red-Black được sử dụng cho các thuật toán tìm kiếm hiệu quả.
- **Tổ chức dữ liệu:** Cây được sử dụng để tổ chức dữ liệu theo dạng phân cấp, ví dụ: hệ thống tệp, biểu diễn ngữ pháp.
- **Thuật toán:** Cây được sử dụng trong các thuật toán như:
  - Dijkstra, Bellman-Ford (tìm đường đi ngắn nhất).
  - Kruskal, Prim (tìm cây khung).

**Kết luận:**

Cây là một cấu trúc dữ liệu mạnh mẽ và linh hoạt, được sử dụng rộng rãi trong nhiều lĩnh vực của khoa học máy tính. Hiểu rõ các khái niệm và cách triển khai cây giúp bạn giải quyết hiệu quả các bài toán liên quan đến dữ liệu có cấu trúc phân cấp.
