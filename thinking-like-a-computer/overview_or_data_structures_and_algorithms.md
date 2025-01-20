## **🚀 "GIẢI MÃ" CẤU TRÚC DỮ LIỆU VÀ THUẬT TOÁN: BẢN ĐỒ CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" hai chủ đề cực kỳ quan trọng và là nền tảng của mọi
chương trình: Cấu trúc dữ liệu và Thuật toán. Đây như là "bản đồ" giúp chúng ta đi đúng hướng trong thế giới lập trình.
Mình sẽ cố gắng giải thích dễ hiểu nhất có thể, kèm theo ví dụ thực tế để các bạn dễ hình dung nhé! Let's go!

### **I. TẠI SAO CẦN HỌC CẤU TRÚC DỮ LIỆU VÀ THUẬT TOÁN?**

* **Cấu trúc dữ liệu:** Là cách tổ chức dữ liệu sao cho dễ lưu trữ, truy cập và thao tác.
* **Thuật toán:** Là cách giải quyết một bài toán một cách hiệu quả.
* **Quan trọng vì:**
    * **Tổ chức dữ liệu tốt:** Giúp code chạy nhanh hơn, dễ quản lý hơn.
    * **Giải quyết bài toán nhanh:** Chọn thuật toán phù hợp giúp code tối ưu hơn.
    * **Tư duy logic:** Giúp bạn rèn luyện tư duy logic, phân tích vấn đề.
    * **Nền tảng vững chắc:** Giúp bạn hiểu rõ hơn về cách hoạt động của phần mềm.

### **II. CẤU TRÚC DỮ LIỆU: TỪ CƠ BẢN ĐẾN NÂNG CAO**

#### **2.1. HAI CẤU TRÚC CƠ BẢN: MẢNG VÀ DANH SÁCH LIÊN KẾT**

* **Mảng (Array):**
    * Là tập hợp các phần tử cùng kiểu dữ liệu, lưu liên tiếp trong bộ nhớ.
    * Giống như dãy số nhà trên đường, mỗi nhà có số thứ tự (index).
    * **Ưu:** Truy cập nhanh bằng index.
    * **Nhược:** Thêm/xóa khó, kích thước cố định.
* **Danh sách liên kết (Linked List):**
    * Là chuỗi các "nút", mỗi nút chứa dữ liệu và "con trỏ" đến nút tiếp theo.
    * Giống như đoàn tàu, mỗi toa nối với toa tiếp theo.
    * **Ưu:** Thêm/xóa dễ, kích thước động.
    * **Nhược:** Truy cập chậm (phải đi theo con trỏ).

#### **2.2. TƯ DUY ĐỆ QUY: TỪ TRỪU TƯỢNG ĐẾN CỤ THỂ**

* **Tư duy đệ quy:** Đi từ tổng quát đến chi tiết, từ trừu tượng đến cụ thể.
    * Mảng và danh sách liên kết là "gốc rễ".
    * Các cấu trúc khác là "kiến trúc nâng cao" xây dựng từ "gốc rễ" này.

#### **2.3. CÁC CẤU TRÚC DỮ LIỆU NÂNG CAO (ĐƯỢC XÂY TỪ CƠ BẢN)**

1. **Ngăn xếp (Stack) và Hàng đợi (Queue):**
    * **Stack:** LIFO (Last In First Out) - như chồng đĩa (đĩa nào bỏ vào sau cùng thì lấy ra đầu tiên).
        * Dùng mảng (thêm/xóa ở cuối) hoặc linked list (thêm/xóa ở đầu).
    * **Queue:** FIFO (First In First Out) - như hàng đợi (ai đến trước thì được phục vụ trước).
        * Dùng mảng (thêm cuối, xóa đầu) hoặc linked list (thêm cuối, xóa đầu).

   ```csharp
   // Stack dùng linked list
   public class Node
   {
       public int Data;
       public Node Next;
       public Node(int data)
       {
           Data = data;
           Next = null;
       }
   }
   public class Stack
   {
       private Node top;
       public Stack()
       {
           top = null;
       }
       public void Push(int data)
       {
           Node newNode = new Node(data);
           newNode.Next = top;
           top = newNode;
       }
       public int? Pop()
       {
           if (top == null)
               return null;
           int data = top.Data;
           top = top.Next;
           return data;
       }
   }

       // Queue dùng mảng
   using System;
   using System.Collections.Generic;

   public class Queue
   {
       private List<int> queue;

       public Queue()
       {
           queue = new List<int>();
       }

       public void Enqueue(int data)
       {
           queue.Add(data);
       }

       public int? Dequeue()
       {
           if (queue.Count == 0)
               return null;
           int data = queue[0];
           queue.RemoveAt(0);
           return data;
       }
   }
   ```
2. **Đồ thị (Graph):**
    * Tập hợp các "nút" và "cạnh" nối các nút.
    * Biểu diễn bằng danh sách kề (adjacency list) hoặc ma trận kề (adjacency matrix).

```csharp
        // Graph dùng danh sách kề
   using System;
   using System.Collections.Generic;

    public class Graph
    {
        private int numVertices;
        private List<int>[] adjList;

        public Graph(int numVertices)
        {
            this.numVertices = numVertices;
            adjList = new List<int>[numVertices];
            for (int i = 0; i < numVertices; i++)
            {
                adjList[i] = new List<int>();
            }
        }

        public void AddEdge(int u, int v)
        {
            adjList[u].Add(v);
            adjList[v].Add(u); // Cho đồ thị vô hướng
        }
    }

    // Graph dùng ma trận kề
     public class Graph
    {
        private int numVertices;
        private int[,] adjMatrix;

        public Graph(int numVertices)
        {
            this.numVertices = numVertices;
            adjMatrix = new int[numVertices, numVertices];
        }

        public void AddEdge(int u, int v)
        {
            adjMatrix[u, v] = 1;
            adjMatrix[v, u] = 1; // Cho đồ thị vô hướng
        }
    }
```

3. **Bảng băm (Hash Table):**
    * Dùng "hàm băm" để ánh xạ "khóa" vào mảng, giúp tìm kiếm nhanh.
    * Giải quyết "xung đột" bằng chuỗi liên kết hoặc thăm dò tuyến tính.

   ```csharp
     // Hash Table sử dụng chuỗi liên kết
        public class Node
        {
            public string Key;
            public int Value;
            public Node Next;

            public Node(string key, int value)
            {
                Key = key;
                Value = value;
                Next = null;
            }
        }

        public class HashTable
        {
            private Node[] table;

            public HashTable(int size)
            {
                table = new Node[size];
            }

            private int Hash(string key)
            {
                return key.GetHashCode() % table.Length;
            }

            public void Insert(string key, int value)
            {
                int index = Hash(key);
                Node newNode = new Node(key, value);
                newNode.Next = table[index];
                table[index] = newNode;
            }

            public int? Get(string key)
            {
                int index = Hash(key);
                Node current = table[index];
                while (current != null)
                {
                    if (current.Key == key)
                        return current.Value;
                    current = current.Next;
                }
                return null;
            }
        }
   ```

4. **Cây (Tree):**
    * Cấu trúc dữ liệu phân cấp (như cây gia phả).
    * Có cây nhị phân, cây tìm kiếm nhị phân, cây AVL, cây B,...

### **III. CÁC THAO TÁC CƠ BẢN (LÀM GÌ VỚI DỮ LIỆU?)**

1. **Duyệt (Traverse):** Đi qua tất cả phần tử.
2. **Truy cập (Access):** Lấy hoặc thay đổi giá trị phần tử.
3. **Thêm (Insert):** Thêm phần tử mới.
4. **Xóa (Delete):** Xóa phần tử.
5. **Tìm kiếm (Search):** Tìm phần tử.
6. **Sửa đổi (Update):** Thay đổi giá trị.

### **IV. PHÂN LOẠI DUYỆT VÀ TRUY CẬP: TUYẾN TÍNH VÀ PHI TUYẾN TÍNH**

* **Tuyến tính (Linear):** Duyệt theo thứ tự (như mảng).
* **Phi tuyến tính (Non-linear):** Không theo thứ tự cố định (như cây, đồ thị).

  ```csharp
      // Duyệt mảng (tuyến tính)
      using System;

      class Program
      {
          static void Main()
          {
              int[] arr = { 1, 2, 3, 4, 5 };
              foreach (int item in arr)
              {
                  Console.WriteLine(item);
              }
          }
      }
      // Duyệt cây nhị phân (phi tuyến tính)
         using System;
       public class Node
          {
              public int Data;
              public Node Left;
              public Node Right;

              public Node(int data)
              {
                  Data = data;
                  Left = null;
                  Right = null;
              }
          }
  class Program
      {
          static void PreorderTraversal(Node root)
          {
              if (root == null)
                  return;
              Console.Write(root.Data + " ");
              PreorderTraversal(root.Left);
              PreorderTraversal(root.Right);
          }

          static void Main()
          {
              Node root = new Node(1);
              root.Left = new Node(2);
              root.Right = new Node(3);
              root.Left.Left = new Node(4);
              root.Left.Right = new Node(5);

              PreorderTraversal(root);  // Output: 1 2 4 5 3
          }
      }
  ```

### **V. MỐI LIÊN HỆ GIỮA CẤU TRÚC DỮ LIỆU VÀ THUẬT TOÁN (NHƯNG CẶP ĐÔI HOÀN HẢO)**

* **Cấu trúc dữ liệu:** Là "công cụ" để lưu trữ dữ liệu.
* **Thuật toán:** Là "cách dùng" các công cụ đó để giải bài toán.

#### **5.1. VÍ DỤ (ĐỂ THẤY RÕ HƠN)**

1. **Tìm kiếm tuyến tính (Linear Search):** Dùng mảng để lưu danh sách và tìm từng phần tử.

```csharp
        using System;

        public class Program
        {
            public static int LinearSearch(int[] arr, int target)
            {
                for (int i = 0; i < arr.Length; i++)
                {
                    if (arr[i] == target)
                        return i;
                }
                return -1;
            }

            public static void Main()
            {
                int[] arr = { 1, 2, 3, 4, 5 };
                int target = 3;
                int index = LinearSearch(arr, target);
                if (index != -1)
                    Console.WriteLine($"Target {target} found at index {index}");
                else
                    Console.WriteLine($"Target {target} not found");
            }
        }
```

2. **Sắp xếp nổi bọt (Bubble Sort):** Dùng mảng để lưu danh sách và sắp xếp bằng cách so sánh và đổi chỗ các cặp phần
   tử.

```csharp
    using System;

    public class Program
    {
        public static void BubbleSort(int[] arr)
        {
            int n = arr.Length;
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (arr[j] > arr[j + 1])
                    {
                        // Swap
                        int temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                    }
                }
            }
        }

        public static void Main()
        {
            int[] arr = { 64, 34, 25, 12, 22, 11, 90 };
            BubbleSort(arr);
            Console.WriteLine("Sorted array: " + string.Join(", ", arr));
        }
    }
```

### **VI. TÓM TẮT (NHỮNG GÌ CẦN GHI NHỚ)**

1. **Tư duy theo "khung":** Nhìn vấn đề tổng quát trước, rồi đến chi tiết.
2. **Cấu trúc dữ liệu & thuật toán:** Cấu trúc dữ liệu là "công cụ", thuật toán là "cách dùng".

### **VII. LỜI KHUYÊN (ĐỂ HỌC TỐT HƠN)**

1. **Tập trung vào cơ bản:** Nắm chắc mảng, danh sách liên kết, sau đó đến các cấu trúc phức tạp hơn.
2. **Học cách giải quyết:** Đừng chỉ nhớ code, hãy hiểu cách thuật toán hoạt động.
3. **Thực hành thường xuyên:** Giải bài tập để củng cố kiến thức.

### **VIII. KẾT LUẬN**

Cấu trúc dữ liệu và thuật toán là nền tảng quan trọng trong lập trình. Việc nắm vững chúng sẽ giúp bạn trở thành một lập
trình viên giỏi và tự tin hơn khi đối mặt với các bài toán phức tạp. Chúc các bạn học tốt! 😎
