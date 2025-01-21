## **🚀 "GIẢI MÃ" CẤU TRÚC DỮ LIỆU ĐỒ THỊ (GRAPH): "BẢN ĐỒ" KẾT NỐI CHO DÂN CODE 🚀**

Yo các bạn sinh viên IT! Hôm nay chúng ta sẽ cùng nhau "khám phá" một cấu trúc dữ liệu rất quan trọng và thú vị: Đồ
thị (Graph). Đây là một "công cụ" mạnh mẽ giúp bạn biểu diễn các mối quan hệ giữa các đối tượng. Cùng mình "mổ xẻ" nó
nhé!

### **I. ĐỒ THỊ (GRAPH) LÀ GÌ?**

- **Đồ thị (Graph):** Là cấu trúc dữ liệu phi tuyến tính, dùng để biểu diễn mối quan hệ giữa các đối tượng.
- **Nó hoạt động như thế nào?**
    - Giống như bản đồ giao thông: có các "thành phố" (đỉnh), và các "con đường" (cạnh) nối các thành phố đó.
- **Đặc điểm:**
    - **Đỉnh (Node/Vertex):** Các đối tượng trong đồ thị.
    - **Cạnh (Edge):** Liên kết giữa các đỉnh.
        - **Có hướng (Directed):** Cạnh có hướng (ví dụ: A -> B).
        - **Vô hướng (Undirected):** Cạnh không có hướng (ví dụ: A <-> B).
        - **Có trọng số (Weighted):** Cạnh có giá trị (ví dụ: khoảng cách, chi phí).

### **II. CÁC LOẠI ĐỒ THỊ (MỖI LOẠI MỘT VẺ)**

1. **Đồ thị có hướng (Directed Graph):** Các cạnh có hướng rõ ràng.
    - **Ví dụ:** Quan hệ "theo dõi" trên mạng xã hội (A follow B).
2. **Đồ thị vô hướng (Undirected Graph):** Các cạnh không có hướng.
    - **Ví dụ:** Quan hệ "bạn bè" trên mạng xã hội (A is friend with B).
3. **Đồ thị có trọng số (Weighted Graph):** Các cạnh có trọng số.
    - **Ví dụ:** Bản đồ đường đi có khoảng cách giữa các thành phố.

### **III. BIỂU DIỄN ĐỒ THỊ (CÁCH "VẼ" ĐỒ THỊ)**

1. **Danh sách kề (Adjacency List):**
    - Dùng danh sách để lưu các đỉnh kề của từng đỉnh.
    - **Ví dụ:**

```
A: [B, C]
B: [D, E]
C: [F]
D: []
E: [F]
F: []
```

2. **Ma trận kề (Adjacency Matrix):**
    - Dùng ma trận 2 chiều để biểu diễn cạnh.
    - **Ví dụ:**

```
      A B C D E F
  A   0 1 1 0 0 0
  B   1 0 0 1 1 0
  C   1 0 0 0 0 1
  D   0 1 0 0 0 0
  E   0 1 0 0 0 1
  F   0 0 1 0 1 0
```

### **IV. CÀI ĐẶT ĐỒ THỊ (C#)**

```csharp
using System;
using System.Collections.Generic;

public class Graph
{
    private int numVertices;
    private Dictionary<int, List<int>> adjacencyList;

    public Graph(int numVertices)
    {
        this.numVertices = numVertices;
        adjacencyList = new Dictionary<int, List<int>>();
        for (int i = 0; i < numVertices; i++)
        {
            adjacencyList[i] = new List<int>();
        }
    }

    public void AddEdge(int u, int v)
    {
        adjacencyList[u].Add(v);
       // adjacencyList[v].Add(u); // Cho đồ thị vô hướng, nếu cần
    }

      public void PrintGraph()
          {
             foreach (var item in adjacencyList)
             {
                  Console.WriteLine(item.Key + " -> " + string.Join(", ", item.Value));
             }
        }

    public static void Main(string[] args)
    {
        Graph graph = new Graph(6);
        graph.AddEdge(0, 1);
        graph.AddEdge(0, 2);
        graph.AddEdge(1, 3);
        graph.AddEdge(1, 4);
        graph.AddEdge(2, 5);
        graph.AddEdge(4, 5);

        graph.PrintGraph();
         // Output:
         //0 -> 1, 2
         //1 -> 3, 4
         //2 -> 5
         //3 ->
         //4 -> 5
         //5 ->
    }
}
```

**Giải thích:**

- **`Graph`:** Lớp biểu diễn đồ thị.
    - `numVertices`: Số lượng đỉnh.
    - `adjacencyList`: Dùng `Dictionary<int, List<int>>` để lưu danh sách kề.
    - `AddEdge(int u, int v)`: Thêm cạnh từ đỉnh `u` đến đỉnh `v`.
    - `PrintGraph()`: In ra đồ thị.

### **V. CÁC THUẬT TOÁN TRÊN ĐỒ THỊ (NHỮNG THUẬT TOÁN HAY DÙNG)**

1. **Duyệt đồ thị:**
    - **BFS (Breadth-First Search):** Duyệt theo chiều rộng.
    - **DFS (Depth-First Search):** Duyệt theo chiều sâu.
2. **Tìm đường đi:**
    - **Dijkstra, Bellman-Ford:** Tìm đường đi ngắn nhất.
    - **Euler, Hamilton:** Tìm đường đi qua tất cả cạnh/đỉnh.
3. **Tìm chu trình:**
    - **Chu trình Euler, Hamilton**.
4. **Tìm cây khung:**
    - **Kruskal, Prim:** Tìm cây khung nhỏ nhất.
5. **Tô màu đồ thị:** Tìm cách tô màu các đỉnh sao cho các đỉnh kề nhau không cùng màu.

### **VI. ỨNG DỤNG CỦA ĐỒ THỊ (ĐƯỢC DÙNG Ở ĐÂU?)**

- **Mạng xã hội:** Biểu diễn mối quan hệ giữa người dùng.
- **Dẫn đường:** Tìm đường đi ngắn nhất (Google Maps).
- **Mạng máy tính:** Phân bổ tài nguyên.
- **Khoa học máy tính:** Phân tích dữ liệu, xử lý ngôn ngữ tự nhiên,...

### **VII. KẾT LUẬN (TỔNG KẾT)**

Đồ thị là một cấu trúc dữ liệu rất mạnh và linh hoạt, giúp bạn biểu diễn các mối quan hệ phức tạp giữa các đối tượng. Hy
vọng qua bài viết này, các bạn đã hiểu rõ hơn về nó và có thể áp dụng vào nhiều bài toán thực tế. Chúc các bạn code
thành công! 😎
