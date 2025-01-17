# Cấu Trúc Dữ Liệu Cây (Tree) trong TypeScript

## Mục lục

1. [Khái niệm cơ bản](#khái-niệm-cơ-bản)
2. [Triển khai cây trong TypeScript](#triển-khai-cây-trong-typescript)
3. [Duyệt cây (Tree Traversal)](#duyệt-cây-tree-traversal)
4. [Ví dụ](#ví-dụ)
5. [Các loại cây](#các-loại-cây)
6. [Ứng dụng của cây](#ứng-dụng-của-cây)
7. [Kết luận](#kết-luận)

---

## Khái niệm cơ bản

- **Nút (Node):** Mỗi phần tử trong cây, chứa dữ liệu và các liên kết đến các nút con.
- **Nút gốc (Root):** Nút đầu tiên và duy nhất không có nút cha.
- **Nút con (Child):** Nút được nối với một nút cha.
- **Nút cha (Parent):** Nút có liên kết đến một hoặc nhiều nút con.
- **Nút lá (Leaf):** Nút không có nút con.
- **Độ cao (Height):** Số cạnh từ nút gốc đến nút lá xa nhất.
- **Độ sâu (Depth):** Số cạnh từ nút gốc đến một nút bất kỳ.

## Triển khai cây trong TypeScript

Trong TypeScript, bạn có thể triển khai cây nhị phân đơn giản với một lớp `Node` đại diện cho các nút trong cây.

```typescript
class Node {
  data: number;
  left: Node | null;
  right: Node | null;

  constructor(data: number) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}
```

- **Node:** Là lớp đại diện cho một nút trong cây.
- **data:** Dữ liệu được lưu trữ trong nút.
- **left:** Liên kết đến nút con bên trái.
- **right:** Liên kết đến nút con bên phải.

## Duyệt cây (Tree Traversal)

### 1. Duyệt theo thứ tự trước (Preorder)

Duyệt nút gốc trước, sau đó duyệt con trái và cuối cùng duyệt con phải.

```typescript
function preorder(node: Node | null): void {
  if (node) {
    console.log(node.data, ' ');
    preorder(node.left);
    preorder(node.right);
  }
}
```

### 2. Duyệt theo thứ tự giữa (Inorder)

Duyệt con trái, sau đó duyệt nút gốc và cuối cùng duyệt con phải.

```typescript
function inorder(node: Node | null): void {
  if (node) {
    inorder(node.left);
    console.log(node.data, ' ');
    inorder(node.right);
  }
}
```

### 3. Duyệt theo thứ tự sau (Postorder)

Duyệt con trái, sau đó duyệt con phải và cuối cùng duyệt nút gốc.

```typescript
function postorder(node: Node | null): void {
  if (node) {
    postorder(node.left);
    postorder(node.right);
    console.log(node.data, ' ');
  }
}
```

## Ví dụ

Tạo một cây nhị phân đơn giản và duyệt theo thứ tự trước:

```typescript
const root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);
root.left.right = new Node(5);

// Duyệt cây theo thứ tự trước
preorder(root); // Output: 1 2 4 5 3
```

## Các loại cây

1. **Cây nhị phân (Binary Tree):** Mỗi nút có tối đa hai nút con.
2. **Cây tìm kiếm nhị phân (Binary Search Tree):** Cây nhị phân thỏa mãn điều kiện:
    - Giá trị của nút con trái nhỏ hơn giá trị của nút cha.
    - Giá trị của nút con phải lớn hơn giá trị của nút cha.
3. **Cây AVL:** Cây tìm kiếm nhị phân tự cân bằng, đảm bảo độ cao của hai nhánh con của mỗi nút chênh lệch tối đa là 1.
4. **Cây Red-Black:** Cây tìm kiếm nhị phân tự cân bằng, sử dụng màu sắc (đỏ hoặc đen) để quản lý độ cao của các nút.

## Ứng dụng của cây

- **Lưu trữ dữ liệu:** Cây tìm kiếm nhị phân được sử dụng để lưu trữ dữ liệu hiệu quả, cho phép tìm kiếm, chèn, xóa
  nhanh chóng.
- **Tìm kiếm:** Cây tìm kiếm nhị phân, cây AVL, cây Red-Black được sử dụng trong các thuật toán tìm kiếm hiệu quả.
- **Tổ chức dữ liệu:** Cây được sử dụng để tổ chức dữ liệu theo dạng phân cấp, ví dụ: hệ thống tệp, biểu diễn ngữ pháp.
- **Thuật toán:** Cây được sử dụng trong các thuật toán như:
    - Dijkstra, Bellman-Ford (tìm đường đi ngắn nhất).
    - Kruskal, Prim (tìm cây khung).

## Kết luận

Cây là một cấu trúc dữ liệu mạnh mẽ và linh hoạt, được sử dụng rộng rãi trong nhiều lĩnh vực của khoa học máy tính. Việc
hiểu rõ các khái niệm và cách triển khai cây giúp bạn giải quyết hiệu quả các bài toán liên quan đến dữ liệu có cấu trúc
phân cấp.
