## **🚀 "GIẢI MÃ" CẤU TRÚC DỮ LIỆU CÂY (TREE): "BẢN ĐỒ" PHÂN CẤP CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một cấu trúc dữ liệu rất quan trọng và "làm màu":
Cây (Tree). Nghe có vẻ "lâm ly" nhưng thực ra rất gần gũi và dễ hiểu nếu chúng ta "mổ xẻ" nó ra. Cùng mình khám phá nhé!

### **I. CÂY (TREE) LÀ GÌ?**

- **Cây (Tree):** Là cấu trúc dữ liệu phi tuyến tính, có dạng phân cấp (như kiểu cây phả hệ).
- **Nó hoạt động như thế nào?**
    - Giống như một cái cây: có gốc, có cành, có lá,...
- **Đặc điểm:**
    - **Nút (Node):** Mỗi phần tử trong cây.
    - **Nút gốc (Root):** Nút đầu tiên, không có nút cha.
    - **Nút con (Child):** Các nút được liên kết với nút cha.
    - **Nút cha (Parent):** Nút có liên kết đến nút con.
    - **Nút lá (Leaf):** Nút không có nút con.
    - **Độ cao (Height):** Số cạnh từ nút gốc đến nút lá xa nhất.
    - **Độ sâu (Depth):** Số cạnh từ nút gốc đến một nút bất kỳ.

### **II. CÀI ĐẶT CÂY NHỊ PHÂN (C#)**

```csharp
using System;

public class Node
{
    public int Data { get; set; }
    public Node Left { get; set; }
    public Node Right { get; set; }

    public Node(int data)
    {
        Data = data;
        Left = null;
        Right = null;
    }
}
```

**Giải thích:**

- **`Node`:** Lớp biểu diễn một nút trong cây.
    - `Data`: Dữ liệu của nút.
    - `Left`: Con trỏ đến nút con bên trái.
    - `Right`: Con trỏ đến nút con bên phải.

### **III. DUYỆT CÂY (ĐI THĂM TỪNG "NGÓC NGÁCH")**

1. **Duyệt trước (Preorder):** Gốc -> Trái -> Phải.

```csharp
    public static void PreorderTraversal(Node node)
        {
            if (node != null)
            {
                Console.Write(node.Data + " ");
                PreorderTraversal(node.Left);
                PreorderTraversal(node.Right);
            }
        }
```

2. **Duyệt giữa (Inorder):** Trái -> Gốc -> Phải.

```csharp
        public static void InorderTraversal(Node node)
        {
            if (node != null)
            {
                InorderTraversal(node.Left);
                Console.Write(node.Data + " ");
                InorderTraversal(node.Right);
            }
        }
```

3. **Duyệt sau (Postorder):** Trái -> Phải -> Gốc.

```csharp
        public static void PostorderTraversal(Node node)
        {
            if (node != null)
            {
               PostorderTraversal(node.Left);
               PostorderTraversal(node.Right);
               Console.Write(node.Data + " ");
            }
        }
```

### **IV. VÍ DỤ MINH HỌA (C#)**

```csharp
 public class Example
    {
       public static void Main(string[] args)
          {
            Node root = new Node(1);
            root.Left = new Node(2);
            root.Right = new Node(3);
            root.Left.Left = new Node(4);
            root.Left.Right = new Node(5);

            Console.Write("Duyệt trước (Preorder): ");
            PreorderTraversal(root);  // Output: Duyệt trước (Preorder): 1 2 4 5 3
            Console.WriteLine();
           Console.Write("Duyệt giữa (Inorder): ");
             InorderTraversal(root); // Output: Duyệt giữa (Inorder): 4 2 5 1 3
           Console.WriteLine();
           Console.Write("Duyệt sau (Postorder): ");
            PostorderTraversal(root); // Output: Duyệt sau (Postorder): 4 5 2 3 1
            Console.WriteLine();
          }
     }
```

### **V. CÁC LOẠI CÂY PHỔ BIẾN (NHIỀU LOẠI "CÂY" KHÁC NHAU)**

1. **Cây nhị phân (Binary Tree):** Mỗi nút có tối đa 2 nút con.
2. **Cây tìm kiếm nhị phân (Binary Search Tree):** Cây nhị phân mà nút con trái < nút cha < nút con phải.
3. **Cây AVL:** Cây tìm kiếm nhị phân tự cân bằng.
4. **Cây Red-Black:** Cây tìm kiếm nhị phân tự cân bằng, dùng màu (đỏ, đen).

### **VI. ỨNG DỤNG CỦA CÂY (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Lưu trữ dữ liệu:** Cây tìm kiếm nhị phân (BST) dùng để lưu dữ liệu, cho phép tìm kiếm nhanh.
- **Tìm kiếm:** Cây BST, AVL, Red-Black dùng trong thuật toán tìm kiếm hiệu quả.
- **Tổ chức dữ liệu:** Phân cấp dữ liệu (hệ thống tệp, cấu trúc XML, ...).
- **Thuật toán:** Dùng trong nhiều thuật toán: Dijkstra, Bellman-Ford, Kruskal, Prim, ...

### **VII. KẾT LUẬN (TỔNG KẾT)**

Cây là một cấu trúc dữ liệu rất mạnh và linh hoạt, dùng để biểu diễn dữ liệu phân cấp một cách hiệu quả. Hy vọng qua bài
viết này, các bạn đã hiểu rõ hơn về nó. Chúc các bạn code thành công! 😎
